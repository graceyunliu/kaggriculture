#!/usr/bin/env python3
"""Research-direction ledger + evidence contract (AGE-361 / AGE-362, Sep 11).

  python3 evolve/directions.py            # validate evolve/directions.yaml and print the ledger
  python3 evolve/directions.py --check TYPE N_SEEDS N_SETS   # is this evidence deep enough for a decision?

The ledger (`directions.yaml`) records every direction as DO / DELAY / ABANDON / SWITCH with the evidence that produced
the state. The evidence contract (`EVIDENCE_CONTRACT`) says how much evidence a claim of each intervention type needs
before the loop or a person is allowed to move it to DO or ABANDON -- the empirical rules from Sep 9-11:
  * dev-seed selection alone is never enough (M=89 won dev and lost held-out);
  * lumpy capital flips sign between 12 and 32 cells;
  * market-interaction claims need BOTH own money and margin (exploits: margin up, own down; spillovers: own up, margin flat);
  * a one-seed observational table is a hypothesis, not a weight (VaR).
Rendered into the proposer prompt (propose.py) and the run report (report.py).
"""
from __future__ import annotations
import sys, os
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "directions.yaml"
STATES = ("DO", "DELAY", "ABANDON", "SWITCH")
TYPES = ("calibration", "knob", "threshold", "nonlinear_threshold", "lumpy_capital", "architecture", "market_interaction")

# Evidence contract: minimum panel depth before a direction of this type may be moved to DO (promote) or ABANDON (close).
#   seeds_per_set: paired seeds per panel run (x 5 opponents on the tape panel)
#   sets: independent seed sets that must agree in sign (dev AND held-out / fresh)
#   metrics: which panel metrics must clear the floor
#   note: the failure mode this depth guards against
EVIDENCE_CONTRACT = {
    "calibration":         dict(seeds_per_set=20, sets=2, metrics=("margin", "own"), t_min=2.0,
                                note="a corrected constant should show on every tape; if it is tape-specific it is not a calibration"),
    "knob":                dict(seeds_per_set=20, sets=2, metrics=("margin", "own"), t_min=2.0,
                                note="never select the value on the dev set alone (M=89)"),
    "threshold":           dict(seeds_per_set=20, sets=2, metrics=("margin", "own"), t_min=2.0, dose_response=True,
                                note="show the dose-response (interior optimum), pick the parameter on held-out"),
    "nonlinear_threshold": dict(seeds_per_set=20, sets=2, metrics=("margin", "own"), t_min=2.0, segmented=True,
                                note="fixed-cutoff sweep segmented by observable state BEFORE building adaptation"),
    "lumpy_capital":       dict(seeds_per_set=32, sets=2, metrics=("margin", "own"), t_min=2.0,
                                note="12-cell results flipped sign at 24-32 cells (AGE-360); marginal caps, not class ablation"),
    "architecture":        dict(seeds_per_set=20, sets=2, metrics=("margin", "own"), t_min=2.0, parent_comparison=True,
                                note="compare to the immediate parent, not the frontier; h2h is a weak ranking signal"),
    "market_interaction":  dict(seeds_per_set=20, sets=3, metrics=("margin", "own"), t_min=2.0,
                                note="both metrics on 3 sets: exploit = margin up/own down; spillover = own up/margin flat; only own+margin up is core"),
}

REQUIRED = {
    "DO":      ("mechanism", "intervention", "evidence"),
    "DELAY":   ("mechanism", "unknown", "resolving_measurement", "would_do"),
    "ABANDON": ("hypothesis", "negative_evidence", "scope"),
    "SWITCH":  ("original_hypothesis", "failed_assumption", "became", "evidence"),
}


def load():
    import yaml
    rows = yaml.safe_load(LEDGER.read_text()) or []
    ids = set()
    for r in rows:
        assert r.get("state") in STATES, f"{r.get('id')}: bad state {r.get('state')}"
        assert r.get("type") in TYPES, f"{r.get('id')}: bad type {r.get('type')}"
        missing = [k for k in REQUIRED[r["state"]] if k not in r]
        assert not missing, f"{r['id']}: {r['state']} record missing {missing}"
        assert r["id"] not in ids, f"duplicate id {r['id']}"
        ids.add(r["id"])
    for r in rows:
        if r["state"] == "SWITCH":
            assert r["became"] in ids, f"{r['id']}: became -> unknown direction {r['became']}"
    return rows


def enough_evidence(itype, seeds_per_set, sets, metrics_cleared):
    """True if a decision of this intervention type is allowed on this evidence."""
    c = EVIDENCE_CONTRACT[itype]
    return seeds_per_set >= c["seeds_per_set"] and sets >= c["sets"] and all(m in metrics_cleared for m in c["metrics"])


def render(rows, states=STATES, max_chars=6000):
    """Compact text for the proposer prompt / report."""
    out = []
    for st in states:
        rs = [r for r in rows if r["state"] == st]
        if not rs:
            continue
        out.append(f"## {st}")
        for r in rs:
            if st == "DO":
                out.append(f"- {r['id']} [{r['type']}]: {r['mechanism']} -> {r['intervention']}. Evidence: {r['evidence']}")
            elif st == "DELAY":
                out.append(f"- {r['id']} [{r['type']}]: unknown = {r['unknown']}. Resolve by: {r['resolving_measurement']}. DO if: {r['would_do']}")
            elif st == "ABANDON":
                out.append(f"- {r['id']} [{r['type']}]: {r['hypothesis']} -- {r['negative_evidence']}. Scope: {r['scope']}." + (f" Reopen only if: {r['reopen']}" if r.get("reopen") else ""))
            else:
                out.append(f"- {r['id']} -> {r['became']}: {r['original_hypothesis']} failed because {r['failed_assumption']}")
    text = "\n".join(out)
    return text if len(text) <= max_chars else text[:max_chars] + "\n..."


def contract_text():
    return "\n".join(f"- {k}: >= {v['seeds_per_set']} seeds x {v['sets']} independent sets, metrics {'+'.join(v['metrics'])}, t>={v['t_min']}. {v['note']}"
                     for k, v in EVIDENCE_CONTRACT.items())


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        t, n, s = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
        c = EVIDENCE_CONTRACT[t]
        ok = n >= c["seeds_per_set"] and s >= c["sets"]
        print(f"{t}: {'ENOUGH' if ok else 'NOT ENOUGH'} -- need >= {c['seeds_per_set']} seeds x {c['sets']} sets on {'+'.join(c['metrics'])}; {c['note']}")
        sys.exit(0 if ok else 1)
    rows = load()
    print(f"{len(rows)} directions: " + ", ".join(f"{st} {sum(1 for r in rows if r['state']==st)}" for st in STATES))
    print(render(rows))
    print("\n# evidence contract\n" + contract_text())
