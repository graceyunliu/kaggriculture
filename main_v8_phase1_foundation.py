import math
import random
import sys

# =====================================================================
# MAIN V8 -- PHASE 1 FOUNDATION (behavior-preserving)
#
# Base: main_v7.6.py, forked byte-for-byte. Every strategic decision in
# this file still produces exactly what v7.6 produces. Nothing about how
# the agent plays has changed, and that is the point: this release is the
# substrate the v8 architecture gets built on, not the architecture
# itself.
#
# What Phase 1 adds (see kaggriculture-v8-design-spec.md sections 5.1,
# 5.2, 11 and phase list in section 13):
#
#   1. `build_state()` -- one normalized state object per turn, with
#      my/opponent/market/capacity sub-objects. Today nothing reads it
#      for decisions; Phase 2+ scorers will read it INSTEAD of digging
#      into raw `obs` at each call site. This is what makes decisions
#      comparable on a shared basis later.
#   2. `analyze_opponent()` -- direct factual extraction from the
#      opponent's visible tiles (mature crops, imminent supply, fleet,
#      land, concentration). Per the spec's correction to the original
#      v8 pitch: this is state-READING, not Bayesian classification.
#      Kaggriculture is fully observable, so no inference is needed.
#   3. `DecisionLog` -- records what was chosen, the state it was chosen
#      from, and (later) what the alternatives scored, so EV formulas can
#      be calibrated against realized outcomes instead of guessed.
#   4. Workload / market-pressure metrics, computed once per turn in one
#      place rather than recomputed ad hoc inside four different rules.
#
# WHY THE LOG IS ON BY DEFAULT (`DECISION_LOG = True`): downloaded ladder
# replays record what the agent DID, not the state or rule branch that
# produced it. Leaving the log dormant would mean real matches -- the
# only games against real opponents -- generate no diagnostic data at
# all, which is exactly where it is most valuable.
#
# The objection to running it live was never cost (measured agent time is
# ~21ms against a 1s/turn budget; this adds dict-building, not I/O). It
# was `agent()`'s crash guard: it swallows ANY exception and returns a
# PASS turn, so a bug in diagnostic-only code could silently forfeit a
# real turn's entire action set. `_log_safe()` closes that: it takes a
# thunk, so each record is both ASSEMBLED and written inside one
# try/except. A logging bug costs one record and bumps
# `DECISION_LOG_SINK.errors`; it can never cost a turn. Taking a thunk
# also keeps the disabled path genuinely free -- the payload never
# evaluates -- so `disable_decision_log()` remains a real kill switch.
#
# Harnesses call `enable_decision_log()` (which also clears prior
# records) and read `DECISION_LOG_SINK.records` / `.to_jsonl(path)`.
#
# WHAT IS DELIBERATELY NOT HERE: no expected-value engine, no scoring of
# candidate actions, no adaptive selling. Those are Phases 2-4. This
# project's track record (v7.1, v7.2, v7.5, v7.6, v7.7 rounds) is that
# changes only earn trust through seeded A/B testing, and a foundation
# that also changes behavior can't be A/B'd cleanly -- any regression
# would be unattributable. So the foundation ships first, provably
# inert, and each behavioral change gets tested against it one at a
# time.
#
# NOTE ON OPTIMIZATION WORK IN FLIGHT: v7.8 (sheep-enabled fleet) is a
# separate branch off v7.6 that has not passed its own A/B yet. It is
# intentionally NOT merged here. When it lands, its animal-purchase
# change becomes a scored candidate inside the Phase 4 expansion model
# rather than a hand-merge into this file.
#
# ---------------------------------------------------------------------
# Inherited v7.6 behavior notes (unchanged, kept for reference):
#
# v7.6 ships Variant A ("protected crop hands") after A/B testing
# against Variant B (hiring-formula-only, main_v7.6b.py). Variant A won
# 7/8 seeded games vs v7.5 (mean margin +$6,081); Variant B lost to
# v7.5, 3/8 (mean margin -$2,667).
#
# Base: v7.5, unchanged except for labor allocation. Real ladder loss
# replays (5/5, episodes 90064167/90066909/90068269/90070304/90070988)
# showed a reproducible late-game collapse: seed inventory freezes
# ~day 10-15 through day 29, WEED tiles climb from single digits to
# 20-37/100, planted-crop tiles collapse from a mid-game peak of 33-45
# down to 0-8, while WATER actions fall from ~20-38/day to near zero
# and FEED+CARE actions climb from ~2/day to 9-11/day over the same
# window. Root cause confirmed by reading the code: `animal_maintenance
# _action` has unconditional first claim on every hand and the farmer,
# every turn (v7.5's `_agent` loop), regardless of whether crops are
# already neglected -- so as the fleet's maintenance burden grows, crop
# watering/weeding/planting gets crowded out and never recovers. Two
# more contributing bugs, also fixed here: (1) weeds were last in
# TASK_ORDER and excluded entirely for day > 27; (2) hiring's own
# workload formula and the animal-expansion neglect gate both ignore
# weeds, so a heavily-weeded farm doesn't hire more or block further
# animal purchases because of it (see v7.6b for that fix in isolation).
#
# v7.6a's fix: reserve a protected fraction of hands for crop work only.
# Reserved hands may still respond to feed-critical animal needs
# (an animal already missed a feeding, or is due today) since animal
# survival should still preempt crops -- but they never do the
# *optional* animal work (CARE, HARVEST, COLLECT_FERTILIZER, product
# deposit) that was crowding out watering/weeding in the replays. The
# farmer and any hands beyond the reserved count keep v7.5's original
# unconditional-maintenance-first behavior. Weed removal is also
# promoted ahead of ordinary watering (and, once severe, ahead of
# planting) once weed count crosses a threshold, and the day<=27 cutoff
# on weed-clearing is removed.
#
# Full version history, replay evidence, and decision rationale for this
# and every prior version: see kaggriculture-agent-design.md and
# kaggriculture-v7.3-plan.md in the project folder.
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
# V8 FOUNDATION -- DECISION LOG (spec section 11)
# =====================================================================
#
# Dormant by default. See the header for why. The records this produces
# are the calibration data the spec's self-improvement loop (section 12)
# consumes: each entry pairs a decision with the state that produced it,
# so a later EV formula's prediction can be scored against what actually
# happened rather than against intuition.

DECISION_LOG = True           # ON by default -- see "why on" below
DECISION_LOG_MAX = 50000      # hard cap; a 720-turn game logs ~1.9k records


class DecisionLog:
    """Append-only, in-memory record of strategic decisions.

    Deliberately does no disk I/O: the same file runs on the ladder, and
    a failed write there forfeits a match. Harnesses read `.records`
    directly, or call `.to_jsonl(path)` themselves after the episode.

    WHY THIS IS ON BY DEFAULT (revised -- it originally shipped dormant):
    downloaded ladder replays record what the agent DID, not the state or
    the rule branch that produced it. So questions like "which sell branch
    fired in the match we lost to the strawberry specialist" are simply
    unanswerable from replays. Leaving the log dormant meant real matches
    -- the only games against real opponents -- produced no diagnostic
    data at all, which is precisely where it is most valuable.

    The objection to running it live was never the cost (measured agent
    time is ~21ms against a 1s/turn budget, and this adds dict-building,
    not I/O). It was the crash guard in `agent()`: it swallows ANY
    exception and returns a PASS turn, so a bug in diagnostic-only code
    could silently cost a real turn's entire action set. `_log_safe()`
    below removes that: every record is assembled AND written inside one
    try/except, so a logging bug degrades to a missing record and an
    incremented `errors` counter, never to a lost turn.
    """

    def __init__(self):
        self.records = []
        self.dropped = 0
        self.errors = 0

    def reset(self):
        self.records = []
        self.dropped = 0
        self.errors = 0

    def record(self, kind, choice, day=None, hour=None,
               inputs=None, alternatives=None, reason=None):
        """One decision. `alternatives` stays empty in Phase 1 -- there is
        no scoring yet -- but the field exists so Phase 2+ scorers can
        populate it without changing this schema or the readers built
        against it."""
        if len(self.records) >= DECISION_LOG_MAX:
            self.dropped += 1
            return
        self.records.append({
            "turn": (day * 24 + hour) if (day is not None and hour is not None) else None,
            "day": day,
            "hour": hour,
            "kind": kind,
            "choice": choice,
            "inputs": inputs or {},
            "alternatives": alternatives or [],
            "reason": reason,
        })

    def snapshot(self, kind, day, hour, payload):
        """Per-turn state capture, distinct from a decision. Used for the
        mechanism traces this project relies on (weed count, water action
        volume, fleet size over time) -- previously written as one-off
        throwaway diagnostic scripts each round and then lost."""
        self.record(kind, None, day=day, hour=hour, inputs=payload)

    def by_kind(self, kind):
        return [r for r in self.records if r["kind"] == kind]

    def to_jsonl(self, path):
        import json
        with open(path, "w") as fh:
            for r in self.records:
                fh.write(json.dumps(r) + "\n")
        return path


DECISION_LOG_SINK = DecisionLog()


def enable_decision_log():
    """Convenience for harnesses: `mod.enable_decision_log()` then read
    `mod.DECISION_LOG_SINK.records` after the episode. Also clears any
    records already accumulated, so a harness gets a clean episode."""
    global DECISION_LOG
    DECISION_LOG = True
    DECISION_LOG_SINK.reset()
    return DECISION_LOG_SINK


def disable_decision_log():
    """Kill switch. Nothing needs it today, but if logging is ever
    implicated in a ladder problem this is the one-line mitigation."""
    global DECISION_LOG
    DECISION_LOG = False


def _log_safe(kind, day, hour, build):
    """The only logging entry point. `build` is a zero-arg callable
    returning `(choice, inputs, reason)`.

    Two properties matter here, and both come from taking a THUNK rather
    than the assembled values:

      1. Exception containment. The `inputs` dict is the risky part --
         it does nested `.get()` chains, division by base prices, and
         arithmetic on engine-supplied values. Passing pre-built
         arguments would assemble that dict at the call site, OUTSIDE
         any try/except here, where a throw would hit `agent()`'s crash
         guard and forfeit the turn. Building it inside means a logging
         bug costs one record.
      2. Zero cost when disabled. The lambda body never evaluates if the
         flag is off, so turning logging off is genuinely free rather
         than merely not-stored.
    """
    if not DECISION_LOG:
        return
    try:
        choice, inputs, reason = build()
        DECISION_LOG_SINK.record(kind, choice, day=day, hour=hour,
                                 inputs=inputs, reason=reason)
    except Exception:
        DECISION_LOG_SINK.errors += 1


def _snapshot_safe(kind, day, hour, build):
    """Same contract as `_log_safe`, for per-turn state traces. `build`
    returns the payload dict."""
    if not DECISION_LOG:
        return
    try:
        DECISION_LOG_SINK.snapshot(kind, day, hour, build())
    except Exception:
        DECISION_LOG_SINK.errors += 1


# =====================================================================
# V8 FOUNDATION -- OPPONENT STATE ANALYZER (spec section 5.2)
# =====================================================================

def analyze_opponent(opp, day):
    """Direct extraction of the opponent's visible farm state.

    The original v8 proposal wanted a Bayesian strategy classifier here.
    That was dropped because `obs["farms"][1-p]` already exposes tiles,
    money, animals and land every turn -- there is nothing to infer about
    the PRESENT. Probabilistic reasoning is reserved (spec section 8) for
    genuinely uncertain FUTURE behavior, like whether they will sell held
    inventory, which is a Phase 5 concern.
    """
    crop_tiles = {}
    mature = {}
    ready_within_2 = {}
    animals = {}
    n_pastures = 0
    n_empty_pastures = 0
    n_weeds = 0
    n_empty = 0

    for row in opp["tiles"]:
        for t in row:
            if t is None:
                n_empty += 1
                continue
            if not isinstance(t, dict):
                continue
            kind = t.get("kind")
            if kind == "WEED":
                n_weeds += 1
            elif kind == "PASTURE":
                sp = t.get("animal")
                if sp:
                    n_pastures += 1
                    animals[sp] = animals.get(sp, 0) + 1
                else:
                    n_empty_pastures += 1
            elif kind == "PLANT":
                crop = t.get("crop")
                c = CROPS.get(crop)
                if not c:
                    continue
                crop_tiles[crop] = crop_tiles.get(crop, 0) + 1
                age = day - t.get("planted_day", day)
                yu = t.get("yield_units", 0)
                is_ready = c["ongoing"] or (age >= c["first"] and
                            (yu >= c["max_yield"] or age >= c["max_day"]))
                if is_ready and (c["ongoing"] or yu > 0 or age >= c["first"]):
                    mature[crop] = mature.get(crop, 0) + 1
                elif c["first"] - 2 <= age < c["first"]:
                    ready_within_2[crop] = ready_within_2.get(crop, 0) + 1

    total_crop = sum(crop_tiles.values())
    # Herfindahl-style concentration: 1.0 = monoculture, ->0 = diversified.
    # Several real ladder losses were to near-monoculture opponents
    # (a wheat specialist, a strawberry specialist), so "how concentrated
    # is their production" is a real signal for Phase 2 selling, not
    # decoration.
    concentration = (sum((n / total_crop) ** 2 for n in crop_tiles.values())
                     if total_crop else 0.0)
    top_crop = max(crop_tiles, key=crop_tiles.get) if crop_tiles else None

    return {
        "money": opp.get("money", 0),
        "land_quadrants": len(opp.get("unlocked_quadrants", []) or []),
        "n_hands": len(opp.get("hands", []) or []),
        "crop_tiles": crop_tiles,
        "total_crop_tiles": total_crop,
        "mature": mature,
        "ready_within_2": ready_within_2,
        "animals": animals,
        "n_animals": n_pastures,
        "n_empty_pastures": n_empty_pastures,
        "n_weeds": n_weeds,
        "n_empty": n_empty,
        "concentration": concentration,
        "top_crop": top_crop,
    }


# =====================================================================
# V8 FOUNDATION -- MARKET STATE + VELOCITY
# =====================================================================

# Previous-turn market observation, for velocity. Module-level and reset
# per process; `seeded_h2h.py` re-execs the agent module per game, so this
# does not leak across games in local testing.
_MARKET_PREV = {"turn": None, "prices": {}, "inventory": {}}


def build_market_state(obs, shed, day, hour):
    inv = dict(obs.get("market", {}).get("inventory", {}) or {})
    prices = {}
    for item in MARKET_PARAMS:
        prices[item] = live_price(obs, item)

    turn = day * 24 + hour
    price_velocity = {}
    inv_velocity = {}
    if _MARKET_PREV["turn"] is not None and _MARKET_PREV["turn"] != turn:
        span = max(1, turn - _MARKET_PREV["turn"])
        for item, p in prices.items():
            prev = _MARKET_PREV["prices"].get(item)
            if prev is not None:
                price_velocity[item] = (p - prev) / span
        for item, n in inv.items():
            prev = _MARKET_PREV["inventory"].get(item)
            if prev is not None:
                inv_velocity[item] = (n - prev) / span

    _MARKET_PREV["turn"] = turn
    _MARKET_PREV["prices"] = dict(prices)
    _MARKET_PREV["inventory"] = dict(inv)

    shed_load = sum(n for n in shed.values()
                    if isinstance(n, (int, float)) and n > 0)

    return {
        "prices": prices,
        "inventory": inv,
        "price_vs_base": {i: (prices[i] / MARKET_PARAMS[i]["base"])
                          for i in prices if MARKET_PARAMS[i]["base"]},
        "price_velocity": price_velocity,
        "inventory_velocity": inv_velocity,
        "shed_load": shed_load,
        "shed_free": max(0, SHED_CAP - shed_load),
        "shed_pressure": shed_load / float(SHED_CAP),
    }


# =====================================================================
# V8 FOUNDATION -- UNIFIED STATE OBJECT (spec section 5.1)
# =====================================================================

def build_state(obs, me, opp, view, seeds, shed, day, hour, animal_plans):
    """One normalized read-only state object per turn.

    Strictly a reader: it must not mutate `view`, `seeds`, `shed` or
    `animal_plans`, and must not touch any RNG -- otherwise the Phase 1
    no-op guarantee breaks in a way that would be very hard to trace.
    Collections are copied, not aliased, for the same reason.

    The `capacity` block is the one genuinely new computation: v7.6
    recomputes overlapping workload numbers in three separate places
    (the hiring formula, the animal-expansion gate, the protected-hand
    count), each with a slightly different definition of "work". Phase 1
    just surfaces them together; unifying them is a later phase, since
    changing any of those definitions changes behavior.
    """
    n_hands = len(me.get("hands", []) or [])
    quads = len(me.get("unlocked_quadrants", []) or [])

    crop_counts = {}
    for row in me["tiles"]:
        for t in row:
            if isinstance(t, dict) and t.get("kind") == "PLANT":
                crop = t.get("crop")
                if crop:
                    crop_counts[crop] = crop_counts.get(crop, 0) + 1

    fleet = {}
    for _pos, tile in view["my_pastures"]:
        sp = tile.get("animal")
        if sp:
            fleet[sp] = fleet.get(sp, 0) + 1

    animal_needs = {
        "unfed": sum(1 for _p, t in view["my_pastures"]
                     if not t.get("fed_today", True)),
        "at_risk": sum(1 for _p, t in view["my_pastures"]
                       if not t.get("fed_today", True)
                       and t.get("consecutive_unfed", 0) >= 1),
        "uncared": sum(1 for _p, t in view["my_pastures"]
                       if not t.get("cared_today", True)),
        "harvestable": sum(1 for _p, t in view["my_pastures"]
                           if t.get("yield_units", 0) > 0),
        "fertilizer_waiting": sum(1 for _p, t in view["my_pastures"]
                                  if t.get("fertilizer_available", False)),
    }

    market = build_market_state(obs, shed, day, hour)

    # Workload views, matching the definitions the existing rules use so
    # the logged numbers are the ones that actually drove the decision.
    crop_backlog = (len(view["urgent_water"]) + len(view["water"]) +
                    len(view["harvest"]))
    animal_work = _pending_animal_work(view)
    unlocked_tiles = max(1, TILES_PER_QUAD * max(1, quads))
    plantable = plantable_crops(dict(seeds), day)
    n_plantable = sum(seeds.get(c, 0) for c in plantable)

    return {
        "day": day,
        "hour": hour,
        "turn": day * 24 + hour,
        "days_remaining": max(0, 29 - day),
        "phase": phase(day),
        "my": {
            "money": me["money"],
            "quads": quads,
            "n_hands": n_hands,
            "farmer": tuple(me["farmer"]),
            "seeds": dict(seeds),
            "shed": dict(shed),
            "crop_counts": crop_counts,
            "n_empty": len(view["empty"]),
            "n_weeds": len(view["weeds"]),
            "n_urgent_water": len(view["urgent_water"]),
            "n_water": len(view["water"]),
            "n_harvest": len(view["harvest"]),
            "fleet": fleet,
            "n_animals": len(view["my_pastures"]),
            "n_empty_pastures": len(view["empty_pastures"]),
            "animal_needs": animal_needs,
            "plans": [{"species": p["species"], "stage": p["stage"],
                       "retries": p.get("retries", 0)} for p in animal_plans],
        },
        "opponent": analyze_opponent(opp, day),
        "market": market,
        "capacity": {
            "crop_backlog": crop_backlog,
            "animal_work": animal_work,
            "weighted_work": crop_backlog + len(view["empty"]) +
                             animal_work * ANIMAL_WORK_WEIGHT,
            "weed_ratio": len(view["weeds"]) / float(unlocked_tiles),
            "n_plantable_seeds": n_plantable,
            "crop_pressure": (len(view["urgent_water"]) + len(view["water"]) +
                              len(view["weeds"]) +
                              min(len(view["empty"]), n_plantable)),
            "hands_per_backlog": (crop_backlog / float(n_hands)) if n_hands else None,
        },
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


def economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans,
            state=None):
    """v8: `state` is threaded through but NOT read by any rule below --
    the decision logic is byte-identical to v7.6. It is here so Phase 2+
    scorers have the normalized state available at the call site without
    another signature change (and another no-op re-verification round)."""
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
    # Phase 4 replaces these fixed money/day thresholds with a land-value
    # comparison against the next cow / hands / seeds / cash. Logged now
    # so there is a "what did the current rule do, and from what state"
    # baseline to compare that against.
    _land_before = len(strategic_orders)
    if 1 <= day <= 22:
        if quads == 1 and budget > 1000:
            strategic_orders.append(["BUY_LAND"]); budget -= 1000
        elif quads == 2 and budget > 2000 and day <= 18:
            strategic_orders.append(["BUY_LAND"]); budget -= 2000
        elif quads == 3 and budget > 4000 and day <= 16:
            strategic_orders.append(["BUY_LAND"]); budget -= 4000
    _log_safe("land", day, hour, lambda: (
        "BUY_LAND" if len(strategic_orders) > _land_before else "HOLD",
        {"quads": quads, "budget_at_decision": me["money"],
         "budget_after": budget,
         "opp_quads": (state or {}).get("opponent", {}).get("land_quadrants")},
        "v7.6 fixed threshold rule"))

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
        want["STRAWBERRY"] = 3   # ongoing crop, small standing patch is enough
    if day <= CUTOFF["TOMATO"] and budget > 600:
        want["TOMATO"] = 3   # ongoing crop, same small-standing-patch approach
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
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
                _log_safe("seed_buy", day, hour, lambda crop=crop, k=k, have=have,
                          tgt=tgt, cost=cost, budget=budget: (
                    [crop, k],
                    {"have": have, "target": tgt, "cost": cost,
                     "budget_after": budget, "space": space,
                     "shed_load": shed_load,
                     "planted_now": (state or {}).get("my", {}).get(
                         "crop_counts", {}).get(crop, 0)},
                    "v7.6 fixed per-crop target"))

    # --- Animal fleet purchase ---
    # Serialized: only start a new purchase (or retry a stalled one) if
    # nothing is currently BOUGHT/CARRYING -- one farmer can only
    # build+carry+place one animal at a time.
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
                # Phase 4 turns this into a marginal-value comparison
                # against land / hands / seeds / cash. The feasibility
                # inputs are logged because the current gate is a
                # five-condition veto, and knowing WHICH condition bound
                # is what makes it improvable.
                _log_safe("animal_buy", day, hour, lambda budget=budget: (
                    target_plan["species"],
                    {"n_animals_before": n_animals,
                     "budget_after": budget,
                     "cost": spec["cost"],
                     "shed_wheat": shed.get("WHEAT", 0),
                     "n_hands": len(me["hands"]),
                     "crop_backlog": (state or {}).get("capacity", {}).get("crop_backlog"),
                     "weed_ratio": (state or {}).get("capacity", {}).get("weed_ratio"),
                     "opp_animals": (state or {}).get("opponent", {}).get("n_animals")},
                    "v7.6 feasibility gate passed"))

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

    # --- Fertilizer straight to market ---
    fert = shed.get("FERTILIZER", 0)
    if fert > 0:
        sell_orders.append(["SELL", "FERTILIZER", fert])

    # --- Paced selling + demand-timing attack ---
    # force_dump relieves shed overflow by selling only the amount needed,
    # at a real price floor, instead of dumping an item's entire quantity.
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
        # `branch` records WHICH of the six selling rules fired. Selling is
        # the spec's highest-priority adaptive target (section 6.5) and the
        # one place v7.7 already failed once by gating the attack dump on
        # price alone -- so knowing the branch mix across a match, not just
        # the totals, is what a Phase 2 redesign needs.
        branch = None
        if is_attack and item in PREMIUM_CROPS:
            branch = "attack_dump"
            qty = max(1, int(n * timing_engine.dump_ratio))
        elif is_holding and item in PREMIUM_CROPS and not force_dump:
            _log_safe("sell", day, hour, lambda item=item, n=n, base=base,
                      price_now=price_now: (
                None,
                {"item": item, "held": int(n), "qty": 0, "price": price_now,
                 "price_vs_base": price_now / float(base),
                 "shed_load": shed_load,
                 "opp_imminent": view["opp_imminent"].get(item, 0),
                 "opp_mature": (state or {}).get("opponent", {}).get(
                     "mature", {}).get(item, 0)},
                "holding_phase"))
            continue
        elif day >= LIQUIDATE_DAY or price_now >= 1.05 * base:
            branch = "liquidate" if day >= LIQUIDATE_DAY else "price_strong"
            qty = int(n)
        elif force_dump and dump_overflow > 0:
            branch = "force_dump_overflow"
            # Sell only enough to relieve the actual overflow, at a real
            # price floor (50% of base) first; dip below it only for
            # whatever residual is still needed.
            dump_floor = 0.5 * base
            want_qty = min(int(n), int(dump_overflow))
            qty = units_sellable_above(item, inv.get(item, I0), dump_floor, want_qty)
            if qty < want_qty:
                qty += min(int(n) - qty, want_qty - qty)
            dump_overflow -= qty
        elif force_dump:
            # Overflow already relieved by earlier (higher-priced) items
            # this turn -- fall through to normal paced selling.
            branch = "force_dump_residual"
            frac = 0.85 if item in PREMIUM_CROPS else 0.70
            if view["opp_imminent"].get(item, 0) >= 4:
                frac -= 0.25
            floor = frac * base
            relax = max(0.0, 1.0 - max(0, shed_load - 40) / 50.0)
            qty = units_sellable_above(item, inv.get(item, I0), floor * relax, int(n))
        else:
            branch = "paced"
            frac = 0.85 if item in PREMIUM_CROPS else 0.70
            if view["opp_imminent"].get(item, 0) >= 4:
                frac -= 0.25
            if behind and item in PREMIUM_CROPS and day >= 20:
                frac += 0.10
            floor = frac * base
            relax = max(0.0, 1.0 - max(0, shed_load - 40) / 50.0)
            qty = units_sellable_above(item, inv.get(item, I0), floor * relax, int(n))
        _log_safe("sell", day, hour, lambda item=item, n=n, qty=qty, base=base,
                  price_now=price_now, branch=branch: (
            (item, int(qty)) if qty > 0 else None,
            {"item": item, "held": int(n), "qty": int(qty),
             "price": price_now,
             "price_vs_base": price_now / float(base),
             "proceeds_est": int(qty) * price_now,
             "market_inventory": inv.get(item, I0),
             "price_velocity": (state or {}).get("market", {}).get(
                 "price_velocity", {}).get(item),
             "shed_load": shed_load,
             "opp_imminent": view["opp_imminent"].get(item, 0),
             "opp_mature": (state or {}).get("opponent", {}).get(
                 "mature", {}).get(item, 0),
             "days_remaining": max(0, 29 - day)},
            branch))
        if qty > 0:
            sell_orders.append(["SELL", item, qty])

    # --- Hiring: real Fibonacci cost, counts animal maintenance workload
    # alongside crops so the hand pool scales with the fleet too. ---
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
        # Hands wipe to zero at every day boundary (confirmed engine
        # mechanic), so this fires once per day and the whole pool is
        # re-bought. Logging `work` alongside `target` is what makes the
        # Phase 4 marginal-hand model calibratable.
        _log_safe("hire", day, hour, lambda n=n, budget=budget: (
            n,
            {"work": work, "target": target, "need": need,
             "hired": n, "hands_before": len(me["hands"]),
             "animal_work": animal_work,
             "n_weeds": len(view["weeds"]),
             "budget_after": budget,
             "opp_hands": (state or {}).get("opponent", {}).get("n_hands")},
            "v7.6 work/5 formula, weeds excluded"))

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
# ANIMAL PIPELINE (farmer-owned)
#
# Setup stages per plan: NONE -> BOUGHT -> (build) -> CARRYING -> ACTIVE;
# ABANDONED on repeated failure. Only one plan is ever BOUGHT/CARRYING at
# a time. Maintenance is stateless and fleet-wide: it always operates on
# the nearest tile in view["my_pastures"], which naturally includes every
# ACTIVE plan's site regardless of species or how many are active.
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
        # Engine only clears the "animal" key (2 consecutive unfed days),
        # never the tile itself -- should be rare, but treat as abandoned
        # if the animal's gone and we're not carrying a replacement.
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
        # Prefer a still-unclaimed reserved near-shed slot over the nearest
        # fallback, so daily walks stay short even for late purchases.
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
    """Rank a pasture's urgency (lower = more urgent): overdue-unfed >
    unfed > ready-to-harvest > needs-care > fertilizer-waiting > nothing
    pending, distance as tiebreak."""
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
    """Stateless daily care across the whole active fleet. Targets whichever
    pasture has the most urgent pending need (see _pasture_priority).

    Works for any worker (`carry` is that worker's own carry inventory).
    `exclude` is the set of pasture positions already claimed by an earlier
    worker this turn, so multiple workers don't converge on the same
    animal.

    `critical_only` (v7.6a): when True, this worker will only engage with
    feed-related survival work (an animal due for feeding today, or
    already overdue) -- never CARE, HARVEST, COLLECT_FERTILIZER, or
    carried-product deposit trips. This is what lets a reserved crop hand
    still respond to an animal-death risk without being pulled into
    optional animal upkeep that isn't a survival matter. Real ladder
    replays showed exactly this optional work (CARE/HARVEST/FERTILIZER
    collection climbing from ~2/day to 9-11/day) crowding out crop
    watering/weeding as the fleet grew.

    Returns (op_or_None, claimed_pos_or_None) -- callers should add the
    claimed position to their `exclude` set before calling this for the
    next worker."""
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
    # Only claim ppos if it has real pending work.
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

    return None, None  # nothing pending for this worker -- falls back to crops


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
    """v7.6a: weeds start last (matches v7.5) but get promoted as
    infestation grows -- ahead of ordinary planting once there are a
    few, ahead of ordinary watering too once it's severe. Real replays
    showed weed count climbing unchecked to 20-37/100 tiles while weeds
    stayed lowest priority the whole match."""
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
                    tasks["urgent_water"].append((x, y))  # same-day water invariant
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

    fallback = _step_toward((x, y), (4, 4))  # idle drift toward shed
    return [fallback] if fallback else ["PASS"]


# =====================================================================
# ENTRY
# =====================================================================

timing_engine = DemandTimingEngine(match_seed=42)
animal_plans = []    # fleet state -- list of per-animal plan dicts, mutated in place
reserved_sites = []  # near-shed tiles claimed for the fleet, grown incrementally
                      # by _grow_reserved_sites (one per animal actually purchased)


def _init_reserved_sites(view):
    """Accessor for the fleet's currently-reserved near-shed tiles."""
    return reserved_sites


def _reserved_crop_hand_count(view, seeds, day, n_hands, quads):
    """v7.6a: how many of the current hands are walled off for crop-only
    work this turn. Scales with real symptoms of neglect (weed density,
    crop backlog relative to hand count) rather than a flat number."""
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

    # v8 Phase 1: build the normalized state once per turn, after
    # reconciliation so plan stages are current. Read-only -- no rule
    # below consumes it yet.
    state = build_state(obs, me, opp, view, seeds, shed, day, hour, animal_plans)

    market = economy(obs, me, opp, view, seeds, day, hour, timing_engine,
                     animal_plans, state=state)

    crops_now = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(c, 0) for c in crops_now)

    task_order = _task_order(len(view["weeds"]))
    tasks = {
        "urgent_water": list(view["urgent_water"]),
        "harvest": list(view["harvest"]),
        "water": list(view["water"]),
        "plant": (view["empty"][:n_plantable] if crops_now and hour < 21 else []),
        # v7.6a: weed-clearing no longer shuts off for the last two days --
        # replays showed the collapse was already well underway by day 25,
        # long before that cutoff mattered, and disabling it just let the
        # infestation stand unchallenged during the final push.
        "weeds": list(view["weeds"]),
    }
    # Never plant on an in-progress pasture site or an unclaimed reserved
    # near-shed slot -- keeps it available/close for whenever the next
    # purchase actually fires.
    claimed_sites = {pl["site"] for pl in animal_plans if pl.get("site") and pl["stage"] != "ABANDONED"}
    excluded = claimed_sites | set(sites)
    if excluded:
        tasks["plant"] = [t for t in tasks["plant"] if t not in excluded]

    quads = len(me["unlocked_quadrants"])
    n_hands = len(me["hands"])
    reserved_count = _reserved_crop_hand_count(view, seeds, day, n_hands, quads)

    farmer_pos = tuple(me["farmer"])
    active_setup_plan = next((pl for pl in animal_plans if pl["stage"] in ("BOUGHT", "CARRYING")), None)
    # An urgent feed need on an already-placed pasture preempts setup work
    # for the turn, so setting up animal N+1 can't starve animal N.
    urgent_existing_feed = any(
        not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
        for _pos, t in view["my_pastures"]
    )
    claimed_pastures = set()
    farmer_op = None
    if active_setup_plan is not None and not urgent_existing_feed:
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        # Farmer keeps v7.5's original unconditional (critical_only=False)
        # maintenance-first behavior -- only the hand pool is split below.
        farmer_op, claim = animal_maintenance_action(farmer_pos, view, shed, farmer_carry, day, hour, claimed_pastures)
        if claim is not None:
            claimed_pastures.add(claim)
    if farmer_op is None and active_setup_plan is not None:
        # Nothing urgent for maintenance (e.g. no wheat staged yet) -- fall
        # back to setup work rather than idling.
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        farmer_op = unit_action(farmer_pos, tasks, seeds, day, task_order)

    # v7.6a: the first `reserved_count` hands are walled off for crop work
    # -- they may still answer a feed-critical animal need (critical_only
    # still checks fed_today), but never the optional maintenance
    # (CARE/HARVEST/COLLECT_FERTILIZER/product deposit) that was crowding
    # out watering/weeding in the real loss replays. Remaining hands keep
    # v7.5's original full-priority behavior.
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
        else:
            hand_ops.append(unit_action(hand_pos, tasks, seeds, day, task_order))

    # Per-turn mechanism trace. The v7.5->v7.6 round proved that final
    # money alone can't tell you whether a fix worked by the mechanism you
    # intended -- that needed weed-count and water-action curves over
    # time, written as one-off scripts each round and then thrown away.
    # This makes the trace a permanent capability, including on the ladder
    # where replays can't reconstruct it.
    def _turn_payload():
        kinds = {}
        for op in [farmer_op] + hand_ops:
            if op:
                kinds[op[0]] = kinds.get(op[0], 0) + 1
        return {
            "money": me["money"],
            "opp_money": opp["money"],
            "n_hands": n_hands,
            "reserved_crop_hands": reserved_count,
            "n_animals": len(view["my_pastures"]),
            "n_weeds": len(view["weeds"]),
            "n_empty": len(view["empty"]),
            "n_urgent_water": len(view["urgent_water"]),
            "n_water": len(view["water"]),
            "n_harvest": len(view["harvest"]),
            "crop_counts": state["my"]["crop_counts"],
            "seeds": dict(seeds),
            "shed_load": state["market"]["shed_load"],
            "action_kinds": kinds,
            "market_orders": len(market),
            "opp_animals": state["opponent"]["n_animals"],
            "opp_crop_tiles": state["opponent"]["total_crop_tiles"],
        }

    _snapshot_safe("turn", day, hour, _turn_payload)

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
