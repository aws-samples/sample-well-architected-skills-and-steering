#!/usr/bin/env bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# One-liner remote installer for Well-Architected Skills & Steering
# Usage: curl -sL https://raw.githubusercontent.com/aws-samples/sample-well-architected-skills-and-steering/main/bootstrap.sh | bash -s -- --tool claude-code ~/my-project
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
bash "$TMPDIR/install.sh" "$@"
