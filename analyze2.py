import json, sys, collections

def load(fn):
    with open(fn) as fh:
        return json.load(fh)

def target_farm_index(d, username):
    teams = d['info']['TeamNames']
    uname_norm = username.replace('_',' ').replace('.','').lower()
    for i, t in enumerate(teams):
        tn = t.replace('.','').lower()
        if uname_norm in tn or tn in uname_norm or username.lower() in t.lower():
            return i, teams
    return None, teams

def analyze_episode(fn, username):
    d = load(fn)
    idx, teams = target_farm_index(d, username)
    if idx is None:
        return {'error':'no farm match', 'teams':teams}
    steps = d['steps']

    last_ts_for_day = {}
    for t, s in enumerate(steps):
        day = s[idx]['observation']['day']
        last_ts_for_day[day] = t

    fed_total = collections.Counter(); fed_yes = collections.Counter()
    cared_total = collections.Counter(); cared_yes = collections.Counter()
    animal_types_by_day = {}
    crop_types_by_day = {}
    melon_days=0; melon_fert_days=0
    other_fert = collections.Counter(); other_days = collections.Counter()
    tile_crop_history = collections.defaultdict(list)
    last_tile_crop = {}

    for day, t in sorted(last_ts_for_day.items()):
        farm = steps[t][idx]['observation']['farms'][idx]
        animals_today = set()
        crops_today = set()
        for r, row in enumerate(farm['tiles']):
            for c, cell in enumerate(row):
                if not isinstance(cell, dict): continue
                if cell.get('kind')=='PASTURE' and cell.get('animal'):
                    a = cell['animal']
                    animals_today.add(a)
                    fed_total[a]+=1; cared_total[a]+=1
                    if cell.get('fed_today'): fed_yes[a]+=1
                    if cell.get('cared_today'): cared_yes[a]+=1
                elif cell.get('kind')=='PLANT' and cell.get('crop'):
                    crop = cell['crop']
                    crops_today.add(crop)
                    coord=(r,c)
                    if last_tile_crop.get(coord) != crop:
                        tile_crop_history[coord].append((day,crop))
                        last_tile_crop[coord]=crop
                    fert = cell.get('fertilized_until_day', -1)
                    is_fert = fert is not None and fert >= day
                    if crop=='MELON':
                        melon_days+=1
                        if is_fert: melon_fert_days+=1
                    else:
                        other_days[crop]+=1
                        if is_fert: other_fert[crop]+=1
        if animals_today: animal_types_by_day[day]=sorted(animals_today)
        if crops_today: crop_types_by_day[day]=sorted(crops_today)

    max_simultaneous_animals = max((len(v) for v in animal_types_by_day.values()), default=0)
    max_simultaneous_crops = max((len(v) for v in crop_types_by_day.values()), default=0)
    all_animal_combos = sorted(set(tuple(v) for v in animal_types_by_day.values()))
    all_crop_combos_2plus = sorted(set(tuple(v) for v in crop_types_by_day.values() if len(v)>=2))

    fed_frac = {a: round(fed_yes[a]/fed_total[a],3) for a in fed_total}
    cared_frac = {a: round(cared_yes[a]/cared_total[a],3) for a in cared_total}

    melon_fert_frac = round(melon_fert_days/melon_days,3) if melon_days else None
    other_fert_frac = {c: round(other_fert[c]/other_days[c],3) for c in other_days}

    return {
        'teams': teams, 'farm_idx': idx, 'n_days': len(last_ts_for_day),
        'fed_frac': fed_frac, 'cared_frac': cared_frac,
        'max_simultaneous_animals': max_simultaneous_animals,
        'animal_combos_seen': all_animal_combos,
        'max_simultaneous_crop_types': max_simultaneous_crops,
        'crop_combos_2plus_seen (sample)': all_crop_combos_2plus[:10],
        'melon_days': melon_days, 'melon_fert_frac': melon_fert_frac,
        'other_crop_days': dict(other_days), 'other_crop_fert_frac': other_fert_frac,
        'tile_crop_transitions_sample': {str(k): v for k,v in list(tile_crop_history.items())[:8]},
        'has_goose': any('GOOSE' in v for v in animal_types_by_day.values()),
        'has_carrot': any('CARROT' in v for v in crop_types_by_day.values()),
    }

if __name__=='__main__':
    fn, username = sys.argv[1], sys.argv[2]
    print(json.dumps(analyze_episode(fn, username), indent=1, default=str))
