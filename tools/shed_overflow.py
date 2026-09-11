#!/usr/bin/env python3
"""Shed-overflow / margin-calibration measurement (Sep 12).

Resolves the evolve/directions.yaml `shed_capacity_margin_calibration` DELAY: does the chassis's
existing shed_load > 75 (melon sell trigger) and > 80 (wheat surplus sell trigger) margin, under the
verified shed_cap=100 hard-discard ceiling, actually get exercised -- or is occupancy nowhere near it?

Occupancy is `sum(private["shed"].values())`, sampled once per turn (step), both farms. Three deposit
paths are capacity-gated in the vendor engine:
  - _drop_inventories_to_shed (end-of-day forced dump of per-farmer inventories into the shed --
    overflow here is a TRUE DISCARD, not a choice: the unit is deleted outright)
  - _commit_unit BUY_PRODUCT / BUY_ANIMAL (a blocked purchase when the shed is already full --
    not a discard of existing inventory, just a refused spend; reported separately)
Hooking both distinguishes "shed got close to full" from "shed actually lost real inventory".

Usage:
  KAGG_FIXED_SHOPS=1 python3 tools/shed_overflow.py candidates/O26_CARROT_SIZING.py \
      --opp Opponents/tape_bahaenes_106828159.py --seeds 71-90 [--json out.json]

Standard panel (peter/alaylm/bahaen/yangk), both seats, one seed set:
  for T in peter:tape_peterparker_106816877 alaylm:tape_alaylm_106813359 \
           bahaen:tape_bahaenes_106828159 yangk:tape_yangkuang2_106819729; do
    name=${T%%:*}; file=${T##*:}
    KAGG_FIXED_SHOPS=1 python3 tools/shed_overflow.py candidates/O26_CARROT_SIZING.py \
      --opp Opponents/$file.py --seeds 71-90 --json experiments/shed_overflow_${name}.json
  done
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me  # noqa: E402


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


def run_game(cand_path, opp_path, seed, cand_seat):
    """cand_seat: 0 or 1 -- which player index the candidate occupies."""
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

    # per-farm running stats
    max_load = [0, 0]
    ge90 = [0, 0]
    ge95 = [0, 0]
    ge100 = [0, 0]
    discard_events = [0, 0]  # count of end-of-day forced-dump events where anything was actually lost
    discard_units = [0, 0]  # total units lost to end-of-day forced-dump discard
    discard_by_item = [{}, {}]
    blocked_buys = [0, 0]  # BUY_PRODUCT/BUY_ANIMAL refused purely because shed was full

    orig_drop = mod._drop_inventories_to_shed

    # Tag each private dict with its farm index once so the hook below can attribute discards.
    for i in range(2):
        state[i].observation.private["_shed_overflow_farm_idx"] = i

    def counting_drop(private, capacity):
        farm_idx = private.get("_shed_overflow_farm_idx")
        shed = private["shed"]
        lost_total = 0
        for inv in private["inventories"]:
            for item, n in list(inv.items()):
                if n <= 0:
                    continue
                current = sum(v for k, v in shed.items())
                room = max(0, capacity - current)
                lost = max(0, n - room)
                if lost > 0 and farm_idx is not None:
                    discard_units[farm_idx] += lost
                    discard_by_item[farm_idx][item] = discard_by_item[farm_idx].get(item, 0) + lost
                    lost_total += lost
                # mimic the real deposit so downstream state matches (orig_drop redoes this,
                # but del inv[item] below is idempotent with orig_drop's own del)
        if lost_total > 0 and farm_idx is not None:
            discard_events[farm_idx] += 1
        return orig_drop(private, capacity)

    mod._drop_inventories_to_shed = counting_drop

    orig_commit = mod._commit_unit

    def counting_commit(op, item, price, farm, private, market, shed_capacity=100):
        if op in ("BUY_PRODUCT", "BUY_ANIMAL"):
            if farm["money"] >= price and sum(private["shed"].values()) >= shed_capacity:
                farm_idx = private.get("_shed_overflow_farm_idx")
                if farm_idx is not None:
                    blocked_buys[farm_idx] += 1
        return orig_commit(op, item, price, farm, private, market, shed_capacity)

    mod._commit_unit = counting_commit

    step = 0
    while True:
        obs0 = state[0].observation
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        for i in range(2):
            load = sum(state[i].observation.private["shed"].values())
            if load > max_load[i]:
                max_load[i] = load
            if load >= 90:
                ge90[i] += 1
            if load >= 95:
                ge95[i] += 1
            if load >= 100:
                ge100[i] += 1
        if state[0].status != "ACTIVE" or step >= steps:
            break

    mod._drop_inventories_to_shed = orig_drop
    mod._commit_unit = orig_commit

    return {
        "cand": {
            "max_load": max_load[cand_seat],
            "turns_ge90": ge90[cand_seat],
            "turns_ge95": ge95[cand_seat],
            "turns_ge100": ge100[cand_seat],
            "discard_events": discard_events[cand_seat],
            "discard_units": discard_units[cand_seat],
            "discard_by_item": discard_by_item[cand_seat],
            "blocked_buys": blocked_buys[cand_seat],
        },
        "opp": {
            "max_load": max_load[1 - cand_seat],
            "turns_ge90": ge90[1 - cand_seat],
            "turns_ge95": ge95[1 - cand_seat],
            "turns_ge100": ge100[1 - cand_seat],
            "discard_events": discard_events[1 - cand_seat],
            "discard_units": discard_units[1 - cand_seat],
            "discard_by_item": discard_by_item[1 - cand_seat],
            "blocked_buys": blocked_buys[1 - cand_seat],
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cand")
    ap.add_argument("--opp", required=True)
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--json")
    args = ap.parse_args()

    seeds = parse_seeds(args.seeds)
    rows = []
    for seed in seeds:
        for cand_seat in (0, 1):
            r = run_game(args.cand, args.opp, seed, cand_seat)
            r["seed"] = seed
            r["cand_seat"] = cand_seat
            rows.append(r)

    def agg(key, field):
        vals = [r[key][field] for r in rows]
        return {
            "mean": round(statistics.mean(vals), 3),
            "max": max(vals),
            "n_nonzero": sum(1 for v in vals if v > 0),
        }

    summary = {
        "cand": args.cand,
        "opp": args.opp,
        "n_games": len(rows),
        "cand_max_load": agg("cand", "max_load"),
        "cand_turns_ge90": agg("cand", "turns_ge90"),
        "cand_turns_ge95": agg("cand", "turns_ge95"),
        "cand_turns_ge100": agg("cand", "turns_ge100"),
        "cand_discard_events": agg("cand", "discard_events"),
        "cand_discard_units": agg("cand", "discard_units"),
        "cand_blocked_buys": agg("cand", "blocked_buys"),
        "opp_max_load": agg("opp", "max_load"),
        "opp_turns_ge90": agg("opp", "turns_ge90"),
        "opp_discard_events": agg("opp", "discard_events"),
        "opp_discard_units": agg("opp", "discard_units"),
    }
    print(json.dumps(summary, indent=2))
    if args.json:
        with open(args.json, "w") as f:
            json.dump({"summary": summary, "rows": rows}, f, indent=2)


if __name__ == "__main__":
    main()
