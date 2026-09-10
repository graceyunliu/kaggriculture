#!/usr/bin/env python3
"""Sep 9 follow-up: does O2's own site-claim coordination (S["claimed_sites"] /
S["pending_sites"], preventing two of our own units from targeting the same empty
tile for planting/animal-siting in one turn) carry independent value, the way B and
C x D do? Paired same-seed test: O2_no_siteclaim (coordination stripped) vs O2.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade

C = "candidates/"
O2 = C + "O2_STATE_OWNERSHIP.py"
NOCLAIM = C + "O2_no_siteclaim.py"

def run(seeds, label):
    r, dt = cascade._eval(NOCLAIM, O2, seeds, "master", jobs=5)
    print(f"[{label}] O2_no_siteclaim vs O2: mean_margin={r['mean_margin_per_game']:.1f}/game  "
          f"t={r['t']:.2f}  wins={r['wins']}-{r['losses']}")

if __name__ == "__main__":
    run(list(range(1, 11)), "DEV")
    run(list(range(11, 31)), "HELD")
