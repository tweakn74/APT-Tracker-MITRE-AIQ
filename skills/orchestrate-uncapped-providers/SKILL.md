---
name: orchestrate-uncapped-providers
description: >-
  Dispatch an autonomous multi-agent workforce combining Uncapped Concurrency
  and the 4-Frontier External Provider Swarm (Claude Opus, OpenAI Codex, Kimi K3, Gemini Flash).
---

# /orchestrate-uncapped-providers: Uncapped 4-Frontier Swarm Orchestration

## Executive Summary
This slash command directly activates the **Elite Workforce Orchestrator** combining **Uncapped Throttleless Concurrency** (`uncapped=True`) and the full **4-Frontier External Swarm** (`external_providers=True`). It dispatches Claude Opus, OpenAI Codex, Kimi K3, and Gemini Flash simultaneously across parallel isolated Git worktrees, governed dynamically by host memory and CPU headroom.

---

## 1. Operational Parameters

- **Concurrency**: `uncapped=True` (Elastic scaling up to 8 parallel Git worktrees).
- **Provider Policy**: `external_providers=True` (Full 4-Frontier Swarm):
  * `Claude Opus`: Architecture & core systems review
  * `OpenAI Codex`: Strict Pydantic v2 schemas & type contracts
  * `Kimi K3`: Adversarial red-team fuzzing & AST blast-radius sweep
  * `Gemini Flash`: StateGraph loop validation & integration proof
- **Host Safety**: Real-time monitoring via `DynamicPressureGauge`. Auto-sheds load if host free RAM < 1.5 GB.
- **Grounding Mandate**: Mandatory pre-flight scene inspection of `PROJECT_OUTLINE.md`, `memory.md`, and AST callers.
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
/orchestrate-uncapped-providers <task_brief>
```

Example:
```text
/orchestrate-uncapped-providers Execute Phase 4 Win32 DMA ring buffer and speculative scheduler completion.
```

Equivalent base command:
```text
/orchestrate uncapped external providers <task_brief>
```
