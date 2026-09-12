# Decision provenance anchor repair validation

This directory contains the repaired fixed-shop parity smoke. It is instrumentation
validation only; no outcome or strategy analysis was performed.

## Reproduction

```bash
KAGG_FIXED_SHOPS=1 python3 tools/o42_decision_provenance.py \
  --smoke \
  --seeds 303-303 \
  --opponents peter,alaylm,bahaen,yangk \
  --out-dir adaptive/logs/decision_provenance_smoke_repaired_v2
```

Result: 8/8 paired games passed money, step-count, error-count, full action-stream
SHA256, and terminal-observation SHA256 parity. All source anchors resolved to one
AST-structural match in their intended function.

The fixed-shop panel reached `seed_reject_zero_quantity` 119 times and did not reach
`seed_labor_reduction`. Therefore this directory does not claim complete runtime
coverage of both repaired events.

## Targeted semantic smoke

```bash
python3 tools/o42_decision_provenance.py \
  --smoke \
  --seeds 303-303 \
  --opponents peter \
  --out-dir adaptive/logs/decision_provenance_semantic_smoke_repaired
```

Result: 2/2 paired games passed all parity criteria. The repaired labor-reduction
event executed 3 times and the zero-quantity rejection event executed 41 times;
their runtime semantic predicates were asserted at every event.

The semantic regression also demonstrates the rejected ordinal bindings directly:

- `seed_labor_reduction`: legacy first textual match line 552; structurally intended
  line 627, under the seed load-model `while` guard.
- `seed_reject_zero_quantity`: legacy second textual match line 631; structurally
  intended line 629, under `if k <= 0` and immediately before `continue`.

The machine-readable binding details, source context, context hashes, structural
selectors, and uniqueness results are in `anchor_binding_manifest.json`.

O42 SHA256 remained
`154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`.
Phase 1 remains unaccepted pending independent re-audit.
