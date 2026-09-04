#!/usr/bin/env python3
import argparse,csv,json,sys
from collections import Counter
from pathlib import Path
DAYS=30; PLAYERS=2; KNOWN={'PLANT','COOP','PASTURE','WEED'}
class ReplayError(Exception): pass
def need(v,n):
 if v is None: raise ReplayError('missing '+n)
 return v
def paths(root): return sorted(p for p in root.rglob("*.json") if p.is_file())
def obs(data):
 if not isinstance(data,dict): raise ReplayError('top level is not an object')
 steps=need(data.get('steps'),'steps')
 if not isinstance(steps,list) or len(steps)<DAYS: raise ReplayError('steps is not a list of at least 30 entries')
 out=[]
 for si,step in enumerate(steps):
  if not isinstance(step,list) or len(step)!=PLAYERS: raise ReplayError('step %d does not have 2 players'%si)
  row=[]
  for pi,state in enumerate(step):
   if not isinstance(state,dict) or not isinstance(state.get('observation'),dict): raise ReplayError('step %d player %d missing observation'%(si,pi))
   row.append(state['observation'])
  out.append(row)
 return out
def farm(o,p,si):
 fs=need(o.get('farms'),'farms at step %d'%si)
 if not isinstance(fs,list) or len(fs)!=PLAYERS: raise ReplayError('farms at step %d invalid'%si)
 f=fs[p]
 if not isinstance(f,dict): raise ReplayError('farm invalid at step %d'%si)
 for k in ('tiles','unlocked_quadrants','hands','money'): need(f.get(k),'farm.%s at step %d'%(k,si))
 if not all(isinstance(f[k],list) for k in ('tiles','unlocked_quadrants','hands')): raise ReplayError('farm lists invalid at step %d'%si)
 return f
def counts(f,si,p):
 a=Counter(); c=Counter(); odd=[]
 for y,row in enumerate(f['tiles']):
  if not isinstance(row,list): raise ReplayError('tile row invalid at step %d'%si)
  for x,t in enumerate(row):
   if t is None or t=='LOCKED': continue
   if not isinstance(t,dict): raise ReplayError('invalid tile at %d,%d'% (x,y))
   k=t.get('kind')
   if k not in KNOWN: odd.append('tile kind %r at %d,%d step %d player %d'%(k,x,y,si,p))
   if k=='PLANT':
    crop=t.get('crop')
    if not isinstance(crop,str) or not crop: raise ReplayError('plant missing crop at step %d'%si)
    c[crop]+=1
   if isinstance(t.get('animal'),str) and t['animal']: a[t['animal']]+=1
 return a,c,odd
def extract(path):
 try:
  with path.open(encoding='utf-8') as h: data=json.load(h)
 except (OSError,UnicodeDecodeError,json.JSONDecodeError) as e: raise ReplayError('cannot read JSON: %s'%e)
 oo=obs(data); rec=[[],[]]; ats=set(); cts=set(); odd=[]
 for p in range(PLAYERS):
  placed={d:Counter() for d in range(DAYS)}; seen=set(); latest={}; eod={}
  for si,row in enumerate(oo):
   f=farm(row[p],p,si); day=row[p].get('day')
   if isinstance(day,int) and 0<=day<DAYS:
    latest[day]=(row[p],si)
    if row[p].get('hour') == 0 and day > 0: eod[day-1]=(row[p],si)
   for y,tiles in enumerate(f['tiles']):
    if not isinstance(tiles,list): raise ReplayError('tile row invalid at step %d'%si)
    for x,t in enumerate(tiles):
     if not isinstance(t,dict) or t.get('kind')!='PLANT': continue
     crop,planted=t.get('crop'),t.get('planted_day')
     if not isinstance(crop,str) or not crop: raise ReplayError('plant missing crop at step %d'%si)
     if not isinstance(planted,int) or not 0<=planted<DAYS: raise ReplayError('invalid planted_day at step %d'%si)
     key=(x,y,planted,crop)
     if key not in seen: placed[planted][crop]+=1; seen.add(key)
     cts.add(crop)
   odd.extend(counts(f,si,p)[2])
  for d in range(DAYS):
   if d not in eod and d not in latest: raise ReplayError('no observation for day %d'%d)
   o,si=eod.get(d,latest.get(d)); f=farm(o,p,si); a,c,more=counts(f,si,p); odd.extend(more); ats.update(a); cts.update(c)
   rec[p].append({'day':d,'animals_by_type':dict(sorted(a.items())),'plants_by_crop':dict(sorted(c.items())),'tiles_planted_today':dict(sorted(placed[d].items())),'land_owned':len(f['unlocked_quadrants']),'hands':len(f['hands']),'money':f['money']})
 return rec,ats,cts,sorted(set(odd))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--input',type=Path,default=Path('Replays/Auto')); ap.add_argument('--output',type=Path,default=Path('Opponents/schedules')); a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
 skipped=[]; rows=[]; animals=set(); crops=set(); notes={}; success=0
 for path in paths(a.input):
  try: rec,ats,cts,odd=extract(path)
  except ReplayError as e: skipped.append('%s: %s'%(path,e)); continue
  success+=1; animals.update(ats); crops.update(cts)
  if odd: notes[path.stem]=set(odd)
  for p in range(PLAYERS):
   (a.output/(path.stem+'_p%d.json'%p)).write_text(json.dumps(rec[p],indent=2)+'\n',encoding='utf-8')
   rows.extend({'replay':path.stem,'player':p,**r} for r in rec[p])
 ac=['animals_'+x for x in sorted(animals)]; pc=['plants_'+x for x in sorted(crops)]; tc=['tiles_planted_today_'+x for x in sorted(crops)]; fields=['replay','player','day']+ac+pc+tc+['land_owned','hands','money']
 with (a.output/'summary.csv').open('w',newline='',encoding='utf-8') as h:
  w=csv.DictWriter(h,fieldnames=fields); w.writeheader()
  for r in rows:
   q={k:r.get(k,'') for k in fields}
   for x in animals: q['animals_'+x]=r['animals_by_type'].get(x,0)
   for x in crops: q['plants_'+x]=r['plants_by_crop'].get(x,0); q['tiles_planted_today_'+x]=r['tiles_planted_today'].get(x,0)
   w.writerow(q)
 (a.output/'skipped.txt').write_text('\n'.join(skipped)+('\n' if skipped else ''),encoding='utf-8')
 lines=['# Schedule miner notes','','Processed %d replay(s); skipped %d.'%(success,len(skipped)),'','## Unfamiliar tile kinds']
 lines += ['- `%s`: %s'%(k,'; '.join(sorted(v))) for k,v in sorted(notes.items())] or ['- None observed.']
 (a.output/'notes.md').write_text('\n'.join(lines)+'\n',encoding='utf-8'); print('processed=%d skipped=%d rows=%d outputs=%d'%(success,len(skipped),len(rows),success*PLAYERS))
if __name__=='__main__': sys.exit(main())
