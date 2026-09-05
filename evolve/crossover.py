"""Archive-driven, block-wise crossover queue generator."""
from __future__ import annotations

import json
import random
from datetime import datetime
from pathlib import Path


def recombine(parent_a, parent_b, rng=random):
    """Return a queue candidate recombining complete DB rows by parameter and block."""
    pa, pb = json.loads(parent_a["params"]), json.loads(parent_b["params"])
    params = {k: (pa[k] if rng.random() < 0.5 else pb.get(k, pa[k])) for k in pa}
    params.update({k: v for k, v in pb.items() if k not in params})
    ba = json.loads(parent_a["blocks"]) if parent_a.get("blocks") else {}
    bb = json.loads(parent_b["blocks"]) if parent_b.get("blocks") else {}
    blocks = {}
    for name in sorted(set(ba) | set(bb)):
        source = ba.get(name) if rng.random() < 0.5 else bb.get(name)
        if source:
            blocks[name] = source
    return {
        "kind": "candidate", "base": "c1", "params": params, "blocks": blocks,
        "parents": [parent_a["key"], parent_b["key"]],
        "origin": "archive_crossover", "island": "queue",
        "note": f"block-wise archive crossover {parent_a['key']} x {parent_b['key']}",
    }


def queue_top_crossovers(db, queue_dir, generation, rng=random, top_k=10, count=2,
                         k_sha=None, frontier=None):
    """Select distinct top-K archive parents and enqueue a few recombinations."""
    pool = db.alive(limit=top_k, k_sha=k_sha, frontier=frontier)
    if len(pool) < 2:
        return []
    queue_dir = Path(queue_dir)
    queue_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    written = []
    for i in range(count):
        a, b = rng.sample(pool, 2)
        item = recombine(a, b, rng)
        path = queue_dir / f"crossover_g{generation:06d}_{stamp}_{i}.json"
        path.write_text(json.dumps(item))
        written.append(path)
    return written
