import sys
sys.path.insert(0, "/sessions/vigilant-great-cori/mnt/Kaggriculture/evolve")
from cascade import _eval, DEV_SEEDS

PAIRS = [
    ("candidates/O2_plus_sharedstock.py", "candidates/O2_STATE_OWNERSHIP.py", "sharedstock alone vs O2"),
    ("candidates/O2_plus_bundle.py", "candidates/O2_STATE_OWNERSHIP.py", "bundle alone vs O2"),
    ("candidates/O3_PRODUCTIVE_SERVICE.py", "candidates/O2_plus_bundle.py", "sharedstock's marginal add on top of bundle (=O3 vs bundle-alone)"),
    ("candidates/O3_PRODUCTIVE_SERVICE.py", "candidates/O2_plus_sharedstock.py", "bundle's marginal add on top of sharedstock (=O3 vs sharedstock-alone)"),
]

def main():
    for a, b, label in PAIRS:
        r, dt = _eval(a, b, DEV_SEEDS, "master", 4)
        print(f"{label}: margin={r['mean_margin_per_game']:+,.0f} t={r['t']:.2f} {r['wins']}-{r['losses']} errs={r['agent_errors']}", flush=True)

if __name__ == "__main__":
    main()
