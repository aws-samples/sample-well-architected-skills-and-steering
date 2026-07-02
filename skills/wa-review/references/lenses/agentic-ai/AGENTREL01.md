# AGENTREL01 — Predictable agent behavior

**Pillar**: Reliability  
**Best Practices**: 5

---

# AGENTREL01-BP01 Implement a resilient messaging layer

Direct agent-to-agent calls couple failure modes. When one agent
fails, everything downstream fails with it. A messaging layer with
persistence, retry, and dead-letter handling absorbs transient
faults and lets workflows resume from where they stopped.

**Desired outcome:**

- Your agents communicate through an intermediary messaging layer
with persistence, retry, and dead-letter handling rather than
direct synchronous calls.
- You have durable workflow state that survives the restart or
loss of any single component.
- You can trace every agent message across synchronous and
asynchronous boundaries.

**Common anti-patterns:**

- Wiring agents together through direct synchronous calls, so a
single failure cascades through every dependent agent.
- Running messaging infrastructure without persistence, making
workflow recovery impossible after a component outage.
- Treating every interaction as synchronous, creating bottlenecks
that block independent agent operation.

**Benefits of establishing this best
practice:**

- Persistence and retry contain transient failures within the
messaging layer instead of exposing them as agent outages.
- Dead-letter handling helps prevent poison messages from blocking
healthy workflow execution.
- A durable messaging substrate is the foundation for advanced
orchestration patterns including saga and arbiter.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Every agent-to-agent call is a coupling decision. Synchronous
calls tie the caller's availability to the callee's availability.
In a network of agents that multiplies quickly. Five agents with
four synchronous dependencies, and the availability product drops
below any single agent's SLA. A messaging layer breaks the
coupling by buffering the call in durable infrastructure. The
caller emits a message and moves on. The receiver processes it on
its own schedule, with retries and dead-letter routing handled
outside the agent's own code.

Pattern selection follows the interaction shape. Use
[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) for content-based routing where a single event
fans out to multiple consumers, with EventBridge Schema Registry
documenting the contract between agents. Use
[Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) for durable point-to-point delivery with configurable
visibility timeouts and dead-letter queues. Use Amazon SNS for
fan-out to multiple downstream consumers.

Workflow durability ties the messaging layer to business outcomes.
A message that reaches its queue still needs orchestration to
coordinate multi-step work across agents.
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) persists execution state at every step
transition, so recovery starts from the last completed step rather
than the beginning. Without that persistence, a failure in step
five of a seven-step workflow re-executes every prior step,
wasting compute and risking duplicate side effects. Dead-letter
handling complements durability. Poison messages get isolated for
triage rather than blocking healthy traffic behind them.

### Implementation steps

- **Map every agent communication path
and classify it:** Document each interaction as
synchronous direct communication (A2A), loosely coupled tool
invocation (MCP), or asynchronous event-driven through
[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).
- **Configure EventBridge rules and SQS
queues:** Set up Amazon EventBridge content-based
routing for event-driven paths and
[Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) queues for durable point-to-point messaging.
- **Define event schemas in EventBridge
Schema Registry:** Register a schema for each agent
message type so sender and receiver agree on the contract.
- **Configure dead-letter queues with
automated triage:** Route repeatedly failed
messages to DLQs and wire Amazon CloudWatch alarms so
operators see poison messages before they block traffic.
- **Instrument the messaging layer with
AgentCore Observability:** Enable
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) for distributed
tracing so you can follow a message across EventBridge, SQS,
and agent boundaries.

## Resources

**Related best practices:**

- [AGENTREL01-BP02
Establish modular, fault-isolated layers](agentrel01-bp02.html)
- [AGENTREL01-BP03 Design
specialized agents following actor model principles](agentrel01-bp03.html)
- [AGENTREL01-BP04
Standardize communication protocols](agentrel01-bp04.html)

**Related documents:**

- [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)

**Related services:**

- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon SQS](https://aws.amazon.com/sqs/)
- [Amazon SNS](https://aws.amazon.com/sns/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel01-bp01.html*

---

# AGENTREL01-BP02 Establish modular, fault-isolated layers

Monolithic agent architectures force every fault to become a
full-system fault. Splitting compute, memory, reasoning, and
orchestration into independently scalable layers with fail-fast
boundaries keeps the scope of impact small. Teams keep serving
requests at reduced capability instead of going unavailable.

**Desired outcome:**

- Your agent stack is split into distinct layers (compute, memory,
reasoning, orchestration, and tool integration) with documented
API contracts at each boundary.
- You have fail-fast behavior on inter-layer calls, with defined
fallback modes for each degraded state.
- You can toggle non-critical capabilities at runtime without
redeploying.

**Common anti-patterns:**

- Deploying monolithic agents where a failure in any component
forces a full restart for issues that should be isolated.
- Running without automatic cutoffs, allowing latency or error
rates in one component to propagate through every dependent
call.
- Treating all capabilities as equally critical, missing the
chance to keep core functionality available when non-essential
components fail.

**Benefits of establishing this best
practice:**

- Teams can develop, test, and deploy individual layers
independently without blocking on the rest of the stack.
- Fault isolation narrows troubleshooting to the layer that
actually failed rather than the whole system.
- Graceful degradation keeps agents responsive even when
individual layers are unavailable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AgentCore Runtime organizes capabilities into distinct layers
(Runtime, Memory, Gateway, and Identity), each addressable
independently. Design your agents to treat these as separate
failure domains. If Memory becomes unavailable, your agent's
routing logic (Gateway) and authentication (Identity) should
continue functioning. Implement health checks per layer and
configure independent timeout and retry policies for each, rather
than treating AgentCore as a monolithic dependency.

When a downstream layer's error rate climbs, the caller should
stop waiting for timeouts and activate a fallback. Examples
include session-only context instead of long-term memory, an
alternative Amazon Bedrock model instead of the primary, or a
cached answer instead of fresh retrieval. Without fail-fast, every
degraded call consumes thread budget and propagates latency back
to the user. The
[AWS fail-fast pattern guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html) covers the mechanics.

Runtime capability toggling keeps the scope of impact small during
an incident. If one tool is flaky, turn that tool off and keep the
rest of the agent operational rather than taking the whole agent
down. Publish structured health status per layer through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so downstream components
adapt to the toggle state automatically. Service maps give
operators the view they need to correlate layer health to
user-visible symptoms.

### Implementation steps

- **Decompose the architecture into
layers with documented contracts:** Split the agent
into distinct layers for compute, memory, cognition,
orchestration, and tool integration. Publish the API
contract at every boundary.
- **Deploy each layer independently on
AgentCore Runtime:** Run each layer on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with no shared execution
resources between layers.
- **Implement fail-fast logic per
inter-layer call:** For each call boundary, define
the error-rate threshold that trips the cutoff and the
fallback behavior that takes over.
- **Publish structured layer health
through AgentCore Observability:** Emit per-layer
health signals through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so downstream
components can adapt and operators can trace degradation to
its source.
- **Wire runtime capability
toggling:** Build a control plane that disables
non-critical capabilities without redeployment so operators
can contain incidents as they happen.

## Resources

**Related best practices:**

- [AGENTREL01-BP01
Implement a resilient messaging layer](agentrel01-bp01.html)
- [AGENTREL01-BP03 Design
specialized agents following actor model principles](agentrel01-bp03.html)
- [AGENTREL08-BP01
Establish consistent configuration management practices](agentrel08-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [AWS fail-fast pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html)

**Related videos:**

- [AWS re:Invent 2024 - Architecting scalable and secure agentic AI
with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc)
- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel01-bp02.html*

---

# AGENTREL01-BP03 Design specialized agents following actor model principles

Multi-purpose agents concentrate risk. A single failure in one
function affects every other function in the same process.
Specialized agents that encapsulate one atomic capability, own their
state, and communicate through messages keep the impact proportional
to the scope of the failing component.

**Desired outcome:**

- You have each agent scoped to a single atomic function with
explicit input and output schemas.
- Your agents maintain their own state and exchange information
through explicit message passing, not shared memory.
- You can scale, replace, or upgrade any one agent without
disturbing the others.

**Common anti-patterns:**

- Building multi-purpose agents that combine disparate functions
in one component, reducing the ability for independent scaling
and widening the failure impact.
- Coupling agents through shared in-memory state rather than
explicit message passing, so a crash in one process corrupts
another.
- Designing agents as general-purpose processors with overlapping
capabilities, making issue reproduction and remediation harder
than it needs to be.

**Benefits of establishing this best
practice:**

- A failure stays contained to the agent that encountered it,
preserving overall workflow integrity.
- Single-responsibility agents are simpler to test
deterministically because the input-output contract is small.
- Each agent scales, deploys, and is replaced on its own schedule,
which keeps the rest of the system stable during change.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The actor model is a discipline, not a runtime feature. A managed
runtime can give you isolated execution.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) runs each agent in its own
microVM with dedicated tool permissions. But whether your agents
actually follow actor principles depends on how you scope the
system prompt, how narrowly you define the tool set, and whether
inter-agent calls go through messages or shared state.

Give each agent a single, well-scoped system prompt that
constrains it to one domain. Use Strands Agents or another agentic
framework, but the test is framework-independent. Can you describe
the agent's job in a single sentence without using
"and"? If not, the agent carries more than one
responsibility and should be split.

Communication pattern follows interaction shape. Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) to expose agents as discoverable
MCP tools when the caller treats the specialized agent as a
capability it invokes on demand. Use the
[Agent-to-Agent
(A2A) protocol](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html) when agents need peer collaboration with
streaming responses or multi-turn exchanges. Monitor each agent
individually. Track task success rate, processing latency, and
error rate through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so one agent's issues don't
hide under aggregate fleet metrics.

### Implementation steps

- **Decompose the workflow into
specialized agents:** Define each agent around a
single atomic function with explicit input and output
schemas.
- **Deploy each agent on AgentCore
Runtime with a dedicated IAM role:** Run each agent
on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with an execution role
scoped to only the resources required for that agent's
function.
- **Choose the inter-agent communication
pattern:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) for loosely coupled
tool-style invocation, or the
[A2A
protocol](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html) for peer-to-peer collaboration with richer
interaction patterns.
- **Monitor each agent
independently:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with per-agent
metrics and alarms so one agent's issues are not masked by
fleet-level aggregates.

## Resources

**Related best practices:**

- [AGENTREL01-BP01
Implement a resilient messaging layer](agentrel01-bp01.html)
- [AGENTREL01-BP02
Establish modular, fault-isolated layers](agentrel01-bp02.html)
- [AGENTREL01-BP04
Standardize communication protocols](agentrel01-bp04.html)
- [AGENTSUS01-BP01
Design specialized agents with explicit resource
boundaries](agentsus01-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Deploy
A2A servers in AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a.html)
- [Introducing
Amazon Bedrock AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel01-bp03.html*

---

# AGENTREL01-BP04 Standardize communication protocols

Custom message formats between every agent pair turn new
integrations into one-off engineering projects. Standardized
schemas, versioned endpoints, and a canonical error format let
agents compose into workflows without a translation layer at every
boundary.

**Desired outcome:**

- You have a canonical message schema, error format, and retry
policy that every agent follows.
- You version endpoints and maintain backward compatibility so
existing integrations keep working when protocols evolve.
- You enforce protocol adherence through automated contract tests
in the CI/CD pipeline.

**Common anti-patterns:**

- Building ad-hoc communication patterns with custom message
formats per interaction, producing translation layers between
every agent pair.
- Evolving endpoints without versioning or backward compatibility,
breaking existing integrations on each change.
- Allowing each agent to set its own timeout, retry logic, and
error response format, producing unpredictable failure behavior
across the fleet.

**Benefits of establishing this best
practice:**

- Consistent schemas and contracts reduce integration complexity
and remove point-to-point translation code.
- Predictable multi-agent orchestration becomes possible because
agents compose into workflows without hardcoded dependencies.
- New agents can be introduced or replaced without rewriting
dependent components.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides a managed layer for
agent discovery and tool invocation with built-in authentication
and authorization. Underneath it, the Agent-to-Agent (A2A)
protocol standardizes direct agent-to-agent communication and the
Model Context Protocol (MCP) standardizes agent-to-tool
interactions. Choosing these protocols instead of inventing your
own pays off every time a new agent joins the network.

If every agent invents its own error codes and retry guidance, a
caller can't write a single error-handling path. A canonical
format with three fields (error code, correlation ID, and retry
guidance) covers nearly every case and lets callers apply the same
logic regardless of which agent returned the error.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) enforces who can call what at the
gateway boundary through Cedar policies, so the contract is
enforced before the request reaches the agent rather than relying
on documentation alone.

Versioning matters because protocols evolve. Version every
AgentCore Gateway target so callers can migrate at their own pace.
Register message schemas for each agent interaction type so
serialization is consistent across boundaries. Wire contract tests
into CI/CD so protocol regressions get caught before deployment
rather than during an incident.

### Implementation steps

- **Define the canonical communication
taxonomy:** Document the standard message schemas,
error response format, and retry policies that every agent
follows.
- **Configure AgentCore Gateway with A2A
and MCP protocols:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) as the managed surface for
standardized agent-to-agent and agent-to-tool communication.
- **Enforce access control with
AgentCore Policy:** Apply Cedar policies through
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) so the gateway rejects
unauthorized calls at the boundary.
- **Implement canonical error handling
across all agent interfaces:** Propagate a
correlation ID through every call and return errors in the
canonical format so callers can handle them uniformly.
- **Run automated contract tests in
CI/CD:** Block deployment when a protocol
regression is detected so protocol standards stay enforced
as the agent fleet grows.

## Resources

**Related best practices:**

- [AGENTREL01-BP01
Implement a resilient messaging layer](agentrel01-bp01.html)
- [AGENTREL01-BP03 Design
specialized agents following actor model principles](agentrel01-bp03.html)
- [AGENTREL01-BP05
Implement adaptive provisioning](agentrel01-bp05.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Transform
your MCP architecture: Unite MCP servers through AgentCore
Gateway](https://aws.amazon.com/blogs/machine-learning/transform-your-mcp-architecture-unite-mcp-servers-through-agentcore-gateway/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [Strands
Agents A2A Protocol](https://strandsagents.com/docs/user-guide/concepts/multi-agent/agent-to-agent/)
- [Strands
Agents MCP Tools](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/)

**Related videos:**

- [Integrating
MCP Tools with Strands Agents](https://www.youtube.com/watch?v=bHSbjCZZFjE)
- [Breaking
multi-agent silos: A2A + MCP in action with Strands
Agents](https://www.youtube.com/watch?v=TjTgHA5DjDM)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel01-bp04.html*

---

# AGENTREL01-BP05 Implement adaptive provisioning

Static provisioning forces a choice between overpaying for peak and
failing under load. Agent workloads shift minute to minute, so
capacity, model tier, and quota must respond to task complexity and
current demand without operator intervention.

**Desired outcome:**

- You have agent compute allocation that adjusts for each
invocation without manual tuning.
- You route tasks to model tiers appropriate for their complexity,
with fallbacks when quotas tighten.
- You pre-provision resources ahead of known demand patterns and
scale down during quiet periods.

**Common anti-patterns:**

- Running static resource provisioning and paying for peak
capacity even during low-demand periods.
- Skipping the metrics that trigger scaling decisions, so the
system has no basis to provision resources when they are needed.
- Treating every task as needing the same model, ignoring the cost
and latency savings of tiering by complexity.

**Benefits of establishing this best
practice:**

- Performance stays consistent under variable load because
resources track demand instead of a fixed provisioning plan.
- Resource exhaustion during spikes is prevented without human
intervention.
- Cost drops during low-demand periods through automatic
scale-down.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Serverless is the baseline for adaptive compute.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) hosts agents with built-in
scaling that adjusts compute allocation for each invocation, so
individual agents don't need to manage fleet sizing. For LLM
inference, Amazon Bedrock's on-demand mode scales without capacity
reservations.
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) distributes requests across
Regions to reduce the impact of regional capacity constraints.

Tiering matches model selection to workload. Low-complexity tasks
route to smaller, faster Amazon Bedrock models, while complex
reasoning routes to larger models. The router should adjust
dynamically based on task complexity signals and current quota
utilization, not a fixed rule baked into code. For
latency-sensitive user-facing agents where throttling is
unacceptable, use Amazon Bedrock's Priority on-demand tier for
premium throughput allocation. For workloads that need consistent
low latency regardless of overall service demand, use Amazon
Bedrock Provisioned Throughput with fixed model units. The
[Amazon
Bedrock Capacity, Limits, and Cost Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html) guide
covers the trade-offs between Flex, Standard, Priority, and
Reserved tiers.

Monitor composite health signals across agent layers and trigger
coordinated scaling actions when the system approaches capacity
limits. Token throughput, model-level latency, and error rates for
each layer through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) are the signals that drive
tier adjustments. Scheduled scaling handles anticipated demand. If
historical data shows a spike every Monday at 9 a.m.,
pre-provision before the spike lands rather than reacting during
it.

### Implementation steps

- **Deploy agents on AgentCore Runtime
for serverless scaling:** Use
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) so compute allocation
adjusts for each invocation without manual fleet sizing.
- **Route tasks by complexity to
appropriate Amazon Bedrock models:** Implement
tiered model selection that sends low-complexity tasks to
smaller models and reasoning-heavy tasks to larger ones
based on complexity signals.
- **Enable Amazon Bedrock cross-region
inference:** Turn on
[cross-region
inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to distribute requests and reduce the
impact of regional capacity constraints.
- **Monitor token throughput and latency
through AgentCore Observability:** Watch per-tier
throughput and latency through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and trigger tier
adjustments when thresholds are exceeded.
- **Use scheduled scaling ahead of
anticipated spikes:** Pre-provision based on
historical patterns so capacity is ready before demand
lands.

## Resources

**Related best practices:**

- [AGENTREL01-BP01
Implement a resilient messaging layer](agentrel01-bp01.html)
- [AGENTREL01-BP02
Establish modular, fault-isolated layers](agentrel01-bp02.html)
- [AGENTREL08-BP03
Architect agent systems with resource isolation and contention
mitigation](agentrel08-bp03.html)
- [AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Securely
launch and scale your agents and tools on Amazon Bedrock
AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/)
- [Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Amazon
Bedrock Capacity, Limits, and Cost Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html)
- [Effective
cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel01-bp05.html*

---
