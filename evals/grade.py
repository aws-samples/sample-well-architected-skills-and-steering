# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
LLM-as-judge grader for eval assertions.

Takes a model output and a list of assertions, asks a grading model
to evaluate each assertion as PASS or FAIL with justification.
"""

import json

import boto3


GRADING_PROMPT = """You are an evaluation grader. Your job is to determine whether a given output satisfies specific assertions.

For each assertion, respond with a JSON object containing:
- "assertion": the assertion text
- "pass": true or false
- "reason": a one-sentence justification

Respond ONLY with a JSON array of these objects, no other text.

## Output to evaluate

{output}

## Assertions to grade

{assertions}
"""


def grade_response(config: dict, output: str, assertions: list[str]) -> list[dict]:
    """
    Grade a response against a list of assertions using LLM-as-judge.

    Returns a list of dicts: [{"assertion": str, "pass": bool, "reason": str}, ...]
    """
    assertions_text = "\n".join(f"{i+1}. {a}" for i, a in enumerate(assertions))

    prompt = GRADING_PROMPT.format(
        output=output,
        assertions=assertions_text,
    )

    client = boto3.client("bedrock-runtime", region_name=config["region"])

    response = client.converse(
        modelId=config["grading_model"],
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig={
            "temperature": 0,
            "maxTokens": 2048,
        },
    )

    raw = response["output"]["message"]["content"][0]["text"]

    try:
        grades = json.loads(raw)
    except json.JSONDecodeError:
        # Try to extract JSON from the response if wrapped in markdown
        import re
        match = re.search(r"\[.*\]", raw, re.DOTALL)
        if match:
            grades = json.loads(match.group())
        else:
            # Fallback: mark all as failed with parse error
            grades = [
                {"assertion": a, "pass": False, "reason": "Failed to parse grader response"}
                for a in assertions
            ]

    # Normalize: ensure each grade has the right keys
    normalized = []
    for i, assertion in enumerate(assertions):
        if i < len(grades):
            g = grades[i]
            normalized.append({
                "assertion": assertion,
                "pass": bool(g.get("pass", False)),
                "reason": g.get("reason", "No reason provided"),
            })
        else:
            normalized.append({
                "assertion": assertion,
                "pass": False,
                "reason": "Grader did not return result for this assertion",
            })

    return normalized
