#!/usr/bin/env python3
"""Panel-depth runner for crop_window_trace.py (nonlinear_threshold contract: 20 seeds x 2
independent sets). Runs O26_CARROT_SIZING against the standard 4-tape panel on two seed sets,
reports decay/RATE-2/destroyed-yield per (tape, set, farm, crop), and flags whether direction
and magnitude replicate across the two sets. Observational only -- no own/margin money read
here (that only matters once an intervention exists); this is sizing the mechanism itself.
"""
import sys, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import crop_window_trace as cwt

CAND = "candidates/O26_CARROT_SIZING.py"
TAPES = [
    "Opponents/tape_alaylm_106813359.py",
    "Opponents/tape_bahaenes_106828159.py",
    "Opponents/tape_peterparker_106816877.py",
    "Opponents/tape_yangkuang2_106819729.py",
]
SETS = {"set1(11-30)": range(11, 31), "set2(31-50)": range(31, 51)}
CROPS = ("WHEAT", "CARROT", "MELON")


def summarize(lives, crop):
    cl = [L for L in lives if L["crop"] == crop]
    n = len(cl)
    if n == 0:
        return dict(n=0, decay=0, rate2=0, destroyed=0)
    decayed = [L for L in cl if L["outcome"] == "decayed_to_weed"]
    rate2 = [L for L in decayed if not L["ever_watered"]]
    destroyed = sum(L["peak_yield"] for L in decayed)
    return dict(n=n, decay=len(decayed), rate2=len(rate2), destroyed=destroyed)


def main():
    os.chdir(ROOT)
    rows = []  # tape, set, farm, crop, n, decay, rate2, destroyed
    for tape in TAPES:
        tname = os.path.basename(tape)
        for setname, seeds in SETS.items():
            agg = [[], []]
            for seed in seeds:
                done, lp, tpd = cwt.run(CAND, tape, seed, CROPS)
                for p in range(2):
                    agg[p].extend(done[p])
            for p, farm in ((0, "O26"), (1, tname)):
                for crop in CROPS:
                    s = summarize(agg[p], crop)
                    rows.append(dict(tape=tname, set=setname, farm=farm, crop=crop, **s))
        print(f"done: {tname}", file=sys.stderr)

    # print raw table
    print(f"{'tape':<28}{'set':<14}{'farm':<10}{'crop':<9}{'n':>5}{'decay':>7}{'decay%':>8}{'rate2%':>8}{'destroyed':>11}")
    for r in rows:
        pct = r["decay"] / r["n"] * 100 if r["n"] else 0.0
        r2 = r["rate2"] / r["n"] * 100 if r["n"] else 0.0
        print(f"{r['tape']:<28}{r['set']:<14}{r['farm']:<10}{r['crop']:<9}{r['n']:>5}{r['decay']:>7}{pct:>7.1f}%{r2:>7.1f}%{r['destroyed']:>11}")

    # replication check: for each (tape, farm, crop), compare decay% across the two sets
    print("\n=== replication across the two independent seed sets ===")
    key = lambda r: (r["tape"], r["farm"], r["crop"])
    by_key = collections.defaultdict(dict)
    for r in rows:
        by_key[key(r)][r["set"]] = r
    set_names = list(SETS.keys())
    for k, d in sorted(by_key.items()):
        if set_names[0] not in d or set_names[1] not in d:
            continue
        r1, r2 = d[set_names[0]], d[set_names[1]]
        p1 = r1["decay"] / r1["n"] * 100 if r1["n"] else 0.0
        p2 = r2["decay"] / r2["n"] * 100 if r2["n"] else 0.0
        flag = "STABLE" if abs(p1 - p2) <= 5 else ("DIRECTION-CONSISTENT" if (p1 > 0) == (p2 > 0) and min(p1,p2) > 0 else "UNSTABLE")
        tape, farm, crop = k
        print(f"  {tape:<28}{farm:<10}{crop:<9} set1={p1:5.1f}%  set2={p2:5.1f}%  n1={r1['n']:<4} n2={r2['n']:<4} -> {flag}")

    # O26-only view aggregated across all 4 tapes (its own planting volume, both sets), by crop
    print("\n=== O26 aggregate across all 4 tapes, both sets (own planting-volume-normalized) ===")
    for crop in CROPS:
        o26_rows = [r for r in rows if r["farm"] == "O26" and r["crop"] == crop]
        n = sum(r["n"] for r in o26_rows); dec = sum(r["decay"] for r in o26_rows)
        r2 = sum(r["rate2"] for r in o26_rows); destroyed = sum(r["destroyed"] for r in o26_rows)
        pct = dec / n * 100 if n else 0.0
        print(f"  {crop}: {n} plantings, {dec} decayed ({pct:.1f}%), {r2} rate-2 (never watered), {destroyed} peak-yield units destroyed")


if __name__ == "__main__":
    main()
