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


def knob_importance(rows, ref):
    """Mean dev margin by parameter value, for params that varied. Crude but tells you where the signal is."""
    by = defaultdict(lambda: defaultdict(list))
    for r in rows:
        if r.get("dev_margin") is None:
            continue
        p = json.loads(r["params"])
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
        out.append((spread, k, best, ref.get(k), {str(v): (round(m), len(vals[v])) for v, m in sorted(means.items(), key=lambda x: -x[1])}))
    out.sort(reverse=True)
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
            d = space.diff(json.loads(r["params"]), c1)
            ds = ", ".join(f"{k} {a}→{b}" for k, (a, b) in d.items())
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
        d = space.diff(json.loads(r["params"]), c1)
        ds = ", ".join(f"{k} {a}→{b}" for k, (a, b) in d.items())
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

    L.append("## Where the signal is (mean dev margin by parameter value, all runs)")
    L.append("")
    imp = knob_importance(all_rows, c1)
    if imp:
        L.append("| param | spread | best value | C1 value | means (value: $, n) |")
        L.append("|---|---:|---|---|---|")
        for spread, k, best, refv, means in imp[:20]:
            ms = ", ".join(f"{v}: {m:+,} ({n})" for v, (m, n) in means.items())
            L.append(f"| {k} | {spread:,.0f} | {best} | {refv} | {ms} |")
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
