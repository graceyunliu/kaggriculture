#!/usr/bin/env python3
"""Pull a submission's ladder episodes (replays + results) and classify opponents.

  python3 pull_ladder.py                  # latest submission
  python3 pull_ladder.py --sub 55977482   # specific submission id
  python3 pull_ladder.py --all            # every submission

Uses the bearer token in .kaggle/access_token. Episode list: EpisodeService/ListEpisodes;
replay JSON: https://www.kaggleusercontent.com/episodes/<id>.json (public GET).
Replays land in Replays/Auto/mine/. Prints one row per game with the opponent's turn-1/2
market fingerprint, whether it matches the 53/48 tape cluster, and local exact-reproduction.
"""
import argparse
import json
import os
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
TOK = (ROOT / ".kaggle" / "access_token").read_text().strip()
H = {"Authorization": f"Bearer {TOK}"}
DEST = ROOT / "Replays" / "Auto" / "mine"


def submissions():
    r = requests.get("https://www.kaggle.com/api/v1/competitions/submissions/list/kaggriculture", headers=H, timeout=60)
    r.raise_for_status()
    return sorted(r.json(), key=lambda s: s["date"], reverse=True)


def episodes(sub_id):
    r = requests.post("https://www.kaggle.com/api/i/competitions.EpisodeService/ListEpisodes",
                      headers=H, json={"submissionId": sub_id}, timeout=60)
    r.raise_for_status()
    j = r.json()
    sub2team = {s["id"]: s["teamId"] for s in j.get("submissions", [])}
    team = {t["id"]: t.get("teamName") for t in j.get("teams", [])}
    out = []
    for e in j["episodes"]:
        ags = e.get("agents", [])
        if len(ags) < 2:
            continue
        seat = next(i for i, a in enumerate(ags) if a["submissionId"] == sub_id)
        me, opp = ags[seat], ags[1 - seat]
        out.append({"ep": e["id"], "time": e["createTime"], "state": e["state"], "seat": seat,
                    "me": me.get("reward"), "opp": opp.get("reward"), "score": me.get("updatedScore"),
                    "opp_name": team.get(sub2team.get(opp["submissionId"]), "?"), "opp_sub": opp["submissionId"]})
    return sorted(out, key=lambda x: x["time"])


def fetch(ep_id):
    DEST.mkdir(parents=True, exist_ok=True)
    p = DEST / f"episode-{ep_id}-replay.json"
    if not p.exists():
        r = requests.get(f"https://www.kaggleusercontent.com/episodes/{ep_id}.json", timeout=180)
        if not r.ok:
            return None
        p.write_bytes(r.content)
    return p


def fingerprint(d, seat):
    def fmt(m):
        return " ".join(f"{x[0][:3]}{'' if len(x) < 3 else x[1][:2] + str(x[2])}" for x in m)
    m1 = d["steps"][1][seat].get("action", {}).get("market", []) if len(d["steps"]) > 1 else []
    m2 = d["steps"][2][seat].get("action", {}).get("market", []) if len(d["steps"]) > 2 else []
    cluster = any(x[0] == "BUY_PRODUCT" and x[1] == "WHEAT" and int(x[2]) >= 25 for x in m1 if len(x) >= 3) and \
        any(x[0] == "SELL" and x[1] == "WHEAT" for x in m2 if len(x) >= 3)
    return fmt(m1) + " | " + fmt(m2), cluster


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sub", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--no-verify", action="store_true")
    a = ap.parse_args()
    subs = submissions()
    if a.sub:
        subs = [s for s in subs if s["ref"] == a.sub]
    elif not a.all:
        subs = subs[:1]
    import replay_verify as rv
    for s in subs:
        eps = episodes(s["ref"])
        done = [e for e in eps if e["state"] == "COMPLETED" and e["me"] is not None]
        real = [e for e in done if e["opp_sub"] != s["ref"]]
        w = sum(e["me"] > e["opp"] for e in real)
        print(f"\n== {s['fileName']} (sub {s['ref']}, score {s['publicScore']}): {len(done)} games, real {w}-{len(real) - w}")
        for e in done:
            p = fetch(e["ep"])
            fp, cluster = ("?", False)
            exact = "?"
            if p:
                d = json.load(open(p))
                fp, cluster = fingerprint(d, 1 - e["seat"])
                if not a.no_verify:
                    exact = rv.verify(str(p))["exact"]
            res = "WIN " if e["me"] > e["opp"] else "LOSS"
            print(f"{e['ep']} s{e['seat']} {res} me ${e['me']:>8,.0f} opp ${e['opp']:>8,.0f} {e['opp_name'][:22]:22s} "
                  f"{'TAPE53' if cluster else '      '} exact={exact} | {fp[:95]}")
        json.dump(eps, open(ROOT / "Replays" / "Auto" / f"ladder_{s['ref']}.json", "w"), indent=1)


if __name__ == "__main__":
    main()
