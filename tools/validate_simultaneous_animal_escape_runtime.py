#!/usr/bin/env python3
"""Deterministic real-engine validation of two escapes in one daily refresh."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import o42_animal_formation_provenance as formation
import o42_decision_provenance as base


def digest_state(farm, private):
    return base.digest({"farm": base.clean(farm), "private": base.clean(private)})


def run_once():
    eng, defaults = base.me.load_engine("master")
    board_size = int(defaults["boardSize"])
    turns_per_day = int(defaults["turnsPerDay"])
    farm = eng._new_farm(board_size, float(defaults["startingMoney"]))
    private = eng._new_private()
    spawn = tuple(farm["farmer"])
    positions = [spawn, (spawn[0] - 1, spawn[1])]

    # Fixture setup only. All placements, both simultaneous escapes, and both
    # replacements below execute through the real engine functions.
    for x, y in positions:
        farm["tiles"][y][x] = {"kind": eng.ANIMALS["COW"]["structure"]}
    baseline_farm = copy.deepcopy(farm)
    baseline_private = copy.deepcopy(private)
    farms_ref = [[farm, eng._new_farm(board_size, float(defaults["startingMoney"]))]]
    ledger = formation.Ledger(eng, 0, farms_ref, None)
    ledger.install()
    instrumented_actions = []
    baseline_actions = []
    try:
        ledger.observe(farm)
        place = ["PLACE", "COW"]
        for pos in positions:
            farm["farmer"] = list(pos)
            baseline_farm["farmer"] = list(pos)
            private["inventories"][0]["COW"] = 1
            baseline_private["inventories"][0]["COW"] = 1
            instrumented_actions.append(copy.deepcopy(place))
            baseline_actions.append(copy.deepcopy(place))
            eng._apply_unit_action(farm, private, 0, place, board_size, 0, turns_per_day)
            ledger.oa(baseline_farm, baseline_private, 0, place, board_size, 0, turns_per_day)
            ledger.observe(farm)

        entered_before = [e for e in ledger.events if e["event"] == "animal_entered_farm_tiles"]
        retired_ids = [e["asset_id"] for e in entered_before]
        for x, y in positions:
            farm["tiles"][y][x]["consecutive_unfed"] = 1
            farm["tiles"][y][x]["fed_today"] = False
            baseline_farm["tiles"][y][x] = copy.deepcopy(farm["tiles"][y][x])

        ledger.day = 0
        eng._daily_refresh_animals(farm, 0)
        ledger.orf(baseline_farm, 0)
        post_refresh_state_parity = digest_state(farm, private) == digest_state(baseline_farm, baseline_private)
        ledger.observe(farm)
        escapes = [e for e in ledger.events if e["event"] == "animal_escape"]
        leaves = [e for e in ledger.events if e["event"] == "animal_left_farm_tiles"]
        removal_snapshot = [e for e in ledger.events if e["event"] == "farm_animal_snapshot"][-1]
        ids_retired_immediately = all(pos not in ledger.ids for pos in positions)

        for pos in positions:
            farm["farmer"] = list(pos)
            baseline_farm["farmer"] = list(pos)
            private["inventories"][0]["COW"] = 1
            baseline_private["inventories"][0]["COW"] = 1
            instrumented_actions.append(copy.deepcopy(place))
            baseline_actions.append(copy.deepcopy(place))
            eng._apply_unit_action(farm, private, 0, place, board_size, 1, turns_per_day)
            ledger.oa(baseline_farm, baseline_private, 0, place, board_size, 1, turns_per_day)
            ledger.day = 1
            ledger.observe(farm)

        all_entries = [e for e in ledger.events if e["event"] == "animal_entered_farm_tiles"]
        replacement_ids = [e["asset_id"] for e in all_entries[-2:]]
        leave_ids = [e["asset_id"] for e in leaves]
        removal_seqs = [e["seq"] for e in escapes + leaves]
        invariants = {
            "two_escapes_same_refresh": len(escapes) == 2 and len({(e["day"], e["step"]) for e in escapes}) == 1,
            "two_corresponding_leaves": len(leaves) == 2 and {tuple(e["position"]) for e in leaves} == set(positions),
            "each_surrogate_retired_once": sorted(leave_ids) == sorted(retired_ids) and len(set(leave_ids)) == 2,
            "removals_not_collapsed": len({e["seq"] for e in leaves}) == 2 and len({tuple(e["position"]) for e in leaves}) == 2,
            "collection_shrank_by_two": removal_snapshot["size_before"] == 2 and removal_snapshot["size_after"] == 0,
            "ledger_matches_engine_after_removal": removal_snapshot["animals"] == [] and formation.animals(farm) != {},
            "ids_retired_immediately": ids_retired_immediately,
            "replacement_ids_fresh": len(set(replacement_ids)) == 2 and not (set(replacement_ids) & set(retired_ids)),
            "event_sequence_preserves_all_removals": len(set(removal_seqs)) == 4 and max(e["seq"] for e in escapes) < min(e["seq"] for e in leaves),
            "post_refresh_engine_state_parity": post_refresh_state_parity,
            "fixture_action_stream_parity": instrumented_actions == baseline_actions,
            "fixture_terminal_state_parity": digest_state(farm, private) == digest_state(baseline_farm, baseline_private),
        }
        # The current farm contains replacements; the removal-time engine state
        # was empty and is captured by the snapshot. Validate that explicitly.
        invariants["ledger_matches_engine_after_removal"] = (
            removal_snapshot["animals"] == []
            and removal_snapshot["size_after"] == 0
            and post_refresh_state_parity
        )
        if not all(invariants.values()):
            raise RuntimeError(json.dumps(invariants, indent=2))
        return {
            "events": ledger.events,
            "result": {
                "retired_asset_ids": retired_ids,
                "replacement_asset_ids": replacement_ids,
                "invariants": invariants,
            },
        }
    finally:
        ledger.restore()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    first = run_once()
    second = run_once()
    first_bytes = "".join(json.dumps(e, sort_keys=True) + "\n" for e in first["events"]).encode()
    second_bytes = "".join(json.dumps(e, sort_keys=True) + "\n" for e in second["events"]).encode()
    deterministic = first_bytes == second_bytes and first["result"] == second["result"]
    if not deterministic:
        raise RuntimeError("two fixture runs differed")
    (out_dir / "simultaneous_escape_run1.jsonl").write_bytes(first_bytes)
    (out_dir / "simultaneous_escape_run2.jsonl").write_bytes(second_bytes)
    summary = {
        "scope": "simultaneous lifecycle validation fixture only; not natural O42 gameplay",
        "o42_sha256": hashlib.sha256(base.O42.read_bytes()).hexdigest(),
        "engine_path": str(formation.ENGINE),
        "runs": 2,
        "byte_identical_event_logs": deterministic,
        "event_log_sha256": hashlib.sha256(first_bytes).hexdigest(),
        **first["result"],
        "untested": [
            "simultaneous escapes arising naturally in O42 gameplay",
            "more than two simultaneous escapes",
            "non-escape removal causes",
        ],
    }
    (out_dir / "simultaneous_escape_summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
