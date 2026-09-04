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

    # ---- sells (every hour on days >= 28, otherwise hour 0)
    shed_load = sum(n for k, n in shed.items() if k not in ANIMALS and n > 0)
    revenue_est = 0.0
    fert_want = 0
    if day <= 26 and (KNOBS["fert_keep"] > 0 or KNOBS["fert_buy"] > 0):
        fert_want = min(KNOBS["fert_keep"] + KNOBS["fert_buy"], len(v["fert"]))
    if hour == 0 or day >= 28 or KNOBS["sell_hourly"]:
        for item in ("MILK", "WOOL", "STRAWBERRY", "FERTILIZER", "TOMATO", "CARROT", "EGG"):
            n = shed.get(item, 0)
            if item == "FERTILIZER" and day <= 26:
                n = max(0, n - min(KNOBS["fert_keep"], fert_want))
            if n > 0:
                orders.append(["SELL", item, int(n)])
                revenue_est += n * prices.get(item, 0) * 0.85
        n = shed.get("MELON", 0)
        if n > 0 and (prices.get("MELON", 0) >= KNOBS["melon_floor"] or day >= 27 or shed_load > 75):
            orders.append(["SELL", "MELON", int(n)])
            revenue_est += n * prices.get("MELON", 0) * 0.7
        w = shed.get("WHEAT", 0)
        if day >= 29:
            if w > 0:
                orders.append(["SELL", "WHEAT", int(w)])
        elif prices.get("WHEAT", 0) >= (KNOBS["wheat_sell_price"] if day < 27 else 30):
            hold = KNOBS["wheat_stock"] if day < 27 else 0
            reserve_feed = (n_total + 3) + (n_total * KNOBS["wheat_hold_days"] if day < 27 else 0)
            surplus = int(w - reserve_feed - hold)
            if shed_load > 80:
                surplus = int(w - (n_total + 3))
            if surplus > 0:
                orders.append(["SELL", "WHEAT", surplus])
                revenue_est += surplus * prices.get("WHEAT", 0) * 0.9
    capital_hour = 0 if day == 0 else 1          # V3.10: capital decisions on exact post-sale cash at hour 1
    if hour != capital_hour and not (KNOBS["capital_hour2"] >= 0 and hour == KNOBS["capital_hour2"] and day >= 1):
        if hour == 0:
            spare = 3 if cash + revenue_est >= 300 else KNOBS["feed_spare_poor"]
            feed_need = max(0, n_total + spare - shed.get("WHEAT", 0)) if day < 29 else 0
            wheat_cost = feed_need * prices.get("WHEAT", 40) * 1.15
            seeds_on_hand = sum(seeds.get(c, 0) for c in CROP_SPECS)
            target = _load_model(v, seeds_on_hand, n_total, shed_animals + carried_animals, day)
            S["hires_target"] = target
            if day <= KNOBS["early_hire_days"]:
                # labor first: hires cost fib dollars; feed is bought with whatever is left
                n, spent = _hire_plan(target, n_hands, me["hires_today"], max(0.0, cash + revenue_est))
                orders += [["HIRE"]] * max(0, min(n, MAX_ORDERS - len(orders)))
                affordable = int(max(0.0, cash + revenue_est - spent) // (prices.get("WHEAT", 40) * 1.15))
                feed_need = min(feed_need, affordable)
                if feed_need > 0:
                    orders.append(["BUY_PRODUCT", "WHEAT", int(feed_need)])
            else:
                if feed_need > 0:
                    orders.append(["BUY_PRODUCT", "WHEAT", int(feed_need)])
                n, _ = _hire_plan(target, n_hands, me["hires_today"], max(0.0, cash + revenue_est - wheat_cost - 50))
                orders += [["HIRE"]] * max(0, min(n, MAX_ORDERS - len(orders)))
        elif hour <= 2 and day < 30:
            need = S["hires_target"] - n_hands
            if need > 0:
                n, _ = _hire_plan(S["hires_target"], n_hands, me["hires_today"], max(0.0, cash - 50))
                orders += [["HIRE"]] * min(n, MAX_ORDERS - len(orders))
        return orders[:MAX_ORDERS]

    # ---- frontier opening: the whole $3,000 at hour 0 of day 0 (exactly 10 orders)
    if day == 0 and KNOBS["opening"] == "frontier" and n_total == 0:
        S["hires_target"] = 5
        oc, osh, om, ow = KNOBS["open_cows"], KNOBS["open_sheep"], KNOBS["open_melons"], KNOBS["open_wheat"]
        o = [["HIRE"]] * 5
        if oc: o.append(["BUY_ANIMAL", "COW", oc])
        if osh: o.append(["BUY_ANIMAL", "SHEEP", osh])
        if om: o.append(["BUY_SEED", "MELON", om])
        if ow: o.append(["BUY_SEED", "WHEAT", ow])
        o.append(["BUY_PRODUCT", "WHEAT", min(5, oc + osh + 1)])
        return o[:MAX_ORDERS]

    budget = cash + revenue_est
    wheat_price = prices.get("WHEAT", 40)
    feed_need = 0
    if day < 29:
        feed_need = max(0, n_total + 3 - shed.get("WHEAT", 0))
    wheat_cost = feed_need * wheat_price * 1.15
    seeds_on_hand = sum(seeds.get(c, 0) for c in CROP_SPECS)
    target = _load_model(v, seeds_on_hand, n_total, shed_animals + carried_animals, day)
    _, labor_cost_today = _hire_plan(target, n_hands, me["hires_today"], 10 ** 9)
    reserve = wheat_cost + labor_cost_today + 100
    free = budget - reserve

    empty_count = len(v["empty"]) + len(v["empty_pastures"])
    land_wanted = 0

    # ---- herd
    pending_place = shed_animals + carried_animals
    if day == 0 and n_total == 0:
        orders.append(["BUY_ANIMAL", "COW", 1])
        orders.append(["BUY_ANIMAL", "SHEEP", 1])
        free -= 900
        pending_place = 2
        n_total = 2
    elif 1 <= day <= 21 and pending_place <= 3 and n_total < KNOBS["max_animals"]:
        opp = obs["farms"][1 - p]
        opp_counts = {"COW": 0, "SHEEP": 0}
        for row in opp["tiles"]:
            for t in row:
                if isinstance(t, dict) and t.get("animal") in opp_counts:
                    opp_counts[t["animal"]] += 1
        my_counts = {"COW": shed.get("COW", 0), "SHEEP": shed.get("SHEEP", 0), "GOOSE": shed.get("GOOSE", 0)}
        for _pos, t in v["animals"]:
            if t.get("animal") in my_counts:
                my_counts[t["animal"]] += 1
        for i_ in inv:
            for sp in my_counts:
                my_counts[sp] += i_.get(sp, 0)
        _, labor_tomorrow = _hire_plan(target, 0, 0, 10 ** 9)
        income_tomorrow = n_active * prices.get("FERTILIZER", 50) * 0.8
        for i_ in inv:
            for k_, n_ in i_.items():
                if k_ in ("MILK", "WOOL", "STRAWBERRY", "MELON", "EGG", "FERTILIZER"):
                    income_tomorrow += n_ * prices.get(k_, 0) * 0.8
        if KNOBS["geese"] > 0 and day <= 3 and my_counts["GOOSE"] < KNOBS["geese"]:
            k = min(KNOBS["geese"] - my_counts["GOOSE"], int(free // ANIMALS["GOOSE"]))
            if k > 0:
                orders.append(["BUY_ANIMAL", "GOOSE", int(k)])
                free -= ANIMALS["GOOSE"] * k
                n_total += k
                pending_place += k
        for sp in ("SHEEP", "COW"):
            if day > HERD_LAST_DAY and sp == "COW":
                continue
            room = _demand_room(obs, v, sp, day, my_counts[sp], opp_counts[sp])
            if sp == "SHEEP":
                yarn = _instances(obs, "WOOL")
                if yarn == 0:
                    room = min(room, 2 - my_counts[sp])
                elif prices.get("WOOL", 0) >= 1.05 * 200 and day >= 8:
                    room = max(room, 2)
                room = min(room, MAX_SHEEP - my_counts[sp])
            else:
                if _instances(obs, "MILK") == 0 and day >= 9:
                    room = min(room, 4 - my_counts[sp])
            k = min(6, room, KNOBS["max_animals"] - n_total, int(free // ANIMALS[sp]), empty_count - 4)
            while k > 0 and _load_model(v, seeds_on_hand, n_total + k, pending_place + k, day) > MAX_HANDS:
                k -= 1
            while k > 0:
                cash_after = free - ANIMALS[sp] * k + reserve - wheat_cost - labor_cost_today
                need_tomorrow = labor_tomorrow + (n_total + k) * wheat_price - income_tomorrow
                if cash_after >= need_tomorrow:
                    break
                k -= 1
            if k > 0:
                orders.append(["BUY_ANIMAL", sp, int(k)])
                free -= ANIMALS[sp] * k
                n_total += k
                pending_place += k
                my_counts[sp] += k

    # ---- seeds
    if day == 0:
        orders.append(["BUY_SEED", "MELON", OPENING_MELONS])
        free -= 80 * OPENING_MELONS
    else:
        opp = obs["farms"][1 - p]
        committed = {c: 0.0 for c in CROP_SPECS}
        wheat_tiles_now = 0
        for _pos, t in v["crops"]:
            c = t.get("crop")
            if c in committed:
                committed[c] += CROP_SPECS[c]["units"]
            if c == "WHEAT":
                wheat_tiles_now += 1
        for c in committed:
            committed[c] += seeds.get(c, 0) * CROP_SPECS[c]["units"]
        space = empty_count - pending_place - sum(seeds.get(c, 0) for c in CROP_SPECS)
        seed_orders = {}
        n_seed_orders = 0
        excluded = set()
        # ---- wheat tile floor (feed self-supply + late sale)
        wheat_target = max(KNOBS["wheat_tiles"], int(round(KNOBS["wheat_per_animal"] * n_total)))
        wheat_target = min(wheat_target, KNOBS["wheat_cap"])
        if wheat_target > 0 and day <= 24:
            deficit = wheat_target - wheat_tiles_now - seeds.get("WHEAT", 0)
            k = min(deficit, space, int(free // 10))
            if k > 0:
                seed_orders["WHEAT"] = k
                free -= 10 * k
                seeds_on_hand += k
                space -= k
                committed["WHEAT"] += k * CROP_SPECS["WHEAT"]["units"]
                n_seed_orders += 1
                excluded.add("WHEAT")
        while space > 0 and n_seed_orders < 4:
            best = None
            for c, sp_ in CROP_SPECS.items():
                if c in excluded or day > sp_["cutoff"] or day < sp_.get("start", 0):
                    continue
                if c == "STRAWBERRY" and day < KNOBS["straw_delay"]:
                    continue
                T_sell = max(0, 29 - day - sp_["first"])
                if T_sell <= 0:
                    continue
                inv_c = obs["market"]["inventory"].get(c, I0)
                cushion_left = max(0.0, sp_.get("cushion", 0) - max(0.0, inv_c - I0))
                pool = DEMAND_SHARE * (max(0.0, I0 - inv_c) + cushion_left + _daily_demand(obs, c, day, day + sp_["first"]) * (29 - day))
                room_units = pool - committed[c] - seed_orders.get(c, 0) * sp_["units"]
                if room_units < sp_["units"] * 0.5:
                    continue
                price = min(prices.get(c, sp_["base"]), sp_["base"] * 2.0)
                val = min(sp_["units"], room_units) * price / sp_["cycle"]
                if val < sp_["min_val"]:
                    continue
                if best is None or val > best[0]:
                    best = (val, c, room_units)
            if best is None:
                break
            _val, c, room_units = best
            k = min(space, int(room_units // CROP_SPECS[c]["units"]), int(free // CROP_SPECS[c]["seed"]), 20)
            while k > 0 and _load_model(v, seeds_on_hand + k, n_total, pending_place, day) >= MAX_HANDS:
                k -= 1
            if k <= 0:
                excluded.add(c)
                continue
            excluded.add(c)
            seed_orders[c] = seed_orders.get(c, 0) + k
            free -= CROP_SPECS[c]["seed"] * k
            seeds_on_hand += k
            space -= k
            n_seed_orders += 1
            if c == "STRAWBERRY" and room_units // CROP_SPECS[c]["units"] > k + 4:
                land_wanted = int(room_units // CROP_SPECS[c]["units"]) - k
        for c, k in seed_orders.items():
            orders.append(["BUY_SEED", c, int(k)])

    # ---- land
    if quads < 4 and 1 <= day <= LAND_DEADLINE[quads + 1] and empty_count - pending_place < 8 and (land_wanted > 0 or pending_place > empty_count - 2):
        price = LAND_PRICES[quads - 1]
        if quads == 3 and not (day <= 14 and land_wanted >= 12):
            price = float("inf")
        if free >= price:
            orders.append(["BUY_LAND"])
            free -= price

    # ---- wheat feed
    if day < 29:
        feed_need = max(0, n_total + 3 - shed.get("WHEAT", 0) - sum(int(o[2]) for o in orders if o[0] == "BUY_PRODUCT"))
    if feed_need > 0:
        orders.append(["BUY_PRODUCT", "WHEAT", int(feed_need)])

    # ---- fertilizer to apply on ongoing crops (3-day boost doubles the next yields)
    if KNOBS["fert_buy"] > 0 and day <= 26 and len(v["fert"]) > 0:
        fp = prices.get("FERTILIZER", 100)
        eligible = len(v["fert"])
        have = shed.get("FERTILIZER", 0)
        k = min(KNOBS["fert_buy"], max(0, eligible - have), int(max(0.0, free - 50) // max(1, fp)))
        if k > 0 and fp <= 0.6 * prices.get("STRAWBERRY", 120):
            orders.append(["BUY_PRODUCT", "FERTILIZER", int(k)])
            free -= fp * k

    # ---- hires
    target = _load_model(v, seeds_on_hand, n_total, pending_place, day)
    S["hires_target"] = target
    n, _ = _hire_plan(target, n_hands, me["hires_today"], max(0.0, cash + revenue_est - wheat_cost))
    slots = MAX_ORDERS - len(orders)
    orders += [["HIRE"]] * max(0, min(n, slots))
    return orders[:MAX_ORDERS]
