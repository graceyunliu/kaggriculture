# Automatic Ladder Watcher

Adds `adaptive/research_loop/ladder_watcher.py`: a read-only poller so a
human no longer has to manually check Kaggle for when enough
Adaptive-v0.3-ladder-submission games have completed. It sits in front of
the existing Adaptive Research Loop v0.1 infrastructure
(`ladder_ingest.py`, `experiment_ledger.py`, `hypothesis_store.py`) and
triggers it -- it does not duplicate it.

## Flow

```
Kaggle ladder (live)
      |  KaggleLadderDataSource: EpisodeService/ListEpisodes,
      |  same bearer-token pattern pull_ladder.py already uses
      v
ladder_watcher.poll_once()
      |  1. discover_candidates() -- finds active submissions whose
      |     filename matches our candidate lineage (adaptive-v0.2/-v0.3/...)
      |  2. poll_submission() -- current games_completed / wins / losses /
      |     draws / rating
      |  3. write_raw_evidence() -- new, timestamped file every poll,
      |     never overwritten
      |  4. newly_crossed_checkpoints() -- compares against persisted
      |     completed_checkpoints; fires each configured threshold
      |     (default 10/20/30/50/100/200 games) at most once, however big
      |     the jump between polls
      v  (only on a newly crossed checkpoint)
trigger_research_loop_ingestion()
      |  writes state/checkpoint_diagnostics/<candidate>_checkpoint_<N>_games.json
      v
ladder_ingest.load_checkpoint_summary()      <- EXISTING module, extended
      |  reads + hashes the diagnostic (same pattern as
      |  load_v0_2_ladder_summary: read/hash, never re-derive)
      v
experiment_ledger.append_entry / append_result_update   <- EXISTING module,
      |  unchanged API                                      unmodified
      |  ladder_result = "CHECKPOINT: N_GAMES", observations explicitly
      |  says PARTIAL / not final
      v
(future) hypothesis_store.record_evidence + diagnostic_engine
      -- left for a human/research_loop.py run to interpret; the watcher
      itself never judges whether a checkpoint supports or contradicts a
      hypothesis (that judgment call belongs to diagnostic_engine.py,
      same separation of concerns as v0.1)
```

Terminal/log output on every checkpoint (always works, no external
notification service required):

```
LADDER CHECKPOINT REACHED
candidate: adaptive-v0.3
submission: <id>
games: 20
rating: <value>
Research-loop ingestion triggered.
```

## Configuration

- Checkpoints: `DEFAULT_CHECKPOINTS = (10, 20, 30, 50, 100, 200)` in
  `ladder_watcher.py`, overridable with `--checkpoints 10,20,30,50,100,200`.
  Never hard-coded elsewhere in the module -- every check reads this list
  (or a caller override) rather than repeating numbers.
- Poll interval: `--interval 300` (default 5 minutes).
- One-shot mode: `--once` (poll every lineage candidate once and exit).
- Competition slug: `--competition kaggriculture` (default).

## State

`adaptive/research_loop/state/ladder_watcher_state.json` -- one record per
candidate:

```json
{
  "candidate_id": "adaptive-v0.3",
  "submission_id": "...",
  "last_seen_game_count": 21,
  "last_seen_rating": 870,
  "last_poll_timestamp": "2026-09-13T...Z",
  "completed_checkpoints": [10, 20],
  "poll_history": [ ... ]
}
```

Written atomically (write-to-`.tmp` + `os.replace`) so a crash mid-write
never leaves a torn/unreadable state file. Raw per-poll evidence is written
to `adaptive/research_loop/state/raw_ladder_evidence/` as a new,
timestamped file every poll -- prior raw evidence is never overwritten.
Per-checkpoint diagnostics live in
`adaptive/research_loop/state/checkpoint_diagnostics/`.

## New-data detection

Checkpoint crossing does not assume the game count only increases by 1.
`newly_crossed_checkpoints(previous, current, already_completed, checkpoints)`
fires every configured threshold `<=` the new count that isn't already
marked completed -- so:

- `7 -> 13` fires `10` only.
- `13 -> 21` (after `10` already fired) fires `20` only.
- `21 -> 21` fires nothing (idempotent replay / restart).
- `7 -> 25` in one poll fires **both** `10` and `20`, each exactly once.

`new_games_since_previous_checkpoint` in each diagnostic is the gap between
the checkpoint just fired and the last checkpoint fired before it (e.g. for
the `7 -> 25` jump, checkpoint 10 reports 10 new games since 0, checkpoint
20 reports 10 new games since checkpoint 10).

## Diagnostic fields (per checkpoint)

`candidate, parent, submission_id, games_completed, wins, losses, draws,
rating, rating_change, checkpoint, new_games_since_previous_checkpoint`,
plus, where available, per-game `opponent_submission_id`, `opponent_name`,
`result`, `money_margin`, `replay_available`. Any field the data source
could not supply is recorded literally as the string `"unavailable"` --
never fabricated. `is_final_result: false` is always set on a checkpoint
diagnostic, and the ledger's `ladder_result` field is always labeled
`CHECKPOINT: N_GAMES` (never described as a final result).

## Reliability / safety

- **Auth failures fail clearly**: `LadderAuthError` on HTTP 401/403 or a
  missing/empty token file; never silently retried or swallowed.
- **Transient failures back off**: `LadderTransientError` on timeouts,
  connection errors, HTTP 5xx/429, retried with exponential backoff
  (5 attempts, base delay 2s) before surfacing.
- **Malformed responses never crash the watcher**: a poll result missing
  `games_completed`, or an exception during polling, is logged and skipped
  for that candidate this cycle; the next scheduled poll tries again.
- **No credentials in the repo**: the real data source reads
  `.kaggle/access_token` (same file `pull_ladder.py` already uses),
  nothing is hard-coded.
- **Read-only / no auto-submission**: `LadderDataSource` exposes only
  `discover_candidates()` and `poll_submission()`; `KaggleLadderDataSource`
  only ever issues GET/list-style HTTP calls (`submissions/list`,
  `EpisodeService/ListEpisodes`, both already used read-only by
  `pull_ladder.py`) -- there is no code path in this module that can call a
  Kaggle submission-creation endpoint. `run()` also calls
  `verify_o42_immutable()` at startup and refuses to run if O42's hash
  ever stops matching the certified
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813` --
  itself a read (`sha256_file`), never a write.

## Testing (`adaptive/research_loop/test_ladder_watcher.py`, mocked --
no live Kaggle access needed or attempted)

9 tests, all passing:

1. `test_sequential_checkpoints_and_idempotent_replay` -- 7 -> nothing,
   13 -> fires 10, 21 -> fires 20, 21 (repeat) -> nothing.
2. `test_big_jump_fires_both_checkpoints_once` -- 7 -> 25 in one poll fires
   10 and 20, each exactly once (verified via ledger + diagnostic-file
   counts).
3. `test_restart_persistence_no_refire` -- state reloaded from disk after
   a simulated process restart does not refire an already-completed
   checkpoint.
4. `test_transient_failure_does_not_crash` -- a scripted
   `LadderTransientError` is surfaced as a non-fatal error, state is not
   advanced, and the next poll succeeds normally.
5. `test_auth_failure_surfaced_clearly` -- an auth failure is surfaced as
   `fatal: true` rather than retried.
6. `test_malformed_response_does_not_crash` -- a response missing
   `games_completed`, and a `None` response, are both handled without
   raising.
7. `test_newly_crossed_checkpoints_helper` -- direct unit coverage of the
   checkpoint-math edge cases above.
8. `test_o42_hash_check_detects_mismatch` -- the immutability check passes
   against the real, unmodified O42 file and correctly flags a tampered
   copy.
9. `test_checkpoint_triggers_ledger_and_diagnostic` -- one checkpoint
   produces exactly one ledger row labeled `CHECKPOINT: 10_GAMES` /
   `PARTIAL`, and one diagnostic file with `is_final_result: false`.

```
$ python3 -m unittest test_ladder_watcher -v
...
Ran 9 tests in 0.006s
OK
```

## Verification performed

- `sha256sum candidates/O42_MAX_HANDS_LATE_EXPAND.py` ==
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`
  (matches the certified hash; unchanged by this work).
- `git diff --stat -- candidate/ candidates/` is empty -- no v0.2/v0.3
  candidate files were modified.
- Only files touched by this work: `adaptive/research_loop/ladder_watcher.py`
  (new), `adaptive/research_loop/test_ladder_watcher.py` (new),
  `adaptive/research_loop/ladder_ingest.py` (one function added,
  `load_checkpoint_summary`, nothing existing changed), this report, and
  `adaptive/research_loop/README.md`.

## What this deliberately does NOT do

No web server, no dashboard, no database server, no autonomous submission
service, no second hypothesis system, no complex event/notification
infrastructure. Plain JSON state + JSONL ledger (both pre-existing
formats in this repo) plus stdout logging are sufficient.

## STATUS: LADDER_WATCHER_READY
