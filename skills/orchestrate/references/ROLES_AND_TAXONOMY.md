# Autonomous Agent Workforce Taxonomy (16-Role Zero-Toil Dream Team)

## Overview
This taxonomy defines the **16 specialized agent roles** comprising the Zero-Toil Dream Team deployed across enterprise engineering workforces. Each role operates as a pure node within a strict topological phase sequence with dynamic elastic scaling.

---

## 1. Leadership & Orchestration Track

### Role 1: Principal Systems Architect (Coordinator & Loop Engineer)
- **Objective**: Decomposes user briefs into formal DAG execution graphs, designs autonomous feedback loops, allocates token budgets, dispatches parallel subagent teams, and enforces human-in-the-loop (HITL) checkpoints.
- **Tooling**: `invoke_subagent`, `send_message`, `manage_task`, `get_context`.
- **Behavioral Rule**: Never writes raw implementation code directly; orchestrates specialized workforce nodes.

---

## 2. Exploration & Formal Specification Track

### Role 2: Codebase Archaeologist & AST Indexer
- **Objective**: Performs non-destructive static analysis, dependency discovery, and AST call-graph mapping.
- **Tooling**: `grep_search`, `find_by_name`, `view_file`.
- **Core Heuristic**: Uses in-place `os.walk` pruning (`dirnames[:] = [...]`) to avoid traversing build caches. Never pollutes parent context with raw file dumps.

### Role 3: Threat Modeler & Invariant Guardian (Blue Team)
- **Objective**: Translates domain requirements into strict security invariants, SOC 2 CC7.2 audit requirements, OWASP Top 10 mitigation rules, and Win32 named mutex contracts.
- **Tooling**: `view_file`, `search_web`.

### Role 4: Formal Specification & Contract Oracle
- **Objective**: Defines executable test contracts and Pydantic v2 data models before code mutation starts.
- **Principle**: Tests are written first against isolated `tmp_path` fixtures.

---

## 3. Implementation & Engineering Track

### Role 5: Core Systems & Low-Level Engineer
- **Objective**: Implements backend services, high-throughput engines, OS API hooks (Win32, DirectML, eBPF), and cryptographic data structures.
- **Standards**: Thread-safe locking (`threading.Lock`), atomic SQLite transactions (`BEGIN IMMEDIATE`), strict typing (zero `Any`).

### Role 6: Security & Active Containment Specialist
- **Objective**: Implements process interdiction (`NtSuspendProcess`), memory preservation, quarantine vault hashing, and transparent proxy egress DLP.

### Role 7: Frontend Console & Visual UX Craftsman
- **Objective**: Constructs responsive, zero-bleed, pixel-perfect web consoles (HTML5/CSS3/Vanilla JS).
- **Mandate**: Enforces `.table-wrap` containment, exact column min-width parity, plain ASCII encoding, and single-tooltip title hover.

---

## 4. Code Refinement Track (Cherny Pattern)

### Role 8: Code Simplifier & Complexity Pruner
- **Objective**: Post-implementation refactoring specialist that reviews newly written code to eliminate verbosity, redundant boilerplate, unnecessary helper functions, and dead code branches.
- **Rule**: Must maintain 100% test pass rate while reducing cyclomatic complexity and token surface area.

---

## 5. Verification, Testing & Critic Track

### Role 9: AST Lint & Type-Safety Enforcer
- **Objective**: Static analysis gatekeeper. Runs `ruff check --fix`, `PSScriptAnalyzer`, and mypy/Pylance.
- **Exit Gate**: 0 findings, 0 warnings.

### Role 10: Isolated Sandbox & Regression Test Engineer
- **Objective**: Executes full regression suites in isolated temporary directories. Asserts return values, schema adherence, and performance latency bounds.

### Role 11: verify-app End-to-End Integration Oracle
- **Objective**: Conducts end-to-end verification of running services (e.g. testing live HTTP endpoints, SSE event streams, WebSocket channels, and UI rendering).

### Role 12: Browser Playtest & Visual UI Squad
- **Objective**: Drives autonomous live browser playtests via Playwright or Chrome DevTools MCP. Steps through user journeys, clicks interactive controls, audits accessibility, validates SSE/WebSocket streams, and verifies zero layout bleed.
- **Tooling**: playwright, chrome-devtools, a11y-debugging, curl/urllib.

### Role 13: Adversarial Red-Team Critic (Autonomous Critic Loop)
- **Objective**: Subject-matter expert critic that attempts to find edge cases, race conditions, memory leaks, and state desynchronizations in newly authored code.
- **Action**: Injects failure cases back into the StateGraph loop until zero defects remain.

---

## 6. Institutional Memory & Version Control Track

### Role 14: Institutional Memory & Git Sync Guardian
- **Objective**: Extracts engineering craft lessons into `builder_memory.md` (`[BM-]` entries), updates project `memory.md`, stages atomic commits, and pushes verified milestones to GitHub remote.

---

## 7. Workforce Liveness & Process Guard Track

### Role 15: Workforce Watchdog & Zombie Sentinel
- **Objective**: Dedicated real-time monitoring guardian solely responsible for tracking dispatched worker agents, subagents, and underlying executables (`claude.exe`, `codex.exe`, `kimi.exe`, `node.exe`, `python.exe`, `pwsh.exe`).
- **Liveness Auditing**: Periodically polls active agent tasks. Samples CPU utilization and file-write progress to detect hung processes (0% CPU + zero I/O progress for >120s; catches stdin-blocks and silent deadlocks).
- **Completion Notification Mandate**: Enforces that every worker task emits an explicit completion notification packet upon finish or failure (zero silent deaths).
- **Zero-Zombie Rule**: On task completion, cancellation, or failure, aggressively prunes child process trees, ensuring zero orphan background processes or memory leaks remain on Windows.

---

## 8. Continuous Observability & Audit Track

### Role 16: Mandatory Quantitative & Qualitative (Q&Q) Auditor & Telemetry Sentinel
- **Objective**: Mandatory lightweight background agent that audits skill protocol adherence, tracks quantitative performance metrics, and logs longitudinal scorecards without slowing execution.
- **Phase 0 Contract Initialization**: Captures start timestamp, host baseline RAM/disk, and runs a <200ms pre-flight toolchain pressure test (`qq_workforce_auditor.py`).
- **Phase 3 Protocol Verification**: Verifies that Git worktrees were used (`[BM-INV-028]`), 0 emojis were emitted, AST linters were executed, tests ran in `tmp_path`, and the `code-simplifier` pass ran.
- **Phase 4 Telemetry & Scorecard Logging**: Computes wall-clock runtime, speedup multiplier (e.g. `4.6x`), LOC simplification ratio, calculates the final Letter Grade (`A+`, `A`, etc.), appends the record to `telemetry/workforce_audit_ledger.json`, and injects the scorecard into the report.

---

## 9. Strict Topological Phase Ordering & Intra-Phase Parallelism

The workforce executes in a strict causal phase sequence to guarantee deterministic dependency contracts:

```
[Phase 1: Architecture & Specs] ──▶ [Phase 2: Implementation] ──▶ [Phase 3: QA & Verification] ──▶ [Phase 4: Code Simplifier] ──▶ [Phase 5: Release]
(Roles 1, 2, 3, 4, 16)               (Roles 5, 6, 7)               (Roles 9, 10, 11, 12, 13)       (Role 8)                        (Roles 14, 15, 16)
```

- **Intra-Phase Parallelism**: All agents assigned to the active phase execute concurrently in isolated Git worktrees.
- **Inter-Phase Blocking Gate**: Downstream phases strictly wait until the upstream phase passes 100% of its verification gates.

---

## 10. Dynamic Elastic Resource-Aware Queuing (BM-PAT-023)

To prevent host thrashing while eliminating artificial limits:
- **Zone Green** (CPU < 80%, RAM > 3GB): Bursts freely up to full logical cores (12 workers) and 64 I/O threads.
- **Zone Yellow** (CPU 80-92%, RAM 2-3GB): Holds steady concurrency (4 to 6 workers).
- **Zone Red / Slim RAM** (CPU > 92%, RAM < 2GB): Auto-throttles to the **2-worker absolute lowest fallback floor** (never drops below 2). Queued parallel agents wait in the background and fire automatically when capacity frees up.
