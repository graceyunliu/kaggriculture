import sys
sys.path.insert(0, "/sessions/vigilant-great-cori/mnt/Kaggriculture/evolve")
from cascade import _eval, HELD_SEEDS

def main():
    for opp, label in [("candidates/V3_15.py", "V3_15"), ("candidates/C1.py", "C1")]:
        r, dt = _eval("candidates/O4_PRODUCTIVE_SERVICE.py", opp, HELD_SEEDS, "master", 4)
        print(f"O4 HELD-OUT vs {label}: margin={r['mean_margin_per_game']:+,.0f} t={r['t']:.2f} {r['wins']}-{r['losses']} errs={r['agent_errors']}", flush=True)

if __name__ == "__main__":
    main()
