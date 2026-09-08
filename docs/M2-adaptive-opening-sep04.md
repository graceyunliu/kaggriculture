# M2 — adaptive opening (Sep 4, night)

`candidates/M2.py`, `submissions/M2_ADAPTIVE_OPENING.zip`. H32 with one runtime decision.

## Mechanism

H32's edge is not the round-trip itself (a buy/sell round trip is free — the engine quotes BUYs at post-buy inventory) but its side effect: in lockstep with the opponent's own turn-0/turn-1 wheat round-trip it moves the wheat price by a few dollars at the exact steps where the cluster tapes buy feed with $20–50 of slack. Their feed buys or day-1 hires fail, animals go unfed, the herd escapes. Which opponent breaks depends on the quantity pair (buy n at turn 0, sell m at turn 1) — see `docs/opening-grid-sep04.txt` (seeds 1–6, both seats):

| (n, m) | vs yuan800 (53/48) | vs atakan (53/48) | vs strawhats (43/38) | vs iamlonely | vs yangkuang |
|---|---|---|---|---|---|
| H32 = (30, 25) | +$4.5k | +$6.4k | **+$96.9k** | +$14.9k | +$8.4k |
| (30, 24) | +$4.5k | +$6.4k | **+$119.0k** | +$14.9k | +$8.4k |
| (30, 18) | **+$70.4k** | **+$150.8k** | −$3.6k | −$5.1k | −$7.9k |
| (40, 30) | **+$89.1k** | **+$35.3k** | −$0.1k | +$11.3k | +$5.6k |
| (40, 38) | −$39.8k | −$36.8k | −$45.3k | −$9.6k | −$34.5k |

Knife-edge: (40, 38) starves *us*. No single pair breaks both classes.

The opponent's turn-0 wheat purchase is exact at turn 1 from the shared market inventory (`10000 − inventory − our 30 − 1`), so M2 keeps n = 30 and picks m at turn 1: opponent bought ≥ 48 → sell 18; 38–47 → sell 24; otherwise 25 (= H32). Every other step is H32's tape; guards unchanged.

## Held-out, seeds 11–30, both seats

| opponent | M2 margin | t | W-L | H32 (same seeds) |
|---|---:|---:|---:|---:|
| tape_yuan800 | **+$65,911** | 17.3 | 20-0 | +$5.1k |
| tape_atakan | **+$147,315** | 30.0 | 20-0 | +$5.8k |
| tape_strawhats | **+$109,345** | 19.3 | 20-0 | +$86.4k |
| tape_kiro | +$23,027 | 10.7 | 20-0 | +$28.0k |
| tape_antigone | +$14,589 | 5.2 | 19-1 | +$15.8k |
| tape_shirabe | +$21,660 | 10.0 | 20-0 | +$22.6k |
| tape_iamlonely | +$10,638 | 4.4 | 16-4 | +$10,638 (identical) |
| tape_yangkuang | +$11,758 | 5.1 | 19-1 | — |
| V3_12 | +$45,527 | 18.8 | 20-0 | — |
| H10 | +$51,912 | 15.7 | 20-0 | — |
| H32 | $0 | — | 0-0 (exact tie) | — |
| M2 (self) | $0 | — | 0-0 | — |

M2 is byte-for-byte H32 against every opponent outside the two classes, and turns the 53/48 cluster from a coin flip into a 20-0.

## Caveats

- Exploits a cash-starvation cascade in fixed tapes; any opponent that adapts its opening (or runs a different round-trip quantity) falls into "other" and gets H32 behaviour. Classes were fit on five tapes; new cluster variants may need their own (n, m) row — the grid takes ~2 min per pair.
- Symmetric risk: an opponent could do this to us. H32/M2's own day-1 feed buys already run at negative slack; the guard (75% money) would hand over to C1 if starved.
- Next: extend the same runtime decision to days 1–9 (choose our feed-buy/sell steps to keep our slack positive and theirs negative), and re-run the grid against any new top-30 tapes after the next ladder pull.

## Sep 5 ladder pull — the 13/8 lineage explains the slump

M2 2043.7 (clean 39-38, recent 7-9), H32 2020.1 (recent 5-15). In the last ~45 M2 games, ~14 opponents open `BUY 13 / SELL 8` with the same frontier opening otherwise (Furina #2, Hamachi, XW, Sergey Kutepov, Akshay, Hiro Nomo, ibr mo sal, SCLim, guruguru000, Toru59er, Aikyatan Sinha, nadhir hasan, ShaoCharles, Ignat) and M2 lost 12 of them by $1–10k. Tapes built: `Opponents/tape_furina_105708344.py`, `tape_hamachi_105670479.py`, `tape_xw_105683882.py`.

What it is: an improved twin of our own tape — only 245/719 steps differ (yuan800 differs on 698); same economy, one more cow, +18 strawberry, +21 milk (`decompose`: −$3.9k for us, 1-5 on seeds 1–6 both seats, identical for M2 and H32 since it classifies as "other").

What doesn't work against it (seeds 1–6, both seats, vs furina/hamachi):

| our opening | margin |
|---|---|
| 30/25 (M2, H32) | −$3.9k / −$4.3k |
| 30/29, 30/27 | −$42k / −$37k (starves us) |
| 30/23 … 30/17 | −$4.7k … −$5.6k |
| 30/15 | −$8.2k |
| 40/34, 40/30 | −$4.7k…−$7.9k / −$2.0k…−$5.6k |
| 20/15 | −$3.9k / −$4.2k |
| 13/8 (mirror them), 5/none | −$1.1k / −$1.2k |
| M2 + sell-shift k=1,2 | −$48k (breaks our own opening) |

No (n, m) pair starves it — this lineage has positive day-1 slack — so M2's "other" branch is already the best available; the residual −$1…−$4k is the twin's better mid-game, decided per seed. To beat it we need a better tape body or a better own economy, not a different opening.

## Sep 8 — M4 (turn-level tape ablation) and a fresh ladder loss audit

`candidates/M4.py`, `submissions/M4_TURN_ABLATION.zip`, pushed `main`@`d460bef7eb6f`. M2's copied tape (H32's, inherited from H30/H31/H32) was ablated turn-by-turn instead of touched wholesale: every one of the 247 steps with a market action was individually no-op'd and screened, combos of the survivors were checked against `_diverged()` via debug instrumentation (combining is **not additive** — several individually-positive removals push live animal/hand counts far enough from the recorded `_SIG` to trip the fallback guard and hand the rest of the game to the much weaker general dispatcher; this cost −$100k+ in more than one tested combo). Only one safe combo survived: dropping three redundant 1-unit `BUY_PRODUCT WHEAT` top-ups on day 4 (steps 97/101/103, a few hours apart, each buying a single unit at an already-elevated price for negligible benefit).

- 29-opponent replay panel, 3 seeds: M4 = **+$38,314/game, 69-18** vs M2's +$36,316/game, 68-19. No opponent regressed more than ~$400; zero agent errors.
- Follow-up search for 2 more candidates (M5–M28, 20 variants: single-step removals of every other micro-purchase in the tape — day-1 steps 31-39, day-6 steps 152-164, isolated COW/SHEEP/SEED/FERTILIZER buys at steps 65/88/108/143/168/176/226/241/264) — **all rejected**. Two (steps 145, 193 individually) looked positive on the 6-opponent loser subset but reversed to worse-than-M2 on the full 29-opponent panel (subset screening overfits). The rest were either exact no-ops or catastrophic divergence triggers (−$57k to −$164k on the 6-loser screen). **This tape has no more free wins from single- or paired-turn removal** — day 4's cluster was apparently the only isolated, non-load-bearing redundancy in it.

**Ladder pull (sub 56096391, `pull_ladder.py`), score 1567.2, real 56-9 across 66 games.** All 9 real losses are close (−$607 to −$25,662), no crashes/divergence on the ladder. Two loss pairs share byte-identical opponent openings (i.e. two more shared-clone instances, per `kaggriculture_opponent_strategy_identifiers.md`):
- Peter Parker / Baha Enes Ören: opp turn1 `BUYWH13`, turn2 `SELWH9 BUYWH7 BUYME12 HIR×5 BUYCO2 BUYSH2`. Margins −$18.2k / −$4.3k.
- As Long As You Love Me / Yangle Ma: opp turn1 `BUYWH13 SELWH13 BUYWH13` (buy-sell-buy churn), turn2 `SELWH13 BUYWH5 HIR×5 BUYCO2 BUYSH2`. Margins −$25.7k / −$14.5k — our two worst losses this pull.

Both open with the opponent buying 13 wheat, landing in M2/M4's "other" classifier bucket (n<38) — same bucket as the Sep 5 furina/hamachi twin-tape lineage above. **Caution before re-chasing this**: Sep 5 already ground through the full (n,m) grid against a 13/8-opening twin tape and found no sell quantity starves it (see table above) — "other" was already the best available response *for that specific tape body*. These two new pairs share the turn-1 signature but their turn-2 body (`SELWH9 BUYWH7 BUYME12...` / `SELWH13 BUYWH5...`) doesn't match furina/hamachi's, so they may be a distinct variant requiring their own tape diff before assuming the Sep 5 conclusion still holds. Next step if this is picked up: build tapes from these two replay pairs (`Replays/Auto/mine/episode-106816877-*.json` etc., already fetched) the same way `tape_furina_105708344.py` etc. were built, then re-run the (n,m) grid against them specifically rather than assuming "other" is unbeatable — don't skip straight to a new sell quantity without confirming the tape body first.

**Follow-up (same day): confirmed, Sep 5's conclusion generalizes.** Built 4 tapes from the loss replays (`Opponents/tape_peterparker_106816877.py`, `tape_alaylm_106813359.py`, `tape_bahaenes_106828159.py`, `tape_yangkuang2_106819729.py` — the 4 full 719-step bodies are NOT byte-identical within each pair despite matching turn-1/2 fingerprints, so genuinely 4 distinct opponents). Ran the same 14-point (n,m) grid (n∈{5,13,20,30,40}, m spanning 15–34) at 3 seeds both seats:
- **m never changes the outcome at all** — every n=30 variant (m=15…29) scored byte-identical margins against all 4 tapes. Our own turn-1 sell quantity is simply not the lever against this opener class; whatever decides these games happens elsewhere.
- n=30 (M2/H32 default) is a near-wash vs bahaenes/yangkuang2 (+$1.4k total) but a real loss vs peterparker/alaylm (−$24.0k total). n=40 flips it (−$17.0k vs peterparker/alaylm, but −$17.9k vs bahaenes/yangkuang2, worse than n=30 there). n=20/13/5 are all decisively worse everywhere (−$67k to −$104k).
- No single (n, m) choice is better than today's default across all 4 — confirms Sep 5: **this class of opener genuinely isn't solvable by tuning the turn-1 round-trip.** Closed again, now against 4 more real tape bodies. Don't re-run this grid against "other"-bucket ladder losses without a new hypothesis for *what* does decide them (likely mid/late-game economy, not the opening).
