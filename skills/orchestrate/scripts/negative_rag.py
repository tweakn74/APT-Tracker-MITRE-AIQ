"""
Elite Workforce Orchestrator - Negative Invariant & Dead-End RAG Engine.
Part of the 16-Role Zero-Toil Dream Team Framework.
Scans builder_memory.md and memory.md in <5ms for [BM-DEAD] failure modes, [BM-INV-] invariants,
and [BM-TC-] toolchain rules matching target keywords.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path


def search_invariants(
    keywords: list[str], search_dirs: list[Path]
) -> list[tuple[str, str, str]]:
    matches: list[tuple[str, str, str]] = []
    keywords_lower = [k.lower() for k in keywords]
    pattern = re.compile(r"^\s*(BM-(?:INV|DEAD|TC|ORA|PAT)-\d+):\s*(.*)$")

    for s_dir in search_dirs:
        for md_name in ["builder_memory.md", "memory.md", "CODE-QUALITY.md"]:
            target_file = s_dir / md_name
            if not target_file.exists():
                continue
            lines = target_file.read_text(
                encoding="utf-8", errors="replace"
            ).splitlines()
            for line in lines:
                m = pattern.search(line)
                if m:
                    rule_tag = m.group(1)
                    rule_body = m.group(2)
                    line_lower = line.lower()
                    if any(k in line_lower for k in keywords_lower) or not keywords:
                        matches.append((str(target_file), rule_tag, rule_body))
    return matches


def main() -> None:
    keywords = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    # Default search roots: user global .gemini and current working directory
    user_home = Path(os.path.expanduser("~")) / ".gemini"
    current_dir = Path.cwd()
    search_dirs = [user_home, current_dir]

    results = search_invariants(keywords, search_dirs)
    if not results:
        print(f"[RAG] 0 negative invariants found matching: {', '.join(keywords)}")
        return

    print(
        f"[RAG] Matched {len(results)} Invariant(s) for query '{' '.join(keywords)}':"
    )
    for file_path, tag, rule in results[:10]:
        print(f"  [{tag}] {rule.strip()} ({Path(file_path).name})")


if __name__ == "__main__":
    main()

# Version: 2.1.0-elite-dreamteam
