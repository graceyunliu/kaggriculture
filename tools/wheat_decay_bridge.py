#!/usr/bin/env python3
"""Wheat harvest-window decay accounting bridge (ledger DELAY `crop_harvest_window_recoverability`).

Unlike an inferred-displacement analysis, the engine gives us the real answer directly: each unit
(farmer or hand) occupies a single (x,y) each turn and can only take ONE action there. So for every
WHEAT tile that decays to WEED, we can look at every turn a unit stood on that exact tile while it
still held yield_units>0, and read off literally what action the candidate chose to take instead of
HARVEST. That answers the bridge's four questions directly from the candidate's own decisions:

  expired tile -> was a unit ever there with the tile harvestable? (physical opportunity)
  -> what did the unit do instead that turn?              (the actual displacement, not a guess)
  -> units/revenue destroyed (peak yield_units, valued at last-seen WHEAT price -- context only)
  -> is the fix free (unit was idle/PASSing) or does it cost something real (unit was doing
     productive work elsewhere on the SAME tile, e.g. watering a tile that was never going to
     reach harvest again anyway)?

Classes recorded per decayed tile:
  NEVER_VISITED   -- no farmer/hand ever stood on this tile while it held yield_units>0. A pure
                     routing/dispatch gap: the tile was never in reach of the day's plan at all.
  VISITED_PASSED  -- a unit was on the tile with yield_units>0 at least once and took PASS (or an
                     action that isn't WATER/HARVEST) instead -- free to fix, no real displacement.
  VISITED_WATERED -- a unit was on the tile and chose WATER instead of HARVEST on a turn where
                     harvest was also available (yield_units>0). Watering a tile this late is not
                     obviously wrong (fertilizer/window logic may still want it) -- this is the
                     class that would need a real guardrail, not a free win, if promoted.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/wheat_decay_bridge.py candidates/O26_CARROT_SIZING.py \
    --opp Opponents/tape_bahaenes_106828159.py --seeds 11-30
"""
import sys, os, argparse, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me

CROP = "WHEAT"


def run(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    prev = None
    lives = {}   # pos -> life dict, tracking farm 0 (O26) only
    done = []
    last_price = None
    while True:
        acts = [None, None]
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {"farmer": ["PASS"], "hands": []}
            state[i].action = act
            acts[i] = act if isinstance(act, dict) else {"farmer": ["PASS"], "hands": []}

        # Build this turn's unit -> (pos, op) map for farm 0 BEFORE the engine applies actions,
        # using this turn's positions (units act from where they currently stand).
        o0 = state[0].observation
        farm0 = o0.farms[0]
        farmer_pos = tuple(farm0["farmer"])
        hand_positions = [tuple(p) for p in farm0["hands"]]
        farmer_act = acts[0].get("farmer", ["PASS"]) if isinstance(acts[0], dict) else ["PASS"]
        hands_acts = acts[0].get("hands", []) if isinstance(acts[0], dict) else []
        turn_ops_by_pos = collections.defaultdict(list)
        op0 = farmer_act[0] if isinstance(farmer_act, list) and farmer_act else "PASS"
        turn_ops_by_pos[farmer_pos].append(op0)
        for idx, hp in enumerate(hand_positions):
            ha = hands_acts[idx] if idx < len(hands_acts) else ["PASS"]
            hop = ha[0] if isinstance(ha, list) and ha else "PASS"
            turn_ops_by_pos[hp].append(hop)

        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation; day, hour = o.day, o.hour
        mkt = getattr(o, "market", None) or {}
        prices = mkt.get("prices") or {}
        if CROP in prices: last_price = prices[CROP]

        tiles = o.farms[0]["tiles"]
        pt = prev
        for y, row in enumerate(tiles):
            for x, t in enumerate(row):
                pos = (x, y)
                is_tracked = isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("crop") == CROP
                q = pt[y][x] if pt is not None else None
                was_tracked = isinstance(q, dict) and q.get("kind") == "PLANT" and q.get("crop") == CROP
                if is_tracked:
                    L = lives.get(pos)
                    if L is None or L["planted_day"] != t["planted_day"]:
                        if L is not None: done.append(L)
                        L = {"planted_day": t["planted_day"], "peak_yield": t.get("yield_units", 0),
                             "last_yield": t.get("yield_units", 0), "visits_with_yield": [],
                             "outcome": None}
                        lives[pos] = L
                    yu = t.get("yield_units", 0)
                    L["peak_yield"] = max(L["peak_yield"], yu)
                    L["last_yield"] = yu
                    # Was a unit standing HERE this turn (using pre-action positions) while
                    # yield_units was already >0 (i.e. harvest was a real option this turn)?
                    if yu > 0 and pos in turn_ops_by_pos:
                        for op in turn_ops_by_pos[pos]:
                            L["visits_with_yield"].append((op, yu))
                elif was_tracked and pos in lives:
                    L = lives.pop(pos)
                    if isinstance(t, dict) and t.get("kind") == "WEED":
                        L["outcome"] = "decayed_to_weed"
                    elif t is None:
                        L["outcome"] = "harvested"
                    else:
                        L["outcome"] = "replanted_over"
                    done.append(L)
        prev = [[dict(t) if isinstance(t, dict) else t for t in row] for row in tiles]
        if all(s.status == "DONE" for s in state) or step >= steps: break
    for L in list(lives.values()):
        L["outcome"] = "standing_at_end"; done.append(L)
    return done, last_price


WHEAT_MAX_YIELD = 6  # CROPS["WHEAT"]["max_yield"], vendor engine


def classify(L):
    if not L["visits_with_yield"]:
        return "NEVER_VISITED"
    ops = [op for op, yu in L["visits_with_yield"]]
    if "HARVEST" in ops:
        return "HARVESTED_SOME_THEN_LOST_REST"  # partial harvest happened, still decayed -- rare, worth a look
    if "WATER" in ops:
        # was every watering visit at/after max_yield already reached, i.e. objectively wasted
        # regardless of the wheat-decay question (engine caps yield at max_yield -- more watering
        # buys nothing)? If so, swapping WATER->HARVEST here costs nothing real.
        water_visits = [yu for op, yu in L["visits_with_yield"] if op == "WATER"]
        if all(yu >= WHEAT_MAX_YIELD for yu in water_visits):
            return "VISITED_WATERED_BUT_ALREADY_MAXED"  # free fix: watering there was already pointless
        return "VISITED_WATERED_BELOW_MAX"  # real tradeoff: watering was still adding yield
    return "VISITED_PASSED_OR_OTHER"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cand"); ap.add_argument("--opp", required=True); ap.add_argument("--seeds", default="11-30")
    a = ap.parse_args(); os.chdir(ROOT)
    lo, hi = map(int, a.seeds.split("-"))
    all_lives = []; last_price = None
    for s in range(lo, hi + 1):
        lives, px = run(a.cand, a.opp, s)
        all_lives.extend(lives)
        if px: last_price = px
    decayed = [L for L in all_lives if L["outcome"] == "decayed_to_weed"]
    n = len(all_lives)
    print(f"{os.path.basename(a.cand)} vs {os.path.basename(a.opp)}, seeds {a.seeds}: "
          f"{n} wheat plantings, {len(decayed)} decayed ({len(decayed)/n:.1%})" if n else "no plantings")
    by_class = collections.Counter(classify(L) for L in decayed)
    print("classification of decayed tiles (what the candidate actually did while the tile still had yield):")
    for cls, cnt in by_class.most_common():
        pct = cnt / len(decayed) * 100 if decayed else 0
        units = sum(L["peak_yield"] for L in decayed if classify(L) == cls)
        print(f"  {cls}: {cnt}/{len(decayed)} ({pct:.0f}%), {units} peak-yield units destroyed in this class")
    total_units = sum(L["peak_yield"] for L in decayed)
    px_str = f" (~${total_units*last_price:,.0f} at last-seen price ${last_price}/u, context only, not a realized-revenue claim)" if last_price else ""
    print(f"\ntotal peak-yield units destroyed across all decayed wheat tiles: {total_units}{px_str}")
    never = [L for L in decayed if classify(L) == "NEVER_VISITED"]
    if never:
        print(f"\nNEVER_VISITED is the true free-fix-candidate class -- a unit literally never reached the tile "
              f"while it held yield. {len(never)} tiles, {sum(L['peak_yield'] for L in never)} units. "
              f"These are the ones where 'harvest it before it decays' has zero displacement cost by definition "
              f"(no other work was happening there) -- ONLY if a unit could have been routed there in time, "
              f"which this tool does not yet check (routing-cost is a separate, harder question).")
    maxed = [L for L in decayed if classify(L) == "VISITED_WATERED_BUT_ALREADY_MAXED"]
    if maxed:
        print(f"\nVISITED_WATERED_BUT_ALREADY_MAXED is a SECOND free-fix class -- {len(maxed)} tiles, "
              f"{sum(L['peak_yield'] for L in maxed)} units. The candidate stood on the tile and chose WATER on "
              f"a turn when yield_units was already at WHEAT's max_yield (6) -- watering there bought nothing "
              f"(engine caps yield at max_yield) regardless of the decay question. Swapping that WATER for "
              f"HARVEST would have displaced a turn that was already worthless, so this recovery is free too.")
    below = [L for L in decayed if classify(L) == "VISITED_WATERED_BELOW_MAX"]
    if below:
        print(f"\nVISITED_WATERED_BELOW_MAX is the ONE real-tradeoff class -- {len(below)} tiles, "
              f"{sum(L['peak_yield'] for L in below)} units, where the candidate chose to keep growing this tile "
              f"(watering while still below max_yield) rather than harvest early for a smaller guaranteed amount. "
              f"This is the O30/O31-style tension: harvesting early here trades away future yield for certainty. "
              f"Any intervention should target only NEVER_VISITED + VISITED_WATERED_BUT_ALREADY_MAXED first (free "
              f"recoveries) and treat this class as needing its own dose-response / interior-optimum evidence "
              f"before touching it, per the threshold evidence contract.")
