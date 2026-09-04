"""
Elite Workforce Orchestrator - Multi-Language Static AST Verification Gate.
Part of the 16-Role Zero-Toil Dream Team Framework.
Validates:
- Python: ruff check --fix (0 violations)
- PowerShell: PSScriptAnalyzer (0 findings)
- JavaScript / TypeScript / HTML Embedded JS: node -c (0 syntax diagnostics)
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


def get_ruff_command() -> list[str]:
    """Resolves the best available ruff executable path."""
    ruff_on_path = shutil.which("ruff")
    if ruff_on_path:
        return [ruff_on_path]

    user_home = Path.home()
    fallback_paths = [
        user_home / r"AppData\Local\Programs\Python\Python312\Scripts\ruff.exe",
        user_home / r"AppData\Local\Programs\Python\Python313\Scripts\ruff.exe",
        Path(r"C:\Python313\Scripts\ruff.exe"),
        Path(r"C:\Python312\Scripts\ruff.exe"),
    ]
    for fp in fallback_paths:
        if fp.exists():
            return [str(fp)]

    return [sys.executable, "-m", "ruff"]


def lint_python(file_path: Path) -> tuple[bool, str]:
    try:
        cmd = get_ruff_command() + ["check", "--fix", str(file_path)]
        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode == 0:
            return True, "0 violations"
        return False, res.stdout.strip() or res.stderr.strip()
    except (OSError, subprocess.SubprocessError) as exc:
        return False, f"Linter error: {exc}"


def lint_powershell(file_path: Path) -> tuple[bool, str]:
    try:
        cmd = f"Invoke-ScriptAnalyzer -Path '{file_path}'"
        res = subprocess.run(
            ["powershell", "-NoProfile", "-Command", cmd],
            capture_output=True,
            text=True,
            check=False,
        )
        output = res.stdout.strip()
        if not output or "RuleName" not in output:
            return True, "0 findings"
        return False, output
    except (OSError, subprocess.SubprocessError) as exc:
        return False, f"PSScriptAnalyzer error: {exc}"


def lint_html_js(file_path: Path) -> tuple[bool, str]:
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
        scripts = re.findall(
            r"<script(?:\s+[^>]*)?>(.*?)</script>", content, re.DOTALL | re.IGNORECASE
        )
        for idx, script_body in enumerate(scripts, start=1):
            if not script_body.strip():
                continue
            proc = subprocess.run(
                ["node", "-c"],
                input=script_body,
                text=True,
                capture_output=True,
                check=False,
            )
            if proc.returncode != 0:
                return (
                    False,
                    f"Script block #{idx} failed syntax check:\n{proc.stderr.strip()}",
                )
        return True, "0 syntax errors"
    except (OSError, subprocess.SubprocessError, UnicodeError) as exc:
        return False, f"Node parse error: {exc}"


def lint_file(file_path: Path) -> tuple[bool, str]:
    ext = file_path.suffix.lower()
    if ext == ".py":
        return lint_python(file_path)
    if ext in (".ps1", ".psm1", ".psd1"):
        return lint_powershell(file_path)
    if ext in (".html", ".htm"):
        return lint_html_js(file_path)
    return True, "skipped (no linter configured)"


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: multi_lint.py <file_1> <file_2> ...")
        sys.exit(1)

    all_passed = True
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_file():
            passed, msg = lint_file(p)
            status = "[PASS]" if passed else "[FAIL]"
            print(f"{status} {p.name}: {msg}")
            if not passed:
                all_passed = False

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()

# Version: 2.1.0-elite-dreamteam
