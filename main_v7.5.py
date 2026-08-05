import math
import random
import sys

# =====================================================================
# MAIN V7.5
#
# Base: v7.3 (fleet-ceiling round, see that section below), unchanged
# except a deliberate design choice about HOW to keep fleet growth in check.
#
# v7.3's dynamic expansion gate (_animal_expansion_feasible) has no fixed
# animal-count cap by design, and testing showed why that's the right call:
# a flat cap at 15 (matching where real top players land) recovered one
# matchup but gave back the entire gain in another -- the right ceiling
# genuinely differs by game, so no single number is correct in general.
#
# But letting the fleet grow to 19 also isn't obviously right just because
# nothing stopped it -- the gate only checks whether the NEXT animal is
# feasible (affordable, staffable, safe), never whether something else
# competing for the same cash/land/hand-time would pay off more. Real top
# players settling near 15 looks less like a hard cap and more like the
# natural outcome of ALSO investing seriously in land and crops, not just
# animals. So v7.5 doesn't touch the animal gate at all -- instead it
# strengthens what animals have to compete against, so the same gate
# produces a smaller, more selective fleet on its own:
#   1. Budget priority reordered: land expansion and seed buying are now
#      checked BEFORE the animal purchase block, not after. Previously
#      animals had unconditional first claim on cash every turn; now they
#      only get what's left over once land/seeds have taken their share.
#   2. TOMATO turned on: fully priced and costed in CROPS/MARKET_PARAMS
#      (seed $50, base $60, ongoing/repeating harvest) but never included
#      in PLANT_PRIORITY in any prior version -- a real, already-balanced
#      revenue stream that was sitting completely unused, now competing for
#      land and hand-time alongside melon/strawberry.
#   3. Crop-land reserve now scales with unlocked land instead of a flat 8
#      tiles -- 8 tiles was a meaningful share of a 1-quadrant farm but
#      nothing on the full 4-quadrant board, so crops were claiming a
#      shrinking proportion of land as the game went on even as more became
#      available.
# The animal feasibility gate itself (survival / wheat affordability / hand
# capacity / crop-space checks) is unchanged from v7.3.
#
# =====================================================================
# v7.3 header below, unchanged history:
#
# Base: v7.2, unchanged except three replay-proven fixes (see
# kaggriculture-v7.3-plan.md for the full evidence trail):
#
#   1. Force-dump firesale fix (economy(), sell loop). v7.2's shed-overflow
#      dump sold the ENTIRE remaining quantity of an item at whatever price
#      the market bore, no floor. Replay evidence: 11 orders / 800 units at
#      ~$1/unit across the 6 traced losses, mostly MELON, day 23-28. Fixed
#      by computing the actual overflow that needs relieving this turn and
#      only selling that much, at a real price floor (50% of base) first,
#      dropping below it only for whatever residual is still needed to
#      clear the shed. Also throttles MELON seed buying when shed load is
#      already elevated, so the overflow is less likely to occur at all.
#   2. WHEAT planting priority. Bought every game, planted 0-2 times
#      because it was last in PLANT_PRIORITY. Four of six real opponents
#      sell hundreds of units of it. Reordered above CARROT and its seed
#      target raised so purchased wheat actually gets planting capacity.
#   3. COW start_day moved from 3 to 0. Replay trace (episode 90010183):
#      money clears the $700 purchase gate on day 1 (728) but erodes back
#      under it by day 3 (624) from ordinary day-1/day-2 hire/seed spend,
#      and stays blocked for a further 8 days until the first melon
#      harvest pays out on day 11 — so land AND the cow both sat waiting
#      on the same cash wall. Since the animal-purchase check runs first
#      in economy(), ahead of all other spending that turn, moving
#      start_day earlier lets it claim the cash before erosion, no new
#      reserve logic needed. LAND purchase logic is intentionally left
#      unchanged — its day-16/18 cutoffs already tolerated the day-11
#      delay in the traced game (nothing was missed, just fewer productive
#      cycles on the new tiles), and reserving land's larger $1,000+
#      threshold risks shrinking the very day-0 seed spend that produces
#      the day-11 windfall.
#
# Follow-up round (same file, still called v7.3): fleet ceiling. Real
# opponents extracted from a public notebook (Frontier V12 / Scenario V14,
# both targeting a 15-animal fleet) beat this build 3-4x once FLEET_TARGET=4
# was diagnosed as the dominant remaining gap — the money curves diverge
# almost exactly when their fleet finishes ramping to 15 on day 12, not from
# land (we actually unlock MORE quadrants than they do).
#
# Fixed FLEET_TARGET replaced with a live feasibility gate (see
# _animal_expansion_feasible) instead of just raising the number, because
# raising the number alone doesn't fix anything: the v7.2 6-animal collapse
# was caused by feed-wheat cost and reserved-tile crop-crowding, and if
# those mechanisms are unchanged, a "smarter" gate would just rediscover
# roughly the same ceiling on its own. So this round fixes both underlying
# mechanisms, not just the number:
#   - Wheat: JIT feed-buying already prefers home-grown shed wheat over
#     market purchases (unchanged code), and v7.3's WHEAT-priority fix
#     (item 2 above) means more of it should now be actually home-grown
#     rather than bought — the feasibility gate's wheat check directly
#     measures this (blocks expansion only when the marginal feed cost is
#     still a meaningful bite out of current cash, not on a fixed count).
#   - Tiles: pasture reservation changed from "reserve N tiles upfront for
#     a hypothetical target fleet size" (locks land for animals that might
#     never get bought) to "reserve one more tile only at the moment a
#     purchase actually fires" (_grow_reserved_sites) — plus a floor on how
#     much open land must remain for crops before another pasture is
#     allowed to claim a tile.
#   - Survival: a hard gate independent of the above two — if any existing
#     animal is already missing a feeding, don't add another one regardless
#     of budget/land, since that's a sign the farm is already stretched.
# SHEEP stays deliberately disabled (SHEEP_ENABLED=False) — isolating this
# experiment to COW scaling only, same incremental-and-test discipline
# used for every prior version of this file.
#
# ---------------------------------------------------------------------
# v7.2 header below, unchanged history:
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
    # COW start_day moved 3 -> 0 for v7.3: replay evidence showed the day-3
    # eligibility check consistently missing a still-adequate day-1 cash
    # buffer by a small margin (~$76 in the traced game) due to ordinary
    # days 1-2 hire/seed spend, then staying blocked for 8+ more days until
    # the first harvest. Moving the gate to day 0 lets the (first-in-turn)
    # animal-purchase check claim the cash before any of that turn's other
    # spending erodes it. See kaggriculture-v7.3-plan.md item 3.
    "COW":   {"cost": 400, "min_money": 700, "start_day": 0,  "last_day": 22},
    "SHEEP": {"cost": 500, "min_money": 800, "start_day": 3,  "last_day": 22},
}
ANIMAL_SPECIES_ORDER = ["COW", "SHEEP"]   # priority order when considering the next purchase
SHEEP_ENABLED = False   # deliberately still off — see header, isolating this round to COW scaling

# --- Dynamic fleet expansion: no fixed count. Buying the next animal is
# gated live by _animal_expansion_feasible() every time it's considered,
# instead of a hardcoded FLEET_TARGET ceiling. See header for why loosening
# a fixed number alone wouldn't have fixed anything.
EXPANSION_WHEAT_BUDGET_FRAC = 0.15  # one more animal's feed shortfall (after
                                     # home-grown wheat) can't cost more than
                                     # this fraction of current cash in a
                                     # single turn — this is the mechanism
                                     # that actually collapsed the v7.2
                                     # 6-animal test, not the raw count
EXPANSION_MIN_CROP_TILES_PER_QUAD = 8  # v7.5: scales with unlocked land
                                     # instead of a flat 8 total -- 8 tiles
                                     # was a meaningful reserve on a
                                     # 1-quadrant farm but a shrinking sliver
                                     # once the full 4-quadrant board is
                                     # unlocked, so crops were claiming a
                                     # smaller and smaller share of land as
                                     # the game went on even as more of it
                                     # became available. Reserve is now
                                     # this-per-quadrant-unlocked, so land
                                     # expansion pulls crop reserve up
                                     # alongside it, not just animal capacity.
# A fixed EXPANSION_MAX_ANIMALS=15 was tested here as a diagnostic (matching
# where both real reactive opponents independently settle). Result: it
# recovered the Scenario V14 loss ($15,661 -> $46,530) but gave back almost
# the entire gain against Frontier V12 ($47,366 -> $25,496, below even the
# original fixed-4 baseline). So the right stopping point genuinely differs
# by game -- growing to 18 was profitable against one opponent and actively
# harmful against the other. No single number threads both. Removed in favor
# of CROP_NEGLECT_TASKS_PER_HAND below, a live signal instead of a fixed one.
#
# Root cause, found by checking whether MILK price was crashing (it wasn't --
# stayed at or above its $160 base the whole game, market never saturated):
# the earlier hand-capacity check (3 below) only verifies a FORMULA target
# stays under HAND_TARGET_MAX -- it doesn't verify hiring can actually AFFORD
# to reach that target. Each additional hire's Fibonacci-scaled cost climbs
# fast, so the real hire loop can stall well short of what the formula says
# is fine, especially while cash is still thin during the fleet's growth
# phase. The farm can keep passing check 3 on paper while genuinely not
# having the real hands to cover crops -- exactly what happened against
# Scenario V14. CROP_NEGLECT_TASKS_PER_HAND checks the real, current,
# already-hired hand count against real, current crop backlog instead of a
# theoretical ceiling -- a direct symptom check, not a forecast.
CROP_NEGLECT_TASKS_PER_HAND = 5     # matches the existing work/5 scaling
                                     # already used by the hiring formula
ANIMAL_WORK_WEIGHT = 2              # how much one pending pasture need counts
                                     # toward "workload" relative to one crop
                                     # tile, in both the hiring formula and
                                     # the expansion gate's capacity check
                                     # below -- a pasture visit is a round
                                     # trip (walk there, act, walk back to
                                     # shed), costing more hand-turns than a
                                     # single water/harvest action

SETUP_STAGE_TIMEOUT = 12
SETUP_MAX_RETRIES = 3
FEED_CARRY_TARGET = 2
PRODUCT_DEPOSIT_AT = 3         # PLACE milk/wool when carrying this many

# --- Real hiring cost model (kaggriculture.py: FARM_HAND_COST_MULT=1, fib(0)=1,1,2,3,5,...) ---
FARM_HAND_COST_MULT = 1
HAND_TARGET_MIN = 4
HAND_TARGET_MAX = 18           # unchanged from v7.1 — see that file's header for why a lower
                                # cap was tried and rejected (2.5x money loss head-to-head)

# --- Market-order category slot reservations (unchanged from v7.1) ---
MAX_HIRE_SLOTS = HAND_TARGET_MAX
MAX_SEED_SLOTS = 5   # bumped from 4 to fit TOMATO alongside MELON/STRAWBERRY/WHEAT/CARROT (v7.5)

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
# STRAWBERRY added after fertilizer logistics were confirmed working at the
# 4-cow fleet size (15 FERTILIZER/game sold reliably, see design doc 5d) —
# ranked below MELON (the dominant profit driver, don't compete with it for
# hand time/planting slots) but above CARROT/WHEAT since it's a premium crop.
# WHEAT moved above CARROT for v7.3: replay evidence showed WHEAT bought
# every game but planted only 0-2 times because it was last in line for
# planting slots, while 4 of 6 real opponents sell hundreds of units of it.
# CARROT's base price ($35) is technically higher than WHEAT's ($25), but
# WHEAT is dual-purpose (feed + sale) and was being crowded out entirely,
# not just under-prioritized — see kaggriculture-v7.3-plan.md item 2.
# TOMATO added for v7.5: fully defined in CROPS/MARKET_PARAMS (seed $50,
# base $60, ongoing/repeating harvest) since at least v7.2 but never once
# included in PLANT_PRIORITY -- a real, already-balanced revenue stream
# sitting unused. Ranked above WHEAT/CARROT by base price, below the two
# premium crops. CUTOFF=20 gives it a similar "needs runway before season
# end" treatment to STRAWBERRY's 18, slightly later since its faster
# interval (1 vs 2) lets it start paying back sooner after planting.
PLANT_PRIORITY = ["MELON", "STRAWBERRY", "TOMATO", "WHEAT", "CARROT"]
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


def _pending_animal_work(view):
    """Count of pastures with an actual pending need this turn (unfed, ready
    to harvest, needs care, or has fertilizer waiting). Shared by the hiring
    formula and the expansion feasibility gate below so both agree on what
    "animal workload" means -- see ANIMAL_WORK_WEIGHT."""
    return sum(1 for _pos, t in view["my_pastures"]
               if (not t.get("fed_today", True)) or t.get("yield_units", 0) > 0
                  or (not t.get("cared_today", True)) or t.get("fertilizer_available", False))


def _animal_expansion_feasible(obs, view, budget, shed, n_animals, n_hands, quads):
    """Live gate for buying the (n_animals+1)th animal, replacing the old
    fixed FLEET_TARGET count (see file header). All five must hold:
      1. Survival: no existing pasture is already missing a feeding -- if
         the farm can't keep up with what it already has, don't add more.
      2. Wheat affordability: the market-buy needed to cover one more
         animal's feed shortfall, after home-grown wheat already sitting in
         the shed, must stay small relative to current cash -- this is the
         actual mechanism that collapsed the economy at 6 animals in the
         v7.2 round, not the raw headcount.
      3. Hand capacity (formula): a projected hiring target, covering crops
         plus animal workload, must stay under HAND_TARGET_MAX -- catches
         the case where hiring could never staff this fleet size even in
         principle.
      4. Crops not already neglected (real, not projected): do the hands we
         ACTUALLY have right now already have their hands full with crop
         backlog alone? Added because check 3 alone wasn't enough in
         testing -- it compares a target to a ceiling, but the real hire
         loop can stall well short of that ceiling because each additional
         hire's Fibonacci-scaled cost climbs fast, especially while cash is
         still thin during the fleet's growth phase. The farm kept passing
         check 3 on paper while genuinely not having enough real hands for
         crops, which is what actually happened against Scenario V14. This
         is a direct symptom check, not a forecast -- see
         CROP_NEGLECT_TASKS_PER_HAND's comment for the fuller story
         (including why a flat animal-count cap was tried and rejected).
      5. Crop space: reserving one more near-shed tile for a pasture must
         still leave enough open land for crops (melon especially) -- the
         other mechanism from the original 6-animal collapse. Reserve now
         scales with unlocked land (EXPANSION_MIN_CROP_TILES_PER_QUAD), not
         a flat number -- see that constant's comment (v7.5).
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
    a new animal purchase actually fires -- not speculatively for a target
    fleet size that may never be reached (see file header). Picks the
    nearest still-unclaimed empty tile to the shed, same site-quality logic
    as the old upfront version, just triggered incrementally instead of all
    at once at match start."""
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
    # Hoisted up from the paced-selling section (v7.5) -- now also needed by
    # land/seeds, which moved ahead of animal purchase, before shed_load used
    # to be computed.
    shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)

    strategic_orders = []
    feed_orders = []
    sell_orders = []
    hire_orders = []
    seed_orders = []

    # --- v7.5: land expansion and seed buying moved AHEAD of animal
    # purchase (previously animals were checked first and had unconditional
    # first claim on cash every turn). Now they only get what land/seeds
    # leave behind -- see file header for why. Nothing about the land/seed
    # logic itself changed, just its position in this function.

    # --- Aggressive land expansion (v5/v7.1, unchanged) ---
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
        # v7.3 fix: throttle new MELON seed buying once the shed is already
        # getting full -- melon is the dominant driver of the force-dump
        # firesale (11 orders / 800 units at ~$1/unit across the 6 traced
        # losses), so slowing new melon production before the shed hits cap
        # is the other half of the fix, alongside the dump-selling change
        # above. See plan item 1.
        if shed_load > SHED_CAP - 30:
            melon_target = min(melon_target, 3)
        want["MELON"] = melon_target
    if day <= CUTOFF["STRAWBERRY"] and budget > 900:
        want["STRAWBERRY"] = 3   # ongoing crop, small standing patch is enough
    if day <= CUTOFF["TOMATO"] and budget > 600:
        want["TOMATO"] = 3   # ongoing crop, same "small standing patch" logic
                              # as STRAWBERRY -- new for v7.5, previously unused
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
        # Bumped 4 -> 8 for v7.3 alongside the PLANT_PRIORITY reorder above —
        # raising the target without also raising planting priority would
        # just mean more unused wheat sitting in seed inventory, same as v7.2.
        want["WHEAT"] = 8

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

    # --- Animal fleet purchase (generalized from v7.1's single cow_state) ---
    # Serialized: only start a new purchase (or retry a stalled one) if nothing
    # is currently BOUGHT/CARRYING — one farmer can only build+carry+place one
    # animal at a time, so there's no benefit to buying a second before the
    # first is resolved, and it would just sit unclaimed risking the shed cap.
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
                _grow_reserved_sites(view)  # claim one more near-shed tile
                                             # now that we've committed to
                                             # this animal, not speculatively
                                             # ahead of time — see header

    # --- JIT feed wheat (FEED consumes carried wheat, staged via shed) ---
    # n_animals computed above, in the animal-purchase block.
    if n_animals > 0:
        target_wheat = n_animals * 2 + FEED_CARRY_TARGET
        have = shed.get("WHEAT", 0)
        if have < target_wheat:
            qty = min(target_wheat - have, 10)
            cost = qty * live_price(obs, "WHEAT")
            if budget >= cost:
                feed_orders.append(["BUY_PRODUCT", "WHEAT", qty])
                budget -= cost

    # --- Fertilizer straight to market ---
    fert = shed.get("FERTILIZER", 0)
    if fert > 0:
        sell_orders.append(["SELL", "FERTILIZER", fert])

    # --- Paced selling + demand-timing attack ---
    # v7.3 fix: force_dump is now just a trigger, not "sell everything at any
    # price". dump_overflow is the actual amount that needs relieving this
    # turn to bring the shed back under a safe load -- that's what gets sold,
    # not the item's entire remaining quantity. See header + plan item 1.
    DUMP_TARGET_LOAD = SHED_CAP - 20   # a bit more buffer than v7.2's -15 trigger
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
            # Sell only enough to relieve the actual overflow, at a real
            # price floor (50% of base) first. Only dip below that floor
            # for whatever residual is still needed after the floor-
            # respecting attempt -- last resort, not the first move.
            dump_floor = 0.5 * base
            want_qty = min(int(n), int(dump_overflow))
            qty = units_sellable_above(item, inv.get(item, I0), dump_floor, want_qty)
            if qty < want_qty:
                qty += min(int(n) - qty, want_qty - qty)
            dump_overflow -= qty
        elif force_dump:
            # Overflow already relieved by earlier (higher-priced) items
            # this turn -- fall through to normal paced selling instead of
            # also liquidating this item at any price.
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

    # --- Hiring: real Fibonacci cost (v7.1 base), now also counting animal
    # maintenance workload alongside crops -- previously `work` only counted
    # crop backlog, so the hand pool stayed crop-sized even as the fleet
    # grew, silently pulling hands off crops rather than actually hiring
    # more to cover the animals. See _animal_expansion_feasible's matching
    # capacity check, which uses the same weighting.
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


def _pasture_priority(pos, farmer_pos, tile):
    """Rank a pasture's urgency, most urgent first. v7.1's original single-cow
    version of this selection just picked the physically NEAREST pasture,
    completely blind to whether that pasture actually had anything pending —
    harmless with exactly one animal, but with a real fleet it meant the
    farmer could return to the same nearby-but-already-fed pasture turn after
    turn while a second pasture's feed need went unaddressed, racking up
    consecutive_unfed and losing the animal (diagnosed via local A/B testing,
    design doc 5d — this, not raw travel distance, was the actual cause of
    fleet-scaling animal deaths seen in testing)."""
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


def animal_maintenance_action(pos, view, shed, carry, day, hour, exclude=()):
    """Stateless daily care across the whole active fleet. Targets whichever
    pasture has the most urgent pending need (see _pasture_priority), not
    just the nearest one — see that function's docstring for why.

    Generalized for v7.3's fleet-ceiling round to run for ANY worker, not
    just the farmer (`carry` is that worker's own carry inventory —
    obs["private"]["inventories"][i]). `exclude` is the set of pasture
    positions already claimed by an earlier worker THIS TURN (see _agent())
    so multiple workers don't converge on the same animal — the same
    coordination problem crop tasks solve by removing a claimed tile from
    the shared pool, applied here to pastures instead. This exists because
    once the fleet grows past ~4-5 animals, a single farmer working through
    them one at a time can't keep pace with feed/care/harvest/collect across
    the whole fleet AND set up new animals in the same day — real testing
    showed animals actually dying (missed feedings) and purchases timing out
    mid-setup as a result, not a wheat/land affordability problem.

    Returns (op_or_None, claimed_pos_or_None) — callers should add the
    claimed position to their `exclude` set before calling this for the
    next worker."""
    candidates = [(p, t) for p, t in view["my_pastures"] if p not in exclude]
    if not candidates:
        return None, None
    (ppos, tile) = min(candidates, key=lambda pt: _pasture_priority(pt[0], pos, pt[1]))

    needs_feed = not tile.get("fed_today", True)
    needs_care = not tile.get("cared_today", True)
    has_yield = tile.get("yield_units", 0) > 0
    has_fert = tile.get("fertilizer_available", False)
    urgent_feed = needs_feed and tile.get("consecutive_unfed", 0) >= 1
    # Only actually "claim" ppos if it has real pending work -- if every
    # remaining pasture is fully serviced, min() still returns the
    # least-bad option, but nothing below should reserve it against other
    # workers (they might still have leftover carry to deposit, which
    # isn't really "about" ppos at all).
    claim = ppos if (needs_feed or needs_care or has_yield or has_fert) else None

    carry_wheat = carry.get("WHEAT", 0)
    carry_products = {i: carry.get(i, 0) for i in ANIMAL_PRODUCTS if carry.get(i, 0) > 0}
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

    return None, None  # nothing pending for this worker — falls back to crops


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
reserved_sites = []  # near-shed tiles claimed for the fleet, grown incrementally
                      # by _grow_reserved_sites (one per animal actually
                      # purchased) instead of precomputed for a fixed
                      # FLEET_TARGET — see file header.


def _init_reserved_sites(view):
    """Accessor for the fleet's currently-reserved near-shed tiles. Originally
    this precomputed FLEET_TARGET-total tiles once at match start (see the
    v7.2-era docstring this replaced) to avoid a late animal purchase being
    stuck with only a far-from-shed site once nearby tiles were already
    crop-planted. With FLEET_TARGET removed (dynamic expansion, see header),
    there's no longer a fixed total to precompute for — growth now happens
    incrementally in economy() (_grow_reserved_sites), one tile per animal
    actually bought, at the moment it's bought. Kept as a thin passthrough
    (rather than inlining `reserved_sites` everywhere) since the rest of the
    file still calls this once per turn."""
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
    claimed_pastures = set()
    farmer_op = None
    if active_setup_plan is not None and not urgent_existing_feed:
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        farmer_op, claim = animal_maintenance_action(farmer_pos, view, shed, farmer_carry, day, hour, claimed_pastures)
        if claim is not None:
            claimed_pastures.add(claim)
    if farmer_op is None and active_setup_plan is not None:
        # Maintenance had nothing urgent to do (e.g. no wheat staged yet) —
        # fall back to setup work rather than idling.
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        farmer_op = unit_action(farmer_pos, tasks, seeds, day)

    # Hands help with animal maintenance whenever there's still pasture work
    # pending after the farmer's own pick — workload-driven, not a fixed
    # animal-count threshold: once the pending-pasture pool (shared via
    # `claimed_pastures`, same coordination pattern as crop `tasks`) is
    # empty, remaining hands just do crops as before. See
    # animal_maintenance_action's docstring for why this exists.
    hand_ops = []
    for i, h in enumerate(me["hands"]):
        hand_pos = tuple(h)
        hand_carry = inventories[i + 1] if len(inventories) > i + 1 else {}
        op, claim = animal_maintenance_action(hand_pos, view, shed, hand_carry, day, hour, claimed_pastures)
        if op is not None:
            hand_ops.append(op)
            if claim is not None:
                claimed_pastures.add(claim)
        else:
            hand_ops.append(unit_action(hand_pos, tasks, seeds, day))

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
