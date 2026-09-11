#!/usr/bin/env python3
"""Per-game action-type counts for BOTH players (moves, each work verb, PASS), plus DROP load sizes."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))))
import mini_engine as me
MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}

def run(a, b, seed):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(a), me.load_agent(b)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    cnt = [{}, {}]; drops = [[], []]
    step = 0
    while True:
        obs0 = state[0].observation
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            inv = obs["private"].get("inventories") or []
            units = [act.get("farmer") or []] + list(act.get("hands") or [])
            for u_idx, u in enumerate(units):
                if not u: cnt[i]["EMPTY"] = cnt[i].get("EMPTY", 0) + 1; continue
                k = "MOVE" if u[0] in MOVES else u[0]
                cnt[i][k] = cnt[i].get(k, 0) + 1
                if u[0] == "DROP" and u_idx < len(inv):
                    drops[i].append(sum(n for it, n in inv[u_idx].items() if it != "WHEAT"))
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    money = [state[0].observation.farms[i]["money"] for i in range(2)]
    return cnt, drops, money

if __name__ == "__main__":
    a, b, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1
    cnt, drops, money = run(a, b, seed)
    keys = sorted(set(cnt[0]) | set(cnt[1]), key=lambda k: -(cnt[0].get(k, 0) + cnt[1].get(k, 0)))
    print(f"money {money}")
    print(f"{'action':18s} {'P0':>7s} {'P1':>7s}")
    for k in keys:
        print(f"{k:18s} {cnt[0].get(k, 0):7d} {cnt[1].get(k, 0):7d}")
    for i in (0, 1):
        d = drops[i]
        print(f"P{i} drops: n={len(d)} avg_load={sum(d)/max(1,len(d)):.1f}")
