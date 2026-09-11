#!/usr/bin/env python3
"""O32_MELON_URGENT_EXEMPT (Sep 11): the narrowest override of the O22 melon-morning convoy.

Mechanism (from tools/straw_displace.py): MELON_MORNING runs before crop-sweep dispatch and
unconditionally claims every routeless unit for hours 0-8 on days 9-14, so a tile that is already
urgent (engine consecutive_unwatered >= 1) can sit unclaimed all day and convert to weed at cu=2.

Fix: if the global orchestrator assigned THIS unit an urgent crop-water task this turn, the melon
mode does not take it. The orchestrator already matches at most one task per unit and prices by
distance, so at most (number of urgent tasks) units are held back, each the nearest one -- no
permanent reservation, no new threshold, no cutoff change (h8 is kept).

Variants:
  O30_MELON_URGENT_EXEMPT  -- exempt on any urgent crop-water task
  O30B_MELON_URGENT_PREPROD -- exempt only on urgent PRE-PRODUCTION tiles (age < first yield day),
                               i.e. exactly the population the strawberry-death trace identified.
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "candidates", "O26_CARROT_SIZING.py")

HELPER = '''
MELON_URGENT_EXEMPT = 1        # O30: melon morning must not bypass an already-urgent lifecycle obligation
MELON_URGENT_PREPROD_ONLY = 0  # O30B: restrict the exemption to pre-production tiles


def _melon_urgent_exempt(i, v, day, carry):
    """True if unit i must be left to normal dispatch instead of being claimed by the melon convoy.

    Uses the orchestrator's own assignment for this turn (S["assign"]), so the unit held back is the
    one global min-cost matching already chose for that urgent tile, and at most one unit is held
    back per outstanding urgent task. A unit already carrying melons is never exempted -- its cargo
    still has to reach the shed."""
    if not MELON_URGENT_EXEMPT:
        return False
    if carry.get("MELON", 0) > 0:
        return False
    a = S.get("assign", {}).get(i)
    if not a or a[1] != "urgent":
        return False
    if MELON_URGENT_PREPROD_ONLY:
        tp = a[0]
        t = v["tiles"][tp[1]][tp[0]]
        if not isinstance(t, dict):
            return False
        c = CROPS.get(t.get("crop"))
        if not c or day - t.get("planted_day", day) >= c["first"]:
            return False
    S.get("melon_claim", {}).pop(i, None)
    return True

'''

OLD_GATE = ('    if MELON_MORNING and 9 <= day <= 14 and hour <= MELON_MORNING_LAST_HOUR '
            'and i not in S["routes"]:\n')
NEW_GATE = ('    if MELON_MORNING and 9 <= day <= 14 and hour <= MELON_MORNING_LAST_HOUR '
            'and i not in S["routes"] \\\n            and not _melon_urgent_exempt(i, v, day, carry):\n')
ANCHOR = "def _unit_action(i, pos, carry, obs, v, pools, seeds_left, shed, unlocked_shed):\n"


def build(name, header, **consts):
    src = open(BASE).read()
    assert src.count(OLD_GATE) == 1, "melon-morning gate not unique"
    src = src.replace(OLD_GATE, NEW_GATE)
    assert src.count(ANCHOR) == 1
    src = src.replace(ANCHOR, HELPER + "\n" + ANCHOR)
    for k, val in consts.items():
        line_old = f"{k} = "
        i = src.index(line_old)
        j = src.index("\n", i)
        src = src[:i] + f"{k} = {val!r}" + src[j:]
    out = os.path.join(ROOT, "candidates", name + ".py")
    body = header + src
    compile(body, out, "exec")
    open(out, "w").write(body)
    print("wrote", out)


if __name__ == "__main__":
    build("O32_MELON_URGENT_EXEMPT",
          "# O30_MELON_URGENT_EXEMPT: O26_CARROT_SIZING + the melon convoy yields a unit back to normal dispatch when the\n"
          "# orchestrator assigned it an URGENT crop-water task (engine consecutive_unwatered >= 1). Narrow override of the\n"
          "# O22 displacement found by tools/straw_displace.py; cutoff unchanged (h8), no reserved worker.\n")
    build("O32B_MELON_URGENT_PREPROD",
          "# O30B_MELON_URGENT_PREPROD: as O30 but the exemption applies only to urgent PRE-PRODUCTION tiles (age < first\n"
          "# yield day) -- exactly the population in the strawberry early-death trace.\n",
          MELON_URGENT_PREPROD_ONLY=1)
