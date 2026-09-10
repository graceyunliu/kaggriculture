#!/usr/bin/env python3
"""Behavioral verification for the O4 bundle-decomposition ablation (Sep 9).
Runs one game per candidate (seat 0 vs C1 seat 1, seed 1) and tallies the specific
observable action patterns each mechanism should (or should not) produce, so a margin
result is never trusted without confirming the code path actually fired.
"""
import sys, copy
sys.path.insert(0, "/sessions/vigilant-great-cori/mnt/Kaggriculture")
import mini_engine as me

def verify(agent_path, opp="candidates/C1.py", seed=1):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(agent_path), me.load_agent(opp)]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    tpd = int(cfg["turnsPerDay"]); steps = int(cfg["episodeSteps"])

    drop_events = []          # (day, hour) for player 0's DROP actions on days < 28
    off_hour_capital = []     # (day, hour, verb, item) for BUY_*/HIRE at hour not in {0,1,2}
    sell_events = []          # (day, hour, item) for SELL market actions at hour not in {0} and day<28
    skip_evidence = 0          # count of turns where a hand near a fed/cared-not-due animal does something else (proxy, cross-checked against trace.py's own metric instead)

    step = 0
    while True:
        obs0 = state[0].observation
        day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            if i == 0:
                farmer_act = act.get("farmer") or []
                hand_acts = act.get("hands") or []
                market_act = act.get("market") or []
                for a in [farmer_act] + list(hand_acts):
                    if a and a[0] == "DROP" and day < 28:
                        drop_events.append((day, hour))
                for m in market_act:
                    if m and m[0] in ("BUY_PRODUCT", "BUY_SEED", "BUY_ANIMAL") and hour not in (0, 1, 2):
                        off_hour_capital.append((day, hour, m[0], m[1] if len(m) > 1 else None))
                    if m and m[0] == "SELL" and hour != 0 and day < 28:
                        sell_events.append((day, hour, m[1] if len(m) > 1 else None))
                for a in [farmer_act] + list(hand_acts):
                    if a and a[0] == "HIRE" and hour not in (0, 1, 2):
                        off_hour_capital.append((day, hour, "HIRE", None))
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            break
        if step >= steps:
            break
    return {
        "drop_events_days<28": len(drop_events),
        "drop_sample": drop_events[:5],
        "off_hour_capital_events": len(off_hour_capital),
        "off_hour_sample": off_hour_capital[:5],
        "sell_events_offhour_days<28": len(sell_events),
        "sell_sample": sell_events[:5],
        "final_money_p0": state[0].observation.farms[0]["money"],
    }

if __name__ == "__main__":
    for cand in sys.argv[1:]:
        r = verify(cand)
        print(f"{cand}: {r}", flush=True)
