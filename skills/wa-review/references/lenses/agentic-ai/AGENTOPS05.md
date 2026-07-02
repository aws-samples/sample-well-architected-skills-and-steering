# AGENTOPS05 — Observability and monitoring for agentic systems

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

# AGENTOPS05-BP01 Establish end-to-end tracing and telemetry for agent operations

When an agent produces an unexpected output, the investigation is
only as good as the telemetry. Distributed tracing that captures the
full execution path (reasoning, tool calls, memory operations, and
model invocations) enables precise reconstruction of every decision
and action.

**Desired outcome:**

- Every agent run produces a complete distributed trace covering
the flow from request to response across all services and
agents.
- Teams can reconstruct the exact sequence of operations for any
run, enabling rapid debugging and targeted optimization.
- Real-time telemetry dashboards give operational teams continuous
visibility into agent health.
- Trace data is retained on a defined policy for post-operations
analysis and compliance.

**Common anti-patterns:**

- Instrumenting only infrastructure metrics (Lambda duration, API Gateway latency) without capturing agent-specific spans for
reasoning steps, tool invocations, and memory operations.
- Implementing tracing without propagating trace context across
agent boundaries, producing disconnected trace fragments that
can't be correlated into end-to-end workflows.
- Capturing telemetry without standardized schemas, making it
impossible to query consistently across agents or compare
behavior across versions.
- Retaining traces forever because no one defined a policy, or
retaining them too briefly to support quarterly trend analysis.

**Benefits of establishing this best
practice:**

- Distributed tracing makes agent operations like decisions and
actions queryable.
- Detailed telemetry provides the empirical foundation for
optimization, identifying bottlenecks and validating
improvements with data.
- Trace context propagation across agent boundaries makes
multi-agent workflow debugging tractable.
- Standardized schemas enable cross-agent comparison and
version-over-version regression analysis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) is the default telemetry
service for agents on AgentCore Runtime. Its
OpenTelemetry-compatible instrumentation automatically captures
LLM inference calls, tool invocations, and memory operations
without requiring each agent to add its own spans. For agents
built on Strands Agents or custom frameworks, the agent loop
itself needs instrumentation. OpenTelemetry spans wrapping each
operation phase make the trace complete.

Trace context propagation separates useful traces from fragmented
ones. W3C Trace Context propagation across all agent boundaries
maintains continuity in distributed workflows, so a request that
passes through five agents produces one trace with five spans, not
five disconnected traces. Without propagation, multi-agent
debugging becomes manual correlation by timestamp, which scales
poorly and produces incorrect answers when concurrent requests
overlap.

Standardized span schemas produce queryable data from your
telemetry. Each span type needs defined fields, like model ID and
token counts for inference, tool name and latency for invocations,
and iteration count for reasoning. Store telemetry in
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Logs with structured JSON so dashboards and
queries work against named fields. Configure sampling to capture
100% of error traces and a configurable percentage of successful
traces. This balances visibility with cost, and errors are not
dropped.

### Implementation steps

- **Instrument agents with OpenTelemetry
spans:** Deploy on
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) or add manual
instrumentation covering all operation phases (reasoning,
tool calls, memory operations).
- **Propagate W3C Trace Context across
agent boundaries:** Carry trace context forward on
every agent-to-agent, agent-to-tool, and agent-to-service
call.
- **Define standardized telemetry
schemas:** Specify fields for each span type, and
log in structured JSON for efficient
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) Logs queries.
- **Build end-to-end
dashboards:** Visualize agent performance with
drill-down to individual trace components.
- **Set retention policies:**
Balance visibility with storage cost, with different tiers
for operational, compliance, and debug telemetry.

## Resources

**Related best practices:**

- [AGENTOPS05-BP02 Monitor
agent behavior patterns and detect anomalies](agentops05-bp02.html)
- [AGENTOPS05-BP03
Implement structured logging and comprehensive audit
trails](agentops05-bp03.html)
- [AGENTOPS04-BP03
Develop fallback behavior and error handling for tool
invocations](agentops04-bp03.html)
- [AGENTPERF01-BP02
Implement comprehensive performance telemetry](agentperf01-bp02.html)
- [AGENTREL07-BP03
Implement distributed tracing to track system dependencies and
facilitate recovery](agentrel07-bp03.html)

**Related documents:**

- [Getting
started with Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Observing
agentic AI workloads using Amazon CloudWatch](https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/)
- [Observability
and monitoring for serverless agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/observability-and-monitoring.html)

**Related videos:**

- [AWS 2025 - AgentCore Observability: Monitor and Debug with
OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k)
- [AWS re:Invent 2024 - Observability for Reliable Agentic AI with
Strands & OpenTelemetry (NTA406)](https://www.youtube.com/watch?v=qJxF4XfMLhk)
- [AWS re:Invent 2024 - Build observable AI agents with Strands,
AgentCore, and Datadog (AIM233)](https://www.youtube.com/watch?v=mOAd8grR1BU)
- [AWS 2025 - Strands Agents Observability, Evaluation, &
Deployment](https://www.youtube.com/watch?v=VgN-6_tmQHE)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore, Lab 4: Deploy to
Production](https://catalog.workshops.aws/agentcore-getting-started/en-US/60-add-runtime)
- [Diving
Deep into Bedrock AgentCore, Observability](https://catalog.workshops.aws/agentcore-deep-dive/en-US/70-agentcore-observability)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS X-Ray](https://aws.amazon.com/xray/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05-bp01.html*

---

# AGENTOPS05-BP02 Monitor agent behavior patterns and detect anomalies

Static threshold alerts catch obvious breakages. Anomaly detection
over behavioral baselines extends coverage to gradual shifts like a
slowly rising escalation rate, a quietly increasing hallucination
frequency, or tool-selection patterns that drift toward less capable
options, providing early visibility into behavioral trends.

**Desired outcome:**

- Baseline behavior profiles are established per agent and updated
continually as normal behavior evolves.
- Anomalies (unusual reasoning patterns, unexpected tool usage,
performance degradation, and behavioral drift) are detected
automatically and routed to the right response workflow.
- Teams receive early warning of emerging issues before they
impact users.
- Behavioral changes can be traced to specific configuration
updates, model updates, or input distribution shifts.

**Common anti-patterns:**

- Relying exclusively on static threshold-based alerting without
anomaly detection, missing gradual drift that never triggers a
single threshold but represents a significant cumulative change.
- Establishing behavior baselines once at deployment without
updating them as normal behavior evolves, so legitimate
evolution is flagged as anomalous.
- Monitoring only performance metrics without behavioral metrics
(reasoning patterns, tool selection, escalation rate), missing
anomalies that don't manifest as performance issues.
- Treating every anomaly with the same urgency, producing alert
fatigue that causes teams to ignore genuine issues.
- Failing to distinguish data drift (input distribution shifts),
concept drift (input-output relationship changes), and
performance drift (output quality degradation), leading to
misdirected remediation.

**Benefits of establishing this best
practice:**

- Behavioral monitoring extends observability from infrastructure
metrics to decision-making patterns, giving visibility into the
aspects of agent behavior that most affect business outcomes.
- Drift detection creates a feedback signal that identifies when
agents need retraining, reconfiguration, or updates to maintain
alignment.
- Severity-aware routing keeps teams responsive to high-impact
anomalies without drowning them in low-severity signal.
- Correlating anomalies with configuration and model changes
accelerates root-cause analysis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establish a baseline, as anomaly detection without a baseline can
produce unreliable signals. Collect agent metrics over two to four
weeks, like reasoning iteration counts, tool selection frequency,
escalation rates, task completion rates, and confidence score
distributions, to establish a baseline for each agent.
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Anomaly Detection produces dynamic baselines
that evolve automatically and detects deviations through ML-based
bands, which catches drift that static thresholds miss.

Choose your metrics carefully. Performance metrics (latency, error
rate) are necessary but not sufficient. Behavioral metrics,
reasoning patterns, tool selection frequency, escalation rate, and
output quality distributions are where subtle drift first appears
and where the anomaly that affects users most commonly occurs.

Severity-based routing helps prevent alert fatigue from eroding
the system's usefulness.

- Performance anomalies trigger automated investigation
- Behavioral anomalies trigger human review
- Security-relevant anomalies trigger immediate escalation

The three queues serve different operational loops, and mixing
them can produce noise and under-response. Correlate anomalies
with deployment events on dashboards.

Rolling baseline updates keep the system aligned with legitimate
change. As agents accumulate usage and mature, normal behavior
shifts, and a baseline frozen at deployment will eventually flag
every day as anomalous. The update cadence should reflect the
agent's stability: weekly rolling windows work for agents under
active iteration, monthly or longer for stable production agents.

### Implementation steps

- **Define behavioral metrics per
agent:** Cover reasoning patterns, tool usage,
escalation rates, and output quality alongside performance
metrics.
- **Collect baselines and configure
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) Anomaly Detection:** Use a
representative observation period and configure anomaly
detection bands on key behavioral metrics.
- **Route anomalies by type and
severity:** Performance anomalies to automated
investigation, behavioral to human review, security to
immediate escalation.
- **Build behavioral monitoring
dashboards:** Show patterns over time and correlate
with configuration or model changes.
- **Update baselines on a rolling
basis:** Reflect legitimate evolution while
maintaining sensitivity to genuine anomalies.

## Resources

**Related best practices:**

- [AGENTOPS05-BP01
Establish end-to-end tracing and telemetry for agent
operations](agentops05-bp01.html)
- [AGENTOPS05-BP03
Implement structured logging and comprehensive audit
trails](agentops05-bp03.html)
- [AGENTOPS02-BP04
Maintain feedback control loops for continuous
improvement](agentops02-bp04.html)
- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Launching
Amazon CloudWatch generative AI observability](https://aws.amazon.com/blogs/mt/launching-amazon-cloudwatch-generative-ai-observability-preview/)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)
- [Advancing
AI agent governance with Boomi and AWS](https://aws.amazon.com/blogs/machine-learning/advancing-ai-agent-governance-with-boomi-and-aws-a-unified-approach-to-observability-and-compliance)

**Related videos:**

- [AWS re:Invent 2024 - Move beyond reactive: Transform cloud ops
with AWS DevOps Agent (COP362)](https://www.youtube.com/watch?v=JajBEYle67I)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05-bp02.html*

---

# AGENTOPS05-BP03 Implement structured logging and comprehensive audit trails

Free-text logs look useful until someone tries to query them at
scale. Structured logs, immutable audit trails, and defined
retention policies make your logs an active operational tool that
provides evidence for compliance.

**Desired outcome:**

- All agent decisions, actions, and interactions are captured in
structured, queryable logs.
- Audit trails are immutable and tamper-evident, providing a
trustworthy record for regulatory and governance purposes.
- Log retention policies balance operational and compliance needs
with storage cost.
- Authorized teams query log data efficiently through defined
interfaces.

**Common anti-patterns:**

- Using unstructured free-text logging that can't be efficiently
queried or parsed at scale.
- Logging only errors and exceptions without capturing successful
operations, producing an incomplete picture that reduces the
ability to reconstruct the full sequence.
- Storing logs in mutable storage without integrity controls,
creating audit trails that could be altered and therefore can't
be relied upon for compliance.
- Logging sensitive information, personally identifiable
information (PII) or credentials, in agent reasoning traces,
creating compliance and security risk.
- Operating without retention policies, producing unbounded log
volumes that become expensive to store and difficult to search.

**Benefits of establishing this best
practice:**

- Immutable, structured audit trails provide the evidentiary
foundation for regulatory compliance and demonstrate that agents
operated within authorized boundaries.
- Structured logging with efficient query interfaces turns log
data from a passive record into an active operational tool,
enabling rapid incident investigation and pattern extraction.
- PII redaction at write time helps prevent sensitive information
from reaching log storage, reducing data protection risk.
- Tiered retention keeps compliance-relevant logs available for
years while retiring short-term debug logs that would otherwise
accumulate cost.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Structured logging is a format discipline that verifies that your
other logging practices work correctly. Your JSON should have a
standardized schema to make it queryable, including:

- Timestamp
- Trace ID
- Agent ID
- Session ID
- Operation type
- Decision rationale
- Outcome

Free-text logs require regex searches to answer simple questions,
while structured logs answer them through
[Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/) Insights queries against named fields.
Enforce the schema, even if it is simple.

Your retention policy should depend on the purpose of the logs.

- Operational logs (30–90 days) support incident investigation
and recent trend analysis.
- Compliance logs (1–7 years depending on regulatory
requirements) support audits and legal discovery.
- Debug logs (7–14 days) support development and are expensive
to keep beyond that.

Applying different retention policies to different log streams,
rather than one policy to everything, cuts storage cost
substantially without losing important log information.

PII redaction should happen before logs reach storage.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) sensitive information filters detect and
redact PII at write time, which is the only reliable place to do
it. Once PII is in the log, every downstream access becomes a data
protection concern.

For compliance-critical logs,
[Amazon S3](https://aws.amazon.com/s3/)
with Object Lock in Compliance mode provides immutable storage
that supports regulatory requirements for tamper-evident audit
trails. [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) captures API-level agent actions as an
infrastructure complement, and
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) captures agent reasoning
chains, tool invocations, and decision artifacts automatically for
agents on AgentCore Runtime.

Establish saved query templates to reduce investigation latency.
For security-focused immutable audit logs with cryptographic
integrity, see
[AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html).

### Implementation steps

- **Define a JSON log schema:**
Cover trace ID, operation type, decision rationale, and
outcome as standard fields for every agent operation.
- **Configure tiered
retention:** Separate operational (30–90 days),
compliance (1–7 years), and debug (7–14 days) log streams.
- **Redact PII before write:**
Integrate
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) sensitive information filters into
the logging pipeline.
- **Use immutable storage for compliance
logs:** Write audit trails to
[Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) with Object Lock in Compliance mode.
- **Create saved query
templates:** Cover common operational analysis
patterns so incident response doesn't start from a blank
screen.

## Resources

**Related best practices:**

- [AGENTOPS05-BP01
Establish end-to-end tracing and telemetry for agent
operations](agentops05-bp01.html)
- [AGENTOPS05-BP02 Monitor
agent behavior patterns and detect anomalies](agentops05-bp02.html)
- [AGENTOPS04-BP02
Establish standardized tool integration protocols (MCP,
A2A)](agentops04-bp02.html)
- [AGENTREL07-BP03
Implement distributed tracing to track system dependencies and
facilitate recovery](agentrel07-bp03.html)
- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Observing
agentic AI workloads using Amazon CloudWatch](https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/)
- [Getting
started with Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-get-started.html)
- [Advancing
AI agent governance with Boomi and AWS](https://aws.amazon.com/blogs/machine-learning/advancing-ai-agent-governance-with-boomi-and-aws-a-unified-approach-to-observability-and-compliance)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05-bp03.html*

---

# AGENTOPS05-BP04 Define and track KPIs for agent workflows

Infrastructure metrics like CPU, memory, and invocation count
explain whether an agent is running. However, these metrics don't
determine whether an agent is actually working. Key performance
indicators (KPIs) tied to business outcomes give teams and
stakeholders a shared language for discussing and improving agent
performance.

**Desired outcome:**

- Every agent workflow has a defined set of KPIs tracked
continually against established baselines.
- Teams identify performance degradation early and correlate KPI
changes with configuration or model updates.
- Optimization efforts are prioritized based on measurable impact
rather than intuition.
- Business stakeholders have regular visibility into how agent
workflows contribute to business outcomes.

**Common anti-patterns:**

- Tracking only infrastructure metrics (like CPU, memory, and
invocation count) without agent-specific KPIs that measure
business outcomes like task completion rate and user
satisfaction.
- Defining KPIs at deployment and never revisiting them as
business objectives evolve, measuring metrics that no longer
reflect what matters.
- Collecting KPI data without establishing baselines or alerting
thresholds, producing dashboards that no one monitors
proactively.
- Weighting operational and business metrics equally when one
matters ten times more than the other, creating dashboards that
feel balanced but mislead.

**Benefits of establishing this best
practice:**

- KPIs provide the quantitative foundation for evidence-based
decisions, so teams measure change impact and prioritize
improvements based on data.
- Trend tracking reveals patterns of degradation or improvement
that inform continuous refinement of prompts, configurations,
and integrations.
- Business outcome metrics connect agent work to value delivered,
giving stakeholders regular, concrete updates instead of vague
reassurance.
- Anomaly-based alerting catches gradual degradation that static
thresholds miss.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A usable KPI framework covers four dimensions rather than one.

- Operational KPIs, like task completion rate, resolution time,
error rate, and escalation rate, measure whether the agent
runs reliably.
- Quality KPIs, like decision accuracy, hallucination rate, and
user satisfaction, measure whether its outputs are correct.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) scores for correctness,
helpfulness, safety, and tool selection accuracy, which
provides automated quality signals.
- Efficiency KPIs, like tokens per task, tool invocations per
task, and cost per task, measure whether the agent is
economical.
- Business KPIs, like outcome achievement rate, SLA compliance,
and customer satisfaction impact, measure whether the agent is
worth the investment.

Skipping any dimension produces a dashboard that looks complete
and can be misleading.

Baselines make KPIs useful by providing context for comparison.
Establish baselines during an initial observation period (two to
four weeks is usually enough), then configure
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Anomaly Detection so baselines adjust
automatically as workflows mature. Set warning and critical
alerting thresholds, where warnings initiate review and critical
alerts dictate the need for action.

Weekly KPI reports through
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/) share the same dashboard with technical and business
stakeholders. The same metrics serve both audiences so that
everyone sees the same trajectory and conversations about
investment and prioritization have shared data to ground them.
Quarterly reviews verify that KPI definitions still reflect
up-to-date business objectives and metrics.

### Implementation steps

- **Define a four-dimensional KPI
framework:** Cover operational, quality,
efficiency, and business dimensions for each agent workflow,
with use-case-specific weighting.
- **Collect KPIs through
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) custom metrics:** Add dimensions
for agent, workflow, and environment so the same metric can
be sliced multiple ways.
- **Establish baselines and configure
anomaly detection:** Use
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) Anomaly Detection with warning and
critical alerting thresholds.
- **Build weekly KPI
dashboards:** Use
[Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/user/welcome.html) reports shared with technical and
business stakeholders.
- **Review KPI alignment
quarterly:** Verify that definitions still reflect
current business objectives, and retire or replace metrics
that no longer apply.

## Resources

**Related best practices:**

- [AGENTOPS05-BP01
Establish end-to-end tracing and telemetry for agent
operations](agentops05-bp01.html)
- [AGENTOPS05-BP05 Create
workflow-specific dashboards for operational health](agentops05-bp05.html)
- [AGENTOPS02-BP04
Maintain feedback control loops for continuous
improvement](agentops02-bp04.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)
- [From
AI agent prototype to product: Lessons from building AWS
DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon Quick](https://aws.amazon.com/quicksuite/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05-bp04.html*

---

# AGENTOPS05-BP05 Create workflow-specific dashboards for operational health

Generic infrastructure dashboards can hide important metrics to
agentic workflows. A dashboard designed around a specific workflow's
critical path, step-level latencies, and characteristic failure
modes provides detail that operators need to quickly see issues and
understand the root cause.

**Desired outcome:**

- Each critical agent workflow has a dedicated dashboard with
real-time visibility into workflow health.
- Operators identify issues and quickly understand root causes.
- Dashboards are tailored to the specific characteristics of each
workflow, not generic templates.
- Operational teams use these dashboards as the primary tool for
workflow monitoring and incident response.

**Common anti-patterns:**

- Using generic infrastructure dashboards for all agent workflows,
missing workflow-specific metrics like handoff success rates,
reasoning iteration counts, and step-level bottlenecks.
- Building dashboards without linking to operational runbooks,
forcing operators to search for remediation during incidents
instead of navigating directly.
- Creating dashboards once and never updating them as workflows
evolve, so metrics for steps that no longer exist stay visible
while new steps go unmonitored.
- Building dashboards that require deep context to interpret, so
only the original author can make sense of them.

**Benefits of establishing this best
practice:**

- Workflow-specific dashboards expose the metrics and patterns
most relevant to each workflow's operational characteristics and
failure modes.
- Tailored dashboards adapt monitoring depth to each workflow's
criticality, providing detail for critical workflows and
overview for less critical ones.
- Embedded runbook links compress the time from detection to
remediation.
- Deployment event annotations correlate metric changes with
configuration changes, giving operators attribution without
cross-referencing tools.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A common layout, like top-level health summary (healthy, degraded,
and critical), key metrics as time-series graphs, and recent
events and alerts, means that operators learn the pattern once and
apply it to every workflow dashboard. Each workflow then adds its
specific content, like the critical-path steps, their completion
times, their success rates, and their queue depths.

Identifying the critical path within the dashboard.
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Contributor Insights identifies top contributors
to errors and latency empirically rather than by guesswork, which
is often more accurate than what the team assumes.

Workflow state visualization, the distribution of in-flight
requests across steps, is a view that reveals accumulation points.
A step that holds more requests than expected is either running
slowly or is the gate before a downstream failure. Either way, the
operator sees the problem without having to reconstruct it from
separate latency and error metrics. Deployment event annotations
then tie metric changes back to configuration changes, compressing
root-cause investigation.

Embed runbook links to lower the time to detect and remediate
issues. An operator looking at a degraded dashboard should be one
click from the runbook for that failure mode. Establish a review
cadence, typically quarterly, so dashboards stay aligned with
workflow changes rather than drifting into obsolete
representations.

### Implementation steps

- **Identify workflows that warrant
dedicated dashboards:** Base the list on business
impact and incident history.
- **Design a consistent dashboard
layout:** Apply the same health summary, key
metrics, and recent events pattern to every workflow
dashboard.
- **Visualize the critical
path:** Show step-level latency and success rates
for the steps where bottlenecks typically form, using
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) Contributor Insights to identify top
contributors empirically.
- **Annotate deployment
events:** Correlate metric changes with
configuration deployments so attribution is visible on the
dashboard.
- **Embed runbook links and review
quarterly:** Link each dashboard to the runbook for
common failure scenarios, and update dashboards as workflows
change.

## Resources

**Related best practices:**

- [AGENTOPS05-BP04 Define
and track KPIs for agent workflows](agentops05-bp04.html)
- [AGENTOPS05-BP01
Establish end-to-end tracing and telemetry for agent
operations](agentops05-bp01.html)
- [AGENTOPS05-BP02 Monitor
agent behavior patterns and detect anomalies](agentops05-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Observing
agentic AI workloads using Amazon CloudWatch](https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05-bp05.html*

---
