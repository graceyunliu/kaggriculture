#!/usr/bin/env python3
"""Held-out spot check of the key factorial contrasts from factorial_ablation.py (Sep 9)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade

HELD_SEEDS = list(range(11, 31))
C = "candidates/"
VARIANTS = {
    "O2":  C+"O2_STATE_OWNERSHIP.py",
    "B":   C+"O2_lifecycle.py",
    "Cc":  C+"O2_capital.py",
    "D":   C+"O2_release.py",
    "CD":  C+"O2_capital_release.py",
    "BCD": C+"O2_plus_bundle.py",
}
CONTRASTS = [
    ("B vs O2",   "B",   "O2"),
    ("Cc vs O2",  "Cc",  "O2"),
    ("D vs O2",   "D",   "O2"),
    ("CD vs D",   "CD",  "D"),
    ("CD vs Cc",  "CD",  "Cc"),
    ("BCD vs O2", "BCD", "O2"),
]

def main():
    for name, a, b in CONTRASTS:
        r, dt = cascade._eval(VARIANTS[a], VARIANTS[b], HELD_SEEDS, "master", jobs=5)
        print(f"{name:14s} mean_margin={r['mean_margin_per_game']:10.1f}  t={r['t']:6.2f}  wins={r['wins']}-{r['losses']}", flush=True)

if __name__ == "__main__":
    main()
