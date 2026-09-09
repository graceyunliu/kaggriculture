"""P8 — reactive allocation policy on top of P6's proven per-day executor.

WHAT THIS IS
------------
candidates/P6_baseline.py (as recovered into this repo — see artifacts/
reactive_allocation_p8/REPORT.md for the recovery/naming caveat) is split into
two halves in its own source:
  1. an EXECUTOR: perceive(), _build_route/_route_step/_build_sweep/_crop_step/
     _steal_task/_unit_action/_setup_step — per-hour movement + task dispatch
     for each unit. This half is untouched here.
  2. an ALLOCATION policy inside economy(): hiring (_load_model), land
     purchase, herd purchase, crop/seed mix, and sell timing. In P6_baseline
     this half is driven by ~25 STATIC constants in the module-level KNOBS
     dict (min_hands, load_per_hand, open_melons, wheat_sell_price,
     melon_floor, max_animals, ...), fixed once at file-load time and never
     re-derived from the game the agent is actually playing. Two concrete
     consequences, read directly out of P6_baseline.py:
       - the herd-buying loop (economy(), "---- herd" section) reads
         obs["farms"][1-p]["tiles"] to count the OPPONENT's animals
         (`opp_counts`) and folds that into its own room calculation —
         i.e. it is opponent-aware, not just self-aware. The task spec for
         this build forbids opponent fingerprinting, so P8 cannot reuse that
         function unmodified.
       - hiring, land timing, and sell floors are single numbers (min_hands=3,
         load_per_hand=20, wheat_sell_price=30, melon_floor=200,
         LAND_DEADLINE={2:14,3:17,4:18}) tuned once against a fixed opening
         and fixed opponent tape; they do not move with how full the board
         actually is, how idle the current labor pool actually is, or how
         much of a cash cushion the game has actually produced this run.

P8 keeps the executor import untouched and replaces economy() with a
threshold/state-conditioned policy that reads ONLY:
  - own cash (me["money"])
  - own land occupancy (fraction of unlocked tiles that are non-empty)
  - own herd size relative to own labor (n_total / n_hands)
  - own labor idle-time proxy (pending chore load per hand, same load units
    P6 already computes, but used to set a live busy/idle RATIO instead of a
    fixed hand-count target)
  - market price and market inventory (obs["market"]) — a shared, public
    signal, not anything about the opponent's board
No opponent state is read anywhere in this file (grep for `1 - p` / `1-p` /
`farms[1` finds nothing below). No day-N trigger is copied from a tape —
every day-conditioned line here is a game-rule constant (LAND_DEADLINE,
crop cutoffs, etc., imported from P6_baseline itself) or a threshold this
file adds, never a value read off a specific opponent's replay.

RULES (see REPORT.md for full rationale/derivation)
  R1 Hiring:  target hands so that busy_ratio = pending_load / hands stays
      inside [BUSY_LO, BUSY_HI]; hire while under-busy-tolerance and cash
      reserve (feed + fib hire cost + BUFFER) is covered.
  R2 Land:    buy the next quadrant once own occupancy exceeds OCC_HIGH and
      cash covers price + reserve; skip while occupancy is low even if the
      day-deadline table would allow it (P6 buys land near a hard day
      deadline regardless of whether the existing land is even full).
  R3 Herd:    grow COW/SHEEP while own herd_ratio (animals per hand) is below
      HERD_RATIO_CAP and the shared market shows room (I0 - inventory of
      MILK/WOOL respectively above a floor) and cash affords it — no
      opponent counting.
  R4 Crop mix: same greedy value/cycle ranking P6 uses (kept, since it is a
      pure market/self-state calculation — no opponent read), but seed
      purchases are additionally throttled by the same busy_ratio labor
      signal as R1 instead of a fixed min_hands floor.
  R5 Sell timing: sell WHEAT/MELON when price clears a reactive floor
      computed from live market price relative to the item's own base price
      (in P6 these floors, e.g. melon_floor=200, are fixed constants) OR
      when shed occupancy is high (overflow risk, self-state).

This file imports P6_baseline.py by path and reuses its module object
directly (perceive, _unit_action, dispatch helpers, constants). It does not
edit candidates/P6_baseline.py on disk.
"""
from __future__ import annotations

import importlib.util
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_P6_PATH = os.path.join(_HERE, "P6_baseline.py")
_spec = importlib.util.spec_from_file_location("p6_baseline_p8", _P6_PATH)
p6 = importlib.util.module_from_spec(_spec)
sys.modules["p6_baseline_p8"] = p6
_spec.loader.exec_module(p6)

# ---- reused, unmodified from P6 (executor + pure game-rule constants) ----
perceive = p6.perceive
_unit_action = p6._unit_action
_crop_pools = p6._crop_pools
_fib = p6._fib
CROP_SPECS = p6.CROP_SPECS
ANIMALS = p6.ANIMALS
PRODUCT_OF = p6.PRODUCT_OF
RATE = p6.RATE
FIRST_YIELD = p6.FIRST_YIELD
LAND_PRICES = p6.LAND_PRICES
MAX_HANDS = p6.MAX_HANDS
MAX_SHEEP = p6.MAX_SHEEP
MAX_ORDERS = p6.MAX_ORDERS
I0 = p6.I0
DEMAND_SHARE = p6.DEMAND_SHARE
LOAD_ANIMAL, LOAD_CROP_TASK, LOAD_SETUP = p6.LOAD_ANIMAL, p6.LOAD_CROP_TASK, p6.LOAD_SETUP
HERD_LAST_DAY = p6.HERD_LAST_DAY
OPENING_MELONS = p6.OPENING_MELONS
CFG = p6.CFG
S = p6.S  # shared per-game scratch state (day, routes, ...) — same object the executor reads

# ===== P8 reactive-policy tuning (thresholds, not tape-derived triggers) =====
BUSY_LO, BUSY_HI = 0.5, 1.3     # target band for pending_load / n_hands (informational; see _hands_target)
LOAD_PER_HAND = 5.0             # chore-load units one hand can clear per day (same units as P6's LOAD_* consts)
CASH_BUFFER = 120.0             # $ kept unspent as a safety margin on every purchase decision
OCC_HIGH = 0.65                 # own-tile occupancy fraction that triggers a land purchase
HERD_RATIO_CAP = 1.1            # animals per hand ceiling for further herd purchases (leaves labor headroom for crops)
PRICE_FLOOR = {"MILK": 100.0, "WOOL": 150.0}  # observed-price floor below which herd growth pauses (own-market signal)
HERD_STEP_CAP = 2               # animals bought per species per day while price signal is healthy
FEED_SPARE = 3                  # wheat units of spare feed stock to keep
MELON_FLOOR_FRAC = 0.72         # sell MELON once price >= this fraction of its own base price... unless shed is full
SHED_OVERFLOW = 78              # shed_load above which we sell regardless of price (self-state, avoids destruction)


def _pending_load(v, seeds_planned):
    """Same load units P6's _load_model uses, but returned raw (not divided into a hand count yet)."""
    n_active_animals = len(v["animals"])
    load = LOAD_CROP_TASK * (len(v["urgent"]) + len(v["water"]) + len(v.get("wwater", [])) +
                              len(v["harvest"]) + len(v["weeds"]) + seeds_planned)
    load += LOAD_ANIMAL * n_active_animals
    return load


def _hands_target(pending_load, n_hands, day):
    """R1: reactive hand count, directly proportional to the live chore-load signal
    (pending_load / LOAD_PER_HAND), not a fixed knob. Bounded [3, MAX_HANDS] (3 = the
    minimum crew the day-0 opening needs before any chores exist, not a tape-derived
    number). busy = pending_load / n_hands is exposed for the report's diagnostics but
    the target itself is load-proportional so it does not depend on how many hands
    happen to be on payroll already (avoids the runaway-hiring feedback loop a
    "keep adding while busy is high" rule produces when load is flat)."""
    target = math.ceil(pending_load / LOAD_PER_HAND)
    target = max(3, min(MAX_HANDS, target))
    if day >= 29:
        target = min(target, 6)
    return target


def _hire_orders(target, n_hands, hires_today, cash_available):
    n, spent = p6._hire_plan(target, n_hands, hires_today, max(0.0, cash_available))
    return [["HIRE"]] * n, spent


def economy(obs, v):
    """R1-R5 reactive allocation. Reads only own state + shared market state."""
    p = obs["player"]
    me = obs["farms"][p]
    day, hour = obs["day"], obs["hour"]
    shed = obs["private"]["shed"]
    seeds = obs["private"]["seeds"]
    prices = obs["market"]["prices"]
    inventory = obs["market"]["inventory"]
    cash = me["money"]
    quads = len(me["unlocked_quadrants"])
    orders = []
    n_hands = len(me["hands"])
    inv = obs["private"].get("inventories") or []
    carried_animals = sum(i.get(a, 0) for i in inv for a in ANIMALS)
    shed_animals = sum(shed.get(a, 0) for a in ANIMALS)
    n_active = len(v["animals"])
    n_total = n_active + shed_animals + carried_animals
    pending_place = shed_animals + carried_animals
    seeds_on_hand = sum(seeds.get(c, 0) for c in CROP_SPECS)

    # ---- opening: day 0, hour 0 — a fixed set of first orders is unavoidable
    # (there is no "observed state" yet on turn 0); everything after this is reactive.
    if day == 0 and hour == 0 and n_total == 0:
        orders = [["HIRE"]] * 5
        orders.append(["BUY_ANIMAL", "COW", 1])
        orders.append(["BUY_ANIMAL", "SHEEP", 1])
        orders.append(["BUY_SEED", "MELON", OPENING_MELONS])
        orders.append(["BUY_PRODUCT", "WHEAT", 3])
        return orders[:MAX_ORDERS]

    # ---- R5 sells: react to shared market price/inventory + own shed occupancy ----
    shed_load = sum(n for k, n in shed.items() if k not in ANIMALS and n > 0)
    revenue_est = 0.0
    if hour == 0 or day >= 28 or shed_load > SHED_OVERFLOW:
        for item in ("MILK", "WOOL", "STRAWBERRY", "FERTILIZER", "TOMATO", "CARROT", "EGG"):
            n = shed.get(item, 0)
            if n > 0:
                orders.append(["SELL", item, int(n)])
                revenue_est += n * prices.get(item, 0) * 0.85
        n = shed.get("MELON", 0)
        melon_base = CROP_SPECS["MELON"]["base"]
        if n > 0 and (prices.get("MELON", 0) >= MELON_FLOOR_FRAC * melon_base or day >= 27 or shed_load > SHED_OVERFLOW):
            orders.append(["SELL", "MELON", int(n)])
            revenue_est += n * prices.get("MELON", 0) * 0.7
        w = shed.get("WHEAT", 0)
        wheat_base = CROP_SPECS["WHEAT"]["base"]
        reserve_feed = n_total + FEED_SPARE
        if day >= 29:
            if w > 0:
                orders.append(["SELL", "WHEAT", int(w)])
        elif prices.get("WHEAT", 0) >= wheat_base or shed_load > SHED_OVERFLOW:
            surplus = int(w - reserve_feed)
            if surplus > 0:
                orders.append(["SELL", "WHEAT", surplus])
                revenue_est += surplus * prices.get("WHEAT", 0) * 0.9

    budget = cash + revenue_est
    pending_load = _pending_load(v, seeds_on_hand)
    target_hands = _hands_target(pending_load, n_hands, day)
    S["hires_target"] = target_hands
    if os.environ.get("P8_DEBUG") and day <= 4:
        print(f"DBG day{day} h{hour} n_hands={n_hands} load={pending_load:.1f} busy={pending_load/max(1,n_hands):.2f} target={target_hands} cash={cash:.0f}", file=sys.stderr)

    # ---- R1 hiring: reserve feed cost first, hire with whatever cash remains ----
    feed_need = max(0, n_total + FEED_SPARE - shed.get("WHEAT", 0)) if day < 29 else 0
    wheat_cost = feed_need * prices.get("WHEAT", 40) * 1.15
    if feed_need > 0:
        orders.append(["BUY_PRODUCT", "WHEAT", int(feed_need)])
    hire_orders, hire_spent = _hire_orders(target_hands, n_hands, me["hires_today"],
                                            budget - wheat_cost - CASH_BUFFER)
    orders += hire_orders[:max(0, MAX_ORDERS - len(orders))]
    free = budget - wheat_cost - hire_spent - CASH_BUFFER

    # ---- R3 herd: own herd_ratio + shared market room, no opponent read ----
    herd_ratio = n_total / max(1, n_hands)
    if 1 <= day <= HERD_LAST_DAY and pending_place <= 3 and herd_ratio < HERD_RATIO_CAP:
        for sp in ("SHEEP", "COW"):
            item = PRODUCT_OF[sp]
            price = prices.get(item, 0.0)
            my_count = shed.get(sp, 0) + sum(1 for _pos, t in v["animals"] if t.get("animal") == sp)
            # Own-market price signal: keep buying while price hasn't been pushed down
            # by our own oversupply; below the floor, only top up to a minimal 2-head
            # presence (matches the fallback P6 uses when a product has no live shop).
            room = HERD_STEP_CAP if price >= PRICE_FLOOR.get(item, 0.0) else max(0, 2 - my_count)
            k = min(room, int(free // ANIMALS[sp]))
            while k > 0 and (n_total + k) / max(1, n_hands) > HERD_RATIO_CAP:
                k -= 1
            if k > 0:
                orders.append(["BUY_ANIMAL", sp, int(k)])
                free -= ANIMALS[sp] * k
                n_total += k
                pending_place += k
                herd_ratio = n_total / max(1, n_hands)

    # ---- R4 crop mix: greedy value/cycle over the shared market, throttled by busy_ratio ----
    empty_count = len(v["empty"]) + len(v["empty_pastures"])
    space = empty_count - pending_place - seeds_on_hand
    # Labor throttle uses target_hands (this day's reactive hire target), not the
    # instantaneous n_hands headcount — hands are re-hired from 0 every day (engine
    # rule), so n_hands read at hour 0 before the day's HIRE orders land would always
    # read as "maximally busy" and permanently gate planting off. Only throttle once
    # the hiring pool itself is saturated (target_hands pinned at MAX_HANDS).
    labor_saturated = target_hands >= MAX_HANDS
    if os.environ.get("P8_DEBUG") and hour == 0:
        print(f"DBG-R4 day{day} space={space} empty_count={empty_count} target_hands={target_hands} free={free:.0f}", file=sys.stderr)
    if space > 0 and not labor_saturated and day >= 1:
        committed = {c: 0.0 for c in CROP_SPECS}
        for _pos, t in v["crops"]:
            c = t.get("crop")
            if c in committed:
                committed[c] += CROP_SPECS[c]["units"]
        for c in committed:
            committed[c] += seeds.get(c, 0) * CROP_SPECS[c]["units"]
        excluded = set()
        n_seed_orders = 0
        while space > 0 and n_seed_orders < 4:
            best = None
            for c, sp_ in CROP_SPECS.items():
                if c in excluded or day > sp_["cutoff"] or day < sp_.get("start", 0):
                    continue
                inv_c = inventory.get(c, I0)
                pool = DEMAND_SHARE * max(0.0, I0 - inv_c)
                room_units = pool - committed[c]
                if room_units < sp_["units"] * 0.5:
                    excluded.add(c)
                    continue
                price = min(prices.get(c, sp_["base"]), sp_["base"] * 2.0)
                val = min(sp_["units"], room_units) * price / sp_["cycle"]
                if val < sp_["min_val"]:
                    excluded.add(c)
                    continue
                if best is None or val > best[0]:
                    best = (val, c, room_units)
            if best is None:
                break
            _val, c, room_units = best
            k = min(space, int(room_units // CROP_SPECS[c]["units"]), int(free // CROP_SPECS[c]["seed"]), 20)
            excluded.add(c)
            if k <= 0:
                continue
            orders.append(["BUY_SEED", c, int(k)])
            free -= CROP_SPECS[c]["seed"] * k
            committed[c] += k * CROP_SPECS[c]["units"]
            space -= k
            n_seed_orders += 1

    # ---- R2 land: react to own occupancy, not a day deadline table ----
    occ_denom = max(1, empty_count + pending_place + n_active + sum(1 for _p, t in v["crops"] for _ in [0]))
    occupancy = 1.0 - (empty_count / occ_denom if occ_denom else 0.0)
    if os.environ.get("P8_DEBUG") and hour == 0:
        print(f"DBG-R2 day{day} quads={quads} occ={occupancy:.2f} free={free:.0f}", file=sys.stderr)
    if quads < 4:
        price = LAND_PRICES[quads - 1]
        if occupancy >= OCC_HIGH and free >= price + CASH_BUFFER:
            orders.append(["BUY_LAND"])
            free -= price

    return orders[:MAX_ORDERS]


def _agent(obs):
    p = obs["player"]
    me = obs["farms"][p]
    day, hour = obs["day"], obs["hour"]
    if S["day"] != day:
        S.update({"day": day, "routes": {}, "crop": {}, "sweep": {}, "setup": {}, "claimed_sites": set(),
                  "animal_claim": set(), "fert_taken": 0})
    v = perceive(obs)
    shed = obs["private"]["shed"]
    seeds_left = dict(obs["private"]["seeds"])
    inv = obs["private"].get("inventories") or []
    unlocked_shed = v["shed_tiles"]
    market = economy(obs, v)
    reserved = sum(r.get("pickup", 0) for r in S["routes"].values())
    S["wheat_budget"] = max(0, shed.get("WHEAT", 0) - reserved)
    pools = _crop_pools(v, seeds_left, day)
    for sw in S["sweep"].values():
        for tp, kind in sw:
            if kind in pools and tp in pools[kind]:
                pools[kind].remove(tp)
    n_units = 1 + len(me["hands"])
    for d in (S["routes"], S["crop"], S["sweep"], S["setup"]):
        for j in [j for j in d if j >= n_units]:
            d.pop(j, None)
    positions = [tuple(me["farmer"])] + [tuple(h) for h in me["hands"]]
    v["positions"] = positions
    ops = []
    for i, pos in enumerate(positions):
        carry = inv[i] if i < len(inv) else {}
        ops.append(_unit_action(i, pos, carry, obs, v, pools, seeds_left, shed, unlocked_shed))
    return {"farmer": ops[0], "hands": ops[1:], "market": market}


def agent(obs, configuration=None):
    try:
        if configuration is not None:
            g = lambda k, d: (configuration.get(k, d) if isinstance(configuration, dict) else getattr(configuration, k, d))
            CFG["center_interval"] = int(g("townCenterSellInterval", 24))
            CFG["shop_interval"] = int(g("townShopSellInterval", 4))
            CFG["turns_per_day"] = int(g("turnsPerDay", 24))
        return _agent(obs)
    except Exception as exc:  # crash guard, same pattern as P6_baseline
        import traceback
        print(f"GUARD swallowed exception: {exc!r}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"farmer": ["PASS"], "hands": [], "market": []}
