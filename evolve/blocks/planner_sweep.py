FERT_RADIUS = 2
SPREAD_W = 1.0
SPREAD_CAP = 5


def _spread_pick(i, pos, cands):
    """First stop of a sweep: nearest tile, discounted by how far it is from where the other
    units are already working, so hands fan out into separate regions (expert pattern) instead
    of crowding the tiles nearest the shed and then criss-crossing."""
    others = []
    for j, sw in S.get("sweep", {}).items():
        if j != i and sw:
            others.append(sw[0][0])
    best, bs = None, None
    for c in cands:
        d = _dist(pos, c)
        sep = min([_dist(c, o) for o in others] + [SPREAD_CAP]) if others else SPREAD_CAP
        score = (d - SPREAD_W * sep, d, c)
        if bs is None or score < bs:
            best, bs = c, score
    return best


def _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left):
    tiers = ["urgent", "wwater", "harvest", "water"]
    if carry.get("FERTILIZER", 0) > 0:
        tiers = ["urgent", "fert", "wwater", "harvest", "water"]
    if hour < 22:
        tiers.append("plant")
    tiers.append("weeds")
    if hour >= 14:
        tiers.append("slack")
    first = None
    for kind in tiers:
        if pools[kind]:
            tp = _spread_pick(i, pos, pools[kind]) if kind != "fert" else _nearest(pos, pools[kind])
            if kind == "fert" and _dist(pos, tp) > FERT_RADIUS:
                continue  # never walk across the map just to fertilize; sell it instead
            first = (tp, kind)
            pools[kind].remove(tp)
            break
    if first is None:
        return None
    sweep = [first]
    cur = first[0]
    if first[1] == "urgent" and pools["urgent"]:
        tiers = ["urgent", "harvest"]
    while len(sweep) < CROP_SWEEP_LEN:
        best = None
        for kind in tiers:
            for tp in pools[kind]:
                d = _dist(cur, tp)
                lim = FERT_RADIUS if kind == "fert" else CROP_SWEEP_RADIUS
                if d <= lim and (best is None or d < best[0]):
                    best = (d, tp, kind)
        if best is None:
            break
        _d, tp, kind = best
        pools[kind].remove(tp)
        sweep.append((tp, kind))
        cur = tp
    return sweep


def _crop_step(i, pos, v, day, hour, carry, pools, seeds_left):
    sweep = S["sweep"].get(i)
    if not sweep:
        sweep = _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left)
        if not sweep:
            S["sweep"].pop(i, None)
            # idle hand with empty pools: take work from another unit's sweep instead of passing
            return _steal_task(i, pos, v, day, hour, carry, pools, seeds_left)
        S["sweep"][i] = sweep
    while sweep:
        tp, kind = sweep[0]
        if not _task_valid(tp, kind, v, day, hour, carry, seeds_left):
            sweep.pop(0)
            continue
        if pos != tp:
            if _dist(pos, tp) + 1 > 24 - hour:
                sweep.pop(0)  # unreachable before end of day: don't march toward it
                continue
            return [_step(pos, tp)]
        sweep.pop(0)
        if kind in ("urgent", "water", "slack", "wwater"):
            return ["WATER"]
        if kind == "harvest":
            # replant-on-harvest (expert pattern H->P->W): if the tile empties, plant and water it
            # before walking on. _task_valid drops the entry if the crop is ongoing and still standing.
            if hour < 22 and _plant_choice(tp, seeds_left) is not None:
                sweep.insert(0, (tp, "plant"))
            return ["HARVEST"]
        if kind == "fert":
            return ["FERTILIZE"]
        if kind == "weeds":
            if hour < 22 and _plant_choice(tp, seeds_left) is not None:
                sweep.insert(0, (tp, "plant"))  # expert pattern D->P->W
            return ["DIG"]
        if kind == "plant":
            c = _plant_choice(tp, seeds_left)
            seeds_left[c] -= 1
            sweep.insert(0, (tp, "urgent"))
            return ["PLANT", c]
    S["sweep"].pop(i, None)
    if any(pools[k] for k in pools):
        return _crop_step(i, pos, v, day, hour, carry, pools, seeds_left)
    return _steal_task(i, pos, v, day, hour, carry, pools, seeds_left)


def _steal_task(i, pos, v, day, hour, carry, pools, seeds_left):
    if S.get("opponent_mode") == "yuan":
        return None
    remaining = 23 - hour
    best = None
    for j, sw in list(S["sweep"].items()):
        if j == i or not sw:
            continue
        eta = 0
        cur = v["positions"][j]
        for idx, (tp, kind) in enumerate(sw):
            eta += _dist(cur, tp) + 1
            cur = tp
            if kind == "urgent" and eta > remaining:
                mine = _dist(pos, tp) + 1
                if mine <= remaining and (best is None or mine < best[0]):
                    best = (mine, j, idx)
    if best is not None:
        _m, j, idx = best
        tp, kind = S["sweep"][j].pop(idx)
        S["sweep"][i] = [(tp, kind)]
        return _crop_step(i, pos, v, day, hour, carry, pools, seeds_left)
    best = None
    for j, sw in S["sweep"].items():
        if j == i or len(sw) < 2:
            continue
        for idx in range(len(sw) - 1, 0, -1):
            tp, kind = sw[idx]
            mine = _dist(pos, tp) + 1
            if mine > remaining:
                continue
            key = (0 if kind == "urgent" else 1, mine, -len(sw))
            if best is None or key < best[0]:
                best = (key, j, idx)
    if best is not None:
        _k, j, idx = best
        task = S["sweep"][j].pop(idx)
        S["sweep"][i] = [task]
        return _crop_step(i, pos, v, day, hour, carry, pools, seeds_left)
    return None

