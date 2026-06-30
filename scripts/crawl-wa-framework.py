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
    skills/wa-review/references/questions/{QUESTION_ID}.md   (framework pillars)
    skills/wa-review/references/lenses/{lens-name}/*.md      (WA lenses)

Usage:
    uv run scripts/crawl-wa-framework.py [--output-dir DIR] [--delay SECS] [--pillar PILLAR] [--dry-run]
    uv run scripts/crawl-wa-framework.py --lens <URL> [--lens-name NAME] [--dry-run]

Examples:
    # Crawl all 6 framework pillars (produces 57 question files)
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

    Returns a list of dicts with keys: bp_id, title, href.
    The bp_id (e.g., "SEC03-BP01") is extracted from the title prefix.
    The href is relative to the pillar/lens base URL.
    """
    results = []

    def walk(contents):
        for item in contents:
            title = item.get("title", "")
            # Match titles that start with a BP ID pattern
            if "-BP" in title and "href" in item:
                bp_match = re.match(r"([A-Z]+\d+-BP\d+)", title)
                if bp_match:
                    results.append({
                        "bp_id": bp_match.group(1),
                        "title": title,
                        "href": item["href"],
                    })
            # Recurse into child nodes
            if "contents" in item:
                walk(item["contents"])

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
    group_id (e.g. "OA.LS"), title, href.
    """
    results = []
    # Titles look like "[OA.LS.1] Human-readable title". Some entries contain
    # non-breaking spaces, so normalize whitespace before matching.
    pattern = re.compile(r"^\[([A-Z]+\.[A-Z]+\.\d+)\]\s*(.*)", re.DOTALL)

    def walk(contents):
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
                })
            if "contents" in item:
                walk(item["contents"])

    walk(toc_json.get("contents", []))
    return results


# ---------------------------------------------------------------------------
# TOC parsing — Topic-page-style (older lenses)
# ---------------------------------------------------------------------------


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

    def walk(contents, section=None, depth=0):
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
                # Branch node — recurse deeper, passing along the current section context
                walk(item["contents"], current_section, depth + 1)
            elif current_section and href and (depth >= 2 or matched):
                # Capture this leaf when either:
                #  - it sits under a pillar section (depth >= 2), the common case; or
                #  - the leaf IS the pillar (matched): some lenses express a whole
                #    pillar as a single content page with no child best practices
                #    (e.g. the serverless lens's "Sustainability" at depth 1).
                #    Without this, that pillar's content is silently dropped.
                results.append({
                    "section": current_section,
                    "title": title,
                    "href": href,
                })

    walk(toc_json.get("contents", []))
    return results


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
        })
        print("OK")

    print(f"  Done: {sum(len(v) for v in question_bps.values())} BPs across {len(question_bps)} questions")
    return dict(question_bps)


# ---------------------------------------------------------------------------
# Output writing
# ---------------------------------------------------------------------------


def write_output(all_questions: dict[str, list[dict]], output_dir: Path) -> int:
    """
    Write consolidated markdown files — one file per WA question.

    Each file contains:
    - H1 title with the official question text
    - Metadata (pillar name, BP count)
    - All BPs for that question in order, separated by horizontal rules
    - Source URL for each BP (for traceability back to the docs)

    The agent loads one of these files at a time during a review to get
    full best-practice-level detail for the question it's evaluating.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    written = 0

    for question_id in sorted(all_questions.keys()):
        bps = all_questions[question_id]
        if not bps:
            continue

        # Look up the human-readable question title; fall back to the raw ID
        title = QUESTION_TITLES.get(question_id, question_id)
        prefix = re.match(r"[A-Z]+", question_id).group(0)
        pillar = PILLAR_DISPLAY.get(prefix, "Unknown")

        # Build the file content
        lines = [
            f"# {title}",
            "",
            f"**Pillar**: {pillar}  ",
            f"**Best Practices**: {len(bps)}",
            "",
            "---",
            "",
        ]

        # Append each BP's content with source attribution
        for bp in sorted(bps, key=lambda b: b["bp_id"]):
            lines.append(bp["content"])
            lines.append("")
            lines.append(f"*Source: {bp['url']}*")
            lines.append("")
            lines.append("---")
            lines.append("")

        (output_dir / f"{question_id}.md").write_text("\n".join(lines), encoding="utf-8")
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
            lines = [
                f"# {bp['title']}",
                "",
                f"**Capability**: {bp['group_id']}",
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
            })
            print("OK")

        written = write_output(dict(question_bps), output_dir)
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
            })
            print("OK")

        # Write one file per section (e.g., "security.md", "reliability.md")
        output_dir.mkdir(parents=True, exist_ok=True)
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
            for p in pages:
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
      Produces per-question files in skills/wa-review/references/questions/.

    - Lens mode (--lens URL): Crawl a WA Lens by its docs URL.
      Auto-detects BP-style vs topic-page-style.
      Produces files in skills/wa-review/references/lenses/{name}/.
    """
    parser = argparse.ArgumentParser(
        description="Crawl AWS WA docs and produce per-question reference files"
    )
    parser.add_argument("--output-dir", default="skills/wa-review/references/questions",
                        help="Output directory (default: skills/wa-review/references/questions)")
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
        if args.output_dir == "skills/wa-review/references/questions":
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

    written = write_output(all_questions, output_dir)
    total_bps = sum(len(v) for v in all_questions.values())
    print(f"\n{'='*60}")
    print(f"  DONE: {written} question files, {total_bps} best practices")
    print(f"  Output: {output_dir}/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
