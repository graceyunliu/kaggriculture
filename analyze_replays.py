import json, sys, collections, os

CROPS = {'WHEAT','MELON','CARROT','STRAWBERRY'}
ANIMALS = {'SHEEP','COW','GOOSE'}

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

def tile_iter(farm):
    for r, row in enumerate(farm['tiles']):
        for c, cell in enumerate(row):
            if cell not in (None, 'LOCKED'):
                yield (r,c), cell

def analyze_episode(fn, username):
    d = load(fn)
    idx, teams = target_farm_index(d, username)
    if idx is None:
        return {'error':'no farm match', 'teams':teams}
    steps = d['steps']
    action_log = []
    crop_seen = collections.Counter()
    animal_seen = collections.Counter()
    tile_crop_history = collections.defaultdict(list)
    animal_by_day = {}
    melon_fertilized_days = 0
    melon_tile_days = 0
    other_crop_fertilized = collections.Counter()
    other_crop_days = collections.Counter()
    day_actions = collections.defaultdict(list)
    max_day = 0

    last_tile_crop = {}

    for s in steps:
        agent = s[idx]
        obs = agent['observation']
        day = obs['day']
        max_day = max(max_day, day)
        verbs = agent['action']['farmer']
        if verbs:
            day_actions[day].append(tuple(verbs))
            action_log.append((day, tuple(verbs)))
        farm = obs['farms'][idx]
        day_animals = set()
        for coord, cell in tile_iter(farm):
            kind = cell.get('kind') if isinstance(cell, dict) else None
            if kind == 'PLANT':
                crop = cell.get('crop')
                if crop:
                    crop_seen[crop] += 1
                    if last_tile_crop.get(coord) != crop:
                        tile_crop_history[coord].append((day, crop))
                        last_tile_crop[coord] = crop
                    fert = cell.get('fertilized_until_day', -1)
                    is_fert = fert is not None and fert >= day
                    if crop == 'MELON':
                        melon_tile_days += 1
                        if is_fert:
                            melon_fertilized_days += 1
                    else:
                        other_crop_days[crop] += 1
                        if is_fert:
                            other_crop_fertilized[crop] += 1
            elif kind == 'PASTURE':
                animal = cell.get('animal')
                if animal:
                    animal_seen[animal] += 1
                    day_animals.add(animal)
        if day_animals:
            animal_by_day.setdefault(day, set()).update(day_animals)

    feed_days = 0
    care_days = 0
    animal_present_days = sorted(animal_by_day.keys())
    for day in animal_present_days:
        acts = [v[0] for v in day_actions.get(day, [])]
        if 'FEED' in acts:
            feed_days += 1
        if 'CARE' in acts:
            care_days += 1
    n_animal_days = len(animal_present_days)

    wheat_pickup_days = sorted(set(day for day, v in action_log if v and v[0]=='PICKUP' and len(v)>1 and v[1]=='WHEAT'))
    feed_action_days = sorted(set(day for day, v in action_log if v and v[0]=='FEED'))
    wheat_then_feed = 0
    for wd in wheat_pickup_days:
        if any(0 <= fd - wd <= 3 for fd in feed_action_days):
            wheat_then_feed += 1

    return {
        'teams': teams,
        'farm_idx': idx,
        'max_day': max_day,
        'crop_seen': dict(crop_seen),
        'animal_seen': dict(animal_seen),
        'tile_crop_history': {str(k): v for k, v in tile_crop_history.items()},
        'melon_tile_days': melon_tile_days,
        'melon_fertilized_days': melon_fertilized_days,
        'other_crop_days': dict(other_crop_days),
        'other_crop_fertilized': dict(other_crop_fertilized),
        'n_animal_present_days': n_animal_days,
        'feed_days': feed_days,
        'care_days': care_days,
        'wheat_pickup_days': wheat_pickup_days,
        'wheat_then_feed_count': wheat_then_feed,
        'action_verb_counts': dict(collections.Counter(v[0] for _, v in action_log)),
    }

if __name__ == '__main__':
    fn = sys.argv[1]
    username = sys.argv[2]
    out = analyze_episode(fn, username)
    print(json.dumps(out, indent=1, default=str))
