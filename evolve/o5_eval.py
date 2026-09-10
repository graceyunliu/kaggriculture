"""O5 end-game candidate: paired both-seat head-to-head vs O4 (and optional other opponents).

Usage:
  python3 evolve/o5_eval.py --cand candidates/O5_ENDGAME.py --opp candidates/O4_PRODUCTIVE_SERVICE.py --seeds 1-10
  python3 evolve/o5_eval.py --variant same_turn_sell=2 ...   # rewrite EG knobs into a temp copy first
"""
import argparse
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "evolve"))
from cascade import evaluate, close_pool  # noqa: E402


def parse_seeds(s):
    out = []
    for part in s.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def make_variant(src, kv, tag):
    text = Path(src).read_text()
    for k, v in kv.items():
        text, n = re.subn(rf'"{k}": *[^,}}]+', f'"{k}": {v}', text, count=1)
        assert n == 1, k
    out = ROOT / "candidates" / f"_tmp_{Path(src).stem}_{tag}.py"
    out.write_text(text)
    return str(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cand", default="candidates/O5_ENDGAME.py")
    ap.add_argument("--opp", action="append", default=[])
    ap.add_argument("--seeds", default="1-10")
    ap.add_argument("--variant", action="append", default=[], help="k=v EG knob overrides")
    ap.add_argument("--jobs", type=int, default=None)
    ap.add_argument("--label", default="")
    ap.add_argument("--per-seed", action="store_true")
    a = ap.parse_args()
    opps = a.opp or ["candidates/O4_PRODUCTIVE_SERVICE.py"]
    cand = a.cand
    if a.variant:
        kv = dict(x.split("=") for x in a.variant)
        cand = make_variant(a.cand, kv, "_".join(f"{k}{v}" for k, v in kv.items()))
    seeds = parse_seeds(a.seeds)
    for opp in opps:
        t0 = time.time()
        r = evaluate(cand, opp, seeds, engine="master", jobs=a.jobs)
        print(f"{a.label or Path(cand).stem} vs {Path(opp).stem} seeds={a.seeds} n={len(seeds)}: "
              f"margin={r['mean_margin_per_game']:+,.0f}/game t={r['t']:.2f} {r['wins']}-{r['losses']} "
              f"errs={r['agent_errors']} ({time.time()-t0:.0f}s)", flush=True)
        if a.per_seed:
            for s_, d in sorted(r["per_seed"].items()):
                print(f"   seed {s_}: seat0 {d['seat_margin'].get(0, 0):+,.0f} seat1 {d['seat_margin'].get(1, 0):+,.0f}"
                      f"  total {d['a'] - d['b']:+,.0f}")
    close_pool()


if __name__ == "__main__":
    main()
