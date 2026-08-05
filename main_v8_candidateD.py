import math
import random
import sys

# =====================================================================
# MAIN V8 CANDIDATE D -- fertilize WHEAT only, ISOLATED. Base: v7.9,
# unchanged except for: (1) a FERTILIZER_RESERVE kept in the shed instead
# of selling 100%, and (2) a new fertilize-then-water pipeline for WHEAT
# tiles. want["WHEAT"] is left at v7.9's value of 8 -- this candidate
# isolates the fertilize effect alone, nothing else.
#
# --- Why WHEAT and not STRAWBERRY (the prior round's Candidate A) ---
#
# Re-reading vendor/kaggle_environments_engine/kaggriculture.py directly:
# STRAWBERRY is `"ongoing": True`. Ongoing crops accrue yield only via
# `_daily_refresh_plants`'s calendar path: every `interval` days,
# `yield_units = min(max_yield, yield_units + (2 if fertilized else 1))`.
# Because of the `min(max_yield, ...)`, fertilizing an ongoing crop can
# NEVER raise its yield ceiling -- it only reaches the same max_yield in
# fewer production events. That's a small lifecycle-speed effect, not a
# yield effect, and it matches exactly what the prior round's Candidate A
# measured (no benefit, pure labor/fertilizer cost -- lost 3/3 decisively).
#
# WHEAT is `"ongoing": False`. Non-ongoing crops accrue yield through a
# DIFFERENT path entirely: the WATER action handler
# (`_apply_unit_action`, op == "WATER"), which on each watering day inside
# the window `[(max_yield_day+1)//2, max_yield_day]` (inclusive, by age
# in days since planting) adds `2 if fertilized_until_day >= day else 1`
# to yield_units, capped at max_yield. For WHEAT: max_yield_day=4, so the
# window is ages 2/3/4 (3 possible watering days) against max_yield=6.
# Unfertilized: at most 3 waterings x 1 = 3 units, HALF the cap.
# Fertilized: 3 waterings x 2 = 6 units -- the FULL cap. This is a real
# ~2x yield lever, not a cosmetic one, on a $10-seed crop with a 635-unit
# town demand pool (v7.9 sells only ~243 units into it, nowhere near
# saturated) that is also the animal-feed input.
#
# --- The catch: timing ---
#
# FERTILIZE sets `tile["fertilized_until_day"] = max(existing, day + 2)`
# (active for day, day+1, day+2). A single application exactly at age 2
# (the day the window opens) covers all three window days (2, 3, 4) with
# one FERTILIZER unit -- the efficient case. Applied earlier (age 0/1) it
# lapses before age 4 unless reapplied; applied later it has already
# missed whatever window days passed unwatered-and-fertilized. So this
# candidate targets WHEAT tiles at age <= 2 specifically (see
# WHEAT_FERT_MAX_AGE below) and instruments the actual hit distribution
# by age at the moment FERTILIZE fires, plus a miss counter for tiles
# that aged past the window without ever being fertilized -- see the
# FERTTRACE summary printed on the last turn.
#
# --- Mechanics, not races ---
#
# `_daily_refresh_plants` turns a PLANT tile into a WEED if
# `consecutive_unwatered` reaches 2 -- i.e. skipping watering entirely
# for a tile to "wait" for fertilizer would risk killing it. This
# candidate does NOT remove fertilize-pending WHEAT tiles from the normal
# water task pool; it only gives the fertilize trip priority over
# ordinary crop work when a worker is otherwise free, so on a day it
# doesn't win the race the tile still gets watered on schedule (just
# without that day's bonus) -- a same-as-v7.9 fallback, never worse.
#
# --- Inherited from v7.9 / v7.6 (unchanged) ---
# See main_v7.9.py's header for the strawberry/melon planting-priority
# rationale and the v7.6a protected-crop-hand history; nothing there is
# touched by this candidate.
# =====================================================================

PRICE_FLOOR = 1
I0 = 10_000
SHED_CAP = 100
LIQUIDATE_DAY = 28
MAX_MARKET_ORDERS = 10

BOARD = 10
CENTER_TILES = [(4, 4), (4, 5), (5, 4), (5, 5)]

# Animal fleet config (verified against engine's ANIMALS dict: COW cost=400,
# SHEEP cost=500; both use structure="PASTURE", so no separate site-type
# bookkeeping is needed for either species).
ANIMAL_SPECS = {
    # COW starts day 0 (claims cash before ordinary day-1/2 spend erodes
    # it); SHEEP stays day 3.
    "COW":   {"cost": 400, "min_money": 700, "start_day": 0,  "last_day": 22},
    "SHEEP": {"cost": 500, "min_money": 800, "start_day": 3,  "last_day": 22},
}
ANIMAL_SPECIES_ORDER = ["COW", "SHEEP"]   # priority order when considering the next purchase
SHEEP_ENABLED = False   # disabled -- COW-only fleet scaling for now

# Dynamic fleet expansion: no fixed animal-count cap. Each next purchase is
# gated live by _animal_expansion_feasible() (survival/wheat/hands/crop-space
# checks) instead of a hardcoded target.
EXPANSION_WHEAT_BUDGET_FRAC = 0.15   # next animal's feed shortfall can't cost
                                      # more than this fraction of current cash
EXPANSION_MIN_CROP_TILES_PER_QUAD = 8   # crop-land reserve, scales with
                                          # unlocked quadrants

# A flat animal-count cap was tried and rejected -- it helped one opponent
# and hurt another by roughly the same amount, so no single number
# generalizes (see design doc). CROP_NEGLECT_TASKS_PER_HAND instead checks
# real current hand count against real current crop backlog -- a direct
# symptom check, not a forecast.
CROP_NEGLECT_TASKS_PER_HAND = 5      # matches hiring formula's work/5 scaling
ANIMAL_WORK_WEIGHT = 2               # pasture visit weight vs. one crop tile
                                       # (a round trip costs more hand-turns)

SETUP_STAGE_TIMEOUT = 12
SETUP_MAX_RETRIES = 3
FEED_CARRY_TARGET = 2
PRODUCT_DEPOSIT_AT = 3         # PLACE milk/wool when carrying this many

# Real hiring cost model (kaggriculture.py: FARM_HAND_COST_MULT=1, fib(0)=1,1,2,3,5,...)
FARM_HAND_COST_MULT = 1
HAND_TARGET_MIN = 4
HAND_TARGET_MAX = 18

# Market-order category slot reservations
MAX_HIRE_SLOTS = HAND_TARGET_MAX
MAX_SEED_SLOTS = 5   # fits MELON/STRAWBERRY/TOMATO/WHEAT/CARROT

# --- v7.6a: protected crop-hand reservation ---
# Fraction of the current hand count that is walled off for crop-only work
# (watering/weeding/harvest/planting), scaled up once the farm is showing
# real symptoms of neglect rather than always being a flat number.
WEED_RATIO_HIGH = 0.10          # weeds / unlocked-tile-count threshold
CROP_PRESSURE_HAND_MULT = 4     # crop backlog vs. hand count threshold
PROTECTED_FRACTION_LOW = 0.50
PROTECTED_FRACTION_HIGH = 0.70
MIN_RESERVED_CROP_HANDS = 2
TILES_PER_QUAD = 25              # 10x10 board / 4 quadrants

# Weed-priority escalation thresholds (tune TASK_ORDER as infestation grows).
WEED_PRIORITY_THRESHOLD = 5     # promote weeds ahead of ordinary planting
WEED_URGENT_THRESHOLD = 20      # promote weeds ahead of ordinary watering too

# --- v8 candidate D: WHEAT fertilize pipeline ---
FERTILIZER_RESERVE = 8      # keep this many FERTILIZER in shed for wheat use;
                              # the rest still gets sold every turn like v7.9
WHEAT_FERT_MAX_AGE = 2       # only chase the fertilize bonus while age <= 2
                              # (yield window is ages 2-4); a single
                              # application at age 2 covers the whole window

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

CUTOFF = {"WHEAT": 25, "CARROT": 26, "MELON": 16, "STRAWBERRY": 18, "TOMATO": 20}
PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]
PREMIUM_CROPS = {"STRAWBERRY", "MELON"}
ANIMAL_PRODUCTS = ("MILK", "WOOL", "EGG", "FERTILIZER")

# --- instrumentation (v8 candidate D) ---
FERT_STATS = {
    "fertilize_ops": 0, "age_hist": {0: 0, 1: 0, 2: 0},
    "wheat_units_sold": 0, "wheat_revenue": 0.0,
    "fert_units_sold": 0, "fert_units_used_running": 0,
    "printed": False,
}


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
    fert_wheat = []            # v8D: WHEAT tiles eligible for FERTILIZE
    fert_wheat_age = {}        # v8D: pos -> age, for instrumentation

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
                # v8D: WHEAT fertilize eligibility -- age <= 2, not already
                # covering today. See WHEAT_FERT_MAX_AGE header note: a
                # single application at age 2 covers the whole ages-2-4
                # bonus window with one FERTILIZER unit.
                if t.get("crop") == "WHEAT":
                    age = day - t.get("planted_day", day)
                    if 0 <= age <= WHEAT_FERT_MAX_AGE and t.get("fertilized_until_day", -1) < day:
                        fert_wheat.append((x, y))
                        fert_wheat_age[(x, y)] = age

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
        "fert_wheat": fert_wheat, "fert_wheat_age": fert_wheat_age,
    }


# =====================================================================
# ECONOMY
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


def _pending_animal_work(view):
    """Count of pastures with an actual pending need this turn (unfed, ready
    to harvest, needs care, or has fertilizer waiting)."""
    return sum(1 for _pos, t in view["my_pastures"]
               if (not t.get("fed_today", True)) or t.get("yield_units", 0) > 0
                  or (not t.get("cared_today", True)) or t.get("fertilizer_available", False))


def _animal_expansion_feasible(obs, view, budget, shed, n_animals, n_hands, quads):
    """Gate for buying the (n_animals+1)th animal. All five must hold:
      1. Survival: no existing pasture is already missing a feeding.
      2. Wheat affordability: the market-buy needed to cover one more
         animal's feed shortfall, after home-grown wheat, must stay small
         relative to current cash.
      3. Hand capacity (formula): a projected hiring target, covering crops
         plus animal workload, must stay under HAND_TARGET_MAX.
      4. Crops not already neglected (real, not projected): do the hands we
         actually have right now already have their hands full with crop
         backlog alone?
      5. Crop space: reserving one more near-shed tile for a pasture must
         still leave enough open land for crops.
    """
    if any(not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
           for _pos, t in view["my_pastures"]):
        return False

    next_target_wheat = (n_animals + 1) * 2 + FEED_CARRY_TARGET
    have = shed.get("WHEAT", 0)
    shortfall = max(0, next_target_wheat - have)
    shortfall_cost = shortfall * live_price(obs, "WHEAT")
    if shortfall_cost > EXPANSION_WHEAT_BUDGET_FRAC * max(budget, 1):
        return False

    animal_work = _pending_animal_work(view)
    neglect_work = len(view["water"]) + len(view["urgent_water"]) + len(view["harvest"])
    crop_work = neglect_work + len(view["empty"])
    projected_work = crop_work + (animal_work + 1) * ANIMAL_WORK_WEIGHT
    if math.ceil(projected_work / 5) > HAND_TARGET_MAX:
        return False

    if neglect_work > n_hands * CROP_NEGLECT_TASKS_PER_HAND:
        return False

    available_for_crops = len(view["empty"]) - len(reserved_sites) - 1
    if available_for_crops < EXPANSION_MIN_CROP_TILES_PER_QUAD * quads:
        return False

    return True


def _grow_reserved_sites(view):
    """Claim exactly one more near-shed tile for the fleet, called only when
    a new animal purchase actually fires. Picks the nearest still-unclaimed
    empty tile to the shed."""
    candidates = [t for t in view["empty"]
                  if t not in CENTER_TILES and t not in reserved_sites]
    if not candidates:
        return
    candidates.sort(key=lambda t: _dist(t, _nearest_center(t)))
    reserved_sites.append(candidates[0])


def economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans):
    budget = me["money"]
    shed = obs["private"]["shed"]
    inv = obs["market"]["inventory"]
    behind = me["money"] < opp["money"] - 500
    quads = len(me["unlocked_quadrants"])
    # Needed early now that land/seeds run before animal purchase.
    shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)

    strategic_orders = []
    feed_orders = []
    sell_orders = []
    hire_orders = []
    seed_orders = []

    # --- Land expansion ---
    if 1 <= day <= 22:
        if quads == 1 and budget > 1000:
            strategic_orders.append(["BUY_LAND"]); budget -= 1000
        elif quads == 2 and budget > 2000 and day <= 18:
            strategic_orders.append(["BUY_LAND"]); budget -= 2000
        elif quads == 3 and budget > 4000 and day <= 16:
            strategic_orders.append(["BUY_LAND"]); budget -= 4000

    # --- Seed pipeline ---
    ph = phase(day)
    space = len(view["empty"]) + 2
    want = {}
    if day <= CUTOFF["MELON"] and budget > 700:
        melon_target = min(space, 6 if ph == 0 else 10)
        # Throttle new MELON seeds once shed is nearly full, to reduce
        # future force-dump firesales.
        if shed_load > SHED_CAP - 30:
            melon_target = min(melon_target, 3)
        want["MELON"] = melon_target
    if day <= CUTOFF["STRAWBERRY"] and budget > 900:
        want["STRAWBERRY"] = min(space, 6 if ph == 0 else 10)
    if day <= CUTOFF["TOMATO"] and budget > 600:
        want["TOMATO"] = 3   # ongoing crop, same small-standing-patch approach
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
        want["WHEAT"] = 8   # v8D: UNCHANGED from v7.9 -- isolate fertilize effect alone

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

    # --- Animal fleet purchase ---
    n_animals = (len(view["my_pastures"]) +
                 sum(1 for p in animal_plans if p["stage"] in ("BOUGHT", "CARRYING")))
    in_progress = any(p["stage"] in ("BOUGHT", "CARRYING") for p in animal_plans)
    if not in_progress:
        target_plan = next((p for p in animal_plans if p["stage"] == "NONE"), None)
        if target_plan is None:
            for species in ANIMAL_SPECIES_ORDER:
                if species == "SHEEP" and not SHEEP_ENABLED:
                    continue
                if _animal_expansion_feasible(obs, view, budget, shed, n_animals, len(me["hands"]), quads):
                    target_plan = {"species": species, "stage": "NONE", "site": None,
                                    "stage_turn": None, "retries": 0}
                    break
        if target_plan is not None:
            spec = ANIMAL_SPECS[target_plan["species"]]
            if (spec["start_day"] <= day <= spec["last_day"]
                    and shed.get(target_plan["species"], 0) == 0
                    and budget > spec["min_money"]):
                strategic_orders.append(["BUY_ANIMAL", target_plan["species"], 1])
                if target_plan not in animal_plans:
                    animal_plans.append(target_plan)
                _advance(target_plan, "BOUGHT", day, hour)
                budget -= spec["cost"]
                _grow_reserved_sites(view)  # claim a tile now that we've committed

    # --- JIT feed wheat (FEED consumes carried wheat, staged via shed) ---
    if n_animals > 0:
        target_wheat = n_animals * 2 + FEED_CARRY_TARGET
        have = shed.get("WHEAT", 0)
        if have < target_wheat:
            qty = min(target_wheat - have, 10)
            cost = qty * live_price(obs, "WHEAT")
            if budget >= cost:
                feed_orders.append(["BUY_PRODUCT", "WHEAT", qty])
                budget -= cost

    # --- Fertilizer straight to market, minus a reserve for wheat use ---
    # v8D: was "sell everything"; now keep FERTILIZER_RESERVE units in the
    # shed so the fertilize pipeline (fertilize_action, below) has stock
    # to PICKUP for WHEAT tiles.
    fert = shed.get("FERTILIZER", 0)
    fert_sellable = fert - FERTILIZER_RESERVE
    if fert_sellable > 0:
        sell_orders.append(["SELL", "FERTILIZER", fert_sellable])
        FERT_STATS["fert_units_sold"] += fert_sellable

    # --- Paced selling + demand-timing attack ---
    DUMP_TARGET_LOAD = SHED_CAP - 20
    force_dump = shed_load > SHED_CAP - 15 and hour >= 18
    dump_overflow = max(0, shed_load - DUMP_TARGET_LOAD) if force_dump else 0
    is_attack = timing_engine.is_attack_turn(day, hour)
    is_holding = timing_engine.is_holding_phase(day, hour)

    feed_reserve = n_animals * 2 + (FEED_CARRY_TARGET if n_animals else 0)
    sellable = []
    for i, n in shed.items():
        if not (isinstance(n, (int, float)) and n > 0):
            continue
        if i not in MARKET_PARAMS or i == "FERTILIZER" or i in ("COW", "SHEEP", "GOOSE"):
            continue
        if i == "WHEAT":
            n = n - feed_reserve
            if n <= 0:
                continue
        sellable.append((i, n))

    for item, n in sorted(sellable, key=lambda kv: -live_price(obs, kv[0])):
        base = MARKET_PARAMS[item]["base"]
        price_now = live_price(obs, item)
        if is_attack and item in PREMIUM_CROPS:
            qty = max(1, int(n * timing_engine.dump_ratio))
        elif is_holding and item in PREMIUM_CROPS and not force_dump:
            continue
        elif day >= LIQUIDATE_DAY or price_now >= 1.05 * base:
            qty = int(n)
        elif force_dump and dump_overflow > 0:
            dump_floor = 0.5 * base
            want_qty = min(int(n), int(dump_overflow))
            qty = units_sellable_above(item, inv.get(item, I0), dump_floor, want_qty)
            if qty < want_qty:
                qty += min(int(n) - qty, want_qty - qty)
            dump_overflow -= qty
        elif force_dump:
            frac = 0.85 if item in PREMIUM_CROPS else 0.70
            if view["opp_imminent"].get(item, 0) >= 4:
                frac -= 0.25
            floor = frac * base
            relax = max(0.0, 1.0 - max(0, shed_load - 40) / 50.0)
            qty = units_sellable_above(item, inv.get(item, I0), floor * relax, int(n))
        else:
            frac = 0.85 if item in PREMIUM_CROPS else 0.70
            if view["opp_imminent"].get(item, 0) >= 4:
                frac -= 0.25
            if behind and item in PREMIUM_CROPS and day >= 20:
                frac += 0.10
            floor = frac * base
            relax = max(0.0, 1.0 - max(0, shed_load - 40) / 50.0)
            qty = units_sellable_above(item, inv.get(item, I0), floor * relax, int(n))
        if qty > 0:
            sell_orders.append(["SELL", item, qty])
            if item == "WHEAT":  # v8D instrumentation
                FERT_STATS["wheat_units_sold"] += qty
                FERT_STATS["wheat_revenue"] += qty * price_now

    # --- Hiring ---
    if hour == 0 and day < 29:
        animal_work = _pending_animal_work(view)
        work = (len(view["water"]) + len(view["urgent_water"]) +
                len(view["harvest"]) + len(view["empty"]) +
                animal_work * ANIMAL_WORK_WEIGHT)
        target = max(HAND_TARGET_MIN, min(HAND_TARGET_MAX, math.ceil(work / 5)))
        need = max(0, target - len(me["hands"]))
        n = 0
        while n < need and len(hire_orders) < MAX_HIRE_SLOTS:
            cost = FARM_HAND_COST_MULT * _fib(n)
            if budget < cost:
                break
            hire_orders.append(["HIRE"])
            budget -= cost
            n += 1

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

    # v8D: print the mechanism trace on every turn of the last day. The
    # engine's final input observation the agent ever receives tops out at
    # day=29, hour=22 (day=29/hour=23 is only ever a terminal RECORD, never
    # fed back in as an input -- confirmed empirically), so there is no
    # single reliable "last call" day/hour to gate a one-shot print on.
    # Printing every turn from day 29 onward and taking the LAST such line
    # per game (grep) gives the true final, fully-accumulated counters.
    if day >= 29:
        hist = FERT_STATS["age_hist"]
        avg_price = (FERT_STATS["wheat_revenue"] / FERT_STATS["wheat_units_sold"]
                     if FERT_STATS["wheat_units_sold"] else 0.0)
        print(
            f"FERTTRACE fertilize_ops={FERT_STATS['fertilize_ops']} "
            f"age_hist={hist} "
            f"wheat_units_sold={FERT_STATS['wheat_units_sold']} "
            f"wheat_avg_price={avg_price:.1f} "
            f"wheat_revenue={FERT_STATS['wheat_revenue']:.0f} "
            f"fert_units_sold={FERT_STATS['fert_units_sold']}",
            file=sys.stderr,
        )

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
# FERTILIZE PIPELINE (v8 candidate D) -- proactively fetches FERTILIZER
# from the shed and applies it to WHEAT tiles in view["fert_wheat"]
# before their yield-bonus window closes. Mirrors the PICKUP-then-carry
# pattern animal_maintenance_action already uses for WHEAT-as-feed.
# =====================================================================

def fertilize_action(pos, view, shed, carry, day, exclude=()):
    """Returns (op_or_None, claimed_pos_or_None). Only engages when there's
    an eligible WHEAT tile (age <= WHEAT_FERT_MAX_AGE, not yet covering
    today) and either the worker is already carrying FERTILIZER or the
    shed has some to spare above FERTILIZER_RESERVE."""
    targets = [t for t in view["fert_wheat"] if t not in exclude]
    if not targets:
        return None, None
    tpos = _nearest(pos, targets)
    carry_fert = carry.get("FERTILIZER", 0)

    if pos == tpos and carry_fert > 0:
        FERT_STATS["fertilize_ops"] += 1
        age = view.get("fert_wheat_age", {}).get(tpos)
        if age in FERT_STATS["age_hist"]:
            FERT_STATS["age_hist"][age] += 1
        return ["FERTILIZE"], tpos

    if carry_fert > 0:
        return [_step_toward(pos, tpos)], tpos

    avail = shed.get("FERTILIZER", 0) - FERTILIZER_RESERVE
    if avail <= 0:
        return None, None
    if pos in CENTER_TILES:
        return ["PICKUP", "FERTILIZER", 1], tpos
    return [_step_toward(pos, _nearest_center(pos))], tpos


# =====================================================================
# ANIMAL PIPELINE (farmer-owned)
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


def animal_reconcile(plan, view, shed, farmer_carry, day, hour):
    """Verify last turn's animal-setup action against the new observation."""
    species = plan["species"]
    stage = plan["stage"]
    turn = day * 24 + hour
    timed_out = plan.get("stage_turn") is not None and turn - plan["stage_turn"] >= SETUP_STAGE_TIMEOUT
    site = plan.get("site")

    site_occupied = site is not None and any(pos == site for pos, _tile in view["my_pastures"])
    if site_occupied:
        if stage != "ACTIVE":
            _advance(plan, "ACTIVE", day, hour)
        return

    if stage == "BOUGHT":
        if shed.get(species, 0) > 0 or farmer_carry.get(species, 0) > 0:
            pass
        elif timed_out:
            _fail_stage(plan, "NONE")
    elif stage == "ACTIVE":
        if shed.get(species, 0) == 0 and farmer_carry.get(species, 0) == 0:
            _advance(plan, "ABANDONED", day, hour)
    elif stage == "CARRYING" and farmer_carry.get(species, 0) == 0 and shed.get(species, 0) > 0:
        _fail_stage(plan, "BOUGHT")
    elif timed_out and stage not in ("NONE", "ABANDONED"):
        _fail_stage(plan, "NONE" if shed.get(species, 0) == 0 else "BOUGHT")


def animal_setup_action(pos, view, shed, farmer_carry, plan, day, hour, reserved_sites=()):
    """Multi-turn setup for the one in-progress plan. Returns an op, or None
    to release the farmer to maintenance/crop work."""
    species = plan["species"]
    stage = plan["stage"]
    if stage in ("NONE", "ABANDONED", "ACTIVE"):
        return None

    carrying = farmer_carry.get(species, 0) > 0

    site = plan.get("site")
    if site is None or (site not in view["empty"] and site not in view["empty_pastures"]):
        candidates = [t for t in (view["empty_pastures"] or view["empty"])
                      if t not in CENTER_TILES]
        if not candidates:
            return None
        pool = [t for t in reserved_sites if t in candidates] or candidates
        site = min(pool, key=lambda p2: _dist(p2, _nearest_center(p2)))
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


def _pasture_priority(pos, farmer_pos, tile):
    fed = tile.get("fed_today", True)
    urgent = (not fed) and tile.get("consecutive_unfed", 0) >= 1
    if urgent:
        rank = 0
    elif not fed:
        rank = 1
    elif tile.get("yield_units", 0) > 0:
        rank = 2
    elif not tile.get("cared_today", True):
        rank = 3
    elif tile.get("fertilizer_available", False):
        rank = 4
    else:
        rank = 5
    return (rank, _dist(pos, farmer_pos))


def animal_maintenance_action(pos, view, shed, carry, day, hour, exclude=(), critical_only=False):
    candidates = [(p, t) for p, t in view["my_pastures"] if p not in exclude]
    if critical_only:
        candidates = [(p, t) for p, t in candidates if not t.get("fed_today", True)]
    if not candidates:
        return None, None
    (ppos, tile) = min(candidates, key=lambda pt: _pasture_priority(pt[0], pos, pt[1]))

    needs_feed = not tile.get("fed_today", True)
    needs_care = (not critical_only) and (not tile.get("cared_today", True))
    has_yield = (not critical_only) and tile.get("yield_units", 0) > 0
    has_fert = (not critical_only) and tile.get("fertilizer_available", False)
    urgent_feed = needs_feed and tile.get("consecutive_unfed", 0) >= 1
    claim = ppos if (needs_feed or needs_care or has_yield or has_fert) else None

    carry_wheat = carry.get("WHEAT", 0)
    carry_products = {} if critical_only else {i: carry.get(i, 0) for i in ANIMAL_PRODUCTS if carry.get(i, 0) > 0}
    deposit_due = sum(carry_products.values()) >= PRODUCT_DEPOSIT_AT or (
        carry_products and (needs_feed and carry_wheat == 0))
    fetch_wheat_due = needs_feed and carry_wheat == 0 and shed.get("WHEAT", 0) > 0

    if pos == ppos:
        if needs_feed and carry_wheat > 0:
            return ["FEED"], claim
        if has_yield:
            return ["HARVEST"], claim
        if needs_care:
            return ["CARE"], claim
        if has_fert:
            return ["COLLECT_FERTILIZER"], claim

    if pos in CENTER_TILES:
        if fetch_wheat_due and urgent_feed:
            return ["PICKUP", "WHEAT", min(FEED_CARRY_TARGET, shed.get("WHEAT", 0))], claim
        if carry_products:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]], claim
        if fetch_wheat_due:
            return ["PICKUP", "WHEAT", min(FEED_CARRY_TARGET, shed.get("WHEAT", 0))], claim

    if fetch_wheat_due and urgent_feed:
        return [_step_toward(pos, _nearest_center(pos))], claim
    if fetch_wheat_due or deposit_due:
        return [_step_toward(pos, _nearest_center(pos))], claim
    if (needs_feed and carry_wheat > 0) or has_yield or needs_care or has_fert:
        return [_step_toward(pos, ppos)], claim

    if day >= LIQUIDATE_DAY and carry_products:
        if pos in CENTER_TILES:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]], claim
        return [_step_toward(pos, _nearest_center(pos))], claim

    return None, None


# =====================================================================
# CROP TASK ALLOCATION
# =====================================================================

TASK_ACTION = {
    "urgent_water": ["WATER"],
    "harvest": ["HARVEST"],
    "water": ["WATER"],
    "weeds": ["DIG"],
}


def _task_order(n_weeds):
    if n_weeds >= WEED_URGENT_THRESHOLD:
        return ["urgent_water", "harvest", "weeds", "water", "plant"]
    if n_weeds >= WEED_PRIORITY_THRESHOLD:
        return ["urgent_water", "harvest", "water", "weeds", "plant"]
    return ["urgent_water", "harvest", "water", "plant", "weeds"]


def unit_action(pos, tasks, seeds, day, task_order):
    x, y = pos
    for key in task_order:
        if (x, y) in tasks[key]:
            tasks[key].remove((x, y))
            if key == "plant":
                for crop in plantable_crops(seeds, day):
                    seeds[crop] -= 1
                    tasks["urgent_water"].append((x, y))
                    return ["PLANT", crop]
                continue
            return TASK_ACTION[key]

    for key in task_order:
        tgt = _nearest((x, y), tasks[key])
        if tgt:
            step = _step_toward((x, y), tgt)
            if step:
                tasks[key].remove(tgt)
                return [step]

    fallback = _step_toward((x, y), (4, 4))
    return [fallback] if fallback else ["PASS"]


# =====================================================================
# ENTRY
# =====================================================================

timing_engine = DemandTimingEngine(match_seed=42)
animal_plans = []
reserved_sites = []


def _init_reserved_sites(view):
    return reserved_sites


def _reserved_crop_hand_count(view, seeds, day, n_hands, quads):
    if n_hands <= 0:
        return 0
    unlocked_tiles = max(1, TILES_PER_QUAD * max(1, quads))
    weed_ratio = len(view["weeds"]) / unlocked_tiles
    plantable = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(c, 0) for c in plantable)
    crop_pressure = (len(view["urgent_water"]) + len(view["water"]) +
                      len(view["weeds"]) + min(len(view["empty"]), n_plantable))
    if weed_ratio >= WEED_RATIO_HIGH or crop_pressure > n_hands * CROP_PRESSURE_HAND_MULT:
        fraction = PROTECTED_FRACTION_HIGH
    else:
        fraction = PROTECTED_FRACTION_LOW
    return min(n_hands, max(MIN_RESERVED_CROP_HANDS, math.ceil(n_hands * fraction)))


def _agent(obs):
    p = obs["player"]
    me, opp = obs["farms"][p], obs["farms"][1 - p]
    day, hour = obs["day"], obs["hour"]
    seeds = dict(obs["private"]["seeds"])
    shed = obs["private"]["shed"]

    inventories = obs["private"].get("inventories") or []
    farmer_carry = inventories[0] if inventories else {}

    view = perceive(me, opp, day)
    sites = _init_reserved_sites(view)
    for plan in animal_plans:
        animal_reconcile(plan, view, shed, farmer_carry, day, hour)

    market = economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans)

    crops_now = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(c, 0) for c in crops_now)

    task_order = _task_order(len(view["weeds"]))
    tasks = {
        "urgent_water": list(view["urgent_water"]),
        "harvest": list(view["harvest"]),
        "water": list(view["water"]),
        "plant": (view["empty"][:n_plantable] if crops_now and hour < 21 else []),
        "weeds": list(view["weeds"]),
    }
    claimed_sites = {pl["site"] for pl in animal_plans if pl.get("site") and pl["stage"] != "ABANDONED"}
    excluded = claimed_sites | set(sites)
    if excluded:
        tasks["plant"] = [t for t in tasks["plant"] if t not in excluded]

    quads = len(me["unlocked_quadrants"])
    n_hands = len(me["hands"])
    reserved_count = _reserved_crop_hand_count(view, seeds, day, n_hands, quads)

    farmer_pos = tuple(me["farmer"])
    active_setup_plan = next((pl for pl in animal_plans if pl["stage"] in ("BOUGHT", "CARRYING")), None)
    urgent_existing_feed = any(
        not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
        for _pos, t in view["my_pastures"]
    )
    claimed_pastures = set()
    claimed_fert = set()   # v8D
    farmer_op = None
    if active_setup_plan is not None and not urgent_existing_feed:
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        farmer_op, claim = animal_maintenance_action(farmer_pos, view, shed, farmer_carry, day, hour, claimed_pastures)
        if claim is not None:
            claimed_pastures.add(claim)
    if farmer_op is None and active_setup_plan is not None:
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        # v8D: fertilize-wheat gets priority over ordinary crop work
        # (ahead of the plain WATER task) when the farmer has nothing more
        # urgent to do.
        farmer_op, fclaim = fertilize_action(farmer_pos, view, shed, farmer_carry, day, claimed_fert)
        if fclaim is not None:
            claimed_fert.add(fclaim)
    if farmer_op is None:
        farmer_op = unit_action(farmer_pos, tasks, seeds, day, task_order)

    hand_ops = []
    for i, h in enumerate(me["hands"]):
        hand_pos = tuple(h)
        hand_carry = inventories[i + 1] if len(inventories) > i + 1 else {}
        is_reserved = i < reserved_count
        op, claim = animal_maintenance_action(hand_pos, view, shed, hand_carry, day, hour,
                                                claimed_pastures, critical_only=is_reserved)
        if op is not None:
            hand_ops.append(op)
            if claim is not None:
                claimed_pastures.add(claim)
            continue
        # v8D: fertilize-wheat before falling to ordinary crop tasks.
        fop, fclaim = fertilize_action(hand_pos, view, shed, hand_carry, day, claimed_fert)
        if fop is not None:
            hand_ops.append(fop)
            if fclaim is not None:
                claimed_fert.add(fclaim)
        else:
            hand_ops.append(unit_action(hand_pos, tasks, seeds, day, task_order))

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
