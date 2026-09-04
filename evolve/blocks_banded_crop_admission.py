def _crop_pools(v, seeds_left, day):
    free = [q for q in sorted(v["empty"], key=lambda q: (_shed_dist(q), q)) if q not in S["claimed_sites"]]
    n_rec = seeds_left.get("STRAWBERRY", 0) + seeds_left.get("TOMATO", 0)
    n_one = sum(seeds_left.get(c, 0) for c in CROP_SPECS) - n_rec
    if n_one < 0:
        n_one = 0
    near = [q for q in free if _shed_dist(q) <= NEAR_RADIUS]
    far_left = [q for q in free if _shed_dist(q) > NEAR_RADIUS]
    rec_sites = near[:n_rec]
    near_left = near[n_rec:]
    if len(rec_sites) < n_rec:
        take = n_rec - len(rec_sites)
        rec_sites = rec_sites + far_left[:take]
        far_left = far_left[take:]
    one_sites = far_left[:n_one]
    if len(one_sites) < n_one:
        one_sites = one_sites + near_left[:n_one - len(one_sites)]
    plant = rec_sites + one_sites
    return {"urgent": list(v["urgent"]), "wwater": list(v["wwater"]), "harvest": list(v["harvest"]), "water": list(v["water"]),
            "fert": list(v["fert"]), "plant": plant, "weeds": list(v["weeds"]), "slack": list(v["slack"])}


def _plant_choice(pos, seeds_left):
    d = _shed_dist(pos)
    if d <= NEAR_RADIUS:
        order = ["STRAWBERRY", "TOMATO", "MELON", "CARROT", "WHEAT"]
    elif d <= NEAR_RADIUS + 3:
        order = ["MELON", "CARROT", "WHEAT", "STRAWBERRY", "TOMATO"]
    else:
        order = ["WHEAT", "MELON", "CARROT", "TOMATO", "STRAWBERRY"]
    for c in order:
        if seeds_left.get(c, 0) > 0:
            return c
    return None


def _task_valid(tp, kind, v, day, hour, carry, seeds_left):
    t = v["tiles"][tp[1]][tp[0]]
    if kind in ("urgent", "water", "slack", "wwater"):
        return isinstance(t, dict) and t.get("kind") == "PLANT" and not t.get("watered_today")
    if kind == "harvest":
        return isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("yield_units", 0) > 0
    if kind == "fert":
        return carry.get("FERTILIZER", 0) > 0 and isinstance(t, dict) and _fert_eligible(t, day)
    if kind == "plant":
        return t is None and _plant_choice(tp, seeds_left) is not None and hour < 22
    if kind == "weeds":
        return isinstance(t, dict) and t.get("kind") == "WEED"
    return False
