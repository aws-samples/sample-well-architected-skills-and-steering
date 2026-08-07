"""Tests for wa-ci delta classification and gating.

Stdlib unittest, no network, no AWS, no third-party deps. Run with either:
    python3 -m unittest tools/wa-ci/test_wa_ci.py
    cd tools/wa-ci && python3 -m pytest test_wa_ci.py -q
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))

import wa_ci  # noqa: E402


def finding(bp_id, status, severity=None, pillar="security"):
    row = {"bp_id": bp_id, "pillar": pillar, "status": status}
    if severity is not None:
        row["severity"] = severity
    return row


def review(findings, **overrides):
    doc = {
        "schema_version": "1.0.0",
        "workload": "test",
        "date": "2026-08-06",
        "review_mode": "full",
        "skill_version": "2.2.0",
        "run_id": "test-run",
        "pillar_scores": {"security": 3},
        "findings": findings,
        "recall_note": "test",
    }
    doc.update(overrides)
    return doc


def deltas_by_id(changes):
    return {c["bp_id"]: c["delta"] for c in changes}


class TestClassify(unittest.TestCase):
    def test_resolved_when_gap_becomes_implemented(self):
        base = review([finding("SEC08-BP01", "not_implemented", "high")])
        cur = review([finding("SEC08-BP01", "implemented")])
        self.assertEqual(deltas_by_id(wa_ci.classify(base, cur)), {"SEC08-BP01": wa_ci.RESOLVED})

    def test_resolved_when_gap_becomes_not_applicable(self):
        base = review([finding("SEC08-BP01", "partially_implemented", "medium")])
        cur = review([finding("SEC08-BP01", "not_applicable")])
        self.assertEqual(deltas_by_id(wa_ci.classify(base, cur)), {"SEC08-BP01": wa_ci.RESOLVED})

    def test_still_open_when_gap_persists(self):
        base = review([finding("SEC08-BP01", "not_implemented", "high")])
        cur = review([finding("SEC08-BP01", "not_implemented", "high")])
        self.assertEqual(deltas_by_id(wa_ci.classify(base, cur)), {"SEC08-BP01": wa_ci.STILL_OPEN})

    def test_partial_to_not_implemented_is_still_open(self):
        # Both are gap statuses, so this stays Still-open (not New/Regressed).
        base = review([finding("SEC08-BP01", "partially_implemented", "medium")])
        cur = review([finding("SEC08-BP01", "not_implemented", "high")])
        self.assertEqual(deltas_by_id(wa_ci.classify(base, cur)), {"SEC08-BP01": wa_ci.STILL_OPEN})

    def test_new_when_bp_absent_from_baseline(self):
        base = review([])
        cur = review([finding("SEC05-BP01", "not_implemented", "critical")])
        self.assertEqual(deltas_by_id(wa_ci.classify(base, cur)), {"SEC05-BP01": wa_ci.NEW})

    def test_regressed_when_passing_becomes_gap(self):
        base = review([finding("REL09-BP01", "implemented")])
        cur = review([finding("REL09-BP01", "not_implemented", "high")])
        self.assertEqual(deltas_by_id(wa_ci.classify(base, cur)), {"REL09-BP01": wa_ci.REGRESSED})

    def test_cannot_determine_baseline_gap_now_is_new_not_regressed(self):
        # cannot_determine is neither pass nor gap; a gap now is New, not Regressed.
        base = review([finding("SEC08-BP01", "cannot_determine")])
        cur = review([finding("SEC08-BP01", "not_implemented", "high")])
        self.assertEqual(deltas_by_id(wa_ci.classify(base, cur)), {"SEC08-BP01": wa_ci.NEW})

    def test_absent_baseline_gap_not_reported_as_resolved(self):
        # A baseline gap that simply drops out of the current review is NOT resolved.
        base = review([finding("SEC08-BP01", "not_implemented", "high")])
        cur = review([])
        self.assertEqual(wa_ci.classify(base, cur), [])

    def test_unchanged_passing_bp_produces_no_delta(self):
        base = review([finding("REL09-BP01", "implemented")])
        cur = review([finding("REL09-BP01", "implemented")])
        self.assertEqual(wa_ci.classify(base, cur), [])

    def test_full_example_mix(self):
        base = review([
            finding("SEC08-BP01", "not_implemented", "high"),
            finding("SEC03-BP02", "partially_implemented", "medium"),
            finding("REL09-BP01", "implemented", pillar="reliability"),
        ])
        cur = review([
            finding("SEC08-BP01", "implemented"),                       # resolved
            finding("SEC03-BP02", "partially_implemented", "medium"),   # still open
            finding("REL09-BP01", "not_implemented", "high", "reliability"),  # regressed
            finding("SEC05-BP01", "not_implemented", "critical"),       # new
        ])
        self.assertEqual(deltas_by_id(wa_ci.classify(base, cur)), {
            "SEC08-BP01": wa_ci.RESOLVED,
            "SEC03-BP02": wa_ci.STILL_OPEN,
            "REL09-BP01": wa_ci.REGRESSED,
            "SEC05-BP01": wa_ci.NEW,
        })


class TestGating(unittest.TestCase):
    def _changes(self):
        base = review([finding("REL09-BP01", "implemented", pillar="reliability")])
        cur = review([
            finding("REL09-BP01", "not_implemented", "high", "reliability"),  # regressed high
            finding("SEC05-BP01", "not_implemented", "critical"),             # new critical
            finding("COST04-BP01", "not_implemented", "low", "cost_optimization"),  # new low
        ])
        return wa_ci.classify(base, cur)

    def test_fail_on_high_catches_high_and_critical(self):
        failures = wa_ci.gating_failures(self._changes(), "high")
        self.assertEqual(
            sorted(f["bp_id"] for f in failures),
            ["REL09-BP01", "SEC05-BP01"],
        )

    def test_fail_on_low_catches_everything_new_or_regressed(self):
        failures = wa_ci.gating_failures(self._changes(), "low")
        self.assertEqual(len(failures), 3)

    def test_fail_on_critical_catches_only_critical(self):
        failures = wa_ci.gating_failures(self._changes(), "critical")
        self.assertEqual([f["bp_id"] for f in failures], ["SEC05-BP01"])

    def test_still_open_never_gates(self):
        # A pre-existing gap that persists must not fail the build.
        base = review([finding("SEC08-BP01", "not_implemented", "critical")])
        cur = review([finding("SEC08-BP01", "not_implemented", "critical")])
        self.assertEqual(wa_ci.gating_failures(wa_ci.classify(base, cur), "low"), [])

    def test_resolved_never_gates(self):
        base = review([finding("SEC08-BP01", "not_implemented", "critical")])
        cur = review([finding("SEC08-BP01", "implemented")])
        self.assertEqual(wa_ci.gating_failures(wa_ci.classify(base, cur), "low"), [])

    def test_new_gap_without_severity_fails_closed(self):
        # A New gap with no severity must gate at every threshold, not slip through.
        base = review([])
        cur = review([finding("SEC05-BP01", "not_implemented", severity=None)])
        changes = wa_ci.classify(base, cur)
        for level in ("low", "medium", "high", "critical"):
            self.assertEqual(
                [f["bp_id"] for f in wa_ci.gating_failures(changes, level)],
                ["SEC05-BP01"],
                f"unrated new gap should gate at --fail-on {level}",
            )

    def test_regressed_gap_without_severity_fails_closed(self):
        base = review([finding("REL09-BP01", "implemented", pillar="reliability")])
        cur = review([finding("REL09-BP01", "not_implemented", severity=None, pillar="reliability")])
        changes = wa_ci.classify(base, cur)
        self.assertEqual(
            [f["bp_id"] for f in wa_ci.gating_failures(changes, "critical")],
            ["REL09-BP01"],
        )

    def test_unrated_gap_does_not_affect_still_open(self):
        # Still-open never gates, even without a severity.
        base = review([finding("SEC08-BP01", "not_implemented", severity=None)])
        cur = review([finding("SEC08-BP01", "not_implemented", severity=None)])
        self.assertEqual(wa_ci.gating_failures(wa_ci.classify(base, cur), "low"), [])


def advisory(title, status, severity=None, pillar="performance_efficiency", lens="serverless-applications"):
    row = {"title": title, "pillar": pillar, "status": status, "lens": lens}
    if severity is not None:
        row["severity"] = severity
    return row


class TestAdvisoryFindings(unittest.TestCase):
    def test_findings_without_bp_id_are_excluded_from_diff(self):
        # An ID-less gap must never appear as New/Regressed/etc.
        base = review([])
        cur = review([advisory("Async Lambda", "not_implemented", "high")])
        self.assertEqual(wa_ci.classify(base, cur), [])

    def test_findings_without_bp_id_never_gate(self):
        base = review([])
        cur = review([advisory("Async Lambda", "not_implemented", "critical")])
        changes = wa_ci.classify(base, cur)
        self.assertEqual(wa_ci.gating_failures(changes, "low"), [])

    def test_advisory_gaps_are_collected(self):
        cur = review([
            finding("SEC05-BP01", "not_implemented", "critical"),
            advisory("Async Lambda", "not_implemented", "medium"),
            advisory("Tenant isolation", "partially_implemented", "high", lens="saas"),
        ])
        advisories = wa_ci.advisory_findings(cur)
        self.assertEqual(len(advisories), 2)
        self.assertEqual({a["title"] for a in advisories}, {"Async Lambda", "Tenant isolation"})

    def test_passing_advisory_is_not_collected(self):
        # Only gap-status advisories are worth surfacing.
        cur = review([advisory("Async Lambda", "implemented")])
        self.assertEqual(wa_ci.advisory_findings(cur), [])

    def test_advisory_alone_does_not_fail_the_build(self):
        base = _named(review([]))
        cur = _named(review([advisory("Async Lambda", "not_implemented", "critical")]))
        rc = wa_ci.main(["--baseline", base, "--current", cur, "--fail-on", "low"])
        self.assertEqual(rc, 0)


_TMP_PATHS = []


def _named(doc):
    handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
    json.dump(doc, handle)
    handle.close()
    _TMP_PATHS.append(handle.name)
    return handle.name


def tearDownModule():
    for path in _TMP_PATHS:
        try:
            os.unlink(path)
        except OSError:
            pass


class TestCoverageWarnings(unittest.TestCase):
    def test_schema_major_mismatch_warns(self):
        base = review([], schema_version="1.0.0")
        cur = review([], schema_version="2.0.0")
        self.assertTrue(any("schema major" in w for w in wa_ci.coverage_warnings(base, cur)))

    def test_narrower_current_mode_warns(self):
        base = review([], review_mode="full")
        cur = review([], review_mode="quick")
        self.assertTrue(any("review_mode" in w for w in wa_ci.coverage_warnings(base, cur)))

    def test_matching_full_reviews_no_warning(self):
        base = review([], review_mode="full")
        cur = review([], review_mode="full")
        self.assertEqual(wa_ci.coverage_warnings(base, cur), [])

    def test_baseline_gap_now_cannot_determine_warns(self):
        base = review([finding("SEC08-BP01", "not_implemented", "high")])
        cur = review([finding("SEC08-BP01", "cannot_determine")])
        warnings = wa_ci.coverage_warnings(base, cur)
        self.assertTrue(any("cannot_determine" in w and "SEC08-BP01" in w for w in warnings))

    def test_baseline_gap_still_open_does_not_warn_cannot_determine(self):
        base = review([finding("SEC08-BP01", "not_implemented", "high")])
        cur = review([finding("SEC08-BP01", "not_implemented", "high")])
        self.assertFalse(any("cannot_determine" in w for w in wa_ci.coverage_warnings(base, cur)))


class TestMainExitCodes(unittest.TestCase):
    def _write(self, doc):
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8")
        json.dump(doc, handle)
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def test_exit_zero_when_no_new_or_regressed(self):
        base = self._write(review([finding("SEC08-BP01", "not_implemented", "high")]))
        cur = self._write(review([finding("SEC08-BP01", "implemented")]))
        rc = wa_ci.main(["--baseline", base, "--current", cur, "--fail-on", "high"])
        self.assertEqual(rc, 0)

    def test_exit_one_on_new_high_finding(self):
        base = self._write(review([]))
        cur = self._write(review([finding("SEC05-BP01", "not_implemented", "high")]))
        rc = wa_ci.main(["--baseline", base, "--current", cur, "--fail-on", "high"])
        self.assertEqual(rc, 1)

    def test_fail_on_none_never_gates(self):
        base = self._write(review([]))
        cur = self._write(review([finding("SEC05-BP01", "not_implemented", "critical")]))
        rc = wa_ci.main(["--baseline", base, "--current", cur, "--fail-on", "none"])
        self.assertEqual(rc, 0)

    def test_update_baseline_writes_file(self):
        cur = self._write(review([finding("SEC08-BP01", "not_implemented", "high")]))
        out = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
        out.close()
        self.addCleanup(os.unlink, out.name)
        rc = wa_ci.main(["--current", cur, "--update-baseline", out.name])
        self.assertEqual(rc, 0)
        with open(out.name, encoding="utf-8") as handle:
            written = json.load(handle)
        self.assertEqual(written["findings"][0]["bp_id"], "SEC08-BP01")

    def test_baseline_required_without_update(self):
        cur = self._write(review([]))
        with self.assertRaises(SystemExit):
            wa_ci.main(["--current", cur])


if __name__ == "__main__":
    unittest.main()
