def _unit_action(i, pos, carry, obs, v, pools, seeds_left, shed, unlocked_shed):
    day, hour = obs["day"], obs["hour"]
    if any(carry.get(a, 0) > 0 for a in ANIMALS):
        op = _setup_step(i, pos, v, carry)
        if op is not None:
            return op
    prod_carried = sum(carry.get(k, 0) for k in PRODUCTS if k != "WHEAT")
    if day >= 28 and prod_carried >= (3 if day == 29 else 6) and i not in S["routes"]:
        if pos in unlocked_shed:
            return ["DROP"]
        if day == 29 and hour >= 20:
            return [_step(pos, _nearest(pos, unlocked_shed))]
        if day == 29 or hour >= 18:
            return [_step(pos, _nearest(pos, unlocked_shed))]
    # 2a. melon rush: carried melons go straight to the shed to sell into the day-10 price
    if KNOBS["melon_rush"] and 10 <= day <= 14 and carry.get("MELON", 0) >= 4 and carry.get("WHEAT", 0) == 0 and i not in S["routes"]:
        if pos in unlocked_shed:
            return ["DROP"]
        return [_step(pos, _nearest(pos, unlocked_shed))]
    # 2b. intraday deposit: carrying products (no feed wheat, no animals) near/at the shed -> DROP
    if KNOBS["drop_min"] > 0 and prod_carried >= KNOBS["drop_min"] and carry.get("WHEAT", 0) == 0 \
            and i not in S["routes"] and day < 28 and hour >= 1:
        shed_room = 100 - sum(n for k, n in shed.items() if n > 0)
        if shed_room >= prod_carried:
            if pos in unlocked_shed:
                return ["DROP"]
            if KNOBS["drop_radius"] > 0 and _shed_dist(pos) <= KNOBS["drop_radius"]:
                return [_step(pos, _nearest(pos, unlocked_shed))]
    if i in S["routes"]:
        op = _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed)
        if op is not None:
            return op
    shed_animals = [(a, n) for a, n in shed.items() if a in ANIMALS and n > 0]
    if shed_animals and len(S["animal_claim"]) < 2 and hour >= 1 and day < 27:
        if pos in unlocked_shed:
            S["animal_claim"].add(i)
            return ["PICKUP", shed_animals[0][0], 1]
        if i in S["animal_claim"] or len(S["animal_claim"]) < 1:
            S["animal_claim"].add(i)
            return [_step(pos, _nearest(pos, unlocked_shed))]
    S["animal_claim"].discard(i)
    # 4b. fertilizer pickup for the crop sweep (hands spawn on shed tiles; hour >= 1 so morning orders landed)
    if (KNOBS["fert_keep"] > 0 or KNOBS["fert_buy"] > 0) and day <= 26 and hour >= 1 and pos in unlocked_shed \
            and carry.get("FERTILIZER", 0) == 0 and pools["fert"] and shed.get("FERTILIZER", 0) > 0 \
            and S.get("fert_taken", 0) < len(v["fert"]):
        n = min(KNOBS["fert_carry"], shed.get("FERTILIZER", 0), len(v["fert"]) - S.get("fert_taken", 0))
        if n > 0:
            S["fert_taken"] = S.get("fert_taken", 0) + n
            return ["PICKUP", "FERTILIZER", int(n)]
    r = None if hour == 0 else _build_route(i, pos, v, day, shed, carry, unlocked_shed, hour)
    if r is not None:
        S["routes"][i] = r
        S["sweep"].pop(i, None)
        op = _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed)
        if op is not None:
            return op
    op = _crop_step(i, pos, v, day, hour, carry, pools, seeds_left)
    if op is not None:
        return op
    # idle deposit: a unit with nothing left to do carries its products (and spare feed) back to the shed
    # so they can be sold this hour instead of at tomorrow's dawn (the frontier sells wool/fertilizer same day).
    if day < 28 and any(carry.get(k, 0) > 0 for k in PRODUCTS) and i not in S["routes"]:
        if pos in unlocked_shed:
            return ["DROP"]
        return [_step(pos, _nearest(pos, unlocked_shed))]
    return ["PASS"]
