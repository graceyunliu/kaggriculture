# Regime matrix (Sep 4 night) — does the best policy differ by opponent regime?

Question: among existing held-out-qualified candidates, is the per-regime winner a different file from the overall winner by more than noise? If not, a runtime router has nothing to route to.

Pools (held-out seeds 11–30, both seats, master engine): R0 mirror tapes = strawhats, yuan800, atakan, iamlonely, yangkuang; R1 basin-B tapes = shirabe, kiro, antigone; R2 own-code = V3_12, E1, opp_scenario_v14. Data: `tools/regime/matrix.json` (16 × 11), script `tools/regime/matrix.py`.

| candidate | R0 | R1 | R2 |
|---|---:|---:|---:|
| H32 | **+23,369** | **+19,759** | **+42,969** |
| H31 | +4,348 | +19,466 | +42,022 |
| M1_k1 (H31 sells 1 step early) | +4,373 | +18,981 | +41,577 |
| H30 | +2,013 | +17,437 | +41,692 |
| H12 | −12,809 | −4,639 | +18,947 |
| H10 | −25,770 | −4,639 | +18,947 |
| E_e4a4 | −26,689 | −21,557 | +10,004 |
| P5 | −26,966 | −19,994 | +9,984 |
| E1 | −30,090 | −24,455 | +9,664 |
| C1 | −29,675 | −22,733 | +5,151 |
| V3_12 | −32,316 | −24,757 | −143 |

Answer: **no regime-specific winner exists among current candidates.** H32 tops all three; the H30/H31/M1 tier is within $1k of it in R1/R2. H32's R0 lead is a single opponent (strawhats +$84.7k via the cash-starvation opening; other R0 tapes +$2k–$4k over H31). A router over these files would always choose H32.

Where adaptation does pay is inside the opening, not between policies: M2 (`candidates/M2.py`, other session) reads the opponent's turn-0 wheat buy from market inventory and picks the turn-1 sell that starves that specific tape — +$66k/+$147k/+$109k vs yuan800/atakan/strawhats, identical to H32 elsewhere. That is opponent-conditional play at the market layer with one policy body.

Decision: do not add per-regime scoring to the evolve loop or a policy router to the agent now. Re-run this matrix when (a) a runtime-adaptive own-code policy is within ~$5k of the tapes, or (b) a new tape family appears on the ladder that M2's opening does not break.
