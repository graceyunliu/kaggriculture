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
