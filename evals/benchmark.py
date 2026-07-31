#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
Model Benchmark — Compare configured models on wa-review quality, cost, and latency.

Sends the same WA review prompt to multiple models via Bedrock Converse or
OpenAI-compatible chat endpoints,
capturing: output text, input/output token counts, wall-clock latency,
and (optionally) LLM-as-judge quality scores.

Usage:
    python benchmark.py                    # Run all models in config
    python benchmark.py --models us.anthropic.claude-sonnet-5 us.amazon.nova-pro-v1:0
    python benchmark.py --grade            # Also run quality grading
    python benchmark.py --results results/benchmark-2026-07-01.json  # Custom output path
"""

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import boto3
import yaml
from botocore.config import Config as BotoConfig
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials

SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "benchmark_config.yaml"
RESULTS_DIR = SCRIPT_DIR / "results"


def load_config(path: Path = CONFIG_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _extract_text(response: dict) -> str:
    """Extract text from a Converse API response, handling thinking/reasoning blocks."""
    text_parts = []
    for block in response["output"]["message"]["content"]:
        if "text" in block:
            text_parts.append(block["text"])
        elif "reasoningContent" in block:
            reasoning = block["reasoningContent"].get("reasoningText", {}).get("text", "")
            if reasoning:
                text_parts.append(reasoning)
    return "\n".join(text_parts)


MANTLE_CHAT_MODELS = {"openai.gpt-oss-120b", "openai.gpt-oss-20b"}
MANTLE_RESPONSES_MODELS = {"openai.gpt-5.5", "openai.gpt-5.4"}


def _is_mantle_model(model_id: str) -> bool:
    """Check if a model requires the bedrock-mantle endpoint."""
    return model_id in MANTLE_CHAT_MODELS or model_id in MANTLE_RESPONSES_MODELS


def _openai_provider_for_model(config: dict, model_id: str) -> tuple[str, dict] | None:
    """Return the configured OpenAI-compatible provider for a model, if any."""
    for provider_name, provider in config.get("openai_compatible_providers", {}).items():
        if model_id in provider.get("models", {}):
            return provider_name, provider
    return None


def _to_openai_messages(messages: list[dict], system: str | None = None) -> list[dict]:
    """Convert the benchmark's content-block messages to plain OpenAI messages."""
    oai_messages = []
    if system:
        oai_messages.append({"role": "system", "content": system})
    for msg in messages:
        content = msg["content"]
        if isinstance(content, list):
            content = "".join(
                block.get("text", "") for block in content if isinstance(block, dict)
            )
        oai_messages.append({"role": msg["role"], "content": content})
    return oai_messages


def _openai_compatible_request(endpoint: str, body: dict, api_key: str, timeout: int = 300):
    """Send a bearer-authenticated request to an OpenAI-compatible endpoint."""
    import requests as req

    response = req.post(
        endpoint,
        json=body,
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def call_openai_compatible_model(config: dict, model_id: str, messages: list[dict],
                                 system: str | None = None, max_tokens: int = 4096,
                                 temperature: float = 0) -> dict:
    """Call a configured model through its OpenAI-compatible chat endpoint."""
    start = time.time()
    provider_match = _openai_provider_for_model(config, model_id)
    if provider_match is None:
        return {
            "model_id": model_id,
            "error": "no OpenAI-compatible provider configured",
            "latency_s": 0,
        }

    provider_name, provider = provider_match
    api_key_env = provider["api_key_env"]
    api_key = os.getenv(api_key_env)
    if not api_key:
        return {
            "model_id": model_id,
            "error": f"{api_key_env} is not set",
            "latency_s": 0,
        }

    try:
        endpoint_region = provider.get("endpoint_region", "global_en")
        base_url = provider["endpoints"][endpoint_region].rstrip("/")
        body = {
            "model": model_id,
            "messages": _to_openai_messages(messages, system=system),
            "max_tokens": max_tokens,
        }
        if temperature is not None:
            body["temperature"] = temperature

        data = _openai_compatible_request(
            f"{base_url}/chat/completions", body, api_key
        )
        choice = data.get("choices", [{}])[0]
        message = choice.get("message", {})
        output_text = message.get("content") or ""
        if isinstance(output_text, list):
            output_text = "".join(
                part.get("text", "") for part in output_text if isinstance(part, dict)
            )
        usage = data.get("usage") or {}
        input_tokens = usage.get("prompt_tokens", 0) or 0
        output_tokens = usage.get("completion_tokens", 0) or 0
        cached_input_tokens = (
            (usage.get("prompt_tokens_details") or {}).get("cached_tokens", 0) or 0
        )
    except Exception as e:
        return {
            "model_id": model_id,
            "error": str(e),
            "latency_s": time.time() - start,
        }

    latency = time.time() - start
    if not output_text:
        return {
            "model_id": model_id,
            "error": f"empty response from {provider_name}",
            "latency_s": round(latency, 2),
        }

    return {
        "model_id": model_id,
        "output": output_text,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": usage.get("total_tokens", input_tokens + output_tokens),
        "cached_input_tokens": cached_input_tokens,
        "latency_s": round(latency, 2),
        "stop_reason": choice.get("finish_reason", "unknown"),
        "provider": provider_name,
        "endpoint_region": endpoint_region,
    }


def _mantle_request(endpoint: str, body: dict, region: str, timeout: int = 300):
    """Send a SigV4-signed request to bedrock-mantle."""
    import requests as req

    session = boto3.Session()
    credentials = session.get_credentials().get_frozen_credentials()
    body_bytes = json.dumps(body).encode()

    aws_request = AWSRequest(
        method="POST",
        url=endpoint,
        data=body_bytes,
        headers={"Content-Type": "application/json"},
    )
    SigV4Auth(credentials, "bedrock", region).add_auth(aws_request)

    resp = req.post(endpoint, data=body_bytes, headers=dict(aws_request.headers), timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def call_mantle_model(model_id: str, messages: list[dict], system: str | None = None,
                      max_tokens: int = 4096, temperature: float = 0, region: str = "us-east-1") -> dict:
    """Call a model via bedrock-mantle with SigV4 auth. Routes to correct API path."""

    start = time.time()
    try:
        if model_id in MANTLE_RESPONSES_MODELS:
            # GPT-5.5/5.4 use /openai/v1/responses (Responses API)
            endpoint = f"https://bedrock-mantle.{region}.api.aws/openai/v1/responses"
            user_input = ""
            if system:
                user_input += f"[System: {system}]\n\n"
            for msg in messages:
                content = msg["content"]
                if isinstance(content, list):
                    content = "".join(block.get("text", "") for block in content)
                user_input += content

            user_content = ""
            for msg in messages:
                content = msg["content"]
                if isinstance(content, list):
                    content = "".join(block.get("text", "") for block in content)
                user_content += content

            body = {
                "model": model_id,
                "input": user_content,
                "max_output_tokens": max_tokens,
            }
            if system:
                body["instructions"] = system

            data = _mantle_request(endpoint, body, region)

            # Extract text from Responses API format
            output_text = ""
            for output_item in data.get("output", []):
                for content_block in output_item.get("content", []):
                    if content_block.get("type") == "output_text":
                        output_text += content_block.get("text", "")

            usage = data.get("usage", {})
            input_tokens = usage.get("input_tokens", 0)
            output_tokens = usage.get("output_tokens", 0)

        else:
            # GPT-OSS models use /v1/chat/completions (Chat Completions API)
            endpoint = f"https://bedrock-mantle.{region}.api.aws/v1/chat/completions"
            oai_messages = []
            if system:
                oai_messages.append({"role": "system", "content": system})
            for msg in messages:
                content = msg["content"]
                if isinstance(content, list):
                    content = "".join(block.get("text", "") for block in content)
                oai_messages.append({"role": msg["role"], "content": content})

            body = {
                "model": model_id,
                "messages": oai_messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            }

            data = _mantle_request(endpoint, body, region)

            choice = data.get("choices", [{}])[0]
            output_text = choice.get("message", {}).get("content", "")
            usage = data.get("usage", {})
            input_tokens = usage.get("prompt_tokens", 0)
            output_tokens = usage.get("completion_tokens", 0)

    except Exception as e:
        return {"model_id": model_id, "error": str(e), "latency_s": time.time() - start}

    latency = time.time() - start

    if not output_text:
        return {"model_id": model_id, "error": "empty response from mantle", "latency_s": round(latency, 2)}

    return {
        "model_id": model_id,
        "output": output_text,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "latency_s": round(latency, 2),
        "stop_reason": data.get("status", "unknown"),
    }


THINKING_MODELS = {"claude-sonnet-5", "claude-opus-4-8", "claude-opus-4-7", "claude-fable-5"}


def _needs_thinking(model_id: str) -> bool:
    """Check if a model requires extended thinking configuration."""
    return any(m in model_id for m in THINKING_MODELS)


def _converse_with_retries(client, kwargs: dict, inference_config: dict, model_id: str):
    """Attempt converse call with fallback retries for validation errors."""
    try:
        return client.converse(**kwargs)
    except client.exceptions.ValidationException as e:
        err_msg = str(e).lower()
        # Retry 1: drop temperature if unsupported
        if "temperature" in err_msg and "temperature" in inference_config:
            del inference_config["temperature"]
            return client.converse(**kwargs)
        # Retry 2: switch thinking type from enabled to adaptive
        if "thinking.type.enabled" in err_msg or "adaptive" in err_msg:
            kwargs["additionalModelRequestFields"] = {
                "thinking": {"type": "adaptive"},
                "output_config": {"effort": "medium"},
            }
            inference_config.pop("temperature", None)
            return client.converse(**kwargs)
        # Retry 3: add thinking if model requires it
        if "think" in err_msg or "budget" in err_msg:
            inference_config.pop("temperature", None)
            kwargs["additionalModelRequestFields"] = {
                "thinking": {"type": "adaptive"},
                "output_config": {"effort": "medium"},
            }
            return client.converse(**kwargs)
        raise


PILLAR_FILES = [
    ("operational-excellence", "Operational Excellence (OPS)"),
    ("security", "Security (SEC)"),
    ("reliability", "Reliability (REL)"),
    ("performance-efficiency", "Performance Efficiency (PERF)"),
    ("cost-optimization", "Cost Optimization (COST)"),
    ("sustainability", "Sustainability (SUS)"),
]


def _load_pillar_content() -> dict[str, str]:
    """Load the 6 pillar-merged reference files from the shipped skill."""
    pillars_dir = SCRIPT_DIR.parent / "skills" / "wa-review" / "references" / "pillars"
    content = {}
    for slug, _ in PILLAR_FILES:
        p = pillars_dir / f"{slug}.md"
        if p.exists():
            content[slug] = p.read_text()
    return content


def call_model_subagent(client, model_id: str, workload_prompt: str,
                        system: str | None = None, max_tokens: int = 4096,
                        temperature: float = 0, region: str = "us-east-1",
                        config: dict | None = None) -> dict:
    """Subagent-pattern review: 6 parallel model calls (one per pillar) with
    pre-loaded pillar references. Aggregates cost/latency/output.

    This measures what real users experience when following the shipped skill's
    default full-review path (dispatch 6 pillar subagents).
    """
    pillar_content = _load_pillar_content()
    if len(pillar_content) != 6:
        return {"model_id": model_id,
                "error": f"missing pillar files (got {len(pillar_content)}/6)",
                "latency_s": 0}

    def _one_pillar(pillar_slug: str, pillar_name: str) -> dict:
        pillar_prompt = f"""# Reference: {pillar_name} pillar

The following pillar reference is pre-loaded. All best-practice content for this
pillar is included below.

{pillar_content[pillar_slug]}

---

# Workload to review

{workload_prompt}

---

# Your task

Review the workload above **ONLY for the {pillar_name} pillar**. Enumerate every
BP in the reference above. For each BP, assign one of four statuses: Implemented,
Partially Implemented, Not Implemented, or Not Applicable (with brief rationale).

Cite BPs in canonical `PILLAR##-BP##` format. Do not comment on other pillars —
they are reviewed in separate subagent invocations."""

        messages = [{"role": "user", "content": [{"text": pillar_prompt}]}]

        if config and _openai_provider_for_model(config, model_id):
            return call_openai_compatible_model(
                config, model_id, messages, system=system,
                max_tokens=max_tokens, temperature=temperature,
            )
        if _is_mantle_model(model_id):
            return call_mantle_model(model_id, messages, system=system,
                                     max_tokens=max_tokens, temperature=temperature,
                                     region=region)
        return call_model(client, model_id, messages, system=system,
                          max_tokens=max_tokens, temperature=temperature)

    start = time.time()
    pillar_results: list[dict] = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(_one_pillar, slug, name): slug
                   for slug, name in PILLAR_FILES}
        for fut in as_completed(futures):
            slug = futures[fut]
            try:
                pillar_results.append({"slug": slug, "result": fut.result()})
            except Exception as e:
                pillar_results.append({"slug": slug, "result": {"error": str(e)}})

    wall_clock = time.time() - start

    total_input = 0
    total_output = 0
    total_pillar_latency = 0.0
    output_parts = []
    errors: list[str] = []

    for pr in pillar_results:
        r = pr["result"]
        if "error" in r:
            errors.append(f"{pr['slug']}: {r['error']}")
            continue
        total_input += r.get("input_tokens", 0)
        total_output += r.get("output_tokens", 0)
        total_pillar_latency += r.get("latency_s", 0)
        output_parts.append(f"\n\n===== {pr['slug']} =====\n\n{r.get('output', '')}")

    if errors and not output_parts:
        return {"model_id": model_id, "error": f"all pillars failed: {'; '.join(errors)}",
                "latency_s": round(wall_clock, 2)}

    return {
        "model_id": model_id,
        "mode": "subagent",
        "output": "".join(output_parts),
        "input_tokens": total_input,
        "output_tokens": total_output,
        "total_tokens": total_input + total_output,
        "latency_s": round(wall_clock, 2),  # bounded by slowest pillar (parallel)
        "sum_pillar_latency_s": round(total_pillar_latency, 2),  # cost-proxy sum
        "pillars_succeeded": 6 - len(errors),
        "pillar_errors": errors,
    }


def call_model(client, model_id: str, messages: list[dict], system: str | None = None,
               max_tokens: int = 4096, temperature: float = 0) -> dict:
    """Call a single model via Converse API. Returns metrics + output."""
    inference_config = {"maxTokens": max_tokens}

    kwargs = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": inference_config,
    }

    if _needs_thinking(model_id):
        kwargs["additionalModelRequestFields"] = {
            "thinking": {"type": "adaptive"},
            "output_config": {"effort": "medium"},
        }
    else:
        if temperature is not None:
            inference_config["temperature"] = temperature

    if system:
        kwargs["system"] = [{"text": system}]

    start = time.time()
    try:
        response = _converse_with_retries(client, kwargs, inference_config, model_id)
    except Exception as e:
        return {"model_id": model_id, "error": str(e), "latency_s": time.time() - start}

    latency = time.time() - start
    usage = response.get("usage", {})
    output_text = _extract_text(response)

    if not output_text:
        return {"model_id": model_id, "error": "empty response (no text blocks)", "latency_s": round(latency, 2)}

    return {
        "model_id": model_id,
        "output": output_text,
        "input_tokens": usage.get("inputTokens", 0),
        "output_tokens": usage.get("outputTokens", 0),
        "total_tokens": usage.get("totalTokens", 0),
        "latency_s": round(latency, 2),
        "stop_reason": response.get("stopReason", "unknown"),
    }


def compute_cost(result: dict, pricing: dict) -> float | None:
    """Compute cost in USD for a single model invocation. Returns None if pricing unavailable."""
    model_id = result["model_id"]
    if model_id not in pricing or "error" in result:
        return None
    rates = pricing[model_id]
    cached_input_tokens = max(
        0, min(result.get("cached_input_tokens", 0), result["input_tokens"])
    )
    uncached_input_tokens = result["input_tokens"] - cached_input_tokens
    input_cost = (uncached_input_tokens / 1_000_000) * rates["input"]
    input_cost += (cached_input_tokens / 1_000_000) * rates.get(
        "cache_read", rates["input"]
    )
    output_cost = (result["output_tokens"] / 1_000_000) * rates["output"]
    return round(input_cost + output_cost, 6)


def grade_output(client, grading_model: str, prompt: str, output: str,
                 criteria: list[str], region: str) -> dict:
    """Use an LLM judge to score the output against criteria."""
    grading_prompt = f"""You are an expert evaluator for AWS Well-Architected reviews.

Score the following model output against each criterion on a 1-5 scale:
1 = completely fails  2 = poor  3 = adequate  4 = good  5 = excellent

MODEL INPUT (the prompt given):
{prompt}

MODEL OUTPUT (to evaluate):
{output}

CRITERIA:
{json.dumps(criteria, indent=2)}

Respond with ONLY a JSON object:
{{
  "scores": {{
    "<criterion>": {{"score": <1-5>, "reason": "<one sentence>"}},
    ...
  }},
  "overall": <1-5 average rounded to 1 decimal>
}}"""

    inference_config = {"maxTokens": 2048, "temperature": 0}
    kwargs = {
        "modelId": grading_model,
        "messages": [{"role": "user", "content": [{"text": grading_prompt}]}],
        "inferenceConfig": inference_config,
    }

    try:
        response = client.converse(**kwargs)
    except client.exceptions.ValidationException as e:
        if "temperature" in str(e).lower():
            del inference_config["temperature"]
            response = client.converse(**kwargs)
        else:
            return {"error": str(e)}

    text = _extract_text(response)
    if not text:
        return {"error": "grading model returned empty response"}
    try:
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])
    except (json.JSONDecodeError, ValueError):
        return {"raw": text, "error": "failed to parse grading JSON"}


def run_benchmark(config: dict, models: list[str], grade: bool = False) -> dict:
    """Run the benchmark across all models."""
    region = config["region"]
    client = boto3.client(
        "bedrock-runtime",
        region_name=region,
        config=BotoConfig(read_timeout=300),
    )

    prompt_config = config["prompt"]
    system_prompt = prompt_config.get("system")
    user_prompt = prompt_config["user"]
    messages = [{"role": "user", "content": [{"text": user_prompt}]}]

    max_tokens = config.get("max_tokens", 4096)
    temperature = config.get("temperature", 0)

    print(f"Benchmarking {len(models)} models in {region}")
    print(f"Prompt length: ~{len(user_prompt)} chars")
    print(f"Max tokens: {max_tokens}, Temperature: {temperature}")
    print("-" * 60)

    results = []

    mode = config.get("mode", "single")

    def run_one(model_id):
        print(f"  → {model_id} ({mode} mode)...")
        try:
            if mode == "subagent":
                result = call_model_subagent(client, model_id, user_prompt,
                                             system=system_prompt,
                                             max_tokens=max_tokens,
                                             temperature=temperature, region=region,
                                             config=config)
            elif _openai_provider_for_model(config, model_id):
                result = call_openai_compatible_model(
                    config, model_id, messages, system=system_prompt,
                    max_tokens=max_tokens, temperature=temperature,
                )
            elif _is_mantle_model(model_id):
                result = call_mantle_model(model_id, messages, system=system_prompt,
                                           max_tokens=max_tokens, temperature=temperature, region=region)
            else:
                result = call_model(client, model_id, messages, system=system_prompt,
                                    max_tokens=max_tokens, temperature=temperature)
        except Exception as e:
            return {"model_id": model_id, "error": str(e), "latency_s": 0}
        if "error" not in result:
            tokens_per_sec = result["output_tokens"] / result["latency_s"] if result["latency_s"] > 0 else 0
            result["tokens_per_sec"] = round(tokens_per_sec, 1)
            print(f"  ✓ {model_id}: {result['output_tokens']} tokens, "
                  f"{result['latency_s']}s, {result['tokens_per_sec']} tok/s")
        else:
            print(f"  ✗ {model_id}: {result['error'][:80]}")
        return result

    with ThreadPoolExecutor(max_workers=config.get("concurrency", 4)) as executor:
        futures = {executor.submit(run_one, m): m for m in models}
        for future in as_completed(futures):
            results.append(future.result())

    # Sort by model_id for consistent output
    results.sort(key=lambda r: r["model_id"])

    # Compute cost per invocation
    pricing = config.get("pricing", {})
    for r in results:
        cost = compute_cost(r, pricing)
        if cost is not None:
            r["cost_usd"] = cost

    # Optional grading pass — multi-model judge panel, no self-grading
    if grade and config.get("grading"):
        grading_config = config["grading"]
        panel = grading_config.get("panel", [grading_config.get("model")])
        criteria = grading_config["criteria"]

        def _model_family(model_id: str) -> str:
            """Extract provider family for self-grading exclusion."""
            if "minimax" in model_id.lower():
                return "minimax"
            if "anthropic" in model_id:
                return "anthropic"
            if "openai" in model_id or "gpt" in model_id:
                return "openai"
            if "deepseek" in model_id:
                return "deepseek"
            if "nova" in model_id or "amazon" in model_id:
                return "amazon"
            if "meta" in model_id or "llama" in model_id:
                return "meta"
            if "mistral" in model_id or "pixtral" in model_id:
                return "mistral"
            return model_id.split(".")[0]

        print(f"\nGrading with {len(panel)}-judge panel (no self-grading)...")
        print(f"  Panel: {', '.join(panel)}")
        for r in results:
            if "error" in r:
                r["grade"] = {"error": "skipped — model call failed"}
                continue

            model_family = _model_family(r["model_id"])
            eligible_judges = [j for j in panel if _model_family(j) != model_family]
            if not eligible_judges:
                eligible_judges = panel  # fallback if no cross-family judge available

            judge_scores = []
            for judge in eligible_judges:
                print(f"  {r['model_id']} ← judged by {judge}...")
                if _is_mantle_model(judge) or _openai_provider_for_model(config, judge):
                    # Use the configured OpenAI-compatible transport for grading.
                    grading_prompt = f"""You are an expert evaluator for AWS Well-Architected reviews.

Score the following model output against each criterion on a 1-5 scale:
1 = completely fails  2 = poor  3 = adequate  4 = good  5 = excellent

MODEL INPUT (the prompt given):
{user_prompt}

MODEL OUTPUT (to evaluate):
{r['output']}

CRITERIA:
{json.dumps(criteria, indent=2)}

Respond with ONLY a JSON object:
{{
  "scores": {{
    "<criterion>": {{"score": <1-5>, "reason": "<one sentence>"}},
    ...
  }},
  "overall": <1-5 average rounded to 1 decimal>
}}"""
                    if _is_mantle_model(judge):
                        transport_result = call_mantle_model(
                            judge,
                            [{"role": "user", "content": [{"text": grading_prompt}]}],
                            max_tokens=2048, temperature=0, region=region,
                        )
                    else:
                        transport_result = call_openai_compatible_model(
                            config,
                            judge,
                            [{"role": "user", "content": [{"text": grading_prompt}]}],
                            max_tokens=2048, temperature=0,
                        )
                    if "error" not in transport_result:
                        text = transport_result["output"]
                        try:
                            start_idx = text.find("{")
                            end_idx = text.rfind("}") + 1
                            parsed = json.loads(text[start_idx:end_idx])
                            if "overall" in parsed:
                                judge_scores.append(parsed["overall"])
                        except (json.JSONDecodeError, ValueError):
                            pass
                else:
                    result_grade = grade_output(client, judge, user_prompt,
                                               r["output"], criteria, region)
                    if "overall" in result_grade:
                        judge_scores.append(result_grade["overall"])

            if judge_scores:
                avg_score = round(sum(judge_scores) / len(judge_scores), 1)
                r["grade"] = {
                    "overall": avg_score,
                    "judge_scores": {panel[i] if i < len(panel) else f"judge_{i}": s
                                     for i, s in enumerate(judge_scores)},
                    "judges_used": len(judge_scores),
                }
            else:
                r["grade"] = {"error": "all judges failed"}

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "config": {
            "region": region,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "prompt_chars": len(user_prompt),
            "models_tested": len(models),
        },
        "results": results,
    }


def print_summary(benchmark: dict):
    """Print a comparison table."""
    results = benchmark["results"]
    has_cost = any("cost_usd" in r for r in results)
    width = 100 if has_cost else 90
    print("\n" + "=" * width)
    header = f"{'Model':<45} {'In Tok':>7} {'Out Tok':>8} {'Latency':>8} {'Tok/s':>7} {'Grade':>6}"
    if has_cost:
        header += f" {'Cost':>8}"
    print(header)
    print("-" * width)
    for r in sorted(results, key=lambda x: x.get("latency_s", 999)):
        if "error" in r:
            line = f"{r['model_id']:<45} {'ERROR':>7} {'':<8} {r['latency_s']:>7.1f}s {'':<7} {'—':>6}"
            if has_cost:
                line += f" {'—':>8}"
            print(line)
            continue
        grade_str = "—"
        if "grade" in r and "overall" in r.get("grade", {}):
            grade_str = f"{r['grade']['overall']:.1f}"
        line = (f"{r['model_id']:<45} {r['input_tokens']:>7,} {r['output_tokens']:>8,} "
                f"{r['latency_s']:>7.1f}s {r['tokens_per_sec']:>6.0f} {grade_str:>6}")
        if has_cost:
            cost = r.get("cost_usd")
            cost_str = f"${cost:.4f}" if cost is not None else "—"
            line += f" {cost_str:>8}"
        print(line)
    print("=" * width)


def main():
    parser = argparse.ArgumentParser(description="Benchmark configured models on WA review tasks")
    parser.add_argument("--config", type=Path, default=CONFIG_PATH, help="Config file path")
    parser.add_argument("--models", nargs="+", help="Override model list from config")
    parser.add_argument("--grade", action="store_true", help="Run LLM-as-judge quality grading")
    parser.add_argument("--results", type=Path, help="Custom output file path")
    parser.add_argument("--concurrency", type=int, help="Max parallel model calls")
    parser.add_argument("--mode", choices=["single", "subagent"], default="single",
                        help="single = one Converse call per model (baseline). "
                             "subagent = 6 parallel calls per model with pre-loaded pillar refs "
                             "(measures the shipped skill's default full-review path).")
    args = parser.parse_args()

    config = load_config(args.config)
    models = args.models or config["models"]
    if args.concurrency:
        config["concurrency"] = args.concurrency
    config["mode"] = args.mode

    benchmark = run_benchmark(config, models, grade=args.grade)
    print_summary(benchmark)

    # Save results
    RESULTS_DIR.mkdir(exist_ok=True)
    out_path = args.results or RESULTS_DIR / f"benchmark-{time.strftime('%Y%m%d-%H%M%S')}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(benchmark, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to: {out_path}")


if __name__ == "__main__":
    main()
