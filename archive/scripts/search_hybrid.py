#!/usr/bin/env python3
"""Knob search over H11-style hybrids (tape prefix + guard + K policy), scored against a
set of opponents at once. Prints per-opponent margins and a cluster average.

  python3 search_hybrid.py --grid '{"max_animals":[14,18],"wheat_tiles":[0,8]}' \
      --opps Opponents/tape_yuan800_104892947.py Opponents/tape_strawhats_105080848.py \
      --seeds 1-10
"""
import argparse
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mini_engine as me  # noqa: E402
import make_hybrid as mh  # noqa: E402

ROOT = Path(__file__).resolve().parent
GEN = ROOT / "candidates" / "gen_h"
BASE_KNOBS = {"opening": "frontier", "early_hire_days": 5, "feed_spare_poor": 0, "open_melons": 8}
REPLAY = ROOT / "Replays/Auto/leaderboard-Yuan800/episode-104892947-replay.json"


def seeds_of(s):
    out = []
    for part in s.split(","):
        if "-" in part:
            a, b = part.split("-"); out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def tag(k):
    return "_".join(f"{a[:6]}{str(b).replace('.', 'p')}" for a, b in sorted(k.items()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grid")
    ap.add_argument("--list")
    ap.add_argument("--opps", nargs="+", required=True)
    ap.add_argument("--seeds", default="1-10")
    ap.add_argument("--switch-day", type=int, default=10)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.grid:
        g = json.loads(a.grid); keys = list(g)
        variants = [dict(zip(keys, v)) for v in itertools.product(*[g[k] for k in keys])]
    else:
        variants = json.load(open(a.list))
    GEN.mkdir(parents=True, exist_ok=True)
    seeds = seeds_of(a.seeds)
    rows = []
    for kn in variants:
        knobs = dict(BASE_KNOBS); knobs.update(kn)
        path = GEN / f"H_{tag(kn) or 'base'}.py"
        mh.build(str(REPLAY), 1, a.switch_day, knobs, True, str(path), money_tol=800)
        res = {}
        for opp in a.opps:
            r = me.evaluate(str(path), opp, seeds, both_seats=True, jobs=a.jobs)
            res[Path(opp).stem] = (r["mean_margin_per_game"], r["wins"], r["losses"], r["mean_a"])
        avg = sum(v[0] for v in res.values()) / len(res)
        rows.append((avg, kn, res))
        print(f"{str(kn):70s} avg {avg:+8.0f} | " + " ".join(f"{k[5:13]}:{v[0]:+7.0f}({v[1]}-{v[2]})" for k, v in res.items()), flush=True)
    rows.sort(key=lambda r: -r[0])
    print("\n=== ranked by cluster average ===")
    for avg, kn, res in rows:
        print(f"{avg:+8.0f}  {kn}")
    if a.out:
        json.dump([{"avg": r[0], "knobs": r[1], "res": r[2]} for r in rows], open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
