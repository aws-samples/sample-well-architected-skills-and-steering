#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
Well-Architected Skills Eval Runner

Runs skill evaluations using Amazon Bedrock's Converse API.
For each test case, generates responses with and without the skill loaded,
then grades assertions using an LLM-as-judge.
"""

import argparse
import functools
import json
import sys
import time

print = functools.partial(print, flush=True)
from pathlib import Path

import yaml

from grade import grade_response, grade_process, grade_knowledge
from report import print_report, save_results

SKILLS_DIR = Path(__file__).parent.parent / "skills"
CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config(config_path: Path = CONFIG_PATH) -> dict:
    with open(config_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_skill(skill_name: str) -> str:
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_path.exists():
        raise FileNotFoundError(f"Skill not found: {skill_path}")
    return skill_path.read_text()


def load_evals(skill_name: str) -> dict:
    evals_path = SKILLS_DIR / skill_name / "evals" / "evals.json"
    if not evals_path.exists():
        raise FileNotFoundError(f"Evals not found: {evals_path}")
    with open(evals_path, encoding="utf-8") as f:
        return json.load(f)


def load_triggering(skill_name: str) -> dict | None:
    path = SKILLS_DIR / skill_name / "evals" / "triggering.json"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def list_skills_with_triggering() -> list[str]:
    return sorted(
        d.name for d in SKILLS_DIR.iterdir()
        if d.is_dir() and (d / "evals" / "triggering.json").exists()
    )


def list_skills() -> list[str]:
    return sorted(
        d.name for d in SKILLS_DIR.iterdir()
        if d.is_dir() and (d / "evals" / "evals.json").exists()
    )


def call_bedrock(config: dict, messages: list[dict], system: str | None = None) -> str:
    import boto3
    from botocore.config import Config

    client = boto3.client(
        "bedrock-runtime",
        region_name=config["region"],
        config=Config(read_timeout=300),
    )

    inference_config = {"maxTokens": config["max_tokens"]}
    if config.get("temperature") is not None:
        inference_config["temperature"] = config["temperature"]

    kwargs = {
        "modelId": config["generation_model"],
        "messages": messages,
        "inferenceConfig": inference_config,
    }
    if system:
        kwargs["system"] = [{"text": system}]

    try:
        response = client.converse(**kwargs)
    except client.exceptions.ValidationException as e:
        # Some models (e.g. Claude Opus 4.8) reject the temperature parameter.
        # Rather than guessing from the model id, drop it and retry once when
        # Bedrock tells us the parameter is unsupported.
        if "temperature" in inference_config and "temperature" in str(e).lower():
            del inference_config["temperature"]
            response = client.converse(**kwargs)
        else:
            raise
    return response["output"]["message"]["content"][0]["text"]


def run_eval_case(config: dict, skill_content: str, eval_case: dict) -> dict:
    prompt = eval_case["prompt"]
    messages = [{"role": "user", "content": [{"text": prompt}]}]

    # Baseline: no skill context
    baseline_output = call_bedrock(config, messages)

    # With skill: inject SKILL.md as system context
    system_prompt = (
        "You are an AWS Well-Architected expert. Follow the skill instructions below "
        "to produce your response.\n\n"
        f"---\n\n{skill_content}"
    )
    skill_output = call_bedrock(config, messages, system=system_prompt)

    return {
        "id": eval_case["id"],
        "prompt": prompt,
        "baseline_output": baseline_output,
        "skill_output": skill_output,
    }


def _run_and_grade_case(config: dict, skill_content: str, case: dict, verbose: bool = False) -> dict:
    """Run a single eval case (generate + grade). Thread-safe."""
    case_id = case["id"]
    prompt_short = case["prompt"][:60]
    print(f"\n  Case {case_id}: {prompt_short}...")
    start = time.time()

    outputs = run_eval_case(config, skill_content, case)
    elapsed = time.time() - start
    print(f"  Case {case_id}: Generated in {elapsed:.1f}s")

    print(f"  Case {case_id}: Grading baseline...")
    baseline_grades = grade_response(
        config, outputs["baseline_output"], case["assertions"]
    )

    print(f"  Case {case_id}: Grading with-skill...")
    skill_grades = grade_response(
        config, outputs["skill_output"], case["assertions"]
    )

    case_result = {
        "id": case_id,
        "prompt": case["prompt"],
        "assertions": case["assertions"],
        "baseline": {
            "output": outputs["baseline_output"],
            "grades": baseline_grades,
            "score": sum(1 for g in baseline_grades if g["pass"]) / len(baseline_grades),
        },
        "with_skill": {
            "output": outputs["skill_output"],
            "grades": skill_grades,
            "score": sum(1 for g in skill_grades if g["pass"]) / len(skill_grades),
        },
    }

    # Process assertions (optional layer)
    if "process_assertions" in case:
        print(f"  Case {case_id}: Grading process...")
        process_grades = grade_process(
            config, outputs["skill_output"], case["process_assertions"]
        )
        case_result["with_skill"]["process_grades"] = process_grades
        case_result["with_skill"]["process_score"] = (
            sum(1 for g in process_grades if g["pass"]) / len(process_grades)
        )

    # Knowledge assertions (optional layer)
    if "knowledge_assertions" in case:
        print(f"  Case {case_id}: Grading knowledge...")
        knowledge_grades = grade_knowledge(
            config, outputs["skill_output"], case["knowledge_assertions"]
        )
        case_result["with_skill"]["knowledge_grades"] = knowledge_grades
        case_result["with_skill"]["knowledge_score"] = (
            sum(1 for g in knowledge_grades if g["pass"]) / len(knowledge_grades)
        )

    if verbose:
        print(f"\n    Case {case_id} — Baseline: {case_result['baseline']['score']:.0%}  Skill: {case_result['with_skill']['score']:.0%}")
        for i, (bg, sg) in enumerate(zip(baseline_grades, skill_grades)):
            b_icon = "✓" if bg["pass"] else "✗"
            s_icon = "✓" if sg["pass"] else "✗"
            print(f"      [{b_icon} → {s_icon}] {case['assertions'][i]}")

    return case_result


def run_skill_evals(config: dict, skill_name: str, verbose: bool = False, parallel: bool = False) -> dict:
    print(f"\n{'='*60}")
    print(f"  Evaluating: {skill_name}" + (" (parallel)" if parallel else ""))
    print(f"{'='*60}")

    skill_content = load_skill(skill_name)
    evals_data = load_evals(skill_name)
    eval_cases = evals_data["evals"]

    results = {
        "skill_name": skill_name,
        "cases": [],
    }

    if parallel:
        from concurrent.futures import ThreadPoolExecutor, as_completed

        with ThreadPoolExecutor(max_workers=len(eval_cases)) as executor:
            futures = {
                executor.submit(_run_and_grade_case, config, skill_content, case, verbose): case["id"]
                for case in eval_cases
            }
            case_results = {}
            for future in as_completed(futures):
                case_id = futures[future]
                case_results[case_id] = future.result()

        results["cases"] = [case_results[case["id"]] for case in eval_cases]
    else:
        for case in eval_cases:
            case_result = _run_and_grade_case(config, skill_content, case, verbose)
            results["cases"].append(case_result)

    # Aggregate scores
    baseline_scores = [c["baseline"]["score"] for c in results["cases"]]
    skill_scores = [c["with_skill"]["score"] for c in results["cases"]]
    results["aggregate"] = {
        "baseline_avg": sum(baseline_scores) / len(baseline_scores),
        "skill_avg": sum(skill_scores) / len(skill_scores),
        "delta": sum(skill_scores) / len(skill_scores) - sum(baseline_scores) / len(baseline_scores),
    }

    return results


def extract_description(skill_content: str) -> str:
    """Extract the description field from SKILL.md YAML frontmatter."""
    lines = skill_content.split("\n")
    if lines[0].strip() != "---":
        return ""
    desc_lines = []
    capturing_desc = False
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("description:"):
            capturing_desc = True
            value = line[len("description:"):].strip()
            if value:
                desc_lines.append(value.strip('"'))
        elif capturing_desc:
            if line.startswith(" ") or line.startswith("\t"):
                desc_lines.append(line.strip())
            else:
                capturing_desc = False
    return " ".join(desc_lines)


def run_triggering_evals(config: dict, skill_name: str | None = None, verbose: bool = False) -> list[dict]:
    """Run triggering evals: test if skill descriptions route user intent correctly."""
    from report import print_triggering_report

    skills_to_test = [skill_name] if skill_name else list_skills_with_triggering()

    # Collect all skill descriptions for the routing prompt
    all_skills = list_skills()
    skill_descriptions = {}
    for s in all_skills:
        content = load_skill(s)
        desc = extract_description(content)
        if desc:
            skill_descriptions[s] = desc

    results = []

    for skill in skills_to_test:
        triggering_data = load_triggering(skill)
        if not triggering_data:
            continue

        print(f"\n{'='*60}")
        print(f"  Triggering eval: {skill}")
        print(f"{'='*60}")

        prompts = triggering_data["prompts"]
        tp, tn, fp, fn = 0, 0, 0, 0
        details = []

        for prompt_item in prompts:
            text = prompt_item["text"]
            should_trigger = prompt_item["should_trigger"]

            routing_prompt = "Given these available skills:\n"
            for s_name, s_desc in skill_descriptions.items():
                routing_prompt += f"- {s_name}: {s_desc}\n"
            routing_prompt += (
                f"\nWhich skill should handle this user request? "
                f"Reply with ONLY the skill name (exactly as listed above), or \"none\" if no skill matches.\n\n"
                f"User request: \"{text}\""
            )

            messages = [{"role": "user", "content": [{"text": routing_prompt}]}]
            response = call_bedrock(config, messages).strip().lower()

            routed_to_skill = response == skill

            if should_trigger and routed_to_skill:
                tp += 1
                status = "TP"
            elif not should_trigger and not routed_to_skill:
                tn += 1
                status = "TN"
            elif should_trigger and not routed_to_skill:
                fn += 1
                status = "FN"
            else:
                fp += 1
                status = "FP"

            details.append({
                "text": text,
                "should_trigger": should_trigger,
                "model_response": response,
                "status": status,
            })

            if verbose:
                icon = "✓" if status in ("TP", "TN") else "✗"
                print(f"    [{icon} {status}] \"{text[:50]}...\" → {response}")

        total = tp + tn + fp + fn
        accuracy = (tp + tn) / total if total > 0 else 0

        results.append({
            "skill_name": skill,
            "accuracy": accuracy,
            "tp": tp, "tn": tn, "fp": fp, "fn": fn,
            "total": total,
            "details": details,
        })

        print(f"  Accuracy: {accuracy:.0%} (TP={tp} TN={tn} FP={fp} FN={fn})")

    print_triggering_report(results)
    return results


def main():
    parser = argparse.ArgumentParser(description="Run Well-Architected skill evaluations")
    parser.add_argument(
        "--skill", type=str, default=None,
        help="Skill to evaluate (default: all skills)"
    )
    parser.add_argument(
        "--config", type=str, default=None,
        help="Path to config.yaml (default: evals/config.yaml)"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show detailed grading output"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List available skills and exit"
    )
    parser.add_argument(
        "--save", action="store_true",
        help="Save results to evals/results/"
    )
    parser.add_argument(
        "--runs", type=int, default=1,
        help="Number of runs per skill for statistical significance (default: 1)"
    )
    parser.add_argument(
        "--parallel", "-p", action="store_true",
        help="Run eval cases in parallel within each skill"
    )
    parser.add_argument(
        "--triggering", action="store_true",
        help="Run triggering evals (description routing accuracy)"
    )
    parser.add_argument(
        "--model", type=str, default=None,
        help="Override generation model (e.g. us.anthropic.claude-sonnet-4-6-v1)"
    )
    parser.add_argument(
        "--grading-model", type=str, default=None,
        help="Override grading model (e.g. us.anthropic.claude-sonnet-4-6-v1)"
    )
    args = parser.parse_args()

    if args.list:
        print("Available skills with evals:")
        for s in list_skills():
            print(f"  - {s}")
        sys.exit(0)

    config_path = Path(args.config) if args.config else CONFIG_PATH
    config = load_config(config_path)

    if args.model:
        config["generation_model"] = args.model
    if args.grading_model:
        config["grading_model"] = args.grading_model

    if args.triggering:
        run_triggering_evals(config, skill_name=args.skill, verbose=args.verbose)
        sys.exit(0)

    skills_to_run = [args.skill] if args.skill else list_skills()

    # Validate skills exist
    for skill_name in skills_to_run:
        if skill_name not in list_skills():
            print(f"Error: skill '{skill_name}' not found or has no evals.")
            print(f"Available: {', '.join(list_skills())}")
            sys.exit(1)

    num_runs = args.runs

    if num_runs > 1:
        print(f"\n  Running {num_runs} iterations for statistical significance...\n")

    all_run_results = []
    for run_idx in range(num_runs):
        if num_runs > 1:
            print(f"\n{'#'*60}")
            print(f"  RUN {run_idx + 1} of {num_runs}")
            print(f"{'#'*60}")

        run_results = []
        for skill_name in skills_to_run:
            result = run_skill_evals(config, skill_name, verbose=args.verbose, parallel=args.parallel)
            run_results.append(result)

        all_run_results.append(run_results)

    # Aggregate across runs
    if num_runs == 1:
        final_results = all_run_results[0]
    else:
        final_results = []
        for skill_idx, skill_name in enumerate(skills_to_run):
            baselines = [all_run_results[r][skill_idx]["aggregate"]["baseline_avg"] for r in range(num_runs)]
            skills = [all_run_results[r][skill_idx]["aggregate"]["skill_avg"] for r in range(num_runs)]

            avg_baseline = sum(baselines) / len(baselines)
            avg_skill = sum(skills) / len(skills)

            final_results.append({
                "skill_name": skill_name,
                "cases": all_run_results[-1][skill_idx]["cases"],
                "aggregate": {
                    "baseline_avg": avg_baseline,
                    "skill_avg": avg_skill,
                    "delta": avg_skill - avg_baseline,
                },
                "runs": num_runs,
                "per_run_baseline": baselines,
                "per_run_skill": skills,
            })

        print(f"\n\n  Per-run breakdown:")
        for result in final_results:
            print(f"\n  {result['skill_name']}:")
            for i, (b, s) in enumerate(zip(result["per_run_baseline"], result["per_run_skill"])):
                print(f"    Run {i+1}: baseline={b:.0%}  skill={s:.0%}  delta={s-b:+.0%}")

    print_report(final_results)

    if args.save:
        save_results(final_results)


if __name__ == "__main__":
    main()
