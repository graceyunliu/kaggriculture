import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_validated_gene_matches_candidate_and_loop_defaults():
    registry = json.loads((ROOT / "evolve" / "gene_registry.json").read_text())
    genes = {gene["id"]: gene for gene in registry["genes"]}
    gene = genes["FERT_DENIAL4"]
    assert gene["id"] == "FERT_DENIAL4"
    assert gene["status"] == "validated_small_positive"
    assert gene["parameter_change"]["fert_buy"] == {"from": 3, "to": 4}
    assert {
        "LIFECYCLE_AWARE_HUSBANDRY",
        "INTRADAY_RELEASE_AND_SELL",
        "ANIMAL_CLAIM4_2",
        "GLOBAL_CROP_ORCHESTRATOR",
        "MELON_MORNING_CONVOY",
        "STRAW_UNITS7_5",
        "HIRE_MAX_MARGINAL144",
        "CARROT_UNITS3",
    } <= genes.keys()

    o26 = (ROOT / registry["immutable_reference"]).read_text()
    o33 = (ROOT / registry["experimental_champion"]).read_text()
    assert "'fert_buy': 3" in o26
    assert "'fert_buy': 4" in o33

    loop = (ROOT / "evolve" / "loop.py").read_text()
    assert 'candidates" / "O33_FERT_DENIAL4.py' in loop
