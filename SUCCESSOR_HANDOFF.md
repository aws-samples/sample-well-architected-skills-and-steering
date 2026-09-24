# AWS Agent Toolkit successor handoff

## Status

This repository remains the active portable skill package until the [Agent
Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws) successor passes the gates below. Supersession changes the execution
engine; it does not discard the public contracts, evidence rules, fixtures, or
evaluation history maintained here.

## Ownership boundary

This repository owns:

- Tool-agnostic skill behavior and evidence-sufficiency rules
- Canonical BP and lens reference snapshots
- Versioned structured-output schemas
- Deterministic fixtures, annotation workflow, and quality metrics
- Runtime adapters and matched control/treatment evaluation harnesses
- Historical releases and migration notes

The successor owns:

- Live AWS documentation and knowledge retrieval
- Agent Toolkit orchestration and tool integration
- Runtime-specific packaging, deployment, and observability
- Retrieval freshness and failure handling

Both implementations must preserve these behavioral invariants:

1. Produce review findings and guidance, never mutate customer code.
2. Treat missing or inaccessible evidence as `Cannot Determine`, not as proof
   that a control is absent.
3. Cite the workload artifact, resource, metric, or interview answer supporting
   every determinate finding.
4. Use canonical BP IDs when AWS publishes them; never invent IDs.
5. Keep citation coverage separate from applicability and finding quality.
6. Emit the versioned structured-output contract or publish an explicit,
   tested schema migration.
7. Keep raw customer evidence and raw evaluation output outside Git.

## Supersession gates

The successor becomes the default only after all gates pass on the same pinned
fixture set and runtime configuration.

| Gate | Required result |
| --- | --- |
| Contract | 100% of complete outputs validate against the agreed schema |
| Completion | No partial run is ranked or counted as successful |
| Evidence validity | At least 0.95 on expert-adjudicated fixtures |
| Unsupported determinate claims | At most 0.05 |
| Critical/High precision | At least 0.90 |
| Seeded Critical/High recall | At least 0.90 |
| Uncertainty recall | At least 0.90 |
| Data hygiene | No credentials, account IDs, internal URLs, or workstation paths in publishable artifacts |
| Regression | No material quality regression whose confidence interval excludes the current implementation |
| Operations | Retrieval denial, timeout, throttling, and partial-pillar scenarios fail closed |

Canonical BP citation F1 remains a ledger-coverage diagnostic. It is never a
quality gate.

## Comparison protocol

1. Pin the same scenario snapshot, inventory, framework version, prompts,
   model, inference settings, tools, and repetition policy.
2. Run both implementations from isolated workspaces.
3. Record immutable manifests, completion state, cost, latency, and tokens.
4. Score both outputs with `evals/quality.py` against independently
   adjudicated labels.
5. Report evidence, risk, status, uncertainty, severity, recommendation,
   completion, cost, and latency separately.
6. Investigate disagreements at the BP/evidence-pointer level. Do not collapse
   them into one score.

## Migration sequence

1. Add a successor adapter that maps Agent Toolkit output to the current
   structured-output schema.
2. Run a non-production shadow comparison and publish sanitized aggregates.
3. Complete at least one release cycle with both implementations available.
4. Publish a versioned deprecation notice identifying the replacement,
   compatibility differences, and rollback path.
5. Switch the default only after the supersession gates pass.
6. Retain this repository's schemas, fixtures, evaluators, and release history
   as the compatibility and regression suite.

## Local validation

From `evals/`:

```bash
uv run pytest -m "not eval" -q
uv run python validate_artifact.py <quality-result.json>
uv run python cli_effectiveness/compute_skill_lift.py
```

Paid or live-runtime evaluations require explicit operator confirmation and
must write raw artifacts only to gitignored paths.
