#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
Crawl AWS Well-Architected Framework public documentation and produce
per-question reference files for the wa-review skill.

Architecture:
    AWS docs publish a toc-contents.json manifest alongside each pillar/lens
    documentation set. This JSON contains the full page tree with titles and
    relative hrefs. We parse this tree to discover all Best Practice (BP) pages,
    then fetch each page's HTML, extract the main content area, convert it to
    clean markdown, and group all BPs belonging to the same WA question into a
    single consolidated file.

Three content modes are supported:
    1. BP-style (modern pillars + newer lenses like GenAI, Agentic AI, ML):
       TOC titles follow the pattern "{PREFIX}{NUM}-BP{NUM} Title".
       Output: one file per question, containing all BPs for that question.

    2. Dotted-BP-style (e.g. DevOps Guidance):
       TOC titles follow the bracketed dotted pattern "[AREA.SUB.N] Title".
       Output: one file per best practice, named by its ID (OA.LS.1 -> OALS01.md).

    3. Topic-page-style (older lenses like Serverless, Migration, Data Analytics):
       TOC has no BP-pattern titles. Instead, content is organized under
       pillar section headings with leaf pages containing guidance.
       Output: one file per pillar section, containing all pages for that section.

Output structure:
    skills/wa-review/references/pillars/{pillar-name}.md   (framework pillars, one per pillar)
    skills/wa-review/references/lenses/{lens-name}/*.md    (WA lenses, per-question)

Usage:
    uv run scripts/crawl-wa-framework.py [--output-dir DIR] [--delay SECS] [--pillar PILLAR] [--dry-run]
    uv run scripts/crawl-wa-framework.py --lens <URL> [--lens-name NAME] [--dry-run]

Examples:
    # Crawl all 6 framework pillars (produces 6 pillar-merged files)
    uv run scripts/crawl-wa-framework.py

    # Crawl only the security pillar
    uv run scripts/crawl-wa-framework.py --pillar security

    # Preview what pages would be fetched without actually fetching
    uv run scripts/crawl-wa-framework.py --pillar reliability --dry-run

    # Crawl a WA Lens (auto-detects BP-style vs topic-page-style)
    uv run scripts/crawl-wa-framework.py --lens https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html

    # Crawl a lens with a custom output name
    uv run scripts/crawl-wa-framework.py --lens https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html --lens-name genai
"""

import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_URL = "https://docs.aws.amazon.com"

# Each pillar has a dedicated documentation set with its own toc-contents.json.
# The "prefix" is the shorthand used in BP IDs (e.g., SEC03-BP01).
PILLAR_CONFIGS = {
    "operational-excellence": {
        "toc": f"{BASE_URL}/wellarchitected/latest/operational-excellence-pillar/toc-contents.json",
        "base": f"{BASE_URL}/wellarchitected/latest/operational-excellence-pillar",
        "prefix": "OPS",
    },
    "security": {
        "toc": f"{BASE_URL}/wellarchitected/latest/security-pillar/toc-contents.json",
        "base": f"{BASE_URL}/wellarchitected/latest/security-pillar",
        "prefix": "SEC",
    },
    "reliability": {
        "toc": f"{BASE_URL}/wellarchitected/latest/reliability-pillar/toc-contents.json",
        "base": f"{BASE_URL}/wellarchitected/latest/reliability-pillar",
        "prefix": "REL",
    },
    "performance-efficiency": {
        "toc": f"{BASE_URL}/wellarchitected/latest/performance-efficiency-pillar/toc-contents.json",
        "base": f"{BASE_URL}/wellarchitected/latest/performance-efficiency-pillar",
        "prefix": "PERF",
    },
    "cost-optimization": {
        "toc": f"{BASE_URL}/wellarchitected/latest/cost-optimization-pillar/toc-contents.json",
        "base": f"{BASE_URL}/wellarchitected/latest/cost-optimization-pillar",
        "prefix": "COST",
    },
    "sustainability": {
        "toc": f"{BASE_URL}/wellarchitected/latest/sustainability-pillar/toc-contents.json",
        "base": f"{BASE_URL}/wellarchitected/latest/sustainability-pillar",
        "prefix": "SUS",
    },
}

# Human-readable pillar names for output file headers.
PILLAR_DISPLAY = {
    "OPS": "Operational Excellence",
    "SEC": "Security",
    "REL": "Reliability",
    "PERF": "Performance Efficiency",
    "COST": "Cost Optimization",
    "SUS": "Sustainability",
}


def pillar_for_id(question_id: str) -> str | None:
    """
    Resolve the WA pillar for a question/BP ID, or None if it isn't organized
    by the 6 pillars. Framework IDs map directly (SEC03 -> Security); lens IDs
    embed the pillar as a trailing code in their prefix (MLCOST01 -> COST,
    AGENTSEC03 -> SEC, FSISEC01 -> SEC, GAMESOPS01 -> OPS). Lenses like
    responsible-ai (RAIBR/RAIMON) and DevOps (OA.LS) aren't pillar-based -> None.
    """
    prefix = re.match(r"[A-Z]+", question_id)
    if not prefix:
        return None
    prefix = prefix.group(0)
    if prefix in PILLAR_DISPLAY:
        return PILLAR_DISPLAY[prefix]
    code = next((c for c in ("OPS", "SEC", "REL", "PERF", "COST", "SUS")
                 if prefix.endswith(c)), None)
    return PILLAR_DISPLAY.get(code) if code else None

# Maps question IDs to their official WA Framework question text.
# Used as the H1 title in consolidated output files.
QUESTION_TITLES = {
    "OPS01": "OPS 1 — How do you determine what your priorities are?",
    "OPS02": "OPS 2 — How do you structure your organization to support your business outcomes?",
    "OPS03": "OPS 3 — How does your organizational culture support your business outcomes?",
    "OPS04": "OPS 4 — How do you implement observability in your workload?",
    "OPS05": "OPS 5 — How do you reduce defects, ease remediation, and improve flow into production?",
    "OPS06": "OPS 6 — How do you mitigate deployment risks?",
    "OPS07": "OPS 7 — How do you know that you are ready to support a workload?",
    "OPS08": "OPS 8 — How do you utilize workload observability in your organization?",
    "OPS09": "OPS 9 — How do you understand the health of your operations?",
    "OPS10": "OPS 10 — How do you manage workload and operations events?",
    "OPS11": "OPS 11 — How do you evolve operations?",
    "SEC01": "SEC 1 — How do you securely operate your workload?",
    "SEC02": "SEC 2 — How do you manage identities for people and machines?",
    "SEC03": "SEC 3 — How do you manage permissions for people and machines?",
    "SEC04": "SEC 4 — How do you detect and investigate security events?",
    "SEC05": "SEC 5 — How do you protect your network resources?",
    "SEC06": "SEC 6 — How do you protect your compute resources?",
    "SEC07": "SEC 7 — How do you classify your data?",
    "SEC08": "SEC 8 — How do you protect your data at rest?",
    "SEC09": "SEC 9 — How do you protect your data in transit?",
    "SEC10": "SEC 10 — How do you anticipate, respond to, and recover from incidents?",
    "SEC11": "SEC 11 — How do you incorporate and validate the security properties of applications?",
    "REL01": "REL 1 — How do you manage Service Quotas and constraints?",
    "REL02": "REL 2 — How do you plan your network topology?",
    "REL03": "REL 3 — How do you design your workload service architecture?",
    "REL04": "REL 4 — How do you design interactions in a distributed system to prevent failures?",
    "REL05": "REL 5 — How do you design interactions in a distributed system to mitigate or withstand failures?",
    "REL06": "REL 6 — How do you monitor workload resources?",
    "REL07": "REL 7 — How do you design your workload to adapt to changes in demand?",
    "REL08": "REL 8 — How do you implement change?",
    "REL09": "REL 9 — How do you back up data?",
    "REL10": "REL 10 — How do you use fault isolation to protect your workload?",
    "REL11": "REL 11 — How do you design your workload to withstand component failures?",
    "REL12": "REL 12 — How do you test reliability?",
    "REL13": "REL 13 — How do you plan for disaster recovery (DR)?",
    "PERF01": "PERF 1 — How do you select appropriate cloud resources and architecture patterns?",
    "PERF02": "PERF 2 — How do you select and use compute resources?",
    "PERF03": "PERF 3 — How do you store, manage, and access data?",
    "PERF04": "PERF 4 — How do you select and configure networking resources?",
    "PERF05": "PERF 5 — What process do you use to support more performance efficiency?",
    "COST01": "COST 1 — How do you implement cloud financial management?",
    "COST02": "COST 2 — How do you govern usage?",
    "COST03": "COST 3 — How do you monitor usage and cost?",
    "COST04": "COST 4 — How do you decommission resources?",
    "COST05": "COST 5 — How do you evaluate cost when you select services?",
    "COST06": "COST 6 — How do you meet cost targets when you select resource type, size and number?",
    "COST07": "COST 7 — How do you use pricing models to reduce cost?",
    "COST08": "COST 8 — How do you plan for data transfer charges?",
    "COST09": "COST 9 — How do you manage demand, and supply resources?",
    "COST10": "COST 10 — How do you evaluate new services?",
    "COST11": "COST 11 — How do you evaluate the cost of effort?",
    "SUS01": "SUS 1 — How do you select Regions for your workload?",
    "SUS02": "SUS 2 — How do you align cloud resources to your demand?",
    "SUS03": "SUS 3 — How do you take advantage of software and architecture patterns to support your sustainability goals?",
    "SUS04": "SUS 4 — How do you take advantage of data management policies and patterns?",
    "SUS05": "SUS 5 — How do you select and use cloud hardware and services to support your sustainability goals?",
    "SUS06": "SUS 6 — How do your organizational processes support your sustainability goals?",
}


# ---------------------------------------------------------------------------
# HTTP fetching
# ---------------------------------------------------------------------------


def fetch(url: str, retries: int = 3) -> str | None:
    """
    Fetch a URL and return its content as a string.

    Retries up to `retries` times with exponential backoff on network errors.
    Returns None if all attempts fail (logs the error to stderr).
    Uses a browser-like User-Agent to avoid being blocked by CloudFront.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WA-Skills-Crawler/1.0)"
    }
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
                return resp.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt < retries - 1:
                time.sleep(1 * (attempt + 1))
            else:
                print(f"    FAILED: {url}: {e}", file=sys.stderr)
                return None


# ---------------------------------------------------------------------------
# HTML to Markdown conversion
# ---------------------------------------------------------------------------


def decode_entities(text: str) -> str:
    """
    Decode common HTML entities (&amp;, &lt;, &gt;, &nbsp;, etc.) into their
    plain-text equivalents. Also strips any remaining numeric character references
    (&#123; or &#xAB;) that we don't explicitly handle.
    """
    for old, new in [("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                     ("&nbsp;", " "), ("&#39;", "'"), ("&quot;", '"'),
                     ("&#x27;", "'"), ("&#x2F;", "/")]:
        text = text.replace(old, new)
    return re.sub(r"&#x?[0-9a-fA-F]+;", "", text)


def strip_tags(html: str) -> str:
    """
    Remove ALL HTML tags from a string and decode entities.
    Used as a final cleanup pass after structured elements (headers, links, etc.)
    have already been converted to markdown syntax.
    """
    return decode_entities(re.sub(r"<[^>]+>", "", html))


def html_to_markdown(html: str) -> str:
    """
    Convert an HTML fragment into clean, readable markdown.

    Processing order matters — we handle structured elements (headers, links,
    bold, code, lists) first while tags are still parseable, then strip any
    remaining tags as a final pass.

    Steps:
    1. Remove non-content elements (scripts, styles, nav, AWS-specific components)
    2. Convert headers (h1-h4) to markdown heading syntax (# ## ### ####)
    3. Convert links to [text](url) format, resolving relative URLs
    4. Convert bold/italic to **text** / *text*
    5. Convert code/pre to `inline` and ```blocks```
    6. Convert lists (ul/ol/li) to markdown bullet points
    7. Convert paragraphs to double-newline separated text
    8. Strip any remaining HTML tags
    9. Normalize whitespace (collapse multiple blank lines, trim)
    """
    text = html

    # Step 1: Remove non-content elements that would pollute the output
    for tag in ["script", "style", "nav"]:
        text = re.sub(rf"<{tag}[^>]*>.*?</{tag}>", "", text, flags=re.DOTALL)
    # AWS docs use custom web components for copyright, feedback, etc.
    text = re.sub(r"<awsdocs-[^>]*>.*?</awsdocs-[^>]*>", "", text, flags=re.DOTALL)
    text = re.sub(r"<awsdocs-[^>]*/>", "", text)

    # Step 2: Convert HTML headings to markdown headings
    for level, tag in [(1, "h1"), (2, "h2"), (3, "h3"), (4, "h4")]:
        prefix = "#" * level
        text = re.sub(
            rf"<{tag}[^>]*>(.*?)</{tag}>",
            lambda m, p=prefix: f"\n{p} {strip_tags(m.group(1)).strip()}\n\n",
            text, flags=re.DOTALL,
        )

    # Step 3: Convert links — resolve relative URLs to absolute
    def fix_link(m):
        href, link_text = m.group(1), strip_tags(m.group(2)).strip()
        if not link_text:
            return ""
        if href.startswith("/"):
            href = f"{BASE_URL}{href}"
        return f"[{link_text}]({href})"

    text = re.sub(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', fix_link, text, flags=re.DOTALL)

    # Step 4: Convert bold and italic
    text = re.sub(r"<(?:b|strong)[^>]*>(.*?)</(?:b|strong)>",
                  lambda m: f"**{strip_tags(m.group(1)).strip()}**", text, flags=re.DOTALL)
    text = re.sub(r"<(?:i|em)[^>]*>(.*?)</(?:i|em)>",
                  lambda m: f"*{strip_tags(m.group(1)).strip()}*", text, flags=re.DOTALL)

    # Step 5: Convert code elements
    text = re.sub(r"<code[^>]*>(.*?)</code>",
                  lambda m: f"`{strip_tags(m.group(1)).strip()}`", text, flags=re.DOTALL)
    text = re.sub(r"<pre[^>]*>(.*?)</pre>",
                  lambda m: f"\n```\n{strip_tags(m.group(1)).strip()}\n```\n", text, flags=re.DOTALL)

    # Step 6: Convert lists — remove list wrappers, convert items to "- " bullets
    text = re.sub(r"<[ou]l[^>]*>", "\n", text)
    text = re.sub(r"</[ou]l>", "\n", text)
    text = re.sub(r"<li[^>]*>(.*?)</li>",
                  lambda m: f"- {strip_tags(m.group(1)).strip()}\n", text, flags=re.DOTALL)

    # Step 7: Convert paragraphs to newline-separated text
    text = re.sub(r"<p[^>]*>(.*?)</p>",
                  lambda m: f"\n{strip_tags(m.group(1)).strip()}\n", text, flags=re.DOTALL)

    # Step 8: Strip any remaining HTML tags we didn't handle above
    text = strip_tags(text)

    # Step 9: Normalize whitespace for clean readable output
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    lines = [line.strip() for line in text.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


# ---------------------------------------------------------------------------
# Content extraction
# ---------------------------------------------------------------------------


def extract_content(html: str) -> str:
    """
    Extract the main article content from a full AWS docs HTML page.

    AWS docs pages have a consistent structure: the article content starts
    at the first <h1> tag and ends before the <awsdocs-copyright>, <footer>,
    or <div id="footer"> element. Everything outside that range is navigation,
    breadcrumbs, or page chrome that we don't want.

    Returns the raw HTML substring between those boundaries (still needs
    html_to_markdown conversion).
    """
    h1 = re.search(r"<h1[^>]*>", html)
    if not h1:
        return ""
    start = h1.start()
    end_match = re.search(r"<awsdocs-copyright|<footer|<div id=\"footer\"", html[start:])
    end = start + end_match.start() if end_match else len(html)
    return html[start:end]


# ---------------------------------------------------------------------------
# TOC parsing — BP-style (modern format)
# ---------------------------------------------------------------------------


def discover_bp_pages(toc_json: dict) -> list[dict]:
    """
    Walk the toc-contents.json tree and find all Best Practice page entries.

    BP entries are identified by their title matching the pattern:
    "{PREFIX}{NUM}-BP{NUM} Human-readable title"
    e.g., "SEC03-BP01 Define access requirements"

    Returns a list of dicts with keys: bp_id, title, href, group.
    The bp_id (e.g., "SEC03-BP01") is extracted from the title prefix.
    The href is relative to the pillar/lens base URL.
    "group" is the human-readable title of the question branch the BP sits under
    (e.g. "Reasoning and execution cost optimization" for AGENTCOST01-BP01), or
    None. The caller can use it as the question heading — otherwise the question
    is only identifiable by its opaque ID (AGENTCOST01).
    """
    results = []

    def walk(contents, group=None):
        for item in contents:
            title = (item.get("title") or "").replace("\xa0", " ").strip()
            # Match titles that start with a BP ID pattern
            if "-BP" in title and "href" in item:
                bp_match = re.match(r"([A-Z]+\d+-BP\d+)", title)
                if bp_match:
                    results.append({
                        "bp_id": bp_match.group(1),
                        "title": title,
                        "href": item["href"],
                        "group": group,
                    })
            # Recurse into child nodes. A branch that is NOT itself a BP page
            # and whose children ARE BPs is the question group — record its
            # title as context for those BPs.
            if "contents" in item:
                child_group = group
                if "-BP" not in title and any(
                    "-BP" in (c.get("title") or "") for c in item["contents"]
                ):
                    child_group = title
                walk(item["contents"], child_group)

    walk(toc_json.get("contents", []))
    return results


def dotted_bp_filename(bp_id: str) -> str:
    """
    Convert a dotted BP ID to an ID-derived filename matching the convention
    used by other BP-style lenses (e.g. "AGENTCOST01.md"): drop the dots and
    zero-pad the trailing number to two digits.

    "OA.LS.1"  -> "OALS01.md"
    "QA.ST.4"  -> "QAST04.md"
    "AG.ACG.4" -> "AGACG04.md"
    """
    parts = bp_id.split(".")
    num = parts[-1].zfill(2)
    return "".join(parts[:-1]) + num + ".md"


def discover_dotted_bp_pages(toc_json: dict) -> list[dict]:
    """
    Walk the TOC tree and find Best Practice pages that use the dotted-ID
    format, e.g. "[OA.LS.1] Appoint a decision-making leader...".

    This is the convention used by AWS DevOps Guidance (and any lens whose
    capability areas are named "{AREA}.{SUBCATEGORY}.{NUM}"). It is distinct
    from the pillar "{PREFIX}{NUM}-BP{NUM}" format handled by
    discover_bp_pages(); without this, such lenses fall through to the
    topic-page fallback, which only reaches a small fraction of the pages.

    Returns a list of dicts with keys: bp_id (e.g. "OA.LS.1"),
    group_id (e.g. "OA.LS"), title, href, saga, capability.
    DevOps Guidance is organized as Sagas -> Capabilities -> best practices
    (not pillars/questions). "saga" (e.g. "Organizational adoption") and
    "capability" (e.g. "Leader sponsorship") are the human-readable names of
    those two grouping levels, captured so the output isn't reduced to the
    opaque code (OA.LS).
    """
    results = []
    # Titles look like "[OA.LS.1] Human-readable title". Some entries contain
    # non-breaking spaces, so normalize whitespace before matching.
    pattern = re.compile(r"^\[([A-Z]+\.[A-Z]+\.\d+)\]\s*(.*)", re.DOTALL)

    # Depth is measured from the saga wrapper's children:
    #   depth 0 = saga (e.g. "Organizational adoption")
    #   depth 1 = capability (e.g. "Leader sponsorship")
    #   deeper  = sub-pages / BP leaves
    def walk(contents, depth=0, saga=None, capability=None):
        for item in contents:
            title = (item.get("title") or "").replace("\xa0", " ").strip()
            match = pattern.match(title)
            if match and "href" in item:
                bp_id = match.group(1)
                results.append({
                    "bp_id": bp_id,
                    "group_id": ".".join(bp_id.split(".")[:2]),
                    "title": title,
                    "href": item["href"],
                    "saga": saga,
                    "capability": capability,
                })
            if "contents" in item:
                child_saga = title if depth == 0 else saga
                child_cap = title if depth == 1 else capability
                walk(item["contents"], depth + 1, child_saga, child_cap)

    # Enter at the "The DevOps Sagas" wrapper if present so its children (the
    # sagas) start at depth 0; otherwise walk from the root.
    root = toc_json.get("contents", [])
    saga_wrapper = next((it for it in root if (it.get("title") or "").strip() == "The DevOps Sagas"), None)
    walk(saga_wrapper["contents"] if saga_wrapper else root)
    return results


# ---------------------------------------------------------------------------
# TOC parsing — Topic-page-style (older lenses)
# ---------------------------------------------------------------------------


# Generic per-pillar scaffolding pages that mirror the core WA Framework and add
# no lens-specific guidance the LLM doesn't already know. They appear as depth-1
# children of a pillar in flat-TOC lenses (e.g. IoT); excluded from capture so we
# keep the pillar's real best-practice pages without the boilerplate.
_GENERIC_PILLAR_PAGES = {
    "definitions", "design principles", "key aws services", "resources",
}


def discover_leaf_pages(toc_json: dict, pillar_sections: list[str] | None = None) -> list[dict]:
    """
    Walk the TOC tree for older-format lenses that don't use BP-style naming.

    These lenses organize content under pillar section headings (e.g.,
    "Operational excellence", "Security") with leaf pages containing the
    actual guidance. This function finds all leaf pages (pages with no
    children) that live under a recognized pillar section heading.

    A page qualifies if it is a leaf (no "contents") whose section resolves to
    a known pillar name, AND either:
    - it's nested at depth >= 2 (a leaf under a pillar section — the common case), or
    - the leaf IS the pillar node itself (a pillar expressed as a single content
      page with no child best practices, e.g. the serverless lens's
      "Sustainability" at depth 1).

    Returns a list of dicts with keys: section, title, href.
    """
    results = []
    # Pillar names we want as section buckets. The generic "Pillars of the
    # Well-Architected Framework" wrapper is intentionally NOT here — it's a
    # container above the real pillars, not a bucket itself.
    pillar_names = pillar_sections or [
        "Operational excellence", "Security", "Reliability",
        "Performance efficiency", "Cost optimization", "Sustainability",
    ]

    def matches_pillar(title):
        tl = title.lower()
        return next((p for p in pillar_names if p.lower() in tl), None)

    # A numbered-question branch title, e.g. "1 – Monitor the health..." or
    # "11 – Choose cost-effective compute and storage...". These sit between a
    # pillar and its best-practice leaves in some lenses (Data Analytics, SAP)
    # and group the BPs by the question they answer. We record the title so the
    # writer can emit it as a heading — generic wrappers like "Best practices"
    # (not numbered) are ignored.
    numbered_question = re.compile(r"^\d+\s*[–-]\s+")

    def walk(contents, section=None, depth=0, parent=None):
        for item in contents:
            title = item.get("title", "")
            href = item.get("href", "")

            # Adopt a pillar name as the section bucket, but only the FIRST
            # (shallowest) pillar match wins — so a deeper numbered question
            # that repeats a pillar keyword (e.g. the analytics lens's
            # "15 - Sustainability implementation guidance" under the
            # "Sustainability" pillar) can't overwrite the clean pillar name.
            matched = matches_pillar(title)
            if matched and section is None:
                current_section = matched
            else:
                current_section = section

            if "contents" in item:
                # Track a numbered-question branch (below the pillar) as the
                # parent context for the best-practice leaves beneath it.
                child_parent = parent
                if section and not matched and numbered_question.match(title.replace("\xa0", " ").strip()):
                    child_parent = title.replace("\xa0", " ").strip()
                walk(item["contents"], current_section, depth + 1, child_parent)
            elif current_section and href and (depth >= 2 or matched or (
                    # Some lenses (e.g. IoT) place per-topic best-practice pages
                    # directly under the pillar at depth 1 rather than nesting them
                    # under a sub-branch. Capture those too — but skip the generic
                    # framework scaffolding pages the LLM already knows, which also
                    # live at depth 1 (Definitions / Design principles / Key AWS
                    # services / Resources). Without this, whole pillars of a
                    # flat-TOC lens are silently dropped.
                    depth == 1
                    and title.replace("\xa0", " ").strip().rstrip(".").lower()
                    not in _GENERIC_PILLAR_PAGES)):
                # Capture this leaf when either:
                #  - it sits under a pillar section (depth >= 2), the common case; or
                #  - the leaf IS the pillar (matched): some lenses express a whole
                #    pillar as a single content page with no child best practices
                #    (e.g. the serverless lens's "Sustainability" at depth 1); or
                #  - it's a depth-1 per-topic page under a pillar (IoT-style flat
                #    TOC), excluding the generic scaffolding pages above.
                #    Without this, that pillar's content is silently dropped.
                #
                # qid: some lenses (e.g. Financial Services) give each leaf a
                # question ID like "FSISEC01: ...". When present, the caller can
                # write one file per question instead of one per pillar. None for
                # lenses without per-question IDs (serverless, migration, etc.).
                # Normalize the question ID's trailing number to two digits so
                # filenames sort and look consistent — AWS source titles mix
                # padded and unpadded forms (e.g. "FSIOPS01:" and "FSIOPS2:").
                qid_match = re.match(r"^([A-Z]{2,})0*(\d+)\s*:", title)
                qid = f"{qid_match.group(1)}{int(qid_match.group(2)):02d}" if qid_match else None
                results.append({
                    "section": current_section,
                    "title": title,
                    "href": href,
                    "qid": qid,
                    # Numbered-question title (e.g. "11 – Choose cost-effective
                    # compute...") this BP answers, or None if no numbered parent.
                    "parent": parent,
                })

    walk(toc_json.get("contents", []))
    return results


# A best-practice heading embedded in a topic-page body, e.g.
# "## IOTSEC01-BP01 Assign unique identities to each IoT device". Some lenses
# (IoT) are really BP-style but don't expose each BP as its own TOC page — the
# BPs live as headings inside the pillar's focus-area pages. This matches such a
# heading and captures the BP ID so the body can be split into per-question files.
# Note: no trailing \b — some source headings omit the space between the BP ID
# and its title (e.g. "## IOTREL07-BP02Implement storage redundancy..."), and a
# \b there would fail to match, merging that BP into the previous block.
_EMBEDDED_BP_HEADING = re.compile(r"^#{1,6}\s+([A-Z]{2,}\d+-BP\d+)", re.M)


def split_embedded_bps(section_pages: dict) -> dict | None:
    """
    Detect and split topic-page bodies that embed BP-ID headings into a
    per-question structure compatible with write_output().

    Some lenses (e.g. IoT) have a flat TOC whose leaf pages are pillar
    "focus areas" (Identity and access management, Detective controls, ...),
    but the real best practices are ``## IOTSEC01-BP01 ...`` headings *inside*
    those page bodies rather than separate TOC pages. This slices each focus-area
    body at its BP headings, groups the resulting blocks by question ID
    (IOTSEC02-BP01/02/03 -> IOTSEC02), and returns a dict shaped like the
    ``{question_id: [bp, ...]}`` that write_output() consumes.

    Returns None when no page body contains an embedded BP heading — so every
    existing topic-page lens (serverless, migration, saas, connected-mobility,
    government, ...) skips this path entirely and stays byte-identical.

    Also returns None when the pages already carry per-question IDs (qid): lenses
    like Financial Services expose one page PER QUESTION (title "FSISEC01: ...")
    while also embedding "## FSISEC01-BP01" headings in the body. Those already
    have a clean per-question structure via the qid writer, so this split must
    not intercept them. Only flat-TOC lenses whose BPs live purely inside
    focus-area pages with no page-level qid (IoT, HPC) should be split here.
    """
    # Don't intercept lenses that already have per-question (qid) pages.
    if any(p.get("qid") for pages in section_pages.values() for p in pages):
        return None
    # Only engage when embedded BP headings are actually present.
    if not any(_EMBEDDED_BP_HEADING.search(p["content"]) for pages in section_pages.values() for p in pages):
        return None

    questions = defaultdict(list)
    for section, pages in section_pages.items():
        for page in pages:
            content = page["content"]
            # Find every embedded BP heading and its position, then carve the
            # body into [heading, next-heading) blocks — one block per BP.
            matches = list(_EMBEDDED_BP_HEADING.finditer(content))
            if not matches:
                continue
            for idx, m in enumerate(matches):
                bp_id = m.group(1)
                start = m.start()
                end = matches[idx + 1].start() if idx + 1 < len(matches) else len(content)
                block = content[start:end].strip()
                question_id = bp_id.split("-BP")[0]
                questions[question_id].append({
                    "bp_id": bp_id,
                    "title": bp_id,
                    "content": block,
                    "url": page["url"],
                    # The focus-area section (e.g. "Identity and access
                    # management") is the group context for this question.
                    "group": section,
                })
    return dict(questions)


# ---------------------------------------------------------------------------
# Pillar crawling (framework mode)
# ---------------------------------------------------------------------------


def crawl_pillar(pillar_name: str, config: dict, delay: float, dry_run: bool) -> dict[str, list[dict]]:
    """
    Crawl a single WA Framework pillar and return all BPs grouped by question.

    Workflow:
    1. Fetch the pillar's toc-contents.json manifest
    2. Parse the TOC to discover all BP page entries
    3. Fetch each BP page HTML with a polite delay between requests
    4. Extract the article content and convert to markdown
    5. Group BPs by their parent question ID (e.g., SEC03-BP01 -> SEC03)

    Returns:
        Dict mapping question_id -> list of BP dicts (bp_id, title, content, url).
        Empty dict if dry_run=True (only prints discovered pages).
    """
    prefix = config["prefix"]
    base_url = config["base"]
    toc_url = config["toc"]

    print(f"\n{'='*60}")
    print(f"  Pillar: {pillar_name} ({prefix})")
    print(f"{'='*60}")

    # Step 1: Fetch the TOC manifest — this is a lightweight JSON file that
    # contains the entire page tree for this pillar's documentation
    toc_raw = fetch(toc_url)
    if not toc_raw:
        print(f"  ERROR: Could not fetch TOC for {pillar_name}")
        return {}

    # Step 2: Parse the TOC tree to find all BP-pattern entries
    toc_data = json.loads(toc_raw)
    bp_pages = discover_bp_pages(toc_data)
    print(f"  Found {len(bp_pages)} best practice pages in TOC")

    if dry_run:
        for bp in bp_pages[:10]:
            print(f"    {bp['bp_id']}: {bp['href']}")
        if len(bp_pages) > 10:
            print(f"    ... and {len(bp_pages) - 10} more")
        return {}

    # Step 3-5: Fetch each BP page, extract content, group by question
    question_bps = defaultdict(list)
    for i, bp in enumerate(bp_pages):
        # Polite delay to avoid overwhelming the docs server
        time.sleep(delay)
        url = f"{base_url}/{bp['href']}"
        print(f"  [{i+1}/{len(bp_pages)}] {bp['bp_id']}...", end=" ", flush=True)

        # Fetch the full HTML page
        html = fetch(url)
        if not html:
            print("SKIP")
            continue

        # Extract just the article content (between h1 and footer)
        content_html = extract_content(html)
        if not content_html:
            print("NO_CONTENT")
            continue

        # Convert HTML to clean markdown
        md = html_to_markdown(content_html)
        if len(md) < 50:
            print("TOO_SHORT")
            continue

        # Group by question: "SEC03-BP01" -> question "SEC03"
        question_id = bp["bp_id"].split("-BP")[0]
        question_bps[question_id].append({
            "bp_id": bp["bp_id"],
            "title": bp["title"],
            "content": md,
            "url": url,
            "group": bp.get("group"),
        })
        print("OK")

    print(f"  Done: {sum(len(v) for v in question_bps.values())} BPs across {len(question_bps)} questions")
    return dict(question_bps)


# ---------------------------------------------------------------------------
# Output writing
# ---------------------------------------------------------------------------


def _question_block(question_id: str, bps: list[dict]) -> str:
    """Build a markdown block for a single WA question (H1 title + all BPs)."""
    group = next((b.get("group") for b in bps if b.get("group")), None)
    if question_id in QUESTION_TITLES:
        title = QUESTION_TITLES[question_id]
    elif group:
        title = f"{question_id} — {group}"
    else:
        title = question_id
    pillar = pillar_for_id(question_id)

    lines = [f"# {title}", ""]
    if pillar:
        lines.append(f"**Pillar**: {pillar}  ")
    lines += [
        f"**Best Practices**: {len(bps)}",
        "",
        "---",
        "",
    ]
    for bp in sorted(bps, key=lambda b: b["bp_id"]):
        lines.append(bp["content"])
        lines.append("")
        lines.append(f"*Source: {bp['url']}*")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def write_output_per_question(all_questions: dict[str, list[dict]], output_dir: Path) -> int:
    """Per-question output — used by lenses (each question stays in its own file)."""
    output_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for question_id in sorted(all_questions.keys()):
        bps = all_questions[question_id]
        if not bps:
            continue
        content = _question_block(question_id, bps)
        (output_dir / f"{question_id}.md").write_text(content, encoding="utf-8")
        written += 1
    return written


# Pillar names, prefixes, and expected question counts — used for pillar-merged output.
PILLAR_MERGED_ORDER = [
    ("operational-excellence", "OPS", 11),
    ("security",              "SEC", 11),
    ("reliability",           "REL", 13),
    ("performance-efficiency","PERF", 5),
    ("cost-optimization",     "COST", 11),
    ("sustainability",        "SUS",  6),
]


def write_output_pillar_merged(all_questions: dict[str, list[dict]], output_dir: Path) -> int:
    """Pillar-merged output — one file per pillar containing all its questions.

    Used for the 6 WA Framework pillars. The v4.2+ SKILL.md dispatches one
    Task subagent per pillar and each subagent loads exactly one of these
    files, so grouping by pillar matches how the skill consumes the data.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    written = 0

    for pillar_name, prefix, count in PILLAR_MERGED_ORDER:
        pillar_qids = sorted(qid for qid in all_questions
                             if re.match(rf"^{prefix}\d+$", qid) and all_questions[qid])
        if not pillar_qids:
            continue

        parts = [
            f"# {pillar_name.replace('-', ' ').title()} — All Questions & Best Practices",
            "",
            f"This file contains all {len(pillar_qids)} WA Framework questions for the "
            f"{pillar_name} pillar and their complete best-practice content. Load this ONE "
            f"file to have the entire pillar in context at once.",
            "",
            "For a lightweight catalog of every BP ID across all 6 pillars, see "
            "`references/manifest.md`.",
            "",
            "---",
            "",
        ]
        for qid in pillar_qids:
            parts.append(f"## Question {qid}")
            parts.append("")
            parts.append(_question_block(qid, all_questions[qid]).strip())
            parts.append("")
            parts.append("---")
            parts.append("")

        out_file = output_dir / f"{pillar_name}.md"
        out_file.write_text("\n".join(parts), encoding="utf-8")
        size_kb = out_file.stat().st_size / 1024
        print(f"  {pillar_name:<25s} → {size_kb:>7.1f} KB ({len(pillar_qids)} questions)")
        written += 1

    return written


# ---------------------------------------------------------------------------
# Lens crawling (handles both BP-style and topic-page-style)
# ---------------------------------------------------------------------------


def crawl_lens(lens_url: str, lens_name: str, output_dir: Path, delay: float, dry_run: bool):
    """
    Crawl a WA Lens and produce reference files.

    Lenses use the same toc-contents.json pattern as pillars. This function
    auto-detects the content format (the three modes are mutually exclusive —
    a title matches at most one pattern):

    - Dotted-BP-style: TOC has bracketed dotted IDs (e.g. "[OA.LS.1] ...", DevOps
      Guidance). One file per best practice, named by ID (OA.LS.1 -> OALS01.md).

    - BP-style: TOC has "{PREFIX}{NUM}-BP{NUM}" entries (e.g. "GENSEC01-BP01").
      Same crawling as pillars: group by question, one file per question.

    - Topic-page-style: no BP-pattern titles (older lenses like Serverless,
      Migration, Data Analytics). Finds leaf pages under pillar section headings,
      groups them by section, and writes one file per section.

    The lens URL can point to any page in the lens docs (welcome.html, the lens
    main page, etc.) — the script derives the base URL and toc-contents.json path
    from it.
    """
    # Derive the docs base URL by stripping the filename from the lens URL.
    # e.g., ".../serverless-applications-lens/welcome.html" -> ".../serverless-applications-lens"
    base_url = lens_url.rsplit("/", 1)[0]
    toc_url = f"{base_url}/toc-contents.json"

    print(f"\n{'='*60}")
    print(f"  Lens: {lens_name}")
    print(f"  TOC: {toc_url}")
    print(f"{'='*60}")

    toc_raw = fetch(toc_url)
    if not toc_raw:
        print(f"  ERROR: Could not fetch TOC")
        return

    toc_data = json.loads(toc_raw)

    # Auto-detect: try BP-style first (modern lenses)
    bp_pages = discover_bp_pages(toc_data)
    dotted_pages = discover_dotted_bp_pages(toc_data)

    if dotted_pages and len(dotted_pages) >= len(bp_pages):
        # --- Dotted-ID lens (DevOps Guidance: "[OA.LS.1] ..." format) ---
        # Each best practice is its own page. Write one file per best
        # practice, named by its ID (OA.LS.1 -> OALS01.md), mirroring the
        # one-file-per-question convention used by the other BP-style lenses
        # (e.g. agentic-ai's AGENTCOST01.md) and the pillar question corpus.
        print(f"  Mode: Dotted-BP-style ({len(dotted_pages)} best practices)")
        if dry_run:
            for bp in dotted_pages[:20]:
                print(f"    {bp['bp_id']} -> {dotted_bp_filename(bp['bp_id'])}")
            if len(dotted_pages) > 20:
                print(f"    ... and {len(dotted_pages) - 20} more")
            return

        output_dir.mkdir(parents=True, exist_ok=True)
        written = 0
        for i, bp in enumerate(dotted_pages):
            time.sleep(delay)
            url = f"{base_url}/{bp['href']}"
            print(f"  [{i+1}/{len(dotted_pages)}] {bp['bp_id']}...", end=" ", flush=True)

            html = fetch(url)
            if not html:
                print("SKIP")
                continue
            content_html = extract_content(html)
            if not content_html:
                print("NO_CONTENT")
                continue
            md = html_to_markdown(content_html)
            if len(md) < 50:
                print("TOO_SHORT")
                continue

            filename = dotted_bp_filename(bp["bp_id"])
            # Lead with grouping metadata (saga + capability), then the fetched
            # content — which already begins with its own "# [OA.AWE.1] Title"
            # heading, so we don't emit a synthetic title (avoids duplication).
            # Capability pairs the code with its human name when known
            # (e.g. "OA.LS — Leader sponsorship").
            cap = bp["group_id"]
            if bp.get("capability"):
                cap = f"{bp['group_id']} — {bp['capability']}"
            lines = []
            if bp.get("saga"):
                lines.append(f"**Saga**: {bp['saga']}")
            lines += [
                f"**Capability**: {cap}",
                "",
                "---",
                "",
                md,
                "",
                f"*Source: {url}*",
                "",
            ]
            (output_dir / filename).write_text("\n".join(lines), encoding="utf-8")
            written += 1
            print("OK")

        print(f"\n  Done: {written} files, {len(dotted_pages)} best practices -> {output_dir}/")

    elif bp_pages:
        # --- BP-style lens (GenAI, Agentic AI, Responsible AI, Hybrid Networking) ---
        print(f"  Mode: BP-style ({len(bp_pages)} best practices)")
        if dry_run:
            for bp in bp_pages[:15]:
                print(f"    {bp['bp_id']}: {bp['href']}")
            if len(bp_pages) > 15:
                print(f"    ... and {len(bp_pages) - 15} more")
            return

        # Fetch each BP page and group by question (same logic as pillar crawling)
        question_bps = defaultdict(list)
        for i, bp in enumerate(bp_pages):
            time.sleep(delay)
            url = f"{base_url}/{bp['href']}"
            print(f"  [{i+1}/{len(bp_pages)}] {bp['bp_id']}...", end=" ", flush=True)

            html = fetch(url)
            if not html:
                print("SKIP")
                continue
            content_html = extract_content(html)
            if not content_html:
                print("NO_CONTENT")
                continue
            md = html_to_markdown(content_html)
            if len(md) < 50:
                print("TOO_SHORT")
                continue

            question_id = bp["bp_id"].split("-BP")[0]
            question_bps[question_id].append({
                "bp_id": bp["bp_id"],
                "title": bp["title"],
                "content": md,
                "url": url,
                "group": bp.get("group"),
            })
            print("OK")

        written = write_output_per_question(dict(question_bps), output_dir)
        total = sum(len(v) for v in question_bps.values())
        print(f"\n  Done: {written} files, {total} best practices -> {output_dir}/")

    else:
        # --- Topic-page-style lens (Serverless, Migration, Data Analytics) ---
        # These lenses don't use individual BP-ID pages. Instead, guidance is
        # organized as topic pages under pillar section headings.
        leaf_pages = discover_leaf_pages(toc_data)
        print(f"  Mode: Topic-page-style ({len(leaf_pages)} pages)")

        if dry_run:
            for page in leaf_pages[:20]:
                print(f"    [{page['section']}] {page['title']} -> {page['href']}")
            if len(leaf_pages) > 20:
                print(f"    ... and {len(leaf_pages) - 20} more")
            return

        # Fetch each leaf page and group by its parent section
        section_pages = defaultdict(list)
        for i, page in enumerate(leaf_pages):
            time.sleep(delay)
            url = f"{base_url}/{page['href']}"
            print(f"  [{i+1}/{len(leaf_pages)}] {page['title'][:50]}...", end=" ", flush=True)

            html = fetch(url)
            if not html:
                print("SKIP")
                continue
            content_html = extract_content(html)
            if not content_html:
                print("NO_CONTENT")
                continue
            md = html_to_markdown(content_html)
            if len(md) < 50:
                print("TOO_SHORT")
                continue

            section_pages[page["section"]].append({
                "title": page["title"],
                "content": md,
                "url": url,
                "qid": page.get("qid"),
                "parent": page.get("parent"),
            })
            print("OK")

        output_dir.mkdir(parents=True, exist_ok=True)

        # Some flat-TOC lenses (IoT) are really BP-style: the focus-area pages
        # embed "## IOTSEC01-BP01 ..." headings in their bodies rather than
        # exposing each BP as its own TOC page. When detected, split those bodies
        # into per-question files (IOTSEC01.md, ...) via the shared write_output,
        # so IoT reads like the other BP-style lenses. Returns None — and this
        # branch is skipped — for every lens without embedded BP headings, so
        # they stay byte-identical.
        embedded = split_embedded_bps(section_pages)
        if embedded:
            written = write_output_per_question(embedded, output_dir)
            total = sum(len(v) for v in embedded.values())
            print(f"\n  Done: {written} question files, {total} best practices -> {output_dir}/")
            return

        # If every captured page carries a question ID (e.g. Financial Services'
        # "FSISEC01: ..."), write one file per question — finer-grained and
        # consistent with the BP-style lenses. Otherwise keep the per-pillar
        # grouping used by serverless/migration/data-analytics. The branch is
        # all-or-nothing so a lens without qids is byte-identical to before.
        all_pages = [p for pages in section_pages.values() for p in pages]
        if all_pages and all(p.get("qid") for p in all_pages):
            written = 0
            for p in sorted(all_pages, key=lambda x: x["qid"]):
                # Prepend the pillar when derivable from the qid (FSISEC01 ->
                # Security). The content already carries its own "# FSISEC01:"
                # title heading, so we only add the metadata line.
                lines = []
                pillar = pillar_for_id(p["qid"])
                if pillar:
                    lines += [f"**Pillar**: {pillar}", ""]
                lines += [
                    p["content"],
                    "",
                    f"*Source: {p['url']}*",
                    "",
                ]
                (output_dir / f"{p['qid']}.md").write_text("\n".join(lines), encoding="utf-8")
                written += 1
            print(f"\n  Done: {written} question files, {len(all_pages)} pages -> {output_dir}/")
        else:
            # Write one file per section (e.g., "security.md", "reliability.md")
            written = 0
            for section, pages in sorted(section_pages.items()):
                # Convert section title to a filesystem-safe slug
                slug = re.sub(r"[^a-z0-9]+", "-", section.lower()).strip("-")
                lines = [
                    f"# {section}",
                    "",
                    f"**Pages**: {len(pages)}",
                    "",
                    "---",
                    "",
                ]
                last_parent = None
                for p in pages:
                    # Emit the numbered-question title as a sub-heading the first
                    # time it appears, so best practices keep the context of the
                    # question they answer. Pages with no numbered parent
                    # (serverless, migration, etc.) are unaffected -> byte-identical.
                    if p.get("parent") and p["parent"] != last_parent:
                        lines.append(f"## {p['parent']}")
                        lines.append("")
                        last_parent = p["parent"]
                    lines.append(p["content"])
                    lines.append("")
                    lines.append(f"*Source: {p['url']}*")
                    lines.append("")
                    lines.append("---")
                    lines.append("")

                (output_dir / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")
                written += 1

            total = sum(len(v) for v in section_pages.values())
            print(f"\n  Done: {written} files, {total} pages -> {output_dir}/")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main():
    """
    Parse arguments and dispatch to the appropriate crawling mode.

    Two modes:
    - Pillar mode (default): Crawl one or all 6 WA Framework pillars.
      Produces pillar-merged files in skills/wa-review/references/pillars/
      (one file per pillar containing all its questions).

    - Lens mode (--lens URL): Crawl a WA Lens by its docs URL.
      Auto-detects BP-style vs topic-page-style.
      Produces files in skills/wa-review/references/lenses/{name}/.
    """
    parser = argparse.ArgumentParser(
        description="Crawl AWS WA docs. Framework mode → pillar-merged files "
                    "(6 files, one per pillar). Lens mode → per-question files."
    )
    parser.add_argument("--output-dir", default="skills/wa-review/references/pillars",
                        help="Output directory for framework pillars "
                             "(default: skills/wa-review/references/pillars). "
                             "Lens mode uses skills/wa-review/references/lenses/{name}/.")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between requests in seconds (default: 0.3)")
    parser.add_argument("--pillar", choices=list(PILLAR_CONFIGS.keys()),
                        help="Crawl only one pillar (default: all)")
    parser.add_argument("--lens", type=str, default=None,
                        help="Crawl a WA Lens by URL (e.g. https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)")
    parser.add_argument("--lens-name", type=str, default=None,
                        help="Name for the lens (used in output, e.g. 'serverless')")
    parser.add_argument("--dry-run", action="store_true",
                        help="Only discover pages from TOC, don't fetch content")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)

    # --- Lens mode ---
    # When --lens is provided, we crawl a single lens and output to
    # the lenses subdirectory (unless --output-dir is explicitly overridden).
    if args.lens:
        # Derive a short name from the URL path if not provided
        # e.g., ".../generative-ai-lens/..." -> "generative-ai"
        lens_name = args.lens_name or args.lens.rsplit("/", 2)[-2].replace("-lens", "")
        if args.output_dir == "skills/wa-review/references/pillars":
            output_dir = Path(f"skills/wa-review/references/lenses/{lens_name}")
        crawl_lens(args.lens, lens_name, output_dir, args.delay, args.dry_run)
        return

    # --- Pillar mode ---
    # Crawl one or all 6 framework pillars. Each pillar produces question files
    # that are written to the same output directory (they don't overlap because
    # each pillar uses a unique prefix: OPS, SEC, REL, PERF, COST, SUS).
    pillars = {args.pillar: PILLAR_CONFIGS[args.pillar]} if args.pillar else PILLAR_CONFIGS

    print(f"Output: {output_dir}")
    print(f"Delay: {args.delay}s")
    print(f"Pillars: {', '.join(pillars.keys())}")

    all_questions = {}
    for name, config in pillars.items():
        result = crawl_pillar(name, config, args.delay, args.dry_run)
        all_questions.update(result)

    if args.dry_run:
        print(f"\nDry run complete.")
        return

    written = write_output_pillar_merged(all_questions, output_dir)
    total_bps = sum(len(v) for v in all_questions.values())
    print(f"\n{'='*60}")
    print(f"  DONE: {written} pillar files, {total_bps} best practices")
    print(f"  Output: {output_dir}/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
