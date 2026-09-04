#!/usr/bin/env python3
"""Mirror specialist v1: move a tape agent's SELL orders earlier.

In a mirror match both tapes sell the same items at the same steps; the engine quotes both
players the same pre-commit price per unit, so neither gains. Selling k steps earlier gets
the uncontested price and leaves the opponent selling into the depressed market.

Availability is taken from a recorded per-step shed trace of the base agent in the mirror
(base vs base), so a moved SELL never asks for more than the shed holds at the new step.

  python3 tools/sell_shift.py candidates/H31.py --k 1 --out candidates/M1_k1.py
  python3 tools/sell_shift.py candidates/H31.py --k 3 --items STRAWBERRY,MILK --out candidates/M1_k3sm.py
"""
import argparse
import base64
import importlib.util
import io
import contextlib
import json
import re
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402

MAX_ORDERS = 10


def load_module(path):
    spec = importlib.util.spec_from_file_location("base_tape", path)
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def shed_trace(path, seed=1):
    """Per-step shed dict for seat 0 of base-vs-base (the mirror), via a wrapped agent."""
    sheds = {}
    m = load_module(path)
    base_agent = m.agent

    def wrapped(obs, cfg=None):
        if obs.get("player") == 0:
            sheds[obs["step"]] = dict((obs.get("private") or {}).get("shed") or {})
        return base_agent(obs, cfg)

    orig = me.load_agent
    me.load_agent = lambda p: wrapped if str(p) == "__wrapped__" else orig(p)
    try:
        me.run_game("__wrapped__", path, seed, trace=False)
    finally:
        me.load_agent = orig
    return sheds


def shift(tape, sheds, k, items, same_day=True):
    tape = [json.loads(json.dumps(a)) for a in tape]
    # pending demand per (step,item) already moved into that step, so availability is net
    reserved = {}
    moved = 0
    for s in range(len(tape)):
        mk = tape[s].get("market") or []
        keep = []
        for o in mk:
            if not (isinstance(o, list) and o and o[0] == "SELL" and (items is None or o[1] in items)):
                keep.append(o)
                continue
            item, n = o[1], int(o[2])
            lo = max(0, s - k)
            if same_day:
                lo = max(lo, (s // 24) * 24)
            target = None
            for t in range(lo, s):
                avail = sheds.get(t, {}).get(item, 0) - reserved.get((t, item), 0)
                # units moved to t must still be in the shed at every step between t and s
                ok = avail >= n and len(tape[t].get("market") or []) < MAX_ORDERS
                if ok:
                    for u in range(t, s):
                        if sheds.get(u, {}).get(item, 0) - reserved.get((u, item), 0) < n:
                            ok = False
                            break
                if ok:
                    target = t
                    break
            if target is None:
                keep.append(o)
                continue
            tape[target].setdefault("market", []).append(["SELL", item, n])
            for u in range(target, s):
                reserved[(u, item)] = reserved.get((u, item), 0) + n
            moved += 1
        tape[s]["market"] = keep
    return tape, moved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base")
    ap.add_argument("--k", type=int, default=1)
    ap.add_argument("--items", default=None, help="comma list; default all products")
    ap.add_argument("--cross-day", action="store_true")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    items = set(a.items.split(",")) if a.items else None
    src = Path(a.base).read_text()
    m = load_module(a.base)
    sheds = shed_trace(a.base, a.seed)
    new_tape, moved = shift(m._TAPE, sheds, a.k, items, same_day=not a.cross_day)
    blob = base64.b85encode(zlib.compress(json.dumps(new_tape, separators=(",", ":")).encode())).decode()
    pat = re.compile(r"_TAPE = _json\.loads\(_zlib\.decompress\(_b64\.b85decode\('[^']*'\)\)\.decode\(\"utf-8\"\)\)")
    assert pat.search(src), "tape literal not found"
    out = pat.sub(lambda _: "_TAPE = _json.loads(_zlib.decompress(_b64.b85decode('%s')).decode(\"utf-8\"))" % blob, src)
    Path(a.out).write_text(out)
    print(f"{a.out}: moved {moved} SELL orders earlier (k={a.k}, items={a.items or 'all'})")


if __name__ == "__main__":
    main()
