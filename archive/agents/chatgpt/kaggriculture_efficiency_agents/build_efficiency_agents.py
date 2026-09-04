from pathlib import Path
import json, re

BASE_PATH = Path('/mnt/data/main_v8.3.py')
BASE = BASE_PATH.read_text()
OUT = Path('/mnt/data/efficiency_agents')
OUT.mkdir(exist_ok=True)

agents = []

def replace_once(s, old, new, label):
    if old not in s:
        raise RuntimeError(f'missing patch target: {label}')
    return s.replace(old, new, 1)

def add_header(s, family, idx, name, objective, changes):
    hdr = (
        f'# {family.upper()} EFFICIENCY AGENT {idx:02d}: {name}\n'
        f'# Base: main_v8.3.py\n'
        f'# Objective: {objective}\n'
        f'# Isolated policy changes: {changes}\n\n'
    )
    return hdr + s

def patch_seed_targets(s, melon=None, strawberry=None, tomato=None, carrot=None, wheat=None):
    if melon is not None:
        s = re.sub(r'melon_target = min\(space, 6 if ph == 0 else 10\)',
                   f'melon_target = min(space, {melon[0]} if ph == 0 else {melon[1]})', s, count=1)
    if strawberry is not None:
        s = re.sub(r'want\["STRAWBERRY"\] = min\(space, 8 if ph == 0 else 14\)',
                   f'want["STRAWBERRY"] = min(space, {strawberry[0]} if ph == 0 else {strawberry[1]})', s, count=1)
    if tomato is not None:
        s = re.sub(r'want\["TOMATO"\] = 3', f'want["TOMATO"] = {tomato}', s, count=1)
    if carrot is not None:
        s = re.sub(r'want\["CARROT"\] = 4', f'want["CARROT"] = {carrot}', s, count=1)
    if wheat is not None:
        s = re.sub(r'want\["WHEAT"\] = min\(space, 40\)', f'want["WHEAT"] = min(space, {wheat})', s, count=1)
    return s

def patch_care_mode(s, mode):
    old = '    needs_care = (not critical_only) and (not tile.get("cared_today", True))\n'
    if mode == 'alternate':
        new = '    needs_care = (not critical_only) and (day % 2 == 0) and (not tile.get("cared_today", True))\n'
    elif mode == 'production_window':
        # Care only after feed on days likely to bank value before common cow/sheep ticks.
        new = '    needs_care = (not critical_only) and (day % 3 != 0) and (not tile.get("cared_today", True))\n'
    elif mode == 'none':
        new = '    needs_care = False\n'
    else:
        return s
    return replace_once(s, old, new, f'care mode {mode}')

def patch_fertilizer_collection(s, enabled):
    if enabled:
        return s
    s = replace_once(s,
        '    has_fert = (not critical_only) and tile.get("fertilizer_available", False)\n',
        '    has_fert = False  # efficiency variant skips optional fertilizer collection\n',
        'disable fertilizer collection')
    return s

def patch_land_gate(s, min_money_delta=0, start_day=None):
    # Tighten the existing land thresholds without restructuring economy.
    if min_money_delta:
        s = s.replace('LAND_PRICES[quads - 1] + 500', f'LAND_PRICES[quads - 1] + {500 + min_money_delta}')
    if start_day is not None:
        s = re.sub(r'if day >= 1 and quads < 4:', f'if day >= {start_day} and quads < 4:', s, count=1)
    return s

def patch_animals(s, cow_last=None, sheep_enabled=None, sheep_last=None, headroom=None):
    if cow_last is not None:
        s = re.sub(r'("COW":\s+\{"cost": 400, "min_money": 700, "start_day": 0,\s+"last_day": )22', rf'\g<1>{cow_last}', s, count=1)
    if sheep_last is not None:
        s = re.sub(r'("SHEEP": \{"cost": 500, "min_money": 800, "start_day": 3,\s+"last_day": )22', rf'\g<1>{sheep_last}', s, count=1)
    if sheep_enabled is not None:
        s = re.sub(r'SHEEP_ENABLED = True', f'SHEEP_ENABLED = {str(sheep_enabled)}', s, count=1)
    if headroom is not None:
        s = re.sub(r'SHEEP_HAND_HEADROOM = 4', f'SHEEP_HAND_HEADROOM = {headroom}', s, count=1)
    return s

def patch_hiring(s, hmin=None, hmax=None, slots=None, weight=None, divisor=None):
    if hmin is not None: s = re.sub(r'HAND_TARGET_MIN = 4', f'HAND_TARGET_MIN = {hmin}', s, count=1)
    if hmax is not None: s = re.sub(r'HAND_TARGET_MAX = 18', f'HAND_TARGET_MAX = {hmax}', s, count=1)
    if slots is not None: s = re.sub(r'MAX_HIRE_SLOTS = HAND_TARGET_MAX', f'MAX_HIRE_SLOTS = {slots}', s, count=1)
    if weight is not None: s = re.sub(r'ANIMAL_WORK_WEIGHT = 2', f'ANIMAL_WORK_WEIGHT = {weight}', s, count=1)
    if divisor is not None:
        s = replace_once(s, 'math.ceil(work / 5)', f'math.ceil(work / {divisor})', 'hire work divisor')
    return s

def make(family, idx, slug, objective, changes, fn):
    s = fn(BASE)
    s = add_header(s, family, idx, slug, objective, changes)
    filename = f'{family}_{idx:02d}_{slug}.py'
    path = OUT / filename
    compile(s, str(path), 'exec')
    path.write_text(s)
    agents.append({
        'family': family,
        'id': idx,
        'name': slug,
        'file': filename,
        'objective': objective,
        'changes': changes,
    })

# --------------------------- Turn efficiency ---------------------------
make('turn',1,'ongoing_crop_core',
     'Maximize revenue per unit action by reducing harvest/replant cycles.',
     'Prioritize strawberry/tomato; suppress short-cycle carrot and excess wheat.',
     lambda s: patch_seed_targets(replace_once(s, 'PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]',
        'PLANT_PRIORITY = ["STRAWBERRY", "TOMATO", "MELON", "WHEAT", "CARROT"]','priority'),
        melon=(4,7), strawberry=(12,20), tomato=8, carrot=1, wheat=18))

make('turn',2,'melon_batch_farming',
     'Concentrate labor into infrequent, high-value batch harvests.',
     'Melon-first portfolio; sharply reduce ongoing and short-cycle crops.',
     lambda s: patch_seed_targets(replace_once(s, 'PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]',
        'PLANT_PRIORITY = ["MELON", "STRAWBERRY", "WHEAT", "TOMATO", "CARROT"]','priority'),
        melon=(14,24), strawberry=(4,7), tomato=1, carrot=1, wheat=16))

make('turn',3,'wheat_batch_feed',
     'Use simple four-day crop cycles and local feed to reduce market and routing actions.',
     'Wheat-first planting; moderate cow window; sheep disabled.',
     lambda s: patch_animals(patch_seed_targets(replace_once(s, 'PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]',
        'PLANT_PRIORITY = ["WHEAT", "MELON", "STRAWBERRY", "TOMATO", "CARROT"]','priority'),
        melon=(5,8), strawberry=(5,8), tomato=1, carrot=1, wheat=40), sheep_enabled=False, cow_last=18))

make('turn',4,'minimal_optional_animal_work',
     'Reserve turns for mandatory feed, crop work, and harvest.',
     'Disable animal care and fertilizer collection; retain v8.3 fleet economics.',
     lambda s: patch_fertilizer_collection(patch_care_mode(s,'none'),False))

make('turn',5,'alternate_care',
     'Capture some care bonus with half the routine care actions.',
     'Care only on even-numbered days; fertilizer collection disabled.',
     lambda s: patch_fertilizer_collection(patch_care_mode(s,'alternate'),False))

make('turn',6,'production_window_care',
     'Spend care actions selectively rather than every eligible day.',
     'Skip care every third day and skip fertilizer collection.',
     lambda s: patch_fertilizer_collection(patch_care_mode(s,'production_window'),False))

make('turn',7,'compact_farm',
     'Reduce walking turns by delaying expansion and keeping work near the shed.',
     'Land purchases start day 8 and require an additional $2,000 reserve.',
     lambda s: patch_land_gate(s, min_money_delta=2000, start_day=8))

make('turn',8,'small_cow_fleet',
     'Limit daily maintenance actions while retaining premium animal output.',
     'Disable sheep; stop cow purchases after day 12; lower animal labor weighting.',
     lambda s: patch_hiring(patch_animals(s, sheep_enabled=False, cow_last=12), weight=1))

make('turn',9,'no_fertilizer_logistics',
     'Eliminate collect, carry, deposit, and sale actions for a low-priority byproduct.',
     'Fertilizer collection disabled; all other behavior unchanged.',
     lambda s: patch_fertilizer_collection(s,False))

make('turn',10,'crop_only_batch',
     'Avoid all animal setup and daily maintenance actions.',
     'Disable sheep and close cow purchase window; melon/strawberry batch crop mix.',
     lambda s: patch_seed_targets(patch_animals(replace_once(s, 'PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]',
        'PLANT_PRIORITY = ["MELON", "STRAWBERRY", "TOMATO", "WHEAT", "CARROT"]','priority'),
        sheep_enabled=False, cow_last=-1), melon=(14,22), strawberry=(10,16), tomato=3, carrot=1, wheat=12))

# --------------------------- Labor efficiency ---------------------------
make('labor',1,'six_hand_cap',
     'Maximize farm output per worker by imposing a hard six-hand ceiling.',
     'Hand target 3–6; maximum six hires; expansion gates inherit the cap.',
     lambda s: patch_hiring(s,hmin=3,hmax=6,slots=6,divisor=7))

make('labor',2,'eight_hand_cap',
     'Use a moderate worker ceiling while preserving more throughput than the strict cap.',
     'Hand target 3–8; maximum eight hires; seven work units per target hand.',
     lambda s: patch_hiring(s,hmin=3,hmax=8,slots=8,divisor=7))

make('labor',3,'ten_hand_cap',
     'Seek a balanced labor frontier between v8.3 throughput and payroll footprint.',
     'Hand target 4–10; maximum ten hires; six work units per target hand.',
     lambda s: patch_hiring(s,hmin=4,hmax=10,slots=10,divisor=6))

make('labor',4,'crop_protected_small_team',
     'Make a small team dependable by protecting most workers for crop survival.',
     'Eight-hand cap and protected crop fraction raised to 70–85%.',
     lambda s: replace_once(replace_once(patch_hiring(s,hmin=3,hmax=8,slots=8,divisor=7),
        'PROTECTED_FRACTION_LOW = 0.50','PROTECTED_FRACTION_LOW = 0.70','protected low'),
        'PROTECTED_FRACTION_HIGH = 0.70','PROTECTED_FRACTION_HIGH = 0.85','protected high'))

make('labor',5,'animal_specialist_small_team',
     'Use fewer workers but devote a larger share to high-value animal maintenance.',
     'Eight-hand cap, low crop protection, animal workload counted at weight three.',
     lambda s: replace_once(replace_once(patch_hiring(s,hmin=3,hmax=8,slots=8,weight=3,divisor=6),
        'PROTECTED_FRACTION_LOW = 0.50','PROTECTED_FRACTION_LOW = 0.30','protected low'),
        'PROTECTED_FRACTION_HIGH = 0.70','PROTECTED_FRACTION_HIGH = 0.45','protected high'))

make('labor',6,'ongoing_crops_eight_hands',
     'Reduce replant burden so each worker supports more occupied tiles.',
     'Eight-hand cap plus strawberry/tomato-heavy ongoing-crop portfolio.',
     lambda s: patch_seed_targets(patch_hiring(replace_once(s, 'PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]',
        'PLANT_PRIORITY = ["STRAWBERRY", "TOMATO", "MELON", "WHEAT", "CARROT"]','priority'),
        hmin=3,hmax=8,slots=8,divisor=7), melon=(4,7), strawberry=(12,20), tomato=8, carrot=1, wheat=16))

make('labor',7,'melon_eight_hands',
     'Allocate a constrained workforce to a high-value, infrequent-harvest crop.',
     'Eight-hand cap; melon-first portfolio; reduced crop variety.',
     lambda s: patch_seed_targets(patch_hiring(replace_once(s, 'PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]',
        'PLANT_PRIORITY = ["MELON", "STRAWBERRY", "WHEAT", "TOMATO", "CARROT"]','priority'),
        hmin=3,hmax=8,slots=8,divisor=7), melon=(14,22), strawberry=(5,8), tomato=1, carrot=1, wheat=16))

make('labor',8,'cow_wheat_eight_hands',
     'Use a constrained team on home-fed cows rather than a mixed premium fleet.',
     'Eight-hand cap, sheep disabled, wheat-first portfolio, cows available through day 18.',
     lambda s: patch_seed_targets(patch_animals(patch_hiring(replace_once(s, 'PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]',
        'PLANT_PRIORITY = ["WHEAT", "STRAWBERRY", "MELON", "TOMATO", "CARROT"]','priority'),
        hmin=3,hmax=8,slots=8,weight=2,divisor=6), sheep_enabled=False, cow_last=18),
        melon=(4,7), strawberry=(6,10), tomato=1, carrot=1, wheat=40))

make('labor',9,'alternate_care_eight_hands',
     'Stretch a limited workforce across animals by halving care cadence.',
     'Eight-hand cap, alternate-day care, no fertilizer collection.',
     lambda s: patch_fertilizer_collection(patch_care_mode(patch_hiring(s,hmin=3,hmax=8,slots=8,divisor=6),'alternate'),False))

make('labor',10,'four_hand_austerity',
     'Measure the extreme output-per-worker frontier with a four-hand ceiling.',
     'Hand target 2–4, no sheep, no care, no fertilizer collection, delayed land.',
     lambda s: patch_land_gate(patch_fertilizer_collection(patch_care_mode(patch_animals(patch_hiring(s,hmin=2,hmax=4,slots=4,weight=1,divisor=9),
        sheep_enabled=False,cow_last=10),'none'),False),min_money_delta=1500,start_day=6))

manifest = {
    'base': 'main_v8.3.py',
    'definitions': {
        'turn_efficiency': 'Revenue generated per scarce unit action/turn; variants reduce recurring actions, travel, replanting, and optional maintenance.',
        'labor_efficiency': 'Revenue generated per hired hand-day; variants constrain team size and adapt production to the smaller workforce.'
    },
    'agents': agents,
}
Path('/mnt/data/efficiency_agents_manifest.json').write_text(json.dumps(manifest, indent=2))
print(f'created {len(agents)} agents')
for a in agents:
    print(a['file'])
