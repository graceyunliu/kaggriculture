# Animal Formation Provenance — Independent Audit Handoff

This is the pre-panel validation gate. The canonical 320-game run has **not** been
started and must not start until Claude independently audits this commit.

## Reproduction

```bash
KAGG_FIXED_SHOPS=1 python3 tools/o42_animal_formation_provenance.py \
  --smoke \
  --seeds 303-303 \
  --opponents peter \
  --out-dir adaptive/logs/animal_formation_smoke_audit_final
```

Result: 2/2 games passed money, steps, errors, action-stream SHA256, and terminal-state
SHA256 parity. Both games passed lifecycle entry/exit conservation and post-placement
ID uniqueness. O42 SHA256 remained
`154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`.

## Instrument boundaries

- O42 `perceive()` animal-key guard and append are observed by the existing fail-closed
  AST resolver.
- Existing audited `_pick_site` and `_build_route` events connect site choice and final
  route-entry contents.
- Engine purchase, pickup/place, and daily escape functions are wrapped observationally;
  originals are called exactly once.
- Engine mutation source anchors are independently recorded in
  `anchor_binding_manifest.json` with function, exact line, structural node types,
  context, context hash, and uniqueness.
- Farm-tile snapshots provide before/after collection sizes and state transitions.

## Persistent identity

The engine exposes no native animal ID. After successful placement, the ledger assigns
the explicit surrogate:

`p<seat>:x<X>y<Y>:d<placed_day>:e<placement_epoch>`

Identity is not claimed before placement. Purchase lots, shed units, and carried units
are recorded as flows but cannot be linked one-to-one to a later placed animal.

## Smoke observations and limitations

- Each seat recorded 11 committed purchases and 11 placed farm-tile entries.
- All 22 entries had origin `placed`; none was unresolved.
- IDs were unique within both runs.
- The smoke produced no animal escape. Escape anchors are statically bound, but escape
  mutation/conservation lacks runtime coverage in this smoke. This must be considered
  explicitly in the audit verdict.
- `v["animals"]` is reconstructed on every O42 call; it is not itself persistent.
  Persistence belongs to the underlying farm tile, represented by the post-placement
  surrogate ID.
- “Never generated” means no successful engine placement/farm-tile entry occurred.
  “Generated then removed” requires a recorded farm-tile entry followed by an escape
  removal. The instrument does not infer hypothetical animals from absent purchases.

## Requested audit checks

1. Verify O42 `perceive` AST anchors bind to the intended animal guard and append.
2. Verify engine purchase/place/escape anchors bind to the intended mutations.
3. Verify wrappers call originals exactly once and do not mutate inputs afterward.
4. Verify entry/exit conservation and surrogate-ID lifecycle logic.
5. Verify `perceive_animal_append` counts and route-entry contents agree with farm-tile
   snapshots for representative turns.
6. Decide whether missing runtime escape coverage requires a different smoke before the
   canonical panel.

No outcome analysis or strategy analysis has been performed.
