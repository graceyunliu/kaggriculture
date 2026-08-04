#!/usr/bin/env bash
# Sets up a local sandbox to run kaggle-environments' "kaggriculture" env.
#
# Why this script exists instead of a plain `pip install kaggle-environments`:
#
# 1. As of 2026-08-04, kaggriculture is on the kaggle-environments GitHub
#    main branch but NOT in the latest PyPI release (1.25.9). A plain
#    `pip install kaggle-environments` gives you the harness, but
#    `make("kaggriculture")` fails with "Unknown Environment Specification".
#    The GitHub repo also declares Python >=3.11.
#
# 2. kaggle-environments' declared dependencies (torch/jax-scale stack via
#    stable-baselines3, transformers, gymnax, accelerate, bitsandbytes, ...)
#    are needed for OTHER bundled competitions, not for kaggriculture, whose
#    own engine (kaggriculture.py) imports only stdlib + one small helper
#    from kaggle_environments.utils. Verified in a clean venv: kaggriculture
#    registers and runs full episodes with only `kaggle-environments`
#    (--no-deps) + `jsonschema` + `requests` installed - no torch/jax needed.
#
# This script tries the lightweight path first (fast, ~seconds, small disk
# footprint) since that's confirmed sufficient for local agent testing.
# If you separately want the full package (rendering, other envs, RL
# baselines), just run `pip install -U kaggle-environments` yourself - it's
# several GB and unrelated to running kaggriculture locally.
#
# Usage: ./setup_local_env.sh

set -euo pipefail

PY_MAJOR=$(python3 -c 'import sys; print(sys.version_info[0])')
PY_MINOR=$(python3 -c 'import sys; print(sys.version_info[1])')
echo "Python version: $PY_MAJOR.$PY_MINOR"

# kaggle-environments on PyPI has required Python >=3.10 since release 1.20.0
# (checked against PyPI metadata 2026-08-04). Below that, `pip install` will
# fail outright with a "requires a different Python" error - not a bug in
# this script, just a real version floor. Fail fast with a clear message
# instead of a confusing pip error.
if [ "$PY_MAJOR" -lt 3 ] || { [ "$PY_MAJOR" -eq 3 ] && [ "$PY_MINOR" -lt 10 ]; }; then
    echo ""
    echo "ERROR: kaggle-environments requires Python 3.10+ (you have $PY_MAJOR.$PY_MINOR)."
    echo "Install a newer Python and re-run this script with it, e.g.:"
    echo "  brew install python@3.12"
    echo "  /opt/homebrew/bin/python3.12 -m venv .venv && source .venv/bin/activate"
    echo "  ./setup_local_env.sh"
    echo "(3.11+ also lets you install kaggle-environments straight from GitHub"
    echo "source, which already has kaggriculture registered - no vendoring hack needed.)"
    exit 1
fi

# Use `python3 -m pip` rather than a bare `pip` - more portable across
# macOS Python installs where the `pip` command isn't always on PATH.
PIP="python3 -m pip"
$PIP install -q -U pip
$PIP install -q --no-deps kaggle-environments
$PIP install -q jsonschema requests

echo "==> Checking if kaggriculture is already registered (in case PyPI has caught up)"
if python3 -c "from kaggle_environments import make; make('kaggriculture', configuration={'episodeSteps': 10})" 2>/dev/null; then
    echo "kaggriculture available. Done. Run: python3 smoke_test.py main_v5.py"
    exit 0
fi

echo "==> Not yet on PyPI. Vendoring the engine from vendor/kaggle_environments_engine/"
echo "    (source: github.com/Kaggle/kaggle-environments, master branch - see vendor/kaggle_environments_engine/SOURCE.md)"

SITE_PKG=$(python3 -c "import kaggle_environments, os; print(os.path.dirname(kaggle_environments.__file__))" 2>/dev/null | tail -1)
ENV_DIR="$SITE_PKG/envs/kaggriculture"
mkdir -p "$ENV_DIR"
cp vendor/kaggle_environments_engine/kaggriculture.py "$ENV_DIR/"
cp vendor/kaggle_environments_engine/kaggriculture.json "$ENV_DIR/"
cp vendor/kaggle_environments_engine/README.md "$ENV_DIR/"
cp vendor/kaggle_environments_engine/AGENTS.md "$ENV_DIR/"

UTILS="$SITE_PKG/utils.py"
if ! grep -q "def resolve_episode_seed" "$UTILS"; then
    cat >> "$UTILS" << 'PYEOF'


def resolve_episode_seed(env, *, config_key="seed", fallback=None):
    """Vendored from kaggle-environments master for kaggriculture support (py3.10-compatible signature)."""
    import random as _random
    if not hasattr(env, "info") or env.info is None:
        env.info = {}
    seed = env.info.get("seed")
    config = env.configuration
    if seed is None:
        seed = getattr(config, config_key, None)
        if seed is None and isinstance(config, dict):
            seed = config.get(config_key)
    if seed is None:
        seed = fallback() if fallback is not None else _random.randrange(2**31)
    try:
        setattr(config, config_key, None)
    except (AttributeError, TypeError):
        config[config_key] = None
    env.info["seed"] = seed
    return seed
PYEOF
fi

python3 -c "from kaggle_environments import make; make('kaggriculture', configuration={'episodeSteps': 10}); print('OK: kaggriculture registered via vendored fallback')"
echo "Done. Run: python3 smoke_test.py main_v5.py"
