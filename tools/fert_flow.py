#!/usr/bin/env python3
"""Count fertilizer flow for player 0: BUY units, SELL units, PICKUP units, FERTILIZE actions, COLLECT actions."""
import sys
sys.path.insert(0, "/sessions/confident-jolly-fermat/mnt/Kaggriculture")
import mini_engine as me

def run(a, b, seed=1):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(a), me.load_agent(b)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    k = {"buy": 0, "sell": 0, "pickup": 0, "fertilize": 0, "collect": 0, "fert_melon": 0}
    step = 0
    while True:
        obs0 = state[0].observation
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            if i == 0:
                for m in (act.get("market") or []):
                    if m and len(m) >= 3 and m[1] == "FERTILIZER":
                        if m[0] == "BUY_PRODUCT": k["buy"] += int(m[2])
                        elif m[0] == "SELL": k["sell"] += int(m[2])
                farm = obs0.farms[0]
                positions = [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]
                for pos, u in zip(positions, [act.get("farmer") or []] + list(act.get("hands") or [])):
                    if not u: continue
                    if u[0] == "PICKUP" and u[1] == "FERTILIZER": k["pickup"] += int(u[2])
                    elif u[0] == "FERTILIZE":
                        k["fertilize"] += 1
                        t = farm["tiles"][pos[1]][pos[0]]
                        if isinstance(t, dict) and t.get("crop") == "MELON": k["fert_melon"] += 1
                    elif u[0] == "COLLECT_FERTILIZER": k["collect"] += 1
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    k["money"] = state[0].observation.farms[0]["money"]
    return k

if __name__ == "__main__":
    opp = sys.argv[2] if len(sys.argv) > 2 else "candidates/C1.py"
    for c in sys.argv[1].split(","):
        print(c, run(c, opp))
