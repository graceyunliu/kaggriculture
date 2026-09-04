# economy block variant: scheduled frontier opening (days 0..SCHED_LAST_DAY), then the stock economy.
# Derived from Yuan800's ladder episode 104892947 days 0-11 (evolve/README.md "scheduled opening"):
#   4-5 hands on $30-250 of cash, hires first, feed bought just-in-time in small chunks funded by intraday
#   fertilizer/wool/milk sales, cows bought in the afternoon from the day's proceeds, 3-5 wheat tiles planted
#   every day from day 2, strawberries from day 4, melons held until day 10.
# The decisions are a policy over targets (not recorded actions); the executor is the chassis's own.

SCHED = {
    "last_day": 11,
    "hands": {0: 5, 1: 4, 2: 4, 3: 5, 4: 4, 5: 5, 6: 8, 7: 8, 8: 10, 9: 11, 10: 11, 11: 11},
    "animals": [(2, "COW", 1), (3, "COW", 1), (6, "COW", 2), (8, "COW", 1), (8, "SHEEP", 2)],   # after the day-0 opening
    "wheat_seeds": {2: 3, 3: 4, 4: 3, 6: 5, 7: 4, 8: 3, 9: 4, 10: 5, 11: 14},
    "straw_seeds": {4: 4, 5: 4, 6: 6, 7: 4, 8: 4, 11: 17},
    "land": {6: 1, 11: 1},    # quadrant purchases: day -> count (tape: BUY_LAND day 6 h6, day 11 h1)
    "feed_chunk": 4,          # units of wheat bought per hour when animals are unfed and cash allows
    "feed_buffer": 1,         # wheat units kept beyond today's unfed animals
    "melon_hold_day": 10,     # do not sell melons before this day unless price is very high
    "melon_price_hi": 230,
    "wheat_sell_price": 40,   # sell surplus wheat above feed need at/above this price
    "seed_hours": (0, 1, 2),  # seeds are bought in the morning
}


def _sched_state():
    st = S.get("sched")
    if st is None:
        st = {"bought": {}, "seeds": {}}   # bought: (day,sp,idx)->True ; seeds: day -> {crop: n}
        S["sched"] = st
    return st


def _schedule_economy(obs, v):
    """Orders for days 0..last_day under the scheduled opening. Returns a list (possibly empty)."""
    p = obs["player"]
    me = obs["farms"][p]
    day, hour = obs["day"], obs["hour"]
    shed = obs["private"]["shed"]
    seeds = obs["private"]["seeds"]
    prices = obs["market"]["prices"]
    cash = float(me["money"])
    inv = obs["private"].get("inventories") or []
    n_hands = len(me["hands"])
    st = _sched_state()
    orders = []

    # ---- day 0, hour 0: the frontier opening (all cash)
    n_active = len(v["animals"])
    carried_animals = sum(i.get(a, 0) for i in inv for a in ANIMALS)
    shed_animals = sum(shed.get(a, 0) for a in ANIMALS)
    n_total = n_active + shed_animals + carried_animals
    if day == 0 and hour == 0 and n_total == 0:
        S["hires_target"] = SCHED["hands"][0]
        oc, osh, om, ow = KNOBS["open_cows"], KNOBS["open_sheep"], KNOBS["open_melons"], KNOBS["open_wheat"]
        o = [["HIRE"]] * SCHED["hands"][0]
        if oc: o.append(["BUY_ANIMAL", "COW", oc])
        if osh: o.append(["BUY_ANIMAL", "SHEEP", osh])
        if om: o.append(["BUY_SEED", "MELON", om])
        if ow: o.append(["BUY_SEED", "WHEAT", ow])
        o.append(["BUY_PRODUCT", "WHEAT", min(5, oc + osh + 1)])
        return o[:MAX_ORDERS]

    # ---- sells: every hour, everything except melons (held) and feed wheat
    revenue = 0.0
    for item in ("FERTILIZER", "MILK", "WOOL", "EGG", "STRAWBERRY", "CARROT", "TOMATO"):
        n = int(shed.get(item, 0))
        if n > 0:
            orders.append(["SELL", item, n])
            revenue += n * prices.get(item, 0) * 0.85
    m = int(shed.get("MELON", 0))
    if m > 0 and (day >= SCHED["melon_hold_day"] or prices.get("MELON", 0) >= SCHED["melon_price_hi"]):
        orders.append(["SELL", "MELON", m])
        revenue += m * prices.get("MELON", 0) * 0.7
    unfed = sum(1 for _pos, t in v["animals"] if not t.get("fed_today"))
    wheat_have = int(shed.get("WHEAT", 0)) + sum(int(i.get("WHEAT", 0)) for i in inv)
    surplus = wheat_have - (unfed + shed_animals + carried_animals + SCHED["feed_buffer"])
    if surplus > 0 and prices.get("WHEAT", 0) >= SCHED["wheat_sell_price"] and hour <= 4:
        orders.append(["SELL", "WHEAT", int(surplus)])
        revenue += surplus * prices.get("WHEAT", 0) * 0.9
    budget = cash + revenue

    # ---- hires: hours 0-1, toward the day's target, hires before feed (fib costs are tiny early)
    target = SCHED["hands"].get(day, SCHED["hands"][SCHED["last_day"]])
    S["hires_target"] = target
    if hour <= 1 and n_hands < target:
        n, spent = _hire_plan(target, n_hands, me["hires_today"], max(0.0, budget))
        n = max(0, min(n, MAX_ORDERS - len(orders)))
        orders += [["HIRE"]] * n
        budget -= spent if n > 0 else 0

    # ---- feed just-in-time: keep unfed animals covered, small chunks, funded by the sales above
    wp = prices.get("WHEAT", 40) * 1.1
    need = (unfed + shed_animals + carried_animals + SCHED["feed_buffer"]) - wheat_have
    if need > 0 and len(orders) < MAX_ORDERS:
        k = min(need, SCHED["feed_chunk"], int(budget // wp))
        if k > 0:
            orders.append(["BUY_PRODUCT", "WHEAT", int(k)])
            budget -= k * wp

    # ---- animals: the plan, bought one unit at a time whenever the day's proceeds cover it (any hour >= 1)
    if hour >= 1 and len(orders) < MAX_ORDERS:
        for idx, (d, sp, cnt) in enumerate(SCHED["animals"]):
            if d > day:
                continue
            for j in range(cnt):
                key = (idx, j)
                if st["bought"].get(key):
                    continue
                cost = ANIMALS[sp]
                if budget >= cost + wp:            # keep one unit of feed money
                    orders.append(["BUY_ANIMAL", sp, 1])
                    budget -= cost
                    st["bought"][key] = True
                    break                          # one animal per hour keeps cash for feed
            else:
                continue
            break

    # ---- land: scheduled quadrant purchases, as soon as the day's proceeds cover the price (carried over if not)
    quads = len(me["unlocked_quadrants"])
    land_due = sum(c for d, c in SCHED["land"].items() if d <= day)
    if quads < 4 and (quads - 1) < land_due and hour >= 1 and len(orders) < MAX_ORDERS:
        price = LAND_PRICES[quads - 1]
        if budget >= price + wp:
            orders.append(["BUY_LAND"])
            budget -= price

    # ---- seeds: daily quota in the morning, after hires/feed
    if hour in SCHED["seed_hours"] and len(orders) < MAX_ORDERS:
        got = st["seeds"].setdefault(day, {})
        for crop, table in (("WHEAT", SCHED["wheat_seeds"]), ("STRAWBERRY", SCHED["straw_seeds"])):
            want = table.get(day, 0) - got.get(crop, 0)
            price = CROP_SPECS[crop]["seed"]
            k = min(want, int(budget // price))
            if k > 0 and len(orders) < MAX_ORDERS:
                orders.append(["BUY_SEED", crop, int(k)])
                budget -= k * price
                got[crop] = got.get(crop, 0) + k
    return orders[:MAX_ORDERS]


def economy(obs, v):
    if KNOBS.get("opening") == "schedule" and obs["day"] <= SCHED["last_day"]:
        return _schedule_economy(obs, v)
    return _economy_base(obs, v)


def _economy_base(obs, v):
    p = obs["player"]
    me = obs["farms"][p]
    day, hour = obs["day"], obs["hour"]
    shed = obs["private"]["shed"]
    seeds = obs["private"]["seeds"]
    prices = obs["market"]["prices"]
    cash = me["money"]
    quads = len(me["unlocked_quadrants"])
    orders = []
    n_hands = len(me["hands"])
    inv = obs["private"].get("inventories") or []
    carried_animals = sum(i.get(a, 0) for i in inv for a in ANIMALS)
    shed_animals = sum(shed.get(a, 0) for a in ANIMALS)
    n_active = len(v["animals"])
    n_total = n_active + shed_animals + carried_animals
