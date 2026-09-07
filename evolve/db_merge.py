#!/usr/bin/env python3
"""Merge one evolve.db (e.g. from a different machine/session) into another, without duplicating
or clobbering candidates.

Why this exists: `evolve/*.db` is gitignored (see .gitignore) -- it is never pushed/pulled with the
code, so two machines running the loop independently (e.g. this sandbox and the Air) end up with two
separate SQLite files. `space.params_key()` is a deterministic hash of a candidate's actual params +
blocks + chassis/frontier shas, so the *same* candidate always gets the *same* `key` regardless of
which machine generated it -- merging is just "insert rows whose key/run_id isn't already present",
never an overwrite, so it's safe to run more than once and safe in either direction.

    python3 evolve/db_merge.py --source /path/to/other/evolve.db --target evolve/evolve.db
    python3 evolve/db_merge.py --source /path/to/other/evolve.db --dry-run   # report only, no writes

Handles schema drift between the two files (e.g. the source predates AGE-331/332 and has no
trajectory_summary/failure_profile columns yet): only columns present in BOTH schemas are copied for
a given table; already-migrated columns in the target that the source lacks are simply left NULL for
the merged-in rows, same as any pre-existing row from before that column was added.
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import db as db_mod  # noqa: E402

TABLES = (
    ("candidates", "key"),
    ("runs", "run_id"),
    ("rejected_mechanisms", "mechanism_tag"),
)


def _columns(conn, schema, table):
    return [r[1] for r in conn.execute(f"PRAGMA {schema}.table_info({table})")]


def merge(target_path, source_path, dry_run=False):
    """Ensure `target_path` has the current schema (runs DB migrations), then copy any row from
    `source_path` whose identity column isn't already present. Returns {table: n_inserted}."""
    # DB() runs the ALTER TABLE migration loop, so the target always has the newest columns
    # before we compute the column intersection below.
    db_mod.DB(path=target_path)

    conn = sqlite3.connect(str(target_path))
    conn.execute("ATTACH DATABASE ? AS src", (str(source_path),))
    results = {}
    try:
        for table, id_col in TABLES:
            src_cols = set(_columns(conn, "src", table))
            tgt_cols = set(_columns(conn, "main", table))
            cols = [c for c in _columns(conn, "main", table) if c in src_cols and c in tgt_cols]
            if not cols:
                results[table] = (0, f"no shared columns between source and target for {table}")
                continue
            col_list = ", ".join(cols)
            before = conn.execute(f"SELECT COUNT(*) FROM main.{table}").fetchone()[0]
            if not dry_run:
                conn.execute(
                    f"INSERT OR IGNORE INTO main.{table} ({col_list}) "
                    f"SELECT {col_list} FROM src.{table}"
                )
                conn.commit()
                after = conn.execute(f"SELECT COUNT(*) FROM main.{table}").fetchone()[0]
                results[table] = (after - before, None)
            else:
                n_new = conn.execute(
                    f"SELECT COUNT(*) FROM src.{table} WHERE {id_col} NOT IN "
                    f"(SELECT {id_col} FROM main.{table})"
                ).fetchone()[0]
                results[table] = (n_new, "dry-run, not written")
    finally:
        conn.execute("DETACH DATABASE src")
        conn.close()
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="the other machine's evolve.db")
    ap.add_argument("--target", default=str(db_mod.DB_PATH), help="the DB to merge into (default evolve/evolve.db)")
    ap.add_argument("--dry-run", action="store_true", help="report what would be inserted, write nothing")
    args = ap.parse_args()
    source, target = Path(args.source), Path(args.target)
    if not source.exists():
        raise SystemExit(f"source not found: {source}")
    if not target.exists():
        raise SystemExit(f"target not found: {target} (run any evolve script once to create it, or pass --target)")
    if source.resolve() == target.resolve():
        raise SystemExit("source and target are the same file")

    results = merge(target, source, dry_run=args.dry_run)
    label = "would insert" if args.dry_run else "inserted"
    for table, (n, note) in results.items():
        suffix = f"  ({note})" if note and not args.dry_run else (f"  ({note})" if note else "")
        print(f"{table:20s} {label} {n} row(s){suffix}")


if __name__ == "__main__":
    main()
