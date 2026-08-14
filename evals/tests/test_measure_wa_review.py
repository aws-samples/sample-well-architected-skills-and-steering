# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Offline tests for the Claude Code aws-well-architected-framework-review effectiveness harness."""

import sys
from pathlib import Path

import pytest

CLI_DIR = Path(__file__).parent.parent / "cli_effectiveness"
sys.path.insert(0, str(CLI_DIR))

import measure_wa_review as measure


def test_autonomous_preamble_requires_uncertainty_calibration():
    assert "Cannot\nDetermine" in measure.AUTONOMOUS_PREAMBLE
    assert "leave severity blank" in measure.AUTONOMOUS_PREAMBLE
    assert "specific artifact, metric" in measure.AUTONOMOUS_PREAMBLE
    assert "explicitly says a control is absent" in measure.AUTONOMOUS_PREAMBLE
    assert "Based on description" not in measure.AUTONOMOUS_PREAMBLE


def test_parser_supports_single_case_run_and_isolated_output(tmp_path):
    output = tmp_path / "candidate_results.json"

    args = measure.build_parser().parse_args([
        "--cases", "2",
        "--runs", "1",
        "--model", "opus",
        "--output", str(output),
    ])

    assert args.cases == [2]
    assert args.runs == 1
    assert args.model == "opus"
    assert args.output == output


def test_main_rejects_unknown_case_without_calling_claude(tmp_path):
    with pytest.raises(SystemExit):
        measure.main([
            "--cases", "999",
            "--runs", "1",
            "--output", str(tmp_path / "unused.json"),
        ])
