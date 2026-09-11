#!/usr/bin/env python3
"""Average per-day gap profile of cand vs opp over seeds (both seats): money, animals, plants, hands(h3),
and cumulative sales units + revenue by item. Usage: gap_profile.py cand opp --seeds 1-10"""
import sys, argparse
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))))
import mini_engine as me
ITEMS = ["MELON", "STRAWBERRY", "MILK", "WOOL", "WHEAT", "TOMATO", "CARROT", "FERTILIZER"]

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
    daily = {0: {}, 1: {}}
    rev = {0: {it: 0.0 for it in ITEMS}, 1: {it: 0.0 for it in ITEMS}}
    units = {0: {it: 0 for it in ITEMS}, 1: {it: 0 for it in ITEMS}}
    step = 0
    while True:
        obs0 = state[0].observation
        day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            for m in (act.get("market") or []):
                if m and len(m) >= 3 and m[0] == "SELL" and m[1] in ITEMS:
                    n = min(int(m[2]), obs["private"]["shed"].get(m[1], 0))
                    units[i][m[1]] += n
                    rev[i][m[1]] += n * obs["market"]["prices"].get(m[1], 0)
            farm = obs0.farms[i]
            if hour == 3:
                tiles = farm["tiles"]
                animals = sum(1 for row in tiles for t in row if isinstance(t, dict) and "animal" in t)
                plants = sum(1 for row in tiles for t in row if isinstance(t, dict) and t.get("kind") == "PLANT")
                daily[i][day] = (farm["money"], animals, plants, len(farm["hands"]), len(farm["unlocked_quadrants"]))
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    final = [state[0].observation.farms[i]["money"] for i in range(2)]
    return daily, rev, units, final

def _parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-")
            out.extend(range(int(lo), int(hi) + 1))
        else:
            out.append(int(part))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--seeds", default="1-10")
    args = ap.parse_args()
    seeds = _parse_seeds(args.seeds)
    acc = {0: {}, 1: {}}; R = {0: {it: 0.0 for it in ITEMS}, 1: {it: 0.0 for it in ITEMS}}; U = {0: {it: 0 for it in ITEMS}, 1: {it: 0 for it in ITEMS}}
    finals = [0.0, 0.0]
    for s in seeds:
        daily, rev, units, final = run(args.a, args.b, s)
        for i in (0, 1):
            finals[i] += final[i] / len(seeds)
            for it in ITEMS:
                R[i][it] += rev[i][it] / len(seeds); U[i][it] += units[i][it] / len(seeds)
            for d, row in daily[i].items():
                a = acc[i].setdefault(d, [0.0] * 5)
                for k in range(5): a[k] += row[k] / len(seeds)
    print(f"mean final money: cand {finals[0]:.0f}  opp {finals[1]:.0f}   (n={len(seeds)})")
    print("day |   money cand/opp   | animals c/o | plants c/o | hands c/o | quads c/o")
    for d in sorted(acc[0]):
        c = acc[0][d]; o = acc[1].get(d, [0] * 5)
        print(f"{d:3d} | {c[0]:8.0f} /{o[0]:8.0f} | {c[1]:5.1f}/{o[1]:5.1f} | {c[2]:5.1f}/{o[2]:5.1f} | {c[3]:4.1f}/{o[3]:4.1f} | {c[4]:3.1f}/{o[4]:3.1f}")
    print("\nmean sales (units, revenue) cand vs opp:")
    for it in ITEMS:
        print(f"  {it:10s} cand {U[0][it]:6.1f}u ${R[0][it]:7.0f}   opp {U[1][it]:6.1f}u ${R[1][it]:7.0f}   gap ${R[0][it]-R[1][it]:+7.0f}")
