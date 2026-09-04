#!/usr/bin/env python3
"""Factorial / list search over KNOBS variants of candidates/K.py.

  python3 search.py --grid '{"melon_floor":[150,0],"harvest_min":[2,1]}' --vs candidates/V3_12.py
  python3 search.py --list variants.json --vs candidates/V3_11.py --seeds 1-10

Cascade: every variant plays --screen seeds (default 1-3) both seats; variants whose
margin/game is below --screen-floor are dropped; survivors play the full --seeds set.
Results are cached by mini_engine (file sha), so re-runs are free.
"""
import argparse
import itertools
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mini_engine as me  # noqa: E402

ROOT = Path(__file__).resolve().parent
GEN = ROOT / "candidates" / "gen"
K_SRC = ROOT / "candidates" / "K.py"


def parse_seeds(s):
    out = []
    for part in s.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def tag_of(knobs):
    return "_".join(f"{k[:5]}{str(v).replace('.', 'p')}" for k, v in sorted(knobs.items()))


def make_variant(knobs, src=K_SRC):
    GEN.mkdir(parents=True, exist_ok=True)
    text = src.read_text()
    m = re.search(r"^KNOBS = \{.*?\}\n", text, re.S | re.M)
    assert m, "KNOBS block not found"
    base = eval(m.group(0)[len("KNOBS = "):])
    base.update(knobs)
    new = "KNOBS = " + json.dumps(base) + "\n"
    out = GEN / f"K_{tag_of(knobs)}.py"
    out.write_text(text[:m.start()] + new + text[m.end():])
    return out


def run(variants, vs, screen, seeds, floor, jobs, engine):
    rows = []
    for knobs in variants:
        path = make_variant(knobs)
        r = me.evaluate(str(path), vs, screen, engine=engine, both_seats=True, jobs=jobs)
        row = {"knobs": knobs, "path": str(path.name), "screen_margin": r["mean_margin_per_game"],
               "screen_wins": f"{r['wins']}-{r['losses']}", "full_margin": None, "t": None, "wins": None,
               "mean_a": r["mean_a"], "errors": r["agent_errors"][0]}
        if r["mean_margin_per_game"] >= floor and set(seeds) != set(screen):
            r2 = me.evaluate(str(path), vs, seeds, engine=engine, both_seats=True, jobs=jobs)
            row.update({"full_margin": r2["mean_margin_per_game"], "t": r2["t"], "wins": f"{r2['wins']}-{r2['losses']}",
                        "mean_a": r2["mean_a"], "errors": r2["agent_errors"][0]})
        rows.append(row)
        fm = row["full_margin"]
        full = "-" if fm is None else "%+8.0f t=%.2f %s" % (fm, row["t"], row["wins"])
        print("%-60s screen %+8.0f (%s)  full %s  own $%s  err %s" % (
            row["path"], row["screen_margin"], row["screen_wins"], full, f"{row['mean_a']:,.0f}", row["errors"]), flush=True)
    return rows


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--grid", help="JSON dict knob -> list of values (full factorial)")
    p.add_argument("--list", help="JSON file: list of knob dicts")
    p.add_argument("--vs", required=True)
    p.add_argument("--screen", default="1-3")
    p.add_argument("--seeds", default="1-10")
    p.add_argument("--screen-floor", type=float, default=-5000)
    p.add_argument("--jobs", type=int, default=None)
    p.add_argument("--engine", default="master")
    p.add_argument("--out", default=None)
    a = p.parse_args()
    if a.grid:
        g = json.loads(a.grid)
        keys = list(g)
        variants = [dict(zip(keys, vals)) for vals in itertools.product(*[g[k] for k in keys])]
    else:
        variants = json.load(open(a.list))
    rows = run(variants, a.vs, parse_seeds(a.screen), parse_seeds(a.seeds), a.screen_floor, a.jobs, a.engine)
    rows.sort(key=lambda r: (r["full_margin"] if r["full_margin"] is not None else -1e9, r["screen_margin"]), reverse=True)
    print("\n=== ranked ===")
    for r in rows:
        fm = r["full_margin"]
        print("%9s  %+8.0f  %s" % ("-" if fm is None else "%+8.0f" % fm, r["screen_margin"], r["knobs"]))
    if a.out:
        json.dump(rows, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
