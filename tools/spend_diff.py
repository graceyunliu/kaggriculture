#!/usr/bin/env python3
"""Spend diff (Sep 11): what an intervention actually DID, decomposed into three layers, both farms.

Companion to tools/horizon_roi.py, which says an intervention is worth $X but not what changed to produce
it. Every intervention in this game acts on three layers and the project has been bitten by each:

  Layer 1  direct economics     -- what did we stop spending, or start spending?
  Layer 2  trajectory redeploy  -- what did the UNCHANGED policy buy instead, because state changed?
  Layer 3  shared market        -- how did our changed production move prices, and who else gained?

The capital checkpoint was layer 3 faking a win (margin up, own money DOWN). The hire gate is a layer-1 win
that ALSO creates a layer-3 spillover the opponent shares in (both farms gain; we gain more). A single ROI
number cannot tell those apart, which is why this exists.

Accounting is EXACT, not inferred. Following tools/allocation_matrix.py, we wrap the engine's
`_commit_unit` so every committed market unit is recorded with its realized price and owning farm. That
matters because sales commit unit by unit at a price that moves with market inventory as the sale proceeds,
and a SELL larger than the shed holds is a legal no-op -- so a submitted order is only an upper bound on
both units and revenue, and quoting the order price overstates a large sale. `_do_hire` and `_do_buy_land`
are wrapped the same way, because both deduct inside the engine and both can silently skip when money is
short: HIRE costs `_fib(n)` for the n-th hire of the day and hands are cleared nightly, so the wage bill is
convex in the day's hire count and cannot be recovered from a headcount average, and an assumed schedule
would count hires that never happened.

Usage:
  KAGG_FIXED_SHOPS=1 python3 tools/spend_diff.py BASE CAND --opp TAPE --seeds 21-30
  KAGG_FIXED_SHOPS=1 python3 tools/spend_diff.py BASE CAND --opp TAPE --seeds 21-30 --by-day
"""
from __future__ import annotations

import argparse
import collections
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me  # noqa: E402

YIELD_OF = {"MILK": "COW", "WOOL": "SHEEP", "EGG": "GOOSE"}


def run(cand, opp, seed):
    """One game. Returns per-farm exact ledgers plus end-of-game market inventory."""
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    step = 0

    L = [collections.Counter() for _ in range(2)]          # scalar totals per farm
    SOLD = [collections.Counter() for _ in range(2)]       # units sold per product
    REV = [collections.Counter() for _ in range(2)]        # realized revenue per product
    BUY = [collections.Counter() for _ in range(2)]        # units bought per "VERB:ITEM"
    BUYC = [collections.Counter() for _ in range(2)]       # realized cost per "VERB:ITEM"
    WAGE_DAY = [collections.Counter() for _ in range(2)]   # realized wage by day
    HIRE_DAY = [collections.Counter() for _ in range(2)]   # successful hires by day

    # --- exact engine-side accounting -------------------------------------------------------------
    trades, hires, lands = [], [], []
    orig_commit, orig_hire, orig_land = mod._commit_unit, mod._do_hire, mod._do_buy_land

    def rec_commit(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig_commit(op, item, price, farm, private, market, shed_capacity)
        if ok:
            trades.append((id(farm), op, item, price))
        return ok

    def rec_hire(farm, private, board_size, mult=1):
        before = farm["money"]
        orig_hire(farm, private, board_size, mult)
        spent = before - farm["money"]
        if spent > 0:                      # _do_hire returns early when money < cost
            hires.append((id(farm), spent))

    def rec_land(farm, board_size):
        before = farm["money"]
        orig_land(farm, board_size)
        spent = before - farm["money"]
        if spent > 0:
            lands.append((id(farm), spent))

    mod._commit_unit, mod._do_hire, mod._do_buy_land = rec_commit, rec_hire, rec_land
    try:
        while True:
            day = state[0].observation.day
            for i in range(2):
                obs = me._fast_copy(state[i].observation)
                obs["step"] = step
                try:
                    act = agents[i](obs, me._fast_copy(env.configuration))
                except Exception:
                    act = {}
                state[i].action = act
            state = mod.interpreter(state, env)
            step += 1
            for s in state:
                s.observation.step = step
            o = state[0].observation
            fid = {id(o.farms[p]): p for p in range(2)}
            for (f, op, item, price) in trades:
                i = fid.get(f)
                if i is None:
                    continue
                if op == "SELL":
                    SOLD[i][item] += 1
                    REV[i][item] += price
                    L[i]["revenue"] += price
                else:
                    BUY[i][f"{op}:{item}"] += 1
                    BUYC[i][f"{op}:{item}"] += price
                    L[i]["purchases"] += price
            for (f, spent) in hires:
                i = fid.get(f)
                if i is not None:
                    L[i]["wages"] += spent
                    WAGE_DAY[i][day] += spent
                    HIRE_DAY[i][day] += 1
            for (f, spent) in lands:
                i = fid.get(f)
                if i is not None:
                    L[i]["land"] += spent
                    BUY[i]["BUY_LAND"] += 1
                    BUYC[i]["BUY_LAND"] += spent
            trades.clear()
            hires.clear()
            lands.clear()
            if all(s.status == "DONE" for s in state) or step >= steps:
                break
    finally:
        mod._commit_unit, mod._do_hire, mod._do_buy_land = orig_commit, orig_hire, orig_land

    o = state[0].observation
    for p in range(2):
        L[p]["final"] = o.farms[p]["money"]
    return {"L": L, "SOLD": SOLD, "REV": REV, "BUY": BUY, "BUYC": BUYC,
            "WAGE_DAY": WAGE_DAY, "HIRE_DAY": HIRE_DAY,
            "inv": dict(o.market["inventory"])}


def mean_over(cand, opp, seeds):
    acc = None
    for s in seeds:
        r = run(cand, opp, s)
        if acc is None:
            acc = r
            acc["inv"] = collections.Counter(r["inv"])
            continue
        for key in ("L", "SOLD", "REV", "BUY", "BUYC", "WAGE_DAY", "HIRE_DAY"):
            for p in range(2):
                acc[key][p].update(r[key][p])
        acc["inv"].update(r["inv"])
    n = float(len(seeds))
    for key in ("L", "SOLD", "REV", "BUY", "BUYC", "WAGE_DAY", "HIRE_DAY"):
        for p in range(2):
            acc[key][p] = {k: v / n for k, v in acc[key][p].items()}
    acc["inv"] = {k: v / n for k, v in acc["inv"].items()}
    return acc


def row(label, a, b, money=True):
    d = b - a
    if abs(d) < 1e-9 and abs(a) < 1e-9 and abs(b) < 1e-9:
        return None
    fmt = "{:>12,.0f}" if money else "{:>12,.1f}"
    return ("  {:<26}".format(label) + fmt.format(a) + fmt.format(b)
            + ("{:>+13,.0f}".format(d) if money else "{:>+13,.1f}".format(d))
            + ("" if abs(d) > 1e-9 else "   (unchanged)"))


def emit(label, a, b, money=True):
    r = row(label, a, b, money)
    if r:
        print(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("base")
    ap.add_argument("cand")
    ap.add_argument("--opp", required=True)
    ap.add_argument("--seeds", default="21-30")
    ap.add_argument("--by-day", action="store_true", help="also print the wage bill by day")
    a = ap.parse_args()
    if os.environ.get("KAGG_FIXED_SHOPS") != "1":
        print("WARNING: KAGG_FIXED_SHOPS is not 1; shop draws are policy-dependent and every delta below "
              "is contaminated by the shop lottery.", file=sys.stderr)
    if "-" in a.seeds:
        lo, hi = a.seeds.split("-")
        seeds = list(range(int(lo), int(hi) + 1))
    else:
        seeds = [int(x) for x in a.seeds.split(",")]

    B = mean_over(a.base, a.opp, seeds)
    C = mean_over(a.cand, a.opp, seeds)
    bn, cn = os.path.basename(a.base), os.path.basename(a.cand)
    print(f"# {bn}  ->  {cn}   vs {os.path.basename(a.opp)}, {len(seeds)} seeds, per game")
    print("  {:<26}{:>12}{:>12}{:>13}".format("", "base", "cand", "delta"))

    print("\nLAYER 1 -- direct economics (us)")
    for k, lbl in (("wages", "wages (realized)"), ("purchases", "market purchases"),
                   ("land", "land"), ("revenue", "revenue (realized)"), ("final", "final money")):
        emit(lbl, B["L"][0].get(k, 0.0), C["L"][0].get(k, 0.0))

    print("\nLAYER 2 -- redeployment: what the unchanged policy bought instead")
    print("  (units, then realized cost)")
    for k in sorted(set(B["BUY"][0]) | set(C["BUY"][0])):
        emit(k + " units", B["BUY"][0].get(k, 0.0), C["BUY"][0].get(k, 0.0), money=False)
        emit(k + " cost", B["BUYC"][0].get(k, 0.0), C["BUYC"][0].get(k, 0.0))

    print("\nLAYER 3 -- shared market")
    print("  our sales (realized units and revenue)")
    for k in sorted(set(B["SOLD"][0]) | set(C["SOLD"][0])):
        emit("sold " + k, B["SOLD"][0].get(k, 0.0), C["SOLD"][0].get(k, 0.0), money=False)
        emit("rev  " + k, B["REV"][0].get(k, 0.0), C["REV"][0].get(k, 0.0))
    print("  opponent")
    for k, lbl in (("final", "opp final money"), ("revenue", "opp revenue"),
                   ("purchases", "opp purchases"), ("wages", "opp wages")):
        emit(lbl, B["L"][1].get(k, 0.0), C["L"][1].get(k, 0.0))
    print("  opponent sales (realized units)")
    for k in sorted(set(B["SOLD"][1]) | set(C["SOLD"][1])):
        emit("opp sold " + k, B["SOLD"][1].get(k, 0.0), C["SOLD"][1].get(k, 0.0), money=False)
    print("  end-of-game market inventory (rises as either farm sells into the pool)")
    for k in sorted(set(B["inv"]) | set(C["inv"])):
        emit("inv " + k, B["inv"].get(k, 0.0), C["inv"].get(k, 0.0), money=False)

    if a.by_day:
        print("\nWAGE BILL BY DAY (realized)")
        days = sorted(set(B["WAGE_DAY"][0]) | set(C["WAGE_DAY"][0]))
        for d in days:
            emit(f"day {d:2d} wages", B["WAGE_DAY"][0].get(d, 0.0), C["WAGE_DAY"][0].get(d, 0.0))
            emit(f"day {d:2d} hires", B["HIRE_DAY"][0].get(d, 0.0), C["HIRE_DAY"][0].get(d, 0.0),
                 money=False)

    ours = C["L"][0].get("final", 0.0) - B["L"][0].get("final", 0.0)
    theirs = C["L"][1].get("final", 0.0) - B["L"][1].get("final", 0.0)
    wages_saved = B["L"][0].get("wages", 0.0) - C["L"][0].get("wages", 0.0)
    rev_delta = C["L"][0].get("revenue", 0.0) - B["L"][0].get("revenue", 0.0)
    print(f"\nSUMMARY   ours {ours:+,.0f}   opponent {theirs:+,.0f}   margin {ours - theirs:+,.0f}")
    cls = ("own-up/opponent-up (shared-market spillover)" if ours > 0 and theirs > 0 else
           "own-up/opponent-down (competitive gain)" if ours > 0 and theirs < 0 else
           "own-down (exploit or failure -- check margin)" if ours < 0 else "neutral")
    print(f"          class: {cls}")
    print(f"          wages saved {wages_saved:+,.0f}, revenue {rev_delta:+,.0f} "
          f"-> {wages_saved + rev_delta:+,.0f} of a {ours:+,.0f} own-money change; "
          f"remainder is other spend")


if __name__ == "__main__":
    main()
