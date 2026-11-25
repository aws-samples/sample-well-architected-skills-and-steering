# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Offline tests for the RAE (Retrieval-Invoked Actual-Use Effect) estimator."""

import json
import sys
from pathlib import Path

import pytest

CLI_DIR = Path(__file__).parent.parent / "cli_effectiveness"
sys.path.insert(0, str(CLI_DIR))

import rae  # noqa: E402


# --------------------------------------------------------------------------- #
# Voting
# --------------------------------------------------------------------------- #
def test_vote_any_majority_all():
    runs = [{"SEC01-BP01"}, {"SEC01-BP01"}, set()]  # 2 of 3 hit
    assert rae.vote_hit("SEC01-BP01", runs, "any") is True
    assert rae.vote_hit("SEC01-BP01", runs, "majority") is True   # 2 >= ceil(3/2)=2
    assert rae.vote_hit("SEC01-BP01", runs, "all") is False
    # 1 of 3 -> majority False
    runs2 = [{"SEC01-BP01"}, set(), set()]
    assert rae.vote_hit("SEC01-BP01", runs2, "majority") is False
    assert rae.vote_hit("SEC01-BP01", runs2, "any") is True


# --------------------------------------------------------------------------- #
# Core b / c / RAE
# --------------------------------------------------------------------------- #
def test_rae_counts_helpful_and_harmful_flips():
    # GT = 4 BPs. SE cites {1,2,3}, SD cites {2,3,4}.
    #   BP1: SE hit, SD miss -> helpful (+1)
    #   BP2: both hit        -> concordant (0)
    #   BP3: both hit        -> concordant (0)
    #   BP4: SE miss, SD hit -> harmful (-1)
    se = {1: [{"SEC01-BP01", "SEC01-BP02", "SEC01-BP03"}]}
    sd = {1: [{"SEC01-BP02", "SEC01-BP03", "SEC01-BP04"}]}
    gt = {1: {"SEC01-BP01", "SEC01-BP02", "SEC01-BP03", "SEC01-BP04"}}
    res = rae.compute_rae(se, sd, gt, conditioned_cases={1}, vote="any", bootstrap=200)
    assert res["rae"]["helpful_b"] == 1
    assert res["rae"]["harmful_c"] == 1
    assert res["rae"]["n_cond"] == 4
    assert res["rae"]["value"] == 0.0  # (1-1)/4


def test_rae_positive_when_se_rescues_more():
    # SE cites all 3 GT BPs; SD cites none -> 3 helpful, 0 harmful.
    se = {1: [{"SEC01-BP01", "SEC01-BP02", "SEC01-BP03"}]}
    sd = {1: [set()]}
    gt = {1: {"SEC01-BP01", "SEC01-BP02", "SEC01-BP03"}}
    res = rae.compute_rae(se, sd, gt, conditioned_cases={1}, vote="any", bootstrap=200)
    assert res["rae"]["value"] == 100.0
    assert res["rae"]["helpful_b"] == 3
    assert res["rae"]["harmful_c"] == 0


def test_rae_negative_matches_paper_paradox():
    # The paper's paradox: SE (retrieval) drops BPs the SD baseline caught.
    se = {1: [{"SEC01-BP01"}]}
    sd = {1: [{"SEC01-BP01", "SEC01-BP02", "SEC01-BP03"}]}
    gt = {1: {"SEC01-BP01", "SEC01-BP02", "SEC01-BP03"}}
    res = rae.compute_rae(se, sd, gt, conditioned_cases={1}, vote="any", bootstrap=200)
    assert res["rae"]["value"] < 0
    assert res["rae"]["harmful_c"] == 2
    assert res["rae"]["helpful_b"] == 0


# --------------------------------------------------------------------------- #
# Conditioning + decomposition (Eq. 4/12)
# --------------------------------------------------------------------------- #
def test_conditioning_restricts_rae_but_not_oae():
    # Case 1 conditioned (SE helpful), case 2 not conditioned (SE harmful).
    se = {1: [{"SEC01-BP01"}], 2: [set()]}
    sd = {1: [set()], 2: [{"REL01-BP01"}]}
    gt = {1: {"SEC01-BP01"}, 2: {"REL01-BP01"}}
    res = rae.compute_rae(se, sd, gt, conditioned_cases={1}, vote="any", bootstrap=200)
    # RAE sees only case 1 (helpful): +100
    assert res["rae"]["value"] == 100.0
    assert res["rae"]["n_cond"] == 1
    # OAE sees both (one helpful, one harmful): 0 over 2 units
    assert res["oae"]["value"] == 0.0
    assert res["oae"]["n_all"] == 2
    # delta_skip = case 2 only (harmful): -100
    assert res["delta_skip"]["value"] == -100.0
    assert res["delta_skip"]["n_skip"] == 1
    # decomposition identity holds
    assert res["decomposition_check"]["ok"] is True


def test_decomposition_identity_holds_on_mixed_case():
    se = {1: [{"SEC01-BP01", "SEC01-BP02"}], 3: [{"COST01-BP01"}]}
    sd = {1: [{"SEC01-BP02"}], 3: [{"COST01-BP01", "COST01-BP02"}]}
    gt = {
        1: {"SEC01-BP01", "SEC01-BP02"},
        3: {"COST01-BP01", "COST01-BP02"},
    }
    res = rae.compute_rae(se, sd, gt, conditioned_cases={1}, vote="any", bootstrap=200)
    assert res["decomposition_check"]["ok"] is True


# --------------------------------------------------------------------------- #
# Universe (pillar) filter for the lens surface
# --------------------------------------------------------------------------- #
def test_pillar_universe_filter():
    se = {1: [{"SEC01-BP01", "REL01-BP01"}]}
    sd = {1: [set()]}
    gt = {1: {"SEC01-BP01", "REL01-BP01", "COST01-BP01"}}
    # Restrict to SEC only: only SEC01-BP01 is a unit (helpful) -> RAE 100 over n=1
    res = rae.compute_rae(
        se, sd, gt, conditioned_cases={1}, vote="any",
        universe_prefixes=("SEC",), bootstrap=200,
    )
    assert res["rae"]["n_cond"] == 1
    assert res["rae"]["value"] == 100.0


# --------------------------------------------------------------------------- #
# Statistics
# --------------------------------------------------------------------------- #
def test_mcnemar_exact_symmetry_and_bounds():
    assert rae.mcnemar_exact_p(0, 0) is None
    # Perfectly symmetric discordant counts -> p == 1.0
    assert rae.mcnemar_exact_p(5, 5) == pytest.approx(1.0)
    # Highly asymmetric -> small p
    assert rae.mcnemar_exact_p(10, 0) < 0.01
    # bounded to 1.0
    assert rae.mcnemar_exact_p(1, 1) <= 1.0


def test_bootstrap_ci_brackets_point_estimate():
    units = [1] * 8 + [-1] * 2  # RAE = 100*(8-2)/10 = 60
    ci = rae.bootstrap_ci(units, resamples=2000, seed=1)
    assert ci is not None
    lo, hi = ci
    assert lo <= 60 <= hi


def test_min_cond_reporting_filter():
    se = {1: [{"SEC01-BP01"}]}
    sd = {1: [set()]}
    gt = {1: {"SEC01-BP01"}}
    res = rae.compute_rae(se, sd, gt, conditioned_cases={1}, vote="any",
                          min_cond=10, bootstrap=200)
    assert res["reportable"] is False  # n_cond=1 < 10


# --------------------------------------------------------------------------- #
# Loading + conditioning inference from result JSON
# --------------------------------------------------------------------------- #
def _write_result(path: Path, cases: list[dict]) -> None:
    path.write_text(json.dumps({"cases": cases}))


def test_load_run_bps_skips_errored_runs(tmp_path):
    f = tmp_path / "se.json"
    _write_result(f, [{
        "case_id": 1,
        "runs": [
            {"error": "timeout"},
            {"subagent_total": {"valid_cited_bps": ["SEC01-BP01"]},
             "report": {"valid_cited_bps": ["SEC01-BP01"]}},
        ],
    }])
    got = rae.load_run_bps(f, scope="subagent_total")
    assert got == {1: [{"SEC01-BP01"}]}


def test_infer_conditioned_from_field(tmp_path):
    f = tmp_path / "se.json"
    _write_result(f, [
        {"case_id": 1, "runs": [{"mcp_tool_calls": 3,
                                 "subagent_total": {"valid_cited_bps": []}}]},
        {"case_id": 2, "runs": [{"mcp_tool_calls": 0,
                                 "subagent_total": {"valid_cited_bps": []}}]},
    ])
    fired, source = rae.infer_conditioned_cases(f, explicit=None, field_name="mcp_tool_calls")
    assert fired == {1}
    assert source == "field:mcp_tool_calls"


def test_infer_conditioned_fallback(tmp_path):
    f = tmp_path / "se.json"
    _write_result(f, [{"case_id": 1, "runs": [{"subagent_total": {"valid_cited_bps": []}}]}])
    fired, source = rae.infer_conditioned_cases(f, explicit=None, field_name=None)
    assert fired == {1}
    assert source == "all_cases_fallback"


def test_infer_conditioned_explicit_intersects_available(tmp_path):
    f = tmp_path / "se.json"
    _write_result(f, [{"case_id": 1, "runs": []}, {"case_id": 2, "runs": []}])
    fired, source = rae.infer_conditioned_cases(f, explicit=[2, 99], field_name=None)
    assert fired == {2}
    assert source == "explicit"
