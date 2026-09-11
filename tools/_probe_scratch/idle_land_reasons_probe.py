#!/usr/bin/env python3
"""
Trace WHY O36 leaves land idle in days 11-25 -- observational only, O36 unmodified, no gameplay change.

Code facts established first (candidates/O36_MIN_HANDS2.py):
  - Capital decisions (BUY_SEED / BUY_ANIMAL / land purchase) fire only once per day, at hour==1 (or a
    rare capital-event hour, or hour==0 on day 0) -- see economy()'s `capital_hour` gate. Every other
    hour, economy() only hires/feeds and returns early. So idle land isn't continuously reconsidered.
  - Crop seed-buying loops over CROP_SPECS picking the best-value crop, but SKIPS a crop if:
      (a) day is outside that crop's [start, cutoff] window (or STRAWBERRY's straw_delay gate)
      (b) `room_units < units*0.5` -- the DEMAND_SHARE-based "pool" for that crop (bounded by market
          inventory I0, cushion, and daily demand) is already exhausted by what's already planted/seeded
      (c) `val < min_val` -- expected value density too low
    If EVERY crop gets excluded this way, the loop breaks (`best is None: break`) and NO more seeds get
    bought that day even if `space` (available land) > 0 -- land stays idle by explicit policy design,
    not by accident. Also capped at n_seed_orders < 4 (at most 4 crop types bought per day).
  - Animal purchases are separately capped by KNOBS['max_animals']=17, per-species `_demand_room`, and a
    hard labor ceiling MAX_HANDS=14 (via `_load_model(...) >= MAX_HANDS` throttling k down).
  - Two DIFFERENT demand-share constants exist: DEMAND_SHARE=0.5 (module constant, drives crop `pool`)
    and KNOBS['demand_share']=0.55 (drives animal-product `_demand_room`) -- these are NOT the same
    number and this script does not touch either; it only measures how often each stop condition fires.

This probe replays O36's own real decision functions (read-only, external re-computation, not a patch)
at each day's capital hour for days 11-25, to classify why the crop seed-buying loop stopped when land
was still available, and whether the herd purchase was capped by max_animals or the MAX_HANDS throttle.
"""
import sys, os, argparse, importlib.util
from pathlib import Path
from collections import Counter

def find_repo_root():
    for p in [Path.home() / "mnt" / "Kaggriculture"]:
        if (p / "mini_engine.py").exists():
            return p
    return None

REPO = find_repo_root()
sys.path.insert(0, str(REPO))
os.chdir(REPO)
import mini_engine as me  # noqa: E402

OPPS = {
    "peter": "Opponents/tape_peterparker_106816877.py",
    "alaylm": "Opponents/tape_alaylm_106813359.py",
    "bahaen": "Opponents/tape_bahaenes_106828159.py",
    "yangk": "Opponents/tape_yangkuang2_106819729.py",
}
DAY_LO, DAY_HI = 11, 25


def load_agent_module(path, tag):
    p = Path(path)
    name = f"idle_probe_{tag}_{p.stem}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def classify_day(mod, obs, v):
    """Re-run (read-only) the same crop-exclusion logic economy() uses, to classify why each crop
    is or isn't eligible for a seed order right now, and whether land (`space`) would go unused."""
    day = obs["day"]
    seeds = obs["private"]["seeds"]
    shed = obs["private"]["shed"]
    inv = obs["private"].get("inventories") or []
    carried_animals = sum(i.get(a, 0) for i in inv for a in mod.ANIMALS)
    shed_animals = sum(shed.get(a, 0) for a in mod.ANIMALS)
    n_active = len(v["animals"])
    n_total = n_active + shed_animals + carried_animals
    pending_place = shed_animals + carried_animals
    empty_count = len(v["empty"]) + len(v["empty_pastures"])
    committed = {c: 0.0 for c in mod.CROP_SPECS}
    for _pos, t in v["crops"]:
        c = t.get("crop")
        if c in committed:
            committed[c] += mod.CROP_SPECS[c]["units"]
    for c in committed:
        committed[c] += seeds.get(c, 0) * mod.CROP_SPECS[c]["units"]
    space = empty_count - pending_place - sum(seeds.get(c, 0) for c in mod.CROP_SPECS)
    prices = obs["market"]["prices"]

    reasons = {}
    any_eligible = False
    for c, sp_ in mod.CROP_SPECS.items():
        if day > sp_["cutoff"] or day < sp_.get("start", 0):
            reasons[c] = "outside_day_window"
            continue
        if c == "STRAWBERRY" and day < mod.KNOBS["straw_delay"]:
            reasons[c] = "straw_delay_gate"
            continue
        T_sell = max(0, 29 - day - sp_["first"])
        if T_sell <= 0:
            reasons[c] = "no_sell_time_left"
            continue
        inv_c = obs["market"]["inventory"].get(c, mod.I0)
        cushion_left = max(0.0, sp_.get("cushion", 0) - max(0.0, inv_c - mod.I0))
        pool = mod.DEMAND_SHARE * (max(0.0, mod.I0 - inv_c) + cushion_left +
                                     mod._daily_demand(obs, c, day, day + sp_["first"]) * (29 - day))
        room_units = pool - committed[c]
        if room_units < sp_["units"] * 0.5:
            reasons[c] = "demand_room_exhausted"
            continue
        price = min(prices.get(c, sp_["base"]), sp_["base"] * 2.0)
        val = min(sp_["units"], room_units) * price / sp_["cycle"]
        if val < sp_["min_val"]:
            reasons[c] = "value_density_too_low"
            continue
        reasons[c] = "eligible"
        any_eligible = True

    herd_reason = None
    if 1 <= day <= 21 and pending_place <= 3 and n_total < mod.KNOBS["max_animals"]:
        herd_reason = "herd_purchase_window_open"
    elif n_total >= mod.KNOBS["max_animals"]:
        herd_reason = "max_animals_cap_reached"
    elif pending_place > 3:
        herd_reason = "too_many_unplaced_already"
    else:
        herd_reason = "outside_herd_day_window"

    # replicate the actual capital math (reserve, free) to see whether the always-eligible crop
    # (CARROT) still gets k=0 due to a real cash or labor-throughput throttle, not demand.
    inv_ = inv
    due_feed = sum(mod._feed_useful(t, day) for q, t in v["animals"]) + shed_animals + carried_animals
    feed_need = max(0, due_feed + 3 - shed.get("WHEAT", 0)) if day < 29 else 0
    wheat_price = prices.get("WHEAT", 40)
    wheat_cost = feed_need * wheat_price * 1.15
    seeds_on_hand = sum(seeds.get(c, 0) for c in mod.CROP_SPECS)
    target = mod._load_model(v, seeds_on_hand, n_total, pending_place, day)
    _, labor_cost_today = mod._hire_plan(target, len(obs["farms"][obs["player"]]["hands"]), obs["farms"][obs["player"]]["hires_today"], 10**9)
    reserve = wheat_cost + labor_cost_today + 100
    cash = obs["farms"][obs["player"]]["money"]
    free = cash - reserve  # ignoring revenue_est and any herd spend already committed -- upper bound on `free`
    carrot_spec = mod.CROP_SPECS["CARROT"]
    inv_c = obs["market"]["inventory"].get("CARROT", mod.I0)
    cushion_left = max(0.0, carrot_spec.get("cushion", 0) - max(0.0, inv_c - mod.I0))
    pool = mod.DEMAND_SHARE * (max(0.0, mod.I0 - inv_c) + cushion_left +
                                 mod._daily_demand(obs, "CARROT", day, day + carrot_spec["first"]) * (29 - day))
    committed_carrot = sum(carrot_spec["units"] for _pos, t in v["crops"] if t.get("crop") == "CARROT")
    committed_carrot += seeds.get("CARROT", 0) * carrot_spec["units"]
    room_units = pool - committed_carrot
    k_by_space = space
    k_by_room = int(room_units // carrot_spec["units"]) if carrot_spec["units"] else 0
    k_by_cash = int(free // carrot_spec["seed"]) if carrot_spec["seed"] else 0
    k_carrot = max(0, min(k_by_space, k_by_room, k_by_cash, 20))

    return {
        "day": day, "space": space, "any_eligible": any_eligible, "reasons": reasons,
        "n_total": n_total, "max_animals": mod.KNOBS["max_animals"], "herd_reason": herd_reason,
        "free_cash": free, "k_carrot": k_carrot, "k_by_room": k_by_room, "k_by_cash": k_by_cash,
        "k_by_space": k_by_space,
    }


def run_game(agent_path, opp_path, seed, out):
    engmod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    mod0 = load_agent_module(agent_path, "p0")
    orig_agent = mod0.agent

    def agent_patched(obs, configuration=None):
        day, hour = obs["day"], obs["hour"]
        if hour == 1 and DAY_LO <= day <= DAY_HI:
            v = mod0.perceive(obs)
            out.append(classify_day(mod0, obs, v))
        return orig_agent(obs, configuration)

    mod0.agent = agent_patched
    a1 = load_agent_module(opp_path, "p1").agent
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
                            "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = engmod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    while True:
        for i in (0, 1):
            o = me._fast_copy(state[i].observation); o["step"] = step
            try: act = (agent_patched if i == 0 else a1)(o, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = engmod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent", nargs="?", default="candidates/O36_MIN_HANDS2.py")
    ap.add_argument("--seeds", default="11-18")
    ap.add_argument("--opp", default="all")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    opps = OPPS if args.opp == "all" else {args.opp: OPPS[args.opp]}

    records = []
    for opp_name, opp_path in opps.items():
        for seed in range(lo, hi + 1):
            run_game(args.agent, opp_path, seed, records)

    n = len(records)
    print(f"=== idle-land reasons, days {DAY_LO}-{DAY_HI}, {n} capital-hour observations ===\n")

    space_positive = [r for r in records if r["space"] > 0]
    print(f"observations with unused land available (space>0): {len(space_positive)}/{n} "
          f"({100*len(space_positive)/n:.1f}%)")
    no_crop_eligible = [r for r in space_positive if not r["any_eligible"]]
    print(f"  of those, NO crop was eligible for a seed order at all: {len(no_crop_eligible)}/{len(space_positive)} "
          f"({100*len(no_crop_eligible)/max(1,len(space_positive)):.1f}%)  <- land idle BY POLICY DESIGN, not accident\n")

    print("Per-crop exclusion reason counts (across all observations, not just space>0):")
    per_crop_reason = Counter()
    for r in records:
        for c, reason in r["reasons"].items():
            per_crop_reason[(c, reason)] += 1
    crops = sorted(set(c for c, _ in per_crop_reason))
    for c in crops:
        print(f"  {c}:")
        for reason in ["eligible", "outside_day_window", "straw_delay_gate", "no_sell_time_left",
                       "demand_room_exhausted", "value_density_too_low"]:
            cnt = per_crop_reason.get((c, reason), 0)
            if cnt:
                print(f"    {reason:24s}: {cnt:4d} ({100*cnt/n:.1f}%)")

    print("\nHerd (animal-purchase) status distribution:")
    herd_ct = Counter(r["herd_reason"] for r in records)
    for k, v in herd_ct.most_common():
        print(f"  {k:28s}: {v:4d} ({100*v/n:.1f}%)")

    n_total_vals = [r["n_total"] for r in records]
    print(f"\nn_total (animals owned) at these observations: min={min(n_total_vals)} max={max(n_total_vals)} "
          f"mean={sum(n_total_vals)/len(n_total_vals):.1f}  (cap max_animals={records[0]['max_animals']})")

    print("\nCARROT (always-eligible crop) actual k breakdown at space>0 observations -- what's the binding constraint?")
    sp = [r for r in records if r["space"] > 0]
    zero_k = [r for r in sp if r["k_carrot"] <= 0]
    print(f"  k_carrot<=0 despite space>0: {len(zero_k)}/{len(sp)} ({100*len(zero_k)/max(1,len(sp)):.1f}%)")
    if zero_k:
        cash_bound = sum(1 for r in zero_k if r["k_by_cash"] <= 0 and r["k_by_room"] > 0)
        room_bound = sum(1 for r in zero_k if r["k_by_room"] <= 0)
        print(f"    of those: cash-bound (k_by_cash<=0, room ok): {cash_bound}   demand-room-bound (k_by_room<=0): {room_bound}")
    nonzero = [r["k_carrot"] for r in sp if r["k_carrot"] > 0]
    if nonzero:
        print(f"  when k_carrot>0: mean={sum(nonzero)/len(nonzero):.1f}, vs mean space available={sum(r['space'] for r in sp)/len(sp):.1f}")


if __name__ == "__main__":
    main()
