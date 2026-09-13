#!/usr/bin/env python3
"""Minimal real-engine runtime validation of animal escape lifecycle tracing."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import o42_animal_formation_provenance as formation
import o42_decision_provenance as base


def state_digest(farm, private):
    return base.digest({"farm": base.clean(farm), "private": base.clean(private)})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    eng, defaults = base.me.load_engine("master")
    board_size = int(defaults["boardSize"])
    turns_per_day = int(defaults["turnsPerDay"])
    farm = eng._new_farm(board_size, float(defaults["startingMoney"]))
    private = eng._new_private()

    # Validation fixture setup only: create the required matching structure and
    # inventory. Placement, escape, and replacement all run through real engine
    # functions below.
    pos = tuple(farm["farmer"])
    x, y = pos
    farm["tiles"][y][x] = {"kind": eng.ANIMALS["COW"]["structure"]}
    private["inventories"][0]["COW"] = 1
    baseline_farm = copy.deepcopy(farm)
    baseline_private = copy.deepcopy(private)

    farms_ref = [[farm, eng._new_farm(board_size, float(defaults["startingMoney"]))]]
    ledger = formation.Ledger(eng, 0, farms_ref, None)
    ledger.install()
    actions_instrumented = []
    actions_baseline = []
    try:
        ledger.observe(farm)

        place = ["PLACE", "COW"]
        actions_instrumented.append(place)
        eng._apply_unit_action(farm, private, 0, place, board_size, 0, turns_per_day)
        actions_baseline.append(copy.deepcopy(place))
        ledger.oa(baseline_farm, baseline_private, 0, place, board_size, 0, turns_per_day)
        ledger.observe(farm)
        first_entry = next(e for e in ledger.events if e["event"] == "animal_entered_farm_tiles")
        retired_id = first_entry["asset_id"]

        pre_escape = copy.deepcopy(farm["tiles"][y][x])
        pre_escape["consecutive_unfed"] = 1
        pre_escape["fed_today"] = False
        farm["tiles"][y][x] = copy.deepcopy(pre_escape)
        baseline_farm["tiles"][y][x] = copy.deepcopy(pre_escape)

        ledger.day = 0
        eng._daily_refresh_animals(farm, 0)
        ledger.orf(baseline_farm, 0)
        post_refresh_engine_parity = state_digest(farm, private) == state_digest(baseline_farm, baseline_private)
        ledger.observe(farm)

        escape_event = next(e for e in ledger.events if e["event"] == "animal_escape")
        leave_event = next(e for e in ledger.events if e["event"] == "animal_left_farm_tiles")
        removal_snapshot = next(
            e for e in ledger.events
            if e["event"] == "farm_animal_snapshot" and e["seq"] > leave_event["seq"]
        )
        retired_immediately_after_removal = pos not in ledger.ids

        private["inventories"][0]["COW"] = 1
        baseline_private["inventories"][0]["COW"] = 1
        actions_instrumented.append(place)
        eng._apply_unit_action(farm, private, 0, place, board_size, 1, turns_per_day)
        actions_baseline.append(copy.deepcopy(place))
        ledger.oa(baseline_farm, baseline_private, 0, place, board_size, 1, turns_per_day)
        ledger.day = 1
        ledger.observe(farm)
        entries = [e for e in ledger.events if e["event"] == "animal_entered_farm_tiles"]
        replacement_id = entries[-1]["asset_id"]

        action_parity = actions_instrumented == actions_baseline
        terminal_parity = state_digest(farm, private) == state_digest(baseline_farm, baseline_private)
        escape_count = sum(e["event"] == "animal_escape" for e in ledger.events)
        left_count = sum(e["event"] == "animal_left_farm_tiles" for e in ledger.events)
        invariants = {
            "real_engine_escape_event_observed": escape_count == 1,
            "animal_left_farm_tiles_observed": left_count == 1,
            "pre_removal_identity_matches": leave_event.get("asset_id") == retired_id,
            "pre_removal_state_matches_engine": escape_event.get("animal_before") == {k: pre_escape.get(k) for k in formation.RELEVANT},
            "removal_cause_is_escape": leave_event.get("cause") == "escape",
            "escape_and_leave_positions_match": escape_event.get("position") == leave_event.get("position") == list(pos),
            "surrogate_id_retired_immediately": retired_immediately_after_removal,
            "post_removal_collection_empty": removal_snapshot.get("size_after") == 0 and removal_snapshot.get("animals") == [],
            "shrink_conservation": removal_snapshot.get("size_before") == 1 and removal_snapshot.get("size_after") == 0 and left_count == 1,
            "replacement_received_new_id": replacement_id != retired_id,
            "retired_id_not_reused": sum(e.get("asset_id") == retired_id and e["event"] == "animal_entered_farm_tiles" for e in ledger.events) == 1,
            "post_refresh_engine_state_parity": post_refresh_engine_parity,
            "fixture_action_stream_parity": action_parity,
            "fixture_terminal_state_parity": terminal_parity,
        }
        if not all(invariants.values()):
            raise SystemExit(json.dumps(invariants, indent=2))
    finally:
        ledger.restore()

    log_path = out_dir / "escape_lifecycle.jsonl"
    log_path.write_text("".join(json.dumps(e, sort_keys=True) + "\n" for e in ledger.events))
    summary = {
        "scope": "deterministic validation fixture; not a strategy or outcome experiment",
        "fixture_setup": "matching cow pasture and one cow inventory item; placement/escape/replacement use real engine functions",
        "o42_sha256": hashlib.sha256(base.O42.read_bytes()).hexdigest(),
        "engine_path": str(formation.ENGINE),
        "escape_event_count": escape_count,
        "animal_left_farm_tiles_count": left_count,
        "retired_asset_id": retired_id,
        "replacement_asset_id": replacement_id,
        "invariants": invariants,
        "untested": [
            "natural O42 gameplay producing an escape",
            "multiple simultaneous escapes",
            "non-escape animal removal causes",
            "escape of sheep or goose",
            "surrogate identity across position changes (animals do not move in the engine)",
        ],
        "event_log": str(log_path),
    }
    (out_dir / "escape_validation_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
