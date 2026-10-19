# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Tests for the benchmark transport and model configuration."""

import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest
import requests
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmark import (  # noqa: E402
    CONFIG_PATH,
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

    assert [m for m in config["models"] if m.startswith("MiniMax-")] == [
        "MiniMax-M3.1-Flash", "MiniMax-M3",
    ]
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
    assert provider["models"]["MiniMax-M3.1-Flash"] == {
        "context_window": 1000000,
        "input_modalities": ["text", "image", "video"],
        "thinking": ["adaptive"],
    }
    assert "MiniMax-M3.1-Flash" in config["grading"]["panel"]


def test_tracked_config_carries_no_pricing():
    """Rates are looked up locally, never committed. See pricing.local.yaml.example."""
    with open(CONFIG_PATH, encoding="utf-8") as f:
        tracked = yaml.safe_load(f)

    assert "pricing" not in tracked
    example = CONFIG_PATH.with_name("pricing.local.yaml.example")
    pricing = yaml.safe_load(example.read_text(encoding="utf-8"))["pricing"]
    assert [m for m in pricing if m.startswith("MiniMax-")] == [
        "MiniMax-M3.1-Flash", "MiniMax-M3",
    ]
    assert all(rate is None for rates in pricing.values() for rate in rates.values())


def test_local_pricing_merges_over_the_tracked_config(tmp_path, monkeypatch):
    local = tmp_path / "pricing.local.yaml"
    local.write_text(
        "pricing:\n"
        "  test.model-a:\n"
        "    input: 1.0\n"
        "    output: 2.0\n"
        # Placeholder entries stay out: compute_cost would divide by None.
        "  test.model-b:\n"
        "    input: null\n"
        "    output: null\n",
        encoding="utf-8",
    )
    monkeypatch.setattr("benchmark.PRICING_PATH", local)

    pricing = load_config().get("pricing", {})

    assert pricing == {"test.model-a": {"input": 1.0, "output": 2.0}}


@pytest.mark.parametrize(
    ("endpoint_region", "endpoint"),
    [
        ("global_en", "https://api.minimax.io/v1/chat/completions"),
        ("cn_zh", "https://api.minimaxi.com/v1/chat/completions"),
    ],
)
@pytest.mark.parametrize("model_id", ["MiniMax-M3.1-Flash", "MiniMax-M3"])
@pytest.mark.parametrize("temperature", [0, None])
def test_openai_compatible_call_uses_configured_region(
    monkeypatch, endpoint_region, endpoint, model_id, temperature
):
    config = load_config()
    config["openai_compatible_providers"]["MiniMax"]["endpoint_region"] = endpoint_region
    monkeypatch.setenv("MINIMAX_API_KEY", "test-key")
    messages = [{"role": "user", "content": [{"text": "hello"}]}]

    response = requests.Response()
    response.status_code = 200
    response._content = json.dumps(_response()).encode()
    with patch("requests.sessions.Session.send", return_value=response) as send:
        result = call_openai_compatible_model(
            config,
            model_id,
            messages,
            system="system prompt",
            max_tokens=128,
            temperature=temperature,
        )

    send.assert_called_once()
    request = send.call_args.args[0]
    assert request.method == "POST"
    assert request.url == endpoint
    assert request.headers["Authorization"] == "Bearer test-key"
    assert request.headers["Content-Type"] == "application/json"
    expected = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": "system prompt"},
            {"role": "user", "content": "hello"},
        ],
        "max_tokens": 128,
    }
    if temperature is not None:
        expected["temperature"] = temperature
    # Capability metadata must not leak into thinking, effort, or service-tier fields.
    assert json.loads(request.body) == expected
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
            "MiniMax-M3.1-Flash",
            [{"role": "user", "content": [{"text": "hello"}]}],
        )

    assert result["error"] == "MINIMAX_API_KEY is not set"
    request.assert_not_called()


@pytest.mark.parametrize("model_id", ["MiniMax-M3.1-Flash", "MiniMax-M3"])
def test_run_benchmark_routes_minimax_to_openai_compatible_transport(model_id):
    config = load_config()
    config["prompt"] = {"user": "test prompt"}
    config["concurrency"] = 1
    result = {
        "model_id": model_id,
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
        benchmark = run_benchmark(config, [model_id])

    call.assert_called_once()
    assert call.call_args.args[0] is config
    assert call.call_args.args[1] == model_id
    assert benchmark["results"][0]["model_id"] == model_id


def test_compute_cost_accounts_for_cached_input_tokens():
    result = {
        "model_id": "test.model",
        "input_tokens": 1000,
        "cached_input_tokens": 400,
        "output_tokens": 500,
    }
    # Synthetic round rates, not any provider's real prices: 600 uncached input
    # at 10.0, 400 cached at 5.0, 500 output at 20.0, all per 1M tokens.
    pricing = {
        "test.model": {
            "input": 10.0,
            "output": 20.0,
            "cache_read": 5.0,
        }
    }

    assert compute_cost(result, pricing) == 0.018


def test_compute_cost_is_none_without_a_rate_for_the_model():
    result = {"model_id": "test.model", "input_tokens": 1000, "output_tokens": 500}

    assert compute_cost(result, {}) is None


@pytest.mark.parametrize("model_id", ["MiniMax-M3.1-Flash", "MiniMax-M3"])
def test_openai_provider_lookup_is_model_specific(model_id):
    config = load_config()

    provider = _openai_provider_for_model(config, model_id)

    assert provider is not None
    assert provider[0] == "MiniMax"
    assert _openai_provider_for_model(config, "unconfigured-model") is None


@pytest.mark.parametrize("model_id", ["MiniMax-M2.7", "custom-model"])
def test_explicit_legacy_and_custom_provider_models_remain_usable(monkeypatch, model_id):
    config = load_config()
    config["openai_compatible_providers"]["MiniMax"]["models"][model_id] = {}
    monkeypatch.setenv("MINIMAX_API_KEY", "test-key")

    with patch("benchmark._openai_compatible_request", return_value=_response()) as request:
        result = call_openai_compatible_model(
            config, model_id, [{"role": "user", "content": "hello"}]
        )

    assert request.call_args.args[1]["model"] == model_id
    assert result["model_id"] == model_id
    assert result["output"] == "test response"
