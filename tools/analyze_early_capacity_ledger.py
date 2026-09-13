#!/usr/bin/env python3
"""Stage-ordered strong/weak analysis of the frozen early-capacity ledger."""
from __future__ import annotations
import argparse, collections, json, math, statistics
from pathlib import Path

ITEMS = ("STRAWBERRY", "WHEAT", "MELON", "CARROT", "TOMATO", "COW", "SHEEP", "GOOSE")
ANIMALS = {"COW", "SHEEP", "GOOSE"}
STAGES = ("opportunity_hours", "selected_units", "submitted_units", "committed_units",
          "capacity_created", "survived_to_day10", "productive_occupancy_days",
          "service_successes", "yield_realized", "removed_or_lost")

def mean(xs): return statistics.fmean(xs) if xs else 0.0
def variance(xs): return statistics.variance(xs) if len(xs) > 1 else 0.0
def effect(a, b):
    va, vb = variance(a), variance(b); na, nb = len(a), len(b)
    se = math.sqrt(va/na + vb/nb) if na and nb else 0
    pooled = math.sqrt(((na-1)*va+(nb-1)*vb)/(na+nb-2)) if na+nb > 2 else 0
    return {"strong": mean(a), "weak": mean(b), "difference": mean(a)-mean(b),
            "welch_t": (mean(a)-mean(b))/se if se else 0,
            "cohen_d": (mean(a)-mean(b))/pooled if pooled else 0}

def qty(orders, item, op):
    total = 0
    for o in orders or []:
        if isinstance(o, list) and len(o) >= 2 and o[0] == op and o[1] == item:
            total += int(o[2]) if len(o) >= 3 else 1
    return total

def game_metrics(path):
    result = {item: collections.Counter() for item in ITEMS}
    created = collections.defaultdict(dict)
    harvest = collections.Counter()
    last_state = {}
    for line in path.open():
        x = json.loads(line); ev=x["event"]; day=int(x.get("day",0))
        if ev == "decision":
            for item in ITEMS:
                if x.get("opportunities",{}).get(item,{}).get("available"):
                    result[item]["opportunity_hours"] += 1
            action=x.get("submitted_action",{}); orders=action.get("market",[]) if isinstance(action,dict) else []
            for item in ITEMS:
                result[item]["submitted_units"] += qty(orders,item,"BUY_ANIMAL" if item in ANIMALS else "BUY_SEED")
        elif ev == "internal_selection":
            for item in ITEMS:
                cat="ANIMALS" if item in ANIMALS else "SEEDS"
                orders=x.get("selected",{}).get(cat,{}).get("orders",[])
                result[item]["selected_units"] += qty(orders,item,"BUY_ANIMAL" if item in ANIMALS else "BUY_SEED")
        elif ev == "market_commit" and x.get("committed") and x.get("item") in result:
            if x.get("operation") == ("BUY_ANIMAL" if x["item"] in ANIMALS else "BUY_SEED"):
                result[x["item"]]["committed_units"] += 1
        elif ev == "asset_created" and x.get("item") in result:
            item=x["item"]; aid=x["asset_kind"]+":"+str(x.get("position"))+":"+str(x.get("origin_day"))
            result[item]["capacity_created"] += 1; created[item][aid]=day
        elif ev == "asset_daily_state" and x.get("item") in result:
            item=x["item"]; aid=x["asset_kind"]+":"+str(x.get("position"))+":"+str(x.get("origin_day"))
            result[item]["productive_occupancy_days"] += 1
            last_state[(item,aid)] = x
        elif ev == "unit_action":
            action=x.get("action",[]); tile=x.get("tile_before") or x.get("tile_after") or {}
            item=tile.get("animal") or tile.get("crop")
            if item in result and x.get("success"):
                if action and action[0] in ({"FEED","CARE"} if item in ANIMALS else {"WATER"}):
                    result[item]["service_successes"] += 1
                if action and action[0] == "HARVEST":
                    before=x.get("inventory_before",{}); after=x.get("inventory_after",{})
                    product={"COW":"MILK","SHEEP":"WOOL","GOOSE":"EGG"}.get(item,item)
                    harvest[item] += max(0,after.get(product,0)-before.get(product,0))
        elif ev == "asset_removed" and x.get("item") in result:
            result[x["item"]]["removed_or_lost"] += 1
    for (item, aid), x in last_state.items():
        if int(x.get("day",0)) == 10: result[item]["survived_to_day10"] += 1
    for item in ITEMS:
        result[item]["yield_realized"] = harvest[item] + sum(
            x.get("yield_units",0) for (it,_),x in last_state.items() if it==item)
    return result

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--panel-summary",required=True); ap.add_argument("--ledger-dir",required=True); ap.add_argument("--out")
    a=ap.parse_args(); summary=json.load(open(a.panel_summary)); games=[]
    for row in summary.get("rows", summary.get("games", [])):
        opp,seed,seat=row["opponent"],int(row["seed"]),int(row["seat"])
        if "margin" in row:
            margin=float(row["margin"])
        else:
            money=row["observed"]["money"]; margin=money[seat]-money[1-seat]
        p=Path(a.ledger_dir)/f"{opp}_seat{seat}_seed{seed}.jsonl"
        games.append({"opponent":opp,"seed":seed,"seat":seat,"margin":margin,"metrics":game_metrics(p)})
    # Outcome residual within opponent x seat; extreme quartiles are strong/weak.
    cells=collections.defaultdict(list)
    for g in games: cells[(g["opponent"],g["seat"])].append(g["margin"])
    for g in games: g["residual"]=g["margin"]-mean(cells[(g["opponent"],g["seat"])])
    ordered=sorted(games,key=lambda g:g["residual"]); n=len(games)//4
    weak,strong=ordered[:n],ordered[-n:]
    output={"games":len(games),"strong_n":n,"weak_n":n,"definition":"top/bottom quartile opponent-seat demeaned final margin","items":{}}
    for item in ITEMS:
        output["items"][item]={}
        for stage in STAGES:
            e=effect([g["metrics"][item][stage] for g in strong],[g["metrics"][item][stage] for g in weak])
            signs=[]
            for key,vals in [("opponent",sorted(set(g["opponent"] for g in games))),("seat",[0,1]),("seed_half",[0,1])]:
                ds=[]
                for val in vals:
                    filt=lambda g: (g["opponent"]==val if key=="opponent" else g["seat"]==val if key=="seat" else (g["seed"]<=320)==(val==0))
                    sa=[g["metrics"][item][stage] for g in strong if filt(g)]; wa=[g["metrics"][item][stage] for g in weak if filt(g)]
                    ds.append(mean(sa)-mean(wa) if sa and wa else 0)
                signs.append({"split":key,"differences":ds})
            direction=1 if e["difference"]>0 else -1 if e["difference"]<0 else 0
            robust=abs(e["welch_t"])>=2 and direction and all(all((d*direction)>0 for d in s["differences"]) for s in signs)
            output["items"][item][stage]={**e,"robust":bool(robust),"robustness":signs}
        first=next((s for s in STAGES if output["items"][item][s]["robust"]),None)
        output["items"][item]["first_reproducible_divergence"]=first
    text=json.dumps(output,indent=2); print(text)
    if a.out: Path(a.out).write_text(text+"\n")
if __name__=="__main__": main()
