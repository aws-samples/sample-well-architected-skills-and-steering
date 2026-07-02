# AGENTREL08 — Graceful degradation and configuration management

**Pillar**: Reliability  
**Best Practices**: 4

---

# AGENTREL08-BP01 Establish consistent configuration management practices

When different agent instances run with different configuration, the
resulting reliability issues are hard to reproduce and harder to
trust. Centralized configuration with versioning, validation, and
automated distribution keeps every instance on the same current
state and makes rollback a matter of changing a version pointer.

**Desired outcome:**

- You have centralized configuration with versioning and
validation for every setting agents read dynamically.
- You have deployment strategies, gradual rollout for routine
changes, immediate for emergencies, with automatic rollback on
error.
- You detect configuration drift across the agent fleet and
remediate it automatically.

**Common anti-patterns:**

- Hardcoding configuration in agent code, requiring redeployment
to change values and reducing the risk of dynamic adjustment.
- Managing configuration without versioning, making it impossible
to identify which change caused a regression or roll back
cleanly.
- Applying configuration changes without validation, letting
misconfigured values reach production.

**Benefits of establishing this best
practice:**

- Agent behavior stays consistent across instances through
centralized management.
- Configuration changes ship safely through validation and gradual
rollout with rollback capability.
- Operational issues get resolved faster through dynamic
adjustment without redeployment.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Centralized configuration is the unifying pattern.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)'s configuration capabilities
manage agent settings centrally with versioning and validation.
Runtime configuration that agents read dynamically includes model
selection, tool availability, rate limits, feature flags, and
operational thresholds. Use a managed configuration service with
JSON Schema validators that enforce compliance before deployment.
Validation at the configuration layer catches bad values before
they become production incidents.

Deployment strategy keeps configuration changes safe. Gradual
rollout handles the routine case. Propagate the new config to a
small percentage of the fleet, watch for regressions, then expand.
Automatic rollback on error reverses the change when something
goes wrong. Immediate deployment handles the emergency case where
the current configuration is actively breaking production and the
cure can't wait for gradual rollout. Having both modes available,
and knowing which one applies to each change, is what keeps the
system responsive without being reckless.

Drift detection closes the loop. Configuration change detection in
agent functions logs when versions change, enabling correlation of
behavioral changes with specific deployments. For sensitive
configuration values, use encrypted parameter storage with
fine-grained access control. Monitor for configuration drift
across the agent fleet through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), alerting when instances
are running with different configuration versions. Drift that
persists is usually a sign that deployment rolled out partially or
that a manual override was applied and forgotten.

### Implementation steps

- **Define configuration profiles per
domain:** Build profiles for model selection, tool
availability, rate limits, and feature flags. Apply JSON
Schema validation to each profile.
- **Configure deployment
strategies:** Use gradual rollout for routine
changes and immediate deployment for emergencies, with
automatic rollback on error.
- **Implement configuration change
detection logging:** Log version changes so
behavioral changes can be correlated with deployments.
- **Use encrypted parameter storage for
sensitive values:** Apply fine-grained access
control on secrets.
- **Monitor for configuration
drift:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to alert when
instances run different configuration versions.

## Resources

**Related best practices:**

- [AGENTREL06-BP05
Implement dynamic capability toggling](agentrel06-bp05.html)
- [AGENTREL08-BP02
Implement agent tracing for telemetry throughout agent
processing](agentrel08-bp02.html)
- [AGENTREL08-BP03
Architect agent systems with resource isolation and contention
mitigation](agentrel08-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Make
agents a reality with Amazon Bedrock AgentCore: Now generally
available](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-is-now-generally-available/)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel08-bp01.html*

---

# AGENTREL08-BP02 Implement agent tracing for telemetry throughout agent processing

Request-boundary telemetry can't distinguish between normal
variation and genuine degradation. Stage-level telemetry across the
full processing lifecycle gives operators the signal they need to
activate graceful degradation at the right time rather than too
early or too late.

**Desired outcome:**

- You have stage-level telemetry across context retrieval, model
inference, tool execution, and response generation.
- You capture LLM-specific data, token counts, inference latency,
finish reason, on every model call.
- You have CloudWatch dashboards with stage-level widgets and
composite alarms that drive automated degradation activation.

**Common anti-patterns:**

- Implementing telemetry only at the request boundary without
instrumenting individual processing stages.
- Omitting LLM-specific telemetry, token counts, inference
latency, output quality. That is essential for detecting
model-related degradation.
- Treating telemetry as a post-deployment concern rather than
designing it into the architecture from the start.

**Benefits of establishing this best
practice:**

- Degradation detection is accurate because telemetry covers every
processing stage.
- Degradation decisions are informed by which stage is actually
under pressure.
- Incident response is faster through pre-built dashboards that
expose the signals immediately.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) captures agent-specific
telemetry through OpenTelemetry-compatible instrumentation. This
includes tool invocation traces, model interaction details, and
memory access patterns. Stage-level instrumentation is what
distinguishes this from generic request logging. A single latency
metric at the request boundary can't tell you whether slowness
came from retrieval, inference, tool execution, or response
parsing.

LLM-specific telemetry deserves its own emphasis. Enable
[Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) to capture full request
and response data for every LLM call, including token counts,
latency, and finish reason. A spike in output token counts or a
shift in finish-reason distribution often precedes a visible
quality regression by hours. Without the logs, those early signals
are invisible.

The metric set needs structure. For each processing stage define a
standard set. Context retrieval tracks latency and result count.
Model inference tracks latency, token counts, and model ID. Tool
execution tracks call count, latency, and error rate. Response
generation tracks output validation pass rate. Build Amazon CloudWatch dashboards with stage-level widgets and a composite
health summary so operators can see the full lifecycle at a
glance.
[Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) on the key metrics establishes
baselines automatically, removing the need to hand-tune
thresholds. Composite alarms across multiple stages detect
degradation patterns that span boundaries and trigger automated
degradation activation when the composite health signal drops.

### Implementation steps

- **Enable AgentCore Observability with
stage-level telemetry:** Instrument context
retrieval, inference, tool execution, and response
generation. Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) for collection.
- **Enable Amazon Bedrock model
invocation logging:** Capture token counts,
latency, and finish reason for every LLM call through
[Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html).
- **Build CloudWatch dashboards with
stage-level widgets:** Include a composite health
summary so operators see the full lifecycle at a glance.
- **Configure CloudWatch Anomaly
Detection on key metrics:** Use
[Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) for automatic baseline
modeling.
- **Create composite alarms:**
Combine multi-stage signals to trigger automated degradation
activation.

## Resources

**Related best practices:**

- [AGENTREL07-BP03
Implement distributed tracing to track system dependencies and
facilitate recovery](agentrel07-bp03.html)
- [AGENTREL08-BP01
Establish consistent configuration management practices](agentrel08-bp01.html)
- [AGENTREL08-BP03
Architect agent systems with resource isolation and contention
mitigation](agentrel08-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Build
trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel08-bp02.html*

---

# AGENTREL08-BP03 Architect agent systems with resource isolation and contention mitigation

Shared resource pools let one noisy agent starve the rest. Priority
tiers with dedicated resource allocations and contention detection
keep user-facing agents responsive even when background workloads
spike.

**Desired outcome:**

- You have separate runtime infrastructure for different agent
priority tiers so high-priority agents have dedicated resources.
- You track token consumption for each agent and enforce per-agent
access to shared model capacity.
- You detect contention early through composite signals and
activate automated mitigation before failures occur.

**Common anti-patterns:**

- Sharing resource pools across every agent without isolation,
letting high-volume agents consume resources needed by others.
- Skipping API quota management, so throttling affects every agent
whenever any single agent exceeds quotas.
- Treating every agent as equally important, letting background
workload spikes degrade user-facing agents.

**Benefits of establishing this best
practice:**

- Performance stays predictable because resource isolation helps
prevent cross-workload interference.
- Service quality for high-priority agents holds through
priority-based resource allocation.
- Contention gets detected early through composite monitoring
before it becomes a failure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Isolation starts at the execution surface. Deploy separate
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) instances for different agent
priority tiers, so high-priority user-facing agents run on
dedicated Runtime instances with their own resource allocations
that background agents can't consume. This is the cleanest form of
bulkheading for agent workloads, separate pools that physically
can't interfere with each other, with no shared scheduler to
introduce coupling.

Quota protection handles the shared-model case. Amazon Bedrock
inference capacity is shared across the account. Track token
consumption for each agent through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch
alarms to catch individual agents approaching consumption
thresholds.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies control which
agents can access which models. Combining policy with Amazon
Bedrock service quotas and
[Provisioned
Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) helps prevent one agent from exhausting shared
model capacity. For latency-sensitive agents that need predictable
inference performance regardless of overall service demand,
Provisioned Throughput gives you fixed model units and the
predictable latency that goes with them.

With contention detection, you can act before the incident hits.
Amazon CloudWatch composite alarms combine multiple resource
utilization signals into a contention score. These signals include
concurrency utilization, token consumption rates, and queue
depths. When the score crosses the threshold, trigger automated
mitigation. Use
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to deny tool access for
low-priority agents, or activate graceful degradation for
non-critical capabilities. Monitor resource utilization across
priority tiers through AgentCore Observability dashboards so
emerging contention becomes visible before it causes user-visible
failures.

### Implementation steps

- **Deploy separate AgentCore Runtime
instances per priority tier:** Give high-priority
user-facing agents dedicated
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) resource allocations.
- **Track per-agent token consumption
and enforce access:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to control model access per
agent.
- **Use Amazon Bedrock Provisioned
Throughput for latency-sensitive agents:** Use
[Provisioned
Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) for predictable inference performance.
- **Configure composite alarms on
resource utilization signals:** Combine
concurrency, token consumption, and queue depth signals
through Amazon CloudWatch into a contention score.
- **Implement automated contention
mitigation:** Deny tool access for low-priority
agents through AgentCore Policy when pressure is detected.

## Resources

**Related best practices:**

- [AGENTREL01-BP05
Implement adaptive provisioning](agentrel01-bp05.html)
- [AGENTREL08-BP01
Establish consistent configuration management practices](agentrel08-bp01.html)
- [AGENTREL08-BP02
Implement agent tracing for telemetry throughout agent
processing](agentrel08-bp02.html)
- [AGENTREL08-BP04 Track
agent memory utilization metrics](agentrel08-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Securely
launch and scale your agents and tools on Amazon Bedrock
AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/)
- [Amazon
Bedrock Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel08-bp03.html*

---

# AGENTREL08-BP04 Track agent memory utilization metrics

Memory exhaustion produces agents that look healthy but lack the
context to reason well. Tracking utilization across short-term,
long-term, and in-context tiers reveals the pressure before silent
failures begin.

**Desired outcome:**

- You track token counts per context component and emit
context-window utilization percentages.
- You have alarms when context window utilization exceeds 80%,
triggering summarization or pruning workflows.
- You detect memory growth trends through metric math so gradual
leaks surface before they cause failures.

**Common anti-patterns:**

- Monitoring only infrastructure-level memory metrics without
tracking agent-specific patterns like context window utilization
and session state growth.
- Operating without baselines for normal memory consumption,
making anomalous growth undetectable.
- Skipping in-context memory utilization, the most direct
indicator of context-related degradation.

**Benefits of establishing this best
practice:**

- Memory pressure gets detected early through continual monitoring
before exhaustion causes failures.
- Degradation decisions are informed by which memory tier is
actually under pressure.
- Silent memory-related failures get prevented because in-context
utilization is monitored proactively.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

In-context memory is where silent failures start. When the context
window fills with retrieved context, conversation history, and
tool results, the model has less room for new information and its
effective reasoning capacity drops. Tracking utilization by
component (system prompt, retrieved context, conversation history,
tool results) through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tells you which component
is driving pressure. Alarms when utilization exceeds 80% of the
model's context window trigger summarization or pruning workflows
before the limit becomes a hard wall. For accurate token
measurement with Anthropic models on Amazon Bedrock, use
[Amazon
Bedrock token counting](https://docs.aws.amazon.com/bedrock/latest/userguide/count-tokens.html). For other providers, approximate
estimation works well enough for baseline purposes.

External memory stores are the other place pressure shows up.
Monitor
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) access latency and error rates
through AgentCore Observability, and watch infrastructure-level
metrics through Amazon CloudWatch. Latency climbing on memory
access is often the first signal that the store is under pressure,
well before it actually fails.

Growth trend analysis catches the leaks infrastructure-level
metrics miss. Use
[Amazon CloudWatch Metric Math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) to calculate growth rates over
configurable windows and alert when the rate exceeds baseline.
Steady incremental growth rarely trips a threshold alarm but often
indicates a leak that will eventually exhaust memory. Build
automated memory management responses for each tier. Apply context
summarization for in-context pressure, session pruning for
short-term memory pressure, and memory consolidation for long-term
memory pressure.

### Implementation steps

- **Track in-context memory utilization
per component:** Measure token counts for system
prompt, retrieved context, conversation history, and tool
results. Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) for collection.
- **Configure alarms at 80% context
window utilization:** Trigger summarization or
pruning workflows before the limit becomes a hard wall.
- **Monitor AgentCore Memory access
latency and error rates:** Catch external store
pressure early through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html).
- **Implement memory growth trend
analysis:** Use
[Amazon CloudWatch Metric Math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) to detect gradual leaks that
don't trip threshold alarms.
- **Build automated memory management
responses:** Implement summarization, pruning, and
consolidation responses per tier.

## Resources

**Related best practices:**

- [AGENTREL03-BP04
Implement graceful degradation for memory and state
operations](agentrel03-bp04.html)
- [AGENTREL08-BP01
Establish consistent configuration management practices](agentrel08-bp01.html)
- [AGENTREL08-BP02
Implement agent tracing for telemetry throughout agent
processing](agentrel08-bp02.html)
- [AGENTREL08-BP03
Architect agent systems with resource isolation and contention
mitigation](agentrel08-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock token counting](https://docs.aws.amazon.com/bedrock/latest/userguide/count-tokens.html)
- [Amazon CloudWatch Metric Math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel08-bp04.html*

---
