#!/usr/bin/env python3
"""Re-score archived evolution candidates on the current chassis and engine."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sqlite3
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HERE = ROOT / "evolve"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import mini_engine  # noqa: E402
import replay_verify  # noqa: E402
import space  # noqa: E402

ENGINE_FILE = ROOT / "vendor/kaggle_environments_engine_master/kaggriculture.py"
CHASSIS_FILE = HERE / "chassis.py"
BASELINE = HERE / "regress_baseline.json"
REPORTS = HERE / "reports"
GEN = HERE / "gen_regress"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_seeds(value: str) -> list[int]:
    try:
        if "-" in value:
            lo, hi = (int(x) for x in value.split("-", 1))
            if hi < lo:
                raise ValueError
            return list(range(lo, hi + 1))
        seeds = [int(x) for x in value.split(",") if x.strip()]
        if not seeds:
            raise ValueError
        return seeds
    except ValueError as exc:
        raise argparse.ArgumentTypeError("use LO-HI or comma-separated integers") from exc


def _rows_from_db(path: Path) -> list[dict]:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        return [dict(r) for r in conn.execute(
            "SELECT key, params, blocks, held_margin, held_clone_margin, status, island "
            "FROM candidates"
        )]
    finally:
        conn.close()


def _archive_json_rows(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    if isinstance(data, list):
        return data
    for name in ("held_out", "candidates", "rows"):
        if isinstance(data.get(name), list):
            return data[name]
    return []


def load_archive() -> tuple[list[dict], str]:
    """Fetch results and choose its DB/JSON only when it has more rows than local."""
    local_db = HERE / "evolve.db"
    local_rows = _rows_from_db(local_db) if local_db.exists() else _archive_json_rows(HERE / "archive.json")
    source = f"local {local_db.relative_to(ROOT)} ({len(local_rows)} rows)"
    try:
        subprocess.run(["git", "fetch", "origin", "results"], cwd=ROOT, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=60)
        with tempfile.TemporaryDirectory(prefix="kag-regress-") as td:
            tmp = Path(td)
            remote_rows: list[dict] = []
            remote_kind = ""
            db = subprocess.run(["git", "show", "origin/results:evolve/evolve.db"], cwd=ROOT,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if db.returncode == 0:
                db_path = tmp / "evolve.db"
                db_path.write_bytes(db.stdout)
                remote_rows = _rows_from_db(db_path)
                remote_kind = "evolve.db"
            archive = subprocess.run(["git", "show", "origin/results:evolve/archive.json"], cwd=ROOT,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if archive.returncode == 0:
                archive_path = tmp / "archive.json"
                archive_path.write_bytes(archive.stdout)
                json_rows = _archive_json_rows(archive_path)
                if len(json_rows) > len(remote_rows):
                    remote_rows, remote_kind = json_rows, "archive.json"
            if len(remote_rows) > len(local_rows):
                return remote_rows, f"origin/results:evolve/{remote_kind} ({len(remote_rows)} rows)"
            source += f"; results branch had {len(remote_rows)} rows"
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError, sqlite3.Error) as exc:
        source += f"; results fetch/read failed ({exc})"
    return local_rows, source


def _json_value(value, default):
    if value is None:
        return default
    if isinstance(value, (dict, list)):
        return value
    return json.loads(value)


def resolve_blocks(raw) -> dict[str, str]:
    blocks = _json_value(raw, {})
    resolved = {}
    for block, value in blocks.items():
        if not isinstance(value, str):
            raise ValueError(f"block {block!r} is not text or a variant name")
        if "def " in value:
            resolved[block] = value
            continue
        token = value.strip()
        candidates = [HERE / "blocks" / token, HERE / "blocks" / f"{token}.py"]
        if token in ("banded", "banded_crop_admission", "blocks_banded_crop_admission"):
            candidates.append(HERE / "blocks_banded_crop_admission.py")
        matches = [p for p in candidates if p.is_file()]
        if not matches:
            matches = sorted((HERE / "blocks").glob(f"*{token}*.py"))
        if len(matches) != 1:
            raise ValueError(f"block {block!r} variant {token!r} resolved to {len(matches)} files")
        resolved[block] = matches[0].read_text()
    return resolved


def select_candidates(rows: list[dict], top: int, pins: set[str]) -> list[dict]:
    eligible = [r for r in rows if r.get("status") == "held_pass"]
    eligible.sort(key=lambda r: float("inf") if r.get("held_margin") is None else -float(r["held_margin"]))
    chosen = eligible[:top]
    by_key = {str(r.get("key")): r for r in rows}
    for key in sorted(pins):
        if key not in by_key:
            print(f"warning: pinned candidate {key!r} was not found", file=sys.stderr)
        elif all(str(r.get("key")) != key for r in chosen):
            chosen.append(by_key[key])
    return chosen


def paired_se(current: dict, old: dict) -> float | None:
    a, b = current.get("per_seed", {}), old.get("per_seed", {})
    diffs = []
    for seed in current["seeds"]:
        x, y = a.get(str(seed), a.get(seed)), b.get(str(seed), b.get(seed))
        if x is None or y is None:
            return None
        diffs.append(((x["a"] - x["b"]) - (y["a"] - y["b"])) / 2.0)
    if len(diffs) < 2:
        return 0.0
    mean = sum(diffs) / len(diffs)
    sd = math.sqrt(sum((x - mean) ** 2 for x in diffs) / (len(diffs) - 1))
    return sd / math.sqrt(len(diffs))


def baseline_key(candidate: str, opponent: str, seeds: list[int], engine_sha: str, chassis_sha: str) -> str:
    return json.dumps([candidate, opponent, seeds, engine_sha, chassis_sha], separators=(",", ":"))


def money(v: float) -> str:
    return f"{v:+,.0f}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", type=int, default=5)
    parser.add_argument("--pin", default="", help="comma-separated archive keys")
    parser.add_argument("--seeds", type=parse_seeds, default=parse_seeds("11-30"))
    parser.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    parser.add_argument("--tol", type=float, default=2000.0)
    parser.add_argument("--accept", action="store_true")
    args = parser.parse_args()
    if args.top < 0 or args.jobs < 1 or args.tol < 0:
        parser.error("--top and --tol must be nonnegative; --jobs must be positive")

    engine_sha, chassis_sha = sha256(ENGINE_FILE), sha256(CHASSIS_FILE)
    replay_paths = sorted((ROOT / "Replays/Auto/mine").glob("episode-*-replay.json"),
                          key=lambda p: p.stat().st_mtime, reverse=True)[:3]
    replay_results = []
    for path in replay_paths:
        result = replay_verify.verify(path)
        replay_results.append((path, result))
        print(f"engine check {path.name}: exact={result['exact']}")
    if len(replay_paths) < 3:
        print(f"\033[31mENGINE CHECK: only {len(replay_paths)} replay(s) found\033[0m")
    if any(not result["exact"] for _, result in replay_results):
        print("\033[31mENGINE CHECK FAILED: replay divergence detected (scoring continues)\033[0m")

    rows, archive_source = load_archive()
    pins = {x.strip() for x in args.pin.split(",") if x.strip()}
    archived = select_candidates(rows, args.top, pins)
    candidates = []
    unrenderable = []
    for row in archived:
        key = str(row.get("key"))
        try:
            params = _json_value(row.get("params"), {})
            blocks = resolve_blocks(row.get("blocks"))
            path = space.render(params, blocks, out_dir=GEN)
            candidates.append({"key": key, "label": key, "path": path, "archive": True})
        except Exception as exc:  # one old candidate must not abort the nightly run
            unrenderable.append((key, str(exc)))
            print(f"unrenderable {key}: {exc}", file=sys.stderr)
    for name in ("E1", "C1", "V3_12"):
        candidates.append({"key": f"ref:{name}", "label": name,
                           "path": ROOT / "candidates" / f"{name}.py", "archive": False})

    opponents = [("E1", ROOT / "candidates/E1.py"), ("V3_12", ROOT / "candidates/V3_12.py")]
    opponents += [(p.stem, p) for p in sorted((ROOT / "Opponents").glob("tape_*.py"))]
    old_entries = {}
    if BASELINE.exists():
        try:
            old_entries = json.loads(BASELINE.read_text()).get("entries", {})
        except (OSError, json.JSONDecodeError):
            print("warning: baseline is unreadable; treating as empty", file=sys.stderr)

    results, regressions, improvements = {}, [], []
    seed_label = f"{args.seeds[0]}-{args.seeds[-1]}" if args.seeds == list(range(args.seeds[0], args.seeds[-1] + 1)) else ",".join(map(str, args.seeds))
    for ci, candidate in enumerate(candidates, 1):
        print(f"candidate {ci}/{len(candidates)} {candidate['label']} ({len(opponents)} opponents)", flush=True)
        for opponent, opp_path in opponents:
            res = mini_engine.evaluate(candidate["path"], opp_path, args.seeds,
                                       engine="master", both_seats=True, jobs=args.jobs)
            key = baseline_key(candidate["key"], opponent, args.seeds, engine_sha, chassis_sha)
            status, delta, se = "new", None, None
            old = old_entries.get(key)
            if old:
                delta = res["mean_margin_per_game"] - old["mean_margin_per_game"]
                se = paired_se(res, old)
                if abs(delta) > args.tol and se is not None and abs(delta) > 2 * se:
                    status = "regression" if delta < 0 else "improvement"
                    (regressions if delta < 0 else improvements).append(
                        (candidate["label"], opponent, old["mean_margin_per_game"], res["mean_margin_per_game"], delta, se))
                else:
                    status = "unchanged"
            else:
                logical = json.dumps([candidate["key"], opponent, args.seeds], separators=(",", ":"))
                for old_key in old_entries:
                    parts = json.loads(old_key)
                    if json.dumps(parts[:3], separators=(",", ":")) == logical:
                        status = "rebased"
                        break
            results[key] = {**res, "candidate": candidate["key"], "candidate_label": candidate["label"],
                            "opponent": opponent, "status": status, "delta": delta, "paired_se": se}

    accepted_entries = dict(old_entries)
    accepted_entries.update(results)
    if args.accept:
        BASELINE.write_text(json.dumps({"version": 1, "accepted_at": datetime.now().isoformat(timespec="seconds"),
                                        "entries": accepted_entries}, indent=2, sort_keys=True) + "\n")

    lines = [f"# Regression report — {datetime.now().strftime('%Y-%m-%d %H:%M')}", "",
             f"Archive: {archive_source}  ", f"Seeds: `{seed_label}` · jobs: {args.jobs} · tolerance: ${args.tol:,.0f}  ",
             f"Engine sha: `{engine_sha}`  ", f"Chassis sha: `{chassis_sha}`", "", "## Engine check", ""]
    if replay_results:
        for path, result in replay_results:
            lines.append(f"- `{path.name}`: exact=`{result['exact']}`, seed={result.get('seed')}, max abs diff={result.get('max_abs_diff', 0):,.0f}")
    else:
        lines.append("- No ladder replays found.")
    lines += ["", "## Scores", "", "| candidate | opponent | margin/game (Δ) | t | W-L | state |",
              "|---|---|---:|---:|---:|---|"]
    for entry in results.values():
        delta = "" if entry["delta"] is None else f" ({money(entry['delta'])})"
        t = entry["t"]
        t_text = "∞" if math.isinf(t) else f"{t:.2f}"
        lines.append(f"| `{entry['candidate_label']}` | `{entry['opponent']}` | {money(entry['mean_margin_per_game'])}{delta} | {t_text} | {entry['wins']}-{entry['losses']} | {entry['status']} |")
    lines += ["", "## REGRESSIONS", ""]
    if regressions:
        for cand, opp, old, new, delta, se in regressions:
            lines.append(f"- `{cand}` vs `{opp}`: {money(old)} → {money(new)} (Δ {money(delta)}, paired SE ${se:,.0f})")
    else:
        lines.append("None.")
    lines += ["", "## Improvements", ""]
    if improvements:
        for cand, opp, old, new, delta, se in improvements:
            lines.append(f"- `{cand}` vs `{opp}`: {money(old)} → {money(new)} (Δ {money(delta)}, paired SE ${se:,.0f})")
    else:
        lines.append("None.")
    lines += ["", "## Unrenderable", ""]
    lines.extend([f"- `{key}`: {reason}" for key, reason in unrenderable] or ["None."])
    if args.accept:
        lines += ["", f"Baseline accepted in `{BASELINE.relative_to(ROOT)}`."]
    REPORTS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    report = REPORTS / f"regress-{stamp}.md"
    report.write_text("\n".join(lines) + "\n")
    (REPORTS / "regress-latest.md").write_text("\n".join(lines) + "\n")
    print(f"report: {report}")
    print(f"regressions: {len(regressions)}")
    return 1 if regressions else 0


if __name__ == "__main__":
    raise SystemExit(main())
