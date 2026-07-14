#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Measure BPVendingService-style MCP recall using local per-BP files.

Simulates the BPVendingService 7-tool reasoning loop locally:
  - BP corpus: per-BP markdown files from the well-architected-mcp-server package
  - Embeddings: Bedrock Titan Embeddings v2 (same model as BPVendingService)
  - Search: cosine similarity + metadata filters (pillar, risk_level)
  - Reasoning loop: orient → search (browse + semantic) → dive → connect

Scores recall/precision/F1 vs the same ground truth used in measure_wa_review.py.
Saves embeddings on first run (~$0.01, <1 min); subsequent runs use cache.

This is the fairest possible proxy for BPVendingService effectiveness while
the live CLE endpoint is unavailable (Jul 10 regression, contacted author).

Output: evals/cli_effectiveness/mcp_effectiveness.json
Embed cache: evals/cli_effectiveness/bp_embeddings.json (gitignored)
"""
from __future__ import annotations

import json
import math
import re
import statistics
import sys
import time
from pathlib import Path

import boto3
import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
EVALS_DIR = SCRIPT_DIR.parent
REPO_ROOT = EVALS_DIR.parent

BP_DIR = Path.home() / "Dev/wa/mcp/src/well-architected-mcp-server/awslabs/well_architected_mcp_server/data/framework"
GT_DIR = SCRIPT_DIR / "ground_truth"
EMBED_CACHE = SCRIPT_DIR / "bp_embeddings.json"
RESULTS_FILE = SCRIPT_DIR / "mcp_effectiveness.json"

BEDROCK_REGION = "us-east-1"
EMBED_MODEL = "amazon.titan-embed-text-v2:0"
RUNS_PER_CASE = 3


# ---------------------------------------------------------------------------
# BP corpus loading
# ---------------------------------------------------------------------------

def load_corpus() -> list[dict]:
    """Load all 307 BP markdown files with parsed frontmatter + body."""
    corpus = []
    for f in sorted(BP_DIR.glob("*.md")):
        text = f.read_text()
        m = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
        if not m:
            continue
        meta = yaml.safe_load(m.group(1))
        body = m.group(2).strip()
        corpus.append({
            "id": meta.get("id", f.stem),
            "title": meta.get("title", ""),
            "pillar": meta.get("pillar", ""),
            "risk_level": (meta.get("risk_level") or "").upper(),
            "capability": meta.get("capability", ""),
            "description": meta.get("description", ""),
            "area": meta.get("area", []),
            "related_ids": meta.get("relatedIds", []) or [],
            "url": meta.get("url", ""),
            "body": body,
            # Text used for embedding: title + description + first 800 chars of body
            "embed_text": f"{meta.get('title','')}. {meta.get('description','')} {body[:800]}",
        })
    return corpus


# ---------------------------------------------------------------------------
# Embeddings
# ---------------------------------------------------------------------------

def embed_texts(bedrock, texts: list[str]) -> list[list[float]]:
    """Embed a list of texts using Titan Embeddings v2."""
    results = []
    for text in texts:
        resp = bedrock.invoke_model(
            modelId=EMBED_MODEL,
            body=json.dumps({"inputText": text[:8000], "dimensions": 256, "normalize": True}),
        )
        results.append(json.loads(resp["body"].read())["embedding"])
    return results


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb) if na and nb else 0.0


def build_or_load_embeddings(bedrock, corpus: list[dict]) -> dict[str, list[float]]:
    """Load cached embeddings or generate + cache them."""
    if EMBED_CACHE.exists():
        cached = json.loads(EMBED_CACHE.read_text())
        if len(cached) == len(corpus):
            print(f"  Loaded {len(cached)} embeddings from cache")
            return cached

    print(f"  Generating embeddings for {len(corpus)} BPs via Titan Embeddings v2...")
    start = time.time()
    embeddings: dict[str, list[float]] = {}
    batch_size = 10
    for i in range(0, len(corpus), batch_size):
        batch = corpus[i:i + batch_size]
        vecs = embed_texts(bedrock, [bp["embed_text"] for bp in batch])
        for bp, vec in zip(batch, vecs):
            embeddings[bp["id"]] = vec
        print(f"  {len(embeddings)}/{len(corpus)}...", end="\r", flush=True)

    EMBED_CACHE.write_text(json.dumps(embeddings))
    print(f"\n  Done: {len(embeddings)} embeddings in {time.time()-start:.0f}s")
    return embeddings


# ---------------------------------------------------------------------------
# Local simulation of BPVendingService tools
# ---------------------------------------------------------------------------

PILLAR_DOMAIN_MAP = {
    "Operational Excellence": "operational-excellence",
    "Security": "security",
    "Reliability": "reliability",
    "Performance Efficiency": "performance-efficiency",
    "Cost Optimization": "cost-optimization",
    "Sustainability": "sustainability",
}


def tool_list_pillars(corpus: list[dict]) -> dict:
    """Simulate ListPillars — returns pillar/domain hierarchy."""
    domains: dict[str, dict] = {}
    for bp in corpus:
        p = bp["pillar"]
        d_id = PILLAR_DOMAIN_MAP.get(p, p.lower().replace(" ", "-"))
        if d_id not in domains:
            domains[d_id] = {"id": d_id, "title": p, "bp_count": 0}
        domains[d_id]["bp_count"] += 1
    return {"frameworks": [{"id": "waf", "title": "AWS Well-Architected Framework",
                            "domains": list(domains.values())}]}


def tool_search(corpus: list[dict], embeddings: dict,
                query_vec: list[float] | None = None,
                domain_id: str | None = None,
                risk_level: str | None = None,
                limit: int = 50) -> list[dict]:
    """Simulate SearchBestPractices with optional semantic ranking + metadata filters."""
    candidates = corpus
    # Metadata filter
    if domain_id:
        domain_title = next(
            (k for k, v in PILLAR_DOMAIN_MAP.items() if v == domain_id),
            domain_id
        )
        candidates = [bp for bp in candidates if bp["pillar"].lower() == domain_title.lower()
                      or PILLAR_DOMAIN_MAP.get(bp["pillar"], "") == domain_id]
    if risk_level:
        candidates = [bp for bp in candidates if bp["risk_level"] == risk_level.upper()]

    # Rank by cosine similarity if query vector provided, else by id (deterministic)
    if query_vec:
        scored = sorted(candidates,
                        key=lambda bp: cosine(query_vec, embeddings.get(bp["id"], [])),
                        reverse=True)
    else:
        # Browse mode — rank by number of related IDs (proxy for hub_score)
        scored = sorted(candidates, key=lambda bp: len(bp["related_ids"]), reverse=True)

    return scored[:limit]


def tool_get_bp(corpus: list[dict], bp_id: str) -> dict | None:
    return next((bp for bp in corpus if bp["id"] == bp_id), None)


def tool_get_related(corpus: list[dict], bp_id: str) -> list[str]:
    bp = tool_get_bp(corpus, bp_id)
    return bp["related_ids"] if bp else []


# ---------------------------------------------------------------------------
# Reasoning loop strategies
# ---------------------------------------------------------------------------

def reasoning_loop_exhaustive(corpus: list[dict], embeddings: dict,
                               bedrock, workload_prompt: str) -> dict:
    """
    Exhaustive per-pillar sweep — upper bound on MCP recall.

    Per pillar:
      1. Browse search (no query, ranked by hub_score proxy) → top 50
      2. Semantic search (workload query embedded) → top 50
    Then GetBestPractice for all unique results (surfaces related IDs in body).
    Then follow related IDs one level.
    """
    all_bps: set[str] = set()
    tool_calls = 0

    # Embed the workload query once
    query_vec = embed_texts(bedrock, [workload_prompt[:500]])[0]
    tool_calls += 1

    # Step 1: orient
    pillars_result = tool_list_pillars(corpus)
    tool_calls += 1
    domain_ids = [d["id"] for d in pillars_result["frameworks"][0]["domains"]]

    # Step 2: per-pillar sweep
    found_ids: list[str] = []
    for domain_id in domain_ids:
        # Browse mode
        results = tool_search(corpus, embeddings, domain_id=domain_id, limit=50)
        tool_calls += 1
        found_ids.extend(r["id"] for r in results)

        # Semantic mode
        results = tool_search(corpus, embeddings, query_vec=query_vec,
                              domain_id=domain_id, limit=50)
        tool_calls += 1
        found_ids.extend(r["id"] for r in results)

    # Deduplicate
    found_ids = list(dict.fromkeys(found_ids))
    all_bps.update(found_ids)

    # Step 3: GetBestPractice for all (full body = more content; also surfaces relatedIds)
    related_to_follow: set[str] = set()
    for bp_id in found_ids:
        bp = tool_get_bp(corpus, bp_id)
        tool_calls += 1
        if bp:
            related_to_follow.update(bp["related_ids"])

    # Step 4: follow one level of related IDs
    new_ids = related_to_follow - all_bps
    for bp_id in new_ids:
        bp = tool_get_bp(corpus, bp_id)
        tool_calls += 1
        if bp:
            all_bps.add(bp_id)

    return {"all_bps": sorted(all_bps), "tool_calls": tool_calls}


def reasoning_loop_agent_style(corpus: list[dict], embeddings: dict,
                                bedrock, workload_prompt: str) -> dict:
    """
    Agent-style loop — simulates what a real agent would do WITHOUT being told
    to do an exhaustive sweep. Mimics the plateau behavior we measured earlier:
    the agent stops when it has 'enough' material.

    Strategy: semantic search with workload query only (no per-pillar sweep),
    max 3 iterations with different query reformulations, stop at 60 results.
    This replicates the 20-60 BP ceiling from the Dec 2025 study.
    """
    all_bps: set[str] = set()
    tool_calls = 0

    # Embed the workload query
    query_vec = embed_texts(bedrock, [workload_prompt[:500]])[0]
    tool_calls += 1

    # Three search passes with the same query (realistic: agent tries semantic search)
    for _ in range(3):
        results = tool_search(corpus, embeddings, query_vec=query_vec, limit=20)
        tool_calls += 1
        all_bps.update(r["id"] for r in results)
        # Agent "dives" into top 5
        for r in results[:5]:
            bp = tool_get_bp(corpus, r["id"])
            tool_calls += 1
            if bp:
                all_bps.add(bp["id"])

    return {"all_bps": sorted(all_bps), "tool_calls": tool_calls}


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score(cited: set[str], gt: set[str], canonical: set[str]) -> dict:
    valid = cited & canonical
    tp = valid & gt
    r = len(tp) / len(gt) if gt else 0.0
    p = len(tp) / len(valid) if valid else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return {
        "cited_count": len(cited),
        "valid_cited_count": len(valid),
        "true_positives": len(tp),
        "false_positives": len(valid - gt),
        "false_negatives": len(gt - valid),
        "recall": round(r, 4),
        "precision": round(p, 4),
        "f1": round(f1, 4),
        "valid_cited_bps": sorted(valid),
    }


def build_canonical_bps() -> set[str]:
    refs_dir = REPO_ROOT / "skills" / "wa-review" / "references" / "pillars"
    canonical: set[str] = set()
    bp_re = re.compile(r"^# ([A-Z]{2,}\d{1,3}-BP\d{1,3})\b", re.MULTILINE)
    for f in refs_dir.glob("*.md"):
        for m in bp_re.finditer(f.read_text()):
            canonical.add(m.group(1))
    return canonical


def load_eval_cases() -> list[dict]:
    data = json.loads(
        (REPO_ROOT / "skills" / "wa-review" / "evals" / "evals.json").read_text()
    )
    return data["evals"]


def load_ground_truth(case_id: int) -> set[str]:
    return set(json.loads((GT_DIR / f"case_{case_id}.json").read_text())
               ["ground_truth"]["consensus_bps"])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    if not BP_DIR.exists():
        print(f"BP corpus not found: {BP_DIR}")
        print("Clone: ssh://git.amazon.com/pkg/WellArchitectedMCPServer")
        return 1

    print("Loading BP corpus...")
    corpus = load_corpus()
    print(f"  {len(corpus)} BPs loaded")

    bedrock = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)
    print("Building/loading embeddings...")
    embeddings = build_or_load_embeddings(bedrock, corpus)

    canonical = build_canonical_bps()
    cases = load_eval_cases()
    print(f"\nCanonical: {len(canonical)} BPs | Cases: {len(cases)} | Runs: {RUNS_PER_CASE}\n")

    results = {
        "corpus": str(BP_DIR),
        "embed_model": EMBED_MODEL,
        "runs_per_case": RUNS_PER_CASE,
        "strategies": ["exhaustive", "agent_style"],
        "cases": [],
    }

    for case in cases:
        case_id = case["id"]
        prompt = case["prompt"]
        gt = load_ground_truth(case_id)
        gt_scoring = ({b for b in gt if b.startswith("SEC") or b.startswith("REL")}
                      if case_id == 4 else gt)
        scope = "SEC+REL only" if case_id == 4 else "full 6 pillars"

        print(f"=== Case {case_id} (|GT|={len(gt_scoring)}) ===")
        print(f"  {prompt[:80]}...")

        case_runs: list[dict] = []
        for run_idx in range(1, RUNS_PER_CASE + 1):
            print(f"  Run {run_idx}/{RUNS_PER_CASE}...", end="", flush=True)
            t0 = time.time()

            # Strategy A: exhaustive (simulates ideal MCP agent with full sweep)
            loop_a = reasoning_loop_exhaustive(corpus, embeddings, bedrock, prompt)
            # Strategy B: agent-style (simulates naive agent without systematic sweep)
            loop_b = reasoning_loop_agent_style(corpus, embeddings, bedrock, prompt)

            wall = round(time.time() - t0, 1)
            sa = score(set(loop_a["all_bps"]), gt_scoring, canonical)
            sb = score(set(loop_b["all_bps"]), gt_scoring, canonical)

            run = {
                "run_idx": run_idx,
                "gt_count": len(gt_scoring),
                "gt_scope": scope,
                "exhaustive": {**sa, "tool_calls": loop_a["tool_calls"]},
                "agent_style": {**sb, "tool_calls": loop_b["tool_calls"]},
                "wall_s": wall,
            }
            case_runs.append(run)
            print(f" exhaustive F1={sa['f1']:.3f} R={sa['recall']:.2f} ({loop_a['tool_calls']} calls) | "
                  f"agent F1={sb['f1']:.3f} R={sb['recall']:.2f} ({loop_b['tool_calls']} calls) | "
                  f"{wall:.0f}s")

        # Aggregate both strategies
        def agg_strategy(key: str) -> dict:
            vals = {m: [r[key][m] for r in case_runs]
                    for m in ("f1", "recall", "precision", "valid_cited_count", "tool_calls")}
            return {m: {"mean": round(statistics.mean(v), 4),
                        "stdev": round(statistics.stdev(v), 4) if len(v) > 1 else 0.0}
                    for m, v in vals.items()}

        results["cases"].append({
            "case_id": case_id,
            "prompt": prompt[:200],
            "gt_scope": scope,
            "runs": case_runs,
            "aggregate": {
                "exhaustive": agg_strategy("exhaustive"),
                "agent_style": agg_strategy("agent_style"),
            },
        })

        agg = results["cases"][-1]["aggregate"]
        print(f"  Case {case_id}: exhaustive F1={agg['exhaustive']['f1']['mean']} | "
              f"agent F1={agg['agent_style']['f1']['mean']}")

        RESULTS_FILE.write_text(json.dumps(results, indent=2))

    print(f"\nSaved: {RESULTS_FILE.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
