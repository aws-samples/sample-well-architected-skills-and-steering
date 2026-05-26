#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# One-liner remote installer for Well-Architected Skills & Steering
# Usage: curl -sL https://raw.githubusercontent.com/aws-samples/sample-well-architected-skills-and-steering/main/bootstrap.sh | bash
# Defaults to --tool auto in current directory (auto-detects installed AI tools)
set -euo pipefail

REPO_URL="https://github.com/aws-samples/sample-well-architected-skills-and-steering/tarball/main"
TMPDIR_PREFIX="wa-skills-install"

cleanup() {
  [[ -n "${TMPDIR:-}" ]] && rm -rf "$TMPDIR"
}
trap cleanup EXIT

TMPDIR="$(mktemp -d -t "$TMPDIR_PREFIX.XXXXXX")"

echo "Downloading Well-Architected Skills & Steering..."
curl -sL "$REPO_URL" | tar xz -C "$TMPDIR" --strip-components=1

echo "Running installer..."
if [[ $# -eq 0 ]]; then
  bash "$TMPDIR/install.sh" --tool auto --force
else
  bash "$TMPDIR/install.sh" "$@"
fi
