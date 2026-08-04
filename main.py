# Kaggriculture v1: heuristic planner
# Strategy: hire cheap hands, run a wheat+tomato economy, water religiously,
# harvest when ready, sell every turn, stop planting near season end.

WHEAT_CUTOFF_DAY = 25   # wheat needs ~4 days
TOMATO_CUTOFF_DAY = 19  # tomato needs 8 days to first yield
HANDS_PER_DAY = 4

def _tiles_of_interest(me, day):
    water, harvest, empty = [], [], []
    for y, row in enumerate(me["tiles"]):
        for x, t in enumerate(row):
            if t is None:
                empty.append((x, y))
            elif isinstance(t, dict) and t.get("kind") == "PLANT":
                if not t["watered_today"]:
                    water.append((x, y))
                age = day - t["planted_day"]
                crop = t["crop"]
                ready = (crop == "TOMATO" and t["yield_units"] > 0) or \
                        (crop == "WHEAT" and age >= 4 and t["yield_units"] > 0)
                if ready:
                    harvest.append((x, y))
    return water, harvest, empty

def _step_toward(pos, target):
    x, y = pos; tx, ty = target
    if x < tx: return "EAST"
    if x > tx: return "WEST"
    if y < ty: return "SOUTH"
    if y > ty: return "NORTH"
    return None

def _nearest(pos, targets):
    if not targets: return None
    return min(targets, key=lambda t: abs(t[0]-pos[0]) + abs(t[1]-pos[1]))

def _unit_action(pos, tasks, seeds, day):
    """tasks = dict of lists; mutates lists so units don't double-book."""
    x, y = pos
    # already standing on a task tile?
    if (x, y) in tasks["harvest"]:
        tasks["harvest"].remove((x, y)); return ["HARVEST"]
    if (x, y) in tasks["water"]:
        tasks["water"].remove((x, y)); return ["WATER"]
    if (x, y) in tasks["plant"]:
        tasks["plant"].remove((x, y))
        if seeds.get("TOMATO", 0) > 0 and day <= TOMATO_CUTOFF_DAY:
            seeds["TOMATO"] -= 1; return ["PLANT", "TOMATO"]
        if seeds.get("WHEAT", 0) > 0 and day <= WHEAT_CUTOFF_DAY:
            seeds["WHEAT"] -= 1; return ["PLANT", "WHEAT"]
    # otherwise walk to nearest task (priority: harvest > water > plant)
    for key in ("harvest", "water", "plant"):
        tgt = _nearest((x, y), tasks[key])
        if tgt:
            step = _step_toward((x, y), tgt)
            if step:
                # reserve the tile so others pick different work
                tasks[key].remove(tgt)
                return [step]
    return ["PASS"]

def agent(obs):
    p = obs["player"]
    me = obs["farms"][p]
    priv = obs["private"]
    day, hour = obs["day"], obs["hour"]
    money = me["money"]
    seeds = dict(priv["seeds"])

    water, harvest, empty = _tiles_of_interest(me, day)

    market = []

    # --- sell everything in the shed, every turn ---
    for item, n in priv["shed"].items():
        if n > 0 and item not in ("FERTILIZER",):
            market.append(["SELL", item, n])

    # --- hire hands at the start of each day (cost: 1,1,2,3 = $7 total) ---
    if hour == 0:
        for _ in range(HANDS_PER_DAY):
            market.append(["HIRE"])

    # --- keep a seed pipeline stocked ---
    plantable = len(empty)
    want_tomato = day <= TOMATO_CUTOFF_DAY and plantable > 0
    want_wheat = day <= WHEAT_CUTOFF_DAY and plantable > 0
    if want_tomato and seeds.get("TOMATO", 0) < 3 and money > 400:
        market.append(["BUY_SEED", "TOMATO", 2])
    if want_wheat and seeds.get("WHEAT", 0) < 4 and money > 100:
        market.append(["BUY_SEED", "WHEAT", 3])

    # --- expand land once cash-rich ---
    if len(me["unlocked_quadrants"]) == 1 and money > 2500 and day >= 3 and day <= 20:
        market.append(["BUY_LAND"])

    market = market[:10]

    # --- allocate unit actions ---
    total_seeds = sum(seeds.values())
    plant_targets = empty[:total_seeds] if (want_tomato or want_wheat) else []
    tasks = {"water": water, "harvest": harvest, "plant": list(plant_targets)}

    farmer_op = _unit_action(me["farmer"], tasks, seeds, day)
    hand_ops = [_unit_action(h, tasks, seeds, day) for h in me["hands"]]

    return {"farmer": farmer_op, "hands": hand_ops, "market": market}
