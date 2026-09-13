# BUY_ANIMAL Commit-Result Panel — Audit Handoff

## Scope and result

This panel measures only the boolean returned by the real engine `_commit_unit`
when `op == "BUY_ANIMAL"`. Across the canonical 320 games there were:

- `committed=True`: 4,065
- `committed=False`: 0

Therefore there is no failure-rate divergence and no earliest failure day. The
successful-commit volume contrast independently reproduces first at day 8, but
this does not support any inference about candidate generation, affordability,
or why O42 submitted different numbers of orders.

## Canonical panel

- Opponents: Peter, Alaylm, Bahaen, Yangk.
- Seeds: 301–340.
- Both seats: 320 games.
- Fixed shops enabled.
- Strong/weak cohort definition matches the certified formation panel: positive
  versus negative final own-minus-opponent money (52 strong, 268 weak).

## Reproduction

```bash
for opponent in peter alaylm bahaen yangk; do
  KAGG_FIXED_SHOPS=1 python3 tools/o42_buy_animal_commit_panel.py \
    --seeds 301-340 --opponents "$opponent" \
    --out "adaptive/logs/buy_animal_commit_panel_s301_340/$opponent.json" &
done
wait

python3 tools/analyze_buy_animal_commits.py \
  --panel-dir adaptive/logs/buy_animal_commit_panel_s301_340 \
  --certified-panel-dir adaptive/logs/animal_formation_panel_canonical_s301_340 \
  --out adaptive/logs/buy_animal_commit_panel_s301_340/analysis.json
```

## Evidence retained

Each opponent JSON contains every game identifier, seed, opponent, seat, final
money, exact action and terminal hashes, every observed engine commit-result
event with item/day/hour/step, and exact per-day true/false counts. These four
files are sufficient to reconstruct all aggregates.

`analysis.json` contains the complete exact
`committed × day × cohort × opponent × seat` cross-tab, residualized daily tests,
seed-half checks, opponent/seat strata, and leave-one-opponent-out checks.

## Validation

- Focused instrumented/baseline parity: 320/320.
- Exact action hash, terminal hash, and final-money match against the certified
  formation-panel records: 320/320.
- O42 SHA-256 remained
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`.
- O42 and the engine were not modified.
- The wrapper records the saved original `_commit_unit` return value after
  calling it exactly once.

No strategy, intervention, candidate model, or affordability analysis was
introduced.
