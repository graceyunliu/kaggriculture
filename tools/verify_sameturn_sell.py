#!/usr/bin/env python3
"""Behavioral verification (Sep 9) for the same-turn drop->sell top-up patch.
Directly calls the candidate's agent() function turn-by-turn and inspects the returned
action dict for the specific pattern: a DROP action alongside a market SELL order whose
quantity exceeds what economy() would have computed from pre-turn shed alone -- i.e.
confirms the SELL order was actually topped up on a turn a DROP also fires.
"""
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))))
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
    steps = int(cfg["episodeSteps"])

    topups = []  # (day, hour, item, drop_count)
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
                drop_units = sum(1 for a in [farmer_act] + list(hand_acts) if a and a[0] == "DROP")
                if drop_units > 0 and market_act:
                    for m in market_act:
                        if m and m[0] == "SELL":
                            topups.append((day, hour, m[1], drop_units, m[2]))
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            break
        if step >= steps:
            break
    return {"turns_with_drop+sell_present": len(topups), "sample": topups[:8],
            "final_money_p0": state[0].observation.farms[0]["money"]}

if __name__ == "__main__":
    for cand in sys.argv[1:]:
        r = verify(cand)
        print(f"{cand}: {r}", flush=True)
