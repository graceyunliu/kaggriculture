#!/usr/bin/env python3
"""Execution provenance for O42's five genuine discretionary decision families.

No decision logic is duplicated.  Python's execution tracer observes locals only at
source-text anchors actually reached by the untouched O42 module.  Engine commit
events are recorded separately.  Anchor resolution is fail-closed.
"""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, inspect, json, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
import mini_engine as me

O42=ROOT/"candidates/O42_MAX_HANDS_LATE_EXPAND.py"
OPPS={"peter":ROOT/"Opponents/tape_peterparker_106816877.py","alaylm":ROOT/"Opponents/tape_alaylm_106813359.py","bahaen":ROOT/"Opponents/tape_bahaenes_106828159.py","yangk":ROOT/"Opponents/tape_yangkuang2_106819729.py"}

ANCHORS={
 "economy":[
  ("seed_candidate_reached",'if c in excluded or day > sp_["cutoff"] or day < sp_.get("start", 0):',1),
  ("seed_reject_eligibility",'continue',2),("seed_strawberry_delay_guard",'if c == "STRAWBERRY" and day < KNOBS["straw_delay"]:',1),
  ("seed_reject_strawberry_delay",'continue',3),("seed_sell_horizon",'T_sell = max(0, 29 - day - sp_["first"])',1),
  ("seed_reject_sell_horizon",'continue',4),("seed_demand_room",'room_units = pool - committed[c] - seed_orders.get(c, 0) * sp_["units"]',1),
  ("seed_room_guard",'if room_units < sp_["units"] * 0.5:',1),("seed_reject_room",'continue',5),
  ("seed_value",'val = min(sp_["units"], room_units) * price / sp_["cycle"]',1),
  ("seed_min_value_guard",'if val < sp_["min_val"]:',1),("seed_reject_min_value",'continue',6),
  ("seed_best_update_guard",'if best is None or val > best[0]:',1),("seed_best_updated",'best = (val, c, room_units)',1),
  ("seed_no_best",'if best is None:',1),("seed_best_selected",'_val, c, room_units = best',1),
  ("seed_initial_quantity",'k = min(space, int(room_units // CROP_SPECS[c]["units"]), int(free // CROP_SPECS[c]["seed"]), 20)',1),
  ("seed_labor_reduction",'k -= 1',1),("seed_reject_zero_quantity",'excluded.add(c)',2),
  ("seed_order_recorded",'seed_orders[c] = seed_orders.get(c, 0) + k',1),
 ],
 "_orchestrate":[("orch_tasks_built",'free = [j for j in range(len(positions)) if j not in busy]',1),
  ("orch_empty_guard",'if not free or not tasks:',1),
  ("orch_reject_no_fertilizer",'continue',2),("orch_reject_no_seed",'continue',3),
  ("orch_reject_unreachable",'continue',4),("orch_pair_feasible",'pairs.append((cost, j, ti))',1),
  ("orch_reject_collision",'continue',5),
  ("orch_assignment",'assigned[j] = tasks[ti]; used_t.add(ti)',1)],
 "_build_route":[("route_claims_built",'cands = [(p2, t) for p2, t in v["animals"] if p2 not in claimed and _animal_pending(t, day)]',1),
  ("route_candidates_built",'if EG["work_filter"] and day == 29:',1),
  ("route_nearest_choice",'nxt = _nearest(cur, list(pool.keys()))',1),("route_stop_selected",'stops.append(nxt)',1)],
 "_pick_site":[("site_pasture_candidates",'c = [s_ for s_ in v["empty_pastures"] if s_ not in S["claimed_sites"]]',1),
  ("site_select_pasture",'return min(c, key=_shed_dist)',1),("site_empty_candidates",'c = [s_ for s_ in v["empty"] if s_ not in S["claimed_sites"] and s_ not in SHED_TILES]',1),
  ("site_no_candidate",'return None',1),("site_select_empty",'return min(c, key=lambda s_: (_shed_dist(s_), s_))',1)],
 "_steal_task":[("steal_urgent_candidate",'for idx, (tp, kind) in enumerate(sw):',1),("steal_urgent_late",'if kind == "urgent" and eta > remaining:',1),
  ("steal_urgent_feasible",'if mine <= remaining and (best is None or mine < best[0]):',1),("steal_urgent_best",'best = (mine, j, idx)',1),
  ("steal_general_candidate",'tp, kind = sw[idx]',1),("steal_reject_time",'continue',3),("steal_general_score",'key = (0 if kind == "urgent" else 1, mine, -len(sw))',1),
  ("steal_general_best",'best = (key, j, idx)',1),("steal_transfer",'task = S["sweep"][j].pop(idx)',1)],
}
KEEP={"economy":{"day","hour","c","sp_","excluded","T_sell","inv_c","cushion_left","pool","room_units","price","val","best","k","space","free","seed_orders","committed","n_seed_orders","seeds_on_hand"},
 "_orchestrate":{"day","hour","pools","positions","busy","tasks","free","j","ti","tp","kind","carry","d","cost","pairs","assigned","used_t","prev"},
 "_build_route":{"i","pos","day","hour","claimed","cands","best","stops","cur","pool","nxt","unfed","need","pickup"},
 "_pick_site":{"species","c"},"_steal_task":{"i","pos","day","hour","remaining","j","sw","eta","idx","tp","kind","mine","key","best","task"}}
EVENT_KEEP={
 "function_enter":{"day","hour","i","pos","species","pools","positions","busy","seeds_left"},
 "orch_reject_no_fertilizer":{"j","ti","tp","kind"},
 "orch_reject_no_seed":{"j","ti","tp","kind"},
 "orch_reject_unreachable":{"j","ti","tp","kind","d"},"orch_pair_feasible":{"j","ti","tp","kind","d","cost"},
 "orch_reject_collision":{"j","ti","cost"},"orch_assignment":{"j","ti","cost"},
 "route_nearest_choice":{"i","cur","pool","nxt"},"route_stop_selected":{"i","nxt","stops"},
}

def clean(x,depth=0):
 if depth>4:return "<depth-limit>"
 if isinstance(x,dict):return {str(k):clean(v,depth+1) for k,v in list(x.items())[:200]}
 if isinstance(x,(list,tuple,set)):return [clean(v,depth+1) for v in list(x)[:200]]
 if isinstance(x,(str,int,float,bool)) or x is None:return x
 return repr(x)
def digest(x):return hashlib.sha256(json.dumps(clean(x),sort_keys=True,separators=(",",":")).encode()).hexdigest()

class Provenance:
 def __init__(self,mod):
  self.mod=mod;self.file=str(O42.resolve());self.events=[];self.context={};self.lines={};self.stack=[];self.seq=0
  source=O42.read_text().splitlines();self.source=source
  for fn,specs in ANCHORS.items():
   obj=getattr(mod,fn);_,start=inspect.getsourcelines(obj);end=start+len(inspect.getsourcelines(obj)[0])-1
   chunk=[(i+1,source[i]) for i in range(start-1,end)]
   for label,text,nth in specs:
    hits=[ln for ln,s in chunk if text in s]
    if len(hits)<nth:raise RuntimeError(f"missing provenance anchor {fn}:{label}: {text!r}")
    self.lines[(fn,hits[nth-1])]=label
 def emit(self,event,fn,frame,**extra):
  self.seq+=1
  if event=="function_return":
   allowed={"economy":{"day","hour","seed_orders","excluded","space","free"},"_orchestrate":{"day","hour","tasks","free","assigned","used_t"},"_build_route":{"i","day","hour","claimed","cands","stops","unfed","need","pickup"},"_pick_site":{"species","c"},"_steal_task":{"i","day","hour","remaining","best","task"}}.get(fn,set())
  else:allowed=EVENT_KEEP.get(event,KEEP.get(fn,set()))
  loc={k:clean(v) for k,v in frame.f_locals.items() if k in allowed}
  self.events.append({"seq":self.seq,"event":event,"family":fn,"day":self.context.get("day"),"hour":self.context.get("hour"),"line":frame.f_lineno,"code_path":f"{fn}:{frame.f_lineno}","source":self.source[frame.f_lineno-1].strip(),"locals":loc,**clean(extra)})
 def trace(self,frame,event,arg):
  if frame.f_code.co_filename!=self.file:return None
  fn=frame.f_code.co_name
  if fn not in ANCHORS:return self.trace
  if event=="call":self.emit("function_enter",fn,frame)
  elif event=="line" and (fn,frame.f_lineno) in self.lines:self.emit(self.lines[(fn,frame.f_lineno)],fn,frame)
  elif event=="return":self.emit("function_return",fn,frame,returned=clean(arg))
  return self.trace
 def call(self,agent,obs,cfg):
  self.context={"day":obs.get("day"),"hour":obs.get("hour")};old=sys.gettrace();sys.settrace(self.trace)
  try:return agent(obs,cfg)
  finally:sys.settrace(old)

def load(path,tag):
 s=importlib.util.spec_from_file_location(f"prov_{tag}_{os.getpid()}",path);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m

def run(opponent,seed,seat,instrumented,log=None):
 eng,defaults=me.load_engine("master");cfg=dict(defaults);cfg["seed"]=None;env=me._Env(cfg,seed)
 cm=load(O42,f"c{seed}{seat}{instrumented}");om=load(OPPS[opponent],f"o{seed}{seat}{instrumented}");agents=[None,None];agents[seat]=cm.agent;agents[1-seat]=om.agent
 prov=Provenance(cm) if instrumented else None;events=[];farms=[None];orig=eng._commit_unit
 def commit(op,item,price,farm,private,market,shed_capacity=100):
  before=(farm.get("money"),private.get("seeds",{}).get(item,0),private.get("shed",{}).get(item,0));ok=orig(op,item,price,farm,private,market,shed_capacity)
  if prov and farms[0] and farm is farms[0][seat] and op in {"BUY_SEED","BUY_ANIMAL"}:
   prov.seq+=1;events.append({"seq":prov.seq,"event":"engine_commit","day":prov.context.get("day"),"hour":prov.context.get("hour"),"operation":op,"item":item,"price":price,"committed":bool(ok),"before":before,"after":(farm.get("money"),private.get("seeds",{}).get(item,0),private.get("shed",{}).get(item,0))})
  return ok
 if prov:eng._commit_unit=commit
 state=me.structify([{"observation":{"player":i,"remainingOverageTime":60,"step":0},"action":{},"reward":0.0,"status":"ACTIVE","info":{}} for i in range(2)]);state=eng.interpreter(state,env);farms[0]=[state[i].observation.farms[i] for i in range(2)]
 for s in state:s.observation.step=0
 actions=[];step=0;errors=0
 try:
  while True:
   aa=[]
   for i in (0,1):
    obs=me._fast_copy(state[i].observation);obs["step"]=step
    try:a=prov.call(agents[i],obs,me._fast_copy(env.configuration)) if prov and i==seat else agents[i](obs,me._fast_copy(env.configuration))
    except Exception:a={};errors+=1
    state[i].action=a;aa.append(clean(a))
   actions.append(aa);state=eng.interpreter(state,env);step+=1
   for s in state:s.observation.step=step
   farms[0]=[state[i].observation.farms[i] for i in range(2)]
   if all(s.status=="DONE" for s in state) or step>=int(cfg["episodeSteps"]):break
 finally:
  if prov:eng._commit_unit=orig
 terminal=[clean(state[i].observation) for i in range(2)];res={"money":[state[i].observation.farms[i]["money"] for i in range(2)],"steps":step,"errors":errors,"actions_sha256":digest(actions),"terminal_sha256":digest(terminal)}
 if prov and log:
  Path(log).parent.mkdir(parents=True,exist_ok=True)
  with Path(log).open("w") as f:
   for e in sorted(prov.events+events,key=lambda x:(x.get("day",-1),x.get("hour",-1),x.get("seq",10**9))):f.write(json.dumps(e,sort_keys=True)+"\n")
  res["events"]=len(prov.events)+len(events)
 return res

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--smoke",action="store_true");ap.add_argument("--seeds",default="301-301");ap.add_argument("--opponents",default="peter,alaylm,bahaen,yangk");ap.add_argument("--out-dir",required=True);a=ap.parse_args();lo,hi=map(int,a.seeds.split("-"));rows=[]
 for o in a.opponents.split(","):
  for seed in range(lo,hi+1):
   for seat in (0,1):
    log=Path(a.out_dir)/f"{o}_seat{seat}_seed{seed}.jsonl";observed=run(o,seed,seat,True,log);baseline=run(o,seed,seat,False);keys=("money","steps","errors","actions_sha256","terminal_sha256");parity=all(observed[k]==baseline[k] for k in keys);rows.append({"opponent":o,"seed":seed,"seat":seat,"parity":parity,"observed":observed,"baseline":baseline,"log":str(log)})
    if not parity:raise SystemExit(json.dumps(rows[-1],indent=2))
 summary={"trace_source":str(Path(__file__).resolve()),"o42_source":str(O42.resolve()),"o42_sha256":hashlib.sha256(O42.read_bytes()).hexdigest(),"criteria":["money","steps","errors","actions_sha256","terminal_sha256"],"games":len(rows),"parity_passed":all(r["parity"] for r in rows),"rows":rows}
 Path(a.out_dir).mkdir(parents=True,exist_ok=True);(Path(a.out_dir)/"smoke_summary.json").write_text(json.dumps(summary,indent=2));print(json.dumps({k:summary[k] for k in ("games","parity_passed","criteria","o42_sha256")},indent=2))
if __name__=="__main__":main()
