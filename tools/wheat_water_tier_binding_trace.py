#!/usr/bin/env python3
"""wheat_water_tier binding/error trace (Sep 13) -- per Grace's spec, run BEFORE any economic panel.

Branch: candidates/K_SELFMODEL.py perceive() lines ~261-264. When wheat_water_tier is on, wheat tiles
needing water are pulled out of the generic "water" pool (orchestrator priority 1.0) into a new "wwater"
pool (priority 0.5, tied with "harvest" and "fert", ahead of generic "water" and "plant"). So the knob's
only possible effect is: wheat tiles get serviced before other water-needing crops when hands are scarce,
and get serviced at the same nominal priority as harvest (previously lower, at 1.0).

The concrete, measurable "did this go wrong" signal already exists in the engine's own model:
_water_needed() returns "urgent" exactly when a tile went a day UNWATERED (consecutive_unwatered>=1) --
i.e. a missed watering, which is a real yield-risk event (the code comment: "WATER raises yield now").
So: count urgent-water events per crop bucket (WHEAT vs OTHER) under wheat_water_tier=0 (O36_MIN_HANDS2,
baseline) vs =1 (candidates/_probe_wheat_water_tier_1.py, treatment), same seeds/opponents, single seat.

This directly operationalizes Grace's 5-part spec:
  1. Opportunity population: wheat-water-need frequency + how often it's contended with harvest/other-water.
  2. Actual binding: does turning the knob on change which pool wheat lands in and how often it's serviced
     same-day vs missed (goes urgent).
  3/4. Counterfactual consequence / cost of priority: baseline vs treatment urgent-event counts for WHEAT
     (does the tier reduce wheat misses) and for OTHER crops (does elevating wheat cost other crops misses).

Usage: KAGG_FIXED_SHOPS=1 python3 tools/wheat_water_tier_binding_trace.py --seeds 11-30 --opps peter,alaylm,bahaen,yangk
"""
import sys, os, argparse
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me

BASE = os.path.join(ROOT, "candidates/O36_MIN_HANDS2.py")
TREAT = os.path.join(ROOT, "candidates/_probe_wheat_water_tier_1.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}


def play(cand, opp, seed, stats, opp_stats):
    """stats: dict accumulating counts. Instruments the candidate's own perceive() each decision hour
    (hour 0/1, once per day) to read wheat-water opportunity + contention, and separately scans ALL crop
    tiles each hour for urgent-transition events (a tile with consecutive_unwatered>=1 this hour that
    didn't have it last hour we looked -- approximated by checking once per day at hour 0, since
    consecutive_unwatered increments daily)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("kcand", cand)
    kc = importlib.util.module_from_spec(spec); spec.loader.exec_module(kc)

    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    last_day = -1
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if i == 0 and day != last_day and hour == 0:
                v = kc.perceive(obs)
                tiles = obs["farms"][obs["player"]]["tiles"]
                wheat_needs_water = 0; other_needs_water = 0
                wheat_urgent = 0; other_urgent = 0
                for pos, t in v["crops"]:
                    need = kc._water_needed(t, day)
                    is_wheat = (t.get("crop") == "WHEAT")
                    if need == "water":
                        if is_wheat: wheat_needs_water += 1
                        else: other_needs_water += 1
                    elif need == "urgent":
                        if is_wheat: wheat_urgent += 1
                        else: other_urgent += 1
                harvest_n = len(v["harvest"])
                stats["days_seen"] += 1
                stats["wheat_needs_water_days"] += 1 if wheat_needs_water > 0 else 0
                stats["wheat_urgent_events"] += wheat_urgent
                stats["other_urgent_events"] += other_urgent
                stats["contend_harvest_days"] += 1 if (wheat_needs_water > 0 and harvest_n > 0) else 0
                stats["contend_otherwater_days"] += 1 if (wheat_needs_water > 0 and other_needs_water > 0) else 0
                last_day = day
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break


def _parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-"); out.extend(range(int(lo), int(hi) + 1))
        else:
            out.append(int(part))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default="11-20")
    ap.add_argument("--opps", default="peter,alaylm")
    args = ap.parse_args()
    seeds = _parse_seeds(args.seeds)
    opp_names = [o.strip() for o in args.opps.split(",")]

    def new_stats():
        return Counter()

    results = {}
    for label, cand in [("baseline(tier=0)", BASE), ("treatment(tier=1)", TREAT)]:
        stats = new_stats()
        n_games = 0
        for opp_name in opp_names:
            opp = OPPS[opp_name]
            for sd in seeds:
                play(cand, opp, sd, stats, None)
                n_games += 1
        results[label] = (stats, n_games)

    for label, (stats, n_games) in results.items():
        print(f"\n=== {label} -- {n_games} games, {stats['days_seen']} decision-days ===")
        print(f"  wheat_needs_water_days: {stats['wheat_needs_water_days']} ({100*stats['wheat_needs_water_days']/stats['days_seen']:.1f}%)")
        print(f"  contend_with_harvest_days: {stats['contend_harvest_days']} ({100*stats['contend_harvest_days']/stats['days_seen']:.1f}%)")
        print(f"  contend_with_other_water_days: {stats['contend_otherwater_days']} ({100*stats['contend_otherwater_days']/stats['days_seen']:.1f}%)")
        print(f"  wheat_urgent_events (missed-water, total): {stats['wheat_urgent_events']}  ({stats['wheat_urgent_events']/n_games:.2f}/game)")
        print(f"  other_urgent_events (missed-water, total): {stats['other_urgent_events']}  ({stats['other_urgent_events']/n_games:.2f}/game)")
