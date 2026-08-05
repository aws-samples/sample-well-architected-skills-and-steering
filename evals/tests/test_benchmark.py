# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Tests for the benchmark transport and model configuration."""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmark import (  # noqa: E402
    _openai_provider_for_model,
    call_openai_compatible_model,
    compute_cost,
    load_config,
    run_benchmark,
)


def _response():
    return {
        "choices": [{
            "message": {"content": "test response"},
            "finish_reason": "stop",
        }],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 4,
            "total_tokens": 14,
            "prompt_tokens_details": {"cached_tokens": 2},
        },
    }


def test_minimax_config_contains_current_models_and_metadata():
    config = load_config()
    provider = config["openai_compatible_providers"]["MiniMax"]

    assert config["models"][-2:] == ["MiniMax-M3", "MiniMax-M2.7"]
    assert provider["endpoint_region"] == "global_en"
    assert provider["endpoints"] == {
        "global_en": "https://api.minimax.io/v1",
        "cn_zh": "https://api.minimaxi.com/v1",
    }
    assert provider["models"]["MiniMax-M3"] == {
        "context_window": 1000000,
        "input_modalities": ["text", "image", "video"],
        "thinking": ["adaptive", "disabled"],
    }
    assert provider["models"]["MiniMax-M2.7"] == {
        "context_window": 204800,
        "input_modalities": ["text"],
        "thinking": ["always_on"],
    }
    assert config["pricing"]["MiniMax-M3"] == {
        "input": 0.6,
        "output": 2.4,
        "cache_read": 0.12,
        "cache_write": None,
    }
    assert config["pricing"]["MiniMax-M2.7"] == {
        "input": 0.3,
        "output": 1.2,
        "cache_read": 0.06,
        "cache_write": 0.375,
    }
    assert "MiniMax-M3" in config["grading"]["panel"]


@pytest.mark.parametrize(
    ("endpoint_region", "endpoint"),
    [
        ("global_en", "https://api.minimax.io/v1/chat/completions"),
        ("cn_zh", "https://api.minimaxi.com/v1/chat/completions"),
    ],
)
def test_openai_compatible_call_uses_configured_region(
    monkeypatch, endpoint_region, endpoint
):
    config = load_config()
    config["openai_compatible_providers"]["MiniMax"]["endpoint_region"] = endpoint_region
    monkeypatch.setenv("MINIMAX_API_KEY", "test-key")
    messages = [{"role": "user", "content": [{"text": "hello"}]}]

    with patch("benchmark._openai_compatible_request", return_value=_response()) as request:
        result = call_openai_compatible_model(
            config,
            "MiniMax-M3",
            messages,
            system="system prompt",
            max_tokens=128,
            temperature=0,
        )

    request.assert_called_once()
    request_endpoint, body, api_key = request.call_args.args
    assert request_endpoint == endpoint
    assert api_key == "test-key"
    assert body == {
        "model": "MiniMax-M3",
        "messages": [
            {"role": "system", "content": "system prompt"},
            {"role": "user", "content": "hello"},
        ],
        "max_tokens": 128,
        "temperature": 0,
    }
    assert result["output"] == "test response"
    assert result["input_tokens"] == 10
    assert result["output_tokens"] == 4
    assert result["cached_input_tokens"] == 2
    assert result["endpoint_region"] == endpoint_region


def test_openai_compatible_call_reports_missing_api_key(monkeypatch):
    config = load_config()
    monkeypatch.delenv("MINIMAX_API_KEY", raising=False)

    with patch("benchmark._openai_compatible_request") as request:
        result = call_openai_compatible_model(
            config,
            "MiniMax-M2.7",
            [{"role": "user", "content": [{"text": "hello"}]}],
        )

    assert result["error"] == "MINIMAX_API_KEY is not set"
    request.assert_not_called()


def test_run_benchmark_routes_minimax_to_openai_compatible_transport():
    config = load_config()
    config["prompt"] = {"user": "test prompt"}
    config["concurrency"] = 1
    result = {
        "model_id": "MiniMax-M3",
        "output": "test response",
        "input_tokens": 10,
        "output_tokens": 4,
        "total_tokens": 14,
        "latency_s": 0.1,
    }

    with (
        patch("benchmark.boto3.client"),
        patch("benchmark.call_openai_compatible_model", return_value=result) as call,
    ):
        benchmark = run_benchmark(config, ["MiniMax-M3"])

    call.assert_called_once()
    assert call.call_args.args[0] is config
    assert call.call_args.args[1] == "MiniMax-M3"
    assert benchmark["results"][0]["model_id"] == "MiniMax-M3"


def test_compute_cost_accounts_for_cached_input_tokens():
    result = {
        "model_id": "MiniMax-M3",
        "input_tokens": 1000,
        "cached_input_tokens": 400,
        "output_tokens": 500,
    }
    pricing = {
        "MiniMax-M3": {
            "input": 0.6,
            "output": 2.4,
            "cache_read": 0.12,
        }
    }

    assert compute_cost(result, pricing) == 0.001608


def test_openai_provider_lookup_is_model_specific():
    config = load_config()

    provider = _openai_provider_for_model(config, "MiniMax-M2.7")

    assert provider is not None
    assert provider[0] == "MiniMax"
