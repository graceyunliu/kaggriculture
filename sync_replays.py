#!/usr/bin/env python3
"""
Kaggriculture replay auto-downloader.

Pulls new episode replays straight from the Kaggle API (no manual
download-from-the-episode-page needed) and drops them into Replays/Auto/,
then re-ingests them into the harness SQLite DB. Safe to re-run any time —
already-downloaded episodes are skipped, and harness.py ingest is already
a no-op on episode ids it's seen before.

ONE-TIME SETUP
  1. pip install kaggle          (needs Python 3.11+ -- this is the new
                                   kagglesdk-based CLI, not the old
                                   username/key kaggle.json one)
  2. Get a token: kaggle.com -> Settings -> API -> "Create New Token"
  3. Save it:
       mkdir -p ~/.kaggle
       echo '<YOUR_KGAT_TOKEN>' > ~/.kaggle/access_token
       chmod 600 ~/.kaggle/access_token
  4. Sanity check:  kaggle competitions list -s kaggriculture

USAGE
  python3 sync_replays.py mine                  # all your submissions' new episodes
  python3 sync_replays.py mine --latest          # only your most recent submission
  python3 sync_replays.py scout <team_id>        # one opponent's best-scoring submission
  python3 sync_replays.py leaderboard [N]        # top N leaderboard teams (default 5)

  --max-episodes N   available on every subcommand. Caps how many *new*
                      episodes are pulled per submission, keeping the N most
                      recently played ones (by createTime) and skipping the
                      rest. The Kaggle episodes API doesn't expose a
                      per-episode score (only submission-level publicScore),
                      so this is the closest thing to "just the interesting
                      ones" without downloading everything first.

Every mode ends by calling `harness.py ingest` on whatever was newly
downloaded, so kaggriculture.db stays current automatically.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

COMPETITION = "kaggriculture"
PROJECT_DIR = Path(__file__).resolve().parent
REPLAYS_DIR = PROJECT_DIR / "Replays"
AUTO_DIR = REPLAYS_DIR / "Auto"
HARNESS = PROJECT_DIR / "harness.py"


def kaggle_json(*args):
    """Run a kaggle CLI command and parse its --format json output."""
    result = subprocess.run(
        ["kaggle", *args, "--format", "json"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        sys.exit(f"kaggle {' '.join(args)} failed:\n{result.stderr}")
    # Some subcommands print extra lines before/after the JSON array
    # (e.g. leaderboard -s prints "Next Page Token = ..." first, episodes
    # prints a usage hint after) -- find the array and parse just that.
    out = result.stdout.strip()
    start = out.find("[")
    if start < 0:
        sys.exit(f"kaggle {' '.join(args)}: no JSON array in output:\n{out}")
    obj, _ = json.JSONDecoder().raw_decode(out[start:])
    return obj


def select_new(episodes, seen, cap=None):
    """New (not-yet-downloaded) episode ids, most-recently-played first,
    capped at `cap` if given."""
    episodes = sorted(episodes, key=lambda e: e.get("createTime", ""), reverse=True)
    new_ids = [e["id"] for e in episodes if e["id"] not in seen]
    if cap is not None:
        new_ids = new_ids[:cap]
    return new_ids


def already_downloaded():
    """Episode ids that already exist somewhere under Replays/ (any subfolder)."""
    ids = set()
    if REPLAYS_DIR.exists():
        for p in REPLAYS_DIR.rglob("*.json"):
            digits = "".join(c for c in p.stem if c.isdigit())
            # filenames are inconsistent (episode-<id>-replay, <id>-0, <id>_0804, ...)
            # take the first long digit run as the episode id
            import re
            m = re.search(r"\d{6,}", p.stem)
            if m:
                ids.add(int(m.group()))
    return ids


def download_episode(episode_id, dest_dir):
    dest_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["kaggle", "competitions", "replay", str(episode_id), "-p", str(dest_dir), "-q"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"  ! failed to download episode {episode_id}: {result.stderr.strip()}")
        return None
    return dest_dir / f"episode-{episode_id}-replay.json"


def ingest(paths):
    paths = [str(p) for p in paths if p]
    if not paths:
        return
    print(f"\nIngesting {len(paths)} new replay(s) into harness DB...")
    subprocess.run([sys.executable, str(HARNESS), "ingest", *paths], cwd=PROJECT_DIR)


def my_submissions(latest_only=False):
    subs = kaggle_json("competitions", "submissions", COMPETITION)
    subs.sort(key=lambda s: s["date"], reverse=True)
    return subs[:1] if latest_only else subs


def cmd_mine(args):
    seen = already_downloaded()
    downloaded = []
    for sub in my_submissions(latest_only=args.latest):
        sub_id = sub["ref"]
        print(f"Submission {sub_id} ({sub['fileName']}, score {sub['publicScore']})")
        episodes = kaggle_json("competitions", "episodes", str(sub_id))
        new = select_new(episodes, seen, args.max_episodes)
        print(f"  {len(episodes)} episodes total, {len(new)} new"
              + (f" (capped at {args.max_episodes})" if args.max_episodes else ""))
        for ep_id in new:
            path = download_episode(ep_id, AUTO_DIR / "mine")
            if path:
                downloaded.append(path)
                seen.add(ep_id)
    ingest(downloaded)
    print(f"\nDone. {len(downloaded)} new replay(s) downloaded to {AUTO_DIR / 'mine'}")


def cmd_scout(args):
    seen = already_downloaded()
    team_subs = kaggle_json("competitions", "team-submissions", str(args.team_id))
    if not team_subs:
        sys.exit(f"No submissions found for team {args.team_id}")
    best = max(team_subs, key=lambda s: float(s.get("publicScore") or 0))
    print(f"Best submission for team {args.team_id}: {best['id']} (score {best.get('publicScore')})")
    episodes = kaggle_json("competitions", "episodes", str(best["id"]))
    new = select_new(episodes, seen, args.max_episodes)
    print(f"  {len(episodes)} episodes total, {len(new)} new"
          + (f" (capped at {args.max_episodes})" if args.max_episodes else ""))
    downloaded = []
    for ep_id in new:
        path = download_episode(ep_id, AUTO_DIR / f"scout-{args.team_id}")
        if path:
            downloaded.append(path)
    ingest(downloaded)
    print(f"\nDone. {len(downloaded)} new replay(s) downloaded.")


def cmd_leaderboard(args):
    board = kaggle_json("competitions", "leaderboard", COMPETITION, "-s")
    top = board[:args.n]
    seen = already_downloaded()
    downloaded = []
    for row in top:
        team_id, team_name = row["teamId"], row["teamName"]
        print(f"\n{team_name} (team {team_id}, score {row['score']})")
        team_subs = kaggle_json("competitions", "team-submissions", str(team_id))
        if not team_subs:
            print("  no public submissions")
            continue
        best = max(team_subs, key=lambda s: float(s.get("publicScore") or 0))
        episodes = kaggle_json("competitions", "episodes", str(best["id"]))
        new = select_new(episodes, seen, args.max_episodes)
        print(f"  submission {best['id']}: {len(episodes)} episodes, {len(new)} new"
              + (f" (capped at {args.max_episodes})" if args.max_episodes else ""))
        for ep_id in new:
            path = download_episode(ep_id, AUTO_DIR / f"leaderboard-{team_name.replace(' ', '_')}")
            if path:
                downloaded.append(path)
                seen.add(ep_id)
    ingest(downloaded)
    print(f"\nDone. {len(downloaded)} new replay(s) downloaded.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    cap_parent = argparse.ArgumentParser(add_help=False)
    cap_parent.add_argument(
        "--max-episodes", type=int, default=None, metavar="N",
        help="cap new episodes pulled per submission to the N most recent (by createTime)",
    )

    p_mine = sub.add_parser("mine", parents=[cap_parent], help="download new episodes for your own submissions")
    p_mine.add_argument("--latest", action="store_true", help="only your most recent submission")
    p_mine.set_defaults(func=cmd_mine)

    p_scout = sub.add_parser("scout", parents=[cap_parent], help="download new episodes for one opponent team")
    p_scout.add_argument("team_id", type=int)
    p_scout.set_defaults(func=cmd_scout)

    p_lb = sub.add_parser("leaderboard", parents=[cap_parent], help="download new episodes for top-N leaderboard teams")
    p_lb.add_argument("n", type=int, nargs="?", default=5)
    p_lb.set_defaults(func=cmd_leaderboard)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
