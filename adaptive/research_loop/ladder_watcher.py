"""
ladder_watcher.py -- Adaptive Research Loop, Ladder Watcher

Replaces "a human periodically checks Kaggle" with a read-only poller that:

  1. identifies active submissions belonging to our candidate lineage
     (adaptive-v0.2-ladder-candidate, adaptive-v0.3-ladder-candidate, ...)
     via LadderDataSource.discover_candidates();
  2. periodically polls each one's game/result data
     (LadderDataSource.poll_submission);
  3. detects newly completed games / a changed rating vs. the last
     persisted observation;
  4. persists the latest observed state (never overwriting prior raw
     evidence -- each poll's raw response is written to a new file);
  5. detects which configured checkpoint thresholds (default 10, 20, 30,
     50, 100, 200 games) have newly been crossed, exactly once each, no
     matter how big the jump between polls (e.g. 7 -> 25 fires both the
     10 and 20 checkpoints, each exactly once; a re-poll at the same game
     count fires nothing);
  6. on a newly crossed checkpoint, triggers the EXISTING research-loop
     ingestion/ledger infrastructure (ladder_ingest.py, experiment_ledger.py)
     rather than building a second one;
  7. NEVER submits anything to Kaggle, and never touches O42 / v0.2 / v0.3
     candidate files. It only ever writes: its own state file, raw pulled
     ladder evidence, derived checkpoint diagnostics, and
     experiment_ledger.jsonl rows (via the existing, append-only
     experiment_ledger API).

Run once (single poll of all lineage candidates, then exit):
    python3 ladder_watcher.py --once

Run continuously (poll every 300s until Ctrl-C):
    python3 ladder_watcher.py --interval 300

Everything here is READ-ONLY with respect to Kaggle: it only ever issues
GET/list-style calls (via KaggleLadderDataSource, which wraps the same
requests-based calls pull_ladder.py already makes) and never calls any
Kaggle submission-creation endpoint.
"""
from __future__ import annotations

import argparse
import copy
import glob
import hashlib
import json
import os
import re
import sys
import time
import traceback
from typing import Optional

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RESEARCH_LOOP_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(RESEARCH_LOOP_DIR, "state")
STATE_PATH = os.path.join(STATE_DIR, "ladder_watcher_state.json")
RAW_EVIDENCE_DIR = os.path.join(STATE_DIR, "raw_ladder_evidence")
DIAGNOSTICS_DIR = os.path.join(STATE_DIR, "checkpoint_diagnostics")

if RESEARCH_LOOP_DIR not in sys.path:
    sys.path.insert(0, RESEARCH_LOOP_DIR)

import experiment_ledger as el  # noqa: E402
import ladder_ingest  # noqa: E402

O42_CANONICAL_HASH = "154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813"
O42_PATH = os.path.join(REPO_ROOT, "candidates", "O42_MAX_HANDS_LATE_EXPAND.py")

# Configuration: checkpoint games thresholds. Not hard-coded through the
# module -- everything downstream reads this list (or a caller-supplied
# override) rather than repeating the numbers.
DEFAULT_CHECKPOINTS = (10, 20, 30, 50, 100, 200)

# Which candidate-lineage filename prefixes the watcher looks for among the
# competition's submission list. Extend this, don't hard-code a specific
# submission id -- v0.3's live Kaggle submission id is discovered at poll
# time, not baked into this file.
CANDIDATE_LINEAGE_PREFIXES = (
    "adaptive-v0.2-ladder",
    "adaptive-v0.3-ladder",
    "adaptive-v0.4-ladder",  # forward-compatible; harmless if never used
)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def verify_o42_immutable() -> dict:
    """Read-only check that O42's canonical file still hashes to the
    certified value. Never writes to O42; raises nothing -- returns a
    result dict so a hash mismatch can be surfaced as data, not a crash."""
    if not os.path.exists(O42_PATH):
        return {"checked": False, "reason": f"O42 file not found at {O42_PATH}"}
    actual = sha256_file(O42_PATH)
    return {
        "checked": True,
        "path": os.path.relpath(O42_PATH, REPO_ROOT),
        "expected_hash": O42_CANONICAL_HASH,
        "actual_hash": actual,
        "matches": actual == O42_CANONICAL_HASH,
    }


# ---------------------------------------------------------------------------
# LadderDataSource abstraction
# ---------------------------------------------------------------------------
class LadderAuthError(RuntimeError):
    """Raised when Kaggle auth is missing/rejected. Never retried silently --
    the caller must surface this clearly rather than backing off forever."""


class LadderTransientError(RuntimeError):
    """Raised for retryable failures (timeouts, 5xx, connection errors)."""


class LadderDataSource:
    """Abstract read-only interface the watcher polls against. A real
    implementation talks to Kaggle; the test suite uses a scripted mock.
    Implementations MUST NOT provide any submit/create/write capability --
    by design this class only exposes read methods."""

    def discover_candidates(self) -> list:
        """Return a list of dicts: {candidate_id, submission_id, filename,
        parent_candidate}. One entry per active submission whose filename
        matches our candidate lineage."""
        raise NotImplementedError

    def poll_submission(self, submission_id) -> dict:
        """Return a dict describing the submission's current observed
        state:
          {
            "submission_id": ..., "games_completed": int,
            "wins": int, "losses": int, "draws": int,
            "rating": float | None,
            "games": [ {opponent_submission_id, result, margin, episode_id,
                        replay_available, ...}, ... ],   # per-game detail,
                                                          # "unavailable" for
                                                          # any field the
                                                          # source can't
                                                          # supply
            "raw": <opaque source-specific payload, stored verbatim as
                    raw evidence>,
          }
        Must raise LadderAuthError on authentication failure and
        LadderTransientError on a retryable failure. Any field that cannot
        be determined MUST be omitted or set to the string
        "unavailable" -- never fabricated.
        """
        raise NotImplementedError


class KaggleLadderDataSource(LadderDataSource):
    """Real implementation. Reuses the exact Kaggle access pattern
    pull_ladder.py already uses (bearer token in .kaggle/access_token,
    EpisodeService/ListEpisodes) instead of re-implementing it. Read-only:
    only issues GET/list-style requests."""

    def __init__(self, competition_slug: str = "kaggriculture", token_path: Optional[str] = None):
        self.competition_slug = competition_slug
        self.token_path = token_path or os.path.join(REPO_ROOT, ".kaggle", "access_token")
        self._requests = None  # lazily imported so the mock path needs no `requests` dependency

    def _session(self):
        if self._requests is None:
            import requests  # local import: keeps the mock/test path dependency-free
            self._requests = requests
        if not os.path.exists(self.token_path):
            raise LadderAuthError(
                f"No Kaggle access token at {self.token_path}. Auth is required to poll "
                f"the ladder; the watcher will not guess or fall back silently."
            )
        token = open(self.token_path).read().strip()
        if not token:
            raise LadderAuthError(f"Kaggle access token at {self.token_path} is empty.")
        return self._requests, {"Authorization": f"Bearer {token}"}

    def _get_json_with_retry(self, method: str, url: str, headers: dict, *, json_body=None,
                              max_attempts: int = 5, base_delay: float = 2.0):
        requests = self._requests
        last_exc = None
        for attempt in range(1, max_attempts + 1):
            try:
                if method == "GET":
                    r = requests.get(url, headers=headers, timeout=60)
                else:
                    r = requests.post(url, headers=headers, json=json_body, timeout=60)
            except Exception as exc:  # connection errors, timeouts, etc.
                last_exc = exc
                if attempt == max_attempts:
                    raise LadderTransientError(f"Transient failure calling {url}: {exc}") from exc
                time.sleep(base_delay * (2 ** (attempt - 1)))
                continue

            if r.status_code in (401, 403):
                raise LadderAuthError(
                    f"Kaggle auth rejected ({r.status_code}) calling {url}. "
                    f"Refresh .kaggle/access_token; the watcher will not retry auth failures."
                )
            if r.status_code >= 500 or r.status_code == 429:
                last_exc = RuntimeError(f"HTTP {r.status_code} from {url}")
                if attempt == max_attempts:
                    raise LadderTransientError(
                        f"Transient failure ({r.status_code}) calling {url} after "
                        f"{max_attempts} attempts."
                    )
                time.sleep(base_delay * (2 ** (attempt - 1)))
                continue
            r.raise_for_status()
            return r.json()
        raise LadderTransientError(f"Exhausted retries calling {url}: {last_exc}")

    def discover_candidates(self) -> list:
        requests, headers = self._session()
        url = f"https://www.kaggle.com/api/v1/competitions/submissions/list/{self.competition_slug}"
        subs = self._get_json_with_retry("GET", url, headers)
        out = []
        for s in subs:
            fname = s.get("fileName", "") or ""
            for prefix in CANDIDATE_LINEAGE_PREFIXES:
                if fname.startswith(prefix) or prefix.replace("-ladder", "") in fname:
                    version_match = re.search(r"adaptive-v(\d+\.\d+)", fname)
                    candidate_id = f"adaptive-v{version_match.group(1)}" if version_match else fname
                    out.append({
                        "candidate_id": candidate_id,
                        "submission_id": str(s.get("ref")),
                        "filename": fname,
                        "public_score": s.get("publicScore"),
                        "date": s.get("date"),
                    })
                    break
        return out

    def poll_submission(self, submission_id) -> dict:
        requests, headers = self._session()
        url = "https://www.kaggle.com/api/i/competitions.EpisodeService/ListEpisodes"
        j = self._get_json_with_retry("POST", url, headers, json_body={"submissionId": submission_id})

        sub2team = {s["id"]: s["teamId"] for s in j.get("submissions", [])}
        team = {t["id"]: t.get("teamName") for t in j.get("teams", [])}
        games = []
        for e in j.get("episodes", []):
            ags = e.get("agents", [])
            if len(ags) < 2:
                continue
            try:
                seat = next(i for i, a in enumerate(ags) if a.get("submissionId") == submission_id)
            except StopIteration:
                continue
            me, opp = ags[seat], ags[1 - seat]
            if e.get("state") != "COMPLETED" or me.get("reward") is None:
                continue
            games.append({
                "episode_id": e.get("id"),
                "time": e.get("createTime", "unavailable"),
                "opponent_submission_id": opp.get("submissionId", "unavailable"),
                "opponent_name": team.get(sub2team.get(opp.get("submissionId")), "unavailable"),
                "my_reward": me.get("reward"),
                "opponent_reward": opp.get("reward", "unavailable"),
                "money_margin": (me.get("reward") - opp.get("reward"))
                                 if isinstance(me.get("reward"), (int, float))
                                 and isinstance(opp.get("reward"), (int, float)) else "unavailable",
                "result": ("win" if me.get("reward") > opp.get("reward")
                           else "loss" if me.get("reward") < opp.get("reward") else "draw")
                          if isinstance(me.get("reward"), (int, float))
                          and isinstance(opp.get("reward"), (int, float)) else "unavailable",
                "rating_after": me.get("updatedScore", "unavailable"),
                "replay_available": "unavailable",  # only known if pull_ladder.py's fetch() ran
                "is_real_opponent": opp.get("submissionId") != submission_id,
            })
        games.sort(key=lambda g: g.get("time") or "")
        real_games = [g for g in games if g.get("is_real_opponent")]
        wins = sum(1 for g in real_games if g.get("result") == "win")
        losses = sum(1 for g in real_games if g.get("result") == "loss")
        draws = sum(1 for g in real_games if g.get("result") == "draw")
        rating = real_games[-1]["rating_after"] if real_games else None

        return {
            "submission_id": str(submission_id),
            "games_completed": len(real_games),
            "wins": wins, "losses": losses, "draws": draws,
            "rating": rating,
            "games": real_games,
            "raw": j,
        }


class MockLadderDataSource(LadderDataSource):
    """Deterministic, scripted data source for tests. `script` maps
    submission_id -> a list of poll results (dicts, same shape
    KaggleLadderDataSource.poll_submission returns); each call to
    poll_submission advances that submission's script by one, repeating the
    last entry once exhausted. `candidates` is the fixed discover_candidates()
    return value."""

    def __init__(self, candidates: list, script: dict, fail_script: Optional[dict] = None):
        self.candidates = candidates
        self.script = {k: list(v) for k, v in script.items()}
        self._cursor = {k: 0 for k in script}
        # fail_script: submission_id -> list of exceptions (or None) to raise
        # instead of returning a result, consumed in the same call order.
        self.fail_script = {k: list(v) for k, v in (fail_script or {}).items()}
        self._fail_cursor = {k: 0 for k in (fail_script or {})}

    def discover_candidates(self) -> list:
        return copy.deepcopy(self.candidates)

    def poll_submission(self, submission_id) -> dict:
        if submission_id in self.fail_script:
            fc = self._fail_cursor[submission_id]
            failures = self.fail_script[submission_id]
            if fc < len(failures) and failures[fc] is not None:
                self._fail_cursor[submission_id] += 1
                raise failures[fc]
            self._fail_cursor[submission_id] += 1

        polls = self.script.get(submission_id, [])
        cur = self._cursor.get(submission_id, 0)
        if not polls:
            raise ValueError(f"No scripted polls for {submission_id}")
        result = polls[min(cur, len(polls) - 1)]
        self._cursor[submission_id] = cur + 1
        return copy.deepcopy(result)


# ---------------------------------------------------------------------------
# State persistence
# ---------------------------------------------------------------------------
def _default_state() -> dict:
    return {"schema_version": 1, "candidates": {}}


def load_state(path: str = STATE_PATH) -> dict:
    if not os.path.exists(path):
        return _default_state()
    with open(path) as f:
        return json.load(f)


def save_state(state: dict, path: str = STATE_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(state, f, indent=2, sort_keys=True)
    os.replace(tmp, path)  # atomic on POSIX -- avoids a torn state file on crash


def _candidate_record(state: dict, candidate_id: str, submission_id: str) -> dict:
    rec = state["candidates"].get(candidate_id)
    if rec is None:
        rec = {
            "candidate_id": candidate_id,
            "submission_id": str(submission_id),
            "last_seen_game_count": 0,
            "last_seen_rating": None,
            "last_poll_timestamp": None,
            "completed_checkpoints": [],
            "poll_history": [],  # append-only summary log, not raw evidence
        }
        state["candidates"][candidate_id] = rec
    return rec


def write_raw_evidence(candidate_id: str, submission_id: str, poll_result: dict,
                        raw_dir: str = None) -> str:
    """Persist this poll's raw evidence to a NEW file -- never overwrite a
    prior poll's raw evidence, so history is fully reconstructable."""
    if raw_dir is None:
        raw_dir = RAW_EVIDENCE_DIR
    os.makedirs(raw_dir, exist_ok=True)
    ts = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    safe_cid = re.sub(r"[^A-Za-z0-9_.-]", "_", candidate_id)
    fname = f"{safe_cid}_{submission_id}_{ts}_{poll_result.get('games_completed', 0)}games.json"
    path = os.path.join(raw_dir, fname)
    payload = {k: v for k, v in poll_result.items()}
    with open(path, "w") as f:
        json.dump(payload, f, indent=2, sort_keys=True, default=str)
    return path


def write_checkpoint_diagnostic(candidate_id: str, parent_candidate: str, submission_id: str,
                                 checkpoint: int, new_games_since_previous_checkpoint: int,
                                 poll_result: dict, raw_evidence_path: str,
                                 diagnostics_dir: str = None) -> str:
    """Small machine-readable diagnostic for one checkpoint event. Any field
    the data source could not supply is recorded literally as
    "unavailable" -- never fabricated. This file is what
    ladder_ingest.load_checkpoint_summary() reads."""
    if diagnostics_dir is None:
        diagnostics_dir = DIAGNOSTICS_DIR
    os.makedirs(diagnostics_dir, exist_ok=True)
    safe_cid = re.sub(r"[^A-Za-z0-9_.-]", "_", candidate_id)
    fname = f"{safe_cid}_checkpoint_{checkpoint}_games.json"
    path = os.path.join(diagnostics_dir, fname)

    games = poll_result.get("games", [])
    diagnostic = {
        "label": f"CHECKPOINT: {checkpoint}_GAMES",
        "is_final_result": False,  # a checkpoint is NEVER the final result
        "candidate": candidate_id,
        "parent": parent_candidate or "unavailable",
        "submission_id": str(submission_id),
        "checkpoint": checkpoint,
        "games_completed": poll_result.get("games_completed", "unavailable"),
        "new_games_since_previous_checkpoint": new_games_since_previous_checkpoint,
        "wins": poll_result.get("wins", "unavailable"),
        "losses": poll_result.get("losses", "unavailable"),
        "draws": poll_result.get("draws", "unavailable"),
        "rating": poll_result.get("rating", "unavailable"),
        "rating_change": poll_result.get("rating_change", "unavailable"),
        "opponents": [
            {
                "episode_id": g.get("episode_id", "unavailable"),
                "opponent_submission_id": g.get("opponent_submission_id", "unavailable"),
                "opponent_name": g.get("opponent_name", "unavailable"),
                "result": g.get("result", "unavailable"),
                "money_margin": g.get("money_margin", "unavailable"),
                "replay_available": g.get("replay_available", "unavailable"),
            }
            for g in games
        ] if games else "unavailable",
        "raw_evidence_file": os.path.relpath(raw_evidence_path, REPO_ROOT),
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    with open(path, "w") as f:
        json.dump(diagnostic, f, indent=2, sort_keys=True, default=str)
    return path


# ---------------------------------------------------------------------------
# Checkpoint detection
# ---------------------------------------------------------------------------
def newly_crossed_checkpoints(previous_count: int, current_count: int,
                               already_completed: list, checkpoints=DEFAULT_CHECKPOINTS) -> list:
    """Return the sorted list of checkpoints newly reached by
    `current_count` that are not already in `already_completed`. Does not
    assume monotonic +1 steps: a jump from 7 to 25 returns [10, 20] in one
    call. A checkpoint already in `already_completed` is never returned
    again, so re-polling the same (or a lower, e.g. stale) count is a no-op."""
    done = set(already_completed)
    fired = []
    for cp in sorted(checkpoints):
        if cp in done:
            continue
        if current_count >= cp:
            fired.append(cp)
    return fired


# ---------------------------------------------------------------------------
# Research-loop trigger
# ---------------------------------------------------------------------------
def trigger_research_loop_ingestion(candidate_id: str, parent_candidate: str, submission_id: str,
                                     checkpoint: int, new_games_since_previous_checkpoint: int,
                                     poll_result: dict, raw_evidence_path: str) -> dict:
    """The one place the watcher calls into the EXISTING research-loop
    infrastructure. Writes a checkpoint diagnostic, hashes it via
    ladder_ingest.load_checkpoint_summary (added alongside this module,
    following load_v0_2_ladder_summary's own pattern of hashing derived
    evidence rather than recomputing it), and records the checkpoint as a
    new, clearly-labeled, explicitly-partial row in experiment_ledger --
    never claiming a checkpoint is a final ladder result."""
    diag_path = write_checkpoint_diagnostic(
        candidate_id, parent_candidate, submission_id, checkpoint,
        new_games_since_previous_checkpoint, poll_result, raw_evidence_path,
    )
    summary = ladder_ingest.load_checkpoint_summary(diag_path)

    label = f"CHECKPOINT: {checkpoint}_GAMES"
    ledger_candidate_id = f"{candidate_id}-ladder-submission"
    entry_fields = dict(
        parent_candidate=parent_candidate,
        submission_id=str(submission_id),
        ladder_result=label,
        score=poll_result.get("rating"),
        wins=poll_result.get("wins"),
        losses=poll_result.get("losses"),
        draws=poll_result.get("draws"),
        games=poll_result.get("games_completed"),
        observations=(
            f"PARTIAL result at the {checkpoint}-game checkpoint "
            f"({new_games_since_previous_checkpoint} new game(s) since the previous "
            f"checkpoint). This is NOT a final ladder result -- more games are still "
            f"expected. Evidence hash: {summary.get('_diagnostic_hash')}."
        ),
    )
    if el.get(ledger_candidate_id) is None:
        entry_fields.update(
            candidate_id=ledger_candidate_id,
            hypothesis_id="unavailable", hypothesis="unavailable", rationale="unavailable",
            predicted_effect="unavailable",
            change_description=f"Automated ladder-watcher checkpoint ingestion for {candidate_id}.",
            changed_files=[], controller_hash="unavailable", learner_hash="unavailable",
            o42_hash=O42_CANONICAL_HASH, preflight_status="not evaluated by the watcher",
            submission_timestamp="unavailable",
            hypothesis_update="none (automated checkpoint ingestion does not itself judge hypotheses)",
            decision="none -- awaiting a full-sample review, this is a checkpoint only",
        )
        row = el.append_entry(entry_fields)
    else:
        row = el.append_result_update(ledger_candidate_id, **entry_fields)

    print("LADDER CHECKPOINT REACHED")
    print(f"candidate: {candidate_id}")
    print(f"submission: {submission_id}")
    print(f"games: {poll_result.get('games_completed')}")
    print(f"rating: {poll_result.get('rating')}")
    print("Research-loop ingestion triggered.")

    return {"diagnostic_path": diag_path, "ledger_row": row, "summary": summary}


# ---------------------------------------------------------------------------
# Poll loop
# ---------------------------------------------------------------------------
def poll_once(source: LadderDataSource, state: Optional[dict] = None,
              checkpoints=DEFAULT_CHECKPOINTS, state_path: str = STATE_PATH) -> dict:
    """One full poll pass over every discovered lineage candidate. Returns a
    report dict; also persists state (unless a caller-supplied `state` dict
    is given AND they choose not to save -- normal callers should just use
    run() below, which always persists)."""
    if state is None:
        state = load_state(state_path)

    report = {"polled": [], "errors": [], "checkpoints_fired": []}

    candidates = []
    try:
        candidates = source.discover_candidates()
    except LadderAuthError as exc:
        print(f"AUTH FAILURE discovering candidates: {exc}", file=sys.stderr)
        report["errors"].append({"stage": "discover_candidates", "error": str(exc), "fatal": True})
        return report
    except LadderTransientError as exc:
        print(f"TRANSIENT FAILURE discovering candidates (will retry next poll): {exc}", file=sys.stderr)
        report["errors"].append({"stage": "discover_candidates", "error": str(exc), "fatal": False})
        return report

    for cand in candidates:
        candidate_id = cand["candidate_id"]
        submission_id = cand["submission_id"]
        parent_candidate = cand.get("parent_candidate", "unavailable")
        rec = _candidate_record(state, candidate_id, submission_id)

        try:
            poll_result = source.poll_submission(submission_id)
        except LadderAuthError as exc:
            print(f"AUTH FAILURE polling {candidate_id} ({submission_id}): {exc}", file=sys.stderr)
            report["errors"].append({"candidate_id": candidate_id, "error": str(exc), "fatal": True})
            continue
        except LadderTransientError as exc:
            print(f"TRANSIENT FAILURE polling {candidate_id} ({submission_id}), will retry next "
                  f"poll: {exc}", file=sys.stderr)
            report["errors"].append({"candidate_id": candidate_id, "error": str(exc), "fatal": False})
            continue
        except Exception as exc:  # malformed response etc: never crash the watcher
            print(f"MALFORMED RESPONSE polling {candidate_id} ({submission_id}), skipping this "
                  f"poll: {exc}", file=sys.stderr)
            traceback.print_exc()
            report["errors"].append({"candidate_id": candidate_id, "error": str(exc), "fatal": False})
            continue

        if not isinstance(poll_result, dict) or "games_completed" not in poll_result:
            print(f"MALFORMED RESPONSE polling {candidate_id} ({submission_id}): missing "
                  f"games_completed, skipping this poll.", file=sys.stderr)
            report["errors"].append({"candidate_id": candidate_id,
                                      "error": "malformed poll_result", "fatal": False})
            continue

        current_count = poll_result.get("games_completed") or 0
        previous_count = rec["last_seen_game_count"]
        previous_rating = rec["last_seen_rating"]
        current_rating = poll_result.get("rating")

        raw_path = write_raw_evidence(candidate_id, submission_id, poll_result)

        fired = newly_crossed_checkpoints(previous_count, current_count,
                                           rec["completed_checkpoints"], checkpoints)

        checkpoint_results = []
        prev_cp_value = max([c for c in rec["completed_checkpoints"]], default=0)
        for cp in fired:
            new_since = cp - prev_cp_value
            poll_result_with_delta = dict(poll_result)
            poll_result_with_delta["rating_change"] = (
                (current_rating - previous_rating)
                if isinstance(current_rating, (int, float)) and isinstance(previous_rating, (int, float))
                else "unavailable"
            )
            result = trigger_research_loop_ingestion(
                candidate_id, parent_candidate, submission_id, cp, new_since,
                poll_result_with_delta, raw_path,
            )
            checkpoint_results.append({"checkpoint": cp, **result})
            rec["completed_checkpoints"].append(cp)
            rec["completed_checkpoints"].sort()
            prev_cp_value = cp
            report["checkpoints_fired"].append({"candidate_id": candidate_id, "checkpoint": cp})

        rec["last_seen_game_count"] = current_count
        rec["last_seen_rating"] = current_rating
        rec["last_poll_timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        rec["poll_history"].append({
            "timestamp": rec["last_poll_timestamp"],
            "games_completed": current_count,
            "rating": current_rating,
            "raw_evidence_file": os.path.relpath(raw_path, REPO_ROOT),
            "new_checkpoints_fired": fired,
        })

        report["polled"].append({
            "candidate_id": candidate_id, "submission_id": submission_id,
            "previous_game_count": previous_count, "current_game_count": current_count,
            "new_games": max(current_count - previous_count, 0),
            "rating": current_rating,
            "checkpoints_fired": fired,
        })

    save_state(state, state_path)
    return report


def run(source: LadderDataSource, *, interval: int = 300, once: bool = False,
        checkpoints=DEFAULT_CHECKPOINTS, state_path: str = STATE_PATH) -> None:
    o42_check = verify_o42_immutable()
    if o42_check.get("checked") and not o42_check.get("matches"):
        print("FATAL: O42 hash mismatch -- refusing to run. "
              f"expected={o42_check['expected_hash']} actual={o42_check['actual_hash']}",
              file=sys.stderr)
        sys.exit(2)

    while True:
        report = poll_once(source, checkpoints=checkpoints, state_path=state_path)
        for p in report["polled"]:
            print(f"[poll] {p['candidate_id']} sub={p['submission_id']} "
                  f"games={p['current_game_count']} (+{p['new_games']}) rating={p['rating']} "
                  f"checkpoints_fired={p['checkpoints_fired'] or 'none'}")
        for e in report["errors"]:
            if e.get("fatal"):
                print(f"FATAL for this poll: {e}", file=sys.stderr)
        if once:
            return
        time.sleep(interval)


def main():
    ap = argparse.ArgumentParser(description="Automatic Kaggle ladder watcher (read-only).")
    ap.add_argument("--interval", type=int, default=300,
                     help="Seconds between polls (default 300 = ~5 minutes).")
    ap.add_argument("--once", action="store_true", help="Poll once and exit.")
    ap.add_argument("--checkpoints", type=str, default=",".join(str(c) for c in DEFAULT_CHECKPOINTS),
                     help="Comma-separated game-count checkpoints, e.g. 10,20,30,50,100,200")
    ap.add_argument("--competition", type=str, default="kaggriculture")
    ap.add_argument("--state-path", type=str, default=STATE_PATH)
    args = ap.parse_args()

    checkpoints = tuple(sorted(int(c) for c in args.checkpoints.split(",") if c.strip()))
    source = KaggleLadderDataSource(competition_slug=args.competition)
    run(source, interval=args.interval, once=args.once, checkpoints=checkpoints,
        state_path=args.state_path)


if __name__ == "__main__":
    main()
