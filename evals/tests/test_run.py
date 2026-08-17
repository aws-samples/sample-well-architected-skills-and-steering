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
    assert "aws-well-architected-framework-review" in skills


def test_load_skill():
    content = load_skill("aws-well-architected-framework-review")
    assert "Well-Architected" in content
    assert len(content) > 100


def test_load_skill_not_found():
    with pytest.raises(FileNotFoundError):
        load_skill("nonexistent-skill")


def test_load_evals():
    evals = load_evals("aws-well-architected-framework-review")
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


def test_all_skills_description_under_1024_chars():
    """Skill descriptions MUST be under 1024 characters for selection accuracy."""
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        content = skill_md.read_text()
        if not content.startswith("---"):
            continue
        # Parse description from frontmatter
        lines = content.split("\n")
        desc_lines = []
        capturing = False
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if line.startswith("description:"):
                capturing = True
                value = line[len("description:"):].strip().strip('"')
                if value:
                    desc_lines.append(value)
            elif capturing:
                if line.startswith(" ") or line.startswith("\t"):
                    desc_lines.append(line.strip())
                else:
                    capturing = False
        desc = " ".join(desc_lines)
        assert len(desc) <= 1024, (
            f"{skill_dir.name}: description is {len(desc)} chars (max 1024)"
        )


def test_all_skills_have_metadata_tags():
    """Every metadata.json should have structured metadata tags."""
    required_tags = {"service", "task", "persona", "workload"}
    for skill_dir in SKILLS_DIR.iterdir():
        if not skill_dir.is_dir():
            continue
        meta_path = skill_dir / "metadata.json"
        if not meta_path.exists():
            continue
        import json
        data = json.loads(meta_path.read_text())
        assert "metadata" in data, f"{skill_dir.name}: missing 'metadata' in metadata.json"
        for tag in required_tags:
            assert tag in data["metadata"], (
                f"{skill_dir.name}: missing metadata tag '{tag}'"
            )
            assert isinstance(data["metadata"][tag], list), (
                f"{skill_dir.name}: metadata.{tag} must be a list"
            )
            assert len(data["metadata"][tag]) >= 1, (
                f"{skill_dir.name}: metadata.{tag} must have at least one value"
            )


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


@patch("boto3.client")
def test_call_bedrock_retries_without_temperature_when_unsupported(mock_client_factory):
    """Models like Opus 4.8 reject temperature; the call should drop it and retry."""
    from run import call_bedrock

    class ValidationException(Exception):
        pass

    mock_client = MagicMock()
    mock_client_factory.return_value = mock_client
    mock_client.exceptions.ValidationException = ValidationException

    # First call raises a temperature ValidationException, second succeeds.
    mock_client.converse.side_effect = [
        ValidationException("The model returned the following errors: temperature ... not supported"),
        {"output": {"message": {"content": [{"text": "ok"}]}}},
    ]

    config = {"region": "us-east-1", "generation_model": "us.anthropic.claude-opus-4-8", "temperature": 0, "max_tokens": 4096}
    messages = [{"role": "user", "content": [{"text": "hello"}]}]

    result = call_bedrock(config, messages)

    assert result == "ok"
    assert mock_client.converse.call_count == 2
    # The retry must not include temperature in inferenceConfig.
    retry_kwargs = mock_client.converse.call_args_list[1][1]
    assert "temperature" not in retry_kwargs["inferenceConfig"]


@patch("boto3.client")
def test_call_bedrock_reraises_unrelated_validation_errors(mock_client_factory):
    """A ValidationException not about temperature must propagate, not retry."""
    from run import call_bedrock

    class ValidationException(Exception):
        pass

    mock_client = MagicMock()
    mock_client_factory.return_value = mock_client
    mock_client.exceptions.ValidationException = ValidationException
    mock_client.converse.side_effect = ValidationException("malformed input: messages is empty")

    config = {"region": "us-east-1", "generation_model": "us.anthropic.claude-opus-4-8", "temperature": 0, "max_tokens": 4096}
    messages = [{"role": "user", "content": [{"text": "hello"}]}]

    with pytest.raises(ValidationException):
        call_bedrock(config, messages)
    mock_client.converse.assert_called_once()
