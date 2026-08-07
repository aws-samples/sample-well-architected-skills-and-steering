#!/usr/bin/env python3
"""wa-ci: gate a pull request on the Well-Architected delta.

Diffs a fresh wa-review.json against a committed baseline and classifies each
best practice as Resolved, Still-open, New, or Regressed. Exits non-zero when
the delta introduces a gap at or above a severity threshold, so a pipeline can
block a change that erodes the workload's Well-Architected posture.

Stdlib only. No AWS credentials, no network. Reads the structured output
contract in schemas/wa-review-v1.schema.json (identity key: bp_id).

Design boundary: this reports and gates. It never mutates a workload's code.

Usage:
    python3 wa_ci.py --baseline .well-architected/baseline.json \\
                     --current wa-review.json \\
                     --fail-on high

    # Refresh the baseline after a review is accepted (no gating):
    python3 wa_ci.py --current wa-review.json --update-baseline .well-architected/baseline.json
"""

import argparse
import json
import sys

# Severity order, lowest to highest. A finding with no severity (implemented /
# not_applicable rows carry none) sorts below "low" so it never trips a gate.
SEVERITY_ORDER = ["low", "medium", "high", "critical"]

# A BP in one of these statuses is an open gap in the workload.
GAP_STATUSES = {"not_implemented", "partially_implemented"}
# A BP in one of these statuses is explicitly passing. Note "cannot_determine"
# is deliberately NEITHER: it is not a confirmed gap and not proof of a control.
PASS_STATUSES = {"implemented", "not_applicable"}

# Delta classifications.
RESOLVED = "resolved"        # was a gap in baseline, now explicitly passing
STILL_OPEN = "still_open"    # gap in baseline and still a gap now
NEW = "new"                  # a gap now that was not a gap in baseline
REGRESSED = "regressed"      # was passing in baseline, now a gap


def severity_rank(severity):
    """Rank a severity string. Unknown / null sorts below the lowest real level."""
    if severity in SEVERITY_ORDER:
        return SEVERITY_ORDER.index(severity)
    return -1


def load_review(path):
    """Load and minimally validate a wa-review document."""
    try:
        with open(path, encoding="utf-8") as handle:
            doc = json.load(handle)
    except FileNotFoundError:
        raise SystemExit(f"wa-ci: file not found: {path}")
    except json.JSONDecodeError as err:
        raise SystemExit(f"wa-ci: {path} is not valid JSON: {err}")
    if not isinstance(doc, dict) or "findings" not in doc:
        raise SystemExit(f"wa-ci: {path} does not look like a wa-review document (no 'findings').")
    return doc


def index_findings(doc):
    """Map bp_id -> finding, for findings that carry a canonical bp_id.

    Only bp_id-bearing findings can be paired across reviews, so only these
    participate in the diff and the gate. Findings without a bp_id (topic-organized
    lens findings, which carry a title instead) are handled separately by
    advisory_findings so they are counted and shown, never silently dropped.
    Last write wins if a document repeats a BP id.
    """
    index = {}
    for finding in doc.get("findings", []):
        bp_id = finding.get("bp_id")
        if bp_id:
            index[bp_id] = finding
    return index


def advisory_findings(doc):
    """Findings with no bp_id: gaps a title identifies but a diff cannot pair.

    These come from topic-organized lenses (e.g. serverless-applications, saas).
    They are reported and counted so coverage is visible, but they never gate a
    build because a title is not a stable identity key across reviews.
    """
    advisories = []
    for finding in doc.get("findings", []):
        if finding.get("bp_id"):
            continue
        if finding.get("status") not in GAP_STATUSES:
            continue
        advisories.append({
            "title": finding.get("title", "(untitled)"),
            "pillar": finding.get("pillar"),
            "lens": finding.get("lens"),
            "status": finding.get("status"),
            "severity": finding.get("severity"),
            "recommendation": finding.get("recommendation", ""),
        })
    return advisories


def schema_major(doc):
    """Major version of the document's schema_version (e.g. '1' from '1.2.0')."""
    version = str(doc.get("schema_version", ""))
    return version.split(".")[0] if version else ""


def classify(baseline_doc, current_doc):
    """Return the list of changed findings, each tagged with a delta class.

    Pairs findings on bp_id. Only findings whose status changed in a way that
    matters to the gate are returned; unchanged rows are omitted to keep the
    report focused on the delta.

    Absence is never read as a pass. A BP that drops out of the current review
    (e.g. a narrower review_mode did not evaluate it) is NOT counted as
    Resolved, because the contract guarantees coverage is not exhaustiveness.
    """
    baseline = index_findings(baseline_doc)
    current = index_findings(current_doc)

    changes = []
    for bp_id, cur in current.items():
        base = baseline.get(bp_id)
        cur_status = cur.get("status")
        base_status = base.get("status") if base else None

        cur_is_gap = cur_status in GAP_STATUSES
        base_was_gap = base_status in GAP_STATUSES
        base_was_pass = base_status in PASS_STATUSES

        if cur_is_gap and not base_was_gap:
            # New gap. Regressed if the baseline explicitly passed it; otherwise
            # New (baseline was absent, or cannot_determine).
            changes.append(_change(REGRESSED if base_was_pass else NEW, cur, base))
        elif cur_is_gap and base_was_gap:
            changes.append(_change(STILL_OPEN, cur, base))

    # Resolved: a baseline gap that the current review explicitly marks passing.
    # Requires the BP to be present-and-passing in current, not merely absent.
    for bp_id, base in baseline.items():
        if base.get("status") not in GAP_STATUSES:
            continue
        cur = current.get(bp_id)
        if cur and cur.get("status") in PASS_STATUSES:
            changes.append(_change(RESOLVED, cur, base))

    return changes


def _change(delta, current_finding, baseline_finding):
    return {
        "delta": delta,
        "bp_id": current_finding.get("bp_id"),
        "pillar": current_finding.get("pillar"),
        "status": current_finding.get("status"),
        "baseline_status": baseline_finding.get("status") if baseline_finding else None,
        "severity": current_finding.get("severity"),
        "recommendation": current_finding.get("recommendation", ""),
    }


def gating_failures(changes, fail_on):
    """Findings that should fail the build: New or Regressed gaps at/above fail_on.

    A New or Regressed gap whose severity is missing or unrecognized ALSO fails,
    regardless of threshold. The schema requires a severity on every gap finding,
    so an unrated gap means a malformed review; failing closed keeps the gate from
    silently passing a regression a producer forgot to rate.
    """
    threshold = severity_rank(fail_on)
    failures = []
    for c in changes:
        if c["delta"] not in (NEW, REGRESSED):
            continue
        rank = severity_rank(c["severity"])
        if rank < 0 or rank >= threshold:
            failures.append(c)
    return failures


def render_report(changes, failures, fail_on, baseline_doc, current_doc, coverage_warnings, advisories):
    """Human-readable summary for the CI log."""
    lines = []
    workload = current_doc.get("workload", "unknown")
    lines.append(f"Well-Architected delta for: {workload}")
    lines.append(
        f"  baseline: {baseline_doc.get('date', '?')} "
        f"(mode={baseline_doc.get('review_mode', '?')}, run={baseline_doc.get('run_id', '?')})"
    )
    lines.append(
        f"  current:  {current_doc.get('date', '?')} "
        f"(mode={current_doc.get('review_mode', '?')}, run={current_doc.get('run_id', '?')})"
    )

    counts = {RESOLVED: 0, STILL_OPEN: 0, NEW: 0, REGRESSED: 0}
    for change in changes:
        counts[change["delta"]] += 1
    lines.append("")
    lines.append(
        f"  Resolved: {counts[RESOLVED]}   New: {counts[NEW]}   "
        f"Regressed: {counts[REGRESSED]}   Still open: {counts[STILL_OPEN]}"
        f"   Advisory: {len(advisories)}"
    )

    for warning in coverage_warnings:
        lines.append(f"  ! {warning}")

    def block(title, delta):
        rows = [c for c in changes if c["delta"] == delta]
        if not rows:
            return
        lines.append("")
        lines.append(f"{title} ({len(rows)}):")
        for change in _sorted_by_severity(rows):
            sev = change["severity"] or "-"
            lines.append(f"  [{sev:>8}] {change['bp_id']} ({change['pillar']}): {change['status']}")

    block("Regressed", REGRESSED)
    block("New gaps", NEW)
    block("Resolved", RESOLVED)
    block("Still open", STILL_OPEN)

    if advisories:
        lines.append("")
        lines.append(f"Advisory (lens findings without a BP ID, not gated) ({len(advisories)}):")
        for adv in _sorted_by_severity(advisories):
            sev = adv["severity"] or "-"
            lens = f" [{adv['lens']}]" if adv.get("lens") else ""
            lines.append(f"  [{sev:>8}]{lens} {adv['title']} ({adv['pillar']}): {adv['status']}")

    lines.append("")
    if failures:
        lines.append(
            f"FAIL: {len(failures)} new or regressed finding(s) at or above '{fail_on}'."
        )
    else:
        lines.append(f"PASS: no new or regressed findings at or above '{fail_on}'.")
    return "\n".join(lines)


def _sorted_by_severity(rows):
    return sorted(rows, key=lambda c: severity_rank(c["severity"]), reverse=True)


def coverage_warnings(baseline_doc, current_doc):
    """Warn about conditions that make the delta less trustworthy."""
    warnings = []
    base_major = schema_major(baseline_doc)
    cur_major = schema_major(current_doc)
    if base_major and cur_major and base_major != cur_major:
        warnings.append(
            f"schema major version changed ({base_major} -> {cur_major}); "
            "the delta may not be comparable."
        )
    # A narrower current review evaluates fewer BPs, so a baseline gap can vanish
    # from the current findings without being resolved. classify() already refuses
    # to call that Resolved, but the reader should know coverage shrank.
    if current_doc.get("review_mode") != "full" and baseline_doc.get("review_mode") == "full":
        warnings.append(
            f"current review_mode is '{current_doc.get('review_mode')}' but baseline was 'full'; "
            "absent baseline gaps are NOT treated as resolved."
        )
    return warnings


def update_baseline(current_path, baseline_path):
    """Copy the current review to the baseline path verbatim."""
    doc = load_review(current_path)
    with open(baseline_path, "w", encoding="utf-8") as handle:
        json.dump(doc, handle, indent=2)
        handle.write("\n")
    print(f"wa-ci: wrote baseline {baseline_path} from {current_path}")


def build_parser():
    parser = argparse.ArgumentParser(
        prog="wa-ci",
        description="Gate a pull request on the Well-Architected delta between a baseline and a fresh review.",
    )
    parser.add_argument("--current", required=True, help="Path to the fresh wa-review.json.")
    parser.add_argument("--baseline", help="Path to the committed baseline wa-review.json.")
    parser.add_argument(
        "--fail-on",
        default="high",
        choices=SEVERITY_ORDER + ["none"],
        help="Fail the build on a new or regressed finding at or above this severity "
             "(default: high). 'none' reports without ever failing.",
    )
    parser.add_argument(
        "--update-baseline",
        metavar="PATH",
        help="Write --current to PATH as the new baseline and exit. Does not gate.",
    )
    parser.add_argument(
        "--json",
        dest="emit_json",
        action="store_true",
        help="Emit the classified delta as JSON on stdout instead of a text report.",
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.update_baseline:
        update_baseline(args.current, args.update_baseline)
        return 0

    if not args.baseline:
        raise SystemExit("wa-ci: --baseline is required unless --update-baseline is given.")

    baseline_doc = load_review(args.baseline)
    current_doc = load_review(args.current)

    changes = classify(baseline_doc, current_doc)
    warnings = coverage_warnings(baseline_doc, current_doc)
    # Gaps from the current review that carry no bp_id: reported, never gated.
    advisories = advisory_findings(current_doc)

    # A New/Regressed gap without a valid severity is a malformed review (the
    # schema requires one). Warn so the fail-closed behavior is not mysterious.
    unrated = [
        c for c in changes
        if c["delta"] in (NEW, REGRESSED) and severity_rank(c["severity"]) < 0
    ]
    if unrated:
        ids = ", ".join(c["bp_id"] for c in unrated)
        warnings.append(
            f"{len(unrated)} new/regressed finding(s) have no valid severity ({ids}); "
            "treating as gating. Add a severity in the review."
        )

    # --fail-on none: report every delta but never gate.
    failures = [] if args.fail_on == "none" else gating_failures(changes, args.fail_on)

    if args.emit_json:
        print(json.dumps({
            "workload": current_doc.get("workload"),
            "fail_on": args.fail_on,
            "changes": changes,
            "advisories": advisories,
            "failures": [f["bp_id"] for f in failures],
            "warnings": warnings,
            "gate": "fail" if failures else "pass",
        }, indent=2))
    else:
        print(render_report(changes, failures, args.fail_on, baseline_doc, current_doc, warnings, advisories))

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
