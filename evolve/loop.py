#!/usr/bin/env python3
"""Autonomous evolution loop (v2): islands, candidate queue, factorials, auto-ablation.

    python3 evolve/loop.py --hours 2 --jobs 7          # one segment (the supervisor runs these back to back)
    python3 evolve/loop.py --minutes 5                  # quick check

Candidates are (params, blocks): 36 numeric/categorical parameters of the frozen chassis
(evolve/chassis.py) plus optional replacement source for any typed mutation block (evolve/blocks.py).

Islands (separate parent pools, occasional migration):
    v312   seeded from the V3.12 defaults, sigma 0.2
    c1     seeded from C1 (frontier opening), sigma 0.2
    wide   seeded from C1, sigma 0.5 / rate 0.35 -- the exploration island
    queue  every externally supplied candidate (factorial designs, LLM proposals, hand-written files)
Parent choice inside an island: tournament from its top (65%), a random behavioural cell (25%),
uniform (10%); with prob MIGRATE the parent is drawn from the global top-10 instead.

Queue: evolve/queue/*.json, consumed before any random generation. Two kinds:
    {"kind":"candidate","base":"c1","params":{..partial..},"blocks":{name: src},"origin":"llm","note":"..."}
    {"kind":"factorial","base":"c1","axes":{"open_wheat":[7,9],"fert_buy":[0,1]},"block_options":{"sweep":[null,"<src>"]}}
Consumed files move to evolve/queue/done/.

Ablation: when a candidate passes held-out, each single change vs its parent is reverted and
evaluated (dev stage only), so the report can say which changes carried the win.

Yardstick (frontier + clone) is fixed for a segment. Held-out results are never used for selection.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import random
import shutil
import signal
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

import blocks as blocks_mod  # noqa: E402
import space  # noqa: E402
from cascade import DEFAULTS, DEV_SEEDS, close_pool, get_pool, run_cascade, evaluate as cascade_eval  # noqa: E402
from db import DB  # noqa: E402
import report as report_mod  # noqa: E402

LOG_DIR = HERE / "logs"
QUEUE_DIR = HERE / "queue"
ARCHIVE = HERE / "archive.json"

ISLANDS = {
    "v312": {"seed": "base", "rate": 0.2, "sigma": 0.2},
    "c1":   {"seed": "c1", "rate": 0.2, "sigma": 0.2},
    "wide": {"seed": "c1", "rate": 0.35, "sigma": 0.5},
    "queue": {"seed": None, "rate": 0.2, "sigma": 0.2},
}
MIGRATE = 0.1
CROSSOVER = 0.3


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]


def cell_of(desc):
    if not desc:
        return None
    d = json.loads(desc) if isinstance(desc, str) else desc
    return (d.get("animals_d15", 0) // 3, d.get("land_final", 0), d.get("hands_max", 0) // 3)


def pick_parent(pool, rng):
    """pool: list of candidate rows sorted by dev_margin desc."""
    if not pool:
        return None
    u = rng.random()
    if u < 0.25:
        cells = {}
        for c in pool:
            k = cell_of(c.get("descriptor"))
            if k is not None and k not in cells:
                cells[k] = c
        if cells:
            return rng.choice(list(cells.values()))
    if u < 0.35:
        return rng.choice(pool)
    top = pool[:30]
    return max(rng.sample(top, min(3, len(top))), key=lambda c: c["dev_margin"])


def load_blocks(row):
    return json.loads(row["blocks"]) if row and row.get("blocks") else None


class Loop:
    def __init__(self, args):
        self.args = args
        self.run_id = args.run_id or datetime.now().strftime("%Y%m%d-%H%M")
        self.rng = random.Random(args.seed if args.seed is not None else int(time.time()))
        LOG_DIR.mkdir(exist_ok=True)
        self.logf = open(LOG_DIR / f"{self.run_id}.log", "a")
        get_pool(args.jobs)
        self.db = DB(args.db) if args.db else DB()
        self.cfg = {"smoke_floor": args.smoke_floor, "dev_promote": args.dev_promote,
                    "dev_promote_t": DEFAULTS["dev_promote_t"], "engine": "master", "jobs": args.jobs}
        self.engine_sha = sha(ROOT / "vendor" / "kaggle_environments_engine_master" / "kaggriculture.py")
        snap, self.k_sha = space.freeze_base(args.base) if args.base else space.freeze_base()
        space.set_frontier(args.frontier)   # keys candidates by (params, chassis, frontier) so switching the
                                             # yardstick can never reuse or mix in a score from the old one
        self.cfg["base"] = str(snap)
        self.chassis_text = snap.read_text()
        self.cfg["reference"] = str(space.render(space.c1_params()))   # diagnosis baseline = C1 on this chassis
        self.db.start_run(self.run_id, self.engine_sha, self.k_sha, args.frontier, args.clone, self.cfg)
        self.stats = defaultdict(int)
        self.gen = 0
        self.stop = False
        self.t_start = time.time()
        self.budget = args.hours * 3600 + args.minutes * 60
        self.log(f"run {self.run_id}: engine={self.engine_sha} chassis={snap.name} frontier={Path(args.frontier).name} "
                 f"clone={Path(args.clone).name} budget={self.budget/3600:.2f}h jobs={args.jobs}")

    def log(self, msg):
        line = f"[{datetime.now().strftime('%H:%M:%S')}] {msg}"
        print(line, flush=True)
        self.logf.write(line + "\n")
        self.logf.flush()

    def out_of_budget(self):
        if self.stop:
            return True
        if self.budget and time.time() - self.t_start > self.budget:
            self.log("time budget reached")
            return True
        if self.args.max_candidates and self.stats["evaluated"] >= self.args.max_candidates:
            self.log("candidate budget reached")
            return True
        return False

    # ---------------------------------------------------------------- evaluation
    def evaluate(self, params, blocks, parents, origin, island, note=None):
        key = space.params_key(params, blocks)
        if self.db.get(key):
            self.stats["dup"] += 1
            return None, key
        try:
            path = space.render(params, blocks)
            compile(path.read_text(), str(path), "exec")
        except Exception as e:  # noqa: BLE001
            self.db.insert(key, params, self.run_id, self.gen, parents, origin, "", island, blocks)
            self.db.update(key, status="error", note=f"render/compile: {e!r}"[:300])
            self.stats["error"] += 1
            self.log(f"#{self.stats['evaluated']+1} {origin} {key} [{island}] RENDER ERROR {e!r}"[:200])
            return "error", key
        self.db.insert(key, params, self.run_id, self.gen, parents, origin, path, island, blocks)
        if note:
            self.db.update(key, note=note[:300])
        desc = ""
        if parents:
            pp = json.loads(self.db.get(parents[0])["params"])
            desc = " ".join(f"{k}:{a}->{b}" for k, (a, b) in space.diff(params, pp).items())
        if blocks:
            desc += " blocks=" + ",".join(sorted(blocks))
        self.log(f"#{self.stats['evaluated']+1} {origin} {key} [{island}] {desc}")
        status = run_cascade(self.db, key, path, self.args.frontier, self.args.clone, self.cfg, jobs=self.args.jobs, log=self.log)
        self.stats["evaluated"] += 1
        self.stats[status] += 1
        if status == "held_pass":
            self.ablate(key, params, blocks, parents, island)
        return status, key

    def ablate(self, key, params, blocks, parents, island):
        """Revert each single change vs the parent and score it at the dev stage."""
        if not parents:
            return
        parent = self.db.get(parents[0])
        if not parent:
            return
        pp = json.loads(parent["params"])
        pb = load_blocks(parent) or {}
        changes = [("p", k) for k in space.diff(params, pp)]
        changes += [("b", b) for b in (blocks or {}) if (blocks or {}).get(b) != pb.get(b)]
        if len(changes) < 2 or len(changes) > 8:
            return
        results = {}
        for kind, name in changes:
            if self.out_of_budget():
                break
            q, qb = dict(params), dict(blocks or {})
            if kind == "p":
                q[name] = pp[name]
            else:
                if name in pb:
                    qb[name] = pb[name]
                else:
                    qb.pop(name, None)
            akey = space.params_key(q, qb or None)
            row = self.db.get(akey)
            if row and row.get("dev_margin") is not None:
                results[name] = row["dev_margin"]
                continue
            st, akey = self.evaluate(q, qb or None, [key], f"ablate:{name}", island, note=f"revert {name} of {key}")
            row = self.db.get(akey) if akey else None
            results[name] = row["dev_margin"] if row and row.get("dev_margin") is not None else None
        me = self.db.get(key)["dev_margin"]
        summary = {n: (None if v is None else round(me - v)) for n, v in results.items()}  # loss from reverting = contribution
        self.db.update(key, ablation=json.dumps(summary))
        self.log(f"    ablation of {key}: " + ", ".join(f"{n}:{v:+,}" if v is not None else f"{n}:?" for n, v in summary.items()))

    # ---------------------------------------------------------------- queue
    def base_params_for(self, name):
        return space.c1_params() if (name or "c1") == "c1" else space.base_params()

    def consume_queue(self):
        QUEUE_DIR.mkdir(exist_ok=True)
        (QUEUE_DIR / "done").mkdir(exist_ok=True)
        files = sorted(p for p in QUEUE_DIR.glob("*.json"))
        for f in files:
            if self.out_of_budget():
                return
            try:
                item = json.loads(f.read_text())
            except Exception as e:  # noqa: BLE001
                self.log(f"queue {f.name}: bad json {e!r}")
                shutil.move(str(f), str(QUEUE_DIR / "done" / (f.name + ".bad")))
                continue
            kind = item.get("kind", "candidate")
            origin = item.get("origin", "queue")
            island = item.get("island", "queue")
            parent = item.get("parent")
            base = self.base_params_for(item.get("base"))
            if parent and self.db.get(parent):
                base = json.loads(self.db.get(parent)["params"])
            n = 0
            if kind == "candidate":
                params = dict(base)
                params.update({k: space.clamp(k, v) for k, v in (item.get("params") or {}).items() if k in space.SPACE})
                blocks = item.get("blocks") or None
                self.evaluate(params, blocks, [parent] if parent else [], f"{origin}:{f.stem}", island, item.get("note"))
                n = 1
            elif kind == "factorial":
                axes = {k: v for k, v in (item.get("axes") or {}).items() if k in space.SPACE}
                bopts = item.get("block_options") or {}
                names = list(axes) + [f"block:{b}" for b in bopts]
                levels = [axes[k] for k in axes] + [bopts[b] for b in bopts]
                for combo in itertools.product(*levels):
                    if self.out_of_budget():
                        break
                    params = dict(base)
                    blocks = {}
                    tag = []
                    for name, val in zip(names, combo):
                        if name.startswith("block:"):
                            if val:
                                blocks[name[6:]] = val
                                tag.append(name[6:])
                        else:
                            params[name] = space.clamp(name, val)
                            tag.append(f"{name}={val}")
                    self.evaluate(params, blocks or None, [parent] if parent else [], f"{origin}:{f.stem}", island,
                                  note="factorial " + " ".join(tag))
                    n += 1
            self.log(f"queue {f.name}: {kind}, {n} candidates")
            shutil.move(str(f), str(QUEUE_DIR / "done" / f.name))

    # ---------------------------------------------------------------- generation
    def seed_islands(self):
        for name, cfg in ISLANDS.items():
            if not cfg["seed"]:
                continue
            p = self.base_params_for(cfg["seed"])
            key = space.params_key(p)
            row = self.db.get(key)
            if row is None:
                self.log(f"seeding island {name} from {cfg['seed']}")
                self.evaluate(p, None, [], f"seed:{cfg['seed']}", name)
            elif row.get("island") != name and name in ("v312", "c1"):
                pass  # same params can live in one island only; the shared seed is fine

    def pools(self):
        allp = self.db.alive(k_sha=self.k_sha, frontier=self.args.frontier)
        by = defaultdict(list)
        for r in allp:
            by[r.get("island") or "c1"].append(r)
        return allp, by

    def generate_one(self, island):
        allp, by = self.pools()
        pool = by.get(island) or []
        cfg = ISLANDS[island]
        if not pool and island == "queue":
            return False
        if not pool:
            pool = by.get("c1") or allp
        if not pool:
            return False
        if self.rng.random() < MIGRATE and allp:
            parent = self.rng.choice(allp[:10])
            origin = "migrate"
        else:
            parent = pick_parent(pool, self.rng)
            origin = "mutate"
        pparams = json.loads(parent["params"])
        pblocks = load_blocks(parent)
        if len(pool) >= 2 and self.rng.random() < CROSSOVER:
            other = self.rng.choice(pool[:40])
            child = space.crossover(pparams, json.loads(other["params"]), self.rng)
            # blocks: take each block from either parent
            ob = load_blocks(other) or {}
            cb = {}
            for b in set(pblocks or {}) | set(ob):
                src = (pblocks or {}).get(b) if self.rng.random() < 0.5 else ob.get(b)
                if src:
                    cb[b] = src
            self.evaluate(child, cb or None, [parent["key"], other["key"]], "crossover", island)
        else:
            child = space.mutate(pparams, rate=cfg["rate"], sigma_frac=cfg["sigma"], rng=self.rng)
            self.evaluate(child, pblocks, [parent["key"]], origin, island)
        return True

    # ---------------------------------------------------------------- main
    def run(self):
        main_pid = os.getpid()

        def _stop(signum, _frame):
            if os.getpid() != main_pid:
                return
            self.stop = True
            self.log(f"signal {signum}: stop requested; finishing current candidate")

        signal.signal(signal.SIGTERM, _stop)
        signal.signal(signal.SIGINT, _stop)
        try:
            self.seed_islands()
            order = [i for i in ISLANDS if ISLANDS[i]["seed"]]
            while not self.out_of_budget():
                self.consume_queue()
                if self.out_of_budget():
                    break
                self.gen += 1
                island = order[self.gen % len(order)] if self.gen % 4 else "queue"
                if not self.generate_one(island):
                    self.generate_one("c1")
        finally:
            close_pool()
            elapsed = time.time() - self.t_start
            counts = self.db.counts(self.run_id)
            games = sum(g for _, g in counts.values())
            summary = {"elapsed_s": round(elapsed), "evaluated": self.stats["evaluated"],
                       "counts": {k: v[0] for k, v in counts.items()}, "games": games,
                       "games_per_hour": round(games / max(elapsed, 1) * 3600)}
            self.db.finish_run(self.run_id, summary)
            self.log(f"done: {json.dumps(summary)}")
            out = report_mod.write_report(self.db, self.run_id)
            self.log(f"report: {out}")
            export_archive(self.db, self.run_id, self.k_sha, self.args.frontier)
            self.log(f"archive: {ARCHIVE}")
            self.logf.close()


def export_archive(db, run_id, k_sha, frontier=None):
    """Machine-readable state for the proposer and the Mac-side task."""
    c1 = space.c1_params()
    rows = db.alive(k_sha=k_sha, frontier=frontier)
    by = defaultdict(list)
    for r in rows:
        by[r.get("island") or "c1"].append(r)

    def slim(r):
        p = json.loads(r["params"])
        return {"key": r["key"], "island": r.get("island"), "origin": r["origin"], "status": r["status"],
                "dev": r["dev_margin"], "dev_t": r["dev_t"], "dev_wl": [r["dev_wins"], r["dev_losses"]],
                "clone": r["clone_margin"], "held": r["held_margin"], "held_t": r["held_t"], "held_clone": r["held_clone_margin"],
                "diff_vs_c1": {k: [a, b] for k, (a, b) in space.diff(p, c1).items()},
                "blocks": sorted(json.loads(r["blocks"]).keys()) if r.get("blocks") else [],
                "ablation": json.loads(r["ablation"]) if r.get("ablation") else None,
                "diag": r.get("diagnosis"),
                "exec": json.loads(r["exec_summary"]) if r.get("exec_summary") else None,
                "descriptor": json.loads(r["descriptor"]) if r.get("descriptor") else None,
                "note": r.get("note")}

    counts_all = db.counts()
    held = sorted([r for r in rows if r["status"] in ("held_pass", "held_fail")], key=lambda r: -(r["held_margin"] or -1e9))
    imp = report_mod.knob_importance(db.all(), c1)
    dead = [dict(r) for r in db.conn.execute(
        "SELECT origin, note, smoke_margin, status, diagnosis FROM candidates WHERE status IN ('dead_smoke','error') ORDER BY created DESC LIMIT 40")]
    # execution gap between C1 and the frontier tape (clone) on seed 1 -- the standing diagnosis for the LLM
    run = db.run(run_id) or {}
    frontier_gap = None
    try:
        import trace as trace_mod
        c1_path = space.render(c1)
        if run.get("clone"):
            g = trace_mod.traced(str(c1_path), str(run["clone"]), 1)
            dg = trace_mod.diagnose(g["trace"][0], g["trace"][1], "C1", Path(run["clone"]).stem)
            frontier_gap = {"text": dg["text"], "c1": trace_mod.summary_row(g["trace"][0]), "tape": trace_mod.summary_row(g["trace"][1])}
    except Exception as e:  # noqa: BLE001
        frontier_gap = {"error": repr(e)[:200]}
    out = {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "run_id": run_id, "chassis_sha": k_sha, "frontier": run.get("frontier"), "clone": run.get("clone"),
        "summary": json.loads(run["summary"]) if run.get("summary") else None,
        "counts_all_runs": {k: v[0] for k, v in counts_all.items()},
        "islands": {name: [slim(r) for r in lst[:10]] for name, lst in by.items()},
        "held_out": [slim(r) for r in held[:20]],
        "param_importance": [{"param": k, "spread": round(s), "best": b, "c1": c, "means": m} for s, k, b, c, m in imp[:20]],
        "recent_dead": dead,
        "frontier_gap": frontier_gap,
        "reference": {"c1": slim(db.get(space.params_key(c1))) if db.get(space.params_key(c1)) else None},
    }
    ARCHIVE.write_text(json.dumps(out, indent=1, default=str))
    return ARCHIVE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=0.0)
    ap.add_argument("--minutes", type=float, default=0.0)
    ap.add_argument("--max-candidates", type=int, default=0)
    ap.add_argument("--jobs", type=int, default=None)
    ap.add_argument("--frontier", default=str(ROOT / "candidates" / "V3_12.py"))
    ap.add_argument("--clone", default=str(ROOT / "Opponents" / "opp_scenario_v14.py"))
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--smoke-floor", type=float, default=DEFAULTS["smoke_floor"])
    ap.add_argument("--dev-promote", type=float, default=DEFAULTS["dev_promote"])
    ap.add_argument("--db", default=None)
    ap.add_argument("--base", default=None, help="chassis file to snapshot (default evolve/chassis.py)")
    args = ap.parse_args()
    Loop(args).run()


if __name__ == "__main__":
    main()
