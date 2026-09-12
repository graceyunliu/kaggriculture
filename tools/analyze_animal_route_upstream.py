#!/usr/bin/env python3
"""Measurement-only upstream animal-route provenance analysis."""
from __future__ import annotations
import argparse, collections, gzip, json, math
from pathlib import Path

STAGES=("route_calls","raw_candidates","claimed_removed","pending_evaluated","pending_rejected","post_pending","day29_removed","fallback_added","pre_construction","selected_stops","routes_returned")
HELPER_TERMINALS=("feed_reject_already_fed_or_late","feed_final_decision","care_reject_already_cared","care_due_tomorrow_decision","care_reject_after_horizon","care_reject_bonus_cap","care_reject_too_early","care_accept")
def mean(x):return sum(x)/len(x) if x else 0.0
def add(c,key,n,day):c[key]+=n;c[f"day.{day}.{key}"]+=n
def parse(path,meta):
 c=collections.Counter();stack=[]
 with gzip.open(path,"rt") as f:
  for line in f:
   e=json.loads(line);fn=e.get("family");ev=e.get("event");day=int(e.get("day",-1))
   if fn=="_build_route" and ev=="function_enter":
    raw=e.get("raw_candidates",[]);stack.append({"day":day,"raw":raw});add(c,"route_calls",1,day);add(c,"raw_candidates",len(raw),day)
   elif fn=="_animal_pending" and ev=="function_return":
    d=e["decision"];add(c,"pending_evaluated",1,day);add(c,"pending_accepted" if d["pending"] else "pending_rejected",1,day)
    if d["pending"]:
     for reason,yes in (("feed",d["need_feed"]),("care",d["need_care"]),("fertilizer",d["fertilizer_available"]),("yield",d["yield_units_positive"])):
      if yes:add(c,"pending_accept_reason."+reason,1,day)
    else:add(c,"pending_reject_reason.no_feed_care_fertilizer_or_yield",1,day)
   elif fn in {"_feed_useful","_care_useful"} and ev in HELPER_TERMINALS:
    add(c,"helper_path."+ev,1,day)
   elif fn=="_build_route":
    if not stack:raise RuntimeError(f"route event outside call: {ev}")
    r=stack[-1]
    if ev=="route_claims_built":
     claimed=set(map(tuple,e.get("claimed_positions",[])));n=sum(tuple(x["position"]) in claimed for x in r["raw"]);add(c,"claimed_removed",n,day)
    elif ev=="route_candidates_built":r["post_pending"]=len(e.get("candidates",[]));add(c,"post_pending",r["post_pending"],day)
    elif ev=="route_candidates_after_day29_filter":
     n=len(e.get("candidates",[]));add(c,"day29_removed",r["post_pending"]-n,day);r["post_day29"]=n
    elif ev=="route_candidates_before_construction":
     n=len(e.get("candidates",[]));add(c,"fallback_added",max(0,n-r["post_day29"]),day);add(c,"pre_construction",n,day)
    elif ev=="route_stop_selected":add(c,"selected_stops",1,day)
    elif ev=="function_return":
     if isinstance(e.get("returned"),dict):add(c,"routes_returned",1,day);add(c,"final_route_stops",len(e["returned"].get("stops",[])),day)
     stack.pop()
 if stack:raise RuntimeError("unterminated route call")
 return {**meta,"metrics":dict(c)}

def comparison(rows,key):
 cells=collections.defaultdict(list)
 for r in rows:cells[(r["opponent"],r["seat"])].append(r["metrics"].get(key,0))
 cm={k:mean(v) for k,v in cells.items()};a=[];b=[];ra=[];rb=[]
 for r in rows:
  raw=r["metrics"].get(key,0);res=raw-cm[(r["opponent"],r["seat"])]
  (a if r["label"]=="strong" else b).append(res);(ra if r["label"]=="strong" else rb).append(raw)
 if len(a)<2 or len(b)<2:return {"n_strong":len(a),"n_weak":len(b),"strong_mean":mean(ra),"weak_mean":mean(rb),"residualized_difference":0,"p_approx":1.0}
 va=sum((x-mean(a))**2 for x in a)/(len(a)-1);vb=sum((x-mean(b))**2 for x in b)/(len(b)-1);se=math.sqrt(va/len(a)+vb/len(b));t=(mean(a)-mean(b))/se if se else 0
 return {"n_strong":len(a),"n_weak":len(b),"strong_mean":mean(ra),"weak_mean":mean(rb),"difference":mean(ra)-mean(rb),"residualized_difference":mean(a)-mean(b),"t":t,"p_approx":math.erfc(abs(t)/math.sqrt(2))}
def bh(tests):
 order=sorted(range(len(tests)),key=lambda i:tests[i]["full"]["p_approx"]);q=1.0
 for rank,i in reversed(list(enumerate(order,1))):q=min(q,tests[i]["full"]["p_approx"]*len(tests)/rank);tests[i]["full"]["q_bh"]=q
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--panel-dir",required=True);ap.add_argument("--outcomes",required=True);ap.add_argument("--out",required=True);a=ap.parse_args();games=json.load(open(a.outcomes))["games"];rows=[]
 for g in games:
  p=Path(a.panel_dir)/g["opponent"]/f"{g['opponent']}_seat{g['seat']}_seed{g['seed']}.jsonl.gz"
  if not p.exists():raise SystemExit(f"missing upstream provenance log: {p}")
  rows.append(parse(p,{"opponent":g["opponent"],"seat":g["seat"],"seed":g["seed"],"label":"strong" if g["margin"]>0 else "weak"}))
 keys=list(STAGES)+["pending_accepted","final_route_stops"]+["pending_accept_reason."+x for x in ("feed","care","fertilizer","yield")]+["pending_reject_reason.no_feed_care_fertilizer_or_yield"]+["helper_path."+x for x in HELPER_TERMINALS]
 opponents=sorted({r["opponent"] for r in rows});tests=[]
 for key in keys:
  full=comparison(rows,key);halves={"301_320":comparison([r for r in rows if r["seed"]<=320],key),"321_340":comparison([r for r in rows if r["seed"]>320],key)};loo={o:comparison([r for r in rows if r["opponent"]!=o],key) for o in opponents};tests.append({"metric":key,"full":full,"seed_halves":halves,"leave_one_opponent_out":loo})
 bh(tests)
 for t in tests:
  sign=1 if t["full"]["residualized_difference"]>0 else -1;vals=list(t["seed_halves"].values())+list(t["leave_one_opponent_out"].values());t["direction_replicates"]=all(v["residualized_difference"]*sign>0 for v in vals);t["reproducible"]=t["full"]["q_bh"]<=.05 and t["direction_replicates"]
 daily=[]
 for stage in STAGES:
  for day in range(30):
   key=f"day.{day}.{stage}";full=comparison(rows,key);halves=[comparison([r for r in rows if r["seed"]<=320],key),comparison([r for r in rows if r["seed"]>320],key)];loo=[comparison([r for r in rows if r["opponent"]!=o],key) for o in opponents];daily.append({"stage":stage,"day":day,"full":full,"validation":halves+loo})
 bh(daily)
 for d in daily:
  sign=1 if d["full"]["residualized_difference"]>0 else -1;d["reproducible"]=d["full"]["q_bh"]<=.05 and all(v["residualized_difference"]*sign>0 for v in d["validation"])
 earliest={s:min((d["day"] for d in daily if d["stage"]==s and d["reproducible"]),default=None) for s in STAGES}
 raw=next(t for t in tests if t["metric"]=="raw_candidates");stop=raw["reproducible"]
 result={"status":"stopped_at_upstream_entry" if stop else "filter_attribution_completed","stop_rule_triggered":stop,"stop_reason":"Strong/weak divergence is already reproducible in raw v['animals'] candidates before claim or pending-work filtering." if stop else None,"cohort":{"games":len(rows),"strong":sum(r["label"]=="strong" for r in rows),"weak":sum(r["label"]=="weak" for r in rows),"seeds":"301-340","fixed_shops":True},"method":{"stratification":"opponent x seat residualization","replication":"both reciprocal seed halves and every leave-one-opponent-out direction","multiplicity":"BH-FDR across declared stages/guards and separately across stage-by-day tests"},"tests":tests,"earliest_reproducible_day":earliest}
 Path(a.out).parent.mkdir(parents=True,exist_ok=True);Path(a.out).write_text(json.dumps(result,indent=2));print(json.dumps({"status":result["status"],"stop_reason":result["stop_reason"],"raw":raw,"stages":[{"metric":t["metric"],"strong":t["full"]["strong_mean"],"weak":t["full"]["weak_mean"],"q":t["full"]["q_bh"],"reproducible":t["reproducible"],"earliest":earliest.get(t["metric"])} for t in tests if t["metric"] in STAGES]},indent=2))
if __name__=="__main__":main()
