# LSREL06 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# LSREL06-BP01 Orchestrate workflows with checkpointing and failure isolation

Implement workflow orchestration with built-in checkpoints, retries,
and error isolation. By persisting intermediate results and enabling
targeted retries, failed tasks can be reprocessed independently
without requiring full pipeline reruns. Event-driven reprocessing
further improves efficiency, allowing workflows to resume from the
last successful step.

**Desired outcome:**

- Multi-step workflows can continue execution despite partial
failures.
- Failed tasks are retried automatically or isolated for
reprocessing.
- Long-running pipelines are resilient and cost-efficient with
research reproducibility requirements.

**Common anti-patterns:**

- Monolithic pipelines without checkpointing, forcing a complete
rerun if one step fails.
- Lack of retry or backoff strategies for transient errors,
leading to wasted compute cycles.
- Hardcoding dependencies between tasks so that downstream steps
fail on minor upstream issues.
- No visibility into workflow state, making recovery manual and
error-prone.

**Benefits of establishing this best
practice:**

- Reduces wasted compute and accelerates scientific turnaround
time.
- Improves reproducibility and auditability by maintaining
step-level logs and artifacts.
- Lowers cost by reprocessing only failed tasks instead of entire
workflows.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Break workflows into modular, independently testable steps with
well-defined inputs and outputs. Introduce checkpoints by
persisting intermediate artifacts in durable storage, allowing
workflows to restart from the last good state. Implement retry and
backoff strategies for transient errors to avoid unnecessary
failures.

Event-driven or rule-based triggers can restart only failed steps,
enabling faster recovery. Build in bservability from the start,
with centralized logs, metrics, and traces for each step to
support debugging and auditing.

### Implementation steps

- Use AWS Step Functions to orchestrate pipelines with retry
and error handling policies.
- Execute step workloads on AWS Batch or Amazon ECS or Amazon EKS for scalable and isolated compute.
- For genomics workloads, use AWS HealthOmics Workflows to run
CWL and WDL pipelines with built-in support for
checkpointing.
- Persist intermediate results in Amazon S3 for recovery and
reproducibility.
- Capture centralized logs and metrics in Amazon CloudWatch
for workflow observability.
- Use Amazon EventBridge to automatically trigger recovery
workflows for failed steps without restarting the full
pipeline.

## Resources

**Related best practices:**

- Long-term storage and reliable recovery of trial data
- Improve observability and operational insights in pipelines

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel06-bp01.html*

---
