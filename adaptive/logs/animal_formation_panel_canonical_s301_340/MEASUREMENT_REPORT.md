# Canonical Animal-Formation Provenance Panel

Status: measurement-only complete; stopped before intervention or strategy work.

## Panel and validation

- 320 games: seeds 301–340, Peter/Alaylm/Bahaen/Yangk, both seats, fixed shops.
- Strong = positive final own-minus-opponent money; 52 strong, 268 weak, no ties.
- Exact instrumented/baseline action-stream and terminal-state parity: 320/320.
- Lifecycle conservation: 320/320.
- O42 SHA-256:
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`.

The canonical run exposed one tracer-wrapper defect before the final panel: the
observational wrapper directly indexed a hand after the engine had removed it.
The final panel uses the minimal repair: obtain the unit position through the
engine's real `_farmer_position`; when it returns `None`, call the original
engine function and return without emitting an animal action event. The accepted
anchors and O42 were unchanged. An eight-game four-opponent smoke, single-escape
fixture, and simultaneous-escape fixture passed before the final panel.

## Primary result

**The first reproducible strong/weak difference is observable by day 8 at the
committed animal-purchase/placement/ledger-addition boundary.** At day 8, strong
games have 9.962 cumulative committed animal purchases versus 8.724 in weak
games (opponent×seat-residualized difference +1.238, Welch p=7.72e-12,
BH q=1.67e-11). Every committed purchase in this panel maps one-for-one to a
successful placement and a lifecycle addition, so the daily resolution cannot
separate those three counts further. Within engine event order, purchase commit
precedes placement, and placement precedes the ledger addition.

This is the first **reproducible observation**, not a causal origin. The trace
does not capture the full pre-purchase animal opportunity, internal selection,
affordability, or constraint set. It therefore cannot establish whether the
day-8 purchase difference is an O42 choice/constraint effect or a consequence of
already-different economic state.

## Lifecycle map

| Measured stage | Strong | Weak | Residualized difference | Earliest replicated day | Classification |
|---|---:|---:|---:|---:|---|
| Rebuild calls | 719.000 | 719.000 | 0.000 | none | Control/exposure count |
| Repeated animal observations | 8507.115 | 7044.328 | +1461.091 | day 8 for mean pool | B: downstream of formed capacity |
| Mean `v["animals"]` observation pool | 11.832 | 9.797 | +2.032 | day 8 | B: downstream consequence |
| Committed animal purchases | 15.346 | 12.190 | +3.146 | day 8 cumulative | C: earliest boundary; causal source unresolved |
| Genuine successful placements | 15.346 | 12.190 | +3.146 | day 8 cumulative | C at same daily gate; no placement loss observed |
| Lifecycle additions / surrogate IDs formed | 15.346 | 12.190 | +3.146 | day 8 cumulative | B relative to purchase commit |
| Terminal persistent surrogate IDs | 15.269 | 12.138 | +3.119 | not separately day-tested | B: additions minus rare removals |
| Lifecycle removals | 0.077 | 0.052 | +0.027 | none | C: no reproducible divergence |
| Escape removals | 0.077 | 0.052 | +0.027 | none | C: no reproducible divergence |
| Mean route-entry candidate pool | 12.883 | 10.553 | +2.328 | day 8 | B: downstream of formed capacity |

“Repeated animal observations” counts real appends during each rebuild of
`v["animals"]`; it is explicitly **not** a count of animal formations.

## Day-8 validation gate

For cumulative purchase/placement/addition count, the residualized strong-minus-
weak difference is +1.238. It has the same direction in both seed halves
(+1.026, +1.449), both seats (+1.238, +1.238), and all leave-one-opponent-out
checks (+1.110 to +1.465). Opponent-specific differences are also positive:
Alaylm +2.184, Bahaen +0.610, Peter +1.357, Yangk +1.657.

For mean route-entry pool on day 8, the residualized difference is +1.135
(p=1.03e-10, q=2.20e-10), with positive opponent-specific differences from
+0.485 to +1.881 and essentially identical seat differences (+1.135, +1.134).

Days 5–7 contain some nominal or FDR-significant contrasts, but none passes the
declared replication gate across both seed halves and every leave-one-opponent-
out check. Day 8 is therefore the first reproducible detection gate under the
predeclared rule.

## Removal and escape accounting

There were 18 lifecycle removals/escapes across the panel: four among 52 strong
games and fourteen among 268 weak games. The per-game difference is small and
not significant after residualization (p=0.547, q=0.597), with no reproducible
day gate. Removal does not explain the candidate-pool divergence.

## Interpretation boundary and stopping result

- No reproducible O42-controlled animal choice or binding constraint was
  established.
- The observed purchase boundary is upstream of placement, persistence,
  repeated observation, and route-entry pool differences, but its own upstream
  decision context is unobserved here.
- Accordingly, purchase formation is classified **C (descriptive / causality
  unresolved)**, while later pool and persistence differences are classified
  **B (downstream consequences of already-diverged formed capacity)**.
- No stage qualifies as **A** from this instrument alone.

Per the stopping rule, no strategy recommendation, intervention, or optimization
is proposed. The raw panel remains local and is excluded from the audit commit.
