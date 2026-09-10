#!/usr/bin/env python3
"""O16K_ORCH_KNOBBED (Sep 10): O16_ORCH_ON_O15 with the orchestrator made switchable and its constants
promoted to top-level `NAME = value` lines so evolve/space.py CONST_SPACE can mutate them.

  ORCH_ON = 0  -> orchestration skipped entirely; behaviour must equal O15_SALE_PRIORITY exactly
  ORCH_ON = 1  -> equals O16_ORCH_ON_O15 exactly (default priorities/commit/slack hour)

The ORCH section is moved out of the `sweep` block range (it sat between _steal_task and _crop_step,
which blocks.build() rejects) to just before _build_sweep, as its own `orchestrator` block.
This file is the new chassis source (blocks.K_LIVE). Verified byte-behaviour with evolve/orch_knobbed_check.py.
"""
import re
SRC = "candidates/O16_ORCH_ON_O15.py"
OUT = "candidates/O16K_ORCH_KNOBBED.py"
c = open(SRC).read()

def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)

# 1. cut the ORCH section out
m = re.search(r"\n# ===== ORCHESTRATOR \(global assignment of crop tasks\) =====\n.*?\n(?=def _crop_step\()", c, re.S)
assert m
orch = m.group(0)
c = c[:m.start()] + "\n" + c[m.end():]

# 2. scalar constants instead of the dict
orch = rep(orch, '''ORCH_PRIO = {"urgent": 0.0, "harvest": 0.5, "wwater": 0.5, "fert": 0.5, "plant": 1.0, "water": 1.0, "weeds": 1.5, "slack": 6.0}
ORCH_COMMIT = 0.75      # bonus for keeping the task a unit is already heading to (prevents swap oscillation)
ORCH_SLACK_HOUR = 14
''', '''ORCH_ON = 1             # 0 = no orchestration (exactly O15), 1 = global crop-task assignment (exactly O16)
ORCH_P_HARVEST = 0.5    # priority offsets added to walking distance; lower = taken first
ORCH_P_WWATER = 0.5
ORCH_P_FERT = 0.5
ORCH_P_PLANT = 1.0
ORCH_P_WATER = 1.0
ORCH_P_WEEDS = 1.5
ORCH_P_SLACK = 6.0
ORCH_COMMIT = 0.75      # bonus for keeping the task a unit is already heading to (prevents swap oscillation)
ORCH_SLACK_HOUR = 14


def _orch_prio():
    return {"urgent": 0.0, "harvest": ORCH_P_HARVEST, "wwater": ORCH_P_WWATER, "fert": ORCH_P_FERT,
            "plant": ORCH_P_PLANT, "water": ORCH_P_WATER, "weeds": ORCH_P_WEEDS, "slack": ORCH_P_SLACK}
''')
orch = rep(orch, '''    prev = S.get("assign", {})
    tasks = []''', '''    prev = S.get("assign", {})
    prio = _orch_prio()
    tasks = []''')
orch = rep(orch, "cost = d + ORCH_PRIO[kind]", "cost = d + prio[kind]")

# 3. re-insert before the sweep block
c = rep(c, "\n# ===== EVOLVE-BLOCK: sweep =====\ndef _build_sweep(", orch.rstrip("\n") + "\n\n\n# ===== EVOLVE-BLOCK: sweep =====\ndef _build_sweep(")

# 4. gate the per-turn assignment
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

hdr = ("# O16K_ORCH_KNOBBED: O16_ORCH_ON_O15 with ORCH_ON gate (0 = O15 behaviour, 1 = O16) and the orchestrator's\n"
       "# priorities/commit bonus/slack hour as top-level constants so the evolve loop can mutate them. Chassis source since Sep 10.\n")
open(OUT, "w").write(hdr + c)
compile(open(OUT).read(), OUT, "exec")
print("wrote", OUT)
