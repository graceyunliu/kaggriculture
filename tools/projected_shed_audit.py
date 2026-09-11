#!/usr/bin/env python3
"""Measure whether end-of-day shed discard was visible and actionable at hour 23."""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402

ANIMALS = {"COW", "SHEEP", "GOOSE"}


def _positive(bag):
    return Counter({k: int(v) for k, v in bag.items() if v > 0})


def audit(candidate, opponent, seed, seat=0):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    capacity = int(cfg.get("shedCapacity", 100))
    env = me._Env(cfg, seed)
    paths = [candidate, opponent] if seat == 0 else [opponent, candidate]
    agents = [me.load_agent(p) for p in paths]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
         "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}}
        for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0

    focal_private = state[seat].observation.private
    cur = {"day": 0, "hour": 0}
    losses = []
    checkpoints = {}
    orig_eod = mod._drop_inventories_to_shed

    def wrapped_eod(private, cap):
        if private is focal_private:
            shed = _positive(private["shed"])
            room = max(0, cap - sum(shed.values()))
            accepted = Counter()
            discarded = Counter()
            for inv in private["inventories"]:
                for item, n in list(inv.items()):
                    if n <= 0:
                        continue
                    take = min(int(n), room)
                    accepted[item] += take
                    discarded[item] += int(n) - take
                    room -= take
            if sum(discarded.values()):
                losses.append({"day": cur["day"], "accepted": dict(accepted),
                               "discarded": dict(discarded)})
        orig_eod(private, cap)

    mod._drop_inventories_to_shed = wrapped_eod
    step = 0
    while True:
        obs = state[seat].observation
        cur["day"], cur["hour"] = int(obs["day"]), int(obs["hour"])
        actions = []
        for i in range(2):
            copied = me._fast_copy(state[i].observation)
            copied["step"] = step
            act = agents[i](copied, me._fast_copy(env.configuration))
            state[i].action = act if isinstance(act, dict) else {}
            actions.append(state[i].action)
        if cur["hour"] == 23 and cur["day"] < 29:
            private = obs.private
            shed = _positive(private["shed"])
            carried = Counter()
            for inv in private["inventories"]:
                carried.update(_positive(inv))
            sales = Counter()
            for order in actions[seat].get("market", []):
                if isinstance(order, list) and len(order) >= 3 and order[0] == "SELL":
                    sales[order[1]] += int(order[2])
            projected_after_sales = sum(shed.values()) - sum(
                min(shed.get(item, 0), n) for item, n in sales.items()) + sum(carried.values())
            checkpoints[cur["day"]] = {
                "shed": dict(shed), "carried": dict(carried), "sales": dict(sales),
                "projected_load_before_sales": sum(shed.values()) + sum(carried.values()),
                "projected_overflow_after_sales": max(0, projected_after_sales - capacity),
                "sellable_shed_products": sum(n for k, n in shed.items() if k not in ANIMALS),
            }
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            break
    mod._drop_inventories_to_shed = orig_eod
    for event in losses:
        event["checkpoint"] = checkpoints.get(event["day"], {})
    return {"seed": seed, "seat": seat, "money": state[seat].observation.farms[seat]["money"],
            "losses": losses}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    ap.add_argument("opponent")
    ap.add_argument("--seeds", required=True, help="inclusive range such as 151-170")
    ap.add_argument("--both-seats", action="store_true")
    ap.add_argument("--output")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    rows = [audit(args.candidate, args.opponent, seed, seat)
            for seed in range(lo, hi + 1) for seat in ([0, 1] if args.both_seats else [0])]
    discarded = Counter()
    foreseeable = 0
    events = 0
    for row in rows:
        for event in row["losses"]:
            discarded.update(event["discarded"])
            events += 1
            if event.get("checkpoint", {}).get("projected_overflow_after_sales", 0) > 0:
                foreseeable += 1
    result = {"summary": {"games": len(rows), "loss_events": events,
                           "foreseeable_events": foreseeable,
                           "discarded_by_item": dict(discarded),
                           "discarded_units": sum(discarded.values())},
              "rows": rows}
    print(json.dumps(result["summary"], indent=2))
    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
