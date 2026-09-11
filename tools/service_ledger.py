#!/usr/bin/env python3
"""Service-debt ledger (Sep 11): chronic lateness by obligation class, for BOTH farms in a game.

The delay panel showed a 1-4 h delay of one action has no measurable consequence. What can still cost money is
structural lateness: obligations that are repeatedly serviced late by many hours, carried overnight, or never
serviced. This ledger derives obligations from engine tile state every step and records when each is serviced.

Obligation classes (per farm):
  feed          animal, per day: created h0, serviced when fed_today flips; missed = unfed day (2 in a row -> escape)
  feed_prod     subset of feed on a production day (yield accrues only if fed): missed = lost unit
  care          animal, per day (cared_today): missed = no care bonus
  collect       animal with yield_units >= max_held: created when capped, serviced on HARVEST (yield drops);
                each production day spent capped = lost unit
  fert          animal with fertilizer_available: per day, serviced when it flips False
  water_ongoing ongoing crop tile, per day: created h0, serviced when watered_today flips; missed = cu++ (2 -> weed)
  water_prod    subset on a production day (yield only accrues on watered production days)
  water_window  one-shot crop inside its yield window with yield < max: per day; missed = lost yield unit
  harvest_ready one-shot crop with yield >= max or age >= max_day: created then, serviced on harvest; deadline = rot
                start ((planted+max_day+1)*24); late = steps past rot (yield decays)
  harvest_cap   ongoing crop with yield_units == max_yield: created when capped; each production day capped = lost unit
  weed          WEED tile: created when it appears; serviced when it disappears

Usage: KAGG_FIXED_SHOPS=1 python3 tools/service_ledger.py CAND --opp TAPE --seeds 11-14 [--json out.jsonl]
Prints per farm x class: n/game, serviced %, age at service (mean / p90, hours), overnight-carry %, missed %, lost units.
"""
import sys, os, argparse, json, statistics
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me

CROPS = {"WHEAT": (2, 4, 0, 6, False), "CARROT": (2, 3, 0, 4, False), "TOMATO": (8, 8, 1, 4, True),
         "STRAWBERRY": (10, 10, 2, 4, True), "MELON": (10, 12, 0, 6, False)}   # first, max_day, interval, max_yield, ongoing
ANIMALS = {"GOOSE": (4, 1, 4), "COW": (8, 2, 6), "SHEEP": (6, 3, 6)}          # first, interval, max_held
TPD = 24


def crop_prod_day(t, day):
    """True if the night after `day` is a production night for this ongoing crop (engine: next_day - planted - first) % interval == 0."""
    first, md, itv, mx, ong = CROPS[t["crop"]]
    if not ong: return False
    d = day + 1 - t["planted_day"] - first
    return d >= 0 and d % itv == 0 and (d // itv + 1) <= mx


def animal_prod_day(t, day):
    first, itv, mh = ANIMALS[t["animal"]]
    d = day + 1 - t["placed_day"] - first
    return d >= 0 and d % itv == 0


class Ledger:
    def __init__(self):
        self.open = {}      # key -> obligation dict
        self.closed = []
        self.done = set()   # keys already closed (a serviced per-day obligation must not be re-created that day)
        self.prev = {}      # pos -> (kind, crop, age_days) last step, to classify weeds as crop deaths vs spawns
        self.deaths = []    # (day, crop, age, yield_units) ongoing/one-shot crops that turned into WEED

    def ensure(self, key, cls, step, day, **extra):
        if key not in self.open and (key not in self.done or cls in ("collect", "harvest_cap", "weed")):
            self.open[key] = {"cls": cls, "created": step, "day": day, "prod_days_lost": 0, **extra}

    def close(self, key, step, status):
        o = self.open.pop(key, None)
        if o is None: return
        self.done.add(key)
        o["closed"] = step; o["status"] = status; o["age"] = step - o["created"]
        self.closed.append(o)

    def scan(self, farm, day, hour, step, end_of_day):
        tiles = farm["tiles"]
        seen = set()
        for y, row in enumerate(tiles):
            for x, t in enumerate(row):
                pos = (x, y)
                if isinstance(t, dict) and "animal" in t:
                    a = t["animal"]
                    k = ("feed", pos, day); seen.add(k)
                    self.ensure(k, "feed", day * TPD, day)
                    if t["fed_today"]: self.close(k, step, "serviced")
                    if animal_prod_day(t, day):
                        k = ("feed_prod", pos, day); seen.add(k)
                        self.ensure(k, "feed_prod", day * TPD, day)
                        if t["fed_today"]: self.close(k, step, "serviced")
                    k = ("care", pos, day); seen.add(k)
                    self.ensure(k, "care", day * TPD, day)
                    if t["cared_today"]: self.close(k, step, "serviced")
                    if t.get("fertilizer_available"):
                        k = ("fert", pos, day); seen.add(k); self.ensure(k, "fert", day * TPD, day)
                    else:
                        if ("fert", pos, day) in self.open: self.close(("fert", pos, day), step, "serviced")
                    k = ("collect", pos)
                    if t["yield_units"] >= ANIMALS[a][2]:
                        seen.add(k); self.ensure(k, "collect", step, day, last_day=day)
                        if k in self.open and end_of_day and animal_prod_day(t, day):
                            self.open[k]["prod_days_lost"] += 1
                    elif k in self.open:
                        self.close(k, step, "serviced"); self.done.discard(k)
                elif isinstance(t, dict) and t.get("kind") == "PLANT":
                    first, md, itv, mx, ong = CROPS[t["crop"]]
                    age = day - t["planted_day"]
                    if ong:
                        k = ("water_ongoing", pos, day); seen.add(k)
                        self.ensure(k, "water_ongoing", day * TPD, day)
                        if t["watered_today"]: self.close(k, step, "serviced")
                        if crop_prod_day(t, day):
                            k = ("water_prod", pos, day); seen.add(k)
                            self.ensure(k, "water_prod", day * TPD, day, fert=t.get("fertilized_until_day", -1) >= day)
                            if t["watered_today"]: self.close(k, step, "serviced")
                        k = ("harvest_cap", pos)
                        if t["yield_units"] >= mx:
                            seen.add(k); self.ensure(k, "harvest_cap", step, day)
                            if end_of_day and crop_prod_day(t, day): self.open[k]["prod_days_lost"] += 1
                        elif k in self.open:
                            self.close(k, step, "serviced"); self.done.discard(k)
                    else:
                        ws = (md + 1) // 2
                        if ws <= age <= md and t["yield_units"] < mx:
                            k = ("water_window", pos, day); seen.add(k)
                            self.ensure(k, "water_window", day * TPD, day)
                            if t["watered_today"]: self.close(k, step, "serviced")
                        k = ("harvest_ready", pos, t["planted_day"])
                        if t["yield_units"] >= mx or age >= md:
                            seen.add(k)
                            self.ensure(k, "harvest_ready", step, day, rot=(t["planted_day"] + md + 1) * TPD, yield0=t["yield_units"])
                elif isinstance(t, dict) and t.get("kind") == "WEED":
                    k = ("weed", pos); seen.add(k)
                    if k not in self.open:
                        pv = self.prev.get(pos)
                        if pv and pv[0] == "PLANT":
                            self.deaths.append({"day": day, "crop": pv[1], "age": pv[2], "yield": pv[3]})
                        self.ensure(k, "weed", step, day, origin=("death" if pv and pv[0] == "PLANT" else "spawn"))
        for y, row in enumerate(tiles):
            for x, t in enumerate(row):
                if isinstance(t, dict) and t.get("kind") == "PLANT":
                    self.prev[(x, y)] = ("PLANT", t["crop"], day - t["planted_day"], t["yield_units"])
                else:
                    self.prev[(x, y)] = (t.get("kind") if isinstance(t, dict) else None, None, 0, 0)
        # obligations that vanished from the board: harvested (harvest_ready), dug (weed), escaped/weeded/replanted
        for k in list(self.open):
            if k in seen: continue
            cls = k[0]
            if cls in ("harvest_ready", "weed", "collect", "harvest_cap"):
                self.close(k, step, "serviced")
            elif cls in ("feed", "feed_prod", "care", "fert", "water_ongoing", "water_prod", "water_window"):
                if k[2] != day:
                    self.close(k, step, "missed")     # the day ended without service
                else:
                    self.close(k, step, "gone")       # tile changed mid-day (harvested/escaped/replanted)


def run(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    ledgers = [Ledger(), Ledger()]
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        for p in range(2):
            ledgers[p].scan(o.farms[p], o.day, o.hour, step, end_of_day=(o.hour == TPD - 1))
        if all(s.status == "DONE" for s in state) or step >= steps: break
    for L in ledgers:
        for k in list(L.open): L.close(k, step, "open_at_end")
        for d in L.deaths: L.closed.append({"cls": "crop_death", "status": "death", "created": 0, "closed": 0, "age": 0, **d})
    return [o.farms[p]["money"] for p in range(2)], [L.closed for L in ledgers]


def summarize(rows, n_games):
    by = {}
    for o in rows: by.setdefault(o["cls"], []).append(o)
    out = []
    deaths = by.get("crop_death", [])
    if deaths:
        bc = {}
        for d in deaths: bc.setdefault(d["crop"], []).append(d)
        out.append("  crop deaths (crop -> WEED after 2 unwatered days) per game: " + " ".join(
            f"{c}:{len(v)/n_games:.1f} (mean age {statistics.mean(x['age'] for x in v):.1f}d, yield lost {sum(x['yield'] for x in v)/n_games:.1f}u)" for c, v in sorted(bc.items())))
        wd = by.get("weed", [])
        out.append(f"  weeds/game: from crop death {sum(1 for w in wd if w.get('origin')=='death')/n_games:.1f}, spawned on empty {sum(1 for w in wd if w.get('origin')=='spawn')/n_games:.1f}")
    for cls in ("feed", "feed_prod", "care", "fert", "collect", "water_ongoing", "water_prod", "water_window", "harvest_ready", "harvest_cap", "weed"):
        L = by.get(cls, [])
        if not L: continue
        sv = [o for o in L if o["status"] == "serviced"]
        ages = [o["age"] for o in sv]
        overnight = sum(1 for o in sv if (o["closed"] - 1) // TPD > o["day"])
        missed = sum(1 for o in L if o["status"] in ("missed", "open_at_end"))
        lost = sum(o.get("prod_days_lost", 0) for o in L)
        late_rot = [max(0, o["closed"] - o["rot"]) for o in sv if cls == "harvest_ready"]
        extra = ""
        if cls == "harvest_ready" and late_rot:
            extra = f" past-rot {sum(1 for r in late_rot if r > 0)/n_games:.1f}/game, mean {statistics.mean(late_rot):.0f} steps"
        if cls in ("collect", "harvest_cap"):
            extra = f" prod-days lost at cap {lost/n_games:.1f}/game"
        if cls == "water_prod":
            extra = f" missed while fertilized (lost +1 bonus) {sum(1 for o in L if o['status']=='missed' and o.get('fert'))/n_games:.1f}/game"
        p90 = sorted(ages)[int(0.9 * (len(ages) - 1))] if ages else 0
        out.append(f"  {cls:14s} n/game {len(L)/n_games:6.1f}  serviced {100*len(sv)/len(L):5.1f}%  age h mean {statistics.mean(ages) if ages else 0:5.1f} p90 {p90:4d}  "
                   f"overnight {100*overnight/max(1,len(sv)):4.1f}%  missed {100*missed/len(L):4.1f}%{extra}")
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--opp", required=True)
    ap.add_argument("--seeds", default="11-14"); ap.add_argument("--json", default=None)
    a = ap.parse_args(); os.chdir(ROOT)
    lo, hi = map(int, a.seeds.split("-")); seeds = list(range(lo, hi + 1))
    rows = [[], []]; money = [[], []]
    for s in seeds:
        m, led = run(a.cand, a.opp, s)
        for p in range(2):
            money[p].append(m[p])
            for o in led[p]:
                o["seed"] = s; o["farm"] = p; rows[p].append(o)
    if a.json:
        with open(a.json, "w") as f:
            for p in range(2):
                for o in rows[p]: f.write(json.dumps(o) + "\n")
    for p, name in ((0, os.path.basename(a.cand)), (1, os.path.basename(a.opp))):
        print(f"\n{name}  (farm {p}, mean money {statistics.mean(money[p]):,.0f}, {len(seeds)} games)")
        print(summarize(rows[p], len(seeds)))
