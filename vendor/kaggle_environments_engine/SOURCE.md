# Provenance

Vendored from https://github.com/Kaggle/kaggle-environments (master branch,
commit 3fe0e0b58eb6ac1aaffcb60bf19726a65377b4a2), fetched 2026-08-04.

This is the actual engine ground truth referenced in kaggriculture-agent-design.md
D2 and D42 — it was not yet published to the kaggle-environments PyPI package
(latest release at fetch time: 1.25.9) or discoverable via `pip install`, only
on GitHub main. Every rule belief in main*.py should be checked against
kaggriculture.py directly rather than the README/AGENTS.md prose, which can
drift from the actual implementation.

Re-fetch if the design doc's D42 concerns get stale:
  curl -sL "https://raw.githubusercontent.com/Kaggle/kaggle-environments/master/kaggle_environments/envs/kaggriculture/kaggriculture.py" -o vendor/kaggle_environments_engine/kaggriculture.py
