# wa-ci: continuous Well-Architected gating

`wa_ci.py` diffs a fresh `aws-well-architected-framework-review.json` against a committed baseline and gates a pull request
on the Well-Architected delta. A review is a point-in-time snapshot; this turns it into a
tripwire, so a change that erodes the workload's posture fails the build instead of landing
silently.

It consumes the structured output the [`aws-well-architected-framework-review`](../../skills/aws-well-architected-framework-review/SKILL.md) skill emits
(Step 6b), validated by [`schemas/aws-well-architected-framework-review-v1.schema.json`](../../schemas/aws-well-architected-framework-review-v1.schema.json).

- **Stdlib only.** No third-party packages, no AWS credentials, no network. Runs on any Python 3.8+.
- **Reports and gates. Never mutates code**, consistent with the repo's
  [design principles](../../CONTRIBUTING.md).

## How the delta is classified

Findings pair on `bp_id` (the contract's identity key). Each changed BP is one of:

| Class | Meaning | Gates the build? |
|-------|---------|------------------|
| **Resolved** | A baseline gap the current review explicitly marks `implemented` or `not_applicable`. | No |
| **Still-open** | A gap in the baseline that is still a gap now. | No (pre-existing) |
| **New** | A gap now that the baseline did not record as a gap (absent, or `cannot_determine`). | Yes, at/above `--fail-on` |
| **Regressed** | A BP the baseline marked passing that is now a gap. | Yes, at/above `--fail-on` |

Three rules keep the gate honest, all drawn from the schema's coverage guarantees:

- **Absence is never a pass.** A baseline gap that simply drops out of the current review (for
  example, a narrower `review_mode` did not evaluate it) is NOT counted as Resolved. Resolution
  requires the BP to be present and explicitly passing.
- **`cannot_determine` is neither.** It is not a confirmed gap and not proof of a control, so a
  BP going from `cannot_determine` to a gap is New, not Regressed.
- **Advisory findings never gate.** A few lenses are topic-organized and expose no BP ID
  (serverless-applications, saas, government, healthcare-industry, container-build, sap,
  streaming-media, plus some mixed cases). Their findings carry a `title` instead of a `bp_id`.
  A title is not a stable identity key, so the diff cannot pair it across reviews. These gaps are
  counted and printed under an "Advisory" heading so coverage stays visible, but they never fail
  the build. Gating on a key that can drift between reviews would make the gate noisy.

Only New and Regressed findings can fail the build: they are what *this change* introduced.
Still-open gaps are pre-existing and must not block an unrelated PR; fix them deliberately, then
refresh the baseline.

## Usage

```bash
# Gate a PR: fail on any new or regressed finding at High or above (the default).
python3 tools/wa-ci/wa_ci.py \
  --baseline .well-architected/baseline.json \
  --current aws-well-architected-framework-review.json \
  --fail-on high

# Report the full delta without ever failing (useful on a warn-only branch).
python3 tools/wa-ci/wa_ci.py --baseline baseline.json --current aws-well-architected-framework-review.json --fail-on none

# Emit the classified delta as JSON (for a bot comment, a dashboard, wa-portfolio).
python3 tools/wa-ci/wa_ci.py --baseline baseline.json --current aws-well-architected-framework-review.json --json

# Accept a new review as the baseline (run after a review is reviewed and merged).
python3 tools/wa-ci/wa_ci.py --current aws-well-architected-framework-review.json --update-baseline .well-architected/baseline.json
```

`--fail-on` accepts `low`, `medium`, `high` (default), `critical`, or `none`. The process exits
`1` when the gate fails and `0` otherwise.

### Coverage warnings

The report flags conditions that make a delta less trustworthy rather than failing silently:

- the schema major version changed between baseline and current,
- the current review is narrower than the baseline (e.g. `quick` vs `full`), so some baseline
  gaps were not re-evaluated. Those are held as Still-open, never silently Resolved, or
- a baseline gap is now `cannot_determine`. It drops from the delta (neither Still-open nor
  Resolved, since `cannot_determine` is not a pass), so `Still open` can undercount. This never
  fails open; the warning names the affected BPs so the drop is visible.

## Wiring it into CI

See [`examples/github-actions-wa-gate.yml`](examples/github-actions-wa-gate.yml) for a GitHub
Actions workflow. `aws-well-architected-framework-review` runs inside an AI coding agent, not a headless runner, so teams
typically generate `aws-well-architected-framework-review.json` as part of the change (and commit it or attach it as an
artifact) rather than invoking the skill in CI. The gate job only diffs two JSON documents.

Recommended flow:

1. Run a full `aws-well-architected-framework-review`, accept it, and commit the emitted `aws-well-architected-framework-review.json` as
   `.well-architected/baseline.json`.
2. For each PR, produce a fresh `aws-well-architected-framework-review.json` for the change and run `wa_ci.py` against the
   baseline.
3. When you deliberately close gaps, refresh the baseline with `--update-baseline` so Still-open
   counts shrink over time.

## Running the tests

```bash
python3 -m unittest tools/wa-ci/test_wa_ci.py
# or, from this directory:
cd tools/wa-ci && python3 -m pytest test_wa_ci.py -q
```

The tests are stdlib `unittest` with no external dependencies, kept separate from the Bedrock
eval harness in [`evals/`](../../evals/) (which needs Python 3.13 + boto3). They cover every
delta class, the two absence rules, the severity threshold behavior, coverage warnings, and the
process exit codes.

## Try it against the examples

[`examples/`](examples/) holds a `baseline.json` and a later `aws-well-architected-framework-review.json` for the same
workload. Running the gate against them produces one Resolved, one New (critical), one Regressed
(high), two Still-open findings, and one Advisory (a serverless-lens finding with no BP ID, shown
but not gated), and exits `1`:

```bash
python3 tools/wa-ci/wa_ci.py \
  --baseline tools/wa-ci/examples/baseline.json \
  --current tools/wa-ci/examples/aws-well-architected-framework-review.json \
  --fail-on high
```

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
