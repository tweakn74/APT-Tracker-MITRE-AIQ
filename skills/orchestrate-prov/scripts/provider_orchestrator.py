"""
Multi-Provider Workforce Orchestrator & Token Arbitrage Engine.
Executes external local CLI assistants (Claude Code, OpenAI Codex, Kimi Code)
inside isolated Git worktrees, allowing Antigravity to act as Director without
consuming local context tokens on mechanical implementation toil.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

USER_HOME = Path.home()

class Provider(StrEnum):
    CLAUDE = "claude"
    CODEX = "codex"
    KIMI = "kimi"
    AGY = "agy"

@dataclass(frozen=True)
class ProviderConfig:
    name: Provider
    binary_path: Path
    base_args: tuple[str, ...]
    description: str

PROVIDER_REGISTRY: dict[Provider, ProviderConfig] = {
    Provider.CLAUDE: ProviderConfig(
        name=Provider.CLAUDE,
        binary_path=USER_HOME / ".local" / "bin" / "claude.exe",
        base_args=(
            "--permission-mode",
            "bypassPermissions",
            "-p",
        ),
        description="Claude Code (Best for deep refactoring, code synthesis, full-file authoring)",
    ),
    Provider.CODEX: ProviderConfig(
        name=Provider.CODEX,
        binary_path=USER_HOME / "AppData" / "Roaming" / "npm" / "codex.ps1",
        base_args=(
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
        ),
        description=(
            "OpenAI Codex (Best for strict type contracts, AST audits, formal verification)"
        ),
    ),
    Provider.KIMI: ProviderConfig(
        name=Provider.KIMI,
        binary_path=USER_HOME / ".kimi-code" / "bin" / "kimi.exe",
        base_args=(
            "run",
            "-p",
        ),
        description="Kimi Code (Best for massive repository synthesis and multi-file context)",
    ),
    Provider.AGY: ProviderConfig(
        name=Provider.AGY,
        binary_path=USER_HOME / "AppData" / "Local" / "agy" / "bin" / "agy.exe",
        base_args=(
            "-p",
        ),
        description="Google Antigravity CLI",
    ),
}

@dataclass
class ExecutionResult:
    provider: Provider
    success: bool
    exit_code: int
    duration_seconds: float
    worktree_dir: Path
    diff_stat: str
    stdout: str
    stderr: str

def find_git_root(cwd: Path) -> Path | None:
    """Traverse upward to find the repository root containing .git."""
    curr = cwd.resolve()
    for parent in [curr, *curr.parents]:
        if (parent / ".git").exists():
            return parent
    return None

def create_isolated_worktree(repo_root: Path, branch_name: str) -> Path:
    """Provisions an isolated Git worktree to eliminate lock contention."""
    worktree_path = repo_root.parent / f"{repo_root.name}-wt-{branch_name}"
    if worktree_path.exists():
        # Prune existing dirty worktree if present
        subprocess.run(
            ["git", "worktree", "remove", "--force", str(worktree_path)],
            cwd=str(repo_root),
            capture_output=True,
            check=False,
        )
        if worktree_path.exists():
            shutil.rmtree(worktree_path, ignore_errors=True)

    subprocess.run(
        ["git", "worktree", "add", "-b", f"task/{branch_name}", str(worktree_path)],
        cwd=str(repo_root),
        capture_output=True,
        check=True,
        text=True,
    )
    return worktree_path

def cleanup_worktree(repo_root: Path, worktree_path: Path, keep: bool = False) -> None:
    """Removes the worktree and cleans dangling references unless keep is True."""
    if keep or not worktree_path.exists():
        return
    subprocess.run(
        ["git", "worktree", "remove", "--force", str(worktree_path)],
        cwd=str(repo_root),
        capture_output=True,
        check=False,
    )
    subprocess.run(
        ["git", "worktree", "prune"],
        cwd=str(repo_root),
        capture_output=True,
        check=False,
    )

def build_contract_prompt(raw_prompt: str) -> str:
    """Enriches the task with strict engineering standards and invariants."""
    preamble = (
        "Operating Standard: Plain ASCII Only | Zero Emojis | Strict Type Annotations.\n"
        "Rules: Contiguous edits <= 300 LOC. No mock stubs or demo fallbacks.\n"
        "Enforce zero lint errors (ruff / PSScriptAnalyzer). State verification rung."
    )
    return f"{preamble}\n\nTask Specification:\n{raw_prompt}"

def execute_provider(
    provider_name: Provider,
    task_prompt: str,
    repo_root: Path,
    timeout_secs: int = 300,
    keep_worktree: bool = False,
) -> ExecutionResult:
    """Executes a provider within a dedicated worktree and returns diff & metrics."""
    cfg = PROVIDER_REGISTRY.get(provider_name)
    if not cfg:
        raise ValueError(f"Unknown provider: {provider_name}")

    if not cfg.binary_path.exists():
        raise FileNotFoundError(f"Provider binary not found at: {cfg.binary_path}")

    timestamp_str = str(int(time.time()))
    branch_name = f"{provider_name.value}-{timestamp_str}"
    worktree_dir = create_isolated_worktree(repo_root, branch_name)

    enriched_prompt = build_contract_prompt(task_prompt)

    # Build command list
    if provider_name == Provider.CODEX:
        cmd: list[str] = [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(cfg.binary_path),
            "-p",
            enriched_prompt,
        ]
    else:
        cmd = [str(cfg.binary_path), *cfg.base_args, enriched_prompt]

    start_time = time.monotonic()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(worktree_dir),
            capture_output=True,
            text=True,
            timeout=timeout_secs,
            check=False,
        )
        duration = round(time.monotonic() - start_time, 2)

        # Inspect git diff in the worktree
        diff_res = subprocess.run(
            ["git", "diff", "--stat"],
            cwd=str(worktree_dir),
            capture_output=True,
            text=True,
            check=False,
        )
        diff_stat = diff_res.stdout.strip()

        result = ExecutionResult(
            provider=provider_name,
            success=(proc.returncode == 0),
            exit_code=proc.returncode,
            duration_seconds=duration,
            worktree_dir=worktree_dir,
            diff_stat=diff_stat,
            stdout=proc.stdout.strip(),
            stderr=proc.stderr.strip(),
        )
    finally:
        if not keep_worktree:
            cleanup_worktree(repo_root, worktree_dir, keep=keep_worktree)

    return result

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Orchestrate external CLI providers to perform heavy dev toil."
    )
    parser.add_argument(
        "--provider",
        "-p",
        choices=[p.value for p in Provider],
        default=Provider.CLAUDE.value,
        help="Target provider CLI to execute.",
    )
    parser.add_argument(
        "--task",
        "-t",
        required=True,
        help="Task description or architectural specification to execute.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Execution timeout in seconds (default: 300).",
    )
    parser.add_argument(
        "--keep-worktree",
        action="store_true",
        help="Preserve worktree directory post-execution for inspection.",
    )

    args = parser.parse_args()

    repo_root = find_git_root(Path.cwd())
    if not repo_root:
        sys.stderr.write("Error: Current directory is not inside a Git repository.\n")
        sys.exit(1)

    provider_enum = Provider(args.provider)
    print(f"[Orchestrator] Dispatching '{provider_enum.value}' in isolated worktree...")
    print(f"[Orchestrator] Target repository: {repo_root}")

    res = execute_provider(
        provider_name=provider_enum,
        task_prompt=args.task,
        repo_root=repo_root,
        timeout_secs=args.timeout,
        keep_worktree=args.keep_worktree,
    )

    print("\n" + "=" * 60)
    print(f"PROVIDER EXECUTION COMPLETE: {res.provider.upper()}")
    print("=" * 60)
    print(f"Status:       {'SUCCESS' if res.success else 'FAILED'} (Exit code: {res.exit_code})")
    print(f"Duration:     {res.duration_seconds}s")
    print(f"Worktree:     {res.worktree_dir}")
    print(f"Diff Summary:\n{res.diff_stat or 'No files modified.'}")
    print("-" * 60)
    if res.stdout:
        print(f"Output:\n{res.stdout[:1500]}")
    if res.stderr:
        print(f"Errors:\n{res.stderr[:1000]}")
    print("=" * 60)

if __name__ == "__main__":
    main()
