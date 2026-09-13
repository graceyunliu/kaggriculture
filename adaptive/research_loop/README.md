# Adaptive Research Loop v0.1

Infrastructure so the Kaggriculture project can learn from successive ladder
submissions itself, instead of a human inspecting ladder results and saying
"try X." Implements: candidate -> ladder submission -> ladder result ->
diagnosis -> hypotheses -> evidence update -> next-experiment selection ->
ONE controlled candidate change -> next candidate (repeat).

See `../../ADAPTIVE_RESEARCH_LOOP_V0_1_REPORT.md` (repo root) for the full
report, and `../../ADAPTIVE_RESEARCH_LOOP_V0_1_AUDIT_HANDOFF.md` for what is
directly observed vs. reconstructed vs. unavailable.

## Modules

| File | Role |
|---|---|
| `experiment_ledger.py` / `experiment_ledger.jsonl` | Append-only provenance record, one row per candidate/experiment. Never overwrites; a later ladder result is a new `row_kind=result_update` row, folded at read time by `effective_rows()`. |
| `hypothesis_store.py` / `hypotheses.json` | The "research learner": persistent hypothesis registry with qualitative confidence (`NO_EVIDENCE`/`WEAK`/`MODERATE`/`STRONG`, each meaning fixed in code, not asserted per-hypothesis). |
| `ladder_ingest.py` | Reads the existing ladder diagnostic evidence at `artifacts/ladder_adaptive_v0.2_diagnostic_2026-09-13/` into the compact shape the rest of the loop uses. Does not re-pull Kaggle or recompute statistics that audit already computed. |
| `diagnostic_engine.py` | Generates hypotheses FROM evidence (not from a human saying "try being more conservative"); answers what-changed / what-happened / was-the-prediction-supported. |
| `experiment_selector.py` | Simple 5-factor heuristic (information value, cost, isolability, untested-ness, avoids-local-optimum) ranking which hypothesis to test next. Not a Bayesian optimizer. |
| `candidate_builder.py` | Turns a selected hypothesis into a candidate PLAN (version name, parent, one change, prediction) and runs the lightweight (not full-audit) validation checklist. Does not itself write controller code or touch O42/v0.2/v0.3. |
| `research_loop.py` | Orchestrates phases 1-6 read-only and prints the proposal. STOPS before submission -- a human must explicitly authorize SUBMIT (phase 6/7 boundary). Run: `python3 research_loop.py` from this directory. |
| `ladder_watcher.py` / `test_ladder_watcher.py` / `state/` | Automatic, read-only Kaggle ladder poller. Discovers active submissions in our candidate lineage, detects newly completed games and configurable checkpoints (default 10/20/30/50/100/200 games, no refire across restarts), and triggers `ladder_ingest.load_checkpoint_summary()` -> `experiment_ledger` on each new checkpoint, labeled `CHECKPOINT: N_GAMES` (never final). Never submits to Kaggle. See `../../ADAPTIVE_LADDER_WATCHER_REPORT.md`. |

## Three layers of learning (kept separate, per spec)

1. **Gameplay learner** -- `adaptive_slice_v0.py`'s frozen A/B controller: game state -> A/B choice. Untouched by this loop.
2. **Research learner** -- this directory: experiment evidence -> which hypotheses are promising.
3. **Candidate lineage** -- `experiment_ledger.jsonl`: parent -> change -> result, so nothing is silently forgotten or rediscovered.

## Ladder submission -> watcher -> checkpoint -> ingestion -> hypothesis update

Once a candidate is on the live ladder, a human no longer has to poll Kaggle
by hand:

```
human submits candidate to Kaggle (unchanged: still a human action)
        v
ladder_watcher.py polls Kaggle read-only on an interval (default 5 min)
        v
a configured game-count checkpoint (10/20/30/50/100/200) is newly crossed
        v
ladder_watcher writes a checkpoint diagnostic + calls
ladder_ingest.load_checkpoint_summary() (existing module, extended)
        v
experiment_ledger.append_entry/append_result_update records a PARTIAL,
explicitly-labeled `CHECKPOINT: N_GAMES` row (existing module, unmodified API)
        v
a human (or a future research_loop.py run) reviews the checkpoint and,
via diagnostic_engine.py / hypothesis_store.py, judges whether it
supports/contradicts a hypothesis -- the watcher itself never makes that
judgment call, same separation of concerns as the rest of this loop
```

See `../../ADAPTIVE_LADDER_WATCHER_REPORT.md` for the full design, the
`LadderDataSource` abstraction (mockable for tests, no live Kaggle access
needed to test checkpoint logic), and test results.

## Safety boundaries preserved

- O42 (`candidates/O42_MAX_HANDS_LATE_EXPAND.py`, sha256 `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`) was not modified by building this infrastructure. `candidate_builder.check_o42_immutable()` re-verifies this hash every run.
- `candidate/adaptive-v0.2-ladder-candidate/` and `candidate/adaptive-v0.3-ladder-candidate/` (pre-existing, unsubmitted) were inspected but not modified.
- No ladder submission was made by this work. `research_loop.py` prints a plan and stops at the human SUBMIT gate.
