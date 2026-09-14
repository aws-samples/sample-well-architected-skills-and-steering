#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#
# Fail if a tracked file publishes a measurement result.
#
# This repository ships the measurement tooling and tells you how to run it. It
# does not publish result figures or result datasets — no F1 scores, skill-lift
# deltas, per-run costs, throughput numbers, or head-to-head model tables. See
# CONTRIBUTING.md, "Measurement results stay local".
#
# Scope: `git ls-files` only. Your local runs write into gitignored paths
# (evals/results/, evals/cli_effectiveness/*.json, evals/pricing.local.yaml) and
# are never scanned — measure freely, just do not commit the numbers.
#
# Deliberately NOT scanned:
#   skills/*/references/** and powers/*/steering/references/**
#     AWS Well-Architected Framework and lens documentation is reproduced
#     verbatim there. Its figures are AWS's own published statements; rewording
#     them here would be worse than leaving them intact.
#   *.lock
#     Machine-generated hashes and version pins. Nothing authored, and the hex
#     collides with every numeric pattern below.
#
# Usage: bash scripts/check-no-published-metrics.sh

set -uo pipefail

cd "$(dirname "$0")/.." || exit 2

SELF="scripts/check-no-published-metrics.sh"
status=0

# Tracked, non-binary files, minus the verbatim AWS reference corpora and this
# script (which necessarily spells out every pattern it looks for).
# (read -d '' rather than mapfile: this must also run on the bash 3.2 that
# ships with macOS.)
FILES=()
while IFS= read -r -d '' f; do
  FILES+=("$f")
done < <(
  git ls-files -z \
    | grep -zv '^skills/[^/]*/references/' \
    | grep -zv '^powers/[^/]*/steering/references/' \
    | grep -zv '\.lock$' \
    | grep -zv "^${SELF}\$"
)

if [ "${#FILES[@]}" -eq 0 ]; then
  echo "check-no-published-metrics: no tracked files to scan" >&2
  exit 2
fi

# Same list, minus shell/PowerShell scripts — `$1` there is a positional
# parameter, not a dollar amount.
NON_SHELL=()
for f in "${FILES[@]}"; do
  case "$f" in
    *.sh | *.ps1) ;;
    *) NON_SHELL+=("$f") ;;
  esac
done

# scan <label> <extended-regex> [file...]  (case-insensitive)
# Reports every match and flips the exit status. Patterns require a LITERAL
# number, so harness code that computes and prints a metric at runtime
# (`f"F1={rep['f1']:.3f}"`, `recall = len(tp) / len(gt_bps)`) stays clean.
scan() {
  local label="$1" pattern="$2"
  shift 2
  local hits
  hits=$(grep -nIEi "$pattern" "$@" 2>/dev/null)
  if [ -n "$hits" ]; then
    printf '\n✗ %s\n' "$label"
    printf '%s\n' "$hits" | sed 's/^/    /'
    status=1
  fi
}

# SEP: prose between a metric word and its number. Excluding quotes, braces and
# angle brackets is what keeps f-string format specs — `{r['accuracy']:>8.0%}`,
# `f"F1={rep['f1']:.3f}"` — out of the results below.
SEP="[^0-9'\"{}<>|]"
# METRIC: the vocabulary a result gets reported in. `with skill (0.96)` slipped
# past an earlier version of this list, hence baseline/skill/delta/score.
METRIC="F1|f1_score|recall|precision|lift|retention|coverage|accuracy|baseline|with[- ]skill|delta|score|p-value"

scan "Measured score stated as fact (delete the figure, keep the method)" \
  "(${METRIC})${SEP}{0,24}[0-9]*\.[0-9][0-9]|[0-9]*\.[0-9][0-9]${SEP}{0,24}(${METRIC})" \
  "${FILES[@]}"

scan "Percentage result for a measured metric" \
  "[0-9]+(\.[0-9]+)? *% *(${METRIC})|(${METRIC})${SEP}{0,12}[0-9]+(\.[0-9]+)? *%([^}]|\$)" \
  "${FILES[@]}"

scan "Speedup multiplier" \
  '[0-9]+(\.[0-9]+)? *x *(faster|slower|speedup|more|better)' \
  "${FILES[@]}"

scan "Measured throughput" \
  '[0-9]+(\.[0-9]+)? *(tokens/s|tok/s|tokens per second)' \
  "${FILES[@]}"

scan "Per-run cost figure (link the provider's pricing page instead)" \
  '\$[0-9]+(\.[0-9]+)? *[kKmM]? *(/|per +)(run|invocation|review|assessment|M tokens|million tokens)' \
  "${NON_SHELL[@]}"

scan "Unreleased endpoint hostname" \
  'bedrock-mantle' \
  "${FILES[@]}"

scan "Amazon-internal service name" \
  'BPVendingService' \
  "${FILES[@]}"

# A rate card carries no metric word, so the patterns above cannot see it. Rates
# belong in the gitignored evals/pricing.local.yaml; the tracked .example ships
# them all as null.
for f in "${FILES[@]}"; do
  case "$f" in
    *.yaml | *.yml | *.json)
      [ "$f" = "evals/pricing.local.yaml.example" ] && continue
      hits=$(grep -nE '^ *(input|output|cache_read|cache_write|input_cost|output_cost|price_per_[a-z_]+) *: *[0-9]' "$f")
      if [ -n "$hits" ]; then
        printf "\n✗ Per-token rate card is tracked (move it to evals/pricing.local.yaml)\n"
        printf '%s\n' "$hits" | sed "s|^|    ${f}:|"
        status=1
      fi
      ;;
  esac
done

# Result artifacts must not be tracked at all.
results=$(printf '%s\n' "${FILES[@]}" | grep -E '^evals/results/|^evals/pricing\.local\.yaml$')
if [ -n "$results" ]; then
  printf '\n✗ Result artifact is tracked (git rm --cached it; it is gitignored)\n'
  printf '%s\n' "$results" | sed 's/^/    /'
  status=1
fi

# Ground-truth fixtures carry only what the scorers read. Per-run panel
# measurements (latency, tokens, raw output, per-model frequencies) belong in
# the gitignored panel/ directory.
for f in "${FILES[@]}"; do
  case "$f" in
    */ground_truth/*.json)
      hits=$(grep -nE '"(raw_runs|panel_runs|per_model_bp_frequency|latency_s|output_tokens|input_tokens|cost_usd)"' "$f")
      if [ -n "$hits" ]; then
        printf '\n✗ Ground-truth fixture carries panel measurements, not just scorer inputs\n'
        printf '%s\n' "$hits" | sed "s|^|    ${f}:|"
        status=1
      fi
      ;;
  esac
done

if [ "$status" -ne 0 ]; then
  cat >&2 <<'EOF'

This repository publishes the measurement tooling, not its results. Describe
what the harness measures and how to run it; do not state a figure it produced.
If a match above is a false positive, narrow the pattern in
scripts/check-no-published-metrics.sh rather than adding a blanket exclusion.
EOF
  exit 1
fi

echo "✓ no published measurement results in tracked files"
