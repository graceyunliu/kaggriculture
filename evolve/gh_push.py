#!/usr/bin/env python3
"""Publish files to GitHub via the Contents API — no local git needed.

    python3 evolve/gh_push.py Opponents/tape_x.py Opponents/tapes.json [-m "message"]

Why: the Cowork sandbox cannot delete files on the mounted folder, so `git commit` there leaves
lock files behind. The API path has no such problem, and the Air's nightly `git pull` picks the
files up. Needs a fine-grained GitHub token with Contents: read/write for the repo, stored
(gitignored) at .github/token in the project folder — same pattern as .kaggle/access_token.

Files are pushed one commit each, to branch master. Existing files are updated (sha fetched first).
"""
from __future__ import annotations

import argparse
import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "graceyunliu/kaggriculture"
BRANCH = "master"
TOKEN_FILE = ROOT / ".github" / "token"


def _req(method, url, token, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "kaggriculture-evolve"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def push(path, token, message):
    rel = str(Path(path).resolve().relative_to(ROOT))
    url = f"https://api.github.com/repos/{REPO}/contents/{rel}"
    status, cur = _req("GET", url + f"?ref={BRANCH}", token)
    sha = cur.get("sha") if status == 200 else None
    content = base64.b64encode(Path(path).read_bytes()).decode()
    if sha and cur.get("content") and base64.b64decode(cur["content"].replace("\n", "")) == Path(path).read_bytes():
        return "unchanged"
    body = {"message": message, "content": content, "branch": BRANCH}
    if sha:
        body["sha"] = sha
    status, resp = _req("PUT", url, token, body)
    if status in (200, 201):
        return "updated" if sha else "created"
    raise SystemExit(f"push failed for {rel}: {status} {resp.get('message')}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("-m", "--message", default="frontier refresh: new opponent tapes")
    a = ap.parse_args()
    if not TOKEN_FILE.exists():
        print(f"no token at {TOKEN_FILE}. Create a fine-grained GitHub token (repo {REPO}, Contents: read/write), "
              f"save it there, chmod 600. Until then, commit by hand:\n  git add {' '.join(a.files)} && git commit -m '{a.message}' && git push")
        return 2
    token = TOKEN_FILE.read_text().strip()
    for f in a.files:
        print(f"{f}: {push(f, token, a.message)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
