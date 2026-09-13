#!/usr/bin/env python3
"""Measurement-only strong/weak analysis of the accepted animal formation ledger."""
from __future__ import annotations

import argparse
import collections
import gzip
import json
import math
from pathlib import Path

try:
    from scipy import stats
except ImportError:
    stats = None


STAGES = (
    "observation_rebuilds",
    "animal_observations",
    "purchase_commits",
    "successful_placements",
    "lifecycle_additions",
    "lifecycle_removals",
    "escape_removals",
    "route_entries",
    "route_candidate_total",
    "snapshot_live_total",
    "snapshot_count",
)
FLOW_STAGES = {
    "observation_rebuilds", "animal_observations", "purchase_commits",
    "successful_placements", "lifecycle_additions", "lifecycle_removals",
    "escape_removals", "route_entries", "route_candidate_total",
    "snapshot_live_total", "snapshot_count",
}


def mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def metric_value(row, key):
    if key == "mean_observed_pool":
        return row["metrics"].get("animal_observations", 0) / max(1, row["metrics"].get("observation_rebuilds", 0))
    if key == "mean_route_entry_pool":
        return row["metrics"].get("route_candidate_total", 0) / max(1, row["metrics"].get("route_entries", 0))
    if key == "mean_live_surrogates":
        return row["metrics"].get("snapshot_live_total", 0) / max(1, row["metrics"].get("snapshot_count", 0))
    return row["metrics"].get(key, 0)


def parse_log(path, meta):
    totals = collections.Counter()
    daily = collections.defaultdict(collections.Counter)
    entered_ids, removed_ids = [], []
    with gzip.open(path, "rt") as handle:
        for line in handle:
            event = json.loads(line)
            name = event.get("event")
            family = event.get("family")
            day = int(event.get("day", -1))
            keys = []
            if family == "perceive" and name == "function_return":
                keys.append(("observation_rebuilds", 1))
            if family == "perceive" and name == "perceive_animal_append_committed":
                keys.append(("animal_observations", 1))
            if name == "animal_purchase" and event.get("committed"):
                keys.append(("purchase_commits", 1))
            if name == "animal_unit_action" and event.get("action", [None])[0] == "PLACE" and event.get("success"):
                keys.append(("successful_placements", 1))
            if name == "animal_entered_farm_tiles":
                keys.append(("lifecycle_additions", 1)); entered_ids.append(event.get("asset_id"))
            if name == "animal_left_farm_tiles":
                keys.append(("lifecycle_removals", 1)); removed_ids.append(event.get("asset_id"))
                if event.get("cause") == "escape": keys.append(("escape_removals", 1))
            if family == "_build_route" and name == "function_enter":
                keys.extend((("route_entries", 1), ("route_candidate_total", len(event.get("raw_candidates", [])))))
            if name == "farm_animal_snapshot":
                keys.extend((("snapshot_count", 1), ("snapshot_live_total", int(event.get("size_after", 0)))))
            for key, value in keys:
                totals[key] += value
                if 0 <= day <= 29: daily[day][key] += value
    if len(entered_ids) != len(set(entered_ids)):
        raise RuntimeError(f"duplicate surrogate entry ID: {path}")
    if not set(removed_ids).issubset(set(entered_ids)):
        raise RuntimeError(f"removal without prior surrogate: {path}")
    totals["persistent_ids_formed"] = len(entered_ids)
    totals["persistent_ids_removed"] = len(removed_ids)
    totals["persistent_ids_terminal"] = len(set(entered_ids) - set(removed_ids))
    return {**meta, "metrics": dict(totals), "daily": {str(k): dict(v) for k, v in daily.items()}}


def compare(rows, key, daily_day=None, cumulative=False):
    values = []
    for row in rows:
        if daily_day is None:
            value = metric_value(row, key)
        elif cumulative:
            value = sum(row["daily"].get(str(d), {}).get(key, 0) for d in range(daily_day + 1))
        else:
            value = row["daily"].get(str(daily_day), {}).get(key, 0)
            if key == "mean_observed_pool":
                den = row["daily"].get(str(daily_day), {}).get("observation_rebuilds", 0)
                num = row["daily"].get(str(daily_day), {}).get("animal_observations", 0)
                value = num / max(1, den)
            elif key == "mean_route_entry_pool":
                den = row["daily"].get(str(daily_day), {}).get("route_entries", 0)
                num = row["daily"].get(str(daily_day), {}).get("route_candidate_total", 0)
                value = num / max(1, den)
            elif key == "mean_live_surrogates":
                den = row["daily"].get(str(daily_day), {}).get("snapshot_count", 0)
                num = row["daily"].get(str(daily_day), {}).get("snapshot_live_total", 0)
                value = num / max(1, den)
        values.append((row, value))
    cell_means = collections.defaultdict(list)
    for row, value in values: cell_means[(row["opponent"], row["seat"])].append(value)
    centers = {cell: mean(xs) for cell, xs in cell_means.items()}
    strong_raw, weak_raw, strong_res, weak_res = [], [], [], []
    for row, value in values:
        residual = value - centers[(row["opponent"], row["seat"])]
        (strong_raw if row["label"] == "strong" else weak_raw).append(value)
        (strong_res if row["label"] == "strong" else weak_res).append(residual)
    if stats and len(strong_res) > 1 and len(weak_res) > 1:
        test = stats.ttest_ind(strong_res, weak_res, equal_var=False)
        statistic, p_value = float(test.statistic), float(test.pvalue)
    else:
        va = sum((x-mean(strong_res))**2 for x in strong_res) / max(1, len(strong_res)-1)
        vb = sum((x-mean(weak_res))**2 for x in weak_res) / max(1, len(weak_res)-1)
        se = math.sqrt(va/max(1, len(strong_res)) + vb/max(1, len(weak_res)))
        statistic = (mean(strong_res)-mean(weak_res))/se if se else 0.0
        p_value = math.erfc(abs(statistic)/math.sqrt(2))
    return {
        "n_strong": len(strong_raw), "n_weak": len(weak_raw),
        "strong_mean": mean(strong_raw), "weak_mean": mean(weak_raw),
        "raw_difference": mean(strong_raw)-mean(weak_raw),
        "residualized_difference": mean(strong_res)-mean(weak_res),
        "welch_t": statistic, "p_value": p_value,
    }


def bh(items, field="full"):
    order = sorted(range(len(items)), key=lambda i: items[i][field]["p_value"])
    q = 1.0
    for rank, index in reversed(list(enumerate(order, 1))):
        q = min(q, items[index][field]["p_value"] * len(items) / rank)
        items[index][field]["q_bh"] = q


def validations(rows, key, day=None, cumulative=False):
    opponents = sorted({row["opponent"] for row in rows})
    return {
        "seed_halves": {
            "301_320": compare([r for r in rows if r["seed"] <= 320], key, day, cumulative),
            "321_340": compare([r for r in rows if r["seed"] >= 321], key, day, cumulative),
        },
        "leave_one_opponent_out": {
            opponent: compare([r for r in rows if r["opponent"] != opponent], key, day, cumulative)
            for opponent in opponents
        },
        "by_opponent": {opponent: compare([r for r in rows if r["opponent"] == opponent], key, day, cumulative) for opponent in opponents},
        "by_seat": {str(seat): compare([r for r in rows if r["seat"] == seat], key, day, cumulative) for seat in (0, 1)},
    }


def replicated(full, validation):
    direction = 1 if full["residualized_difference"] > 0 else -1
    required = list(validation["seed_halves"].values()) + list(validation["leave_one_opponent_out"].values())
    return full.get("q_bh", 1) <= .05 and full["residualized_difference"] != 0 and all(x["residualized_difference"] * direction > 0 for x in required)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--panel-dir", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    panel = Path(args.panel_dir)
    rows = []
    parity_rows = []
    for opponent_dir in sorted(p for p in panel.iterdir() if p.is_dir()):
        summary = json.loads((opponent_dir / "smoke_summary.json").read_text())
        parity_rows.extend(summary["rows"])
        for game in summary["rows"]:
            money = game["instrumented"]["money"]
            seat = int(game["seat"])
            margin = money[seat] - money[1-seat]
            if margin == 0: label = "tie"
            else: label = "strong" if margin > 0 else "weak"
            log = opponent_dir / f"{game['opponent']}_seat{seat}_seed{game['seed']}.jsonl.gz"
            rows.append(parse_log(log, {"opponent": game["opponent"], "seat": seat, "seed": int(game["seed"]), "margin": margin, "label": label}))
    rows = [row for row in rows if row["label"] != "tie"]
    overall_keys = (
        "observation_rebuilds", "animal_observations", "mean_observed_pool",
        "purchase_commits", "successful_placements", "lifecycle_additions",
        "lifecycle_removals", "persistent_ids_terminal", "escape_removals",
        "route_entries", "mean_route_entry_pool", "mean_live_surrogates",
    )
    overall = []
    for key in overall_keys:
        full = compare(rows, key); validation = validations(rows, key)
        overall.append({"metric": key, "full": full, **validation})
    bh(overall)
    for item in overall:
        validation = {"seed_halves": item["seed_halves"], "leave_one_opponent_out": item["leave_one_opponent_out"]}
        item["reproducible"] = replicated(item["full"], validation)

    daily_keys = ("mean_observed_pool", "purchase_commits", "successful_placements", "lifecycle_additions", "lifecycle_removals", "escape_removals", "mean_live_surrogates", "mean_route_entry_pool")
    daily = []
    for key in daily_keys:
        cumulative = key in {"purchase_commits", "successful_placements", "lifecycle_additions", "lifecycle_removals", "escape_removals"}
        for day in range(30):
            full = compare(rows, key, day, cumulative); validation = validations(rows, key, day, cumulative)
            daily.append({"metric": key, "day": day, "mode": "cumulative" if cumulative else "daily_mean", "full": full, **validation})
    bh(daily)
    for item in daily:
        validation = {"seed_halves": item["seed_halves"], "leave_one_opponent_out": item["leave_one_opponent_out"]}
        item["reproducible"] = replicated(item["full"], validation)
    earliest = {key: min((x["day"] for x in daily if x["metric"] == key and x["reproducible"]), default=None) for key in daily_keys}

    result = {
        "status": "measurement_only_complete",
        "cohort": {"games": len(rows), "strong": sum(r["label"] == "strong" for r in rows), "weak": sum(r["label"] == "weak" for r in rows), "ties_excluded": 320-len(rows), "seeds": "301-340", "opponents": sorted({r["opponent"] for r in rows}), "both_seats": True, "fixed_shops": True},
        "parity": {"games": len(parity_rows), "all_passed": all(r["parity"] for r in parity_rows), "all_lifecycle_conservation_passed": all(r["instrumented"]["lifecycle_validation"]["unresolved_entries_or_exits"] == 0 for r in parity_rows), "o42_sha256": "154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813"},
        "terminology": {"animal_observations": "repeated committed appends while rebuilding v['animals']; not formations", "successful_placements": "successful real PLACE unit actions", "lifecycle_additions": "new animals observed on farm tiles and assigned post-placement surrogate IDs", "mean_route_entry_pool": "mean len(v['animals']) at actual _build_route entry", "persistent_ids_terminal": "formed surrogate IDs not subsequently removed"},
        "method": {"strong_weak": "strong iff final own-minus-opponent money > 0; ties excluded", "residualization": "subtract opponent-by-seat cell mean before Welch unequal-variance t-test", "multiplicity": "Benjamini-Hochberg FDR separately for overall and declared day-by-stage tests", "replication_gate": "q_BH <= .05 plus identical residualized direction in both seed halves and all four leave-one-opponent-out checks", "causality": "all strong/weak contrasts are observational"},
        "overall_tests": overall,
        "day_tests": daily,
        "earliest_reproducible_day": earliest,
    }
    out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True); out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"cohort": result["cohort"], "parity": result["parity"], "earliest_reproducible_day": earliest, "reproducible_overall": [{"metric": x["metric"], "difference": x["full"]["raw_difference"], "residualized_difference": x["full"]["residualized_difference"], "q_bh": x["full"]["q_bh"]} for x in overall if x["reproducible"]]}, indent=2))


if __name__ == "__main__":
    main()
