#!/usr/bin/env python3
"""O8 margin/win record vs each real tape, dev+held seeds, with per-seed margins to find losing seeds."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade
O8 = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
PANEL = {"peter": "Opponents/tape_peterparker_106816877.py", "alaylm": "Opponents/tape_alaylm_106813359.py",
         "bahaen": "Opponents/tape_bahaenes_106828159.py", "yangk": "Opponents/tape_yangkuang2_106819729.py",
         "clone": "Opponents/opp_scenario_v14.py"}
if __name__ == "__main__":
    cand = sys.argv[1] if len(sys.argv) > 1 else O8
    seeds = list(range(1, 31))
    for name, opp in PANEL.items():
        r, _ = cascade._eval(cand, opp, seeds, "master", jobs=5)
        ps = r["per_seed"]
        worst = sorted(seeds, key=lambda s: ps[s]["a"] - ps[s]["b"])[:5]
        print(f"{name:7s} margin={r['mean_margin_per_game']:8.0f} t={r['t']:5.2f} w-l={r['wins']}-{r['losses']}  worst seeds: " +
              " ".join(f"s{s}:{(ps[s]['a']-ps[s]['b'])/2:+.0f}(me{ps[s]['a']/2:.0f})" for s in worst), flush=True)
