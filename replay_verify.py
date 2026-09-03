#!/usr/bin/env python3
"""Replay a recorded Kaggle episode through the vendored engine via mini_engine and
check that money (and optionally full farm state) matches step for step.

This is the determinism/engine-version test: if the local engine reproduces a ladder
replay exactly, then (a) mini_engine's framework shim is faithful and (b) the vendored
engine version matches what the ladder ran for that episode.

Usage: python3 replay_verify.py Replays/Auto/<dir>/episode-XXXX-replay.json [--engine master]
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mini_engine as me  # noqa: E402


def verify(path, engine="master", verbose=False):
    d = json.load(open(path))
    cfg = dict(d["configuration"])
    seed = d["info"].get("seed")
    mod, defaults = me.load_engine(engine)
    c = dict(defaults)
    c.update(cfg)
    c["seed"] = None
    env = me._Env(c, seed)
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    steps = d["steps"]
    first_div = None
    max_abs = 0
    for k in range(len(steps) - 1):
        # recorded state k -> actions taken at k -> recorded state k+1
        rec = steps[k][0]["observation"]["farms"]
        for i in range(2):
            got = state[0].observation.farms[i]["money"]
            exp = rec[i]["money"]
            if abs(got - exp) > 0.5:
                max_abs = max(max_abs, abs(got - exp))
                if first_div is None:
                    first_div = (k, i, exp, got)
                    if verbose:
                        print(f"first divergence step {k} player {i}: recorded ${exp} engine ${got}")
        for i in range(2):
            state[i].action = steps[k + 1][i]["action"] if "action" in steps[k + 1][i] else {}
            state[i].observation.step = k
        state = mod.interpreter(state, env)
    final_rec = [steps[-1][i]["reward"] for i in range(2)]
    final_got = [state[0].observation.farms[i]["money"] for i in range(2)]
    return {"episode": d.get("id") or d["info"].get("EpisodeId"), "engine": engine, "seed": seed,
            "first_divergence": first_div, "max_abs_diff": max_abs,
            "final_recorded": final_rec, "final_engine": final_got,
            "exact": first_div is None and all(abs(a - b) < 0.5 for a, b in zip(final_rec, final_got))}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("replays", nargs="+")
    p.add_argument("--engine", default="master", choices=list(me.ENGINES))
    args = p.parse_args()
    for r in args.replays:
        res = verify(r, args.engine, verbose=True)
        print(json.dumps(res))


if __name__ == "__main__":
    main()
