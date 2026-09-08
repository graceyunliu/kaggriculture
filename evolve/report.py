"""Morning report for an evolution run.

    python3 evolve/report.py [run_id]      # defaults to the latest run
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import space  # noqa: E402
from db import DB  # noqa: E402

REPORT_DIR = HERE / "reports"


def _fmt(v, money=True):
    if v is None:
        return "—"
    return f"{v:+,.0f}" if money else f"{v:.1f}"


def _params_dict(row):
    """Parse a candidate's stored params, tolerating legacy rows where params ended up
    double-JSON-encoded (e.g. a stray pre-existing row from an older loop.py build -- seen on
    m2_9e2d396b9d6e). Repairs the common one-extra-encoding case; returns None (never raises) for
    anything that still isn't a dict, so one bad row can't crash the whole report."""
    try:
        p = json.loads(row["params"])
    except (TypeError, ValueError):
        return None
    if isinstance(p, str):
        try:
            p = json.loads(p)
        except (TypeError, ValueError):
            return None
    return p if isinstance(p, dict) else None


def _grouped_failure_observations(rows):
    """Group recent dead candidates by failure_profile.primary_class.

    Returns a list of dicts with:
    - class: the failure class name (e.g. "EXECUTION_FAILURE")
    - n: number of candidates in this group
    - seeds: set of seeds these candidates were tested on
    - outcome: the observed outcome signature (from diagnosis/exec_summary)
    - param_ranges: parameter ranges observed in these candidates (correlation, not cause)
    - confidence: "low" / "moderate" / "high" based on n and seed diversity

    This is purely observational. A parameter appearing in param_ranges may be part
    of the failure mechanism, or it may be confounded by companion parameters, seeds,
    matchups, or RNG-path effects. Consumers must NOT treat these as 'avoid this range.'
    """
    from collections import defaultdict
    import json as _json

    groups = defaultdict(lambda: {"candidates": [], "seeds": set()})
    for r in rows:
        fp = r.get("failure_profile")
        if not fp or r.get("status") not in ("dead_smoke", "dead_pattern", "held_fail", "error"):
            continue
        try:
            fpd = _json.loads(fp) if isinstance(fp, str) else fp
        except (_json.JSONDecodeError, TypeError, ValueError):
            continue
        cls = fpd.get("primary_class", "UNKNOWN")
        groups[cls]["candidates"].append(r)

    out = []
    for cls, data in groups.items():
        n = len(data["candidates"])
        if n < 2:
            continue
        param_ranges = defaultdict(list)
        for r in data["candidates"]:
            p = _params_dict(r)
            if p is None:
                continue
            for k, v in p.items():
                if not isinstance(v, (int, float)):
                    continue
                param_ranges[k].append(v)
        range_strs = []
        for k, vals in sorted(param_ranges.items(), key=lambda kv: -len(kv[1]))[:8]:
            lo, hi = min(vals), max(vals)
            if lo == hi:
                range_strs.append(f"{k}={lo}")
            else:
                range_strs.append(f"{k}={lo}–{hi} (n={len(vals)})")
        diag = data["candidates"][0].get("diagnosis", "")
        exec_sum = data["candidates"][0].get("exec_summary")
        try:
            es = _json.loads(exec_sum) if isinstance(exec_sum, str) else {}
        except (_json.JSONDecodeError, TypeError, ValueError):
            es = {}
        outcome_parts = []
        if es.get("sales"):
            outcome_parts.append(f"sales={es['sales']:,}")
        if es.get("missed_water") is not None:
            outcome_parts.append(f"missed_water={es['missed_water']}")
        if es.get("idle_share") is not None:
            outcome_parts.append(f"idle_share={es['idle_share']:.2f}")
        outcome = "; ".join(outcome_parts) if outcome_parts else (diag[:200] if diag else "unknown")
        confidence = "low" if n < 5 else ("moderate" if n < 15 else "high")
        out.append({
            "class": cls,
            "n": n,
            "seeds": "multiple",
            "outcome": outcome,
            "param_ranges": "; ".join(range_strs) if range_strs else "none captured",
            "confidence": confidence,
        })
    out.sort(key=lambda x: -x["n"])
    return out


def param_exploration(rows, ref):
    """Observed outcome variation by parameter value, across all candidates with dev_margin.

    This is NOT causal importance or sensitivity. High spread may reflect:
    - interactions with other parameters (a value looks good only with certain companions)
    - seed/matchup variance (a value won in dominant matchups, lost in weak ones)
    - a few outlier candidates (one strong seed-fit candidate can move the mean)
    - selection bias (some values were only tested in weak candidate contexts)
    - parameters tested in more diverse contexts naturally show wider spread

    Consumers (especially the LLM proposer) should treat these as EXPLORATION WEIGHTS:
    "where has the search looked, and what was the observed range of outcomes?"
    not as "which parameters matter most."

    Each entry includes per-value sample counts so the consumer can judge reliability:
    - n >= 10 at a value: rough estimate, still confounded
    - n >= 30 at a value: moderate confidence in the mean
    - n < 5 at a value: do not over-interpret; could be noise or a single outlier

    The "balance" field flags values with very uneven sampling (one value tested 50x,
    another 3x) -- the apparent spread may just reflect the better-sampled value having
    more chances to find an outlier.
    """
    from collections import defaultdict
    by = defaultdict(lambda: defaultdict(list))
    for r in rows:
        if r.get("dev_margin") is None:
            continue
        p = _params_dict(r)
        if p is None:
            continue
        for k in space.SPACE:
            if k not in p:          # candidates rendered before the chassis gained this key
                continue
            v = p[k]
            by[k][v if not isinstance(v, (list, dict)) else str(v)].append(r["dev_margin"])
    out = []
    for k, vals in by.items():
        if len(vals) < 2:
            continue
        means = {v: sum(m) / len(m) for v, m in vals.items() if len(m) >= 2}
        if len(means) < 2:
            continue
        spread = max(means.values()) - min(means.values())
        best = max(means, key=means.get)
        counts = {str(v): len(vals[v]) for v in means}
        total = sum(counts.values())
        cnt_vals = list(counts.values())
        mean_cnt = sum(cnt_vals) / len(cnt_vals)
        balance = (max(cnt_vals) - mean_cnt) / mean_cnt if mean_cnt > 0 else 1.0
        out.append({
            "param": k,
            "spread": round(spread),
            "best_value": best,
            "best_mean": round(means[best]),
            "c1_value": ref.get(k),
            "c1_mean": round(means.get(str(ref.get(k)), float('nan')), 1) if str(ref.get(k)) in means else None,
            "means": {str(v): {"mean": round(m), "n": len(vals[v])} for v, m in sorted(means.items(), key=lambda x: -x[1])},
            "total_candidates": total,
            "n_values_tested": len(vals),
            "sampling_balance": round(balance, 2),
            "_note": "Observed outcome variation, NOT causal importance. Confounded by interactions, seed variance, selection bias, and outliers. Treat as exploration weight only."
        })
    out.sort(key=lambda x: -x["spread"])
    return out


def write_report(db, run_id):
    run = db.run(run_id) or {}
    cfg = json.loads(run["config"]) if run.get("config") else {}
    if cfg.get("base"):
        space.freeze_base(cfg["base"])
    rows = db.all(run_id)
    # population = every run on the same chassis snapshot (keys/scores are comparable only within a chassis)
    same = {r["run_id"] for r in db.conn.execute("SELECT run_id FROM runs WHERE k_sha=?", (run.get("k_sha"),))}
    all_rows = [r for r in db.all() if r["run_id"] in same]
    counts = db.counts(run_id)
    ref = space.base_params()
    c1 = space.c1_params()

    alive = [r for r in all_rows if r.get("dev_margin") is not None]
    alive.sort(key=lambda r: r["dev_margin"], reverse=True)
    held = [r for r in all_rows if r["status"] in ("held_pass", "held_fail")]
    held.sort(key=lambda r: (r["held_margin"] or -1e9), reverse=True)

    summary = json.loads(run["summary"]) if run.get("summary") else {}
    L = []
    L.append(f"# Evolution run {run_id}")
    L.append("")
    L.append(f"Frontier opponent: `{Path(run.get('frontier','?')).name}` · clone: `{Path(run.get('clone','?')).name}` · "
             f"engine sha `{run.get('engine_sha','?')}` · chassis snapshot `{Path(cfg.get('base','?')).name}` "
             f"(sha `{run.get('k_sha','?')}`)")
    if summary:
        L.append(f"Elapsed {summary.get('elapsed_s',0)/3600:.2f} h · candidates evaluated this run: {summary.get('evaluated',0)} · "
                 f"games {summary.get('games',0):,} ({summary.get('games_per_hour',0):,}/h)")
    L.append("")
    L.append("## Cascade counts (this run)")
    L.append("")
    L.append("| status | candidates | games |")
    L.append("|---|---:|---:|")
    for s in ("noop", "dead_pattern", "dead_smoke", "alive", "held_fail", "held_pass", "error"):
        n, g = counts.get(s, (0, 0))
        L.append(f"| {s} | {n} | {g} |")
    L.append("")
    L.append(f"Population (all runs, reached dev): {len(alive)} · held-out evaluated: {len(held)} · "
             f"held-out PASS: {sum(1 for r in held if r['status']=='held_pass')}")
    L.append("")

    # seeds as reference
    L.append("## Reference points")
    L.append("")
    L.append("| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for name, p in (("V3_12 (K defaults)", ref), ("C1", c1)):
        r = db.get(space.params_key(p))
        if r:
            L.append(f"| {name} | {_fmt(r['dev_margin'])} | {_fmt(r['dev_t'], False)} | {r['dev_wins']}-{r['dev_losses']} | "
                     f"{_fmt(r['clone_margin'])} | {_fmt(r['held_margin'])} | {_fmt(r['held_t'], False)} | "
                     f"{r['held_wins'] or '—'}-{r['held_losses'] or '—'} |")
    L.append("")

    L.append("## Held-out results (the only numbers that count)")
    L.append("")
    if held:
        L.append("| key | island | origin | held vs frontier | t | W-L | held vs clone | dev | changes vs C1 | ablation (loss if reverted) | diagnosis vs C1 |")
        L.append("|---|---|---|---:|---:|---:|---:|---:|---|---|---|")
        for r in held[:15]:
            p = _params_dict(r)
            d = space.diff(p, c1) if p is not None else {}
            ds = ", ".join(f"{k} {a}→{b}" for k, (a, b) in d.items()) if p is not None else "(malformed params row)"
            if r.get("blocks"):
                ds += " · blocks: " + ",".join(sorted(json.loads(r["blocks"])))
            ab = ""
            if r.get("ablation"):
                ab = ", ".join(f"{k} {v:+,}" if v is not None else f"{k} ?" for k, v in json.loads(r["ablation"]).items())
            L.append(f"| `{r['key']}` | {r.get('island','')} | {r['origin']} | **{_fmt(r['held_margin'])}** | {_fmt(r['held_t'], False)} | "
                     f"{r['held_wins']}-{r['held_losses']} | {_fmt(r['held_clone_margin'])} | {_fmt(r['dev_margin'])} | {ds} | {ab} | {(r.get('diagnosis') or '')[:200]} |")
    else:
        L.append("None reached held-out this run.")
    L.append("")

    L.append("## Top 15 by dev margin (selection score; may be seed-fit — trust held-out)")
    L.append("")
    L.append("| key | island | origin | dev | t | W-L | clone | status | changes vs C1 |")
    L.append("|---|---|---|---:|---:|---:|---:|---|---|")
    for r in alive[:15]:
        p = _params_dict(r)
        d = space.diff(p, c1) if p is not None else {}
        ds = ", ".join(f"{k} {a}→{b}" for k, (a, b) in d.items()) if p is not None else "(malformed params row)"
        if r.get("blocks"):
            ds += " · blocks: " + ",".join(sorted(json.loads(r["blocks"])))
        L.append(f"| `{r['key']}` | {r.get('island','')} | {r['origin']} | {_fmt(r['dev_margin'])} | {_fmt(r['dev_t'], False)} | "
                 f"{r['dev_wins']}-{r['dev_losses']} | {_fmt(r['clone_margin'])} | {r['status']} | {ds} |")
    L.append("")
    by_island = defaultdict(list)
    for r in alive:
        by_island[r.get("island") or "c1"].append(r)
    L.append("## Islands (best dev margin, population size)")
    L.append("")
    for name, lst in sorted(by_island.items()):
        L.append(f"- {name}: best {_fmt(lst[0]['dev_margin'])} (`{lst[0]['key']}`), n={len(lst)}")
    L.append("")

    L.append("## Where the signal is (observed outcome variation by parameter value, all runs)")
    L.append("")
    L.append("**These are exploration weights, NOT causal importance.** High spread may reflect parameter interactions, seed/matchup variance, outliers, or selection bias — not necessarily parameter sensitivity. Treat as 'where has the search looked and what was the observed range?' not 'which parameters matter most.'")
    L.append("")
    L.append("Per-value sample counts (`n=`) let you judge reliability: n<5 is fragile, n>=30 is moderate confidence.")
    L.append("")
    imp = param_exploration(all_rows, c1)
    if imp:
        L.append("| param | observed spread ($, best−worst mean) | best value | C1 value | values tested | total n | sampling balance | per-value means (value: $mean, n) |")
        L.append("|---|---:|---|---|---:|---:|---:|---|")
        for entry in imp[:20]:
            ms = ", ".join(f"{v}: {d['mean']:+,} (n={d['n']})" for v, d in entry["means"].items())
            L.append(f"| {entry['param']} | {entry['spread']:+,.0f} | {entry['best_value']} | {entry['c1_value']} | {entry['n_values_tested']} | {entry['total_candidates']} | {entry['sampling_balance']} | {ms} |")
            L.append(f"  __{entry['_note']}__")
    L.append("")

    # behavioural cells
    cells = defaultdict(list)
    for r in alive:
        if r.get("descriptor"):
            d = json.loads(r["descriptor"])
            cells[(d.get("animals_d15"), d.get("land_final"), d.get("hands_max"))].append(r["dev_margin"])
    L.append("## Behavioural cells (animals@d15, land, max hands) → best dev margin, n")
    L.append("")
    for k, v in sorted(cells.items(), key=lambda kv: -max(kv[1]))[:15]:
        L.append(f"- {k}: {max(v):+,.0f} (n={len(v)})")
    L.append("")
    L.append(f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._")

    # grouped failure observations (observational only — correlations, not established causes)
    failure_groups = _grouped_failure_observations(all_rows)
    if failure_groups:
        L.append("")
        L.append("## Recent failure observations (grouped by failure class)")
        L.append("")
        L.append("**Observational only. Correlations, not established causes.** These groups describe parameter ranges frequently seen in recent failures of each class. A parameter appearing here may be part of the failure mechanism, or it may be confounded by the companion parameters tested alongside it, the seeds/matchups used, or RNG-path effects. Do not interpret these as 'avoid this parameter range.'")
        L.append("")
        for fg in failure_groups:
            L.append(f"### {fg['class']} (observed in {fg['n']} recent candidates)")
            L.append("")
            L.append(f"- **Observed outcome:** {fg['outcome']}")
            L.append(f"- **Associated parameter ranges (correlation, not cause):** {fg['param_ranges']}")
            L.append(f"- **Evidence:** {fg['n']} candidates, {fg['seeds']} seeds. Confidence: {fg['confidence']}")
            L.append("")

    L.append(f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}. Candidate files in `evolve/gen/`, DB `evolve/evolve.db`._")

    REPORT_DIR.mkdir(exist_ok=True)
    out = REPORT_DIR / f"{run_id}.md"
    out.write_text("\n".join(L))
    return out


if __name__ == "__main__":
    db = DB()
    rid = sys.argv[1] if len(sys.argv) > 1 else None
    if rid is None:
        r = db.conn.execute("SELECT run_id FROM runs ORDER BY started DESC LIMIT 1").fetchone()
        rid = r["run_id"] if r else None
    if not rid:
        print("no runs")
        sys.exit(1)
    print(write_report(db, rid))
