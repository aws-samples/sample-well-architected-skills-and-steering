# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Tests for the grading module — no Bedrock calls required."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

from grade import grade_response


def make_mock_config():
    return {"region": "us-east-1", "grading_model": "test-model"}


@patch("grade.boto3")
def test_grade_response_parses_json(mock_boto3):
    mock_client = MagicMock()
    mock_boto3.client.return_value = mock_client

    grader_response = json.dumps([
        {"assertion": "Has all pillars", "pass": True, "reason": "All 6 pillars mentioned"},
        {"assertion": "Has severity", "pass": False, "reason": "No severity labels found"},
    ])

    mock_client.converse.return_value = {
        "output": {"message": {"content": [{"text": grader_response}]}}
    }

    assertions = ["Has all pillars", "Has severity"]
    result = grade_response(make_mock_config(), "some output", assertions)

    assert len(result) == 2
    assert result[0]["pass"] is True
    assert result[1]["pass"] is False
    assert "reason" in result[0]


@patch("grade.boto3")
def test_grade_response_handles_markdown_wrapped_json(mock_boto3):
    mock_client = MagicMock()
    mock_boto3.client.return_value = mock_client

    grader_response = '```json\n[{"assertion": "test", "pass": true, "reason": "ok"}]\n```'

    mock_client.converse.return_value = {
        "output": {"message": {"content": [{"text": grader_response}]}}
    }

    result = grade_response(make_mock_config(), "some output", ["test"])

    assert len(result) == 1
    assert result[0]["pass"] is True


@patch("grade.boto3")
def test_grade_response_handles_malformed_response(mock_boto3):
    mock_client = MagicMock()
    mock_boto3.client.return_value = mock_client

    mock_client.converse.return_value = {
        "output": {"message": {"content": [{"text": "not valid json at all"}]}}
    }

    assertions = ["assertion one", "assertion two"]
    result = grade_response(make_mock_config(), "some output", assertions)

    assert len(result) == 2
    assert result[0]["pass"] is False
    assert result[1]["pass"] is False
    assert "parse" in result[0]["reason"].lower()


@patch("grade.boto3")
def test_grade_response_normalizes_missing_entries(mock_boto3):
    mock_client = MagicMock()
    mock_boto3.client.return_value = mock_client

    # Grader only returns 1 result for 3 assertions
    grader_response = json.dumps([
        {"assertion": "first", "pass": True, "reason": "found it"},
    ])

    mock_client.converse.return_value = {
        "output": {"message": {"content": [{"text": grader_response}]}}
    }

    assertions = ["first", "second", "third"]
    result = grade_response(make_mock_config(), "some output", assertions)

    assert len(result) == 3
    assert result[0]["pass"] is True
    assert result[1]["pass"] is False
    assert result[2]["pass"] is False
