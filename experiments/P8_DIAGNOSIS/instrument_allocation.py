#!/usr/bin/env python3
"""
instrument_allocation.py — day-by-day allocation-timing diagnosis for
candidates/P8_reactive_allocation.py vs candidates/P6_baseline.py (and C1),
on IDENTICAL seeds through the real engine.

WHY: artifacts/reactive_allocation_p8/REPORT.md found P8 loses -$48-50k/game
to P6/C1 but only diagnosed the gap from the final $ delta ("root cause, read
off the per-day traces gathered DURING DEBUGGING" — informal, not saved). This
script produces a saved, reproducible day-by-day comparison so a retune can
target the actual leak instead of re-guessing from the final score.

HOW: reuses mini_engine.run_game() (via eval_protocol's already-imported `me`
module) exactly as eval_protocol.py does — no new engine-calling code. Each
policy plays the SAME opponent (Opponents/opp_scenario_v14.py) on the SAME
seed; mini_engine's own per-day trace (money/hands/land/animals/shed/buys,
snapshotted at hour 0 of each day) already contains everything requested:
cash, hands (labor units), land tiles (unlocked_quadrants -- proxy for "land
tiles owned"), herd size+mix, and hire/buy events (inferred from day-over-day
deltas in hands/land/animal_mix, since HIRE/BUY_LAND aren't logged via
_commit_unit the way SELL/BUY_PRODUCT/BUY_SEED/BUY_ANIMAL are -- see
mini_engine.py's `logged_commit`).

OUTPUT: experiments/P8_DIAGNOSIS/raw/*.json (one per seed x policy, full
mini_engine trace) and experiments/P8_DIAGNOSIS/summary.json (cross-seed
aggregate: first day each policy reaches N hands / land quadrant K / herd
size M).
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

CANDS = ROOT / "candidates"
OPP = ROOT / "Opponents" / "opp_scenario_v14.py"
OUT_DIR = Path(__file__).resolve().parent
RAW_DIR = OUT_DIR / "raw"
RAW_DIR.mkdir(exist_ok=True)

POLICIES = {
    "P8": CANDS / "P8_reactive_allocation.py",
    "P6": CANDS / "P6_baseline.py",
    "C1": CANDS / "C1.py",
}


def run_one(policy_path, seed, seat_swapped):
    """Run policy vs OPP on seed; return (per-day trace dict for the policy's
    own seat, final money delta policy-minus-opponent)."""
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


def first_day_reaching_list(values, threshold):
    """values is a plain list indexed by day (e.g. hands_eod); returns first day index >= threshold."""
    for day, v in enumerate(values):
        if v >= threshold:
            return day
    return None


def first_day_reaching(trace, key, threshold, reducer=lambda v: v):
    """First day index (0-based, matches trace list index) where reducer(trace[key][day]) >= threshold."""
    for day, v in enumerate(trace[key]):
        if reducer(v) >= threshold:
            return day
    return None


def hire_events(trace):
    """Infer effective daily hand-count changes from hands_eod (end-of-day
    count). NOTE: the engine re-hires the whole crew from 0 every day (see
    P6/P8 source comments), so this is not a literal "kept employee" count --
    it is this day's realized hiring target, i.e. exactly the number a
    day-by-day allocation-timing comparison needs. trace["hands"] (hour-0
    snapshot, BEFORE the day's HIRE orders land) is always 0 and not useful
    for this purpose -- confirmed empirically, kept in the record for
    completeness but not used for the hire-event log."""
    events = []
    hands = trace["hands_eod"]
    for day in range(1, len(hands)):
        delta = hands[day] - hands[day - 1]
        if delta != 0:
            events.append({"day": day, "hands_before": hands[day - 1], "hands_after": hands[day], "delta": delta})
    return events


def land_events(trace):
    events = []
    land = trace["land"]
    for day in range(1, len(land)):
        if land[day] != land[day - 1]:
            events.append({"day": day, "quads_before": land[day - 1], "quads_after": land[day]})
    return events


def herd_events(trace):
    events = []
    mixes = trace["animal_mix"]
    for day in range(1, len(mixes)):
        prev, cur = mixes[day - 1], mixes[day]
        for sp in set(prev) | set(cur):
            d = cur.get(sp, 0) - prev.get(sp, 0)
            if d != 0:
                events.append({"day": day, "species": sp, "delta": d, "count_after": cur.get(sp, 0)})
    return events


def summarize_policy_seed(name, trace, money_delta, errors, seed, seat_swapped):
    return {
        "policy": name, "seed": seed, "seat_swapped": seat_swapped, "errors": errors,
        "final_money_vs_opp_delta": money_delta,
        "day_reach_5_hands": first_day_reaching_list(trace["hands_eod"], 5),
        "day_reach_8_hands": first_day_reaching_list(trace["hands_eod"], 8),
        "day_reach_10_hands": first_day_reaching_list(trace["hands_eod"], 10),
        "day_reach_2quads": first_day_reaching(trace, "land", 2),
        "day_reach_3quads": first_day_reaching(trace, "land", 3),
        "day_reach_4quads": first_day_reaching(trace, "land", 4),
        "day_reach_10_animals": first_day_reaching(trace, "animals", 10),
        "day_reach_15_animals": first_day_reaching(trace, "animals", 15),
        "hands_eod_by_day": trace["hands_eod"],
        "hands_by_day": trace["hands"],
        "land_by_day": trace["land"],
        "animals_by_day": trace["animals"],
        "money_by_day": trace["money"],
        "plants_by_day": trace["plants"],
        "hire_events": hire_events(trace),
        "land_events": land_events(trace),
        "herd_events": herd_events(trace),
    }


def main(seeds, policies=("P8", "P6", "C1")):
    all_records = []
    for seed in seeds:
        for swapped in (False, True):
            for name in policies:
                path = POLICIES[name]
                trace, delta, errors = run_one(path, seed, swapped)
                rec = summarize_policy_seed(name, trace, delta, errors, seed, swapped)
                all_records.append(rec)
                json.dump(rec, open(RAW_DIR / f"{name}_seed{seed}_swap{int(swapped)}.json", "w"), indent=2, default=str)
                print(f"{name} seed={seed} swap={swapped}: errors={errors} "
                      f"final_delta_vs_opp=${delta:+,.0f} "
                      f"5hands@d{rec['day_reach_5_hands']} 2quads@d{rec['day_reach_2quads']} "
                      f"3quads@d{rec['day_reach_3quads']} 10animals@d{rec['day_reach_10_animals']}")

    # ---- cross-seed aggregate summary
    summary = {}
    for name in policies:
        recs = [r for r in all_records if r["policy"] == name]
        def agg(key):
            vals = [r[key] for r in recs if r[key] is not None]
            return {
                "n_reached": len(vals), "n_total": len(recs),
                "mean_day": round(statistics.mean(vals), 2) if vals else None,
                "median_day": statistics.median(vals) if vals else None,
                "days": vals,
            }
        summary[name] = {
            "n_games": len(recs),
            "mean_final_delta_vs_opp": round(statistics.mean(r["final_money_vs_opp_delta"] for r in recs), 1),
            "day_reach_5_hands": agg("day_reach_5_hands"),
            "day_reach_8_hands": agg("day_reach_8_hands"),
            "day_reach_10_hands": agg("day_reach_10_hands"),
            "day_reach_2quads": agg("day_reach_2quads"),
            "day_reach_3quads": agg("day_reach_3quads"),
            "day_reach_4quads": agg("day_reach_4quads"),
            "day_reach_10_animals": agg("day_reach_10_animals"),
            "day_reach_15_animals": agg("day_reach_15_animals"),
            "total_errors": sum(r["errors"] for r in recs),
        }
    json.dump(summary, open(OUT_DIR / "summary.json", "w"), indent=2, default=str)
    print("\n=== SUMMARY ===")
    print(json.dumps(summary, indent=2, default=str))
    return summary


if __name__ == "__main__":
    seeds = list(range(1, 11))
    if len(sys.argv) > 1:
        seeds = [int(x) for x in sys.argv[1:]]
    main(seeds)
