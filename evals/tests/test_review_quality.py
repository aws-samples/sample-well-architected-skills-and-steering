# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Offline tests for blind and adversarial wa-review evaluation."""

import json
import sys
from pathlib import Path

import pytest

EVALS_DIR = Path(__file__).parent.parent
CLI_DIR = EVALS_DIR / "cli_effectiveness"
sys.path.insert(0, str(EVALS_DIR))
sys.path.insert(0, str(CLI_DIR))

import review_quality as rq
from benchmark import _extract_text
from generate_ground_truth import MODELS, build_canonical_bps, compute_ground_truth
from review_quality import (
    Candidate,
    build_blind_prompt,
    build_evidence_catalog,
    cohen_kappa,
    compute_quality_metrics,
    extract_pillar_excerpt,
    load_candidates,
    normalize_bp_id,
    normalize_reviewer_row,
    parse_candidate_ledger,
    parse_model_rows,
    run_quality_review,
    select_adversarial_ids,
    severity_within_one,
    validate_panel,
)

WORKLOAD = (
    "The workload uses one EC2 instance and has no backups configured. "
    "Monitoring is limited to basic metrics."
)


def evidence_for_status(status):
    return {
        "Implemented": ("explicit_presence", "uses one EC2 instance"),
        "Partially Implemented": (
            "explicit_partial",
            "Monitoring is limited to basic metrics",
        ),
        "Not Implemented": ("explicit_absence", "no backups configured"),
        "Not Applicable": ("not_applicable", None),
        "Cannot Determine": ("omitted", None),
    }[status]


def reviewer_row(
    bp_id,
    *,
    candidate_status="Not Implemented",
    reference_status="Not Implemented",
    evidence_kind=None,
    evidence_quote=None,
    candidate_severity="High",
    reference_severity="High",
    recommendation_score=4,
):
    default_kind, default_quote = evidence_for_status(reference_status)
    return {
        "bp_id": bp_id,
        # Included for metric fixtures; schema-v3 normalization ignores these
        # model-supplied values and injects the parsed candidate ledger values.
        "candidate_status": candidate_status,
        "reference_status": reference_status,
        "evidence_kind": evidence_kind or default_kind,
        "evidence_quote": (
            default_quote
            if evidence_kind is None and evidence_quote is None
            else evidence_quote
        ),
        "evidence_rationale": "The workload statement supports this conclusion.",
        "candidate_severity": candidate_severity,
        "reference_severity": reference_severity,
        "recommendation_score": recommendation_score,
        "challenge": None,
        "confidence": "high",
    }


def adversary_row(
    bp_id,
    *,
    disposition="uphold_candidate",
    final_status="Not Implemented",
    final_severity="High",
    evidence_kind=None,
    evidence_quote=None,
    reviewer_assessment="both_hold",
):
    default_kind, default_quote = evidence_for_status(final_status)
    return {
        "bp_id": bp_id,
        "disposition": disposition,
        "final_status": final_status,
        "final_severity": final_severity,
        "evidence_kind": evidence_kind or default_kind,
        "evidence_quote": (
            default_quote
            if evidence_kind is None and evidence_quote is None
            else evidence_quote
        ),
        "reviewer_assessment": reviewer_assessment,
        "rationale": "The workload directly supports this conclusion.",
        "confidence": "high",
    }


def candidate_rows(*rows):
    return {
        row["bp_id"]: {
            "bp_id": row["bp_id"],
            "candidate_status": row["candidate_status"],
            "candidate_severity": row["candidate_severity"],
        }
        for row in rows
    }


def normalize_test_reviewer(row):
    return normalize_reviewer_row(
        row,
        workload=WORKLOAD,
        candidate_rows=candidate_rows(row),
    )


def normalize_test_adversary(row, reviewer_a, reviewer_b):
    return rq.normalize_adversary_row(
        row,
        workload=WORKLOAD,
        reviewer_a=reviewer_a,
        reviewer_b=reviewer_b,
    )


def test_normalize_bp_id_accepts_unicode_hyphen():
    assert normalize_bp_id("SEC03‑BP02") == "SEC03-BP02"


def test_structured_calls_can_exclude_reasoning_blocks():
    response = {
        "output": {
            "message": {
                "content": [
                    {"reasoningContent": {"reasoningText": {"text": '{"rows":[]}'}}},
                    {"text": '{"rows":[{"bp_id":"SEC01-BP01"}]}'},
                ]
            }
        }
    }

    assert _extract_text(response, include_reasoning=False) == (
        '{"rows":[{"bp_id":"SEC01-BP01"}]}'
    )


def test_parse_model_rows_requires_exact_complete_ledger():
    expected = {"SEC01-BP01", "SEC01-BP02"}
    response = json.dumps({
        "rows": [
            reviewer_row("SEC01-BP01"),
            reviewer_row("SEC01-BP02", candidate_severity=None, reference_severity=None),
        ]
    })

    parsed = parse_model_rows(response, expected, normalize_test_reviewer)

    assert parsed["complete"] is True
    assert set(parsed["rows"]) == expected


def test_reviewer_missing_confidence_defaults_to_low():
    row = reviewer_row("SEC01-BP01")
    row.pop("confidence")

    normalized = normalize_test_reviewer(row)

    assert normalized["confidence"] == "low"


def test_reviewer_requires_status_to_match_evidence_provenance():
    invalid = reviewer_row(
        "SEC01-BP01",
        reference_status="Not Implemented",
        evidence_kind="omitted",
        evidence_quote=None,
        reference_severity=None,
    )

    with pytest.raises(ValueError, match="incompatible"):
        normalize_test_reviewer(invalid)

    valid = normalize_test_reviewer(reviewer_row(
        "SEC01-BP01",
        reference_status="Cannot Determine",
        evidence_kind="omitted",
        evidence_quote=None,
        reference_severity=None,
    ))

    assert valid["reference_status"] == "Cannot Determine"
    assert valid["reference_severity"] is None
    assert valid["evidence_kind"] == "omitted"


def test_reviewer_rejects_fabricated_evidence_quote():
    row = reviewer_row(
        "SEC01-BP01",
        evidence_quote="no incident response process",
    )

    with pytest.raises(ValueError, match="not an exact workload quote"):
        normalize_test_reviewer(row)


def test_evidence_catalog_preserves_exact_atomic_workload_spans():
    catalog = build_evidence_catalog(
        "Single EC2 instance, no backups configured. Basic metrics only."
    )

    assert catalog == {
        "W001": "Single EC2 instance",
        "W002": "no backups configured.",
        "W003": "Basic metrics only.",
    }


def test_reviewer_resolves_catalog_id_to_exact_workload_quote():
    row = reviewer_row("SEC01-BP01")
    row.pop("evidence_quote")
    row["evidence_quote_id"] = "w001"

    normalized = normalize_test_reviewer(row)

    assert normalized["evidence_quote_id"] == "W001"
    assert normalized["evidence_quote"] == (
        "The workload uses one EC2 instance and has no backups configured."
    )


def test_reviewer_rejects_unknown_catalog_id():
    row = reviewer_row("SEC01-BP01")
    row.pop("evidence_quote")
    row["evidence_quote_id"] = "W999"

    with pytest.raises(ValueError, match="invalid evidence_quote_id"):
        normalize_test_reviewer(row)


def test_reviewer_uses_parsed_candidate_status_not_model_supplied_values():
    raw = reviewer_row(
        "SEC01-BP01",
        candidate_status="Not Implemented",
        candidate_severity="Critical",
        reference_status="Cannot Determine",
        reference_severity=None,
    )
    parsed_candidate = {
        "SEC01-BP01": {
            "bp_id": "SEC01-BP01",
            "candidate_status": "Cannot Determine",
            "candidate_severity": None,
        }
    }

    normalized = normalize_reviewer_row(
        raw,
        workload=WORKLOAD,
        candidate_rows=parsed_candidate,
    )

    assert normalized["candidate_status"] == "Cannot Determine"
    assert normalized["candidate_severity"] is None


def test_adversary_requires_status_to_match_reviewer_evidence():
    blind_a = normalize_test_reviewer(reviewer_row(
        "SEC01-BP01",
        candidate_status="Cannot Determine",
        candidate_severity=None,
        reference_status="Cannot Determine",
        reference_severity=None,
    ))
    blind_b = dict(blind_a)
    invalid = adversary_row(
        "SEC01-BP01",
        final_status="Not Implemented",
        final_severity=None,
        evidence_kind="explicit_absence",
        evidence_quote="no backups configured",
        disposition="accept_challenge",
    )

    with pytest.raises(ValueError, match="supplied by a blind reviewer"):
        normalize_test_adversary(
            invalid,
            {"SEC01-BP01": blind_a},
            {"SEC01-BP01": blind_b},
        )

    valid = normalize_test_adversary(adversary_row(
        "SEC01-BP01",
        final_status="Cannot Determine",
        final_severity=None,
        evidence_kind="omitted",
        evidence_quote=None,
        disposition="insufficient_evidence",
    ), {"SEC01-BP01": blind_a}, {"SEC01-BP01": blind_b})

    assert valid["final_status"] == "Cannot Determine"
    assert valid["final_severity"] is None


@pytest.mark.parametrize(
    ("rows", "field"),
    [
        ([reviewer_row("SEC01-BP01")], "missing_ids"),
        (
            [reviewer_row("SEC01-BP01"), reviewer_row("SEC01-BP01")],
            "duplicate_ids",
        ),
        (
            [reviewer_row("SEC01-BP01"), reviewer_row("REL01-BP01")],
            "unexpected_ids",
        ),
    ],
)
def test_parse_model_rows_rejects_incomplete_duplicate_or_unexpected(rows, field):
    parsed = parse_model_rows(
        json.dumps({"rows": rows}),
        {"SEC01-BP01", "SEC01-BP02"},
        normalize_test_reviewer,
    )

    assert parsed["complete"] is False
    assert parsed[field]


def test_extract_pillar_excerpt_keeps_only_requested_pillar():
    report = "\n".join([
        "| SEC01-BP01 | Not Implemented | High |",
        "| REL01-BP01 | Implemented | |",
        "| SEC01‑BP02 | Cannot Determine | |",
    ])

    excerpt = extract_pillar_excerpt(report, "SEC")

    assert "SEC01-BP01" in excerpt
    assert "SEC01‑BP02" in excerpt
    assert "REL01-BP01" not in excerpt


def test_reference_and_candidate_excerpts_can_be_scoped_to_chunk():
    reference = "\n".join([
        "# Security",
        "# SEC01-BP01 First",
        "First guidance.",
        "# SEC01-BP02 Second",
        "Second guidance.",
        "# SEC01-BP03 Third",
        "Third guidance.",
    ])
    report = "\n".join([
        "| SEC01-BP01 | Implemented |",
        "| SEC01-BP02 | Not Implemented |",
        "| SEC01-BP03 | Cannot Determine |",
    ])

    reference_subset = rq.extract_reference_subset(
        reference,
        ["SEC01-BP02"],
    )
    candidate_subset = extract_pillar_excerpt(
        report,
        "SEC",
        ["SEC01-BP02"],
    )

    assert "SEC01-BP02" in reference_subset
    assert "SEC01-BP01" not in reference_subset
    assert "SEC01-BP03" not in reference_subset
    assert "SEC01-BP02" in candidate_subset
    assert "SEC01-BP01" not in candidate_subset
    assert "SEC01-BP03" not in candidate_subset


def test_candidate_ledger_is_parsed_deterministically():
    report = "\n".join([
        "| BP ID | Status | Severity | Evidence |",
        "| SEC01-BP01 | Cannot Determine | | Need account configuration |",
        "| SEC01-BP02 | Not Implemented | High | no backups configured |",
        "| SEC01-BP03 | OPS | Not a ledger row |",
    ])

    rows = parse_candidate_ledger(report)

    assert rows == {
        "SEC01-BP01": {
            "bp_id": "SEC01-BP01",
            "candidate_status": "Cannot Determine",
            "candidate_severity": None,
        },
        "SEC01-BP02": {
            "bp_id": "SEC01-BP02",
            "candidate_status": "Not Implemented",
            "candidate_severity": "High",
        },
    }


def test_candidate_ledger_rejects_severity_for_cannot_determine():
    with pytest.raises(ValueError, match="must be null"):
        parse_candidate_ledger(
            "| SEC01-BP01 | Cannot Determine | High | Need account config |"
        )


def test_blind_prompt_does_not_receive_candidate_identity_metadata():
    prompt = build_blind_prompt(
        "A workload on AWS.",
        "| SEC01-BP01 | Implemented |",
        "# SEC01-BP01 Example",
        "Security",
        1,
    )

    assert "candidate-001" not in prompt
    assert "wa_review_effectiveness" not in prompt
    assert "claude-sonnet" not in prompt
    assert "baseline" not in prompt.lower()
    assert "existing score" not in prompt.lower()
    assert "not explicit_absence" in prompt
    assert "exact contiguous quote from WORKLOAD" in prompt
    assert "evidence_quote_id" in prompt
    assert "W001:" in prompt
    assert "do not return either" in prompt


def test_skill_contract_includes_cannot_determine_as_fifth_status():
    for filename in ("SKILL.md", "SKILL-devops-agent.md"):
        text = (EVALS_DIR.parent / "skills" / "wa-review" / filename).read_text()

        assert "one of four statuses" not in text
        assert "all four statuses" not in text
        assert "one of five statuses" in text
        assert "Absence of evidence is not evidence of absence." in text
        assert "`Cannot Determine` counts as evaluated coverage" in text



def test_validate_panel_rejects_candidate_family_self_grading():
    with pytest.raises(ValueError, match="self-grading"):
        validate_panel(
            ["sonnet"],
            ["us.anthropic.claude-sonnet-5", "openai.gpt-oss-120b"],
            "us.deepseek.r1-v1:0",
        )


def test_validate_panel_accepts_three_independent_families():
    validate_panel(
        ["sonnet"],
        ["openai.gpt-oss-120b", "us.amazon.nova-pro-v1:0"],
        "us.deepseek.r1-v1:0",
    )


def test_invoke_model_applies_provider_output_limit(monkeypatch):
    captured = {}

    def fake_call_model(client, model_id, messages, **kwargs):
        captured.update(kwargs)
        return {
            "model_id": model_id,
            "output": "{}",
            "input_tokens": 1,
            "output_tokens": 1,
        }

    monkeypatch.setattr(rq, "call_model", fake_call_model)

    result = rq._invoke_model(
        object(),
        "us.amazon.nova-pro-v1:0",
        "test",
        "us-east-1",
        16_384,
    )

    assert captured["max_tokens"] == 9_999
    assert result["requested_max_tokens"] == 16_384
    assert result["effective_max_tokens"] == 9_999


def test_chunk_review_retries_only_unresolved_rows(monkeypatch):
    requested = []

    def prompt_builder(bp_ids):
        requested.append(list(bp_ids))
        return ",".join(bp_ids)

    def fake_invoke(client, model_id, prompt, region, max_tokens):
        bp_ids = prompt.split("\n", 1)[0].split(",")
        returned = bp_ids[:1]
        return {
            "model_id": model_id,
            "output": json.dumps({
                "rows": [reviewer_row(bp_id) for bp_id in returned],
            }),
            "input_tokens": 10,
            "output_tokens": 5,
            "latency_s": 0.1,
        }

    monkeypatch.setattr(rq, "_invoke_model", fake_invoke)

    result = rq._run_review_chunk(
        object(),
        "reviewer-model",
        prompt_builder,
        ["SEC01-BP01", "SEC01-BP02"],
        normalize_test_reviewer,
        "us-east-1",
        1024,
        retries=1,
    )

    assert requested == [
        ["SEC01-BP01", "SEC01-BP02"],
        ["SEC01-BP02"],
    ]
    assert result["assessment"]["complete"] is True
    assert set(result["assessment"]["rows"]) == {
        "SEC01-BP01",
        "SEC01-BP02",
    }
    assert result["assessment"]["recovered_issue_count"] == 1


def test_chunk_merge_rejects_missing_rows():
    first = {
        "complete": True,
        "rows": {"SEC01-BP01": reviewer_row("SEC01-BP01")},
        "missing_ids": [],
        "unexpected_ids": [],
        "duplicate_ids": [],
        "invalid_rows": [],
    }

    merged = rq.merge_chunk_assessments(
        ["SEC01-BP01", "SEC01-BP02"],
        [first],
    )

    assert merged["complete"] is False
    assert merged["missing_ids"] == ["SEC01-BP02"]


def test_adversarial_selection_includes_risk_disagreement_and_seeded_sample():
    reviewer_a = {
        "SEC01-BP01": reviewer_row("SEC01-BP01"),
        "SEC01-BP02": reviewer_row(
            "SEC01-BP02",
            candidate_severity="Low",
            reference_severity="Low",
        ),
        "SEC01-BP03": reviewer_row(
            "SEC01-BP03",
            candidate_severity="Low",
            reference_severity="Low",
        ),
    }
    reviewer_b = {
        "SEC01-BP01": reviewer_row("SEC01-BP01"),
        "SEC01-BP02": reviewer_row(
            "SEC01-BP02",
            candidate_severity="Low",
            reference_severity="Medium",
        ),
        "SEC01-BP03": reviewer_row(
            "SEC01-BP03",
            candidate_severity="Low",
            reference_severity="Low",
        ),
    }

    first = select_adversarial_ids(reviewer_a, reviewer_b, seed=7)
    second = select_adversarial_ids(reviewer_a, reviewer_b, seed=7)

    assert first == second
    assert "SEC01-BP01" in first  # Candidate High finding.
    assert "SEC01-BP02" in first  # Reviewer severity disagreement.
    assert "SEC01-BP03" in first  # Deterministic 10% agreement sample.


def test_agreement_metrics_handle_exact_and_adjacent_severity():
    assert cohen_kappa(["a", "b"], ["a", "b"]) == 1.0
    assert severity_within_one(["High", "Medium"], ["Medium", "Low"]) == 1.0


def test_quality_metrics_include_overturns_and_unresolved_items():
    reviewer_a = {
        "SEC01-BP01": reviewer_row("SEC01-BP01"),
        "SEC01-BP02": reviewer_row(
            "SEC01-BP02",
            candidate_severity="Low",
            reference_severity="Low",
        ),
    }
    reviewer_b = {
        "SEC01-BP01": reviewer_row("SEC01-BP01"),
        "SEC01-BP02": reviewer_row(
            "SEC01-BP02",
            candidate_severity="Low",
            reference_severity="Medium",
        ),
    }
    adversary = {
        "SEC01-BP01": adversary_row(
            "SEC01-BP01",
            disposition="accept_challenge",
            final_status="Cannot Determine",
            final_severity=None,
            evidence_kind="omitted",
            evidence_quote=None,
            reviewer_assessment="both_weak",
        ),
        "SEC01-BP02": adversary_row(
            "SEC01-BP02",
            disposition="insufficient_evidence",
            final_status="Cannot Determine",
            final_severity=None,
            evidence_kind="omitted",
            evidence_quote=None,
        ),
    }
    candidates = candidate_rows(*reviewer_a.values())

    metrics = compute_quality_metrics(
        reviewer_a,
        reviewer_b,
        adversary,
        {"SEC01-BP01", "SEC01-BP02"},
        candidates,
    )

    assert metrics["bps_reviewed"] == 2
    assert metrics["candidate_overturn_rate"] == 0.5
    assert metrics["reviewer_consensus_overturn_rate"] == 1.0
    assert metrics["unresolved_count"] == 0
    assert metrics["adjudication_abstention_count"] == 1
    assert metrics["critical_high_precision"] == 0.0
    assert metrics["uncertainty_handling_rate"] == 0.0
    assert metrics["uncertainty_aligned_count"] == 0
    assert metrics["uncertainty_items"] == 2
    assert metrics["uncertainty_ids"] == ["SEC01-BP01", "SEC01-BP02"]
    assert metrics["unsupported_determinate_assertion_count"] == 2
    assert metrics["unsupported_determinate_assertion_ids"] == [
        "SEC01-BP01",
        "SEC01-BP02",
    ]
    assert metrics["unsupported_determinate_assertion_rate"] == 1.0
    assert metrics["unsupported_negative_assertion_count"] == 2
    assert metrics["unsupported_negative_assertion_ids"] == [
        "SEC01-BP01",
        "SEC01-BP02",
    ]
    assert metrics["unsupported_negative_assertion_rate"] == 1.0


def test_sparse_evidence_rewards_explicit_abstention():
    reviewer_a = {
        "SEC01-BP01": reviewer_row(
            "SEC01-BP01",
            candidate_status="Cannot Determine",
            reference_status="Cannot Determine",
            evidence_kind="omitted",
            evidence_quote=None,
            candidate_severity=None,
            reference_severity=None,
            recommendation_score=None,
        ),
    }
    reviewer_b = dict(reviewer_a)
    adversary = {
        "SEC01-BP01": adversary_row(
            "SEC01-BP01",
            final_status="Cannot Determine",
            final_severity=None,
            evidence_kind="omitted",
            evidence_quote=None,
        ),
    }
    candidates = candidate_rows(*reviewer_a.values())

    metrics = compute_quality_metrics(
        reviewer_a,
        reviewer_b,
        adversary,
        {"SEC01-BP01"},
        candidates,
    )

    assert metrics["uncertainty_aligned_count"] == 1
    assert metrics["uncertainty_items"] == 1
    assert metrics["uncertainty_aligned_ids"] == ["SEC01-BP01"]
    assert metrics["uncertainty_handling_rate"] == 1.0
    assert metrics["legitimate_unknown_count"] == 1
    assert metrics["evidence_availability_rate"] == 0.0
    assert metrics["unsupported_determinate_assertion_count"] == 0
    assert metrics["unsupported_determinate_assertion_rate"] is None


def test_provenance_backed_determinate_status_measures_overconservatism():
    candidate = reviewer_row(
        "SEC01-BP01",
        candidate_status="Cannot Determine",
        candidate_severity=None,
    )
    reviewer_a = {"SEC01-BP01": candidate}
    reviewer_b = {"SEC01-BP01": dict(candidate)}
    adversary = {
        "SEC01-BP01": adversary_row(
            "SEC01-BP01",
            disposition="accept_challenge",
        ),
    }

    metrics = compute_quality_metrics(
        reviewer_a,
        reviewer_b,
        adversary,
        {"SEC01-BP01"},
        candidate_rows(candidate),
    )

    assert metrics["uncertainty_items"] == 0
    assert metrics["candidate_uncertainty_count"] == 1
    assert metrics["overconservative_count"] == 1
    assert metrics["overconservative_rate"] == 1.0


def test_summary_reports_weighted_uncertainty_counts():
    summary = rq.summarize_metrics([
        {
            "uncertainty_aligned_count": 0,
            "uncertainty_items": 2,
            "determinate_assertion_count": 10,
            "unsupported_determinate_assertion_count": 2,
            "negative_assertion_count": 5,
            "unsupported_negative_assertion_count": 1,
        },
        {
            "uncertainty_aligned_count": 1,
            "uncertainty_items": 1,
            "determinate_assertion_count": 5,
            "unsupported_determinate_assertion_count": 0,
            "negative_assertion_count": 2,
            "unsupported_negative_assertion_count": 0,
        },
    ])

    assert summary["uncertainty_aligned_count"] == 1
    assert summary["uncertainty_items"] == 3
    assert summary["uncertainty_handling_rate"] == 0.3333
    assert summary["unsupported_determinate_assertion_rate"] == 0.1333
    assert summary["unsupported_negative_assertion_rate"] == 0.1429


def test_summary_uses_global_counts_for_overturn_rate():
    summary = rq.summarize_metrics([
        {
            "adjudicated_count": 100,
            "candidate_overturn_count": 10,
        },
        {
            "adjudicated_count": 1,
            "candidate_overturn_count": 1,
        },
    ])

    assert summary["candidate_overturn_rate"] == 0.1089


def test_load_candidates_uses_full_eval_prompt_and_requires_captured_report(tmp_path):
    path = tmp_path / "results.json"
    path.write_text(json.dumps({
        "model": "sonnet",
        "cases": [{
            "case_id": 2,
            "runs": [{"run_idx": 1, "assembled_text": "Full candidate report"}],
        }],
    }))

    candidates = load_candidates(path, {2}, runs_per_case=1, seed=42)

    assert len(candidates) == 1
    assert candidates[0].candidate_id == "candidate-001"
    assert candidates[0].report == "Full candidate report"
    assert "monolithic Java app" in candidates[0].workload


def test_load_candidates_rejects_legacy_results_without_report(tmp_path):
    path = tmp_path / "results.json"
    path.write_text(json.dumps({
        "model": "sonnet",
        "cases": [{"case_id": 2, "runs": [{"run_idx": 1, "assembled_head": "short"}]}],
    }))

    with pytest.raises(ValueError, match="no captured candidate reports"):
        load_candidates(path, {2}, runs_per_case=1, seed=42)


def test_raw_artifacts_use_explicit_isolated_directory(tmp_path):
    artifact = rq._write_raw_artifact(
        "candidate-001",
        "security",
        "reviewer-a",
        "reviewer/model",
        '{"rows":[]}',
        tmp_path / "fresh-responses",
    )

    expected = (
        tmp_path
        / "fresh-responses"
        / "candidate-001"
        / "security-reviewer-a-reviewer-model.txt"
    )
    assert expected.read_text() == '{"rows":[]}'
    assert artifact == str(expected)


def test_structured_ground_truth_consensus_preserves_status_and_severity():
    canonical = {"SEC01-BP01"}
    runs = []
    for model in MODELS:
        for run_idx in range(1, 4):
            runs.append({
                "model": model,
                "run_idx": run_idx,
                "valid_bps": ["SEC01-BP01"],
                "assessments": {
                    "SEC01-BP01": {
                        "bp_id": "SEC01-BP01",
                        "applicability": "applicable",
                        "expected_status": "Not Implemented",
                        "expected_severity": "High",
                        "evidence_basis": "The workload explicitly lacks this control.",
                        "confidence": "high",
                    }
                },
            })

    ground_truth = compute_ground_truth(runs, canonical)

    reference = ground_truth["reference_ledger"]["SEC01-BP01"]
    assert ground_truth["consensus_bps"] == ["SEC01-BP01"]
    assert reference["applicability"] == "applicable"
    assert reference["expected_status"] == "Not Implemented"
    assert reference["acceptable_severities"] == ["High"]
    assert reference["confidence"] == "high"


def test_ground_truth_uses_current_307_bp_pillar_corpus():
    assert len(build_canonical_bps()) == 307


def test_quality_orchestration_requires_complete_blind_and_adversarial_passes(
    tmp_path,
    monkeypatch,
):
    references = tmp_path / "references"
    references.mkdir()
    (references / "security.md").write_text("# SEC01-BP01 Example\nReference content.")
    monkeypatch.setattr(rq, "REFERENCES_DIR", references)
    monkeypatch.setattr(rq, "ARTIFACTS_DIR", tmp_path / "artifacts")
    monkeypatch.setattr(rq, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(rq, "PILLARS", (("security", "Security", "SEC"),))
    monkeypatch.setattr(rq.boto3, "client", lambda *args, **kwargs: object())

    calls = []

    def fake_invoke(client, model_id, prompt, region, max_tokens):
        calls.append((model_id, prompt))
        if "adversarial adjudicator" in prompt:
            output = json.dumps({"rows": [adversary_row("SEC01-BP01")]})
        else:
            output = json.dumps({"rows": [reviewer_row("SEC01-BP01")]})
        return {
            "model_id": model_id,
            "output": output,
            "input_tokens": 100,
            "output_tokens": 50,
            "latency_s": 0.1,
        }

    monkeypatch.setattr(rq, "_invoke_model", fake_invoke)
    candidate = Candidate(
        candidate_id="candidate-001",
        case_id=1,
        run_idx=1,
        workload=WORKLOAD,
        report="| SEC01-BP01 | Not Implemented | High | Evidence | Recommendation |",
        source_model="sonnet",
        source_mode="skill",
    )

    result = run_quality_review(
        [candidate],
        ("openai.gpt-oss-120b", "us.amazon.nova-pro-v1:0"),
        "us.deepseek.r1-v1:0",
        "us-east-1",
        1024,
        2,
        42,
    )

    reviewed = result["candidates"][0]
    assert reviewed["status"] == "complete"
    assert reviewed["pillars"]["SEC"]["status"] == "complete"
    assert reviewed["summary"]["bps_reviewed"] == 1
    assert reviewed["resource_usage"]["total"]["calls"] == 3
    assert result["resource_usage"]["calls"] == 3
    assert len(calls) == 3

    calls.clear()
    resumed = run_quality_review(
        [candidate],
        ("openai.gpt-oss-120b", "us.amazon.nova-pro-v1:0"),
        "us.deepseek.r1-v1:0",
        "us-east-1",
        1024,
        2,
        42,
        chunk_size=1,
        retries=1,
        resume=result,
    )

    assert resumed["candidates"][0]["status"] == "complete"
    assert resumed["resource_usage"]["calls"] == 3
    assert calls == []


def test_quality_orchestration_never_scores_incomplete_reviewer_output(
    tmp_path,
    monkeypatch,
):
    references = tmp_path / "references"
    references.mkdir()
    (references / "security.md").write_text("# SEC01-BP01 Example\nReference content.")
    monkeypatch.setattr(rq, "REFERENCES_DIR", references)
    monkeypatch.setattr(rq, "ARTIFACTS_DIR", tmp_path / "artifacts")
    monkeypatch.setattr(rq, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(rq, "PILLARS", (("security", "Security", "SEC"),))
    monkeypatch.setattr(rq.boto3, "client", lambda *args, **kwargs: object())
    monkeypatch.setattr(
        rq,
        "_invoke_model",
        lambda client, model_id, prompt, region, max_tokens: {
            "model_id": model_id,
            "output": '{"rows":[]}',
            "input_tokens": 1,
            "output_tokens": 1,
            "latency_s": 0.1,
        },
    )
    candidate = Candidate(
        candidate_id="candidate-001",
        case_id=1,
        run_idx=1,
        workload=WORKLOAD,
        report="| SEC01-BP01 | Cannot Determine | | Need evidence | Verify |",
        source_model="sonnet",
        source_mode="skill",
    )

    result = run_quality_review(
        [candidate],
        ("openai.gpt-oss-120b", "us.amazon.nova-pro-v1:0"),
        "us.deepseek.r1-v1:0",
        "us-east-1",
        1024,
        2,
        42,
    )

    reviewed = result["candidates"][0]
    assert reviewed["status"] == "incomplete"
    assert reviewed["pillars"]["SEC"]["status"] == "incomplete_blind_review"
    assert reviewed["summary"] == {"completed_units": 0}
    assert result["summary"] == {"completed_units": 0}
