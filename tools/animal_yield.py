#!/usr/bin/env python3
"""Animal production self-model audit (Sep 11).

The policy sizes the herd from RATE = {"COW": 1.5, "SHEEP": 1.33} units/animal/day
(`_demand_room`: n_max = sustainable_rate // RATE[species]). Those numbers are the
PERFECT-CARE ceiling: the engine gives base 1 unit per production event plus one bonus
unit per consecutive fed+cared day since the last event, so a cow fed and cared every
day yields 1+2 every 2 days (1.5/day) and a sheep 1+3 every 3 days (1.33/day).

Two ways reality can fall short, both engine-visible:
  * care misses      -> smaller pending_care_bonus at the production event
  * max_held = 6     -> production truncated when units are not collected in time

This wraps the engine's own `_daily_refresh_animals` and records, per production event,
the units the animal was entitled to (1 + bonus) and the units it actually banked after
the min(max_held, ...) clamp -- for both farms in the same games.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/animal_yield.py CAND --opp TAPE --seeds 151-154
"""
import argparse, collections, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me

EV = []            # one record per production event
ALIVE = []         # (species, animal-days alive) per farm
SPEC = {"COW": (8, 2, 6), "SHEEP": (6, 3, 6), "GOOSE": (4, 1, 4)}
RATE = {"COW": 1.5, "SHEEP": 1.33, "GOOSE": 2.0}


def install(mod):
    if getattr(mod._daily_refresh_animals, "_audit", False):
        return
    orig = mod._daily_refresh_animals

    def wrapped(farm, day):
        pre = {}
        for y, row in enumerate(farm["tiles"]):
            for x, t in enumerate(row):
                if isinstance(t, dict) and "animal" in t:
                    pre[(x, y)] = (t["animal"], t.get("yield_units", 0), t.get("pending_care_bonus", 0),
                                   t.get("fed_today", False), t.get("cared_today", False), t["placed_day"])
        seat = farm.get("_audit_seat")
        orig(farm, day)
        for (x, y), (sp, yu, bonus, fed, cared, placed) in pre.items():
            ALIVE.append((seat, sp))
            first, interval, cap = SPEC[sp]
            dsf = (day + 1) - placed - first
            if dsf < 0 or dsf % interval != 0:
                continue
            gained = 1 + (bonus if fed else 0)
            banked = min(cap, yu + gained) - yu
            EV.append({"seat": seat, "sp": sp, "day": day, "entitled": gained, "banked": banked,
                       "fed": fed, "cared": cared, "bonus": bonus, "held_before": yu})
        return None

    wrapped._audit = True
    mod._daily_refresh_animals = wrapped


def run(cand, opp, seed):
    mod, defaults = me.load_engine("master")
    install(mod)
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    while step < steps:
        obs0 = state[0].observation
        for i in range(2):
            obs0.farms[i]["_audit_seat"] = i
        for i in range(2):
            o = me._fast_copy(state[i].observation); o["step"] = step
            try:
                act = agents[i](o, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act if isinstance(act, dict) else {}
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            break
    return [state[0].observation.farms[i]["money"] for i in range(2)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cand"); ap.add_argument("--opp", required=True); ap.add_argument("--seeds", default="151-154")
    a = ap.parse_args()
    lo, hi = (int(x) for x in a.seeds.split("-"))
    names = [os.path.basename(a.cand), os.path.basename(a.opp)]
    money = [0.0, 0.0]
    n = 0
    for s in range(lo, hi + 1):
        m = run(a.cand, a.opp, s)
        money[0] += m[0]; money[1] += m[1]; n += 1
    alive = collections.Counter(ALIVE)
    for seat in (0, 1):
        ev = [e for e in EV if e["seat"] == seat]
        print(f"\n{names[seat]}  (mean money ${money[seat]/n:,.0f}, {n} games)")
        if not ev:
            print("  no animal production events"); continue
        for sp in ("COW", "SHEEP", "GOOSE"):
            e = [x for x in ev if x["sp"] == sp]
            if not e:
                continue
            days = alive[(seat, sp)]
            banked = sum(x["banked"] for x in e)
            entitled = sum(x["entitled"] for x in e)
            perfect = len(e) * (1 + SPEC[sp][1])
            fed = sum(1 for x in e if x["fed"]); cared = sum(1 for x in e if x["cared"])
            print(f"  {sp:6s} {len(e):5d} production events over {days:5d} animal-days"
                  f"   realised {banked/max(1,days):.3f} u/animal-day   (policy RATE {RATE[sp]})")
            print(f"         entitled {entitled/len(e):.2f} u/event vs perfect-care {perfect/len(e):.2f}"
                  f"   banked {banked/len(e):.2f}   lost to max_held {entitled-banked} u"
                  f" ({(entitled-banked)/max(1,entitled):.0%})   fed at event {fed/len(e):.0%}")


if __name__ == "__main__":
    main()
