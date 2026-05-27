# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Tests for the eval runner — no Bedrock calls required."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from run import list_skills, load_config, load_evals, load_skill


SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"


def test_load_config():
    config = load_config()
    assert "region" in config
    assert "generation_model" in config
    assert "grading_model" in config
    assert config["temperature"] == 0


def test_list_skills():
    skills = list_skills()
    assert len(skills) >= 1
    assert "wa-review" in skills


def test_load_skill():
    content = load_skill("wa-review")
    assert "Well-Architected" in content
    assert len(content) > 100


def test_load_skill_not_found():
    with pytest.raises(FileNotFoundError):
        load_skill("nonexistent-skill")


def test_load_evals():
    evals = load_evals("wa-review")
    assert "skill_name" in evals
    assert "evals" in evals
    assert len(evals["evals"]) >= 1

    case = evals["evals"][0]
    assert "id" in case
    assert "prompt" in case
    assert "assertions" in case
    assert len(case["assertions"]) >= 3


def test_load_evals_not_found():
    with pytest.raises(FileNotFoundError):
        load_evals("nonexistent-skill")


def test_all_skills_have_valid_evals():
    """Every skill with an evals.json should have well-formed test cases."""
    for skill_name in list_skills():
        evals = load_evals(skill_name)
        assert evals["skill_name"] == skill_name, f"{skill_name}: skill_name mismatch"
        assert len(evals["evals"]) >= 1, f"{skill_name}: no eval cases"

        for case in evals["evals"]:
            assert "id" in case, f"{skill_name}: missing id"
            assert "prompt" in case, f"{skill_name}: missing prompt"
            assert len(case["prompt"]) > 10, f"{skill_name}: prompt too short"
            assert "assertions" in case, f"{skill_name}: missing assertions"
            assert len(case["assertions"]) >= 3, f"{skill_name}: fewer than 3 assertions"


@patch("boto3.client")
def test_call_bedrock_constructs_correct_request(mock_client_factory):
    from run import call_bedrock

    mock_client = MagicMock()
    mock_client_factory.return_value = mock_client
    mock_client.converse.return_value = {
        "output": {"message": {"content": [{"text": "test response"}]}}
    }

    config = {"region": "us-east-1", "generation_model": "test-model", "temperature": 0, "max_tokens": 4096}
    messages = [{"role": "user", "content": [{"text": "hello"}]}]

    result = call_bedrock(config, messages, system="system prompt")

    assert result == "test response"
    mock_client.converse.assert_called_once()
    call_kwargs = mock_client.converse.call_args[1]
    assert call_kwargs["modelId"] == "test-model"
    assert call_kwargs["system"] == [{"text": "system prompt"}]
