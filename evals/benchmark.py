#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
Model Benchmark — Compare Bedrock models on wa-review quality, cost, and latency.

Sends the same WA review prompt to multiple models via the Converse API,
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


THINKING_MODELS = {"claude-sonnet-5", "claude-opus-4-8", "claude-opus-4-7"}


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
    input_cost = (result["input_tokens"] / 1_000_000) * rates["input"]
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

    def run_one(model_id):
        print(f"  → {model_id}...")
        try:
            if _is_mantle_model(model_id):
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

    # Optional grading pass
    if grade and config.get("grading"):
        grading_model = config["grading"]["model"]
        criteria = config["grading"]["criteria"]
        print(f"\nGrading with {grading_model}...")
        for r in results:
            if "error" in r:
                r["grade"] = {"error": "skipped — model call failed"}
                continue
            print(f"  Grading {r['model_id']}...")
            r["grade"] = grade_output(client, grading_model, user_prompt,
                                      r["output"], criteria, region)

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
    parser = argparse.ArgumentParser(description="Benchmark Bedrock models on WA review tasks")
    parser.add_argument("--config", type=Path, default=CONFIG_PATH, help="Config file path")
    parser.add_argument("--models", nargs="+", help="Override model list from config")
    parser.add_argument("--grade", action="store_true", help="Run LLM-as-judge quality grading")
    parser.add_argument("--results", type=Path, help="Custom output file path")
    parser.add_argument("--concurrency", type=int, help="Max parallel model calls")
    args = parser.parse_args()

    config = load_config(args.config)
    models = args.models or config["models"]
    if args.concurrency:
        config["concurrency"] = args.concurrency

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
