#!/usr/bin/env python3
"""Focused paired panel for actual BUY_ANIMAL _commit_unit return values only."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import o42_decision_provenance as base


def run(opponent, seed, seat, instrumented):
    engine, defaults = base.me.load_engine("master")
    configuration = dict(defaults)
    configuration["seed"] = None
    environment = base.me._Env(configuration, seed)
    candidate = base.load(base.O42, f"bac{seed}{seat}{instrumented}")
    rival = base.load(base.OPPS[opponent], f"bao{seed}{seat}{instrumented}")
    agents = [None, None]
    agents[seat] = candidate.agent
    agents[1-seat] = rival.agent
    state = base.me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
         "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}}
        for i in range(2)
    ])
    state = engine.interpreter(state, environment)
    original_commit = engine._commit_unit
    clock = {"day": 0, "hour": 0, "step": 0}
    events = []

    if instrumented:
        def commit(op, item, price, farm, private, market, shed_capacity=100):
            result = original_commit(op, item, price, farm, private, market, shed_capacity)
            if farm is state[seat].observation.farms[seat] and op == "BUY_ANIMAL":
                events.append({
                    "event": "buy_animal_commit_result",
                    "op": op,
                    "item": item,
                    "price": price,
                    "committed": bool(result),
                    "day": clock["day"],
                    "hour": clock["hour"],
                    "step": clock["step"],
                })
            return result
        engine._commit_unit = commit

    actions = []
    errors = 0
    step = 0
    try:
        while True:
            clock.update(day=int(state[seat].observation.get("day", 0)),
                         hour=int(state[seat].observation.get("hour", 0)), step=step)
            joint = []
            for player in (0, 1):
                observation = base.me._fast_copy(state[player].observation)
                observation["step"] = step
                try:
                    action = agents[player](observation, base.me._fast_copy(environment.configuration))
                except Exception:
                    action = {}
                    errors += 1
                state[player].action = action
                joint.append(base.clean(action))
            actions.append(joint)
            state = engine.interpreter(state, environment)
            step += 1
            for player_state in state:
                player_state.observation.step = step
            if all(s.status == "DONE" for s in state) or step >= int(configuration["episodeSteps"]):
                break
    finally:
        engine._commit_unit = original_commit

    result = {
        "money": [state[i].observation.farms[i]["money"] for i in range(2)],
        "steps": step,
        "errors": errors,
        "actions_sha256": base.digest(actions),
        "terminal_sha256": base.digest([base.clean(state[i].observation) for i in range(2)]),
    }
    return result, events


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", default="301-340")
    parser.add_argument("--opponents", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    low, high = map(int, args.seeds.split("-"))
    games = []
    for opponent in args.opponents.split(","):
        for seed in range(low, high + 1):
            for seat in (0, 1):
                measured, events = run(opponent, seed, seat, True)
                baseline, _ = run(opponent, seed, seat, False)
                parity_fields = ("money", "steps", "errors", "actions_sha256", "terminal_sha256")
                parity = all(measured[key] == baseline[key] for key in parity_fields)
                if not parity:
                    raise SystemExit(json.dumps({"opponent": opponent, "seed": seed, "seat": seat,
                                                 "measured": measured, "baseline": baseline}, indent=2))
                counts = {}
                for event in events:
                    day = str(event["day"])
                    bucket = counts.setdefault(day, {"committed_true": 0, "committed_false": 0})
                    bucket["committed_true" if event["committed"] else "committed_false"] += 1
                games.append({
                    "opponent": opponent, "seed": seed, "seat": seat,
                    "money": measured["money"], "parity": parity,
                    "actions_sha256": measured["actions_sha256"],
                    "terminal_sha256": measured["terminal_sha256"],
                    "counts_by_day": counts,
                    "events": events,
                })
    output = {
        "schema": "actual engine _commit_unit BUY_ANIMAL return values",
        "o42_path": str(base.O42),
        "o42_sha256": hashlib.sha256(base.O42.read_bytes()).hexdigest(),
        "games": games,
        "validation": {"games": len(games), "all_parity": all(g["parity"] for g in games)},
    }
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"games": len(games), "all_parity": output["validation"]["all_parity"],
                      "o42_sha256": output["o42_sha256"],
                      "committed_true": sum(e["committed"] for g in games for e in g["events"]),
                      "committed_false": sum(not e["committed"] for g in games for e in g["events"])}, indent=2))


if __name__ == "__main__":
    main()
