"""Markdown diagnostic report for the scenario suite (AGE-333).

Three views, in the order a reader needs them:

  1. per-candidate  -- the pass/fail grid, one row per agent, one column per scenario
  2. per-scenario   -- population pass rate and the spread of the metric each verdict turned on
  3. fail analysis  -- every FAIL with the criterion that fired and the number behind it

    python3 evolve/run_scenarios.py --agent candidates/C1.py --md evolve/reports/scenarios.md
    python3 -c "import scenarios.report as r; print(r.render_from_db())"
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from registry import SUITE_VERSION, all_scenarios   # noqa: E402

MARK = {True: "PASS", False: "**FAIL**", None: "?"}


def _fmt(v):
    if v is None:
        return "-"
    if isinstance(v, float):
        return f"{v:,.2f}".rstrip("0").rstrip(".")
    return f"{v:,}" if isinstance(v, int) else str(v)


def _label(report):
    return Path(report["agent"]).stem + (f" ({report['key'][:8]})" if report.get("key") else "")


def render(reports, title="Adversarial diagnostic scenarios (AGE-333)"):
    scen = all_scenarios()
    by_name = {s.name: s for s in scen}
    order = [s.name for s in scen]
    out = [f"# {title}", ""]
    if not reports:
        return "\n".join(out + ["No scenario results.", ""])
    opp = reports[0].get("opponent") or "?"
    out += [f"Suite `{reports[0].get('suite_version', SUITE_VERSION)}` | opponent `{opp}` | "
            f"{len(reports)} agent(s) | diagnostic only -- these verdicts never enter cascade ranking.",
            ""]

    # ------------------------------------------------------------------ 1. per-candidate grid
    present = [n for n in order if any(r["scenario"] == n for rep in reports for r in rep["results"])]
    out += ["## Per-candidate", "",
            "| agent | " + " | ".join(present) + " | pass |",
            "|---|" + "---|" * (len(present) + 1)]
    for rep in reports:
        got = {r["scenario"]: r for r in rep["results"]}
        cells = [MARK[got[n]["passed"]] if n in got else "-" for n in present]
        out.append(f"| {_label(rep)} | " + " | ".join(cells)
                   + f" | {rep.get('n_pass', 0)}/{len(rep['results'])} |")
    out.append("")

    # ------------------------------------------------------------------ 2. per-scenario population
    out += ["## Per-scenario", ""]
    for name in present:
        sc = by_name.get(name)
        rows = [(rep, r) for rep in reports for r in rep["results"] if r["scenario"] == name]
        n_pass = sum(r["passed"] is True for _, r in rows)
        n_fail = sum(r["passed"] is False for _, r in rows)
        n_inc = sum(r["passed"] is None for _, r in rows)
        out += [f"### {name} -- {n_pass} pass / {n_fail} fail"
                + (f" / {n_inc} inconclusive" if n_inc else ""), ""]
        if sc:
            out += [f"*{sc.question}*", "", sc.description, ""]
            for c in sc.exempt_when:
                out.append(f"- PASS if `{c.metric} {c.op} {c.threshold}` -- {c.why}")
            for c in sc.fail_when:
                out.append(f"- FAIL if `{c.metric} {c.op} {c.threshold}` -- {c.why}")
            if sc.notes:
                out += ["", f"> Note: {sc.notes}"]
            out.append("")
        cols = list(dict.fromkeys([c.metric for c in (sc.exempt_when + sc.fail_when)] +
                                  list(sc.report_metrics))) if sc else []
        if cols:
            out += ["| agent | verdict | " + " | ".join(f"`{c}`" for c in cols) + " |",
                    "|---|---|" + "---|" * len(cols)]
            for rep, r in rows:
                vals = [_fmt(r["metrics"].get(c)) for c in cols]
                out.append(f"| {_label(rep)} | {MARK[r['passed']]} | " + " | ".join(vals) + " |")
            out.append("")

    # ------------------------------------------------------------------ 3. fail analysis
    fails = [(rep, r) for rep in reports for r in rep["results"] if r["passed"] is False]
    inc = [(rep, r) for rep in reports for r in rep["results"] if r["passed"] is None]
    out += ["## Fail analysis", ""]
    if not fails and not inc:
        out += ["Every agent passed every scenario it was run on.", ""]
    if fails:
        counts = {}
        for _, r in fails:
            counts[(r["scenario"], r["trigger"])] = counts.get((r["scenario"], r["trigger"]), 0) + 1
        out += ["Triggering metric, by frequency:", "",
                "| scenario | triggering metric | fails |", "|---|---|---|"]
        for (name, trig), n in sorted(counts.items(), key=lambda kv: -kv[1]):
            out.append(f"| {name} | `{trig}` | {n} |")
        out += ["", "Per fail:", ""]
        for rep, r in fails:
            out.append(f"- **{_label(rep)} / {r['scenario']}** -- {r['explanation']}")
        out.append("")
    if inc:
        out += ["Inconclusive (the agent raised inside the scenario world, so no verdict was taken):", ""]
        for rep, r in inc:
            out.append(f"- **{_label(rep)} / {r['scenario']}** -- {r['explanation']}")
        out.append("")
    return "\n".join(out)


def render_from_db(db_path=None, suite_version=SUITE_VERSION):
    """Render the report from whatever is already stored, without replaying any game."""
    import db as db_mod
    import store as store_mod
    db = db_mod.DB(db_path) if db_path else db_mod.DB()
    return render(store_mod.reports_from_rows(store_mod.population(db.conn, suite_version)))
