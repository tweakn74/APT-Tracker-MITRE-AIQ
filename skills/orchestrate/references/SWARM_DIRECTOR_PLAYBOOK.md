# Swarm Director Playbook

## Autonomous Leadership Principles for Autonomous Agent Fleets

### 1. "Loop Engineering" is the Future of Development
- Moving from manual turn-by-turn prompting to designing **autonomous recursive systems**.
- The human engineer acts as the **Director**: defining explicit contracts, budgets, constraints, and verification hooks.
- The agent fleet executes in self-correcting loops until all deterministic gates pass.

### 2. The Living Memory Mandate (Cherny's CLAUDE.md & Antigravity's BM- Standard)
- Whenever a human correction is made, or an invariant is discovered:
  > *"Update your memory so the fleet never makes that mistake again."*
- Keep project `memory.md` concise (<2,500 tokens of high-leverage context).
- Universal toolchain invariants belong in `builder_memory.md` (`[BM-]` entries).

### 3. Dedicated Code Simplification (The `code-simplifier` Rule)
- AI agents naturally generate verbose, defensive, and boilerplate-heavy code.
- **Rule**: Never merge raw first-pass AI code without a dedicated simplification pass that prunes dead paths, collapses redundancy, and enforces David Beazley-grade minimalism.

### 4. Zero-Defect Standard (The Beazley / Cyclic StateGraph Benchmark)
- Software is never marked "done" upon file generation; it is done only when:
  1. Multi-language static analysis passes with 0 lint/AST violations (`ruff` for Python, `node -c` on all HTML script blocks, `PSScriptAnalyzer` for PowerShell).
  2. Isolated unit & contract tests pass 100% in ephemeral `tmp_path` environments.
  3. Headless UI smoke tests (`playwright`) confirm 0 unhandled JavaScript runtime exceptions (`pageerror == 0` & `console.error == 0`).
  4. Live end-to-end verification (`verify-app`) passes with status 200.
  5. Full regression suite confirms 0 collateral breakages.
  6. Institutional craft lessons are recorded in `builder_memory.md`.
  7. Verified atomic commits are pushed to GitHub remote.

### 5. Plain ASCII & Zero-Emoji Mandate
- Production code, scripts, logs, and developer interfaces must strictly use Plain ASCII encoding.
- Emojis introduce Windows CP-1252 character corruption and degrade enterprise Blue Team telemetry.

### 6. The 16-Role Zero-Toil Dream Team Standard
- Default to the 16-role taxonomy across all enterprise dev cycles.
- Enforce strict topological phase ordering (Phase 1: Architecture -> Phase 2: Implementation -> Phase 3: QA -> Phase 4: Simplifier -> Phase 5: Release).
- Maintain 100% intra-phase Git worktree parallelism with 3-tier QC verification gates.

### 7. Elastic Hardware Scaling & 2-Worker Floor (BM-PAT-023)
- Concurrency scales dynamically with live host RAM and CPU load.
- Under heavy load or critically slim memory (<2GB RAM), the orchestrator automatically holds at the **2-worker absolute lowest fallback floor** without freezing the operating system.

