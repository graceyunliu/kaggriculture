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
            tp = _nearest(pos, pools[kind])
            first = (tp, kind)
            pools[kind].remove(tp)
            break
    if first is None:
        return None
    sweep = [first]
    cur = first[0]
    if first[1] == "urgent" and pools["urgent"]:
        tiers = ["urgent", "harvest"]
    # A: once the urgent tier is drained, chain ALL remaining pending water/urgent-class
    # tasks by nearest-neighbour in one pass instead of capping at CROP_SWEEP_LEN.
    urgent_drained = not pools["urgent"]
    cap = None if urgent_drained else CROP_SWEEP_LEN
    while cap is None or len(sweep) < cap:
        best = None
        for kind in tiers:
            for tp in pools[kind]:
                d = _dist(cur, tp)
                if d <= CROP_SWEEP_RADIUS and (best is None or d < best[0]):
                    best = (d, tp, kind)
        if best is None:
            break
        _d, tp, kind = best
        pools[kind].remove(tp)
        sweep.append((tp, kind))
        cur = tp
        if not pools["urgent"]:
            urgent_drained = True
    return sweep


def _crop_step(i, pos, v, day, hour, carry, pools, seeds_left):
    sweep = S["sweep"].get(i)
    if not sweep:
        sweep = _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left)
        if not sweep:
            S["sweep"].pop(i, None)
            return None
        S["sweep"][i] = sweep
    while sweep:
        tp, kind = sweep[0]
        if not _task_valid(tp, kind, v, day, hour, carry, seeds_left):
            sweep.pop(0)
            continue
        if pos != tp:
            return [_step(pos, tp)]
        sweep.pop(0)
        if kind in ("urgent", "water", "slack", "wwater"):
            return ["WATER"]
        if kind == "harvest":
            return ["HARVEST"]
        if kind == "fert":
            return ["FERTILIZE"]
        if kind == "weeds":
            return ["DIG"]
        if kind == "plant":
            c = _plant_choice(tp, seeds_left)
            seeds_left[c] -= 1
            sweep.insert(0, (tp, "urgent"))
            return ["PLANT", c]
    S["sweep"].pop(i, None)
    if any(pools[k] for k in pools):
        return _crop_step(i, pos, v, day, hour, carry, pools, seeds_left)
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
            if sw[idx][1] == "urgent" and (best is None or len(sw) > len(S["sweep"][best[0]])):
                best = (j, idx)
                break
    if best is None:
        for j, sw in S["sweep"].items():
            if j != i and len(sw) >= 3 and (best is None or len(sw) > len(S["sweep"][best[0]])):
                best = (j, len(sw) - 1)
    if best is not None:
        j, idx = best
        task = S["sweep"][j].pop(idx)
        S["sweep"][i] = [task]
        return _crop_step(i, pos, v, day, hour, carry, pools, seeds_left)
    return None
