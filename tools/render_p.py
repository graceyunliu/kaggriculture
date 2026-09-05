#!/usr/bin/env python3
"""Re-render candidates/P.py from the current planner block sources, keeping P.py's KNOBS/constants.

  python3 tools/render_p.py [--base candidates/P.py] [--out candidates/P.py]
"""
import argparse, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evolve"))
import blocks as _blocks  # noqa: E402

BLOCK_FILES = {
    "hiring": "evolve/blocks/planner_hiring.py",
    "animal_routing": "evolve/blocks/planner_animal_routing.py",
    "sweep": "evolve/blocks/planner_sweep.py",
    "dispatch": "evolve/blocks/planner_dispatch.py",
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="candidates/P.py")
    ap.add_argument("--out", default="candidates/P.py")
    ap.add_argument("--only", default=None, help="comma list of block names")
    a = ap.parse_args()
    names = a.only.split(",") if a.only else list(BLOCK_FILES)
    text = (ROOT / a.base).read_text()
    text = _blocks.substitute(text, {n: (ROOT / BLOCK_FILES[n]).read_text() for n in names})
    (ROOT / a.out).write_text(text)
    print(f"rendered {a.out} from blocks {names}")

if __name__ == "__main__":
    main()
