# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Offline test for the MCP tool-call counter used as the RAE conditioning signal."""

import json
import sys
from pathlib import Path

CLI_DIR = Path(__file__).parent.parent / "cli_effectiveness"
sys.path.insert(0, str(CLI_DIR))

import measure_aws_knowledge_mcp as mcp  # noqa: E402


def _assistant_event(*tool_names: str) -> dict:
    content = [{"type": "text", "text": "thinking"}]
    for name in tool_names:
        content.append({"type": "tool_use", "name": name, "input": {}})
    return {"type": "assistant", "message": {"content": content}}


def test_count_mcp_calls_main_and_subagents(tmp_path):
    session = tmp_path / "abc.jsonl"
    session.write_text(
        "\n".join(json.dumps(e) for e in [
            _assistant_event("mcp__aws-knowledge__search"),
            _assistant_event("Read"),  # not MCP
            _assistant_event("mcp__aws-knowledge__read", "Grep"),
        ])
    )
    # subagent transcript under {stem}/subagents/
    sub_dir = tmp_path / "abc" / "subagents"
    sub_dir.mkdir(parents=True)
    (sub_dir / "agent-1.jsonl").write_text(
        json.dumps(_assistant_event("mcp__aws-knowledge__list"))
    )
    # 2 in main + 1 in subagent = 3
    assert mcp._count_mcp_calls(str(session)) == 3


def test_count_mcp_calls_missing_or_none():
    assert mcp._count_mcp_calls(None) == 0
    assert mcp._count_mcp_calls("/nonexistent/path.jsonl") == 0


def test_count_mcp_calls_ignores_non_mcp_tools(tmp_path):
    session = tmp_path / "s.jsonl"
    session.write_text(json.dumps(_assistant_event("Read", "Grep", "Bash")))
    assert mcp._count_mcp_calls(str(session)) == 0
