#!/usr/bin/env python3
"""Held-out spot check (Sep 9) of the two most interesting robustness_panel.py findings:
1) Clone opponent: do B/CD/BCD/O4 all stay strongly positive vs O2?
2) TapePeter opponent: does O4 uniquely flip negative vs O2 while B/CD/BCD stay positive?
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade

C = "candidates/"
O = "Opponents/"
CANDS = {
    "O2":  C+"O2_STATE_OWNERSHIP.py", "B": C+"O2_lifecycle.py",
    "CD":  C+"O2_capital_release.py", "BCD": C+"O2_plus_bundle.py",
    "O4":  C+"O4_PRODUCTIVE_SERVICE.py",
}
OPPONENTS = {"C1": C+"C1.py", "V3_15": C+"V3_15.py"}
HELD_SEEDS = list(range(11, 31))

def ttest_1samp(vals):
    n = len(vals); mean = sum(vals)/n
    var = sum((v-mean)**2 for v in vals)/(n-1) if n>1 else 0.0
    se = math.sqrt(var/n) if n>0 else 0.0
    t = mean/se if se>0 else (float("inf") if mean!=0 else 0.0)
    return mean, t

def own_money_per_seed(cand_path, opp_path, seeds):
    r, dt = cascade._eval(cand_path, opp_path, seeds, "master", jobs=5)
    ps = r["per_seed"]
    return {s: ps[s]["a"]/2.0 for s in seeds}

def main():
    for opp_name, opp_path in OPPONENTS.items():
        m_o2 = own_money_per_seed(CANDS["O2"], opp_path, HELD_SEEDS)
        print(f"\n=== {opp_name} (held-out, n={len(HELD_SEEDS)}) ===")
        for cand_name in ["B", "CD", "BCD", "O4"]:
            m_c = own_money_per_seed(CANDS[cand_name], opp_path, HELD_SEEDS)
            deltas = [m_c[s]-m_o2[s] for s in HELD_SEEDS]
            mean, t = ttest_1samp(deltas)
            wins = sum(d>0 for d in deltas); losses = sum(d<0 for d in deltas)
            print(f"  {cand_name:5s}-O2: mean={mean:9.1f}  t={t:6.2f}  wins={wins}-{losses}")

if __name__ == "__main__":
    main()
