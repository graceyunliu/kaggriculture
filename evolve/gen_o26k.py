#!/usr/bin/env python3
"""K_SELFMODEL (Sep 11): the O25/O26 lineage as a chassis source with every validated self-model correction behind a
top-level switch/constant, so (a) the evolve loop can tune each one, (b) ORCH_ON=0 MELON_LATE_FERT=0 MELON_MORNING=0
STRAW_UNITS=4.5 CARROT_UNITS=4.0 HIRE_MAX_MARGINAL=10**9 FERT_PHASE_RULE=0 FERT_IS_INPUT=0 reproduces O15 exactly (the ladder entry /
yardstick), and defaults reproduce O25 plus the two Tier-1 engine facts from O23.

Switches (defaults = O25 + facts):
  ORCH_ON=1              global crop cost-matrix dispatch (O16)
  MELON_LATE_FERT=1      fertilize MELON at age 7-8 so the crop is at 6 units on day 10 (O20/O22)
  MELON_MORNING=1        days 9-14, h<=MELON_MORNING_LAST_HOUR: free units harvest ready melons and carry them home (O22)
  STRAW_UNITS=7.5        seed allocator's expected units per strawberry planting (O24; was 4.5)
  CARROT_UNITS=3.0       seed allocator's expected units per carrot planting (O26_CARROT_SIZING, other session; was 4.0)
  HIRE_MAX_MARGINAL=144  refuse a hire whose fibonacci price exceeds this (O25 / H_GATE144)
  FERT_PHASE_RULE=1      fertilize ongoing crops only on production days (2 covered nights per fert)   [O23 fact]
  FERT_IS_INPUT=1        carried fertilizer is not cargo to deposit (PRODUCTS contains FERTILIZER)     [O23 fact]
Verified by evolve/o26k_check.py.
"""
SRC = "candidates/O26_CARROT_SIZING.py"
OUT = "candidates/K_SELFMODEL.py"
c = open(SRC).read()

def rep(c, old, new):
    assert c.count(old) == 1, f"NOT UNIQUE/FOUND:\n{old[:200]}"
    return c.replace(old, new)

# --- melon late-fert switch + fert phase rule (O23 fact) in _fert_eligible
c = rep(c, '''    if not c["ongoing"]:
        if t.get("crop") != "MELON":
            return False
        # O20: fertilize melons late in the yield window (age 7-8) -> 6 units by age 9-10 -> the whole crop is
        # harvested on day 10 and sold into the fresh $270 melon pool before/with the tapes' 60-unit dump
        return (7 <= age <= 8 and t.get("yield_units", 0) < c["max_yield"]
                and t.get("fertilized_until_day", -1) < day)
    step_i = max(1, c["interval"])
    done = 0 if age < c["first"] else (age - c["first"]) // step_i + 1
    return done < c["max_yield"] and age >= c["first"] - 1 and t.get("fertilized_until_day", -1) < day
''', '''    if not c["ongoing"]:
        if not MELON_LATE_FERT or t.get("crop") != "MELON":
            return False
        # O20: fertilize melons late in the yield window (age 7-8) -> 6 units by age 9-10 -> the whole crop is
        # harvested on day 10 and sold into the fresh $270 melon pool before/with the tapes' 60-unit dump
        return (7 <= age <= 8 and t.get("yield_units", 0) < c["max_yield"]
                and t.get("fertilized_until_day", -1) < day)
    step_i = max(1, c["interval"])
    done = 0 if age < c["first"] else (age - c["first"]) // step_i + 1
    if not (done < c["max_yield"] and age >= c["first"] - 1 and t.get("fertilized_until_day", -1) < day):
        return False
    if FERT_PHASE_RULE:
        # engine fact: fertilizer lasts 3 days (day..day+2) and an ongoing crop produces on the night of day d when
        # (d + 1 - first) % interval == 0 -> fertilizing on a production day covers two production nights, on an
        # off day only one (strawberry: ages 9, 11, 13, 15; the tapes fertilize at exactly 9 and 13).
        return (age + 1 - c["first"]) % step_i == 0
    return True
''')

# --- fertilizer is an input, not deposit cargo (O23 fact)
c = rep(c, '''    prod_carried = sum(carry.get(k, 0) for k in PRODUCTS if k != "WHEAT")
    # O22 melon morning''', '''    prod_carried = sum(carry.get(k, 0) for k in PRODUCTS if k != "WHEAT")
    if FERT_IS_INPUT and day <= 26 and v["fert"]:
        prod_carried -= carry.get("FERTILIZER", 0)   # engine fact: PRODUCTS contains FERTILIZER; carried fertilizer is on its way to a tile, not cargo to deposit
    # O22 melon morning''')

# --- ORCH_ON gate (as in gen_orch_knobbed.py)
c = rep(c, '''    busy = set(S["routes"].keys())
    for j, bag in enumerate(inv):
        if any(bag.get(sp, 0) > 0 for sp in ANIMALS):
            busy.add(j)
    # rebuild the pools fresh (the sweep-based removal above is no longer the source of truth)
    pools = _crop_pools(v, seeds_left, day)
    S["assign"] = _orchestrate(v, pools, positions, day, hour, inv, seeds_left, busy)
    for j, (tp, kind) in S["assign"].items():
        sw = S["sweep"].get(j)
        if not sw or sw[0][0] != tp:
            S["sweep"][j] = [(tp, kind)]
        for pool in pools.values():
            if tp in pool: pool.remove(tp)
    ops = []''', '''    if ORCH_ON:
        busy = set(S["routes"].keys())
        for j, bag in enumerate(inv):
            if any(bag.get(sp, 0) > 0 for sp in ANIMALS):
                busy.add(j)
        # rebuild the pools fresh (the sweep-based removal above is no longer the source of truth)
        pools = _crop_pools(v, seeds_left, day)
        S["assign"] = _orchestrate(v, pools, positions, day, hour, inv, seeds_left, busy)
        for j, (tp, kind) in S["assign"].items():
            sw = S["sweep"].get(j)
            if not sw or sw[0][0] != tp:
                S["sweep"][j] = [(tp, kind)]
            for pool in pools.values():
                if tp in pool: pool.remove(tp)
    ops = []''')
c = rep(c, "ORCH_COMMIT = 0.75", "ORCH_ON = 1                  # O16 global crop-task orchestrator (0 = O15 per-unit sweeps)\nORCH_COMMIT = 0.75")

# --- constants block: put every switch next to ORCH_ON
c = rep(c, "MELON_MORNING = 1            # O22", '''MELON_MORNING = 1            # O22 melon morning (0 = off)
MELON_LATE_FERT = 1          # O20/O22 melon fert at age 7-8 (0 = off)
FERT_PHASE_RULE = 1          # O23 engine fact: fertilize ongoing crops on production days only (0 = off)
FERT_IS_INPUT = 1            # O23 engine fact: carried fertilizer is not deposit cargo (0 = off)''')

c = rep(c, '"CARROT":     {"seed": 20,  "units": 3.0,', '"CARROT":     {"seed": 20,  "units": CARROT_UNITS,')
c = rep(c, "STRAW_UNITS = 7.5 ", "CARROT_UNITS = 3.0  # O26_CARROT_SIZING: expected units per carrot planting (was 4.0; measured 3.0)\nSTRAW_UNITS = 7.5 ")

# --- orchestrator block as in gen_orch_knobbed.py: scalar priorities, _orch_prio(), moved out of the sweep block range
import re as _re
m = _re.search(r"\n# ===== ORCHESTRATOR \(global assignment of crop tasks\) =====\n.*?\n(?=def _crop_step\()", c, _re.S)
assert m, "ORCH section not found"
orch = m.group(0)
c = c[:m.start()] + "\n" + c[m.end():]
orch = rep(orch, 'ORCH_PRIO = {"urgent": 0.0, "harvest": 0.5, "wwater": 0.5, "fert": 0.5, "plant": 1.0, "water": 1.0, "weeds": 1.5, "slack": 6.0}\n',
    '''ORCH_P_HARVEST = 0.5    # priority offsets added to walking distance; lower = taken first
ORCH_P_WWATER = 0.5
ORCH_P_FERT = 0.5
ORCH_P_PLANT = 1.0
ORCH_P_WATER = 1.0
ORCH_P_WEEDS = 1.5
ORCH_P_SLACK = 6.0
''')
orch = rep(orch, "def _orchestrate(", '''def _orch_prio():
    return {"urgent": 0.0, "harvest": ORCH_P_HARVEST, "wwater": ORCH_P_WWATER, "fert": ORCH_P_FERT,
            "plant": ORCH_P_PLANT, "water": ORCH_P_WATER, "weeds": ORCH_P_WEEDS, "slack": ORCH_P_SLACK}


def _orchestrate(''')
orch = rep(orch, '''    prev = S.get("assign", {})
    tasks = []''', '''    prev = S.get("assign", {})
    prio = _orch_prio()
    tasks = []''')
orch = rep(orch, "cost = d + ORCH_PRIO[kind]", "cost = d + prio[kind]")
c = rep(c, "\n# ===== EVOLVE-BLOCK: sweep =====\ndef _build_sweep(", orch.rstrip("\n") + "\n\n\n# ===== EVOLVE-BLOCK: sweep =====\ndef _build_sweep(")

hdr = ("# K_SELFMODEL: O26_CARROT_SIZING (= O25 + carrot sizing) with every validated self-model correction behind a top-level switch (see evolve/gen_o26k.py).\n"
       "# Defaults = O26 + two engine facts (fert phase rule, fertilizer-is-input). All switches off + STRAW_UNITS 4.5 + CARROT_UNITS 4.0 + HIRE_MAX_MARGINAL 10**9 == O15 exactly.\n")
open(OUT, "w").write(hdr + c)
compile(hdr + c, OUT, "exec")
print("wrote", OUT)
