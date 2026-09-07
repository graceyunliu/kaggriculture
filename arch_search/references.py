"""arch_search/references.py -- the Phase 0 reference panel, built from real files inspected
in Opponents/ and Opponents/tapes.json (not guessed from filenames).

Selection method: Opponents/tapes.json records each tape's actual final `money` and a
`fingerprint` string (its opening/mid-game order sequence, e.g. "BUYWH53 | SELWH48 BUYCO2
BUYSH2 HIR HIR HIR HIR HIR BUYWH7 BUYME12"). Inspecting all 17 entries (see
`python3 -c` dump in the Phase 0 report) shows:

  - 8 of 17 tapes share one template: 5 HIR (hire) actions, BUYCO2 (2 cows), BUYSH2 (2 sheep),
    BUYWH7 (7 wheat), BUYME12 (12 melon), a wheat round-trip buy/sell -- differing only in the
    exact wheat round-trip size and day ordering. This matches memory's "93.2% shared-clone
    fingerprint" finding closely enough (8/17 here vs. the ~440-tape population memory sampled)
    to be confidently the same family. tape_atakan_104893687.py is picked as its representative:
    it has the exact canonical fingerprint string and a middling money outcome for the family
    ($107,245), avoiding cherry-picking the family's best or worst instance.

  - tape_jessebullard_105876759.py is the clearest minority "budget fork": fingerprint
    "BUYCO2 | HIR HIR HIR HIR HIR BUYSH1" -- cow-heavy, only 1 sheep, no melon/wheat
    round-trip at all, and the lowest hire count of any tape in the panel-eligible set,
    at $115,519. This matches memory's "budget fork: cow-only, land day10" description in
    spirit (much lighter animal/crop diversification than the shared-clone template).

  - Three tapes are picked as "meaningfully divergent, independently strong" agents --
    strong (money within the panel's upper range) but with fingerprints that don't match
    either template above:
      * tape_strawhats_105080848.py ($175,524, the single highest-money tape in the file) --
        fingerprint "BUYWH43 | SELWH38 BUYWH7 BUYME12 HIR HIR HIR HIR HIR BUYCO2 BUYSH2" --
        much larger wheat round-trip (43/38 vs the clone's ~53/48 -- similar shape, different
        scale, and different action ordering: wheat trade BEFORE hiring, not after).
      * tape_kronki_99169921.py ($135,975) -- fingerprint "BUYWH4 HIR HIR BUYME7 BUYWH5 BUYSH4
        | " -- no SELWH round-trip pattern at all, animals bought later/lighter, action order
        interleaves hiring and buying rather than front-loading all HIR together.
      * tape_kwa_105860490.py ($133,821) -- fingerprint "HIR HIR HIR BUYSH2 BUYCO2 BUYME1
        BUYWH1 BUYWH5 | BUYSH1 HIR HIR HIR SELWH5 BUYWH13 BUYCA4" -- hires BEFORE any animal
        purchase (clone template hires after), buys CARROT (BUYCA) which no other panel member
        does, and splits its hiring across two waves (day-0 group of 3, later group of 3 more).

- candidates/V3_12.py is the current champion (confirmed via memory + evolve/README /
  evolve/space.py's KNOBS docstring "K -- knob-parameterized V3.12 chassis" and
  docs/*sep05* notes: "frontier = V3_12 per Grace"). It is NOT part of the reference panel
  (it is the thing being compared AGAINST the panel) and this module never modifies it.

Each reference is run seat 0 vs. candidates/V3_12.py seat 1 (V3_12 as a neutral fixed
opponent) so all five panel trajectories share the same opposing pressure; this is separate
from testing V3_12 itself, which is run seat 0 vs. Opponents/opp_scenario_v14.py (a real,
independent opponent) so its own trajectory isn't self-referential.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from arch_search.trajectory import Trajectory, extract_trajectory

ROOT = Path(__file__).resolve().parent.parent

REFERENCE_PANEL: Dict[str, Dict[str, str]] = {
    "shared_clone": {
        "path": "Opponents/tape_atakan_104893687.py",
        "reason": "Representative of the 8/17-tape shared fingerprint family (5xHIR, "
                   "BUYCO2, BUYSH2, wheat round-trip, BUYME12); median money in that family.",
    },
    "budget_fork": {
        "path": "Opponents/tape_jessebullard_105876759.py",
        "reason": "Clearest minority template: cow-heavy (BUYCO2), only 1 sheep, no wheat "
                   "round-trip or melon buy -- much lighter diversification than the clone.",
    },
    "divergent_strawhats": {
        "path": "Opponents/tape_strawhats_105080848.py",
        "reason": "Highest-money tape in tapes.json ($175,524); wheat round-trip BEFORE "
                   "hiring (clone template hires first), larger round-trip size.",
    },
    "divergent_kronki": {
        "path": "Opponents/tape_kronki_99169921.py",
        "reason": "No SELWH round-trip pattern at all; interleaves hiring/buying rather "
                   "than front-loading hires; strong ($135,975).",
    },
    "divergent_kwa": {
        "path": "Opponents/tape_kwa_105860490.py",
        "reason": "Hires before any animal purchase (reverse of clone order); buys CARROT "
                   "(unique in this set); two-wave hiring; strong ($133,821).",
    },
}

CHAMPION = {
    "path": "candidates/V3_12.py",
    "reason": "Current champion per repo memory/docs (evolve/space.py's K.py docstring: "
              "'knob-parameterized V3.12 chassis'; docs sep05 notes: frontier = V3_12).",
}

# Fixed opposing pressure for panel extraction: V3_12 itself, so all 5 panel members face
# the same opponent and only THEIR OWN trajectories vary. Champion's own trajectory is
# extracted against a genuinely independent opponent instead (see build_reference_panel()).
PANEL_OPPONENT = "candidates/V3_12.py"
CHAMPION_OPPONENT = "Opponents/opp_scenario_v14.py"


def build_reference_panel(seed: int = 1, engine: str = "master") -> Dict[str, Trajectory]:
    """Extract Trajectory objects for every panel member (seat 0, vs PANEL_OPPONENT)."""
    out = {}
    for name, spec in REFERENCE_PANEL.items():
        out[name] = extract_trajectory(str(ROOT / spec["path"]), str(ROOT / PANEL_OPPONENT),
                                        seed, seat=0, engine=engine, label=name)
    return out


def build_champion_trajectory(seed: int = 1, engine: str = "master") -> Trajectory:
    return extract_trajectory(str(ROOT / CHAMPION["path"]), str(ROOT / CHAMPION_OPPONENT),
                               seed, seat=0, engine=engine, label="champion_V3_12")
