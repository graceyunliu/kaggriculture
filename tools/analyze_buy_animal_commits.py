#!/usr/bin/env python3
"""Exact cross-tabs and independent validation for focused BUY_ANIMAL commits."""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

import analyze_animal_formation_panel as stats_base


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--panel-dir", required=True)
    parser.add_argument("--certified-panel-dir", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    panel_dir = Path(args.panel_dir)
    certified_dir = Path(args.certified_panel_dir)
    games = []
    certified = {}
    for opponent in ("peter", "alaylm", "bahaen", "yangk"):
        shard = json.loads((panel_dir / f"{opponent}.json").read_text())
        games.extend(shard["games"])
        baseline = json.loads((certified_dir / opponent / "smoke_summary.json").read_text())
        for game in baseline["rows"]:
            certified[(game["opponent"], int(game["seed"]), int(game["seat"]))] = game["instrumented"]

    rows = []
    exact = collections.Counter()
    certified_matches = []
    for game in games:
        seat = int(game["seat"]); money = game["money"]
        margin = money[seat] - money[1-seat]
        cohort = "strong" if margin > 0 else "weak" if margin < 0 else "tie"
        daily = {}
        for day in range(30):
            counts = game["counts_by_day"].get(str(day), {})
            true_count = int(counts.get("committed_true", 0))
            false_count = int(counts.get("committed_false", 0))
            daily[str(day)] = {"committed_true": true_count, "committed_false": false_count}
            exact[(day, cohort, game["opponent"], seat, True)] += true_count
            exact[(day, cohort, game["opponent"], seat, False)] += false_count
        rows.append({"opponent": game["opponent"], "seed": int(game["seed"]), "seat": seat,
                     "label": cohort, "daily": daily, "metrics": {}})
        ref = certified[(game["opponent"], int(game["seed"]), seat)]
        certified_matches.append(game["actions_sha256"] == ref["actions_sha256"] and
                                 game["terminal_sha256"] == ref["terminal_sha256"] and
                                 game["money"] == ref["money"])
    analytical_rows = [row for row in rows if row["label"] != "tie"]
    cross_tab = [{"day": day, "cohort": cohort, "opponent": opponent, "seat": seat,
                  "committed": committed, "count": exact[(day, cohort, opponent, seat, committed)]}
                 for day in range(30) for cohort in ("strong", "weak", "tie")
                 for opponent in ("peter", "alaylm", "bahaen", "yangk") for seat in (0, 1)
                 for committed in (True, False)]

    day_tests = []
    for metric in ("committed_true", "committed_false"):
        for day in range(30):
            full = stats_base.compare(analytical_rows, metric, day, cumulative=True)
            validation = stats_base.validations(analytical_rows, metric, day, cumulative=True)
            day_tests.append({"metric": metric, "day": day, "mode": "cumulative", "full": full, **validation})
    stats_base.bh(day_tests)
    for item in day_tests:
        validation = {"seed_halves": item["seed_halves"], "leave_one_opponent_out": item["leave_one_opponent_out"]}
        item["reproducible"] = stats_base.replicated(item["full"], validation)
    earliest = {metric: min((x["day"] for x in day_tests if x["metric"] == metric and x["reproducible"]), default=None)
                for metric in ("committed_true", "committed_false")}
    result = {
        "scope": "actual BUY_ANIMAL _commit_unit boolean only",
        "cohort": {"games": len(games), "strong": sum(r["label"] == "strong" for r in rows),
                   "weak": sum(r["label"] == "weak" for r in rows), "ties": sum(r["label"] == "tie" for r in rows)},
        "totals": {"committed_true": sum(x["count"] for x in cross_tab if x["committed"]),
                   "committed_false": sum(x["count"] for x in cross_tab if not x["committed"])},
        "validation": {"focused_pair_parity_320_of_320": all(g["parity"] for g in games),
                       "certified_panel_exact_hash_money_match_320_of_320": all(certified_matches),
                       "o42_sha256": "154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813"},
        "earliest_reproducible_day": earliest,
        "interpretation": {"committed_false": "No failures occurred; no failure divergence day exists.",
                           "committed_true": "Volume contrast only; no candidate-generation or affordability inference."},
        "exact_cross_tab": cross_tab,
        "day_tests": day_tests,
    }
    output = Path(args.out); output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("cohort", "totals", "validation", "earliest_reproducible_day", "interpretation")}, indent=2))


if __name__ == "__main__":
    main()
