#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Blind and adversarial quality evaluation for captured wa-review reports.

The existing effectiveness harness measures Best Practice citation coverage.
This module adds an evaluation-only quality layer for evidence, status,
severity, recommendations, and uncertainty. Candidate identity and existing
scores are deliberately excluded from all reviewer prompts.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import random
import re
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

import boto3
from botocore.config import Config as BotoConfig

SCRIPT_DIR = Path(__file__).resolve().parent
EVALS_DIR = SCRIPT_DIR.parent
REPO_ROOT = EVALS_DIR.parent
REFERENCES_DIR = REPO_ROOT / "skills" / "wa-review" / "references" / "pillars"
ARTIFACTS_DIR = SCRIPT_DIR / "review_artifacts"
DEFAULT_RESULTS = SCRIPT_DIR / "wa_review_effectiveness.json"
DEFAULT_OUTPUT = SCRIPT_DIR / "review_quality_results.json"

sys.path.insert(0, str(EVALS_DIR))
from benchmark import (  # noqa: E402
    _is_mantle_model,
    call_mantle_model,
    call_model,
    compute_cost,
    load_config as load_benchmark_config,
)

SCHEMA_VERSION = 3
DEFAULT_REVIEWERS = (
    "openai.gpt-oss-120b",
    "us.amazon.nova-pro-v1:0",
)
DEFAULT_ADVERSARY = "us.deepseek.r1-v1:0"
DEFAULT_REGION = "us-east-1"
DEFAULT_MAX_TOKENS = 16_384
DEFAULT_CHUNK_SIZE = 20
DEFAULT_RETRIES = 1
MODEL_OUTPUT_LIMITS = {
    "amazon": 9_999,
}

BP_PATTERN = re.compile(r"\b([A-Z]{2,}\d{1,3})[-‐‑–]BP(\d{1,3})\b")
CANONICAL_HEADING_PATTERN = re.compile(
    r"^# ([A-Z]{2,}\d{1,3}-BP\d{1,3})\b",
    re.MULTILINE,
)
EVIDENCE_SEGMENT_PATTERN = re.compile(
    r"(?:\r?\n)+|(?<=[.!?])\s+|[,;]\s+"
)

STATUSES = (
    "Implemented",
    "Partially Implemented",
    "Not Implemented",
    "Not Applicable",
    "Cannot Determine",
    "Missing",
)
APPLICABILITY = ("applicable", "not_applicable", "uncertain")
SEVERITIES = ("Low", "Medium", "High", "Critical")
EVIDENCE_KINDS = (
    "explicit_presence",
    "explicit_absence",
    "explicit_partial",
    "authoritative_absence",
    "omitted",
    "inconclusive",
    "not_applicable",
)
CONFIDENCE_LEVELS = ("low", "medium", "high")
DISPOSITIONS = (
    "uphold_candidate",
    "accept_challenge",
    "insufficient_evidence",
)
REVIEWER_ASSESSMENTS = (
    "both_hold",
    "reviewer_a_stronger",
    "reviewer_b_stronger",
    "both_weak",
)

NULL_SEVERITY_STATUSES = {
    "Implemented",
    "Not Applicable",
    "Cannot Determine",
}
DETERMINATE_STATUSES = {
    "Implemented",
    "Partially Implemented",
    "Not Implemented",
}
EVIDENCE_KIND_STATUSES = {
    "explicit_presence": {"Implemented"},
    "explicit_absence": {"Not Implemented"},
    "explicit_partial": {"Partially Implemented"},
    "authoritative_absence": {"Not Implemented"},
    "omitted": {"Cannot Determine"},
    "inconclusive": {"Cannot Determine"},
    "not_applicable": {"Not Applicable"},
}

PILLARS = (
    ("operational-excellence", "Operational Excellence", "OPS"),
    ("security", "Security", "SEC"),
    ("reliability", "Reliability", "REL"),
    ("performance-efficiency", "Performance Efficiency", "PERF"),
    ("cost-optimization", "Cost Optimization", "COST"),
    ("sustainability", "Sustainability", "SUS"),
)


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    case_id: int
    run_idx: int
    workload: str
    report: str
    source_model: str | None
    source_mode: str | None
    citation_metrics: dict[str, Any] | None = None
    generation_usage: dict[str, Any] | None = None


def normalize_bp_id(value: str) -> str:
    """Normalize common Unicode hyphens in a canonical BP identifier."""
    match = BP_PATTERN.search(value.upper())
    if not match:
        raise ValueError(f"invalid BP ID: {value!r}")
    return f"{match.group(1)}-BP{match.group(2)}"


def _normalize_choice(value: Any, choices: Iterable[str], field: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    by_key = {choice.lower().replace("_", " "): choice for choice in choices}
    key = value.strip().lower().replace("_", " ")
    if key not in by_key:
        raise ValueError(f"invalid {field}: {value!r}")
    return by_key[key]


def normalize_status(value: Any) -> str:
    return _normalize_choice(value, STATUSES, "status")


def normalize_severity(value: Any) -> str | None:
    if value is None or value == "":
        return None
    return _normalize_choice(value, SEVERITIES, "severity")


def normalize_evidence_kind(value: Any) -> str:
    return _normalize_choice(value, EVIDENCE_KINDS, "evidence_kind")


def normalize_confidence(value: Any) -> str:
    """Treat omitted model confidence conservatively without losing the row."""
    if value is None or value == "":
        return "low"
    return _normalize_choice(value, CONFIDENCE_LEVELS, "confidence")


def validate_status_severity(
    status: str,
    severity: str | None,
    *,
    status_field: str,
    severity_field: str,
) -> None:
    if status in NULL_SEVERITY_STATUSES and severity is not None:
        raise ValueError(f"{severity_field} must be null for {status}")


def _normalized_text(value: str) -> str:
    return " ".join(value.split()).casefold()


def normalize_evidence_quote(value: Any) -> str | None:
    if value is None or value == "":
        return None
    if not isinstance(value, str):
        raise ValueError("evidence_quote must be a string or null")
    quote = " ".join(value.split())
    if not quote:
        return None
    return quote


def build_evidence_catalog(workload: str) -> dict[str, str]:
    """Create stable IDs for exact, atomic spans from the workload."""
    catalog: dict[str, str] = {}
    seen: set[str] = set()
    for segment in EVIDENCE_SEGMENT_PATTERN.split(workload):
        quote = normalize_evidence_quote(segment)
        if quote is None:
            continue
        normalized = _normalized_text(quote)
        if normalized in seen:
            continue
        seen.add(normalized)
        catalog[f"W{len(catalog) + 1:03d}"] = quote
    if not catalog:
        raise ValueError("workload has no evidence spans")
    return catalog


def format_evidence_catalog(workload: str) -> str:
    return "\n".join(
        f"{quote_id}: {json.dumps(quote)}"
        for quote_id, quote in build_evidence_catalog(workload).items()
    )


def resolve_reviewer_evidence_quote(
    row: dict[str, Any],
    workload: str,
) -> tuple[str | None, str | None]:
    """Resolve a model-selected catalog ID while accepting legacy exact quotes."""
    quote_id_value = row.get("evidence_quote_id")
    supplied_quote = normalize_evidence_quote(row.get("evidence_quote"))
    if quote_id_value is None or quote_id_value == "":
        return supplied_quote, None
    if not isinstance(quote_id_value, str):
        raise ValueError("evidence_quote_id must be a string or null")

    quote_id = quote_id_value.strip().upper()
    catalog = build_evidence_catalog(workload)
    if quote_id not in catalog:
        raise ValueError(f"invalid evidence_quote_id: {quote_id_value!r}")
    resolved_quote = catalog[quote_id]
    if (
        supplied_quote is not None
        and _normalized_text(supplied_quote) != _normalized_text(resolved_quote)
    ):
        raise ValueError(
            "evidence_quote conflicts with the selected evidence_quote_id"
        )
    return resolved_quote, quote_id


def validate_evidence_provenance(
    status: str,
    severity: str | None,
    evidence_kind: str,
    evidence_quote: str | None,
    workload: str,
    *,
    status_field: str,
    severity_field: str,
    allow_authoritative_absence: bool = False,
) -> None:
    validate_status_severity(
        status,
        severity,
        status_field=status_field,
        severity_field=severity_field,
    )
    if status == "Missing":
        raise ValueError(f"{status_field} cannot be Missing")
    allowed_statuses = EVIDENCE_KIND_STATUSES[evidence_kind]
    if status not in allowed_statuses:
        raise ValueError(
            f"{status_field} {status!r} is incompatible with "
            f"evidence_kind {evidence_kind!r}"
        )
    if evidence_kind == "authoritative_absence" and not allow_authoritative_absence:
        raise ValueError(
            "authoritative_absence is not allowed for a verbal-only workload"
        )
    quote_required = evidence_kind in {
        "explicit_presence",
        "explicit_absence",
        "explicit_partial",
        "inconclusive",
    }
    if quote_required and evidence_quote is None:
        raise ValueError(f"evidence_quote is required for {evidence_kind}")
    if evidence_kind in {"omitted", "not_applicable"} and evidence_quote is not None:
        raise ValueError(f"evidence_quote must be null for {evidence_kind}")
    if evidence_quote is not None:
        normalized_quote = _normalized_text(evidence_quote)
        if normalized_quote not in _normalized_text(workload):
            raise ValueError(
                f"evidence_quote is not an exact workload quote: {evidence_quote!r}"
            )


def _clean_markdown_cell(value: str) -> str:
    return value.strip().strip("`*_").strip()


def parse_candidate_ledger(report: str) -> dict[str, dict[str, Any]]:
    """Parse canonical BP status/severity cells from the candidate Markdown."""
    rows: dict[str, dict[str, Any]] = {}
    duplicates: set[str] = set()
    for line in report.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [_clean_markdown_cell(cell) for cell in stripped.strip("|").split("|")]
        if len(cells) < 3 or not BP_PATTERN.fullmatch(cells[0].upper()):
            continue
        bp_id = normalize_bp_id(cells[0])
        try:
            status = normalize_status(cells[1])
        except ValueError:
            continue
        severity_cell = cells[2]
        severity = normalize_severity(
            None
            if severity_cell in {"", "-", "—", "N/A", "n/a"}
            else severity_cell
        )
        validate_status_severity(
            status,
            severity,
            status_field=f"{bp_id}.candidate_status",
            severity_field=f"{bp_id}.candidate_severity",
        )
        if bp_id in rows:
            duplicates.add(bp_id)
            continue
        rows[bp_id] = {
            "bp_id": bp_id,
            "candidate_status": status,
            "candidate_severity": severity,
        }
    if duplicates:
        raise ValueError(
            "candidate ledger has duplicate BP rows: "
            + ", ".join(sorted(duplicates))
        )
    if not rows:
        raise ValueError("candidate report has no parseable canonical BP ledger rows")
    return rows


def normalize_reference_row(row: dict[str, Any]) -> dict[str, Any]:
    evidence_basis = row.get("evidence_basis")
    if not isinstance(evidence_basis, str) or not evidence_basis.strip():
        raise ValueError("evidence_basis must be a non-empty string")
    return {
        "bp_id": normalize_bp_id(str(row.get("bp_id", ""))),
        "applicability": _normalize_choice(
            row.get("applicability"),
            APPLICABILITY,
            "applicability",
        ),
        "expected_status": normalize_status(row.get("expected_status")),
        "expected_severity": normalize_severity(row.get("expected_severity")),
        "evidence_basis": evidence_basis.strip(),
        "confidence": normalize_confidence(row.get("confidence")),
    }


def decode_json_values(text: str) -> list[Any]:
    """Decode JSON values from plain or fenced model output."""
    decoder = json.JSONDecoder()
    values: list[Any] = []
    cursor = 0
    while cursor < len(text):
        starts = [idx for idx in (text.find("{", cursor), text.find("[", cursor)) if idx >= 0]
        if not starts:
            break
        start = min(starts)
        try:
            value, end = decoder.raw_decode(text[start:])
        except json.JSONDecodeError:
            cursor = start + 1
            continue
        values.append(value)
        cursor = start + end
    return values


def _rows_from_json_values(values: Iterable[Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for value in values:
        if isinstance(value, dict) and isinstance(value.get("rows"), list):
            rows.extend(row for row in value["rows"] if isinstance(row, dict))
        elif isinstance(value, list):
            rows.extend(row for row in value if isinstance(row, dict))
    return rows


def normalize_reviewer_row(
    row: dict[str, Any],
    *,
    workload: str,
    candidate_rows: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    bp_id = normalize_bp_id(str(row.get("bp_id", "")))
    if bp_id not in candidate_rows:
        raise ValueError(f"candidate ledger is missing {bp_id}")
    score = row.get("recommendation_score")
    if score is not None:
        if not isinstance(score, int) or not 1 <= score <= 5:
            raise ValueError("recommendation_score must be an integer from 1 to 5")
    challenge = row.get("challenge")
    if challenge is not None and not isinstance(challenge, str):
        raise ValueError("challenge must be a string or null")
    rationale = row.get("evidence_rationale")
    if not isinstance(rationale, str) or not rationale.strip():
        raise ValueError("evidence_rationale must be a non-empty string")
    reference_status = normalize_status(row.get("reference_status"))
    reference_severity = normalize_severity(row.get("reference_severity"))
    evidence_kind = normalize_evidence_kind(row.get("evidence_kind"))
    evidence_quote, evidence_quote_id = resolve_reviewer_evidence_quote(
        row,
        workload,
    )
    validate_evidence_provenance(
        reference_status,
        reference_severity,
        evidence_kind,
        evidence_quote,
        workload,
        status_field="reference_status",
        severity_field="reference_severity",
    )
    candidate = candidate_rows[bp_id]
    return {
        "bp_id": bp_id,
        "candidate_status": candidate["candidate_status"],
        "reference_status": reference_status,
        "evidence_kind": evidence_kind,
        "evidence_quote": evidence_quote,
        "evidence_quote_id": evidence_quote_id,
        "evidence_rationale": rationale.strip(),
        "candidate_severity": candidate["candidate_severity"],
        "reference_severity": reference_severity,
        "recommendation_score": score,
        "challenge": challenge,
        "confidence": normalize_confidence(row.get("confidence")),
    }


def normalize_adversary_row(
    row: dict[str, Any],
    *,
    workload: str,
    reviewer_a: dict[str, dict[str, Any]],
    reviewer_b: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    bp_id = normalize_bp_id(str(row.get("bp_id", "")))
    if bp_id not in reviewer_a or bp_id not in reviewer_b:
        raise ValueError(f"review material is missing {bp_id}")
    rationale = row.get("rationale")
    if not isinstance(rationale, str) or not rationale.strip():
        raise ValueError("rationale must be a non-empty string")
    final_status = normalize_status(row.get("final_status"))
    final_severity = normalize_severity(row.get("final_severity"))
    evidence_kind = normalize_evidence_kind(row.get("evidence_kind"))
    evidence_quote = normalize_evidence_quote(row.get("evidence_quote"))
    validate_evidence_provenance(
        final_status,
        final_severity,
        evidence_kind,
        evidence_quote,
        workload,
        status_field="final_status",
        severity_field="final_severity",
    )
    allowed_conclusions = {
        (
            reviewer["reference_status"],
            reviewer["evidence_kind"],
            _normalized_text(reviewer["evidence_quote"])
            if reviewer["evidence_quote"] is not None
            else None,
        )
        for reviewer in (reviewer_a[bp_id], reviewer_b[bp_id])
    }
    final_conclusion = (
        final_status,
        evidence_kind,
        _normalized_text(evidence_quote) if evidence_quote is not None else None,
    )
    if final_conclusion not in allowed_conclusions:
        raise ValueError(
            "final conclusion must use a status and evidence pair supplied "
            "by a blind reviewer"
        )
    disposition = _normalize_choice(
        row.get("disposition"),
        DISPOSITIONS,
        "disposition",
    )
    candidate_status = reviewer_a[bp_id]["candidate_status"]
    if reviewer_b[bp_id]["candidate_status"] != candidate_status:
        raise ValueError("blind reviewers have inconsistent candidate status")
    if disposition == "uphold_candidate" and final_status != candidate_status:
        raise ValueError("uphold_candidate requires final_status to match candidate")
    if disposition == "insufficient_evidence" and final_status != "Cannot Determine":
        raise ValueError(
            "insufficient_evidence requires final_status Cannot Determine"
        )
    return {
        "bp_id": bp_id,
        "disposition": disposition,
        "final_status": final_status,
        "final_severity": final_severity,
        "evidence_kind": evidence_kind,
        "evidence_quote": evidence_quote,
        "reviewer_assessment": _normalize_choice(
            row.get("reviewer_assessment"),
            REVIEWER_ASSESSMENTS,
            "reviewer_assessment",
        ),
        "rationale": rationale.strip(),
        "confidence": normalize_confidence(row.get("confidence")),
    }


def parse_model_rows(
    text: str,
    expected_ids: Iterable[str],
    normalizer,
) -> dict[str, Any]:
    """Parse and validate a model's per-BP JSON response."""
    expected = set(expected_ids)
    parsed: dict[str, dict[str, Any]] = {}
    invalid: list[str] = []
    duplicates: list[str] = []

    for raw_row in _rows_from_json_values(decode_json_values(text)):
        try:
            row = normalizer(raw_row)
        except ValueError as exc:
            raw_id = raw_row.get("bp_id", "(unknown BP)")
            invalid.append(f"{raw_id}: {exc}")
            continue
        bp_id = row["bp_id"]
        if bp_id in parsed:
            duplicates.append(bp_id)
            continue
        parsed[bp_id] = row

    actual = set(parsed)
    missing = sorted(expected - actual)
    unexpected = sorted(actual - expected)
    complete = (
        bool(expected)
        and not missing
        and not unexpected
        and not duplicates
        and not invalid
    )
    return {
        "complete": complete,
        "rows": {bp_id: parsed[bp_id] for bp_id in sorted(parsed) if bp_id in expected},
        "missing_ids": missing,
        "unexpected_ids": unexpected,
        "duplicate_ids": sorted(set(duplicates)),
        "invalid_rows": invalid,
    }


def canonical_ids(reference: str, prefix: str) -> list[str]:
    return sorted(
        bp_id
        for bp_id in CANONICAL_HEADING_PATTERN.findall(reference)
        if bp_id.startswith(prefix)
    )


def chunk_values(values: Sequence[str], chunk_size: int) -> list[list[str]]:
    """Split an ordered sequence into stable, non-empty chunks."""
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")
    return [
        list(values[index:index + chunk_size])
        for index in range(0, len(values), chunk_size)
    ]


def extract_reference_subset(reference: str, selected_ids: Iterable[str]) -> str:
    """Return only the canonical BP sections needed for a review chunk."""
    selected = set(selected_ids)
    matches = list(CANONICAL_HEADING_PATTERN.finditer(reference))
    sections: list[str] = []
    found: set[str] = set()
    for index, match in enumerate(matches):
        bp_id = match.group(1)
        if bp_id not in selected:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(reference)
        sections.append(reference[match.start():end].strip())
        found.add(bp_id)
    missing = selected - found
    if missing:
        raise ValueError(
            "reference is missing selected BP IDs: "
            + ", ".join(sorted(missing))
        )
    return "\n\n".join(sections)


def extract_pillar_excerpt(
    report: str,
    prefix: str,
    selected_ids: Iterable[str] | None = None,
) -> str:
    """Extract candidate lines containing the requested canonical BP IDs."""
    selected = set(selected_ids) if selected_ids is not None else None
    lines: list[str] = []
    seen: set[str] = set()
    for line in report.splitlines():
        ids = {
            normalize_bp_id(match.group(0))
            for match in BP_PATTERN.finditer(line)
            if match.group(1).startswith(prefix)
        }
        if selected is not None:
            ids &= selected
        if ids and line not in seen:
            seen.add(line)
            lines.append(line)
    return "\n".join(lines) if lines else "(No candidate rows found for these BPs.)"


def build_blind_prompt(
    workload: str,
    candidate_excerpt: str,
    reference: str,
    pillar_name: str,
    expected_count: int,
    selected_ids: Sequence[str] | None = None,
) -> str:
    """Build a prompt with no candidate runtime, model, or condition metadata."""
    ids = (
        list(selected_ids)
        if selected_ids is not None
        else CANONICAL_HEADING_PATTERN.findall(reference)
    )
    id_list = ", ".join(ids) if ids else "(IDs are the canonical headings below)"
    return f"""You are an independent AWS Well-Architected quality reviewer.

Review the candidate ledger for the {pillar_name} pillar. You are not told which
system produced it. Use only the workload and authoritative pillar reference
below. Evaluate exactly these {expected_count} Best Practices, including
candidate omissions:
{id_list}

Do not infer an absent control as Not Implemented when the supplied evidence
only supports Cannot Determine. `reference_status` is your independent
implementation-status judgment from workload evidence. It is NEVER a documented
risk level. Low, Medium, High, and Critical belong only in severity fields.

For each BP return:
- reference_status: Implemented, Partially Implemented, Not Implemented,
  Not Applicable, or Cannot Determine
- reference_severity: Critical, High, Medium, Low, or null
- evidence_kind: exactly one of explicit_presence, explicit_absence,
  explicit_partial, omitted, inconclusive, or not_applicable
- evidence_quote_id: an exact W### identifier from WORKLOAD EVIDENCE CATALOG,
  or null; the harness resolves it to an exact contiguous quote from WORKLOAD
- evidence_rationale: a concise explanation of how that evidence maps to the BP
- recommendation_score: integer 1-5, or null when no recommendation applies
- challenge: correction of at most 12 words, or null when the candidate is correct
- confidence: high, medium, or low

Return ONLY one JSON object with this shape:
{{"rows":[{{"bp_id":"SEC01-BP01",
"reference_status":"Cannot Determine","reference_severity":null,
"evidence_kind":"omitted","evidence_quote_id":null,
"evidence_rationale":"The workload does not describe this control.",
"recommendation_score":null,"challenge":"Candidate omitted this BP.",
"confidence":"high"}}]}}

The rows array must contain exactly one unique row for every canonical BP in the
list above. Return minified JSON without indentation or narrative.
The harness parses candidate status and severity itself; do not return either.
Apply these mandatory mappings:
- explicit_presence -> Implemented, with a non-null workload evidence ID
- explicit_partial -> Partially Implemented, with a non-null workload evidence ID
- explicit_absence -> Not Implemented, with a non-null workload evidence ID
- omitted or inconclusive -> Cannot Determine
- not_applicable -> Not Applicable

Never write or paraphrase quote text and do not return an evidence_quote field;
select its catalog ID. For omitted and not_applicable evidence,
evidence_quote_id MUST be null. For inconclusive evidence, select the exact
inconclusive workload span. `authoritative_absence` is forbidden because this
is a verbal-only workload. Use null reference_severity for Implemented, Not
Applicable, and Cannot Determine. The candidate ledger and pillar reference are
not evidence of workload implementation. In particular, phrases such as "not
described", "no documentation provided", and "no evidence of" mean omitted and
Cannot Determine, not explicit_absence.

===== WORKLOAD =====
{workload}

===== WORKLOAD EVIDENCE CATALOG =====
{format_evidence_catalog(workload)}

===== CANDIDATE PILLAR LEDGER =====
{candidate_excerpt}

===== AUTHORITATIVE PILLAR REFERENCE =====
{reference}
"""


def build_adversary_prompt(
    workload: str,
    candidate_excerpt: str,
    reference: str,
    reviewer_a: dict[str, dict[str, Any]],
    reviewer_b: dict[str, dict[str, Any]],
    selected_ids: list[str],
    pillar_name: str,
) -> str:
    items = []
    for bp_id in selected_ids:
        items.append({
            "bp_id": bp_id,
            "reviewer_a": reviewer_a[bp_id],
            "reviewer_b": reviewer_b[bp_id],
        })
    return f"""You are the adversarial adjudicator for an AWS Well-Architected
evaluation. Challenge both the candidate and the two anonymous reviewers for the
{pillar_name} pillar. Look for anchoring, shared unsupported assumptions,
severity inflation or understatement, contradictory evidence, and generic
recommendations.

Adjudicate every supplied BP. Return ONLY:
{{"rows":[{{"bp_id":"SEC01-BP01",
"disposition":"insufficient_evidence",
"final_status":"Cannot Determine","final_severity":null,
"evidence_kind":"omitted","evidence_quote":null,
"reviewer_assessment":"both_hold",
"rationale":"The workload omits the implementation detail.",
"confidence":"high"}}]}}

Allowed dispositions: uphold_candidate, accept_challenge, insufficient_evidence.
Allowed reviewer assessments: both_hold, reviewer_a_stronger,
reviewer_b_stronger, both_weak. Include exactly one unique row for each selected
BP and no narrative outside the JSON.

You MUST select a complete (final_status, evidence_kind, evidence_quote) tuple
already supplied by reviewer A or reviewer B. Do not introduce a new quote,
reinterpret omitted information as absence, or use the candidate/reference as
implementation evidence. If both reviewers use omitted evidence, final_status
must be Cannot Determine. `authoritative_absence` is forbidden for this
verbal-only workload. Implemented, Not Applicable, and Cannot Determine require
null final_severity. `uphold_candidate` requires final_status to match the
parsed candidate status. `insufficient_evidence` requires Cannot Determine.

===== WORKLOAD =====
{workload}

===== CANDIDATE PILLAR LEDGER =====
{candidate_excerpt}

===== ANONYMOUS REVIEW MATERIAL =====
{json.dumps(items, indent=2)}

===== AUTHORITATIVE PILLAR REFERENCE =====
{reference}
"""


def model_family(model_id: str | None) -> str:
    value = (model_id or "").lower()
    if (
        "anthropic" in value
        or "claude" in value
        or any(name in value for name in ("sonnet", "opus", "haiku", "fable"))
    ):
        return "anthropic"
    if "openai" in value or "gpt" in value:
        return "openai"
    if "amazon" in value or "nova" in value:
        return "amazon"
    if "deepseek" in value:
        return "deepseek"
    if "meta" in value or "llama" in value:
        return "meta"
    if "mistral" in value:
        return "mistral"
    return value.split(".")[0]


def validate_panel(
    source_models: Iterable[str | None],
    reviewers: Iterable[str],
    adversary: str,
) -> None:
    reviewer_list = list(reviewers)
    reviewer_families = [model_family(model) for model in reviewer_list]
    if len(reviewer_list) != 2:
        raise ValueError("exactly two blind reviewer models are required")
    if len(set(reviewer_families)) != 2:
        raise ValueError("blind reviewers must come from different model families")
    source_families = {model_family(model) for model in source_models if model}
    overlap = source_families & set(reviewer_families)
    if overlap:
        raise ValueError(
            "candidate-family self-grading is not allowed; replace reviewer "
            f"families: {', '.join(sorted(overlap))}"
        )
    adversary_family = model_family(adversary)
    if adversary_family in set(reviewer_families) | source_families:
        raise ValueError("the adversary must use a third, non-candidate model family")


def load_candidates(
    results_path: Path,
    selected_cases: set[int] | None,
    runs_per_case: int,
    seed: int,
) -> list[Candidate]:
    data = json.loads(results_path.read_text())
    eval_cases = {
        int(case["id"]): case["prompt"]
        for case in json.loads(
            (REPO_ROOT / "skills" / "wa-review" / "evals" / "evals.json").read_text()
        )["evals"]
    }
    pending: list[dict[str, Any]] = []
    for case in data.get("cases", []):
        case_id = int(case["case_id"])
        if selected_cases is not None and case_id not in selected_cases:
            continue
        successful = [
            run
            for run in case.get("runs", [])
            if "error" not in run and isinstance(run.get("assembled_text"), str)
            and run["assembled_text"].strip()
        ]
        for run in successful[:runs_per_case]:
            report_metrics = run.get("report", {})
            pending.append({
                "case_id": case_id,
                "run_idx": int(run.get("run_idx", 0)),
                "workload": eval_cases[case_id],
                "report": run["assembled_text"],
                "source_model": data.get("model"),
                "source_mode": data.get("mode") or data.get("runtime"),
                "citation_metrics": {
                    key: report_metrics.get(key)
                    for key in (
                        "cited_count",
                        "valid_cited_count",
                        "true_positives",
                        "false_positives",
                        "false_negatives",
                        "recall",
                        "precision",
                        "f1",
                    )
                },
                "generation_usage": {
                    "ground_truth_count": run.get("gt_count"),
                    "cost_usd": run.get("total_cost_usd"),
                    "wall_s": run.get("wall_s"),
                    "input_tokens": run.get("input_tokens"),
                    "output_tokens": run.get("output_tokens"),
                },
            })
    if not pending:
        raise ValueError(
            "no captured candidate reports found; regenerate effectiveness "
            "results with a harness that stores assembled_text"
        )

    random.Random(seed).shuffle(pending)
    return [
        Candidate(candidate_id=f"candidate-{index:03d}", **candidate)
        for index, candidate in enumerate(pending, start=1)
    ]


def scoped_prefixes(case_id: int) -> set[str]:
    return {"SEC", "REL"} if case_id == 4 else {prefix for _, _, prefix in PILLARS}


def _invoke_model(
    client,
    model_id: str,
    prompt: str,
    region: str,
    max_tokens: int,
) -> dict[str, Any]:
    effective_max_tokens = min(
        max_tokens,
        MODEL_OUTPUT_LIMITS.get(model_family(model_id), max_tokens),
    )
    messages = [{"role": "user", "content": [{"text": prompt}]}]
    if _is_mantle_model(model_id):
        result = call_mantle_model(
            model_id,
            messages,
            max_tokens=effective_max_tokens,
            temperature=0,
            region=region,
        )
    else:
        result = call_model(
            client,
            model_id,
            messages,
            max_tokens=effective_max_tokens,
            temperature=0,
            include_reasoning=False,
        )
    result["requested_max_tokens"] = max_tokens
    result["effective_max_tokens"] = effective_max_tokens
    return result


def _artifact_name(
    candidate_id: str,
    pillar_slug: str,
    role: str,
    model: str,
    artifacts_dir: Path | None = None,
) -> Path:
    safe_model = re.sub(r"[^a-zA-Z0-9._-]+", "-", model)
    root = (artifacts_dir or ARTIFACTS_DIR).expanduser().resolve()
    return root / candidate_id / f"{pillar_slug}-{role}-{safe_model}.txt"


def _write_raw_artifact(
    candidate_id: str,
    pillar_slug: str,
    role: str,
    model: str,
    text: str,
    artifacts_dir: Path | None = None,
) -> str:
    path = _artifact_name(
        candidate_id,
        pillar_slug,
        role,
        model,
        artifacts_dir,
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def select_adversarial_ids(
    reviewer_a: dict[str, dict[str, Any]],
    reviewer_b: dict[str, dict[str, Any]],
    seed: int,
    sample_rate: float = 0.10,
) -> list[str]:
    selected: set[str] = set()
    agreements: list[str] = []
    compared_fields = (
        "reference_status",
        "reference_severity",
        "evidence_kind",
        "evidence_quote",
    )
    for bp_id in sorted(set(reviewer_a) & set(reviewer_b)):
        a = reviewer_a[bp_id]
        b = reviewer_b[bp_id]
        disagrees = any(a[field] != b[field] for field in compared_fields)
        recommendation_gap = (
            a["recommendation_score"] is not None
            and b["recommendation_score"] is not None
            and abs(a["recommendation_score"] - b["recommendation_score"]) >= 2
        )
        high_risk = (
            a["candidate_severity"] in {"Critical", "High"}
            or b["candidate_severity"] in {"Critical", "High"}
        )
        challenged = (
            a["candidate_status"] != a["reference_status"]
            or b["candidate_status"] != b["reference_status"]
            or a["candidate_severity"] != a["reference_severity"]
            or b["candidate_severity"] != b["reference_severity"]
        )
        if disagrees or recommendation_gap or high_risk or challenged:
            selected.add(bp_id)
        else:
            agreements.append(bp_id)

    if agreements and sample_rate > 0:
        sample_size = max(1, math.ceil(len(agreements) * sample_rate))
        selected.update(random.Random(seed).sample(agreements, min(sample_size, len(agreements))))
    return sorted(selected)


def agreement_rate(values_a: list[Any], values_b: list[Any]) -> float | None:
    if not values_a or len(values_a) != len(values_b):
        return None
    return round(sum(a == b for a, b in zip(values_a, values_b)) / len(values_a), 4)


def cohen_kappa(
    values_a: list[Any],
    values_b: list[Any],
    ordered_categories: list[Any] | None = None,
) -> float | None:
    """Compute unweighted or quadratic-weighted Cohen's kappa."""
    if not values_a or len(values_a) != len(values_b):
        return None
    categories = ordered_categories or sorted(set(values_a) | set(values_b))
    if len(categories) == 1:
        return 1.0
    indexes = {value: index for index, value in enumerate(categories)}
    count = len(values_a)
    marginal_a = [0] * len(categories)
    marginal_b = [0] * len(categories)

    def weight(left: Any, right: Any) -> float:
        if ordered_categories is None:
            return 1.0 if left == right else 0.0
        distance = abs(indexes[left] - indexes[right]) / (len(categories) - 1)
        return 1.0 - distance**2

    observed = 0.0
    for left, right in zip(values_a, values_b):
        marginal_a[indexes[left]] += 1
        marginal_b[indexes[right]] += 1
        observed += weight(left, right)
    observed /= count

    expected = 0.0
    for left in categories:
        for right in categories:
            expected += (
                marginal_a[indexes[left]]
                * marginal_b[indexes[right]]
                * weight(left, right)
            )
    expected /= count**2
    if expected == 1:
        return 1.0
    return round((observed - expected) / (1 - expected), 4)


def severity_within_one(values_a: list[str], values_b: list[str]) -> float | None:
    if not values_a or len(values_a) != len(values_b):
        return None
    levels = {severity: index for index, severity in enumerate(SEVERITIES)}
    return round(
        sum(abs(levels[a] - levels[b]) <= 1 for a, b in zip(values_a, values_b))
        / len(values_a),
        4,
    )


def compute_quality_metrics(
    reviewer_a: dict[str, dict[str, Any]],
    reviewer_b: dict[str, dict[str, Any]],
    adversary: dict[str, dict[str, Any]],
    selected_ids: Iterable[str],
    candidate_rows: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    common_ids = sorted(set(reviewer_a) & set(reviewer_b) & set(candidate_rows))
    statuses_a = [reviewer_a[bp_id]["reference_status"] for bp_id in common_ids]
    statuses_b = [reviewer_b[bp_id]["reference_status"] for bp_id in common_ids]
    severity_ids = [
        bp_id for bp_id in common_ids
        if reviewer_a[bp_id]["reference_severity"] is not None
        and reviewer_b[bp_id]["reference_severity"] is not None
    ]
    severities_a = [reviewer_a[bp_id]["reference_severity"] for bp_id in severity_ids]
    severities_b = [reviewer_b[bp_id]["reference_severity"] for bp_id in severity_ids]

    recommendation_scores = [
        score
        for bp_id in common_ids
        for score in (
            reviewer_a[bp_id]["recommendation_score"],
            reviewer_b[bp_id]["recommendation_score"],
        )
        if score is not None
    ]

    selected = set(selected_ids)
    final_rows: dict[str, dict[str, Any]] = {}
    unresolved_ids: list[str] = []
    for bp_id in common_ids:
        if bp_id in selected:
            adjudication = adversary.get(bp_id)
            if adjudication is None:
                unresolved_ids.append(bp_id)
                continue
            final_rows[bp_id] = {
                "status": adjudication["final_status"],
                "severity": adjudication["final_severity"],
                "evidence_kind": adjudication["evidence_kind"],
                "evidence_quote": adjudication["evidence_quote"],
            }
        elif (
            reviewer_a[bp_id]["reference_status"] == reviewer_b[bp_id]["reference_status"]
            and reviewer_a[bp_id]["reference_severity"]
            == reviewer_b[bp_id]["reference_severity"]
            and reviewer_a[bp_id]["evidence_kind"]
            == reviewer_b[bp_id]["evidence_kind"]
            and reviewer_a[bp_id]["evidence_quote"]
            == reviewer_b[bp_id]["evidence_quote"]
        ):
            final_rows[bp_id] = {
                "status": reviewer_a[bp_id]["reference_status"],
                "severity": reviewer_a[bp_id]["reference_severity"],
                "evidence_kind": reviewer_a[bp_id]["evidence_kind"],
                "evidence_quote": reviewer_a[bp_id]["evidence_quote"],
            }
        else:
            unresolved_ids.append(bp_id)

    finalized_ids = set(final_rows)
    evidence_assessed_ids = {
        bp_id
        for bp_id, row in final_rows.items()
        if row["status"] != "Not Applicable"
    }
    final_determinate_ids = {
        bp_id
        for bp_id, row in final_rows.items()
        if row["status"] in DETERMINATE_STATUSES
    }
    legitimate_unknown_ids = {
        bp_id
        for bp_id, row in final_rows.items()
        if (
            row["status"] == "Cannot Determine"
            and row["evidence_kind"] in {"omitted", "inconclusive"}
        )
    }

    candidate_status_correct_ids = {
        bp_id
        for bp_id, row in final_rows.items()
        if candidate_rows[bp_id]["candidate_status"] == row["status"]
    }
    candidate_uncertainty_ids = {
        bp_id
        for bp_id in finalized_ids
        if candidate_rows[bp_id]["candidate_status"] == "Cannot Determine"
    }
    uncertainty_ids = {
        bp_id
        for bp_id, row in final_rows.items()
        if row["status"] == "Cannot Determine"
    }
    uncertainty_aligned_ids = uncertainty_ids & candidate_uncertainty_ids
    overconservative_ids = {
        bp_id
        for bp_id in candidate_uncertainty_ids
        if final_rows[bp_id]["status"] in DETERMINATE_STATUSES
    }
    determinate_assertion_ids = {
        bp_id
        for bp_id in finalized_ids
        if candidate_rows[bp_id]["candidate_status"] in DETERMINATE_STATUSES
    }
    aligned_determinate_ids = {
        bp_id
        for bp_id in determinate_assertion_ids
        if candidate_rows[bp_id]["candidate_status"] == final_rows[bp_id]["status"]
    }
    unsupported_determinate_ids = determinate_assertion_ids & uncertainty_ids
    negative_assertion_ids = {
        bp_id
        for bp_id in finalized_ids
        if candidate_rows[bp_id]["candidate_status"] == "Not Implemented"
    }
    aligned_negative_ids = {
        bp_id
        for bp_id in negative_assertion_ids
        if final_rows[bp_id]["status"] == "Not Implemented"
    }
    unsupported_negative_ids = negative_assertion_ids & uncertainty_ids

    high_risk_ids = [
        bp_id
        for bp_id in finalized_ids
        if candidate_rows[bp_id]["candidate_severity"] in {"Critical", "High"}
    ]
    defensible_high_risk = sum(
        candidate_rows[bp_id]["candidate_status"] == final_rows[bp_id]["status"]
        and final_rows[bp_id]["severity"] in {"Critical", "High"}
        for bp_id in high_risk_ids
    )

    adjudicated = [adversary[bp_id] for bp_id in selected if bp_id in adversary]
    candidate_overturns = sum(
        row["disposition"] == "accept_challenge" for row in adjudicated
    )
    consensus_overturns = 0
    consensus_items = 0
    for bp_id in selected:
        if bp_id not in adversary:
            continue
        a = reviewer_a[bp_id]
        b = reviewer_b[bp_id]
        agreed = (
            a["reference_status"] == b["reference_status"]
            and a["reference_severity"] == b["reference_severity"]
            and a["evidence_kind"] == b["evidence_kind"]
            and a["evidence_quote"] == b["evidence_quote"]
        )
        if agreed:
            consensus_items += 1
            if adversary[bp_id]["reviewer_assessment"] == "both_weak":
                consensus_overturns += 1

    adjudication_abstentions = sum(
        row["disposition"] == "insufficient_evidence"
        for row in adjudicated
    )

    def ratio(numerator: int, denominator: int) -> float | None:
        return round(numerator / denominator, 4) if denominator else None

    return {
        "bps_reviewed": len(common_ids),
        "status_exact_agreement": agreement_rate(statuses_a, statuses_b),
        "status_kappa": cohen_kappa(statuses_a, statuses_b),
        "severity_pairs": len(severity_ids),
        "severity_exact_agreement": agreement_rate(severities_a, severities_b),
        "severity_within_one_agreement": severity_within_one(severities_a, severities_b),
        "severity_weighted_kappa": cohen_kappa(
            severities_a,
            severities_b,
            list(SEVERITIES),
        ),
        "evidence_availability_rate": ratio(
            len(final_determinate_ids),
            len(evidence_assessed_ids),
        ),
        "determinate_evidence_count": len(final_determinate_ids),
        "evidence_assessed_count": len(evidence_assessed_ids),
        "legitimate_unknown_count": len(legitimate_unknown_ids),
        "legitimate_unknown_ids": sorted(legitimate_unknown_ids),
        "critical_high_precision": ratio(
            defensible_high_risk,
            len(high_risk_ids),
        ),
        "defensible_high_risk_count": defensible_high_risk,
        "high_risk_count": len(high_risk_ids),
        "candidate_status_accuracy": ratio(
            len(candidate_status_correct_ids),
            len(finalized_ids),
        ),
        "candidate_status_correct_count": len(candidate_status_correct_ids),
        "candidate_status_assessed_count": len(finalized_ids),
        "uncertainty_recall": ratio(
            len(uncertainty_aligned_ids),
            len(uncertainty_ids),
        ),
        "uncertainty_handling_rate": ratio(
            len(uncertainty_aligned_ids),
            len(uncertainty_ids),
        ),
        "uncertainty_aligned_count": len(uncertainty_aligned_ids),
        "uncertainty_items": len(uncertainty_ids),
        "uncertainty_ids": sorted(uncertainty_ids),
        "uncertainty_aligned_ids": sorted(uncertainty_aligned_ids),
        "candidate_uncertainty_count": len(candidate_uncertainty_ids),
        "overconservative_count": len(overconservative_ids),
        "overconservative_ids": sorted(overconservative_ids),
        "overconservative_rate": ratio(
            len(overconservative_ids),
            len(candidate_uncertainty_ids),
        ),
        "determinate_assertion_count": len(determinate_assertion_ids),
        "aligned_determinate_assertion_count": len(aligned_determinate_ids),
        "determinate_status_precision": ratio(
            len(aligned_determinate_ids),
            len(determinate_assertion_ids),
        ),
        "unsupported_determinate_assertion_count": len(
            unsupported_determinate_ids
        ),
        "unsupported_determinate_assertion_ids": sorted(
            unsupported_determinate_ids
        ),
        "unsupported_determinate_assertion_rate": ratio(
            len(unsupported_determinate_ids),
            len(determinate_assertion_ids),
        ),
        "negative_assertion_count": len(negative_assertion_ids),
        "aligned_negative_assertion_count": len(aligned_negative_ids),
        "negative_assertion_precision": ratio(
            len(aligned_negative_ids),
            len(negative_assertion_ids),
        ),
        "unsupported_negative_assertion_count": len(unsupported_negative_ids),
        "unsupported_negative_assertion_ids": sorted(unsupported_negative_ids),
        "unsupported_negative_assertion_rate": ratio(
            len(unsupported_negative_ids),
            len(negative_assertion_ids),
        ),
        "recommendation_quality_mean": round(statistics.mean(recommendation_scores), 4)
        if recommendation_scores else None,
        "recommendation_score_count": len(recommendation_scores),
        "recommendation_score_total": round(sum(recommendation_scores), 4),
        "adversarial_items": len(selected),
        "adjudicated_count": len(adjudicated),
        "candidate_overturn_count": candidate_overturns,
        "candidate_overturn_rate": ratio(candidate_overturns, len(adjudicated)),
        "reviewer_consensus_items": consensus_items,
        "reviewer_consensus_overturn_count": consensus_overturns,
        "reviewer_consensus_overturn_rate": ratio(
            consensus_overturns,
            consensus_items,
        ),
        "adjudication_abstention_count": adjudication_abstentions,
        "adjudication_abstention_rate": ratio(
            adjudication_abstentions,
            len(adjudicated),
        ),
        "unresolved_count": len(unresolved_ids),
        "unresolved_ids": sorted(unresolved_ids),
        "unresolved_rate": ratio(len(unresolved_ids), len(common_ids)),
    }


def _call_metadata(result: dict[str, Any], pricing: dict[str, Any]) -> dict[str, Any]:
    return {
        "model_id": result.get("model_id"),
        "input_tokens": result.get("input_tokens"),
        "output_tokens": result.get("output_tokens"),
        "latency_s": result.get("latency_s"),
        "cost_usd": compute_cost(result, pricing) if "error" not in result else None,
        "stop_reason": result.get("stop_reason"),
        "requested_max_tokens": result.get("requested_max_tokens"),
        "effective_max_tokens": result.get("effective_max_tokens"),
        "error": result.get("error"),
    }


def _run_review_chunk(
    client,
    model_id: str,
    prompt_builder: Callable[[list[str]], str],
    expected_ids: Sequence[str],
    normalizer,
    region: str,
    max_tokens: int,
    retries: int,
) -> dict[str, Any]:
    """Review one chunk, retaining valid rows and retrying unresolved IDs."""
    accepted: dict[str, dict[str, Any]] = {}
    pending = list(expected_ids)
    attempts: list[dict[str, Any]] = []
    retry_feedback: list[str] = []

    for _ in range(retries + 1):
        attempt_ids = list(pending)
        prompt = prompt_builder(attempt_ids)
        if retry_feedback:
            prompt += (
                "\n\n===== PREVIOUS RESPONSE VALIDATION ERRORS =====\n"
                + "\n".join(f"- {item}" for item in retry_feedback[:20])
                + "\nReturn corrected rows only for the requested BP IDs."
            )
        try:
            result = _invoke_model(
                client,
                model_id,
                prompt,
                region,
                max_tokens,
            )
        except Exception as exc:
            result = {"model_id": model_id, "error": str(exc)}

        attempt: dict[str, Any] = {
            "expected_ids": attempt_ids,
            "result": result,
        }
        if "error" not in result:
            assessment = parse_model_rows(
                result.get("output", ""),
                attempt_ids,
                normalizer,
            )
            attempt["assessment"] = assessment
            duplicate_ids = set(assessment["duplicate_ids"])
            for bp_id, row in assessment["rows"].items():
                if bp_id not in duplicate_ids:
                    accepted[bp_id] = row
            retry_feedback = [
                *assessment["invalid_rows"],
                *(
                    f"missing row: {bp_id}"
                    for bp_id in assessment["missing_ids"]
                ),
                *(
                    f"duplicate row: {bp_id}"
                    for bp_id in assessment["duplicate_ids"]
                ),
                *(
                    f"unexpected row: {bp_id}"
                    for bp_id in assessment["unexpected_ids"]
                ),
            ]
        else:
            retry_feedback = [f"model call failed: {result.get('error')}"]
        attempts.append(attempt)
        pending = [bp_id for bp_id in expected_ids if bp_id not in accepted]
        if not pending:
            break

    return {
        "expected_ids": list(expected_ids),
        "attempts": attempts,
        "assessment": {
            "complete": bool(expected_ids) and not pending,
            "rows": {
                bp_id: accepted[bp_id]
                for bp_id in expected_ids
                if bp_id in accepted
            },
            "missing_ids": pending,
            "unexpected_ids": [],
            "duplicate_ids": [],
            "invalid_rows": [],
            "recovered_issue_count": sum(
                bool(attempt.get("result", {}).get("error"))
                or not attempt.get("assessment", {}).get("complete", False)
                for attempt in attempts[:-1]
            ),
        },
    }


def merge_chunk_assessments(
    expected_ids: Sequence[str],
    assessments: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    """Merge disjoint chunk ledgers and enforce full-pillar completeness."""
    expected = set(expected_ids)
    rows: dict[str, dict[str, Any]] = {}
    duplicates: set[str] = set()
    invalid: list[str] = []
    unexpected: set[str] = set()
    recovered_issue_count = 0

    for assessment in assessments:
        invalid.extend(assessment.get("invalid_rows", []))
        unexpected.update(assessment.get("unexpected_ids", []))
        recovered_issue_count += int(assessment.get("recovered_issue_count", 0))
        for bp_id, row in assessment.get("rows", {}).items():
            if bp_id in rows:
                duplicates.add(bp_id)
            rows[bp_id] = row

    actual = set(rows)
    missing = sorted(expected - actual)
    unexpected.update(actual - expected)
    complete = (
        bool(expected)
        and not missing
        and not unexpected
        and not duplicates
        and not invalid
    )
    return {
        "complete": complete,
        "rows": {bp_id: rows[bp_id] for bp_id in sorted(expected & actual)},
        "missing_ids": missing,
        "unexpected_ids": sorted(unexpected),
        "duplicate_ids": sorted(duplicates),
        "invalid_rows": invalid,
        "recovered_issue_count": recovered_issue_count,
    }


def _summarize_calls(calls: Sequence[dict[str, Any]]) -> dict[str, Any]:
    def total(field: str, *, rounded: bool = False) -> int | float | None:
        values = [
            call[field]
            for call in calls
            if isinstance(call.get(field), (int, float))
        ]
        if not values:
            return None
        value = sum(values)
        return round(value, 6) if rounded else value

    errors = [call["error"] for call in calls if call.get("error")]
    return {
        "model_id": calls[0].get("model_id") if calls else None,
        "attempts": len(calls),
        "successful_calls": len(calls) - len(errors),
        "input_tokens": total("input_tokens"),
        "output_tokens": total("output_tokens"),
        "latency_s": total("latency_s", rounded=True),
        "cost_usd": total("cost_usd", rounded=True),
        "stop_reasons": [
            call["stop_reason"] for call in calls if call.get("stop_reason")
        ],
        "errors": errors,
    }


def _materialize_chunk_result(
    candidate_id: str,
    pillar_slug: str,
    role: str,
    model_id: str,
    chunk_index: int,
    result: dict[str, Any],
    pricing: dict[str, Any],
    artifacts_dir: Path | None = None,
) -> dict[str, Any]:
    attempts: list[dict[str, Any]] = []
    calls: list[dict[str, Any]] = []
    for attempt_index, attempt in enumerate(result["attempts"], start=1):
        raw_result = attempt["result"]
        call = _call_metadata(raw_result, pricing)
        calls.append(call)
        attempt_record: dict[str, Any] = {
            "attempt": attempt_index,
            "expected_ids": attempt["expected_ids"],
            "call": call,
        }
        if "error" not in raw_result:
            attempt_record["artifact"] = _write_raw_artifact(
                candidate_id,
                pillar_slug,
                f"{role}-chunk-{chunk_index:03d}-attempt-{attempt_index:02d}",
                model_id,
                raw_result.get("output", ""),
                artifacts_dir,
            )
            attempt_record["assessment"] = attempt["assessment"]
        attempts.append(attempt_record)
    return {
        "chunk_index": chunk_index,
        "expected_ids": result.get(
            "expected_ids",
            [
                bp_id for bp_id in result["assessment"]["rows"]
            ] + result["assessment"]["missing_ids"],
        ),
        "calls": calls,
        "attempts": attempts,
        "assessment": result["assessment"],
    }


def _finalize_review_record(
    chunks: Sequence[dict[str, Any]],
    expected_ids: Sequence[str],
) -> dict[str, Any]:
    ordered_chunks = sorted(chunks, key=lambda chunk: chunk["chunk_index"])
    calls = [
        call
        for chunk in ordered_chunks
        for call in chunk.get("calls", [])
    ]
    return {
        "call": _summarize_calls(calls),
        "calls": calls,
        "chunks": ordered_chunks,
        "assessment": merge_chunk_assessments(
            expected_ids,
            (chunk["assessment"] for chunk in ordered_chunks),
        ),
    }


def _record_calls(record: dict[str, Any]) -> list[dict[str, Any]]:
    calls = record.get("calls")
    if isinstance(calls, list):
        return calls
    call = record.get("call")
    return [call] if isinstance(call, dict) else []


def summarize_resource_usage(
    pillars: dict[str, dict[str, Any]],
    wall_s: float,
) -> dict[str, Any]:
    by_role = {
        "blind": {
            "calls": 0,
            "failed_calls": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "cost_usd": 0.0,
        },
        "adversarial": {
            "calls": 0,
            "failed_calls": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "cost_usd": 0.0,
        },
    }
    for pillar in pillars.values():
        for reviewer in pillar.get("reviewers", {}).values():
            for call in _record_calls(reviewer):
                by_role["blind"]["calls"] += 1
                by_role["blind"]["failed_calls"] += int(bool(call.get("error")))
                by_role["blind"]["input_tokens"] += int(call.get("input_tokens") or 0)
                by_role["blind"]["output_tokens"] += int(call.get("output_tokens") or 0)
                by_role["blind"]["cost_usd"] += float(call.get("cost_usd") or 0)
        for call in _record_calls(pillar.get("adversary", {})):
            by_role["adversarial"]["calls"] += 1
            by_role["adversarial"]["failed_calls"] += int(bool(call.get("error")))
            by_role["adversarial"]["input_tokens"] += int(call.get("input_tokens") or 0)
            by_role["adversarial"]["output_tokens"] += int(call.get("output_tokens") or 0)
            by_role["adversarial"]["cost_usd"] += float(call.get("cost_usd") or 0)
    for values in by_role.values():
        values["cost_usd"] = round(values["cost_usd"], 6)
    return {
        **by_role,
        "total": {
            "calls": sum(values["calls"] for values in by_role.values()),
            "failed_calls": sum(values["failed_calls"] for values in by_role.values()),
            "input_tokens": sum(values["input_tokens"] for values in by_role.values()),
            "output_tokens": sum(values["output_tokens"] for values in by_role.values()),
            "cost_usd": round(sum(values["cost_usd"] for values in by_role.values()), 6),
            "wall_s": round(wall_s, 2),
        },
    }


def aggregate_resource_usage(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    totals = {
        "calls": 0,
        "failed_calls": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "cost_usd": 0.0,
        "wall_s": 0.0,
    }
    for candidate in candidates:
        usage = candidate.get("resource_usage", {}).get("total", {})
        for field in ("calls", "failed_calls", "input_tokens", "output_tokens"):
            totals[field] += int(usage.get(field) or 0)
        for field in ("cost_usd", "wall_s"):
            totals[field] += float(usage.get(field) or 0)
    totals["cost_usd"] = round(totals["cost_usd"], 6)
    totals["wall_s"] = round(totals["wall_s"], 2)
    return totals


def run_quality_review(
    candidates: list[Candidate],
    reviewers: tuple[str, str],
    adversary_model: str,
    region: str,
    max_tokens: int,
    concurrency: int,
    seed: int,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    retries: int = DEFAULT_RETRIES,
    resume: dict[str, Any] | None = None,
    artifacts_dir: Path | None = None,
) -> dict[str, Any]:
    artifact_root = (artifacts_dir or ARTIFACTS_DIR).expanduser().resolve()
    if resume:
        if resume.get("schema_version") != SCHEMA_VERSION:
            raise ValueError(
                "resume schema mismatch: "
                f"{resume.get('schema_version')} != {SCHEMA_VERSION}"
            )
        resume_config = resume.get("config", {})
        expected_config = {
            "reviewers": list(reviewers),
            "adversary": adversary_model,
            "region": region,
            "seed": seed,
            "artifacts_dir": str(artifact_root),
            "evidence_mode": "verbal_exact_quote",
        }
        mismatches = [
            key
            for key, value in expected_config.items()
            if resume_config.get(key) != value
        ]
        if mismatches:
            raise ValueError(
                "resume configuration mismatch: " + ", ".join(mismatches)
            )
    client = boto3.client(
        "bedrock-runtime",
        region_name=region,
        config=BotoConfig(read_timeout=600),
    )
    pricing = load_benchmark_config().get("pricing", {})
    previous_candidates = {
        candidate["candidate_id"]: candidate
        for candidate in (resume or {}).get("candidates", [])
        if isinstance(candidate, dict) and candidate.get("candidate_id")
    }
    output: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "reviewers": list(reviewers),
            "adversary": adversary_model,
            "region": region,
            "max_tokens": max_tokens,
            "chunk_size": chunk_size,
            "retries": retries,
            "resumed": bool(resume),
            "seed": seed,
            "artifacts_dir": str(artifact_root),
            "evidence_mode": "verbal_exact_quote",
        },
        "candidates": [],
    }

    for candidate in candidates:
        candidate_started = time.time()
        candidate_rows = parse_candidate_ledger(candidate.report)
        previous_candidate = previous_candidates.get(candidate.candidate_id, {})
        previous_source = previous_candidate.get("source", {})
        if previous_source and (
            int(previous_source.get("case_id", -1)) != candidate.case_id
            or int(previous_source.get("run_idx", -1)) != candidate.run_idx
        ):
            raise ValueError(
                f"resume candidate mismatch for {candidate.candidate_id}"
            )
        previous_pillars = previous_candidate.get("pillars", {})
        previous_wall_s = float(
            previous_candidate.get("resource_usage", {})
            .get("total", {})
            .get("wall_s", 0)
            or 0
        )
        prefixes = scoped_prefixes(candidate.case_id)
        candidate_result: dict[str, Any] = {
            "candidate_id": candidate.candidate_id,
            "source": {
                "case_id": candidate.case_id,
                "run_idx": candidate.run_idx,
                "model": candidate.source_model,
                "mode": candidate.source_mode,
            },
            "citation_metrics": candidate.citation_metrics,
            "generation_usage": candidate.generation_usage,
            "candidate_ledger": {
                "parsed_bp_count": len(candidate_rows),
                "status_distribution": {
                    status: sum(
                        row["candidate_status"] == status
                        for row in candidate_rows.values()
                    )
                    for status in STATUSES
                    if status != "Missing"
                },
            },
            "pillars": {},
        }
        pillar_expected: dict[str, list[str]] = {}
        blind_jobs: dict[Any, tuple[str, str, str, str, int, list[str]]] = {}
        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            for slug, pillar_name, prefix in PILLARS:
                if prefix not in prefixes:
                    continue
                reference = (REFERENCES_DIR / f"{slug}.md").read_text()
                expected_ids = canonical_ids(reference, prefix)
                missing_candidate_ids = set(expected_ids) - set(candidate_rows)
                if missing_candidate_ids:
                    raise ValueError(
                        "candidate ledger is missing expected BP rows: "
                        + ", ".join(sorted(missing_candidate_ids))
                    )
                pillar_expected[prefix] = expected_ids
                previous_pillar = previous_pillars.get(prefix, {})
                candidate_result["pillars"][prefix] = {
                    "slug": slug,
                    "name": pillar_name,
                    "expected_bp_count": len(expected_ids),
                    "reviewers": {},
                }
                for label, model_id in zip(("A", "B"), reviewers):
                    previous_review = copy.deepcopy(
                        previous_pillar.get("reviewers", {}).get(label, {})
                    )
                    previous_model = previous_review.get("call", {}).get("model_id")
                    if previous_model and previous_model != model_id:
                        raise ValueError(
                            f"resume reviewer mismatch for {prefix}/{label}: "
                            f"{previous_model} != {model_id}"
                        )
                    review_record = (
                        previous_review
                        if isinstance(previous_review.get("chunks"), list)
                        else {"chunks": []}
                    )
                    candidate_result["pillars"][prefix]["reviewers"][label] = (
                        review_record
                    )
                    existing_rows = set(
                        review_record.get("assessment", {}).get("rows", {})
                    )
                    unresolved_ids = [
                        bp_id for bp_id in expected_ids if bp_id not in existing_rows
                    ]
                    first_chunk_index = 1 + max(
                        (
                            int(chunk.get("chunk_index", 0))
                            for chunk in review_record["chunks"]
                        ),
                        default=0,
                    )
                    for offset, bp_ids in enumerate(
                        chunk_values(unresolved_ids, chunk_size),
                    ):
                        chunk_index = first_chunk_index + offset
                        def prompt_builder(
                            selected: list[str],
                            *,
                            workload=candidate.workload,
                            report=candidate.report,
                            selected_prefix=prefix,
                            full_reference=reference,
                            selected_pillar_name=pillar_name,
                        ) -> str:
                            return build_blind_prompt(
                                workload,
                                extract_pillar_excerpt(
                                    report,
                                    selected_prefix,
                                    selected,
                                ),
                                extract_reference_subset(full_reference, selected),
                                selected_pillar_name,
                                len(selected),
                                selected,
                            )

                        def reviewer_normalizer(
                            row: dict[str, Any],
                            *,
                            workload=candidate.workload,
                            parsed_candidate_rows=candidate_rows,
                        ) -> dict[str, Any]:
                            return normalize_reviewer_row(
                                row,
                                workload=workload,
                                candidate_rows=parsed_candidate_rows,
                            )

                        future = pool.submit(
                            _run_review_chunk,
                            client,
                            model_id,
                            prompt_builder,
                            bp_ids,
                            reviewer_normalizer,
                            region,
                            max_tokens,
                            retries,
                        )
                        blind_jobs[future] = (
                            prefix,
                            slug,
                            label,
                            model_id,
                            chunk_index,
                            bp_ids,
                        )

            for future in as_completed(blind_jobs):
                prefix, slug, label, model_id, chunk_index, bp_ids = blind_jobs[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "attempts": [{
                            "expected_ids": bp_ids,
                            "result": {"model_id": model_id, "error": str(exc)},
                        }],
                        "assessment": {
                            "complete": False,
                            "rows": {},
                            "missing_ids": bp_ids,
                            "unexpected_ids": [],
                            "duplicate_ids": [],
                            "invalid_rows": [],
                            "recovered_issue_count": 0,
                        },
                    }
                chunk_record = _materialize_chunk_result(
                    candidate.candidate_id,
                    slug,
                    f"reviewer-{label.lower()}",
                    model_id,
                    chunk_index,
                    result,
                    pricing,
                    artifact_root,
                )
                candidate_result["pillars"][prefix]["reviewers"][label][
                    "chunks"
                ].append(chunk_record)

        for prefix, pillar_result in candidate_result["pillars"].items():
            expected_ids = pillar_expected[prefix]
            for label in ("A", "B"):
                chunks = pillar_result["reviewers"][label]["chunks"]
                pillar_result["reviewers"][label] = _finalize_review_record(
                    chunks,
                    expected_ids,
                )

        adversary_jobs: dict[
            Any,
            tuple[str, str, int, list[str]],
        ] = {}
        adversary_context: dict[
            str,
            tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], list[str]],
        ] = {}
        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            for slug, pillar_name, prefix in PILLARS:
                if prefix not in prefixes:
                    continue
                pillar_result = candidate_result["pillars"][prefix]
                review_a = pillar_result["reviewers"].get("A", {}).get("assessment", {})
                review_b = pillar_result["reviewers"].get("B", {}).get("assessment", {})
                if not review_a.get("complete") or not review_b.get("complete"):
                    pillar_result["status"] = "incomplete_blind_review"
                    continue

                rows_a = review_a["rows"]
                rows_b = review_b["rows"]
                selected = select_adversarial_ids(
                    rows_a,
                    rows_b,
                    seed=seed + candidate.case_id + sum(ord(char) for char in prefix),
                )
                pillar_result["adversarial_selection"] = selected
                adversary_context[prefix] = (rows_a, rows_b, selected)
                if not selected:
                    pillar_result["status"] = "complete"
                    pillar_result["metrics"] = compute_quality_metrics(
                        rows_a,
                        rows_b,
                        {},
                        [],
                        candidate_rows,
                    )
                    continue

                reference = (REFERENCES_DIR / f"{slug}.md").read_text()
                previous_adversary = copy.deepcopy(
                    previous_pillars.get(prefix, {}).get("adversary", {})
                )
                previous_model = previous_adversary.get("call", {}).get("model_id")
                if previous_model and previous_model != adversary_model:
                    raise ValueError(
                        f"resume adversary mismatch for {prefix}: "
                        f"{previous_model} != {adversary_model}"
                    )
                adversary_record = (
                    previous_adversary
                    if isinstance(previous_adversary.get("chunks"), list)
                    else {"chunks": []}
                )
                pillar_result["adversary"] = adversary_record
                existing_rows = set(
                    adversary_record.get("assessment", {}).get("rows", {})
                )
                unresolved_ids = [
                    bp_id for bp_id in selected if bp_id not in existing_rows
                ]
                first_chunk_index = 1 + max(
                    (
                        int(chunk.get("chunk_index", 0))
                        for chunk in adversary_record["chunks"]
                    ),
                    default=0,
                )
                for offset, bp_ids in enumerate(
                    chunk_values(unresolved_ids, chunk_size),
                ):
                    chunk_index = first_chunk_index + offset
                    def prompt_builder(
                        unresolved: list[str],
                        *,
                        workload=candidate.workload,
                        report=candidate.report,
                        selected_prefix=prefix,
                        full_reference=reference,
                        selected_rows_a=rows_a,
                        selected_rows_b=rows_b,
                        selected_pillar_name=pillar_name,
                    ) -> str:
                        return build_adversary_prompt(
                            workload,
                            extract_pillar_excerpt(
                                report,
                                selected_prefix,
                                unresolved,
                            ),
                            extract_reference_subset(full_reference, unresolved),
                            selected_rows_a,
                            selected_rows_b,
                            unresolved,
                            selected_pillar_name,
                        )

                    def adversary_normalizer(
                        row: dict[str, Any],
                        *,
                        workload=candidate.workload,
                        selected_rows_a=rows_a,
                        selected_rows_b=rows_b,
                    ) -> dict[str, Any]:
                        return normalize_adversary_row(
                            row,
                            workload=workload,
                            reviewer_a=selected_rows_a,
                            reviewer_b=selected_rows_b,
                        )

                    future = pool.submit(
                        _run_review_chunk,
                        client,
                        adversary_model,
                        prompt_builder,
                        bp_ids,
                        adversary_normalizer,
                        region,
                        max_tokens,
                        retries,
                    )
                    adversary_jobs[future] = (
                        prefix,
                        slug,
                        chunk_index,
                        bp_ids,
                    )

            for future in as_completed(adversary_jobs):
                prefix, slug, chunk_index, bp_ids = adversary_jobs[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "attempts": [{
                            "expected_ids": bp_ids,
                            "result": {
                                "model_id": adversary_model,
                                "error": str(exc),
                            },
                        }],
                        "assessment": {
                            "complete": False,
                            "rows": {},
                            "missing_ids": bp_ids,
                            "unexpected_ids": [],
                            "duplicate_ids": [],
                            "invalid_rows": [],
                            "recovered_issue_count": 0,
                        },
                    }
                chunk_record = _materialize_chunk_result(
                    candidate.candidate_id,
                    slug,
                    "adversary",
                    adversary_model,
                    chunk_index,
                    result,
                    pricing,
                    artifact_root,
                )
                candidate_result["pillars"][prefix]["adversary"]["chunks"].append(
                    chunk_record
                )

        for prefix, (rows_a, rows_b, selected) in adversary_context.items():
            if not selected:
                continue
            pillar_result = candidate_result["pillars"][prefix]
            adversary_record = _finalize_review_record(
                pillar_result["adversary"]["chunks"],
                selected,
            )
            pillar_result["adversary"] = adversary_record
            assessment = adversary_record["assessment"]
            pillar_result["status"] = (
                "complete"
                if assessment.get("complete")
                else "incomplete_adversarial_review"
            )
            pillar_result["metrics"] = compute_quality_metrics(
                rows_a,
                rows_b,
                assessment.get("rows", {}),
                selected,
                candidate_rows,
            )

        complete_metrics = [
            pillar["metrics"]
            for pillar in candidate_result["pillars"].values()
            if pillar.get("status") == "complete" and "metrics" in pillar
        ]
        candidate_result["status"] = (
            "complete"
            if len(complete_metrics) == len(candidate_result["pillars"])
            else "incomplete"
        )
        candidate_result["summary"] = summarize_metrics(complete_metrics)
        candidate_result["resource_usage"] = summarize_resource_usage(
            candidate_result["pillars"],
            previous_wall_s + time.time() - candidate_started,
        )
        output["candidates"].append(candidate_result)

    output["summary"] = summarize_metrics([
        candidate["summary"]
        for candidate in output["candidates"]
        if candidate["status"] == "complete"
    ])
    output["resource_usage"] = aggregate_resource_usage(output["candidates"])
    return output


def summarize_metrics(metrics: list[dict[str, Any]]) -> dict[str, Any]:
    if not metrics:
        return {"completed_units": 0}
    macro_rate_fields = (
        "status_exact_agreement",
        "status_kappa",
        "severity_exact_agreement",
        "severity_within_one_agreement",
        "severity_weighted_kappa",
    )
    summary: dict[str, Any] = {"completed_units": len(metrics)}
    for field in macro_rate_fields:
        values = [
            metric[field]
            for metric in metrics
            if isinstance(metric.get(field), (int, float))
        ]
        summary[field] = round(statistics.mean(values), 4) if values else None
    count_fields = (
        "bps_reviewed",
        "severity_pairs",
        "determinate_evidence_count",
        "evidence_assessed_count",
        "legitimate_unknown_count",
        "defensible_high_risk_count",
        "high_risk_count",
        "candidate_status_correct_count",
        "candidate_status_assessed_count",
        "adversarial_items",
        "uncertainty_aligned_count",
        "uncertainty_items",
        "candidate_uncertainty_count",
        "overconservative_count",
        "determinate_assertion_count",
        "aligned_determinate_assertion_count",
        "unsupported_determinate_assertion_count",
        "negative_assertion_count",
        "aligned_negative_assertion_count",
        "unsupported_negative_assertion_count",
        "recommendation_score_count",
        "adjudicated_count",
        "candidate_overturn_count",
        "reviewer_consensus_items",
        "reviewer_consensus_overturn_count",
        "adjudication_abstention_count",
        "unresolved_count",
    )
    for field in count_fields:
        summary[field] = sum(int(metric.get(field, 0)) for metric in metrics)
    summary["recommendation_score_total"] = round(
        sum(float(metric.get("recommendation_score_total", 0)) for metric in metrics),
        4,
    )
    ratio_fields = (
        (
            "evidence_availability_rate",
            "determinate_evidence_count",
            "evidence_assessed_count",
        ),
        (
            "critical_high_precision",
            "defensible_high_risk_count",
            "high_risk_count",
        ),
        (
            "candidate_status_accuracy",
            "candidate_status_correct_count",
            "candidate_status_assessed_count",
        ),
        (
            "uncertainty_handling_rate",
            "uncertainty_aligned_count",
            "uncertainty_items",
        ),
        (
            "uncertainty_recall",
            "uncertainty_aligned_count",
            "uncertainty_items",
        ),
        (
            "overconservative_rate",
            "overconservative_count",
            "candidate_uncertainty_count",
        ),
        (
            "determinate_status_precision",
            "aligned_determinate_assertion_count",
            "determinate_assertion_count",
        ),
        (
            "unsupported_determinate_assertion_rate",
            "unsupported_determinate_assertion_count",
            "determinate_assertion_count",
        ),
        (
            "negative_assertion_precision",
            "aligned_negative_assertion_count",
            "negative_assertion_count",
        ),
        (
            "unsupported_negative_assertion_rate",
            "unsupported_negative_assertion_count",
            "negative_assertion_count",
        ),
        (
            "candidate_overturn_rate",
            "candidate_overturn_count",
            "adjudicated_count",
        ),
        (
            "reviewer_consensus_overturn_rate",
            "reviewer_consensus_overturn_count",
            "reviewer_consensus_items",
        ),
        (
            "adjudication_abstention_rate",
            "adjudication_abstention_count",
            "adjudicated_count",
        ),
        (
            "unresolved_rate",
            "unresolved_count",
            "bps_reviewed",
        ),
    )
    for rate_field, numerator_field, denominator_field in ratio_fields:
        denominator = summary[denominator_field]
        summary[rate_field] = (
            round(summary[numerator_field] / denominator, 4)
            if denominator
            else None
        )
    recommendation_count = summary["recommendation_score_count"]
    summary["recommendation_quality_mean"] = (
        round(summary["recommendation_score_total"] / recommendation_count, 4)
        if recommendation_count
        else None
    )
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run blind and adversarial quality review over captured wa-review reports.",
    )
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--artifacts-dir",
        type=Path,
        default=ARTIFACTS_DIR,
        help="Directory for raw blind-review and adversary responses.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Reuse valid rows and call metadata from the existing output file.",
    )
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--pilot", action="store_true", help="Evaluate cases 2 and 3.")
    selection.add_argument("--cases", type=int, nargs="+", help="Evaluate selected case IDs.")
    parser.add_argument("--runs", type=int, default=1, help="Candidate runs per case.")
    parser.add_argument("--reviewers", nargs=2, default=list(DEFAULT_REVIEWERS))
    parser.add_argument("--adversary", default=DEFAULT_ADVERSARY)
    parser.add_argument("--region", default=DEFAULT_REGION)
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help="Maximum BPs per model call.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=DEFAULT_RETRIES,
        help="Retries for unresolved rows in each chunk.",
    )
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--seed", type=int, default=42)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.runs < 1:
        parser.error("--runs must be at least 1")
    if args.concurrency < 1:
        parser.error("--concurrency must be at least 1")
    if args.max_tokens < 1:
        parser.error("--max-tokens must be at least 1")
    if args.chunk_size < 1:
        parser.error("--chunk-size must be at least 1")
    if args.retries < 0:
        parser.error("--retries must be at least 0")
    selected_cases = {2, 3} if args.pilot else set(args.cases) if args.cases else None
    try:
        candidates = load_candidates(
            args.results,
            selected_cases,
            args.runs,
            args.seed,
        )
        validate_panel(
            (candidate.source_model for candidate in candidates),
            args.reviewers,
            args.adversary,
        )
        resume = (
            json.loads(args.output.read_text())
            if args.resume
            else None
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if args.resume and resume is None:
        parser.error(f"resume output does not exist: {args.output}")
    print(
        f"Quality review: {len(candidates)} candidate(s), "
        f"reviewers={', '.join(args.reviewers)}, adversary={args.adversary}"
    )
    result = run_quality_review(
        candidates,
        tuple(args.reviewers),
        args.adversary,
        args.region,
        args.max_tokens,
        args.concurrency,
        args.seed,
        args.chunk_size,
        args.retries,
        resume,
        args.artifacts_dir,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2))
    print(f"Saved: {args.output}")
    print(json.dumps(result["summary"], indent=2))
    return 0 if all(candidate["status"] == "complete" for candidate in result["candidates"]) else 2


if __name__ == "__main__":
    sys.exit(main())
