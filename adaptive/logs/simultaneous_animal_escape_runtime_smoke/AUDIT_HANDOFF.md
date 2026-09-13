# Simultaneous Animal Escape Runtime Smoke — Audit Handoff

This is a validation-only deterministic fixture. It does not establish that
simultaneous escapes occur naturally in O42 gameplay. No canonical panel was
run. O42 and the accepted tracer/anchor implementation were not changed.

## Reproduction

From `/Users/graceliu/Claude/Projects/Kaggriculture`:

```bash
python3 tools/validate_simultaneous_animal_escape_runtime.py \
  --out-dir adaptive/logs/simultaneous_animal_escape_runtime_smoke

python3 tools/o42_animal_formation_provenance.py \
  --smoke --seeds 303-303 --opponents peter \
  --out-dir adaptive/logs/simultaneous_animal_escape_runtime_smoke/o42_parity
```

The fixture executes itself twice. Its two JSONL event streams must be byte
identical or it fails closed.

## Runtime result

- Both cows escaped through the real engine `_daily_refresh_animals` call in
  the same refresh.
- Two distinct `animal_escape` events and two distinct
  `animal_left_farm_tiles` events were recorded.
- Retired IDs: `p0:x4y4:d0:e1`, `p0:x3y4:d0:e2`.
- Replacement IDs: `p0:x4y4:d1:e3`, `p0:x3y4:d1:e4`.
- Removal snapshot size changed exactly `2 -> 0`.
- Both retired IDs appeared in exactly one removal and neither was reused.
- Removal events have distinct positions and sequence numbers; neither was
  overwritten or collapsed.
- Ledger removal snapshot was empty and matched the baseline real-engine state.
- Fixture action-stream and terminal-state parity passed.
- Repeated fixture event logs were byte-identical, SHA-256
  `e0f31fcdc1bdefc345c1be3fb019b34d9013c954d5293362379ff2069c5477a8`.
- Ordinary untouched-O42 parity passed for both seats (2/2 games), including
  exact action-stream and terminal-observation hashes.
- O42 SHA-256 remained
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`.

## Artifacts

- `simultaneous_escape_summary.json`: all runtime invariants and hashes.
- `simultaneous_escape_run1.jsonl`: first lifecycle event stream.
- `simultaneous_escape_run2.jsonl`: independently repeated lifecycle stream.
- `o42_parity/smoke_summary.json`: ordinary O42 paired parity summary.
- `o42_parity/*.jsonl.gz`: ordinary O42 traces for both seats.
- `o42_parity/anchor_binding_manifest.json`: manifest emitted by the unchanged
  accepted tracer.

## Explicitly untested

- Simultaneous escapes arising naturally during O42 gameplay.
- More than two simultaneous escapes.
- Non-escape animal removal causes.

Stop here for Claude's final independent A/B/C audit. No 320-game panel has
been run or authorized by this smoke.
