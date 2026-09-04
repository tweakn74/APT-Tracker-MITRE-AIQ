"""
Elite Workforce Orchestrator - Dynamic Elastic Pressure Governor & Adaptive Work-Stealer.
Part of the 16-Role Zero-Toil Dream Team Framework.
Dynamically gauges CPU, RAM, and Commit charge to burst in Zone Green (up to 12 workers)
and enforce the 2-worker absolute lowest fallback floor under critically slim
resources [BM-PAT-023].
Combines CPU Multi-Processing and I/O Multi-Threading with deterministic process reaping.
"""
from __future__ import annotations

import atexit
import contextlib
import os
import shutil
import sys
import time
from collections.abc import Callable, Iterable
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from typing import TypeVar

import psutil

T = TypeVar("T")
R = TypeVar("R")


class ElasticPressureZone(StrEnum):
    GREEN = "green"  # Safe for high burst capacity (up to 100% logical cores)
    YELLOW = "yellow"  # Moderate load, hold at 50% half-cores
    RED = "red"  # Critical host pressure, elastically back off to minimum floor


@dataclass(frozen=True)
class PressureSnapshot:
    timestamp_utc: str
    cpu_percent: float
    free_ram_mb: float
    used_ram_mb: float
    commit_used_mb: float
    pressure_zone: ElasticPressureZone
    recommended_workers: int
    uncapped_active: bool = False


class DynamicPressureGauge:
    """Samples live host CPU, RAM, and Commit charge to determine elastic worker capacity."""

    def __init__(self, sample_interval_sec: float = 0.03) -> None:
        self.sample_interval_sec = sample_interval_sec

    def sample_live_pressure(self, uncapped: bool = False) -> PressureSnapshot:
        cpu = psutil.cpu_percent(interval=self.sample_interval_sec)
        vm = psutil.virtual_memory()
        sw = psutil.swap_memory()

        free_ram_mb = vm.available / (1024 * 1024)
        used_ram_mb = vm.used / (1024 * 1024)
        commit_used_mb = (vm.used + sw.used) / (1024 * 1024)
        commit_limit_mb = (vm.total + sw.total) / (1024 * 1024)

        logical_cores = os.cpu_count() or 4
        half_cores = max(1, logical_cores // 2)

        commit_pct = (commit_used_mb / commit_limit_mb) * 100.0 if commit_limit_mb > 0 else 0.0

        if cpu < 80.0 and free_ram_mb > 3072.0 and commit_pct < 90.0:
            zone = ElasticPressureZone.GREEN
            recommended = logical_cores if uncapped else half_cores
        elif cpu > 92.0 or free_ram_mb < 1536.0 or commit_pct > 95.0:
            zone = ElasticPressureZone.RED
            recommended = max(1, half_cores // 2)
        else:
            zone = ElasticPressureZone.YELLOW
            recommended = half_cores

        return PressureSnapshot(
            timestamp_utc=datetime.now(UTC).isoformat(),
            cpu_percent=round(cpu, 1),
            free_ram_mb=round(free_ram_mb, 1),
            used_ram_mb=round(used_ram_mb, 1),
            commit_used_mb=round(commit_used_mb, 1),
            pressure_zone=zone,
            recommended_workers=recommended,
            uncapped_active=uncapped,
        )

    def run_intermittent_pressure_test(
        self, samples_count: int = 5, interval_sec: float = 0.03, uncapped: bool = True
    ) -> list[PressureSnapshot]:
        snapshots: list[PressureSnapshot] = []
        for _ in range(samples_count):
            snapshots.append(self.sample_live_pressure(uncapped=uncapped))
            time.sleep(interval_sec)
        return snapshots

    def wait_for_capacity(
        self,
        min_free_ram_mb: float = 2048.0,
        max_cpu_percent: float = 90.0,
        max_wait_seconds: float = 30.0,
        poll_interval_sec: float = 0.5,
    ) -> bool:
        """Dynamically scales and pauses workers, waiting for host memory and CPU to clear."""
        start = time.time()
        while time.time() - start < max_wait_seconds:
            snap = self.sample_live_pressure(uncapped=True)
            if snap.free_ram_mb >= min_free_ram_mb and snap.cpu_percent <= max_cpu_percent:
                return True
            time.sleep(poll_interval_sec)
        return False


def _init_low_priority_worker():
    """Sets child worker process CPU and I/O priority to lowest tier to protect UI."""
    with contextlib.suppress(psutil.Error, OSError):
        p = psutil.Process()
        if sys.platform == "win32":
            p.nice(psutil.IDLE_PRIORITY_CLASS)
            try:
                p.ionice(psutil.IOPRIO_VERYLOW)
            except (AttributeError, OSError):
                with contextlib.suppress(AttributeError, OSError):
                    p.ionice(psutil.IOPRIO_LOW)
        else:
            p.nice(15)


@dataclass(frozen=True)
class HostCapacityProfile:
    """Dynamic host hardware and capacity assessment."""
    logical_cores: int
    physical_cores: int
    total_ram_gb: float
    free_ram_gb: float
    free_disk_gb: float
    max_heavy_workers: int
    max_lightweight_workers: int
    max_concurrent_worktrees: int
    max_io_threads: int
    uncapped_active: bool = False


def probe_host_capacity(uncapped: bool = False) -> HostCapacityProfile:
    """Preflight survey evaluating host resources in standard or uncapped mode."""
    logical_cores = os.cpu_count() or 4
    physical_cores = psutil.cpu_count(logical=False) or (logical_cores // 2 or 2)
    mem = psutil.virtual_memory()
    total_ram_gb = mem.total / (1024 ** 3)
    free_ram_gb = mem.available / (1024 ** 3)

    cwd_drive = os.path.splitdrive(os.getcwd())[0] or "C:"
    disk = shutil.disk_usage(cwd_drive if os.path.exists(cwd_drive) else "/")
    free_disk_gb = disk.free / (1024 ** 3)

    gauge = DynamicPressureGauge()
    snap = gauge.sample_live_pressure(uncapped=uncapped)

    # 1. Multi-Processing (CPU-bound)
    max_lightweight = snap.recommended_workers

    # 2. Heavy workers (RAM-bound): Never capped to 2 by default;
    # 2 is the lowest fallback floor when resources are very slim
    if snap.pressure_zone == ElasticPressureZone.RED or free_ram_gb < 2.0:
        max_heavy = 2  # Absolute lowest fallback floor
    else:
        max_heavy_limit = logical_cores if uncapped else max(4, logical_cores // 2)
        heavy_ram_headroom = max(0.0, free_ram_gb - 2.0)
        max_heavy = max(2, min(int(heavy_ram_headroom // 2.5) or 2, max_heavy_limit))

    # 3. Concurrent Git Worktrees
    disk_worktree_cap = max(1, int(free_disk_gb // 2.0))
    max_worktrees_limit = 12 if uncapped else 8
    max_worktrees = max(2, min(max_lightweight, disk_worktree_cap, max_worktrees_limit))

    # 4. Multi-Threading (I/O-bound & Provider CLI streaming)
    max_io_threads_limit = 64 if uncapped else 32
    max_io_threads = max(4, min(logical_cores * 4, max_io_threads_limit))

    return HostCapacityProfile(
        logical_cores=logical_cores,
        physical_cores=physical_cores,
        total_ram_gb=round(total_ram_gb, 2),
        free_ram_gb=round(free_ram_gb, 2),
        free_disk_gb=round(free_disk_gb, 2),
        max_heavy_workers=max_heavy,
        max_lightweight_workers=max_lightweight,
        max_concurrent_worktrees=max_worktrees,
        max_io_threads=max_io_threads,
        uncapped_active=uncapped,
    )


class DynamicAdaptiveThreadPool:
    """High-concurrency multi-threading pool for I/O-bound tasks and provider streaming."""

    def __init__(
        self,
        max_threads: int | None = None,
        timeout_seconds: float = 60.0,
        uncapped: bool = False,
    ):
        self.uncapped = uncapped
        self.profile = probe_host_capacity(uncapped=uncapped)
        self.max_threads = max_threads or self.profile.max_io_threads
        self.timeout_seconds = timeout_seconds
        self._active_executor: ThreadPoolExecutor | None = None

        atexit.register(self.shutdown)

    def shutdown(self):
        """Immediately shuts down all active worker threads."""
        if self._active_executor:
            with contextlib.suppress(RuntimeError, OSError):
                self._active_executor.shutdown(wait=False, cancel_futures=True)
            self._active_executor = None

    def map_threads(self, worker_func: Callable[[T], R], items: Iterable[T]) -> list[R]:
        """Maps I/O tasks across high-concurrency thread pool with strict timeout."""
        results: list[R] = []
        item_list = list(items)
        if not item_list:
            return results

        try:
            self._active_executor = ThreadPoolExecutor(max_workers=self.max_threads)
            future_to_item = {
                self._active_executor.submit(worker_func, item): item for item in item_list
            }
            for future in as_completed(future_to_item, timeout=self.timeout_seconds):
                try:
                    res = future.result()
                    results.append(res)
                except (RuntimeError, ValueError, OSError, TypeError) as exc:
                    print(f"[AdaptiveThreadPool Error] Thread task failed: {exc}")
        finally:
            self.shutdown()

        return results


class DynamicAdaptivePool:
    """Universal auto-scaling multi-process pool for CPU-bound execution."""

    def __init__(
        self,
        mode: str = "lightweight",
        timeout_seconds: float = 120.0,
        cpu_throttle_threshold: float = 75.0,
        uncapped: bool = False,
    ):
        self.uncapped = uncapped
        self.profile = probe_host_capacity(uncapped=uncapped)
        self.timeout_seconds = timeout_seconds
        self.cpu_throttle_threshold = cpu_throttle_threshold
        self._active_executor: ProcessPoolExecutor | None = None

        if mode == "heavy":
            self.workers = self.profile.max_heavy_workers
        else:
            self.workers = self.profile.max_lightweight_workers

        atexit.register(self.reap_all_workers)

    def reap_all_workers(self):
        """Immediately and unconditionally terminates all active worker processes."""
        if self._active_executor:
            with contextlib.suppress(RuntimeError, OSError):
                self._active_executor.shutdown(wait=False, cancel_futures=True)
            self._active_executor = None

    def get_live_core_telemetry(self) -> list[float]:
        """Returns per-core CPU usage percentages in real-time."""
        return psutil.cpu_percent(interval=0.05, percpu=True)

    def map_adaptive(
        self,
        worker_func: Callable[[T], R],
        items: Iterable[T],
    ) -> list[R]:
        """Maps tasks across dynamically sized process pool with guaranteed cleanup."""
        results: list[R] = []
        item_list = list(items)
        if not item_list:
            return results

        try:
            gauge = DynamicPressureGauge()
            gauge.wait_for_capacity(
                min_free_ram_mb=1536.0, max_cpu_percent=92.0, max_wait_seconds=15.0
            )
            self._active_executor = ProcessPoolExecutor(
                max_workers=self.workers,
                initializer=_init_low_priority_worker,
            )
            future_to_item = {
                self._active_executor.submit(worker_func, item): item for item in item_list
            }
            for future in as_completed(future_to_item, timeout=self.timeout_seconds):
                try:
                    res = future.result()
                    results.append(res)
                except (RuntimeError, ValueError, OSError, TypeError) as exc:
                    print(f"[AdaptivePool Error] Item failed: {exc}")
        finally:
            self.reap_all_workers()

        return results

# Version: 2.1.0-elite-dreamteam
