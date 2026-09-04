def _build_route(i, pos, v, day, shed, carry, unlocked_shed, hour=0):
    claimed = set()
    for r in S["routes"].values():
        claimed.update(r["stops"])
    cands = [(p2, t) for p2, t in v["animals"] if p2 not in claimed and _animal_pending(t, day)]
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
    # C: route length scales with herd size instead of a fixed constant, so a bigger
    # fleet gets longer batched routes per hand rather than more, shorter ones.
    herd = len(v["animals"])
    route_len = min(5, max(2, herd // 3))
    # unfed animals go first in the stop order so a hand never reaches a cared-but-unfed
    # animal only to have to double back for wheat.
    unfed_pool = {}
    fed_pool = {}
    for p2, t in cands:
        if day < 29 and not t.get("fed_today", False):
            unfed_pool[p2] = t
        else:
            fed_pool[p2] = t
    stops = []
    cur = pos
    while unfed_pool and len(stops) < route_len:
        nxt = _nearest(cur, list(unfed_pool.keys()))
        stops.append(nxt)
        cur = nxt
        del unfed_pool[nxt]
    while fed_pool and len(stops) < route_len:
        nxt = _nearest(cur, list(fed_pool.keys()))
        stops.append(nxt)
        cur = nxt
        del fed_pool[nxt]
    unfed = sum(1 for s_ in stops if not v["tiles"][s_[1]][s_[0]].get("fed_today", False)) if day < 29 else 0
    need = max(0, unfed - carry.get("WHEAT", 0))
    pickup = min(need, S["wheat_budget"]) if unlocked_shed else 0
    S["wheat_budget"] -= pickup
    return {"stops": stops, "pickup": pickup}


def _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed):
    # feed/care are already paired in the same visit, and fertilizer is only collected
    # while standing on the tile (both verified unchanged from the chassis below).
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
