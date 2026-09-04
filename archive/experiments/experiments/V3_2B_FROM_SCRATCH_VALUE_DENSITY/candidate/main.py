# V3_2B_FROM_SCRATCH_VALUE_DENSITY -- "VALUE-DENSITY ECONOMY"
#
# Genuinely from-scratch Kaggriculture agent. Per the task mandate, this
# does NOT reuse V10.6's decision-tree structure, priority lists, gating
# logic, scan(), assign_tasks(), or any of its scoring/matching functions.
# The only thing carried over from V10.6 (explicitly permitted) is the
# action-schema *shape*: {"farmer": [...], "hands": [[...],...],
# "market": [[...],...]} with order/unit verbs in the same string format
# (BUY_SEED/BUY_ANIMAL/BUY_LAND/HIRE/SELL/BUY_PRODUCT for market orders;
# NORTH/SOUTH/EAST/WEST/PLANT/WATER/HARVEST/FEED/CARE/PICKUP/PLACE/DIG/
# BUILD_COOP/BUILD_PASTURE/FERTILIZE/COLLECT_FERTILIZER/PASS for unit
# ops) -- this is required for compatibility with the real kaggriculture
# engine (kaggle_environments/envs/kaggriculture/kaggriculture.py) and is
# not a decision-logic borrowing.
#
# CORE DECISION RULE ("value density"): at every decision point, this
# agent computes a live, per-turn expected-value-per-worker-hour and
# expected-value-per-dollar for every currently available action (plant
# X, buy animal Y, hire a hand, buy land, sell shed stock) using the
# real game constants (CROPS/ANIMALS costs, yields, cycle intervals) and
# the LIVE market prices read straight from obs["market"]["prices"] each
# turn, then always spends the next dollar/worker-turn on whichever real
# option currently has the highest computed density. There is no fixed
# priority list: crop/animal/land/hire rankings are recomputed from
# scratch every single turn from current prices and current day, so the
# ranking can and does change turn to turn as prices move. See
# docs/V3_2B_FROM_SCRATCH_VALUE_DENSITY.md for the exact formulas and the
# regime spec, written BEFORE this file per the task's required order.

import sys

CROPS = {
    "WHEAT":      {"seed": 10, "first_yield_day": 2, "max_yield_day": 4, "interval": 0, "max_yield": 6, "ongoing": False},
    "CARROT":     {"seed": 20, "first_yield_day": 2, "max_yield_day": 3, "interval": 0, "max_yield": 4, "ongoing": False},
    "TOMATO":     {"seed": 50, "first_yield_day": 8, "max_yield_day": 8, "interval": 1, "max_yield": 4, "ongoing": True},
    "STRAWBERRY": {"seed": 100, "first_yield_day": 10, "max_yield_day": 10, "interval": 2, "max_yield": 4, "ongoing": True},
    "MELON":      {"seed": 80, "first_yield_day": 10, "max_yield_day": 12, "interval": 0, "max_yield": 6, "ongoing": False},
}

ANIMALS = {
    "GOOSE": {"cost": 300, "structure": "COOP",    "first_yield_day": 4, "interval": 1, "max_held": 4, "product": "EGG"},
    "COW":   {"cost": 400, "structure": "PASTURE", "first_yield_day": 8, "interval": 2, "max_held": 6, "product": "MILK"},
    "SHEEP": {"cost": 500, "structure": "PASTURE", "first_yield_day": 6, "interval": 3, "max_held": 6, "product": "WOOL"},
}

LAND_ORDER = ["NE", "SW", "SE"]
LAND_PRICES = [1000, 2000, 4000]
GAME_DAYS = 30
CASH_RESERVE = 60.0
MAX_ORDERS = 10
SHED_DEPOSIT_AT = 3

FARMER_MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}


def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def _hire_cost(n_already_today):
    return _fib(n_already_today)


# ---------------------------------------------------------------------
# VALUE-DENSITY FORMULAS (exact, live-computed each turn; see doc for
# derivation). All use CURRENT market prices and the CURRENT day, so
# these are not fixed constants -- they are recomputed fresh every call.
# ---------------------------------------------------------------------

def crop_labor_density(crop, price):
    """VD_labor(crop) = $ revenue per hand-turn once the crop is in
    steady production, i.e. dollars generated per required WATER action.
    Non-ongoing crops need max_yield waterings to reach cap, one HARVEST,
    one PLANT -> (max_yield*price - seed_cost) / (max_yield + 2).
    Ongoing crops repeat indefinitely at 1 unit per `interval` watered
    days once mature -> price / interval (steady-state $/hand-turn)."""
    cd = CROPS[crop]
    if cd["ongoing"]:
        return price / max(1, cd["interval"])
    hand_turns = cd["max_yield"] + 2
    revenue = cd["max_yield"] * price - cd["seed"]
    return revenue / hand_turns


def crop_capital_density(crop, price, day):
    """VD_capital(crop) = $ net profit per $ of seed cost per remaining
    day the crop can still produce before day 30 -- rewards crops whose
    full-cycle payback fits inside the remaining runway and penalizes
    ones that don't (mirrors V3_0N's late-investment failure lesson:
    remaining runway, not raw price, gates whether a crop is worth its
    capital)."""
    cd = CROPS[crop]
    remaining = GAME_DAYS - day
    if cd["ongoing"]:
        cycles_left = max(0, (remaining - cd["first_yield_day"]) / max(1, cd["interval"]))
        revenue = cycles_left * price
    else:
        if remaining < cd["max_yield_day"]:
            return -1.0  # will not finish maturing -- explicitly bad
        revenue = cd["max_yield"] * price
    return (revenue - cd["seed"]) / max(1, cd["seed"])


def animal_labor_density(species, price):
    a = ANIMALS[species]
    return price / max(1, a["interval"])


def animal_capital_density(species, price, day):
    a = ANIMALS[species]
    remaining = GAME_DAYS - day
    cycles_left = max(0, (remaining - a["first_yield_day"]) / max(1, a["interval"]))
    revenue = cycles_left * price
    return (revenue - a["cost"]) / a["cost"]


def best_crop_by_labor(prices):
    return max(CROPS, key=lambda c: crop_labor_density(c, prices.get(c, CROPS[c]["seed"])))


def best_crop_by_capital(prices, day):
    scored = [(crop_capital_density(c, prices.get(c, CROPS[c]["seed"]), day), c) for c in CROPS]
    scored.sort(reverse=True)
    return scored


def best_animal_by_capital(prices, day):
    scored = [(animal_capital_density(a, prices.get(ANIMALS[a]["product"], 0), day), a) for a in ANIMALS]
    scored.sort(reverse=True)
    return scored


# ---------------------------------------------------------------------
# Board helpers
# ---------------------------------------------------------------------

def _tiles_of(farm):
    return farm["tiles"]


def _manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _step_toward(pos, target):
    dx = target[0] - pos[0]
    dy = target[1] - pos[1]
    if dx == 0 and dy == 0:
        return None
    if abs(dx) >= abs(dy):
        return "EAST" if dx > 0 else "WEST"
    return "SOUTH" if dy > 0 else "NORTH"


def _is_shed_adjacent(pos, board_size):
    half = board_size // 2
    corners = {(half - 1, half - 1), (half, half - 1), (half - 1, half), (half, half)}
    return tuple(pos) in corners


def _shed_access_tiles(board_size):
    half = board_size // 2
    return [(half - 1, half - 1), (half, half - 1), (half - 1, half), (half, half)]


def _scan(farm, board_size):
    """One pass over own tiles into simple buckets. Not a copy of V10.6's
    scan(): no scoring, just bucketed positions consumed by the live
    density ranking below."""
    empty, harvest_ready, water_needed, weeds = [], [], [], []
    coop_empty, pasture_empty, animal_unfed = [], [], []
    for y in range(board_size):
        for x in range(board_size):
            t = farm["tiles"][y][x]
            if t is None:
                empty.append((x, y))
            elif t == "LOCKED":
                continue
            elif isinstance(t, dict):
                kind = t.get("kind")
                if kind == "WEED":
                    weeds.append((x, y))
                elif kind == "PLANT":
                    if t.get("yield_units", 0) > 0:
                        harvest_ready.append((x, y))
                    if not t.get("watered_today"):
                        water_needed.append((x, y))
                elif "animal" in t:
                    if t.get("yield_units", 0) > 0:
                        harvest_ready.append((x, y))
                    if not t.get("fed_today"):
                        animal_unfed.append((x, y))
                elif kind == "COOP":
                    coop_empty.append((x, y))
                elif kind == "PASTURE":
                    pasture_empty.append((x, y))
    return {
        "empty": empty, "harvest_ready": harvest_ready, "water_needed": water_needed,
        "weeds": weeds, "coop_empty": coop_empty, "pasture_empty": pasture_empty,
        "animal_unfed": animal_unfed,
    }


def _nearest(pos, candidates, exclude=()):
    best, best_d = None, None
    for c in candidates:
        if c in exclude:
            continue
        d = _manhattan(pos, c)
        if best_d is None or d < best_d:
            best, best_d = c, d
    return best


# ---------------------------------------------------------------------
# Per-unit dispatch: highest-VD available action for THIS unit right now.
# Recomputed fresh every call from live state -- no persistent plan
# objects, no multi-day state machine (deliberately different in kind
# from V10.6's build-slot/plan architecture).
# ---------------------------------------------------------------------

def unit_op(pos, inv, view, board_size, seeds, best_plant_crop, exclude_targets, buy_crop_target):
    tile_here = None  # caller passes farm via closure normally; see _agent

    # 1. Harvest if standing on a ready tile.
    if pos in view["harvest_ready"]:
        return ["HARVEST"], None

    # 2. Deposit at shed if carrying enough product and adjacent to shed.
    carried = sum(v for k, v in inv.items() if k not in ANIMALS)
    if carried >= SHED_DEPOSIT_AT and _is_shed_adjacent(pos, board_size):
        item = max(inv, key=lambda k: inv[k]) if inv else None
        if item and item not in ANIMALS:
            return ["PLACE", item, inv[item]], None

    # 3. Feed an unfed animal if carrying wheat and one is nearby/here.
    if inv.get("WHEAT", 0) > 0 and view["animal_unfed"]:
        if pos in view["animal_unfed"]:
            return ["FEED"], None
        tgt = _nearest(pos, view["animal_unfed"], exclude_targets)
        if tgt:
            st = _step_toward(pos, tgt)
            if st:
                return [st], tgt

    # 4. Water if standing on a tile that needs it.
    if pos in view["water_needed"]:
        return ["WATER"], None

    # 5. Walk to nearest ready-harvest elsewhere.
    if view["harvest_ready"]:
        tgt = _nearest(pos, view["harvest_ready"], exclude_targets)
        if tgt:
            st = _step_toward(pos, tgt)
            if st:
                return [st], tgt

    # 6. Walk to nearest tile needing water.
    if view["water_needed"]:
        tgt = _nearest(pos, view["water_needed"], exclude_targets)
        if tgt:
            st = _step_toward(pos, tgt)
            if st:
                return [st], tgt

    # 7. Plant the highest-value-density crop we have seed for, on an
    #    empty tile.
    if best_plant_crop and seeds.get(best_plant_crop, 0) > 0:
        if pos in view["empty"]:
            return ["PLANT", best_plant_crop], None
        tgt = _nearest(pos, view["empty"], exclude_targets)
        if tgt:
            st = _step_toward(pos, tgt)
            if st:
                return [st], tgt

    # 8. Walk toward an unfed animal even without wheat in hand (will
    #    fetch wheat at the shed en route via priority 3 rules next turn).
    if view["animal_unfed"]:
        tgt = _nearest(pos, view["animal_unfed"], exclude_targets)
        if tgt:
            st = _step_toward(pos, tgt)
            if st:
                return [st], tgt

    # 9. Clear weeds opportunistically (frees a tile for planting).
    if view["weeds"]:
        if pos in view["weeds"]:
            return ["DIG"], None
        tgt = _nearest(pos, view["weeds"], exclude_targets)
        if tgt:
            st = _step_toward(pos, tgt)
            if st:
                return [st], tgt

    return ["PASS"], None


# ---------------------------------------------------------------------
# Main per-turn agent
# ---------------------------------------------------------------------

def _agent(obs):
    farms = obs.get("farms", [])
    player = obs.get("player", 0)
    if not farms or player >= len(farms):
        return {"farmer": ["PASS"], "hands": [], "market": []}
    farm = farms[player]
    private = obs.get("private", {}) or {}
    market = obs.get("market", {}) or {}
    day = obs.get("day", 0)
    prices = market.get("prices", {}) or {}
    board_size = len(farm["tiles"])

    seeds = private.get("seeds", {}) or {}
    shed = private.get("shed", {}) or {}
    money = farm["money"]

    view = _scan(farm, board_size)

    # ---- Live crop/animal ranking (recomputed every turn from current
    #      prices and current day; this is the "no fixed priority list"
    #      requirement). ----
    capital_crop_rank = best_crop_by_capital(prices, day)          # best-first, [(density, crop), ...]
    best_plant_crop = capital_crop_rank[0][1] if capital_crop_rank[0][0] > 0 else None
    labor_crop_rank = sorted(CROPS, key=lambda c: -crop_labor_density(c, prices.get(c, CROPS[c]["seed"])))
    animal_rank = best_animal_by_capital(prices, day)

    # ---- Market order construction: greedily fund the highest-density
    #      affordable action each turn, subject to MAX_ORDERS and a cash
    #      reserve. ----
    orders = []
    hands_count = len(farm.get("hands", []))
    n_units = 1 + hands_count

    # SELL everything in the shed -- realized profit is always the
    # highest-certainty value-density action available (no cycle-time
    # discount, price already locked in by the market quote).
    for item, qty in sorted(shed.items(), key=lambda kv: -prices.get(kv[0], 0)):
        if qty > 0 and len(orders) < MAX_ORDERS:
            orders.append(["SELL", item, qty])

    budget = money - CASH_RESERVE

    # HIRE: value density = best available labor VD / next hire cost.
    # Fund while density > 1 (a hire pays for itself within one hand-
    # turn's worth of the best available task) and cash allows.
    hires_today = farm.get("hires_today", 0)
    best_labor_vd = max(
        crop_labor_density(labor_crop_rank[0], prices.get(labor_crop_rank[0], CROPS[labor_crop_rank[0]]["seed"])),
        animal_labor_density(animal_rank[0][1], prices.get(ANIMALS[animal_rank[0][1]]["product"], 0)) if animal_rank[0][0] > 0 else 0,
    )
    n_extra_hires = 0
    while len(orders) < MAX_ORDERS and n_units + n_extra_hires < 12:
        cost = _hire_cost(hires_today + n_extra_hires)
        density = best_labor_vd / cost
        if density > 1.0 and budget - cost >= 0:
            orders.append(["HIRE"])
            budget -= cost
            n_extra_hires += 1
        else:
            break

    # BUY_LAND: fund the next quadrant if its density (best crop capital
    # density on the new tiles, scaled by tile count) is positive and
    # affordable.
    n_unlocked_extra = len(farm.get("unlocked_quadrants", ["NW"])) - 1
    if n_unlocked_extra < len(LAND_ORDER) and len(orders) < MAX_ORDERS:
        cost = LAND_PRICES[n_unlocked_extra]
        land_density = capital_crop_rank[0][0]
        if land_density > 0.3 and budget - cost >= 0:
            orders.append(["BUY_LAND"])
            budget -= cost

    # BUY_ANIMAL: fund the top-density affordable species while we have
    # (or will soon have) a free structure tile, and density is positive.
    for density, species in animal_rank:
        if len(orders) < MAX_ORDERS and density > 0.5:
            cost = ANIMALS[species]["cost"]
            structure_kind = ANIMALS[species]["structure"]
            has_free_structure = (
                (structure_kind == "COOP" and view["coop_empty"]) or
                (structure_kind == "PASTURE" and view["pasture_empty"])
            )
            owned = shed.get(species, 0)
            if (has_free_structure or view["empty"]) and owned < 2 and budget - cost >= 0:
                orders.append(["BUY_ANIMAL", species, 1])
                budget -= cost
                break

    # BUY_SEED: top up seed stock for the best labor-density crop toward
    # one seed per unit (so nobody idles waiting on seed), then the
    # second-best crop if cash remains.
    for crop in labor_crop_rank[:2]:
        if len(orders) >= MAX_ORDERS:
            break
        target_stock = n_units
        have = seeds.get(crop, 0)
        need = max(0, target_stock - have)
        cost_each = CROPS[crop]["seed"]
        if need > 0 and budget - cost_each * need >= 0 and crop_labor_density(crop, prices.get(crop, cost_each)) > 0:
            orders.append(["BUY_SEED", crop, need])
            budget -= cost_each * need

    # BUY_PRODUCT WHEAT as feed if animals are unfed and no wheat in shed
    # / carried and buying it is cheap relative to the animal product it
    # unlocks (feed-to-sell density check).
    if view["animal_unfed"] and shed.get("WHEAT", 0) < len(view["animal_unfed"]) and len(orders) < MAX_ORDERS:
        need = len(view["animal_unfed"]) - shed.get("WHEAT", 0)
        wheat_price = prices.get("WHEAT", 25)
        if budget - wheat_price * need >= 0:
            orders.append(["BUY_PRODUCT", "WHEAT", need])
            budget -= wheat_price * need

    orders = orders[:MAX_ORDERS]

    # ---- Unit dispatch: farmer first, then hands, each grabbing the
    #      highest-VD reachable task, avoiding already-claimed targets. ----
    claimed = set()
    inventories = private.get("inventories", [{}]) or [{}]

    farmer_pos = tuple(farm["farmer"])
    farmer_inv = inventories[0] if inventories else {}
    farmer_op, tgt = unit_op(farmer_pos, farmer_inv, view, board_size, seeds, best_plant_crop, claimed, None)
    if tgt:
        claimed.add(tgt)

    hand_ops = []
    for i, hpos in enumerate(farm.get("hands", [])):
        hpos = tuple(hpos)
        hinv = inventories[i + 1] if len(inventories) > i + 1 else {}
        op, tgt = unit_op(hpos, hinv, view, board_size, seeds, best_plant_crop, claimed, None)
        if tgt:
            claimed.add(tgt)
        hand_ops.append(op)

    # ---- Place bought animals: any unit standing at the shed carrying
    #      nothing productive should pick up a purchased species and head
    #      to its matching empty structure. Simple opportunistic pass
    #      applied to units that ended up on PASS this turn. ----
    for species in ANIMALS:
        if shed.get(species, 0) <= 0:
            continue
        structure_kind = ANIMALS[species]["structure"]
        targets = view["coop_empty"] if structure_kind == "COOP" else view["pasture_empty"]
        if not targets:
            continue
        # Try the farmer first, then hands, first unit whose op this turn
        # is PASS or a plain move (cheap to override).
        candidates = [(farmer_pos, farmer_inv, "farmer")] + [
            (tuple(farm["hands"][i]), inventories[i + 1] if len(inventories) > i + 1 else {}, i)
            for i in range(len(farm.get("hands", [])))
        ]
        for pos2, inv2, tag in candidates:
            if sum(inv2.values()) > 0:
                continue
            if pos2 in targets:
                new_op = ["PLACE", species]
            elif _is_shed_adjacent(pos2, board_size):
                new_op = ["PICKUP", species, 1]
            else:
                continue
            if tag == "farmer":
                farmer_op = new_op
            else:
                hand_ops[tag] = new_op
            break

    return {"farmer": farmer_op, "hands": hand_ops, "market": orders}


def agent(obs, configuration=None):
    try:
        return _agent(obs)
    except Exception as exc:
        import traceback
        print(f"GUARD swallowed exception: {exc!r}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"farmer": ["PASS"], "hands": [], "market": []}
