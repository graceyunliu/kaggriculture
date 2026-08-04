import math
import random
from collections import deque

# =====================================================================
# LAYER 1: WORLD MODEL & CONSTANTS (Copied / verified against engine)
# =====================================================================

PRICE_FLOOR = 1
I0 = 10_000
SHED_CAP = 100
LIQUIDATE_DAY = 28

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


# =====================================================================
# V5 MODULE: RANDOMIZED DEMAND TIMING ENGINE
# =====================================================================

class DemandTimingEngine:
    def __init__(self, match_seed=42):
        self.rng = random.Random(match_seed)
        # Randomize timing windows around Day 10 and Day 20 town demand jumps
        self.d10_target_turn = 9 * 24 + self.rng.randint(-2, 2)
        self.d20_target_turn = 19 * 24 + self.rng.randint(-2, 2)
        self.dump_ratio = self.rng.uniform(0.65, 0.85)

    def is_holding_phase(self, day, hour):
        curr_turn = day * 24 + hour
        if 7 * 24 <= curr_turn < self.d10_target_turn:
            return True
        if 17 * 24 <= curr_turn < self.d20_target_turn:
            return True
        return False

    def is_attack_turn(self, day, hour):
        curr_turn = day * 24 + hour
        return curr_turn == self.d10_target_turn or curr_turn == self.d20_target_turn


# =====================================================================
# LAYER 2: PERCEPTION & STATE TRACKER
# =====================================================================

def perceive(me, opp, day):
    urgent_water, water, harvest, empty, weeds = [], [], [], [], []
    for y, row in enumerate(me["tiles"]):
        for x, t in enumerate(row):
            if t is None:
                empty.append((x, y))
            elif not isinstance(t, dict):
                continue
            elif t.get("kind") == "WEED":
                weeds.append((x, y))
            elif t.get("kind") == "PLANT":
                if not t["watered_today"]:
                    if t.get("consecutive_unwatered", 0) >= 1:
                        urgent_water.append((x, y))
                    else:
                        water.append((x, y))
                c = CROPS.get(t["crop"])
                if c:
                    age = day - t["planted_day"]
                    ready = c["ongoing"] or (age >= c["first"] and
                            (t["yield_units"] >= c["max_yield"] or age >= c["max_day"]))
                    if t["yield_units"] > 0 and ready:
                        harvest.append((x, y))

    imminent = {}
    for row in opp["tiles"]:
        for t in row:
            if isinstance(t, dict) and t.get("kind") == "PLANT":
                c = CROPS.get(t["crop"])
                if c:
                    age = day - t["planted_day"]
                    if c["first"] - 2 <= age <= c["max_day"]:
                        imminent[t["crop"]] = imminent.get(t["crop"], 0) + 1

    return {
        "urgent_water": urgent_water,
        "water": water,
        "harvest": harvest,
        "empty": empty,
        "weeds": weeds,
        "opp_imminent": imminent
    }


# =====================================================================
# LAYER 3: V5 HIGH-SCALE ECONOMY POLICY (D40/D41 + Macro + Timing)
# =====================================================================

def phase(day):
    return 0 if day < 10 else (1 if day < 20 else 2)


def plantable_crops(seeds, day):
    return [c for c in PLANT_PRIORITY if seeds.get(c, 0) > 0 and day <= CUTOFF.get(c, -1)]


def economy(obs, me, opp, view, seeds, day, hour, timing_engine):
    market_orders = []
    money = me["money"]
    shed = obs["private"]["shed"]
    inv = obs["market"]["inventory"]
    behind = money < opp["money"] - 500
    quads = len(me["unlocked_quadrants"])

    # --- 1. Aggressive Macro Land Expansion (v5 Upgrade) ---
    if day >= 1 and day <= 22:
        if quads == 1 and money > 1000:
            market_orders.append(["BUY_LAND"])
            money -= 1000
        elif quads == 2 and money > 2000 and day <= 18:
            market_orders.append(["BUY_LAND"])
            money -= 2000
        elif quads == 3 and money > 4000 and day <= 16:
            market_orders.append(["BUY_LAND"])
            money -= 4000

    # --- 2. D41 JIT Feed & D40 Fertilizer Liquidation ---
    active_animals = me.get("animals", [])
    if len(active_animals) > 0:
        needed_wheat = len(active_animals) * 2
        have_wheat = shed.get("WHEAT", 0)
        if have_wheat < needed_wheat:
            buy_qty = min(needed_wheat - have_wheat, 10)
            market_orders.append(["BUY_PRODUCT", "WHEAT", buy_qty])

    fert_qty = shed.get("FERTILIZER", 0)
    if fert_qty > 0 and len(market_orders) < 10:
        market_orders.append(["SELL", "FERTILIZER", min(fert_qty, 10 - len(market_orders))])

    # --- 3. Paced Selling vs Turn-0 Timing Attack ---
    shed_load = sum(n for k, n in shed.items() if n > 0)
    force_dump = shed_load > SHED_CAP - 15 and hour >= 18
    is_attack = timing_engine.is_attack_turn(day, hour)
    is_holding = timing_engine.is_holding_phase(day, hour)

    sellable = [(i, n) for i, n in shed.items() if n > 0 and i in MARKET_PARAMS and i != "FERTILIZER"]

    for item, n in sorted(sellable, key=lambda kv: -market_price(kv[0], inv.get(kv[0], I0))):
        if len(market_orders) >= 10:
            break

        base = MARKET_PARAMS[item]["base"]
        price_now = market_price(item, inv.get(item, I0))

        # Turn-0 Timing Attack Liquidation Window
        if is_attack and item in PREMIUM_CROPS:
            qty = max(1, int(n * timing_engine.dump_ratio))
            market_orders.append(["SELL", item, qty])
            continue

        # Hold Premium Crops right before Town Demand Jump (unless Shed is full)
        if is_holding and item in PREMIUM_CROPS and not force_dump:
            continue

        # Standard Paced Selling Floor Math
        if force_dump or day >= LIQUIDATE_DAY:
            qty = n
        elif price_now >= 1.05 * base:
            qty = n
        else:
            frac = 0.85 if item in PREMIUM_CROPS else 0.70
            if item in view["opp_imminent"] and view["opp_imminent"][item] >= 4:
                frac -= 0.25  # Front-run opponent harvest gluts
            if behind and item in PREMIUM_CROPS and day >= 20:
                frac += 0.10

            floor = frac * base
            relax = max(0.0, 1.0 - max(0, shed_load - 40) / 50.0)
            qty = units_sellable_above(item, inv.get(item, I0), floor * relax, n)

        if qty > 0:
            market_orders.append(["SELL", item, qty])

    # --- 4. High-Fleet Labor Scaling (v5 Upgrade: Up to 15-20 Hands) ---
    if hour == 0 and day < 29:
        work = len(view["water"]) + len(view["urgent_water"]) + len(view["harvest"]) + len(view["empty"])
        target = max(6, min(18, work // 4))  # Scale fleet to 4-quadrant task workload
        current_hands = len(me["hands"])
        for _ in range(target - current_hands):
            if len(market_orders) < 10:
                market_orders.append(["HIRE"])

    # --- 5. Seed Pipeline & Capital Management ---
    ph = phase(day)
    space = len(view["empty"]) + 2
    want = {}
    if day <= CUTOFF["MELON"] and money > 700:
        want["MELON"] = min(space, 6 if ph == 0 else 10)
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
        want["WHEAT"] = 4

    budget = money - (500 if ph == 0 else 200)
    for crop, tgt in want.items():
        have = seeds.get(crop, 0)
        if have < tgt:
            k = tgt - have
            cost = CROPS[crop]["seed"] * k
            if budget >= cost and len(market_orders) < 10:
                market_orders.append(["BUY_SEED", crop, k])
                budget -= cost

    return market_orders[:10]


# =====================================================================
# LAYER 4: TASK ALLOCATION & SPATIAL ZERO-PASS MICRO
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


TASK_ORDER = ["urgent_water", "harvest", "water", "plant", "weeds"]
TASK_ACTION = {
    "urgent_water": ["WATER"],
    "harvest": ["HARVEST"],
    "water": ["WATER"],
    "weeds": ["DIG"]
}


def unit_action(pos, tasks, seeds, day):
    x, y = pos

    # Execute action if standing on task tile
    for key in TASK_ORDER:
        if (x, y) in tasks[key]:
            tasks[key].remove((x, y))
            if key == "plant":
                for crop in plantable_crops(seeds, day):
                    seeds[crop] -= 1
                    tasks["urgent_water"].append((x, y))  # Same-day water invariant
                    return ["PLANT", crop]
                continue
            return TASK_ACTION[key]

    # Move toward nearest active task
    for key in TASK_ORDER:
        tgt = _nearest((x, y), tasks[key])
        if tgt:
            step = _step_toward((x, y), tgt)
            if step:
                tasks[key].remove(tgt)  # Reserve waypoint
                return [step]

    # v5 Zero-PASS Micro: Step toward shed (0,0) or center when idle
    fallback_step = _step_toward((x, y), (0, 0))
    if fallback_step:
        return [fallback_step]

    return ["PASS"]


# =====================================================================
# LAYERS 5 & 6: MONOLITH AGENT ENTRY & CRASH GUARD
# =====================================================================

# Global Persistent Instance across turns
timing_engine = DemandTimingEngine(match_seed=42)


def _agent(obs):
    p = obs["player"]
    me, opp = obs["farms"][p], obs["farms"][1 - p]
    day, hour = obs["day"], obs["hour"]
    seeds = dict(obs["private"]["seeds"])

    # 1. Perception
    view = perceive(me, opp, day)

    # 2. Economy & Market Orders
    market = economy(obs, me, opp, view, seeds, day, hour, timing_engine)

    # 3. Task Allocation Setup
    crops_now = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(c, 0) for c in crops_now)
    tasks = {
        "urgent_water": view["urgent_water"],
        "harvest": view["harvest"],
        "water": view["water"],
        "plant": (view["empty"][:n_plantable] if crops_now and hour < 21 else []),
        "weeds": view["weeds"] if day <= 27 else [],
    }

    # 4. Unit Actions
    farmer_op = unit_action(me["farmer"], tasks, seeds, day)
    hand_ops = [unit_action(h, tasks, seeds, day) for h in me["hands"]]

    return {"farmer": farmer_op, "hands": hand_ops, "market": market}


def agent(obs, configuration=None):
    """Kaggle submission entry point with top-level crash guard."""
    try:
        return _agent(obs)
    except Exception as e:
        import sys, traceback
        print(f"GUARD swallowed exception: {e!r}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"farmer": ["PASS"], "hands": [], "market": []}