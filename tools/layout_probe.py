#!/usr/bin/env python3
"""Layout probe: mean shed-distance of animal / melon / strawberry / wheat tiles at given days, both players."""
import sys, argparse
sys.path.insert(0, "/sessions/confident-jolly-fermat/mnt/Kaggriculture")
import mini_engine as me
SHED = [(4, 4), (5, 4), (4, 5), (5, 5)]
def sd(x, y): return min(abs(x - a) + abs(y - b) for a, b in SHED)

def run(a, b, seed, days, acc):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(a), me.load_agent(b)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        if hour == 12 and day in days:
            for i in (0, 1):
                tiles = obs0.farms[i]["tiles"]
                for y, row in enumerate(tiles):
                    for x, t in enumerate(row):
                        if not isinstance(t, dict): continue
                        k = "animal" if "animal" in t else t.get("crop") if t.get("kind") == "PLANT" else None
                        if k: acc[i].setdefault(day, {}).setdefault(k, []).append(sd(x, y))
        for i in (0, 1):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--seeds", default="1-3"); ap.add_argument("--days", default="5,12,20")
    args = ap.parse_args(); lo, hi = map(int, args.seeds.split("-")); days = {int(d) for d in args.days.split(",")}
    acc = [{}, {}]
    for s in range(lo, hi + 1): run(args.a, args.b, s, days, acc)
    for d in sorted(days):
        print(f"day {d}:")
        for i in (0, 1):
            row = acc[i].get(d, {})
            print(f"  P{i}: " + "  ".join(f"{k}: n={len(v)/(hi-lo+1):.1f} dist={sum(v)/len(v):.2f}" for k, v in sorted(row.items())))
