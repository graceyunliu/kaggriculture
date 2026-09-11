#!/usr/bin/env python3
"""shed_capacity_margin_calibration (evolve/directions.yaml DELAY) -- cheap calibration audit,
not a candidate pipeline. Answers: is the chassis's shed_load>75/80 sell-trigger margin (which
excludes ANIMALS from its own shed_load formula -- candidates/O26_CARROT_SIZING.py:382) actually
well-calibrated against the engine's TRUE hard cap, which is sum(private["shed"].values())
INCLUDING animals sitting in the shed between BUY_ANIMAL and PICKUP (vendor kaggriculture.py
_commit_unit / _apply_unit_action)?

Measures, per turn (not just per day -- overflow can happen and get silently discarded by
_drop_inventories_to_shed at end-of-day, or blocked outright by BUY_PRODUCT/BUY_ANIMAL mid-day):
  - true engine shed occupancy sum(shed.values())            [what the cap actually checks]
  - chassis shed_load (excludes ANIMALS)                      [what the 75/80 triggers see]
  - the gap between them (animals sitting in shed, uncounted by the chassis metric)
  - turns >=90 / >=95 / ==100 on the TRUE occupancy
  - actual end-of-day discard events: inventory that could not fit and was deleted outright
    (_drop_inventories_to_shed), detected by diffing pre/post private["inventories"] sum against
    the room that was available.
"""
import sys, copy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me

ANIMALS = {"COW", "SHEEP", "GOOSE"}
CAND = str(ROOT / "candidates/O26_CARROT_SIZING.py")
TAPES = [
    str(ROOT / "Opponents/tape_alaylm_106813359.py"),
    str(ROOT / "Opponents/tape_bahaenes_106828159.py"),
    str(ROOT / "Opponents/tape_peterparker_106816877.py"),
    str(ROOT / "Opponents/tape_yangkuang2_106819729.py"),
]
SEEDS = list(range(11, 31))  # set1, matches the project's standard first seed set


def run_one(cand_path, opp_path, seed, cand_seat=0):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(cand_path), me.load_agent(opp_path)] if cand_seat == 0 else \
             [me.load_agent(opp_path), me.load_agent(cand_path)]

    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0

    tpd = int(cfg["turnsPerDay"])
    steps = int(cfg["episodeSteps"])
    shed_cap = int(mod.get(env.configuration, "shedCapacity", 100))

    max_true = 0
    max_chassis_metric = 0
    turns_ge90 = turns_ge95 = turns_eq100 = 0
    discard_events = 0
    discard_units = 0
    discard_by_item = {}
    step = 0
    while True:
        obs0 = state[0].observation
        farm = obs0.farms[cand_seat]
        private = state[cand_seat].observation.private
        shed = private["shed"]
        true_occ = sum(shed.values())
        chassis_metric = sum(n for k, n in shed.items() if k not in ANIMALS and n > 0)
        max_true = max(max_true, true_occ)
        max_chassis_metric = max(max_chassis_metric, chassis_metric)
        if true_occ >= 90:
            turns_ge90 += 1
        if true_occ >= 95:
            turns_ge95 += 1
        if true_occ >= shed_cap:
            turns_eq100 += 1

        # detect end-of-day discard: snapshot carried-inventory total + shed total just before
        # the day boundary, compare to shed total just after.
        is_last_hour_of_day = (obs0.hour == tpd - 1)
        pre_carry_by_item = {}
        if is_last_hour_of_day:
            for inv in private["inventories"]:
                for k_, v_ in inv.items():
                    if v_ > 0:
                        pre_carry_by_item[k_] = pre_carry_by_item.get(k_, 0) + v_
        pre_carry_total = sum(pre_carry_by_item.values())
        pre_shed_total = true_occ if is_last_hour_of_day else 0

        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act if isinstance(act, dict) else {}
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step

        if is_last_hour_of_day:
            post_private = state[cand_seat].observation.private
            post_shed_total = sum(post_private["shed"].values())
            room_was = max(0, shed_cap - pre_shed_total)
            overflow = pre_carry_total - room_was
            if overflow > 0:
                discard_events += 1
                discard_units += overflow
                # attribute the overflow to items proportionally (engine drops in dict-iteration
                # order until room runs out; proportional split is a reasonable diagnostic estimate)
                for k_, v_ in pre_carry_by_item.items():
                    share = overflow * (v_ / pre_carry_total)
                    discard_by_item[k_] = discard_by_item.get(k_, 0.0) + share

        if all(s.status == "DONE" for s in state):
            break
        if step >= steps:
            break

    return {
        "max_true_occ": max_true, "max_chassis_metric": max_chassis_metric,
        "gap": max_true - max_chassis_metric,
        "turns_ge90": turns_ge90, "turns_ge95": turns_ge95, "turns_at_cap": turns_eq100,
        "discard_events": discard_events, "discard_units": discard_units,
        "discard_by_item": discard_by_item,
    }


def main():
    agg = {"max_true_occ": 0, "max_chassis_metric": 0, "gap": 0,
           "turns_ge90": 0, "turns_ge95": 0, "turns_at_cap": 0,
           "discard_events": 0, "discard_units": 0}
    agg_by_item = {}
    n = 0
    worst = None
    for tape in TAPES:
        for seed in SEEDS:
            r = run_one(CAND, tape, seed, cand_seat=0)
            n += 1
            for k in agg:
                agg[k] += r[k]
            for k_, v_ in r["discard_by_item"].items():
                agg_by_item[k_] = agg_by_item.get(k_, 0.0) + v_
            if worst is None or r["max_true_occ"] > worst[1]["max_true_occ"]:
                worst = (f"{Path(tape).stem} seed={seed}", r)
            if r["discard_events"] > 0:
                print(f"  DISCARD: {Path(tape).stem} seed={seed}: {r['discard_events']} events, {r['discard_units']} units lost")
    print(f"\n=== shed_capacity_margin_calibration: {n} games (4 tapes x seeds 11-30, seat 0) ===")
    print(f"mean max_true_occ (engine's real cap check): {agg['max_true_occ']/n:.1f} / 100")
    print(f"mean max_chassis shed_load metric (excludes animals): {agg['max_chassis_metric']/n:.1f} / 100")
    print(f"mean gap (animals sitting in shed, invisible to chassis metric): {agg['gap']/n:.1f}")
    print(f"mean turns/game >=90: {agg['turns_ge90']/n:.2f}   >=95: {agg['turns_ge95']/n:.2f}   at cap(100): {agg['turns_at_cap']/n:.2f}")
    print(f"total discard events across panel: {agg['discard_events']}  total units silently discarded: {agg['discard_units']}")
    print(f"discarded units by item (proportional attribution): { {k: round(v,1) for k,v in sorted(agg_by_item.items(), key=lambda kv:-kv[1])} }")
    print(f"worst single game: {worst[0]} -> {worst[1]}")


if __name__ == "__main__":
    main()
