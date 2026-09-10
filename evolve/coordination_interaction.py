#!/usr/bin/env python3
"""Sep 9 follow-up: does the site-claim coordination mechanism (Pillar 1) interact with
B (Pillar 2), CD (Pillar 3), or BCD -- or is it additive with all of them, the same way
B and CD were shown to be additive with each other?

interaction(Coord x X) = [effect of coordination inside X] - [effect of coordination in O2]
                        = (X_with_coord - X_no_coord) - (O2_with_coord - O2_no_coord)

Uses SAME per-seed simulation runs for each term (paired by seed), not subtracted means.
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade

C = "candidates/"
PAIRS = {
    "O2":  (C+"O2_STATE_OWNERSHIP.py",       C+"O2_no_siteclaim.py"),
    "B":   (C+"O2_lifecycle.py",             C+"O2_lifecycle_no_siteclaim.py"),
    "CD":  (C+"O2_capital_release.py",       C+"O2_capital_release_no_siteclaim.py"),
    "BCD": (C+"O2_plus_bundle.py",           C+"O2_plus_bundle_no_siteclaim.py"),
}

def per_seed_margin(with_c, without_c, seeds):
    r, dt = cascade._eval(with_c, without_c, seeds, "master", jobs=5)
    ps = r["per_seed"]
    return {s: (ps[s]["a"] - ps[s]["b"]) / 2.0 for s in seeds}  # coord effect per game, per seed

def ttest_1samp(vals):
    n = len(vals); mean = sum(vals)/n
    var = sum((v-mean)**2 for v in vals)/(n-1) if n>1 else 0.0
    se = math.sqrt(var/n) if n>0 else 0.0
    t = mean/se if se>0 else (float("inf") if mean!=0 else 0.0)
    return mean, t

def run(seeds, label):
    coord_effect = {}
    for name, (with_c, without_c) in PAIRS.items():
        coord_effect[name] = per_seed_margin(with_c, without_c, seeds)
        print(f"[{label}] computed coord effect for {name}", flush=True)
    print(f"\n[{label}] Coordination's own effect within each context (mean $/game, t):")
    for name in PAIRS:
        vals = list(coord_effect[name].values())
        mean, t = ttest_1samp(vals)
        print(f"  within {name:4s}: {mean:9.1f}  t={t:6.2f}")
    print(f"\n[{label}] Interaction = coord_effect(X) - coord_effect(O2), per seed, t-tested:")
    for name in ["B", "CD", "BCD"]:
        inter = [coord_effect[name][s] - coord_effect["O2"][s] for s in seeds]
        mean, t = ttest_1samp(inter)
        print(f"  Coord x {name:4s}: mean={mean:9.1f}  t={t:6.2f}  n={len(seeds)}")
    print()

if __name__ == "__main__":
    run(list(range(1, 11)), "DEV")
    run(list(range(11, 31)), "HELD")
