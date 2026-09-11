#!/usr/bin/env python3
"""Melon-side vs strawberry-side decomposition, O26 vs O31 (Sep 11): paired same-seed runs, records
MELON and STRAWBERRY units sold + revenue for farm 0 only, to see which side of the O30/O31 wash the
money actually moves on.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/o31_decompose.py --opp TAPE --seeds 11-25
"""
import sys, os, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me

TRACK = {"MELON", "STRAWBERRY"}

def play(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    trades = []; orig = mod._commit_unit
    def rec(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig(op, item, price, farm, private, market, shed_capacity)
        if ok and op == "SELL" and item in TRACK: trades.append((id(farm), item, price))
        return ok
    mod._commit_unit = rec
    stats = {"MELON": [0, 0.0], "STRAWBERRY": [0, 0.0]}  # units, revenue (farm 0 only)
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        farm0_id = id(o.farms[0])
        for fid, item, price in trades:
            if fid == farm0_id:
                stats[item][0] += 1; stats[item][1] += price
        trades.clear()
        if all(s.status == "DONE" for s in state) or step >= steps: break
    mod._commit_unit = orig
    return o.farms[0]["money"], stats


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--opp", required=True); ap.add_argument("--seeds", default="11-25")
    a = ap.parse_args(); os.chdir(ROOT)
    lo, hi = map(int, a.seeds.split("-")); seeds = range(lo, hi + 1)
    agg = {"O26": {"money": 0.0, "MELON_u": 0, "MELON_r": 0.0, "STRAWBERRY_u": 0, "STRAWBERRY_r": 0.0},
           "O31": {"money": 0.0, "MELON_u": 0, "MELON_r": 0.0, "STRAWBERRY_u": 0, "STRAWBERRY_r": 0.0}}
    n = 0
    for s in seeds:
        m26, st26 = play("candidates/O26_CARROT_SIZING.py", a.opp, s)
        m31, st31 = play("candidates/O31_MELON_CATASTROPHIC_YIELD.py", a.opp, s)
        n += 1
        agg["O26"]["money"] += m26; agg["O31"]["money"] += m31
        for tag, st in (("O26", st26), ("O31", st31)):
            agg[tag]["MELON_u"] += st["MELON"][0]; agg[tag]["MELON_r"] += st["MELON"][1]
            agg[tag]["STRAWBERRY_u"] += st["STRAWBERRY"][0]; agg[tag]["STRAWBERRY_r"] += st["STRAWBERRY"][1]
    print(f"opp={os.path.basename(a.opp)} seeds {lo}-{hi} (n={n})")
    for tag in ("O26", "O31"):
        A = agg[tag]
        print(f"  {tag}: money/game {A['money']/n:,.0f}  MELON {A['MELON_u']/n:.1f}u ${A['MELON_r']/n:,.0f} "
              f"(avg ${A['MELON_r']/max(1,A['MELON_u']):.0f}/u)  STRAWBERRY {A['STRAWBERRY_u']/n:.1f}u "
              f"${A['STRAWBERRY_r']/n:,.0f} (avg ${A['STRAWBERRY_r']/max(1,A['STRAWBERRY_u']):.0f}/u)")
    dM = (agg["O31"]["MELON_r"] - agg["O26"]["MELON_r"]) / n
    dS = (agg["O31"]["STRAWBERRY_r"] - agg["O26"]["STRAWBERRY_r"]) / n
    dMoney = (agg["O31"]["money"] - agg["O26"]["money"]) / n
    print(f"  delta O31-O26: MELON revenue {dM:+,.0f}/game  STRAWBERRY revenue {dS:+,.0f}/game  "
          f"(sum {dM+dS:+,.0f})  total own-money delta {dMoney:+,.0f}/game")
