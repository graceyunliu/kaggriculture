import sys
sys.path.insert(0, "/sessions/vigilant-great-cori/mnt/Kaggriculture/evolve")
from cascade import _eval, DEV_SEEDS

CANDS = ["O2_STATE_OWNERSHIP", "O2_plus_sharedstock", "O2_plus_bundle", "O3_PRODUCTIVE_SERVICE", "O4_PRODUCTIVE_SERVICE"]

def main():
    for name in CANDS:
        r, dt = _eval(f"candidates/{name}.py", "candidates/C1.py", DEV_SEEDS, "master", 4)
        print(f"{name} vs C1: margin={r['mean_margin_per_game']:+,.0f} t={r['t']:.2f} {r['wins']}-{r['losses']} errs={r['agent_errors']}", flush=True)

if __name__ == "__main__":
    main()
