#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
List available Bedrock models that support the Converse API.

Helps you discover models to experiment with in evals.
Usage:
    uv run python list_models.py
    uv run python list_models.py --region us-west-2
    uv run python list_models.py --filter llama
"""

import argparse

import boto3
import yaml

CONFIG_PATH = "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def list_models(region: str, filter_text: str | None = None) -> None:
    client = boto3.client("bedrock", region_name=region)

    print(f"\n  Available Bedrock models in {region}")
    print(f"  {'='*60}\n")

    # List inference profiles (cross-region and on-demand)
    profiles = client.list_inference_profiles()
    profile_ids = {p["inferenceProfileId"] for p in profiles.get("inferenceProfileSummaries", [])}

    # List foundation models with Converse support
    response = client.list_foundation_models()
    models = response.get("modelSummaries", [])

    # Filter to models that support converse
    converse_models = [
        m for m in models
        if "CONVERSE" in m.get("inferenceTypesSupported", [])
        or "ON_DEMAND" in m.get("inferenceTypesSupported", [])
    ]

    if filter_text:
        filter_lower = filter_text.lower()
        converse_models = [
            m for m in converse_models
            if filter_lower in m.get("modelId", "").lower()
            or filter_lower in m.get("providerName", "").lower()
            or filter_lower in m.get("modelName", "").lower()
        ]

    # Group by provider
    by_provider: dict[str, list] = {}
    for m in converse_models:
        provider = m.get("providerName", "Unknown")
        by_provider.setdefault(provider, []).append(m)

    for provider in sorted(by_provider.keys()):
        print(f"  {provider}")
        print(f"  {'-'*40}")
        for m in sorted(by_provider[provider], key=lambda x: x["modelId"]):
            model_id = m["modelId"]
            name = m.get("modelName", "")
            status = "✓ active" if m.get("modelLifecycle", {}).get("status") == "ACTIVE" else ""
            print(f"    {model_id:<55} {name:<25} {status}")
        print()

    # Also show inference profiles
    if profile_ids:
        filtered_profiles = profile_ids
        if filter_text:
            filter_lower = filter_text.lower()
            filtered_profiles = {p for p in profile_ids if filter_lower in p.lower()}

        if filtered_profiles:
            print(f"  Inference Profiles (cross-region)")
            print(f"  {'-'*40}")
            for pid in sorted(filtered_profiles):
                print(f"    {pid}")
            print()

    config = load_config()
    print(f"  Current config:")
    print(f"    generation_model: {config.get('generation_model', 'not set')}")
    print(f"    grading_model:    {config.get('grading_model', 'not set')}")
    print(f"\n  To use a different model, update evals/config.yaml")
    print()


def main():
    parser = argparse.ArgumentParser(description="List available Bedrock models for eval experimentation")
    parser.add_argument("--region", type=str, default=None, help="AWS region (default: from config.yaml)")
    parser.add_argument("--filter", type=str, default=None, help="Filter by provider or model name (e.g., 'llama', 'nova', 'mistral')")
    args = parser.parse_args()

    config = load_config()
    region = args.region or config.get("region", "us-east-1")

    list_models(region, args.filter)


if __name__ == "__main__":
    main()
