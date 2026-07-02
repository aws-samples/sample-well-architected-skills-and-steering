# AGENTPERF01 — Strategic performance planning and measurement

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# AGENTPERF01-BP01 Define performance-aligned success criteria for agent workloads

Agent workloads are harder to measure than traditional applications
because a single user request fans out into multiple inference
calls, tool invocations, and memory retrievals, each with its own
latency, quality, and cost signature. Without explicit performance
targets, teams optimize against a moving reference and can't tell
when an agent is ready for production.

**Desired outcome:**

- You have documented performance success criteria for every agent
workload, with specific, measurable targets that are reviewed as
business requirements evolve.
- Your teams objectively assess whether an agent meets performance
expectations before deployment and continually validate
performance in production.
- You have performance criteria integrated into CI/CD pipelines as
quality gates, helping prevent regressions from reaching
production.

**Common anti-patterns:**

- Defining success criteria only around infrastructure metrics
such as CPU utilization or memory consumption, without measuring
agent-specific dimensions like reasoning latency, token
efficiency, or task completion quality.
- Applying a single latency target across streaming and
non-streaming agents, or across interactive and batch workloads,
when time-to-first-token and end-to-end completion are primary
KPIs for different agent classes.
- Establishing performance targets after deployment rather than
during design, producing architectures that can't meet
requirements without significant rework.

**Benefits of establishing this best
practice:**

- Explicit success criteria establish concrete targets against
which telemetry can be evaluated, making downstream performance
work measurable rather than speculative.
- Performance-aligned criteria direct teams to optimize the
reasoning pipeline for the metrics that matter, rather than
pursuing generic optimizations that don't improve business
outcomes.
- Quality gates tied to measurable targets convert success
criteria into enforceable artifacts that block regressions from
reaching production rather than detecting them after the fact.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Success criteria for an agent workload must be concrete enough to
evaluate a build against and specific enough to drive
architectural decisions. A performance-aligned criterion names the
signal, the threshold, the percentile or attainment goal, the
evaluation window, and the business outcome it helps protect.
Without that specificity, teams can't decide whether to swap
models, add caching, split a workflow, or reject a release, as
there is no reference against which the change can be judged.

Agent workloads have a wider KPI surface than traditional
applications because a single user request expands into multiple
inference calls, retrieval queries, tool invocations, and, for
multi-agent systems, inter-agent handoffs, each with its own
latency, error mode, and cost. A complete set of success criteria
spans four dimensions:

- Latency (time-to-first-token for streaming agents, end-to-end
completion time for task-oriented agents, and per-phase
budgets across the reasoning pipeline)
- Throughput (concurrent sessions, sustained requests per
second, and queue depth under load)
- Quality (task completion rate, tool selection and parameter
accuracy, reasoning grounding, and response faithfulness)
- Efficiency (tokens per task, cost per completion, and cache
hit rate).

Layered
[agent
evaluation frameworks](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) decompose quality further into
component-level signals that infrastructure-only monitoring can't
see, like tool use, memory retrieval, multi-turn topic adherence,
reasoning accuracy, responsibility, and safety.

The primary latency KPI differs by agent class. For streaming,
conversational agents, users perceive responsiveness through
time-to-first-token and inter-token latency, so those are the KPIs
that gate releases. For task-oriented agents that return a single
structured result, task completion time is primary and
time-to-first-token is largely irrelevant. For batch or
asynchronous workflows, throughput and cost-per-task dominate, and
strict p99 latency matters less than predictable
completion-within-SLA. A single latency target across these
classes either over-provisions some agents or sets unachievable
goals for others.
[AWS Well-Architected Performance Efficiency guidance](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html) reinforces
that tail behavior matters more than the mean, p90 and p99 anchor
latency targets because averages mask the slow responses that
drive user-perceived poor experience.

A measurable target has more structure than a number. A
service-level objective (SLO) combines a service-level indicator
(the metric), a threshold, an attainment goal (the percentage of
time or requests that must meet the threshold), an interval
(calendar or rolling window), and an error budget (the allowable
shortfall).

[Amazon CloudWatch Application Signals service level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html)
formalize this structure and add burn-rate alarms that fire when
the budget is being consumed faster than expected, which matters
for agent workloads whose latency distribution shifts subtly as
prompts, tools, or models drift. SLOs should be decomposed into
per-phase latency budgets, inference, retrieval, tool calls,
inter-agent coordination, so that when a budget is exceeded,
attribution to the offending phase is already encoded in the
criteria rather than investigated after the fact.

Success criteria are not static. Agent behavior is shaped by
prompts, memory, tools, and the models behind them, all of which
drift, so criteria that are correct at launch erode as the system
evolves. Integrating targets into CI/CD as quality gates, latency
budgets checked against load-test results, task-completion rate
checked against a curated evaluation set, cost-per-task checked
against a ceiling, converts them from documents into enforceable
artifacts that block regressions at the boundary.

[Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html) frames this lifecycle discipline as
mandatory rather than optional, because continuous measurement is
the only mechanism that keeps criteria aligned with the business
outcomes they were designed to protect.

### Implementation steps

- **Capture business outcomes and user
expectations with stakeholders:** Work with
product, business, and user-experience owners to document
the outcomes the agent must produce, the scenarios in which
it operates, and the user expectations for responsiveness,
quality, and cost. Use this intake to frame every downstream
target so latency, throughput, quality, and efficiency KPIs
trace back to a stated business or user need. The
[AWS Well-Architected Performance Efficiency process
guidance](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html) treats this stakeholder alignment as the
first step in establishing credible KPIs.
- **Classify each agent workload by
interaction pattern:** Determine whether the agent
is streaming or non-streaming, interactive or batch,
synchronous or asynchronous, and single-agent or
multi-agent. The classification dictates which latency KPI
is primary, time-to-first-token for streaming conversational
agents, end-to-end completion for task-oriented agents,
throughput and cost-per-task for batch workflows, and
whether multi-agent coordination metrics such as handoff
latency and collaboration success belong in the criteria
set.
- **Define the KPI taxonomy spanning
latency, throughput, quality, and efficiency:** For
each workload, enumerate the specific signals to measure
along the four dimensions, including agent-specific signals
that infrastructure metrics can't cover. Structure quality
signals in layers, final-response quality, task completion,
tool use accuracy, memory and retrieval relevance, reasoning
grounding, and responsibility and safety, following the
[agent
evaluation framework described by Amazon teams](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/).
Include efficiency signals such as tokens per task, cost per
completion, and cache hit rate to connect performance to
unit economics.
- **Set quantitative targets with
thresholds, percentiles, and attainment goals:**
Attach a numeric target to every KPI, specifying the
percentile (p50, p90, p99) for latency and throughput
signals and the attainment goal (for example, 99.5 percent
of requests) for quality and availability signals. Anchor
latency targets to p90 and p99 rather than averages, because
tail behavior drives user-perceived performance, the
[AWS Well-Architected Performance Efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
cautions that averages hide the slow responses that matter
most.
- **Allocate per-phase latency budgets
within the end-to-end budget:** Decompose the
end-to-end latency target into per-phase budgets, context
retrieval, LLM inference, tool invocation, inter-agent
coordination, output generation, so each phase has its own
ceiling that sums to the overall target. Per-phase budgets
make exceedances attributable at criteria-definition time
and give engineering teams clear optimization targets when a
phase drifts. Validate the decomposition against measured
traces so the budgets reflect real behavior rather than
assumption.
- **Formalize targets as service level
objectives with error budgets and burn-rate
alerts:** For each customer-facing KPI, encode the
target as an SLO with an SLI, threshold, attainment goal,
interval, and period using
[Amazon CloudWatch Application Signals service level
objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html). Configure burn-rate alarms so the service
signals when the error budget is being consumed faster than
expected, giving operators time to respond before an SLO is
exceeded. Group related SLIs into composite SLOs where a
single user-facing outcome depends on multiple operations
meeting their individual targets.
- **Operationalize quality and cost KPIs
through GenAI-aware monitoring:** Publish token
consumption, per-invocation latency percentiles, cost
attribution, and agent-level quality metrics through
[Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html), which
surfaces these signals natively for Amazon Bedrock model
invocations and accepts structured traces from agents
running on any runtime through the
[AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction). Emit agent-specific quality
signals, task completion rate, tool selection accuracy,
reasoning grounding, as custom metrics so they can be
thresholded, alarmed, and tied to SLOs the same way
infrastructure signals are.
- **Integrate targets as quality gates
in the deployment pipeline:** Convert each success
criterion into an automated check in CI/CD so releases that
exceed a latency, quality, or cost target are blocked before
they reach users. Run load tests against the latency and
throughput targets and curated evaluation sets against the
quality targets as part of the pipeline, following the
lifecycle-management framing in
[Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html). Gates turn written criteria into
enforceable artifacts that help prevent regressions rather
than detecting them in production.
- **Revisit targets on a defined cadence
as the workload evolves:** Schedule regular reviews
of each success criterion against production telemetry,
changes in user expectations, and shifts in the underlying
models, prompts, or tools. Tighten targets that are
consistently exceeded, relax targets that are blocking
legitimate improvements, and retire signals that no longer
map to a business outcome, agent behavior drifts, and
criteria that were correct at launch need to be revalidated
against current reality.

## Resources

**Related best practices:**

- [AGENTPERF01-BP02
Implement comprehensive performance telemetry](agentperf01-bp02.html)
- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)
- [AGENTOPS05-BP04
Define and track KPIs for agent workflows](agentops05-bp04.html)
- [AGENTOPS06-BP02
Evaluate and track ongoing agent performance](agentops06-bp02.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [AWS Well-Architected Framework: Performance Efficiency
Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
- [Amazon CloudWatch Application Signals: Service level objectives
(SLOs)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html)
- [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Blog:
Evaluating AI agents: Real-world lessons from building agentic
systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)

**Related videos:**

- [AWS re:Invent 2024 - Elevate application and generative AI
observability (COP326)](https://www.youtube.com/watch?v=vxzq8GthOLs)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon CloudWatch Application Signals](https://aws.amazon.com/cloudwatch/features/application-monitoring/)
- [AWS Distro for
OpenTelemetry (ADOT)](https://aws.amazon.com/otel/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf01-bp01.html*

---

# AGENTPERF01-BP02 Implement comprehensive performance telemetry

A single agent request fans out into chains of inference calls,
parallel tool invocations, memory lookups, and inter-agent
communications. Infrastructure-only monitoring can't determine by
itself which of those contributes to a slow or expensive response.
Agent-aware telemetry decomposes execution into observable,
attributable operations so that performance decisions are grounded
in measured behavior.

**Desired outcome:**

- You have a complete distributed trace for every agent execution
that decomposes total latency into its constituent operations.
- You have real-time dashboards that provide visibility into agent
performance trends, with the resulting metrics feeding the
alerting layer.
- You have historical telemetry data that supports capacity
planning, model selection decisions, and architecture
optimization through data-driven analysis.

**Common anti-patterns:**

- Relying only on infrastructure-level metrics such as function
duration or API gateway latency without instrumenting the
agent's reasoning pipeline, making it impossible to distinguish
between slow inference and slow tool calls.
- Treating telemetry as an afterthought, producing gaps in trace
continuity across agent boundaries, tool invocations, and
asynchronous operations.
- Collecting telemetry data without establishing baselines,
thresholds, or alerts, creating a data lake of metrics that
nobody monitors or acts upon.

**Benefits of establishing this best
practice:**

- Fine-grained performance data directs engineering effort toward
the operations that materially contribute to end-to-end latency,
helping prevent wasted cycles on components with negligible
impact on user experience.
- Span-level attribution reduces mean-time-to-resolution for
production incidents by pinpointing whether slow responses
originate in inference, tool calls, retrieval, or inter-agent
coordination.
- Historical telemetry data supports informed model selection,
routing, and capacity planning by comparing latency, token, and
cost profiles across models and architectures.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Comprehensive agent telemetry means capturing metrics, traces, and
logs, as well as structuring them so every step of the reasoning
pipeline is individually attributable. If any step of the agent's
multiple and unique operations is opaque, performance
investigations become less data-based and therefore less useful.

[OpenTelemetry
(OTel)](https://opentelemetry.io/) is the portable substrate for this instrumentation,
and its
[generative
AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) define standard attributes for LLM
operations, model, input and output tokens, request parameters,
and finish reasons so that spans remain comparable across
frameworks, models, and runtimes. Using these conventions rather
than framework-specific schemas keeps telemetry portable when an
agent moves between Amazon Bedrock AgentCore Runtime, AWS Lambda,
Amazon ECS, Amazon EKS, or self-hosted infrastructure, and helps
prevent a rewrite every time the deployment target changes.

Agent telemetry has a natural three-tier hierarchy documented in
[AgentCore
Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html).

- A *session* represents a complete user
conversation
- A *trace* represents one request-response
cycle within the session
- *Spans* represent discrete operations
inside a trace, a reasoning iteration, an LLM call, a tool
invocation, a memory lookup, a retrieval query, or an
inter-agent handoff

Organizing telemetry against this hierarchy turns an opaque slow
agent signal into an attributable execution tree where each span
carries its own latency, token counts, error status, and
contextual attributes. Session identifiers must flow through every
span so a trace can be linked back to its conversation, and trace
context must propagate across agent and tool boundaries using the
[W3C Trace
Context](https://www.w3.org/TR/trace-context/) standard so asynchronous and multi-service
workflows remain a single connected graph.

Instrumentation approaches differ by runtime, but the resulting
telemetry should look the same. For agents on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), the runtime auto-instruments
agent code and emits OTel-compatible traces, runtime metrics
(invocations, session count, latency, errors, CPU and memory
usage), and structured logs to Amazon CloudWatch without
additional work.

For agents on other runtimes, the
[AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/docs/introduction) exports traces, metrics,
and logs to CloudWatch using the same semantic conventions so both
populations appear in a unified observability surface.

Framework-level instrumentation libraries such as OpenInference,
OpenLLMetry, OpenLit, and Traceloop emit the reasoning-pipeline
spans, reasoning iterations, prompt and response content,
tool-selection decisions, that generic runtime instrumentation
can't see. Select a framework based on the agent framework in use
(for example, Strands Agents, LangChain, LangGraph, CrewAI, or
LlamaIndex).

On the ingestion side,
[Amazon CloudWatch Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) ingests 100 percent of spans
as structured logs in the aws/spans log group
and indexes a configurable percentage as trace summaries,
supporting end-to-end trace search without forcing sampling at the
span level. Enabling
[CloudWatch
Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.html) on Amazon Bedrock API calls
automatically populates OTel GenAI attributes,
gen_ai.system,
gen_ai.request.model,
gen_ai.usage.input_tokens,
gen_ai.usage.output_tokens,
gen_ai.response.finish_reasons, so token, cost,
and finish-reason analysis is available without hand-written
spans.

Some signals may not be captured implicitly, such as task success
and failure rate, cache hit rate, tool-selection accuracy,
time-to-first-token, and cost per task. For these signals, emit
them as CloudWatch custom metrics from the agent or the OTel
collector, dimensioned uniformly (agent ID, workflow, environment,
task type, model ID) so they can be correlated with the spans they
originated from and consumed by dashboards, SLOs, and anomaly
detection downstream.

### Implementation steps

- **Define a standardized telemetry
schema:** Document the span types the agent will
emit (reasoning iteration, LLM inference, tool invocation,
memory operation, retrieval, inter-agent handoff) and the
required attributes for each, aligning LLM spans with the
[OpenTelemetry
generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) and agent spans
with the
[GenAI
agent span conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/). Specify a consistent set of
metric dimensions, agent ID, workflow, environment, task
type, model ID, that every custom metric and span must carry
so signals remain correlatable across the stack.
- **Instrument the reasoning pipeline
across every execution layer:** Wrap reasoning
iterations, LLM inference, tool invocations, memory
operations, retrieval queries, and inter-agent handoffs as
OpenTelemetry spans. For agents on Amazon Bedrock AgentCore
Runtime, the runtime auto-instruments agent code when
[AgentCore
Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html) is enabled. For agents on other
runtimes, use the
[AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/docs/introduction) together with a
framework-specific instrumentation library (OpenInference,
OpenLLMetry, OpenLit, or Traceloop) so reasoning-pipeline
spans are captured rather than only request-level spans.
- **Propagate trace and session context
across every boundary:** Carry
[W3C
Trace Context](https://www.w3.org/TR/trace-context/) headers through every outbound call the
agent makes, tool invocations, retrieval queries,
inter-agent handoffs, asynchronous queue-backed work, so a
single user request produces a single connected trace rather
than disconnected fragments. Propagate the session
identifier through OpenTelemetry baggage so every span in a
conversation can be linked back to its session for
conversation-level analysis.
- **Enable CloudWatch ingestion for
spans and Amazon Bedrock API attributes:** Complete
the one-time setup for
[CloudWatch
Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) so 100 percent of spans are
ingested as structured logs and a configurable percentage
are indexed as trace summaries. Enable
[CloudWatch
Application Signals with GenAI attribute support](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.html) to
auto-populate OTel GenAI attributes on Amazon Bedrock API
calls so token, model, and finish-reason data is captured
without custom instrumentation.
- **Emit custom metrics for signals not
captured natively:** Publish task success and
failure rate, cache hit rate, tool-selection accuracy,
time-to-first-token, and cost per task as
[CloudWatch
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) from the agent runtime or the OTel
collector, using the standard dimension set defined in step
1. Without these, observability tooling can display
infrastructure and inference signals but can't answer
product-level questions about agent quality or unit
economics.
- **Build the observability
surface:** Use the
[Amazon CloudWatch generative AI observability dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) to
provide session, trace, and agent views for incident triage
and trend analysis, and publish composed dashboards for
per-workflow, per-model, and per-tenant slices using the
standard dimension set.

## Resources

**Related best practices:**

- [AGENTPERF01-BP01 Define
performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)
- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)
- [AGENTOPS05-BP01
Establish end-to-end tracing and telemetry for agent
operations](agentops05-bp01.html)
- [AGENTOPS05-BP05
Create workflow-specific dashboards for operational
health](agentops05-bp05.html)
- [AGENTCOST05-BP02
Implement distributed cost tracing for multi-agent
workflows](agentcost05-bp02.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Blog:
Build trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html)
- [CloudWatch
Application Signals: Troubleshoot generative AI applications
with OpenTelemetry GenAI attributes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services-example-scenario-GenerativeAI.html)
- [AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/docs/introduction)
- [Blog:
Observing agentic AI workloads using Amazon CloudWatch](https://aws.amazon.com/blogs/mt/observing-agentic-ai-workloads-using-amazon-cloudwatch/)

**Related videos:**

- [AWS re:Invent 2024 - Observability for Reliable Agentic AI with
Strands & OpenTelemetry (NTA406)](https://www.youtube.com/watch?v=qJxF4XfMLhk)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Observability
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon CloudWatch Application Signals](https://aws.amazon.com/cloudwatch/features/application-monitoring/)
- [AWS Distro for
OpenTelemetry (ADOT)](https://aws.amazon.com/otel/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf01-bp02.html*

---

# AGENTPERF01-BP03 Profile end-to-end agent latency and identify optimization targets

The dominant contributor to agent latency varies by task type: a
simple question-and-answer request can be inference-bound, a
retrieval-heavy request can be retrieval-bound, and a multi-agent
workflow can be coordination-bound. Without decomposing total
latency into per-phase contributions, teams optimize assumed
bottlenecks rather than measured ones, and engineering effort lands
on work that doesn't move performance for users.

**Desired outcome:**

- You have a latency profile for every agent workload that
decomposes latency into per-phase contributions, with the
dominant phase identified and targeted for optimization.
- Your teams diagnose performance issues by examining the phase
breakdown rather than guessing at which component is slow.
- You have per-phase regression alerts that fire on phase-level
drift before the end-to-end service level objective is exceeded.

**Common anti-patterns:**

- Measuring only total latency without decomposing it into phases,
making it impossible to tell whether slowness is caused by
inference, retrieval, tool calls, or coordination overhead.
- Optimizing inference latency (model selection, prompt
compression) when the actual bottleneck is retrieval or tool
call latency, wasting engineering effort on a phase that
contributes a small fraction of total time.
- Profiling under synthetic test conditions without validating
against production traffic patterns, missing bottlenecks that
only appear under concurrent load.

**Benefits of establishing this best
practice:**

- Phase-level visibility directs engineering effort at the actual
bottleneck rather than assumed bottlenecks.
- Per-phase trend monitoring pinpoints which phase degraded,
making latency regressions faster to diagnose.
- Before-and-after phase profiles validate that an optimization
actually shrank the targeted phase without regressing others.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Profiling an agent is the operation of aggregating span-based
telemetry the reasoning pipeline already emits into contributions
per phase, and then asking which phase dominates the budget. The
decomposition is a grouping over existing trace data, provided
every span maps cleanly to a phase in a shared taxonomy. When that
mapping is ambiguous, a single span that covers both retrieval and
output formatting, or a reasoning iteration that hides an inline
tool call, the profile becomes untrustworthy and optimization
decisions drift. The pre-work is in defining the phases once,
aligning span types to them, and making the mapping visible to
every team contributing to the agent.

The dominant phase varies by workload and shifts over time. For
example:

- A conversational question-and-answer agent is usually
inference-bound
- A retrieval-heavy agent that reads across several knowledge
bases can be retrieval-bound
- A multi-agent workflow that serially hands off context between
supervisor and workers is typically coordination-bound
- An agent that invokes external APIs can be tool-bound when a
downstream service degrades

Optimizing the wrong phase produces no measurable user-facing
improvement. For example, a 30 percent inference speedup is
invisible when inference accounts for 10 percent of the budget and
retrieval accounts for 60. Phase-level attribution helps prevent
that mistargeting, and it remains necessary even after a workload
has been tuned because the dominant phase at launch rarely stays
dominant after prompts, tools, and models evolve.

Compute profiles at the distribution level, not the mean. Averages
hide the tail, and tail latency is what users experience when an
agent feels slow. Compute p50, p90, and p99 for each phase
separately, and for total latency. The dominant phase at the
median is often not the dominant phase at p99, because the slow
tail typically concentrates in one or two phases, inference during
model throttling, retrieval during index rebuilds or cold caches,
tool calls during downstream-service incidents. A profile that
reports means only by phase can point a team at the wrong target,
because the phase that hurts users at the tail is usually smaller
than the phase that dominates the average.

Run profiling against production traffic patterns for credible
results. Synthetic load tests can exercise the request path, but
they rarely reproduce the prompt distributions, tool-selection
behaviors, and concurrency patterns real users generate. This
means that bottlenecks that only appear under contention stay
invisible, like thread-pool starvation during fan-out, cache-miss
bursts after warmup expires, or queueing in shared inference
endpoints.

With
[Amazon CloudWatch Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) ingesting 100 percent of
spans to the aws/spans log group, you can
reconstruct a production profile from real traffic using
[CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) queries over span durations without standing
up dedicated profiling infrastructure. Agents on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) produce compatible span data
automatically when AgentCore Observability is enabled, and agents
on Amazon ECS, Amazon EKS, AWS Lambda, or self-hosted
infrastructure produce it through the
[AWS Distro for OpenTelemetry](https://aws-otel.github.io/docs/introduction) collector, so both populations
share a single surface.

Rank optimization targets by contribution multiplied by
addressable variance, not by contribution alone. A phase that
contributes 40 percent of the budget but is already near its
theoretical floor offers less headroom than a phase that
contributes 25 percent but has high variance driven by
implementation choices, sequential retrieval that could be
parallelized, or tool calls that could be cached.

Profiling also makes it possible to detect regression by phase.
Once a baseline distribution exists for each phase,
[Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) alarms on a phase drifting
outside its expected band before the change shows up in the SLO,
so regressions are attributed to the offending phase at alert time
rather than during an incident retrospective.

### Implementation steps

- **Define the phase taxonomy for the
workload:** Enumerate the phases that make up
end-to-end execution, input processing, context and memory
retrieval, LLM inference, tool invocation, output generation
or streaming, and inter-agent coordination, and map every
span type emitted by the agent to exactly one phase,
aligning span attributes with the
[OpenTelemetry
generative AI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/). Document the
taxonomy so every team contributing spans groups them the
same way, and add workload-specific phases such as guardrail
evaluation or structured-output post-processing when they
sit outside the common set.
- **Aggregate spans into per-phase
duration metrics:** Derive per-phase durations from
the span log group using
[CloudWatch
Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) and
[CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) queries that sum span durations grouped
by phase and trace, then emit the result as
[CloudWatch
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) with a phase dimension. Publishing the
profile as metrics, rather than only as ad-hoc log queries,
lets the same signal flow into dashboards, alarms, and
anomaly detection alongside native runtime metrics.
- **Compute percentile-level profiles
for every phase:** Calculate p50, p90, and p99 per
phase and for end-to-end latency over a rolling window that
matches the service level objective interval, and display
the percentiles side by side. The dominant phase at the
median is often not the dominant phase at p99, and profiling
against only the mean hides the tail where user-perceived
slowness concentrates.
- **Visualize the contribution of each
phase to end-to-end latency:** Build a stacked
per-phase contribution view on a
[customized
CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html) using the per-phase metrics
emitted in the previous step, and use
[dashboard
variables](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_dashboard_variables.html) to pivot the same view across the standard
dimension set, agent ID, workflow, environment, task type,
model ID, so dominant-phase analysis runs per slice rather
than against a fleet average that can obscure
tenant-specific or workflow-specific bottlenecks. Pair the
custom view with the pre-built
[Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) views for
session, trace, and span drill-down when a specific slow
request needs investigation.
- **Profile under production traffic
rather than only synthetic tests:** Run the profile
against real production trace data so concurrency effects,
prompt-mix variance, and downstream contention appear in the
distribution. Use synthetic load from tools such as the
[Distributed
Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/solution-overview.html) solution to stress-test specific
hypotheses, for example, to confirm that a proposed
parallel-retrieval change removes an observed p99 tail, and
anchor the phase-contribution view itself to production
traffic so decisions reflect how users actually exercise the
agent.
- **Rank optimization targets by
contribution and addressable variance:** For each
phase, estimate the contribution to the end-to-end budget
and the fraction of that contribution that is addressable by
engineering effort. Prioritize phases where both are high, a
large contribution with room to shrink, over phases that are
large but already near their theoretical floor, so
engineering time moves user-visible latency rather than a
metric that doesn't affect the tail.
- **Set per-phase baselines and alarm on
drift:** Establish a steady-state baseline
distribution for each phase, then apply
[CloudWatch
anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) to the per-phase percentile metrics
so deviations fire with the offending phase already
attributed. Pair the phase-level alarms with the end-to-end
service level objective so a phase drifting inside its
per-phase budget triggers investigation before the
end-to-end budget is exceeded.
- **Measure before and after every
optimization:** Capture the profile for each phase
before an optimization is rolled out and compare it against
the same profile under production traffic after the change
lands. Validate that the targeted phase actually shrank,
check that no other phase regressed to absorb the budget,
and retain the comparison in the change record so future
regressions can be diagnosed against a known-good profile.
- **Revisit the profile as the workload
evolves:** Agent behavior drifts as prompts, tools,
memory, and models change, and the dominant phase at launch
rarely stays dominant six months later. Refresh the
phase-based profile after every significant prompt or model
change and at least quarterly, then re-rank optimization
targets against the current profile so engineering effort
continues to land on the phase that actually limits
user-visible performance.

## Resources

**Related best practices:**

- [AGENTPERF01-BP01 Define
performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)
- [AGENTPERF01-BP02
Implement comprehensive performance telemetry](agentperf01-bp02.html)
- [AGENTPERF02-BP01
Design efficient reasoning pipelines](agentperf02-bp01.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Blog:
Build trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html)
- [Observability
and monitoring, Building serverless architectures for agentic
AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/observability-and-monitoring.html)

**Related videos:**

- [AWS re:Invent 2024 - Elevate application and generative AI
observability (COP326)](https://www.youtube.com/watch?v=vxzq8GthOLs)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Observability
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf01-bp03.html*

---
