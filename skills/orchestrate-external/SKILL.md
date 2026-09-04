---
name: orchestrate-external
description: >-
  Dispatch an autonomous multi-agent workforce across external frontier CLI
  providers (Claude Opus, OpenAI Codex, Kimi K3, Gemini Flash) in parallel isolated Git worktrees.
---

# /orchestrate-external: Frontier Provider Workforce Orchestration

## Executive Summary
This slash command directly activates the **Elite Workforce Orchestrator** in **External Provider Mode** (`external_providers=True`). It dispatches jobs concurrently to external frontier CLI assistants (`Claude Code`, `OpenAI Codex`, `Kimi Code`, and `Gemini`) running inside dedicated, isolated Git worktrees with mandatory pre-flight scene grounding.

---

## 1. Operational Parameters

- **Provider Policy**: `external_providers=True` (Frontier CLI provider swarm).
- **Default Concurrency**: Standard 50% CPU half-core ceiling (Claude Opus + OpenAI Codex pair).
- **Universal Worktree Mandate**: Dedicated Git worktrees (`equinox-worker-*`) preventing lock collision (`BM-INV-028`).
- **Grounding Mandate**: Mandatory pre-flight inspection of `PROJECT_OUTLINE.md`, `memory.md`, and AST callers.
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
/orchestrate-external <task_brief>
```

Example:
```text
/orchestrate-external Author strict Pydantic v2 schemas and review core systems architecture.
```

Equivalent base command:
```text
/orchestrate external providers <task_brief>
```
