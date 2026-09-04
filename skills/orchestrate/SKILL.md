---
name: orchestrate
description: >-
  Architect, dispatch, and coordinate Enterprise-grade autonomous multi-agent engineering workforces.
  Supports /orchestrate, /orchestrate uncapped, /orchestrate external providers, and
  /orchestrate uncapped external providers across parallel Git worktrees with 3-tier QC gates.
---

# Elite Workforce Orchestrator (Cyclic StateGraph & Autonomous Closed-Loop Synthesis)

## Executive Summary
This skill synthesizes **Cyclic StateGraph Graph Engineering** and **Autonomous Closed-Loop (Head of Claude Code) Loop Engineering**. It empowers Antigravity to act as a **Principal Systems Architect & Engineering Director**, orchestrating autonomous agent teams across parallel Git worktrees, recursive self-correction loops, automated code simplification, and deterministic verification gates.

---

## 1. The 5-Phase StateGraph & Loop Architecture

```
[Phase 0: Objective Brief & Dynamic Complexity Grid]
  +-- Dynamic Complexity Grader (5D Complexity Scoring & Worktree Allocation)
  +-- Mandatory Q&Q Auditor (Pre-Run Contract & Toolchain Pressure Test <200ms)
                           |
                           v
[Phase 1: Exploration, Worktree Isolation & Specification]
  +-- Codebase Archaeologist (AST & Dependency Mapping)
  +-- Agentic Search Specialist (Precision grep & Targeted Slices; No RAG Bloat)
  +-- Threat & Invariant Guardian (Blue Team & Mutex Contracts)
  +-- Contract Oracle (Isolated tmp_path Test Specifications)
                           |
                           v
[Phase 2: Parallel Worktree Implementation & Skeptic Gate]
  +-- Core Systems Specialist (Git Worktree Alpha: Backend / Engine)
  +-- Active Containment Specialist (Git Worktree Beta: Interdiction)
  +-- Frontend Console Craftsman (Git Worktree Gamma: Web UX)
  +-- Adversarial Proofreader & Skeptic Gate (Mandatory Pre-Write QC):
        * In-Memory AST / Syntax Sanity Verification (python -m ast / node -c / pwsh)
        * Quoting & String Escaping Integrity Proof (Zero raw unescaped inline strings)
        * Invariant & Protocol Alignment Audit (5 Honest States, zero Any, no silent exceptions)
                           |
                           v
[Phase 3: Cyclic StateGraph Verification Engine] <---+
  +-- PostToolUse Multi-Language Static Gate:
  |     * Python: ruff check --fix (0 violations)
  |     * HTML/Inline JS: Node.js AST parser (node -c) (0 syntax errors)
  |     * PowerShell: PSScriptAnalyzer (0 findings)
  |     * TypeScript/JS: eslint + tsc --noEmit (0 diagnostics)
  +-- Code Simplifier & Complexity Pruner (Anti-Bloat Refactor)
  +-- Isolated Sandbox Test Runner (Pytest tmp_path / Deterministic)
  +-- Playwright Headless UI Smoke Gate (pageerror=0, console.err=0)
  +-- verify-app End-to-End Integration Oracle
  +-- Adversarial Red-Team Critic (Concurrency Fuzzing)      |
  +-- Mandatory Q&Q Auditor (Protocol Compliance Audit Gate) |
                           | (Pass: 0 Defects) -------------+
                           v
[Phase 4: Living LTM Memory, Scorecard & Git Sync]
  +-- Mandatory Q&Q Auditor (Telemetry, Speedup & Ledger Logging)
  +-- Living Memory Updater (Extract [BM-] & project memory.md)
  +-- Version Control Synchronizer (Clean Atomic Git Commit & Push)
```

---

## 2. Autonomous Closed-Loop Engineering & Parallel Execution

### A. "Loop Engineering" Over Prompting
> *"I don't prompt anymore. I write loops that prompt the agents."* - Autonomous Closed-Loop

Instead of step-by-step human prompting, the Principal Architect launches **autonomous recursive loops**:
1. **Goal Formulation**: Define explicit exit criteria (e.g., 0 lint violations, 100% tests passing, 0 page errors).
2. **Autonomous Execution**: Subagent iterates freely, executing tools and inspecting outputs.
3. **Target-Coupled Verification Gate**: Post-execution hooks and test runners evaluate the *exact* modified runtime surface.
4. **Self-Correction Feedback**: On failure, raw compiler/runtime stderr is automatically fed back to the subagent to fix the issue without human intervention.

### B. The 5 Closed-Loop Invariants (Mandatory Across All Variations)

All workforce execution modes (/orchestrate, /orchestrate uncapped, /orchestrate external providers, /orchestrate uncapped external providers) strictly enforce these 5 Closed-Loop Invariants:

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

### C. Universal Dynamic Host Profiling, Multi-Processing & Multi-Threading
The workforce uses a **Hybrid Concurrency Architecture** tailored to task characteristics:
1. **Multi-Processing (`ProcessPoolExecutor`) for CPU-Bound Work**:
   - For CPU-heavy tasks (AST parsing, Python compiling, cryptographic hashing, dataset parsing).
   - **The 50% CPU Half-Core Rule (Standard Mode)**: Strictly allocate `logical_cores // 2` (max 6 workers on 12 threads) to keep 50% of CPU cores permanently free for Windows, browser, and IDE.
   - **IDLE Priority Guard**: All child workers initialize with `IDLE_PRIORITY_CLASS` and `IOPRIO_VERYLOW` to prevent desktop micro-stutter.
   - **Deterministic Reaper**: Registers `atexit` handlers to unconditionally kill all child PIDs on exit.
2. **Multi-Threading (`ThreadPoolExecutor`) for I/O-Bound Work**:
   - For high-concurrency I/O (Git worktree checkouts, fast directory stat passes, external provider CLI streaming, network HTTP calls).
   - Scales up to `min(32, logical_cores * 4)` threads with low overhead and shared in-memory state.
   - Enforces 60-second execution caps and automatic shutdown handlers.

3. **Workforce Concurrency & Provider Mode Variations**:
   - **Supported Command Variations**:
     * `/orchestrate <task>`: Standard Native Workforce (50% CPU half-core ceiling, active identity slots into all worker roles).
     * `/orchestrate uncapped <task>` (or `/orchestrate-uncapped`): Uncapped Native Workforce (Throttleless execution, elastic worker scaling up to 100% cores governed by DynamicPressureGauge).
     * `/orchestrate external providers <task>` (or `/orchestrate-external`): Standard External Provider Swarm (50% CPU core ceiling, 2-provider pair Claude Opus + OpenAI Codex in isolated Git worktrees).
     * `/orchestrate uncapped external providers <task>` (or `/orchestrate-uncapped-providers`): Uncapped 4-Frontier Swarm (Elastic scaling up to 8 worktrees across Claude Opus, OpenAI Codex, Kimi K3, and Gemini Flash simultaneously).
     * CLI: `titanfold orchestrate "<task>" [--uncapped] [--external-providers]` or `titanfold workforce [uncapped]`.
   - **Intermittent Real-Time Pressure Gauge**:
     * Continuously samples CPU utilization, commit charge, and free RAM every 30-50ms during batch bursts.
     * **Green Zone** (CPU < 80%, Free RAM > 3GB): Dynamically bursts worker concurrency up to 100% of logical cores (12 workers).
     * **Yellow Zone** (CPU 80-92%): Dynamically holds at 50% half-core capacity.
     * **Red Zone** (CPU > 92%, Free RAM < 1.5GB): Automatically and instantly sheds worker load, elastically stepping down to safe minimum floors to eliminate any host lockup.




### C. Agentic Tool-Based Retrieval Over Monolithic RAG
Traditional Vector RAG and broad document dumping saturate context windows, leading to attention dilution on large files. The workforce strictly enforces **Agentic Tool-Based Retrieval**:
- `grep_search` and AST call graphs identify exact line numbers and symbol usages.
- `view_file` loads precision line slices rather than monolithic file dumps.
- Subagent context remains lightweight, high-entropy, and focused on target subsystems.

### D. Parallel Git Worktree Isolation & Universal Mandate (BM-INV-028)
To prevent file collision, lock contention, and dirty state corruption across concurrent agents:
- **Universal Worktree Mandate**: All autonomous development, refactoring, self-repair, and feature synthesis across ALL fleet AI orchestrators (Gemini, Claude Code, OpenAI Codex, Kimi), Pulselet dynamic workforces, and DevAgentZero lineages (`devagentzero.v2`, `devagentzero.v4`) must execute strictly within dedicated, isolated Git worktrees (`git worktree add`, `Workspace: 'share'` or `Workspace: 'branch'`).
- **Zero Direct Live-Root Mutation**: In-place mutation of the primary running service checkout is strictly prohibited.
- **Pulselet Dynamic Workforces**: When Pulselet develops using workforces, she does not force static identity personas (Doctor, Mentor, ElectricHulk) into coding tasks. Instead, she dynamically instantiates **replications of herself (self-clones)** or **external provider-backed worker agents (Claude, Codex, Gemini, Kimi)** across isolated worktrees.
- Multiple subagents work concurrently across distinct sub-systems in parallel branches/worktrees before atomic merge.

### E. The `code-simplifier` Agent Pass
AI-generated code often exhibits unnecessary verbosity and defensive bloat. After implementation passes tests, dispatch a specialized `Code Simplifier & Complexity Pruner` subagent:
- Strips redundant helper functions and dead imports.
- Simplifies nested conditional branches.
- Preserves 100% behavioral equivalence while maximizing readability and minimalism.

### F. Multi-Provider CLI Workforce Bridge (Claude Code, OpenAI Codex, Kimi Code, Google Antigravity)

To maximize throughput, exploit token capacity across all available providers, and leverage specialized frontier capabilities, the Principal Architect dispatches background worker tasks to alternate CLI assistants via host terminal commands.

#### 1. Canonical Host Execution Commands (Highest Model Tier & Max Reasoning Effort)

- **Claude Code (Anthropic Frontier)**:
  ```bash
  cmd.exe /c claude --model "claude-opus-5[1m]" --effort ultracode --permission-mode bypassPermissions -p "<prompt>"
  ```
  - **Model**: `claude-opus-5[1m]` (Opus 1M Context Window / 64K Extended Thinking)
  - **Reasoning Effort**: `ultracode` (Highest cognitive budget)
  - **Autonomous Execution**: `--permission-mode bypassPermissions` (Bypasses interactive permission prompts for non-blocking worker execution)
  - **Specialty**: Deep architectural refactoring, neurosurgery, complex diagnostics, and comprehensive codebase modifications.

- **OpenAI Codex (OpenAI Frontier)**:
  ```bash
  codex -m gpt-5.6-sol -c model_reasoning_effort="ultra" -p "<prompt>"
  ```
  - **Model**: `gpt-5.6-sol` (OpenAI Codex 5.6 Sol / Frontier Automation Tier)
  - **Reasoning Effort**: `model_reasoning_effort="ultra"` (Ultra reasoning effort)
  - **Specialty**: Formal verification, strict type invariants, AST syntax auditing, and deterministic contract checking.

- **Kimi Code (Moonshot AI Frontier)**:
  ```bash
  kimi --model k3 --reasoning-effort max -p "<prompt>"
  ```
  - **Model**: `k3` (Kimi K3 Max / 2 Million Token Context Window)
  - **Reasoning Effort**: `max` (Maximum cognitive thinking effort)
  - **Specialty**: Massive repository synthesis, cross-codebase refactoring, large document indexing, and high-entropy problem solving.

- **Google Antigravity (Cyclic StateGraph)**:
  ```bash
  agy --model gemini-3.7-flash --deep-thought --sandbox -p "<prompt>"
  ```
  - **Specialty**: Autonomous multi-turn StateGraph execution, cyclic verification loops, MCP integrations, and git worktree coordination.

### G. Default 16-Role "Zero-Toil" Dream Team Taxonomy

By default, every workforce activation utilizes the **16-Role Zero-Toil Dream Team Taxonomy** (detailed in `references/ROLES_AND_TAXONOMY.md`). This architecture eliminates 100% of developer toil, friction, and context-switching:

1. **Principal Systems Architect**: Macro DAG decomposition and system boundary enforcement.
2. **API & Type Contract Author**: Strict Pydantic v2 / TypeScript schemas before code authoring.
3. **Distributed Systems & Core SWE**: High-throughput backend logic and concurrency engines.
4. **Database & Storage Specialist**: SQLite WAL transactions, indexing, and query optimization.
5. **Frontend Design Systems SWE**: Responsive Lit/React components and UI state bindings.
6. **Rapid Prototyper / Spike Dev**: Quick exploratory validation spikes in temporary branches.
7. **Developer Experience (DevEx) Engineer**: Sub-second hot reloads, build caching, and toolchain tuning.
8. **Workflow Automation Specialist**: Custom CLI macros, agent hooks, and automated scripts.
9. **SRE & Chaos Automation Engineer**: Self-healing loops, canary checks, and failure recovery.
10. **Adversarial QA Lead (SDET)**: Isolated `tmp_path` unit tests, property tests, and boundary fuzzing.
11. **Headless Browser E2E Specialist**: Playwright visual smoke testing and user journey verifications.
12. **Blue-Team Security Auditor**: AST SAST scanning, secret leak detection, and Law Zero guardrails.
13. **Performance & Profiling SWE**: Memory leak detection, flamegraphs, and latency optimization.
14. **Dedicated Code Simplifier**: Continuous anti-bloat refactoring and technical debt reduction.
15. **Living Documentation Scribe**: Synchronizing canon markdown, roadmaps, and telemetry scorecards.
16. **Developer Ergonomics Advocate**: Guarding focus blocks and streamlining inter-agent handoffs.

### H. Strict Topological Phase Ordering with Maximum Intra-Phase Parallelism

The workforce enforces a **hybrid execution pipeline**:
1. **Strict Topological Phase Ordering**:
   - **Phase 1 (Architecture & Contracts)** must pass before **Phase 2 (Implementation)** starts.
   - **Phase 2 (Implementation)** must finish before **Phase 3 (Adversarial QA & Security)** runs.
   - **Phase 3 (QA Gate)** must achieve 100% green pass before **Phase 4 (Code Simplifier)** refactors.
   - **Phase 4 (Simplification & Lint)** must pass before **Phase 5 (Merge & Release)** commits.
2. **Maximum Intra-Phase Parallelism**:
   - Within Phase 2: Backend, Frontend, and Database builders execute concurrently across distinct Git worktrees.
   - Within Phase 3: Unit QA, Security Auditor, and Headless Playwright run simultaneously in parallel.

### I. Dynamic Elastic Resource-Aware Queuing (`wait_for_capacity`)

When concurrent agents or test runners execute on resource-constrained host hardware:
- The orchestrator samples live CPU and RAM pressure via `DynamicPressureGauge` (`psutil`).
- **Zone Green** (CPU < 80%, Free RAM > 3.0 GB): Dynamically bursts to full logical core capacity (12 workers / 8 worktrees).
- **Zone Yellow** (CPU 80-92%, Free RAM 1.5 - 3.0 GB): Holds steady at 50% half-core capacity.
- **Zone Red** (CPU > 92%, Free RAM < 1.5 GB): Active workers finish, but queued parallel workers automatically enter `wait_for_capacity()`, pausing and yielding in the background until memory and CPU clear before resuming. This eliminates out-of-memory (OOM) crashes and desktop lockups.

---

#### 2. Proven Successful Patterns for Multi-Provider Agent Workforces

1. **Dedicated Dispatch Engine (`provider_workforce_dispatcher.py`)**:
   - Executes parallel batch prompts concurrently across `claude.exe -p`, `codex.ps1`, and `kimi.exe run`.
   - Enforces 120s timeout guards, captures stdout/stderr, and returns structured synthesis JSON.

2. **Asynchronous Parallel Workforce Dispatch (`run_command` + Background Task Reactive Notification)**:
   - Dispatch distinct specialized jobs to external provider CLIs in non-blocking background mode (`WaitMsBeforeAsync=500-2000`).
   - The Lead Orchestrator continues parallel work while tasks execute asynchronously.
   - Outputs are captured upon task completion, synthesized into the StateGraph, and cross-verified without stalling the UI.

3. **Dedicated Git Worktree Isolation (`Workspace: 'share'` / `Workspace: 'branch'`)**:
   - Universal Mandate: Each provider worker runs strictly inside an isolated Git worktree branch (`git worktree add`).
   - Prevents write collisions, file lock contention, and dirty checkout corruption across concurrent CLI runs.

4. **Autonomous Closed-Loop Engineering & Automated Self-Correction**:
   - When a provider worker's code mutation fails a static linter, Vitest unit test, or Playwright smoke test, the orchestrator pipes the raw compiler/test stderr back to the provider in a follow-up prompt:
     `claude -p "Fix the following Vitest failure in <target_file>: <stderr>"`
   - The worker iterates autonomously until all deterministic gates turn green.

5. **One-Shot CLI Execution with Non-Interactive Pipelining**:
   - Always supply prompts via `-p "<prompt>"` or redirect stdin (`< /dev/null`) to avoid TUI interactive prompts.
   - Use `--output-format stream-json` or `--verbose` where available for structured streaming output capture.

6. **Standard Dispatch Envelope**:
   - Every prompt sent to an external provider must include the Standard Preamble:
     *"Read and strictly adhere to CODE-QUALITY.md, scoped memory.md, and PROJECT_OUTLINE.md. Plain ASCII only, 0 emojis, 300 LOC atomic mutation budget. Report your verified Five Honest States rung [BUILT -> WIRED -> EXERCISED -> VALIDATED -> PROVEN]."*

7. **Two-Pass Code Simplification (The `code-simplifier` Pass)**:
   - After an external provider (e.g. Claude or Kimi) writes an initial implementation, dispatch a lightweight simplification worker to strip AI bloat, deduplicate helpers, and enforce David Beazley-grade minimalism while keeping all tests passing.

### G. Agentic Invariant & Exemplar RAG (Targeted Context Grounding)
To achieve zero-defect execution without context window saturation, the workforce incorporates precision RAG:
1. **Pre-Flight Invariant Retrieval**: Dynamically indexes `builder_memory.md` and `memory.md` to extract only the 2-3 relevant platform/runtime constraints (`[BM-]` tags, SQLite WAL locks, Provider Seal lists, coordinate transforms) matching the worker's target subsystem.
2. **AST Blast-Radius Analysis**: Semantic dependency indexing retrieves upstream callers and downstream consumers before any export is modified.
3. **Dynamic Few-Shot Exemplar Selection**: Extracts the closest matching prior clean implementations and isolated `tmp_path` unit test patterns to prime worker agents.
4. **Adversarial Red-Team Bug Fuzzing**: Queries historical failure modes and bug categories (`docs/BUGS.md`, crash triage logs) to generate automated boundary stress tests for new features.

### H. Mandatory Project Vision & Codebase Reconnaissance Gate (`PROJECT_OUTLINE.md`)
Subagents must NEVER begin coding blindly, guess system architecture, or invent redundant mechanisms.
1. **Vision Verification**: Before executing any code mutations, the Principal Architect verifies `<project_root>/PROJECT_OUTLINE.md`.
2. **Auto-Reconnaissance on Drift**: If `PROJECT_OUTLINE.md` is missing or out-of-sync with disk, immediately dispatch an automated **Codebase Reconnaissance Workforce** (`Codebase Archaeologist` / AST scanner) to map all models, endpoints, state stores, background workers, and invariants before planning.
3. **Worker Grounding**: Every dispatched implementation subagent must ingest the relevant architectural slice from `PROJECT_OUTLINE.md` to prevent duplicate implementations, broken imports, and cascading silent failures.

### I. Dynamic Resource-Aware Test Tiering & Adaptive Escalation (BM-PAT-010)
To maximize verification velocity while protecting 16GB host memory from thrashing:
1. **Pre-Flight Resource Survey**: Before running tests, survey host Free RAM and active process count.
2. **Adaptive 3-Tier Execution**:
   - **Tier 1 (Lite / Targeted)**: Single test file, `vitest related`, or `--changed` with `<= 2 workers` (<250 MB RAM, <2s). Default for rapid iterative dev loops in Git worktrees.
   - **Tier 2 (Medium / Subsystem)**: Subsystem directory suite with `<= 4 workers` (~600 MB RAM, ~5-10s) for multi-file refactors.
   - **Tier 3 (Full Monty / Monolithic)**: Full repository regression on explicit request or PR merge gates. Requires Host Free RAM > 5.0 GB and 0 competing heavy workers.
3. **Adaptive Timeout & Sharding**: If a Tier 1 targeted run exceeds a soft timeout (>15s), the orchestrator cancels it and escalates via re-dispatch or deterministic sharding (`--shard=1/2`, `--shard=2/2`). In-flight process worker injection is non-viable and strictly prohibited.

---

### J. Mandatory Subagent Dispatch Prompt Envelope
Every subagent dispatch prompt (whether via `invoke_subagent`, `define_subagent`, or external CLI worker) MUST wrap its task description in the Standard Dispatch Envelope:
1. **Preamble**: "Read and strictly adhere to CODE-QUALITY.md, scoped memory.md, and PROJECT_OUTLINE.md before editing code."
2. **Hard Constraints**: Plain ASCII only, 300 LOC atomic mutation budget, isolated `tmp_path` unit tests, multi-language AST pre-flight gate.
3. **Closing Declaration**: Require the subagent to report its verified Five Honest States rung: `[BUILT -> WIRED -> EXERCISED -> VALIDATED -> PROVEN]`.

---

### K. Mandatory Lightweight Q&Q Auditor Agent (`qq_workforce_auditor.py`)
The Quantitative & Qualitative (Q&Q) Auditor is a **mandatory lightweight agent node** that runs automatically during every dev cycle:
1. **Phase 0 Contract & Pressure Test**: Executes a <200ms pre-flight test across all companion scripts and captures baseline host telemetry.
2. **Phase 3 Protocol Verification**: Audits whether worktrees were used, linters ran clean, 0 emojis were emitted, tests passed in `tmp_path`, and simplification occurred.
3. **Phase 4 Telemetry & Ledger Logging**: Calculates wall-clock runtime, speedup multiplier (e.g. `4.6x`), LOC simplification ratio, computes the final letter grade (`A+`, `A`, etc.), appends to `telemetry/workforce_audit_ledger.json`, and injects the scorecard into the final report.

---

### L. Mandatory Multi-Agent QC Layering & Adversarial Proofreader Gate (BM-PAT-012)
Charging ahead with direct file writes without dedicated proofreader validation is strictly prohibited. Every mutation cycle enforces a strict **3-Tier QC Pipeline**:
1. **Tier 1 (Implementer)**: Authors the isolated, minimal code diff (<=300 LOC).
2. **Tier 2 (Adversarial Skeptic & Proofreader Pre-Flight Gate)**:
   - **In-Memory AST / Syntax Validation**: Runs AST parsing (`python -m ast`, `node -c`, `pwsh -Parser`) on code *before* applying to disk.
   - **Quoting & Escaping Proof**: Prohibits raw nested multi-line string injections inside PowerShell/Bash commands; requires clean file writes or base64 decoding.
   - **Protocol & Invariant Audit**: Verifies 0 `Any` types, 0 emojis, 0 silent empty exception blocks, Pydantic v2 adherence, and The Five Honest States contract.
   - **Zero-Mock-Stub Audit (BM-INV-033)**: Strictly audits for and rejects any heuristic keyword string triggers (`if 'hi' in text`), try/except demo fallbacks, or circular test assertions on mock strings. Demands genuine live execution with honest unmasked error raising.
3. **Tier 3 (QA & Runtime Test Gate)**:
   - Automated deterministic test runner (`pytest` in isolated `tmp_path`, `PSScriptAnalyzer`).
   - Verifies runtime behavior against live system artifacts.

---

## 3. The 16-Agent Taxonomy Matrix

| Track | Role | Primary Responsibility |
| :--- | :--- | :--- |
| **Orchestration** | `Principal Systems Architect` | StateGraph coordinator, loop engineer, token budgeter, HITL checkpoint guardian. |
| **Recon & Spec** | `Codebase Archaeologist` | In-place `os.walk` AST parsing, dependency mapping, call graphs. |
| | `Threat Modeler & Invariant Guardian` | Blue Team integrity, SOC 2 CC7.2 rules, Win32 mutex contracts. |
| | `Contract Oracle` | Author of executable Pydantic v2 contracts and `tmp_path` fixtures. |
| **Implementation** | `Core Systems & Kernel Engineer` | Backend APIs, `threading.Lock`, atomic transactions (`BEGIN IMMEDIATE`). |
| | `Security Containment Specialist` | `NtSuspendProcess`, memory preservation, quarantine vaults. |
| | `Frontend Console Craftsman` | Dense `.table-wrap` box containment, plain ASCII, single-tooltip UI. |
| **Refinement** | `Code Simplifier & Complexity Pruner` | Eliminates AI bloat, deduplicates logic, enforces elegance without breaking tests. |
| **Verification** | `Multi-Language AST Gatekeeper` | Multi-language static validation (`ruff`, `node -c` on HTML scripts, `PSScriptAnalyzer`). |
| | `Isolated Sandbox Test Engineer` | Deterministic QA runner in isolated temporary directories (`tmp_path`). |
| | `Playwright UI Smoke Oracle` | Headless browser execution asserting `pageerror == 0` and `console.error == 0`. |
| | `verify-app End-to-End Oracle` | Simulates live operator journeys, verifies REST/SSE telemetry and HTTP 200 responses. |
| | `Adversarial Red-Team Critic` | Multi-threaded fuzzing, race-condition detection, hash-fork hunting. |
| **Evolution** | `Memory & Git Sync Guardian` | Extract `[BM-]` invariants, update project memory, push GitHub milestones. |
| **Liveness Guard** | `Workforce Watchdog & Zombie Sentinel` | Monitors worker executables for hangs (0% CPU / stdin block), enforces completion alerts, prunes zombie processes. |
| **Observability** | `Q&Q Auditor & Telemetry Sentinel` | Mandatory lightweight agent auditing protocol compliance, speedup metrics, and longitudinal scorecards. |

---

## 4. Architectural Invariants for Workforce Subagents

All subagents operating under this skill MUST uphold these engineering standards:
1. **Plain ASCII Mandate**: Absolute ZERO emojis across code, scripts, comments, terminal logs, markdown, PRs, and chat.
2. **Strict Type Safety**: Python 3.11+, Pydantic v2 only, zero `Any`, strict type hints on all function signatures.
3. **Multi-Language AST Pre-Flight**: Any edited file must pass its language-specific AST syntax validator before tests run.
4. **Playwright UI Smoke Standard**: Any modified HTML or frontend JS must pass automated headless browser smoke verification.
5. **Isolated Test Harness**: All test databases and filesystem operations must use temporary isolated directory fixtures (`tmp_path`). Never mutate live databases during test runs.
6. **Dense Table Box Containment**: Any web console table modification must enforce `.table-wrap` (`width:100%!important; max-width:100%!important; overflow-x:auto!important; box-sizing:border-box!important;`), exact column min-width parity, and cell text ellipsis.
7. **Thread & Process Mutual Exclusion**: Shared state and SQLite transaction stores must use `threading.Lock()` and atomic write transactions (`BEGIN IMMEDIATE`) to prevent hash forks.
8. **Living Memory Update Rule**: Whenever a correction or architectural invariant is identified, immediately record it in `builder_memory.md` or `memory.md` so the fleet never repeats a mistake.
9. **Five Honest States Rung Declaration**: Never claim a higher rung than observed. Dispatched subagents and reports must explicitly vocalize the exact achieved verification rung: `[BUILT -> WIRED -> EXERCISED -> VALIDATED (Unit Test & Live Playtest) -> PROVEN (Full Regression & Hashes)]`.
10. **Atomic Mutation Budget**: Single contiguous edit diffs must not exceed 300 LOC. Decompose larger features across parallel Git worktree subagents to maintain high attention density and prevent token bloat.
11. **Immediate Eager Subagent Teardown & Zero-Zombie Law (BM-INV-022)**:
    - **Eager Per-Agent Teardown**: As soon as any subagent, background task, or worker process finishes its assigned task and has no further active function, the Orchestrator must IMMEDIATELY terminate it (`manage_subagents(Action: 'kill', ConversationIds: [id])` or `manage_task(Action: 'kill')`) and release its RAM, CPU threads, and worktree locks on the spot. Subagents, shell pipes, and test workers must NEVER linger idle or become phantom zombies in the task tracker.
    - **Liveness Notification & Ghost Reaper**: All dispatched background tasks and CLI worker processes (`claude.exe`, `codex.exe`, `kimi.exe`, `node.exe`, `python.exe`) must emit an explicit completion notification upon finish or error. The Watchdog proactively sweeps `manage_task(Action: 'list')` to detect and terminate 0% CPU ghost handles.
    - **Phase 4 Teardown Sweep**: Upon receiving all results and before emitting the final report, the Orchestrator MUST unconditionally execute `manage_subagents(Action: 'kill_all')`, check `manage_task(Action: 'list')` to kill any lingering background command tasks, and verify zero active background tasks/subagents remain to guarantee zero orphan processes occupy host memory.
12. **Dynamic Elastic Hardware Scaling & Lowest Fallback Floor (BM-PAT-023)**: Heavy workers and test suites dynamically scale with available host RAM and CPU load (bursting up to full logical cores in Zone Green). Only under critically slim resources (<1.5GB free RAM or >92% CPU) does the orchestrator throttle down to the **2-worker absolute lowest fallback floor** (never drops below 2). Queued tasks wait in the background via `wait_for_capacity()` and auto-resume the moment capacity frees up.
13. **Zero Startup Test Execution (BM-INV-027)**: Session startup must strictly load and audit canon without firing background regression test suites or Vitest runs. Test suites run strictly on-demand during active dev cycles or PR gates.
14. **Universal Worktree Isolation Mandate (BM-INV-028)**: All autonomous dev, self-repair, and feature synthesis across all fleet AIs, Pulselet dynamic workforces, and DevAgentZero lineages (v2/v4) must execute strictly within dedicated Git worktrees. Direct in-place mutation of live running service roots is prohibited.
15. **Mandatory Final Output Report & Spelled-Out 5-Phase Architecture Diagram (BM-PAT-011)**: Every AI operating or orchestrating under this skill MUST format its final completion report using this exact 5-section standard:
    1. `### Elite Workforce Orchestration: <Title>` (Executive summary sentence)
    2. `### Workforce Execution Breakdown` (Itemized roles for Orchestrator and Worker models)
    3. `### Key Capabilities Implemented` (Per-layer architectural breakdown of all modified systems)
    4. `### 5-Phase Workforce Architecture & Execution Diagram` (Fully spelled-out plain ASCII lifecycle diagram detailing Phase 0 through Phase 4 boxes, specific Job titles, exact LLM model names, file paths, test case results, build times, and success percentages on all connecting lines)
    5. `### Verification & Testing` (Unit tests, AST syntax check, compiler build, live endpoint verification)
16. **Real-Time Operator Heartbeat & Subagent Milestone Streaming (BM-PAT-027)**: Whenever background subagents, builds, or test suites are dispatched, the Lead Orchestrator MUST emit concise, live status updates to the operator as phases transition (e.g. Planning -> Subagent Launch -> Archaeology Sync -> Backend Compiling -> Frontend Assembling -> E2E Probing). Prevents operator black-box blindness and maintains continuous trust without multi-minute radio silence.

---

## 5. Detailed References

For deep dive manuals and theoretical foundations, consult:
- [Agent Roles & Taxonomy Reference](references/ROLES_AND_TAXONOMY.md)
- [Graph Engineering & Looping Architecture](references/GRAPH_ENGINEERING_AND_LOOPS.md)
- [Swarm Director Playbook](references/SWARM_DIRECTOR_PLAYBOOK.md)
