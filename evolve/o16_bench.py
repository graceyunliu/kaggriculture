import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cascade
C = "candidates/O16_ORCH_ON_O15.py"
if __name__ == "__main__":
    which = sys.argv[1]
    if which == "self":
        seeds = {"dev": range(1, 11), "held": range(11, 31), "fresh": range(31, 51)}[sys.argv[2]]
        r, _ = cascade._eval(C, "candidates/O15_SALE_PRIORITY.py", list(seeds), "master", jobs=5)
        print(f"O16 vs O15 [{sys.argv[2]}]: {r['mean_margin_per_game']:+.0f}/game t={r['t']:.2f} {r['wins']}-{r['losses']} errors={r['agent_errors']}", flush=True)
    else:
        for opp in ["candidates/C1.py", "candidates/O12_EVENING_DEPOSIT.py", "candidates/X1_ORCH_FLATPRIO.py"]:
            r, _ = cascade._eval(C, opp, list(range(1, 11)), "master", jobs=5)
            print(f"O16 vs {os.path.basename(opp)}: {r['mean_margin_per_game']:+.0f}/game t={r['t']:.2f} {r['wins']}-{r['losses']} errors={r['agent_errors']}", flush=True)
