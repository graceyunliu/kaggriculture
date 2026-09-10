#!/usr/bin/env python3
"""Full 2^3 factorial ablation of the O2->O3 'bundle' (Sep 9).
Mechanisms: B=lifecycle-aware care/feed, C=intraday capital timing, D=mid-route release.
Paired, same-seed contrasts only (per user's explicit rule against independent-sample
'vs C1' margins for small effects). Uses DEV_SEEDS; HELD_SEEDS spot-check follows.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cascade

DEV_SEEDS = list(range(1, 11))
C = "candidates/"

VARIANTS = {
    "O2":        C+"O2_STATE_OWNERSHIP.py",
    "B":         C+"O2_lifecycle.py",
    "Cc":        C+"O2_capital.py",
    "D":         C+"O2_release.py",
    "BC":        C+"O2_lifecycle_capital.py",
    "BD":        C+"O2_lifecycle_release.py",
    "CD":        C+"O2_capital_release.py",
    "BCD":       C+"O2_plus_bundle.py",
}

# contrast, (variant, baseline)
CONTRASTS = [
    ("B vs O2",   "B",   "O2"),
    ("Cc vs O2",  "Cc",  "O2"),
    ("D vs O2",   "D",   "O2"),
    ("BC vs B",   "BC",  "B"),
    ("BC vs Cc",  "BC",  "Cc"),
    ("BD vs B",   "BD",  "B"),
    ("BD vs D",   "BD",  "D"),
    ("CD vs Cc",  "CD",  "Cc"),
    ("CD vs D",   "CD",  "D"),
    ("BCD vs BC", "BCD", "BC"),
    ("BCD vs BD", "BCD", "BD"),
    ("BCD vs CD", "BCD", "CD"),
    ("BCD vs O2", "BCD", "O2"),
]

def main():
    for name, a, b in CONTRASTS:
        pa, pb = VARIANTS[a], VARIANTS[b]
        r, dt = cascade._eval(pa, pb, DEV_SEEDS, "master", jobs=5)
        print(f"{name:14s} mean_margin={r['mean_margin_per_game']:10.1f}  t={r['t']:6.2f}  wins={r['wins']}-{r['losses']}", flush=True)

if __name__ == "__main__":
    main()
