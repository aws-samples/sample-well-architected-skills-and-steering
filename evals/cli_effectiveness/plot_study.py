#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Generate visualization charts for the MCP vs Static Retrieval Study.

Produces docs/study/ with:
  fig1_recall_evolution.png   — Dec 2025 -> Jul 2026 recall lift timeline
  fig2_three_way.png          — Three-way bar chart per case (3 approaches)
  fig3_plateau.png            — Agent-style plateau vs exhaustive vs static
  fig4_token_economy.png      — Cost vs recall scatter with labels
  fig5_model_benchmark.png    — Model quality vs cost
  fig6_compression.png        — v2.1 vs v2.2 report F1 before/after
"""
from __future__ import annotations

import json
import statistics
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
DOCS_DIR = REPO_ROOT / "docs" / "study"

# -- Okabe-Ito colorblind-safe palette --------------------------------------
OI = {
    "orange":     "#E69F00",
    "sky":        "#56B4E9",
    "green":      "#009E73",
    "yellow":     "#F0E442",
    "blue":       "#0072B2",
    "vermillion": "#D55E00",
    "purple":     "#CC79A7",
    "black":      "#000000",
    "grey":       "#4A5568",
}

# Amazon Ember font (falls back gracefully)
_AVAILABLE = {f.name for f in fm.fontManager.ttflist}
_HAS_EMBER = "Amazon Ember" in _AVAILABLE
if _HAS_EMBER:
    plt.rcParams["font.family"] = "Amazon Ember"
FONT_DISPLAY = "Amazon Ember Display" if "Amazon Ember Display" in _AVAILABLE else "sans-serif"
FONT_MONO    = "Amazon Ember Mono"    if "Amazon Ember Mono"    in _AVAILABLE else "monospace"

MCP_DATA_FILE = SCRIPT_DIR / "mcp_effectiveness.json"
V21_MEANS = {1: 0.62, 2: 0.95, 3: 0.51, 4: 0.21, 5: 0.74, 6: 0.35}  # wa-review v2.1
V22_MEANS = {1: 0.947, 2: 0.998, 3: 0.968, 4: 0.955, 5: 0.936, 6: 0.958}  # wa-review v2.2


def load_mcp() -> dict:
    return json.loads(MCP_DATA_FILE.read_text())


# -- Figure 1: Recall evolution timeline ------------------------------------
def fig1_recall_evolution() -> None:
    """Shows the jump from Dec 2025 to Jul 2026 across approaches."""
    fig, ax = plt.subplots(figsize=(12, 6))

    approaches = [
        "AWS Knowledge MCP\n(Dec 2025, Claude)", "AWS Knowledge MCP\n(Dec 2025, ChatGPT)",
        "BPVendingService\nagent-style (Jul 2026)", "BPVendingService\nexhaustive (Jul 2026)",
        "wa-review v2.1\n(static + dispatch)", "wa-review v2.2\n(static + dispatch + ledger)",
    ]
    recalls = [0.024, 0.225, 0.070, 0.997, 0.53, 0.960]
    colors = [OI["vermillion"], OI["orange"], OI["sky"], OI["green"], OI["blue"], OI["blue"]]
    alphas = [1, 1, 1, 1, 0.55, 1]

    bars = ax.barh(approaches, recalls,
                   color=colors, alpha=1)
    for bar, alpha in zip(bars, alphas):
        bar.set_alpha(alpha)

    ax.set_xlim(0, 1.12)
    ax.set_xlabel("Recall vs ground truth (fraction of applicable BPs surfaced)")
    ax.set_title("Recall evolution: December 2025 -> July 2026",
                 family=FONT_DISPLAY, fontsize=14, weight="bold")
    ax.axvline(1.0, color=OI["grey"], linestyle=":", linewidth=0.9)

    for bar, val in zip(bars, recalls):
        ax.text(val + 0.01, bar.get_y() + bar.get_height() / 2,
                f"{val:.1%}", va="center", fontsize=10, color=OI["grey"])

    ax.grid(axis="x", alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)

    # Bracket annotations
    ax.annotate("", xy=(0.997, 4), xytext=(0.024, 4),
                arrowprops=dict(arrowstyle="<->", color=OI["grey"], lw=1.2))
    ax.text(0.50, 3.65, "+97% recall (data quality fix)", ha="center",
            fontsize=8.5, color=OI["grey"], style="italic")
    ax.annotate("", xy=(0.960, 5), xytext=(0.53, 5),
                arrowprops=dict(arrowstyle="<->", color=OI["green"], lw=1.2))
    ax.text(0.745, 5.35, "+43% (assembler fix)", ha="center",
            fontsize=8.5, color=OI["green"], style="italic")

    fig.tight_layout()
    out = DOCS_DIR / "fig1_recall_evolution.png"
    fig.savefig(out, dpi=130)
    plt.close(fig)
    print(f"  {out.name}")


# -- Figure 2: Three-way per-case bar chart ---------------------------------
def fig2_three_way() -> None:
    """F1 for each of 6 cases across 3 approaches."""
    mcp = load_mcp()
    exhaustive = [c["aggregate"]["exhaustive"]["f1"]["mean"] for c in mcp["cases"]]
    agent      = [c["aggregate"]["agent_style"]["f1"]["mean"] for c in mcp["cases"]]
    wa22       = [V22_MEANS[i+1] for i in range(6)]
    labels = [f"Case {i+1}" for i in range(6)]
    x = np.arange(6)
    w = 0.25

    fig, ax = plt.subplots(figsize=(13, 6))
    ax.bar(x - w, agent,      w, label="MCP agent-style",     color=OI["vermillion"])
    ax.bar(x,     exhaustive, w, label="MCP exhaustive sweep", color=OI["orange"])
    ax.bar(x + w, wa22,       w, label="wa-review v2.2",       color=OI["blue"])

    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.12)
    ax.set_ylabel("F1 score")
    ax.set_title("F1 by case: three approaches compared",
                 family=FONT_DISPLAY, fontsize=14, weight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.10), ncol=3, frameon=False)
    ax.grid(axis="y", alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    out = DOCS_DIR / "fig2_three_way.png"
    fig.savefig(out, dpi=130)
    plt.close(fig)
    print(f"  {out.name}")


# -- Figure 3: The plateau --------------------------------------------------
def fig3_plateau() -> None:
    """Shows the plateau: naive agent vs systematic coverage."""
    fig, ax = plt.subplots(figsize=(10, 5.5))

    categories = [
        "Dec 2025\nAWS Knowledge\nMCP (Claude)",
        "Dec 2025\nAWS Knowledge\nMCP (ChatGPT)",
        "Jul 2026\nBPVendingService\nagent-style",
        "Jul 2026\nBPVendingService\nexhaustive",
        "Jul 2026\nwa-review v2.1\n(skill only)",
        "Jul 2026\nwa-review v2.2\n(skill + ledger)",
    ]
    recalls   = [0.024, 0.225, 0.070, 0.997, 0.530, 0.960]
    bp_counts = [int(r * 307) for r in recalls]
    colors    = [OI["vermillion"], OI["orange"], OI["sky"],
                 OI["green"],      OI["blue"],   OI["blue"]]

    bars = ax.bar(categories, bp_counts, color=colors)
    bars[4].set_alpha(0.5)

    ax.axhline(307, color=OI["grey"], linestyle=":", linewidth=0.9,
               label="307 canonical BPs")
    ax.set_ylabel("Best Practices surfaced (out of 307)")
    ax.set_title("The plateau: agent behavior determines coverage more than data quality",
                 family=FONT_DISPLAY, fontsize=13, weight="bold")
    ax.set_ylim(0, 360)

    for bar, count, recall in zip(bars, bp_counts, recalls):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 4,
                f"{count}\n({recall:.0%})", ha="center", fontsize=9, color=OI["grey"])

    # Plateau annotation
    ax.annotate("Plateau zone\n(agent stops when\n'enough' found)",
                xy=(1.0, 70), xytext=(1.5, 160),
                arrowprops=dict(arrowstyle="->", color=OI["vermillion"]),
                fontsize=8.5, color=OI["vermillion"])

    ax.grid(axis="y", alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper left", frameon=False)
    fig.tight_layout()
    out = DOCS_DIR / "fig3_plateau.png"
    fig.savefig(out, dpi=130)
    plt.close(fig)
    print(f"  {out.name}")


# -- Figure 4: Token economy ------------------------------------------------
def fig4_token_economy() -> None:
    """Cost vs recall scatter with labeled annotations."""
    fig, ax = plt.subplots(figsize=(10, 7))

    points = [
        ("AWS Knowledge MCP\n(Claude, Dec 2025)",    2.27,  0.024, OI["vermillion"], 80),
        ("AWS Knowledge MCP\n(ChatGPT, Dec 2025)",   0.56,  0.225, OI["orange"],     80),
        ("BPVendingService\nagent-style",             0.01,  0.07,  OI["sky"],        80),
        ("BPVendingService\nexhaustive sweep",        0.01,  0.997, OI["green"],      80),
        ("wa-review v2.1\n(static + dispatch)",       4.00,  0.53,  OI["blue"],       60),
        ("wa-review v2.2\n(static + dispatch\n+ Full BP Ledger)", 7.00, 0.96, OI["blue"], 120),
    ]

    for label, cost, recall, color, size in points:
        ax.scatter(cost, recall, s=size, color=color, zorder=3,
                   edgecolor="white", linewidth=1.2)
        # Offset labels to avoid overlap
        dx, dy = 0.05, 0.02
        if "agent-style" in label:
            dx, dy = 0.05, -0.07
        if "exhaustive" in label:
            dx, dy = 0.05, 0.02
        if "v2.1" in label:
            dx, dy = 0.1, -0.07
        ax.annotate(label, (cost, recall), xytext=(cost + dx, recall + dy),
                    fontsize=7.5, color=OI["grey"],
                    arrowprops=dict(arrowstyle="-", color=OI["grey"], lw=0.6))

    ax.axhline(1.0, color=OI["grey"], linestyle=":", linewidth=0.8)
    ax.set_xlabel("Cost per review run (USD)")
    ax.set_ylabel("Recall vs ground truth")
    ax.set_title("Cost vs recall: not a simple trade-off",
                 family=FONT_DISPLAY, fontsize=13, weight="bold")
    ax.set_xlim(-0.3, 8.5)
    ax.set_ylim(-0.05, 1.15)
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)

    # Key insight annotation
    ax.text(0.02, 0.83, "High recall at near-zero cost\nrequires systematic sweep strategy,\nnot higher spend",
            fontsize=8.5, color=OI["green"],
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=OI["green"], alpha=0.8))

    fig.tight_layout()
    out = DOCS_DIR / "fig4_token_economy.png"
    fig.savefig(out, dpi=130)
    plt.close(fig)
    print(f"  {out.name}")


# -- Figure 5: Model benchmark ----------------------------------------------
def fig5_model_benchmark() -> None:
    """Quality vs cost for 12 Bedrock models."""
    models = [
        ("Claude Sonnet 5",        2.76,  5.0),
        ("GPT-5.5",                1.41,  5.0),
        ("GPT OSS 120B",           0.087, 5.0),
        ("Haiku 4.5",              0.54,  4.9),
        ("Claude Fable 5",         2.77,  4.8),
        ("DeepSeek R1",            0.74,  4.7),
        ("Amazon Nova Lite",       0.037, 4.2),
        ("Llama 4 Maverick 17B",   0.16,  4.1),
        ("Nova 2 Lite",            0.021, 4.1),
        ("Amazon Nova Pro",        0.50,  3.2),
        ("Pixtral Large",          0.66,  2.5),
        ("Llama 3.3 70B",          0.35,  1.5),
    ]

    fig, ax = plt.subplots(figsize=(11, 7))
    colors_map = {5.0: OI["blue"], 4.9: OI["blue"], 4.8: OI["blue"],
                  4.7: OI["green"], 4.2: OI["green"], 4.1: OI["green"],
                  3.2: OI["orange"], 2.5: OI["vermillion"], 1.5: OI["vermillion"]}

    for name, cost, quality in models:
        color = colors_map.get(quality, OI["grey"])
        ax.scatter(cost, quality, s=90, color=color, zorder=3,
                   edgecolor="white", linewidth=1.2)
        dy = 0.06 if quality < 4.7 else -0.12
        ax.annotate(name, (cost, quality), xytext=(cost + 0.03, quality + dy),
                    fontsize=7.5, color=OI["grey"])

    # Pareto-optimal zone annotation
    ax.fill_betweenx([4.8, 5.1], 0, 3.5, alpha=0.06, color=OI["blue"],
                     label="Top quality zone")
    ax.axhline(4.5, color=OI["grey"], linestyle="--", linewidth=0.7, alpha=0.5)
    ax.text(7, 4.52, "Quality threshold (4.5)", fontsize=8, color=OI["grey"])

    ax.set_xlabel("Cost per review run (USD, subagent mode)")
    ax.set_ylabel("Quality score (LLM-as-judge, 1–5)")
    ax.set_title("Model benchmark: quality vs cost on WA review tasks\n(Amazon Bedrock, 12 models, subagent mode)",
                 family=FONT_DISPLAY, fontsize=13, weight="bold")
    ax.set_ylim(1.0, 5.6)
    ax.set_xlim(-0.2, 8.5)
    ax.grid(alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False)

    fig.tight_layout()
    out = DOCS_DIR / "fig5_model_benchmark.png"
    fig.savefig(out, dpi=130)
    plt.close(fig)
    print(f"  {out.name}")


# -- Figure 6: v2.1 vs v2.2 before/after -----------------------------------
def fig6_compression() -> None:
    """Before/after: wa-review v2.1 vs v2.2 per case."""
    cases = list(range(1, 7))
    v21 = [V21_MEANS[c] for c in cases]
    v22 = [V22_MEANS[c] for c in cases]
    labels = [f"Case {c}" for c in cases]
    x = np.arange(6)
    w = 0.35

    fig, ax = plt.subplots(figsize=(11, 6))
    ax.bar(x - w/2, v21, w, label="wa-review v2.1 (report F1)", color=OI["orange"], alpha=0.8)
    ax.bar(x + w/2, v22, w, label="wa-review v2.2 (report F1)", color=OI["blue"])

    for i, (a, b) in enumerate(zip(v21, v22)):
        ax.annotate("", xy=(i + w/2, b + 0.02), xytext=(i - w/2, a + 0.02),
                    arrowprops=dict(arrowstyle="->", color=OI["green"], lw=1.2))
        ax.text(i, max(a, b) + 0.06, f"+{b-a:.2f}", ha="center",
                fontsize=8.5, color=OI["green"])

    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.22)
    ax.set_ylabel("Report F1 (what the user sees)")
    ax.set_title("Full BP Ledger impact: wa-review v2.1 -> v2.2\n(same subagents, same data; only assembler instructions changed)",
                 family=FONT_DISPLAY, fontsize=13, weight="bold")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=2, frameon=False)
    ax.grid(axis="y", alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)

    # Mean delta annotation
    mean_delta = statistics.mean(v22) - statistics.mean(v21)
    ax.text(0.02, 0.95, f"Mean F1 lift: +{mean_delta:.2f} (+{mean_delta/statistics.mean(v21):.0%})\nSame data, changed agent instructions only",
            transform=ax.transAxes, fontsize=9, color=OI["green"],
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=OI["green"], alpha=0.85))

    fig.tight_layout()
    out = DOCS_DIR / "fig6_compression.png"
    fig.savefig(out, dpi=130)
    plt.close(fig)
    print(f"  {out.name}")


# -- Summary grid ----------------------------------------------------------
def fig0_summary_grid() -> None:
    """2x3 summary grid for the document cover."""
    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    plt.subplots_adjust(hspace=0.55, wspace=0.32, bottom=0.06, top=0.93)

    # Reuse individual plot functions on axes
    def recall_evo(ax):
        approaches = [
            "AWS KnowledgeMCP (Claude, Dec 2025)",
            "AWS Knowledge MCP (ChatGPT, Dec 2025)",
            "BPVendingService agent-style",
            "BPVendingService exhaustive",
            "wa-review v2.1", "wa-review v2.2",
        ]
        recalls = [0.024, 0.225, 0.070, 0.997, 0.530, 0.960]
        colors  = [OI["vermillion"], OI["orange"], OI["sky"], OI["green"], OI["blue"], OI["blue"]]
        bars = ax.barh(approaches, recalls, color=colors)
        bars[4].set_alpha(0.5)
        ax.axvline(1.0, color=OI["grey"], linestyle=":", linewidth=0.8)
        ax.set_xlim(0, 1.15)
        for bar, val in zip(bars, recalls):
            ax.text(val + 0.01, bar.get_y() + bar.get_height()/2,
                    f"{val:.0%}", va="center", fontsize=7.5, color=OI["grey"])
        ax.set_title("Recall evolution", fontsize=11)
        ax.grid(axis="x", alpha=0.2); ax.spines[["top","right"]].set_visible(False)

    def three_way(ax):
        mcp = load_mcp()
        ex = [c["aggregate"]["exhaustive"]["f1"]["mean"] for c in mcp["cases"]]
        ag = [c["aggregate"]["agent_style"]["f1"]["mean"] for c in mcp["cases"]]
        wa = [V22_MEANS[i+1] for i in range(6)]
        x = np.arange(6); w = 0.25
        ax.bar(x-w, ag, w, color=OI["vermillion"], label="MCP naive")
        ax.bar(x,   ex, w, color=OI["orange"],     label="MCP exhaustive")
        ax.bar(x+w, wa, w, color=OI["blue"],        label="wa-review v2.2")
        ax.set_xticks(x); ax.set_xticklabels([f"C{i}" for i in range(1,7)])
        ax.set_ylim(0, 1.12); ax.set_title("F1 by case", fontsize=11)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5,-0.18), ncol=3, frameon=False, fontsize=8)
        ax.grid(axis="y", alpha=0.2); ax.spines[["top","right"]].set_visible(False)

    def before_after(ax):
        cases = list(range(1,7)); x = np.arange(6); w = 0.35
        v21 = [V21_MEANS[c] for c in cases]
        v22 = [V22_MEANS[c] for c in cases]
        ax.bar(x-w/2, v21, w, color=OI["orange"], alpha=0.8, label="v2.1")
        ax.bar(x+w/2, v22, w, color=OI["blue"], label="v2.2")
        ax.set_xticks(x); ax.set_xticklabels([f"C{i}" for i in range(1,7)])
        ax.set_ylim(0, 1.2); ax.set_title("v2.1 -> v2.2 (Full BP Ledger)", fontsize=11)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5,-0.18), ncol=2, frameon=False, fontsize=8)
        ax.grid(axis="y", alpha=0.2); ax.spines[["top","right"]].set_visible(False)

    def cost_recall(ax):
        pts = [
            ("AWS Knwl MCP\n(Claude)", 2.27, 0.024, OI["vermillion"]),
            ("AWS Knwl MCP\n(GPT)",    0.56, 0.225, OI["orange"]),
            ("BPV agent",              0.01, 0.07,  OI["sky"]),
            ("BPV exhaustive",         0.01, 0.997, OI["green"]),
            ("wa-review v2.1",         4.00, 0.53,  OI["blue"]),
            ("wa-review v2.2",         7.00, 0.96,  OI["blue"]),
        ]
        for name, cost, recall, color in pts:
            ax.scatter(cost, recall, s=60, color=color, zorder=3, edgecolor="white", linewidth=1)
            ax.annotate(name, (cost, recall), xytext=(cost+0.1, recall-0.07),
                        fontsize=6.5, color=OI["grey"])
        ax.axhline(1.0, color=OI["grey"], linestyle=":", linewidth=0.7)
        ax.set_xlabel("Cost (USD)"); ax.set_ylabel("Recall")
        ax.set_title("Cost vs recall", fontsize=11)
        ax.set_xlim(-0.5, 9); ax.set_ylim(-0.1, 1.2)
        ax.grid(alpha=0.2); ax.spines[["top","right"]].set_visible(False)

    def model_bench(ax):
        models_bench = [
            ("Sonnet 5",    2.76, 5.0), ("GPT-5.5",  1.41, 5.0), ("GPT OSS", 0.09, 5.0),
            ("Haiku 4.5",   0.54, 4.9), ("Fable 5",  2.77, 4.8), ("R1",      0.74, 4.7),
            ("Nova Lite",   0.04, 4.2), ("Nova 2 L", 0.02, 4.1), ("Nova Pro",0.50, 3.2),
        ]
        for name, cost, q in models_bench:
            color = OI["blue"] if q >= 4.8 else OI["green"] if q >= 4.5 else OI["orange"] if q >= 3.5 else OI["vermillion"]
            ax.scatter(cost, q, s=55, color=color, zorder=3, edgecolor="white", linewidth=1)
            ax.annotate(name, (cost, q), xytext=(cost+0.05, q-0.1), fontsize=6.5, color=OI["grey"])
        ax.axhline(4.5, color=OI["grey"], linestyle="--", linewidth=0.6, alpha=0.6)
        ax.set_xlabel("Cost (USD)"); ax.set_ylabel("Quality (1–5)")
        ax.set_title("Model benchmark", fontsize=11)
        ax.set_ylim(1, 5.6); ax.set_xlim(-0.2, 3.5)
        ax.grid(alpha=0.2); ax.spines[["top","right"]].set_visible(False)

    def summary_text(ax):
        ax.axis("off")
        text = (
            "From 2% to 100% Recall\n"
            f"{'-'*28}\n"
            "Dec 2025 (AWS Knwl MCP):\n"
            "  Claude: 2.4% | ChatGPT: 22.5%\n\n"
            "Jul 2026 — BPVendingService:\n"
            "  Naive agent: 7% recall\n"
            "  Exhaustive:  99.7% recall\n\n"
            "Jul 2026 — wa-review v2.2:\n"
            "  Report F1:  0.960\n"
            "  Recall:     1.00\n\n"
            "Key insight:\n"
            "  Data quality ≠ recall\n"
            "  Coverage strategy = recall"
        )
        ax.text(0.05, 0.95, text, transform=ax.transAxes, va="top",
                family="Amazon Ember Mono" if "Amazon Ember Mono" in _AVAILABLE else "monospace",
                fontsize=9)

    recall_evo(axes[0, 0])
    three_way(axes[0, 1])
    before_after(axes[0, 2])
    cost_recall(axes[1, 0])
    model_bench(axes[1, 1])
    summary_text(axes[1, 2])

    fig.suptitle("MCP vs Static Retrieval: AWS Well-Architected Review Quality Study (Jul 2026)",
                 fontsize=14, weight="bold", family=FONT_DISPLAY, y=0.97)
    out = DOCS_DIR / "fig0_summary_grid.png"
    fig.savefig(out, dpi=130)
    plt.close(fig)
    print(f"  {out.name}")


def main() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    print("Generating study visualizations...")
    fig0_summary_grid()
    fig1_recall_evolution()
    fig2_three_way()
    fig3_plateau()
    fig4_token_economy()
    fig5_model_benchmark()
    fig6_compression()
    print(f"Done. All charts in {DOCS_DIR.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
