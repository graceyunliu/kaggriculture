#!/usr/bin/env python3
"""Batch 9 (Sep 9): zone dispatch — each crop hand owns an angular sector around the shed and builds
its sweep from tasks in that sector (fallback: global pools when the sector is empty). Targets the
measured execution gap: tape 0.6-0.8 moves per work action vs O8 1.1-1.5."""
BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

ZONE_HELPERS = '''
def _zone_of(tp, K):
    ang = math.atan2(tp[1] - 4.5, tp[0] - 4.5)
    return int(((ang + math.pi) / (2 * math.pi)) * K) % K


def _zone_pools(pools, zone, K):
    """Restrict crop pools to one angular sector. Pools are shared per turn; the restricted view keeps
    the same list objects' membership semantics by returning filtered copies that we sync back on pick."""
    return {k: [tp for tp in lst if _zone_of(tp, K) == zone] for k, lst in pools.items()}

'''

def zone_sweep(c, fallback=True, min_zone_tasks=1):
    c = rep(c, "def _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left):\n", ZONE_HELPERS +
    "def _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left):\n"
    "    K = max(1, S.get(\"n_units\", 1))\n"
    "    zp = _zone_pools(pools, i % K, K)\n"
    "    full = pools\n"
    + ("    if sum(len(x) for x in zp.values()) >= %d:\n        pools = zp\n" % min_zone_tasks if fallback else "    pools = zp\n"))
    # every removal must also apply to the shared full pools
    c = rep(c, '''            tp = _nearest(pos, pools[kind])
            first = (tp, kind)
            for pool in pools.values():
                if tp in pool:pool.remove(tp)
            break''', '''            tp = _nearest(pos, pools[kind])
            first = (tp, kind)
            for pool in pools.values():
                if tp in pool:pool.remove(tp)
            for pool in full.values():
                if tp in pool:pool.remove(tp)
            break''')
    c = rep(c, '''        _d, tp, kind = best
        for pool in pools.values():
            if tp in pool:pool.remove(tp)
        sweep.append((tp, kind))''', '''        _d, tp, kind = best
        for pool in pools.values():
            if tp in pool:pool.remove(tp)
        for pool in full.values():
            if tp in pool:pool.remove(tp)
        sweep.append((tp, kind))''')
    c = rep(c, '''    n_units = 1 + len(me["hands"])
    for d in (S["routes"], S["crop"], S["sweep"], S["setup"]):''', '''    n_units = 1 + len(me["hands"])
    S["n_units"] = n_units
    for d in (S["routes"], S["crop"], S["sweep"], S["setup"]):''')
    return c

write("B9_01_ZONE_SWEEP", zone_sweep(src))
write("B9_02_ZONE_SWEEP_MIN3", zone_sweep(src, min_zone_tasks=3))
# zone sweep + larger sweep length inside a zone (compact zone -> longer chains stay short in travel)
write("B9_03_ZONE_SWEEP_LEN9", rep(zone_sweep(src), "CROP_SWEEP_LEN = 6", "CROP_SWEEP_LEN = 9"))
