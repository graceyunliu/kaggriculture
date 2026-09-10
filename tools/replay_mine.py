#!/usr/bin/env python3
"""Replay mining (Sep 9): run cand vs opp and log BOTH players' per-day sells by item
(units, avg price realized), money, animals, plants, hands. Usage:
  python3 tools/replay_mine.py candidates/O8_PURE_ANIMAL_THROTTLE.py Opponents/tape_peterparker_106816877.py --seed 1
"""
import sys, argparse
sys.path.insert(0, "/sessions/confident-jolly-fermat/mnt/Kaggriculture")
import mini_engine as me

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
    sells = {0: {}, 1: {}}   # p -> day -> item -> [units, hour_first]
    daily = {0: {}, 1: {}}   # p -> day -> (money, animals, plants, hands)
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
            for m in (act.get("market") or []):
                if m and m[0] == "SELL":
                    d = sells[i].setdefault(day, {})
                    e = d.setdefault(m[1], [0, hour, obs["market"]["prices"].get(m[1], 0)])
                    e[0] += int(m[2])
            farm = obs0.farms[i]
            if day not in daily[i]:
                tiles = farm["tiles"]
                animals = sum(1 for row in tiles for t in row if isinstance(t, dict) and "animal" in t)
                plants = sum(1 for row in tiles for t in row if isinstance(t, dict) and t.get("kind") == "PLANT")
                daily[i][day] = (farm["money"], animals, plants, len(farm["hands"]), len(farm["unlocked_quadrants"]))
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break
    final = [state[0].observation.farms[i]["money"] for i in range(2)]
    return sells, daily, final

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--items", default="MELON,STRAWBERRY,MILK,WOOL,WHEAT")
    args = ap.parse_args()
    sells, daily, final = run(args.a, args.b, args.seed)
    print("final money:", final)
    items = args.items.split(",")
    for p, name in ((0, args.a), (1, args.b)):
        print(f"\n== P{p} {name}")
        print("day  money  anim plants hands quads | " + " ".join(f"{it[:6]:>10s}" for it in items))
        for d in sorted(daily[p]):
            m, an, pl, h, q = daily[p][d]
            cells = []
            for it in items:
                e = sells[p].get(d, {}).get(it)
                cells.append(f"{e[0]:3d}@h{e[1]:<2d}${e[2]:<3.0f}" if e else "    -    ")
            print(f"{d:3d} {m:7.0f} {an:4d} {pl:5d} {h:5d} {q:4d} | " + " ".join(f"{c:>13s}" for c in cells))
