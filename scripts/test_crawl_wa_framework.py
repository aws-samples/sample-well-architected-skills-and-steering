"""Regression tests for the topic-page crawler's pillar detection (issue #80).

Stdlib unittest, no network, no AWS, no third-party deps. Uses small inline
toc-contents.json fixtures that reproduce the structural variations found in
real lens TOCs. Run with either:
    python3 -m unittest scripts/test_crawl_wa_framework.py
    cd scripts && python3 -m pytest test_crawl_wa_framework.py -q

Focus: discover_leaf_pages must bucket leaves under the correct WA pillar even
when a lens deviates from the canonical US-English, unsuffixed pillar names:
  - British spelling ("Cost optimisation")  -- Māori lens
  - trailing "pillar" suffix                -- government lens
  - a pillar expressed as a single content page (pillar-as-leaf)
  - generic scaffolding pages (Resources/Definitions/...) stay excluded
American-spelling lenses must keep behaving exactly as before (no regression).
"""

import importlib.util
import os
import unittest

# The crawler module's filename has hyphens, so import it by path.
_SCRIPT = os.path.join(os.path.dirname(__file__), "crawl-wa-framework.py")
_spec = importlib.util.spec_from_file_location("crawl_wa_framework", _SCRIPT)
cwf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cwf)


def leaf(title, href):
    return {"title": title, "href": href}


def branch(title, children, href=""):
    return {"title": title, "href": href, "contents": children}


def sections(pages):
    """Map section -> sorted list of captured hrefs."""
    out = {}
    for p in pages:
        out.setdefault(p["section"], []).append(p["href"])
    return {k: sorted(v) for k, v in out.items()}


class TestPillarMatching(unittest.TestCase):
    def test_british_spelling_cost_optimisation_is_captured(self):
        """Māori lens uses 'Cost optimisation'; its leaf must bucket as
        'Cost optimization' (issue #80 root cause #2) rather than being dropped."""
        toc = {"contents": [
            branch("Cost optimisation", [
                leaf("MD_CO 1 Understand costs", "md_cos-1.html"),
            ]),
        ]}
        secs = sections(cwf.discover_leaf_pages(toc))
        self.assertIn("Cost optimization", secs)
        self.assertEqual(secs["Cost optimization"], ["md_cos-1.html"])

    def test_trailing_pillar_suffix_matches(self):
        """government lens uses 'Operational excellence pillar' (suffix)."""
        toc = {"contents": [
            branch("Operational excellence pillar", [
                leaf("GOVOPS 1 How do you...", "govops-1.html"),
            ]),
        ]}
        secs = sections(cwf.discover_leaf_pages(toc))
        self.assertEqual(secs.get("Operational excellence"), ["govops-1.html"])

    def test_pillar_as_leaf(self):
        """A pillar expressed as a single content page (no child BPs) is captured
        under its own name (e.g. Māori 'Performance efficiency')."""
        toc = {"contents": [
            leaf("Performance efficiency", "performance-efficiency.html"),
        ]}
        secs = sections(cwf.discover_leaf_pages(toc))
        self.assertEqual(secs.get("Performance efficiency"),
                         ["performance-efficiency.html"])

    def test_generic_and_custom_pages_excluded(self):
        """Generic scaffolding (Resources/Definitions) and non-pillar custom
        sections (Te Ao Māori principles) are not captured."""
        toc = {"contents": [
            leaf("Definitions", "definitions.html"),
            leaf("Te Ao Māori principles", "te-ao-maori.html"),
            branch("Security", [
                leaf("MD_SEC 1 How is data protected?", "md_sec-1.html"),
                leaf("Resources", "md_sec-resources.html"),
            ]),
        ]}
        secs = sections(cwf.discover_leaf_pages(toc))
        self.assertEqual(secs, {"Security": ["md_sec-1.html"]})
        all_hrefs = {h for hs in secs.values() for h in hs}
        self.assertNotIn("definitions.html", all_hrefs)
        self.assertNotIn("te-ao-maori.html", all_hrefs)
        self.assertNotIn("md_sec-resources.html", all_hrefs)

    def test_american_spelling_unchanged(self):
        """Canonical US-English 'Cost optimization' still matches — the
        normalization must be additive, never altering existing behavior."""
        toc = {"contents": [
            branch("Cost optimization", [
                leaf("1 – Choose cost-effective resources", "co-1.html"),
            ]),
        ]}
        secs = sections(cwf.discover_leaf_pages(toc))
        self.assertEqual(secs.get("Cost optimization"), ["co-1.html"])


class TestLensPillarMergedWriter(unittest.TestCase):
    def test_groups_questions_by_pillar_and_guidance(self):
        """BP-style lens questions merge into one file per pillar; questions
        whose ID has no pillar (responsible-ai style) merge into guidance.md
        (issue #99)."""
        import tempfile
        from pathlib import Path

        def bp(bp_id, group=None):
            return {"bp_id": bp_id, "title": bp_id, "content": f"# {bp_id} body",
                    "url": "https://example.test/x.html", "group": group}

        questions = {
            "GENSEC01": [bp("GENSEC01-BP01", "Endpoint security")],
            "GENSEC02": [bp("GENSEC02-BP01"), bp("GENSEC02-BP02")],
            "GENCOST01": [bp("GENCOST01-BP01")],
            "RAIBR01": [bp("RAIBR01-BP01")],
        }
        with tempfile.TemporaryDirectory() as td:
            out = Path(td)
            written = cwf.write_output_lens_pillar_merged(questions, out, "generative-ai")
            self.assertEqual(written, 3)
            self.assertEqual(sorted(p.name for p in out.glob("*.md")),
                             ["cost-optimization.md", "guidance.md", "security.md"])

            sec = (out / "security.md").read_text()
            self.assertIn("**Pillar**: Security", sec)
            self.assertIn("**Questions**: 2", sec)
            for bp_id in ("GENSEC01-BP01", "GENSEC02-BP01", "GENSEC02-BP02"):
                self.assertIn(bp_id, sec)

            guidance = (out / "guidance.md").read_text()
            self.assertIn("Generative AI Lens — Guidance", guidance)
            self.assertIn("RAIBR01-BP01", guidance)
            self.assertNotIn("**Pillar**:", guidance.split("---")[0])


if __name__ == "__main__":
    unittest.main()
