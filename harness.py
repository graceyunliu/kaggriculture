# Kaggriculture harness: replay archive -> SQLite -> reports
# Design doc: harness module (D18, D30-D34)
#
# Usage:
#   python3 harness.py ingest <replay1.json> [replay2.json ...]
#   python3 harness.py report
#
# Raw replays stay on disk (archival source of truth); this DB stores
# extracted features only. Re-ingesting the same episode id is a no-op.

import json
import sqlite3
import sys
from collections import defaultdict

DB = "kaggriculture.db"
MY_NAME = "graceyunliu"

SCHEMA = """
CREATE TABLE IF NOT EXISTS episodes (
    episode_id INTEGER PRIMARY KEY,
    path TEXT,
    p0 TEXT, p1 TEXT,
    money0 REAL, money1 REAL,
    winner TEXT,               -- name, or 'TIE'
    my_seat INTEGER,           -- 0/1, NULL if we're not in this episode
    my_result TEXT             -- WIN/LOSS/TIE, NULL if not ours
);
CREATE TABLE IF NOT EXISTS profiles (
    episode_id INTEGER, seat INTEGER, name TEXT,
    plant_wheat INTEGER, plant_carrot INTEGER, plant_tomato INTEGER,
    plant_strawberry INTEGER, plant_melon INTEGER,
    quad2_day INTEGER, quad3_day INTEGER, quad4_day INTEGER,
    avg_hires REAL,
    sells_json TEXT,           -- {item: {units, orders, first_day, last_day}}
    PRIMARY KEY (episode_id, seat)
);
CREATE TABLE IF NOT EXISTS tags (
    episode_id INTEGER, seat INTEGER, tag TEXT, detail TEXT
);
"""


def extract(path):
    j = json.load(open(path))
    steps = j["steps"]
    names = (j.get("info", {}).get("TeamNames")) or ["player0", "player1"]
    tpd = j.get("configuration", {}).get("turnsPerDay", 24)
    ep_id = j.get("info", {}).get("EpisodeId") or j.get("id") or abs(hash(path)) % 10**9

    plantings = [defaultdict(int), defaultdict(int)]
    sells = [defaultdict(lambda: {"units": 0, "orders": 0, "first_day": None, "last_day": None}),
             defaultdict(lambda: {"units": 0, "orders": 0, "first_day": None, "last_day": None})]
    hires = [defaultdict(int), defaultdict(int)]
    land = [{}, {}]
    deaths = [0, 0]
    shed_max = [0, 0]
    prev_q = [1, 1]

    for t, step in enumerate(steps):
        day = t // tpd
        farms = step[0].get("observation", {}).get("farms")
        if farms:
            for p in (0, 1):
                q = len(farms[p].get("unlocked_quadrants", ["NW"]))
                if q != prev_q[p]:
                    land[p][q] = day
                    prev_q[p] = q
                hires[p][day] = max(hires[p][day], farms[p].get("hires_today", 0))
                for row in farms[p]["tiles"]:
                    for tile in row:
                        if isinstance(tile, dict) and tile.get("kind") == "PLANT" \
                                and tile.get("consecutive_unwatered", 0) >= 2:
                            deaths[p] += 1
        for p in (0, 1):
            priv = step[p].get("observation", {}).get("private")
            if priv:
                load = sum(n for n in priv["shed"].values() if isinstance(n, int) and n > 0)
                if load >= 100:
                    shed_max[p] += 1
            act = step[p].get("action") or {}
            if not isinstance(act, dict):
                continue
            for op in [act.get("farmer") or []] + list(act.get("hands") or []):
                if op and op[0] == "PLANT" and len(op) > 1:
                    plantings[p][op[1]] += 1
            for order in act.get("market") or []:
                if order and order[0] == "SELL" and len(order) >= 3:
                    s = sells[p][order[1]]
                    s["units"] += int(order[2]); s["orders"] += 1
                    s["first_day"] = day if s["first_day"] is None else s["first_day"]
                    s["last_day"] = day

    money = [steps[-1][0]["observation"]["farms"][p]["money"] for p in (0, 1)]
    winner = "TIE" if money[0] == money[1] else names[money[1] > money[0]]
    my_seat = names.index(MY_NAME) if MY_NAME in names and names[0] != names[1] else \
              (0 if MY_NAME in names else None)
    my_result = None
    if my_seat is not None:
        my_result = "TIE" if winner == "TIE" else ("WIN" if names[my_seat] == winner else "LOSS")

    rows = {"episode": (ep_id, path, names[0], names[1], money[0], money[1],
                        winner, my_seat, my_result),
            "profiles": [], "tags": []}
    for p in (0, 1):
        pl = plantings[p]
        rows["profiles"].append((
            ep_id, p, names[p],
            pl.get("WHEAT", 0), pl.get("CARROT", 0), pl.get("TOMATO", 0),
            pl.get("STRAWBERRY", 0), pl.get("MELON", 0),
            land[p].get(2), land[p].get(3), land[p].get(4),
            sum(hires[p].values()) / max(1, len(hires[p])),
            json.dumps({k: v for k, v in sells[p].items()}),
        ))
        if deaths[p]:
            rows["tags"].append((ep_id, p, "DECAY", f"{deaths[p]} tile-turns at death threshold"))
        if shed_max[p]:
            rows["tags"].append((ep_id, p, "SHED_AT_CAP", f"{shed_max[p]} turns"))
    return rows


def ingest(paths):
    con = sqlite3.connect(DB)
    con.executescript(SCHEMA)
    added = skipped = 0
    for path in paths:
        r = extract(path)
        ep_id = r["episode"][0]
        if con.execute("SELECT 1 FROM episodes WHERE episode_id=?", (ep_id,)).fetchone():
            skipped += 1
            continue
        con.execute("INSERT INTO episodes VALUES (?,?,?,?,?,?,?,?,?)", r["episode"])
        con.executemany("INSERT INTO profiles VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", r["profiles"])
        con.executemany("INSERT INTO tags VALUES (?,?,?,?)", r["tags"])
        added += 1
    con.commit()
    print(f"ingested {added}, skipped {skipped} already-known")


def report():
    con = sqlite3.connect(DB)
    n, w, l, t = con.execute(
        "SELECT COUNT(*), SUM(my_result='WIN'), SUM(my_result='LOSS'), SUM(my_result='TIE') "
        "FROM episodes WHERE my_result IS NOT NULL").fetchone()
    print(f"my episodes: {n}  W/L/T: {w or 0}/{l or 0}/{t or 0}")

    print("\nloss tags (mine):")
    for tag, c in con.execute(
        "SELECT t.tag, COUNT(*) FROM tags t JOIN episodes e ON e.episode_id=t.episode_id "
        "AND t.seat=e.my_seat WHERE e.my_result='LOSS' GROUP BY t.tag ORDER BY 2 DESC"):
        print(f"  {tag}: {c}")

    print("\nopponent meta (avg plantings per game, non-self opponents):")
    row = con.execute(
        "SELECT COUNT(*), AVG(plant_wheat), AVG(plant_carrot), AVG(plant_tomato), "
        "AVG(plant_strawberry), AVG(plant_melon), AVG(quad2_day) FROM profiles p "
        "JOIN episodes e ON e.episode_id=p.episode_id "
        "WHERE e.my_seat IS NOT NULL AND p.seat != e.my_seat AND p.name != ?", (MY_NAME,)).fetchone()
    if row and row[0]:
        n2, wh, ca, to, st, me, q2 = row
        print(f"  games: {n2} | wheat {wh:.0f}, carrot {ca:.0f}, tomato {to:.0f}, "
              f"strawberry {st:.0f}, melon {me:.0f} | avg quad2 day: {q2 if q2 is None else round(q2,1)}")
    else:
        print("  no real opponents ingested yet")

    print("\nrecent episodes:")
    for r in con.execute(
        "SELECT episode_id, p0, p1, money0, money1, my_result FROM episodes "
        "ORDER BY episode_id DESC LIMIT 8"):
        print(f"  {r[0]}: {r[1]} ${r[3]:,.0f} vs {r[2]} ${r[4]:,.0f}  [{r[5]}]")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
    elif sys.argv[1] == "ingest":
        ingest(sys.argv[2:])
    elif sys.argv[1] == "report":
        report()
