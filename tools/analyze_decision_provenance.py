#!/usr/bin/env python3
"""Descriptive O42 decision-bottleneck analysis from audited provenance logs."""
from __future__ import annotations
import argparse, collections, gzip, json, math
from pathlib import Path

FAMILIES=("economy","_orchestrate","_build_route","_pick_site","_steal_task")
EVENT_FAMILY={
 "seed_candidate_reached":"seed_ranking","seed_reject_eligibility":"seed_ranking","seed_reject_strawberry_delay":"seed_ranking",
 "seed_reject_sell_horizon":"seed_ranking","seed_reject_room":"seed_ranking","seed_reject_min_value":"seed_ranking",
 "seed_reject_zero_quantity":"seed_ranking","seed_labor_reduction":"seed_ranking","seed_no_best":"seed_ranking",
 "seed_best_selected":"seed_ranking","seed_order_recorded":"seed_ranking",
 "orch_reject_no_fertilizer":"crop_task_orchestration","orch_reject_no_seed":"crop_task_orchestration",
 "orch_reject_unreachable":"crop_task_orchestration","orch_pair_feasible":"crop_task_orchestration",
 "orch_reject_collision":"crop_task_orchestration","orch_assignment":"crop_task_orchestration",
 "route_candidates_built":"animal_route_composition","route_stop_selected":"animal_route_composition",
 "site_pasture_candidates":"site_selection","site_empty_candidates":"site_selection","site_no_candidate":"site_selection",
 "site_select_pasture":"site_selection","site_select_empty":"site_selection",
 "steal_urgent_candidate":"task_stealing","steal_urgent_late":"task_stealing","steal_urgent_feasible":"task_stealing",
 "steal_general_candidate":"task_stealing","steal_reject_time":"task_stealing","steal_general_score":"task_stealing",
 "steal_urgent_best":"task_stealing","steal_general_best":"task_stealing","steal_transfer":"task_stealing",
}
FAMILY_FN={"seed_ranking":"economy","crop_task_orchestration":"_orchestrate","animal_route_composition":"_build_route","site_selection":"_pick_site","task_stealing":"_steal_task"}

def mean(x):return sum(x)/len(x) if x else 0.0
def residualized(rows,key):
 cells=collections.defaultdict(list)
 for r in rows:cells[(r["opponent"],r["seat"])].append(r["metrics"].get(key,0.0))
 cm={k:mean(v) for k,v in cells.items()}
 return [r["metrics"].get(key,0.0)-cm[(r["opponent"],r["seat"])] for r in rows]
def comparison(rows,key):
 vals=residualized(rows,key);a=[v for v,r in zip(vals,rows) if r["label"]=="strong"];b=[v for v,r in zip(vals,rows) if r["label"]=="weak"]
 raw_a=[r["metrics"].get(key,0.0) for r in rows if r["label"]=="strong"];raw_b=[r["metrics"].get(key,0.0) for r in rows if r["label"]=="weak"]
 if len(a)<2 or len(b)<2:return {"n_strong":len(a),"n_weak":len(b),"strong_mean":mean(raw_a),"weak_mean":mean(raw_b),"difference":mean(raw_a)-mean(raw_b),"t":0.0,"p_approx":1.0}
 va=sum((x-mean(a))**2 for x in a)/(len(a)-1);vb=sum((x-mean(b))**2 for x in b)/(len(b)-1);se=math.sqrt(va/len(a)+vb/len(b));t=(mean(a)-mean(b))/se if se else 0.0
 return {"n_strong":len(a),"n_weak":len(b),"strong_mean":mean(raw_a),"weak_mean":mean(raw_b),"difference":mean(raw_a)-mean(raw_b),"residualized_difference":mean(a)-mean(b),"t":t,"p_approx":math.erfc(abs(t)/math.sqrt(2))}

def add(c,key,n=1,day=None):
 c[key]+=n
 if day is not None:c[f"day.{day}.{key}"]+=n
def parse_game(path,meta):
 c=collections.Counter();opener=gzip.open if path.suffix==".gz" else open
 with opener(path,"rt") as f:
  for line in f:
   e=json.loads(line);ev=e.get("event");fam=e.get("family");day=e.get("day");loc=e.get("locals") or {}
   if ev=="function_enter" and fam in FAMILIES:add(c,"invocations."+fam,day=day)
   if ev in EVENT_FAMILY:add(c,"event."+ev,day=day)
   if ev=="function_return" and fam=="_orchestrate":
    add(c,"choice.crop_tasks",len(loc.get("tasks") or []),day);add(c,"choice.crop_free_units",len(loc.get("free") or []),day)
   elif ev=="route_candidates_built":add(c,"choice.route_candidates",len(loc.get("cands") or []),day)
   elif ev in {"site_select_pasture","site_select_empty"}:add(c,"choice.site_candidates",len(loc.get("c") or []),day)
   elif ev=="engine_commit" and e.get("operation") in {"BUY_SEED","BUY_ANIMAL"}:
    stage="committed" if e.get("committed") else "commit_rejected";add(c,f"market.{e['operation'].lower()}.{stage}",day=day)
 for family,fn in FAMILY_FN.items():
  den=(c.get("event.seed_no_best",0) if family=="seed_ranking" else c.get("invocations."+fn,0))
  c[f"rate.{family}.actual_choice_set_per_invocation"]={
   "seed_ranking":c.get("event.seed_candidate_reached",0),"crop_task_orchestration":c.get("choice.crop_tasks",0),
   "animal_route_composition":c.get("choice.route_candidates",0),"site_selection":c.get("choice.site_candidates",0),
   "task_stealing":c.get("event.steal_urgent_candidate",0)+c.get("event.steal_general_candidate",0)}[family]/max(1,den)
 return {**meta,"metrics":dict(c)}

def direction_ok(full,vals):
 sign=1 if full.get("residualized_difference",full["difference"])>0 else -1
 return full["p_approx"]<.05 and all(v.get("residualized_difference",v["difference"])*sign>0 for v in vals if v["n_strong"]>=2)
def bh(items,pfield="p_approx"):
 ranked=sorted(range(len(items)),key=lambda i:items[i][pfield]);q=1.0
 for rank,i in reversed(list(enumerate(ranked,1))):q=min(q,items[i][pfield]*len(items)/rank);items[i]["q_bh"]=q

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--panel-dir",required=True);ap.add_argument("--outcomes",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 games=json.load(open(a.outcomes))["games"];rows=[]
 for g in games:
  p=Path(a.panel_dir)/g["opponent"]/f"{g['opponent']}_seat{g['seat']}_seed{g['seed']}.jsonl.gz"
  if not p.exists():raise SystemExit(f"missing audited provenance log: {p}")
  label="strong" if g["margin"]>0 else "weak" if g["margin"]<0 else "tie"
  if label!="tie":rows.append(parse_game(p,{"opponent":g["opponent"],"seat":g["seat"],"seed":g["seed"],"margin":g["margin"],"label":label}))
 keys=sorted(set().union(*(r["metrics"] for r in rows)))
 basekeys=[k for k in keys if not k.startswith("day.")]
 tests=[]
 opponents=sorted({r["opponent"] for r in rows})
 for key in basekeys:
  full=comparison(rows,key);halves=[comparison([r for r in rows if (r["seed"]<=320)==first],key) for first in (True,False)];loo=[comparison([r for r in rows if r["opponent"]!=o],key) for o in opponents]
  tests.append({"metric":key,"full":full,"seed_halves":{"301_320":halves[0],"321_340":halves[1]},"leave_one_opponent_out":dict(zip(opponents,loo))})
 bh([t["full"] for t in tests])
 for t in tests:
  vals=list(t["seed_halves"].values())+list(t["leave_one_opponent_out"].values());t["replicates_direction"]=direction_ok(t["full"],vals);t["reproducible_divergence"]=bool(t["full"]["q_bh"]<=.05 and t["replicates_direction"])
 # Earliest day uses the same directional replication rule and BH across all metric/day tests.
 daily=[]
 for key in basekeys:
  for day in range(30):
   dk=f"day.{day}.{key}";full=comparison(rows,dk);halves=[comparison([r for r in rows if (r["seed"]<=320)==first],dk) for first in (True,False)];loo=[comparison([r for r in rows if r["opponent"]!=o],dk) for o in opponents]
   daily.append({"metric":key,"day":day,"full":full,"validations":halves+loo})
 bh([d["full"] for d in daily])
 for d in daily:d["reproducible"]=bool(d["full"]["q_bh"]<=.05 and direction_ok(d["full"],d["validations"]))
 earliest={k:min((d["day"] for d in daily if d["metric"]==k and d["reproducible"]),default=None) for k in basekeys}
 totals={k:{"strong_mean":comparison(rows,k)["strong_mean"],"weak_mean":comparison(rows,k)["weak_mean"]} for k in basekeys}
 result={"status":"descriptive_measurement_only","cohort":{"games":len(rows),"strong":sum(r["label"]=="strong" for r in rows),"weak":sum(r["label"]=="weak" for r in rows),"definition":"strong iff final opponent-relative margin > 0; weak iff margin < 0","fixed_shops":True,"seeds":"301-340","seed_halves":["301-320","321-340"]},"method":{"stratification":"metric residualized within opponent x seat before strong/weak comparison","multiplicity":"Benjamini-Hochberg separately over all-game metrics and metric-by-day tests","reproducible":"full-panel q_BH <= 0.05 and same residualized direction in both seed halves and every leave-one-opponent-out check with >=2 strong games","scope_limit":"only candidates and paths emitted by audited O42 provenance; unavailable or untraced stages are explicitly unobserved"},"tests":tests,"earliest_reproducible_day":earliest,"descriptive_means":totals,"stage_observability":{"seed_ranking":{"candidate_unavailable":"unobserved unless an actual reached candidate fires a rejection guard","generated":"seed_candidate_reached","rejected":"seed_reject_* paths","selected":"seed_best_selected","submitted":"seed_order_recorded","committed":"engine_commit BUY_SEED","executed":"not separately observable after engine commit"},"crop_task_orchestration":{"generated":"tasks in real _orchestrate return locals","rejected":"no fertilizer/no seed/unreachable/collision paths","selected":"orch_assignment","submitted":"unobserved","committed":"unobserved","executed":"unobserved"},"animal_route_composition":{"generated":"route_candidates_built locals","selected":"route_stop_selected","submitted":"not applicable to route construction","executed":"unobserved"},"site_selection":{"generated":"real c list at select event","rejected":"site_no_candidate","selected":"site_select_*","executed":"unobserved"},"task_stealing":{"generated":"urgent/general loop candidates reached","rejected":"time guard where observed","selected":"best-update events","submitted":"steal_transfer","executed":"subsequent task action unobserved"}}}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(result,indent=2));print(json.dumps({"cohort":result["cohort"],"reproducible":[{"metric":t["metric"],"full":t["full"],"earliest_day":earliest[t["metric"]]} for t in tests if t["reproducible_divergence"]]},indent=2))
if __name__=="__main__":main()
