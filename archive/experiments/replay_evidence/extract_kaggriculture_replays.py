#!/usr/bin/env python3
"""
Kaggriculture replay evidence extractor (schema-matched version).

Real replay schema (Kaggle episode JSON):
    d["info"]["TeamNames"] / d["info"]["Agents"]  -> player names, index 0/1
    d["rewards"]                                   -> final money per player
    d["statuses"]                                  -> DONE/ERROR/TIMEOUT per player
    d["steps"][t][p]["action"]["market"]            -> list of [op, item, qty] ops
        ops: SELL, BUY_SEED, HIRE
    d["steps"][t][p]["observation"]["day"] / "hour" -> in-game day/turn

USER_NAME below identifies which player index is "us" (grace) per episode,
so win/loss is relative to grace's seat, not player 0.

Usage:
    python3 extract_kaggriculture_replays.py /path/to/replays --out replay_evidence
"""
from __future__ import annotations
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median

USER_NAME = "graceyunliu"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def find_user_index(team_names: list[str]) -> int | None:
    for i, name in enumerate(team_names or []):
        if name and USER_NAME.lower() in str(name).lower():
            return i
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("replay_dir", type=Path)
    parser.add_argument("--out", type=Path, default=Path("replay_evidence"))
    args = parser.parse_args()

    replay_dir = args.replay_dir.expanduser().resolve()
    out = args.out.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    files = sorted(replay_dir.rglob("*.json"))
    if not files:
        raise SystemExit(f"No JSON files found under {replay_dir}")

    print(f"Found {len(files)} JSON replay files.")

    summary_rows = []
    all_tx = []
    errors = []

    for path in files:
        try:
            d = load_json(path)
            episode_id = d.get("info", {}).get("EpisodeId") or path.stem
            team_names = d.get("info", {}).get("TeamNames") or []
            seed = d.get("info", {}).get("seed")
            rewards = d.get("rewards") or []
            statuses = d.get("statuses") or []
            steps = d.get("steps") or []

            user_idx = find_user_index(team_names)
            opp_idx = 1 - user_idx if user_idx is not None else None
            opp_name = team_names[opp_idx] if opp_idx is not None and opp_idx < len(team_names) else None

            user_money = rewards[user_idx] if user_idx is not None and user_idx < len(rewards) else None
            opp_money = rewards[opp_idx] if opp_idx is not None and opp_idx < len(rewards) else None

            result = None
            if user_money is not None and opp_money is not None:
                if user_money > opp_money:
                    result = "win"
                elif user_money < opp_money:
                    result = "loss"
                else:
                    result = "draw"

            episode_tx = []
            for step in steps:
                for p_idx, agent_step in enumerate(step):
                    if not isinstance(agent_step, dict):
                        continue
                    act = agent_step.get("action") or {}
                    if not isinstance(act, dict):
                        continue
                    obs = agent_step.get("observation") or {}
                    day = obs.get("day")
                    hour = obs.get("hour")
                    for m in act.get("market", []) or []:
                        if not m:
                            continue
                        op = m[0]
                        if op != "SELL":
                            continue
                        item = m[1] if len(m) > 1 else None
                        qty = m[2] if len(m) > 2 else None
                        seller_is_user = p_idx == user_idx
                        tx = {
                            "episode": episode_id,
                            "result": result,
                            "seed": seed,
                            "opponent_policy": opp_name,
                            "player_index": p_idx,
                            "seller": "user" if seller_is_user else "opponent",
                            "day": day,
                            "hour": hour,
                            "item": item,
                            "quantity": qty,
                            "source_file": str(path),
                        }
                        episode_tx.append(tx)
                        all_tx.append(tx)

            user_sells = Counter()
            opp_sells = Counter()
            for tx in episode_tx:
                bucket = user_sells if tx["seller"] == "user" else opp_sells
                if tx["quantity"] is not None:
                    bucket[tx["item"]] += tx["quantity"]

            summary_rows.append({
                "episode": episode_id,
                "team_names": team_names,
                "user_index": user_idx,
                "opponent": opp_name,
                "seed": seed,
                "user_money": user_money,
                "opponent_money": opp_money,
                "result": result,
                "statuses": statuses,
                "sell_events": len(episode_tx),
                "user_sell_units_by_item": dict(user_sells),
                "opponent_sell_units_by_item": dict(opp_sells),
                "source_file": str(path),
            })
        except Exception as exc:
            errors.append({"file": str(path), "error": repr(exc)})

    with (out / "replay_summary.jsonl").open("w", encoding="utf-8") as f:
        for row in summary_rows:
            f.write(json.dumps(row, separators=(",", ":")) + "\n")

    with (out / "sell_transactions.jsonl").open("w", encoding="utf-8") as f:
        for tx in all_tx:
            f.write(json.dumps(tx, separators=(",", ":")) + "\n")

    # crop/item outcome summary, split by seller (user vs opponent) and result
    outcome = defaultdict(list)
    timing = defaultdict(list)
    for tx in all_tx:
        if tx["quantity"] is None or tx["result"] is None:
            continue
        key = (tx["item"], tx["seller"], tx["result"])
        outcome[key].append(tx["quantity"])
        if tx["day"] is not None:
            timing[key].append(tx["day"])

    item_outcome_summary = {}
    for (item, seller, result), quantities in sorted(outcome.items()):
        item_outcome_summary[f"{item}:{seller}:{result}"] = {
            "events": len(quantities),
            "total_units": sum(quantities),
            "mean_units_per_event": mean(quantities),
            "median_units_per_event": median(quantities),
            "max_units_per_event": max(quantities),
        }
    with (out / "item_outcome_summary.json").open("w", encoding="utf-8") as f:
        json.dump(item_outcome_summary, f, indent=2)

    timing_summary = {}
    for (item, seller, result), days in sorted(timing.items()):
        timing_summary[f"{item}:{seller}:{result}"] = {
            "events": len(days),
            "first_day": min(days),
            "median_day": median(days),
            "last_day": max(days),
        }
    with (out / "timing_summary.json").open("w", encoding="utf-8") as f:
        json.dump(timing_summary, f, indent=2)

    with (out / "extraction_errors.json").open("w", encoding="utf-8") as f:
        json.dump(errors, f, indent=2)

    print()
    print("DONE")
    print(f"Replay files: {len(files)}")
    print(f"Episodes summarized: {len(summary_rows)}")
    print(f"SELL transactions extracted: {len(all_tx)}")
    print(f"Errors: {len(errors)}")
    print()
    print("Generated in", out)
    print("  replay_summary.jsonl")
    print("  sell_transactions.jsonl")
    print("  item_outcome_summary.json")
    print("  timing_summary.json")
    print("  extraction_errors.json")


if __name__ == "__main__":
    main()
