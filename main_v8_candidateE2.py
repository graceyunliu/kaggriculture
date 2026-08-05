import math
import random
import sys

# =====================================================================
# MAIN V8 CANDIDATE E2 -- same as Candidate E, with one bug fix to the
# feasibility-gate change (see item 3 below). E's first cut used
# standing_crop_demand = sum(want.values()) -- the WHOLE crop portfolio's
# standing target (melon/strawberry/tomato/carrot/wheat), not just the
# part this candidate actually changed. That subtracted ~30-40 tiles of
# land from the feasibility check from day 1 regardless of wheat target
# size, which made available_for_crops negative almost immediately and
# blocked EVERY animal purchase all game -- peak_animals=0 the whole
# match (confirmed by mechanism trace; v7.9 itself reaches 8-10), and E
# lost catastrophically (-$87,256 mean/11 seeds) largely because of that,
# not because of the fertilize/bigger-wheat/order-priority hypothesis
# actually being tested. E2 uses only the INCREMENTAL wheat demand this
# candidate itself added over v7.9's baseline of 8 -- see the change to
# standing_crop_demand below.
#
# MAIN V8 CANDIDATE E -- fertilize WHEAT (Candidate D) + bigger WHEAT
# target + v7.11's cost-of-delay order priority + a fixed animal-
# expansion feasibility gate. Base: main_v8_candidateD.py (which is
# base v7.9 + the fertilize pipeline).
#
# --- What changed vs Candidate D ---
#
#  1. want["WHEAT"]: 8 -> min(space, 16). Conservative vs the prior
#     round's B3 (25-40), which lost decisively; also not B2's low
#     value, which also lost. Starting point only -- see report for
#     whether this needs another round.
#  2. economy()'s market-order assembly: replaced with v7.11's
#     cost-of-delay priority-scored single list (validated standalone,
#     +$5,143/11 seeds, ~7% uplift, prior round). See main_v7.11.py for
#     the untouched original; folded in here byte-for-byte apart from
#     the want["WHEAT"] and FERTILIZER-reserve/instrumentation changes
#     Candidate D already made.
#  3. _animal_expansion_feasible(): FIXED. Candidate D's own numbers
#     (see report) showed peak animal fleet size jumping to 13-16 vs
#     v7.9's 8-10 EVEN WITHOUT touching want["WHEAT"] -- just adding the
#     fertilize pipeline was enough to trigger it, because hands
#     diverted to fertilize trips plant seeds more slowly, so
#     view["empty"] (unplanted tiles) stays inflated turn over turn, and
#     the feasibility gate's "available_for_crops" reads that inflated
#     empty-tile count as spare land, waving through animal purchases
#     the labor force can't actually service once all that standing
#     crop demand (now MUCH bigger at want["WHEAT"]=16) gets planted.
#     The gate now subtracts `standing_crop_demand` (sum of this turn's
#     `want` dict -- the crop population the plan is actively trying to
#     reach, not just what's literally unplanted right now) from both
#     the crop-space check and the hand-capacity projection, so a bigger
#     wheat target (or slower planting from any cause) tightens the
#     gate instead of loosening it. Goal: keep the fleet in the ~8-10
#     range v7.9 itself sustains, not 13+.
#
# See main_v8_candidateD.py's header for the fertilize-mechanic
# derivation (why WHEAT not STRAWBERRY, the age<=2 timing window) --
# unchanged here.
# =====================================================================

PRICE_FLOOR = 1
I0 = 10_000
SHED_CAP = 100
LIQUIDATE_DAY = 28
MAX_MARKET_ORDERS = 10

BOARD = 10
CENTER_TILES = [(4, 4), (4, 5), (5, 4), (5, 5)]

ANIMAL_SPECS = {
    "COW":   {"cost": 400, "min_money": 700, "start_day": 0,  "last_day": 22},
    "SHEEP": {"cost": 500, "min_money": 800, "start_day": 3,  "last_day": 22},
}
ANIMAL_SPECIES_ORDER = ["COW", "SHEEP"]
SHEEP_ENABLED = False

EXPANSION_WHEAT_BUDGET_FRAC = 0.15
EXPANSION_MIN_CROP_TILES_PER_QUAD = 8

CROP_NEGLECT_TASKS_PER_HAND = 5
ANIMAL_WORK_WEIGHT = 2

SETUP_STAGE_TIMEOUT = 12
SETUP_MAX_RETRIES = 3
FEED_CARRY_TARGET = 2
PRODUCT_DEPOSIT_AT = 3

FARM_HAND_COST_MULT = 1
HAND_TARGET_MIN = 4
HAND_TARGET_MAX = 18

MAX_HIRE_SLOTS = HAND_TARGET_MAX
MAX_SEED_SLOTS = 5

WEED_RATIO_HIGH = 0.10
CROP_PRESSURE_HAND_MULT = 4
PROTECTED_FRACTION_LOW = 0.50
PROTECTED_FRACTION_HIGH = 0.70
MIN_RESERVED_CROP_HANDS = 2
TILES_PER_QUAD = 25

WEED_PRIORITY_THRESHOLD = 5
WEED_URGENT_THRESHOLD = 20

# --- v8 candidate D: WHEAT fertilize pipeline (unchanged from D) ---
FERTILIZER_RESERVE = 8
WHEAT_FERT_MAX_AGE = 2

# --- v8 candidate E: bigger wheat target ---
WHEAT_TARGET_CAP = 16   # was 8 in v7.9/candidate D

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

# --- instrumentation (v8 candidate D/E) ---
FERT_STATS = {
    "fertilize_ops": 0, "age_hist": {0: 0, 1: 0, 2: 0},
    "wheat_units_sold": 0, "wheat_revenue": 0.0,
    "fert_units_sold": 0,
    "peak_animals": 0,
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
    my_pastures = []
    empty_pastures = []
    fert_wheat = []
    fert_wheat_age = {}

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
    return sum(1 for _pos, t in view["my_pastures"]
               if (not t.get("fed_today", True)) or t.get("yield_units", 0) > 0
                  or (not t.get("cared_today", True)) or t.get("fertilizer_available", False))


def _animal_expansion_feasible(obs, view, budget, shed, n_animals, n_hands, quads, standing_crop_demand=0):
    """Gate for buying the (n_animals+1)th animal. v8E fix: takes an extra
    `standing_crop_demand` argument (sum of this turn's `want` dict --
    the crop population the plan is actively trying to reach) and
    subtracts/adds it in the crop-space and hand-capacity checks below,
    so a bigger crop target (or slower planting from labor diverted
    elsewhere, e.g. the fertilize pipeline) tightens the gate instead of
    silently loosening it via an inflated view["empty"] count. See the
    header comment for the Candidate D evidence (peak fleet 13-16 vs
    v7.9's 8-10) that motivated this."""
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
    crop_work = neglect_work + len(view["empty"]) + standing_crop_demand
    projected_work = crop_work + (animal_work + 1) * ANIMAL_WORK_WEIGHT
    if math.ceil(projected_work / 5) > HAND_TARGET_MAX:
        return False

    if neglect_work > n_hands * CROP_NEGLECT_TASKS_PER_HAND:
        return False

    available_for_crops = len(view["empty"]) - len(reserved_sites) - 1 - standing_crop_demand
    if available_for_crops < EXPANSION_MIN_CROP_TILES_PER_QUAD * quads:
        return False

    return True


def _grow_reserved_sites(view):
    candidates = [t for t in view["empty"]
                  if t not in CENTER_TILES and t not in reserved_sites]
    if not candidates:
        return
    candidates.sort(key=lambda t: _dist(t, _nearest_center(t)))
    reserved_sites.append(candidates[0])


# --- v7.11: cost-of-delay order priority scores (unchanged from
# main_v7.11.py -- see that file's header for the full rationale) ---
PRIORITY_ENORMOUS         = 1000
PRIORITY_HIGH             = 700
PRIORITY_HIGH_CAPACITY    = 760
PRIORITY_HIGH_FINAL       = 730
PRIORITY_HIGH_ATTACK      = 715
PRIORITY_HIGH_HIRE        = 700
PRIORITY_MEDIUM_RISING_LO = 400
PRIORITY_MEDIUM_RISING_HI = 690
PRIORITY_MEDIUM           = 320
PRIORITY_FEED_ROUTINE     = 340
PRIORITY_NEAR_ZERO        = 80
PRIORITY_LAND_IDLE        = 15
PRIORITY_LAND_SCARCE      = 320

LAND_IDLE_TILE_THRESHOLD = 15


def _land_priority(view):
    idle = len(view["empty"])
    return PRIORITY_LAND_SCARCE if idle < LAND_IDLE_TILE_THRESHOLD else PRIORITY_LAND_IDLE


def _seed_priority(crop, day):
    cutoff = CUTOFF.get(crop, day)
    span = max(1, cutoff)
    days_left = max(0, cutoff - day)
    urgency = 1.0 - min(1.0, days_left / span)
    return PRIORITY_MEDIUM_RISING_LO + urgency * (PRIORITY_MEDIUM_RISING_HI - PRIORITY_MEDIUM_RISING_LO)


def _feed_priority(view):
    if any(not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
           for _pos, t in view["my_pastures"]):
        return PRIORITY_ENORMOUS
    return PRIORITY_FEED_ROUTINE


def _sell_priority(reason, shed_load):
    if reason == "capacity":
        return PRIORITY_HIGH_CAPACITY
    if reason == "final":
        return PRIORITY_HIGH_FINAL
    if reason == "attack":
        return PRIORITY_HIGH_ATTACK
    room = max(0, SHED_CAP - shed_load)
    fullness = 1.0 - min(1.0, room / SHED_CAP)
    return PRIORITY_NEAR_ZERO + fullness * (PRIORITY_MEDIUM_RISING_LO - PRIORITY_NEAR_ZERO)


def economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans):
    budget = me["money"]
    shed = obs["private"]["shed"]
    inv = obs["market"]["inventory"]
    behind = me["money"] < opp["money"] - 500
    quads = len(me["unlocked_quadrants"])
    shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)

    priced_orders = []
    seed_orders_n = 0

    # --- Land expansion ---
    if 1 <= day <= 22:
        land_score = _land_priority(view)
        if quads == 1 and budget > 1000:
            priced_orders.append((land_score, ["BUY_LAND"])); budget -= 1000
        elif quads == 2 and budget > 2000 and day <= 18:
            priced_orders.append((land_score, ["BUY_LAND"])); budget -= 2000
        elif quads == 3 and budget > 4000 and day <= 16:
            priced_orders.append((land_score, ["BUY_LAND"])); budget -= 4000

    # --- Seed pipeline ---
    ph = phase(day)
    space = len(view["empty"]) + 2
    want = {}
    if day <= CUTOFF["MELON"] and budget > 700:
        melon_target = min(space, 6 if ph == 0 else 10)
        if shed_load > SHED_CAP - 30:
            melon_target = min(melon_target, 3)
        want["MELON"] = melon_target
    if day <= CUTOFF["STRAWBERRY"] and budget > 900:
        want["STRAWBERRY"] = min(space, 6 if ph == 0 else 10)
    if day <= CUTOFF["TOMATO"] and budget > 600:
        want["TOMATO"] = 3
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
        want["WHEAT"] = min(space, WHEAT_TARGET_CAP)   # v8E: 8 -> min(space, 16)

    reserve = 500 if ph == 0 else 200
    for crop, tgt in want.items():
        if seed_orders_n >= MAX_SEED_SLOTS:
            break
        have = seeds.get(crop, 0)
        if have < tgt:
            k = tgt - have
            cost = CROPS[crop]["seed"] * k
            if budget - reserve >= cost:
                priced_orders.append((_seed_priority(crop, day), ["BUY_SEED", crop, k]))
                seed_orders_n += 1
                budget -= cost

    # v8E2: E's first cut used sum(want.values()) here -- the WHOLE crop
    # portfolio's standing target, not just the part that changed. That
    # subtracted ~30-40 tiles of "phantom" land from every feasibility
    # check from day 1 (melon/strawberry/etc targets v7.9 already carries
    # at the same level), which made available_for_crops negative almost
    # immediately and blocked EVERY animal purchase all game --
    # peak_animals=0, confirmed by the mechanism trace (v7.9 itself
    # reaches 8-10). That's not a test of the hypothesis, it's a new bug.
    # v8E2 instead uses only the INCREMENTAL demand this candidate itself
    # added over v7.9's original want["WHEAT"]=8 baseline -- the actual
    # quantity the header comment's fix was meant to account for.
    standing_crop_demand = max(0, want.get("WHEAT", 0) - 8)

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
                if _animal_expansion_feasible(obs, view, budget, shed, n_animals, len(me["hands"]), quads,
                                                standing_crop_demand):
                    target_plan = {"species": species, "stage": "NONE", "site": None,
                                    "stage_turn": None, "retries": 0}
                    break
        if target_plan is not None:
            spec = ANIMAL_SPECS[target_plan["species"]]
            if (spec["start_day"] <= day <= spec["last_day"]
                    and shed.get(target_plan["species"], 0) == 0
                    and budget > spec["min_money"]):
                priced_orders.append((PRIORITY_MEDIUM, ["BUY_ANIMAL", target_plan["species"], 1]))
                if target_plan not in animal_plans:
                    animal_plans.append(target_plan)
                _advance(target_plan, "BOUGHT", day, hour)
                budget -= spec["cost"]
                _grow_reserved_sites(view)

    # --- JIT feed wheat ---
    if n_animals > 0:
        target_wheat = n_animals * 2 + FEED_CARRY_TARGET
        have = shed.get("WHEAT", 0)
        if have < target_wheat:
            qty = min(target_wheat - have, 10)
            cost = qty * live_price(obs, "WHEAT")
            if budget >= cost:
                priced_orders.append((_feed_priority(view), ["BUY_PRODUCT", "WHEAT", qty]))
                budget -= cost

    # --- Fertilizer straight to market, minus a reserve for wheat use ---
    fert = shed.get("FERTILIZER", 0)
    fert_sellable = fert - FERTILIZER_RESERVE
    if fert_sellable > 0:
        priced_orders.append((_sell_priority("paced", shed_load), ["SELL", "FERTILIZER", fert_sellable]))
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
        reason = "paced"
        if is_attack and item in PREMIUM_CROPS:
            qty = max(1, int(n * timing_engine.dump_ratio))
            reason = "attack"
        elif is_holding and item in PREMIUM_CROPS and not force_dump:
            continue
        elif day >= LIQUIDATE_DAY:
            qty = int(n)
            reason = "final"
        elif price_now >= 1.05 * base:
            qty = int(n)
        elif force_dump and dump_overflow > 0:
            dump_floor = 0.5 * base
            want_qty = min(int(n), int(dump_overflow))
            qty = units_sellable_above(item, inv.get(item, I0), dump_floor, want_qty)
            if qty < want_qty:
                qty += min(int(n) - qty, want_qty - qty)
            dump_overflow -= qty
            reason = "capacity"
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
            priced_orders.append((_sell_priority(reason, shed_load), ["SELL", item, qty]))
            if item == "WHEAT":
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
        hire_count = 0
        while n < need and hire_count < MAX_HIRE_SLOTS:
            cost = FARM_HAND_COST_MULT * _fib(n)
            if budget < cost:
                break
            priced_orders.append((PRIORITY_HIGH_HIRE, ["HIRE"]))
            hire_count += 1
            budget -= cost
            n += 1

    priced_orders.sort(key=lambda po: -po[0])
    orders = [order for _score, order in priced_orders[:MAX_MARKET_ORDERS]]

    # v8D/E: mechanism trace, printed every turn of the last day (see
    # main_v8_candidateD.py's comment on why day=29/hour=23 is never an
    # actual input observation -- take the LAST such line per game).
    n_animals_now = len(view["my_pastures"])
    FERT_STATS["peak_animals"] = max(FERT_STATS["peak_animals"], n_animals_now)
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
            f"fert_units_sold={FERT_STATS['fert_units_sold']} "
            f"peak_animals={FERT_STATS['peak_animals']}",
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
# FERTILIZE PIPELINE (unchanged from Candidate D)
# =====================================================================

def fertilize_action(pos, view, shed, carry, day, exclude=()):
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
    claimed_fert = set()
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
