"""TDAS -- Trajectory-Directed Architecture Search.

An isolated search lane, sibling to evolve/, for discovering different economic
*architectures* rather than tuning parameters on the fixed K.py chassis.

See docs/SPEC-trajectory-directed-architecture-search.md for the design.

This package never imports or modifies evolve/loop.py, evolve/db.py, evolve/space.py,
candidates/K.py, mini_engine.py, evolve/cascade.py, evolve/trace.py, or tools/tape_days.py --
it only calls into them.
"""
