"""
Elite Workforce Orchestrator - External Provider Workforce Dispatcher.
Part of the 16-Role Zero-Toil Dream Team Framework.
Executes non-interactive batch prompts across external CLI providers
(Claude, Codex, Kimi, Antigravity).
Captures parallel output streams and synthesizes multi-perspective consensus results.
"""
from __future__ import annotations

import concurrent.futures
import subprocess
import sys
from pathlib import Path
from typing import Any

# Provider CLI Invocation Matrix (Dynamic User Home)
USER_HOME = Path.home()
PROVIDERS: dict[str, list[str]] = {
    "claude": [str(USER_HOME / ".local" / "bin" / "claude.exe"), "-p"],
    "codex": [
        "powershell", "-NoProfile", "-File",
        str(USER_HOME / "AppData" / "Roaming" / "npm" / "codex.ps1"),
    ],
    "kimi": [str(USER_HOME / ".kimi-code" / "bin" / "kimi.exe"), "run"],
}


def invoke_single_provider(
    name: str,
    prompt: str,
    cwd: str,
    timeout_secs: int = 120,
) -> dict[str, Any]:
    """Invokes an external AI CLI non-interactively and captures stdout/stderr."""
    if name not in PROVIDERS:
        return {"provider": name, "success": False, "error": f"Unknown provider: {name}"}

    cmd = PROVIDERS[name] + [prompt]
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout_secs,
            check=False,
        )
        return {
            "provider": name,
            "success": proc.returncode == 0,
            "exit_code": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
        }
    except subprocess.TimeoutExpired:
        return {
            "provider": name,
            "success": False,
            "error": f"Timed out after {timeout_secs}s",
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "provider": name,
            "success": False,
            "error": str(exc),
        }


def dispatch_multi_provider(
    prompt: str,
    cwd: str,
    providers: list[str] | None = None,
    timeout_secs: int = 120,
) -> dict[str, dict[str, Any]]:
    """Concurrently executes the prompt across requested external providers."""
    if providers is None:
        providers = ["claude", "kimi", "codex"]

    results: dict[str, dict[str, Any]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(providers)) as executor:
        future_to_provider = {
            executor.submit(invoke_single_provider, p, prompt, cwd, timeout_secs): p
            for p in providers
        }
        for future in concurrent.futures.as_completed(future_to_provider):
            p_name = future_to_provider[future]
            try:
                results[p_name] = future.result()
            except Exception as exc:  # noqa: BLE001
                results[p_name] = {"provider": p_name, "success": False, "error": str(exc)}

    return results


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python provider_workforce_dispatcher.py '<prompt>' [cwd]")
        sys.exit(1)

    prompt = sys.argv[1]
    cwd = sys.argv[2] if len(sys.argv) > 2 else str(Path.cwd())

    print(f"[Orchestrator] Dispatching to external providers: {prompt[:80]}...")
    results = dispatch_multi_provider(prompt, cwd)

    for name, res in results.items():
        print(f"\n{'='*30} Provider: {name.upper()} {'='*30}")
        if res.get("success"):
            print(res.get("stdout"))
        else:
            err_msg = res.get("error") or res.get("stderr")
            print(f"Error / Failed (Exit {res.get('exit_code')}): {err_msg}")


if __name__ == "__main__":
    main()

# Version: 2.1.0-elite-dreamteam
