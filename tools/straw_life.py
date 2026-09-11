#!/usr/bin/env python3
"""Strawberry lifecycle decomposition (Sep 11): for each strawberry planting on both farms, track its
full life (planted -> dies/game end) and record: total units harvested, age at death, how many of its
production nights (age 9,11,13,15,...) were watered, how many were fertilized-covered, and whether it
was ever fert-eligible-but-unfertilized on a production night. This separates "fertilizer didn't arrive"
(O28's tested hypothesis, closed) from "watering missed on a production night" and "died early" (short
lifespan means fewer of the 7.5 assumed units are ever reachable).

Usage: KAGG_FIXED_SHOPS=1 python3 tools/straw_life.py CAND --opp TAPE --seeds 11-14
"""
import sys, os, argparse, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me

FIRST, MAX_DAY, INTERVAL, MAX_YIELD = 10, 10, 2, 4


def prod_day(age):
    return age >= FIRST and (age - FIRST) % INTERVAL == 0


def run(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    prev = [None, None]
    lives = [{}, {}]     # pos -> life dict, keyed while alive
    done = [[], []]       # finished lives
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation; day, hour = o.day, o.hour
        for p in range(2):
            tiles = o.farms[p]["tiles"]
            pt = prev[p]
            for y, row in enumerate(tiles):
                for x, t in enumerate(row):
                    pos = (x, y)
                    is_straw = isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("crop") == "STRAWBERRY"
                    q = pt[y][x] if pt is not None else None
                    was_straw = isinstance(q, dict) and q.get("kind") == "PLANT" and q.get("crop") == "STRAWBERRY"
                    if is_straw:
                        L = lives[p].get(pos)
                        if L is None or L["planted_day"] != t["planted_day"]:
                            if L is not None: done[p].append(L)
                            L = {"planted_day": t["planted_day"], "total": 0, "prod_nights": 0,
                                 "watered_prod": 0, "fert_covered_prod": 0, "last_age": 0, "hour0_seen": set(),
                                 "pre_prod_days": 0, "pre_prod_watered": 0, "pre_prod_misses": 0, "max_streak": 0, "streak": 0}
                            lives[p][pos] = L
                        age = day - t["planted_day"]
                        L["last_age"] = age
                        if was_straw and q.get("yield_units", 0) > t.get("yield_units", 0):
                            L["total"] += q["yield_units"] - t["yield_units"]
                        if hour == 0 and age not in L["hour0_seen"]:
                            L["hour0_seen"].add(age)
                            watered = bool(q is not None and isinstance(q, dict) and q.get("watered_today"))
                            if age < FIRST:
                                L["pre_prod_days"] += 1
                                if watered:
                                    L["pre_prod_watered"] += 1; L["streak"] = 0
                                else:
                                    L["pre_prod_misses"] += 1; L["streak"] += 1
                                    L["max_streak"] = max(L["max_streak"], L["streak"])
                            if prod_day(age):
                                L["prod_nights"] += 1
                                if watered:
                                    L["watered_prod"] += 1
                                if q is not None and isinstance(q, dict) and q.get("fertilized_until_day", -1) >= day - 1:
                                    L["fert_covered_prod"] += 1
                    elif was_straw and pos in lives[p]:
                        L = lives[p].pop(pos)
                        if isinstance(q, dict) and q.get("yield_units", 0) > 0:
                            L["total"] += q["yield_units"]
                        done[p].append(L)
            prev[p] = [[dict(t) if isinstance(t, dict) else t for t in row] for row in tiles]
        if all(s.status == "DONE" for s in state) or step >= steps: break
    for p in range(2):
        for L in lives[p].values(): done[p].append(L)
    return done


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--opp", required=True); ap.add_argument("--seeds", default="11-14")
    a = ap.parse_args(); os.chdir(ROOT)
    lo, hi = map(int, a.seeds.split("-"))
    names = [os.path.basename(a.cand), os.path.basename(a.opp)]
    agg = [[], []]
    for s in range(lo, hi + 1):
        done = run(a.cand, a.opp, s)
        for p in range(2): agg[p].extend(done[p])
    for p in range(2):
        lives = agg[p]
        n = len(lives)
        if n == 0:
            print(f"{names[p]}: no strawberry plantings"); continue
        tot = sum(L["total"] for L in lives)
        avg_age = sum(L["last_age"] for L in lives) / n
        avg_prod = sum(L["prod_nights"] for L in lives) / n
        avg_watered = sum(L["watered_prod"] for L in lives) / n
        avg_fert = sum(L["fert_covered_prod"] for L in lives) / n
        # theoretical max units if every prod night were both watered AND fertilized: max_yield per interval batch
        watered_rate = sum(L["watered_prod"] for L in lives) / max(1, sum(L["prod_nights"] for L in lives))
        fert_rate = sum(L["fert_covered_prod"] for L in lives) / max(1, sum(L["prod_nights"] for L in lives))
        pre_died = sum(1 for L in lives if L["last_age"] < FIRST)
        pre_watered_rate = sum(L["pre_prod_watered"] for L in lives) / max(1, sum(L["pre_prod_days"] for L in lives))
        avg_max_streak = sum(L["max_streak"] for L in lives) / n
        print(f"{names[p]}: {n} plantings, {tot/n:.2f} units/planting avg, avg death age {avg_age:.1f} "
              f"(first prod night age {FIRST}), avg prod-nights-experienced {avg_prod:.2f}, "
              f"watered-on-prod-night rate {watered_rate:.0%}, fert-covered-on-prod-night rate {fert_rate:.0%}")
        print(f"  DIED BEFORE FIRST PRODUCTION (age<{FIRST}): {pre_died}/{n} ({pre_died/n:.0%}); "
              f"pre-production watered-day rate {pre_watered_rate:.0%}; avg longest missed-water streak {avg_max_streak:.1f}")
        # age histogram
        ages = collections.Counter(L["last_age"] for L in lives)
        print("  death-age histogram: " + " ".join(f"{a}:{n2}" for a, n2 in sorted(ages.items())))
