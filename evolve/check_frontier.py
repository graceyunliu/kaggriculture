#!/usr/bin/env python3
"""Flag held-out candidates that decisively beat the configured frontier."""
from __future__ import annotations

import argparse
import sqlite3
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_DB = HERE / "evolve.db"
DEFAULT_FLAG = HERE / "PROMOTION_PENDING.txt"
DEFAULT_ALERT_STATE = HERE / "logs" / "promotion_alerted.txt"


def decisive_winner(db_path: Path, frontier: str):
    """Return the strongest positive, significant held-out result for frontier."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        return conn.execute(
            """
            SELECT c.key, c.path, c.held_margin, c.held_t
              FROM candidates c
              JOIN runs r ON r.run_id = c.run_id
             WHERE c.status = 'held_pass'
               AND c.stage >= 3
               AND c.held_margin > 0
               AND c.held_t >= 2.0
               AND r.frontier = ?
             ORDER BY c.held_margin DESC, c.held_t DESC
             LIMIT 1
            """,
            (frontier,),
        ).fetchone()
    finally:
        conn.close()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--frontier", required=True)
    ap.add_argument("--flag", type=Path, default=DEFAULT_FLAG)
    ap.add_argument("--alert-state", type=Path, default=DEFAULT_ALERT_STATE)
    ap.add_argument("--notify-script", type=Path, default=HERE / "notify.sh")
    ap.add_argument("--no-notify", action="store_true")
    args = ap.parse_args()

    if not args.db.exists():
        print(f"frontier check skipped: database not found: {args.db}")
        return 0

    try:
        row = decisive_winner(args.db, args.frontier)
    except sqlite3.Error as exc:
        print(f"frontier check failed: {exc}")
        return 1
    if row is None:
        print(f"frontier check: no decisive held-out winner against {args.frontier}")
        return 0

    candidate = row["path"] or row["key"]
    message = (
        f"candidate {candidate} beats current frontier {args.frontier} by "
        f"${row['held_margin']:,.0f}/game (t={row['held_t']:.2f}) — review for promotion"
    )
    flag_text = message + "\n"
    already_alerted = args.alert_state.exists() and args.alert_state.read_text() == flag_text
    args.flag.parent.mkdir(parents=True, exist_ok=True)
    args.flag.write_text(flag_text)
    print(message)

    if not already_alerted and not args.no_notify:
        result = subprocess.run(
            ["bash", str(args.notify_script), "text", "Kaggriculture: promotion pending", message],
            cwd=ROOT,
            check=False,
        )
        if result.returncode:
            print(f"promotion alert failed with rc={result.returncode}")
            return result.returncode
        args.alert_state.parent.mkdir(parents=True, exist_ok=True)
        args.alert_state.write_text(flag_text)
    elif already_alerted:
        print("promotion alert already sent; flag remains pending")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
