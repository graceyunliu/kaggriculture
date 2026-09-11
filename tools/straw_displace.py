#!/usr/bin/env python3
"""Displacement trace for one dying strawberry tile (Sep 11): hooks the candidate module's own
_crop_pools (returns the live urgent/water/harvest/etc pools each time a free unit rebuilds its
sweep) and S["routes"] (units currently committed to a multi-tile sweep) to see, hour by hour on
the day a target tile is urgent, whether it ever appears in a pool snapshot and how many units are
free (routeless) vs total, i.e. whether the miss is a PRIORITY problem (it's in the pool but a unit
picks something else) or a CAPACITY problem (no free unit ever rebuilds a sweep that day) or an
INVISIBILITY problem (it's never in the pool at all -> not flagged urgent when we think it should be).

Usage: KAGG_FIXED_SHOPS=1 python3 tools/straw_displace.py CAND --opp TAPE --seed 11 --tile X,Y --day D
"""
import sys, os, argparse, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me


def run(cand, opp, seed, target, watch_days):
    spec = importlib.util.spec_from_file_location("cand_mod", cand)
    cmod = importlib.util.module_from_spec(spec); spec.loader.exec_module(cmod)
    log = []
    orig_pools = cmod._crop_pools
    def traced_pools(v, seeds_left, day):
        pools = orig_pools(v, seeds_left, day)
        if day in watch_days:
            in_urgent = target in pools["urgent"]
            in_water = target in pools["water"]
            n_routes = len(cmod.S["routes"])
            log.append({"day": day, "in_urgent": in_urgent, "in_water": in_water, "n_routes": n_routes})
        return pools
    cmod._crop_pools = traced_pools

    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [cmod.agent, me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    n_units_hist = []
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if i == 0 and obs["day"] in watch_days:
                farm = obs["farms"][0]
                n_units_hist.append((obs["day"], obs["hour"], 1 + len(farm["hands"])))
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return log, n_units_hist


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--opp", required=True)
    ap.add_argument("--seed", type=int, default=11); ap.add_argument("--tile", required=True)
    ap.add_argument("--days", default="12-15")
    a = ap.parse_args(); os.chdir(ROOT)
    x, y = map(int, a.tile.split(",")); target = (x, y)
    lo, hi = map(int, a.days.split("-")); watch_days = set(range(lo, hi + 1))
    log, n_units_hist = run(a.cand, a.opp, a.seed, target, watch_days)
    print(f"Target tile {target}, days {lo}-{hi}: {len(log)} sweep-rebuild snapshots recorded")
    by_day = {}
    for e in log:
        by_day.setdefault(e["day"], []).append(e)
    for day, es in sorted(by_day.items()):
        n_urgent = sum(1 for e in es if e["in_urgent"])
        n_water = sum(1 for e in es if e["in_water"])
        print(f"  day {day}: {len(es)} sweep-rebuilds observed; target in URGENT pool at {n_urgent}, "
              f"in WATER pool at {n_water}; n_routes(committed units) range "
              f"{min(e['n_routes'] for e in es)}-{max(e['n_routes'] for e in es)}")
    print("  unit count (farmer+hands) sample:", " ".join(f"d{d}h{h}:{n}" for d, h, n in n_units_hist[::6]))
