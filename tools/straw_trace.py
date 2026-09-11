#!/usr/bin/env python3
"""Single-tile strawberry trace (Sep 11): reads the engine's own consecutive_unwatered counter directly
(vendor/.../kaggriculture.py _daily_refresh_plants: consecutive_unwatered>=2 -> WEED, checked once per day
at the day rollover) instead of inferring streaks from watered_today snapshots. For every strawberry tile
that dies before age 10 on farm 0, print its full day-by-day consecutive_unwatered history plus, for the
turn before each miss, what our dispatcher's action was for the nearest free unit (to see if it was ever
even assigned).

Usage: KAGG_FIXED_SHOPS=1 python3 tools/straw_trace.py CAND --opp TAPE --seed 11 [--farm 0]
"""
import sys, os, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me


def run(cand, opp, seed, farm_idx):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    prev = None
    histories = {}   # pos -> list of (day, hour, cu, kind) after each engine step
    while True:
        acts = [None, None]
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act; acts[i] = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation; day, hour = o.day, o.hour
        tiles = o.farms[farm_idx]["tiles"]
        for y, row in enumerate(tiles):
            for x, t in enumerate(row):
                pos = (x, y)
                if isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("crop") == "STRAWBERRY":
                    age = day - t["planted_day"]
                    if age < 10:
                        h = histories.setdefault((pos, t["planted_day"]), [])
                        h.append((day, hour, t.get("consecutive_unwatered"), t.get("watered_today"), "PLANT"))
                elif prev is not None and isinstance(prev[y][x], dict) and prev[y][x].get("kind") == "PLANT" \
                        and prev[y][x].get("crop") == "STRAWBERRY" and isinstance(t, dict) and t.get("kind") == "WEED":
                    pd = prev[y][x]["planted_day"]
                    age = day - pd
                    if age < 10:
                        h = histories.setdefault((pos, pd), [])
                        h.append((day, hour, "->WEED", None, "DIED"))
        prev = [[dict(t) if isinstance(t, dict) else t for t in row] for row in tiles]
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return histories


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--opp", required=True)
    ap.add_argument("--seed", type=int, default=11); ap.add_argument("--farm", type=int, default=0)
    a = ap.parse_args(); os.chdir(ROOT)
    histories = run(a.cand, a.opp, a.seed, a.farm)
    died = {k: v for k, v in histories.items() if v[-1][4] == "DIED"}
    print(f"{len(died)} early strawberry deaths (of {len(histories)} tracked young plantings) on farm {a.farm}, seed {a.seed}")
    for (pos, pday), h in sorted(died.items(), key=lambda kv: kv[0][1])[:6]:
        print(f"\nTile {pos} planted day {pday}:")
        last_day = None
        for day, hour, cu, watered, kind in h:
            if day != last_day:
                print(f"  d{day}h{hour}: consecutive_unwatered={cu} watered_today={watered} {kind}")
                last_day = day
