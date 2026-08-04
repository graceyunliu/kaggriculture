import math
import random
import sys
import traceback

# =====================================================================
# V6 DIAGNOSTIC HYBRID
# - Preserves the v5 crop/market strategy
# - Fixes labor, budget, fertilizer, task-reservation, and planting guards
# - Adds one-cow diagnostic placement and schema logging
# =====================================================================

PRICE_FLOOR = 1
I0 = 10_000
SHED_CAP = 100
LIQUIDATE_DAY = 28
MAX_MARKET_ORDERS = 10
MAX_HANDS = 8
MAX_SELL_SLOTS = 5
MAX_HIRE_SLOTS = 2
MAX_SEED_SLOTS = 2

# Conservative accounting estimates. These affect only virtual budgeting;
# the engine remains the source of truth for whether an order is affordable.
LAND_COST_BY_OWNED_QUADS = {1: 1000, 2: 2000, 3: 4000}
HIRE_COST_ESTIMATE = 100
COW_COST_ESTIMATE = 500
WHEAT_BUY_COST_ESTIMATE = 25

ANIMAL_BUY_START_DAY = 12
ANIMAL_BUY_END_DAY = 14
ANIMAL_MAINTENANCE_CAP_PER_DAY = 20
ANIMAL_STAGE_TIMEOUT = 8
ANIMAL_ACTION_RETRIES = 3
SHED_POS = (0, 0)

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
    base, threshold = p["base"], p["T"]
    if inventory < I0:
        amp = p["bt"] * base / _shape(p["bf"], threshold)
        price = base + amp * _shape(p["bf"], I0 - inventory)
    else:
        amp = p["at"] * base / _shape(p["af"], threshold)
        price = base - amp * _shape(p["af"], inventory - I0)
    return max(PRICE_FLOOR, int(round(price)))


def units_sellable_above(item, inventory, min_price, cap):
    n = 0
    while n < cap and market_price(item, inventory + n) >= min_price:
        n += 1
    return n


class DemandTimingEngine:
    def __init__(self, match_seed=42):
        self.rng = random.Random(match_seed)
        self.d10_target_turn = 9 * 24 + self.rng.randint(-2, 2)
        self.d20_target_turn = 19 * 24 + self.rng.randint(-2, 2)
        self.dump_ratio = self.rng.uniform(0.65, 0.85)

    def is_holding_phase(self, day, hour):
        curr_turn = day * 24 + hour
        return ((7 * 24 <= curr_turn < self.d10_target_turn) or
                (17 * 24 <= curr_turn < self.d20_target_turn))

    def is_attack_turn(self, day, hour):
        curr_turn = day * 24 + hour
        return curr_turn in (self.d10_target_turn, self.d20_target_turn)


def _animal_species(tile):
    value = tile.get("animal") or tile.get("species") or tile.get("animal_type")
    if isinstance(value, str):
        return value.upper()
    # Avoid treating a generic tile "type" such as ANIMAL as the species.
    value = tile.get("type")
    if isinstance(value, str) and value.upper() not in {"ANIMAL", "PASTURE", "PLANT", "WEED"}:
        return value.upper()
    return None


def _is_cow_tile(tile):
    return isinstance(tile, dict) and _animal_species(tile) == "COW"


def perceive(me, opp, day):
    urgent_water, water, harvest, empty, weeds = [], [], [], [], []
    animals, empty_pastures = [], []
    feed, care, animal_harvest, collect_fert = [], [], [], []

    for y, row in enumerate(me["tiles"]):
        for x, tile in enumerate(row):
            if tile is None:
                empty.append((x, y))
                continue
            if not isinstance(tile, dict):
                continue

            kind = tile.get("kind")
            if kind == "WEED":
                weeds.append((x, y))
            elif kind == "PLANT":
                if not tile.get("watered_today", False):
                    if tile.get("consecutive_unwatered", 0) >= 1:
                        urgent_water.append((x, y))
                    else:
                        water.append((x, y))
                crop = CROPS.get(tile.get("crop"))
                if crop:
                    age = day - tile.get("planted_day", day)
                    yield_units = tile.get("yield_units", 0)
                    ready = crop["ongoing"] or (
                        age >= crop["first"] and
                        (yield_units >= crop["max_yield"] or age >= crop["max_day"])
                    )
                    if yield_units > 0 and ready:
                        harvest.append((x, y))
            elif kind == "PASTURE":
                # Diagnostic assumption: an empty pasture may have no animal/species field.
                if not (_animal_species(tile) or tile.get("occupied", False)):
                    empty_pastures.append((x, y))
            elif kind == "ANIMAL" or _animal_species(tile):
                animals.append((x, y, tile))
                print(f"ANIMAL_SCHEMA day={day} pos=({x},{y}): {tile!r}", file=sys.stderr)

                # Known/likely aliases. Tasks are only scheduled when a state key exists,
                # preventing endless invalid-action spam when the schema differs.
                fed_key = next((k for k in ("fed_today", "is_fed", "fed") if k in tile), None)
                cared_key = next((k for k in ("cared_today", "is_cared", "cared") if k in tile), None)
                yield_key = next((k for k in ("yield_units", "product_units", "ready_units") if k in tile), None)
                fert_key = next((k for k in ("fertilizer_ready", "has_fertilizer", "manure_ready") if k in tile), None)

                if fed_key is not None and not tile.get(fed_key, False):
                    feed.append((x, y))
                if cared_key is not None and not tile.get(cared_key, False):
                    care.append((x, y))
                if yield_key is not None and tile.get(yield_key, 0) > 0:
                    animal_harvest.append((x, y))
                if fert_key is not None and tile.get(fert_key, False):
                    collect_fert.append((x, y))

    imminent = {}
    for row in opp["tiles"]:
        for tile in row:
            if isinstance(tile, dict) and tile.get("kind") == "PLANT":
                crop = CROPS.get(tile.get("crop"))
                if crop:
                    age = day - tile.get("planted_day", day)
                    if crop["first"] - 2 <= age <= crop["max_day"]:
                        name = tile.get("crop")
                        imminent[name] = imminent.get(name, 0) + 1

    return {
        "urgent_water": urgent_water,
        "water": water,
        "harvest": harvest,
        "empty": empty,
        "weeds": weeds,
        "animals": animals,
        "empty_pastures": empty_pastures,
        "feed": feed,
        "care": care,
        "animal_harvest": animal_harvest,
        "collect_fert": collect_fert,
        "opp_imminent": imminent,
    }


def phase(day):
    return 0 if day < 10 else (1 if day < 20 else 2)


def plantable_crops(seeds, day):
    return [crop for crop in PLANT_PRIORITY
            if seeds.get(crop, 0) > 0 and day <= CUTOFF.get(crop, -1)]


def _append_order(orders, order, max_slots=MAX_MARKET_ORDERS):
    if len(orders) >= max_slots:
        return False
    orders.append(order)
    return True


def economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plan):
    budget = me["money"]
    shed = obs["private"]["shed"]
    inv = obs["market"]["inventory"]
    behind = me["money"] < opp["money"] - 500
    quads = len(me["unlocked_quadrants"])

    # Build category buckets first, then merge them in a fixed order. This makes
    # the slot policy real rather than relying on a final list slice.
    strategic_orders = []
    feed_orders = []
    sell_orders = []
    hire_orders = []
    seed_orders = []

    cow_on_board = any(_is_cow_tile(t) for _, _, t in view["animals"])
    generic_animal_seen = bool(view["animals"]) and not cow_on_board
    cow_in_shed = shed.get("COW", 0)

    should_buy_cow = (
        ANIMAL_BUY_START_DAY <= day <= ANIMAL_BUY_END_DAY
        and animal_plan["stage"] == "IDLE"
        and not cow_on_board
        and not generic_animal_seen
        and cow_in_shed == 0
        and budget > 1000
    )

    if should_buy_cow:
        strategic_orders.append(["BUY_ANIMAL", "COW", 1])
        budget -= COW_COST_ESTIMATE
        animal_plan.update({
            "stage": "WAIT_FOR_PURCHASE",
            "stage_started_turn": day * 24 + hour,
            "retries": 0,
        })
    elif 1 <= day <= 22:
        land_cost = LAND_COST_BY_OWNED_QUADS.get(quads)
        allow_land = (
            (quads == 1) or
            (quads == 2 and day <= 18) or
            (quads == 3 and day <= 16)
        )
        if land_cost is not None and allow_land and budget > land_cost:
            strategic_orders.append(["BUY_LAND"])
            budget -= land_cost

    # Two-day feed reserve, including a cow whose purchase is pending.
    confirmed_animals = len(view["animals"]) + cow_in_shed
    if animal_plan["stage"] == "WAIT_FOR_PURCHASE":
        confirmed_animals = max(confirmed_animals, 1)
    target_wheat = confirmed_animals * 2
    have_wheat = shed.get("WHEAT", 0)
    if target_wheat > have_wheat:
        buy_qty = min(target_wheat - have_wheat, 10)
        unit_cost = max(PRICE_FLOOR, market_price("WHEAT", inv.get("WHEAT", I0)))
        estimated_cost = buy_qty * unit_cost
        if budget >= estimated_cost:
            feed_orders.append(["BUY_PRODUCT", "WHEAT", buy_qty])
            budget -= estimated_cost

    fert_qty = shed.get("FERTILIZER", 0)
    if fert_qty > 0:
        sell_orders.append(["SELL", "FERTILIZER", fert_qty])

    shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)
    force_dump = shed_load > SHED_CAP - 15 and hour >= 18
    is_attack = timing_engine.is_attack_turn(day, hour)
    is_holding = timing_engine.is_holding_phase(day, hour)

    sellable = [(item, n) for item, n in shed.items()
                if isinstance(n, (int, float)) and n > 0 and
                item in MARKET_PARAMS and item != "FERTILIZER"]

    # Fertilizer counts against the five-slot selling allocation.
    remaining_sell_slots = max(0, MAX_SELL_SLOTS - len(sell_orders))
    for item, n in sorted(sellable, key=lambda kv: -market_price(kv[0], inv.get(kv[0], I0))):
        if len(sell_orders) >= MAX_SELL_SLOTS:
            break
        base = MARKET_PARAMS[item]["base"]
        price_now = market_price(item, inv.get(item, I0))
        if is_attack and item in PREMIUM_CROPS:
            qty = max(1, int(n * timing_engine.dump_ratio))
        elif is_holding and item in PREMIUM_CROPS and not force_dump:
            continue
        elif force_dump or day >= LIQUIDATE_DAY or price_now >= 1.05 * base:
            qty = n
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

    if hour == 0 and day < 29:
        work = (len(view["water"]) + len(view["urgent_water"]) +
                len(view["harvest"]) + len(view["empty"]))
        target = max(4, min(MAX_HANDS, math.ceil(work / 5)))
        hire_count = min(MAX_HIRE_SLOTS, max(0, target - len(me["hands"])))
        for _ in range(hire_count):
            if budget < HIRE_COST_ESTIMATE:
                break
            hire_orders.append(["HIRE"])
            budget -= HIRE_COST_ESTIMATE

    ph = phase(day)
    space = len(view["empty"]) + 2
    want = {}
    if day <= CUTOFF["MELON"] and budget > 700:
        want["MELON"] = min(space, 6 if ph == 0 else 10)
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
        want["WHEAT"] = 4

    reserve = 500 if ph == 0 else 200
    for crop, target in want.items():
        if len(seed_orders) >= MAX_SEED_SLOTS:
            break
        have = seeds.get(crop, 0)
        qty = max(0, target - have)
        cost = CROPS[crop]["seed"] * qty
        if qty > 0 and budget - reserve >= cost:
            seed_orders.append(["BUY_SEED", crop, qty])
            budget -= cost

    # Fixed merge order: 1 strategic, 1 feed, up to 5 sales, 2 hires, 2 seeds.
    # If fewer slots are used early, later categories may use the spare capacity.
    orders = []
    for bucket in (strategic_orders, feed_orders, sell_orders, hire_orders, seed_orders):
        for order in bucket:
            if len(orders) >= MAX_MARKET_ORDERS:
                break
            orders.append(order)
    return orders

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


def _shed_adjacent_target(me, pos):
    height = len(me["tiles"])
    width = len(me["tiles"][0]) if height else 0
    candidates = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    valid = [(x, y) for x, y in candidates if 0 <= x < width and 0 <= y < height]
    return _nearest(pos, valid) if valid else SHED_POS


def _turn(day, hour):
    return day * 24 + hour


def _set_stage(animal_plan, stage, day, hour, **updates):
    animal_plan.update({
        "stage": stage,
        "stage_started_turn": _turn(day, hour),
        "retries": 0,
        **updates,
    })


def _stage_timed_out(animal_plan, day, hour, timeout=ANIMAL_STAGE_TIMEOUT):
    started = animal_plan.get("stage_started_turn")
    return started is not None and _turn(day, hour) - started >= timeout


def _target_is_pasture(view, target):
    return target is not None and target in view["empty_pastures"]


def _reconcile_animal_plan(animal_plan, view, shed, day, hour):
    stage = animal_plan.get("stage", "IDLE")
    target = animal_plan.get("target")
    cow_in_shed = shed.get("COW", 0) > 0
    cow_on_board = any(_is_cow_tile(t) for _, _, t in view["animals"])
    # During placement verification only, accept a generic animal exactly at
    # the planned pasture as provisional success while the schema is unknown.
    generic_at_target = any((x, y) == target for x, y, _ in view["animals"])
    cow_confirmed = cow_on_board or (stage == "VERIFY_ACTIVE" and generic_at_target)

    if cow_confirmed:
        active_pos = next(((x, y) for x, y, t in view["animals"]
                           if _is_cow_tile(t) or (x, y) == target), None)
        _set_stage(animal_plan, "ACTIVE", day, hour, target=None, active_pos=active_pos)
        return

    active_pos = animal_plan.get("active_pos")
    generic_active_seen = any((x, y) == active_pos for x, y, _ in view["animals"])
    if stage == "ACTIVE" and not (cow_on_board or generic_active_seen):
        # The board no longer confirms the cow. Return to diagnostics instead of
        # pretending it remains active.
        _set_stage(animal_plan, "IDLE", day, hour, target=None)
        return

    if stage == "WAIT_FOR_PURCHASE":
        if cow_in_shed:
            _set_stage(animal_plan, "MOVE_TO_LAND", day, hour)
        elif _stage_timed_out(animal_plan, day, hour, timeout=4):
            _set_stage(animal_plan, "IDLE", day, hour, target=None)
        return

    if stage == "VERIFY_PASTURE":
        if _target_is_pasture(view, target):
            _set_stage(animal_plan, "MOVE_TO_SHED", day, hour)
        elif _stage_timed_out(animal_plan, day, hour, timeout=2):
            retries = animal_plan.get("retries", 0) + 1
            if retries >= ANIMAL_ACTION_RETRIES:
                _set_stage(animal_plan, "MOVE_TO_LAND", day, hour, target=None)
            else:
                animal_plan.update({"stage": "BUILD", "retries": retries,
                                    "stage_started_turn": _turn(day, hour)})
        return

    if stage == "VERIFY_PICKUP":
        # Shed quantity dropping is the strongest available confirmation that
        # pickup succeeded. If inventory later appears in observations, add it here.
        if not cow_in_shed:
            _set_stage(animal_plan, "MOVE_TO_PASTURE", day, hour)
        elif _stage_timed_out(animal_plan, day, hour, timeout=2):
            retries = animal_plan.get("retries", 0) + 1
            if retries >= ANIMAL_ACTION_RETRIES:
                _set_stage(animal_plan, "MOVE_TO_SHED", day, hour)
            else:
                animal_plan.update({"stage": "PICKUP", "retries": retries,
                                    "stage_started_turn": _turn(day, hour)})
        return

    if stage == "VERIFY_ACTIVE":
        if cow_confirmed:
            _set_stage(animal_plan, "ACTIVE", day, hour, target=None)
        elif _stage_timed_out(animal_plan, day, hour, timeout=2):
            retries = animal_plan.get("retries", 0) + 1
            if retries >= ANIMAL_ACTION_RETRIES:
                # If the cow is back in shed, restart pickup; otherwise stop the
                # plan rather than passing forever with unknown inventory state.
                if cow_in_shed:
                    _set_stage(animal_plan, "MOVE_TO_SHED", day, hour)
                else:
                    _set_stage(animal_plan, "IDLE", day, hour, target=None)
            else:
                animal_plan.update({"stage": "PLACE", "retries": retries,
                                    "stage_started_turn": _turn(day, hour)})
        return

    # Global stale-state guard for movement stages.
    if stage not in {"IDLE", "ACTIVE"} and _stage_timed_out(animal_plan, day, hour):
        if cow_in_shed:
            _set_stage(animal_plan, "MOVE_TO_LAND" if target is None else "MOVE_TO_SHED", day, hour)
        else:
            _set_stage(animal_plan, "IDLE", day, hour, target=None)


def animal_setup_action(pos, me, view, shed, animal_plan, day, hour):
    stage = animal_plan["stage"]
    target = animal_plan.get("target")

    if stage in {"IDLE", "WAIT_FOR_PURCHASE", "ACTIVE", "VERIFY_PASTURE",
                 "VERIFY_PICKUP", "VERIFY_ACTIVE"}:
        return None

    if stage == "MOVE_TO_LAND":
        if target is None or target not in view["empty"]:
            candidates = sorted(view["empty"], key=lambda p: abs(p[0]) + abs(p[1]), reverse=True)
            if not candidates:
                return None
            target = candidates[0]
            animal_plan["target"] = target
            animal_plan["stage_started_turn"] = _turn(day, hour)
        if pos != target:
            return [_step_toward(pos, target)]
        _set_stage(animal_plan, "BUILD", day, hour)
        stage = "BUILD"

    if stage == "BUILD":
        target = animal_plan.get("target")
        if pos != target:
            _set_stage(animal_plan, "MOVE_TO_LAND", day, hour)
            return [_step_toward(pos, target)] if target else None
        # Do not advance to the shed until the next observation confirms pasture.
        animal_plan.update({"stage": "VERIFY_PASTURE",
                            "stage_started_turn": _turn(day, hour)})
        return ["BUILD_PASTURE"]

    if stage == "MOVE_TO_SHED":
        shed_adjacent = _shed_adjacent_target(me, pos)
        if pos != shed_adjacent:
            return [_step_toward(pos, shed_adjacent)]
        _set_stage(animal_plan, "PICKUP", day, hour)
        stage = "PICKUP"

    if stage == "PICKUP":
        animal_plan.update({"stage": "VERIFY_PICKUP",
                            "stage_started_turn": _turn(day, hour)})
        return ["PICKUP", "COW", 1]

    if stage == "MOVE_TO_PASTURE":
        target = animal_plan.get("target")
        if target is None:
            _set_stage(animal_plan, "IDLE", day, hour, target=None)
            return None
        if pos != target:
            return [_step_toward(pos, target)]
        _set_stage(animal_plan, "PLACE", day, hour)
        stage = "PLACE"

    if stage == "PLACE":
        target = animal_plan.get("target")
        if pos != target:
            _set_stage(animal_plan, "MOVE_TO_PASTURE", day, hour)
            return [_step_toward(pos, target)] if target else None
        animal_plan.update({"stage": "VERIFY_ACTIVE",
                            "stage_started_turn": _turn(day, hour)})
        return ["PLACE", "COW", 1]

    return None


TASK_ORDER = [
    "urgent_water", "feed", "animal_harvest", "care", "collect_fert",
    "harvest", "water", "plant", "weeds"
]
TASK_ACTION = {
    "urgent_water": ["WATER"],
    "feed": ["FEED"],
    "animal_harvest": ["HARVEST"],
    "care": ["CARE"],
    "collect_fert": ["COLLECT_FERTILIZER"],
    "harvest": ["HARVEST"],
    "water": ["WATER"],
    "weeds": ["DIG"],
}
ANIMAL_TASKS = {"feed", "animal_harvest", "care", "collect_fert"}


def unit_action(pos, tasks, seeds, day, action_budget):
    x, y = pos

    for key in TASK_ORDER:
        if (x, y) not in tasks[key]:
            continue
        if key in ANIMAL_TASKS and action_budget["animal_maintenance_actions"] >= ANIMAL_MAINTENANCE_CAP_PER_DAY:
            continue

        tasks[key].remove((x, y))
        if key == "plant":
            for crop in plantable_crops(seeds, day):
                seeds[crop] -= 1
                return ["PLANT", crop]
            continue

        if key in ANIMAL_TASKS:
            action_budget["animal_maintenance_actions"] += 1
        return TASK_ACTION[key]

    # Do not delete a target merely because a unit starts moving toward it.
    # Multiple workers may converge, but only the first arrival consumes it.
    for key in TASK_ORDER:
        if key in ANIMAL_TASKS and action_budget["animal_maintenance_actions"] >= ANIMAL_MAINTENANCE_CAP_PER_DAY:
            continue
        target = _nearest((x, y), tasks[key])
        if target:
            step = _step_toward((x, y), target)
            if step:
                if key in ANIMAL_TASKS:
                    action_budget["animal_maintenance_actions"] += 1
                return [step]

    fallback = _step_toward((x, y), SHED_POS)
    return [fallback] if fallback else ["PASS"]


# Persistent episode state.
timing_engine = DemandTimingEngine(match_seed=42)
animal_plan = {"stage": "IDLE", "target": None, "stage_started_turn": None, "retries": 0}
action_budget = {"day": None, "animal_maintenance_actions": 0}


def _agent(obs):
    player = obs["player"]
    me, opp = obs["farms"][player], obs["farms"][1 - player]
    day, hour = obs["day"], obs["hour"]
    seeds = dict(obs["private"]["seeds"])
    shed = obs["private"]["shed"]

    if action_budget["day"] != day:
        action_budget.update({"day": day, "animal_maintenance_actions": 0})

    view = perceive(me, opp, day)
    _reconcile_animal_plan(animal_plan, view, shed, day, hour)

    market = economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plan)

    crops_now = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(crop, 0) for crop in crops_now)

    # Conservative planting guard: stop early and cap new planting by workers not
    # already needed for urgent watering. This reduces, but cannot fully prove,
    # same-turn watering without engine-level action-resolution guarantees.
    total_units = 1 + len(me["hands"])
    free_units = max(0, total_units - len(view["urgent_water"]))
    latest_plant_hour = max(0, 24 - total_units)
    plant_slots = min(n_plantable, len(view["empty"]), free_units // 2)
    allow_planting = bool(crops_now) and hour < latest_plant_hour and plant_slots > 0

    tasks = {
        "urgent_water": list(view["urgent_water"]),
        "feed": list(view["feed"]),
        "animal_harvest": list(view["animal_harvest"]),
        "care": list(view["care"]),
        "collect_fert": list(view["collect_fert"]),
        "harvest": list(view["harvest"]),
        "water": list(view["water"]),
        "plant": list(view["empty"][:plant_slots]) if allow_planting else [],
        "weeds": list(view["weeds"]) if day <= 27 else [],
    }

    # The farmer exclusively owns the multi-turn cow setup plan.
    farmer_op = animal_setup_action(me["farmer"], me, view, shed, animal_plan, day, hour)
    if farmer_op is None:
        farmer_op = unit_action(me["farmer"], tasks, seeds, day, action_budget)

    hand_ops = [unit_action(hand, tasks, seeds, day, action_budget) for hand in me["hands"]]
    return {"farmer": farmer_op, "hands": hand_ops, "market": market}


def agent(obs, configuration=None):
    try:
        return _agent(obs)
    except Exception as exc:
        print(f"GUARD swallowed exception: {exc!r}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"farmer": ["PASS"], "hands": [], "market": []}
