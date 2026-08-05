import math
import random
import sys

# =====================================================================
# MAIN V7.4 — BLUE OCEAN EXPERIMENT
#
# Experimental smoke-test branch based on v7.2. This branch intentionally
# tests three hypotheses together for a fast top-bot matchup:
#   1. A compact 3-cow fleet with daily CARE can outperform a larger,
#      weakly-cared fleet on product output per pasture tile.
#   2. One dedicated hand can supply CARE without consuming the farmer's
#      feed/harvest/deposit logistics budget.
#   3. Bounded BUY_PRODUCT WHEAT orders can raise the opponent's feed cost
#      when the opponent visibly operates a large animal fleet.
#
# This is NOT a validated champion candidate. It is deliberately instrumented
# and guarded for a quick smoke/A-B test. The engine does not support choosing
# a sale price, so "fertilizer dump at $1" is represented by selling all
# available fertilizer immediately and letting the market curve determine price.
# =====================================================================
# MAIN V7.2 BASE
#
# Base: v7.1, unchanged in every way except the animal pipeline. v7.1's
# single `cow_state` dict (one animal, forever) is replaced with a
# generic `animal_plans` list so the farmer can sequentially set up
# MULTIPLE animals, of MULTIPLE species (COW + SHEEP), instead of one
# cow for the whole match. See kaggriculture-agent-design.md 5d for the
# full rationale — summary:
#
#   v7.1's diagnostic run (starter opponent, full 720-step episode)
#   showed it selling 0 WOOL and only 18 MILK / 17 FERTILIZER, vs. the
#   observed top-2 leaderboard baseline (Savko / Subin An, who run the
#   same underlying script) selling 864 MILK / 487 WOOL / 445
#   FERTILIZER from a deliberately-built 8-cow + 6-sheep fleet by day
#   10. v7.1's cow-buy gate (`not view["my_pastures"]`) makes a SECOND
#   cow purchase structurally impossible, and SHEEP never appears in a
#   BUY_ANIMAL call anywhere in the file. This is a bigger gap than any
#   of the tuning questions (HAND_TARGET_MAX, SE-quadrant timing) raised
#   before it.
#
# Design choice: SEQUENTIAL, not concurrent, animal setup. Only one
# plan is ever in stage BOUGHT/CARRYING at a time — the single farmer
# finishes placing (or abandons) one animal before the next purchase
# fires. This keeps the state machine identical in shape to v7.1's
# (just keyed by plan instead of a bare dict) and avoids the harder
# problem of one farmer juggling multiple simultaneous carries.
#
# Two real maintenance-side bugs were found and fixed via local A/B
# testing once a second pasture existed (both invisible with v7.1's
# single cow, since there was never a second pasture to neglect):
#   1. Site selection could put a late-bought animal's pasture far from
#      the shed once nearby tiles were already planted with crops — a
#      single farmer visiting a far pasture every day, on top of the
#      near one plus wheat/product shed trips, could blow the 24-turn
#      daily budget and miss 2 feedings running, losing the animal for
#      good. Fixed by reserving FLEET_TARGET-total near-shed tiles for
#      pastures from turn one (see _init_reserved_sites), regardless of
#      when the actual purchase fires.
#   2. animal_maintenance_action (née cow_maintenance_action) picked the
#      PHYSICALLY NEAREST pasture every turn, not the one with the most
#      urgent pending need — with only one pasture this was a no-op, but
#      with two+ it meant the farmer could return to an already-fed
#      nearby pasture turn after turn while a farther one starved.
#      Fixed with need-based priority ranking (_pasture_priority):
#      urgent feed > any feed > harvest > care > fertilizer > nothing,
#      distance only as a tiebreak.
#
# FLEET_TARGET below is the deliberate scaling knob (see design doc
# decision log): tested at {"COW": 2} (clean win, 0 losses), {"COW": 4}
# (clean win, 0 losses, ~55-65% more money than v7.1), then {"COW": 4,
# "SHEEP": 2} and {"COW": 6} — BOTH of which caused a catastrophic
# economy collapse (final money ~$2-5k vs v7.1's ~$20k+, not a graceful
# degradation) from feed-wheat cost scaling plus reserved-tile crop-
# capacity loss overwhelming a single farmer's daily budget/attention at
# 6 total animals. Shipped at the validated safe ceiling, {"COW": 4,
# "SHEEP": 0} — the SHEEP purchase pipeline exists and was verified to
# work correctly in isolation, it's just not turned on here. Pushing
# past 4 animals is left for a future v7.3 with either a feasibility
# gate before each purchase or a second hand dedicated to animal duty —
# not attempted in this file. STRAWBERRY was added to the crop mix only
# after fertilizer logistics were confirmed reliable at the 4-cow scale
# (15 FERTILIZER/game sold consistently); it improved final money
# further with no crowding-out of MELON (the dominant profit driver)
# observed in testing.
#
# Each scaling step above was verified via seeded local self-play against
# v7.1 before moving on, watching for the single-farmer bottleneck
# flagged as the real risk of scaling animals (not purchase cost).
#
# Final shipped result: 20/20 seeded head-to-head wins vs v7.1 (~$21-28k
# vs v7.1's ~$13-16k on the same seeds), zero animals lost in any run,
# zero crashes across starter/random/pass opponents and a truncated
# 48-turn episode.
# =====================================================================

PRICE_FLOOR = 1
I0 = 10_000
SHED_CAP = 100
LIQUIDATE_DAY = 28
MAX_MARKET_ORDERS = 10

BOARD = 10
CENTER_TILES = [(4, 4), (4, 5), (5, 4), (5, 5)]

# --- Animal fleet config (verified against vendor/kaggle_environments_engine/kaggriculture.py
# ANIMALS dict: COW cost=400/first_yield_day=8/interval=2/max_held=6/product=MILK,
# SHEEP cost=500/first_yield_day=6/interval=3/max_held=6/product=WOOL. Both use
# structure="PASTURE" — confirmed via engine's PLACE handler that any built PASTURE
# tile accepts either species, so no separate site-type bookkeeping is needed.) ---
ANIMAL_SPECS = {
    "COW":   {"cost": 400, "min_money": 900, "start_day": 8,  "last_day": 18},
    "SHEEP": {"cost": 500, "min_money": 800, "start_day": 3,  "last_day": 22},
}
ANIMAL_SPECIES_ORDER = ["COW", "SHEEP"]   # priority when more than one species is under target
FLEET_TARGET = {"COW": 3, "SHEEP": 0}     # SCALING KNOB — validated safe ceiling for a single farmer,
                                           # see design doc 5d: 6 total animals (4+2 or 6+0, tested both)
                                           # caused a catastrophic economy collapse (~$2-5k final vs
                                           # v7.1's ~$20k+), not a graceful degradation — feed-wheat cost
                                           # scaling plus reserved-tile crop-capacity loss overwhelmed the
                                           # single farmer's daily budget/attention. Pushing past 4 needs a
                                           # feasibility gate or a dedicated second hand, not just a bigger
                                           # number — left for a future v7.3, not attempted here.

SETUP_STAGE_TIMEOUT = 12
SETUP_MAX_RETRIES = 3
FEED_CARRY_TARGET = 2
PRODUCT_DEPOSIT_AT = 3         # PLACE milk/wool when carrying this many

# --- V7.4 experiment controls ---
DEDICATED_CARE_HAND = True
WHEAT_CHOKE_START_DAY = 15
WHEAT_CHOKE_END_DAY = 25
WHEAT_CHOKE_OPP_ANIMALS = 4
WHEAT_CHOKE_QTY = 20           # one order/day, not one order/turn
WHEAT_CHOKE_MAX_PRICE = 55     # stop before manipulation becomes ruinous
WHEAT_CHOKE_MIN_CASH = 1800    # preserve operating liquidity
WHEAT_CHOKE_MAX_CASH_SHARE = 0.18

# --- Real hiring cost model (kaggriculture.py: FARM_HAND_COST_MULT=1, fib(0)=1,1,2,3,5,...) ---
FARM_HAND_COST_MULT = 1
HAND_TARGET_MIN = 4
HAND_TARGET_MAX = 18           # unchanged from v7.1 — see that file's header for why a lower
                                # cap was tried and rejected (2.5x money loss head-to-head)

# --- Market-order category slot reservations (unchanged from v7.1) ---
MAX_HIRE_SLOTS = HAND_TARGET_MAX
MAX_SEED_SLOTS = 4   # bumped from 3 to fit STRAWBERRY alongside MELON/CARROT/WHEAT

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

CUTOFF = {"WHEAT": 25, "CARROT": 26, "MELON": 16, "STRAWBERRY": 18}
# STRAWBERRY added after fertilizer logistics were confirmed working at the
# 4-cow fleet size (15 FERTILIZER/game sold reliably, see design doc 5d) —
# ranked below MELON (the dominant profit driver, don't compete with it for
# hand time/planting slots) but above CARROT/WHEAT since it's a premium crop.
PLANT_PRIORITY = ["MELON", "STRAWBERRY", "CARROT", "WHEAT"]
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
# PERCEPTION (unchanged from v7.1 — already species-agnostic: any
# PASTURE tile with an "animal" key counts, regardless of which one)
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
# ECONOMY (v7.1 unchanged except the animal-purchase block, generalized
# from one cow slot to a fleet loop over `animal_plans`)
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


def count_visible_animals(farm):
    """Count animals directly visible on opponent pasture/coop tiles."""
    total = 0
    for row in farm.get("tiles", []):
        for tile in row:
            if isinstance(tile, dict) and tile.get("animal"):
                total += 1
    return total


def economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans):
    budget = me["money"]
    shed = obs["private"]["shed"]
    inv = obs["market"]["inventory"]
    behind = me["money"] < opp["money"] - 500
    quads = len(me["unlocked_quadrants"])

    strategic_orders = []
    feed_orders = []
    manipulation_orders = []
    sell_orders = []
    hire_orders = []
    seed_orders = []

    # --- Animal fleet purchase (generalized from v7.1's single cow_state) ---
    # Serialized: only start a new purchase (or retry a stalled one) if nothing
    # is currently BOUGHT/CARRYING — one farmer can only build+carry+place one
    # animal at a time, so there's no benefit to buying a second before the
    # first is resolved, and it would just sit unclaimed risking the shed cap.
    in_progress = any(p["stage"] in ("BOUGHT", "CARRYING") for p in animal_plans)
    if not in_progress:
        target_plan = next((p for p in animal_plans if p["stage"] == "NONE"), None)
        if target_plan is None:
            for species in ANIMAL_SPECIES_ORDER:
                active = sum(1 for p in animal_plans
                             if p["species"] == species and p["stage"] == "ACTIVE")
                if active < FLEET_TARGET.get(species, 0):
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

    # --- Aggressive land expansion (v5/v7.1, unchanged) ---
    if 1 <= day <= 22:
        if quads == 1 and budget > 1000:
            strategic_orders.append(["BUY_LAND"]); budget -= 1000
        elif quads == 2 and budget > 2000 and day <= 18:
            strategic_orders.append(["BUY_LAND"]); budget -= 2000
        elif quads == 3 and budget > 4000 and day <= 16:
            strategic_orders.append(["BUY_LAND"]); budget -= 4000

    # --- JIT feed wheat (FEED consumes carried wheat, staged via shed) ---
    n_animals = (len(view["my_pastures"]) +
                 sum(1 for p in animal_plans if p["stage"] in ("BOUGHT", "CARRYING")))
    if n_animals > 0:
        target_wheat = n_animals * 2 + FEED_CARRY_TARGET
        have = shed.get("WHEAT", 0)
        if have < target_wheat:
            qty = min(target_wheat - have, 10)
            cost = qty * live_price(obs, "WHEAT")
            if budget >= cost:
                feed_orders.append(["BUY_PRODUCT", "WHEAT", qty])
                budget -= cost

    # --- V7.4 Wheat chokehold experiment ---
    # Run once per day and only against a visibly animal-heavy opponent.
    # Price, liquidity, and spend-share guards keep this from becoming an
    # unconditional capital bonfire. This buys market wheat in addition to
    # our survival reserve above.
    opp_animals = count_visible_animals(opp)
    wheat_price = live_price(obs, "WHEAT")
    if (hour == 0
            and WHEAT_CHOKE_START_DAY <= day <= WHEAT_CHOKE_END_DAY
            and opp_animals >= WHEAT_CHOKE_OPP_ANIMALS
            and wheat_price <= WHEAT_CHOKE_MAX_PRICE
            and budget >= WHEAT_CHOKE_MIN_CASH):
        affordable = int((budget * WHEAT_CHOKE_MAX_CASH_SHARE) // max(1, wheat_price))
        choke_qty = min(WHEAT_CHOKE_QTY, affordable)
        if choke_qty > 0:
            manipulation_orders.append(["BUY_PRODUCT", "WHEAT", choke_qty])
            budget -= choke_qty * wheat_price

    # --- Fertilizer straight to market ---
    fert = shed.get("FERTILIZER", 0)
    if fert > 0:
        sell_orders.append(["SELL", "FERTILIZER", fert])

    # --- Paced selling + demand-timing attack (unchanged) ---
    shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)
    force_dump = shed_load > SHED_CAP - 15 and hour >= 18
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
        elif force_dump or day >= LIQUIDATE_DAY or price_now >= 1.05 * base:
            qty = int(n)
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

    # --- Hiring: real Fibonacci cost, unchanged from v7.1 ---
    if hour == 0 and day < 29:
        work = (len(view["water"]) + len(view["urgent_water"]) +
                len(view["harvest"]) + len(view["empty"]))
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

    # --- Seed pipeline (unchanged) ---
    ph = phase(day)
    space = len(view["empty"]) + 2
    want = {}
    if day <= CUTOFF["MELON"] and budget > 700:
        want["MELON"] = min(space, 6 if ph == 0 else 10)
    if day <= CUTOFF["STRAWBERRY"] and budget > 900:
        want["STRAWBERRY"] = 3   # ongoing crop, small standing patch is enough
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
        want["WHEAT"] = 4

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

    orders = []
    for bucket in (strategic_orders, feed_orders, manipulation_orders, sell_orders):
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
# MOVEMENT (unchanged)
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
# ANIMAL PIPELINE (farmer-owned) — generalized from v7.1's single
# cow_state to a list of plans, one per animal (any species).
#
# Setup stages per plan: NONE -> BOUGHT -> (build) -> CARRYING -> ACTIVE;
# ABANDONED on repeated failure. Only one plan is ever BOUGHT/CARRYING
# at a time (see economy()'s `in_progress` gate) — the farmer resolves
# one animal before the next purchase fires. Maintenance is stateless
# and already fleet-wide: it always operates on the nearest tile in
# view["my_pastures"], which naturally includes every ACTIVE plan's
# site regardless of species or how many are active.
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
            pass  # good; setup action logic moves us forward
        elif timed_out:
            _fail_stage(plan, "NONE")
    elif stage == "ACTIVE":
        # The engine only ever clears the "animal" key (2 consecutive unfed
        # days), never the pasture tile itself, so this should be rare — but
        # if the animal is gone and we're not carrying/holding a replacement,
        # treat the plan as abandoned so the fleet loop plans a replacement.
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
        # Prefer a still-unclaimed reserved near-shed slot (see _agent's
        # reserved_animal_sites) over the generic nearest-tile fallback — this
        # is what keeps every animal's daily feed/harvest/care/collect walk
        # short even if this particular purchase fires late in the match,
        # after most other near-shed tiles are already planted with crops.
        pool = [t for t in reserved_sites if t in candidates] or candidates
        site = min(pool, key=lambda p2: _dist(p2, _nearest_center(p2)))
        plan["site"] = site

    # 1. Build the pasture first (animal waits safely in the shed).
    if site not in view["empty_pastures"]:
        if pos != site:
            return [_step_toward(pos, site)]
        return ["BUILD_PASTURE"]

    # 2. Pick the animal up at a center (shed) tile.
    if not carrying:
        if shed.get(species, 0) == 0:
            return None  # reconcile will retry/abandon
        center = _nearest_center(pos)
        if pos not in CENTER_TILES:
            return [_step_toward(pos, center)]
        _advance(plan, "CARRYING", day, hour)
        return ["PICKUP", species, 1]

    # 3. Walk it to the pasture and place it. VERIFIED format: no qty arg.
    if pos != site:
        return [_step_toward(pos, site)]
    return ["PLACE", species]


def _pasture_priority(pos, farmer_pos, tile, allow_care=True):
    """Rank pasture urgency. A dedicated care hand can remove CARE from the
    farmer's routing problem while preserving survival and product logistics."""
    fed = tile.get("fed_today", True)
    urgent = (not fed) and tile.get("consecutive_unfed", 0) >= 1
    if urgent:
        rank = 0
    elif not fed:
        rank = 1
    elif tile.get("yield_units", 0) > 0:
        rank = 2
    elif allow_care and not tile.get("cared_today", True):
        rank = 3
    elif tile.get("fertilizer_available", False):
        rank = 4
    else:
        rank = 5
    return (rank, _dist(pos, farmer_pos))


def care_commando_action(pos, pastures):
    """Dedicated hand policy: CARE every visible uncared animal, using
    distance only as a tiebreak. Returns None when care work is complete."""
    targets = [(ppos, tile) for ppos, tile in pastures
               if not tile.get("cared_today", True)]
    if not targets:
        return None
    ppos, _tile = min(targets, key=lambda pt: _dist(pos, pt[0]))
    if pos == ppos:
        return ["CARE"]
    step = _step_toward(pos, ppos)
    return [step] if step else None


def animal_maintenance_action(pos, view, shed, farmer_carry, day, hour, allow_care=True):
    """Stateless maintenance across the active fleet. The farmer handles
    feed, harvest, fertilizer and deposits. CARE may be delegated to hand 0."""
    if not view["my_pastures"]:
        return None

    # Ignore care-only pastures when CARE is delegated; otherwise the farmer
    # can repeatedly route toward work the commando is already assigned to.
    candidates = []
    for ppos, tile in view["my_pastures"]:
        has_noncare_need = (
            not tile.get("fed_today", True)
            or tile.get("yield_units", 0) > 0
            or tile.get("fertilizer_available", False)
        )
        if allow_care or has_noncare_need:
            candidates.append((ppos, tile))
    if not candidates:
        return None

    ppos, tile = min(
        candidates,
        key=lambda pt: _pasture_priority(pt[0], pos, pt[1], allow_care=allow_care),
    )

    needs_feed = not tile.get("fed_today", True)
    needs_care = allow_care and not tile.get("cared_today", True)
    has_yield = tile.get("yield_units", 0) > 0
    has_fert = tile.get("fertilizer_available", False)
    urgent_feed = needs_feed and tile.get("consecutive_unfed", 0) >= 1

    carry_wheat = farmer_carry.get("WHEAT", 0)
    carry_products = {i: farmer_carry.get(i, 0) for i in ANIMAL_PRODUCTS
                      if farmer_carry.get(i, 0) > 0}
    deposit_due = sum(carry_products.values()) >= PRODUCT_DEPOSIT_AT or (
        carry_products and (needs_feed and carry_wheat == 0))
    fetch_wheat_due = needs_feed and carry_wheat == 0 and shed.get("WHEAT", 0) > 0

    if pos == ppos:
        if needs_feed and carry_wheat > 0:
            return ["FEED"]
        if has_yield:
            return ["HARVEST"]
        if needs_care:
            return ["CARE"]
        if has_fert:
            return ["COLLECT_FERTILIZER"]

    if pos in CENTER_TILES:
        if fetch_wheat_due and urgent_feed:
            return ["PICKUP", "WHEAT", min(FEED_CARRY_TARGET, shed.get("WHEAT", 0))]
        if carry_products:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]]
        if fetch_wheat_due:
            return ["PICKUP", "WHEAT", min(FEED_CARRY_TARGET, shed.get("WHEAT", 0))]

    if fetch_wheat_due and urgent_feed:
        return [_step_toward(pos, _nearest_center(pos))]
    if fetch_wheat_due or deposit_due:
        return [_step_toward(pos, _nearest_center(pos))]
    if (needs_feed and carry_wheat > 0) or has_yield or needs_care or has_fert:
        return [_step_toward(pos, ppos)]

    if day >= LIQUIDATE_DAY and carry_products:
        if pos in CENTER_TILES:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]]
        return [_step_toward(pos, _nearest_center(pos))]

    return None


# =====================================================================
# CROP TASK ALLOCATION (unchanged from v7.1)
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
                    tasks["urgent_water"].append((x, y))  # same-day water invariant
                    return ["PLANT", crop]
                continue
            return TASK_ACTION[key]

    for key in TASK_ORDER:
        tgt = _nearest((x, y), tasks[key])
        if tgt:
            step = _step_toward((x, y), tgt)
            if step:
                tasks[key].remove(tgt)
                return [step]

    fallback = _step_toward((x, y), (4, 4))  # idle drift toward shed
    return [fallback] if fallback else ["PASS"]


# =====================================================================
# ENTRY
# =====================================================================

timing_engine = DemandTimingEngine(match_seed=42)
animal_plans = []   # fleet state — list of per-animal plan dicts, mutated in place
reserved_sites = []  # near-shed tile slots reserved for the fleet, computed once (see below)


def _init_reserved_sites(view):
    """Claim the FLEET_TARGET-total nearest empty tiles to the shed for animal
    pastures, computed once at the start of the match and cached for the rest
    of it. Diagnosed via local A/B testing (see design doc 5d): without this,
    a late-game animal purchase (once budget/day conditions align) could only
    choose a site from whatever empty tiles crops hadn't already claimed —
    frequently a tile far from the shed. A single farmer visiting a far
    pasture every day, on top of the near one plus wheat/product shed trips,
    can blow the 24-turn daily budget and miss a feeding 2 days running,
    permanently losing the animal (engine `_daily_refresh_animals`). Reserving
    close slots up front, and excluding them from crop-planting from turn one
    regardless of when the actual purchase happens, keeps every animal's daily
    walk short no matter how late in the match it gets bought."""
    global reserved_sites
    if reserved_sites:
        return reserved_sites
    total_target = sum(FLEET_TARGET.values())
    candidates = [t for t in view["empty"] if t not in CENTER_TILES]
    candidates.sort(key=lambda t: _dist(t, _nearest_center(t)))
    reserved_sites = candidates[:total_target]
    return reserved_sites


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

    tasks = {
        "urgent_water": list(view["urgent_water"]),
        "harvest": list(view["harvest"]),
        "water": list(view["water"]),
        "plant": (view["empty"][:n_plantable] if crops_now and hour < 21 else []),
        "weeds": list(view["weeds"]) if day <= 27 else [],
    }
    # Never plant on any in-progress/active pasture site, or on a reserved
    # near-shed slot not yet claimed by a plan (keeps it available/close for
    # whenever the next purchase actually fires — see _init_reserved_sites).
    claimed_sites = {pl["site"] for pl in animal_plans if pl.get("site") and pl["stage"] != "ABANDONED"}
    excluded = claimed_sites | set(sites)
    if excluded:
        tasks["plant"] = [t for t in tasks["plant"] if t not in excluded]

    farmer_pos = tuple(me["farmer"])
    active_setup_plan = next((pl for pl in animal_plans if pl["stage"] in ("BOUGHT", "CARRYING")), None)
    # An already-ACTIVE animal that's already missed a feeding (consecutive_unfed
    # >= 1) is one more missed day from being permanently lost with no refund
    # (engine `_daily_refresh_animals`). Setting up animal N+1 must not be allowed
    # to starve animal N — that's exactly the single-farmer bottleneck flagged as
    # the real risk of scaling the fleet (design doc 5d). So an urgent feed need
    # on any already-placed pasture preempts setup work for the turn.
    urgent_existing_feed = any(
        not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
        for _pos, t in view["my_pastures"]
    )
    farmer_op = None
    if active_setup_plan is not None and not urgent_existing_feed:
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        farmer_op = animal_maintenance_action(
            farmer_pos, view, shed, farmer_carry, day, hour,
            allow_care=not (DEDICATED_CARE_HAND and len(me["hands"]) > 0),
        )
    if farmer_op is None and active_setup_plan is not None:
        # Maintenance had nothing urgent to do (e.g. no wheat staged yet) —
        # fall back to setup work rather than idling.
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        farmer_op = unit_action(farmer_pos, tasks, seeds, day)

    hand_ops = []
    for idx, hand in enumerate(me["hands"]):
        hpos = tuple(hand)
        op = None
        if DEDICATED_CARE_HAND and idx == 0:
            op = care_commando_action(hpos, view["my_pastures"])
        if op is None:
            op = unit_action(hpos, tasks, seeds, day)
        hand_ops.append(op)
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
