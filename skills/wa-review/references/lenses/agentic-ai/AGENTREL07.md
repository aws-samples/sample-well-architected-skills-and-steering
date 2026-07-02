# AGENTREL07 — Agent monitoring, management and recovery

**Pillar**: Reliability  
**Best Practices**: 3

---

# AGENTREL07-BP01 Design workflows in stages with incremental recovery

Monolithic workflows lose everything on a single failure. Explicit
stage boundaries with persisted outputs contain failures to the
affected stage and let recovery start from the last completed
checkpoint rather than the beginning.

**Desired outcome:**

- You have workflows decomposed into discrete stages at natural
checkpoints where completed work has independent value.
- You persist stage outputs durably so recovery resumes from the
last completed stage.
- You validate stage outputs before advancing so errors don't
propagate silently through subsequent stages.

**Common anti-patterns:**

- Running workflows as monolithic processes without stage
boundaries, so any failure forces a complete restart.
- Defining stages at too coarse a granularity, losing large
amounts of work within a stage when it fails.
- Skipping stage output validation, allowing errors to propagate
through subsequent stages.

**Benefits of establishing this best
practice:**

- Work loss stays minimal because recovery resumes from the last
completed stage.
- Recovery is faster because redundant recomputation of completed
stages is avoided.
- Stage boundaries contain failures, improving error isolation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) persists execution state at every state
transition and enables recovery from the last completed step
rather than restarting entirely. The built-in retry with
exponential backoff handles transient errors within a step, and
the redrive capability restarts the workflow from the point of
failure without re-executing completed steps. This combination,
persistence plus selective retry plus redrive, is what gives
incremental recovery its teeth.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides the execution surface
for individual agent steps within the workflow.

Place stage boundaries where completed work has independent value.
A parsed document, a validated query, and a retrieved and
summarized context are all natural boundaries. If a stage produces
a half-built artifact that is useless on its own, the boundary is
in the wrong place.

Quality protection follows stage design. Stage output validation
between stages, checking schema conformance and quality thresholds
before advancing, keeps errors from propagating.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) can verify that recovered
workflow outputs match pre-failure quality baselines, so
incremental recovery doesn't silently degrade quality. Stage-level
timeouts prevent stuck stages from blocking progress indefinitely.
Stage-level metrics through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), including success rate,
execution time, and timeout frequency, identify stages that need
optimization.

### Implementation steps

- **Decompose workflows into discrete
stages:** Place boundaries at natural checkpoints
where completed work has independent value.
- **Implement with Step Functions for
durable state:** Use
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) with built-in retry and exponential
backoff per step.
- **Configure redrive for recovery from
the point of failure:** Restart failed workflows
without re-executing completed steps.
- **Implement stage output
validation:** Check schema conformance and quality
thresholds between stages so errors don't propagate.
- **Configure stage-level timeouts with
recovery paths:** Handle stages that fail after
exhausting retries.
- **Monitor stage-level
metrics:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to find stages that
need optimization.

## Resources

**Related best practices:**

- [AGENTREL03-BP03
Implement comprehensive state management and checkpoint-based
recovery](agentrel03-bp03.html)
- [AGENTREL07-BP02 Enable
automatic recovery from agent execution failures](agentrel07-bp02.html)
- [AGENTREL07-BP03
Implement distributed tracing to track system dependencies and
facilitate recovery](agentrel07-bp03.html)

**Related documents:**

- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Planning
for failure: How to make generative AI workloads more
resilient](https://aws.amazon.com/blogs/publicsector/planning-for-failure-how-to-make-generative-ai-workloads-more-resilient/)

**Related videos:**

- [AWS 2025 - AgentCore now GA: From Prototype to Production](https://www.youtube.com/watch?v=WyGK8UcAxKo)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel07-bp01.html*

---

# AGENTREL07-BP02 Enable automatic recovery from agent execution failures

Uniform retry wastes effort on non-retryable failures and creates
thundering herds on transient ones. Classifying failures by type and
applying targeted strategies, retry for transient errors, fallback
for persistent ones, escalation for unrecoverable ones, keeps
availability high without manual intervention.

**Desired outcome:**

- You classify agent failures into retryable and non-retryable
categories at the point of failure.
- You use exponential backoff with full jitter on retryable
failures, with failure-type-specific retry counts.
- You enforce retry budgets to help prevent retry storms, and
escalate to fallback or human review when retries are exhausted.

**Common anti-patterns:**

- Applying uniform retry logic to every failure type, retrying
non-retryable failures that will never succeed.
- Retrying at fixed intervals without exponential backoff and
jitter, producing thundering-herd effects during recovery.
- Implementing only retry-based recovery without fallback
strategies for failures that persist after retries.

**Benefits of establishing this best
practice:**

- Availability stays high because transient failures resolve
automatically.
- Resource utilization is efficient because non-retryable failures
don't consume retry budget.
- Persistent failures get handled gracefully through fallback
strategies when retries are exhausted.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Failure classification comes first because the recovery strategy
depends on the category. Retryable failures include transient
infrastructure errors, LLM throttling, and temporary
unavailability, conditions that a short wait and a retry are
likely to resolve. Non-retryable failures include authentication
errors, invalid inputs, and permission denials, conditions where
the same call will fail the same way no matter how many times you
retry. Collapsing the two into a single category means either
retrying things that will never succeed or giving up on things
that would have worked.

Backoff strategy matters as much as classification. Exponential
backoff with full jitter spreads retry attempts across time,
avoiding the thundering herd that fixed-interval retries produce
during widespread failures. Failure-type-specific retry counts
help too: aggressive retry for transient errors, conservative
retry with longer intervals for rate limiting. Enforce retry
budgets at two levels. For each invocation, use
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to cap retries within a single
agent execution. This helps prevent runaway loops without external
dependencies. Across invocations, implement a shared
circuit-breaker backed by a low-latency store (e.g., DynamoDB
atomic counters or ElastiCache) that tracks cumulative retry
counts across concurrent executions. AgentCore Policy evaluates
the circuit-breaker state as a policy input, rejecting new retries
when the global budget is exhausted. This two-tier approach avoids
the anti-pattern of assuming single-invocation limits provide
system-wide protection.

Self-healing workflows extend retry into recovery. Common failure
patterns have targeted remediations. Automatic prompt refinement
handles LLM output validation failures, tool substitution handles
tool call failures, and context reconstruction handles memory
access failures. When retries are exhausted, transition to
fallback strategies or human review rather than terminating. Log
every recovery action through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with structured metadata
including retry counts, strategy used, and outcome, so recovery
effectiveness can be analyzed and tuned.

### Implementation steps

- **Implement failure
classification:** Categorize agent failures into
retryable and non-retryable types at the point of failure.
- **Configure retry with exponential
backoff and full jitter:** Use
failure-type-specific retry counts so the strategy matches
the failure mode.
- **Enforce retry budgets through
AgentCore Policy:** Use
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to help prevent retry storms
during widespread failures.
- **Build self-healing workflows for
common patterns:** Implement prompt refinement,
tool substitution, and context reconstruction as targeted
recovery paths.
- **Log recovery actions for
analysis:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to capture retry
counts, strategies, and outcomes.

## Resources

**Related best practices:**

- [AGENTREL06-BP04
Implement idempotent task execution patterns](agentrel06-bp04.html)
- [AGENTREL07-BP01 Design
workflows in stages with incremental recovery](agentrel07-bp01.html)
- [AGENTREL07-BP03
Implement distributed tracing to track system dependencies and
facilitate recovery](agentrel07-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel07-bp02.html*

---

# AGENTREL07-BP03 Implement distributed tracing to track system dependencies and facilitate recovery

Correlating logs across services by hand is slow, and during an
incident slow is worse than expensive. Distributed tracing across
all components with agent-specific annotations gives operators the
full request path in one view and turns broad restarts into targeted
recovery actions.

**Desired outcome:**

- You have distributed tracing across every agent component with
agent-specific annotations.
- You propagate trace context through synchronous and asynchronous
communication boundaries.
- You correlate traces, metrics, and logs in a unified view that
surfaces root causes quickly.

**Common anti-patterns:**

- Tracing only at the application boundary without propagating
context through internal service calls.
- Skipping correlation of traces with logs and metrics, reducing
the risk of unified analysis during incidents.
- Omitting agent-specific annotations that make filtering by agent
ID, task type, or model used possible.

**Benefits of establishing this best
practice:**

- Root causes surface quickly because the request flow is visible
end to end.
- Mean time to recovery drops because trace data drives targeted
actions instead of broad restarts.
- Latency bottlenecks become visible, enabling proactive
performance optimization.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) captures the full execution
path of each agent invocation through OpenTelemetry-compatible
telemetry. Turn it on across every agent component, not only the
outer boundary, so the trace actually spans the request end to
end. Without component-level coverage, traces have gaps where
invisible work happens, which is exactly where debugging slows
down during an incident.

Annotations are what make traces searchable at the scale of real
systems. Agent-specific tags, agent ID, task type, model ID,
workflow ID, let you filter traces to a specific agent or failure
scenario instead of grepping through an undifferentiated stream.
Instrument Strands Agents framework-level traces to capture
reasoning steps, tool invocations, and their outcomes in a unified
trace view, because the agent's internal decisions are where most
of the interesting signals live.

Context propagation is the detail that decides whether
asynchronous paths are visible. For queue-based communication,
propagate trace headers through message attributes so traces
continue across queue boundaries. Without propagation, the trace
ends at the producer and a new trace starts at the consumer, and
the fact that they relate is lost. Create trace-based alerting
through Amazon CloudWatch that correlates traces, metrics, and
logs in a unified view, so a trace anomaly, a metric spike, and a
log error appear together rather than separately.

### Implementation steps

- **Enable AgentCore Observability with
OpenTelemetry tracing:** Turn on
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) across every agent
component.
- **Add agent-specific
annotations:** Tag traces with agent ID, task type,
and model ID so filtering during incidents is possible.
- **Propagate trace context across
boundaries:** Include synchronous and asynchronous
paths, with message attributes for queue-based
communication.
- **Instrument Strands Agents
framework-level traces:** Capture reasoning steps
and tool invocations in the unified trace view.
- **Create CloudWatch dashboards that
correlate traces, metrics, and logs:** Build one
unified view so incident response works on signal.

## Resources

**Related best practices:**

- [AGENTREL07-BP01 Design
workflows in stages with incremental recovery](agentrel07-bp01.html)
- [AGENTREL07-BP02 Enable
automatic recovery from agent execution failures](agentrel07-bp02.html)
- [AGENTREL08-BP02
Implement agent tracing for telemetry throughout agent
processing](agentrel08-bp02.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Build
trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Strands
Agents Traces](https://strandsagents.com/docs/user-guide/observability-evaluation/traces/)

**Related videos:**

- [AWS 2025 - AgentCore Observability: Monitor and Debug with
OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k)
- [AWS re:Invent 2024 - Observability for Reliable Agentic AI with
Strands & OpenTelemetry (NTA406)](https://www.youtube.com/watch?v=qJxF4XfMLhk)
- [AWS re:Invent 2024 - Build observable AI agents with Strands,
AgentCore, and Datadog (AIM233)](https://www.youtube.com/watch?v=mOAd8grR1BU)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore - Observability](https://catalog.workshops.aws/agentcore-deep-dive/en-US/70-agentcore-observability)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel07-bp03.html*

---
