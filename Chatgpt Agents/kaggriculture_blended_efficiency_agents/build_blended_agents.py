from pathlib import Path
import json, re
BASE=Path('/mnt/data/main_v8.3.py').read_text()
OUT=Path('/mnt/data/blended_agents'); OUT.mkdir(exist_ok=True)

def rep(s,o,n,label):
    if o not in s: raise RuntimeError(label)
    return s.replace(o,n,1)
def hiring(s,hmin,hmax,div=7,weight=2):
    s=re.sub(r'HAND_TARGET_MIN = 4',f'HAND_TARGET_MIN = {hmin}',s,count=1)
    s=re.sub(r'HAND_TARGET_MAX = 18',f'HAND_TARGET_MAX = {hmax}',s,count=1)
    s=re.sub(r'MAX_HIRE_SLOTS = HAND_TARGET_MAX',f'MAX_HIRE_SLOTS = {hmax}',s,count=1)
    s=re.sub(r'ANIMAL_WORK_WEIGHT = 2',f'ANIMAL_WORK_WEIGHT = {weight}',s,count=1)
    s=rep(s,'math.ceil(work / 5)',f'math.ceil(work / {div})','div')
    return s
def land(s,start,reserve):
    s=re.sub(r'if day >= 1 and quads < 4:',f'if day >= {start} and quads < 4:',s,count=1)
    s=s.replace('LAND_PRICES[quads - 1] + 500',f'LAND_PRICES[quads - 1] + {reserve}')
    return s
def priority(s,p):
    return rep(s,'PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]',f'PLANT_PRIORITY = {p!r}','priority')
def seeds(s,melon=(6,10),straw=(8,14),tom=3,car=4,wheat=40):
    s=re.sub(r'melon_target = min\(space, 6 if ph == 0 else 10\)',f'melon_target = min(space, {melon[0]} if ph == 0 else {melon[1]})',s,count=1)
    s=re.sub(r'want\["STRAWBERRY"\] = min\(space, 8 if ph == 0 else 14\)',f'want["STRAWBERRY"] = min(space, {straw[0]} if ph == 0 else {straw[1]})',s,count=1)
    s=re.sub(r'want\["TOMATO"\] = 3',f'want["TOMATO"] = {tom}',s,count=1)
    s=re.sub(r'want\["CARROT"\] = 4',f'want["CARROT"] = {car}',s,count=1)
    s=re.sub(r'want\["WHEAT"\] = min\(space, 40\)',f'want["WHEAT"] = min(space, {wheat})',s,count=1)
    return s
def animals(s,sheep=True,cow_last=22,sheep_last=22,headroom=4):
    s=re.sub(r'SHEEP_ENABLED = True',f'SHEEP_ENABLED = {sheep}',s,count=1)
    s=re.sub(r'("COW":\s+\{"cost": 400, "min_money": 700, "start_day": 0,\s+"last_day": )22',rf'\g<1>{cow_last}',s,count=1)
    s=re.sub(r'("SHEEP": \{"cost": 500, "min_money": 800, "start_day": 3,\s+"last_day": )22',rf'\g<1>{sheep_last}',s,count=1)
    s=re.sub(r'SHEEP_HAND_HEADROOM = 4',f'SHEEP_HAND_HEADROOM = {headroom}',s,count=1)
    return s
def care(s,mode):
    old='    needs_care = (not critical_only) and (not tile.get("cared_today", True))\n'
    if mode=='none': new='    needs_care = False\n'
    elif mode=='alternate': new='    needs_care = (not critical_only) and (day % 2 == 0) and (not tile.get("cared_today", True))\n'
    elif mode=='late': new='    needs_care = (not critical_only) and (day >= 6) and (not tile.get("cared_today", True))\n'
    else: return s
    return rep(s,old,new,'care')
def fert(s,collect):
    if collect:return s
    return rep(s,'    has_fert = (not critical_only) and tile.get("fertilizer_available", False)\n','    has_fert = False\n','fert')
def protect(s,lo,hi):
    s=rep(s,'PROTECTED_FRACTION_LOW = 0.50',f'PROTECTED_FRACTION_LOW = {lo:.2f}','pl')
    s=rep(s,'PROTECTED_FRACTION_HIGH = 0.70',f'PROTECTED_FRACTION_HIGH = {hi:.2f}','ph')
    return s

specs=[
('balanced8_compact','8 hands, modest land delay, original portfolio',dict(h=(3,8,7,2),land=(4,1200))),
('balanced8_no_fert','8 hands, modest land delay, skip fertilizer logistics',dict(h=(3,8,7,2),land=(4,1200),fert=False)),
('balanced8_altcare','8 hands, modest land delay, alternate care',dict(h=(3,8,7,2),land=(4,1200),care='alternate',fert=False)),
('balanced9_compact','9 hands, compact land, original portfolio',dict(h=(3,9,7,2),land=(4,1200))),
('balanced10_compact','10 hands, compact land, original portfolio',dict(h=(4,10,6,2),land=(4,1200))),
('ongoing8_compact','8 hands, compact land, ongoing crop core',dict(h=(3,8,7,2),land=(5,1500),p=['STRAWBERRY','TOMATO','MELON','WHEAT','CARROT'],seed=((4,7),(11,18),6,1,18))),
('melon8_compact','8 hands, compact land, melon batch core',dict(h=(3,8,7,2),land=(5,1500),p=['MELON','STRAWBERRY','WHEAT','TOMATO','CARROT'],seed=((12,20),(5,8),1,1,18))),
('wheatcow8_compact','8 hands, compact land, wheat-fed cow fleet',dict(h=(3,8,6,2),land=(5,1500),p=['WHEAT','STRAWBERRY','MELON','TOMATO','CARROT'],seed=((4,7),(6,10),1,1,40),animal=(False,16,22,0))),
('smallcow8_compact','8 hands, compact land, small cow-only fleet',dict(h=(3,8,7,1),land=(5,1500),animal=(False,12,22,0),fert=False)),
('smallmixed8_compact','8 hands, compact land, shorter mixed expansion',dict(h=(3,8,7,2),land=(5,1500),animal=(True,14,14,2),fert=False)),
('cropguard8_compact','8 hands, compact land, stronger crop protection',dict(h=(3,8,7,2),land=(5,1500),protect=(.62,.78),animal=(True,16,16,2),fert=False)),
('animallean8_compact','8 hands, compact land, animal-oriented allocation',dict(h=(3,8,6,3),land=(5,1500),protect=(.35,.50),animal=(True,14,16,3),fert=False)),
('nine_altcare_compact','9 hands, alternate care, compact land',dict(h=(3,9,7,2),land=(5,1500),care='alternate',fert=False)),
('nine_smallfleet_compact','9 hands, small mixed fleet, compact land',dict(h=(3,9,7,2),land=(5,1500),animal=(True,14,14,2),fert=False)),
('ten_smallfleet_compact','10 hands, small mixed fleet, compact land',dict(h=(4,10,6,2),land=(5,1500),animal=(True,14,14,2),fert=False)),
('eight_latecare_compact','8 hands, delay care until production ramp',dict(h=(3,8,7,2),land=(5,1500),care='late',fert=False)),
('eight_straw_melon_compact','8 hands, compact premium crop blend',dict(h=(3,8,7,2),land=(5,1500),p=['STRAWBERRY','MELON','WHEAT','TOMATO','CARROT'],seed=((9,15),(9,15),2,1,22),animal=(True,14,14,2),fert=False)),
('eight_melon_cow_compact','8 hands, melon emphasis, cow-only small fleet',dict(h=(3,8,7,2),land=(5,1500),p=['MELON','STRAWBERRY','WHEAT','TOMATO','CARROT'],seed=((10,17),(6,10),1,1,24),animal=(False,14,22,0),fert=False)),
('nine_diverse_compact','9 hands, compact diversified crop and mixed fleet',dict(h=(3,9,7,2),land=(4,1300),p=['STRAWBERRY','MELON','WHEAT','TOMATO','CARROT'],seed=((8,13),(8,13),3,3,28),animal=(True,16,16,2),fert=False)),
('eight_austerity_balanced','8 hands, strict compactness, reduced optional work',dict(h=(3,8,8,1),land=(7,2200),animal=(True,12,12,1),care='alternate',fert=False,protect=(.58,.72))),
]
manifest=[]
for i,(slug,desc,cfg) in enumerate(specs,1):
    s=BASE
    if 'h' in cfg:s=hiring(s,*cfg['h'])
    if 'land' in cfg:s=land(s,*cfg['land'])
    if 'p' in cfg:s=priority(s,cfg['p'])
    if 'seed' in cfg:s=seeds(s,*cfg['seed'])
    if 'animal' in cfg:s=animals(s,*cfg['animal'])
    if 'care' in cfg:s=care(s,cfg['care'])
    if 'fert' in cfg:s=fert(s,cfg['fert'])
    if 'protect' in cfg:s=protect(s,*cfg['protect'])
    header=f'# BLENDED EFFICIENCY AGENT {i:02d}: {slug}\n# Objective: jointly improve turn, land, and labor efficiency.\n# Policy: {desc}.\n# Base: main_v8.3.py\n\n'
    path=OUT/f'blend_{i:02d}_{slug}.py'; compile(header+s,str(path),'exec'); path.write_text(header+s)
    manifest.append({'id':i,'file':path.name,'policy':desc,'config':cfg})
Path('/mnt/data/blended_agents_manifest.json').write_text(json.dumps(manifest,indent=2))
print('created',len(manifest))
