#!/usr/bin/env python3
"""Experiment 1 (Sep 9): does B interact with CD, or are they additive subsystems?
Computes per-seed interaction = margin(BCD vs O2) - margin(B vs O2) - margin(CD vs O2),
using the SAME seeds for all three evals so the per-seed subtraction is a true paired
contrast, then t-tests the interaction series against zero. Runs DEV_SEEDS then HELD_SEEDS.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade

C = "candidates/"
O2  = C+"O2_STATE_OWNERSHIP.py"
B   = C+"O2_lifecycle.py"
CD  = C+"O2_capital_release.py"
BCD = C+"O2_plus_bundle.py"

def per_seed_margins(cand, base, seeds):
    r, dt = cascade._eval(cand, base, seeds, "master", jobs=5)
    ps = r["per_seed"]
    # margin per game = (a-b)/2 since a,b are sums over 2 seat-swapped games
    return {s: (ps[s]["a"] - ps[s]["b"]) / 2.0 for s in seeds}

def ttest_1samp(vals):
    n = len(vals)
    mean = sum(vals) / n
    var = sum((v - mean) ** 2 for v in vals) / (n - 1) if n > 1 else 0.0
    se = math.sqrt(var / n) if n > 0 else 0.0
    t = mean / se if se > 0 else float("inf") if mean != 0 else 0.0
    return mean, t

def run(seeds, label):
    m_bcd = per_seed_margins(BCD, O2, seeds)
    m_b   = per_seed_margins(B, O2, seeds)
    m_cd  = per_seed_margins(CD, O2, seeds)
    interaction = [m_bcd[s] - m_b[s] - m_cd[s] for s in seeds]
    mean, t = ttest_1samp(interaction)
    print(f"[{label}] per-seed interaction = margin(BCD)-margin(B)-margin(CD)")
    for s in seeds:
        print(f"  seed {s:2d}: BCD={m_bcd[s]:9.1f}  B={m_b[s]:9.1f}  CD={m_cd[s]:9.1f}  interaction={interaction[-1] if False else (m_bcd[s]-m_b[s]-m_cd[s]):9.1f}")
    print(f"[{label}] mean interaction = {mean:.1f}/game, t = {t:.2f}, n={len(seeds)}")
    print(f"[{label}] sum of solo effects (B+CD) mean = {sum(m_b.values())/len(seeds) + sum(m_cd.values())/len(seeds):.1f}  vs actual BCD mean = {sum(m_bcd.values())/len(seeds):.1f}")
    print()

if __name__ == "__main__":
    run(list(range(1, 11)), "DEV")
    run(list(range(11, 31)), "HELD")
