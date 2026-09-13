# Animal Escape Runtime Smoke — Audit Handoff

Scope: deliberately minimal runtime validation only. No O42 strategy code or
existing tracer/anchor implementation was changed. No canonical panel was run.

## Reproduction

From `/Users/graceliu/Claude/Projects/Kaggriculture`:

```bash
python3 tools/validate_animal_escape_runtime.py \
  --out-dir adaptive/logs/animal_escape_runtime_smoke

python3 tools/o42_animal_formation_provenance.py \
  --smoke --seeds 303-303 --opponents peter \
  --out-dir adaptive/logs/animal_escape_runtime_smoke/o42_parity
```

The first command is a deterministic validation fixture. It creates identical
baseline and instrumented engine states with a matching pasture and one cow in
unit inventory. Placement, daily-refresh escape, and replacement all execute
through the real engine functions. It is not a natural O42 gameplay episode and
must not be used for strategy or outcome analysis.

The second command is an ordinary untouched-O42 paired smoke (seed 303, Peter,
both seats) used independently to confirm action-stream and terminal-state
parity.

## Result

- One real `animal_escape` and one corresponding
  `animal_left_farm_tiles` event were observed.
- Retired surrogate: `p0:x4y4:d0:e1`.
- Replacement surrogate at the same site: `p0:x4y4:d1:e2`.
- All runtime invariants in `escape_validation_summary.json` passed.
- Fixture action-stream and terminal-state parity passed.
- Ordinary O42 parity passed for 2/2 games, including exact action-stream and
  terminal-observation hashes.
- O42 SHA-256 remained
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`.

## Semantic detail for audit

`animal_escape.animal_before` is the state immediately before the real engine
refresh removes the animal. `animal_left_farm_tiles.state` is the most recent
prior observation snapshot. They intentionally need not have identical
`consecutive_unfed` values. The validation checks immediate pre-removal state
against `animal_escape.animal_before`, and identity retirement against
`animal_left_farm_tiles`.

## Artifacts

- `escape_validation_summary.json`: fixture scope, IDs, invariants, and explicit
  untested cases.
- `escape_lifecycle.jsonl`: complete placement/escape/removal/replacement ledger.
- `o42_parity/smoke_summary.json`: ordinary O42 paired parity summary.
- `o42_parity/*.jsonl.gz`: ordinary O42 traces for both seats.
- `o42_parity/anchor_binding_manifest.json`: unchanged anchor manifest emitted by
  the accepted tracer.

## Explicitly untested

- A naturally occurring escape during O42 gameplay.
- Multiple simultaneous escapes.
- Non-escape removal causes.
- Sheep or goose escape.
- Surrogate identity across position changes (engine animals do not move).

Stop here for independent audit. No 320-game panel was run.
