def _build_route(i, pos, v, day, shed, carry, unlocked_shed, hour=0):
    """Compatibility entry point; routes are built jointly by the dispatcher."""
    plan = S.get("plan")
    if plan and plan.get("day") == day:
        return plan.get("routes", {}).get(i)
    return None


def _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed):
    """Execute one step of a jointly planned route."""
    plan = S.get("plan") or {}
    route = plan.get("routes", {}).get(i)
    if not route:
        return None
    pickup = route.get("pickup", {})
    for item in sorted(pickup):
        need = pickup.get(item, 0)
        have = carry.get(item, 0)
        if need > have:
            if pos not in unlocked_shed:
                return [_step(pos, min(unlocked_shed, key=lambda q: (_dist(pos, q), q)))] if unlocked_shed else None
            n = min(need - have, shed.get(item, 0))
            pickup[item] = have
            if n > 0:
                return ["PICKUP", item, int(n)]
    while route.get("stops"):
        chore = route["stops"][0]
        tp = chore["pos"]
        tile = v["tiles"][tp[1]][tp[0]]
        kind = chore["kind"]
        valid = False
        if kind == "water":
            valid = isinstance(tile, dict) and tile.get("kind") == "PLANT" and not tile.get("watered_today")
        elif kind == "harvest_crop":
            valid = isinstance(tile, dict) and tile.get("kind") == "PLANT" and _harvest_ready(tile, day)
        elif kind == "fertilize":
            valid = carry.get("FERTILIZER", 0) > 0 and isinstance(tile, dict) and _fert_eligible(tile, day)
        elif kind == "plant":
            valid = tile is None and hour < 22 and _plant_choice(tp, plan.get("seeds_left", {})) is not None
        elif kind == "dig":
            valid = isinstance(tile, dict) and tile.get("kind") == "WEED"
        elif kind in ("feed", "care", "collect", "harvest_animal"):
            valid = isinstance(tile, dict) and "animal" in tile
            if kind == "feed": valid = valid and not tile.get("fed_today") and carry.get("WHEAT", 0) > 0
            if kind == "care": valid = valid and day < 28 and not tile.get("cared_today")
            if kind == "collect": valid = valid and tile.get("fertilizer_available", False)
            if kind == "harvest_animal": valid = valid and tile.get("yield_units", 0) > 0
        if not valid:
            route["stops"].pop(0)
            continue
        if pos != tp:
            return [_step(pos, tp)]
        route["stops"].pop(0)
        plan.setdefault("chore_done", set()).add(chore["id"])
        if kind == "water": return ["WATER"]
        if kind in ("harvest_crop", "harvest_animal"): return ["HARVEST"]
        if kind == "fertilize": return ["FERTILIZE"]
        if kind == "dig": return ["DIG"]
        if kind == "feed": return ["FEED"]
        if kind == "care": return ["CARE"]
        if kind == "collect": return ["COLLECT_FERTILIZER"]
        if kind == "plant":
            crop = _plant_choice(tp, plan.get("seeds_left", {}))
            if crop is None:
                continue
            plan["seeds_left"][crop] -= 1
            water = {"id": "water:%d,%d" % tp, "kind": "water", "pos": tp,
                     "deadline": 23, "value": 1000.0, "needs": None, "hard": True}
            route["stops"].insert(0, water)
            return ["PLANT", crop]
    return None
