import sys, math
sys.path.insert(0, ".")
from mini_engine import run_game

BASE = "experiments/REPLAY_STATE_POLICY_AUDIT_PHASE7/baseline_V3_15.py"
VAR = "experiments/REPLAY_STATE_POLICY_AUDIT_PHASE7/variant_melon_aggressive.py"

def per_game_money(agent, opp, seeds):
    out = []
    for s in seeds:
        r = run_game(agent, opp, s, "master", None, trace=False)
        out.append(r["money"][0])
        r2 = run_game(opp, agent, s, "master", None, trace=False)
        out.append(r2["money"][1])
    return out

def paired_t(b, v):
    diffs = [vv - bb for vv, bb in zip(v, b)]
    n = len(diffs)
    mean_d = sum(diffs) / n
    sd = (sum((d - mean_d) ** 2 for d in diffs) / (n - 1)) ** 0.5
    se = sd / math.sqrt(n)
    t = mean_d / se if se > 0 else float("nan")
    return n, mean_d, sd, t

if __name__ == "__main__":
    opps = ["Opponents/tape_mtn_105853290.py", "Opponents/tape_kwa_105860490.py",
            "Opponents/tape_furina_105708344.py"]
    print("=== matched seeds 1-20 ===")
    for opp in opps[:1]:
        b = per_game_money(BASE, opp, list(range(1, 21)))
        v = per_game_money(VAR, opp, list(range(1, 21)))
        n, md, sd, t = paired_t(b, v)
        print(opp, "n", n, "mean_diff", round(md, 1), "t", round(t, 3))
    print("=== fresh seeds 101-120, 3 opponents ===")
    for opp in opps:
        b = per_game_money(BASE, opp, list(range(101, 121)))
        v = per_game_money(VAR, opp, list(range(101, 121)))
        n, md, sd, t = paired_t(b, v)
        print(opp, "n", n, "mean_diff", round(md, 1), "t", round(t, 3))
