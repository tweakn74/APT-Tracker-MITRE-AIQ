---
name: orchestrate-uncapped
description: >-
  Dispatch an autonomous multi-agent workforce in Uncapped Throttleless Mode,
  lifting the 50% CPU half-core ceiling with dynamic host pressure safety.
---

# /orchestrate-uncapped: Throttleless Workforce Orchestration

## Executive Summary
This slash command directly activates the **Elite Workforce Orchestrator** in **Uncapped Throttleless Mode** (`uncapped=True`). It lifts the standard 50% CPU half-core throttling ceiling, scaling parallel worker allocation up to 100% of logical CPU cores and available RAM headroom while dynamically governed by the `DynamicPressureGauge` host monitor.

---

## 1. Operational Parameters

- **Concurrency**: `uncapped=True` (Throttleless execution, elastic worker scaling up to 8+ worktrees).
- **Host Safety**: Real-time sampling via `HardwareSensor` and `DynamicPressureGauge` (`BM-PAT-023`). Automatically yields and sheds load if host free RAM < 1.5 GB or CPU > 92%.
- **Lifecycle**: 5-Phase StateGraph architecture with Universal Git Worktree isolation (`BM-INV-028`).
- **Gate Enforcement**: Mandatory 3-Tier QC (Ruff 0 violations, pytest tmp_path clean, Code Simplifier pass).

---

## 2. The 5 Closed-Loop Invariants

1. **Pre-Flight Research & Assimilation (Phase 0)**:
   - **Canon Researcher** ingests `PROJECT_OUTLINE.md`, `memory.md`, and `ROADMAP_TODO.md`.
   - **Codebase Archaeologist** runs AST call-graph scans of target modules and 3 nearby reference files.
   - **Lead Architect** assimilates findings into concrete, granular worker specifications before task dispatch.
2. **Per-Worker Micro-Manager Gate (Phase 2)**:
   - Pair each worker with an immediate adversarial proofreader inside its isolated Git worktree.
   - Execute in-memory AST syntax and type checks immediately upon worker completion.
   - Trigger instant localized redo loops for that specific worker before wider gates run.
3. **True Cycle Decider (Phase 3)**:
   - Capture exact compiler, linter, and test stderr and pipe it back to the failing worker CLI.
   - Iterate autonomous self-correction loops until all deterministic gates turn 100% green.
4. **Pre-Release Cohesion Auditor**:
   - Audit cross-worktree interface alignment, circular imports, and duplicate helper functions.
   - Pass clean diff to Code Simplifier for anti-bloat refactoring.
5. **Progressive Monitor Watchdog**:
   - Continuously monitor agent status in real time.
   - Terminate worker processes eagerly the moment their diffs pass with 0 pending redos (BM-INV-022).

---

## 3. Invocation Syntax

```text
/orchestrate-uncapped <task_brief>
```

Example:
```text
/orchestrate-uncapped Execute full regression and AST optimization on speculative scheduler.
```

Equivalent base command:
```text
/orchestrate uncapped <task_brief>
```
