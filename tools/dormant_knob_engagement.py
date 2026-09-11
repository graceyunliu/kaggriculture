#!/usr/bin/env python3
"""Dormant-knob behavioral-engagement audit (Sep 12): melon_rush, wheat_water_tier, straw_delay.

Funnel: can the knob physically affect policy (branch reached)? does it change behavior (action differs)?
Deliberately NON-ECONOMIC -- no money is read or compared here, only behavioral/state counts. Contrasting
values are chosen only to make engagement easy to detect, not for profit:
  melon_rush: 0 (off, default) vs 1 (on -- it's a truthy switch, no magnitude semantics)
  wheat_water_tier: 0 (off, default) vs 1 (on -- also a truthy switch)
  straw_delay: 0 (off, default) vs 10 (chosen to land near STRAWBERRY's own "first"=10 constant --
               blocks roughly the first third of the seeding window, easy to see in plant counts)

Method: run CAND (O26_CARROT_SIZING, unmodified except for the one knob under test) as a real agent in
real games against real opponent tapes, both seats. Three lightweight monkeypatches on pure/near-pure
functions already used by the agent's own decision loop (no reimplementation of engine or dispatch logic):
  - _harvest_ready(t, day): peek the MELON early-window condition before calling the real function --
    this is the exact boolean the real code already computes, read-only.
  - _unit_action(...): peek the melon-rush routing condition (day window / carry / not-in-routes) before
    calling the real function -- again the exact condition the real code already gates on.
  - perceive(obs): call the real function, then independently compute what v["wwater"] WOULD be from
    v["water"] + v["tiles"] (the same one-line filter the real code applies) -- gives the opportunity
    count regardless of whether the knob's own gate is on or off in this run.
  - economy(obs, v, ...): peek obs["day"] before calling the real function, for the straw_delay window.
Also independently counts real planted STRAWBERRY tiles by day from v["crops"] (post-hoc, no patching)
to see whether straw_delay actually changes what gets planted, not just whether the branch is reachable.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/dormant_knob_engagement.py --config melon_rush_on --opp bahaen --seeds 71-75 --json out.json
Configs: baseline, melon_rush_on, wheat_water_tier_on, straw_delay_on
"""
import sys, os, argparse, importlib.util, json, statistics
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me

CAND_PATH = os.path.join(ROOT, "candidates/O26_CARROT_SIZING.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}

CONFIGS = {
    "baseline": {},
    "melon_rush_on": {"melon_rush": 1},
    "wheat_water_tier_on": {"wheat_water_tier": 1},
    "straw_delay_on": {"straw_delay": 10},
}


def load_cand(knob_overrides):
    spec = importlib.util.spec_from_file_location(f"cand_{id(knob_overrides)}", CAND_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for k, v in knob_overrides.items():
        mod.KNOBS[k] = v
    return mod


def instrument(mod, log):
    orig_harvest_ready = mod._harvest_ready
    CROPS = mod.CROPS

    def patched_harvest_ready(t, day):
        c = CROPS.get(t.get("crop"))
        if c and not c["ongoing"] and t.get("crop") == "MELON":
            yu = t.get("yield_units", 0)
            age = day - t.get("planted_day", day)
            if yu > 0 and age >= c["first"] and yu >= 5:
                fallback_true = yu >= c["max_yield"] or age >= c["max_day"] or day >= 29
                log["melon_rush_harvest_opportunities"] += 1
                if not fallback_true:
                    log["melon_rush_harvest_decisive"] += 1
        return orig_harvest_ready(t, day)

    mod._harvest_ready = patched_harvest_ready

    orig_unit_action = mod._unit_action

    def patched_unit_action(i, pos, carry, obs, v, pools, seeds_left, shed, unlocked_shed):
        day = obs["day"]
        if 10 <= day <= 14 and carry.get("MELON", 0) >= 4 and carry.get("WHEAT", 0) == 0 and i not in mod.S["routes"]:
            log["melon_rush_dispatch_opportunities"] += 1
        return orig_unit_action(i, pos, carry, obs, v, pools, seeds_left, shed, unlocked_shed)

    mod._unit_action = patched_unit_action

    orig_perceive = mod.perceive

    def patched_perceive(obs):
        v = orig_perceive(obs)
        tiles = v["tiles"]
        would_be_wwater = [pos for pos in v["water"] if tiles[pos[1]][pos[0]].get("crop") == "WHEAT"]
        log["wheat_water_tier_opportunities"] += len(would_be_wwater)
        if would_be_wwater:
            log["wheat_water_tier_turns_with_opportunity"] += 1
        # independent strawberry planted-tile census (no patching needed, just reading v)
        day = obs["day"]
        for pos, t in v["crops"]:
            if t.get("crop") == "STRAWBERRY":
                planted_day = t.get("planted_day", day)
                if planted_day == day:  # freshly planted this turn
                    log["straw_planted_by_day"].setdefault(day, 0)
                    log["straw_planted_by_day"][day] += 1
        return v

    mod.perceive = patched_perceive

    orig_economy = mod.economy

    def patched_economy(obs, v, pending_drop=None):
        day = obs["day"]
        cutoff = mod.CROP_SPECS["STRAWBERRY"]["cutoff"]
        if day <= cutoff:
            log["straw_delay_window_turns"] += 1
            if day < 10:  # the contrast threshold used in straw_delay_on
                log["straw_delay_window_turns_lt10"] += 1
        return orig_economy(obs, v, pending_drop)

    mod.economy = patched_economy


def run_game(mod, opp_path, seed, cand_seat, log):
    engine_mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    opp_agent = me.load_agent(opp_path)

    def cand_agent(obs, configuration):
        try:
            return mod.agent(obs, configuration)
        except Exception:
            return {}

    agents = [None, None]
    agents[cand_seat] = cand_agent
    agents[1 - cand_seat] = opp_agent
    state = me.structify(
        [
            {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
             "reward": 0.0, "status": "ACTIVE", "info": {}}
            for i in range(2)
        ]
    )
    state = engine_mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    step = 0
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = engine_mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if state[0].status != "ACTIVE" or step >= steps:
            break


def parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, choices=list(CONFIGS))
    ap.add_argument("--opp", required=True, choices=list(OPPS))
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--json")
    args = ap.parse_args()

    seeds = parse_seeds(args.seeds)
    opp_path = OPPS[args.opp]

    log = {
        "melon_rush_harvest_opportunities": 0, "melon_rush_harvest_decisive": 0,
        "melon_rush_dispatch_opportunities": 0,
        "wheat_water_tier_opportunities": 0, "wheat_water_tier_turns_with_opportunity": 0,
        "straw_delay_window_turns": 0, "straw_delay_window_turns_lt10": 0,
        "straw_planted_by_day": {},
        "n_games": 0,
    }

    for seed in seeds:
        for cand_seat in (0, 1):
            mod = load_cand(CONFIGS[args.config])
            instrument(mod, log)
            run_game(mod, opp_path, seed, cand_seat, log)
            log["n_games"] += 1

    print(f"config={args.config} opp={args.opp} seeds={args.seeds} n_games={log['n_games']}")
    print(json.dumps(log, indent=2))

    if args.json:
        with open(args.json, "w") as f:
            json.dump({"config": args.config, "opp": args.opp, "seeds": args.seeds, "log": log}, f, indent=2)


if __name__ == "__main__":
    main()
