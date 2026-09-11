#!/usr/bin/env python3
"""Non-ongoing crop harvest-window / lifespan-decay trace (Sep 11, ledger DELAY
`crop_harvest_window_recoverability`).

For WHEAT, CARROT, MELON (engine CROPS[...]["ongoing"] == False), each planting's tile dict carries
max_lifespan_step, fixed at plant time: (planted_day + max_yield_day + 1) * turns_per_day. Before that
step the tile only grows (watering during the [ (max_yield_day+1)//2 , max_yield_day ] age-day window
adds yield, capped at max_yield); at/after that step, _decay_plants removes 1 yield_unit every 2 steps
until yield_units<=0, at which point the tile becomes {"kind": "WEED"} outright -- a hard, irreversible
loss of whatever units were still standing. HARVEST (any time yield_units>0) clears the tile to None
and banks the units; a harvested tile cannot decay (it no longer exists).

Because yield_units is set to 1 at planting and never decreases before decay begins, every non-ongoing
planting is technically harvestable (yield_units>0) from the moment it is planted. So the accounting
split this tool exists to make is NOT "was it ever harvestable" (that is close to always true by
construction) but:

  (1) RATE-1 -- decayed to WEED at all (a real, irreversible loss of whatever units were standing
      when the last decay tick zeroed it out) -- this is a genuine scheduling/dispatch failure, since
      the tile was reachable and holding positive yield_units for its entire life up to that point.
  (2) RATE-2 -- decayed with only the planting-time base unit (yield_units==1) never having grown at
all, i.e. it was never watered during its growth window either -- a compounding failure (missed
      water AND missed harvest) rather than a case where growth was captured but harvest wasn't.
  (3) units/revenue actually lost to decay (yield_units destroyed, valued at the last observed market
      price for that product, as an order-of-magnitude estimate -- NOT a claim about realized revenue).

This tool does NOT attempt question 5 from the audit (what would protecting the tile displace) --
that requires an allocation-cost comparison against a parent policy (the o31_decompose.py /
allocation_matrix.py pattern) and is deliberately deferred until (1)-(3) show a non-trivial prize,
per the ledger's would_do/would_abandon gate.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/crop_window_trace.py candidates/O26_CARROT_SIZING.py \
    --opp Opponents/tape_bahaenes_106828159.py --seeds 11-14 --crop WHEAT,CARROT,MELON
"""
import sys, os, argparse, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me

NON_ONGOING = ("WHEAT", "CARROT", "MELON")


def run(cand, opp, seed, crops):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    turns_per_day = int(cfg.get("turnsPerDay", 24))
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    prev = [None, None]
    lives = [{}, {}]     # pos -> life dict, keyed while a tracked crop occupies it
    done = [[], []]       # finished lives (harvested / decayed / standing_at_end)
    last_price = {}      # crop -> most recent observed market price (context only, not a revenue claim)
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation; day, hour = o.day, o.hour
        mkt = getattr(o, "market", None) or {}
        prices = mkt.get("prices") or {}
        for c in crops:
            if c in prices: last_price[c] = prices[c]
        for p in range(2):
            tiles = o.farms[p]["tiles"]
            pt = prev[p]
            for y, row in enumerate(tiles):
                for x, t in enumerate(row):
                    pos = (x, y)
                    is_tracked = isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("crop") in crops
                    q = pt[y][x] if pt is not None else None
                    was_tracked = isinstance(q, dict) and q.get("kind") == "PLANT" and q.get("crop") in crops
                    if is_tracked:
                        L = lives[p].get(pos)
                        if L is None or L["planted_day"] != t["planted_day"]:
                            if L is not None: done[p].append(L)
                            L = {"crop": t["crop"], "planted_day": t["planted_day"], "planted_step": step,
                                 "max_lifespan_step": t["max_lifespan_step"], "ever_watered": False,
                                 "peak_yield": t.get("yield_units", 0), "last_yield": t.get("yield_units", 0),
                                 "outcome": None, "outcome_step": None, "units_at_outcome": None}
                            lives[p][pos] = L
                        if t.get("watered_today"):
                            L["ever_watered"] = True
                        yu = t.get("yield_units", 0)
                        L["peak_yield"] = max(L["peak_yield"], yu)
                        L["last_yield"] = yu
                    elif was_tracked and pos in lives[p]:
                        L = lives[p].pop(pos)
                        if isinstance(t, dict) and t.get("kind") == "WEED":
                            L["outcome"] = "decayed_to_weed"; L["units_at_outcome"] = 0  # decay always ends at yield<=0
                        elif t is None:
                            # HARVEST clears a non-ongoing tile to None and banks whatever yield_units it held.
                            L["outcome"] = "harvested"; L["units_at_outcome"] = L["last_yield"]
                        else:
                            L["outcome"] = "replanted_over"; L["units_at_outcome"] = L["last_yield"]
                        L["outcome_step"] = step
                        done[p].append(L)
            prev[p] = [[dict(t) if isinstance(t, dict) else t for t in row] for row in tiles]
        if all(s.status == "DONE" for s in state) or step >= steps: break
    for p in range(2):
        for L in list(lives[p].values()):
            L["outcome"] = "standing_at_end"; L["units_at_outcome"] = L["last_yield"]; L["outcome_step"] = step
            done[p].append(L)
    return done, last_price, turns_per_day


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cand"); ap.add_argument("--opp", required=True); ap.add_argument("--seeds", default="11-14")
    ap.add_argument("--crop", default=",".join(NON_ONGOING))
    a = ap.parse_args(); os.chdir(ROOT)
    crops = tuple(c.strip().upper() for c in a.crop.split(",") if c.strip())
    lo, hi = map(int, a.seeds.split("-"))
    names = [os.path.basename(a.cand), os.path.basename(a.opp)]
    agg = [[], []]; last_price_seen = {}
    for s in range(lo, hi + 1):
        d, lp, tpd = run(a.cand, a.opp, s, crops)
        for p in range(2): agg[p].extend(d[p])
        last_price_seen.update(lp)
    for p in range(2):
        lives = agg[p]
        n = len(lives)
        if n == 0:
            print(f"{names[p]}: no {'/'.join(crops)} plantings"); continue
        print(f"\n=== {names[p]}: {n} plantings across {'/'.join(crops)} ===")
        for crop in crops:
            cl = [L for L in lives if L["crop"] == crop]
            if not cl: continue
            nc = len(cl)
            by_outcome = collections.Counter(L["outcome"] for L in cl)
            decayed = [L for L in cl if L["outcome"] == "decayed_to_weed"]
            never_grown_decayed = [L for L in decayed if not L["ever_watered"]]
            harvested = [L for L in cl if L["outcome"] == "harvested"]
            avg_harvest_units = (sum(L["units_at_outcome"] for L in harvested) / len(harvested)) if harvested else 0.0
            # value destroyed by decay = the yield still standing right before the tile flipped to WEED
            # (peak_yield reached, since decay only ever subtracts -- this is the last positive level, an
            # upper bound on what a same-day harvest right before decay-completion could still have banked)
            units_destroyed = sum(L["peak_yield"] for L in decayed)
            px = last_price_seen.get(crop)
            print(f"  {crop}: {nc} plantings -- outcomes {dict(by_outcome)}")
            print(f"    RATE-1 (decayed to WEED, any growth level): {len(decayed)}/{nc} ({len(decayed)/nc:.0%})")
            print(f"    RATE-2 (decayed AND never watered -- base unit only, compounding miss): "
                  f"{len(never_grown_decayed)}/{nc} ({len(never_grown_decayed)/nc:.0%})")
            print(f"    harvested: {len(harvested)}/{nc} ({len(harvested)/nc:.0%}), avg {avg_harvest_units:.2f} units/harvest")
            if decayed:
                print(f"    units destroyed by decay (sum of peak yield_units at each decayed tile, upper-bound "
                      f"estimate): {units_destroyed} units" + (f" (~${units_destroyed*px:,.0f} at last-seen price ${px}/u, "
                      f"context only -- not a realized-revenue claim)" if px else ""))
