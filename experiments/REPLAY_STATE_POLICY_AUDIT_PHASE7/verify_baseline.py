import sys, glob, random
sys.path.insert(0, ".")
from mini_engine import run_game

def melon_rate(agent, opp, seed):
    r = run_game(agent, opp, seed, "master", None, trace=True)
    opp_days = 0
    act_days = 0
    for t in r["trace"]:
        shed_series = t.get("shed", [])
        sales_series = t.get("sales", [])
        for day, sh in enumerate(shed_series):
            ms = sh.get("MELON", 0) if isinstance(sh, dict) else 0
            if ms > 0:
                opp_days += 1
                s = sales_series[day] if day < len(sales_series) else {}
                mv = s.get("MELON", (0, 0)) if isinstance(s, dict) else (0, 0)
                if isinstance(mv, tuple) and mv[0] > 0:
                    act_days += 1
    return opp_days, act_days

if __name__ == "__main__":
    opp = "Opponents/tape_mtn_105853290.py"
    bo, ba = 0, 0
    for s in range(1, 6):
        o, a = melon_rate("candidates/V3_15.py", opp, s)
        bo += o
        ba += a
    print("V3_15 melon opportunity_days", bo, "action_days", ba,
          "rate", ba / bo if bo else None,
          " (Phase 4A historical figure: ~0.0063)")
