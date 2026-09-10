#!/usr/bin/env python3
"""Batch 11 (Sep 9): rot-priority harvest (probe 3) and idle-hand pasture pre-build (probe 4), on O9_MELON_LATEFERT."""
BASE = "candidates/O9_MELON_LATEFERT.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

# ---- probe 3: one-shot tiles at age >= max_day rot from the next day; harvest them first ("rharv" tier)
def rot_priority(c):
    c = rep(c, '''    pools = {"urgent": list(v["urgent"]), "wwater": list(v["wwater"]), "harvest": list(v["harvest"]), "water": list(v["water"]),
             "fert": list(v["fert"]), "plant": plant, "weeds": list(v["weeds"]), "slack": list(v["slack"])}''',
    '''    tiles = v["tiles"]
    def _rotting(q):
        t = tiles[q[1]][q[0]]; c_ = CROPS.get(t.get("crop")) if isinstance(t, dict) else None
        return bool(c_) and not c_["ongoing"] and (day - t.get("planted_day", day)) >= c_["max_day"]
    rharv = [q for q in v["harvest"] if _rotting(q)]
    harvest = [q for q in v["harvest"] if q not in rharv]
    pools = {"rharv": rharv, "urgent": list(v["urgent"]), "wwater": list(v["wwater"]), "harvest": harvest, "water": list(v["water"]),
             "fert": list(v["fert"]), "plant": plant, "weeds": list(v["weeds"]), "slack": list(v["slack"])}''')
    c = rep(c, '''    tiers = ["urgent", "wwater", "harvest", "water"]
    if carry.get("FERTILIZER", 0) > 0:
        tiers = ["urgent", "fert", "wwater", "harvest", "water"]''',
    '''    tiers = ["rharv", "urgent", "wwater", "harvest", "water"]
    if carry.get("FERTILIZER", 0) > 0:
        tiers = ["rharv", "urgent", "fert", "wwater", "harvest", "water"]''')
    c = rep(c, '''    if first[1] == "urgent" and pools["urgent"]:
        tiers = ["urgent", "harvest"]''', '''    if first[1] == "urgent" and pools["urgent"]:
        tiers = ["rharv", "urgent", "harvest"]''')
    c = rep(c, '''    if kind == "harvest":
        return isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("yield_units", 0) > 0''',
    '''    if kind in ("harvest", "rharv"):
        return isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("yield_units", 0) > 0''')
    c = rep(c, '''        if kind=="harvest" and c and not c["ongoing"]''', '''        if kind in ("harvest","rharv") and c and not c["ongoing"]''')
    c = rep(c, '''        if kind == "harvest":
            # replant-on-harvest''', '''        if kind in ("harvest", "rharv"):
            # replant-on-harvest''')
    # day-29 work filter treats rharv like harvest
    c = rep(c, '''    if kind == "harvest":
        return True
    if kind in ("urgent", "water", "wwater", "slack"):''', '''    if kind in ("harvest", "rharv"):
        return True
    if kind in ("urgent", "water", "wwater", "slack"):''')
    return c

write("B11_01_ROT_PRIORITY", rot_priority(src))

# ---- probe 4: idle hands on days 1-8 pre-build pastures on the tiles animals will be sited on (BUILD_PASTURE is free;
#      saves the build action + lets _pick_site prefer ready pastures when animals arrive during the busy days 8-14)
def prebuild(c, max_pre=4, last_day=8):
    c = rep(c, '''    op = _crop_step(i, pos, v, day, hour, carry, pools, seeds_left)
    if op is not None:
        return op
    return ["PASS"]''', f'''    op = _crop_step(i, pos, v, day, hour, carry, pools, seeds_left)
    if op is not None:
        return op
    # idle hand, early game: pre-build a pasture on the tile the next animal would be sited on
    if day <= {last_day} and hour < 20 and len(v["empty_pastures"]) < {max_pre}:
        cands = [q for q in v["empty"] if q not in S["claimed_sites"] and q not in SHED_TILES and q not in S.get("prebuild", set())]
        if cands:
            site = min(cands, key=lambda q: (_shed_dist(q), q))
            S.setdefault("prebuild", set()).add(site)
            if pos == site:
                return ["BUILD_PASTURE"]
            return [_step(pos, site)]
    return ["PASS"]''')
    return c

write("B11_02_PREBUILD4", prebuild(src))
write("B11_03_PREBUILD8", prebuild(src, 8, 8))
write("B11_04_ROT_PREBUILD4", prebuild(rot_priority(src)))
