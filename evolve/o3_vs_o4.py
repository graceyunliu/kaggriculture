import sys
sys.path.insert(0, "/sessions/vigilant-great-cori/mnt/Kaggriculture/evolve")
from cascade import _eval, DEV_SEEDS, HELD_SEEDS

def main():
    r, dt = _eval("candidates/O4_PRODUCTIVE_SERVICE.py", "candidates/O3_PRODUCTIVE_SERVICE.py", DEV_SEEDS, "master", 4)
    print(f"O4 vs O3 (paired) dev: margin={r['mean_margin_per_game']:+,.0f} t={r['t']:.2f} {r['wins']}-{r['losses']} errs={r['agent_errors']}", flush=True)
    r2, dt2 = _eval("candidates/O4_PRODUCTIVE_SERVICE.py", "candidates/O3_PRODUCTIVE_SERVICE.py", HELD_SEEDS, "master", 4)
    print(f"O4 vs O3 (paired) held-out: margin={r2['mean_margin_per_game']:+,.0f} t={r2['t']:.2f} {r2['wins']}-{r2['losses']} errs={r2['agent_errors']}", flush=True)

if __name__ == "__main__":
    main()
