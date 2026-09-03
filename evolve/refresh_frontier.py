#!/usr/bin/env python3
"""Turn newly scouted ladder replays into opponent tapes for the evolution loop.

    python3 evolve/refresh_frontier.py            # scan, build any new cluster tapes, update registry
    python3 evolve/refresh_frontier.py --dry-run

Reads Replays/Auto/leaderboard-*/episode-*-replay.json (written by sync_replays.py), fingerprints
each scouted team's opening (turn-1/turn-2 market orders, same rule as pull_ladder.py), clusters the
most recent games, and for every cluster with at least --min-share of recent games that has no tape
yet, builds Opponents/tape_<team>_<episode>.py from that cluster's best-scoring game.

Also writes Opponents/frontier.txt = the tape of the currently dominant cluster (highest mean money
among clusters with >= --min-share). run_nightly.sh uses it as the loop's --clone opponent, so the
Air's yardstick follows the ladder with no manual flag changes.

Registry: Opponents/tapes.json  { tape_file: {fingerprint, team, episode, seat, money, built} }.
Nothing here touches Kaggle; it only reads replays already on disk.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from make_tape_agent import build  # noqa: E402

REPLAYS = ROOT / "Replays" / "Auto"
OPP = ROOT / "Opponents"
REGISTRY = OPP / "tapes.json"
FRONTIER = OPP / "frontier.txt"


def fingerprint(d, seat):
    """Opening fingerprint: turn-1 and turn-2 market orders (item + qty), as in pull_ladder.py."""
    def fmt(m):
        return " ".join(f"{x[0][:3]}{'' if len(x) < 3 else x[1][:2] + str(x[2])}" for x in m)
    steps = d["steps"]
    m1 = steps[1][seat].get("action", {}).get("market", []) if len(steps) > 1 else []
    m2 = steps[2][seat].get("action", {}).get("market", []) if len(steps) > 2 else []
    return fmt(m1) + " | " + fmt(m2)


def slug(name):
    return re.sub(r"[^A-Za-z0-9]+", "", name)[:20] or "team"


def load_registry():
    if REGISTRY.exists():
        return json.loads(REGISTRY.read_text())
    reg = {}
    # bootstrap from existing tape headers if their replays are on disk
    for t in OPP.glob("tape_*.py"):
        head = t.read_text(errors="ignore")[:600]
        m = re.search(r"source episode (\d+)\s+seat (\d)\s+player \"(.*?)\"\s+recorded final money ([\d.]+)", head)
        if not m:
            continue
        ep, seat, player, money = m.group(1), int(m.group(2)), m.group(3), float(m.group(4))
        paths = glob.glob(str(REPLAYS / "*" / f"episode-{ep}-replay.json")) + glob.glob(str(REPLAYS / "**" / f"{ep}.json"), recursive=True)
        fp = None
        if paths:
            try:
                fp = fingerprint(json.load(open(paths[0])), seat)
            except Exception:  # noqa: BLE001
                fp = None
        reg[t.name] = {"fingerprint": fp, "team": player, "episode": int(ep), "seat": seat, "money": money, "built": "bootstrap"}
    return reg


def scouted_games(recent_per_team):
    """Yield (team, path, seat, money, episode_id) for the newest replays of each scouted team."""
    for d in sorted(REPLAYS.glob("leaderboard-*")):
        team_dir = d.name[len("leaderboard-"):]
        files = sorted(d.glob("episode-*-replay.json"), key=lambda p: int(re.search(r"episode-(\d+)", p.name).group(1)), reverse=True)
        for p in files[:recent_per_team]:
            try:
                r = json.load(open(p))
            except Exception:  # noqa: BLE001
                continue
            names = r.get("info", {}).get("TeamNames", ["?", "?"])
            norm = [re.sub(r"[^A-Za-z0-9]+", "_", n) for n in names]
            seat = norm.index(team_dir) if team_dir in norm else None
            if seat is None:
                # folder names may be truncated/normalised differently; fall back to best prefix match
                cands = [i for i, n in enumerate(norm) if n.startswith(team_dir[:8]) or team_dir.startswith(n[:8])]
                seat = cands[0] if cands else None
            if seat is None:
                continue
            money = r.get("rewards", [None, None])[seat]
            if money is None:
                continue
            yield names[seat], p, seat, float(money), int(r.get("info", {}).get("EpisodeId") or re.search(r"episode-(\d+)", p.name).group(1)), r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--recent-per-team", type=int, default=6)
    ap.add_argument("--min-share", type=float, default=0.10)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    reg = load_registry()
    known = {v["fingerprint"] for v in reg.values() if v.get("fingerprint")}

    clusters = defaultdict(list)   # fingerprint -> [(money, team, path, seat, ep)]
    n = 0
    for team, path, seat, money, ep, r in scouted_games(args.recent_per_team):
        try:
            fp = fingerprint(r, seat)
        except Exception:  # noqa: BLE001
            continue
        clusters[fp].append((money, team, path, seat, ep))
        n += 1
    if n == 0:
        print("no scouted replays found under Replays/Auto/leaderboard-*/ — run sync_replays.py leaderboard first")
        return 1

    rows = sorted(clusters.items(), key=lambda kv: -len(kv[1]))
    print(f"{n} recent scouted games, {len(rows)} opening clusters (min share {args.min_share:.0%}):")
    new_tapes = []
    dominant = None
    for fp, games in rows:
        share = len(games) / n
        mean = sum(g[0] for g in games) / len(games)
        teams = sorted({g[1] for g in games})
        have = [k for k, v in reg.items() if v.get("fingerprint") == fp]
        flag = "known" if fp in known else ("NEW" if share >= args.min_share else "minor")
        print(f"  {share:5.0%}  n={len(games):2d}  mean ${mean:>9,.0f}  {flag:5s}  {fp[:60]}  teams={teams[:4]}")
        if share >= args.min_share and (dominant is None or mean > dominant[0]):
            dominant = (mean, fp, have)
        if flag == "NEW":
            best = max(games, key=lambda g: g[0])
            money, team, path, seat, ep = best
            out = OPP / f"tape_{slug(team).lower()}_{ep}.py"
            if not args.dry_run:
                k = build(str(path), seat, str(out))
                reg[out.name] = {"fingerprint": fp, "team": team, "episode": ep, "seat": seat, "money": money, "built": "refresh_frontier", "actions": k}
                known.add(fp)
            new_tapes.append(out.name)
            if dominant and dominant[1] == fp:
                dominant = (mean, fp, [out.name])

    if not args.dry_run:
        REGISTRY.write_text(json.dumps(reg, indent=1, sort_keys=True))
        if dominant and dominant[2]:
            FRONTIER.write_text(f"Opponents/{dominant[2][0]}\n")
            print(f"frontier -> Opponents/{dominant[2][0]}  (cluster mean ${dominant[0]:,.0f})")
    if new_tapes:
        print("NEW TAPES: " + ", ".join(new_tapes))
        print("publish them so the Air picks them up tonight: python3 evolve/gh_push.py Opponents/tapes.json Opponents/frontier.txt "
              + " ".join(f"Opponents/{t}" for t in new_tapes))
    else:
        print("no new clusters; Opponents/ is current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
