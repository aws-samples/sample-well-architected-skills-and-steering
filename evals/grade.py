# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
LLM-as-judge grader for eval assertions.

Takes a model output and a list of assertions, asks a grading model
to evaluate each assertion as PASS or FAIL with justification.
"""

import json

import boto3


def _grader_converse(config: dict, prompt: str) -> str:
    """
    Call the grading model with temperature=0, dropping temperature and retrying
    once if Bedrock reports the parameter is unsupported (e.g. Claude Opus 4.8).

    This is model-agnostic: it reacts to Bedrock's own ValidationException rather
    than guessing from the model id, so it works for ARNs and inference-profile
    ids and does not wrongly strip temperature from models that support it.
    """
    client = boto3.client("bedrock-runtime", region_name=config["region"])

    inference_config = {"maxTokens": 2048, "temperature": 0}
    kwargs = {
        "modelId": config["grading_model"],
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": inference_config,
    }

    try:
        response = client.converse(**kwargs)
    except client.exceptions.ValidationException as e:
        if "temperature" in inference_config and "temperature" in str(e).lower():
            del inference_config["temperature"]
            response = client.converse(**kwargs)
        else:
            raise
    return response["output"]["message"]["content"][0]["text"]


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

    raw = _grader_converse(config, prompt)

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


def grade_process(config: dict, output: str, process_assertions: list[str]) -> list[dict]:
    """
    Grade whether the output follows expected process/structure patterns.

    Returns a list of dicts: [{"assertion": str, "pass": bool, "reason": str}, ...]
    """
    prompt = (
        "You are evaluating whether an AI assistant's response follows the expected process and structure.\n\n"
        "For each assertion about the process/structure, respond with:\n"
        '- "assertion": the assertion text\n'
        '- "pass": true or false\n'
        '- "reason": a one-sentence justification\n\n'
        "Respond ONLY with a JSON array of these objects, no other text.\n\n"
        "## Response to evaluate\n"
        f"{output}\n\n"
        "## Process assertions to grade\n"
    )
    for i, assertion in enumerate(process_assertions, 1):
        prompt += f"{i}. {assertion}\n"

    raw = _grader_converse(config, prompt)

    try:
        grades = json.loads(raw)
    except json.JSONDecodeError:
        import re
        match = re.search(r"\[.*\]", raw, re.DOTALL)
        if match:
            grades = json.loads(match.group())
        else:
            grades = [
                {"assertion": a, "pass": False, "reason": "Failed to parse grader response"}
                for a in process_assertions
            ]

    normalized = []
    for i, assertion in enumerate(process_assertions):
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


def grade_knowledge(config: dict, output: str, knowledge_assertions: list[dict]) -> list[dict]:
    """
    Grade factual accuracy with source-cited assertions.

    Each knowledge assertion has: claim, source, rationale.
    Returns a list of dicts: [{"assertion": str, "pass": bool, "reason": str}, ...]
    """
    prompt = (
        "You are evaluating the factual accuracy of an AI assistant's response.\n\n"
        "For each knowledge assertion, verify whether the response makes the claimed statement correctly.\n"
        "Each assertion has a claim, source, and rationale.\n\n"
        "For each, respond with:\n"
        '- "assertion": the claim text\n'
        '- "pass": true or false\n'
        '- "reason": a one-sentence justification referencing the source\n\n'
        "Respond ONLY with a JSON array of these objects, no other text.\n\n"
        "## Response to evaluate\n"
        f"{output}\n\n"
        "## Knowledge assertions to grade\n"
    )
    for i, ka in enumerate(knowledge_assertions, 1):
        prompt += f'{i}. Claim: {ka["claim"]}\n   Source: {ka["source"]}\n   Rationale: {ka["rationale"]}\n'

    raw = _grader_converse(config, prompt)

    try:
        grades = json.loads(raw)
    except json.JSONDecodeError:
        import re
        match = re.search(r"\[.*\]", raw, re.DOTALL)
        if match:
            grades = json.loads(match.group())
        else:
            grades = [
                {"assertion": ka["claim"], "pass": False, "reason": "Failed to parse grader response"}
                for ka in knowledge_assertions
            ]

    normalized = []
    for i, ka in enumerate(knowledge_assertions):
        if i < len(grades):
            g = grades[i]
            normalized.append({
                "assertion": ka["claim"],
                "pass": bool(g.get("pass", False)),
                "reason": g.get("reason", "No reason provided"),
            })
        else:
            normalized.append({
                "assertion": ka["claim"],
                "pass": False,
                "reason": "Grader did not return result for this assertion",
            })

    return normalized
