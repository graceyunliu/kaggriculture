#!/usr/bin/env python3
"""Process traces: per-day execution metrics for a game, and a diagnosis of where a candidate
loses (or wins) relative to a reference on the same seed/seat.

    python3 evolve/trace.py A.py B.py --seed 1                 # print A's per-day metrics (seat 0)
    python3 evolve/trace.py A.py B.py --seed 1 --ref C1.py     # diagnose A vs C1 (both vs B, seat 0)
    python3 evolve/trace.py A.py B.py --seed 1 --vs-opponent   # diagnose A (seat 0) vs B's own play (seat 1)

Metrics per player per day (index = day 0..29):
  cash, networth (cash + shed/carried inventory at market price + animals at cost),
  sales_rev, buys_cost, hands, animals, plants, weeds_new (plants lost to weeds), escapes (animals lost),
  missed_feed (animal-days unfed), missed_water (plant-days unwatered, excl. planting day),
  feed_hour (mean hour of first FEED per animal), water_hour (mean hour of first WATER per plant),
  unit_turns, move_turns, idle_turns (PASS), reversals (a unit undoing its previous move),
  work_turns (tile/animal actions), travel_per_task (move_turns / work_turns),
  shed_units (inventory awaiting sale at day start), carried_units.
Everything comes from the engine state seen by the driver loop -- no agent cooperation needed.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402

TRACE_DIR = ROOT / "evolve" / "traces"
TRACE_VERSION = "v2"   # bump when metrics change so cached traces are recomputed
MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
WORK = {"PLANT", "WATER", "HARVEST", "FERTILIZE", "DIG", "BUILD_COOP", "BUILD_PASTURE", "FEED", "COLLECT_FERTILIZER",
        "CARE", "PLACE", "PICKUP", "DROP"}
METRICS = ["cash", "networth", "sales_rev", "buys_cost", "hands", "animals", "plants", "weeds_new", "escapes",
           "missed_feed", "missed_water", "feed_hour", "water_hour", "unit_turns", "move_turns", "idle_turns",
           "reversals", "work_turns", "travel_per_task", "shed_units", "carried_units"]


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]


def _tiles(farm):
    for y, row in enumerate(farm["tiles"]):
        for x, t in enumerate(row):
            if isinstance(t, dict):
                yield (x, y), t


def _inv_value(inv, prices):
    return sum(q * prices.get(item, 0) for item, q in (inv or {}).items())


def run_traced(agent_a, agent_b, seed, engine="master", config=None):
    """Play one game, agent_a in seat 0, recording per-day process metrics for both players."""
    mod, defaults = me.load_engine(engine)
    cfg = dict(defaults)
    if config:
        cfg.update(config)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(agent_a), me.load_agent(agent_b)]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    tpd = int(cfg["turnsPerDay"])
    steps = int(cfg["episodeSteps"])
    animal_cost = {k: v["cost"] for k, v in mod.ANIMALS.items()}

    # sales/buys via the engine's commit hook (same trick as mini_engine)
    day_sales = [0.0, 0.0]
    day_buys = [0.0, 0.0]
    farms_ref = [None]
    orig_commit = mod._commit_unit

    def logged_commit(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig_commit(op, item, price, farm, private, market, shed_capacity)
        if ok and farms_ref[0] is not None:
            pid = 0 if farm is farms_ref[0][0] else 1
            if op == "SELL":
                day_sales[pid] += price
            elif op in ("BUY_PRODUCT", "BUY_SEED", "BUY_ANIMAL"):
                day_buys[pid] += price
        return ok

    mod._commit_unit = logged_commit

    T = [{m: [] for m in METRICS} for _ in range(2)]
    acc = [None, None]           # per-day accumulators
    prev_pos = [None, None]      # positions last turn
    prev_move = [None, None]     # last move op per unit
    fed_hour = [{}, {}]          # tile -> hour first fed today
    wat_hour = [{}, {}]
    plant_set_prev = [set(), set()]
    animal_set_prev = [set(), set()]
    errors = [0, 0]

    def new_acc():
        return {"unit_turns": 0, "move_turns": 0, "idle_turns": 0, "reversals": 0, "work_turns": 0, "hands_max": 0}

    def day_start(i, obs, farm, private, day):
        prices = obs["market"]["prices"] if "market" in obs else {}
        shed = private.get("shed", {}) or {}
        carried = private.get("inventories") or []
        animals = [(p, t) for p, t in _tiles(farm) if "animal" in t]
        plants = [(p, t) for p, t in _tiles(farm) if t.get("kind") == "PLANT"]
        nw = farm["money"] + _inv_value(shed, prices) + sum(_inv_value(c, prices) for c in carried) \
            + sum(animal_cost.get(t["animal"], 0) for _, t in animals)
        # obligations missed yesterday: counters incremented by the daily refresh
        missed_feed = sum(1 for _, t in animals if t.get("consecutive_unfed", 0) > 0)
        missed_water = sum(1 for _, t in plants if t.get("consecutive_unwatered", 0) > 0 and t.get("planted_day", day) < day - 1)
        aset = {p for p, _ in animals}
        pset = {p for p, _ in plants}
        escapes = len(animal_set_prev[i] - aset) if day > 0 else 0
        weeds_new = sum(1 for p in plant_set_prev[i] - pset if isinstance(farm["tiles"][p[1]][p[0]], dict)
                        and farm["tiles"][p[1]][p[0]].get("kind") == "WEED") if day > 0 else 0
        animal_set_prev[i], plant_set_prev[i] = aset, pset
        t = T[i]
        t["cash"].append(farm["money"])
        t["networth"].append(round(nw))
        t["animals"].append(len(animals))
        t["plants"].append(len(plants))
        t["missed_feed"].append(missed_feed)
        t["missed_water"].append(missed_water)
        t["escapes"].append(escapes)
        t["weeds_new"].append(weeds_new)
        t["shed_units"].append(sum(shed.values()))
        t["carried_units"].append(sum(sum(c.values()) for c in carried))

    def day_end(i):
        a = acc[i] or new_acc()
        t = T[i]
        for k in ("unit_turns", "move_turns", "idle_turns", "reversals", "work_turns"):
            t[k].append(a[k])
        t["hands"].append(a["hands_max"])
        t["travel_per_task"].append(round(a["move_turns"] / max(1, a["work_turns"]), 2))
        t["sales_rev"].append(round(day_sales[i]))
        t["buys_cost"].append(round(day_buys[i]))
        t["feed_hour"].append(round(sum(fed_hour[i].values()) / len(fed_hour[i]), 1) if fed_hour[i] else None)
        t["water_hour"].append(round(sum(wat_hour[i].values()) / len(wat_hour[i]), 1) if wat_hour[i] else None)
        day_sales[i] = 0.0
        day_buys[i] = 0.0
        fed_hour[i] = {}
        wat_hour[i] = {}
        acc[i] = new_acc()

    t0 = time.time()
    step = 0
    cur_day = -1
    while True:
        obs0 = state[0].observation
        farms_ref[0] = obs0.farms
        day, hour = obs0.day, obs0.hour
        if day != cur_day:
            if cur_day >= 0:
                for i in range(2):
                    day_end(i)
            cur_day = day
            for i in range(2):
                acc[i] = acc[i] or new_acc()
                day_start(i, state[i].observation, obs0.farms[i], state[i].observation.private, day)
        # record first-service hours (state after last turn's actions)
        for i in range(2):
            for p, t in _tiles(obs0.farms[i]):
                if "animal" in t and t.get("fed_today") and p not in fed_hour[i]:
                    fed_hour[i][p] = hour
                elif t.get("kind") == "PLANT" and t.get("watered_today") and p not in wat_hour[i]:
                    wat_hour[i][p] = hour
        acts = []
        for i in range(2):
            obs = copy.deepcopy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, copy.deepcopy(env.configuration))
            except Exception:  # noqa: BLE001
                errors[i] += 1
                act = {}
            act = act if isinstance(act, dict) else {}
            state[i].action = act
            acts.append(act)
        # count unit actions
        for i in range(2):
            farm = obs0.farms[i]
            ops = [acts[i].get("farmer") or ["PASS"]] + list(acts[i].get("hands") or [])
            n_units = 1 + len(farm["hands"])
            ops = (ops + [["PASS"]] * n_units)[:n_units]
            a = acc[i]
            a["unit_turns"] += n_units
            a["hands_max"] = max(a["hands_max"], n_units - 1)
            pm = prev_move[i] or [None] * n_units
            pm = (pm + [None] * n_units)[:n_units]
            for u, op in enumerate(ops):
                verb = op[0] if isinstance(op, (list, tuple)) and op else str(op)
                if verb in MOVES:
                    a["move_turns"] += 1
                    if pm[u] and MOVES[verb] == (-MOVES[pm[u]][0], -MOVES[pm[u]][1]):
                        a["reversals"] += 1
                    pm[u] = verb
                else:
                    if verb == "PASS":
                        a["idle_turns"] += 1
                    elif verb in WORK:
                        a["work_turns"] += 1
                    pm[u] = None
            prev_move[i] = pm
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break
    for i in range(2):
        day_end(i)
    mod._commit_unit = orig_commit
    obs0 = state[0].observation
    money = [obs0.farms[i]["money"] for i in range(2)]
    return {"seed": seed, "engine": engine, "money": money, "errors": errors, "seconds": round(time.time() - t0, 2),
            "a": str(agent_a), "b": str(agent_b), "trace": T}


def traced(agent_a, agent_b, seed, engine="master", use_cache=True):
    """Cached run_traced keyed by file shas."""
    TRACE_DIR.mkdir(exist_ok=True)
    key = f"{TRACE_VERSION}_{_sha(agent_a)}_{_sha(agent_b)}_{engine}_{seed}"
    f = TRACE_DIR / f"{key}.json"
    if use_cache and f.exists():
        try:
            return json.load(open(f))
        except Exception:  # noqa: BLE001
            pass
    r = run_traced(agent_a, agent_b, seed, engine)
    if use_cache:
        json.dump(r, open(f, "w"))
    return r


# ---------------------------------------------------------------------------- diagnosis
def _cum(xs):
    out, s = [], 0
    for x in xs:
        s += (x or 0)
        out.append(s)
    return out


def diagnose(t_cand, t_ref, label_cand="cand", label_ref="ref", threshold=1500):
    """Compare two per-day traces (same seed/seat). Returns dict with first divergence and drivers,
    plus a one-paragraph text."""
    n = min(len(t_cand["networth"]), len(t_ref["networth"]))
    nw = [t_cand["networth"][d] - t_ref["networth"][d] for d in range(n)]
    final = nw[-1] if nw else 0
    sign = -1 if final < 0 else 1
    # first day the gap in the final direction exceeds threshold and never comes back within half of it
    div_day = None
    for d in range(n):
        if sign * nw[d] >= threshold and all(sign * nw[e] >= threshold / 2 for e in range(d, n)):
            div_day = d
            break
    # drivers: cumulative differences of count metrics over the window [div_day-2, min(div_day+5, n)]
    lo = max(0, (div_day or 0) - 2)
    hi = min(n, (div_day if div_day is not None else n - 1) + 6)
    drivers = {}
    for m in ("missed_feed", "missed_water", "escapes", "weeds_new", "idle_turns", "move_turns", "work_turns",
              "reversals", "sales_rev", "buys_cost", "hands", "animals", "plants", "shed_units"):
        a = sum((t_cand[m][d] or 0) for d in range(lo, hi))
        b = sum((t_ref[m][d] or 0) for d in range(lo, hi))
        drivers[m] = a - b
    lat = {}
    for m in ("feed_hour", "water_hour", "travel_per_task"):
        va = [t_cand[m][d] for d in range(lo, hi) if t_cand[m][d] is not None]
        vb = [t_ref[m][d] for d in range(lo, hi) if t_ref[m][d] is not None]
        if va and vb:
            lat[m] = round(sum(va) / len(va) - sum(vb) / len(vb), 2)
    # rank drivers by plausible relevance to the sign of the gap
    bad = []
    if sign < 0:
        for m, w in (("missed_feed", 1), ("missed_water", 1), ("escapes", 5), ("weeds_new", 3), ("idle_turns", 0.2),
                     ("reversals", 0.3)):
            if drivers[m] > 0:
                bad.append((drivers[m] * w, f"{m} +{drivers[m]}"))
        if drivers["sales_rev"] < 0:
            bad.append((-drivers["sales_rev"] / 200, f"sales_rev {drivers['sales_rev']:+,}"))
        if drivers["work_turns"] < 0:
            bad.append((-drivers["work_turns"] * 0.2, f"work_turns {drivers['work_turns']:+}"))
        for m in ("feed_hour", "water_hour", "travel_per_task"):
            if lat.get(m, 0) > 0:
                bad.append((lat[m] * 3, f"{m} +{lat[m]}"))
    else:
        for m, w in (("missed_feed", 1), ("missed_water", 1), ("escapes", 5), ("weeds_new", 3), ("idle_turns", 0.2)):
            if drivers[m] < 0:
                bad.append((-drivers[m] * w, f"{m} {drivers[m]}"))
        if drivers["sales_rev"] > 0:
            bad.append((drivers["sales_rev"] / 200, f"sales_rev {drivers['sales_rev']:+,}"))
        if drivers["work_turns"] > 0:
            bad.append((drivers["work_turns"] * 0.2, f"work_turns {drivers['work_turns']:+}"))
        for m in ("feed_hour", "water_hour", "travel_per_task"):
            if lat.get(m, 0) < 0:
                bad.append((-lat[m] * 3, f"{m} {lat[m]}"))
    bad.sort(reverse=True)
    top = [b[1] for b in bad[:4]]
    if div_day is None:
        text = f"{label_cand} vs {label_ref}: net worth never diverged by >${threshold:,} (final {final:+,})."
    else:
        verb = "falls behind" if sign < 0 else "pulls ahead of"
        text = (f"{label_cand} {verb} {label_ref} from day {div_day} (gap {nw[div_day]:+,} -> final {final:+,}); "
                f"days {lo}-{hi-1} drivers: " + (", ".join(top) if top else "no clear execution driver (allocation/timing)")
                + f". Hands {t_cand['hands'][hi-1]} vs {t_ref['hands'][hi-1]}, animals {t_cand['animals'][hi-1]} vs {t_ref['animals'][hi-1]}, "
                  f"plants {t_cand['plants'][hi-1]} vs {t_ref['plants'][hi-1]}.")
    return {"final_gap": final, "div_day": div_day, "window": [lo, hi - 1], "drivers": drivers, "latency": lat,
            "top": top, "text": text, "networth_gap": nw}


def summary_row(t):
    """Whole-game execution summary for one player trace."""
    n = len(t["networth"])
    tot = lambda m: sum((t[m][d] or 0) for d in range(n))  # noqa: E731
    fh = [x for x in t["feed_hour"] if x is not None]
    wh = [x for x in t["water_hour"] if x is not None]
    return {"final_networth": t["networth"][-1] if n else None, "sales": tot("sales_rev"), "buys": tot("buys_cost"),
            "missed_feed": tot("missed_feed"), "missed_water": tot("missed_water"), "escapes": tot("escapes"),
            "weeds_new": tot("weeds_new"), "unit_turns": tot("unit_turns"), "move_share": round(tot("move_turns") / max(1, tot("unit_turns")), 3),
            "idle_share": round(tot("idle_turns") / max(1, tot("unit_turns")), 3), "travel_per_task": round(tot("move_turns") / max(1, tot("work_turns")), 2),
            "reversals": tot("reversals"), "feed_hour": round(sum(fh) / len(fh), 1) if fh else None,
            "water_hour": round(sum(wh) / len(wh), 1) if wh else None, "max_hands": max(t["hands"]) if n else 0,
            "max_animals": max(t["animals"]) if n else 0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--ref", default=None, help="reference agent to diagnose A against (both vs B, seat 0)")
    ap.add_argument("--vs-opponent", action="store_true", help="diagnose A (seat 0) against B's own trace (seat 1)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    r = traced(args.a, args.b, args.seed)
    ta = r["trace"][0]
    if args.vs_opponent:
        d = diagnose(ta, r["trace"][1], Path(args.a).stem, Path(args.b).stem)
        print(d["text"])
        print("A:", json.dumps(summary_row(ta)))
        print("B:", json.dumps(summary_row(r["trace"][1])))
        return
    if args.ref:
        rr = traced(args.ref, args.b, args.seed)
        d = diagnose(ta, rr["trace"][0], Path(args.a).stem, Path(args.ref).stem)
        print(d["text"])
        if args.json:
            print(json.dumps(d))
        return
    print(f"money {r['money']} errors {r['errors']} {r['seconds']}s")
    print(json.dumps(summary_row(ta)))
    for m in METRICS:
        print(f"{m:16s}", " ".join(f"{(x if x is not None else '-'):>6}" for x in ta[m]))


if __name__ == "__main__":
    main()
