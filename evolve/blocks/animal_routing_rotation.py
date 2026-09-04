def _build_route(i, pos, v, day, shed, carry, unlocked_shed, hour=0):
    claimed = set()
    for r in S["routes"].values():
        claimed.update(r["stops"])
    # feed rotation (frontier behaviour): when wheat is short, animals fed yesterday can skip a day;
    # an animal only escapes after 2 consecutive unfed days, so those at 1 are fed first.
    carried_wheat = carry.get("WHEAT", 0)
    unfed_all = [t for _p, t in v["animals"] if not t.get("fed_today", False)]
    short = day < 29 and (S["wheat_budget"] + carried_wheat) < len(unfed_all)

    def _pending_rot(t):
        if day >= 29:
            return _animal_pending(t, day)
        need_feed = not t.get("fed_today", False)
        if need_feed and short and t.get("consecutive_unfed", 0) == 0:
            need_feed = False                       # can wait until tomorrow; wheat goes to the at-risk ones
        need_care = (not t.get("cared_today", False)) and day < 28
        return need_feed or need_care or t.get("fertilizer_available", False) or t.get("yield_units", 0) > 0

    cands = [(p2, t) for p2, t in v["animals"] if p2 not in claimed and _pending_rot(t)]
    if short:
        # at-risk animals first: build the route from them, then the rest
        risk = [(p2, t) for p2, t in cands if not t.get("fed_today", False) and t.get("consecutive_unfed", 0) >= 1]
        rest = [(p2, t) for p2, t in cands if (p2, t) not in risk]
        cands = risk + rest
    if not cands and hour >= 14:
        best = None
        for j, r in S["routes"].items():
            if j == i or len(r["stops"]) < 2:
                continue
            tp = r["stops"][-1]
            t = v["tiles"][tp[1]][tp[0]]
            needs_wheat = day < 29 and not t.get("fed_today", False) and carry.get("WHEAT", 0) == 0
            if needs_wheat:
                continue
            gain = _dist(v["positions"][j], tp) - _dist(pos, tp)
            if gain >= 3 and (best is None or gain > best[0]):
                best = (gain, j)
        if best is not None:
            tp = S["routes"][best[1]]["stops"].pop()
            cands = [(tp, v["tiles"][tp[1]][tp[0]])]
    if not cands:
        return None
    stops = []
    cur = pos
    if short:
        risk_keys = [p2 for p2, t in cands if not t.get("fed_today", False) and t.get("consecutive_unfed", 0) >= 1]
        pool_r = {p2: t for p2, t in cands if p2 in risk_keys}
        while pool_r and len(stops) < ROUTE_LEN:
            nxt = _nearest(cur, list(pool_r.keys()))
            stops.append(nxt)
            cur = nxt
            del pool_r[nxt]
    pool = {p2: t for p2, t in cands if p2 not in stops}
    while pool and len(stops) < ROUTE_LEN:
        nxt = _nearest(cur, list(pool.keys()))
        stops.append(nxt)
        cur = nxt
        del pool[nxt]
    unfed = sum(1 for s_ in stops if not v["tiles"][s_[1]][s_[0]].get("fed_today", False)) if day < 29 else 0
    need = max(0, unfed - carry.get("WHEAT", 0))
    pickup = min(need, S["wheat_budget"]) if unlocked_shed else 0
    S["wheat_budget"] -= pickup
    return {"stops": stops, "pickup": pickup}


def _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed):
    r = S["routes"][i]
    tiles = v["tiles"]
    if r["pickup"] > 0:
        if pos in unlocked_shed:
            n = min(r["pickup"], shed.get("WHEAT", 0))
            r["pickup"] = 0
            if n > 0:
                return ["PICKUP", "WHEAT", int(n)]
            if hour <= 1:
                r["pickup"] = 1
                return ["PASS"]
        else:
            return [_step(pos, _nearest(pos, unlocked_shed))]
    while r["stops"]:
        tgt = r["stops"][0]
        t = tiles[tgt[1]][tgt[0]]
        if not (isinstance(t, dict) and "animal" in t):
            r["stops"].pop(0)
            continue
        if pos != tgt:
            return [_step(pos, tgt)]
        if day < 29 and not t.get("fed_today", False) and carry.get("WHEAT", 0) > 0:
            return ["FEED"]
        if day < 29 and not t.get("fed_today", False) and carry.get("WHEAT", 0) == 0 and S["wheat_budget"] > 0 and hour < 21 and not r.get("refilled"):
            unfed = sum(1 for s_ in r["stops"] if not tiles[s_[1]][s_[0]].get("fed_today", False))
            r["pickup"] = min(unfed, S["wheat_budget"]); S["wheat_budget"] -= r["pickup"]; r["refilled"] = True
            return [_step(pos, _nearest(pos, unlocked_shed))] if pos not in unlocked_shed else ["PICKUP", "WHEAT", int(r["pickup"])]
        if day < 28 and not t.get("cared_today", False):
            return ["CARE"]
        if t.get("fertilizer_available", False):
            return ["COLLECT_FERTILIZER"]
        if t.get("yield_units", 0) > 0:
            return ["HARVEST"]
        r["stops"].pop(0)
    del S["routes"][i]
    return None
