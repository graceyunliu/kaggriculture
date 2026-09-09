"""Phase 6 step 1: baseline representativeness check (the Phase-4B-lesson fix).

Runs a candidate chassis via mini_engine.run_game against a sample of real
opponent tapes and computes its own BUY_LAND reach-rate (fraction of games
where it ever buys past the starting quadrant), to compare against Phase 5's
measured real-replay figure (59.3%, 89/150) before trusting it as a baseline
for a causal intervention test.
"""
import sys, glob, random, json
sys.path.insert(0, ".")
from mini_engine import run_game

def reach_rate(agent, opponents, seeds):
    reach = 0
    total = 0
    rows = []
    for opp in opponents:
        for seed in seeds:
            try:
                r = run_game(agent, opp, seed, "master", None, trace=True)
            except Exception as e:
                print("ERR", opp, seed, e)
                continue
            for seat_idx, t in enumerate(r["trace"]):
                maxland = max(t["land"]) if t["land"] else 1
                total += 1
                reached = maxland >= 2
                reach += int(reached)
                rows.append({"opp": opp, "seed": seed, "seat": seat_idx, "max_land": maxland})
    return reach, total, rows

if __name__ == "__main__":
    opps = sorted(glob.glob("Opponents/tape_*.py"))
    random.Random(7).shuffle(opps)
    opps = opps[:8]
    seeds = [1, 2, 3]
    out = {}
    for cand in ["candidates/V3_12.py", "candidates/V3_15.py"]:
        reach, total, rows = reach_rate(cand, opps, seeds)
        out[cand] = {"reach": reach, "total": total, "rate": round(reach / total, 4) if total else None}
        print(cand, out[cand])
    out["phase5_measured_real_replay_rate"] = {"reach": 89, "total": 150, "rate": 0.5933}
    json.dump(out, open("/tmp/phase6_baseline_check.json", "w"), indent=2)
