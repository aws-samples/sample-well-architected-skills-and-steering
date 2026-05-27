# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Tests for the report module."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from report import print_report, save_results


def make_sample_results():
    return [
        {
            "skill_name": "wa-review",
            "cases": [
                {
                    "id": 1,
                    "prompt": "Review my architecture",
                    "baseline": {"score": 0.4},
                    "with_skill": {"score": 0.9},
                },
                {
                    "id": 2,
                    "prompt": "Review my monolith",
                    "baseline": {"score": 0.5},
                    "with_skill": {"score": 0.85},
                },
            ],
            "aggregate": {
                "baseline_avg": 0.45,
                "skill_avg": 0.875,
                "delta": 0.425,
            },
        }
    ]


def test_print_report_no_crash(capsys):
    print_report(make_sample_results())
    captured = capsys.readouterr()
    assert "wa-review" in captured.out
    assert "EVALUATION RESULTS" in captured.out


def test_print_report_multiple_skills(capsys):
    results = make_sample_results()
    results.append({
        "skill_name": "security-assessment",
        "cases": [{"id": 1, "prompt": "test", "baseline": {"score": 0.3}, "with_skill": {"score": 0.8}}],
        "aggregate": {"baseline_avg": 0.3, "skill_avg": 0.8, "delta": 0.5},
    })
    print_report(results)
    captured = capsys.readouterr()
    assert "AVERAGE" in captured.out
    assert "security-assessment" in captured.out


def test_save_results(tmp_path, monkeypatch):
    monkeypatch.setattr("report.RESULTS_DIR", tmp_path)
    results = make_sample_results()
    output_path = save_results(results)

    assert output_path.exists()
    with open(output_path) as f:
        data = json.load(f)
    assert "timestamp" in data
    assert "results" in data
    assert "summary" in data
    assert "wa-review" in data["summary"]
