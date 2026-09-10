"""Morning report for an evolution run.

    python3 evolve/report.py [run_id]      # defaults to the latest run
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import space  # noqa: E402
from db import DB  # noqa: E402
import action_table as at_mod  # noqa: E402  # AGE-359/AGE-360: action timing matrix

REPORT_DIR = HERE / "reports"


def _fmt(v, money=True):
    if v is None:
        return "—"
    return f"{v:+,.0f}" if money else f"{v:.1f}"

def _fmt_mean(d):
    """Format a mean_dev from a summary dict {mean_dev, n}. Returns '—' if None."""
    v = d.get("mean_dev") if isinstance(d, dict) else d
    if v is None:
        return "—"
    return f"{v:+,.0f}"


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


def action_table_summary(all_rows):
    """Aggregate action_table across all alive candidates in a run.

    Returns a dict with:
      - by_action_horizon: {action_type: {horizon: {mean_dev, n}}}
      - by_action_context: {action_type: {context_key: {mean_dev, n}}}
      - postponement_curves: {action_type: {postponement_bin: {mean_dev, n}}}
      - top_signals: list of [action_type, context, horizon, mean_dev, n, signal_noise] sorted by |mean_dev|
      - action_type_counts: {action_type: total_events}
      - totals: {total_candidates_with_at, total_events}
    """
    from collections import defaultdict
    import json as _json

    rows_with_at = [r for r in all_rows if r.get("action_table")]
    if not rows_with_at:
        return {}

    by_action_horizon = defaultdict(lambda: defaultdict(list))
    by_action_context = defaultdict(lambda: defaultdict(list))
    postponement_buckets = defaultdict(lambda: defaultdict(list))
    action_counts = defaultdict(int)
    totals = {"total_candidates_with_at": len(rows_with_at), "total_events": 0}

    for r in rows_with_at:
        dev = r.get("dev_margin")
        if dev is None:
            continue
        try:
            at_data = _json.loads(r["action_table"])
        except Exception:
            continue
        at = at_data.get("action_table", {})
        for action_type, events in at.items():
            action_counts[action_type] += len(events)
            totals["total_events"] += len(events)
            for ev in events:
                day = ev.get("day", 0)
                days_remaining = max(0, 29 - day)
                if days_remaining <= 7:
                    horizon = "late"
                elif days_remaining <= 14:
                    horizon = "mid"
                else:
                    horizon = "early"
                by_action_horizon[action_type][horizon].append(dev)

                # Context key
                ctx = ev.get("context", {})
                animals = ctx.get("animals", 0)
                hands = ctx.get("hands", 0)
                cash = ctx.get("cash", 0)
                plants = ctx.get("plants", 0)
                ctx_key = (
                    "low" if animals < 8 else "mid" if animals < 12 else "high",
                    "low" if hands < 6 else "mid" if hands < 10 else "high",
                    "low" if cash < 500 else "mid" if cash < 2000 else "high",
                    "low" if plants < 5 else "mid" if plants < 15 else "high",
                )
                by_action_context[action_type][ctx_key].append(dev)

                # Postponement curve: bin by postponement_days (computed from day + action_type)
                day = ev.get("day", 0)
                if action_type == "SELL":
                    optimal = at_mod.optimal_day_for_sell(ev.get("items", {}))
                else:
                    optimal = 2 if action_type in ("BUY_ANIMAL", "BUY_SEED") else (
                        6 if action_type == "BUY_LAND" else (0 if action_type in ("WATER_MISSED", "FEED_MISSED") else day))
                postponement = max(0, day - optimal)
                pb = max(0, min(5, int(postponement)))  # 0,1,2,3,4,5+
                postponement_buckets[action_type][pb].append(dev)

    def summarize(buckets):
        return {
            h: {"mean_dev": round(sum(v) / len(v)) if v else None, "n": len(v), "total_events": sum(len(v) for v in buckets.values())}
            for h, v in buckets.items()
        }

    result = {
        "by_action_horizon": {at: summarize(bh) for at, bh in by_action_horizon.items()},
        "by_action_context": {at: {str(ctx): {"mean_dev": round(sum(v) / len(v)) if v else None, "n": len(v)} for ctx, v in bctx.items()} for at, bctx in by_action_context.items()},
        "postponement_curves": {at: {str(pb): {"mean_dev": round(sum(v) / len(v)) if v else None, "n": len(v)} for pb, v in pbuckets.items()} for at, pbuckets in postponement_buckets.items()},
        "action_type_counts": dict(action_counts),
        "totals": totals,
    }

    # Top matrix signals: strongest |mean_dev| per action_type × horizon
    signals = []
    for at, bh in by_action_horizon.items():
        for horizon, vals in bh.items():
            if len(vals) < 3:
                continue
            mean = sum(vals) / len(vals)
            variance = max(0, sum(v**2 for v in vals) / len(vals) - mean**2)
            sn = round(mean / max(1, variance**0.5), 2) if len(vals) >= 5 else None
            signals.append([at, "—", horizon, round(mean), len(vals), sn])
    signals.sort(key=lambda x: -abs(x[3]))
    result["top_signals"] = signals[:20]

    return result


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
    c1 = space.o15_params()   # 'changes' column diffs against O15 (the yardstick frontier), Sep 10

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
    L.append("Chassis seed rows are the evolve chassis rendered with a parameter set, NOT the historical files of the "
             "same name; a seed identical to the chassis is a no-op and shows 0-0. The file rows below are the real "
             "`candidates/*.py` agents played against the current frontier on DEV_SEEDS (cached games).")
    L.append("")
    L.append("| candidate | dev vs frontier | t | W-L | dev vs clone | held-out | held t | W-L |")
    L.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for name, p in (("chassis defaults (seed row)", ref), ("chassis + C1 params (seed row)", c1)):
        r = db.get(space.params_key(p))
        if r:
            wl = f"{r['dev_wins']}-{r['dev_losses']}" if (r['dev_wins'] or r['dev_losses']) else "not evaluated (no-op)"
            L.append(f"| {name} | {_fmt(r['dev_margin'])} | {_fmt(r['dev_t'], False)} | {wl} | "
                     f"{_fmt(r['clone_margin'])} | {_fmt(r['held_margin'])} | {_fmt(r['held_t'], False)} | "
                     f"{r['held_wins'] or '—'}-{r['held_losses'] or '—'} |")
    try:
        import cascade as _casc
        fr = run.get("frontier")
        for name, f in (("C1.py (file)", "candidates/C1.py"), ("V3_12.py (file)", "candidates/V3_12.py")):
            if fr and Path(f).exists() and Path(fr).exists():
                rr, _dt = _casc._eval(f, fr, _casc.DEV_SEEDS, "master", None)
                L.append(f"| {name} vs {Path(fr).name} | {_fmt(rr['mean_margin_per_game'])} | {_fmt(rr['t'], False)} | "
                         f"{rr['wins']}-{rr['losses']} | — | — | — | — |")
        fp = cfg.get("frontier_panel_dev")
        if fp is not None:
            L.append(f"| {Path(fr).name} own panel (dev / held) | — | — | — | {_fmt(fp)} / {_fmt(cfg.get('frontier_panel_held'))} | — | — | — |")
    except Exception as e:  # noqa: BLE001
        L.append(f"| (file reference rows unavailable: {e!r}) | | | | | | | |")
    L.append("")
    if os.environ.get("KAGG_FIXED_SHOPS") == "1":
        L.append("Measurement mode: `KAGG_FIXED_SHOPS=1` (shop unlocks policy-independent; panel margins comparable at ±$3k/opponent).")
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

    L.append("## Action timing patterns (AGE-359: observational — correlations, not causes)")
    L.append("")
    timing_summary = action_table_summary(all_rows)
    if not timing_summary:
        L.append("No action_table data yet. Action timing extraction is wired into the cascade (cascade.py "
                 "calls action_table_from_trace after trajectory summary) but the current run's candidates "
                 "haven't completed a cascade pass with the new code. The next dev-stage completion for each "
                 "alive candidate will populate action_table.")
        L.append("")
    else:
        totals = timing_summary.get("totals", {})
        L.append(f"**{totals.get('total_candidates_with_at', 0)} candidates** with action_table data, "
                 f"**{totals.get('total_events', 0)} total action events** extracted "
                 f"(SELL/BUY item counts are averaged across the 5 trajectory seeds — see trace.py SUMMARY_FIELDS).")
        L.append("")
        L.append("Action timing vs outcome correlation. For each action type, the table shows mean dev_margin "
                 "of candidates that performed that action in each horizon bucket. Higher dev_margin = better outcome. "
                 "This is NOT causal — a candidate that sells early may also have other good properties. "
                 "Use as a guide for what to test, not as a proven mechanism.")
        L.append("")
        L.append("| action_type | early (days 1-14) | mid (days 15-21) | late (days 22-29) | total events |")
        L.append("|---|---|---:|---|---|---:|")

        action_order = ["SELL", "BUY_ANIMAL", "BUY_SEED", "BUY_LAND", "BUY_PRODUCT", "HIRE",
                        "WATER_MISSED", "FEED_MISSED"]
        for atype in action_order:
            bh = timing_summary.get("by_action_horizon", {}).get(atype, {})
            early = bh.get("early", {})
            mid = bh.get("mid", {})
            late = bh.get("late", {})
            total = timing_summary.get("action_type_counts", {}).get(atype, 0)
            L.append(f"| {atype} | "
                     f"{_fmt_mean(early):>14} (n={early.get('n',0)}) | "
                     f"{_fmt_mean(mid):>14} (n={mid.get('n',0)}) | "
                     f"{_fmt_mean(late):>14} (n={late.get('n',0)}) | {total} |")
            if atype == "WATER_MISSED":
                L.append(f"  _Water missed = postponement signal. Negative = candidates that missed water had lower dev_margin._")
            if atype == "FEED_MISSED":
                L.append(f"  _Feed missed = postponement signal. Negative = candidates that missed feed had lower dev_margin._")
        L.append("")

        # Postponement curves
        L.append("## Postponement cost curves (mean dev_margin by days postponed)")
        L.append("")
        L.append("For each action type, how does outcome vary with how late the action was taken? "
                 "Postponement days = action_day − optimal_day (approx). 0 = on time, 5+ = very late.")
        L.append("")
        L.append("| action_type | on-time (0d) | 1d late | 2d late | 3d late | 4d late | 5+d late |")
        L.append("|---|---|---:|---:|---:|---:|---:|---:|")
        for atype in action_order:
            pc = timing_summary.get("postponement_curves", {}).get(atype, {})
            vals = [_fmt_mean(pc.get(str(i), {})) for i in range(6)]
            L.append(f"| {atype} | " + " | ".join(f"{v:>11}" for v in vals) + " |")
        L.append("")

        # Top context signals
        L.append("## Action contexts with strongest outcome signal (top 10)")
        L.append("")
        L.append("Action × horizon combinations sorted by |mean_dev|. These are the patterns most "
                 "associated with outcome variation — candidates for matrix-informed runtime rules.")
        L.append("")
        L.append("| rank | action_type | horizon | mean_dev | n | signal/noise |")
        L.append("|---|---|---:|---:|---:|---:|")
        for i, sig in enumerate(timing_summary.get("top_signals", [])[:10], 1):
            atype, ctx, horizon, mean, n, sn = sig
            L.append(f"| {i} | {atype} | {horizon} | {mean:+,.0f} | {n} | {sn or '—'} |")
        L.append("")

        # Context buckets table
        L.append("## Action × context bucket (mean dev_margin, n≥3)")
        L.append("")
        L.append("**Context key:** (animals: low<8/mid8-12/high>12, hands: low<6/mid6-10/high>10, "
                 "cash: low<500/mid500-2000/high>2000, crops: low<5/mid5-15/high>15)")
        L.append("")
        ctx_data = timing_summary.get("by_action_context", {})
        ctx_rows = []
        for atype, ctx_key_str, info in ((at, ck, inf) for at, bctx in ctx_data.items() for ck, inf in bctx.items()):
            if info.get("n", 0) >= 3 and info.get("mean_dev") is not None:
                # ctx_key_str is str((animals, hands, cash, crops)) from JSON round-trip
                try:
                    import ast
                    ctx_key = ast.literal_eval(ctx_key_str)
                except Exception:
                    ctx_key = ctx_key_str
                ctx_rows.append((atype, ctx_key, info["mean_dev"], info["n"]))
        ctx_rows.sort(key=lambda x: -abs(x[2]))
        for atype, ctx_key, mean, n in ctx_rows[:15]:
            L.append(f"- **{atype}** in {ctx_key}: {mean:+,.0f} (n={n})")
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
