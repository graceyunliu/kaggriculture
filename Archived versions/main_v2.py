# Kaggriculture v2: world-model-backed heuristic planner
# Design doc: kaggriculture-agent-design.md (D1-D22)
# Layers: world model -> perception -> economy (phase FSM, paced selling,
# standing evaluator) -> allocation -> guards -> assembly.

import math

# ---------------- Layer 1: world model (copied from engine source) ----------

PRICE_FLOOR = 1
I0 = 10_000

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


def _shape(func, x):
    x = max(0.0, x)
    if func == "linear": return x
    if func == "sq":     return x * x
    if func == "sqrt":   return math.sqrt(x)
    if func == "log":    return math.log(1.0 + x)
    if func == "log10":  return math.log10(1.0 + x)
    return x


def market_price(item, inventory):
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
    """Max units to sell now so the marginal price stays >= min_price.
    Sell price is quoted at pre-sell inventory per unit."""
    n = 0
    while n < cap and market_price(item, inventory + n) >= min_price:
        n += 1
    return n


# ---------------- Config: cutoffs & portfolio (engine-derived, D22) ---------

CUTOFF = {"WHEAT": 25, "CARROT": 26, "MELON": 16}  # last plant day to mature by 29
PLANT_PRIORITY = ["MELON", "CARROT", "WHEAT"]      # what to plant when a tile is free
PREMIUM = {"STRAWBERRY", "MELON", "MILK", "WOOL"}
SHED_CAP = 100
LIQUIDATE_DAY = 28


# ---------------- Layer 2: perception -------------------------------------


def perceive(me, opp, day):
    """Bucket own tiles into urgency-tiered task lists; build opponent glut view."""
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
                c = CROPS[t["crop"]]
                age = day - t["planted_day"]
                if t["yield_units"] > 0 and (c["ongoing"] or age >= c["max_day"]):
                    harvest.append((x, y))
    # Opponent glut forecast: crops maturing within 2 days (public tiles, D14)
    imminent = {}
    for row in opp["tiles"]:
        for t in row:
            if isinstance(t, dict) and t.get("kind") == "PLANT":
                c = CROPS[t["crop"]]
                age = day - t["planted_day"]
                if c["first"] - 2 <= age <= c["max_day"]:
                    imminent[t["crop"]] = imminent.get(t["crop"], 0) + 1
    return {"urgent_water": urgent_water, "water": water, "harvest": harvest,
            "empty": empty, "weeds": weeds, "opp_imminent": imminent}


# ---------------- Layer 3: economy policy ----------------------------------


def phase(day):
    return 0 if day < 10 else (1 if day < 20 else 2)


def plantable_crops(seeds, day):
    """D17: per-crop plantability decided here, once, before targets exist."""
    return [c for c in PLANT_PRIORITY
            if seeds.get(c, 0) > 0 and day <= CUTOFF.get(c, -1)]


def sell_threshold(item, day, opp_imminent, behind):
    """Fraction of base price below which we stop selling this turn."""
    if day >= LIQUIDATE_DAY:
        return 0.0                       # endgame: cash out everything
    frac = 0.85 if item in PREMIUM else 0.70
    if item in opp_imminent and opp_imminent[item] >= 4:
        frac -= 0.25                     # front-run their glut (D14)
    if behind and item in PREMIUM and day >= 20:
        frac += 0.10                     # behind: hold premium for spikes (D3)
    return frac


def economy(obs, me, opp, view, seeds, day, hour):
    market_orders = []
    money = me["money"]
    shed = obs["private"]["shed"]
    inv = obs["market"]["inventory"]
    behind = money < opp["money"] - 500

    # --- selling: price-threshold paced (D13, D20) ---
    shed_load = sum(n for k, n in shed.items() if n > 0)
    force_dump = shed_load > SHED_CAP - 15 and hour >= 18   # shed guard (D10)
    sellable = [(i, n) for i, n in shed.items()
                if n > 0 and i in MARKET_PARAMS and i != "FERTILIZER"]
    for item, n in sorted(sellable, key=lambda kv: -market_price(kv[0], inv.get(kv[0], I0))):
        if force_dump or day >= LIQUIDATE_DAY:
            qty = n
        else:
            floor = sell_threshold(item, day, view["opp_imminent"], behind) * MARKET_PARAMS[item]["base"]
            qty = units_sellable_above(item, inv.get(item, I0), floor, n)
        if qty > 0:
            market_orders.append(["SELL", item, qty])

    # --- hiring: scale to available work (fib costs are cheap) ---
    if hour == 0 and day < 29:
        work = len(view["water"]) + len(view["urgent_water"]) + len(view["harvest"]) + len(view["empty"])
        target = max(3, min(6, work // 6))
        for _ in range(target):
            market_orders.append(["HIRE"])

    # --- seed pipeline by phase FSM (D19, D22 portfolio) ---
    ph = phase(day)
    want = {}
    if day <= CUTOFF["MELON"] and money > 700:
        want["MELON"] = 4 if ph == 0 else 6
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 3
    if day <= CUTOFF["WHEAT"]:
        want["WHEAT"] = 3
    budget = money - (900 if ph == 0 else 300)   # keep working capital
    for crop, tgt in want.items():
        have = seeds.get(crop, 0)
        if have < tgt:
            k = tgt - have
            cost = CROPS[crop]["seed"] * k
            if budget >= cost:
                market_orders.append(["BUY_SEED", crop, k])
                budget -= cost

    # --- land expansion: buy quadrant 2 early, 3 when rich ---
    quads = len(me["unlocked_quadrants"])
    if 2 <= day <= 20:
        if quads == 1 and money > 2200:
            market_orders.append(["BUY_LAND"])
        elif quads == 2 and money > 5500 and day <= 16:
            market_orders.append(["BUY_LAND"])

    return market_orders[:10]


# ---------------- Layer 4: allocation --------------------------------------


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
TASK_ACTION = {"urgent_water": ["WATER"], "harvest": ["HARVEST"],
               "water": ["WATER"], "weeds": ["DIG"]}


def unit_action(pos, tasks, seeds, day):
    x, y = pos
    for key in TASK_ORDER:
        if (x, y) in tasks[key]:
            tasks[key].remove((x, y))
            if key == "plant":
                for crop in plantable_crops(seeds, day):
                    seeds[crop] -= 1
                    return ["PLANT", crop]
                continue   # not plantable after all; try other on-tile tasks
            return TASK_ACTION[key]
    for key in TASK_ORDER:
        tgt = _nearest((x, y), tasks[key])
        if tgt:
            step = _step_toward((x, y), tgt)
            if step:
                tasks[key].remove(tgt)   # reserve so units spread out
                return [step]
    return ["PASS"]


# ---------------- Layers 5+6: guards & assembly ----------------------------


def _agent(obs):
    p = obs["player"]
    me, opp = obs["farms"][p], obs["farms"][1 - p]
    day, hour = obs["day"], obs["hour"]
    seeds = dict(obs["private"]["seeds"])

    view = perceive(me, opp, day)
    market = economy(obs, me, opp, view, seeds, day, hour)

    crops_now = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(c, 0) for c in crops_now)
    tasks = {
        "urgent_water": view["urgent_water"],
        "harvest": view["harvest"],
        "water": view["water"],
        "plant": view["empty"][:n_plantable] if crops_now else [],   # D17
        "weeds": view["weeds"] if day <= 27 else [],
    }

    farmer_op = unit_action(me["farmer"], tasks, seeds, day)
    hand_ops = [unit_action(h, tasks, seeds, day) for h in me["hands"]]
    return {"farmer": farmer_op, "hands": hand_ops, "market": market}


def agent(obs):
    try:
        return _agent(obs)
    except Exception:
        return {"farmer": ["PASS"], "hands": [], "market": []}   # never crash (D-principle 3)
