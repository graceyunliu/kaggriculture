#!/usr/bin/env python3
"""Batch 1 candidate generator (Sep 9) — structural hypotheses on top of O8."""
import re, sys
BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
src = open(BASE).read()

def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)

def write(name, c):
    open(f"candidates/{name}.py", "w").write(c)
    compile(c, name, "exec")
    print("wrote", name)

# ---- C01: fertilizer eligibility for one-shot crops in their watering window (+ harvest age gate)
def melon_fert(c):
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
        # one-shot crop: fertilizer doubles each watering's yield inside the window,
        # so one application at window start fills the tile 2 days earlier (melon: full by age 8)
        ws = (c["max_day"] + 1) // 2
        return (ws - 1 <= age <= c["max_day"] - 2 and t.get("yield_units", 0) < c["max_yield"]
                and t.get("fertilized_until_day", -1) < day)''')
    c = rep(c, '''    return yu >= c["max_yield"] or age >= c["max_day"] or day >= 29''',
               '''    if age < c["first"]:
        return False  # engine: HARVEST before first_yield_day is a silent no-op
    return yu >= c["max_yield"] or age >= c["max_day"] or day >= 29''')
    return c

c01 = melon_fert(src)
write("B1_01_MELON_FERT", c01)

# ---- C02: C01 + enough fertilizer supply for the melon window
def more_fert(c):
    c = rep(c, "'fert_buy': 3, 'fert_carry': 2", "'fert_buy': 6, 'fert_carry': 4")
    return c
c02 = more_fert(c01)
write("B1_02_MELON_FERT_SUPPLY", c02)

# ---- C03: melon harvest-ready tiles get their own top-priority sweep tier ("mharv")
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
c03 = melon_priority(src)
write("B1_03_MELON_PRIORITY", c03)

# ---- C04: C02 + C03
c04 = melon_priority(c02)
write("B1_04_MELON_FERT_PRIORITY", c04)

# ---- C05: C04 + melon_rush (drop-divert days 10-14 + harvest at >=5)
c05 = rep(c04, "'melon_rush': 0", "'melon_rush': 1")
write("B1_05_MELON_FULL_RUSH", c05)

# ---- C06: weeds tier ahead of harvest/water (V3_13's validated reorder, ported)
def weeds_first(c):
    c = rep(c, '''    tiers = ["urgent", "wwater", "harvest", "water"]
    if carry.get("FERTILIZER", 0) > 0:
        tiers = ["urgent", "fert", "wwater", "harvest", "water"]
    if hour < 22:
        tiers.append("plant")
    tiers.append("weeds")''',
    '''    tiers = ["urgent", "weeds", "wwater", "harvest", "water"]
    if carry.get("FERTILIZER", 0) > 0:
        tiers = ["urgent", "weeds", "fert", "wwater", "harvest", "water"]
    if hour < 22:
        tiers.append("plant")''')
    return c
c06 = weeds_first(src)
write("B1_06_WEEDS_FIRST", c06)

# ---- C07: herd cap 17 -> 20 now that placement is unthrottled (interaction hypothesis)
c07 = rep(src, "'max_animals': 17", "'max_animals': 20")
write("B1_07_HERD20", c07)

# ---- C08: keep buying animals while more are pending (placement throughput is higher now)
c08 = rep(src, "elif 1 <= day <= 21 and pending_place <= 3 and n_total < KNOBS[\"max_animals\"]:",
               "elif 1 <= day <= 21 and pending_place <= 6 and n_total < KNOBS[\"max_animals\"]:")
write("B1_08_PENDING6", c08)
