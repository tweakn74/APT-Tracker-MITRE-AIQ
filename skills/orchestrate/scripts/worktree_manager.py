"""
Elite Workforce Orchestrator - Git Worktree Lifecycle Manager.
Part of the 16-Role Zero-Toil Dream Team Framework.
Creates, lists, prunes, and cleans up isolated Git worktrees for autonomous agent teams.
Enforces [BM-INV-028] Universal Worktree Mandate across parallel execution phases.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run_git(cmd: list[str], cwd: Path) -> tuple[int, str, str]:
    proc = subprocess.run(
        ["git", *cmd],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def list_worktrees(repo_dir: Path) -> list[dict[str, str]]:
    code, stdout, _ = run_git(["worktree", "list", "--porcelain"], repo_dir)
    if code != 0:
        return []

    worktrees: list[dict[str, str]] = []
    current_entry: dict[str, str] = {}
    for line in stdout.splitlines():
        if not line.strip():
            if current_entry:
                worktrees.append(current_entry)
                current_entry = {}
            continue
        if line.startswith("worktree "):
            current_entry["path"] = line.split(" ", 1)[1]
        elif line.startswith("branch "):
            current_entry["branch"] = line.split(" ", 1)[1]
        elif line.startswith("HEAD "):
            current_entry["head"] = line.split(" ", 1)[1]

    if current_entry:
        worktrees.append(current_entry)
    return worktrees


def create_agent_worktree(
    repo_dir: Path,
    agent_name: str,
    branch_name: str | None = None,
) -> tuple[bool, str]:
    if not branch_name:
        branch_name = f"workforce/{agent_name}"

    worktree_path = repo_dir / ".worktrees" / agent_name
    worktree_path.parent.mkdir(parents=True, exist_ok=True)

    code, stdout, stderr = run_git(
        ["worktree", "add", "-B", branch_name, str(worktree_path)],
        repo_dir,
    )
    if code == 0:
        return True, str(worktree_path)
    return False, stderr or stdout


def prune_worktrees(repo_dir: Path) -> tuple[bool, str]:
    code, stdout, stderr = run_git(["worktree", "prune"], repo_dir)
    return code == 0, stderr or stdout


def remove_agent_worktree(repo_dir: Path, agent_name: str) -> tuple[bool, str]:
    worktree_path = repo_dir / ".worktrees" / agent_name
    code, stdout, stderr = run_git(["worktree", "remove", "--force", str(worktree_path)], repo_dir)
    prune_worktrees(repo_dir)
    return code == 0, stderr or stdout


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: worktree_manager.py <list|create|remove|prune> [agent_name] [repo_path]")
        sys.exit(1)

    action = sys.argv[1].lower()
    agent_name = sys.argv[2] if len(sys.argv) > 2 else "worker-1"
    repo_path = Path(sys.argv[3]) if len(sys.argv) > 3 else Path.cwd()

    if action == "list":
        wt_list = list_worktrees(repo_path)
        print(f"Active Git Worktrees ({len(wt_list)}):")
        for wt in wt_list:
            print(f"  - {wt.get('path')} [{wt.get('branch', 'detached')}]")
    elif action == "create":
        success, res = create_agent_worktree(repo_path, agent_name)
        status = "[SUCCESS]" if success else "[FAILED]"
        print(f"{status} Created worktree: {res}")
    elif action == "remove":
        success, res = remove_agent_worktree(repo_path, agent_name)
        status = "[SUCCESS]" if success else "[FAILED]"
        print(f"{status} Removed worktree: {res}")
    elif action == "prune":
        success, res = prune_worktrees(repo_path)
        print(f"Worktree prune: {res}")


if __name__ == "__main__":
    main()

# Version: 2.1.0-elite-dreamteam
