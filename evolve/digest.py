#!/usr/bin/env python3
"""Deterministic digest of the evolution archive (no LLM). Used for the morning notification.

    python3 evolve/digest.py            # print digest
    python3 evolve/digest.py --alerts   # print only "beats C1" lines (empty if none) -- for event alerts
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCHIVE = HERE / "archive.json"
STATE = HERE / "logs" / "alerted.json"


def fmt(v):
    return "—" if v is None else f"{v:+,.0f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alerts", action="store_true")
    a = ap.parse_args()
    if not ARCHIVE.exists():
        print("no archive.json yet")
        return 1
    d = json.loads(ARCHIVE.read_text())
    c1 = (d.get("reference") or {}).get("c1") or {}
    c1_held = c1.get("held")
    held = d.get("held_out") or []
    beats = [r for r in held if r.get("status") == "held_pass" and c1_held is not None and (r.get("held") or -1e9) > c1_held
             and r.get("key") != c1.get("key")]

    if a.alerts:
        seen = set(json.loads(STATE.read_text())) if STATE.exists() else set()
        new = [r for r in beats if r["key"] not in seen]
        for r in new:
            print(f"BEATS C1: {r['key']} [{r.get('island')}/{r.get('origin')}] held {fmt(r.get('held'))} (t {r.get('held_t', 0):.1f}) "
                  f"vs C1 {fmt(c1_held)}; clone {fmt(r.get('held_clone'))}; changes: "
                  + (", ".join(f"{k} {v[0]}→{v[1]}" for k, v in (r.get('diff_vs_c1') or {}).items()) or "none")
                  + ("; blocks: " + ",".join(r.get("blocks")) if r.get("blocks") else "")
                  + (f"; note: {r['note'][:120]}" if r.get("note") else ""))
        STATE.parent.mkdir(exist_ok=True)
        STATE.write_text(json.dumps(sorted(seen | {r["key"] for r in beats})))
        return 0

    s = d.get("summary") or {}
    L = [f"Kaggriculture evolve — {datetime.now().strftime('%a %b %d %H:%M')}"]
    L.append(f"Yardstick: {Path(d.get('frontier') or '?').name} + {Path(d.get('clone') or '?').name}. "
             f"C1 reference held-out: {fmt(c1_held)}.")
    if beats:
        L.append(f"BEATS C1: {len(beats)} candidate(s)")
        for r in beats[:5]:
            L.append(f"  {r['key']} [{r.get('island')}/{r.get('origin')}] held {fmt(r.get('held'))} t{r.get('held_t', 0):.1f} "
                     f"clone {fmt(r.get('held_clone'))} :: " + (r.get("note") or ", ".join(f"{k} {v[0]}→{v[1]}" for k, v in (r.get('diff_vs_c1') or {}).items()))[:110])
    else:
        L.append("Nothing beats C1 on held-out yet.")
    if held:
        top = held[0]
        L.append(f"Best held-out: {top['key']} {fmt(top.get('held'))} (t{top.get('held_t', 0):.1f}, {top.get('dev_wl')}) "
                 f"[{top.get('island')}/{top.get('origin')}]" + (f" :: {top['note'][:90]}" if top.get("note") else ""))
        if top.get("diag"):
            L.append(f"  why: {top['diag'][:220]}")
    fg = d.get("frontier_gap") or {}
    if fg.get("text"):
        c1e, te = fg.get("c1") or {}, fg.get("tape") or {}
        L.append(f"Gap to frontier tape: {fg['text'][:200]}")
        L.append(f"  travel/task C1 {c1e.get('travel_per_task')} vs tape {te.get('travel_per_task')}; missed_feed {c1e.get('missed_feed')} vs {te.get('missed_feed')}; "
                 f"missed_water {c1e.get('missed_water')} vs {te.get('missed_water')}; sales {fmt(c1e.get('sales'))} vs {fmt(te.get('sales'))}")
    counts = d.get("counts_all_runs") or {}
    L.append(f"Last segment: {s.get('evaluated', 0)} candidates, {s.get('games', 0):,} games ({s.get('games_per_hour', 0):,}/h). "
             f"Cumulative: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    llm = [r for isl in (d.get("islands") or {}).values() for r in isl if str(r.get("origin", "")).startswith("llm")]
    llm += [r for r in held if str(r.get("origin", "")).startswith("llm")]
    seen = set()
    llm = [r for r in llm if not (r["key"] in seen or seen.add(r["key"]))]
    llm.sort(key=lambda r: -(r.get("dev") or -1e9))
    L.append(f"LLM proposals in archive: {len(llm)}")
    for r in llm[:3]:
        L.append(f"  {r['key']} dev {fmt(r.get('dev'))} held {fmt(r.get('held'))} :: {(r.get('note') or '')[:100]}")
    abl = [r for r in held if r.get("ablation")]
    if abl:
        L.append("Ablations (loss if reverted):")
        for r in abl[:4]:
            items = sorted(((v if v is not None else 0), k) for k, v in r["ablation"].items())
            best = items[-1]
            dead = [k for v, k in items if v <= 0]
            L.append(f"  {r['key']}: carries: {best[1]} ({best[0]:+,}); dead weight: {', '.join(dead) or 'none'}")
    imp = d.get("param_importance") or []
    if imp:
        L.append("Signal: " + "; ".join(f"{p['param']}={p['best']} (${p['spread']:,})" for p in imp[:5]))
    isl = d.get("islands") or {}
    L.append("Islands: " + "; ".join(f"{k}: best {fmt(v[0].get('dev'))} n{len(v)}" for k, v in isl.items() if v))
    if counts.get("error"):
        L.append(f"WARNING: {counts['error']} candidates errored")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
