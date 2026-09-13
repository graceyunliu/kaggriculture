# Crop Capacity Evidence Repair — Claude Audit Handoff

Status: **no STOP/PROMOTE verdict assigned**. No O42 modification, intervention,
new game simulation, or panel generation occurred.

## 1. Independent provenance verification

The existing 320 compressed traces were reparsed from scratch with the existing
analysis program and outcomes manifest:

```bash
python3 tools/analyze_decision_provenance.py \
  --panel-dir adaptive/logs/decision_provenance_panel_s301_340 \
  --outcomes adaptive/logs/o42_conflict_s301_340_games.json \
  --out adaptive/logs/crop_capacity_evidence_repair/provenance_rerun.json
```

The regenerated output is byte-identical to the published analysis:

```text
620977466ffcb9c6a26e0c58b4f0110ae13682daba99593c868bf466932c33f8
```

for both `provenance_rerun.json` and
`decision_provenance_panel_s301_340/decision_bottleneck_analysis.json`.

### What provenance independently supports

- Actual seed-ranking choice-set size does not differ: 5.000 candidates per
  ranking invocation in both cohorts.
- Candidate-reached and best-selected totals do not pass the declared
  reproducibility gate.
- Weak games have more recorded ranked seed orders and more committed seed units.
- Zero-quantity rejection is higher in strong games; demand-room rejection is
  higher in weak games.
- Weak games expose larger actual crop-task pools, more feasible unit-task pairs,
  and more assignments.
- The provenance trace does not observe crop-task submitted/committed/executed
  endpoints or asset-linked production/sale endpoints.

### What provenance does not support

Provenance alone does **not** establish the prior crop STOP. It shows no simple
“weak games receive fewer seed choices/orders” bottleneck, but it cannot prove
that the observed guard/order differences are downstream of already-diverged
state, nor can it exclude an execution or persistence bottleneck at its unobserved
stages.

The analysis field `earliest_reproducible_day` means only **first observed day
within this instrument**. It is neither first instrumented day nor an established
upstream divergence.

Definitions used in this handoff:

- **First observed:** earliest day an emitted metric passes the analysis gate.
- **First instrumented:** earliest day the relevant event could have been emitted;
  this depends on the traced code path and game reachability and was not separately
  estimated here.
- **Established upstream divergence:** a replicated difference shown to precede
  the compared downstream stage without conditioning on already-diverged state.
  No crop divergence has this status from provenance alone.

## 2. Lifecycle reproducibility

All 320 expected lifecycle JSONL files exist locally for four opponents, both
seats, and seeds 301–340. The existing lifecycle analyzer was rerun without game
simulation:

```bash
python3 tools/analyze_early_capacity_ledger.py \
  --panel-summary adaptive/logs/o42_conflict_s301_340_games.json \
  --ledger-dir adaptive/logs/early_capacity_ledger/canonical_s301_340 \
  --out adaptive/logs/crop_capacity_evidence_repair/lifecycle_rerun.json
```

The regenerated output is byte-identical to the pre-existing lifecycle analysis:

```text
f85c091dcf1a7228133f338aaaf13c4eab17781cfe3502af658affe44491a8ed
```

for both `lifecycle_rerun.json` and
`early_capacity_ledger/canonical_s301_340_analysis.json`.

This establishes local computational reproducibility of the reported lifecycle
statistics. It does **not** by itself certify the lifecycle instrumentation or turn
observational stage order into causality. The raw lifecycle ledger directory and
its analyzer were present locally but were not tracked in the shared Git commit at
the time of this repair; Claude should treat that provenance/sync limitation as an
explicit audit item.

## 3. Repaired interpretation

The lifecycle output exactly reproduces these descriptive findings:

- no robust strong-cohort advantage in per-crop capacity created or productive
  occupancy through day 10;
- robust higher melon realized yield in the strong lifecycle quartile;
- robust higher submitted/committed wheat seed in the weak lifecycle quartile;
- no asset-linked sale/use attribution.

The provenance and lifecycle analyses use different predeclared cohorts:

- provenance: positive versus negative final margin (52/268);
- lifecycle: opponent-seat-demeaned top/bottom quartiles (80/80).

Their numbers must not be pooled. Agreement or disagreement across these cohort
definitions is descriptive robustness information only.

## 4. Audit question

Claude should issue an independent A/B/C assessment of whether:

1. the existing local lifecycle ledger and analyzer are trustworthy enough to
   support descriptive use;
2. the narrower evidence establishes a reproducible decision bottleneck;
3. the investigation should be STOPPED or PROMOTED under the user's rule.

Until that audit, the crop verdict remains suspended. No intervention or crop
promotion is authorized.
