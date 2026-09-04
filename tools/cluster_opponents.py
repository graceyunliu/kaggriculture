#!/usr/bin/env python3
"""Cluster ladder opponents by their SELL schedule (units of each product sold, per 5-day bucket).

The market is shared: the only way an opponent affects our payoff is what it sells and when,
not what it buys or how it moves. Clustering on the sale schedule (rather than day-0 purchase
fingerprints) answers "does the best response differ" more directly than "does the opener differ".

  python3 tools/cluster_opponents.py --k 6 --min-share 0.10
"""
import argparse
import glob
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ["STRAWBERRY", "MELON", "MILK", "WOOL", "WHEAT", "FERTILIZER", "EGG", "CARROT", "TOMATO"]
BUCKETS = 6  # 5-day buckets over 30 days


def opponent_seat(names):
    for i, n in enumerate(names or []):
        if "graceyunliu" in (n or "").lower():
            return 1 - i
    return None  # unknown provenance; still usable, just unlabeled as "mine"


CACHE_PATH = ROOT / ".sale_vec_cache.json"


def _load_cache():
    if CACHE_PATH.exists():
        try:
            return json.load(open(CACHE_PATH))
        except Exception:
            return {}
    return {}


def _save_cache(cache):
    tmp = str(CACHE_PATH) + ".tmp"
    json.dump(cache, open(tmp, "w"))
    Path(tmp).replace(CACHE_PATH)


def extract_cached(path, cache):
    key = str(Path(path).resolve())
    if key in cache:
        v = cache[key]
        if v is None:
            return None
        vec = {(int(bk), it): val for bk_it, val in v["vec"].items()
               for bk, it in [bk_it.split("|", 1)]}
        return {"path": path, "name": v["name"], "vec": vec, "total": v["total"]}
    e = extract(path)
    if e is None:
        cache[key] = None
    else:
        cache[key] = {"name": e["name"], "total": e["total"],
                      "vec": {f"{b}|{it}": val for (b, it), val in e["vec"].items()}}
    return e


def extract(path):
    try:
        r = json.load(open(path))
    except Exception:
        return None
    if not isinstance(r, dict):
        return None
    info = r.get("info", {})
    names = info.get("TeamNames", ["", ""]) if isinstance(info, dict) else ["", ""]
    steps = r.get("steps", [])
    if len(steps) < 2:
        return None
    seat = opponent_seat(names)
    if seat is None:
        seat = 1  # fallback: treat seat 1 as "opponent" for solo/self files
    vec = defaultdict(float)
    for s in range(1, len(steps)):
        act = steps[s][seat].get("action") if len(steps[s]) > seat else None
        if not act:
            continue
        day = min((s - 1) // 24, 29)
        bucket = min(day // 5, BUCKETS - 1)
        for o in act.get("market") or []:
            if isinstance(o, list) and len(o) >= 3 and o[0] == "SELL" and o[1] in ITEMS:
                vec[(bucket, o[1])] += float(o[2])
    name = names[seat] if seat < len(names) else "?"
    total = sum(vec.values())
    if total < 10:
        return None
    return {"path": path, "name": name, "vec": vec, "total": total}


def to_array(entries):
    import numpy as np
    dims = [(b, it) for b in range(BUCKETS) for it in ITEMS]
    X = np.zeros((len(entries), len(dims)))
    for i, e in enumerate(entries):
        row_total = e["total"] or 1
        for j, d in enumerate(dims):
            X[i, j] = e["vec"].get(d, 0) / row_total  # normalize: schedule *shape*, not scale
    return X, dims


def kmeans(X, k, iters=100, seed=0):
    import numpy as np
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(X), size=k, replace=False)
    centers = X[idx].copy()
    labels = np.zeros(len(X), dtype=int)
    for _ in range(iters):
        d = ((X[:, None, :] - centers[None, :, :]) ** 2).sum(-1)
        new_labels = d.argmin(1)
        if (new_labels == labels).all():
            break
        labels = new_labels
        for c in range(k):
            m = labels == c
            if m.any():
                centers[c] = X[m].mean(0)
    return labels, centers


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=6)
    ap.add_argument("--min-share", type=float, default=0.10)
    ap.add_argument("--glob", default="Replays/Auto/leaderboard-*/*.json")
    ap.add_argument("--recent-glob", default="Replays/Auto/mine/*.json",
                     help="the pool used to compute cluster *share* (recency-weighted)")
    ap.add_argument("--recent-limit", type=int, default=200,
                     help="cap on how many recent-pool files to load (that folder is huge)")
    ap.add_argument("--fit-limit", type=int, default=250,
                     help="cap on how many leaderboard files to consider (evenly sampled)")
    ap.add_argument("--max-new", type=int, default=25,
                     help="cap on how many *uncached* files to parse this invocation (rerun to accumulate)")
    args = ap.parse_args()

    cache = _load_cache()
    files = sorted(set(glob.glob(str(ROOT / args.glob), recursive=True)))
    if len(files) > args.fit_limit:
        step = len(files) / args.fit_limit
        files = [files[int(i * step)] for i in range(args.fit_limit)]
    print(f"considering {len(files)} replay files ({sum(1 for f in files if str(Path(f).resolve()) in cache)} cached)...", file=sys.stderr)
    entries = []
    new_parsed = 0
    for f in files:
        key = str(Path(f).resolve())
        if key not in cache and new_parsed >= args.max_new:
            continue
        if key not in cache:
            new_parsed += 1
        e = extract_cached(f, cache)
        if e:
            entries.append(e)
    _save_cache(cache)
    print(f"{len(entries)} usable opponent-games ({new_parsed} newly parsed this run, cache now {len(cache)})", file=sys.stderr)
    if len(entries) < args.k * 3:
        print("too few games for k=%d" % args.k, file=sys.stderr)
        return

    X, dims = to_array(entries)
    labels, centers = kmeans(X, args.k)

    all_counts = defaultdict(int)
    reps = defaultdict(list)
    for e, lab in zip(entries, labels):
        all_counts[lab] += 1
        reps[lab].append(e)

    # recency pool: a capped, evenly-spaced sample of the (huge) recent-games folder,
    # scored against the centers already fit on the leaderboard pool (not refit).
    import numpy as np
    recent_files = sorted(glob.glob(str(ROOT / args.recent_glob)))
    if len(recent_files) > args.recent_limit:
        step = len(recent_files) / args.recent_limit
        recent_files = [recent_files[int(i * step)] for i in range(args.recent_limit)]
    print(f"scoring {len(recent_files)} recent-pool files against fitted centers...", file=sys.stderr)
    recent_counts = defaultdict(int)
    n_recent = 0
    recent_new = 0
    for f in recent_files:
        key = str(Path(f).resolve())
        if key not in cache and recent_new >= args.max_new:
            continue
        if key not in cache:
            recent_new += 1
        e = extract_cached(f, cache)
        if not e:
            continue
        row = np.zeros(len(dims))
        tot = e["total"] or 1
        for j, d in enumerate(dims):
            row[j] = e["vec"].get(d, 0) / tot
        c = int(((centers - row[None, :]) ** 2).sum(1).argmin())
        recent_counts[c] += 1
        n_recent += 1
    _save_cache(cache)
    n_recent = n_recent or 1

    print(f"\n{'cluster':8s} {'n_all':>6s} {'n_recent':>9s} {'share_recent':>13s}  top sale pattern")
    order = sorted(range(args.k), key=lambda c: -recent_counts[c])
    for c in order:
        share = recent_counts[c] / n_recent
        # describe center: top 4 (bucket,item) weights
        top = sorted(range(len(dims)), key=lambda j: -centers[c][j])[:4]
        desc = ", ".join(f"{dims[j][1]}@d{dims[j][0]*5}-{dims[j][0]*5+4}:{centers[c][j]:.2f}" for j in top)
        flag = "  <-- pool" if share >= args.min_share else ""
        print(f"{c:<8d} {all_counts[c]:>6d} {recent_counts[c]:>9d} {share:>12.1%}  {desc}{flag}")
        # representative: game closest to centroid among this cluster's members
        import numpy as np
        members = [e for e, lab in zip(entries, labels) if lab == c]
        if members:
            idxs = [i for i, lab in enumerate(labels) if lab == c]
            dists = ((X[idxs] - centers[c]) ** 2).sum(1)
            rep = members[int(dists.argmin())]
            print(f"           representative: {rep['name']!r}  {rep['path']}")

    print(f"\npools with share >= {args.min_share:.0%} of recent games: "
          f"{sorted(c for c in order if recent_counts[c]/n_recent >= args.min_share)}")


if __name__ == "__main__":
    main()
