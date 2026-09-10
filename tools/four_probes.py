#!/usr/bin/env python3
"""Four probes on cand vs opp over seeds (P0 = cand, P1 = opp):
 1. FERTILIZER: sells by hour (units, avg price) for both players
 2. WOOL: sells by hour (units, avg price) for both players
 3. ROT: one-shot plant tiles (P0) whose yield_units dropped without a HARVEST/DIG -> units lost, tiles weeded by rot
 4. EARLY IDLE: P0 PASS turns by day (0-9) and by hour band, vs pending work that existed at those turns
"""
import sys, argparse
sys.path.insert(0, "/sessions/confident-jolly-fermat/mnt/Kaggriculture")
import mini_engine as me
ONE_SHOT = {"WHEAT", "CARROT", "MELON"}

def run(a, b, seed, acc):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(a), me.load_agent(b)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    prev_tiles = None
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        acts = []
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            acts.append(act)
            for m in (act.get("market") or []):
                if m and len(m) >= 3 and m[0] == "SELL" and m[1] in ("FERTILIZER", "WOOL"):
                    n = min(int(m[2]), obs["private"]["shed"].get(m[1], 0))
                    if n > 0:
                        e = acc[m[1]][i].setdefault(hour, [0, 0.0])
                        e[0] += n; e[1] += n * obs["market"]["prices"].get(m[1], 0)
            state[i].action = act
        # probe 4: P0 idle in early days
        if day <= 9:
            units = [acts[0].get("farmer") or []] + list(acts[0].get("hands") or [])
            npass = sum(1 for u in units if not u or u[0] == "PASS")
            d = acc["idle"].setdefault(day, [0, 0]); d[0] += npass; d[1] += len(units)
        # probe 3: rot on P0 tiles (compare before/after interpreter, excluding tiles acted on)
        farm0 = obs0.farms[0]
        acted = set()
        positions = [tuple(farm0["farmer"])] + [tuple(h) for h in farm0["hands"]]
        for pos, u in zip(positions, [acts[0].get("farmer") or []] + list(acts[0].get("hands") or [])):
            if u and u[0] in ("HARVEST", "DIG", "PLANT"): acted.add(pos)
        before = {}
        for y, row in enumerate(farm0["tiles"]):
            for x, t in enumerate(row):
                if isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("crop") in ONE_SHOT:
                    before[(x, y)] = (t.get("crop"), t.get("yield_units", 0))
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        farm0 = state[0].observation.farms[0]
        for (x, y), (crop, yu) in before.items():
            if (x, y) in acted: continue
            t = farm0["tiles"][y][x]
            if isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("yield_units", 0) < yu:
                acc["rot_units"] += yu - t.get("yield_units", 0)
            elif isinstance(t, dict) and t.get("kind") == "WEED" and yu > 0:
                acc["rot_units"] += yu; acc["rot_weeded"] += 1
            elif isinstance(t, dict) and t.get("kind") == "WEED":
                acc["unwatered_weeded"] += 1
        if all(s.status == "DONE" for s in state) or step >= steps: break
    acc["money"][0] += state[0].observation.farms[0]["money"]; acc["money"][1] += state[0].observation.farms[1]["money"]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--seeds", default="1-5")
    args = ap.parse_args(); lo, hi = map(int, args.seeds.split("-")); seeds = list(range(lo, hi + 1)); n = len(seeds)
    acc = {"FERTILIZER": [{}, {}], "WOOL": [{}, {}], "idle": {}, "rot_units": 0, "rot_weeded": 0, "unwatered_weeded": 0, "money": [0, 0]}
    for s in seeds: run(args.a, args.b, s, acc)
    print(f"n={n}  mean money P0 {acc['money'][0]/n:.0f}  P1 {acc['money'][1]/n:.0f}")
    for item in ("FERTILIZER", "WOOL"):
        print(f"\n[{item}] sells by hour (units/game @ avg price)")
        for i in (0, 1):
            tot = sum(v[0] for v in acc[item][i].values()); rev = sum(v[1] for v in acc[item][i].values())
            hrs = " ".join(f"h{h}:{v[0]/n:.0f}@${v[1]/max(1,v[0]):.0f}" for h, v in sorted(acc[item][i].items()))
            print(f"  P{i}: total {tot/n:.0f}u ${rev/n:.0f} (avg ${rev/max(1,tot):.0f})  | {hrs}")
    print(f"\n[ROT] P0 one-shot yield units lost to decay/game: {acc['rot_units']/n:.1f}; tiles rotted to weed: {acc['rot_weeded']/n:.1f}; tiles weeded by non-watering: {acc['unwatered_weeded']/n:.1f}")
    print("\n[EARLY IDLE] P0 PASS share by day:")
    print("  " + " ".join(f"d{d}:{v[0]/max(1,v[1]):.0%}({v[1]/n/24:.1f}u)" for d, v in sorted(acc["idle"].items())))
