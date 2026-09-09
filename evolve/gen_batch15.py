#!/usr/bin/env python3
"""Batch 15 (Sep 9): DIAGNOSTIC, not a candidate — port the tape's coherent plan (layout + obligation set) onto
O12's dispatcher and read the move ledger: can our dispatcher reach the tape's efficiency under the tape's plan?
  L1  herd schedule to 17 by ~day 13 regardless of shop luck, inner ring (shed dist<=2) reserved for pastures
  L2  L1 + strawberry tiles capped at 32 (the tape's compact band), wheat fills the rest far (wheat floor)
  L3  L2 + daily animal service (disable B's lifecycle skips: feed/care every animal every day, like the tape)
"""
BASE = "candidates/O12_EVENING_DEPOSIT.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

def herd17_ring(c):
    c = rep(c, '''            if sp == "SHEEP":
                yarn = _instances(obs, "WOOL")
                if yarn == 0:
                    room = min(room, 2 - my_counts[sp])
                elif prices.get("WOOL", 0) >= 1.05 * 200 and day >= 8:
                    room = max(room, 2)
                room = min(room, MAX_SHEEP - my_counts[sp])
            else:
                if _instances(obs, "MILK") == 0 and day >= 9:
                    room = min(room, 4 - my_counts[sp])''',
    '''            sched = min(17, int(4 + 1.0 * day))
            room = max(room, sched - n_total)
            if sp == "SHEEP":
                room = min(room, MAX_SHEEP - my_counts[sp])''')
    c = rep(c, '''    plant = [q for q in sorted(v["empty"], key=lambda q: (_shed_dist(q), q)) if q not in S["claimed_sites"] and q not in S.get("pending_sites",set())][:n_seeds]''',
    '''    ring = (day <= 17 and S.get("herd_room", 0) > 0)
    plant = [q for q in sorted(v["empty"], key=lambda q: (_shed_dist(q), q)) if q not in S["claimed_sites"] and q not in S.get("pending_sites",set())
             and not (ring and _shed_dist(q) <= 2)][:n_seeds]''')
    c = rep(c, '''    if kind == "plant":
        return tp not in S["claimed_sites"] and tp not in S.get("pending_sites",set()) and t is None and _plant_choice(tp, seeds_left) is not None and hour < 22''',
    '''    if kind == "plant":
        if day <= 17 and S.get("herd_room", 0) > 0 and _shed_dist(tp) <= 2:
            return False
        return tp not in S["claimed_sites"] and tp not in S.get("pending_sites",set()) and t is None and _plant_choice(tp, seeds_left) is not None and hour < 22''')
    c = rep(c, '''    # ---- herd
    pending_place = shed_animals + carried_animals''', '''    # ---- herd
    pending_place = shed_animals + carried_animals
    S["herd_room"] = max(0, KNOBS["max_animals"] - n_total)''')
    return c

def straw_cap_wheat_fill(c, cap=32):
    # cap strawberries at `cap` tiles (committed units), and keep a wheat floor of 20 tiles far
    c = rep(c, '''                if c == "STRAWBERRY" and day < KNOBS["straw_delay"]:
                    continue''', f'''                if c == "STRAWBERRY" and day < KNOBS["straw_delay"]:
                    continue
                if c == "STRAWBERRY" and committed[c] >= {cap} * CROP_SPECS[c]["units"]:
                    continue''')
    c = rep(c, "'wheat_tiles': 0", "'wheat_tiles': 20")
    c = rep(c, "'wheat_cap': 22", "'wheat_cap': 30")
    return c

def daily_service(c):
    c = rep(c, '''def _care_useful(t,day):
    if t.get("cared_today",False):return False''', '''def _care_useful(t,day):
    if t.get("cared_today",False):return False
    if day < 28: return True  # diagnostic: daily care like the tape''')
    c = rep(c, '''def _feed_useful(t,day):
    if t.get("fed_today",False) or day>=29:return False''', '''def _feed_useful(t,day):
    if t.get("fed_today",False) or day>=29:return False
    return True  # diagnostic: daily feed like the tape''')
    return c

c1 = herd17_ring(src); write("L1_HERD17_RING", c1)
c2 = straw_cap_wheat_fill(c1); write("L2_HERD17_RING_STRAW32_WHEAT", c2)
c3 = daily_service(c2); write("L3_L2_DAILY_SERVICE", c3)
