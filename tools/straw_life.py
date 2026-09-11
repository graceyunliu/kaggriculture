#!/usr/bin/env python3
"""Strawberry (ongoing crop) life accounting, both farms: per planting day -> plantings, units harvested, fertilized
production nights, unwatered production nights, and end (harvest count / death). Explains units-per-planting gaps."""
import sys, os, argparse, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me

FERT_AGE = [collections.Counter(), collections.Counter()]

def run(cand, opp, seed, crop):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    cd = mod.CROPS[crop]
    life = [{}, {}]   # (pos, planted_day) -> dict
    prev = [None, None]
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
            farm = state[0].observation.farms[i]
            units = [act.get("farmer") or []] + list(act.get("hands") or [])
            positions = [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]
            for u, ua in enumerate(units):
                if ua and ua[0] == "FERTILIZE" and u < len(positions):
                    x, y = positions[u]; t = farm["tiles"][y][x]
                    if isinstance(t, dict) and t.get("kind") == "PLANT" and t["crop"] == crop:
                        FERT_AGE[i][state[0].observation.day - t["planted_day"]] += 1
        o0 = state[0].observation; day, hour = o0.day, o0.hour
        # end-of-day snapshot BEFORE the night tick: fertilized/watered status on production nights
        if hour == 23:
            for p in range(2):
                for y, row in enumerate(o0.farms[p]["tiles"]):
                    for x, t in enumerate(row):
                        if isinstance(t, dict) and t.get("kind") == "PLANT" and t["crop"] == crop:
                            k = ((x, y), t["planted_day"]); L = life[p].setdefault(k, collections.Counter())
                            d = day + 1 - t["planted_day"] - cd["first_yield_day"]
                            if d >= 0 and d % cd["interval"] == 0 and d // cd["interval"] + 1 <= cd["max_yield"]:
                                L["prod_nights"] += 1
                                if t.get("fertilized_until_day", -1) >= day and t["watered_today"]: L["fert_prod"] += 1
                                if t.get("fertilized_until_day", -1) >= day and not t["watered_today"]: L["fert_unw"] += 1
                                if not t["watered_today"]: L["unwatered_prod"] += 1
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        for p in range(2):
            tiles = o.farms[p]["tiles"]; pt = prev[p]
            for y, row in enumerate(tiles):
                for x, t in enumerate(row):
                    if pt is None: continue
                    q = pt[y][x]
                    if isinstance(q, dict) and q.get("kind") == "PLANT" and q["crop"] == crop:
                        k = ((x, y), q["planted_day"]); L = life[p].setdefault(k, collections.Counter())
                        same = isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("planted_day") == q["planted_day"]
                        if same and t["yield_units"] < q["yield_units"]: L["units"] += q["yield_units"] - t["yield_units"]
                        if not same:
                            L["units"] += q["yield_units"] if not (isinstance(t, dict) and t.get("kind") == "WEED") else 0
                            L["end"] = "weed" if (isinstance(t, dict) and t.get("kind") == "WEED") else "gone"; L["end_day"] = o.day
            prev[p] = [[dict(t) if isinstance(t, dict) else t for t in row] for row in tiles]
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return life

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--opp", required=True); ap.add_argument("--seeds", default="11-14"); ap.add_argument("--crop", default="STRAWBERRY")
    a = ap.parse_args(); os.chdir(ROOT); lo, hi = map(int, a.seeds.split("-")); seeds = list(range(lo, hi + 1))
    agg = [collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)]
    for s in seeds:
        life = run(a.cand, a.opp, s, a.crop)
        for p in range(2):
            for (pos, pd), L in life[p].items():
                A = agg[p][pd]; A["n"] += 1; A["units"] += L["units"]; A["prod"] += L["prod_nights"]; A["fert"] += L["fert_prod"]; A["unw"] += L["unwatered_prod"]; A["fu"] += L["fert_unw"]
    n = len(seeds)
    for p, name in ((0, os.path.basename(a.cand)), (1, os.path.basename(a.opp))):
        print(f"\n{name} {a.crop}: planted_day -> plantings/game, units/planting, prod nights/planting, fertilized+watered prod nights/planting, unwatered prod nights/planting")
        tot = collections.Counter()
        for pd in sorted(agg[p]):
            A = agg[p][pd]; tot.update(A)
            print(f"  d{pd:2d}: {A['n']/n:5.1f}  {A['units']/A['n']:4.1f}u  {A['prod']/A['n']:4.1f}  fert {A['fert']/A['n']:4.1f}  unwatered {A['unw']/A['n']:4.1f}")
        print(f"  FERTILIZE actions on {a.crop} by tile age (per game): " + " ".join(f"a{k}:{v/n:.1f}" for k, v in sorted(FERT_AGE[p].items())))
        print(f"  ALL: {tot['n']/n:5.1f}  {tot['units']/tot['n']:4.1f}u  {tot['prod']/tot['n']:4.1f}  fert {tot['fert']/tot['n']:4.1f}  unwatered {tot['unw']/tot['n']:4.1f}  FERTILIZED-BUT-UNWATERED prod nights {tot['fu']/tot['n']:4.2f}/planting ({tot['fu']/n:.0f}/game)")
