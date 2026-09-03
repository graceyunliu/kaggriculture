#!/usr/bin/env bash
# Build a self-contained zip with everything the loop needs, for copying to the Air.
# Usage: evolve/make_bundle.sh  -> evolve/evolve_bundle.zip
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="evolve/evolve_bundle.zip"
TMP="$(mktemp -d)/evolve_bundle.zip"
zip -qr "$TMP" \
  mini_engine.py \
  candidates/K.py candidates/V3_12.py candidates/C1.py candidates/V3_11.py \
  Opponents/*.py \
  vendor/kaggle_environments_engine_master/kaggriculture.py \
  vendor/kaggle_environments_engine_master/kaggriculture.json \
  vendor/kaggle_environments_engine/kaggriculture.py \
  vendor/kaggle_environments_engine/kaggriculture.json \
  evolve/space.py evolve/db.py evolve/cascade.py evolve/loop.py evolve/report.py \
  evolve/run_nightly.sh evolve/setup_air.sh evolve/com.grace.kaggriculture-evolve.plist evolve/README.md \
  -x '*/__pycache__/*'
cp "$TMP" "$OUT"
ls -lh "$OUT"
echo "copy to the Air, then: unzip -o evolve_bundle.zip -d ~/Kaggriculture && cd ~/Kaggriculture && bash evolve/setup_air.sh"
