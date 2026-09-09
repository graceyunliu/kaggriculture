#!/usr/bin/env python3
"""Layer A of the dispatcher rewrite (Sep 9): herder loops on O12.
At h1 each day, H = ceil(pending_animals/7) (max 3) low-index free units become herders: each gets ONE route
covering a contiguous angular arc of all pending animals, ordered nearest-neighbour from the shed, with the full
wheat need picked up once. Crop hands do not build animal routes while the herd is being served (fallback after h14).
Also fixes the pickup-reset bug (pickup forced to 1 when the shed had no wheat at h1 -> refill trips)."""
import math
BASE = "candidates/O12_EVENING_DEPOSIT.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

HERDER = '''
HERD_MAX = 5
HERD_PER = 3
SPAWN_R = 2


def _assign_herders(v, day, hour, shed, unlocked_shed, inv):
    """Once per day (first call at hour>=1): give the pending animals to H low-index free units as full loops."""
    S["herd_day"] = day
    S["herders"] = set()
    pending = [(p2, t) for p2, t in v["animals"] if _animal_pending(t, day)]
    if not pending:
        return
    free = [j for j, pj in enumerate(v["positions"])
            if j not in S["routes"] and not any((inv[j] if j < len(inv) else {}).get(a, 0) > 0 for a in ANIMALS)]
    if not free:
        return
    # spawn-adjacent chains: every free hand takes the nearest unclaimed pending animal within SPAWN_R steps
    # of where it stands (hands spawn at the shed; ring animals are 1-2 steps away), as a 1-stop route.
    if SPAWN_R > 0:
        taken = set()
        for j in list(free):
            pj = v["positions"][j]
            cands = [p2 for p2, t in pending if p2 not in taken and _dist(pj, p2) <= SPAWN_R]
            if not cands:
                continue
            p2 = _nearest(pj, cands); taken.add(p2)
            t = v["tiles"][p2[1]][p2[0]]
            carry = inv[j] if j < len(inv) else {}
            need = 1 if (day < 29 and _feed_useful(t, day) and carry.get("WHEAT", 0) == 0) else 0
            S["wheat_budget"] = max(0, S["wheat_budget"] - need)
            S["routes"][j] = {"stops": [p2], "pickup": need if unlocked_shed else 0, "herd": True}
            S["sweep"].pop(j, None); S["herders"].add(j); free.remove(j)
        pending = [(p2, t) for p2, t in pending if p2 not in taken]
        if not pending or not free:
            return
    H = max(1, min(HERD_MAX, int(math.ceil(len(pending) / float(HERD_PER)))))
    H = min(H, len(free))
    cx, cy = 4.5, 4.5
    pending.sort(key=lambda pt: math.atan2(pt[0][1] - cy, pt[0][0] - cx))
    chunk = int(math.ceil(len(pending) / float(H)))
    for k in range(H):
        arc = pending[k * chunk:(k + 1) * chunk]
        if not arc:
            continue
        j = free[k]
        pool = {p2: t for p2, t in arc}
        stops = []
        cur = v["positions"][j]
        while pool:
            nxt = _nearest(cur, list(pool.keys()))
            stops.append(nxt); cur = nxt; del pool[nxt]
        carry = inv[j] if j < len(inv) else {}
        unfed = sum(1 for s_ in stops if _feed_useful(v["tiles"][s_[1]][s_[0]], day)) if day < 29 else 0
        need = max(0, unfed - carry.get("WHEAT", 0))
        pickup = need if unlocked_shed else 0      # full need; the route waits at the shed until the h1 order lands
        S["wheat_budget"] = max(0, S["wheat_budget"] - pickup)
        S["routes"][j] = {"stops": stops, "pickup": pickup, "herd": True}
        S["sweep"].pop(j, None)
        S["herders"].add(j)

'''

def herders(c):
    c = rep(c, "def _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed):\n", HERDER + "def _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed):\n")
    # pickup-reset bug: keep the full need while waiting for the morning wheat order to land
    c = rep(c, '''            n = min(r["pickup"], shed.get("WHEAT", 0))
            r["pickup"] = 0
            if n > 0:
                return ["PICKUP", "WHEAT", int(n)]
            if hour <= 1:
                r["pickup"] = 1
                return ["PASS"]''', '''            n = min(r["pickup"], shed.get("WHEAT", 0))
            if n > 0:
                r["pickup"] = 0
                return ["PICKUP", "WHEAT", int(n)]
            if hour <= 2:
                return ["PASS"]  # today's wheat order lands at the end of h1; keep the full need
            r["pickup"] = 0''')
    # assignment hook + gate ordinary route building while herders are out
    c = rep(c, '''    r = None if hour == 0 else _build_route(i, pos, v, day, shed, carry, unlocked_shed, hour)
    if r is not None:''', '''    if hour >= 1 and day < 29 and S.get("herd_day") != day:
        _assign_herders(v, day, hour, shed, unlocked_shed, obs["private"].get("inventories") or [])
        if i in S["routes"]:
            op = _route_step(i, pos, v, day, hour, shed, carry, unlocked_shed)
            if op is not None:
                return op
    herd_out = any(j in S["routes"] and S["routes"][j].get("herd") for j in list(S["routes"]))
    r = None if (hour == 0 or (herd_out and hour < 14)) else _build_route(i, pos, v, day, shed, carry, unlocked_shed, hour)
    if r is not None:''')
    # positions must be visible before dispatch (they are: v["positions"] set before the ops loop) -- also expose
    c = rep(c, '''    v["positions"] = positions''', '''    v["positions"] = positions
    S["positions"] = positions''')
    return c

write("H2_SPAWN_CHAINS", herders(src))
write("H2_SPAWN_CHAINS_R3", herders(src).replace("SPAWN_R = 2", "SPAWN_R = 3"))
write("H1_HERDERS_PER3", herders(src).replace("SPAWN_R = 2", "SPAWN_R = 0"))
