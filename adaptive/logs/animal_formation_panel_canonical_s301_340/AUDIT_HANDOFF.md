# Animal Formation Canonical Panel — Audit Handoff

## Reproduction

The four isolated shards were run in parallel from the repository root:

```bash
for opponent in peter alaylm bahaen yangk; do
  KAGG_FIXED_SHOPS=1 python3 tools/o42_animal_formation_provenance.py \
    --seeds 301-340 --opponents "$opponent" \
    --out-dir "adaptive/logs/animal_formation_panel_canonical_s301_340/$opponent" &
done
wait
```

Analysis command:

```bash
python3 tools/analyze_animal_formation_panel.py \
  --panel-dir adaptive/logs/animal_formation_panel_canonical_s301_340 \
  --out adaptive/logs/animal_formation_panel_canonical_s301_340/animal_formation_analysis.json
```

## Validation

Each opponent shard contains 80 paired games and reports `parity_passed: true`
and `lifecycle_conservation_passed: true`. Together these cover 320/320 games.
Every shard reports O42 SHA-256
`154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`.

## Concrete wrapper repair requiring audit

An earlier serial attempt stopped on an `IndexError` before producing a panel
summary. The engine can invoke `_apply_unit_action` for a hand index after that
hand has been removed; the original engine uses `_farmer_position` and silently
returns when it yields `None`. The observational wrapper had directly indexed
`farm["hands"][idx-1]` first.

The only tracer change is in `Ledger.install.apply`: it now calls the real
engine `_farmer_position`; if the result is `None`, it calls the saved original
function exactly once and returns without emitting an animal action event. No
O42 source or AST/source anchor changed. Before the canonical rerun, the repair
passed an eight-game smoke covering all opponents and both seats, plus the
single- and simultaneous-escape fixtures.

## Artifact policy

The 320 compressed JSONL logs and repeated anchor manifests remain local under
the four opponent directories and are intentionally not staged or pushed.
Committed audit artifacts are limited to:

- this handoff;
- the measurement report;
- the complete compact analysis JSON;
- four shard parity summaries;
- the analysis program;
- the one-line-path wrapper repair.

No intervention, strategy change, or outcome-driven optimization was run.
