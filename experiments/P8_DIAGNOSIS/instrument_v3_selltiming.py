#!/usr/bin/env python3
"""
instrument_v3_selltiming.py — sell-timing / cash-buffer diagnosis for
candidates/P8v2_reactive_allocation.py vs candidates/P6_baseline.py / C1.py.

WHY: DIAGNOSIS_V2.md ruled out land and (in either retune direction) herd as
the residual -$12.6k/-$16.4k P8v2-vs-P6/C1 gap and flagged R5 sell-timing /
CASH_BUFFER sizing as the untested next lever (§3 recommendation). This script
tests that directly.

HOW: reuses mini_engine.run_game()'s own trace fields (via eval_protocol's
`me` import, same pattern as instrument_allocation.py / instrument_v2.py — no
new engine-calling code): trace["money"] (cash by day), trace["shed"]
(inventory held, snapshotted hour 0 -- i.e. BEFORE that day's sell orders
execute, so it is "inventory held before selling"), trace["sales"] (per-day
dict item -> (qty_sold, revenue) logged directly off the engine's own
_commit_unit calls, so sale price is exact, not estimated).

Adds, per policy/seed, per item:
  - shed inventory trajectory (held before that day's sells)
  - sell events: day, item, qty, revenue, avg price per unit
  - "cash velocity": for each item, mean(revenue_that_day / (revenue_that_day
    + shed_held_that_day * mean_market_price)) is not reliable without a
    market-price trace, so velocity is instead measured directly and simply
    as: mean shed-inventory level for the item across the whole game (lower
    = faster conversion to cash / less sitting idle) and the number of
    distinct sell-events (higher with same total qty = more frequent/smaller
    sells = faster velocity, lower = fewer/larger dumps = slower velocity).
  - cash-on-hand trajectory (trace["money"], already directly comparable).

OUTPUT: experiments/P8_DIAGNOSIS/raw_v3/*.json (per seed x policy full
mini_engine trace + derived event log) and
experiments/P8_DIAGNOSIS/summary_v3.json (cross-seed aggregate).
"""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "experiments" / "RNG_PATH_DEPENDENCE_AUDIT"))

import mini_engine as me  # noqa: E402
import instrument_allocation as ia  # noqa: E402  (reuse hire/land/herd helpers)

CANDS = ROOT / "candidates"
OPP = ROOT / "Opponents" / "opp_scenario_v14.py"
OUT_DIR = Path(__file__).resolve().parent
RAW_DIR = OUT_DIR / "raw_v3"
RAW_DIR.mkdir(exist_ok=True)

POLICIES = {
    "P8v2": CANDS / "P8v2_reactive_allocation.py",
    "P6": CANDS / "P6_baseline.py",
    "C1": CANDS / "C1.py",
}

SELL_ITEMS = ("MILK", "WOOL", "STRAWBERRY", "FERTILIZER", "TOMATO", "CARROT", "EGG", "MELON", "WHEAT")


def run_one(policy_path, seed, seat_swapped):
    if not seat_swapped:
        r = me.run_game(str(policy_path), str(OPP), seed, engine="master", trace=True)
        own_idx = 0
    else:
        r = me.run_game(str(OPP), str(policy_path), seed, engine="master", trace=True)
        own_idx = 1
    opp_idx = 1 - own_idx
    tr = r["trace"][own_idx]
    money_delta = r["money"][own_idx] - r["money"][opp_idx]
    return tr, money_delta, r["errors"][own_idx]


def sell_events(trace):
    """Flatten trace['sales'] (per-day item -> (qty, revenue)) into a list."""
    events = []
    for day, day_sales in enumerate(trace["sales"]):
        for item, (qty, rev) in day_sales.items():
            if qty > 0:
                events.append({"day": day, "item": item, "qty": qty, "revenue": round(rev, 1),
                                "avg_price": round(rev / qty, 2)})
    return events


def shed_stats(trace, item):
    """Per-item shed-inventory trajectory (held before that day's sells)."""
    vals = [d.get(item, 0) for d in trace["shed"]]
    return {"by_day": vals, "mean": round(statistics.mean(vals), 2) if vals else 0,
            "max": max(vals) if vals else 0}


def cash_low_days(trace, floor=100.0):
    """Days where cash-on-hand (money, hour-0 snapshot) fell below `floor`,
    i.e. the policy was effectively cash-starved that day (can't afford
    hires/land/herd/seeds regardless of what the allocation rule wants)."""
    return [d for d, m in enumerate(trace["money"][:-1]) if m < floor]


def summarize(name, trace, money_delta, errors, seed, seat_swapped):
    ev = sell_events(trace)
    per_item = {}
    for item in SELL_ITEMS:
        item_events = [e for e in ev if e["item"] == item]
        total_qty = sum(e["qty"] for e in item_events)
        total_rev = sum(e["revenue"] for e in item_events)
        per_item[item] = {
            "n_sell_events": len(item_events),
            "total_qty_sold": total_qty,
            "total_revenue": round(total_rev, 1),
            "mean_price_per_unit": round(total_rev / total_qty, 2) if total_qty else None,
            "shed": shed_stats(trace, item),
        }
    low = cash_low_days(trace, 100.0)
    return {
        "policy": name, "seed": seed, "seat_swapped": seat_swapped, "errors": errors,
        "final_money_vs_opp_delta": money_delta,
        "money_by_day": trace["money"],
        "cash_low_days_lt100": low,
        "n_cash_low_days_lt100": len(low),
        "mean_cash_days1_10": round(statistics.mean(trace["money"][1:11]), 1) if len(trace["money"]) > 10 else None,
        "mean_cash_days11_20": round(statistics.mean(trace["money"][11:21]), 1) if len(trace["money"]) > 20 else None,
        "sell_events": ev,
        "per_item": per_item,
        "n_sell_events_total": len(ev),
    }


def main(seeds, policies=("P8v2", "P6", "C1")):
    all_records = []
    for seed in seeds:
        for swapped in (False, True):
            for name in policies:
                path = POLICIES[name]
                trace, delta, errors = run_one(path, seed, swapped)
                rec = summarize(name, trace, delta, errors, seed, swapped)
                all_records.append(rec)
                json.dump(rec, open(RAW_DIR / f"{name}_seed{seed}_swap{int(swapped)}.json", "w"), indent=2, default=str)
                print(f"{name} seed={seed} swap={swapped}: errors={errors} final_delta=${delta:+,.0f} "
                      f"cash_low_days={rec['n_cash_low_days_lt100']} sell_events={rec['n_sell_events_total']} "
                      f"mean_cash_d1-10={rec['mean_cash_days1_10']}")

    summary = {}
    for name in policies:
        recs = [r for r in all_records if r["policy"] == name]
        summary[name] = {
            "n_games": len(recs),
            "mean_final_delta_vs_opp": round(statistics.mean(r["final_money_vs_opp_delta"] for r in recs), 1),
            "mean_n_cash_low_days_lt100": round(statistics.mean(r["n_cash_low_days_lt100"] for r in recs), 2),
            "mean_cash_days1_10": round(statistics.mean(r["mean_cash_days1_10"] for r in recs if r["mean_cash_days1_10"] is not None), 1),
            "mean_cash_days11_20": round(statistics.mean(r["mean_cash_days11_20"] for r in recs if r["mean_cash_days11_20"] is not None), 1),
            "mean_n_sell_events_total": round(statistics.mean(r["n_sell_events_total"] for r in recs), 2),
            "total_errors": sum(r["errors"] for r in recs),
        }
        for item in SELL_ITEMS:
            qtys = [r["per_item"][item]["total_qty_sold"] for r in recs]
            revs = [r["per_item"][item]["total_revenue"] for r in recs]
            prices = [r["per_item"][item]["mean_price_per_unit"] for r in recs if r["per_item"][item]["mean_price_per_unit"] is not None]
            shed_means = [r["per_item"][item]["shed"]["mean"] for r in recs]
            shed_maxes = [r["per_item"][item]["shed"]["max"] for r in recs]
            n_events = [r["per_item"][item]["n_sell_events"] for r in recs]
            summary[name][f"item_{item}"] = {
                "mean_total_qty_sold": round(statistics.mean(qtys), 2) if qtys else 0,
                "mean_total_revenue": round(statistics.mean(revs), 1) if revs else 0,
                "mean_price_per_unit": round(statistics.mean(prices), 2) if prices else None,
                "mean_shed_level": round(statistics.mean(shed_means), 2) if shed_means else 0,
                "max_shed_level": max(shed_maxes) if shed_maxes else 0,
                "mean_n_sell_events": round(statistics.mean(n_events), 2) if n_events else 0,
            }
    json.dump(summary, open(OUT_DIR / "summary_v3.json", "w"), indent=2, default=str)
    print("\n=== SUMMARY ===")
    print(json.dumps(summary, indent=2, default=str))
    return summary


if __name__ == "__main__":
    seeds = list(range(1, 11))
    if len(sys.argv) > 1:
        seeds = [int(x) for x in sys.argv[1:]]
    main(seeds)
