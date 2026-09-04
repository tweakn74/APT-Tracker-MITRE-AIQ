---
name: orchestrate-prov
description: >-
  Orchestrate external CLI providers (Claude Code, OpenAI Codex, Kimi Code) to perform
  heavy dev toil, extensive file authoring, and test loops in isolated Git worktrees,
  allowing Antigravity to act strictly as Architect and Director while conserving tokens.
---

# /orchestrate-prov: Multi-Provider Workforce Orchestrator

## Executive Summary

`/orchestrate-prov` establishes an **Orchestrator-Only Provider Bridge**. It transforms Antigravity into the **Principal Systems Architect & Director**, delegating heavy implementation toil, multi-file code authoring, and mechanical test loops to local external CLI providers (`Claude Code`, `OpenAI Codex`, and `Moonshot Kimi Code`).

### The Token Arbitrage Advantage
- **Antigravity Consumption**: Consumes minimal tokens (~500 tokens for planning and task dispatch + ~500 tokens for final diff review).
- **External Provider Consumption**: The external CLI provider executes locally via your subscription, absorbing the 50,000+ token churn of editing large files, running test loops, and debugging AST errors.
- **Zero Risk / Zero Contention**: All external provider runs execute in isolated Git worktrees (`BM-INV-028`). They cannot corrupt your active checkout, collide on locks, or stall your interactive session.

---

## 1. Provider Selection Matrix

Select the optimal provider based on the task domain:

| Provider | Local CLI Command | Cognitive Strength & Domain Specialty |
|---|---|---|
| **Claude Code** | `claude --permission-mode bypassPermissions -p "<prompt>"` | **Deep Code Refactoring & Architecture**: Complex logic transforms, full-file authoring, multi-file coherence, and neurosurgical patches. |
| **OpenAI Codex** | `powershell -File .../codex.ps1 -p "<prompt>"` | **Formal Verification & Strict Typing**: Pydantic v2 schemas, strict type contracts, AST validation, and deterministic property checks. |
| **Kimi Code** | `kimi run -p "<prompt>"` | **Massive Context & Broad File Trees**: Large repository-wide file indexing, comprehensive doc migrations, and multi-package search. |

---

## 2. The 4-Phase Provider Orchestration Lifecycle

```
[Phase 0: Architectural Specification & Contract Generation]
  +-- Antigravity drafts precise task requirements and contract tests.
  +-- Generates isolated tmp_path contract specifications.
                           |
                           v
[Phase 1: Universal Git Worktree Isolation (BM-INV-028)]
  +-- Provisions isolated worktree: ../<repo>-wt-<provider>-<timestamp>
  +-- Protects active working tree from dirty states and file locks.
                           |
                           v
[Phase 2: Autonomous Headless Provider Execution ("Dirty Work")]
  +-- Spawns chosen CLI binary in worktree with non-interactive flags.
  +-- Provider executes full edit cycles, compiles, and self-repairs.
                           |
                           v
[Phase 3: Adversarial Proofreader & 3-Tier QC Gate]
  +-- Antigravity inspects git diff --stat across modified files.
  +-- Multi-language static check: ruff check (py), node -c (js), PSScriptAnalyzer (pwsh).
  +-- Runs isolated test verification against the provider's work.
                           |
                           v
[Phase 4: Atomic Merge, Memory Sync & Clean Teardown]
  +-- Fast-forward or squash merge into target branch.
  +-- Immediately prunes worktree (git worktree remove --force).
  +-- Updates project memory.md and builder_memory.md.
```

---

## 3. Invocation & Usage Reference

### Running via Python Helper Script

Antigravity executes the bundled orchestrator engine located at:
`~/.gemini/config/skills/orchestrate-prov/scripts/provider_orchestrator.py`

#### A. Dispatch to Claude Code (Default for Code Synthesis)
```bash
python ~/.gemini/config/skills/orchestrate-prov/scripts/provider_orchestrator.py \
  --provider claude \
  --task "Implement Phase 4 Win32 overlapped DMA ring in core/device/win32_io.py. Obey 300 LOC limit, zero Any types, plain ASCII." \
  --timeout 300
```

#### B. Dispatch to OpenAI Codex (Type Contracts & Formal Logic)
```bash
python ~/.gemini/config/skills/orchestrate-prov/scripts/provider_orchestrator.py \
  --provider codex \
  --task "Refactor core/models/config.py to strict Pydantic v2 schemas with zero Any annotations." \
  --timeout 300
```

#### C. Dispatch to Kimi Code (Repo-Wide Sweeps & Large Context)
```bash
python ~/.gemini/config/skills/orchestrate-prov/scripts/provider_orchestrator.py \
  --provider kimi \
  --task "Scan all doc references in docs/ for stale tau=32 parameters and update to tau=16." \
  --timeout 300
```

---

## 4. Hard Invariants for Provider Orchestration

1. **Universal Worktree Mandate (BM-INV-028)**:
   - External providers must NEVER be executed directly in the main repository checkout. They must execute exclusively in a dedicated Git worktree branch (`task/<provider>-<timestamp>`).
2. **Immediate Eager Teardown (BM-INV-022 / BM-INV-036)**:
   - Once the provider completes and the diff is validated, immediately remove the worktree (`git worktree remove --force`) and prune references.
3. **Zero Deception & Honest Verification (BM-INV-033 / BM-INV-034)**:
   - Antigravity must critically verify the provider's output. Never accept an exit code 0 as proof of completion; inspect `git diff --stat`, verify that real code was written (not mock stubs), and run the test suite.
4. **Surface Pro 16GB Concurrency Ceiling (BM-INV-026)**:
   - Run at most 1 external provider CLI process at a time on the 16GB host to avoid memory pressure and context paging stalls.
