#!/usr/bin/env python3
"""TOMATO exclusion-gate trace (Sep 12/13) -- per Grace's direction: before treating TOMATO's near-zero
planting rate as a knob-sweep opportunity, trace every exclusion gate in the actual O36 seed-selection
competition (candidates/K_SELFMODEL.py lines ~576-609) that TOMATO passes through, and quantify which gate
is actually responsible for excluding it, on each day >=1 decision point across the standard panel.

Gates checked, in the order the real code checks them, for TOMATO specifically:
  1. day_window   -- day > cutoff(20) or day < start(0)          [structural, never true for TOMATO/start=0]
  2. sell_window  -- T_sell = 29 - day - first(8) <= 0            [closes after day 21]
  3. demand_room  -- room_units < units(5.0) * 0.5                [DEMAND_SHARE-driven pool too small]
  4. min_val      -- val = min(units,room_units)*price/cycle(12) < min_val(12)
  5. loses_ranking -- passes all 4 static gates above, but never wins the value-density "best" comparison
                      against MELON/CARROT/STRAWBERRY/WHEAT before the loop exhausts space or n_seed_orders<4
  6. k_zero       -- wins "best" at some iteration but k computed <=0 (space/free-cash/seed-cost binding)
  7. planted      -- actually gets a BUY_SEED order with k>0

Static gates 1-4 don't change across iterations within a day (TOMATO's own `committed`/`seed_orders` stay 0
until it's picked), so they're evaluated once per day; ranking dynamics (5/6) require replaying the loop.

Usage: KAGG_FIXED_SHOPS=1 python3 tomato_gate_trace.py --seeds 11-30 --opps peter,alaylm,bahaen,yangk
"""
import sys, os, importlib.util, argparse
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me

CAND = os.path.join(ROOT, "candidates/O36_MIN_HANDS2.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}
spec = importlib.util.spec_from_file_location("km", CAND)
km = importlib.util.module_from_spec(spec); spec.loader.exec_module(km)


def classify_day(obs, v, seeds):
    """Return (reason, extra) for TOMATO on this decision day."""
    day = obs["day"]; prices = obs["market"]["prices"]
    sp_ = km.CROP_SPECS["TOMATO"]
    if day > sp_["cutoff"] or day < sp_.get("start", 0):
        return "day_window", None
    T_sell = max(0, 29 - day - sp_["first"])
    if T_sell <= 0:
        return "sell_window", None

    committed = {c: 0.0 for c in km.CROP_SPECS}
    for _pos, t in v["crops"]:
        c = t.get("crop")
        if c in committed: committed[c] += km.CROP_SPECS[c]["units"]
    for c in committed:
        committed[c] += seeds.get(c, 0) * km.CROP_SPECS[c]["units"]
    empty_count = len(v["empty"]) + len(v["empty_pastures"])
    space0 = empty_count - 0 - sum(seeds.get(c, 0) for c in km.CROP_SPECS)
    free0 = obs["farms"][obs["player"]]["money"]

    inv_c = obs["market"]["inventory"].get("TOMATO", km.I0)
    cushion_left = max(0.0, sp_.get("cushion", 0) - max(0.0, inv_c - km.I0))
    pool = km.DEMAND_SHARE * (max(0.0, km.I0 - inv_c) + cushion_left +
                               km._daily_demand(obs, "TOMATO", day, day + sp_["first"]) * (29 - day))
    room_units = pool - committed["TOMATO"]
    if room_units < sp_["units"] * 0.5:
        return "demand_room", round(room_units, 2)
    price = min(prices.get("TOMATO", sp_["base"]), sp_["base"] * 2.0)
    tomato_val = min(sp_["units"], room_units) * price / sp_["cycle"]
    if tomato_val < sp_["min_val"]:
        return "min_val", round(tomato_val, 2)

    # passes all static gates -- replay the real loop to see if it ever wins
    space, free = space0, free0
    seed_orders = {}; n_seed_orders = 0; excluded = set()
    beaten_by = Counter()
    while space > 0 and n_seed_orders < 4:
        best = None
        tomato_eligible_here = "TOMATO" not in excluded
        for c, spx in km.CROP_SPECS.items():
            if c in excluded or day > spx["cutoff"] or day < spx.get("start", 0):
                continue
            if c == "STRAWBERRY" and day < km.KNOBS["straw_delay"]:
                continue
            Ts = max(0, 29 - day - spx["first"])
            if Ts <= 0:
                continue
            invc = obs["market"]["inventory"].get(c, km.I0)
            cl = max(0.0, spx.get("cushion", 0) - max(0.0, invc - km.I0))
            pl = km.DEMAND_SHARE * (max(0.0, km.I0 - invc) + cl + km._daily_demand(obs, c, day, day + spx["first"]) * (29 - day))
            ru = pl - committed[c] - seed_orders.get(c, 0) * spx["units"]
            if ru < spx["units"] * 0.5:
                continue
            pr = min(prices.get(c, spx["base"]), spx["base"] * 2.0)
            val = min(spx["units"], ru) * pr / spx["cycle"]
            if val < spx["min_val"]:
                continue
            if best is None or val > best[0]:
                best = (val, c, ru)
        if best is None:
            break
        _val, c, ru = best
        if c != "TOMATO" and tomato_eligible_here:
            beaten_by[c] += 1
        k = min(space, int(ru // km.CROP_SPECS[c]["units"]), int(free // km.CROP_SPECS[c]["seed"]), 20)
        if k <= 0:
            excluded.add(c); continue
        if c == "TOMATO":
            return "planted" if k > 0 else "k_zero", k
        excluded.add(c)
        seed_orders[c] = seed_orders.get(c, 0) + k
        free -= km.CROP_SPECS[c]["seed"] * k
        space -= k
        n_seed_orders += 1
    top_rival = beaten_by.most_common(1)
    return "loses_ranking", (top_rival[0][0] if top_rival else None)


def play(cand, opp, seed, counter, rival_counter, examples):
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
            if i == 0 and day >= 1 and day != last_day and hour in (0, 1):
                v = km.perceive(obs)
                seeds = obs["private"]["seeds"]
                reason, extra = classify_day(obs, v, seeds)
                counter[reason] += 1
                if reason == "loses_ranking" and extra:
                    rival_counter[extra] += 1
                if reason == "planted" and len(examples) < 6:
                    examples.append((seed, opp, day, extra))
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
    counter = Counter(); rival_counter = Counter(); examples = []
    n_games = 0
    for opp_name in opp_names:
        opp = OPPS[opp_name]
        for sd in seeds:
            play(CAND, opp, sd, counter, rival_counter, examples)
            n_games += 1
    total = sum(counter.values())
    print(f"games={n_games} decision_days_seen={total}")
    for reason, cnt in counter.most_common():
        print(f"  {reason:16s} {cnt:5d}  ({100*cnt/total:.1f}%)")
    if rival_counter:
        print("loses_ranking -- beaten by:")
        for rival, cnt in rival_counter.most_common():
            print(f"  {rival:12s} {cnt:5d}")
    if examples:
        print("planted examples (seed, opp, day, k):", examples)
