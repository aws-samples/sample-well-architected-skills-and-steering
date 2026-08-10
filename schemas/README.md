# wa-review structured output schema

`wa-review-v1.schema.json` is the versioned contract for `wa-review.json`, the machine-readable
artifact the [`wa-review`](../skills/wa-review/SKILL.md) skill emits alongside its markdown report.
It exists so downstream tools consume a stable shape instead of parsing prose:

- [`tools/wa-ci`](../tools/wa-ci/) diffs a review against a committed baseline and gates a PR.
- `wa-portfolio` (proposed, [#89](https://github.com/aws-samples/sample-well-architected-skills-and-steering/issues/89)) aggregates many reviews into a fleet view.
- A future WA Tool import can map findings into the AWS console.

Build the artifact once; several features follow.

## Versioning

The filename carries the major version (`-v1`) and the document repeats it in `schema_version`.
This is a published contract: external tools depend on it, so treat changes with care.

- **Backward-compatible change** (new optional field, a widened enum): bump the minor/patch in
  `schema_version`, keep the same file. Consumers keyed on the major version keep working.
- **Breaking change** (a required field, a removed/narrowed field): add
  `wa-review-v2.schema.json` and leave v1 in place until consumers migrate.

A consumer should read `schema_version` and reject a document whose major version it does not
support, rather than assume the shape.

## What the contract guarantees, and what it does not

- **Identity key.** A finding with a canonical `bp_id` (`PILLAR##-BP##`) is identified by it, and
  a baseline diff pairs on `bp_id`. Producers MUST use canonical IDs for these, never shorthand.
  This covers every core-framework BP and every lens that publishes BP IDs (most of them, e.g.
  `IOTCOST01-BP01`).
- **Advisory findings (no ID).** A handful of lenses are organized by topic and expose no BP IDs
  (serverless-applications, saas, government, healthcare-industry, container-build, sap,
  streaming-media; a couple of others mix ID'd and ID-less findings). Their findings carry a
  `title` instead of a `bp_id`. A `title` is NOT a stable identity key, so a diff does not pair on
  it: these findings are reported and counted but are **advisory only and never gate a build**.
  This is deliberate. Gating on an identity that can drift between reviews would make the gate
  noisy and untrustworthy. Every finding therefore has a `bp_id` OR a `title` (enforced by the
  schema's `anyOf`).
- **Coverage is not exhaustiveness.** `wa-review` measures F1 = 0.96, not 1.0. The absence of a
  finding is NOT proof a control exists. Every document carries a `recall_note` stating this, and
  `review_mode` tells a consumer how much was evaluated (a `score` or `pillar-scoped` run does not
  cover all 307 BPs). Gates MUST NOT read "no finding" as "implemented".
- **Every gap is rated.** A finding with a gap status (`not_implemented` /
  `partially_implemented`) MUST carry a non-null `severity`; the schema enforces this. A gate
  ranks by severity, so an unrated gap would fail open. Non-gap statuses (`implemented`,
  `not_applicable`, `cannot_determine`) may omit it. `tools/wa-ci` also fails closed on an unrated
  new or regressed gap as defense in depth.
- **Guidance, not code.** `recommendation` is prose guidance. Consistent with the repo's
  [design principles](../CONTRIBUTING.md), the artifact never contains a code diff.

## Validating a document

```bash
# With check-jsonschema (pip install check-jsonschema), or any Draft 2020-12 validator:
check-jsonschema --schemafile schemas/wa-review-v1.schema.json path/to/wa-review.json
```

A minimal valid document:

```json
{
  "schema_version": "1.0.0",
  "workload": "payments-api",
  "date": "2026-08-06",
  "review_mode": "full",
  "skill_version": "2.2.0",
  "run_id": "2026-08-06T14-02-payments-api",
  "pillar_scores": { "security": 3, "reliability": 2 },
  "findings": [
    {
      "bp_id": "SEC08-BP01",
      "pillar": "security",
      "status": "not_implemented",
      "severity": "high",
      "evidence": { "file": "infra/s3.tf", "line": 14 },
      "effort": "low",
      "recommendation": "Enable SSE and BlockPublicAccess on the uploads bucket."
    }
  ],
  "recall_note": "Full review, F1 approx 0.96. High recall but not exhaustive; absence of a finding is not proof of implementation."
}
```

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
