"""
Elite Workforce Orchestrator - Dynamic Graph Complexity Grader & Topology Allocator.
Part of the 16-Role Zero-Toil Dream Team Framework.
Grades task surface area, architectural depth, subsystem diversity, and risk to dynamically
calculate the optimal agent headcount, specialized roles, model assignments, and Git worktrees.
Supports Standard, Uncapped, External Providers, and Uncapped External Provider variations.
"""
from __future__ import annotations

import math
import os
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class HostCapacity:
    logical_cores: int
    physical_cores: int
    free_ram_gb: float
    total_ram_gb: float
    free_disk_gb: float


def probe_host() -> HostCapacity:
    logical = os.cpu_count() or 4
    physical = max(1, logical // 2)
    free_ram = 8.0
    total_ram = 16.0
    free_disk = 140.0

    try:
        import ctypes

        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
            free_ram = stat.ullAvailPhys / (1024**3)
            total_ram = stat.ullTotalPhys / (1024**3)
    except Exception:  # noqa: BLE001
        pass

    try:
        import shutil

        usage = shutil.disk_usage(Path.cwd())
        free_disk = usage.free / (1024**3)
    except Exception:  # noqa: BLE001
        pass

    return HostCapacity(
        logical_cores=logical,
        physical_cores=physical,
        free_ram_gb=round(free_ram, 2),
        total_ram_gb=round(total_ram, 2),
        free_disk_gb=round(free_disk, 2),
    )


@dataclass
class TaskGradingGrid:
    surface_area: int  # 1 to 10 (single file -> repo-wide)
    architectural_depth: int  # 1 to 10 (formatting -> deep speculative pipeline)
    subsystem_diversity: int  # 1 to 10 (backend only -> multi-tier full-stack)
    security_risk_level: int  # 1 to 10 (isolated script -> kernel/crypto/state)
    concurrency_leverage: str  # "IO_BOUND" | "CPU_BOUND" | "REASONING_BOUND"
    overall_complexity_score: float  # 1.0 to 10.0


def grade_task(prompt: str, touched_files: list[str] | None = None) -> TaskGradingGrid:
    prompt_lower = prompt.lower()

    # 1. Surface Area
    file_count = len(touched_files) if touched_files else 1
    if file_count >= 10 or "entire codebase" in prompt_lower or "all projects" in prompt_lower:
        surface = 10
    elif file_count >= 5 or "multi-file" in prompt_lower or "across" in prompt_lower:
        surface = 7
    elif file_count >= 2 or "refactor" in prompt_lower or "pipeline" in prompt_lower:
        surface = 5
    else:
        surface = 2

    # 2. Architectural Depth
    depth = 3
    deep_kw = ["speculative", "architecture", "distributed", "compiler", "engine", "titanfold"]
    medium_kw = ["pipeline", "state machine", "stategraph", "refactor", "framework"]
    if any(k in prompt_lower for k in deep_kw):
        depth = 9
    elif any(k in prompt_lower for k in medium_kw):
        depth = 7
    elif any(k in prompt_lower for k in ["feature", "implement", "add endpoint", "integration"]):
        depth = 5
    elif any(k in prompt_lower for k in ["fix", "typo", "lint", "format", "cleanup"]):
        depth = 2

    # 3. Subsystem Diversity
    diversity_points = 0
    if any(k in prompt_lower for k in ["ui", "frontend", "html", "css", "console", "table"]):
        diversity_points += 3
    if any(k in prompt_lower for k in ["backend", "api", "server", "service", "fastapi"]):
        diversity_points += 3
    if any(k in prompt_lower for k in ["database", "sqlite", "model", "schema", "store"]):
        diversity_points += 2
    if any(k in prompt_lower for k in ["test", "pytest", "vitest", "playwright", "fuzz"]):
        diversity_points += 2
    diversity = max(2, min(10, diversity_points or 3))

    # 4. Security & Risk Level
    risk = 2
    if any(k in prompt_lower for k in ["auth", "token", "password", "crypto", "merkle"]):
        risk = 8
    elif any(k in prompt_lower for k in ["interdiction", "suspend", "kill", "quarantine"]):
        risk = 9
    elif any(k in prompt_lower for k in ["delete", "purge", "clean", "drop", "truncate"]):
        risk = 6

    # 5. Concurrency Leverage
    if any(k in prompt_lower for k in ["scan", "disk", "ast", "find", "search", "checkout"]):
        concurrency = "IO_BOUND"
    elif any(k in prompt_lower for k in ["compile", "hash", "fuzz", "parse", "benchmark"]):
        concurrency = "CPU_BOUND"
    else:
        concurrency = "REASONING_BOUND"

    overall = round((surface * 0.25) + (depth * 0.35) + (diversity * 0.25) + (risk * 0.15), 2)

    return TaskGradingGrid(
        surface_area=surface,
        architectural_depth=depth,
        subsystem_diversity=diversity,
        security_risk_level=risk,
        concurrency_leverage=concurrency,
        overall_complexity_score=overall,
    )


@dataclass
class WorkforceTopology:
    complexity_score: float
    recommended_worktree_workers: int
    recommended_io_threads: int
    assigned_specialists: list[dict[str, str]]
    model_dispatch_plan: list[dict[str, str]]
    active_verification_loops: list[str]
    rationale: str


def compute_dynamic_topology(
    grid: TaskGradingGrid,
    host: HostCapacity,
    prompt: str,
) -> WorkforceTopology:
    prompt_lower = prompt.lower()
    is_uncapped = (
        ("uncapped" in prompt_lower)
        or ("--uncapped" in sys.argv)
        or ("-u" in sys.argv)
    )
    is_external = (
        ("external provider" in prompt_lower)
        or ("external-provider" in prompt_lower)
        or ("--external-providers" in sys.argv)
        or ("-e" in sys.argv)
    )

    if is_uncapped:
        # Throttleless dynamic scaling up to logical core capacity
        max_possible = min(12, int(host.free_ram_gb * 1.5), host.logical_cores)
        worktrees = max(2, min(max_possible, math.ceil(grid.overall_complexity_score * 0.9)))
    elif grid.concurrency_leverage == "CPU_BOUND":
        worktrees = max(
            1, min(host.logical_cores // 2, math.ceil(grid.overall_complexity_score / 2.0))
        )
    else:
        max_possible = min(12, int(host.free_disk_gb // 2.0), int(host.free_ram_gb * 1.5))
        worktrees = max(1, min(max_possible, math.ceil(grid.overall_complexity_score * 0.8)))

    io_threads = max(4, min(32, host.logical_cores * 4))

    specialists: list[dict[str, str]] = [
        {
            "role": "Principal Systems Architect",
            "track": "Orchestration",
            "duty": "DAG StateGraph coordination & Autonomous closed-loop engineering",
        },
        {
            "role": "Q&Q Auditor & Telemetry Sentinel",
            "track": "Observability",
            "duty": "Mandatory lightweight protocol audit, speedup metrics & ledger logging",
        },
    ]

    models: list[dict[str, str]] = []

    if is_external:
        models.append({
            "provider": "claude",
            "model": "claude-opus-5[1m]",
            "role": "Systems Architecture & Core Engine Review",
        })
        models.append({
            "provider": "codex",
            "model": "gpt-5.6-sol",
            "role": "Strict Pydantic v2 Models & Typing Contracts",
        })
        if is_uncapped:
            models.append({
                "provider": "kimi",
                "model": "kimi-k3",
                "role": "Adversarial Red-Team Fuzzing & Blast-Radius Sweep",
            })
            models.append({
                "provider": "gemini",
                "model": "gemini-3.8-flash",
                "role": "StateGraph Integration Proof & AST Validation",
            })
    else:
        is_deep = (
            grid.architectural_depth >= 6
            or any(k in prompt_lower for k in ["speculative", "titanfold"])
        )
        if is_deep:
            specialists.append({
                "role": "Core Systems & Low-Level Engineer",
                "track": "Implementation",
                "duty": "Speculative pipeline, memory preservation & engine mechanics",
            })
            models.append({
                "provider": "claude",
                "model": "claude-opus-5[1m]",
                "role": "Deep Architectural Implementation",
            })

        if grid.subsystem_diversity >= 4 or "ui" in prompt_lower or "frontend" in prompt_lower:
            specialists.append({
                "role": "Frontend Console Craftsman",
                "track": "Implementation",
                "duty": "Dense .table-wrap UI, zero-bleed layouts, plain ASCII",
            })
            models.append({
                "provider": "kimi",
                "model": "kimi-k3",
                "role": "Frontend / Full-Stack Synthesis",
            })

        if grid.security_risk_level >= 5 or "mutex" in prompt_lower or "lock" in prompt_lower:
            specialists.append({
                "role": "Threat Modeler & Invariant Guardian",
                "track": "Specification",
                "duty": "Strict Pydantic v2 invariants, mutex contracts & Blue Team safety",
            })
            models.append({
                "provider": "codex",
                "model": "gpt-5.6-sol",
                "role": "Formal Verification & Type Contracts",
            })

    if grid.overall_complexity_score >= 3.0:
        specialists.append({
            "role": "Code Simplifier & Complexity Pruner",
            "track": "Refinement",
            "duty": "Strip AI bloat, deduplicate helpers, enforce Beazley minimalism",
        })
        specialists.append({
            "role": "Isolated Sandbox Test Engineer",
            "track": "Verification",
            "duty": "Execute deterministic unit/contract tests in tmp_path",
        })
        specialists.append({
            "role": "Workforce Watchdog & Zombie Sentinel",
            "track": "Liveness",
            "duty": "Real-time process liveness, completion notifications & auto-reaping",
        })

    if not models:
        models.append({
            "provider": "gemini",
            "model": "gemini-3.7-flash",
            "role": "Fast-Loop StateGraph Execution",
        })

    loops = [
        "Loop 1: Multi-Language AST Pre-Flight (ruff/node/pwsh)",
        "Loop 2: Deterministic tmp_path TDD Suite",
    ]
    if "ui" in prompt_lower or "html" in prompt_lower or "frontend" in prompt_lower:
        loops.append("Loop 3: Playwright Headless Browser Smoke (pageerror=0)")
    loops.append("Loop 4: Two-Pass Code Simplifier Complexity Pruning")
    is_concurrency_sensitive = (
        grid.concurrency_leverage == "CPU_BOUND"
        or any(k in prompt_lower for k in ["mutex", "race"])
    )
    if is_concurrency_sensitive:
        loops.append("Loop 5: Adversarial Concurrency & Fuzzing Probe")

    mode_info = (
        "Uncapped 4-Frontier Swarm"
        if (is_uncapped and is_external)
        else "Uncapped Native"
        if is_uncapped
        else "External Provider Swarm"
        if is_external
        else "Standard Native"
    )
    rationale = (
        f"Mode: {mode_info} | Graded Complexity: {grid.overall_complexity_score}/10. "
        f"Allocated {worktrees} Git worktrees across {len(specialists)} specialist nodes "
        f"and {len(models)} model tiers."
    )

    return WorkforceTopology(
        complexity_score=grid.overall_complexity_score,
        recommended_worktree_workers=worktrees,
        recommended_io_threads=io_threads,
        assigned_specialists=specialists,
        model_dispatch_plan=models,
        active_verification_loops=loops,
        rationale=rationale,
    )


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: graph_complexity_grader.py '<task_description>' [comma_separated_files]")
        sys.exit(1)

    prompt = sys.argv[1]
    files = sys.argv[2].split(",") if len(sys.argv) > 2 else []

    host = probe_host()
    grid = grade_task(prompt, files)
    topology = compute_dynamic_topology(grid, host, prompt)

    print("================================================================================")
    print("            DYNAMIC STATEGRAPH COMPLEXITY GRADER & TOPOLOGY ENGINE")
    print("================================================================================")
    print(f"Task Brief: {prompt}\n")
    print(
        f"Host: {host.logical_cores} Cores | {host.free_ram_gb} GB Free RAM | "
        f"{host.free_disk_gb} GB Free Disk"
    )
    print("--- 5-DIMENSIONAL GRADING GRID ---")
    print(f"  * Surface Area Scope:       {grid.surface_area}/10")
    print(f"  * Architectural Depth:      {grid.architectural_depth}/10")
    print(f"  * Subsystem Diversity:      {grid.subsystem_diversity}/10")
    print(f"  * Security & State Risk:    {grid.security_risk_level}/10")
    print(f"  * Concurrency Leverage:     {grid.concurrency_leverage}")
    print(f"  => OVERALL COMPLEXITY SCORE: {grid.overall_complexity_score} / 10.0\n")

    print("--- DYNAMIC WORKFORCE TOPOLOGY ALLOCATION ---")
    print(f"  * Parallel Git Worktrees:   {topology.recommended_worktree_workers} Active Worktrees")
    print(f"  * I/O Thread Pool:          {topology.recommended_io_threads} Threads")
    print(f"\n--- SPECIALIST NODES ASSIGNED ({len(topology.assigned_specialists)}) ---")
    for s in topology.assigned_specialists:
        print(f"  - [{s['track'].upper()}] {s['role']}: {s['duty']}")

    print(f"\n--- MODEL TIER DISPATCH PLAN ({len(topology.model_dispatch_plan)}) ---")
    for m in topology.model_dispatch_plan:
        print(f"  - {m['provider'].upper()} ({m['model']}) -> {m['role']}")

    print(f"\n--- ACTIVE VERIFICATION LOOPS ({len(topology.active_verification_loops)}) ---")
    for loop in topology.active_verification_loops:
        print(f"  * {loop}")

    print(f"\nRationale: {topology.rationale}")


if __name__ == "__main__":
    main()

# Version: 2.2.0-elite-dreamteam
