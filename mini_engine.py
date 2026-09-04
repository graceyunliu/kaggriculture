#!/usr/bin/env python3
"""mini_engine: run kaggriculture games on the vendored engine WITHOUT kaggle_environments.

Why: the kaggle_environments package is not needed to run the engine -- kaggriculture.py
imports only stdlib plus `resolve_episode_seed` from kaggle_environments.utils. This
module shims that one import and re-implements the ~40 lines of framework loop the
engine relies on (Struct attribute access, step counter, done flag, info["seed"]).

Benefits over seeded_h2h.py / smoke_test.py:
  * no pip install, works in any sandbox with python3
  * picks the engine explicitly: --engine master (ladder) or --engine 1.32 (older vendored)
  * emits a per-day trace for both players (money, hands, animals, land, shed inventory)
  * parallel both-seats evaluation via multiprocessing, results cached by
    (agent sha, opp sha, engine, config, seed, seat)

Usage:
  python3 mini_engine.py A.py B.py --seeds 1 2 3 --both-seats [--engine master] [--jobs 8]
  python3 mini_engine.py A.py B.py --seeds 5 --trace out.json     # per-day traces

Programmatic:
  from mini_engine import run_game
  res = run_game("A.py", "B.py", seed=5, engine="master")
  res["money"], res["trace"][0]["money"][29]
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import random
import sys
import time
import types
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENGINES = {
    "master": ROOT / "vendor" / "kaggle_environments_engine_master",
    "1.32": ROOT / "vendor" / "kaggle_environments_engine",
}
CACHE_DIR = ROOT / ".mini_engine_cache"
CACHE_VERSION = "v2"  # v2 adds plants/weeds to cached traces


# --------------------------------------------------------------------------- shim
class Struct(dict):
    """dict with attribute access, like kaggle_environments.utils.Struct."""

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k)

    def __setattr__(self, k, v):
        self[k] = v

    def __delattr__(self, k):
        del self[k]


def structify(o):
    if isinstance(o, dict) and not isinstance(o, Struct):
        return Struct({k: structify(v) for k, v in o.items()})
    if isinstance(o, Struct):
        for k, v in o.items():
            o[k] = structify(v)
        return o
    if isinstance(o, list):
        return [structify(v) for v in o]
    return o


def _fast_copy(o):
    """Copy the JSON-like engine state without deepcopy's memo/reconstruction cost."""
    kind = type(o)
    if kind is Struct:
        return Struct({k: _fast_copy(v) for k, v in o.items()})
    if kind is dict:
        return {k: _fast_copy(v) for k, v in o.items()}
    if kind is list:
        return [_fast_copy(v) for v in o]
    if kind is tuple:
        return tuple(_fast_copy(v) for v in o)
    # Engine observations are restricted to immutable JSON scalars.
    return o


def _resolve_episode_seed(env, *, config_key="seed", fallback=None):
    if not hasattr(env, "info") or env.info is None:
        env.info = {}
    seed = env.info.get("seed")
    if seed is None:
        seed = env.configuration.get(config_key)
    if seed is None:
        seed = fallback() if fallback else random.randrange(2**31)
    env.configuration[config_key] = None
    env.info["seed"] = seed
    return seed


def _install_shim():
    if "kaggle_environments" in sys.modules:
        return
    pkg = types.ModuleType("kaggle_environments")
    utils = types.ModuleType("kaggle_environments.utils")
    utils.resolve_episode_seed = _resolve_episode_seed
    utils.Struct = Struct
    utils.structify = structify
    pkg.utils = utils
    sys.modules["kaggle_environments"] = pkg
    sys.modules["kaggle_environments.utils"] = utils


_ENGINE_CACHE = {}


def load_engine(name="master"):
    if name in _ENGINE_CACHE:
        return _ENGINE_CACHE[name]
    _install_shim()
    d = ENGINES[name]
    spec = importlib.util.spec_from_file_location(f"kag_engine_{name.replace('.', '_')}", d / "kaggriculture.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cfg_defaults = {}
    for k, v in json.load(open(d / "kaggriculture.json"))["configuration"].items():
        cfg_defaults[k] = v.get("default") if isinstance(v, dict) else v
    _ENGINE_CACHE[name] = (mod, cfg_defaults)
    return mod, cfg_defaults


_AGENT_N = 0


def load_agent(path):
    """Fresh module instance per call (agents keep global state)."""
    global _AGENT_N
    _AGENT_N += 1
    path = Path(path)
    name = f"agent_{path.stem}_{_AGENT_N}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod.agent


class _Env:
    def __init__(self, configuration, seed):
        self.configuration = Struct(configuration)
        self.info = {"seed": seed}
        self.done = False


# --------------------------------------------------------------------------- game
def _snapshot(farm, private):
    animals = {}
    plants = 0
    weeds = 0
    for row in farm["tiles"]:
        for t in row:
            if isinstance(t, dict) and "animal" in t:
                animals[t["animal"]] = animals.get(t["animal"], 0) + 1
            if isinstance(t, dict) and t.get("kind") == "PLANT":
                plants += 1
            if isinstance(t, dict) and t.get("kind") == "WEED":
                weeds += 1
    return {
        "money": farm["money"],
        "hands": len(farm["hands"]),
        "animals": sum(animals.values()),
        "animal_mix": animals,
        "plants": plants,
        "weeds": weeds,
        "land": len(farm["unlocked_quadrants"]),
        "shed": dict(private["shed"]),
        "seeds": dict(private.get("seeds", {})),
    }


def run_game(agent_a, agent_b, seed, engine="master", config=None, trace=True, turns=None,
             debug_agent_mutation=False):
    """Play one game, agent_a in seat 0. Returns dict with money, winner, trace."""
    mod, defaults = load_engine(engine)
    cfg = dict(defaults)
    if config:
        cfg.update(config)
    if turns:
        cfg["episodeSteps"] = turns
    cfg["seed"] = None
    env = _Env(cfg, seed)
    agents = [load_agent(agent_a), load_agent(agent_b)]

    state = structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)  # _initialize
    for s in state:
        s.observation.step = 0

    tpd = int(cfg["turnsPerDay"])
    steps = int(cfg["episodeSteps"])
    traces = [{"money": [], "hands": [], "animals": [], "land": [], "shed": [], "animal_mix": [],
               "plants": [], "weeds": [],
               "sales": [], "buys": [], "hands_eod": []} for _ in range(2)]
    # --- sales/buy logging: wrap the engine's _commit_unit (looked up by global name)
    day_sales = [dict(), dict()]
    day_buys = [dict(), dict()]
    farms_ref = [None]
    orig_commit = mod._commit_unit

    def logged_commit(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig_commit(op, item, price, farm, private, market, shed_capacity)
        if ok and trace and farms_ref[0] is not None:
            pid = 0 if farm is farms_ref[0][0] else 1
            if op == "SELL":
                q, rev = day_sales[pid].get(item, (0, 0))
                day_sales[pid][item] = (q + 1, rev + price)
            elif op in ("BUY_PRODUCT", "BUY_SEED", "BUY_ANIMAL"):
                q, cost = day_buys[pid].get(item, (0, 0))
                day_buys[pid][item] = (q + 1, cost + price)
        return ok

    mod._commit_unit = logged_commit
    errors = [0, 0]
    t0 = time.time()
    step = 0
    while True:
        obs0 = state[0].observation
        farms_ref[0] = obs0.farms
        # per-day snapshot at hour 0
        if obs0.hour == 0 and trace:
            for i in range(2):
                snap = _snapshot(obs0.farms[i], state[i].observation.private)
                for k in ("money", "hands", "animals", "land", "shed", "animal_mix", "plants", "weeds"):
                    traces[i][k].append(snap[k])
                if step > 0:
                    traces[i]["sales"].append(day_sales[i])
                    traces[i]["buys"].append(day_buys[i])
                    day_sales[i] = {}
                    day_buys[i] = {}
        if obs0.hour == tpd - 1 and trace:
            for i in range(2):
                traces[i]["hands_eod"].append(len(obs0.farms[i]["hands"]))
        for i in range(2):
            before = copy.deepcopy(state) if debug_agent_mutation else None
            obs = _fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, _fast_copy(env.configuration))
            except Exception as e:  # noqa: BLE001 - agent crash = PASS turn, counted
                errors[i] += 1
                act = {}
            if debug_agent_mutation and state != before:
                raise AssertionError(f"agent {i} mutated engine state at step {step}")
            state[i].action = act if isinstance(act, dict) else {}
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            env.done = True
            break
        if step >= steps:
            break
    mod._commit_unit = orig_commit
    obs0 = state[0].observation
    money = [obs0.farms[i]["money"] for i in range(2)]
    if trace:
        for i in range(2):
            snap = _snapshot(obs0.farms[i], state[i].observation.private)
            for k in ("money", "hands", "animals", "land", "shed", "animal_mix", "plants", "weeds"):
                traces[i][k].append(snap[k])
            traces[i]["sales"].append(day_sales[i])
            traces[i]["buys"].append(day_buys[i])
    return {
        "seed": seed, "engine": engine, "money": money,
        "winner": 0 if money[0] > money[1] else (1 if money[1] > money[0] else None),
        "errors": errors, "seconds": round(time.time() - t0, 2), "steps": step,
        "trace": traces if trace else None,
    }


# --------------------------------------------------------------------------- eval
def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]


def _cache_key(a, b, seed, engine, config):
    c = json.dumps(config or {}, sort_keys=True)
    return f"{CACHE_VERSION}_{_sha(a)}_{_sha(b)}_{engine}_{hashlib.md5(c.encode()).hexdigest()[:8]}_{seed}"


def _job(args):
    a, b, seed, engine, config, use_cache, swapped = args
    key = _cache_key(a, b, seed, engine, config)
    f = CACHE_DIR / f"{key}.json"
    res = None
    if use_cache and f.exists():
        try:
            res = json.load(open(f))
        except Exception:
            res = None
    if res is None:
        res = run_game(a, b, seed, engine, config)
        res["a"], res["b"] = str(a), str(b)
        if use_cache:
            CACHE_DIR.mkdir(exist_ok=True)
            json.dump(res, open(f, "w"))
    res["swapped"] = swapped   # seat of the evaluated agent is decided by the job, never by cached paths
    return res


def evaluate(a, b, seeds, engine="master", config=None, both_seats=True, jobs=None, use_cache=True, pool=None):
    """Paired evaluation of agent a vs b. Returns per-seed margins (a - b) and summary."""
    jobs_list = []
    for s in seeds:
        jobs_list.append((a, b, s, engine, config, use_cache, False))
        if both_seats:
            jobs_list.append((b, a, s, engine, config, use_cache, True))
    if pool is not None:
        results = pool.map(_job, jobs_list)
    else:
        with Pool(jobs or max(1, os.cpu_count() - 1)) as p:
            results = p.map(_job, jobs_list)
    per_seed = {}
    for r in results:
        s = r["seed"]
        if not r["swapped"]:
            a_money, b_money, seat = r["money"][0], r["money"][1], 0
        else:
            a_money, b_money, seat = r["money"][1], r["money"][0], 1
        d = per_seed.setdefault(s, {"a": 0.0, "b": 0.0, "seat_margin": {}, "errors": [0, 0]})
        d["a"] += a_money
        d["b"] += b_money
        d["seat_margin"][seat] = a_money - b_money
        d["errors"][0] += r["errors"][0 if seat == 0 else 1]
        d["errors"][1] += r["errors"][1 if seat == 0 else 0]
    margins = [d["a"] - d["b"] for d in per_seed.values()]
    n = len(margins)
    mean = sum(margins) / n
    sd = (sum((m - mean) ** 2 for m in margins) / (n - 1)) ** 0.5 if n > 1 else 0.0
    t = mean / (sd / n ** 0.5) if sd > 0 else float("inf")
    games = 2 if both_seats else 1
    return {
        "a": str(a), "b": str(b), "engine": engine, "config": config or {}, "seeds": list(seeds),
        "both_seats": both_seats,
        "mean_a": sum(d["a"] for d in per_seed.values()) / n / games,
        "mean_b": sum(d["b"] for d in per_seed.values()) / n / games,
        "mean_margin_per_game": mean / games, "t": t,
        "wins": sum(m > 0 for m in margins), "losses": sum(m < 0 for m in margins),
        "seat0_wins": sum(d["seat_margin"].get(0, 0) > 0 for d in per_seed.values()),
        "seat1_wins": sum(d["seat_margin"].get(1, 0) > 0 for d in per_seed.values()),
        "per_seed": per_seed,
        "agent_errors": [sum(d["errors"][0] for d in per_seed.values()), sum(d["errors"][1] for d in per_seed.values())],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("a")
    p.add_argument("b")
    p.add_argument("--seeds", type=int, nargs="+", default=list(range(1, 11)))
    p.add_argument("--engine", default="master", choices=list(ENGINES))
    p.add_argument("--config", default=None, help='JSON overrides, e.g. \'{"townCenterSellInterval": 12}\'')
    p.add_argument("--both-seats", action="store_true")
    p.add_argument("--jobs", type=int, default=None)
    p.add_argument("--no-cache", action="store_true")
    p.add_argument("--trace", default=None, help="write per-seed traces (single-seat runs) to this JSON")
    args = p.parse_args()
    config = json.loads(args.config) if args.config else None

    if args.trace:
        out = [run_game(args.a, args.b, s, args.engine, config) for s in args.seeds]
        json.dump(out, open(args.trace, "w"))
        for r in out:
            print(f"seed {r['seed']}: A ${r['money'][0]:,.0f}  B ${r['money'][1]:,.0f}  errors={r['errors']}  {r['seconds']}s")
        return

    res = evaluate(args.a, args.b, args.seeds, args.engine, config, args.both_seats, args.jobs, not args.no_cache)
    print(f"{Path(args.a).name} vs {Path(args.b).name}  engine={args.engine} config={config or {}}")
    print(f"seeds={len(args.seeds)} both_seats={args.both_seats}")
    print(f"mean A ${res['mean_a']:,.0f}  mean B ${res['mean_b']:,.0f}  margin/game ${res['mean_margin_per_game']:+,.0f}  t={res['t']:.2f}")
    print(f"seed-wins {res['wins']}-{res['losses']}   seat0 wins {res['seat0_wins']}  seat1 wins {res['seat1_wins']}   agent errors {res['agent_errors']}")
    for s, d in sorted(res["per_seed"].items()):
        sm = "  ".join(f"seat{k}:{v:+,.0f}" for k, v in sorted(d["seat_margin"].items()))
        print(f"  seed {s:>5}: margin {d['a']-d['b']:+,.0f}   {sm}")


if __name__ == "__main__":
    main()
