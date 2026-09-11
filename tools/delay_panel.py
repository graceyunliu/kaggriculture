#!/usr/bin/env python3
"""Phase 1 of the value-at-risk programme (Sep 10/11): validate the delay-consequence table across seeds, tapes,
horizons and delay lengths before any dispatcher change.

For each (seed, tape): play the base game with the candidate, record every work action with its state bucket
(tools/delay_counterfactual.bucket). Sample events stratified per bucket; for each sampled event and each delay
k in --delays, replay and force that unit to PASS for k consecutive steps starting at the event step, then read
the consequence at --horizons (0 = final money; h>0 = net-worth proxy h steps after the event).

Output: JSONL of every counterfactual + a summary per bucket: mean/CI per (delay, horizon), sign consistency per
seed and per tape, and the delay curve (loss at 1h/2h/4h) so linear vs deadline-shaped loss is visible.

Usage (run under KAGG_FIXED_SHOPS=1):
  python3 tools/delay_panel.py CAND --tapes a.py,b.py,c.py --seeds 11-16 --per-bucket 30 --delays 1,2,4 --horizons 0,48 \
      --jobs 5 --out evolve/delay_panel_O16.jsonl
"""
import sys, os, argparse, random, json, math, time
from multiprocessing import Pool
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "tools"))
import mini_engine as me
from delay_counterfactual import bucket, networth, WORK


def play(cand, opp, seed, force=None, record=None, stop_at=None):
    """force=(step, unit, k): that unit PASSes on steps step..step+k-1."""
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            if i == 0:
                if record is not None:
                    units = [act.get("farmer") or []] + list(act.get("hands") or [])
                    farm = obs0.farms[0]
                    positions = [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]
                    inv = obs["private"].get("inventories") or []
                    for u, ua in enumerate(units):
                        if ua and ua[0] in WORK and u < len(positions):
                            x, y = positions[u]; t = farm["tiles"][y][x]
                            record.append((step, u, ua[0], bucket(ua[0], t, day, hour, inv[u] if u < len(inv) else {}), day, hour))
                if force is not None and force[0] <= step < force[0] + force[2]:
                    u = force[1]
                    if u == 0: act["farmer"] = ["PASS"]
                    elif u - 1 < len(act.get("hands") or []): act["hands"][u - 1] = ["PASS"]
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if stop_at is not None and step >= stop_at:
            return networth(state[0].observation, state[0].observation.private)
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return state[0].observation.farms[0]["money"]


def base_job(args):
    cand, opp, seed = args
    rec = []
    money = play(cand, opp, seed, record=rec)
    return (opp, seed, money, rec)


def cf_job(args):
    cand, opp, seed, step, u, k, horizons, base_money = args
    out = []
    for h in horizons:
        if h > 0:
            b = play(cand, opp, seed, stop_at=step + h + k)
            c = play(cand, opp, seed, force=(step, u, k), stop_at=step + h + k)
            out.append((h, c - b))
        else:
            c = play(cand, opp, seed, force=(step, u, k)); out.append((0, c - base_money))
    return (opp, seed, step, u, k, out)


def ci95(xs):
    n = len(xs); m = sum(xs) / n
    if n < 2: return m, float("nan")
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    return m, 1.96 * sd / math.sqrt(n)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand")
    ap.add_argument("--tapes", required=True); ap.add_argument("--seeds", default="11-16")
    ap.add_argument("--per-bucket", type=int, default=30); ap.add_argument("--delays", default="1,2,4")
    ap.add_argument("--horizons", default="0,48"); ap.add_argument("--jobs", type=int, default=5)
    ap.add_argument("--verbs", default="WATER,HARVEST,FEED,CARE,COLLECT_FERTILIZER,PLANT,DROP")
    ap.add_argument("--maxday", type=int, default=27); ap.add_argument("--maxhour", type=int, default=19)
    ap.add_argument("--out", required=True); ap.add_argument("--summary-only", action="store_true")
    ap.add_argument("--budget-s", type=float, default=0, help="stop launching new jobs after this many seconds (resumable: rerun same command)")
    a = ap.parse_args()
    os.chdir(ROOT)
    tapes = a.tapes.split(","); lo, hi = map(int, a.seeds.split("-")); seeds = list(range(lo, hi + 1))
    delays = [int(x) for x in a.delays.split(",")]; horizons = [int(x) for x in a.horizons.split(",")]
    verbs = set(a.verbs.split(","))
    t0 = time.time()
    if not a.summary_only:
        with Pool(a.jobs) as pool:
            bases = pool.map(base_job, [(a.cand, t, s, ) for t in tapes for s in seeds])
            # stratified sample: per bucket, spread evenly over (tape, seed)
            by_b = {}
            base_money = {}
            for opp, seed, money, rec in bases:
                base_money[(opp, seed)] = money
                for r in rec:
                    if r[2] in verbs and 2 <= r[4] <= a.maxday and r[5] <= a.maxhour:
                        by_b.setdefault(r[3], []).append((opp, seed) + r)
            rng = random.Random(1)
            jobs = []
            for b, lst in by_b.items():
                rng.shuffle(lst)
                # round-robin over (opp, seed) so every cell contributes
                cells = {}
                for e in lst: cells.setdefault((e[0], e[1]), []).append(e)
                picked = []
                while len(picked) < a.per_bucket and any(cells.values()):
                    for key in list(cells):
                        if cells[key]:
                            picked.append(cells[key].pop())
                            if len(picked) >= a.per_bucket: break
                for e in picked:
                    opp, seed, step, u, verb, bk, day, hour = e
                    for k in delays:
                        jobs.append((a.cand, opp, seed, step, u, k, horizons, base_money[(opp, seed)]))
            done = set()
            if os.path.exists(a.out):
                for l in open(a.out):
                    r = json.loads(l); done.add((r["opp"], r["seed"], r["step"], r["unit"], r["delay"]))
            total = len(jobs)
            jobs = [j for j in jobs if (j[1], j[2], j[3], j[4], j[5]) not in done]
            print(f"{len(by_b)} buckets, {total} counterfactual jobs, {len(jobs)} remaining after {time.time()-t0:.0f}s", flush=True)
            meta = {(opp, seed, step, u): (verb, bk, day, hour) for lst in by_b.values() for (opp, seed, step, u, verb, bk, day, hour) in lst}
            with open(a.out, "a") as f:
                it = pool.imap_unordered(cf_job, jobs, chunksize=1)
                for i in range(len(jobs)):
                    if a.budget_s and time.time() - t0 > a.budget_s:
                        print(f"budget reached at {i}/{len(jobs)}; rerun to resume", flush=True); pool.terminate(); break
                    res = next(it)
                    opp, seed, step, u, k, out = res
                    verb, bk, day, hour = meta[(opp, seed, step, u)]
                    for h, d in out:
                        f.write(json.dumps({"cand": a.cand, "opp": opp, "seed": seed, "step": step, "unit": u, "verb": verb,
                                            "bucket": bk, "day": day, "hour": hour, "delay": k, "horizon": h, "delta": d}) + "\n")
                    f.flush()
                    if i % 50 == 0: print(f"  {i}/{len(jobs)} {time.time()-t0:.0f}s", flush=True)
    rows = [json.loads(l) for l in open(a.out)]
    print(f"\n== summary: {len(rows)} counterfactuals, {len(set(r['opp'] for r in rows))} tapes, {len(set(r['seed'] for r in rows))} seeds ==")
    buckets = sorted(set(r["bucket"] for r in rows))
    for h in horizons:
        print(f"\n-- horizon {h} ({'final money' if h == 0 else f'net-worth proxy {h} steps after'}) --")
        print(f"{'bucket':28s} " + " ".join(f"{'d'+str(k)+' mean±ci':>16s}" for k in delays) + "   sign/seed  sign/tape  (delay 1)")
        table = []
        for b in buckets:
            cells = []
            for k in delays:
                xs = [r["delta"] for r in rows if r["bucket"] == b and r["horizon"] == h and r["delay"] == k]
                cells.append((ci95(xs) if xs else (float("nan"), float("nan")), len(xs)))
            d1 = [r for r in rows if r["bucket"] == b and r["horizon"] == h and r["delay"] == delays[0]]
            def frac_neg(key):
                groups = {}
                for r in d1: groups.setdefault(r[key], []).append(r["delta"])
                ms = [sum(v) / len(v) for v in groups.values() if len(v) >= 3]
                return f"{sum(1 for m in ms if m < 0)}/{len(ms)}" if ms else "-"
            table.append((cells[0][0][0], b, cells, frac_neg("seed"), frac_neg("opp")))
        for _, b, cells, fs, ft in sorted(table):
            print(f"{b:28s} " + " ".join(f"{m:+7.0f}±{c:5.0f}n{n:<3d}" for (m, c), n in cells) + f"   {fs:>9s}  {ft:>9s}")
    print(f"\n{time.time()-t0:.0f}s")
