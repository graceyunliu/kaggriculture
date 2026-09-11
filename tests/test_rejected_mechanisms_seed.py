"""The proposer's closed-mechanism list must seed completely (Sep 11: 5 of 14 were silently dropped by INSERT OR IGNORE)."""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "evolve"))
import db as dbm


def test_all_rejected_mechanisms_seed():
    with tempfile.TemporaryDirectory() as d:
        conn = dbm.DB(os.path.join(d, "t.db"))
        tags = {r["mechanism_tag"] for r in conn.rejected_mechanisms()}
        assert tags == {t[0] for t in dbm.REJECTED_MECHANISMS}
        assert all(t[1] in ("rejected", "exhausted", "no_general_fix") for t in dbm.REJECTED_MECHANISMS)


def test_bad_verdict_is_a_hard_failure(monkeypatch):
    bad = dbm.REJECTED_MECHANISMS + (("zz_bad", "closed", "x", "y", "2026-09-11"),)
    monkeypatch.setattr(dbm, "REJECTED_MECHANISMS", bad)
    with tempfile.TemporaryDirectory() as d:
        try:
            dbm.DB(os.path.join(d, "t.db"))
        except RuntimeError as e:
            assert "zz_bad" in str(e)
        else:
            raise AssertionError("partial seed did not raise")
