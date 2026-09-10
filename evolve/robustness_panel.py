#!/usr/bin/env python3
"""Experiment 4 (Sep 9): mechanism portability panel.

For each opponent environment, run O2/B/CD/BCD/O4 against that SAME opponent on the
SAME seeds, then compute paired same-seed deltas (candidate's own money minus O2's own
money, per seed, both having faced the identical opponent/seed) for B, CD, BCD, O4.
This asks: does each mechanism's direction/magnitude hold across materially different
opponent architectures, or is it exploiting something specific to one opponent?

Also records weeds_new (a cheap occupancy/RNG-path proxy per the Sep 7 partial-coupling
finding) per candidate per opponent so a robustness win isn't silently attributed to
economic skill when part of it is a shifted RNG path.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade

C = "candidates/"
O = "Opponents/"

CANDS = {
    "O2":  C+"O2_STATE_OWNERSHIP.py",
    "B":   C+"O2_lifecycle.py",
    "CD":  C+"O2_capital_release.py",
    "BCD": C+"O2_plus_bundle.py",
    "O4":  C+"O4_PRODUCTIVE_SERVICE.py",
}

OPPONENTS = {
    "C1":         C+"C1.py",
    "V3_15":      C+"V3_15.py",
    "Clone":      O+"opp_scenario_v14.py",
    "TapePeter":  O+"tape_peterparker_106816877.py",
}

DEV_SEEDS = list(range(1, 11))

def ttest_1samp(vals):
    n = len(vals)
    mean = sum(vals) / n
    var = sum((v - mean) ** 2 for v in vals) / (n - 1) if n > 1 else 0.0
    se = math.sqrt(var / n) if n > 0 else 0.0
    t = mean / se if se > 0 else (float("inf") if mean != 0 else 0.0)
    return mean, t

def own_money_per_seed(cand_path, opp_path, seeds):
    r, dt = cascade._eval(cand_path, opp_path, seeds, "master", jobs=5)
    ps = r["per_seed"]
    return {s: ps[s]["a"] / 2.0 for s in seeds}  # per-game average money for cand

def main():
    results = {}  # (opp_name, cand_name) -> {seed: money}
    for opp_name, opp_path in OPPONENTS.items():
        for cand_name, cand_path in CANDS.items():
            results[(opp_name, cand_name)] = own_money_per_seed(cand_path, opp_path, DEV_SEEDS)
            print(f"done: {cand_name} vs {opp_name}", flush=True)

    print("\n=== Portability panel: paired delta vs O2, same opponent, same seed ===")
    header = f"{'Environment':12s} " + " ".join(f"{n:>18s}" for n in ["B-O2", "CD-O2", "BCD-O2", "O4-O2"])
    print(header)
    for opp_name in OPPONENTS:
        row = [opp_name]
        cells = []
        m_o2 = results[(opp_name, "O2")]
        for cand_name in ["B", "CD", "BCD", "O4"]:
            m_c = results[(opp_name, cand_name)]
            deltas = [m_c[s] - m_o2[s] for s in DEV_SEEDS]
            mean, t = ttest_1samp(deltas)
            cells.append(f"{mean:8.0f}(t={t:4.1f})")
        print(f"{opp_name:12s} " + " ".join(f"{c:>18s}" for c in cells))

if __name__ == "__main__":
    main()
