# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 7

---

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

# AGENTPERF02 — Core processing and reasoning pipeline optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# AGENTPERF02-BP01 Design efficient reasoning pipelines

Each iteration of the perceive-reason-act loop typically involves an
LLM inference call, so the number of iterations an agent takes
multiplies both latency and cost. An efficient pipeline reaches
accurate decisions in the fewest iterations the task requires, uses
bounded iteration limits and confidence-based early termination to
help prevent runaway loops, and handles retries within explicit
performance budgets rather than silently eroding them.

**Desired outcome:**

- You have per-task iteration limits and confidence-based early
termination configured, so reasoning loops can't run without
bounds.
- You have pipeline shapes that scale reasoning depth to task
complexity, with simple tasks resolving in one or two iterations
and complex tasks receiving the iterations they need.
- You have retry strategies bounded by explicit latency budgets,
with semantic re-prompting or graceful degradation engaged
before the end-to-end SLO is exceeded.
- You have average reasoning iterations per task tracked as a
first-class KPI, visible alongside latency and token metrics.

**Common anti-patterns:**

- Allowing agents to reason indefinitely without iteration limits
or early termination conditions, producing runaway loops that
consume tokens and time without improving output quality.
- Designing reasoning pipelines that always execute the same
sequence of steps regardless of task complexity, applying
heavyweight reasoning to simple tasks that could be resolved
with a single inference call.
- Designing retry strategies without performance budgets, so
exponential backoff retries accumulate latency that exceeds the
end-to-end SLO when semantic re-prompting or graceful
degradation would preserve performance targets.
- Retrying a failed LLM call with the identical prompt and model,
rather than re-prompting semantically, rephrasing the
instruction, simplifying the task, or falling back to a more
capable model, to increase the chance that the retry succeeds
inside the remaining latency budget.

**Benefits of establishing this best
practice:**

- Efficient pipeline design reduces the number of LLM inference
calls per task, which is one of the highest-impact optimizations
for agent latency and cost.
- Adaptive pipeline shape makes simple tasks resolve quickly while
complex tasks receive the iterations they need.
- Explicit retry budgets and semantic re-prompting keep tail
latency within SLO even when a tool or model call fails on the
first attempt.
- Iteration caps produce tighter latency distributions that
simplify capacity planning, auto scaling thresholds, and cost
forecasting.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Total latency and token spend scale with the number of iterations
the pipeline takes to reach an accepted output, so pipeline
design, how the loop is structured, when it terminates, and how
failures are handled has a multiplicative effect on both latency
and cost. A well-designed pipeline reaches an accepted output in
the fewest iterations the task actually requires.

The right pipeline shape depends on task complexity and
predictability.
[Basic
reasoning agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/basic-reasoning-agents.html) handle single-turn classification,
extraction, or summarization in one inference call and should not
be wrapped in iterative reasoning loops.
[ReAct-style
loops](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html), in which the agent interleaves reasoning, tool
calls, and observation, fit open-ended tasks where the next step
can't be predicted at design time.

Plan-then-execute shapes such as ReWOO and plan-and-solve hybrids
separate planning from execution and bound iteration by plan
length rather than by the model's willingness to keep looping, and
reflect-and-revise shapes such as Reflexion introduce explicit
critique cycles with hard caps on revision passes. Both patterns
are described in
[Customize
agent workflows with advanced orchestration techniques using
Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/).

Iteration caps and early termination are the two controls that
keep a loop from consuming resources without producing value, and
they serve complementary roles. A per-task iteration cap is an
upper bound that helps prevent pathological runaway (a model that
keeps calling tools without converging), and it must be set per
task class because a ceiling appropriate for multi-step research
is wasteful for a simple lookup.

Early termination ends the loop before the cap when additional
iterations would not improve the output. For example, when a
critique step returns a structured "no further revision
needed" signal, when the agent's own confidence assessment
exceeds a threshold, or when a deterministic validator (schema
check, grounding check, policy check) confirms the output is
acceptable.

Together, caps help prevent the worst case while termination
removes the common case of paying for unnecessary iterations.

Failure recovery is part of the latency budget, not an exception
to it. When a tool call or model inference fails, naive
exponential backoff can consume more time than the end-to-end
target allows. Every retry strategy should be bounded by an
explicit performance budget that specifies how much latency and
how many tokens retries can consume before the pipeline falls back
to a degraded response.

Identical retries against the same prompt and model frequently
fail for the same reasons:

- Semantic re-prompting (rephrasing the instruction, simplifying
the task, or tightening the output contract)
- Model escalation (routing the retry to a more capable model)
- Tool substitution (using an alternative data source)

Each of these failures change a variable in the failure mode and
increase the chance that the retry succeeds within the remaining
budget. To preserve user trust, implement strategies like graceful
degradation, returning a partial answer with marked gaps, a
lower-confidence answer with explicit uncertainty, or a clear
"can't complete" response before the latency target
is exceeded.

Average reasoning iterations per task belongs alongside latency,
tokens, and cost as a first-class performance KPI. It is the
earliest signal that pipeline shape, prompt quality, or upstream
tool reliability has drifted, because a rising iteration count
typically precedes a latency or cost regression. Each extra
iteration compounds with the others downstream before the
user-facing metric shifts enough to trigger an alarm.

Tracked by task class and by pipeline shape, iteration count also
reveals misrouted tasks like simple requests running through
heavyweight loops or complex tasks capped before they converge.
Both of these patterns are invisible to metrics that only measure
the end result.

### Implementation steps

- **Classify each agent task by
reasoning complexity:** Group tasks by the
reasoning depth they require, single-step extraction or
classification, multi-step reasoning over known steps, and
open-ended investigation where the path isn't knowable in
advance. Use this classification as the input to
pipeline-shape selection and iteration budgets, because
applying the same shape and budget to every class either
wastes iterations on simple work or under-reasons on complex
work. Document the classification alongside the workload's
success criteria so routing decisions can be audited and
revisited as task distributions change.
- **Select a pipeline shape that matches
each task class:** Map each class to a reasoning
pattern documented in
[Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html), a
[basic
reasoning pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/basic-reasoning-agents.html) for single-step tasks, a
[ReAct
loop](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html) for open-ended reasoning where tool use drives
the next step, and a plan-then-execute or reflect-and-revise
shape for tasks that benefit from an explicit planner or
critique stage as described in
[Customize
agent workflows with advanced orchestration techniques using
Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/). Avoid wrapping single-step tasks in
iterative loops, which inflates cost and latency with no
accuracy gain.
- **Set per-task iteration caps sized to
the complexity class:** Configure a hard maximum on
reasoning iterations for each task class using the
iteration-control primitive exposed by the agent framework
in use, and size the cap to a value the workload will hit
only on pathological cases. Caps are a floor on the worst
case, tasks that converge early still terminate early
through the confidence signals configured next, so tune caps
to the most complex variant of each class rather than to the
typical case.
- **Define early-termination conditions
so loops stop when iterations stop adding value:**
Specify structured signals that end the loop before the cap,
a critique step returning a boolean "revision
needed" flag, a confidence score exceeding a defined
threshold, or a deterministic validator (schema, grounding,
or policy check) confirming the output is acceptable. Treat
these signals as data the pipeline produces and logs, not as
implicit model behavior, so termination decisions are
observable and auditable rather than hidden inside a chain
of thought.
- **Establish a retry budget bounded by
the end-to-end latency target:** Allocate an
explicit portion of the end-to-end latency target to retry
handling and enforce it at the pipeline level so accumulated
retries can't silently exceed the target. Decompose the
budget into latency and token components, because a retry
that stays inside the latency budget but triples token
consumption still degrades unit economics. Align the budget
with the service level objective the workload is graded on
so retry behavior is measured against the same target as
everything else in the pipeline.
- **Replace identical retries with
semantic re-prompting, model escalation, or tool
substitution:** When a call fails, retry with a
rephrased instruction, a simpler task decomposition, a more
capable model, or an alternative tool, each changes a
variable in the failure mode instead of repeating the same
failing call. Select the substitution based on the failure
signal: a timeout suggests model escalation or tool
substitution, a parsing failure suggests re-prompting with a
stricter output contract, and a grounding failure suggests
retrieval expansion.
- **Configure graceful degradation paths
that return before the target is exceeded:** Define
the fallback response for each task class, a partial answer
with marked gaps, a lower-confidence answer with explicit
uncertainty, or a clear "unable to complete"
response, and invoke the fallback when the retry budget is
exhausted or the latency budget is within a configured
safety margin of being exceeded. Predictable tail behavior
and a clear failure response preserve user trust better than
maximizing the chance of an eventual success on every
request.
- **Emit reasoning iterations, retries,
and terminations as first-class telemetry:**
Publish iteration count, termination cause (early
termination, cap hit, retry-budget exhausted, graceful
degradation), and retry count for every invocation as
metrics that can be thresholded and alarmed alongside
latency and token metrics using a capability such as
[Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) or an
equivalent pipeline on the agent's runtime. Put average
iterations per task on the same dashboards as latency
percentiles and cost per completion, since it is the
earliest indicator that pipeline shape, prompt quality, or
tool reliability has drifted.
- **Review pipeline shape, caps, and
budgets against production telemetry on a defined
cadence:** Schedule regular reviews of iteration
distributions, early-termination rates, retry-budget
consumption, and degradation frequency so pipeline
parameters track actual behavior rather than launch-time
assumption. Tighten caps that are consistently
under-utilized, relax caps that are being hit on legitimate
complex tasks, and re-classify tasks whose iteration
distribution reveals they belong to a different complexity
class than originally assigned.

## Resources

**Related best practices:**

- [AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)
- [AGENTPERF03-BP02
Optimize context window utilization and prompt
management](agentperf03-bp02.html)

**Related documents:**

- [Blog:
Customize agent workflows with advanced orchestration
techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Agentic
AI - Generative AI Lens (Well-Architected Framework)](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html)
- [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf02-bp01.html*

---

# AGENTPERF02-BP02 Implement task-appropriate model selection strategies

Agent tasks vary widely in the reasoning they require, but default
routing often sends every task to the same large model, paying the
latency cost of a heavyweight model even for work a smaller one
resolves as well. Matching model capability to task demand is one of
the highest-use performance decisions in an agent system, because
inference latency and throughput scale directly with model size.
Done systematically, model selection reduces per-task latency
without sacrificing quality on complex reasoning.

**Desired outcome:**

- You have agent tasks classified by reasoning complexity, with
each class mapped to the smallest model that meets its quality
bar.
- You have routing logic that directs each request to its assigned
model at runtime, with a cascading fallback to a more capable
model when the assigned model produces low-confidence or failed
outputs.
- You have model assignments validated against benchmarked quality
and latency on the workload's own task distribution rather than
on generic leaderboard rankings.
- You have model selection treated as a runtime-configurable
parameter so new model releases can be evaluated and rolled out
without redeploying the agent.
- You have inference latency and task quality tracked per task
class, so routing decisions are continually validated against
both.

**Common anti-patterns:**

- Using a single large model for every agent task regardless of
complexity, paying the latency and cost premium of a heavyweight
model on work a smaller one resolves as well.
- Using a small or general-purpose model for tasks that require
deeper reasoning, producing low-quality outputs that trigger
retries, extra reasoning iterations, or manual escalation and
eroding the latency savings the small model was meant to
provide.
- Selecting models from general benchmark rankings rather than
from benchmarks run on the workload's own task distribution,
producing choices that are optimal for the leaderboard but
suboptimal for actual traffic.
- Treating model choice as a one-time architectural decision baked
into application code, so evaluating or rolling out a newly
released model requires a code change and redeploy rather than a
configuration update.
- Operating without a fallback path when the assigned model
returns low-confidence or failing outputs, forcing the pipeline
to return a poor answer or fail entirely rather than escalating
that request to a more capable model.

**Benefits of establishing this best
practice:**

- Routing lightweight work to smaller, faster models avoids paying
the inference time of a large model for tasks that don't require
it.
- Explicit routing to capable models and cascading fallback when a
smaller model underperforms protect user-facing accuracy on
complex tasks.
- Benchmarks against the workload's actual task distribution
continually improve assignments as new evaluation data
accumulates.
- Runtime-configurable selection lets capability and latency
improvements from new models reach production without redeploy
cycles.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The reasoning pipeline's dominant cost component is the inference
call, and inference latency and throughput scale directly with
model size. Typical agent workloads have heterogeneous task mixes
and simple classification alongside multi-step reasoning, so
applying the largest model uniformly forces the blended latency
and cost to track the most capable option even though most
requests don't need it. Systematic model selection shifts this by
assigning each task to the smallest model that still meets its
quality bar.

Two approaches fit together:

- Explicit task classification, where the agent assigns each
task to a class and each class to a model or model tier, gives
fine-grained control and works across providers and model
families.
- Managed routing such as
[Amazon
Bedrock intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) predicts response
quality per request within a model family and routes to the
smallest model predicted to meet the quality bar, which hands
off the per-request pick when the decision is purely
capability-compared to-cost inside one family.

Many workloads combine both. The agent picks the tier by task type
while the router selects the specific model within that tier.
Purpose-built services such as
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) for intelligent document processing
are also worth considering as a model for document-heavy tasks,
where a dedicated pipeline is typically faster and more accurate
than routing documents through a general-purpose vision model.

Routing decisions are only as good as the benchmarks behind them.
Public leaderboards rank models on averages across heterogeneous
benchmarks whose task distributions can bear little resemblance to
a specific workload, so a model that leads a general benchmark can
underperform on the traffic a particular agent actually serves.

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) provides built-in evaluators,
LLM-as-a-Judge, ground-truth correctness, and trajectory matching
that make it practical to benchmark candidate models against an
evaluation set representative of actual traffic. Without
workload-specific evaluation, routing choices are effectively
guesses.

Selection is the starting point of a request, not the end of the
decision. Cascading fallback preserves quality without forcing the
whole task class to the larger model. Fallback differs from retry:
retries repeat the same call hoping for a better draw, while
fallback changes a variable by switching models. To promote new
models through progressive rollouts with automated rollback, hold
model identifiers, tier mappings, and fallback rules as runtime
configuration in
[AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) feature flags (or a comparable config service),
combined with
[deployment
strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html) gated by CloudWatch alarms on latency and
quality.

Per-class latency, token consumption, quality scores, and
fallback-escalation rate belong on the same performance dashboards
as total latency and reasoning iteration counts. A rising fallback
rate on a class is an early indicator that the primary model no
longer fits, either because traffic has shifted or because a newly
available model would serve the class better. This typically shows
up before the user-facing regression is large enough to alarm.

### Implementation steps

- **Classify agent tasks by reasoning
complexity:** Group the workload's tasks into
classes based on the reasoning they require, for example,
single-step extraction or classification, structured
multi-step reasoning over known steps, and open-ended
investigation. Document representative examples per class so
routing decisions are auditable and can be revisited as task
distributions shift. Use the classification as the input to
model assignment rather than letting each caller pick a
model case by case.
- **Benchmark candidate models on the
workload's own task distribution:** Build an
evaluation set representative of production traffic and
score candidate models against it using
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) or an equivalent
evaluation harness. Capture quality signals (correctness,
goal success rate, tool-trajectory match) alongside latency
and tokens so you can identify the smallest model meeting
the quality bar for each class. Treat leaderboard rankings
as a starting shortlist, not as the decision.
- **Map each task class to a model or
model tier:** Define a small set of tiers, for
example, fast, standard, and advanced, and assign each class
to the tier that benchmarks demonstrate is sufficient. For
each tier, select a specific model or Amazon Bedrock
inference profile. Where routing within a family is the
goal,
[Amazon
Bedrock intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) can make the
per-request pick automatically. For document-heavy tasks,
consider
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) as the right example rather
than a general-purpose vision LLM.
- **Implement routing logic that
dispatches requests to the assigned model at
runtime:** Resolve the task-class-to-model mapping
at the start of each request and issue the inference call
against the chosen model. When crossing providers or model
families, a framework abstraction such as
[Strands
Agents model providers](https://strandsagents.com/docs/user-guide/concepts/model-providers/) keeps the routing code stable
as providers change underneath it.
- **Configure a cascading fallback to a
more capable model for low-confidence or failing
outputs:** Define structured signals, confidence
score below a threshold, schema validation failure, parse
error, or an explicit incomplete response, that escalate the
specific request to a more capable model. Limit the
escalation to a single step so tail latency stays
predictable, and log both the primary and fallback decision
for each request that escalates.
- **Externalize model assignments and
routing rules as runtime configuration:** Hold
model identifiers, task-class-to-tier mappings, and fallback
rules in
[AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) feature flags (or an equivalent config
service) and read them at request time. Decoupling selection
from deployment lets new models be evaluated, promoted, or
rolled back without redeploying the agent.
- **Roll out model changes progressively
with automated rollback:** Use
[AWS AppConfig deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html) to shift traffic to a
new model in steps with bake-time validation, and attach
CloudWatch alarms on latency and quality so the change rolls
back automatically when the alarm fires. Treating a model
swap as a monitored deployment makes frequent model updates
safe.
- **Emit per-task-class telemetry for
latency, tokens, quality, and fallback rate:**
Publish per-class metrics so the effect of each routing
decision is visible on dashboards and can be alarmed. Use
[Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) together with
[AgentCore
Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) to attribute latency, tokens, and
evaluation scores to the class and model that served each
request.
- **Review routing decisions against
production telemetry on a defined cadence:**
Schedule periodic reviews of per-class latency
distributions, fallback-escalation rates, and quality
scores, and re-run AgentCore Evaluations against newly
released models using the same task-distribution benchmark.
Promote, demote, or re-tier models based on observed data
rather than provider release cadence.

## Resources

**Related best practices:**

- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)
- [AGENTPERF02-BP01 Design
efficient reasoning pipelines](agentperf02-bp01.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)
- [AGENTPERF02-BP04
Optimize streaming responses and time-to-first-token for agent
interactions](agentperf02-bp04.html)

**Related documents:**

- [Understanding
intelligent prompt routing in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)
- [Evaluate
agent performance with Amazon Bedrock AgentCore
Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [What
is AWS AppConfig?](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)
- [Create
a deployment strategy (AWS AppConfig)](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html)
- [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/introduction.html)
- [Blog:
Build reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [Strands
Agents Model Providers](https://strandsagents.com/docs/user-guide/concepts/model-providers/)

**Related videos:**

- [AWS re:Invent 2025 - Mastering model choice: The 3-step Amazon
Bedrock advantage (AIM391)](https://www.youtube.com/watch?v=Vu91YwZxskY)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Evaluations](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf02-bp02.html*

---

# AGENTPERF02-BP03 Optimize agent execution paths for reduced latency

Most of an agent request's total latency time is spent waiting on
model inference, retrieval, tool invocations, and memory lookups
rather than on CPU work inside the agent process. Executing
independent operations concurrently, reusing warm connections and
runtimes, and deduplicating repeated lookups within a single request
cut total latency without changing models or prompts.

**Desired outcome:**

- You have independent operations within an agent request executed
concurrently sequential execution is reserved for operations
with genuine data dependencies.
- You have connections to downstream services, model endpoints,
tool APIs, memory stores, vector indexes, pooled and reused
across requests rather than reestablished per invocation.
- You have runtime cold starts removed from the critical path or
bounded through provisioned capacity, pre-warming, or persistent
execution environments.
- You have repeated lookups within a single request resolved from
a request-scoped cache, so duplicate work isn't paid twice
inside one invocation.

**Common anti-patterns:**

- Executing independent operations sequentially when they share no
data dependencies, making total latency the sum of operation
durations rather than the slowest operation.
- Establishing new connections to model endpoints, tool APIs, or
data stores on every invocation, paying connection setup and TLS
handshake costs on the critical path.
- Running agent code on compute that pays a cold-start penalty on
the critical path without provisioned capacity, pre-warming, or
a persistent runtime to absorb it.
- Re-executing the same lookup multiple times within a single
request, for example, fetching the same knowledge base passage
or user profile across consecutive reasoning steps, with no
request-scoped cache to deduplicate the work.
- Introducing parallelism without respecting downstream rate
limits or connection pool capacity, so concurrent calls throttle
or queue and the intended latency win turns into added latency
plus failures.

**Benefits of establishing this best
practice:**

- Overlapping independent operations makes the critical path track
the slowest operation rather than the sum of every operation.
- Amortizing connection setup and runtime initialization across
requests avoids paying those costs on every invocation.
- Parallel calls that respect downstream capacity avoid the
throttling and retry storms naive parallelism triggers.
- Overlapping I/O-bound waits, retrievals and tool calls, with
compute-bound work such as inference and parsing keeps the agent
productive during waits.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Most of an agent request's total latency time is spent waiting, on
model inference, retrieval, tool invocations, and memory lookups,
rather than on CPU work inside the agent process. The structure of
how those waits are composed dominates total latency more than the
speed of any single downstream dependency. Four structural
decisions typically affect latency:

- Running independent operations concurrently rather than
sequentially
- Reusing warm connections and runtimes across invocations
- Removing cold starts from the critical path
- Deduplicating repeated lookups within a single request.

Each decision is independent of model and prompt choices, so the
gains compound with the reasoning-loop and model-selection
optimizations addressed elsewhere in this pillar.

Concurrency is the largest impact when the agent fans out across
independent data sources or tool calls. Dependency analysis
identifies operations that share no data dependency (for example,
a personalization lookup and a knowledge-base query issued from
the same reasoning step, and executes them in parallel so the
step's latency equals the slowest operation rather than the sum).

Agent frameworks expose this directly. Strands Agents executes
independent tool calls emitted in a single reasoning step
concurrently, and graph-based orchestrators such as LangGraph fan
out across independent edges. The constraint is downstream
capacity, where concurrent model calls and tool invocations must
respect
[Amazon
Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) (requests-per-minute and
tokens-per-minute) and tool-API rate limits, or parallelism
converts into throttling and retry storms that undo the latency
win.

Connection reuse and cold-start removal address the per-invocation
setup costs that compound with concurrency. HTTP connections to
model endpoints and tool APIs should persist across invocations
through the SDK or HTTP-client connection pool rather than be
opened and torn down per request. Each fresh connection pays
TLS-handshake and connection-setup overhead on the critical path
that a pooled connection avoids entirely, and that overhead
accumulates across fan-out and across invocations.

Database connections follow the same principle.
[Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) pools connections to Aurora and RDS so serverless
agents don't exhaust database connection limits or pay
connection-setup latency per invocation. At runtime,
[Amazon
Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) reuse a dedicated
microVM across invocations that share a session identifier, which
removes cold starts while a session is active and preserves
in-memory state across reasoning steps.

For agents hosted on AWS Lambda,
[Lambda
provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) pre-initializes execution
environments and
[Lambda
SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) restores from a cached snapshot on supported
runtimes, reducing first-invocation latency to sub-second at the
cost of continuous capacity or per-restoration charges.

Request-scoped caching addresses redundant work that happens
inside a single invocation rather than across invocations. A
reasoning loop that calls the same tool twice, retrieves the same
passage across successive steps, or refetches the same user
profile in the planner and the executor wastes latency budget on
repeated I/O. A cache keyed by the request or session identifier
deduplicates these lookups for the remainder of the request
without the consistency complexity of a cross-request cache.

The scope is deliberately narrow, persistent and cross-request
caches such as Amazon Bedrock prompt caching and semantic caches
are higher-level optimizations addressed in context- and
memory-focused best practices. However, request-scoped
deduplication is frequently the lowest-risk caching optimization
available, because the cache is discarded at the end of the
invocation and can't serve stale data to a subsequent request.

### Implementation steps

- **Profile the critical path to
identify parallelizable operations:** Trace a
representative sample of production requests with the
performance telemetry already in place to decompose each
invocation into per-operation durations and dependencies.
Identify operations that share no data dependency, separate
tool calls, independent retrievals, personalization lookups
alongside knowledge queries, and flag the sequential
segments where concurrency would collapse wall-clock latency
onto the slowest operation. Revisit the inventory as prompts
and tools change, because dependency graphs shift with them.
- **Execute independent operations
concurrently within downstream capacity limits:**
Configure the agent framework to fan out independent tool
calls and retrievals in the same reasoning step, Strands
Agents, LangGraph, and similar frameworks expose this as a
native primitive. Bound concurrency to the downstream
service's capacity,
[Amazon
Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html), tool-API rate limits, and
database connection ceilings, so a step that fans out to 10
concurrent calls doesn't trigger throttling that costs more
latency than it saves.
- **Reuse connections to model endpoints
and external APIs across invocations:** Configure
the HTTP client's connection pool so TLS sessions to Amazon
Bedrock and tool APIs persist across invocations rather than
being reestablished per request. On runtimes that preserve
memory across invocations,
[AWS Lambda execution environments](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html), container-based
services, and long-running services, initialize the client
once per execution environment rather than per invocation so
its connection pool survives across calls. A warm invocation
should pay zero connection-setup latency on downstream
calls.
- **Pool database connections through a
managed connection pool:** For agents that read
from or write to relational data, front Aurora and RDS
databases with
[Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) so serverless invocations share a bounded
pool of database connections rather than opening a new
connection each time. Without a pooler, concurrent agent
invocations exhaust the database's connection ceiling and
pay per-invocation setup latency on the critical path, both
failure modes worsen as parallelism increases.
- **Remove cold starts from the agent
execution runtime:** Select a runtime that keeps
the agent's execution environment warm on the critical path.
[Amazon
Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) reuse a dedicated
microVM across invocations that share a session identifier,
preserving in-memory state and avoiding per-invocation cold
starts while the session is active. For Lambda-hosted
agents,
[Lambda
provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) pre-initializes execution
environments and
[Lambda
SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) restores from a cached snapshot on
supported runtimes. Always-on container services such as
Amazon ECS or Amazon EKS avoid cold starts entirely at the
cost of continuous capacity. Choose based on traffic shape
rather than runtime preference.
- **Deduplicate repeated lookups within
a single request using a request-scoped cache:**
Add an in-memory cache scoped to the lifetime of the request
or session that memoizes idempotent lookups, tool responses,
retrieved passages, user-profile reads, keyed by input. A
reasoning loop that calls the same tool twice or retrieves
the same passage across successive steps resolves the second
call from the cache, recovering that latency without the
consistency complexity of a cross-invocation cache. The
cache is discarded at the end of the request, so it can't
serve stale data to a subsequent invocation.
- **Re-measure the critical path after
each structural change and as traffic grows:**
After applying concurrency, pooling, cold-start, or caching
changes, re-profile the critical path under representative
production load to confirm the optimization held and did not
introduce new failure modes such as throttling or
connection-pool saturation. Repeat the measurement as
traffic grows, because parallelism bounded correctly at
launch frequently exceeds quotas at higher scale and the
latency profile silently regresses before an SLO is
exceeded.

## Resources

**Related best practices:**

- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)
- [AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html)
- [AGENTPERF02-BP04
Optimize streaming responses and time-to-first-token for agent
interactions](agentperf02-bp04.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)

**Related documents:**

- [Amazon
Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)
- [Amazon
Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html)
- [Amazon
Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
- [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)
- [AWS Lambda execution environments](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html)
- [AWS Lambda provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)
- [AWS Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)
- [Building
serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf02-bp03.html*

---

# AGENTPERF02-BP04 Optimize streaming responses and time-to-first-token for agent interactions

User-facing agents are judged on perceived latency, not total
processing time. Time-to-first-token (TTFT), the delay before the
first output reaches the user, is the dominant perceived-performance
signal, and streaming delivery keeps TTFT short even when total
processing takes several seconds. Agentic streaming is complicated
by reasoning loops that must pause mid-stream to invoke tools and by
multi-agent workflows where the final agent streams while upstream
agents are still producing.

**Desired outcome:**

- You have TTFT tracked as a distinct KPI from end-to-end latency,
with a target bounded by the interaction type.
- You have LLM output streamed to the user as it is generated, so
the user begins seeing output well before the reasoning loop
finishes.
- You have pre-inference latency, context assembly, prompt
construction, retrieval, kept short enough that it doesn't
dominate TTFT.
- You have tool invocations handled within streams so the user
receives progress feedback rather than an unexplained pause when
the agent calls a tool mid-response.
- You have multi-agent workflows designed so the user-facing agent
begins streaming as soon as its inputs are available, rather
than blocking until every upstream agent fully completes.

**Common anti-patterns:**

- Waiting for the complete agent response before delivering any
output, making perceived latency equal to total processing time
rather than time-to-first-token.
- Streaming the LLM inference call but not the pre-inference
pipeline, so context retrieval and prompt construction add
seconds of delay before the first token reaches the user.
- Pausing the output stream with no indication when the agent
invokes a tool mid-response, so the user sees partial output
followed by an unexplained pause.
- Blocking multi-agent workflows until every upstream agent
finishes before the user-facing agent begins streaming,
converting sequential coordination delay into user-visible
latency.
- Treating TTFT as interchangeable with end-to-end latency in KPIs
and alarms, so regressions in time-to-first-token go unnoticed
while total-duration metrics look unchanged.

**Benefits of establishing this best
practice:**

- Sub-second time-to-first-token keeps the agent feeling fast even
when total processing time spans several seconds.
- Progress feedback replaces the unexplained pauses that would
otherwise appear to the user as a stall when tools run
mid-stream.
- Tracking TTFT as a distinct KPI surfaces drift in perceived
responsiveness that end-to-end latency dashboards would
otherwise hide.
- Progressive streaming in multi-agent workflows lets the
user-facing agent deliver output concurrently with upstream
processing rather than blocking until every upstream step
completes.
- A short TTFT reduces the share of users who abandon interactive
workloads before any output appears.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Time-to-first-token (TTFT) is typically the performance metric
that most directly shapes user perception of an interactive agent.
A response that begins within a few hundred milliseconds typically
feels fast to users even when total generation takes several
seconds. End-to-end latency and TTFT move independently. A faster
model improves total duration but leaves TTFT unchanged when the
pre-inference pipeline is the bottleneck, so tracking only total
latency hides the regressions users actually feel. The difference
lies in instrumenting TTFT as a distinct metric, separate from
total-duration dashboards.

Streaming the model's output is necessary but not sufficient: by
the time the first token leaves the model, the agent can already
have consumed the entire TTFT budget on work that happens before
inference begins. Context assembly, prompt construction,
retrieval, and serial pre-checks all count, and streaming recovers
nothing from that window.

The pre-inference path is usually where the most significant TTFT
improvements come from: compressing retrieval, narrowing retrieved
context, and parallelizing independent pre-inference steps. The
same concurrency and warm-connection patterns that reduce total
latency elsewhere in this pillar apply to the pre-inference path,
and they pay back specifically against TTFT. Post-inference
filtering is also in the budget.
[Amazon
Bedrock Guardrails streaming modes](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html) introduce an explicit
trade-off between moderation accuracy and TTFT that must be tuned
to the workload rather than left at default.

On Amazon Bedrock,
[ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
is the model-agnostic streaming inference API recommended for chat
and agent workloads, while
[InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)
remains available when a model-specific payload shape is required.
Both emit an event stream of content-block start, delta, and stop
events that the agent layer translates into user-visible output.

Tool invocation introduces a discontinuity. When the model decides
to call a tool, the event stream opens a content block of type
toolUse, streams the tool's input as deltas,
and then pauses while the agent runs the tool and feeds results
back. A client that receives no signal during this gap shows the
user partial output followed by a silent stall. The baseline
pattern, buffer-and-resume with an explicit progress indicator,
forwards a user-visible status the moment a tool-use block appears
and resumes streaming when the next content block starts. More
advanced patterns such as speculative streaming exist, but the
baseline is that no silent pause reaches the user.

Multi-agent pipelines amplify the TTFT problem when every upstream
agent must fully complete before the user-facing agent begins.
Each serial handoff contributes its full duration to TTFT rather
than overlapping with downstream work. Progressive streaming is
the alternative, where the user-facing agent begins reasoning as
soon as its minimum required inputs are available, and upstream
agents' intermediate outputs stream into its context as they are
produced.

Agent frameworks expose this pattern directly:
[Strands
Agents](https://strandsagents.com/) yields agent events (tokens, tool calls, messages)
as an async iterator that downstream consumers can subscribe to,
and graph-based orchestrators such as LangGraph expose equivalent
streaming primitives. Reserve synchronous full-response handoff
for workflows where the downstream agent genuinely can't begin
until the upstream result is complete.

Two AWS capabilities reduce inter-token latency and coordination
overhead beyond what API choice alone can deliver.
[Amazon
Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html) (in preview at
publication) reduces inter-token latency on supported models
through routing and capacity optimizations, at the cost of tighter
throughput limits and model-specific token ceilings. For voice and
real-time interactive workloads,
[Amazon
Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html) over
WebSocket or WebRTC allows the client to send input while the
agent is still streaming output, the prerequisite for natural
interrupt and turn-taking behavior in voice agents.

[Amazon
Nova Sonic](https://docs.aws.amazon.com/nova/latest/userguide/speech.html) provides a speech-to-speech path on Amazon
Bedrock. You can route voice through Amazon Nova Sonic rather than
separate speech-to-text, text-generation, and text-to-speech
stages, collapsing multiple sequential stages into one
bidirectional stream. This approach typically provides substantial
TTFT improvements for voice workloads.

### Implementation steps

- **Define TTFT targets for each
user-facing interaction type:** Set a TTFT target
per workload based on how the user consumes output, text
chat tolerates hundreds of milliseconds, voice tolerates far
less, batch pipelines have no user-facing TTFT at all. Treat
the target as a budget to be allocated across pre-inference
work, model first-token latency, and any post-processing,
and anchor it to user research or published
interaction-design norms rather than a round number.
- **Instrument TTFT as two distinct
metrics, pipeline TTFT and model TTFT:** Emit
*pipeline TTFT* at the user-facing
boundary (the first output byte reaching the client) as the
SLO KPI, and *model TTFT* at the first
text delta from the inference call whose output first
streams to the user, which isolates model and routing
behavior from pre-inference and post-processing
contributions. Publish both through
[OpenTelemetry
through the CloudWatch OTLP endpoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) or
[CloudWatch
Embedded Metric Format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html). When pipeline TTFT and model
TTFT diverge, the gap points at the non-model contributors.
- **Extend TTFT instrumentation to
multi-inference and voice workloads:** When an
agent makes multiple inference calls per request, planners,
routers, sub-agent fan-outs, treat silent upstream calls as
part of the pre-inference budget and emit per-call TTFT as a
tagged dimension so the contribution of each inference call
remains visible for diagnosis. For voice workloads, add
time-to-first-audio-chunk because text-token arrival is an
upstream signal, not the user boundary.
- **Reduce pre-inference latency on the
critical path to the first token:** Profile the
work that happens between request arrival and the first
inference call, context assembly, retrieval, prompt
construction, pre-checks, and compress or parallelize it so
most of the TTFT budget remains when the model begins
generating. The concurrency and connection-reuse patterns
applied elsewhere to reduce end-to-end latency pay back
specifically against TTFT when applied to the pre-inference
path. Streaming token delivery can't recover any time lost
before the first model call.
- **Use streaming inference APIs rather
than synchronous inference for user-facing
agents:** Call
[ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
as the model-agnostic default for chat and agent workloads.
Use
[InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)
only when a model-specific payload shape is required.
Consume the event stream as it arrives and forward each
content-block delta to the client rather than buffering the
full response server-side.
- **Tune Amazon Bedrock Guardrails
streaming mode when guardrails are in the critical
path:** If
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html) filters output on the user-facing
path, choose the stream processing mode based on the
workload's policy tolerance, synchronous processing raises
moderation accuracy and raises TTFT, asynchronous processing
preserves TTFT at the cost of potentially emitting a token
that is later retracted. Drive the decision for mode by the
content-risk profile of the workload.
- **Surface tool-invocation events to
the user rather than pausing the stream silently:**
When the model emits a tool-use event mid-stream, forward a
user-visible progress indicator to the client before the
agent begins executing the tool, and resume streaming when
the next content block starts. Use the explicit start and
stop boundaries of the tool-use content block as the signal
to transition the UI between streaming and working states,
rather than letting the client see a silent gap.
- **Stream multi-agent workflows
progressively rather than blocking on upstream
completion:** Design the orchestration so the
user-facing agent begins reasoning as soon as its minimum
required inputs are available, and pipe upstream
intermediate events into its context as they are produced.
Agent frameworks expose this streaming-handoff pattern
directly through async-iterator primitives such as
[Strands
Agents'](https://strandsagents.com/) streaming API and equivalent mechanisms in
graph-based orchestrators. Reserve synchronous full-response
handoff for workflows where the downstream agent genuinely
can't begin until the upstream result is complete.
- **Evaluate latency-optimized inference
for inter-token latency on supported models:**
[Amazon
Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html) (in preview at
publication) reduces inter-token latency on supported
models, Amazon Nova Pro, Anthropic Claude 3.5 Haiku, and
Meta Llama 3.1 70B/405B, through routing and capacity
optimizations, at the cost of tighter throughput limits and
model-specific token ceilings. Enable the latency mode on
the runtime API and validate with the two-metric TTFT
instrumentation that the reduction is real for the workload
rather than a cache-warmed artifact.
- **Use AgentCore Runtime bi-directional
streaming and Amazon Nova Sonic for voice and real-time
workloads:** For voice agents and other workloads
where the user must interrupt or turn-take, run the agent on
[Amazon
Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html)
over WebSocket or WebRTC so the client can send input while
the agent is streaming output. Route voice specifically
through
[Amazon
Nova Sonic](https://docs.aws.amazon.com/nova/latest/userguide/speech.html), which collapses the separate
speech-to-text, text-generation, and text-to-speech stages
of a traditional voice pipeline into a single bidirectional
stream, typically a substantial TTFT improvement for voice
workloads.
- **Re-measure TTFT after each change
and as traffic shifts:** Re-profile both pipeline
TTFT and model TTFT under representative production load
after applying streaming, pre-inference, tool-handling, or
runtime changes, because optimizations that work in
isolation frequently regress at scale. Alert on TTFT
percentile violations distinct from end-to-end latency SLOs
so regressions in perceived responsiveness surface before
they reach users.

## Resources

**Related best practices:**

- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)
- [AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)
- [AGENTPERF05-BP04
Implement efficient agent delegation and handoff
patterns](agentperf05-bp04.html)

**Related documents:**

- [Amazon
Bedrock ConverseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
- [Amazon
Bedrock InvokeModelWithResponseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)
- [Amazon
Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
- [Amazon
Bedrock Guardrails streaming](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html)
- [Amazon
Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html)
- [Get
started with bidirectional streaming using WebSocket on
AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-websocket.html)
- [Amazon
Nova Sonic, real-time conversational speech](https://docs.aws.amazon.com/nova/latest/userguide/speech.html)
- [CloudWatch
Embedded Metric Format specification](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html)
- [Publishing
custom metrics to Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- [AWS blog: Bi-directional streaming for real-time agent
interactions now available in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/bi-directional-streaming-for-real-time-agent-interactions-now-available-in-amazon-bedrock-agentcore-runtime/)

**Related examples:**

- [Amazon
Bedrock AgentCore samples, Runtime tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)
- [Amazon
Bedrock AgentCore samples, Nova Sonic integration](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/nova/nova-sonic)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore, Runtime](https://catalog.workshops.aws/agentcore-deep-dive/en-US/20-agentcore-runtime)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf02-bp04.html*

---

# AGENTPERF03 — Memory, context, and RAG optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# AGENTPERF03-BP01 Implement tiered memory management systems

Agents that carry context across turns and sessions deliver more
personalized and accurate responses, but only when memory retrieval
doesn't become the latency bottleneck on every reasoning iteration.
A tiered memory architecture separates fast, transient session state
from durable cross-session knowledge so each tier's storage
technology, access pattern, and lifecycle can be optimized
independently rather than forced through a single store.

**Desired outcome:**

- You have agent memory separated into a short-term tier for
in-session context and a long-term tier for cross-session
knowledge, each backed by storage matched to its access pattern.
- You have automated lifecycle policies that extract durable
insights from short-term memory into long-term strategies
(semantic, episodic, summary, and user preference) and evict
stale short-term state without manual intervention.
- You have per-tier retrieval latency tracked as a first-class
KPI, with budgets that keep memory access from dominating the
reasoning loop.
- You have long-term memory scoped and namespaced per user,
session, or tenant so retrievals return only the records
relevant to the current actor.

**Common anti-patterns:**

- Storing all agent memory in a single database regardless of
access pattern, forcing sub-second session reads and large-scale
semantic searches through the same storage layer.
- Persisting every turn of short-term memory indefinitely without
extraction into long-term strategies or eviction, allowing
session stores to grow without bounds and retrieval latency to
degrade over time.
- Treating long-term memory as a single bag of records rather than
differentiating between semantic facts, episodic events,
conversation summaries, and user preferences, which forces every
query to search all record types.
- Scoping long-term memory globally rather than per user, session,
or tenant, so retrievals return cross-actor records that inflate
context and leak information.
- Building custom tiered memory infrastructure from scratch
instead of evaluating managed services that provide session
stores, extraction strategies, and vector retrieval as
primitives.

**Benefits of establishing this best
practice:**

- Fast in-memory stores serve session reads in single-digit
milliseconds while vector stores handle long-term semantic
queries without coupling the two.
- Automated extraction and eviction policies keep each tier's
footprint and retrieval latency stable as usage scales.
- Separating long-term memory into distinct strategies, semantic,
episodic, summary, preference, lets the agent query only the
record type relevant to its current reasoning step.
- Namespacing long-term memory by user, session, or tenant helps
prevent cross-actor retrievals and keeps context relevant.
- Managed memory primitives remove the need to operate session
stores, extraction pipelines, and vector indexes as bespoke
infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Memory access sits on the hot path of every reasoning iteration.
An agent that reads session context and retrieves relevant
long-term knowledge at every step pays that retrieval latency
multiplied by the iteration count, which makes memory one of the
largest use points in the reasoning loop.

The root cause of poor memory performance is typically an
access-pattern mismatch. Using a single storage layer for both
sub-millisecond session reads and large-scale semantic searches
forces one pattern to carry cost and latency characteristics
suited to the other. Tiering resolves the mismatch by splitting
memory into a short-term tier for in-session context and a
long-term tier for cross-session knowledge, then matching each
tier to storage with the right latency, durability, and query
model.

Short-term memory holds the turn-by-turn state an agent reads and
writes within a single session: the last N turns, intermediate
reasoning, tool outputs, and transient user-provided context.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides a managed short-term tier
that stores session events and integrates with extraction into the
long-term tier, removing the need to operate a separate session
store or extraction pipeline.

For workloads that need sub-millisecond short-term reads or prefer
to own the extraction pipeline,
[Amazon ElastiCache (Valkey)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-why-elasticache.html) provides in-memory reads, TTL-based
expiration, and native structures (hashes, lists, sorted sets)
that map well to session data. Durability requirements for
short-term memory are typically low, state can be regenerated or
discarded on session end, so the tier should be sized for latency,
not for archival.

Long-term memory holds durable knowledge that persists across
sessions: user preferences, domain facts, past-interaction
summaries, and episodic records of past task outcomes. Access is
less frequent but operates over a much larger corpus and typically
relies on semantic similarity rather than key lookup. AgentCore
Memory provides a managed long-term tier with
[four
built-in strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html), semantic, episodic, summary, and user
preference, each extracted from session events and indexed
separately, so the agent can query only the store relevant to its
current reasoning step.

For teams that prefer to own the long-term store directly,
[agentic
memory in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-agentic-memory.html) provides dense and
hybrid retrieval over long-term records, and
[Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html) provides a graph-based alternative for
domains where long-term memory is defined by relationships between
entities, enabling multi-hop queries that vector similarity can't
answer on its own. Separating strategies (managed or self-indexed)
matters for performance, as every irrelevant record retrieved is
latency and context budget spent on noise.

Tiers are only high-performing when their lifecycle is automated.
Short-term state that isn't evicted grows until reads slow and
session stores run out of memory, while long-term records that are
not extracted from short-term events represent knowledge the agent
has to relearn every session.

Managed services handle both movements: AgentCore Memory extracts
long-term strategies from short-term events asynchronously and
applies TTLs to short-term records, while self-managed stacks must
build extraction and eviction explicitly, either by adopting an
open source orchestration layer such as Mem0 or by writing bespoke
pipelines on top of primitives like ElastiCache, OpenSearch, or
Neptune Analytics.

Long-term memory must also be namespaced by actor (user, session,
or tenant), because unscoped retrievals return records from other
actors that inflate context and, depending on the deployment, leak
information across isolation boundaries. Scoping is both a
performance control (a smaller search space per query returns
faster) and a correctness control.

### Implementation steps

- **Inventory the memory the agent reads
and writes:** List the distinct pieces of state the
agent maintains, last-N-turn context, intermediate
reasoning, tool outputs, user preferences, past-interaction
summaries, domain facts, and for each note the access
pattern (read per iteration, read per session, read per task
class), retention requirement (session-scoped or durable),
and query shape (key lookup or semantic search). This
inventory is the input to tier selection, as without it,
tier boundaries are drawn by guess and either fragment
naturally grouped data or collapse patterns that should be
separated. Record the inventory alongside the workload's
performance budgets so tiering decisions can be audited and
revisited.
- **Assign each inventoried item to a
short-term or long-term tier:** Place
session-scoped, high-frequency, latency-critical items in
the short-term tier and durable, cross-session items queried
semantically in the long-term tier. Avoid intermediate
"working memory" tiers unless a concrete access
pattern justifies one, most "working memory" is
either active short-term state or a long-term record that
has not been extracted. Document the tier boundary so every
new memory item has a clear home.
- **Choose storage for each tier based
on the tier's access pattern:** For the short-term
tier, select
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) if you also want managed
long-term extraction, or
[Amazon ElastiCache (Valkey)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-why-elasticache.html) if you prefer to own the
extraction pipeline. For the long-term tier, use AgentCore
Memory's built-in strategies or
[Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-agentic-memory.html) for dense and hybrid retrieval.
Resist using one storage layer for both tiers. It is the
single most common cause of memory-bound latency
regressions.
- **Configure long-term memory with
strategies that match what the agent retrieves:**
Enable the subset of
[AgentCore's
built-in long-term strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html), semantic, episodic,
summary, and user preference, that correspond to the
retrieval patterns in the inventory. Each strategy extracts
a different shape of record from short-term events and
indexes it separately, so the agent can query only the store
relevant to its current step. In self-managed stacks, create
equivalent per-strategy indexes rather than a single
general-purpose corpus.
- **Namespace every memory record to its
actor (user, session, or tenant):** Attach an actor
identifier to every short-term and long-term record and
filter every retrieval by that identifier using AgentCore
Memory's
[actor
and session scoping](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html) or an equivalent filter in
self-managed stacks. Scoping reduces the search space (lower
retrieval latency) and helps prevent cross-actor context
leakage (correctness and isolation). Align the actor key
with the authentication identity used by the agent so
scoping can't be bypassed by a missing filter in application
code.
- **Automate extraction from short-term
to long-term and eviction of stale short-term
state:** Configure the managed extraction pipeline,
AgentCore Memory's asynchronous strategy extraction, or
build an equivalent job in self-managed stacks that reads
session events, derives long-term records per enabled
strategy, and writes them to the long-term index. Apply TTLs
or sliding-window eviction to short-term state so session
stores don't grow without bounds. Both movements must run
without manual intervention. If either requires human
action, memory growth and extraction lag will exceed design
targets.
- **Emit per-tier retrieval latency as a
first-class performance metric and set budgets:**
Publish short-term read latency and long-term query latency
as distinct time-series through
[Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) or an
equivalent pipeline, alongside tier size, hit rate, and
extraction lag. Allocate each tier an explicit portion of
the per-iteration latency budget so memory can't silently
consume time reserved for inference or tool calls. Treat
per-tier latency as an early indicator: sustained growth in
long-term query latency usually signals index size or scope
drift before it registers on end-to-end metrics.
- **Review tier sizing, strategies, and
budgets against production telemetry on a defined
cadence:** Schedule reviews of short-term tier size
distributions, long-term strategy growth rates, extraction
lag, and per-tier latency against budget. Tighten TTLs on
short-term stores that are consistently oversized, disable
long-term strategies that are never queried, and re-scope
memory if retrievals are returning more cross-actor records
than the scope intended. Tiering parameters set at launch
rarely match production traffic unless they are reviewed on
an ongoing basis.

## Resources

**Related best practices:**

- [AGENTPERF03-BP02
Optimize context window utilization and prompt
management](agentperf03-bp02.html)
- [AGENTPERF03-BP03
Optimize RAG retrieval pipelines for latency and
precision](agentperf03-bp03.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)
- [AGENTPERF03-BP05
Implement agentic retrieval patterns for dynamic, agent-driven
knowledge access](agentperf03-bp05.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [AgentCore
Memory, memory organization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html)
- [AgentCore
Memory, long-term built-in strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html)
- [Agentic
memory in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-agentic-memory.html)
- [Why
use ElastiCache for agentic memory](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-why-elasticache.html)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)
- [Blog:
Amazon Bedrock AgentCore Memory, Building context-aware
agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [Blog:
Building smarter AI agents, AgentCore long-term memory deep
dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [Blog:
Build agents to learn from experiences using AgentCore
episodic memory](https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/)
- [Blog:
Build persistent memory for agentic AI applications with Mem0,
ElastiCache for Valkey, and Neptune Analytics](https://aws.amazon.com/blogs/database/build-persistent-memory-for-agentic-ai-applications-with-mem0-open-source-amazon-elasticache-for-valkey-and-amazon-neptune-analytics/)

**Related videos:**

- [AWS re:Invent 2024 - Make agents remember with Amazon Bedrock
AgentCore Memory (AIM331)](https://www.youtube.com/watch?v=Sh0Ro00_rpA)
- [AgentCore
Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)
- [Solving
LLM Amnesia: Cross Session Memory](https://www.youtube.com/watch?v=ZY5WXDDp9g8)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Memory tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore, Memory](https://catalog.workshops.aws/agentcore-deep-dive/en-US/50-agentcore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp01.html*

---

# AGENTPERF03-BP02 Optimize context window utilization and prompt management

Every token sent to an LLM competes for the model's attention,
consumes input-token cost, and adds inference latency, which makes
prompt content a first-order performance lever. Effective context
window management budgets tokens across prompt components, assembles
only what the current task needs, and compresses or summarizes the
rest. Without this discipline, conversation history and tool schemas
crowd out reasoning capacity and inflate latency on every iteration.

**Desired outcome:**

- You have an explicit token budget allocated across prompt
components, system instructions, conversation history, retrieved
knowledge, and tool schemas, with per-component token usage
measured on every request.
- You have context assembled dynamically per request, including
only the tool definitions, retrieved passages, and conversation
context relevant to the current task rather than a fixed maximal
payload.
- You have conversation history bounded by summarization, sliding
windows, or semantic compression so prompt size doesn't grow
linearly with session length.
- You have prompt templates versioned and evaluated so changes to
wording, ordering, or component composition are measured against
quality and token-cost baselines before rollout.

**Common anti-patterns:**

- Including the full conversation history in every prompt without
summarization or truncation, causing prompt size and inference
latency to grow linearly with session length.
- Injecting the full tool catalog in every prompt regardless of
task relevance, spending context budget on schemas the agent
will not invoke for the current request.
- Passing RAG retrievals straight into the prompt without
per-passage filtering or truncation, so low-relevance chunks
displace more useful context.
- Treating the prompt as a single opaque string rather than a
composition of components, making it impossible to attribute
token consumption to system instructions, history, retrievals,
or tool schemas.
- Shipping prompt changes without versioning or side-by-side
evaluation, so quality or token-cost regressions are detected
only after rollout.

**Benefits of establishing this best
practice:**

- Removing tokens from the prompt can reduce request cost and
shorten time-to-first-token on each iteration.
- Pruned, high-density context leaves more of the model's
effective attention on the current task instead of parsing stale
history or unused tool schemas.
- Summarization and sliding-window strategies decouple prompt size
from conversation length, keeping per-turn latency and cost
stable.
- Stable, component-structured prompts with invariant prefixes
compose with prompt caching, turning a large portion of input
tokens into cached reads at a fraction of standard input cost.
- Versioned templates with evaluation gates let prompt changes
ship with quality and cost evidence rather than by guess.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Prompts behave as compositions of discrete components, system
instructions, tool schemas, retrieved knowledge, conversation
history, and the current user turn. Treating them as a single
opaque string makes runaway growth impossible to attribute.
Per-component token attribution on every request demystifies
issues, such as a tool catalog that doubled when a new tool was
registered. Component-level budgets that sum to the workload's
input-length target make the trade-offs explicit: more budget for
retrievals means less for history, and every reallocation becomes
a deliberate decision.

The
[Amazon
Bedrock prompt design guidance](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html) describes how clear
instructions, output indicators, and question placement at the end
of the prompt shape the system-instruction and user-turn
components individually.

The cheapest tokens are the ones never sent. Most agents register
many more tools than any single turn will invoke, so injecting the
full tool catalog on every request spends context budget on
schemas the model ignores.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html) addresses this with semantic
search that returns only the tools relevant to the current user
intent.

Retrieval-augmented context suffers from the same failure mode,
passing raw top-K passages into the prompt without a relevance
threshold or per-passage cap lets low-signal chunks displace
higher-signal context.

Conversation history is the third inflation source: the
[SummaryMemoryStrategy
in Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html#long-term-session-summaries-strategy) maintains a running
per-session summary that replaces raw turns after the session
exceeds a threshold, decoupling prompt size from session length so
per-turn latency remains stable as conversations grow.

Static prefixes unlock large, recurring input-token savings.
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) accepts cache checkpoints in the
system, tools, and
messages fields on the Converse API, with cache
reads charged at a reduced rate on a 5-minute default TTL, or a
1-hour TTL on Claude Opus 4.5, Haiku 4.5, and Sonnet 4.5 for
longer-running or intermittent agent traffic.

Invariant content (system instructions, stable tool definitions,
and pinned context) belongs before the checkpoint, and variable
content (current user turn and session-specific retrievals)
belongs after it so the cached prefix remains identical across
turns. Simplified cache management for Claude models looks back
approximately 20 content blocks for the longest matching prefix,
so the most-reused content should sit within that range.

Prompts behave like code, so a change to wording, component order,
or a tool description can shift quality, token count, and
cache-hit rate simultaneously, while the effects remain invisible
until rollout unless they are measured.
[Amazon
Bedrock Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) stores prompts as versioned
artifacts with variables, inference configuration, and optional
prompt-caching settings, and its console variant comparison
surfaces quality and token differences side by side before
promotion.

[Prompt
Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html) generates model-specific rewrites that serve
as candidate variants rather than drop-in replacements, and
quality plus token-cost benchmarks on representative test sets
should gate promotion of any variant.

### Implementation steps

- **Define the prompt component taxonomy
and per-component token budget:** Decompose every
prompt into a fixed set of components, system instructions,
tool schemas, retrieved knowledge, conversation history, and
the current user turn, and allocate a token budget to each
that sums to the input-length target derived from the
workload's latency and cost SLO. Apply the
[Amazon
Bedrock prompt design guidance](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html) to keep the
system-instruction component clear, concise, and consistent
with the user query placed at the end of the prompt.
- **Instrument per-component token usage
on every request:** Emit token counts for each
component as structured logs or CloudWatch metrics alongside
the inputTokens and
outputTokens returned by the
[Amazon
Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html), dimensioned by agent ID and
task type. Include cacheReadInputTokens
and cacheWriteInputTokens from the
Converse response so cache effectiveness is measured
alongside component growth, and alert when any component
trends outside its budget before it impacts the end-to-end
SLO.
- **Assemble tool schemas dynamically
with just-in-time selection:** Replace full-catalog
injection with task-relevant selection so the prompt carries
only the tools the agent might invoke for the current turn.
For agents using
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html), enable semantic search by
setting
"searchType": "SEMANTIC"
on the mcp protocol in the gateway's
protocolConfiguration so tool retrieval
narrows on user intent. Keep each tool's schema compact with
clear parameter descriptions and required fields to reduce
its per-invocation token weight.
- **Bound conversation history with
summarization and a sliding window:** Cap raw-turn
retention and replace older turns with a running summary
after the session exceeds a threshold expressed in turns or
tokens. Configure the
[SummaryMemoryStrategy
in Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html#long-term-session-summaries-strategy) with a
namespaceTemplates entry such as
/summaries/{actorId}/{sessionId}/ and
inject the summary rather than the raw transcript into the
prompt, paired with a small sliding window of recent turns
to preserve near-term conversational detail.
- **Filter and truncate retrieved
passages before prompt assembly:** Apply a
relevance threshold, a per-passage token cap, and a total
retrieval budget so low-signal chunks can't displace
higher-signal context. Rank passages by relevance score,
drop any below the threshold, and truncate long passages to
the per-passage cap before composing the retrieved-knowledge
component.
- **Structure prompts so they compose
with prompt caching:** Order every prompt so
invariant content (system instructions, stable tool
definitions, pinned reference material) appears before
variant content (user turn, per-request retrievals), then
place
[Amazon
Bedrock prompt cache checkpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) in the
system, tools, and
messages fields at the boundary between
static and dynamic content. For long-running or intermittent
sessions on supported Claude models, set
"ttl": "1h" on the
cachePoint to extend the cache window
beyond the 5-minute default, keeping the 1-hour entry ahead
of any 5-minute entries in the same request.
- **Version prompts and gate changes on
evaluation:** Store prompts as versioned artifacts
in
[Amazon
Bedrock Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) with variables for dynamic
inputs and inference configuration tied to the version, then
use
[Create
version](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-create.html) to snapshot known-good drafts. Use the
side-by-side variant comparison in the prompt builder to
evaluate candidates against each other, and promote a new
version only after it clears quality and token-cost
baselines on a representative test set.
- **Generate model-tuned rewrites with
prompt optimization:** Run candidate prompts
through
[Amazon
Bedrock Prompt Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html) to produce model-specific
rewrites, passing the target model through
targetModelId when using the
OptimizePrompt API. Treat the optimized
output as a candidate variant rather than a drop-in
replacement, and compare it against the original on the same
evaluation set so token-count reductions are weighed against
any quality impact before promotion.

## Resources

**Related best practices:**

- [AGENTPERF03-BP01
Implement tiered memory management systems](agentperf03-bp01.html)
- [AGENTPERF03-BP03
Optimize RAG retrieval pipelines for latency and
precision](agentperf03-bp03.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)
- [AGENTPERF06-BP01
Design optimized tool integration strategies](agentperf06-bp01.html)

**Related documents:**

- [Amazon
Bedrock, Prompt caching for faster model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Amazon
Bedrock, Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html)
- [Amazon
Bedrock, Create a version of a prompt in Prompt
management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-create.html)
- [Amazon
Bedrock, Optimize a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html)
- [Amazon
Bedrock, Design a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html)
- [AgentCore
Gateway, Performance optimization (refined tool schemas and
semantic search)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html)
- [AgentCore
Memory, Long-term built-in strategies (semantic, episodic,
summary, user preference)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp02.html*

---

# AGENTPERF03-BP03 Optimize RAG retrieval pipelines for latency and precision

Retrieval-augmented generation gives agents access to knowledge
beyond the model's training data, but every reasoning iteration that
queries a retrieval pipeline pays its latency and inherits the
quality of its results. A well-tuned RAG pipeline returns
high-relevance passages within a small latency budget. Without this
discipline, retrieval either dominates per-iteration latency or
returns noisy context that degrades reasoning quality.

**Desired outcome:**

- You have a chunking strategy matched to the structure and query
shape of each source corpus, with chunk size and boundaries
tuned against retrieval precision rather than defaulted to a
single fixed size.
- You have retrieval latency tracked per stage (embedding, search,
and re-ranking) with explicit budgets so retrieval can't
silently consume time allocated to reasoning or tool calls.
- You have hybrid retrieval and re-ranking used where the corpus
and query mix justify their added latency, rather than stacked
by default.
- You have query reformulation ahead of every retrieval, so recall
holds when agent phrasing diverges from corpus vocabulary.
- You have retrieval precision and relevance continually evaluated
against a representative query set so quality regressions are
caught before they reach production behavior.

**Common anti-patterns:**

- Using a single fixed chunk size across all document types,
forcing structured content (tables, code, lists) through the
same boundaries as flowing prose and splitting related
information across chunks.
- Passing raw top-K retrieval results to the LLM without
re-ranking or relevance filtering, letting low-signal passages
displace high-signal context in the agent's prompt.
- Embedding the agent's raw query without reformulation, missing
relevant documents that use different terminology than the query
phrasing.
- Running every retrieval through pure dense similarity search
when the corpus contains exact identifiers, code, or numeric
values that keyword search recovers more reliably.
- Choosing an embedding model once and never revisiting it,
missing precision gains from newer models or domain-tuned
alternatives.
- Treating retrieval latency as a single metric rather than
attributing it across embedding, search, and re-ranking stages,
so performance regressions can't be localized.

**Benefits of establishing this best
practice:**

- Stage-level attribution and index tuning keep embedding, search,
and re-ranking within a predictable per-retrieval budget.
- Matching chunking strategy to document structure, hybrid
retrieval where warranted, and re-ranking before context
delivery keeps noise out of the prompt.
- High-precision first retrievals reduce the number of reasoning
iterations that retry retrieval with reformulated queries.
- Continuous evaluation against a representative query set detects
relevance drift before it reaches production.
- Tighter, more relevant retrievals consume less of the context
window, leaving more budget for reasoning.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

At ingest, four decisions fix what any future retrieval can see
before a single query runs: parsing, chunking, embedding, and the
choice of
[vector
store](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html). Query-time stages can filter and reorder what ingest
produced, but they can't recover information ingest discarded.
This asymmetry is the architectural reason RAG pipelines can't be
tuned as a single knob. Errors that are built in at ingest require
re-ingesting the whole corpus to fix. Query-time misconfigurations
can be patched without touching storage. When designers treat RAG
as an unknown, they inherit both sides of that commitment without
seeing where it was made.

Chunking is an ingest-time commitment with no cheap fix.
Fixed-size chunks fragment tables and mix unrelated passages when
topics shift mid-chunk. Hierarchical chunking preserves
nested-document relationships but roughly doubles the index
footprint because parent chunks are indexed alongside their
children. Semantic chunking breaks on meaning rather than token
count and can disagree with domain experts about where a topic
actually shifts.
[Advanced
parsing](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html) recovers figures and tables from PDFs before
chunking runs but adds a foundation-model invocation per document.
Getting any of these wrong isn't a query-time tuning problem,
requiring a full re-embedding of the corpus to fix.

Three query-time stages each convert latency into precision, and
the embedding model used at ingest sets the floor for all three.

- Hybrid retrieval adds BM25 scoring alongside vector
similarity, recovering exact-match queries but doubling
first-stage work.
- Re-ranking runs a second, heavier model over a broad top-k to
earn back prompt tokens, spending milliseconds per passage.
- Query reformulation expands a single query into several,
trading fan-out latency for recall when agent phrasing misses
corpus terminology.

Stacking these stages doesn't give additive precision gains:
rerank over hybrid often matches rerank over dense-only, and
reformulation paired with re-ranking can overlap in what each
fixes. Layering all three yields a precision return that flattens
before the last layer contributes, and a latency cost that
doesn't.

Between one deploy and the next, corpora grow, embedding models
update, re-rankers retrain, and agent query patterns shift. Each
change can move retrieval quality in either direction with no
in-band signal. Drift is only detectable against a representative
query set labeled with expected passages.

Recall@k and nDCG@k quantify whether the right passages were
returned, and the RAG triad (context relevance, answer relevance,
groundedness) extends the measurement to whether retrieved context
actually supported the answer. The eval set is also the joint
between corpus owners, who update documents, and pipeline owners,
who tune stages. Without shared evaluation, teams can ship
regressions that other teams aren't aware of.

### Implementation steps

- **Inventory source corpora and query
patterns:** For each knowledge corpus the agent
will query, record document type (prose, hierarchical
document, PDF with figures, structured tables, code),
typical query shape (conceptual intent vs. exact
identifier), expected query volume, and precision/latency
budget. This inventory drives every downstream choice
(chunking strategy, embedding model, index configuration,
and re-ranker placement). Without it, the pipeline is tuned
by guess against an imagined average.
- **Choose a chunking and parsing
strategy per corpus:** For flowing prose, use
semantic chunking to break on meaning. For nested documents,
use hierarchical chunking to preserve parent-child context.
For PDFs and multimodal content with figures or tables,
enable
[advanced
parsing](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html) via a foundation model or Amazon Bedrock Data
Automation before chunking. Configure the strategy in the
[Knowledge
Base chunking configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html) per data source rather
than defaulting every source to fixed-size chunks.
- **Select an embedding model and
dimensionality:** Pick an embedding model that
covers the modalities, languages, and domain of the corpora
and whose cost and latency fit the per-retrieval budget.
[Amazon
Titan Text Embeddings V2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) exposes configurable output
dimensions so text-corpus index size, recall, and query
latency can be balanced against each other, and
[Amazon
Nova Multimodal Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-amazon-nova-multimodal-embeddings.html) produces a single
embedding space across text, images, video, and audio for
corpora that contain mixed modalities. Re-evaluate the
choice when new models are released, because embedding
quality improvements translate directly into retrieval
precision.
- **Configure the index for the
retrieval pattern:** For corpora with both
conceptual and exact-match queries, enable hybrid search
rather than relying on pure dense similarity. With Amazon
Bedrock Knowledge Bases backed by Amazon OpenSearch Service
Serverless, set
[overrideSearchType: HYBRID](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)
on the Retrieve request to combine vector and raw-text
scoring in a single call. For direct OpenSearch workloads,
configure
[neural
and hybrid search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-neural-search.html) explicitly. Apply metadata filters
on the retrieve request to narrow the search space by
document source, freshness, or scope before vector
similarity runs, and tune
[vector
index parameters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html) against retrieval precision on a
representative query set so the index favors recall or
latency according to the workload's budget.
- **Add re-ranking before context
delivery:** Run first-stage retrieval at a wider
top-K than the prompt context budget allows, then pass the
results through
[Amazon
Bedrock Rerank](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) to produce a higher-precision subset.
The re-ranker compensates for vector-search noise and lets
the LLM receive fewer but higher-relevance passages, which
both tightens prompt quality and reduces input tokens.
Configure the re-ranker on the Knowledge Base retrieve
request rather than orchestrating it client-side so the hop
stays inside the retrieval path.
- **Enable query
reformulation:** Transform agent-generated queries
before they hit the index so retrieval doesn't fail on
terminology mismatches with the source corpus. Knowledge
Bases supports
[query
reformulation and decomposition](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-advanced-parsing-chunking-and-query-reformulation-giving-greater-control-of-accuracy-in-rag-based-applications/) through the Retrieve
API, expanding a broad question into focused sub-queries
executed against the index. Prefer the managed reformulation
path over a bespoke preprocessing step so it stays colocate
with the retrieval hop and benefits from future improvements
to the feature.
- **Instrument per-stage retrieval
latency and relevance:** Emit distinct metrics for
embedding latency, search latency, re-ranker latency, top-k
size, and the relevance score distribution of returned
passages, dimensioned by data source and query class.
Per-stage attribution makes it possible to localize
regressions. A rising re-ranker latency with a stable search
latency points at a different root cause than the reverse.
Set per-stage budgets that sum to the pipeline's end-to-end
latency target so any single stage exceeding its budget
alerts before end-to-end performance is affected.
- **Evaluate the pipeline on a
representative query set on a defined cadence:**
Maintain a fixed evaluation set that spans the corpora and
query shapes in the inventory, and run it against the
pipeline on every significant change (new data source,
chunking change, embedding or re-ranker upgrade, index
parameter tuning), following the approach in
[Evaluate
and improve performance of Amazon Bedrock Knowledge
Bases](https://aws.amazon.com/blogs/machine-learning/evaluate-and-improve-performance-of-amazon-bedrock-knowledge-bases/). Track Recall@k, nDCG@k, and RAG triad scores
per change so quality regressions are caught before rollout,
and refresh the evaluation set as real query patterns drift.

## Resources

**Related best practices:**

- [AGENTPERF03-BP01
Implement tiered memory management systems](agentperf03-bp01.html)
- [AGENTPERF03-BP02
Optimize context window utilization and prompt
management](agentperf03-bp02.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)
- [AGENTPERF03-BP05
Implement agentic retrieval patterns for dynamic, agent-driven
knowledge access](agentperf03-bp05.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases, How content chunking works](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html)
- [Amazon
Bedrock Knowledge Bases, Parsing options for your data
source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html)
- [Amazon
Bedrock Knowledge Bases, Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)
- [Amazon
Bedrock, Improve the relevance of query responses with a
re-ranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html)
- [Amazon
Titan Text Embeddings models](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html)
- [Amazon
Nova Multimodal Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-amazon-nova-multimodal-embeddings.html)
- [Amazon OpenSearch Service, Vector search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html)
- [Amazon OpenSearch Service Serverless, Configure Neural Search and Hybrid
Search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-neural-search.html)
- [Blog:
Amazon Bedrock Knowledge Bases, advanced parsing, chunking,
and query reformulation](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-advanced-parsing-chunking-and-query-reformulation-giving-greater-control-of-accuracy-in-rag-based-applications/)
- [Blog:
Evaluate and improve performance of Amazon Bedrock Knowledge
Bases](https://aws.amazon.com/blogs/machine-learning/evaluate-and-improve-performance-of-amazon-bedrock-knowledge-bases/)
- [Choosing
an AWS vector database for RAG use cases](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html)

**Related videos:**

- [AWS re:Invent 2025 - Advanced agentic RAG Systems: Deep dive with
Amazon Bedrock (AIM425)](https://www.youtube.com/watch?v=bu2cD1pCFTs)

**Related examples:**

- [GitHub:
Amazon Bedrock samples, Knowledge Bases and RAG](https://github.com/aws-samples/amazon-bedrock-samples)

**Related tools:**

- [Amazon
Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp03.html*

---

# AGENTPERF03-BP04 Establish efficient agent caching and data access patterns

Agents that repeatedly fetch the same data benefit from caching,
breaking the cycle of redundant retrievals speeds up every reasoning
iteration. Agentic workloads often access the same tool outputs,
retrieved documents, computed embeddings, and configuration data
across multiple reasoning iterations, sessions, or agents in a
multi-agent workflow. Without caching, each access pays the full
latency and cost of the original operation.

**Desired outcome:**

- You have multi-layer caching that removes redundant computations
and data fetches across reasoning iterations, sessions, and
agents.
- You have cache hit rates monitored and optimized.
- You have cache invalidation policies tuned to balance freshness
requirements with performance benefits.

**Common anti-patterns:**

- Implementing no caching at all, forcing agents to re-fetch the
same documents, re-compute the same embeddings, and re-invoke
the same tools on every reasoning iteration.
- Using a single cache TTL for all data types without considering
freshness requirements, producing either stale data (TTL too
long) or poor hit rates (TTL too short).
- Designing cache keys based only on exact string matching,
missing cache hits for semantically equivalent queries that use
different phrasing.

**Benefits of establishing this best
practice:**

- Cache hits substantially reduce latency for repeated data
access.
- Removing redundant LLM inference calls and external API
invocations lowers cost.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Caching is applied at multiple layers of the agent stack, and each
layer has its own invalidation discipline.

At the LLM inference layer,
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) caches and reuses common prompt
prefixes (like system instructions and tool definitions) across
invocations, reducing both latency and cost for repeated portions
of prompts, prompt caching savings compound further when combined
with Amazon Bedrock's Flex pricing tier for development and
testing workloads.

At the retrieval layer, caching RAG query results under semantic
cache keys (embedding-based similarity) rather than exact string
matching lets semantically similar queries share cached results.

At the tool invocation layer, caching tool outputs based on input
parameters with TTLs matched to the data's freshness requirements,
a cached stock price has a very different TTL than a cached
company description.

Cache warming is valuable where access patterns are predictable.
If agents frequently access the same knowledge base sections
during business hours, pre-warming the cache before peak periods
avoids the first-miss penalty for early users. Data access
patterns benefit from batching: retrieving multiple items in a
single round trip rather than making sequential individual
requests reduces both latency and connection overhead.

Monitoring cache hit rates, latency savings, and cost savings per
cache layer in Amazon CloudWatch makes caching a tunable
parameter.

### Implementation steps

- **Identify cacheable data across the
agent stack:** Enumerate LLM prompt prefixes, RAG
results, tool outputs, session state, and configuration
data, each has its own access pattern, freshness
requirement, and cache layer.
- **Enable Amazon Bedrock prompt caching
for common prompt prefixes shared across
invocations:** Turn on
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) and structure prompts so
system instructions and tool definitions appear before
variable content, letting the cached prefix be reused across
requests.
- **Implement retrieval result caching
with semantic cache keys and data-type-specific
TTLs:** Cache RAG results under embedding-based
similarity keys so semantically equivalent queries share
results, and tune TTLs to the freshness needs of each data
type rather than applying a single global TTL.
- **Implement tool output caching with
TTLs calibrated to data freshness requirements:**
Cache tool outputs under input-parameter keys with TTLs that
match how fast each tool's data changes, short TTLs for
real-time data, long TTLs for static reference data.
- **Monitor cache hit rates and latency
savings per cache layer using CloudWatch:** Publish
hit rate, miss rate, and latency savings per cache layer as
CloudWatch metrics so TTLs and warming strategies can be
tuned from data rather than assumption.

## Resources

**Related best practices:**

- [AGENTPERF03-BP01
Implement tiered memory management systems](agentperf03-bp01.html)
- [AGENTPERF03-BP03
Optimize RAG retrieval pipelines for latency and
precision](agentperf03-bp03.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)

**Related documents:**

- [Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Blog:
Effectively use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/)
- [Blog:
Optimize LLM response costs and latency with effective
caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp04.html*

---

# AGENTPERF03-BP05 Implement agentic retrieval patterns for dynamic, agent-driven knowledge access

Complex questions often require information from multiple sources,
iterative refinement, or real-time data that a single retrieval pass
can't provide. In agentic retrieval the agent actively controls the
retrieval process as part of its reasoning loop, deciding when to
retrieve, what to retrieve, which retrieval tool to use, and whether
the retrieved context is sufficient before proceeding. Each
iteration adds embedding generation, vector search, re-ranking, and
context injection overhead, so the retrieval loop needs explicit
termination conditions.

**Desired outcome:**

- You have agents retrieving the right information in the minimum
number of iterations required.
- You have simple questions answered with a single retrieval and
complex questions handled through structured multi-hop retrieval
with explicit termination conditions.
- You have the agent selecting the most appropriate retrieval tool
for each query type.
- You have retrieval iteration counts, per-iteration latency, and
sufficiency rates tracked and optimized.

**Common anti-patterns:**

- Treating all retrieval as a single-shot preprocessing step,
forcing the agent to work with whatever context was retrieved on
the first attempt regardless of sufficiency.
- Allowing agents to retrieve iteratively without retrieval
budgets or termination conditions, producing unbounded retrieval
loops that consume tokens and latency without converging.
- Routing all retrieval through a single pipeline regardless of
query type, missing opportunities to use faster or more
appropriate retrieval tools for different information needs.

**Benefits of establishing this best
practice:**

- Parallel sub-query execution and retrieval-tool routing reduce
end-to-end latency by selecting the fastest appropriate source.
- Explicit budgets that cap iterations and total tokens keep
retrieval costs under control.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design retrieval as a set of agent tools rather than a monolithic
pipeline. Distinct retrieval tools for different knowledge access
patterns let the agent route to the right source:

- A semantic search tool backed by
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for conceptual questions
- A structured query tool for exact lookups by identifier
- A real-time data tool for information requiring current values
- A web search tool for questions beyond the organization's
knowledge base
- A document processing tool backed by
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) for extracting structured data
from images, forms, and tables

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) exposes retrieval tools as
MCP-compatible endpoints, and registering each tool with clear
descriptions, what question types it handles, what data sources it
accesses, and its expected latency guides the agent's tool
selection.

Retrieval sufficiency evaluation is a lightweight assessment after
each retrieval iteration, typically run by a smaller, faster
model. The evaluator judges whether the retrieved context is
sufficient, identifies gaps, and formulates refined queries. A
maximum retrieval iteration limit (typically 2-3 iterations) helps
prevent unbounded loops. If the agent has not retrieved sufficient
context within the budget, it proceeds with the best available
context and communicates uncertainty.

For complex questions requiring multiple sources, query
decomposition breaks the question into focused sub-queries and
runs independent sub-queries concurrently. Per-task retrieval
performance budgets, derived from the task's overall latency SLO,
keep the iterative pattern inside the workload's target.

### Implementation steps

- **Implement distinct retrieval tools
for different knowledge access patterns:** Register
a semantic search tool, a structured-query tool, a real-time
data tool, a web search tool, and a document processing tool
through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with clear descriptions
that guide the agent's tool selection.
- **Implement retrieval sufficiency
evaluation as a lightweight post-retrieval
assessment:** Use a small, fast model to judge
whether retrieved context is sufficient, identify gaps, and
formulate refined queries for the next iteration.
- **Configure maximum retrieval
iteration limits with graceful fallback to best-available
context:** Cap iterations at 2-3 for most tasks,
and when the budget is exhausted proceed with the best
context obtained and communicate uncertainty rather than
looping without bounds.
- **Implement query decomposition for
complex questions, running independent sub-queries
concurrently:** Break multi-source questions into
focused sub-queries and fan them out in parallel so
sub-query latency doesn't accumulate serially.
- **Define per-task retrieval
performance budgets based on the overall latency
SLO:** Allocate an explicit portion of the task's
latency SLO to retrieval so the iterative pattern can't
silently consume the budget reserved for inference or
downstream tool calls.

## Resources

**Related best practices:**

- [AGENTPERF03-BP03
Optimize RAG retrieval pipelines for latency and
precision](agentperf03-bp03.html)
- [AGENTPERF03-BP02
Optimize context window utilization and prompt
management](agentperf03-bp02.html)
- [AGENTPERF02-BP01
Design efficient reasoning pipelines](agentperf02-bp01.html)
- [AGENTREL05-BP03
Ground agent cognition in real information](agentrel05-bp03.html)
- [AGENTCOST03-BP02
Cost optimize through intelligent compression and pruning of
context windows](agentcost03-bp02.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Blog:
Building intelligent search with Amazon Bedrock and Amazon OpenSearch Service for hybrid RAG solutions](https://aws.amazon.com/blogs/machine-learning/building-intelligent-search-with-amazon-bedrock-and-amazon-opensearch-for-hybrid-rag-solutions/)

**Related examples:**

- [GitHub:
Advanced RAG using Bedrock and SageMaker AI](https://github.com/aws-samples/sample-advanced-rag-using-bedrock-and-sagemaker)

**Related services:**

- [Amazon
Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
- [Amazon
Bedrock AgentCore Gateway](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp05.html*

---

# AGENTPERF04 — Communication and protocol efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# AGENTPERF04-BP01 Optimize asynchronous message handling patterns

Asynchronous messaging lets agents operate independently at their
optimal pace, with message queues absorbing throughput variations
and leveling load across the workflow. Synchronous request-response
patterns create tight coupling that makes a slow downstream agent
block the entire upstream chain. Async decouples producers from
consumers so fast agents are not held up by slow ones.

**Desired outcome:**

- You have agent-to-agent and agent-to-service communications
using asynchronous patterns by default, with synchronous
communication reserved for interactions that genuinely require
immediate responses.
- You have compact message payloads that pass references rather
than inline data.
- You have agents processing messages at their own pace without
being overwhelmed by upstream producers.

**Common anti-patterns:**

- Using synchronous HTTP request-response for all agent
communications, creating tight coupling where a slow downstream
agent blocks the entire upstream chain.
- Including large payloads (like full documents or base64-encoded
files) in messages rather than passing references (like S3 URIs
or document IDs) and letting the consumer retrieve the data when
needed.
- Skipping backpressure mechanisms, allowing fast-producing agents
to overwhelm slow-consuming agents with messages that queue up
and eventually cause timeouts.

**Benefits of establishing this best
practice:**

- Decoupled agent execution helps prevent slow agents from
blocking fast agents.
- Each agent scales independently based on its own queue depth and
processing rate.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For agents deployed on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), the runtime's built-in session
management handles message passing and state management for
agent-to-agent communication inside a workflow. For workflows that
need custom messaging patterns or cross-system integration,
[Amazon SQS](https://aws.amazon.com/sqs/)
provides reliable point-to-point messaging and
[Amazon SNS](https://aws.amazon.com/sns/)
provides fan-out where a single agent event triggers multiple
downstream agents. Message payloads should stay compact: pass S3
URIs, DynamoDB keys, or document IDs rather than inline data, and
let the consumer retrieve the bytes on demand.

Dead letter queues (DLQs) capture messages that fail processing
after retries, so failure analysis doesn't block the main flow.
When consumer queues exceed depth thresholds, producers should be
throttled or consumers scaled. Amazon CloudWatch alarms on queue
depth are the signal that triggers either response. For
high-volume workflows, SQS batch size and long polling let you
balance latency and throughput, long polling reduces empty
receives, and larger batch sizes amortize request overhead across
more messages.

### Implementation steps

- **Use AgentCore Runtime session
management for agent-to-agent communication where possible,
and use SQS or SNS for custom messaging patterns:**
Let the runtime handle message passing and state inside a
workflow, and fall back to Amazon SQS or Amazon SNS only for
custom patterns or cross-system integration.
- **Design compact message payloads
using references rather than inline data:** Pass S3
URIs, DynamoDB keys, or document IDs in messages and let the
consumer retrieve the full payload on demand.
- **Implement dead letter queues for
failed message processing with alerting on DLQ
depth:** Route messages that fail after retries to
a DLQ and alert when DLQ depth grows, so failure analysis
happens off the main path.
- **Add backpressure mechanisms that
throttle producers when consumer queues exceed depth
thresholds:** Use Amazon CloudWatch alarms on queue
depth to trigger producer throttling or consumer scaling
before queues reach timeout-triggering depths.
- **Configure long polling and batch
sizes for SQS consumers based on latency and throughput
requirements:** Tune long polling and batch size on
SQS consumers to balance empty-receive cost, per-message
latency, and throughput.

## Resources

**Related best practices:**

- [AGENTPERF04-BP02
Implement efficient protocol-based agent communications](agentperf04-bp02.html)
- [AGENTPERF04-BP03 Design
performant event-driven integration patterns](agentperf04-bp03.html)
- [AGENTPERF05-BP01
Design efficient workflow orchestration patterns](agentperf05-bp01.html)

**Related documents:**

- [Building
serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)

**Related services:**

- [Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon SQS](https://aws.amazon.com/sqs/)
- [Amazon SNS](https://aws.amazon.com/sns/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf04-bp01.html*

---

# AGENTPERF04-BP02 Implement efficient protocol-based agent communications

Standardized protocols such as the Model Context Protocol (MCP) and
agent-to-agent (A2A) give agents a consistent way to communicate
with tools and each other, reducing per-interaction overhead and
enabling interoperability. Different protocols have different
performance profiles, connection establishment, serialization,
streaming, multiplexing, which makes protocol selection a meaningful
performance decision for high-frequency agent communication.

**Desired outcome:**

- You use MCP for tool integration, A2A for agent-to-agent
coordination, and streaming protocols for real-time agent-user
interactions.
- You have protocol overhead minimized through connection reuse
and efficient serialization.
- You have documented protocol selection guidelines for the
organization.

**Common anti-patterns:**

- Using HTTP or REST APIs with JSON serialization for all agent
communications regardless of interaction pattern, paying
connection establishment and verbose serialization overhead for
high-frequency internal communications.
- Implementing custom communication protocols instead of adopting
standards like MCP and A2A, creating maintenance burden and
blocking interoperability with the broader agent ecosystem.
- Establishing new connections for every agent interaction rather
than pooling and reusing them, adding unnecessary handshake
latency.

**Benefits of establishing this best
practice:**

- Protocol-appropriate connection management reduces
per-interaction overhead.
- Standard protocols open interoperability with the broader agent
ecosystem.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Adopt MCP as the standard protocol for agent-to-tool
communication.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) exposes tools as MCP-compatible
endpoints that agents discover and invoke through a consistent
interface. For agent-to-agent communication, the A2A protocol
supported by AgentCore Runtime provides structured inter-agent
coordination with agent card discovery, task delegation, and
result collection. Frameworks such as Strands Agents and LangGraph
provide MCP and A2A support.

For real-time agent-user interactions that need streaming,
WebSocket connections through
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) keep a persistent channel open rather than
reestablishing connections per turn. Connection pooling belongs on
every protocol path, and protocol-level compression pays off once
payloads exceed a few kilobytes.

Authentication overhead is part of the protocol performance
profile. In complex multi-agent workflows, token validation,
credential issuance, and policy evaluation accumulate into a
measurable latency contributor. AgentCore Identity provides agent
authentication with token caching, and AWS IAM roles for
service-to-service authentication remove explicit credential
exchange from the critical path.

### Implementation steps

- **Adopt MCP for agent-to-tool
communications through AgentCore Gateway:** Expose
tools as MCP-compatible endpoints through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) so agents discover and
invoke tools through a consistent interface.
- **Use A2A protocol through AgentCore
Runtime for agent-to-agent coordination:** Use the
A2A protocol supported by AgentCore Runtime for
agent-to-agent coordination, with agent card discovery, task
delegation, and result collection.
- **Implement WebSocket connections
through API Gateway for real-time streaming agent-user
interactions:** Use WebSocket connections through
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) for real-time streaming so the channel
stays open rather than reestablishing on each turn.
- **Enable connection pooling and
protocol-level compression for all
communications:** Pool connections on every
protocol path and enable compression once payloads exceed a
few kilobytes.
- **Budget for authentication overhead
and implement token caching through AgentCore
Identity:** Use AgentCore Identity with token
caching for agent authentication, and use AWS IAM roles for
service-to-service calls so credential exchange isn't on the
critical path.

## Resources

**Related best practices:**

- [AGENTPERF04-BP01
Optimize asynchronous message handling patterns](agentperf04-bp01.html)
- [AGENTPERF06-BP01
Design optimized tool integration strategies](agentperf06-bp01.html)
- [AGENTPERF05-BP02
Implement optimized multi-agent collaboration models](agentperf05-bp02.html)

**Related documents:**

- [Agentic
AI frameworks, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html)
- [Blog:
Open Protocols for Agent Interoperability Part 1: Inter-Agent
Communication on MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp)
- [Blog:
Open Protocols for Agent Interoperability Part 4: Inter-Agent
Communication on A2A](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)

**Related videos:**

- [AgentCore
Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8)
- [Building
Scalable, Self-Orchestrating AI Workflows with A2A and MCP
(DEV415)](https://www.youtube.com/watch?v=9O9zZ1lQWiI)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf04-bp02.html*

---

# AGENTPERF04-BP03 Design high-performing event-driven integration patterns

Agents that react to events in real time, data changes, user
actions, and system alerts deliver faster business outcomes than
agents that poll for work. Overly broad event subscriptions trigger
agents for irrelevant events, missing filtering causes agents to
process and discard events they don't need. Inefficient routing adds
delays that push response time past user expectations.

**Desired outcome:**

- You have agent workflows triggered by precisely filtered events
that match their processing requirements, with minimal latency
between event emission and agent invocation.
- You have efficient event schemas that include only routing
metadata, with agents retrieving full context on demand.
- You have event-driven patterns that support both real-time and
batch processing modes.

**Common anti-patterns:**

- Subscribing agents to broad event streams without filtering,
forcing agents to receive and process events they immediately
discard and wasting compute resources.
- Using polling-based event detection instead of push-based event
delivery, adding latency and consuming compute during idle
periods.
- Including full data payloads in events rather than event
references, inflating event size and network transfer time when
most consumers only need a subset.

**Benefits of establishing this best
practice:**

- Push-based delivery reduces latency between event occurrence and
agent invocation.
- Filtering at the event bus reduces compute waste by invoking
agents only for relevant events.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use [Amazon EventBridge](https://aws.amazon.com/eventbridge/) as the primary event bus for agent workflow
triggers, with content-based filtering rules that route events to
specific agents based on event attributes. For high-throughput
streams,
[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) with Lambda event source mappings
supports batch processing without forcing agents into per-event
invocation. Event payloads should carry metadata, identifiers, and
routing information, the full data belongs in
[Amazon S3](https://aws.amazon.com/s3/) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/), with references in the event. EventBridge Schema
Registry standardizes event formats across the organization so
consumers can generate code bindings from the schema rather than
parsing one-time JSON.

For agents that need to react to database changes,
[Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) triggers agents directly from data changes
without polling. Event deduplication using idempotency keys helps
prevent agents from processing the same event twice, relevant
whenever at-least-once delivery is the default. For complex event
processing that requires correlation of multiple events before
triggering an agent,
[AWS Step Functions](https://aws.amazon.com/step-functions/) or
[EventBridge
Pipes](https://aws.amazon.com/eventbridge/pipes/) aggregate and transform events before agent
invocation.

### Implementation steps

- **Configure EventBridge rules with
content-based filtering to route events to specific
agents:** Use content-based filtering on
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) so agents receive only the events whose
attributes match their responsibilities.
- **Design minimal event schemas with
references rather than full payloads, registered in
EventBridge Schema Registry:** Keep event payloads
to routing metadata and identifiers, store full data in S3
or DynamoDB, and register schemas in EventBridge Schema
Registry so consumers can generate bindings.
- **Implement DynamoDB Streams for
data-change-driven agent triggers:** Use
[Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) to trigger agents directly from data
changes without polling.
- **Implement idempotency keys for event
deduplication in agent processing logic:** Apply
idempotency keys so agents don't process the same event
twice under at-least-once delivery.
- **Monitor event processing metrics:
event-to-invocation latency, filter efficiency, and
throughput:** Publish these metrics to CloudWatch
so filtering and routing can be tuned from measured
behavior.

## Resources

**Related best practices:**

- [AGENTPERF04-BP01
Optimize asynchronous message handling patterns](agentperf04-bp01.html)
- [AGENTPERF05-BP01
Design efficient workflow orchestration patterns](agentperf05-bp01.html)
- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)

**Related documents:**

- [Building
serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html)
- [Blog:
Effectively building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/)

**Related services:**

- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf04-bp03.html*

---

# AGENTPERF05 — Workflow orchestration and multi-agent collaboration

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# AGENTPERF05-BP01 Design efficient workflow orchestration patterns

Agents that coordinate specialized sub-agents can solve complex
tasks faster than any single agent, and the orchestration pattern
you choose determines whether that coordination adds milliseconds or
seconds. Orchestration patterns range from static workflows (the
execution graph is fully defined at design time) to dynamic
workflows (the agent's reasoning determines the next step at
runtime). Efficient orchestration means decomposing tasks for
parallelism, minimizing data passed between steps, and matching the
orchestration pattern to the task's dependency structure.

**Desired outcome:**

- You have multi-agent workflows that execute with minimal
orchestration overhead, with independent subtasks running in
parallel and dependent tasks executing as soon as prerequisites
complete.
- You have task routing decisions that are fast and accurate.
- You have end-to-end workflow latency that approaches the
theoretical minimum defined by the critical path of dependent
operations.

**Common anti-patterns:**

- Running all workflow steps sequentially even when some steps
have no data dependencies and could run in parallel, making
end-to-end latency equal to the sum of all step durations rather
than the critical path.
- Using the orchestrator agent as a pass-through for all data
between worker agents, creating a serialization bottleneck at
every step instead of having workers write results directly to
shared storage.
- Implementing dynamic graph orchestration without cycle detection
or maximum depth limits, allowing LLM-driven routing decisions
to produce infinite loops where agents repeatedly invoke each
other without converging.

**Benefits of establishing this best
practice:**

- Parallel execution of independent subtasks reduces end-to-end
latency.
- Managed orchestration with built-in retry and error handling
improves reliability.
- Scalable orchestration handles dynamic fan-out patterns without
code changes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Most agentic workflows are dynamic, meaning that the LLM's
reasoning determines which tool or sub-agent to invoke next based
on intermediate results. For these workflows, use your agentic
framework's built-in orchestration capabilities:

- Strands Agents provides graph-based orchestration
(GraphBuilder), supervisor patterns, and swarm coordination
- LangGraph offers stateful graph workflows
- CrewAI provides role-based crew orchestration

These framework-driven patterns are the natural fit for agent
workloads because the execution path emerges from the model's
reasoning rather than being predefined. To keep dynamic
orchestration high-performing, implement cycle detection (track
visited nodes with input hashing), maximum depth limits (10–15
steps), and bounded fan-out cardinality (5–10 concurrent branches)
to help prevent unbounded execution chains.

For deterministic workflows where the run graph is fully known at
design time, batch processing pipelines, approval workflows, data
transformation chains, use
[AWS Step Functions](https://aws.amazon.com/step-functions/) with Parallel and Map states to run steps
concurrently, Choice states for conditional branching, and
built-in Catch and Retry for error handling. Step Functions is
also valuable as a hybrid layer that handles durable orchestration
and state persistence while invoking LLM-based agents only at
decision points that require reasoning.

Keep state payloads small by storing large intermediate results in
[Amazon S3](https://aws.amazon.com/s3/) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and passing only references through the
orchestration layer.

For all orchestration patterns, configure per-step and
workflow-level timeouts that help prevent slow agents from
blocking the entire workflow. For dynamic graph workflows,
allocate per-branch latency budgets derived from the overall task
SLO, if a branch exceeds its budget, terminate it and proceed with
the best available partial result. Design workflows to maximize
parallelism by analyzing task dependencies and executing
independent subtasks concurrently.

Monitor workflow execution metrics including step duration,
parallel efficiency, state payload sizes, and graph depth
distribution.

### Implementation steps

- **Analyze multi-agent task
dependencies and classify each workflow:** Classify
each workflow as dynamic graph (LLM-driven routing, most
agent workflows), hybrid (deterministic flow with LLM
decision points), or static (fully predefined execution
graph), and use the classification to drive the
orchestration choice.
- **For dynamic graph workflows, use
your agentic framework's native orchestration:**
Use Strands GraphBuilder, LangGraph, or equivalent with
cycle detection, maximum depth limits, and bounded fan-out
cardinality to help prevent unbounded execution chains.
- **For static/hybrid workflows,
implement using Step Functions with Parallel and Map
states:** Use
[AWS Step Functions](https://aws.amazon.com/step-functions/) Parallel and Map states to run steps
concurrently with built-in retry and error handling on
deterministic paths.
- **Implement efficient state passing
using S3/DynamoDB references rather than inline
payloads:** Keep orchestration payloads small by
storing large intermediate results in S3 or DynamoDB and
passing only references.
- **Configure per-step and
workflow-level timeouts with fallback strategies for slow
agents:** Set timeouts at both the step and
workflow level, and define fallback behavior so a single
slow agent can't stall the whole workflow.
- **Monitor workflow execution metrics:
step duration, parallel efficiency, state payload sizes, and
graph depth distribution:** Publish these metrics
to CloudWatch so orchestration performance can be tuned from
data rather than assumption.

## Resources

**Related best practices:**

- [AGENTPERF05-BP02
Implement optimized multi-agent collaboration models](agentperf05-bp02.html)
- [AGENTPERF05-BP03
Optimize multi-stage AI pipeline execution](agentperf05-bp03.html)
- [AGENTPERF02-BP01
Design efficient reasoning pipelines](agentperf02-bp01.html)

**Related documents:**

- [Blog:
Customize agent workflows with advanced orchestration
techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/)
- [Agentic
AI patterns and workflows on AWS, Workflow orchestration
agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html)
- [Building
serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html)
- [Blog:
Effectively building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/)

**Related videos:**

- [Architecting
scalable and secure agentic AI with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc)
- [Build
Your First Agent Workflow with Strands](https://www.youtube.com/watch?v=oGzEKQVhKQU)
- [Build
Reliable AI Agents with LangGraph](https://www.youtube.com/watch?v=E0BtW2yt2pA)

**Related examples:**

- [GitHub:
Guidance for multi-agent orchestration using Bedrock
AgentCore](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-using-bedrock-agentcore-on-aws)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05-bp01.html*

---

# AGENTPERF05-BP02 Implement optimized multi-agent collaboration models

Multi-agent systems typically deliver the strongest results when
each collaboration pattern is matched to the task it was designed
for (for example, supervisor-worker for structured decomposition,
swarm for creative exploration, and pipeline for sequential
processing). Before picking any multi-agent pattern, decide whether
a capability should be a sub-agent or a tool that a single agent
invokes. A tool call completes in milliseconds, while a sub-agent
delegation is a full LLM reasoning loop that costs time and tokens.

**Desired outcome:**

- You have multi-agent workflows that use collaboration models
matched to their task characteristics.
- You have each capability implemented at the right abstraction
level, tool for deterministic single-step operations, sub-agent
for tasks that require independent reasoning.
- You have coordination overhead minimized through appropriate
pattern selection and implementation.

**Common anti-patterns:**

- Delegating to a sub-agent for capabilities that are
deterministic, stateless, and single-step, API calls, database
lookups, or format conversions, paying the full cost of an LLM
reasoning loop for work that a tool call would handle in
milliseconds.
- Using a supervisor-worker model for all multi-agent workflows,
creating a bottleneck at the supervisor that must process every
intermediate result and make every delegation decision.
- Deploying swarm patterns without explicit convergence criteria
or resource budgets, letting agents continue exploring
indefinitely without converging on a shared outcome.

**Benefits of establishing this best
practice:**

- Matching the collaboration model to task structure minimizes
coordination overhead.
- Appropriate model selection for decomposable tasks maximizes
parallelism.
- Timeouts and fallback mechanisms keep collaboration resilient
when individual agents fail or slow down.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use a sub-agent when the capability requires its own reasoning
(LLM inference for ambiguous inputs or judgment calls), its own
context or memory scope, multi-step tool orchestration where
sequencing requires reasoning, a different model or prompt, or
independent failure isolation.

Use a tool when the capability is deterministic, stateless,
single-step, and fast (under 2-3 seconds).

For borderline cases, start with a tool and promote to a sub-agent
only when frequent re-invocation patterns indicate the capability
needs its own reasoning loop.

Once multi-agent architecture is warranted, select the
collaboration model based on task characteristics. Use
supervisor-worker when the task has clear decomposition and
centralized quality control is needed. Strands Agents's
agent-as-tool pattern and Amazon Bedrock Agents' multi-agent
collaboration provide supervisor-worker orchestration with
automatic context passing and result aggregation.

Use pipeline when the task has a natural sequential flow, balance
stage durations and use your framework's graph orchestration to
chain agents sequentially.

Use peer-to-peer or blackboard when multiple agents need to
contribute partial solutions asynchronously, implement a shared
workspace using AgentCore Memory or DynamoDB with event-driven
notifications.

Use swarm when the task benefits from parallel exploration and
emergent behavior, implement convergence detection and per-swarm
token budgets to help prevent unbounded resource consumption.

For deterministic delegation logic or durable long-running
workflows,
[AWS Step Functions](https://aws.amazon.com/step-functions/) remains a strong alternative for orchestrating
agent invocations.

For all collaboration models, implement timeout and fallback
mechanisms that help prevent a single slow or failed agent from
blocking the entire workflow. Deploy multi-agent systems on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for managed scaling and
observability, or on Amazon EKS or Amazon ECS for custom
container-based deployments. Monitor collaboration overhead
metrics including coordination latency, redundant work rate, and
throughput per model.

### Implementation steps

- **Evaluate whether each capability
should be a tool or a sub-agent:** Default to tools
and promote to sub-agents only when re-invocation patterns
indicate the need for independent reasoning.
- **Classify multi-agent workflows by
task characteristics:** Assess decomposability,
dependency structure, latency requirements, and whether the
task benefits from parallel exploration.
- **Select the collaboration
model:** Use supervisor-worker for clear
decomposition, pipeline for sequential flow, peer-to-peer
for shared problem spaces, and swarm for parallel
exploration.
- **Implement using your framework's
native multi-agent patterns:** Use Strands
agent-as-tool, Amazon Bedrock multi-agent collaboration, or
an equivalent, and use
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for shared context across
agents.
- **Implement timeout and fallback
mechanisms for all collaboration models:** Set
per-agent timeouts and define fallback behavior so one slow
or failed agent can't block the full workflow.
- **Monitor collaboration overhead
metrics and optimize model selection over time:**
Track coordination latency, redundant work rate, and
throughput per model, and re-evaluate the collaboration
choice as traffic shifts.

## Resources

**Related best practices:**

- [AGENTPERF05-BP01 Design
efficient workflow orchestration patterns](agentperf05-bp01.html)
- [AGENTPERF05-BP04
Implement efficient agent delegation and handoff
patterns](agentperf05-bp04.html)
- [AGENTPERF04-BP02
Implement efficient protocol-based agent communications](agentperf04-bp02.html)

**Related documents:**

- [Blog:
Multi-agent collaboration patterns with Strands Agents and
Amazon Nova](https://aws.amazon.com/blogs/machine-learning/multi-agent-collaboration-patterns-with-strands-agents-and-amazon-nova/)
- [Blog:
Multi-agent collaboration with Strands](https://aws.amazon.com/blogs/devops/multi-agent-collaboration-with-strands/)
- [Agentic
AI patterns and workflows on AWS, Multi-agent
collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html)
- [Agentic
AI patterns and workflows on AWS, Workflow orchestration
agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html)
- [Use
multi-agent collaboration with Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html)

**Related videos:**

- [Amazon
Bedrock Agents and AgentCore Design Patterns (TNC322)](https://www.youtube.com/watch?v=GYlPFmrATjU)

**Related examples:**

- [GitHub:
Bedrock multi-agent collaboration workshop](https://github.com/aws-samples/bedrock-multi-agents-collaboration-workshop)
- [GitHub:
Multi-agent collaboration with Strands](https://github.com/aws-samples/sample-multi-agent-collaboration-with-strands)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock Agents](https://aws.amazon.com/bedrock/agents/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05-bp02.html*

---

# AGENTPERF05-BP03 Optimize multi-stage AI pipeline execution

Real-world agent tasks rarely complete in a single step. Document
processing, data analysis, and customer service workflows all
involve multiple sequential stages where each stage's throughput is
limited by the slowest process or mechanism. Each stage transition
introduces overhead (like serialization, network transfer, or cold
starts), and streaming or micro-batching allows downstream stages to
begin processing before upstream stages complete, overlapping
execution to cut total latency.

**Desired outcome:**

- You have multi-stage AI pipelines that execute with minimal
inter-stage overhead, with data flowing efficiently between
stages.
- You have pipeline throughput balanced across stages with no
single stage creating a persistent bottleneck.
- You have streaming implemented where possible to overlap
processing.
- You have each stage's compute resources right-sized for its
specific requirements.

**Common anti-patterns:**

- Waiting for an entire batch to complete one stage before
starting the next, when streaming or micro-batching would let
downstream stages begin processing as upstream results become
available.
- Using the same compute configuration for all pipeline stages
regardless of their processing requirements, over-provisioning
lightweight stages and under-provisioning compute-intensive
stages.
- Serializing large intermediate results to persistent storage
between every stage when in-memory passing or streaming would be
more efficient for stages that execute in close succession.

**Benefits of establishing this best
practice:**

- Streaming and micro-batching overlap stage processing, reducing
end-to-end latency.
- Balanced stage capacity and buffered inter-stage communication
improve throughput.
- Right-sized compute per stage optimizes cost.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement multi-stage pipelines using
[AWS Step Functions](https://aws.amazon.com/step-functions/) with stage-specific
[AWS Lambda](https://aws.amazon.com/lambda/) functions,
[Amazon ECS](https://aws.amazon.com/ecs/)
tasks, or agents hosted on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), where each stage's compute
configuration is independently tuned. For pipelines with high
throughput requirements, Step Functions Distributed Map processes
items in parallel across stages. Right-size compute for each
stage, using Lambda for lightweight processing, ECS for
compute-intensive stages, and AgentCore Runtime for stages that
require LLM-based reasoning.

Streaming between stages is the single largest latency win when it
applies. Use Amazon Bedrock's streaming inference API to begin
post-processing output tokens as they are generated rather than
waiting for the complete response. For data-intensive pipelines,
[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) acts as an inter-stage buffer that
supports streaming data flow, so downstream stages begin
processing as soon as upstream results are available. For batch
pipelines, micro-batching sends small groups of items to
downstream stages as they complete rather than waiting for the
entire batch.

Pipeline-level observability through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) or
[AWS X-Ray](https://aws.amazon.com/xray/)
traces requests across all stages, identifying the critical path
and the stage that contributes most to end-to-end latency. Balance
stage durations by profiling each stage and adjusting processing
granularity, split slow stages into parallel sub-stages or combine
fast stages to reduce inter-stage transitions.

### Implementation steps

- **Map the multi-stage pipeline and
identify dependencies between stages:** Document
stage dependencies, opportunities for streaming, and the
critical path so optimization effort lands on the stages
that drive end-to-end latency.
- **Implement each stage as an
independent compute unit with stage-specific resource
configurations:** Use
[AWS Lambda](https://aws.amazon.com/lambda/) for lightweight processing,
[Amazon ECS](https://aws.amazon.com/ecs/) for compute-intensive stages, and AgentCore
Runtime for stages that require LLM reasoning, and tune each
stage's resources to its own profile.
- **Enable streaming between stages
using the Amazon Bedrock streaming API and Kinesis Data
Streams where applicable:** Use the streaming
inference API to post-process output tokens as they are
generated, and
[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) as an inter-stage buffer so
downstream stages begin processing as upstream results
arrive.
- **Implement micro-batching for batch
pipelines to reduce end-to-end latency:** Send
small groups of items to downstream stages as they complete
rather than waiting for the full batch.
- **Configure AgentCore Observability or
X-Ray tracing across all pipeline stages for end-to-end
latency visibility:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) or
[AWS X-Ray](https://aws.amazon.com/xray/) to trace requests across every stage.
- **Monitor per-stage latency,
throughput, and resource utilization to identify and resolve
bottlenecks:** Publish metrics for each stage so
bottleneck stages are visible and can be split,
parallelized, or resized.

## Resources

**Related best practices:**

- [AGENTPERF05-BP01 Design
efficient workflow orchestration patterns](agentperf05-bp01.html)
- [AGENTPERF02-BP04
Optimize streaming responses and time-to-first-token for agent
interactions](agentperf02-bp04.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)

**Related documents:**

- [Multi-stage
AI workflow pattern, Building serverless architectures for
agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/pattern-multi-stage-ai.html)
- [Blog:
Effectively building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)

**Related examples:**

- [GitHub:
Build GenAI agent workflows with Step Functions](https://github.com/aws-samples/build-genai-agent-workflows-with-step-functions)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05-bp03.html*

---

# AGENTPERF05-BP04 Implement efficient agent delegation and handoff patterns

Smooth agent-to-agent transitions make multi-agent workflows feel
like a single cohesive experience, where the receiving agent picks
up exactly where the delegating agent left off. Delegation and
handoff both require efficient context transfer. The receiving agent
needs enough context to act, but transferring too much wastes time
and tokens.

**Desired outcome:**

- You have agent delegation and handoff operations that complete
with minimal latency, transferring precisely the context needed
by the receiving agent.
- You have receiving agents that begin productive processing
immediately without re-deriving context the delegating agent
already possessed.
- You have standardized context transfer mechanisms that let any
agent delegate to or receive handoffs from any other agent.
- You have handoff latency measured and optimized as part of the
overall workflow performance budget.

**Common anti-patterns:**

- Transferring the entire conversation history and all accumulated
context during every delegation, regardless of what the
receiving agent actually needs, wasting serialization time and
context window capacity.
- Requiring receiving agents to re-derive context (re-query
databases, re-retrieve documents) that the delegating agent
already had, duplicating work and adding latency.
- Implementing delegation as synchronous blocking calls where the
parent agent waits idle for the child agent to complete, wasting
the parent's compute resources.

**Benefits of establishing this best
practice:**

- Selective context transfer and shared context stores reduce
delegation latency.
- Receiving agents reuse context already gathered by delegating
agents instead of repeating the work.
- Asynchronous delegation patterns improve parent agent
throughput.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement a shared context store using
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) where delegating agents write context and
receiving agents read it, avoiding the need to serialize and
transfer large context payloads through the orchestration layer.
Context transfer schemas define the minimum context required for
each delegation type, a data validation agent needs the data and
validation rules, not the full conversation history. For agents
built with Strands Agents, the built-in agent-as-tool pattern
automatically inherits relevant context from the parent agent's
session.

For handoff patterns in conversational agents, context
summarization compresses the conversation into a concise handoff
summary tailored to the receiving agent's role, rather than
transferring raw conversation history. For predictable delegation
patterns, for example, a triage agent that consistently delegates
to one of several specialist agents, pre-warming through
[AWS Lambda](https://aws.amazon.com/lambda/) provisioned concurrency or warm session pools on
AgentCore Runtime removes cold-start latency from the receiving
side. Asynchronous delegation lets the parent agent continue
processing other tasks while the child agent works, using
callbacks or
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) notifications to receive results.

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) standardizes delegation
interfaces, letting any agent delegate to any other agent through
a consistent API that handles context transfer, authentication,
and result delivery. Handoff latency belongs in agent performance
dashboards as a distinct metric, measured from delegation
initiation to the receiving agent's first productive action.

### Implementation steps

- **Identify delegation and handoff
patterns in existing multi-agent workflows and measure
current transition latency:** Map delegation and
handoff points and measure the current transition latency so
optimization targets are grounded in data.
- **Implement shared context stores
using AgentCore Memory or DynamoDB for context transfer
between agents:** Use
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) so delegating agents write context once and
receiving agents read it without serializing large payloads.
- **Define minimum context schemas for
each delegation type, specifying exactly what the receiving
agent needs:** Keep the delegation payload small
and purpose-specific so receivers only get the context
required for their role.
- **Implement context summarization for
conversational handoffs that compresses history into
role-appropriate summaries:** Summarize raw
conversation history into a handoff summary tailored to the
receiving agent's role rather than forwarding the full
transcript.
- **Configure pre-warming for
predictable delegation patterns using provisioned
concurrency or warm session pools:** For recurring
delegation targets, use
[AWS Lambda](https://aws.amazon.com/lambda/) provisioned concurrency or warm session pools
on AgentCore Runtime to remove cold-start latency.
- **Convert synchronous delegations to
asynchronous patterns with callback-based result
delivery:** Let the parent agent continue other
work while the child agent runs, receiving results through
callbacks or EventBridge notifications.

## Resources

**Related best practices:**

- [AGENTPERF05-BP01 Design
efficient workflow orchestration patterns](agentperf05-bp01.html)
- [AGENTPERF05-BP02
Implement optimized multi-agent collaboration models](agentperf05-bp02.html)
- [AGENTPERF04-BP01
Optimize asynchronous message handling patterns](agentperf04-bp01.html)

**Related documents:**

- [Blog:
Multi-agent collaboration patterns with Strands Agents and
Amazon Nova](https://aws.amazon.com/blogs/machine-learning/multi-agent-collaboration-patterns-with-strands-agents-and-amazon-nova/)
- [Agentic
AI patterns and workflows on AWS, Multi-agent
collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html)
- [Operationalizing
agentic AI on AWS, Design for composability and
collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)

**Related videos:**

- [AgentCore
Memory: Episodic Memory & Patterns](https://www.youtube.com/watch?v=1EEIGsKIjGA)

**Related examples:**

- [GitHub:
Guidance for multi-agent orchestration using Bedrock
AgentCore](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-using-bedrock-agentcore-on-aws)
- [GitHub:
Amazon Bedrock AgentCore samples, Memory tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05-bp04.html*

---

# AGENTPERF06 — Tool integration and framework optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# AGENTPERF06-BP01 Design optimized tool integration strategies

Agents that surface the right tools at the right time respond faster
and make better decisions. LLMs make increasingly poor tool
selection decisions once the candidate set grows beyond 10-15 tools,
so dynamic filtering, parallel execution, and cached results keep
the reasoning loop tight even as the tool catalog grows. Tool
invocations happen inside the reasoning loop, which means their
latency adds directly to response time.

**Desired outcome:**

- You have tool invocations that add minimal latency to the agent
reasoning loop.
- You have tool selection that is fast and accurate, with agents
choosing from a filtered set of 5-10 relevant options rather
than evaluating the full catalog.
- You have independent tool calls executing in parallel.
- You have tool results cached where appropriate.
- You have per-tool latency, error rate, and usage metrics
providing visibility into tool performance.

**Common anti-patterns:**

- Presenting all available tools to the agent on every reasoning
iteration, forcing the LLM to evaluate dozens of tool
descriptions, consuming context window capacity and degrading
selection accuracy.
- Executing tool calls sequentially when they have no data
dependencies, adding latency equal to the sum of all tool
durations rather than the maximum.
- Skipping tool result caching, so agents re-invoke the same tool
with identical parameters multiple times within a single task.

**Benefits of establishing this best
practice:**

- Parallel tool execution and result caching reduce reasoning loop
latency.
- Dynamic filtering that presents only relevant tools improves
tool selection accuracy.
- Per-tool monitoring speeds detection of tool performance issues.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Adopt MCP as the standard tool integration protocol and use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) to expose tools as MCP-compatible
endpoints. AgentCore Gateway provides built-in semantic tool
discovery (x_amz_bedrock_agentcore_search) so
agents query for relevant tools by natural language description
rather than receiving the full catalog. For agents with access to
large tool catalogs, a two-stage selection pattern works well: a
lightweight pre-filter narrows the full catalog to the 5-10 most
relevant tools based on current task context, and only those
filtered tools appear in the LLM's prompt. For agents built with
Strands Agents or another agentic framework, built-in parallel
tool execution runs independent tool calls concurrently.

Design tool APIs specifically for agent consumption, like compact
response schemas that return only the fields the agent needs,
pagination for large result sets, and partial response support.
Cache tool results at multiple levels, request-scoped (within a
single reasoning session), session-scoped (across reasoning
iterations for the same user), and global (shared data with
appropriate TTLs). Tool health monitoring tracks per-tool latency,
error rates, and availability, and automatic cutoffs route around
slow or failing tools.

### Implementation steps

- **Adopt MCP as the standard tool
integration protocol and expose tools through AgentCore
Gateway:** Expose tools as MCP-compatible endpoints
through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) so agents use a single
consistent interface.
- **Enable AgentCore Gateway's semantic
tool discovery to filter tools by task relevance:**
Use x_amz_bedrock_agentcore_search to
narrow the tool set per request so the LLM evaluates only
the most relevant 5-10 tools.
- **Implement parallel tool execution
for independent tool calls within the same reasoning
step:** Use your framework's native parallel tool
execution (Strands Agents, LangGraph) so independent tool
calls run concurrently.
- **Deploy multi-level tool result
caching with appropriate TTLs per tool:** Cache
tool results at request-, session-, and global-scope with
TTLs matched to each tool's freshness requirements.
- **Configure tool health monitoring
with per-tool latency and error rate metrics, and automatic
cutoffs for degraded tools:** Track per-tool
latency and error rate in Amazon CloudWatch and use
automatic cutoffs to route around degraded tools.

## Resources

**Related best practices:**

- [AGENTPERF06-BP02
Implement efficient tool invocation patterns](agentperf06-bp02.html)
- [AGENTPERF06-BP03
Optimize meta-tool utilization and tool chaining](agentperf06-bp03.html)
- [AGENTPERF04-BP02
Implement efficient protocol-based agent communications](agentperf04-bp02.html)

**Related documents:**

- [Blog:
Introducing Amazon Bedrock AgentCore Gateway: Transforming
enterprise AI agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [Blog:
Transform your MCP architecture: Unite MCP servers through
AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/transform-your-mcp-architecture-unite-mcp-servers-through-agentcore-gateway/)
- [Blog:
Open Protocols for Agent Interoperability Part 3: Strands
Agents & MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-3-strands-agents-mcp/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [Agentic
AI frameworks, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html)

**Related videos:**

- [Scale
agent tools with AgentCore Gateway (AIM3313)](https://www.youtube.com/watch?v=DlIHB8i6uyE)
- [Integrating
MCP Tools with Strands Agents](https://www.youtube.com/watch?v=bHSbjCZZFjE)
- [Strands
Tools: Building Custom AI Agents with Python](https://www.youtube.com/watch?v=EGhIZCfOvG4)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore, Lab 3: Gateway,
Identity & Policy](https://catalog.workshops.aws/agentcore-getting-started/en-US/50-add-tool-gateway)
- [Diving
Deep into Bedrock AgentCore, Gateway](https://catalog.workshops.aws/agentcore-deep-dive/en-US/30-agentcore-gateway)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf06-bp01.html*

---

# AGENTPERF06-BP02 Implement efficient tool invocation patterns

Well-tuned tool invocation patterns help the agent's responsiveness
reflect the tool's actual processing time, not infrastructure
overhead. Each tool invocation involves connection establishment,
serialization, network transfer, processing, and deserialization,
trimming each component compounds across the many tool calls in a
typical agent task.

**Desired outcome:**

- You have individual tool invocations that execute with minimal
overhead beyond the tool's inherent processing time.
- You have connection pooling that removes repeated connection
establishment costs.
- You have timeouts that help prevent slow tools from blocking
agent execution.
- You have automatic cutoffs that detect degraded tools and route
to alternatives.
- You have per-tool invocation metrics that provide visibility
into performance characteristics.

**Common anti-patterns:**

- Establishing new connections for every tool invocation rather
than maintaining connection pools, adding hundreds of
milliseconds of TLS handshake latency to each call.
- Implementing aggressive retry strategies without backoff or
jitter, creating retry storms that overwhelm already-degraded
tools.
- Setting tool invocation timeouts too high or not at all, letting
a single slow tool call block the agent for seconds and exceed
the overall task latency budget.

**Benefits of establishing this best
practice:**

- Connection pooling and persistent connections reduce
per-tool-call overhead.
- Appropriate timeouts protect the agent latency budget.
- Automatic cutoffs support fast failover to alternatives.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

For tools accessed through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), the gateway handles connection
management, authentication, and routing automatically. For custom
tool endpoints, connection pooling through HTTP keep-alive
connections or framework-specific pool configurations keeps TLS
sessions warm across invocations.

For [AWS Lambda](https://aws.amazon.com/lambda/)-based tools, initializing connections outside the
handler function so they persist across invocations within the
same execution environment turns a handshake for each request into
one per environment. Tool invocation timeouts should be set based
on the tool's expected response time, typically two to three times
the p95 latency.

Retry strategies with exponential backoff and jitter handle
transient failures, with a maximum of two to three retries and a
total retry budget that doesn't exceed the tool's timeout.
Automatic cutoff patterns track tool failure rates and open the
circuit when failures exceed a threshold, returning a cached
result or error immediately rather than waiting for another
timeout.

For tools that support batch operations, request batching (a batch
API for multiple item lookups) reduces overhead for each call
across the set. Per-tool invocation metrics (latency percentiles,
error rates, timeout rates, and automatic cutoff state) belong on
the agent performance dashboard alongside reasoning-loop metrics.

### Implementation steps

- **Use AgentCore Gateway for managed
tool access where possible, and implement connection pooling
for custom tool endpoints:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) for managed tool access.
For custom endpoints, enable HTTP keep-alive and
framework-level connection pools.
- **Configure per-tool timeouts based on
profiled p95 latency:** Size each tool's timeout to
two to three times its measured p95 latency so slow
individual calls don't stall the agent.
- **Implement retry strategies with
exponential backoff and jitter:** Use exponential
backoff with jitter and cap retries at two to three so
transient failures recover without overwhelming
already-degraded tools.
- **Deploy automatic cutoff patterns
that fast-fail when tools are degraded:** Track
failure rate per tool and open the circuit when failures
exceed a threshold, returning a cached result or error
immediately.
- **Implement request batching for tools
that support batch operations:** Use batch APIs
when multiple items are needed so per-call overhead
amortizes across the set.
- **Monitor per-tool invocation metrics
and establish alerting for latency and error rate
anomalies:** Publish per-tool latency percentiles,
error rates, timeout rates, and cutoff state to CloudWatch
with alarms on anomalies.

## Resources

**Related best practices:**

- [AGENTPERF06-BP01 Design
optimized tool integration strategies](agentperf06-bp01.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)

**Related documents:**

- [Blog:
Build long-running MCP servers on Amazon Bedrock AgentCore
with Strands Agents integration](https://aws.amazon.com/blogs/machine-learning/build-long-running-mcp-servers-on-amazon-bedrock-agentcore-with-strands-agents-integration/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Agentic
AI frameworks, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf06-bp02.html*

---

# AGENTPERF06-BP03 Optimize meta-tool utilization and tool chaining

Meta-tools let agents accomplish in one reasoning step what would
otherwise take five. For tasks that require a predictable sequence
of tool calls, a meta-tool combines the entire sequence into a
single server-side operation and returns the final result in one
reasoning iteration instead of many, cutting both latency and token
cost by removing intermediate reasoning steps.

**Desired outcome:**

- You have common multi-step tool sequences encapsulated as
meta-tools that execute the full sequence in a single agent
reasoning iteration.
- You have agents using meta-tools for routine operations and
individual tools for novel or unpredictable tasks.
- You have meta-tool performance monitored to validate that the
composite operation is faster than the equivalent sequence of
individual tool calls.

**Common anti-patterns:**

- Requiring the agent to make individual tool calls for every step
of a predictable sequence (for example, search, retrieve, parse,
and format), consuming multiple reasoning iterations for what
could be a single meta-tool invocation.
- Creating overly complex meta-tools that try to handle too many
variations, becoming hard to maintain and slower than individual
tools for edge cases.
- Skipping meta-tools for frequently repeated tool sequences,
forcing agents to re-discover and re-execute the same tool chain
on every occurrence.

**Benefits of establishing this best
practice:**

- Meta-tools that collapse multi-step sequences into single
invocations reduce LLM inference calls.
- Removing intermediate reasoning iterations lowers latency and
token cost.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Analyze agent telemetry to identify frequently repeated tool call
sequences, patterns where agents consistently call the same tools
in the same order with predictable data flow between them.
Implement these sequences as meta-tools using
[AWS Lambda](https://aws.amazon.com/lambda/) functions that execute the entire sequence
server-side and return the final result.

For example, a "research" meta-tool might combine
knowledge base search, document retrieval, and relevance
extraction into a single invocation.

Expose meta-tools through MCP through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) alongside individual tools, so
agents can choose between the meta-tool for routine operations and
individual tools for novel tasks that require step-by-step
reasoning.

Design meta-tools with clear input and output contracts and error
handling that provides meaningful feedback when any step in the
sequence fails. Update agent prompts to include meta-tool
descriptions that guide the agent to prefer them for routine
operations.

Monitor meta-tool performance to validate that the composite
operation is faster than the equivalent individual tool sequence,
and decompose meta-tool latency into per-step metrics so
optimization is directed at the slowest step.

### Implementation steps

- **Analyze agent telemetry to identify
frequently repeated tool call sequences:** Look for
sequences that occur three or more times with predictable
data flow between steps.
- **Design meta-tools for the most
common sequences with clear input/output contracts and error
handling:** Define explicit contracts and per-step
error handling so meta-tool failures are attributable.
- **Implement meta-tools as Lambda
functions that execute the full sequence
server-side:** Use
[AWS Lambda](https://aws.amazon.com/lambda/) to run the sequence server-side so the agent
sees one call instead of many.
- **Expose meta-tools through MCP and
AgentCore Gateway alongside individual tools:**
Register meta-tools with
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) alongside individual tools
so the agent can choose based on task.
- **Monitor meta-tool performance and
compare against equivalent individual tool
sequences:** Track meta-tool latency and per-step
breakdown and compare against the individual-tool path to
confirm the meta-tool is actually faster.

## Resources

**Related best practices:**

- [AGENTPERF06-BP01 Design
optimized tool integration strategies](agentperf06-bp01.html)
- [AGENTPERF06-BP02
Implement efficient tool invocation patterns](agentperf06-bp02.html)
- [AGENTPERF05-BP03
Optimize multi-stage AI pipeline execution](agentperf05-bp03.html)

**Related documents:**

- [Blog:
Flexibility to Framework: Building MCP Servers with Controlled
Tool Orchestration](https://aws.amazon.com/blogs/devops/flexibility-to-framework-building-mcp-servers-with-controlled-tool-orchestration/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Agentic
AI frameworks, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html)

**Related videos:**

- [AgentCore
Deep Dive: Browser Tool & Code Interpreter](https://www.youtube.com/watch?v=z3lAJ-Nf_lk)
- [Excel-lent
Agents: AgentCore's Code Interpreter](https://www.youtube.com/watch?v=THUX2ycix3Y)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf06-bp03.html*

---

# AGENTPERF07 — Multi-tenancy and resource optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# AGENTPERF07-BP01 Design efficient multitenant agent deployment models

Organizations that serve multiple tenants from a shared agent
service get better resource efficiency and faster tenant onboarding
when the deployment model delivers consistent performance for every
tenant. Siloed deployments provide strong isolation at higher cost.
Pooled deployments maximize efficiency but need mechanisms to help
prevent noisy neighbor effects. Hybrid models combine both, using
pooled resources for standard tenants and dedicated resources for
premium tenants.

**Desired outcome:**

- You have multitenant agent deployments that use deployment
models matched to tenant requirements.
- You have deployment models documented with clear performance
characteristics and SLA commitments for each tier.
- You have a deployment model that supports efficient tenant
onboarding through configuration rather than infrastructure
provisioning.

**Common anti-patterns:**

- Deploying fully siloed infrastructure for every tenant
regardless of their performance requirements, creating resource
waste for tenants that would be well-served by pooled resources.
- Using a single pooled deployment without isolation mechanisms,
allowing high-volume tenants to consume disproportionate
resources and degrade performance for others.
- Skipping tenant tiers with different performance SLAs, treating
all tenants identically regardless of business value.

**Benefits of establishing this best
practice:**

- Resource investment stays proportional to tenant value and
performance requirements.
- Appropriate isolation mechanisms deliver consistent performance
for every tenant.
- Configuration-driven provisioning speeds tenant onboarding.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Define tenant tiers based on performance requirements and business
value:

- A standard tier using pooled resources with best-effort
performance
- A premium tier using dedicated resources with stronger SLA
targets
- (Optional) An enterprise tier with fully isolated
infrastructure

For pooled deployments,
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides session-isolated
execution that naturally helps prevent cross-tenant interference
at the agent execution level. For tenants that need custom
container environments, deploy on
[Amazon EKS](https://aws.amazon.com/eks/)
or [Amazon ECS](https://aws.amazon.com/ecs/) with namespace-level or task-level isolation. For
simpler tenant needs such as team-specific chat assistants or
enterprise Q&A,
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/) provides a managed no-code option where business
users create and deploy agents without custom infrastructure.

Tenant-aware routing at the API layer uses
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) with usage plans that enforce per-tenant rate
limits and throttling. At the inference layer, Amazon Bedrock's
provisioned throughput gives premium tenants reserved capacity
while standard tenants use on-demand capacity. Tenant context
propagates through the agent stack so every component (runtime,
memory, tools) applies tenant-specific configurations. For data
isolation, use
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with tenant partition keys for pooled access, or
separate tables for siloed tenants. Tenant onboarding automated
through [AWS CDK](https://aws.amazon.com/cdk/) or CloudFormation makes new standard tenants a
configuration change rather than an infrastructure provisioning
project.

### Implementation steps

- **Define tenant tiers with specific
performance SLAs, isolation requirements, and
pricing:** Define standard, premium, and optional
enterprise tiers with explicit SLAs and isolation
expectations.
- **Design the deployment architecture
for each tier:** Architect pooled (shared AgentCore
Runtime, on-demand Amazon Bedrock), premium (dedicated
resources, provisioned throughput), and enterprise (fully
isolated) deployments.
- **Implement tenant-aware routing using
API Gateway with per-tenant usage plans and rate
limits:** Use
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) usage plans with per-tenant rate and
burst limits.
- **Configure data isolation using
DynamoDB tenant partition keys (pooled) or separate tables
(siloed):** Enforce data isolation at the data
layer with partition keys or separate tables as appropriate
for the tier.
- **Automate tenant onboarding for each
tier using CDK/CloudFormation templates:** Template
onboarding so new tenants are provisioned through
configuration rather than manual infrastructure work.
- **Monitor per-tenant performance
metrics to validate SLA compliance:** Publish
per-tenant metrics to CloudWatch and alert when observed
performance drifts outside SLA.

## Resources

**Related best practices:**

- [AGENTPERF07-BP02
Implement tenant-aware performance isolation and
throttling](agentperf07-bp02.html)
- [AGENTPERF02-BP01
Design efficient reasoning pipelines](agentperf02-bp01.html)

**Related documents:**

- [Building
multi-tenant architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/introduction.html)
- [Enforcing
tenant isolation, Multi-tenant agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.html)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)

**Related videos:**

- [Building
multi-tenant SaaS agents with AgentCore (SAS407)](https://www.youtube.com/watch?v=uwXrtyXXuy8)
- [Transforming
from SaaS to multi-tenant agentic SaaS (SAS304)](https://www.youtube.com/watch?v=YOQlbZojPB4)
- [Deploy
Production-Ready Agents in 22 Minutes with AgentCore
Runtime](https://www.youtube.com/watch?v=Q-tYIAuv9WI)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon EKS](https://aws.amazon.com/eks/)
- [AWS CDK](https://aws.amazon.com/cdk/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf07-bp01.html*

---

# AGENTPERF07-BP02 Implement tenant-aware performance isolation and throttling

Trust in a shared agent service is built through consistent,
predictable performance for every tenant, even during demand spikes.
In pooled multitenant deployments, effective isolation requires
throttling at multiple layers (API, inference, memory, and tools),
monitoring per-tenant resource consumption, and adaptive fairness
mechanisms that distribute shared resources equitably based on
current load.

**Desired outcome:**

- You have per-tenant throttling enforced at every shared resource
layer.
- You have tenant resource consumption monitored in real time with
alerts for tenants approaching their limits.
- You have graceful throttling that provides clear feedback to
throttled tenants.
- You have performance isolation validated through regular load
testing that simulates noisy neighbor scenarios.

**Common anti-patterns:**

- Applying throttling only at the API gateway layer without
enforcing limits at downstream shared resources, letting tenants
bypass API-level limits through long-running operations.
- Using static throttling limits that don't adapt to current
system load, wasting available capacity during low-load periods
or failing to protect isolation during high-load periods.
- Throttling all tenants equally regardless of their service tier,
failing to honor premium SLAs.

**Benefits of establishing this best
practice:**

- Multi-layer throttling distributes shared resources fairly
across tenants.
- Real-time per-tenant consumption metrics support proactive
management.
- Per-tenant performance monitoring validates SLA compliance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Multi-layer throttling enforces tenant limits at every shared
resource. At the API layer,
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) usage plans with per-tenant API keys enforce
request rate and burst limits. At the inference layer,
tenant-aware request queuing caps concurrent
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) inference calls per tenant. At the memory and tool
layers, per-tenant rate limiting applies to shared endpoints. For
agents deployed on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), the runtime's session isolation
provides natural per-session resource boundaries.

Adaptive throttling adjusts limits based on current system load:
during low-load periods, tenants can burst above their baseline
limits to use available capacity, and during high-load periods,
strict limits protect isolation. Per-tenant
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboards and metrics track request volume,
inference consumption, latency percentiles, throttle rates, and
error rates. Alarms fire when a tenant approaches their limits or
when per-tenant latency exceeds SLA thresholds. Regular noisy
neighbor testing, simulating high-load scenarios for individual
tenants, validates that other tenants' performance stays within
SLA bounds.

### Implementation steps

- **Define per-tenant throttling limits
for each resource layer:** Set per-tenant limits
for API requests per second, concurrent inference calls,
memory storage quota, and tool invocations per minute.
- **Implement API Gateway usage plans
with per-tenant API keys and rate/burst limits:**
Use
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) usage plans with per-tenant API keys to
enforce rate and burst limits at ingress.
- **Deploy tenant-aware inference
queuing with per-tenant concurrency limits:** Queue
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) inference calls per tenant so no single
tenant can consume all inference capacity.
- **Configure adaptive throttling that
adjusts limits based on current system load:**
Allow bursts during low-load periods and enforce strict
limits during high-load periods to protect isolation.
- **Create per-tenant CloudWatch
dashboards and configure SLA-based alarms:**
Publish per-tenant metrics in
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and alarm on consumption approaching
limits or latency exceeding SLA thresholds.
- **Establish regular noisy neighbor
load testing to validate isolation effectiveness:**
Schedule noisy neighbor load tests that simulate high-load
scenarios for individual tenants and verify others stay
within SLA.

## Resources

**Related best practices:**

- [AGENTPERF07-BP01 Design
efficient multi-tenant agent deployment models](agentperf07-bp01.html)
- [AGENTPERF04-BP02
Implement efficient protocol-based agent communications](agentperf04-bp02.html)
- [AGENTSUS01-BP04
Scale cognitive processing pathways appropriately](agentsus01-bp04.html)

**Related documents:**

- [Building
multi-tenant architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/introduction.html)
- [Enforcing
tenant isolation, Multi-tenant agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.html)

**Related videos:**

- [Building
multi-tenant SaaS agents with AgentCore (SAS407)](https://www.youtube.com/watch?v=uwXrtyXXuy8)

**Related services:**

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf07-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
