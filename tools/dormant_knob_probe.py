#!/usr/bin/env python3
"""Dormant-knob engagement probe (Sep 12 discovery-phase audit): for each currently-off/default knob in
O36_MIN_HANDS2's KNOBS, run ONE fixed-shops game vs a real tape with the knob nudged to a plausible nonzero
value and count how many turns produce a DIFFERENT action list than the O36 baseline (same seed/opp/seat).
This is an engagement check (does the branch even get exercised / does it ever change behavior), not an
economic panel -- classification per Grace's 5-step protocol still needs a real panel before any DO.
Usage: KAGG_FIXED_SHOPS=1 python3 tools/dormant_knob_probe.py
"""
import sys, os, copy
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me

OPP = os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py")
BASE = os.path.join(ROOT, "candidates/O36_MIN_HANDS2.py")
SEEDS = [21, 22, 23]

CANDIDATES = {
    "wheat_tiles_6": {"wheat_tiles": 6},
    "wheat_per_animal_0.5": {"wheat_per_animal": 0.5},
    "wheat_stock_20": {"wheat_stock": 20},
    "wheat_hold_days_1": {"wheat_hold_days": 1},
    "wheat_water_tier_1": {"wheat_water_tier": 1},
    "drop_radius_2": {"drop_radius": 2},
    "capital_hour2_6": {"capital_hour2": 6},
    "melon_rush_1": {"melon_rush": 1},
    "straw_delay_5": {"straw_delay": 5},
    "sell_hourly_1": {"sell_hourly": 1},
    "wheat_cap_30": {"wheat_cap": 30},
    "fert_carry_4": {"fert_carry": 4},
}


def make_variant(name, overrides):
    src = open(BASE).read()
    import re
    m = re.search(r"^KNOBS = (\{.*\})$", src, re.M)
    knobs = eval(m.group(1))
    knobs.update(overrides)
    new_src = src[:m.start()] + f"KNOBS = {knobs!r}" + src[m.end():]
    path = os.path.join(ROOT, "candidates", f"_probe_{name}.py")
    open(path, "w").write(new_src)
    return path


def play(cand_path, opp_path, seed):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(cand_path), me.load_agent(opp_path)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    actions = []
    while True:
        obs = me._fast_copy(state[0].observation); obs["step"] = step
        try: act0 = agents[0](obs, me._fast_copy(env.configuration))
        except Exception: act0 = {}
        actions.append(act0.get("market", []))
        for i in range(2):
            obsx = me._fast_copy(state[i].observation); obsx["step"] = step
            if i == 0:
                act = act0
            else:
                try: act = agents[i](obsx, me._fast_copy(env.configuration))
                except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    money = state[0].observation.farms[0]["money"]
    return actions, money


if __name__ == "__main__":
    base_runs = {s: play(BASE, OPP, s) for s in SEEDS}
    print(f"{'knob':22s} {'turns_diff/total':>18s}  {'money_delta (per seed)'}")
    for name, overrides in CANDIDATES.items():
        path = make_variant(name, overrides)
        deltas = []
        diffturns = []
        for s in SEEDS:
            acts, money = play(path, OPP, s)
            base_acts, base_money = base_runs[s]
            nd = sum(1 for a, b in zip(acts, base_acts) if a != b)
            diffturns.append((nd, len(acts)))
            deltas.append(money - base_money)
        dtxt = ", ".join(f"{n}/{t}" for n, t in diffturns)
        mtxt = ", ".join(f"{d:+.0f}" for d in deltas)
        print(f"{name:22s} {dtxt:>18s}  {mtxt}")
        pass  # leave probe file (no delete perms); reused each run
