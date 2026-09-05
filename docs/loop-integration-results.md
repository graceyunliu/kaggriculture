# Always-on loop integration results

Date: 2026-09-05  
Branch: `codex/loop-integration`

## Planner queue integration

The four planner files satisfy the existing typed-block contracts without adapters:

- `planner_hiring.py`: `_hire_plan`, `_load_model`
- `planner_dispatch.py`: `_unit_action`
- `planner_sweep.py`: `_build_sweep`, `_crop_step` (and its private helper)
- `planner_animal_routing.py`: `_build_route`, `_route_step`

Queue items can now refer to repository-relative block files with `{"path": ...}` instead of embedding large source strings. `planner_hiring_split.json` crosses both hiring arms with setup-capital shares 0.15/0.25/0.35 and recurring-labor buffers 25/75 while holding the other three planner blocks together. New planner constants are present in `space.py`; defaults are centered on the validated planner values (`FERT_RADIUS=2`, `SPREAD_W=1.0`, `SPREAD_CAP=5`).

The split hiring arm reserves a configurable lumpy setup-capital share first, then funds recurring hires from the independent remainder and buffer. It does not reuse P7's failed immediate-affordability blend.

Verification:

```text
contracts and path-backed queue sources: ok
render: /tmp/kag-loop-render/cand_cfe57bffc628.py
```

Bounded loop command:

```text
python3 evolve/loop.py --minutes 10 --max-candidates 1 --jobs 1 \
  --queue-dir /tmp/kag-loop-integration.7wy7df \
  --db /tmp/kag-loop-integration.7wy7df/evolve.db \
  --run-id loop-integration-queue
```

Relevant output:

```text
#1 planner_hiring_split:planner_hiring_split acccba77d8cd [queue] blocks=animal_routing,dispatch,hiring,sweep
dev +5,239 (t=2.9, 9-1) clone +12,369
HELD-OUT +4,002 (t=3.7, 16-4) clone +19,121 -> PASS
queue planner_hiring_split.json: factorial, 1 candidates
done: {"elapsed_s": 230, "evaluated": 1, "games": 128, ...}
```

This is an integration smoke result, not a promotion or strategy claim. The one-candidate cap intentionally stopped the factorial after one cell. A debugging fix now retains a factorial when a budget expires mid-design instead of discarding its remaining cells.

## Structured rejected mechanisms

`evolve/db.py` now creates and seeds `rejected_mechanisms`, with `id`, `mechanism_tag`, `verdict`, `one_line_cause`, `doc_ref`, and `date`. The three seeded records are:

- `opponent_fingerprint_sizing` / `rejected`
- `shared_market_inventory_threshold_fix` / `no_general_fix`
- `blended_capital_labor_constraint` / `rejected`

`propose.build_prompt()` includes these rows under `CLOSED MECHANISMS (do not re-propose)`.

Verification:

```text
rejected rows: [('opponent_fingerprint_sizing', 'rejected'),
 ('shared_market_inventory_threshold_fix', 'no_general_fix'),
 ('blended_capital_labor_constraint', 'rejected')]
prompt closed-mechanisms section: ok
```

## Generator portfolio

The loop already had stochastic crossover inside `generate_one()`. The missing portfolio behavior was an explicit archive-to-queue generator. `evolve/crossover.py` now recombines two DB archive members by candidate key, independently chooses parameter values and whole typed blocks, records both parents, and periodically queues children from the top-K compatible archive members. Defaults: every 25 generations, top 10, two children; CLI flags can tune or disable this.

`tools/replay_imitation.py` AST-parses and decodes tape payloads without importing them. Its output contains only aggregate statistics and bounded `sweep`/`crop_admission` parameter suggestions. A three-tape check produced:

```text
mean_wheat_pickup_size: 4.153
mean_days_between_water_service_by_hand: 1.298
alternate_day_water_interval_share: 0.114
mean_crop_work_actions_per_active_day: 59.534
sweep suggestion: CROP_SWEEP_LEN=4, CROP_SWEEP_RADIUS=4
crop_admission suggestion: NEAR_RADIUS=3
crossover queue: parents ['a', 'b']; blocks ['hiring', 'sweep']
```

No action sequence is emitted or converted into a candidate.

## Clean limitations

- The concurrent main checkout contains a newer, uncommitted `planner_sweep.py` associated with P6. This branch does not copy or rewrite that claimed block body; the queue references the version-controlled planner block available at the branch point. Once the owning planner work is committed, merging that commit will automatically make the path-backed queue use the newer validated source.
- A hiring block's fixed `_hire_plan(target, have, hires_today, cash)` contract cannot receive a detailed prospective setup purchase ledger. The implemented arm therefore searches a clean cash-budget partition (setup share versus recurring labor plus buffer), not a larger admission/economy refactor. Such a refactor would cross the infrastructure-only boundary and was deliberately not forced.
- The smoke run evaluated one factorial cell, not all 12, because the deliverable was crash-free queue/render/cascade integration rather than a result search.
