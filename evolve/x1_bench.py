import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade
X1 = "candidates/X1_ORCH_FLATPRIO.py"
if __name__ == "__main__":
    for opp in ["candidates/C1.py", "candidates/V3_15.py", "candidates/O9_MELON_LATEFERT.py"]:
        r, _ = cascade._eval(X1, opp, list(range(1, 11)), "master", jobs=5)
        print(f"X1 vs {os.path.basename(opp)}: {r['mean_margin_per_game']:+.0f}/game t={r['t']:.2f} {r['wins']}-{r['losses']} errors={r['agent_errors']}", flush=True)
