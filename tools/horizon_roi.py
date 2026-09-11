#!/usr/bin/env python3
"""Remaining-horizon ROI of investments and production, measured by counterfactual (AGE-360, Sep 11).

Companion to tools/delay_counterfactual.py. That tool answers "what does postponing this ONE action by one
hour cost?". This one answers the capacity/spending question:

    "Is there enough game left for this purchase class to pay back?"

Method. Against a deterministic tape with KAGG_FIXED_SHOPS=1 the whole game is deterministic, so a
counterfactual is exact rather than sampled. Two modes:

  cutoff  Block every order of investment type T from day D to the end of the game.
          roi = base_final - cf_final = the realized remaining-horizon return of continuing to invest in T
          from day D onward, NET of acquisition cost, operating cost, AND opportunity cost -- because the
          counterfactual policy plays the whole rest of the game with that cash free to deploy elsewhere.
          Sweeping D gives an ROI-vs-horizon curve, which is the direct measurement behind every hand-tuned
          "buy until day X" threshold in the chassis.

  marginal Allow at most (what this cell's base run placed that day) - K UNITS of type T from day D on.
          roi = base_final - cf_final = the realized value of the LAST K units per day of that class.
          This is the mode that answers "is one more worker / tile / animal worth it?". Cutoff does NOT
          answer that for any class the policy replenishes continuously (labour, feed): blocking those is
          near-total ablation, and its number is the value of HAVING the subsystem, not of its last unit.
          The two can have opposite signs, and for HIRE on this chassis they do.

  defer   Block type T for days [D, D+K), then allow it again.
          roi = base_final - cf_final = the cost of postponing that investment class by K days. Negative
          means waiting was free or better -- i.e. option value of waiting.

Payback horizon. Both modes record a per-day net-worth trace for base and counterfactual. At the cutoff day
the base run is POORER (it just spent the money), so delta(day) = base_nw - cf_nw starts negative. The
payback day is the first day delta crosses >= 0 and stays there. If it never crosses, the purchase did not
pay back inside the horizon.

EPISTEMIC STATUS. Each (candidate, tape, seed, type, day) cell is an exact counterfactual, not an estimate --
there is no sampling error within a cell. The uncertainty is entirely ACROSS cells: different tapes and seeds
are different games, so the mean over a panel is an estimate of "ROI against the field" with a real CI. This
is an OBSERVATIONAL instrument. It measures what one policy's investment schedule was worth on these tapes.
It does NOT say the optimum is at the cutoff day where ROI hits zero (the policy's own downstream behaviour
is held fixed), and nothing here feeds mutation weighting automatically. See docs/AGE-360-horizon-roi.md.

Usage:
  KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py CAND --mode marginal --reduce 1 \
      --types HIRE --days 8,12,16,20,24 --seeds 1,2,3,4,5,6,7,8
  KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py CAND --tapes panel --seeds 1,2,3 \
      --types HIRE,BUY_ANIMAL,BUY_LAND,BUY_SEED,BUY_PRODUCT --days 6,10,14,18,22,26 --emit
  KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py CAND --mode defer --defer-days 3 --types BUY_ANIMAL
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402

# The 4-tape ladder panel used by evolve/batch_vs_o8.py -- keep these in sync.
PANEL = {
    "peter": "Opponents/tape_peterparker_106816877.py",
    "alaylm": "Opponents/tape_alaylm_106813359.py",
    "bahaen": "Opponents/tape_bahaenes_106828159.py",
    "yangk": "Opponents/tape_yangkuang2_106819729.py",
}

# Investment types the tool understands. verb -> item filter (None = every item of that verb).
# A type string may also be "VERB:ITEM" (e.g. BUY_ANIMAL:COW, BUY_SEED:MELON) for a per-item curve.
INVESTMENT_VERBS = {
    "HIRE": "labor",
    "BUY_ANIMAL": "livestock",
    "BUY_LAND": "land",
    "BUY_SEED": "crop cycle",
    "BUY_PRODUCT": "feed/fertilizer",
    "BUILD_PASTURE": "infrastructure",
    "BUILD_COOP": "infrastructure",
}

PRICE_FALLBACK = {"MILK": 160, "WOOL": 200, "STRAWBERRY": 120, "MELON": 250, "TOMATO": 60,
                  "CARROT": 35, "WHEAT": 25, "EGG": 50, "FERTILIZER": 100}
ANIMAL_VALUE = {"COW": 400, "SHEEP": 500, "GOOSE": 300}
YIELD_GOOD = {"COW": "MILK", "SHEEP": "WOOL", "GOOSE": "EGG"}


def parse_type(spec: str):
    """'BUY_ANIMAL' -> ('BUY_ANIMAL', None); 'BUY_ANIMAL:COW' -> ('BUY_ANIMAL', 'COW')."""
    if ":" in spec:
        verb, item = spec.split(":", 1)
        return verb.strip().upper(), item.strip().upper()
    return spec.strip().upper(), None


def networth(obs0, priv):
    """Cash + shed & carried goods at current price + standing yield at price + live animals.

    Same valuation as tools/delay_counterfactual.py::networth so the two tools' traces are comparable.
    """
    farm = obs0.farms[0]
    prices = dict(obs0.market["prices"])
    val = farm["money"]
    for k, n in dict(priv["shed"]).items():
        if k in ANIMAL_VALUE:
            val += ANIMAL_VALUE[k] * n
        elif n > 0:
            val += prices.get(k, PRICE_FALLBACK.get(k, 0)) * n
    for bag in (priv.get("inventories") or []):
        for k, n in bag.items():
            if k in ANIMAL_VALUE:
                val += ANIMAL_VALUE[k] * n
            elif n > 0:
                val += prices.get(k, PRICE_FALLBACK.get(k, 0)) * n
    for row in farm["tiles"]:
        for t in row:
            if not isinstance(t, dict):
                continue
            if "animal" in t:
                val += ANIMAL_VALUE.get(t["animal"], 300) + t.get("yield_units", 0) * prices.get(
                    YIELD_GOOD.get(t["animal"], ""), 100)
            elif t.get("kind") == "PLANT":
                val += t.get("yield_units", 0) * prices.get(t.get("crop"), PRICE_FALLBACK.get(t.get("crop"), 0))
    return val


def play(cand, opp, seed, block=None, daily=None, spend=None, units=None, marginal=None):
    """Run one deterministic game as player 0.

    block:  (verb, item, day_from, day_to) -- drop matching market orders on days
            day_from <= day < day_to (day_to None = to the end of the game). item None matches any.
    daily:  list to append (day, networth, cash) once per day, at the first turn of that day.
    spend:  dict to accumulate observed gross spend per investment type, so acquisition cost is
            measured rather than assumed.
    units:  dict to accumulate observed order UNITS as units[(verb, item)][day] = qty. This is what a
            marginal intervention is calibrated against -- you cannot cap a class at "one fewer per day"
            without first knowing how many it places per day, in this exact cell.
    marginal: (verb, item, day_from, day_to, caps) -- on days in range, allow at most caps[day] UNITS of
            the matching class, reducing an order's quantity rather than dropping it whole where possible.
            A per-DAY unit budget, not a per-turn one: the policies here re-issue a shortfall on a later
            turn of the same day (hiring tops up to a target), so a per-turn filter would be silently
            absorbed and measure nothing.
    Returns final money.
    """
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    step = 0
    seen_day = -1
    marg_day = -1      # day the marginal unit budget was last reset
    marg_used = 0      # units of the capped class already allowed today
    while True:
        obs0 = state[0].observation
        day = obs0.day
        if daily is not None and day != seen_day:
            daily.append((day, networth(obs0, obs0.private), obs0.farms[0]["money"]))
            seen_day = day
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            if i == 0:
                orders = list(act.get("market") or [])
                if block is not None and orders:
                    bv, bi, d0, d1 = block
                    if day >= d0 and (d1 is None or day < d1):
                        act["market"] = [o for o in orders
                                         if not (o and o[0] == bv and (bi is None or (len(o) > 1 and o[1] == bi)))]
                elif marginal is not None and orders:
                    mv, mi, d0, d1, caps = marginal
                    if day != marg_day:
                        marg_day, marg_used = day, 0
                    if day >= d0 and (d1 is None or day < d1):
                        cap = caps.get(day, 0.0)
                        kept = []
                        for o in orders:
                            if not (o and o[0] == mv and (mi is None or (len(o) > 1 and o[1] == mi))):
                                kept.append(o)
                                continue
                            qty = o[2] if len(o) > 2 and isinstance(o[2], (int, float)) else 1
                            room = cap - marg_used
                            if room >= qty:
                                marg_used += qty
                                kept.append(o)
                            elif room > 0 and len(o) > 2 and isinstance(o[2], (int, float)):
                                kept.append(list(o[:2]) + [int(room)] + list(o[3:]))
                                marg_used += int(room)
                            # else: today's budget is spent -- drop the order entirely
                        act["market"] = kept
                # Record AFTER the intervention, from what is actually submitted to the engine. Recording
                # the pre-intervention list would log what the policy WANTED, not what it got -- and a
                # capped policy asks for more, not less, because it keeps falling short of its target. That
                # made the first verification pass read as "the cap increased purchases".
                final_orders = act.get("market") or []
                if (spend is not None or units is not None) and final_orders:
                    prices = dict(obs0.market["prices"])
                    for o in final_orders:
                        if not o or o[0] not in INVESTMENT_VERBS:
                            continue
                        item = o[1] if len(o) > 1 and isinstance(o[1], str) else None
                        qty = o[2] if len(o) > 2 and isinstance(o[2], (int, float)) else 1
                        if units is not None:
                            by_day = units.setdefault((o[0], item), {})
                            by_day[day] = by_day.get(day, 0) + float(qty)
                        if spend is not None:
                            # HIRE cost is a fibonacci schedule and BUY_LAND a computed price -- neither is
                            # a market good, so est_cost stays None rather than reading as a silent $0.
                            unit = ANIMAL_VALUE.get(item) or prices.get(item) or PRICE_FALLBACK.get(item)
                            key = o[0] if item is None else f"{o[0]}:{item}"
                            e = spend.setdefault(key, {"orders": 0, "units": 0.0, "est_cost": 0.0,
                                                       "priced": unit is not None, "days": []})
                            e["orders"] += 1
                            e["units"] += float(qty)
                            if unit is None:
                                e["priced"] = False
                            else:
                                e["est_cost"] += float(unit) * float(qty)
                            e["days"].append(day)
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break
    if daily is not None:
        obs0 = state[0].observation
        daily.append((obs0.day, networth(obs0, obs0.private), obs0.farms[0]["money"]))
    return state[0].observation.farms[0]["money"]


def payback_day(base_daily, cf_daily, cutoff_day):
    """First day AFTER cutoff_day on which the investing run's CASH has overtaken the non-investing run's,
    and stays ahead for the rest of the game.

    Payback is measured on cash, not net worth: net worth counts a just-bought asset at roughly its purchase
    price, so it hides the outlay the payback period is defined against. delta(day) = base_cash - cf_cash is
    therefore negative right after the spend and turns positive once the asset has earned its cost back.
    Day cutoff_day itself is excluded -- it is sampled at the first turn of the day, before the blocked
    orders would have been placed, so delta there is identically 0 and would spuriously read as instant
    payback.

    Returns (payback_day or None, delta_series).
    """
    bl = {d: cash for d, _, cash in base_daily}
    cl = {d: cash for d, _, cash in cf_daily}
    days = sorted(set(bl) & set(cl))
    series = [(d, bl[d] - cl[d]) for d in days]
    tail = [(d, x) for d, x in series if d > cutoff_day]
    for idx, (d, x) in enumerate(tail):
        if x > 0 and all(y > 0 for _, y in tail[idx:]):
            return d, series
    return None, series


def mean_ci(vals, conf_t=1.96):
    n = len(vals)
    if n == 0:
        return 0.0, 0.0, 0.0, 0.0
    m = sum(vals) / n
    if n < 2:
        return m, 0.0, m, m
    var = sum((v - m) ** 2 for v in vals) / (n - 1)
    se = math.sqrt(var / n)
    t = m / se if se > 0 else 0.0
    return m, t, m - conf_t * se, m + conf_t * se


def aggregate(a):
    """Rebuild the summary table + artifact from a jsonl written by earlier (possibly chunked) runs."""
    recs = [json.loads(ln) for ln in open(a.aggregate) if ln.strip()]
    if not recs:
        print(f"{a.aggregate}: empty", file=sys.stderr)
        return
    # Deduplicate: a cell is (mode, type, day, defer_days, tape, seed). Chunked or repeated runs write the
    # same cell more than once; each is the SAME deterministic counterfactual, so keeping duplicates would
    # inflate n and shrink the CI for free. Last write wins.
    uniq = {}
    for r in recs:
        uniq[(r["mode"], r["type"], r["day"], r.get("defer_days"), r.get("reduce"),
              r["tape"], r["seed"])] = r
    dropped = len(recs) - len(uniq)
    recs = list(uniq.values())
    modes = {r["mode"] for r in recs}
    # Group by the INTERVENTION, not just (type, day): a -1 unit/day cap and a -2 unit/day cap are
    # different experiments and pooling them averages two different effect sizes into one meaningless row.
    cells = {}
    for r in recs:
        size = r.get("reduce") if r["mode"] == "marginal" else r.get("defer_days")
        cells.setdefault((r["type"], r["day"], size), []).append(r)
    rows = []
    for (label, D, size), rs in sorted(cells.items(), key=lambda kv: (kv[0][0], kv[0][2] or 0, kv[0][1])):
        deltas = [r["roi"] for r in rs]
        pbs = [r["payback_day"] for r in rs]
        hit = [p for p in pbs if p is not None]
        m, t, lo, hi = mean_ci(deltas)
        rows.append({"type": label, "day": D, "size": size, "mode": rs[0]["mode"],
                     "roi_mean": m, "t": t, "ci_lo": lo, "ci_hi": hi,
                     "n": len(deltas), "pos_frac": sum(1 for d in deltas if d > 0) / len(deltas),
                     "payback_rate": len(hit) / len(pbs),
                     "payback_median": (sorted(hit)[len(hit) // 2] if hit else None),
                     "min": min(deltas), "max": max(deltas)})
    if not a.quiet:
        print(f"# horizon ROI (aggregated from {a.aggregate})  modes={sorted(modes)}  "
              f"{len(recs)} distinct counterfactual cells"
              + (f" ({dropped} duplicate cells dropped)" if dropped else ""))
        for r in rows:
            pbm = r["payback_median"]
            how = (f"-{r['size']}u/day from day" if r["mode"] == "marginal"
                   else f"deferred {r['size']}d at day" if r["mode"] == "defer" else "from day")
            print(f"{r['type']:20s} {how} {r['day']:2d}  n={r['n']:2d}  roi ${r['roi_mean']:9,.0f}  t={r['t']:6.2f}  "
                  f"95% CI [{r['ci_lo']:9,.0f},{r['ci_hi']:9,.0f}]  +{r['pos_frac']:.0%}  "
                  f"payback {r['payback_rate']:.0%}" + (f" by day {pbm}" if pbm is not None else " never"))
    if a.emit:
        outdir = ROOT / "artifacts" / "horizon_roi"
        outdir.mkdir(parents=True, exist_ok=True)
        payload = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "cand": recs[0]["cand"],
                   "mode": "+".join(sorted(modes)), "defer_days": recs[0].get("defer_days"),
                   "tapes": sorted({r["tape"] for r in recs}), "seeds": sorted({r["seed"] for r in recs}),
                   "fixed_shops": os.environ.get("KAGG_FIXED_SHOPS") == "1",
                   "base_mean": sum({(r["tape"], r["seed"]): r["base"] for r in recs}.values())
                                / len({(r["tape"], r["seed"]) for r in recs}),
                   "spend": {}, "rows": rows,
                   "caveat": ("Observational. Exact per-cell counterfactual against deterministic tapes; "
                              "uncertainty is across tapes/seeds only. Downstream policy behaviour is held "
                              "fixed, so a zero crossing is NOT an optimal cutoff day. Not wired to "
                              "mutation weighting.")}
        (outdir / "latest.json").write_text(json.dumps(payload, indent=2))
        if not a.quiet:
            print(f"\nwrote {outdir/'latest.json'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cand", help="candidate .py to measure")
    ap.add_argument("--tapes", default="panel",
                    help="'panel' for the 4-tape ladder panel, or a comma list of Opponents/*.py paths")
    ap.add_argument("--seeds", default="1,2,3")
    ap.add_argument("--types", default="HIRE,BUY_ANIMAL,BUY_LAND,BUY_SEED,BUY_PRODUCT",
                    help="comma list; VERB or VERB:ITEM (e.g. BUY_ANIMAL:COW, BUY_SEED:MELON)")
    ap.add_argument("--days", default="4,8,12,16,20,24",
                    help="cutoff days to sweep (cutoff mode) or start days (defer mode)")
    ap.add_argument("--mode", choices=["cutoff", "defer", "marginal"], default="cutoff")
    ap.add_argument("--reduce", type=int, default=1, metavar="K",
                    help="marginal mode: remove K UNITS per day of the class, relative to what this cell's "
                         "base run actually placed that day. K=1 prices one more worker / tile / animal.")
    ap.add_argument("--defer-days", type=int, default=3, help="defer mode: how many days to block")
    ap.add_argument("--json", default=None, help="append per-cell results to this jsonl")
    ap.add_argument("--emit", action="store_true",
                    help="write artifacts/horizon_roi/latest.json for evolve/report.py to render")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--aggregate", default=None, metavar="JSONL",
                    help="skip all replays; rebuild the table and artifact from an existing --json file. "
                         "Lets a long sweep be run in chunks (one --types slice per call) and pooled at the end.")
    a = ap.parse_args()

    if a.aggregate:
        aggregate(a)
        return

    if os.environ.get("KAGG_FIXED_SHOPS") != "1":
        print("WARNING: KAGG_FIXED_SHOPS is not 1. Shop draws will be policy-dependent and every number "
              "below will be dominated by shop-lottery noise. Re-run with KAGG_FIXED_SHOPS=1.",
              file=sys.stderr)

    tapes = PANEL if a.tapes == "panel" else {Path(p).stem: p for p in a.tapes.split(",")}
    seeds = [int(s) for s in a.seeds.split(",")]
    types = [parse_type(t) for t in a.types.split(",")]
    days = [int(d) for d in a.days.split(",")]

    t_start = time.time()
    # --- base runs (one per tape x seed), plus observed acquisition spend
    base = {}
    base_daily = {}
    base_units = {}
    spend = {}
    for tname, tpath in tapes.items():
        for seed in seeds:
            d = []
            u = {}
            base[(tname, seed)] = play(a.cand, tpath, seed, daily=d, spend=spend, units=u)
            base_units[(tname, seed)] = u
            base_daily[(tname, seed)] = d
    n_cells = len(tapes) * len(seeds)
    if not a.quiet:
        print(f"# horizon ROI -- {a.cand}  mode={a.mode}  cells={n_cells} "
              f"({len(tapes)} tapes x {len(seeds)} seeds)")
        bm = sum(base.values()) / len(base)
        print(f"# base final money, mean over cells: ${bm:,.0f}")
        print(f"# observed acquisition spend in base runs (gross, per game, averaged over cells):")
        for k, e in sorted(spend.items(), key=lambda kv: -kv[1]["est_cost"]):
            if e["orders"] == 0:
                continue
            dmin, dmax = min(e["days"]), max(e["days"])
            cost = f"~${e['est_cost']/n_cells:9,.0f}" if e["priced"] else "      n/a"
            print(f"#   {k:22s} {e['orders']/n_cells:6.1f} orders  {e['units']/n_cells:7.1f} units  "
                  f"{cost}  days {dmin}-{dmax}")
        print()

    rows = []
    for verb, item in types:
        label = verb if item is None else f"{verb}:{item}"
        for D in days:
            d1 = None if a.mode == "cutoff" else D + a.defer_days
            deltas, paybacks = [], []
            for tname, tpath in tapes.items():
                for seed in seeds:
                    cfd = []
                    if a.mode == "marginal":
                        # Per-day unit budget = what THIS cell's base run actually placed that day, minus K.
                        # Calibrating per cell matters: the same policy places different quantities against
                        # different tapes, so a single global cap would be a different-sized intervention
                        # in every cell and the CI would be measuring that instead of the effect.
                        bu = base_units[(tname, seed)]
                        per_day = {}
                        for (v, it), by_day in bu.items():
                            if v != verb or (item is not None and it != item):
                                continue
                            for dd, q in by_day.items():
                                per_day[dd] = per_day.get(dd, 0.0) + q
                        caps = {dd: max(0.0, q - a.reduce) for dd, q in per_day.items()}
                        cf = play(a.cand, tpath, seed, marginal=(verb, item, D, None, caps), daily=cfd)
                    else:
                        cf = play(a.cand, tpath, seed, block=(verb, item, D, d1), daily=cfd)
                    delta = base[(tname, seed)] - cf
                    deltas.append(delta)
                    pb, _ = payback_day(base_daily[(tname, seed)], cfd, D)
                    paybacks.append(pb)
                    if a.json:
                        with open(a.json, "a") as fh:
                            fh.write(json.dumps({
                                "cand": a.cand, "mode": a.mode, "type": label, "day": D,
                                "defer_days": a.defer_days if a.mode == "defer" else None,
                                "reduce": a.reduce if a.mode == "marginal" else None,
                                "tape": tname, "seed": seed, "base": base[(tname, seed)],
                                "cf": cf, "roi": delta, "payback_day": pb}) + "\n")
            m, t, lo, hi = mean_ci(deltas)
            pb_hit = [p for p in paybacks if p is not None]
            rows.append({
                "type": label, "day": D, "roi_mean": m, "t": t, "ci_lo": lo, "ci_hi": hi,
                "n": len(deltas), "pos_frac": sum(1 for d in deltas if d > 0) / len(deltas),
                "payback_rate": len(pb_hit) / len(paybacks),
                "payback_median": (sorted(pb_hit)[len(pb_hit) // 2] if pb_hit else None),
                "min": min(deltas), "max": max(deltas),
            })
            if not a.quiet:
                pbm = rows[-1]["payback_median"]
                verb_word = ("from day" if a.mode == "cutoff"
                             else f"-{a.reduce}u/day from day" if a.mode == "marginal"
                             else f"deferred {a.defer_days}d at day")
                print(f"{label:20s} {verb_word} {D:2d}  roi ${m:9,.0f}  t={t:6.2f}  "
                      f"95% CI [{lo:9,.0f},{hi:9,.0f}]  +{rows[-1]['pos_frac']:.0%}  "
                      f"payback {rows[-1]['payback_rate']:.0%}"
                      + (f" by day {pbm}" if pbm is not None else " never"), flush=True)

    if a.emit:
        outdir = ROOT / "artifacts" / "horizon_roi"
        outdir.mkdir(parents=True, exist_ok=True)
        payload = {
            "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "cand": a.cand, "mode": a.mode, "defer_days": a.defer_days,
            "tapes": list(tapes), "seeds": seeds,
            "fixed_shops": os.environ.get("KAGG_FIXED_SHOPS") == "1",
            "base_mean": sum(base.values()) / len(base),
            "spend": {k: {"orders_per_game": v["orders"] / n_cells,
                          "units_per_game": v["units"] / n_cells,
                          "est_cost_per_game": (v["est_cost"] / n_cells) if v["priced"] else None,
                          "first_day": min(v["days"]), "last_day": max(v["days"])}
                      for k, v in spend.items()},
            "rows": rows,
            "caveat": ("Observational. Exact per-cell counterfactual against deterministic tapes; uncertainty "
                       "is across tapes/seeds only. Downstream policy behaviour is held fixed, so a zero "
                       "crossing is NOT an optimal cutoff day. Not wired to mutation weighting."),
        }
        (outdir / "latest.json").write_text(json.dumps(payload, indent=2))
        stamp = time.strftime("%Y%m%d-%H%M")
        (outdir / f"{a.mode}-{stamp}.json").write_text(json.dumps(payload, indent=2))
        if not a.quiet:
            print(f"\nwrote {outdir/'latest.json'}")
    if not a.quiet:
        print(f"# {time.time()-t_start:.0f}s")


if __name__ == "__main__":
    main()
