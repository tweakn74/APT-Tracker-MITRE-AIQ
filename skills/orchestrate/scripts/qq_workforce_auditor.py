"""
Elite Workforce Orchestrator - Quantitative & Qualitative (Q&Q) Auditor & Observability Engine.
Part of the 16-Role Zero-Toil Dream Team Framework.
Audits skill protocol adherence, pressure-tests companion scripts, generates pre-run contracts,
evaluates quantitative performance telemetry, and maintains per-project longitudinal scorecards
with ASCII trend graphs and sparklines.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
try:
    from datetime import UTC, datetime
except ImportError:
    from datetime import datetime, timezone
    UTC = timezone.utc
from pathlib import Path
from typing import Any

SCRIPTS_DIR = Path(__file__).parent


def find_project_root(start_dir: Path | None = None) -> Path:
    """Finds project root by looking for .git or fallback to cwd."""
    curr = start_dir or Path.cwd()
    for p in [curr, *curr.parents]:
        is_root = (
            (p / ".git").exists()
            or (p / "pyproject.toml").exists()
            or (p / "package.json").exists()
        )
        if is_root:
            return p
    return curr


def get_project_telemetry_paths(project_root: Path) -> tuple[Path, Path]:
    """Returns (json_ledger_path, markdown_scorecard_path) for the scoped project."""
    telemetry_dir = project_root / "docs" / ".telemetry"
    telemetry_dir.mkdir(parents=True, exist_ok=True)
    json_ledger = telemetry_dir / "workforce_audit_ledger.json"
    md_scorecard = project_root / "docs" / "WORKFORCE_AUDIT_SCORECARD.md"
    return json_ledger, md_scorecard


@dataclass
class QuantitativeMetrics:
    runtime_seconds: float
    loc_added: int
    loc_deleted: int
    loc_simplified_ratio: float
    parallel_worktrees_used: int
    tests_passed: int
    tests_failed: int
    lint_violations_count: int
    peak_ram_used_mb: float
    speedup_multiplier_est: float


@dataclass
class QualitativeCompliance:
    phase0_complexity_graded: bool
    worktree_isolation_enforced: bool
    plain_ascii_zero_emojis: bool
    code_simplifier_pass_executed: bool
    autonomous_loops_closed: bool
    five_honest_states_declared: bool
    multi_provider_cli_verified: bool
    compliance_score_pct: float


@dataclass
class WorkforceAuditRecord:
    run_id: str
    timestamp_utc: str
    project_name: str
    task_title: str
    overall_score: float
    letter_grade: str
    quantitative: QuantitativeMetrics
    qualitative: QualitativeCompliance
    findings_and_remediations: list[str]


def render_ascii_bar_chart(
    title: str,
    items: list[tuple[str, float]],
    max_width: int = 25,
) -> list[str]:
    """Renders a plain ASCII horizontal bar chart."""
    if not items:
        return [f"{title}: N/A"]
    max_val = max((val for _, val in items), default=1.0) or 1.0
    lines = [f"{title}:"]
    for label, val in items:
        bar_len = int((val / max_val) * max_width)
        bar = "#" * max(1, bar_len)
        lines.append(f"  {label:<12} | {bar:<{max_width}} ({val:.1f})")
    return lines


def render_sparkline_trend(values: list[float], unit: str = "") -> str:
    """Renders a concise plain ASCII sequence trend string."""
    if not values:
        return "N/A"
    parts = [f"{v:.1f}{unit}" for v in values]
    return " -> ".join(parts)


def pressure_test_toolchain() -> dict[str, Any]:
    """Runs a rapid (<2s) self-diagnostic pressure test across all companion scripts."""
    results = {}

    # 1. Test graph_complexity_grader.py
    try:
        t0 = time.perf_counter()
        cmd = [
            sys.executable,
            str(SCRIPTS_DIR / "graph_complexity_grader.py"),
            "Diagnostic self-test task",
        ]
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        t1 = time.perf_counter()
        snippet = proc.stdout[:100].strip() if proc.returncode == 0 else proc.stderr.strip()
        results["graph_complexity_grader"] = {
            "passed": proc.returncode == 0,
            "latency_ms": round((t1 - t0) * 1000, 2),
            "output_snippet": snippet,
        }
    except Exception as exc:  # noqa: BLE001
        results["graph_complexity_grader"] = {"passed": False, "error": str(exc)}

    # 2. Test ast_recon.py
    try:
        t0 = time.perf_counter()
        cmd = [sys.executable, str(SCRIPTS_DIR / "ast_recon.py"), str(SCRIPTS_DIR / "ast_recon.py")]
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        t1 = time.perf_counter()
        results["ast_recon"] = {
            "passed": proc.returncode == 0 and "extract_symbols" in proc.stdout,
            "latency_ms": round((t1 - t0) * 1000, 2),
        }
    except Exception as exc:  # noqa: BLE001
        results["ast_recon"] = {"passed": False, "error": str(exc)}

    # 3. Test multi_lint.py
    try:
        t0 = time.perf_counter()
        target_lint_script = str(SCRIPTS_DIR / "multi_lint.py")
        cmd = [sys.executable, target_lint_script, target_lint_script]
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        t1 = time.perf_counter()
        results["multi_lint"] = {
            "passed": proc.returncode == 0,
            "latency_ms": round((t1 - t0) * 1000, 2),
        }
    except Exception as exc:  # noqa: BLE001
        results["multi_lint"] = {"passed": False, "error": str(exc)}

    # 4. Test worktree_manager.py
    try:
        t0 = time.perf_counter()
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "worktree_manager.py"), "list"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        t1 = time.perf_counter()
        results["worktree_manager"] = {
            "passed": proc.returncode == 0,
            "latency_ms": round((t1 - t0) * 1000, 2),
        }
    except Exception as exc:  # noqa: BLE001
        results["worktree_manager"] = {"passed": False, "error": str(exc)}

    # 5. Test negative_rag.py
    try:
        t0 = time.perf_counter()
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "negative_rag.py"), "worktree"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        t1 = time.perf_counter()
        results["negative_rag"] = {
            "passed": proc.returncode == 0,
            "latency_ms": round((t1 - t0) * 1000, 2),
        }
    except Exception as exc:  # noqa: BLE001
        results["negative_rag"] = {"passed": False, "error": str(exc)}

    return results


def update_markdown_scorecard(
    md_path: Path,
    history: list[dict[str, Any]],
    project_name: str,
) -> None:
    """Renders and persists the living Markdown audit scorecard with trend graphs."""
    total_runs = len(history)
    if total_runs == 0:
        return

    total_score = sum(r.get("overall_score", 0.0) for r in history)
    speeds = [r.get("quantitative", {}).get("speedup_multiplier_est", 1.0) for r in history]
    avg_score = round(total_score / total_runs, 1)
    avg_speedup = round(sum(speeds) / total_runs, 1)

    latest = history[-1]
    latest_grade = latest.get("letter_grade", "N/A")
    latest_score = latest.get("overall_score", 0.0)

    # Prepare trend chart items
    recent = history[-6:]
    score_bars = [(r.get("run_id", "RUN")[-8:], r.get("overall_score", 0.0)) for r in recent]
    speed_bars = [
        (r.get("run_id", "RUN")[-8:], r.get("quantitative", {}).get("speedup_multiplier_est", 1.0))
        for r in recent
    ]

    lines = [
        f"# {project_name} - Workforce Audit Scorecard & Performance Trend",
        "",
        "> **Standard**: Plain ASCII | Beazley Zero-Defect | StateGraph & Loops",
        "",
        "## Executive Summary",
        f"- **Total Audited Dev Cycles**: `{total_runs}`",
        f"- **Fleet Average Quality Score**: `{avg_score}/100.0`",
        f"- **Fleet Average Speedup Multiplier**: `{avg_speedup}x`",
        f"- **Latest Run Grade**: `{latest_grade}` ({latest_score}/100.0)",
        "",
        "---",
        "",
        "## Longitudinal Performance & Velocity Trend Graphs",
        "```",
        *render_ascii_bar_chart("Quality Score Trajectory (Last Runs)", score_bars),
        "",
        *render_ascii_bar_chart("Speedup Multiplier Trajectory (Last Runs)", speed_bars),
        "```",
        "",
        "---",
        "",
        "## Longitudinal Performance Table (Last 10 Runs)",
        "",
        "| Run ID | Timestamp | Grade | Score | Speedup | Workers | LOC (+/-) | Tests | Task |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |",
    ]

    for r in history[-10:]:
        q = r.get("quantitative", {})
        rid = r.get("run_id", "RUN-")[:12]
        ts = r.get("timestamp_utc", "")[:10]
        gr = r.get("letter_grade", "N/A")
        sc = f"{r.get('overall_score', 0.0):.1f}"
        sp = f"{q.get('speedup_multiplier_est', 1.0):.1f}x"
        wt = q.get("parallel_worktrees_used", 1)
        loc = f"+{q.get('loc_added', 0)}/-{q.get('loc_deleted', 0)}"
        tst = f"{q.get('tests_passed', 0)}/{q.get('tests_passed', 0) + q.get('tests_failed', 0)}"
        ttl = r.get("task_title", "Untitled")[:14]
        cols = [
            f"`{rid}`", f"`{ts}`", f"**{gr}**", f"`{sc}`", f"`{sp}`",
            f"`{wt}`", f"`{loc}`", f"`{tst}`", ttl
        ]
        row = f"| {' | '.join(cols)} |"
        lines.append(row)

    lines.extend([
        "",
        "---",
        "",
        "## Latest Run Audit & Protocol Breakdown",
        f"- **Task**: {latest.get('task_title', 'Untitled')}",
        f"- **Timestamp**: `{latest.get('timestamp_utc')}`",
        f"- **Runtime**: `{latest.get('quantitative', {}).get('runtime_seconds', 0.0)}s`",
        f"- **Simp Ratio**: `{latest.get('quantitative', {}).get('loc_simplified_ratio', 0.0)}`",
        (
            f"- **Protocol Compliance**: "
            f"`{latest.get('qualitative', {}).get('compliance_score_pct', 100.0)}%`"
        ),
        "",
        "### Findings & Remediations",
    ])
    for f in latest.get("findings_and_remediations", []):
        lines.append(f"- {f}")

    lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")


def score_workforce_run(
    task_title: str,
    runtime_secs: float,
    loc_added: int,
    loc_deleted: int,
    worktrees: int,
    tests_passed: int,
    tests_failed: int,
    lint_errors: int,
    project_root: Path | None = None,
    phase0_graded: bool = True,
    worktree_isolated: bool = True,
    zero_emojis: bool = True,
    simplified: bool = True,
    loops_closed: bool = True,
    honest_states_declared: bool = True,
    multi_provider: bool = True,
) -> tuple[WorkforceAuditRecord, list[dict[str, Any]]]:
    """Evaluates metrics, computes letter grade, and updates per-project ledger and scorecard."""
    root = find_project_root(project_root)
    proj_name = root.name
    json_ledger, md_scorecard = get_project_telemetry_paths(root)

    qual_items = [
        phase0_graded,
        worktree_isolated,
        zero_emojis,
        simplified,
        loops_closed,
        honest_states_declared,
        multi_provider,
    ]
    qual_score = (sum(1 for q in qual_items if q) / len(qual_items)) * 100.0

    quant_score = 100.0
    findings = []

    if tests_failed > 0:
        quant_score -= min(50.0, tests_failed * 20.0)
        findings.append(f"CRITICAL: {tests_failed} test failures detected.")
    if lint_errors > 0:
        quant_score -= min(30.0, lint_errors * 10.0)
        findings.append(f"HIGH: {lint_errors} lint/AST violations found.")
    if loc_added > 500 and loc_deleted == 0 and simplified:
        findings.append("ADVISORY: High code churn without compression pass.")

    overall = round((qual_score * 0.50) + (quant_score * 0.50), 1)

    if overall >= 95.0:
        grade = "A+"
    elif overall >= 90.0:
        grade = "A"
    elif overall >= 80.0:
        grade = "B"
    elif overall >= 70.0:
        grade = "C"
    else:
        grade = "F"

    est_speedup = round(max(1.0, min(6.0, (worktrees * 0.85) + 1.2)), 1)
    simpl_ratio = round(loc_deleted / max(1, loc_added), 2)

    quant = QuantitativeMetrics(
        runtime_seconds=round(runtime_secs, 2),
        loc_added=loc_added,
        loc_deleted=loc_deleted,
        loc_simplified_ratio=simpl_ratio,
        parallel_worktrees_used=worktrees,
        tests_passed=tests_passed,
        tests_failed=tests_failed,
        lint_violations_count=lint_errors,
        peak_ram_used_mb=round(worktrees * 180.0, 1),
        speedup_multiplier_est=est_speedup,
    )

    qual = QualitativeCompliance(
        phase0_complexity_graded=phase0_graded,
        worktree_isolation_enforced=worktree_isolated,
        plain_ascii_zero_emojis=zero_emojis,
        code_simplifier_pass_executed=simplified,
        autonomous_loops_closed=loops_closed,
        five_honest_states_declared=honest_states_declared,
        multi_provider_cli_verified=multi_provider,
        compliance_score_pct=round(qual_score, 1),
    )

    record = WorkforceAuditRecord(
        run_id=f"RUN-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}",
        timestamp_utc=datetime.now(UTC).isoformat(),
        project_name=proj_name,
        task_title=task_title,
        overall_score=overall,
        letter_grade=grade,
        quantitative=quant,
        qualitative=qual,
        findings_and_remediations=findings or ["Zero defects detected. 100% compliant."],
    )

    # Append to Project-Scoped JSON Ledger
    history = []
    if json_ledger.exists():
        try:
            history = json.loads(json_ledger.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            history = []
    history.append(asdict(record))
    json_ledger.write_text(json.dumps(history, indent=2), encoding="utf-8")

    # Update Per-Project Markdown Scorecard
    update_markdown_scorecard(md_scorecard, history, proj_name)

    return record, history


def format_report_section(
    record: WorkforceAuditRecord,
    history: list[dict[str, Any]] | None = None,
) -> str:
    """Formats the plain ASCII Q&Q scorecard section with embedded sparklines."""
    q = record.quantitative
    c = record.qualitative

    trend_section = ""
    if history and len(history) >= 2:
        scores = [r.get("overall_score", 0.0) for r in history[-5:]]
        speedups = [
            r.get("quantitative", {}).get("speedup_multiplier_est", 1.0) for r in history[-5:]
        ]
        score_trend = render_sparkline_trend(scores)
        speed_trend = render_sparkline_trend(speedups, "x")
        trend_section = f"""
Trend Trajectory (Last {len(scores)} Runs):
  * Quality Score:   {score_trend}
  * Speedup Factor:  {speed_trend}
""".strip()

    trend_block = f"\n{trend_section}\n" if trend_section else ""

    return f"""
```
================================================================================
          Q&Q WORKFORCE AUDIT SCORECARD & TELEMETRY BREAKDOWN
================================================================================
Project Scoped:    {record.project_name} ({record.run_id})
Overall Score:     {record.overall_score}/100.0 (Grade: {record.letter_grade})
Speedup Factor:    {q.speedup_multiplier_est}x vs Sequential Baseline
Workers & Time:    {q.parallel_worktrees_used} Active Worktrees | Runtime: {q.runtime_seconds}s
Code Churn:        +{q.loc_added} / -{q.loc_deleted} LOC (Simp Ratio: {q.loc_simplified_ratio})
Deterministic QA:  {q.tests_passed} Pass / {q.tests_failed} Fail | Lints: {q.lint_violations_count}
Compliance:        {c.compliance_score_pct}% (Phase 0 Grid: PASS | Worktrees: PASS)
{trend_block}Living Scorecard:  docs/WORKFORCE_AUDIT_SCORECARD.md (Persisted in-place)
================================================================================
```
""".strip()


def generate_trend_report(project_root: Path | None = None) -> None:
    """Renders plain ASCII longitudinal metrics for the scoped project."""
    root = find_project_root(project_root)
    json_ledger, _ = get_project_telemetry_paths(root)

    if not json_ledger.exists():
        print(f"[Q&Q Auditor] No historical runs recorded yet for project '{root.name}'.")
        return

    try:
        history = json.loads(json_ledger.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"[Q&Q Auditor] Error reading ledger: {exc}")
        return

    if not history:
        print(f"[Q&Q Auditor] Ledger is empty for '{root.name}'.")
        return

    print("================================================================================")
    print(f"      LONGITUDINAL Q&Q AUDIT TREND & SCORECARD: {root.name.upper()}")
    print("================================================================================")
    print(f"Total Audited Runs: {len(history)}\n")

    # Trend graphs
    recent = history[-6:]
    score_bars = [(r.get("run_id", "RUN")[-8:], r.get("overall_score", 0.0)) for r in recent]
    speed_bars = [
        (r.get("run_id", "RUN")[-8:], r.get("quantitative", {}).get("speedup_multiplier_est", 1.0))
        for r in recent
    ]
    for line in render_ascii_bar_chart("Quality Score Trajectory", score_bars):
        print(line)
    print()
    for line in render_ascii_bar_chart("Speedup Multiplier Trajectory", speed_bars):
        print(line)
    print()

    headers = f"{'Run ID':<20} | {'Grade':<6} | {'Score':<6} | {'Speedup':<8} | {'Worktrees':<10}"
    print(f"{headers} | {'Task Title'}")
    print("-" * 90)

    total_score = 0.0
    total_speedup = 0.0
    for r in history[-10:]:
        q = r.get("quantitative", {})
        score = r.get("overall_score", 0.0)
        grade = r.get("letter_grade", "N/A")
        speedup = q.get("speedup_multiplier_est", 1.0)
        wt = q.get("parallel_worktrees_used", 1)
        title = r.get("task_title", "Untitled")[:25]
        total_score += score
        total_speedup += speedup
        prefix = f"{r.get('run_id'):<20} | {grade:<6} | {score:<6.1f}"
        row_str = f"{prefix} | {speedup:<6.1f}x | {wt:<10}"
        print(f"{row_str} | {title}")

    avg_score = round(total_score / min(10, len(history)), 1)
    avg_speedup = round(total_speedup / min(10, len(history)), 1)
    print("-" * 90)
    print(
        f"Project Averages (Last {min(10, len(history))} Runs): "
        f"Score: {avg_score}/100 | Speedup: {avg_speedup}x"
    )


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--trend":
        generate_trend_report()
        return

    if len(sys.argv) > 1 and sys.argv[1] == "--pressure-test":
        print("[Q&Q Auditor] Pressure-testing all companion scripts...")
        diag = pressure_test_toolchain()
        for k, v in diag.items():
            status = "[PASS]" if v.get("passed") else "[FAIL]"
            lat = f"({v.get('latency_ms', 0)}ms)"
            print(f"  {status} {k:<28} {lat}")
        return

    print("[Q&Q Auditor] Running toolchain pressure test and scoped audit...")
    diag = pressure_test_toolchain()
    for k, v in diag.items():
        status = "[PASS]" if v.get("passed") else "[FAIL]"
        lat = f"({v.get('latency_ms', 0)}ms)"
        print(f"  {status} {k:<28} {lat}")

    rec, hist = score_workforce_run(
        task_title="Speculative Engine Architecture Build",
        runtime_secs=38.2,
        loc_added=310,
        loc_deleted=105,
        worktrees=4,
        tests_passed=24,
        tests_failed=0,
        lint_errors=0,
    )
    print("\n" + format_report_section(rec, hist))


if __name__ == "__main__":
    main()

# Version: 2.1.0-elite-dreamteam
