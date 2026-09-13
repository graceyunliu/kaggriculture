#!/usr/bin/env python3
"""Read-only smoke/panel driver for formation of O42's perceived animal collection."""
from __future__ import annotations
import argparse, copy, gzip, hashlib, json
from pathlib import Path
import o42_decision_provenance as base

ENGINE=base.ROOT/"vendor/kaggle_environments_engine_master/kaggriculture.py"
RELEVANT=("animal","placed_day","fed_today","cared_today","consecutive_unfed","fertilizer_available","yield_units","pending_care_bonus")
def animals(farm):
 out={}
 for y,row in enumerate(farm["tiles"]):
  for x,t in enumerate(row):
   if isinstance(t,dict) and "animal" in t:out[(x,y)]={k:t.get(k) for k in RELEVANT}
 return out
def engine_manifest():
 src=ENGINE.read_text().splitlines();specs=[
  ("animal_purchase_commit","_commit_unit",'if op == "BUY_ANIMAL":'),
  ("animal_place_guard","_apply_unit_action",'if op == "PLACE":'),
  ("animal_place_mutation","_apply_unit_action",'farm["tiles"][fy][fx] = _new_animal(item, day)'),
  ("animal_escape_guard","_daily_refresh_animals",'if tile["consecutive_unfed"] >= 2:'),
  ("animal_escape_mutation","_daily_refresh_animals",'farm["tiles"][y][x] = {"kind": ANIMALS[tile["animal"]]["structure"]}'),]
 import ast
 tree=ast.parse("\n".join(src));funcs={n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)};rows=[]
 for event,fn,text in specs:
  f=funcs[fn];hits=[n for n in ast.walk(f) if hasattr(n,"lineno") and src[n.lineno-1].strip()==text]
  lines=sorted({n.lineno for n in hits})
  if len(lines)!=1:raise RuntimeError(f"engine anchor {event} expected one structural source line, got {lines}")
  ln=lines[0];ctx=src[max(0,ln-3):min(len(src),ln+2)]
  rows.append({"event":event,"intended_function":fn,"resolved_line":ln,"exact_source_text":text,"context":ctx,"context_sha256":hashlib.sha256("\n".join(ctx).encode()).hexdigest(),"structural_node_types":sorted({type(n).__name__ for n in hits}),"uniqueness_status":"unique_source_line"})
 return rows

class Ledger:
 def __init__(self,eng,seat,farms,prov):
  self.eng=eng;self.seat=seat;self.farms=farms;self.prov=prov;self.events=[];self.step=0;self.day=0;self.hour=0;self.epoch=0;self.ids={};self.last={};self.placements=[];self.escapes=[]
  self.oc=eng._commit_unit;self.oa=eng._apply_unit_action;self.orf=eng._daily_refresh_animals
 def emit(self,event,**kw):self.events.append({"seq":10**9+len(self.events),"event":event,"day":self.day,"hour":self.hour,"step":self.step,**base.clean(kw)})
 def own(self,farm):return bool(self.farms[0] and farm is self.farms[0][self.seat])
 def install(self):
  L=self
  def commit(op,item,price,farm,private,market,shed_capacity=100):
   before=(farm.get("money"),private.get("shed",{}).get(item,0));ok=L.oc(op,item,price,farm,private,market,shed_capacity)
   if L.own(farm) and op=="BUY_ANIMAL":L.emit("animal_purchase",species=item,committed=bool(ok),before=before,after=(farm.get("money"),private.get("shed",{}).get(item,0)))
   return ok
  def apply(farm,private,idx,action,board_size,day,turns_per_day,shed_capacity=100):
   raw_pos=L.eng._farmer_position(farm,idx)
   if raw_pos is None:
    L.oa(farm,private,idx,action,board_size,day,turns_per_day,shed_capacity);return
   pos=tuple(raw_pos);bt=copy.deepcopy(farm["tiles"][pos[1]][pos[0]]);bi=copy.deepcopy(private["inventories"][idx]);L.oa(farm,private,idx,action,board_size,day,turns_per_day,shed_capacity);at=copy.deepcopy(farm["tiles"][pos[1]][pos[0]]);ai=copy.deepcopy(private["inventories"][idx])
   if L.own(farm) and isinstance(action,list) and len(action)>=2 and action[0] in {"PICKUP","PLACE"} and action[1] in {"COW","SHEEP","GOOSE"}:
    success=bt!=at or bi!=ai;L.emit("animal_unit_action",unit=idx,position=pos,action=action,success=success,tile_before=bt,tile_after=at,inventory_before=bi,inventory_after=ai)
    if action[0]=="PLACE" and success:L.placements.append((pos,at))
  def refresh(farm,day):
   before=animals(farm);L.orf(farm,day);after=animals(farm)
   if L.own(farm):
    for pos in sorted(set(before)-set(after)):L.emit("animal_escape",position=pos,animal_before=before[pos],post_tile=farm["tiles"][pos[1]][pos[0]]);L.escapes.append((pos,before[pos]))
  self.eng._commit_unit=commit;self.eng._apply_unit_action=apply;self.eng._daily_refresh_animals=refresh
 def restore(self):self.eng._commit_unit=self.oc;self.eng._apply_unit_action=self.oa;self.eng._daily_refresh_animals=self.orf
 def observe(self,farm):
  cur=animals(farm);added=set(cur)-set(self.last);removed=set(self.last)-set(cur)
  for pos in sorted(added):
   self.epoch+=1;aid=f"p{self.seat}:x{pos[0]}y{pos[1]}:d{cur[pos]['placed_day']}:e{self.epoch}";self.ids[pos]=aid;self.emit("animal_entered_farm_tiles",asset_id=aid,position=pos,state=cur[pos],origin="placed" if any(p==pos for p,_ in self.placements) else "unresolved")
  for pos in sorted(set(cur)&set(self.last)):
   changed={k:{"before":self.last[pos].get(k),"after":cur[pos].get(k)} for k in RELEVANT if self.last[pos].get(k)!=cur[pos].get(k)}
   if changed:self.emit("animal_state_transition",asset_id=self.ids.get(pos),position=pos,changes=changed)
  for pos in sorted(removed):self.emit("animal_left_farm_tiles",asset_id=self.ids.pop(pos,None),position=pos,state=self.last[pos],cause="escape" if any(p==pos for p,_ in self.escapes) else "unresolved")
  self.emit("farm_animal_snapshot",size_before=len(self.last),size_after=len(cur),animals=[{"asset_id":self.ids.get(p),"position":p,**t} for p,t in sorted(cur.items())]);self.last=cur;self.placements.clear();self.escapes.clear()

def run(opponent,seed,seat,instrumented,out=None):
 eng,defaults=base.me.load_engine("master");cfg=dict(defaults);cfg["seed"]=None;env=base.me._Env(cfg,seed);cm=base.load(base.O42,f"fc{seed}{seat}{instrumented}");om=base.load(base.OPPS[opponent],f"fo{seed}{seat}{instrumented}");agents=[None,None];agents[seat]=cm.agent;agents[1-seat]=om.agent
 state=base.me.structify([{"observation":{"player":i,"remainingOverageTime":60,"step":0},"action":{},"reward":0.0,"status":"ACTIVE","info":{}} for i in range(2)]);state=eng.interpreter(state,env);farms=[[state[i].observation.farms[i] for i in range(2)]];prov=base.Provenance(cm,formation_only=True) if instrumented else None;led=Ledger(eng,seat,farms,prov) if instrumented else None
 if led:led.install();led.observe(state[seat].observation.farms[seat])
 actions=[];step=0;errors=0
 try:
  while True:
   aa=[]
   for i in (0,1):
    obs=base.me._fast_copy(state[i].observation);obs["step"]=step
    try:a=prov.call(agents[i],obs,base.me._fast_copy(env.configuration)) if prov and i==seat else agents[i](obs,base.me._fast_copy(env.configuration))
    except Exception:a={};errors+=1
    state[i].action=a;aa.append(base.clean(a))
   actions.append(aa);state=eng.interpreter(state,env);step+=1
   for s in state:s.observation.step=step
   farms[0]=[state[i].observation.farms[i] for i in range(2)]
   if led:led.step=step;led.day=int(state[seat].observation.get("day",0));led.hour=int(state[seat].observation.get("hour",0));led.observe(state[seat].observation.farms[seat])
   if all(s.status=="DONE" for s in state) or step>=int(cfg["episodeSteps"]):break
 finally:
  if led:led.restore()
 res={"money":[state[i].observation.farms[i]["money"] for i in range(2)],"steps":step,"errors":errors,"actions_sha256":base.digest(actions),"terminal_sha256":base.digest([base.clean(state[i].observation) for i in range(2)])}
 if led and out:
  unresolved=sum(e["event"] in {"animal_entered_farm_tiles","animal_left_farm_tiles"} and e.get("origin",e.get("cause"))=="unresolved" for e in led.events);res["lifecycle_validation"]={"unresolved_entries_or_exits":unresolved,"persistent_ids_unique":len({e.get("asset_id") for e in led.events if e.get("event")=="animal_entered_farm_tiles"})==sum(e.get("event")=="animal_entered_farm_tiles" for e in led.events)}
  with gzip.open(out,"wt") as f:
   for e in sorted(prov.events+led.events,key=lambda x:(x.get("step",-1),x.get("seq",0))):f.write(json.dumps(e,sort_keys=True)+"\n")
 return res

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--smoke",action="store_true");ap.add_argument("--seeds",default="303-303");ap.add_argument("--opponents",default="peter");ap.add_argument("--out-dir",required=True);a=ap.parse_args();lo,hi=map(int,a.seeds.split("-"));rows=[];Path(a.out_dir).mkdir(parents=True,exist_ok=True)
 for o in a.opponents.split(","):
  for seed in range(lo,hi+1):
   for seat in (0,1):
    log=Path(a.out_dir)/f"{o}_seat{seat}_seed{seed}.jsonl.gz";x=run(o,seed,seat,True,log);b=run(o,seed,seat,False);keys=("money","steps","errors","actions_sha256","terminal_sha256");parity=all(x[k]==b[k] for k in keys);rows.append({"opponent":o,"seed":seed,"seat":seat,"parity":parity,"instrumented":x,"baseline":b,"log":str(log)})
    if not parity or x["lifecycle_validation"]["unresolved_entries_or_exits"]:raise SystemExit(json.dumps(rows[-1],indent=2))
 manifest={"o42":base.Provenance(base.load(base.O42,"formation_manifest"),formation_only=True).manifest,"engine":engine_manifest()};(Path(a.out_dir)/"anchor_binding_manifest.json").write_text(json.dumps(manifest,indent=2));summary={"games":len(rows),"parity_passed":all(r["parity"] for r in rows),"lifecycle_conservation_passed":all(not r["instrumented"]["lifecycle_validation"]["unresolved_entries_or_exits"] for r in rows),"o42_sha256":hashlib.sha256(base.O42.read_bytes()).hexdigest(),"persistent_id_scope":"post-placement surrogate only; engine exposes no native pre-placement animal ID","rows":rows};(Path(a.out_dir)/"smoke_summary.json").write_text(json.dumps(summary,indent=2));print(json.dumps({k:summary[k] for k in ("games","parity_passed","lifecycle_conservation_passed","o42_sha256","persistent_id_scope")},indent=2))
if __name__=="__main__":main()
