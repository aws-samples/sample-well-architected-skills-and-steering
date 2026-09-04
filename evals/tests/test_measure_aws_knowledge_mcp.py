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


def test_count_retrieval_calls_main_and_subagents(tmp_path):
    session = tmp_path / "abc.jsonl"
    session.write_text(
        "\n".join(json.dumps(e) for e in [
            _assistant_event("mcp__aws-knowledge__search"),
            _assistant_event("Read"),  # not retrieval
            _assistant_event("mcp__aws-knowledge__read", "WebFetch"),
        ])
    )
    # subagent transcript under {stem}/subagents/
    sub_dir = tmp_path / "abc" / "subagents"
    sub_dir.mkdir(parents=True)
    (sub_dir / "agent-1.jsonl").write_text(
        json.dumps(_assistant_event("mcp__aws-knowledge__list"))
    )
    got = mcp._count_retrieval_calls(str(session))
    # 3 MCP (2 main + 1 subagent) + 1 WebFetch
    assert got["mcp_tool_calls"] == 3
    assert got["webfetch_calls"] == 1
    assert got["retrieval_tool_calls"] == 4


def test_count_retrieval_calls_missing_or_none():
    for arg in (None, "/nonexistent/path.jsonl"):
        got = mcp._count_retrieval_calls(arg)
        assert got == {"mcp_tool_calls": 0, "webfetch_calls": 0, "retrieval_tool_calls": 0}


def test_count_retrieval_calls_webfetch_fallback(tmp_path):
    # MCP server did not register: only WebFetch retrieval fired.
    session = tmp_path / "s.jsonl"
    session.write_text(json.dumps(_assistant_event("WebFetch", "WebFetch", "Bash")))
    got = mcp._count_retrieval_calls(str(session))
    assert got["mcp_tool_calls"] == 0
    assert got["webfetch_calls"] == 2
    assert got["retrieval_tool_calls"] == 2


def test_count_retrieval_calls_ignores_non_retrieval_tools(tmp_path):
    session = tmp_path / "s.jsonl"
    session.write_text(json.dumps(_assistant_event("Read", "Grep", "Bash")))
    got = mcp._count_retrieval_calls(str(session))
    assert got["retrieval_tool_calls"] == 0
