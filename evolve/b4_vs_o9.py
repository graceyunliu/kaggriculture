#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade
O9 = "candidates/O9_O8_ENDGAME.py"
def run(a, b, seeds, label):
    r, _ = cascade._eval(a, b, seeds, "master", jobs=5)
    print(f"[{label}] {os.path.basename(a)} vs {os.path.basename(b)}: {r['mean_margin_per_game']:+.0f}/game t={r['t']:.2f} {r['wins']}-{r['losses']} errors={r['agent_errors']}", flush=True)
if __name__ == "__main__":
    which = sys.argv[1]
    seeds = {"dev": range(1, 11), "held": range(11, 31), "fresh": range(31, 51)}[sys.argv[2]]
    cand = {"b4": "candidates/B4_01_MELON_LATEFERT.py", "o10": "candidates/O10_O9_MELON_LATEFERT.py"}[which]
    run(cand, O9, list(seeds), sys.argv[2])
