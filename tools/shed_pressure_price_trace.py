#!/usr/bin/env python3
"""shed_capacity_margin_calibration resolving measurement (Sep 12, 3rd pass):

The shed_threshold_tightening_redundant trace only sampled turns inside the OLD trigger windows
([65,75) melon, [70,80) wheat) and found price_cond already true in every one -- so it never actually
tested whether a "capacity pressure high AND price_cond false" population exists at all. This script
removes the window restriction and asks that question directly: for every turn where shed_load is under
real capacity pressure (>=90, matching the corrected shed_overflow.py's dwell-time definition), is there
sellable MELON/WHEAT sitting in the shed that CAN'T be sold because price is below the sell floor?

Runs O26_CARROT_SIZING as seat 0 against the real standard-panel opponent tapes (not a mirror -- price
pressure is opponent-market-dependent, so self-play would understate it), both seats, so it also serves
as an independent 3rd cross-check of the shed_overflow.py corrected result.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/shed_pressure_price_trace.py --seeds 71-90 --json out.json
"""
import sys, os, argparse, importlib.util, json, statistics
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me

CAND = os.path.join(ROOT, "candidates/O26_CARROT_SIZING.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}

def load_module_with_knobs(path, tag):
    spec = importlib.util.spec_from_file_location(f"knobs_{tag}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

KM = load_module_with_knobs(CAND, "cand")
KNOBS = KM.KNOBS
ANIMALS = KM.ANIMALS

PRESSURE_THRESHOLD = 90  # matches shed_overflow.py's turns_ge90 definition


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


def trace_game(cand_path, opp_path, seed, cand_seat):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agent_paths = [None, None]
    agent_paths[cand_seat] = cand_path
    agent_paths[1 - cand_seat] = opp_path
    agents = [me.load_agent(p) for p in agent_paths]
    state = me.structify(
        [
            {
                "observation": {"player": i, "remainingOverageTime": 60, "step": 0},
                "action": {},
                "reward": 0.0,
                "status": "ACTIVE",
                "info": {},
            }
            for i in range(2)
        ]
    )
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    step = 0
    records = []
    pressure_turns = 0
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            if i == cand_seat:
                o = obs
                shed = o["private"]["shed"]
                shed_load = sum(n for k, n in shed.items() if k not in ANIMALS and n > 0)
                if shed_load >= PRESSURE_THRESHOLD:
                    pressure_turns += 1
                    prices = o["market"]["prices"]
                    day = o["day"]

                    n_melon = shed.get("MELON", 0)
                    if n_melon > 0:
                        melon_price_cond = prices.get("MELON", 0) >= KNOBS["melon_floor"]
                        melon_day_cond = day >= 27
                        if not melon_price_cond and not melon_day_cond:
                            records.append({
                                "item": "MELON", "day": day, "hour": o["hour"], "shed_load": shed_load,
                                "units_stuck": n_melon, "price": prices.get("MELON", 0),
                                "floor": KNOBS["melon_floor"],
                            })

                    w = shed.get("WHEAT", 0)
                    if w > 0 and day < 29:
                        wheat_price_cond = prices.get("WHEAT", 0) >= (KNOBS["wheat_sell_price"] if day < 27 else 30)
                        if not wheat_price_cond:
                            records.append({
                                "item": "WHEAT", "day": day, "hour": o["hour"], "shed_load": shed_load,
                                "units_stuck": w, "price": prices.get("WHEAT", 0),
                                "floor": KNOBS["wheat_sell_price"] if day < 27 else 30,
                            })
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if state[0].status != "ACTIVE" or step >= steps:
            break
    return records, pressure_turns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--json")
    args = ap.parse_args()

    seeds = parse_seeds(args.seeds)
    all_records = []
    total_pressure_turns = 0
    total_games = 0
    games_with_stuck_melon = 0
    games_with_stuck_wheat = 0

    for opp_name, opp_path in OPPS.items():
        for seed in seeds:
            for cand_seat in (0, 1):
                recs, pressure_turns = trace_game(CAND, opp_path, seed, cand_seat)
                total_games += 1
                total_pressure_turns += pressure_turns
                for r in recs:
                    r["seed"] = seed
                    r["opp"] = opp_name
                    r["cand_seat"] = cand_seat
                    all_records.append(r)
                if any(r["item"] == "MELON" for r in recs):
                    games_with_stuck_melon += 1
                if any(r["item"] == "WHEAT" for r in recs):
                    games_with_stuck_wheat += 1

    n_melon = sum(1 for r in all_records if r["item"] == "MELON")
    n_wheat = sum(1 for r in all_records if r["item"] == "WHEAT")

    print("=== SUMMARY ===")
    print(f"games: {total_games}  total turns with shed_load>={PRESSURE_THRESHOLD}: {total_pressure_turns}")
    print(f"melon stuck-behind-price events: {n_melon}  (games affected: {games_with_stuck_melon}/{total_games})")
    print(f"wheat stuck-behind-price events: {n_wheat}  (games affected: {games_with_stuck_wheat}/{total_games})")
    if all_records:
        print("\nsample records:")
        for r in all_records[:15]:
            print(r)

    out = {
        "summary": {
            "games": total_games,
            "pressure_turns": total_pressure_turns,
            "melon_events": n_melon,
            "wheat_events": n_wheat,
            "games_with_stuck_melon": games_with_stuck_melon,
            "games_with_stuck_wheat": games_with_stuck_wheat,
        },
        "records": all_records,
    }
    if args.json:
        with open(args.json, "w") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
