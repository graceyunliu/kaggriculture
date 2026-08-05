import math
import random
import sys

# =====================================================================
# MAIN V7.2 DRAFT
#
# Base: v7's animal pipeline (schema, shed geometry, worker-inventory
# tracking, stateless maintenance loop) — verified correct against the
# real vendored engine source AND the real replay data, not guesses.
#
# Fixes applied on top of v7, each grounded in engine source, replay data,
# or head-to-head local testing against v7 (not just static review claims):
#   1. Hiring cost is now the REAL engine formula — fib(hires_today) *
#      farmHandCostMult (mult=1) — deducted from the virtual budget
#      order-by-order, instead of v7's no-deduction-at-all. Hand target
#      ceiling is kept at v7's original 18, NOT lowered to 8 as both
#      external reviews urged: that "18-hand bomb" fear doesn't hold up
#      (worst case ~$143/day, capped by the engine's own 10-order/turn
#      ceiling, and every hire is affordability-gated so it can't
#      overdraw), and empirically, capping it at 8 lost head-to-head to
#      v7 by ~2.5x on identical seeds — this economy's profit is
#      dominated by one melon stockpile-and-dump around day 10-11, and
#      that dump's size is a direct function of early-game labor.
#   2. Real cow economics: cost is a flat $400 (not ~$1,000-1,200
#      guessed from replays), max_held=6 (not 5), first_yield_day=8,
#      interval=2. Cow purchase gate and budget deduction corrected
#      accordingly — this one turned out to be free (no throughput
#      cost either way in testing), unlike hand count and planting.
#   3. Feed is now prioritized over product deposit at the shed once an
#      animal has already missed a feeding (consecutive_unfed >= 1) —
#      2 consecutive unfed days permanently loses the animal with no
#      refund (engine `_daily_refresh_animals`), a risk neither v6.1
#      nor v7 explicitly guarded against.
#   4. Market-order merge keeps v7's original order (strategic, feed,
#      sell, hire, seed) rather than moving hire/seed ahead of sell as
#      first attempted — that reordering, meant to fix the real
#      market-slot-starvation bug ChatGPT flagged, instead cost the
#      melon dump its slot on the turns that mattered and cost ~2x
#      final money in testing. Starvation is instead fixed with a
#      floor: hire/seed each get a guaranteed slot by bumping the
#      lowest-priority SELL order only if literally all 10 are full,
#      rather than pre-reserving space nothing may need that turn.
#
# Explicitly NOT changed, even though both external reviews recommended these
# and it seemed obviously correct on paper — each was tried and cost real
# money head-to-head against v7 in local testing:
#   - v6.1's dynamic (worker/backlog-aware) planting guard, in place of v7's
#     flat hour<21 cutoff. Combined with a lower hand cap it throttled early
#     planting enough to starve the day-10 dump; the same-day-water invariant
#     (kept, see unit_action) already prevents the actual death case a
#     tighter guard would add, so the extra restriction bought no real safety.
#   - Removing a task from the shared list only on arrival instead of on the
#     first step toward it (see the comment on tasks[key].remove(tgt) in
#     unit_action for the mechanism — it's a same-turn load-balancing effect
#     that matters a lot given units respawn clustered at the shed every day).
#
# Kept unchanged from v7 (already verified correct, not touched):
#   - CENTER_TILES = shed geometry (confirmed against engine source;
#     v6.1's SHED_POS=(0,0) was wrong and never fixed for submission)
#   - Occupied-pasture perception ({"kind":"PASTURE","animal":...})
#   - obs["private"]["inventories"] carry tracking (farmer first)
#   - Cow setup state machine, wheat pickup/feed travel, product
#     carry+deposit loop
#   - DemandTimingEngine — byte-identical in v7 and v6.1, and actually
#     fully deterministic (hardcoded seed 42, not the episode seed),
#     contra both external reviews calling it "randomized"
# =====================================================================

PRICE_FLOOR = 1
I0 = 10_000
SHED_CAP = 100
LIQUIDATE_DAY = 28
MAX_MARKET_ORDERS = 10

BOARD = 10
CENTER_TILES = [(4, 4), (4, 5), (5, 4), (5, 5)]

# --- Multi-animal experiment constants ---
# COW values are engine-verified from v7.1. SHEEP_COST should be rechecked
# against the vendored engine before ladder submission; 500 is the working
# draft value used to make the experiment executable.
ANIMAL_CONFIG = {
    "COW": {
        "cost": 400,
        "min_money": 700,
        "start_day": 3,
        "last_day": 18,
        "product": "MILK",
    },
    "SHEEP": {
        "cost": 500,
        "min_money": 1000,
        "start_day": 8,
        "last_day": 18,
        "product": "WOOL",
    },
}

# Conservative scale test: enough animals to test the leaderboard hypothesis,
# but small enough for one farmer to service. Set entries to NONE/ABANDONED
# independently; only one setup plan is allowed to progress at a time.
ANIMAL_ROSTER = ("COW", "COW", "COW", "SHEEP")
MAX_ACTIVE_ANIMALS = len(ANIMAL_ROSTER)
MAX_CONCURRENT_SETUPS = 1
ANIMAL_BUY_MIN_DAY_GAP = 2
SETUP_STAGE_TIMEOUT = 12
SETUP_MAX_RETRIES = 3
FEED_CARRY_TARGET = 4
PRODUCT_DEPOSIT_AT = 4

# --- Real hiring cost model (kaggriculture.py: FARM_HAND_COST_MULT=1, fib(0)=1,1,2,3,5,...) ---
FARM_HAND_COST_MULT = 1
HAND_TARGET_MIN = 4
HAND_TARGET_MAX = 18           # hands + farmer position + inventories ALL reset to empty every
                                # single day (engine `_end_of_day`) — there is no such thing as a
                                # persistent fleet, only a daily re-buy, and the real Fibonacci cost
                                # of even a full day's hiring is cheap (~$143 worst case, capped by
                                # the engine's own 10-order/turn ceiling) and self-gated by budget
                                # (see FARM_HAND_COST_MULT/_fib below) — so there's no bankruptcy
                                # risk either way. A lower cap (8, as both external reviews urged)
                                # was tested here and head-to-head lost to v7 by ~2.5x on identical
                                # seeds: this economy's profit is dominated by a single melon
                                # stockpile-and-dump around day 10, and that dump's size is a direct
                                # function of how many tiles got planted/watered/harvested by enough
                                # hands beforehand. Capping labor to guard against a cost that was
                                # never actually dangerous just throttled the thing that matters.

# --- Market-order category slot reservations ---
# Sell is placed BEFORE hire/seed in the merge (v7's original order — see
# economy()), not bucketed ahead of it. Both a hard 5-slot sell cap AND
# reordering hire/seed ahead of sell were tried and tanked revenue ~2-2.5x in
# local head-to-head testing against v7 (identical seeds): this economy's
# profit is dominated by one big melon dump around day 10-11, a single SELL
# order that needs whatever room it needs that turn, and it kept losing its
# slot on days hiring also fired. Instead, a small floor below guarantees
# hire/seed always get at least one order through even on a fully-booked
# selling day (the real starvation bug ChatGPT flagged), by bumping the
# lowest-value sell order rather than pre-reserving space nothing may need.
MAX_HIRE_SLOTS = HAND_TARGET_MAX
MAX_SEED_SLOTS = 3

CROPS = {
    "WHEAT":      {"seed": 10,  "first": 2,  "max_day": 4,  "interval": 0, "max_yield": 6, "ongoing": False},
    "CARROT":     {"seed": 20,  "first": 2,  "max_day": 3,  "interval": 0, "max_yield": 4, "ongoing": False},
    "TOMATO":     {"seed": 50,  "first": 8,  "max_day": 8,  "interval": 1, "max_yield": 4, "ongoing": True},
    "STRAWBERRY": {"seed": 100, "first": 10, "max_day": 10, "interval": 2, "max_yield": 4, "ongoing": True},
    "MELON":      {"seed": 80,  "first": 10, "max_day": 12, "interval": 0, "max_yield": 6, "ongoing": False},
}

MARKET_PARAMS = {
    "WHEAT":      {"base": 25,  "T": 400, "bf": "sqrt",   "bt": 0.80, "af": "log",    "at": 0.20},
    "CARROT":     {"base": 35,  "T": 450, "bf": "log",    "bt": 0.20, "af": "sqrt",   "at": 0.70},
    "TOMATO":     {"base": 60,  "T": 200, "bf": "linear", "bt": 0.40, "af": "sqrt",   "at": 0.60},
    "STRAWBERRY": {"base": 120, "T": 100, "bf": "sqrt",   "bt": 0.70, "af": "linear", "at": 1.60},
    "MELON":      {"base": 250, "T": 300, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.60},
    "EGG":        {"base": 50,  "T": 332, "bf": "linear", "bt": 0.40, "af": "log",    "at": 0.20},
    "MILK":       {"base": 160, "T": 122, "bf": "sqrt",   "bt": 0.60, "af": "linear", "at": 1.60},
    "WOOL":       {"base": 200, "T": 105, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.20},
    "FERTILIZER": {"base": 100, "T": 200, "bf": "linear", "bt": 0.40, "af": "linear", "at": 0.40},
}

CUTOFF = {"WHEAT": 25, "CARROT": 26, "MELON": 16}
PLANT_PRIORITY = ["MELON", "CARROT", "WHEAT"]
PREMIUM_CROPS = {"STRAWBERRY", "MELON"}
ANIMAL_PRODUCTS = ("MILK", "WOOL", "EGG", "FERTILIZER")


def _shape(func, x):
    x = max(0.0, x)
    if func == "linear": return x
    if func == "sq":     return x * x
    if func == "sqrt":   return math.sqrt(x)
    if func == "log":    return math.log(1.0 + x)
    if func == "log10":  return math.log10(1.0 + x)
    return x


def market_price(item, inventory):
    if item not in MARKET_PARAMS:
        return PRICE_FLOOR
    p = MARKET_PARAMS[item]
    base, T = p["base"], p["T"]
    if inventory < I0:
        amp = p["bt"] * base / _shape(p["bf"], T)
        price = base + amp * _shape(p["bf"], I0 - inventory)
    else:
        amp = p["at"] * base / _shape(p["af"], T)
        price = base - amp * _shape(p["af"], inventory - I0)
    return max(PRICE_FLOOR, int(round(price)))


def units_sellable_above(item, inventory, min_price, cap):
    n = 0
    while n < cap and market_price(item, inventory + n) >= min_price:
        n += 1
    return n


def _fib(n):
    """Matches engine's _fib: fib(0)=1, fib(1)=1, fib(2)=2, fib(3)=3, fib(4)=5, ..."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class DemandTimingEngine:
    def __init__(self, match_seed=42):
        # NOTE: hardcoded seed, not the episode seed — this jitter is fully
        # deterministic and identical every single game, not "randomized".
        self.rng = random.Random(match_seed)
        self.d10_target_turn = 9 * 24 + self.rng.randint(-2, 2)
        self.d20_target_turn = 19 * 24 + self.rng.randint(-2, 2)
        self.dump_ratio = self.rng.uniform(0.65, 0.85)

    def is_holding_phase(self, day, hour):
        t = day * 24 + hour
        return (7 * 24 <= t < self.d10_target_turn) or (17 * 24 <= t < self.d20_target_turn)

    def is_attack_turn(self, day, hour):
        t = day * 24 + hour
        return t in (self.d10_target_turn, self.d20_target_turn)


# =====================================================================
# PERCEPTION
# =====================================================================

def perceive(me, opp, day):
    urgent_water, water, harvest, empty, weeds = [], [], [], [], []
    my_pastures = []          # (pos, tile) for pastures WITH an animal
    empty_pastures = []

    for y, row in enumerate(me["tiles"]):
        for x, t in enumerate(row):
            if t is None:
                empty.append((x, y))
                continue
            if not isinstance(t, dict):
                continue
            kind = t.get("kind")
            if kind == "WEED":
                weeds.append((x, y))
            elif kind == "PASTURE":
                # VERIFIED (engine source `_new_animal`): the animal lives ON
                # the pasture tile via an "animal" key.
                if t.get("animal"):
                    my_pastures.append(((x, y), t))
                else:
                    empty_pastures.append((x, y))
            elif kind == "PLANT":
                if not t.get("watered_today", False):
                    if t.get("consecutive_unwatered", 0) >= 1:
                        urgent_water.append((x, y))
                    else:
                        water.append((x, y))
                c = CROPS.get(t.get("crop"))
                if c:
                    age = day - t.get("planted_day", day)
                    yu = t.get("yield_units", 0)
                    ready = c["ongoing"] or (age >= c["first"] and
                            (yu >= c["max_yield"] or age >= c["max_day"]))
                    if yu > 0 and ready:
                        harvest.append((x, y))

    imminent = {}
    for row in opp["tiles"]:
        for t in row:
            if isinstance(t, dict) and t.get("kind") == "PLANT":
                c = CROPS.get(t.get("crop"))
                if c:
                    age = day - t.get("planted_day", day)
                    if c["first"] - 2 <= age <= c["max_day"]:
                        imminent[t["crop"]] = imminent.get(t["crop"], 0) + 1

    return {
        "urgent_water": urgent_water, "water": water, "harvest": harvest,
        "empty": empty, "weeds": weeds,
        "my_pastures": my_pastures, "empty_pastures": empty_pastures,
        "opp_imminent": imminent,
    }


# =====================================================================
# ECONOMY (v5 policy + real bucketed market ordering + real hire cost)
# =====================================================================

def phase(day):
    return 0 if day < 10 else (1 if day < 20 else 2)


def plantable_crops(seeds, day):
    return [c for c in PLANT_PRIORITY if seeds.get(c, 0) > 0 and day <= CUTOFF.get(c, -1)]


def live_price(obs, item):
    prices = obs.get("market", {}).get("prices") or {}
    if item in prices:
        return prices[item]
    return market_price(item, obs.get("market", {}).get("inventory", {}).get(item, I0))


def _plan_is_live(plan):
    return plan["stage"] not in ("NONE", "ABANDONED")


def _occupied_species(view):
    counts = {}
    for _, tile in view["my_pastures"]:
        species = tile.get("animal")
        if species:
            counts[species] = counts.get(species, 0) + 1
    return counts


def economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans):
    budget = me["money"]
    shed = obs["private"]["shed"]
    inv = obs["market"]["inventory"]
    behind = me["money"] < opp["money"] - 500
    quads = len(me["unlocked_quadrants"])

    strategic_orders = []
    feed_orders = []
    sell_orders = []
    hire_orders = []
    seed_orders = []

    # --- Buy at most one animal at a time. The plan itself owns setup/retries. ---
    live_setups = sum(1 for p in animal_plans if p["stage"] in ("BOUGHT", "CARRYING"))
    active_count = len(view["my_pastures"])
    last_buy_turn = max((p.get("buy_turn", -10_000) for p in animal_plans), default=-10_000)
    now = day * 24 + hour

    if live_setups < MAX_CONCURRENT_SETUPS and active_count < MAX_ACTIVE_ANIMALS:
        for plan in animal_plans:
            if plan["stage"] != "NONE":
                continue
            species = plan["species"]
            cfg = ANIMAL_CONFIG[species]
            if not (cfg["start_day"] <= day <= cfg["last_day"]):
                continue
            if now - last_buy_turn < ANIMAL_BUY_MIN_DAY_GAP * 24:
                continue
            if budget <= cfg["min_money"]:
                continue
            strategic_orders.append(["BUY_ANIMAL", species, 1])
            plan["buy_attempts"] += 1
            plan["stage"] = "BOUGHT"
            plan["stage_turn"] = now
            plan["buy_turn"] = now
            budget -= cfg["cost"]
            break

    # --- Aggressive land expansion, preserved from v7.1. ---
    if 1 <= day <= 22:
        if quads == 1 and budget > 1000:
            strategic_orders.append(["BUY_LAND"]); budget -= 1000
        elif quads == 2 and budget > 2000 and day <= 18:
            strategic_orders.append(["BUY_LAND"]); budget -= 2000
        elif quads == 3 and budget > 4000 and day <= 16:
            strategic_orders.append(["BUY_LAND"]); budget -= 4000

    # --- Feed reserve scales with the real fleet, including animals in setup. ---
    staged_animals = sum(1 for p in animal_plans if p["stage"] in ("BOUGHT", "CARRYING"))
    n_animals = active_count + staged_animals
    if n_animals > 0:
        target_wheat = n_animals * 2 + FEED_CARRY_TARGET
        have = shed.get("WHEAT", 0)
        if have < target_wheat:
            qty = min(target_wheat - have, 20)
            cost = qty * live_price(obs, "WHEAT")
            if budget >= cost:
                feed_orders.append(["BUY_PRODUCT", "WHEAT", qty])
                budget -= cost

    fert = shed.get("FERTILIZER", 0)
    if fert > 0:
        sell_orders.append(["SELL", "FERTILIZER", fert])

    shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)
    force_dump = shed_load > SHED_CAP - 15 and hour >= 18
    is_attack = timing_engine.is_attack_turn(day, hour)
    is_holding = timing_engine.is_holding_phase(day, hour)

    feed_reserve = n_animals * 2 + (FEED_CARRY_TARGET if n_animals else 0)
    sellable = []
    for item, qty in shed.items():
        if not (isinstance(qty, (int, float)) and qty > 0):
            continue
        if item not in MARKET_PARAMS or item == "FERTILIZER" or item in ANIMAL_CONFIG:
            continue
        if item == "WHEAT":
            qty -= feed_reserve
            if qty <= 0:
                continue
        sellable.append((item, qty))

    for item, qty_available in sorted(sellable, key=lambda kv: -live_price(obs, kv[0])):
        base = MARKET_PARAMS[item]["base"]
        price_now = live_price(obs, item)
        if is_attack and item in PREMIUM_CROPS:
            qty = max(1, int(qty_available * timing_engine.dump_ratio))
        elif is_holding and item in PREMIUM_CROPS and not force_dump:
            continue
        elif force_dump or day >= LIQUIDATE_DAY or price_now >= 1.05 * base:
            qty = int(qty_available)
        else:
            frac = 0.85 if item in PREMIUM_CROPS else 0.70
            if view["opp_imminent"].get(item, 0) >= 4:
                frac -= 0.25
            if behind and item in PREMIUM_CROPS and day >= 20:
                frac += 0.10
            floor = frac * base
            relax = max(0.0, 1.0 - max(0, shed_load - 40) / 50.0)
            qty = units_sellable_above(item, inv.get(item, I0), floor * relax, int(qty_available))
        if qty > 0:
            sell_orders.append(["SELL", item, qty])

    if hour == 0 and day < 29:
        work = (len(view["water"]) + len(view["urgent_water"]) +
                len(view["harvest"]) + len(view["empty"]))
        # Animal fleet adds daily travel/maintenance load; one extra target hand
        # per two active animals, while preserving the experimentally validated cap.
        target = max(HAND_TARGET_MIN,
                     min(HAND_TARGET_MAX, math.ceil(work / 5) + math.ceil(active_count / 2)))
        need = max(0, target - len(me["hands"]))
        n = 0
        while n < need and len(hire_orders) < MAX_HIRE_SLOTS:
            cost = FARM_HAND_COST_MULT * _fib(me.get("hires_today", 0) + n)
            if budget < cost:
                break
            hire_orders.append(["HIRE"])
            budget -= cost
            n += 1

    ph = phase(day)
    space = len(view["empty"]) + 2
    want = {}
    if day <= CUTOFF["MELON"] and budget > 700:
        want["MELON"] = min(space, 6 if ph == 0 else 10)
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
        # More fleet means more feed demand; seed target grows modestly.
        want["WHEAT"] = 4 + min(8, active_count * 2)

    reserve = 500 if ph == 0 else 200
    for crop, tgt in want.items():
        if len(seed_orders) >= MAX_SEED_SLOTS:
            break
        have = seeds.get(crop, 0)
        if have < tgt:
            k = tgt - have
            cost = CROPS[crop]["seed"] * k
            if budget - reserve >= cost:
                seed_orders.append(["BUY_SEED", crop, k])
                budget -= cost

    # Preserve v7.1's tested order behavior and starvation floor.
    orders = []
    for bucket in (strategic_orders, feed_orders, sell_orders):
        for order in bucket:
            if len(orders) >= MAX_MARKET_ORDERS:
                break
            orders.append(order)

    for bucket in (hire_orders, seed_orders):
        for order in bucket:
            if len(orders) < MAX_MARKET_ORDERS:
                orders.append(order)
            else:
                for i in range(len(orders) - 1, -1, -1):
                    if orders[i][0] == "SELL":
                        orders[i] = order
                        break
                break
    return orders


# =====================================================================
# MOVEMENT
# =====================================================================

def _step_toward(pos, target):
    x, y = pos
    tx, ty = target
    if x < tx: return "EAST"
    if x > tx: return "WEST"
    if y < ty: return "SOUTH"
    if y > ty: return "NORTH"
    return None


def _nearest(pos, targets):
    if not targets:
        return None
    return min(targets, key=lambda t: abs(t[0] - pos[0]) + abs(t[1] - pos[1]))


def _dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _nearest_center(pos):
    return _nearest(pos, CENTER_TILES)


# =====================================================================
# COW PIPELINE (farmer-owned)
#
# Setup stages: NONE -> BOUGHT -> (build) PASTURE_READY -> CARRYING
#               -> ACTIVE; ABANDONED on repeated failure. Maintenance
#               is stateless: recomputed from tile + carry every turn.
# =====================================================================

def _fail_stage(plan, fallback_stage):
    plan["retries"] += 1
    if plan["retries"] > SETUP_MAX_RETRIES:
        plan["stage"] = "ABANDONED"
    else:
        plan["stage"] = fallback_stage


def _advance(plan, stage, day, hour, **kv):
    plan["stage"] = stage
    plan["stage_turn"] = day * 24 + hour
    plan["retries"] = 0
    plan.update(kv)


def _pasture_tile_at(view, site):
    for pos, tile in view["my_pastures"]:
        if pos == site:
            return tile
    return None


def reconcile_animal_plans(animal_plans, view, shed, farmer_carry, day, hour):
    """Verify every setup plan against board, shed, and farmer inventory."""
    turn = day * 24 + hour
    for plan in animal_plans:
        stage = plan["stage"]
        species = plan["species"]
        site = plan.get("site")
        tile = _pasture_tile_at(view, site) if site is not None else None
        timed_out = (plan.get("stage_turn") is not None and
                     turn - plan["stage_turn"] >= SETUP_STAGE_TIMEOUT)

        if tile and tile.get("animal") == species:
            if stage != "ACTIVE":
                _advance(plan, "ACTIVE", day, hour)
            continue

        if stage == "BOUGHT":
            if shed.get(species, 0) > 0 or farmer_carry.get(species, 0) > 0:
                continue
            if timed_out:
                _fail_stage(plan, "NONE")
        elif stage == "CARRYING":
            if farmer_carry.get(species, 0) > 0:
                continue
            if shed.get(species, 0) > 0:
                _fail_stage(plan, "BOUGHT")
            elif timed_out:
                _fail_stage(plan, "NONE")
        elif stage == "ACTIVE":
            # Animal disappeared from its assigned pasture.
            if shed.get(species, 0) == 0 and farmer_carry.get(species, 0) == 0:
                _advance(plan, "ABANDONED", day, hour)
        elif timed_out and stage not in ("NONE", "ABANDONED"):
            _fail_stage(plan, "NONE" if shed.get(species, 0) == 0 else "BOUGHT")


def next_setup_plan(animal_plans):
    for plan in animal_plans:
        if plan["stage"] in ("BOUGHT", "CARRYING"):
            return plan
    return None


def animal_setup_action(pos, view, shed, farmer_carry, animal_plans, day, hour):
    """Progress one animal setup at a time; return None when farmer is free."""
    plan = next_setup_plan(animal_plans)
    if plan is None:
        return None

    species = plan["species"]
    carrying = farmer_carry.get(species, 0) > 0
    used_sites = {p.get("site") for p in animal_plans if p.get("site") is not None and p is not plan}

    site = plan.get("site")
    if site is None or (site not in view["empty"] and site not in view["empty_pastures"]):
        candidates = [t for t in (view["empty_pastures"] or view["empty"])
                      if t not in CENTER_TILES and t not in used_sites]
        if not candidates:
            return None
        site = min(candidates, key=lambda p2: _dist(p2, _nearest_center(p2)))
        plan["site"] = site

    if site not in view["empty_pastures"]:
        if pos != site:
            return [_step_toward(pos, site)]
        return ["BUILD_PASTURE"]

    if not carrying:
        if shed.get(species, 0) == 0:
            return None
        center = _nearest_center(pos)
        if pos not in CENTER_TILES:
            return [_step_toward(pos, center)]
        _advance(plan, "CARRYING", day, hour)
        return ["PICKUP", species, 1]

    if pos != site:
        return [_step_toward(pos, site)]
    return ["PLACE", species]


def _animal_need(tile):
    needs_feed = not tile.get("fed_today", True)
    urgent_feed = needs_feed and tile.get("consecutive_unfed", 0) >= 1
    if urgent_feed:
        return 0, "feed"
    if needs_feed:
        return 1, "feed"
    if tile.get("yield_units", 0) > 0:
        return 2, "harvest"
    if not tile.get("cared_today", True):
        return 3, "care"
    if tile.get("fertilizer_available", False):
        return 4, "fertilizer"
    return 99, None


def animal_maintenance_action(pos, view, shed, farmer_carry, day, hour):
    """Service a small mixed fleet with survival-first routing."""
    if not view["my_pastures"]:
        return None

    carry_wheat = farmer_carry.get("WHEAT", 0)
    carry_products = {i: farmer_carry.get(i, 0) for i in ANIMAL_PRODUCTS
                      if farmer_carry.get(i, 0) > 0}

    needs = []
    for ppos, tile in view["my_pastures"]:
        priority, action = _animal_need(tile)
        if action is not None:
            needs.append((priority, _dist(pos, ppos), ppos, tile, action))
    needs.sort(key=lambda row: (row[0], row[1]))

    urgent_unfed = any(priority == 0 for priority, *_ in needs)
    any_feed_needed = any(action == "feed" for *_, action in needs)
    fetch_wheat_due = any_feed_needed and carry_wheat == 0 and shed.get("WHEAT", 0) > 0
    deposit_due = sum(carry_products.values()) >= PRODUCT_DEPOSIT_AT

    if pos in CENTER_TILES:
        if fetch_wheat_due and urgent_unfed:
            return ["PICKUP", "WHEAT", min(FEED_CARRY_TARGET, shed.get("WHEAT", 0))]
        if carry_products and (deposit_due or fetch_wheat_due):
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]]
        if fetch_wheat_due:
            return ["PICKUP", "WHEAT", min(FEED_CARRY_TARGET, shed.get("WHEAT", 0))]

    if fetch_wheat_due:
        return [_step_toward(pos, _nearest_center(pos))]

    if needs:
        _, _, ppos, tile, action = needs[0]
        if pos != ppos:
            return [_step_toward(pos, ppos)]
        if action == "feed" and carry_wheat > 0:
            return ["FEED"]
        if action == "harvest":
            return ["HARVEST"]
        if action == "care":
            return ["CARE"]
        if action == "fertilizer":
            return ["COLLECT_FERTILIZER"]

    if carry_products and (day >= LIQUIDATE_DAY or deposit_due):
        if pos in CENTER_TILES:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]]
        return [_step_toward(pos, _nearest_center(pos))]

    return None


# =====================================================================
# CROP TASK ALLOCATION
# =====================================================================

TASK_ORDER = ["urgent_water", "harvest", "water", "plant", "weeds"]
TASK_ACTION = {
    "urgent_water": ["WATER"],
    "harvest": ["HARVEST"],
    "water": ["WATER"],
    "weeds": ["DIG"],
}


def unit_action(pos, tasks, seeds, day):
    x, y = pos
    for key in TASK_ORDER:
        if (x, y) in tasks[key]:
            tasks[key].remove((x, y))
            if key == "plant":
                for crop in plantable_crops(seeds, day):
                    seeds[crop] -= 1
                    tasks["urgent_water"].append((x, y))  # same-day water invariant (D11)
                    return ["PLANT", crop]
                continue
            return TASK_ACTION[key]

    # `tasks` is rebuilt fresh from the board every turn (see _agent) — removing
    # a target here only affects who else gets assigned to it THIS turn, it does
    # not lose the underlying work; next turn's perceive() re-adds it if still
    # outstanding. Both external reviews flagged this remove-on-first-step as a
    # bug ("the crop may never get watered"), and v6.1's alternative (only
    # remove on arrival) was tried here. It's worse: every unit respawns
    # clustered at the same shed tiles each day (the engine wipes
    # hands/farmer position daily — see HAND_TARGET_MAX comment), so without
    # this line, many freshly-spawned units all compute the same "_nearest"
    # target from nearly the same position and pile onto ONE tile instead of
    # spreading out; removing it here is what makes unit 2's _nearest() land on
    # the second-closest tile instead of unit 1's. Reverting it cost ~2.5x
    # final money in head-to-head testing against v7.
    for key in TASK_ORDER:
        tgt = _nearest((x, y), tasks[key])
        if tgt:
            step = _step_toward((x, y), tgt)
            if step:
                tasks[key].remove(tgt)
                return [step]

    fallback = _step_toward((x, y), (4, 4))  # idle drift toward shed (VERIFIED center)
    return [fallback] if fallback else ["PASS"]


# =====================================================================
# ENTRY
# =====================================================================

timing_engine = DemandTimingEngine(match_seed=42)
animal_plans = [
    {"species": species, "stage": "NONE", "site": None, "stage_turn": None,
     "retries": 0, "buy_attempts": 0, "buy_turn": -10_000}
    for species in ANIMAL_ROSTER
]


def _agent(obs):
    p = obs["player"]
    me, opp = obs["farms"][p], obs["farms"][1 - p]
    day, hour = obs["day"], obs["hour"]
    seeds = dict(obs["private"]["seeds"])
    shed = obs["private"]["shed"]

    # VERIFIED: inventories is a per-unit list, farmer first.
    inventories = obs["private"].get("inventories") or []
    farmer_carry = inventories[0] if inventories else {}

    view = perceive(me, opp, day)
    reconcile_animal_plans(animal_plans, view, shed, farmer_carry, day, hour)

    market = economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans)

    crops_now = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(c, 0) for c in crops_now)

    # Planting guard: v7's original flat cutoff, combined with the same-day-water
    # invariant (handled in unit_action). v6.1's dynamic worker/backlog-aware
    # guard was tried here too and — combined with the lower hand cap — throttled
    # early planting enough to starve the day-10ish melon dump (see
    # HAND_TARGET_MAX comment); the same-day-water invariant already prevents
    # the actual death case (a fresh plant going unwatered), so the extra
    # slot-limiting math wasn't buying additional safety, just less throughput.
    tasks = {
        "urgent_water": list(view["urgent_water"]),
        "harvest": list(view["harvest"]),
        "water": list(view["water"]),
        "plant": (view["empty"][:n_plantable] if crops_now and hour < 21 else []),
        "weeds": list(view["weeds"]) if day <= 27 else [],
    }
    # Never plant on any reserved animal site.
    reserved_sites = {p.get("site") for p in animal_plans if p.get("site") is not None}
    tasks["plant"] = [t for t in tasks["plant"] if t not in reserved_sites]

    farmer_pos = tuple(me["farmer"])
    farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, animal_plans, day, hour)
    if farmer_op is None:
        farmer_op = animal_maintenance_action(farmer_pos, view, shed, farmer_carry, day, hour)
    if farmer_op is None:
        farmer_op = unit_action(farmer_pos, tasks, seeds, day)

    hand_ops = [unit_action(tuple(h), tasks, seeds, day) for h in me["hands"]]
    return {"farmer": farmer_op, "hands": hand_ops, "market": market}


def agent(obs, configuration=None):
    """Kaggle submission entry point with top-level crash guard."""
    try:
        return _agent(obs)
    except Exception as exc:
        import traceback
        print(f"GUARD swallowed exception: {exc!r}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"farmer": ["PASS"], "hands": [], "market": []}
