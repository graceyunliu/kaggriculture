# Canonical upstream animal-route panel validation

The panel was generated in four opponent-parallel strata with fixed shops:

```bash
KAGG_FIXED_SHOPS=1 python3 tools/o42_decision_provenance.py \
  --route-upstream-only \
  --seeds 301-340 \
  --opponents <peter|alaylm|bahaen|yangk> \
  --out-dir adaptive/logs/animal_route_upstream_panel_scoped_s301_340/<opponent>
```

Each stratum contains 80 games (40 seeds × both seats). All four summaries report:

- `parity_passed: true`
- `anchor_bindings_passed: true`
- `trace_scope: animal_route_upstream`
- unchanged O42 SHA256
  `154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813`

The complete local panel contains 320 gzip JSONL logs. Raw logs are retained locally
but are not committed because they total approximately 1.4 GB. The compact analysis,
map, stratum summaries, analyzer, smoke logs, and binding manifest are committed.

Analysis command:

```bash
python3 tools/analyze_animal_route_upstream.py \
  --panel-dir adaptive/logs/animal_route_upstream_panel_scoped_s301_340 \
  --outcomes adaptive/logs/o42_seed_attribution_v2_s301_340_games.json \
  --out adaptive/logs/animal_route_upstream_panel_scoped_s301_340/animal_route_upstream_analysis.json
```
