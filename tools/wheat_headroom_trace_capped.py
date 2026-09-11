#!/usr/bin/env python3
"""Capped WHEAT headroom probe (Sep 12) -- follow-up to wheat_headroom_trace.py per Grace's direction: the
uncapped version's raw numbers ignore tile space, the daily 20-unit BUY_SEED cap, and competition with other
crops for the same day's seed-order slots. This version replicates K_SELFMODEL.py's ACTUAL seed-selection
while-loop (candidates/K_SELFMODEL.py lines ~576-609: value-density competition across CROP_SPECS, capped by
space/20/free, at most 4 crops picked per day) twice per day -- once with the real WHEAT constants
(units=5.0, its share of the pool via the shared DEMAND_SHARE=0.5) and once with WHEAT's constants corrected
(units=3.8, WHEAT's own pool computed with share=0.36) -- and compares the WHEAT k actually selected by the
competition in each pass. Other crops keep their real constants in both passes; only WHEAT's assumption is
being tested, so this isolates whether CORRECTING WHEAT lets it win a seed-order slot it currently loses (or
lose one it currently wins), not a blanket DEMAND_SHARE change.

Approximations acknowledged (kept simple by design, per "cheap to implement by reusing the existing trace"):
  - `free` budget is approximated as the observed cash on hand (a generous upper bound -- the real formula
    reserves labor/wheat-feed cost first, so this may overstate how much is actually free for seeds).
  - `pending_place` (animals awaiting placement) is approximated as 0 -- the real number is usually small.
  - the `_load_model`/MAX_HANDS labor-capacity check that can further shrink k is NOT replicated.
  These all bias toward being SLIGHTLY MORE generous to planting than the real policy, on both the real and
  corrected pass equally, so the REAL-vs-CORRECTED comparison (the number that matters) is not biased by them
  even though the absolute k values might be a little high.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/wheat_headroom_trace_capped.py --seeds 11-20 --opps peter,alaylm
"""
import sys, os, importlib.util, statistics, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
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

REAL_UNITS, CORR_UNITS = 5.0, 3.8
REAL_SHARE, CORR_SHARE = 0.5, 0.36


def run_seed_selection(obs, v, seeds, wheat_units, wheat_share):
    """Faithful replica of the CROP_SPECS competition loop, with WHEAT's units/share swapped."""
    day = obs["day"]; prices = obs["market"]["prices"]
    n_total_approx = sum(1 for _pos, t in v["animals"])  # approx: active animals only, no shed/carried
    committed = {c: 0.0 for c in km.CROP_SPECS}
    for _pos, t in v["crops"]:
        c = t.get("crop")
        if c in committed: committed[c] += km.CROP_SPECS[c]["units"] if c != "WHEAT" else wheat_units
    for c in committed:
        base_units = km.CROP_SPECS[c]["units"] if c != "WHEAT" else wheat_units
        committed[c] += seeds.get(c, 0) * base_units
    empty_count = len(v["empty"]) + len(v["empty_pastures"])
    space = empty_count - 0 - sum(seeds.get(c, 0) for c in km.CROP_SPECS)   # pending_place approx 0
    free = obs["player" if False else "private"].get("cash", None)
    # cash actually lives at obs["farms"][obs["player"]]["money"]
    free = obs["farms"][obs["player"]]["money"]
    seed_orders = {}; n_seed_orders = 0; excluded = set()
    while space > 0 and n_seed_orders < 4:
        best = None
        for c, sp_ in km.CROP_SPECS.items():
            if c in excluded or day > sp_["cutoff"] or day < sp_.get("start", 0):
                continue
            if c == "STRAWBERRY" and day < km.KNOBS["straw_delay"]:
                continue
            T_sell = max(0, 29 - day - sp_["first"])
            if T_sell <= 0:
                continue
            units = wheat_units if c == "WHEAT" else sp_["units"]
            share = wheat_share if c == "WHEAT" else km.DEMAND_SHARE
            inv_c = obs["market"]["inventory"].get(c, km.I0)
            cushion_left = max(0.0, sp_.get("cushion", 0) - max(0.0, inv_c - km.I0))
            pool = share * (max(0.0, km.I0 - inv_c) + cushion_left + km._daily_demand(obs, c, day, day + sp_["first"]) * (29 - day))
            room_units = pool - committed[c] - seed_orders.get(c, 0) * units
            if room_units < units * 0.5:
                continue
            price = min(prices.get(c, sp_["base"]), sp_["base"] * 2.0)
            val = min(units, room_units) * price / sp_["cycle"]
            if val < sp_["min_val"]:
                continue
            if best is None or val > best[0]:
                best = (val, c, room_units, units)
        if best is None:
            break
        _val, c, room_units, units = best
        k = min(space, int(room_units // units), int(free // km.CROP_SPECS[c]["seed"]), 20)
        if k <= 0:
            excluded.add(c); continue
        excluded.add(c)
        seed_orders[c] = seed_orders.get(c, 0) + k
        free -= km.CROP_SPECS[c]["seed"] * k
        space -= k
        n_seed_orders += 1
    return seed_orders.get("WHEAT", 0)


def play(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    real_k_sum = 0; corr_k_sum = 0; days_wheat_selected_real = 0; days_wheat_selected_corr = 0
    last_day = -1
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if i == 0 and day > 0 and day != last_day and hour in (0, 1):
                v = km.perceive(obs)
                seeds = obs["private"]["seeds"]
                kr = run_seed_selection(obs, v, seeds, REAL_UNITS, REAL_SHARE)
                kc = run_seed_selection(obs, v, seeds, CORR_UNITS, CORR_SHARE)
                real_k_sum += kr; corr_k_sum += kc
                days_wheat_selected_real += 1 if kr > 0 else 0
                days_wheat_selected_corr += 1 if kc > 0 else 0
                last_day = day
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return real_k_sum, corr_k_sum, days_wheat_selected_real, days_wheat_selected_corr


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
    ap = argparse.ArgumentParser(); ap.add_argument("--seeds", default="11-20"); ap.add_argument("--opps", default="peter,alaylm")
    a = ap.parse_args(); os.chdir(ROOT)
    seeds = _parse_seeds(a.seeds); opp_names = a.opps.split(",")
    reals, corrs, dreal, dcorr = [], [], [], []
    for opp_name in opp_names:
        opp = OPPS[opp_name]
        for s in seeds:
            r, c, dr, dc = play(CAND, opp, s)
            reals.append(r); corrs.append(c); dreal.append(dr); dcorr.append(dc)
    n = len(reals)
    print(f"n_games={n}  cand={CAND}  opps={opp_names}  seeds={a.seeds}\n")
    print(f"Capped WHEAT plantings actually selected by the competition loop, per game:")
    print(f"  REAL constants (5.0u, share 0.5):       mean {statistics.mean(reals):7.1f}  (range {min(reals)}-{max(reals)})")
    print(f"  CORRECTED constants (3.8u, share 0.36): mean {statistics.mean(corrs):7.1f}  (range {min(corrs)}-{max(corrs)})")
    print(f"  NET delta (corrected - real):            {statistics.mean(corrs)-statistics.mean(reals):+7.1f} /game")
    print(f"\nDays WHEAT actually won a seed-order slot at all (out of ~15 seed-decision days/game):")
    print(f"  REAL:      mean {statistics.mean(dreal):.1f}")
    print(f"  CORRECTED: mean {statistics.mean(dcorr):.1f}")
