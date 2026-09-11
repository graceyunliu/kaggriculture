#!/usr/bin/env python3
"""Instrumented trace for shed_capacity_margin_calibration Stage-1 (AGE-363 candidate family):
for every turn shed_load enters the melon [65,75) or wheat [70,80) intervention window, log the
subconditions and classify whether O34's tighter threshold would have changed the actual SELL order,
vs. the baseline O26 threshold already firing for another reason (price/day) -- "behaviorally redundant"
vs "genuinely decisive".

Runs the BASELINE agent's real trajectory (O26 vs O26 mirror) and evaluates what each threshold would
decide at each in-window turn using the actual observation at that point -- valid because the Sep-11
first-pass panel showed O26 and O34 produce byte-identical trajectories on these seeds, so replaying
under O26 and asking "what would O34 have decided here" is equivalent to actually running O34.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/shed_tighten_trace.py --seeds 71-75
"""
import sys, os, argparse, importlib.util, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me

CAND_A = os.path.join(ROOT, "candidates/O34_SHED_TIGHT.py")   # tightened: melon>65, wheat>70
CAND_B = os.path.join(ROOT, "candidates/O26_CARROT_SIZING.py")  # baseline: melon>75, wheat>80

def load_module_with_knobs(path, tag):
    spec = importlib.util.spec_from_file_location(f"knobs_{tag}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

KM_A = load_module_with_knobs(CAND_A, "a")  # tightened thresholds live inline in code, not KNOBS
KM_B = load_module_with_knobs(CAND_B, "b")
KNOBS = KM_B.KNOBS  # melon_floor, wheat_sell_price, wheat_stock, wheat_hold_days shared by both variants
ANIMALS = KM_B.ANIMALS


def parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part: continue
        if "-" in part:
            a, b = part.split("-"); out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def trace_seed(seed, cand_seat=0):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    # separate module instances per seat -- each candidate keeps its own global state (S dict etc.),
    # reusing one loaded module for both seats corrupts both trajectories.
    agents = [me.load_agent(CAND_B), me.load_agent(CAND_B)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
        "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    step = 0
    records = []
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if i == cand_seat:
                o = obs
                shed = o["private"]["shed"]
                shed_load = sum(n for k, n in shed.items() if k not in ANIMALS and n > 0)
                prices = o["market"]["prices"]
                day = o["day"]; hour = o["hour"]

                # --- melon ---
                n_melon = shed.get("MELON", 0)
                if n_melon > 0 and 65 <= shed_load < 75:
                    price_cond = prices.get("MELON", 0) >= KNOBS["melon_floor"]
                    day_cond = day >= 27
                    old_shed_cond = shed_load > 75
                    new_shed_cond = shed_load > 65
                    decision_old = price_cond or day_cond or old_shed_cond
                    decision_new = price_cond or day_cond or new_shed_cond
                    records.append({
                        "item": "MELON", "day": day, "hour": hour, "shed_load": shed_load,
                        "price": prices.get("MELON", 0), "price_cond": price_cond, "day_cond": day_cond,
                        "old_shed_cond": old_shed_cond, "new_shed_cond": new_shed_cond,
                        "decision_old": decision_old, "decision_new": decision_new,
                        "decisive": decision_old != decision_new,
                    })

                # --- wheat --- (shed_load>80/70 only matters inside the day<29 elif branch when the
                # wheat price condition is already true; it changes the surplus RESERVE, not a gate)
                w = shed.get("WHEAT", 0)
                if 70 <= shed_load < 80 and day < 29:
                    farm_view = KM_B.perceive(o)
                    inv = o["private"].get("inventories") or []
                    carried_animals = sum(iv.get(a, 0) for iv in inv for a in ANIMALS)
                    shed_animals = sum(shed.get(a, 0) for a in ANIMALS)
                    n_active = len(farm_view["animals"])
                    n_total = n_active + shed_animals + carried_animals
                    wheat_price_cond = prices.get("WHEAT", 0) >= (KNOBS["wheat_sell_price"] if day < 27 else 30)
                    if wheat_price_cond:
                        hold = KNOBS["wheat_stock"] if day < 27 else 0
                        reserve_feed = (n_total + 3) + (n_total * KNOBS["wheat_hold_days"] if day < 27 else 0)
                        surplus_old = int(w - reserve_feed - hold)
                        if shed_load > 80:
                            surplus_old = int(w - (n_total + 3))
                        surplus_new = int(w - reserve_feed - hold)
                        if shed_load > 70:
                            surplus_new = int(w - (n_total + 3))
                        records.append({
                            "item": "WHEAT", "day": day, "hour": hour, "shed_load": shed_load,
                            "price": prices.get("WHEAT", 0), "price_cond": wheat_price_cond,
                            "w_in_shed": w, "surplus_old": surplus_old, "surplus_new": surplus_new,
                            "order_old": max(0, surplus_old), "order_new": max(0, surplus_new),
                            "decisive": max(0, surplus_old) != max(0, surplus_new),
                        })
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if state[0].status != "ACTIVE" or step >= steps:
            break
    return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", required=True)
    args = ap.parse_args()
    all_records = []
    for seed in parse_seeds(args.seeds):
        recs = trace_seed(seed)
        for r in recs:
            r["seed"] = seed
        all_records.extend(recs)

    print(json.dumps(all_records, indent=2))
    n_melon = sum(1 for r in all_records if r["item"] == "MELON")
    n_wheat = sum(1 for r in all_records if r["item"] == "WHEAT")
    n_melon_decisive = sum(1 for r in all_records if r["item"] == "MELON" and r["decisive"])
    n_wheat_decisive = sum(1 for r in all_records if r["item"] == "WHEAT" and r["decisive"])
    print("=== SUMMARY ===")
    print(f"melon in-window events: {n_melon}, decisive: {n_melon_decisive}")
    print(f"wheat in-window events: {n_wheat}, decisive: {n_wheat_decisive}")


if __name__ == "__main__":
    main()
