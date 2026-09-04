"""
Elite Workforce Orchestrator - AST Reconnaissance & Call-Graph Engine.
Part of the 16-Role Zero-Toil Dream Team Framework.
Extracts top-level function definitions, classes, and import dependencies without full execution.
Enforces [BM-INV-001] in-place directory pruning for ultra-fast traversal.
"""
from __future__ import annotations

import ast
import json
import os
import sys
from pathlib import Path

IGNORE_DIRS = {".git", ".venv", "venv", "node_modules", ".cache", "__pycache__", "build", "dist"}


def extract_symbols(file_path: Path) -> dict:
    """Extracts function, class, and import symbols from a Python file AST."""
    try:
        source_code = file_path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(source_code, filename=str(file_path))
    except (SyntaxError, UnicodeError, OSError) as exc:
        return {"file": str(file_path), "error": str(exc)}

    functions: list[str] = []
    classes: list[str] = []
    imports: list[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.AsyncFunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.append(node.module)

    return {
        "file": str(file_path),
        "functions": sorted(set(functions)),
        "classes": sorted(set(classes)),
        "imports": sorted(set(imports)),
    }


def scan_directory(target_dir: Path) -> list[dict]:
    """Scans all python files in directory applying [BM-INV-001] directory pruning."""
    results: list[dict] = []
    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file.endswith(".py"):
                results.append(extract_symbols(Path(root) / file))
    return results


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ast_recon.py <path_to_file_or_dir>")
        sys.exit(1)

    target_path = Path(sys.argv[1])
    if target_path.is_file():
        res = extract_symbols(target_path)
        print(json.dumps(res, indent=2))
    elif target_path.is_dir():
        results = scan_directory(target_path)
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()

# Version: 2.1.0-elite-dreamteam
