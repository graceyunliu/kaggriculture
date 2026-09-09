#!/usr/bin/env python3
"""Same as instrument_allocation.py but P8v2 vs P6 vs C1 (P8v2 retune check)."""
from __future__ import annotations
import json, statistics, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "experiments" / "RNG_PATH_DEPENDENCE_AUDIT"))
import mini_engine as me  # noqa: E402
import instrument_allocation as ia  # reuse helper functions
CANDS = ROOT / "candidates"
OPP = ROOT / "Opponents" / "opp_scenario_v14.py"
OUT_DIR = Path(__file__).resolve().parent
RAW_DIR = OUT_DIR / "raw_v2"
RAW_DIR.mkdir(exist_ok=True)
POLICIES = {"P8v2": CANDS / "P8v2_reactive_allocation.py", "P6": CANDS / "P6_baseline.py", "C1": CANDS / "C1.py"}

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

def main(seeds, policies=("P8v2", "P6", "C1")):
    all_records = []
    for seed in seeds:
        for swapped in (False, True):
            for name in policies:
                path = POLICIES[name]
                trace, delta, errors = run_one(path, seed, swapped)
                rec = ia.summarize_policy_seed(name, trace, delta, errors, seed, swapped)
                all_records.append(rec)
                json.dump(rec, open(RAW_DIR / f"{name}_seed{seed}_swap{int(swapped)}.json", "w"), indent=2, default=str)
                print(f"{name} seed={seed} swap={swapped}: errors={errors} final_delta_vs_opp=${delta:+,.0f} "
                      f"2quads@d{rec['day_reach_2quads']} 3quads@d{rec['day_reach_3quads']} 4quads@d{rec['day_reach_4quads']} "
                      f"10animals@d{rec['day_reach_10_animals']} 15animals@d{rec['day_reach_15_animals']} "
                      f"final_land={rec['land_by_day'][-1]} final_animals={rec['animals_by_day'][-1]}")
    summary = {}
    for name in policies:
        recs = [r for r in all_records if r["policy"] == name]
        def agg(key):
            vals = [r[key] for r in recs if r[key] is not None]
            return {"n_reached": len(vals), "n_total": len(recs),
                    "mean_day": round(statistics.mean(vals), 2) if vals else None,
                    "median_day": statistics.median(vals) if vals else None}
        summary[name] = {
            "n_games": len(recs),
            "mean_final_delta_vs_opp": round(statistics.mean(r["final_money_vs_opp_delta"] for r in recs), 1),
            "mean_final_land": round(statistics.mean(r["land_by_day"][-1] for r in recs), 2),
            "mean_final_animals": round(statistics.mean(r["animals_by_day"][-1] for r in recs), 2),
            "day_reach_2quads": agg("day_reach_2quads"),
            "day_reach_3quads": agg("day_reach_3quads"),
            "day_reach_4quads": agg("day_reach_4quads"),
            "day_reach_10_animals": agg("day_reach_10_animals"),
            "day_reach_15_animals": agg("day_reach_15_animals"),
            "total_errors": sum(r["errors"] for r in recs),
        }
    json.dump(summary, open(OUT_DIR / "summary_v2.json", "w"), indent=2, default=str)
    print("\n=== SUMMARY ===")
    print(json.dumps(summary, indent=2, default=str))
    return summary

if __name__ == "__main__":
    seeds = list(range(1, 11))
    if len(sys.argv) > 1:
        seeds = [int(x) for x in sys.argv[1:]]
    main(seeds)
