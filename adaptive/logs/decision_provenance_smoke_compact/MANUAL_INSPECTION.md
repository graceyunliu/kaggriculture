# O42 Decision Provenance smoke inspection

Scope: seed `303`, four canonical opponents, both seats, fixed shops. The eight
instrumented runs were paired with untouched O42 runs.

## Integrity checks

- 8/8 paired games matched final money, step count, error count, complete action-stream SHA256,
  and complete terminal-observation SHA256.
- O42 SHA256: `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`.
- 1,725,375 provenance records were parsed from the eight compressed JSONL logs.
- Every record containing a source line was compared with the same numbered line in O42:
  0 source-text mismatches.
- Family coverage: seed economy 25,065 records; orchestration 1,472,535; animal routes
  155,386; site selection 352; task stealing 70,632.

## Representative source reconciliations

The following records were inspected in `alaylm_seat0_seed303.jsonl.gz`.

1. Seed candidate: `economy:603`, day 1 hour 1. Candidate `STRAWBERRY` appears in local `c`;
   the recorded source is the actual combined eligibility guard.
2. Seed rejection: `economy:615`, day 10 hour 3. `MELON` had `room_units=2.0`; execution
   reached the `continue` immediately below the half-unit room guard.
3. Seed winner: `economy:624`, day 1 hour 1. Actual local `best` was
   `(108.3333, MELON, 5.0)` when execution reached tuple unpacking.
4. Seed order: `economy:632`, day 2 hour 1. Actual selected item was `STRAWBERRY`, `k=2`,
   when execution reached the real `seed_orders` mutation.
5. Orchestrator feasible pair: `_orchestrate:1022`, day 0 hour 1. Unit 0/task 0 had
   distance 0 and actual cost 1.0 when execution reached `pairs.append`.
6. Orchestrator assignment: `_orchestrate:1028` selected that unit/task. A later actual
   pair reached collision rejection at `_orchestrate:1027`.
7. Animal route: `_build_route:733`, day 0 hour 7 exposed two real pending, unclaimed sheep.
   `_build_route:759` then appended `(2,4)` as the first real stop.
8. Site selection: `_pick_site:822`, day 0 hour 2 contained 24 feasible empty sites and
   executed the real shed-distance/coordinate tie-break return.
9. Task stealing: `_steal_task:969`, day 5 hour 13 reached a real three-task sweep;
   `_steal_task:978` executed the selected transfer.

These checks establish execution provenance, not correctness or causal value. A line event on an
`if` statement means the guard was reached; only a subsequent anchored `continue`, assignment, or
return establishes its outcome.

## Known limitations

- The tracer records only candidates materialized by the five scoped O42 functions.
- Alternatives outside those functions are unobserved, not rejected.
- List comprehensions expose their resulting candidate lists, not per-element branch events.
- Python line tracing exposes executed lines and locals; it does not directly expose the Boolean
  value of a compound expression. Guard outcome is established only where control flow reaches a
  uniquely anchored successor line.
- Orchestrator logs are large because each genuinely feasible pair and directly observed rejection
  is retained. Compressed logs are canonical for audit.
- No outcome, winner/loser, causal, scoring, or optimization analysis was performed.
