#!/usr/bin/env python3
"""
Prune old leaderboard-scouting replay files to bound disk usage on always-on
deployment machines (e.g. the Air).

Why this is safe to delete: an opponent's opening fingerprint (turn-1/turn-2
market orders) is computed once, early, by evolve/refresh_frontier.py, and
what actually matters going forward is its clustering output
(Opponents/tapes.json, Opponents/tape_*.py) -- not the raw scouted replay
JSON itself. Once a batch of replays has been clustered, there is no
ongoing need to keep the raw files around.

Safe by construction re: re-download: sync_replays.py's dedup
(already_downloaded()) scans the filesystem for episode ids under Replays/,
it does not consult a database. So pruning a file just means that episode
*could* be re-downloaded later if it resurfaces in a "new" window (e.g. the
same team is scouted again before 10 days pass and the episode is still
among their newest N) -- that's harmless extra bandwidth, never incorrect
or duplicate data.

Only touches Replays/Auto/leaderboard-*/ (opponent-scouting replays).
Never touches Replays/Auto/mine/ (this project's own submission history)
-- that's a separate retention concern, out of scope here.

Usage:
  python3 evolve/prune_replays.py                  # prune files older than 10 days
  python3 evolve/prune_replays.py --max-age-days 14
  python3 evolve/prune_replays.py --dry-run         # report only, delete nothing
"""

import argparse
import time
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
TARGET_DIR = PROJECT_DIR / "Replays" / "Auto"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-age-days", type=float, default=10,
                     help="delete leaderboard-scouting replay files older than this many days (default 10)")
    ap.add_argument("--dry-run", action="store_true", help="report what would be deleted, delete nothing")
    args = ap.parse_args()

    if not TARGET_DIR.exists():
        print(f"{TARGET_DIR} does not exist yet -- nothing to prune.")
        return

    cutoff = time.time() - args.max_age_days * 86400
    files = sorted(TARGET_DIR.glob("leaderboard-*/*.json"))
    to_delete = [f for f in files if f.stat().st_mtime < cutoff]
    total_bytes = sum(f.stat().st_size for f in to_delete)

    print(f"{len(files)} replay file(s) under Replays/Auto/leaderboard-*/, "
          f"{len(to_delete)} older than {args.max_age_days} day(s) "
          f"({total_bytes / 1e6:.1f} MB)" + (" [dry-run]" if args.dry_run else ""))

    for f in to_delete:
        rel = f.relative_to(PROJECT_DIR)
        if args.dry_run:
            print(f"  would delete {rel}")
        else:
            f.unlink()

    if not args.dry_run and to_delete:
        print(f"Deleted {len(to_delete)} file(s), freed {total_bytes / 1e6:.1f} MB.")
        for d in sorted(TARGET_DIR.glob("leaderboard-*")):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
                print(f"  removed now-empty directory {d.relative_to(PROJECT_DIR)}")


if __name__ == "__main__":
    main()
