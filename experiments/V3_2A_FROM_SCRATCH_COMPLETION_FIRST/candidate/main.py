"""
V3_2A_FROM_SCRATCH_COMPLETION_FIRST -- Kaggriculture agent.

Written entirely FROM SCRATCH: own state tracking, own dispatcher, own
economy rules. Only the action-schema SHAPE (dict with "farmer"/"hands"/
"market" keys; market order verbs BUY_LAND/BUY_SEED/HIRE/SELL/BUY_PRODUCT;
unit verbs WATER/HARVEST/PLANT/DIG/PICKUP/PLACE/NORTH.../PASS) and the raw
engine facts (seed/land/hand costs, crop cycle times, market base prices)
were read from kaggriculture.py / V10.6 purely for compatibility -- none
of V10.6's or the real opponent's priority scoring, gating formulas, or
dispatch algorithms are reused.

REGIME: COMPLETION-FIRST ECONOMY.

Thesis: from day 1, only invest in NEW capacity (land / hands) once the
CURRENT production commitment (the batch of tiles planted since the last
investment event) is mostly harvested-and-sold, not left growing. Once
capital is committed to a batch, the agent finishes that batch before
expanding again. This is the mirror image of V3_0N's liquidity-first
regime (REJECTED: -$135k/game -- delaying investment to day 15 left too
little runway for premium crops to mature) -- here investment starts
immediately on day 1 (never delayed), but each investment step is
individually GATED on completion of the prior one, and every crop
planting is horizon-checked against day 30 using the crop's real cycle
time. See docs/V3_2A_FROM_SCRATCH_COMPLETION_FIRST.md for full spec.

Animal purchase/placement is OUT OF SCOPE (documented limitation, same
precedent as V3_0N): a full pickup/carry/place state machine for
COW/SHEEP/GOOSE is a separate engineering task; all capital here routes
to land, hands, and crop seed so the completion-gating mechanism itself
is tested cleanly without confounding it with an animal-placement bug.
"""

import sys

# ---------------------------------------------------------------------
# ENGINE FACTS (not strategy) -- read from kaggriculture.py.
# ---------------------------------------------------------------------
CENTER_TILES = [(4, 4), (4, 5), (5, 4), (5, 5)]
I0 = 10_000
MAX_MARKET_ORDERS = 10
LIQUIDATE_DAY = 28
HORIZON_DAY = 30          # episode ends at day 30 (episodeSteps=720, 24h/day)
SELL_BUFFER = 1           # want the crop sellable with >=1 day to spare

# crop: seed cost, first_yield_day, max_yield_day, interval, max_yield, ongoing
CROPS = {
    "WHEAT":      {"seed": 10,  "first": 2,  "max_day": 4,  "interval": 0, "max_yield": 6, "ongoing": False},
    "CARROT":     {"seed": 20,  "first": 2,  "max_day": 3,  "interval": 0, "max_yield": 4, "ongoing": False},
    "TOMATO":     {"seed": 50,  "first": 8,  "max_day": 8,  "interval": 1, "max_yield": 4, "ongoing": True},
    "STRAWBERRY": {"seed": 100, "first": 10, "max_day": 10, "interval": 2, "max_yield": 4, "ongoing": True},
    "MELON":      {"seed": 80,  "first": 10, "max_day": 12, "interval": 0, "max_yield": 6, "ongoing": False},
}
MARKET_BASE = {
    "WHEAT": 25, "CARROT": 35, "TOMATO": 60, "STRAWBERRY": 120, "MELON": 250,
    "EGG": 50, "MILK": 160, "WOOL": 200, "FERTILIZER": 100,
}
LAND_COST_BY_QUADS = {1: 1000, 2: 2000, 3: 4000}
FARM_HAND_COST_MULT = 1

# ---------------------------------------------------------------------
# REGIME PARAMETERS -- from first principles, not tuned against either
# V10.6 or the opponent.
# ---------------------------------------------------------------------
COMPLETION_THRESHOLD = 0.65   # fraction of the committed batch that must be
                              # harvested+sold before the NEXT investment fires
CROP_ORDER = ["WHEAT", "CARROT", "MELON", "TOMATO", "STRAWBERRY"]
SEED_TARGET_PER_CROP = 10
CASH_RESERVE = 250
MAX_HANDS_PER_INVEST_STEP = 2
HAND_CEILING = 12


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def _dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _step_toward(pos, target):
    x, y = pos
    tx, ty = target
    if x < tx:
        return "EAST"
    if x > tx:
        return "WEST"
    if y < ty:
        return "SOUTH"
    if y > ty:
        return "NORTH"
    return None


def _nearest_center(pos):
    return min(CENTER_TILES, key=lambda c: _dist(pos, c))


def _nearest(pos, targets):
    if not targets:
        return None
    return min(targets, key=lambda t: _dist(pos, t))


def crop_fits_horizon(crop, day):
    """Horizon-awareness: never start a crop cycle that cannot mature AND
    be sold before day 30, using the crop's real cycle time.
    - One-time crops (WHEAT/CARROT/MELON): need day + first_yield_day to
      leave at least SELL_BUFFER days before HORIZON_DAY to harvest+sell.
    - Ongoing crops (TOMATO/STRAWBERRY): need day + first_yield_day to
      leave enough room for at least one harvest+sell cycle.
    """
    c = CROPS[crop]
    return day + c["first"] + SELL_BUFFER <= HORIZON_DAY


# ---------------------------------------------------------------------
# PRODUCTION-CHAIN STATE TRACKING (persists across turns via module
# globals -- kaggle_environments re-imports/re-instantiates the agent
# module fresh per game process in this harness, so this is safe and is
# the same pattern other from-scratch experiments in this repo use for
# per-episode state).
# ---------------------------------------------------------------------
STATE = {
    "batch_planted": 0,     # tiles planted since the last investment event
    "batch_harvested_sold": 0,  # of those, how many have been harvested+sold
    "batch_open": False,    # whether we are currently mid-batch (have any
                             # unresolved planted tiles from the last invest)
    "last_seed_counts": {},  # crop -> seed count last turn, to detect PLANT actions indirectly
    "sold_this_batch_by_crop": {},
    "initialized": False,
}


def _completion_ratio():
    if STATE["batch_planted"] <= 0:
        return 1.0  # nothing committed yet -- treat as "fully complete", i.e. free to invest
    return STATE["batch_harvested_sold"] / STATE["batch_planted"]


def _investment_gate_ok():
    """Gating formula: allow new investment (BUY_LAND / HIRE) only when
    completion_ratio(current batch) >= COMPLETION_THRESHOLD, i.e. the
    tiles committed under the last investment are mostly
    harvested-and-sold, not left growing."""
    return _completion_ratio() >= COMPLETION_THRESHOLD


def _open_new_batch(n_new_tiles):
    """Called at an investment event: start tracking a fresh batch sized
    to the tiles we intend to plant with the new capacity."""
    STATE["batch_planted"] = max(1, n_new_tiles)
    STATE["batch_harvested_sold"] = 0
    STATE["batch_open"] = True


# ---------------------------------------------------------------------
# PERCEPTION -- scan own tiles into simple task buckets, and update the
# completion-tracking state from real board observations (planted tiles,
# harvested/sold quantities) rather than guessing.
# ---------------------------------------------------------------------
def scan(me, day):
    empty, water, urgent_water, harvest, weeds = [], [], [], [], []
    planted_total = 0
    harvested_ready_or_done = 0
    for row in me["tiles"]:
        for t in row:
            if t is None:
                continue
            if not isinstance(t, dict):
                continue
            kind = t.get("kind")
            if kind == "PLANT":
                planted_total += 1
                c = CROPS.get(t.get("crop"))
                if c:
                    age = day - t.get("planted_day", day)
                    yu = t.get("yield_units", 0)
                    ready = c["ongoing"] or (age >= c["first"] and
                            (yu >= c["max_yield"] or age >= c["max_day"]))
                    if yu > 0 and ready:
                        harvest.append((t))
                    if age >= c["max_day"] and not c["ongoing"]:
                        harvested_ready_or_done += 1  # cycle finished (harvested or expired)
    for y, row in enumerate(me["tiles"]):
        for x, t in enumerate(row):
            pos = (x, y)
            if t is None:
                empty.append(pos)
                continue
            if not isinstance(t, dict):
                continue
            kind = t.get("kind")
            if kind == "WEED":
                weeds.append(pos)
            elif kind == "PLANT":
                if not t.get("watered_today", False):
                    if t.get("consecutive_unwatered", 0) >= 1:
                        urgent_water.append(pos)
                    else:
                        water.append(pos)
                c = CROPS.get(t.get("crop"))
                if c:
                    age = day - t.get("planted_day", day)
                    yu = t.get("yield_units", 0)
                    ready = c["ongoing"] or (age >= c["first"] and
                            (yu >= c["max_yield"] or age >= c["max_day"]))
                    if yu > 0 and ready:
                        harvest.append(pos)
    return {
        "empty": empty, "water": water, "urgent_water": urgent_water,
        "harvest": harvest, "weeds": weeds,
        "planted_total": planted_total,
    }


def plantable_now(seeds, day):
    out = []
    for c in CROP_ORDER:
        if seeds.get(c, 0) > 0 and crop_fits_horizon(c, day):
            out.append(c)
    return out


# ---------------------------------------------------------------------
# UNIT DISPATCH -- simple sequential nearest-task assignment.
# ---------------------------------------------------------------------
def unit_op(pos, view, seeds, day, shed, carry):
    carried_products = {k: carry.get(k, 0) for k in ("MILK", "WOOL", "EGG", "FERTILIZER") if carry.get(k, 0) > 0}
    if carried_products and sum(carried_products.values()) >= 3:
        if pos in CENTER_TILES:
            item = max(carried_products, key=carried_products.get)
            return ["PLACE", item, carried_products[item]]
        step = _step_toward(pos, _nearest_center(pos))
        if step:
            return [step]

    for key, act in (("urgent_water", "WATER"), ("harvest", "HARVEST"), ("water", "WATER")):
        lst = view[key]
        if pos in lst:
            lst.remove(pos)
            if act == "HARVEST":
                STATE["_harvest_events_this_turn"] = STATE.get("_harvest_events_this_turn", 0) + 1
            return [act]
    if pos in view["empty"]:
        cands = plantable_now(seeds, day)
        if cands:
            crop = cands[0]
            seeds[crop] -= 1
            view["empty"].remove(pos)
            view["urgent_water"].append(pos)
            STATE["_plant_events_this_turn"] = STATE.get("_plant_events_this_turn", 0) + 1
            return ["PLANT", crop]
    if pos in view["weeds"]:
        view["weeds"].remove(pos)
        return ["DIG"]

    for key in ("urgent_water", "harvest", "water", "weeds"):
        tgt = _nearest(pos, view[key])
        if tgt:
            step = _step_toward(pos, tgt)
            if step:
                return [step]
    if plantable_now(seeds, day):
        tgt = _nearest(pos, view["empty"])
        if tgt:
            step = _step_toward(pos, tgt)
            if step:
                return [step]

    return ["PASS"]


def _agent(obs):
    p = obs["player"]
    me = obs["farms"][p]
    day, hour = obs["day"], obs["hour"]
    seeds = dict(obs["private"]["seeds"])
    shed = obs["private"]["shed"]
    inventories = obs["private"].get("inventories") or []
    farmer_carry = inventories[0] if inventories else {}
    inv = obs["market"]["inventory"]

    view = scan(me, day)
    quads = len(me["unlocked_quadrants"])
    n_hands = len(me["hands"])

    orders = []
    budget = me["money"]

    STATE["_harvest_events_this_turn"] = 0
    STATE["_plant_events_this_turn"] = 0

    # --- Update completion tracking from real observed sells this turn:
    # we approximate "harvested_sold" progress by counting SELL orders
    # issued this turn for crop items (a sale is the true completion
    # event for a tile's production chain, not merely harvest-to-shed).
    sellable = [(item, n) for item, n in shed.items()
                if isinstance(n, (int, float)) and n > 0 and item in CROPS]
    sell_units_this_turn = 0
    for item, n in sorted(sellable, key=lambda kv: -MARKET_BASE.get(kv[0], 0)):
        if len(orders) >= MAX_MARKET_ORDERS:
            break
        price_signal = inv.get(item, I0)
        if day >= LIQUIDATE_DAY or price_signal <= I0:
            qty = int(n)
        else:
            qty = int(n * 0.6)
        if qty > 0:
            orders.append(["SELL", item, qty])
            sell_units_this_turn += qty

    if STATE["batch_open"] and sell_units_this_turn > 0:
        STATE["batch_harvested_sold"] = min(
            STATE["batch_planted"],
            STATE["batch_harvested_sold"] + sell_units_this_turn,
        )
        if STATE["batch_harvested_sold"] >= STATE["batch_planted"]:
            STATE["batch_open"] = False

    # Also sell non-crop shed items (fertilizer etc) opportunistically --
    # doesn't affect completion tracking (not part of a planted batch).
    other_sellable = [(item, n) for item, n in shed.items()
                       if isinstance(n, (int, float)) and n > 0
                       and item not in CROPS and item not in ("COW", "SHEEP", "GOOSE")]
    for item, n in sorted(other_sellable, key=lambda kv: -MARKET_BASE.get(kv[0], 0)):
        if len(orders) >= MAX_MARKET_ORDERS:
            break
        if MARKET_BASE.get(item) is None:
            continue
        qty = int(n)
        if qty > 0:
            orders.append(["SELL", item, qty])

    gate_ok = _investment_gate_ok()

    # --- Investment: BUY_LAND, gated on completion ratio + horizon
    # (never expand so late there's no runway left to work the new land).
    if gate_ok and quads < 4 and day <= 24 and len(orders) < MAX_MARKET_ORDERS:
        land_cost = LAND_COST_BY_QUADS.get(quads, 4000)
        if budget - land_cost >= CASH_RESERVE:
            orders.append(["BUY_LAND"])
            budget -= land_cost
            _open_new_batch(n_new_tiles=16)  # a new quadrant is ~16 tiles

    # --- Investment: HIRE, gated the same way, small step size so each
    # hire is its own completable increment rather than a lump purchase.
    if gate_ok and hour == 0 and n_hands < HAND_CEILING and day <= 27 and len(orders) < MAX_MARKET_ORDERS:
        hires = 0
        while (hires < MAX_HANDS_PER_INVEST_STEP and n_hands + hires < HAND_CEILING
               and len(orders) < MAX_MARKET_ORDERS):
            cost = FARM_HAND_COST_MULT * _fib(n_hands + hires)
            if budget - cost < CASH_RESERVE:
                break
            orders.append(["HIRE"])
            budget -= cost
            hires += 1
        if hires > 0:
            # a new hand's marginal capacity is roughly a few extra tiles
            # of throughput per cycle -- treat it as opening a small batch
            # only if no batch is currently open (avoid double-gating).
            if not STATE["batch_open"]:
                _open_new_batch(n_new_tiles=6 * hires)

    # --- Crop seed purchasing: always allowed (not "new capacity", it's
    # working capital for tiles we already have), but every crop is
    # horizon-checked so we never start a cycle that can't finish.
    for crop in CROP_ORDER:
        if len(orders) >= MAX_MARKET_ORDERS:
            break
        if not crop_fits_horizon(crop, day):
            continue
        have = seeds.get(crop, 0)
        if have < SEED_TARGET_PER_CROP:
            k = SEED_TARGET_PER_CROP - have
            cost = CROPS[crop]["seed"] * k
            if budget - CASH_RESERVE >= cost:
                orders.append(["BUY_SEED", crop, k])
                budget -= cost

    orders = orders[:MAX_MARKET_ORDERS]

    # --- Unit dispatch.
    farmer_pos = tuple(me["farmer"])
    farmer_op = unit_op(farmer_pos, view, seeds, day, shed, farmer_carry)

    hand_ops = []
    for i, h in enumerate(me["hands"]):
        hand_pos = tuple(h)
        hand_carry = inventories[i + 1] if len(inventories) > i + 1 else {}
        hand_ops.append(unit_op(hand_pos, view, seeds, day, shed, hand_carry))

    STATE["initialized"] = True
    return {"farmer": farmer_op, "hands": hand_ops, "market": orders}


def agent(obs, configuration=None):
    """Kaggle submission entry point with top-level crash guard."""
    try:
        return _agent(obs)
    except Exception as exc:
        import traceback
        print(f"GUARD swallowed exception: {exc!r}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"farmer": ["PASS"], "hands": [], "market": []}
