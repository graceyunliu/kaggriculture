#!/usr/bin/env python3
"""Batch 2 (Sep 9): melon-only fertilizer, fertilizer retention, strawberry-fert priority."""
BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
src = open(BASE).read()

def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)

def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

def melon_only_fert(c):
    c = rep(c, '''def _fert_eligible(t, day):
    c = CROPS.get(t.get("crop"))
    if not c or not c["ongoing"] or day > 26:
        return False
    age = day - t.get("planted_day", day)''',
    '''def _fert_eligible(t, day):
    c = CROPS.get(t.get("crop"))
    if not c or day > 26:
        return False
    age = day - t.get("planted_day", day)
    if not c["ongoing"]:
        if t.get("crop") != "MELON":
            return False
        # melon: one application at window start doubles 3 waterings -> 6 units by age 8,
        # harvestable+sellable at day 10 hour 0, ahead of the frontier's day-10 dump
        ws = (c["max_day"] + 1) // 2
        return (ws - 1 <= age <= ws + 1 and t.get("yield_units", 0) < c["max_yield"]
                and t.get("fertilized_until_day", -1) < day)''')
    c = rep(c, '''    return yu >= c["max_yield"] or age >= c["max_day"] or day >= 29''',
               '''    if age < c["first"]:
        return False  # engine: HARVEST before first_yield_day is a silent no-op
    return yu >= c["max_yield"] or age >= c["max_day"] or day >= 29''')
    return c

def melon_priority(c):
    c = rep(c, '''    return {"urgent": list(v["urgent"]), "wwater": list(v["wwater"]), "harvest": list(v["harvest"]), "water": list(v["water"]),
            "fert": list(v["fert"]), "plant": plant, "weeds": list(v["weeds"]), "slack": list(v["slack"])}''',
    '''    tiles = v["tiles"]
    mharv = [q for q in v["harvest"] if tiles[q[1]][q[0]].get("crop") == "MELON"]
    harvest = [q for q in v["harvest"] if q not in mharv]
    return {"mharv": mharv, "urgent": list(v["urgent"]), "wwater": list(v["wwater"]), "harvest": harvest, "water": list(v["water"]),
            "fert": list(v["fert"]), "plant": plant, "weeds": list(v["weeds"]), "slack": list(v["slack"])}''')
    c = rep(c, '''    tiers = ["urgent", "wwater", "harvest", "water"]
    if carry.get("FERTILIZER", 0) > 0:
        tiers = ["urgent", "fert", "wwater", "harvest", "water"]''',
    '''    tiers = ["mharv", "urgent", "wwater", "harvest", "water"]
    if carry.get("FERTILIZER", 0) > 0:
        tiers = ["mharv", "urgent", "fert", "wwater", "harvest", "water"]''')
    c = rep(c, '''    if first[1] == "urgent" and pools["urgent"]:
        tiers = ["urgent", "harvest"]''',
    '''    if first[1] == "urgent" and pools["urgent"]:
        tiers = ["mharv", "urgent", "harvest"]
    if first[1] == "mharv":
        tiers = ["mharv", "harvest"]''')
    c = rep(c, '''    if kind == "harvest":
        return isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("yield_units", 0) > 0''',
    '''    if kind in ("harvest", "mharv"):
        return isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("yield_units", 0) > 0''')
    c = rep(c, '''        if kind=="harvest" and c and not c["ongoing"]''', '''        if kind in ("harvest","mharv") and c and not c["ongoing"]''')
    c = rep(c, '''        if kind == "harvest":
            # replant-on-harvest''', '''        if kind in ("harvest", "mharv"):
            # replant-on-harvest''')
    return c

# B2_01: melon-only fert eligibility
c1 = melon_only_fert(src); write("B2_01_MELON_ONLY_FERT", c1)
# B2_02: + melon harvest priority tier
c2 = melon_priority(c1); write("B2_02_MELON_FERT_PRIO", c2)
# B2_03: fertilizer retention — keep bought/collected fertilizer in the shed for pickup instead of selling it back each hour
c3 = rep(src, "'fert_keep': 0", "'fert_keep': 6"); write("B2_03_FERT_KEEP6", c3)
# B2_04: B2_02 + retention
c4 = rep(c2, "'fert_keep': 0", "'fert_keep': 6"); write("B2_04_MELON_FERT_PRIO_KEEP", c4)
# B2_05: fert pickup carry 2 -> 4 with retention (hands carry more per trip)
c5 = rep(c3, "'fert_carry': 2", "'fert_carry': 4"); write("B2_05_FERT_KEEP6_CARRY4", c5)
# B2_06: sell melons in one hour-0 block on the first harvest day rather than dribbling: hold melons in shed until >= 24 units or day>=12
c6 = rep(src, '''        n = shed.get("MELON", 0)
        if n > 0 and (prices.get("MELON", 0) >= KNOBS["melon_floor"] or day >= 27 or shed_load > 75):''',
'''        n = shed.get("MELON", 0)
        if n > 0 and (n >= 24 or day >= 12 or day >= 27 or shed_load > 75):''')
write("B2_06_MELON_BLOCK_SELL", c6)
