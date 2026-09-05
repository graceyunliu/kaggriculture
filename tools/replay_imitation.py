#!/usr/bin/env python3
"""Extract general cadence/batching statistics from replay tapes; never replay actions."""
from __future__ import annotations

import argparse
import ast
import base64
import json
import statistics
import zlib
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_actions(path):
    """Decode the embedded tape payload without executing the Python tape module."""
    tree = ast.parse(Path(path).read_text())
    assign = next(n for n in tree.body if isinstance(n, ast.Assign) and
                  any(isinstance(t, ast.Name) and t.id == "_ACTIONS" for t in n.targets))
    for node in ast.walk(assign.value):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            try:
                value = json.loads(zlib.decompress(base64.b85decode(node.value)).decode("utf-8"))
            except Exception:  # not the payload string
                continue
            if isinstance(value, list):
                return value
    raise ValueError(f"no decodable _ACTIONS payload in {path}")


def commands(turn):
    farmer = turn.get("farmer") or []
    if farmer:
        yield ("farmer", farmer)
    for i, command in enumerate(turn.get("hands") or []):
        if command:
            yield (f"hand:{i}", command)


def summarize(paths):
    pickup_sizes = []
    water_days = defaultdict(set)
    work_by_day = defaultdict(int)
    tape_rows = []
    for path in paths:
        actions = load_actions(path)
        local_water = 0
        for step, turn in enumerate(actions):
            day = step // 24
            for actor, command in commands(turn):
                op = command[0]
                if op == "WATER":
                    water_days[(str(path), actor)].add(day)
                    local_water += 1
                if op == "PICKUP" and len(command) >= 3 and command[1] == "WHEAT":
                    pickup_sizes.append(float(command[2]))
                if op in {"WATER", "HARVEST", "PLANT", "DIG", "FERTILIZE"}:
                    work_by_day[(str(path), day)] += 1
        tape_rows.append({"tape": Path(path).name, "turns": len(actions), "water_actions": local_water})
    intervals = []
    for days in water_days.values():
        ordered = sorted(days)
        intervals.extend(b - a for a, b in zip(ordered, ordered[1:]))
    mean_pickup = statistics.mean(pickup_sizes) if pickup_sizes else 0.0
    mean_cadence = statistics.mean(intervals) if intervals else 0.0
    mean_daily_work = statistics.mean(work_by_day.values()) if work_by_day else 0.0
    return {
        "tapes": tape_rows,
        "statistics": {
            "wheat_pickup_count": len(pickup_sizes),
            "mean_wheat_pickup_size": round(mean_pickup, 3),
            "mean_days_between_water_service_by_hand": round(mean_cadence, 3),
            "alternate_day_water_interval_share": round(
                sum(x == 2 for x in intervals) / len(intervals), 3) if intervals else 0.0,
            "mean_crop_work_actions_per_active_day": round(mean_daily_work, 3),
        },
        "suggestions": [
            {"block": "sweep", "params": {
                "CROP_SWEEP_LEN": max(3, min(10, round(mean_pickup or 6))),
                "CROP_SWEEP_RADIUS": max(2, min(6, round(mean_cadence + 3))) if mean_cadence else 4,
            }, "basis": "aggregate pickup batching and watering cadence"},
            {"block": "crop_admission", "params": {
                "NEAR_RADIUS": max(2, min(5, round(mean_cadence + 2))) if mean_cadence else 3,
            }, "basis": "aggregate watering revisit cadence"},
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tapes", nargs="*", type=Path)
    ap.add_argument("--limit", type=int, default=8)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    paths = args.tapes or sorted((ROOT / "Opponents").glob("tape_*.py"))[:args.limit]
    result = summarize(paths)
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(text + "\n")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
