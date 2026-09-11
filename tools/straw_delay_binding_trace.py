#!/usr/bin/env python3
"""straw_delay binding trace (Sep 12, reconciliation follow-up).

Question (Grace's framing): when baseline O26 plants strawberries before day 10 (the straw_delay=10
contrast threshold from the engagement audit), what economically relevant state would justify waiting
instead -- and does that state later prove the early planting decision wrong? Concretely: do pre-day-10
plantings realize measurably WORSE economics (early death before ever reaching a production night, or
fewer total units) than day-10-to-cutoff plantings, in the SAME baseline games, using the SAME per-planting
lifecycle tracker already validated in kaggriculture-strawberry-early-death-sep11 (tools/straw_life.py)?

This reuses straw_life.run() verbatim (no reimplementation of its tile-lifecycle tracking) and adds only
a planted_day bucketing + comparison layer on top. Non-economic engagement is NOT re-tested here -- that's
already closed (REACHED, ACTION CHANGES). This is the binding/error trace the reconciliation called for.

Usage: KAGG_FIXED_SHOPS=1 python3 straw_delay_binding_trace.py --opp bahaen --seeds 71-90
"""
import sys, os, argparse, json
ROOT = "/root/mnt/Kaggriculture" if os.path.isdir("/root/mnt/Kaggriculture") else os.path.expanduser("~/mnt/Kaggriculture")
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import straw_life as sl

CAND = os.path.join(ROOT, "candidates/O26_CARROT_SIZING.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}
THRESH = 10  # straw_delay contrast value from the engagement audit


def bucket_stats(lives):
    n = len(lives)
    if n == 0:
        return None
    tot_units = sum(L["total"] for L in lives)
    pre_died = sum(1 for L in lives if L["last_age"] < sl.FIRST)
    avg_age = sum(L["last_age"] for L in lives) / n
    return {
        "n": n,
        "units_per_planting": tot_units / n,
        "pre_production_death_rate": pre_died / n,
        "avg_death_age": avg_age,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--opp", required=True, choices=list(OPPS) + ["all"])
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--json")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    opp_list = list(OPPS) if args.opp == "all" else [args.opp]

    early, late = [], []  # cand-side (index 0) lives, bucketed by planted_day
    per_opp = {}
    for opp_key in opp_list:
        opp_path = OPPS[opp_key]
        opp_early, opp_late = [], []
        for seed in range(lo, hi + 1):
            done = sl.run(CAND, opp_path, seed)
            cand_lives = done[0]  # our farm is always seat 0 in this straw_life harness
            for L in cand_lives:
                (opp_early if L["planted_day"] < THRESH else opp_late).append(L)
        early.extend(opp_early)
        late.extend(opp_late)
        per_opp[opp_key] = {"early": bucket_stats(opp_early), "late": bucket_stats(opp_late)}

    result = {
        "opp": args.opp, "seeds": args.seeds, "threshold_day": THRESH,
        "note": "cand=O26_CARROT_SIZING, seat 0 only (straw_life harness is seat-fixed); baseline straw_delay=0 (default, unmodified)",
        "combined_early_lt10": bucket_stats(early),
        "combined_late_ge10": bucket_stats(late),
        "per_opp": per_opp,
    }
    print(json.dumps(result, indent=2))
    if args.json:
        with open(args.json, "w") as f:
            json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()
