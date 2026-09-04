# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Offline tests for the lens RAE data generator's pure helpers.

These do not invoke the Claude Code CLI; they exercise only lens-metadata
derivation and prompt construction against the real lens reference files.
"""

import sys
from pathlib import Path

import pytest

CLI_DIR = Path(__file__).parent.parent / "cli_effectiveness"
sys.path.insert(0, str(CLI_DIR))

import measure_lens_rae as lens  # noqa: E402

VALID_PREFIXES = {"OPS", "SEC", "REL", "PERF", "COST", "SUS"}


def test_covered_pillars_are_valid_core_prefixes():
    pillars = lens.lens_covered_pillars("generative-ai")
    assert pillars, "generative-ai lens should span at least one pillar"
    assert set(pillars) <= VALID_PREFIXES
    assert pillars == sorted(pillars)  # deterministic, sorted


def test_lens_bp_universe_nonempty():
    universe = lens.lens_bp_universe("generative-ai")
    assert universe
    # generative-ai uses the GEN* BP-per-file layout
    assert any(bp.startswith("GEN") for bp in universe)


def test_unknown_lens_raises():
    with pytest.raises(SystemExit):
        lens.lens_covered_pillars("no-such-lens")


def test_se_preamble_injects_lens_and_keeps_workload_marker():
    se = lens._preamble("generative-ai", lens_on=True)
    assert "apply the generative-ai lens" in se
    assert "===== WORKLOAD =====" in se
    # instruction must come before the workload block
    assert se.index("generative-ai lens") < se.index("===== WORKLOAD =====")


def test_sd_preamble_suppresses_lens():
    sd = lens._preamble("generative-ai", lens_on=False)
    assert "Do NOT apply any lens" in sd
    assert "===== WORKLOAD =====" in sd


def test_parser_requires_lens_and_cases():
    args = lens.build_parser().parse_args(["--lens", "generative-ai", "--cases", "5"])
    assert args.lens == "generative-ai"
    assert args.cases == [5]
    assert args.arm == "both"
