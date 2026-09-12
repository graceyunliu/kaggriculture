#!/usr/bin/env python3
"""Execution provenance for O42's five genuine discretionary decision families.

No decision logic is duplicated. Python's execution tracer observes locals only at
AST-structural anchors actually reached by the untouched O42 module. Engine commit
events are recorded separately. Anchor resolution is fail-closed.
"""
from __future__ import annotations
import argparse, ast, gzip, hashlib, importlib.util, json, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT))
import mini_engine as me

O42=ROOT/"candidates/O42_MAX_HANDS_LATE_EXPAND.py"
OPPS={"peter":ROOT/"Opponents/tape_peterparker_106816877.py","alaylm":ROOT/"Opponents/tape_alaylm_106813359.py","bahaen":ROOT/"Opponents/tape_bahaenes_106828159.py","yangk":ROOT/"Opponents/tape_yangkuang2_106819729.py"}

def A(event, text, *, node=None, parent_test=None):
 return {"event":event,"text":text,"node":node,"parent_test":parent_test}

ANCHORS={
 "economy":[
  A("seed_candidate_reached",'if c in excluded or day > sp_["cutoff"] or day < sp_.get("start", 0):',node="If"),
  A("seed_reject_eligibility",'continue',node="Continue",parent_test='c in excluded or day > sp_["cutoff"] or day < sp_.get("start", 0)'),A("seed_strawberry_delay_guard",'if c == "STRAWBERRY" and day < KNOBS["straw_delay"]:',node="If"),
  A("seed_reject_strawberry_delay",'continue',node="Continue",parent_test='c == "STRAWBERRY" and day < KNOBS["straw_delay"]'),A("seed_sell_horizon",'T_sell = max(0, 29 - day - sp_["first"])',node="Assign"),
  A("seed_reject_sell_horizon",'continue',node="Continue",parent_test="T_sell <= 0"),A("seed_demand_room",'room_units = pool - committed[c] - seed_orders.get(c, 0) * sp_["units"]',node="Assign"),
  A("seed_room_guard",'if room_units < sp_["units"] * 0.5:',node="If"),A("seed_reject_room",'continue',node="Continue",parent_test='room_units < sp_["units"] * 0.5'),
  A("seed_value",'val = min(sp_["units"], room_units) * price / sp_["cycle"]',node="Assign"),
  A("seed_min_value_guard",'if val < sp_["min_val"]:',node="If"),A("seed_reject_min_value",'continue',node="Continue",parent_test='val < sp_["min_val"]'),
  A("seed_best_update_guard",'if best is None or val > best[0]:',node="If"),A("seed_best_updated",'best = (val, c, room_units)',node="Assign"),
  A("seed_no_best",'if best is None:',node="If"),A("seed_best_selected",'_val, c, room_units = best',node="Assign"),
  A("seed_initial_quantity",'k = min(space, int(room_units // CROP_SPECS[c]["units"]), int(free // CROP_SPECS[c]["seed"]), 20)',node="Assign"),
  A("seed_labor_reduction",'k -= 1',node="AugAssign",parent_test='k > 0 and _load_model(v, seeds_on_hand + k, n_total, pending_place, day) >= _max_hands_for_day(day)'),
  A("seed_reject_zero_quantity",'excluded.add(c)',node="Expr",parent_test="k <= 0"),
  A("seed_order_recorded",'seed_orders[c] = seed_orders.get(c, 0) + k',node="Assign"),
 ],
 "_orchestrate":[A("orch_tasks_built",'free = [j for j in range(len(positions)) if j not in busy]',node="Assign"),
  A("orch_empty_guard",'if not free or not tasks:',node="If"),
  A("orch_reject_no_fertilizer",'continue',node="Continue",parent_test='kind == "fert" and carry.get("FERTILIZER", 0) <= 0'),A("orch_reject_no_seed",'continue',node="Continue",parent_test='kind == "plant" and not any((seeds_left.get(c, 0) > 0 for c in CROP_SPECS))'),
  A("orch_reject_unreachable",'continue',node="Continue",parent_test="d + 1 > 24 - hour"),A("orch_pair_feasible",'pairs.append((cost, j, ti))',node="Expr"),
  A("orch_reject_collision",'continue',node="Continue",parent_test="j in assigned or ti in used_t"),
  A("orch_assignment",'assigned[j] = tasks[ti]; used_t.add(ti)',node="Assign")],
 "_build_route":[A("route_claims_built",'cands = [(p2, t) for p2, t in v["animals"] if p2 not in claimed and _animal_pending(t, day)]',node="Assign"),
  A("route_candidates_built",'if EG["work_filter"] and day == 29:',node="If"),
  A("route_nearest_choice",'nxt = _nearest(cur, list(pool.keys()))',node="Assign"),A("route_stop_selected",'stops.append(nxt)',node="Expr")],
 "_pick_site":[A("site_pasture_candidates",'c = [s_ for s_ in v["empty_pastures"] if s_ not in S["claimed_sites"]]',node="Assign"),
  A("site_select_pasture",'return min(c, key=_shed_dist)',node="Return"),A("site_empty_candidates",'c = [s_ for s_ in v["empty"] if s_ not in S["claimed_sites"] and s_ not in SHED_TILES]',node="Assign"),
  A("site_no_candidate",'return None',node="Return",parent_test="not c"),A("site_select_empty",'return min(c, key=lambda s_: (_shed_dist(s_), s_))',node="Return")],
 "_steal_task":[A("steal_urgent_candidate",'for idx, (tp, kind) in enumerate(sw):',node="For"),A("steal_urgent_late",'if kind == "urgent" and eta > remaining:',node="If"),
  A("steal_urgent_feasible",'if mine <= remaining and (best is None or mine < best[0]):',node="If"),A("steal_urgent_best",'best = (mine, j, idx)',node="Assign"),
  A("steal_general_candidate",'tp, kind = sw[idx]',node="Assign"),A("steal_reject_time",'continue',node="Continue",parent_test="mine > remaining"),A("steal_general_score",'key = (0 if kind == "urgent" else 1, mine, -len(sw))',node="Assign"),
  A("steal_general_best",'best = (key, j, idx)',node="Assign"),A("steal_transfer",'task = S["sweep"][j].pop(idx)',node="Assign")],
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

def expr_shape(text):
 return ast.dump(ast.parse(text,mode="eval").body,include_attributes=False)

def enclosing_control(node,parents):
 cur=parents.get(node)
 while cur is not None:
  if isinstance(cur,(ast.If,ast.While)):return cur
  cur=parents.get(cur)
 return None

class Provenance:
 def __init__(self,mod):
  self.mod=mod;self.file=str(O42.resolve());self.events=[];self.context={};self.lines={};self.stack=[];self.seq=0;self.manifest=[]
  source=O42.read_text().splitlines();self.source=source;tree=ast.parse("\n".join(source),filename=self.file)
  parents={child:parent for parent in ast.walk(tree) for child in ast.iter_child_nodes(parent)}
  funcs={n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
  for fn,specs in ANCHORS.items():
   if fn not in funcs:raise RuntimeError(f"missing provenance function {fn}")
   fnode=funcs[fn]
   for spec in specs:
    matches=[]
    for node in ast.walk(fnode):
     if type(node).__name__!=spec["node"] or not hasattr(node,"lineno"):continue
     if source[node.lineno-1].strip()!=spec["text"]:continue
     control=enclosing_control(node,parents)
     actual_parent=ast.unparse(control.test) if control is not None else None
     if spec["parent_test"] is not None and (control is None or expr_shape(actual_parent)!=expr_shape(spec["parent_test"])):continue
     matches.append((node,control,actual_parent))
    if len(matches)!=1:
     raise RuntimeError(f"ambiguous provenance anchor {fn}:{spec['event']}: expected 1 structural match, got {len(matches)}")
    node,control,actual_parent=matches[0];ln=node.lineno;key=(fn,ln)
    if key in self.lines:raise RuntimeError(f"duplicate provenance line binding {fn}:{ln}: {self.lines[key]} and {spec['event']}")
    self.lines[key]=spec["event"]
    lo=max(1,ln-2);hi=min(len(source),ln+2);context=[{"line":i,"text":source[i-1]} for i in range(lo,hi+1)]
    nonblank_before=next((source[i-1].strip() for i in range(ln-1,0,-1) if source[i-1].strip()),None)
    nonblank_after=next((source[i-1].strip() for i in range(ln+1,len(source)+1) if source[i-1].strip()),None)
    textual_matches=[i for i in range(fnode.lineno,fnode.end_lineno+1) if source[i-1].strip()==spec["text"]]
    self.manifest.append({"event":spec["event"],"intended_function":fn,"resolved_line":ln,"exact_source_text":source[ln-1].strip(),"ast_node":type(node).__name__,"enclosing_control":actual_parent,"expected_enclosing_control":spec["parent_test"],"predecessor_nonblank":nonblank_before,"successor_nonblank":nonblank_after,"surrounding_context":context,"context_sha256":hashlib.sha256("\n".join(x["text"] for x in context).encode()).hexdigest(),"textual_match_lines":textual_matches,"structural_match_count":len(matches),"uniqueness_status":"unique"})
  self.manifest.extend([{"event":e,"intended_function":None,"resolved_line":None,"exact_source_text":None,"surrounding_context":None,"context_sha256":None,"uniqueness_status":"synthetic_not_source_anchored"} for e in ("function_enter","function_return","engine_commit")])
  self._validate_repaired_seed_bindings()
 def _validate_repaired_seed_bindings(self):
  by_event={m["event"]:m for m in self.manifest}
  labor=by_event["seed_labor_reduction"];zero=by_event["seed_reject_zero_quantity"]
  if labor["ast_node"]!="AugAssign" or expr_shape(labor["enclosing_control"])!=expr_shape('k > 0 and _load_model(v, seeds_on_hand + k, n_total, pending_place, day) >= _max_hands_for_day(day)'):
   raise RuntimeError("semantic anchor failure: seed_labor_reduction is not the seed load-model while-body decrement")
  if zero["ast_node"]!="Expr" or expr_shape(zero["enclosing_control"])!=expr_shape("k <= 0") or zero["successor_nonblank"]!="continue":
   raise RuntimeError("semantic anchor failure: seed_reject_zero_quantity is not excluded.add(c) under if k <= 0 immediately before continue")
 def emit(self,event,fn,frame,**extra):
  self.seq+=1
  if event=="seed_labor_reduction":
   loc=frame.f_locals
   if not (loc.get("k",0)>0 and self.mod._load_model(loc["v"],loc["seeds_on_hand"]+loc["k"],loc["n_total"],loc["pending_place"],loc["day"])>=self.mod._max_hands_for_day(loc["day"])):
    raise RuntimeError("runtime semantic failure: seed_labor_reduction guard is false")
  if event=="seed_reject_zero_quantity" and frame.f_locals.get("k",1)>0:
   raise RuntimeError("runtime semantic failure: seed_reject_zero_quantity observed with k > 0")
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
  opener=gzip.open if str(log).endswith(".gz") else open
  with opener(log,"wt") as f:
   for e in sorted(prov.events+events,key=lambda x:(x.get("day",-1),x.get("hour",-1),x.get("seq",10**9))):f.write(json.dumps(e,sort_keys=True)+"\n")
  res["events"]=len(prov.events)+len(events);res["semantic_event_counts"]={name:sum(e.get("event")==name for e in prov.events) for name in ("seed_labor_reduction","seed_reject_zero_quantity")}
 return res

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--smoke",action="store_true");ap.add_argument("--seeds",default="301-301");ap.add_argument("--opponents",default="peter,alaylm,bahaen,yangk");ap.add_argument("--out-dir",required=True);a=ap.parse_args();lo,hi=map(int,a.seeds.split("-"));rows=[]
 for o in a.opponents.split(","):
  for seed in range(lo,hi+1):
   for seat in (0,1):
    log=Path(a.out_dir)/f"{o}_seat{seat}_seed{seed}.jsonl.gz";observed=run(o,seed,seat,True,log);baseline=run(o,seed,seat,False);keys=("money","steps","errors","actions_sha256","terminal_sha256");parity=all(observed[k]==baseline[k] for k in keys);rows.append({"opponent":o,"seed":seed,"seat":seat,"parity":parity,"observed":observed,"baseline":baseline,"log":str(log)})
    if not parity:raise SystemExit(json.dumps(rows[-1],indent=2))
 manifest=Provenance(load(O42,"manifest")).manifest
 semantic_counts={name:sum(r["observed"]["semantic_event_counts"][name] for r in rows) for name in ("seed_labor_reduction","seed_reject_zero_quantity")}
 by_event={m["event"]:m for m in manifest};labor=by_event["seed_labor_reduction"];zero=by_event["seed_reject_zero_quantity"]
 if len(labor["textual_match_lines"])<2 or len(zero["textual_match_lines"])<2:raise SystemExit("semantic misbinding regression fixture no longer contains repeated generic statements")
 regression={"seed_labor_reduction_legacy_first_text_line":labor["textual_match_lines"][0],"seed_labor_reduction_structural_line":labor["resolved_line"],"seed_reject_zero_quantity_legacy_second_text_line":zero["textual_match_lines"][1],"seed_reject_zero_quantity_structural_line":zero["resolved_line"]}
 semantic_passed=(len(labor["textual_match_lines"])>1 and labor["resolved_line"]!=labor["textual_match_lines"][0] and len(zero["textual_match_lines"])>1 and zero["resolved_line"]!=zero["textual_match_lines"][1])
 if a.smoke and not semantic_passed:raise SystemExit(f"semantic misbinding regression failed: {regression}")
 summary={"trace_source":str(Path(__file__).resolve()),"o42_source":str(O42.resolve()),"o42_sha256":hashlib.sha256(O42.read_bytes()).hexdigest(),"criteria":["money","steps","errors","actions_sha256","terminal_sha256"],"semantic_binding_criteria":["AST node type","unique structural match inside intended function","expected enclosing guard for branch-body anchors","legacy ordinal resolutions demonstrably differ from intended structural resolutions","runtime predicate assertion whenever either repaired event executes"],"semantic_event_counts":semantic_counts,"semantic_event_runtime_coverage_complete":all(n>0 for n in semantic_counts.values()),"semantic_misbinding_regression":regression,"semantic_binding_smoke_passed":semantic_passed,"games":len(rows),"parity_passed":all(r["parity"] for r in rows),"anchor_bindings_passed":all(m["uniqueness_status"] in {"unique","synthetic_not_source_anchored"} for m in manifest),"rows":rows}
 Path(a.out_dir).mkdir(parents=True,exist_ok=True);(Path(a.out_dir)/"anchor_binding_manifest.json").write_text(json.dumps({"o42_source":str(O42.resolve()),"o42_sha256":summary["o42_sha256"],"bindings":manifest},indent=2));(Path(a.out_dir)/"smoke_summary.json").write_text(json.dumps(summary,indent=2));print(json.dumps({k:summary[k] for k in ("games","parity_passed","anchor_bindings_passed","criteria","semantic_binding_criteria","o42_sha256")},indent=2))
if __name__=="__main__":main()
