# Reliability

**Pillar**: Reliability  
**Questions**: 8

---

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

# AGENTREL02 — Predictable task execution

**Pillar**: Reliability  
**Best Practices**: 5

---

# AGENTREL02-BP01 Design agents for specific and atomic tasks

LLM outputs are stochastic, so the scope of an agent's
responsibility is also the scope of that stochasticity. Narrow,
atomic agents with explicit input contracts and structured output
schemas make the unpredictable parts of the model more observable,
testable, and containable.

**Desired outcome:**

- You have each agent scoped to one atomic function with explicit
input validation and a structured output schema.
- Your agents are tested with deterministic, representative inputs
before deployment.
- You track per-agent quality metrics (schema compliance rate and
task completion rate) so regressions appear before users see
them.

**Common anti-patterns:**

- Building multi-purpose agents that combine disparate functions,
widening the surface area for unpredictable model behavior.
- Skipping explicit input contracts and output schemas, allowing
ambiguous data flows that amplify LLM stochasticity.
- Treating agents as general-purpose processors without discrete
responsibilities, making issue reproduction hard.

**Benefits of establishing this best
practice:**

- Constrained scope shrinks the surface for unpredictable
behavior.
- Composable units can be independently validated with
deterministic test cases.
- Clear operational boundaries speed up issue identification and
remediation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Atomic design starts with the prompt. A single, well-defined
system prompt that describes exactly one capability is the easiest
constraint to enforce and the hardest to violate silently. Pair it
with explicit input validation that rejects out-of-scope requests
before the LLM is invoked, and a structured output schema that
constrains the response format. Amazon Bedrock's tool use
(function calling) limits the model's action space to operations
relevant to the agent's function. Amazon Bedrock's
[structured
output](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html) feature enforces JSON schema compliance at the model
level to reduce output validation failures.

Deployment reinforces the atomic boundary. Each agent runs on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with its own execution context
and dedicated tool permissions, so a misconfigured or compromised
agent can't reach beyond its scope. This gives you a physical
boundary that matches the logical one you defined in the prompt.

Testing is where atomic design pays off. Because each agent has a
narrow contract, you can run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against representative inputs
and compare outputs to expected results. LLM outputs are not fully
deterministic even with temperature=0, so the tests should
validate semantic correctness rather than exact string matching.
Monitoring each agent through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks schema compliance
rate and task completion rate, with alarms when metrics drift from
baselines.

### Implementation steps

- **Decompose workflows into atomic
agents:** Give each agent a single system prompt, a
constrained tool set, and explicit input/output schemas.
- **Deploy on AgentCore Runtime with
structured output enforcement:** Run each agent on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with dedicated tool
permissions and
[Bedrock
structured output](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html) enforcement.
- **Implement input validation that
rejects out-of-scope requests:** Validate inputs
before the LLM is called so malformed or out-of-scope
requests don't reach the model.
- **Validate behavior with AgentCore
Evaluations:** Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) with representative
inputs and golden-path test cases, asserting semantic
correctness rather than exact strings.
- **Monitor per-agent quality
metrics:** Track schema compliance rate and task
completion rate through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with alarms for
baseline deviations.

## Resources

**Related best practices:**

- [AGENTREL01-BP03
Design specialized agents following actor model
principles](agentrel01-bp03.html)
- [AGENTREL02-BP02 Limit
agent permissions to minimum required access](agentrel02-bp02.html)
- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTREL02-BP04 Develop
clear instruction protocols for agents](agentrel02-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Build
reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [Amazon
Bedrock structured output](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html)
- [Strands
Agents Custom Tools](https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/)

**Related videos:**

- [Strands
Tools: Building Custom AI Agents with Python](https://www.youtube.com/watch?v=EGhIZCfOvG4)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02-bp01.html*

---

# AGENTREL02-BP02 Limit agent permissions to minimum required access

Broad permissions turn a misinterpreted instruction into a cascading
incident. Least-privilege access keeps the scope of impact of
unpredictable LLM behavior narrow and makes anomalous activity more
visible against a well-defined baseline.

**Desired outcome:**

- You have each agent granted only the permissions required for
its specific function.
- You apply runtime access boundaries at the gateway, so the LLM's
reasoning can't widen the agent's reach.
- You audit agent policies continually and remove permissions that
actual usage doesn't justify.

**Common anti-patterns:**

- Granting broad permissions beyond the agent's function, allowing
unpredictable behavior to reach unauthorized systems.
- Writing coarse-grained policies that span multiple systems, so a
single misstep has an outsized impact.
- Skipping audit and monitoring of agent access patterns, missing
the signals that indicate permission misuse.

**Benefits of establishing this best
practice:**

- The scope of impact stays contained when an agent makes an
unexpected decision.
- Clear operational boundaries make agent behavior more
predictable.
- Baseline access patterns make anomalies visible instead of lost
in noise.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Defense-in-depth is the frame for agent authorization. No single
control is enough. AgentCore Identity, AgentCore Policy, and IAM
all have roles to play, and the combination helps prevent a gap in
one layer from becoming an unchecked privilege in another. Use
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) to manage authentication for
agent access to third-party services through OAuth and API key
credentials. Use
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to enforce runtime access
boundaries through Cedar policies at the AgentCore Gateway
boundary, independent of how the agent's LLM reasons.

For agents interacting with Amazon Bedrock models and Knowledge
Bases, use IAM identity-based policies with condition keys to
restrict which models each agent can invoke. Scope Memory access
to designated namespaces using IAM policy conditions. Attach
identity-based policies with Condition blocks that constrain
access by namespace identifier and session context (e.g.,
bedrock:AgentId, bedrock:SessionId). With these conditions in
place, agents operate within their designated memory boundaries
without cross-namespace leakage. As AgentCore Memory's
authorization model evolves, adopt resource-based policies when
available to further simplify namespace-level grants. Avoid
wildcard resources in agent IAM policies. The temptation to use
* for convenience is the single most common
reason least-privilege quietly degrades into broad access over
time.

[AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) generates least-privilege
recommendations based on actual access patterns captured in
CloudTrail, so policies can be tightened based on what the agent
actually uses rather than what it was originally granted.
CloudTrail captures the audit trail, and
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) detects deviations from the
expected operational profile. When suspicious access patterns
appear, automated responses such as permission revocation or agent
quarantine help prevent the deviation from becoming an incident.

### Implementation steps

- **Configure AgentCore Identity and
AgentCore Policy:** Use
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) for authentication and
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) with Cedar to enforce
runtime access boundaries.
- **Create dedicated IAM execution roles
per agent:** Scope each role to specific resource
ARNs and avoid wildcards.
- **Restrict Amazon Bedrock model and
Knowledge Base access with IAM condition keys:**
Allow each agent only the models and knowledge bases its
function requires.
- **Audit policies with IAM Access Analyzer:** Use
[AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to generate least-privilege
recommendations from CloudTrail data and remediate overly
permissive policies.
- **Monitor access patterns and automate
response:** Watch access patterns through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and configure
automated permission revocation or quarantine when anomalies
appear.

## Resources

**Related best practices:**

- [AGENTREL02-BP01 Design
agents for specific and atomic tasks](agentrel02-bp01.html)
- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTSEC03-BP01
Implement strong authentication for agent identities](agentsec03-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02-bp02.html*

---

# AGENTREL02-BP03 Implement behavioral anomaly detection and monitoring

Generic logs miss what matters most for agents: decision points,
tool invocations, and LLM interactions. Structured telemetry with
behavioral baselines exposes anomalies early and gives operators the
audit trail they need to reconstruct why an agent did what it did.

**Desired outcome:**

- You capture decision points, tool invocations, and LLM
interactions for every agent invocation.
- You have behavioral baselines per agent and automated alarms
that fire when metrics drift outside expected ranges.
- You detect behavioral drift through periodic evaluation, not
only through infrastructure errors.

**Common anti-patterns:**

- Running generic logging that doesn't capture agent-specific
decision points, leaving teams unable to understand why an agent
produced an unexpected outcome.
- Operating without behavioral baselines, so there is no basis for
deciding when agent behavior has actually deviated.
- Relying only on manual log review, which delays detection of
reliability issues until users complain.

**Benefits of establishing this best
practice:**

- Automated anomaly detection catches reliability issues before
they cascade.
- Full execution transparency through decision-point logging
speeds up root-cause analysis.
- Structured audit trails reconstruct agent decision-making for
compliance and debugging.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Behavioral monitoring starts with capturing the execution path,
not the final response.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides
OpenTelemetry-compatible telemetry that covers the full path of
each agent invocation, from initial request through LLM inference,
tool calls, memory access, and response generation. Tag traces
with agent-specific metadata such as agent ID, task type, model
used, and tool calls made, so filtering and analysis target the
agent or failure scenario of interest.

Raw telemetry is necessary but not sufficient. Enable
[Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) to capture every LLM
request and response, including prompts, model parameters, token
counts, and latency. Without that depth, reconstructing "why
did the agent choose this tool" reduces to guessing from
summary metrics.

Collect agent-specific metrics over a representative period,
including tool invocation frequency, output token count
distribution, task completion rate, and error rate by type. Apply
[Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) so the system learns the
expected range rather than relying on fixed thresholds. Configure
alarms on anomaly detection bands. Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to periodically assess agent
behavior against quality benchmarks so behavioral drift that
doesn't show up as infrastructure errors still gets caught.

### Implementation steps

- **Enable AgentCore Observability
across every invocation:** Turn on
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with OpenTelemetry
tracing and tag traces with agent-specific metadata.
- **Capture full LLM request/response
data:** Enable
[Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) for anomaly analysis
and audit.
- **Establish behavioral
baselines:** Collect representative agent-specific
metrics and apply
[Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) so thresholds are
learned rather than hand-tuned.
- **Configure alarms on anomaly
detection bands:** Trigger investigation workflows
when metrics drift outside expected ranges.
- **Run AgentCore Evaluations on a
periodic cadence:** Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to detect behavioral
drift against quality benchmarks, not only infrastructure
signals.

## Resources

**Related best practices:**

- [AGENTREL02-BP01 Design
agents for specific and atomic tasks](agentrel02-bp01.html)
- [AGENTREL02-BP02 Limit
agent permissions to minimum required access](agentrel02-bp02.html)
- [AGENTREL08-BP02
Implement agent tracing for telemetry throughout agent
processing](agentrel08-bp02.html)
- [AGENTCOST07-BP02
Establish proactive anomaly detection for agent cost
patterns](agentcost07-bp02.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Build
trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)

**Related videos:**

- [AWS 2025 - AgentCore Observability: Monitor and Debug with
OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02-bp03.html*

---

# AGENTREL02-BP04 Develop clear instruction protocols for agents

Ad-hoc prompts interpreted slightly differently by each model call
produce unpredictable behavior, and the problem multiplies in
multi-agent workflows. Standardized instruction templates, versioned
prompts, and explicit handoff schemas reduce ambiguity and make
regressions traceable to a specific version.

**Desired outcome:**

- You have a canonical system prompt template that every agent
follows, covering role, capabilities, constraints, output
format, and escalation behavior.
- You version prompt templates centrally and log the version used
on every invocation.
- You have explicit handoff schemas for multi-agent delegation so
receiving agents get unambiguous instructions.

**Common anti-patterns:**

- Running ad-hoc prompting without standardized formats, producing
inconsistent interpretation of objectives across agents.
- Omitting explicit handoff procedures for multi-agent
orchestration, leaving downstream agents to guess their role.
- Skipping prompt versioning, so rolling back a problematic change
requires archaeology rather than a configuration flip.

**Benefits of establishing this best
practice:**

- Predictable behavior through standardized instruction formats
that reduce ambiguity.
- Reliable multi-agent orchestration through explicit handoff
procedures and context preservation.
- Faster debugging and refinement through consistent patterns you
can test systematically.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Define one structure that every system prompt follows. This
structure should cover role definition, capability description,
constraint specification, output format requirements, and
escalation behavior. Make the template the starting point for any
new agent. When every agent inherits the same structure, reviewers
can check the important parts at a glance and regressions are more
visible because the diffs are small.

Template storage is where versioning happens. Store prompts in a
versioned configuration store so changes don't require
redeployment. Assign version identifiers to every template and log
the version used in every invocation through
[Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html). When a regression
appears, the version ID on the failing trace tells you exactly
which template is to blame.

Handoffs need their own schema. For multi-agent orchestration, an
explicit handoff message should carry the task identifier, task
type, message body, execution context, deadline, and callback
mechanism. Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) to manage discovery and
invocation with well-defined interface contracts. Validate new
prompt versions offline using
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to compare agent behavior
before migration, and run contract tests in CI/CD including
adversarial cases designed to expose prompt injection
vulnerabilities.

### Implementation steps

- **Define a canonical system prompt
template:** Establish a common structure for role,
capabilities, constraints, output format, and escalation
behavior that every agent inherits.
- **Store prompt templates in a
versioned configuration store:** Centralize
management so prompt updates don't require redeployment.
- **Design explicit handoff message
schemas:** Define a canonical handoff message
format for multi-agent delegation with task identifiers,
message bodies, and callback mechanisms.
- **Use AgentCore Evaluations to compare
prompt versions:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) on candidate versions
before migrating production traffic.
- **Run automated contract tests in
CI/CD:** Include adversarial prompt injection
detection so protocol regressions don't ship.

## Resources

**Related best practices:**

- [AGENTREL02-BP01 Design
agents for specific and atomic tasks](agentrel02-bp01.html)
- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTREL02-BP05
Establish tiered human oversight and approval workflows](agentrel02-bp05.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Build
reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02-bp04.html*

---

# AGENTREL02-BP05 Establish tiered human oversight and approval workflows

Uniform oversight either slows every routine action to a crawl or
lets a high-consequence decision slip through unchecked. Tiering
review to match the risk and reversibility of each action balances
throughput with appropriate governance.

**Desired outcome:**

- You have agent actions classified into tiers (autonomous,
notify, and approve) based on impact and reversibility.
- You have a first-pass automated review layer that filters
policy-violating actions before human reviewers see them.
- You log every oversight decision with reviewer identity,
rationale, and timestamp for compliance and governance
reporting.

**Common anti-patterns:**

- Applying uniform oversight regardless of risk, creating
bottlenecks for routine tasks or letting high-consequence
actions slip through unchecked.
- Skipping clear escalation criteria, so some high-risk actions
proceed autonomously while some low-risk actions queue for
review.
- Running approval workflows without timeouts or fallback, causing
agents to stall indefinitely when reviewers are unavailable.

**Benefits of establishing this best
practice:**

- Appropriate governance for high-consequence actions without
bottlenecks on routine work.
- Reduced risk from LLM stochasticity because irreversible or
high-stakes decisions get human review.
- An audit trail for compliance through structured logging of
oversight decisions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Risk classification is the first design choice. Categorize agent
actions into three tiers. Autonomous actions are low-risk and
reversible. Notify actions are medium-risk and proceed with
operator awareness. Approve actions are high-risk or irreversible
and require explicit human approval. Encode the classification as
Cedar policies through
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html), so tier enforcement happens at
the gateway boundary before the agent can execute. Policy-based
enforcement applies the classification at runtime rather than
relying on reference documentation alone.

Automated first-pass review reduces the load on human reviewers.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) intercepts agent outputs before they
reach reviewers, filtering content that violates predefined
policies. What reaches the human queue should be the genuinely
ambiguous cases, with policy violations filtered automatically.

Approval workflows need structure, not just a pause. A structured
review request should include the action description, the agent's
reasoning, an impact assessment, and the execution history so the
reviewer can decide quickly. Configure timeouts that escalate to
secondary reviewers or fall back to safe defaults when primary
reviewers are unavailable so the system handles reviewer
unavailability without blocking indefinitely. Log every decision
with reviewer identity, rationale, and timestamp, and monitor
approval queue depth through Amazon CloudWatch to detect when
reviews are accumulating. Development tools like
[Kiro](https://kiro.dev/autonomous-agent/)
implement this progressive autonomy pattern directly. Supervised
mode reviews each action before it is applied, while autopilot
mode grants full autonomy for trusted workflows. The two modes
mirror the tiered oversight model at the development layer.

### Implementation steps

- **Define a risk classification
framework:** Categorize agent actions into
autonomous, notify, and approve tiers based on impact and
reversibility, and encode the classification as Cedar
policies through
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html).
- **Configure Amazon Bedrock Guardrails
as the automated first-pass layer:** Use
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to filter policy-violating actions
before human escalation.
- **Build structured approval
workflows:** Pause execution and route review
requests to reviewers. Each request should include the
action description, agent reasoning, impact assessment, and
execution history.
- **Configure timeouts and escalation
paths:** Handle reviewer unavailability without
blocking indefinitely, with escalation to secondary
reviewers or safe default fallbacks.
- **Log every oversight
decision:** Capture reviewer identity, rationale,
and timestamp so the audit trail supports compliance and
governance reporting.

## Resources

**Related best practices:**

- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTREL02-BP04 Develop
clear instruction protocols for agents](agentrel02-bp04.html)
- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSUS03-BP01
Maintain organizational skills and competencies](agentsus03-bp01.html)

**Related documents:**

- [Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Human-in-the-loop
(HITL) - Amazon Nova Act](https://docs.aws.amazon.com/nova-act/latest/userguide/hitl.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)

**Related tools:**

- [Kiro
Autonomous Agent](https://kiro.dev/autonomous-agent/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel02-bp05.html*

---

# AGENTREL03 — Agent memory and state management

**Pillar**: Reliability  
**Best Practices**: 4

---

# AGENTREL03-BP01 Design an information classification model to identify short-term and long-term memories

A single undifferentiated memory store blurs conversation context
with durable knowledge and pulls stale or irrelevant data into
active tasks. Classifying memory at ingestion time and routing each
item to the right tier keeps retrieval predictable and storage costs
aligned with how long each type actually needs to live.

**Desired outcome:**

- You have an explicit memory taxonomy distinguishing short-term
session context from long-term persistent knowledge.
- Your agents classify information at ingestion time and route it
to the appropriate tier with metadata tags.
- You retain each memory type according to a policy matched to its
persistence requirement.

**Common anti-patterns:**

- Storing all memory in a single undifferentiated store, so agents
retrieve stale or irrelevant items during active tasks.
- Running without retention or eviction policies for short-term
memory, letting session context accumulate indefinitely.
- Skipping classification at ingestion, making targeted retrieval
and appropriate retention impossible.

**Benefits of establishing this best
practice:**

- Predictable retrieval through explicit classification that
routes information to the correct store.
- Storage costs aligned with persistence requirements instead of a
one-size-fits-all retention window.
- Reduced context pollution because transient session data can't
contaminate long-term knowledge.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A memory taxonomy is the foundation. At minimum, distinguish
short-term (scoped to a single conversation) from long-term
(durable across sessions). For complex agents, extend the taxonomy
to include episodic memory (records of specific past interactions)
and semantic memory (general domain knowledge). The taxonomy
should be documented in accessible reference materials in addition
to code, because classification decisions happen at ingestion and
must be consistent across agents that write to shared memory.

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides session-scoped and
persistent memory namespaces, handling the underlying
infrastructure. Use session memory for short-term context scoped
to a single conversation, persistent memory for cross-session
knowledge, and shared memory for facts multiple agents consume.
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) handles RAG over external document
corpora, policy documents, product catalogs, and domain reference
material that supplement agent memory with organizational
knowledge.

Classification logic belongs in a dedicated component of the
agent's processing flow, not scattered across prompts. Evaluate
each piece of information against source (conversation turn
vs. task outcome), temporal scope (session-specific
vs. cross-session), and content type (procedural vs. factual).
Route accordingly and tag with metadata so later retrieval can
filter precisely. Monitor memory access patterns through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to catch misclassified
memories. The signal is usually unexpectedly high retrieval rates
from the wrong tier.

### Implementation steps

- **Define a memory taxonomy:**
Document classification criteria for each memory type
(session context, persistent knowledge, episodic records)
and the retention policy that fits each.
- **Configure AgentCore Memory
namespaces:** Provision
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) with session-scoped and
persistent namespaces that map to the taxonomy.
- **Implement classification logic at
ingestion:** Evaluate each item against the
taxonomy criteria and route to the appropriate tier with
metadata tags.
- **Use Amazon Bedrock Knowledge Bases
for external corpora:** Supplement agent memory
with
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for RAG over organizational
knowledge.
- **Monitor access patterns to detect
classification errors:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to spot unexpectedly
high retrieval rates from wrong tiers.

## Resources

**Related best practices:**

- [AGENTREL03-BP02
Architect fault-tolerant memory stores with redundancy and
failover](agentrel03-bp02.html)
- [AGENTREL03-BP03
Implement comprehensive state management and checkpoint-based
recovery](agentrel03-bp03.html)
- [AGENTREL03-BP04
Implement graceful degradation for memory and state
operations](agentrel03-bp04.html)
- [AGENTSUS02-BP01
Optimize context management and memory utilization](agentsus02-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [Building
smarter AI agents: AgentCore long-term memory deep dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Strands
Agents Session Management](https://strandsagents.com/docs/user-guide/concepts/agents/conversation-management/)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)
- [AWS re:Invent 2024 - Make agents remember with AgentCore Memory
(AIM331)](https://www.youtube.com/watch?v=Sh0Ro00_rpA)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore - Lab 2: Memory](https://catalog.workshops.aws/agentcore-getting-started/en-US/30-add-memory)
- [Diving
Deep into Bedrock AgentCore - Memory](https://catalog.workshops.aws/agentcore-deep-dive/en-US/50-agentcore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03-bp01.html*

---

# AGENTREL03-BP02 Architect fault-tolerant memory stores with redundancy and failover

Memory failures don't need to mean agent failures. With redundancy,
fallback paths, and a discipline of testing failover under
controlled conditions, an agent keeps serving reduced-capability
responses until its primary stores recover instead of becoming
completely unavailable.

**Desired outcome:**

- You have primary memory infrastructure with built-in durability
and availability, backed by explicit fallback stores for
degraded operation.
- You have fail-fast logic on memory access that routes to
fallback when primary stores are unavailable.
- You exercise failover regularly in non-production environments
to validate degraded-mode behavior.

**Common anti-patterns:**

- Running memory stores as single points of failure without
replication or failover, causing complete memory loss during
outages.
- Leaving failover manual, so recovery waits on operators and
extends agent downtime.
- Skipping failover testing, discovering the gaps only when
production incidents force the issue.

**Benefits of establishing this best
practice:**

- Downtime drops because automated failover takes over before
operators can intervene.
- Agents keep behaving consistently during memory store failures
through graceful degradation.
- Memory replication across Availability Zones helps protect
against data loss.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides managed memory
infrastructure with built-in durability and availability, so the
default path is already fault-tolerant. The design work is on the
degraded path: what does the agent do when even the managed store
is briefly unreachable, or when a custom store sits alongside it?
Fail-fast logic on memory access is the first answer. When a store
shows elevated error rates, the caller stops waiting and routes to
a fallback. For short-term memory, that fallback is an in-process
cache. For long-term memory, it is a read-through cache of
frequently accessed items.

For agents running on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), the runtime's managed session
storage persists filesystem-level state across stop and resume
cycles. For workflow-stage-aware checkpointing with redrive from
specific failure points, use
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) or framework-level orchestration such as
LangGraph with AgentCore Memory. The choice depends on how
granular the recovery needs to be. Step Functions gives you
durability for each step, while managed session storage gives you
whole-agent durability at session boundaries.

Regular testing validates that failover mechanisms work as
designed.
[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) simulates memory store failures in
non-production environments so you can validate that failover
mechanisms activate correctly and agents continue operating in
degraded mode. Document expected behavior for each failure
scenario and compare observed behavior against the expectations
every time you run the test. Drift between what you expect and
what actually happens is the signal that a regression slipped in.

### Implementation steps

- **Use AgentCore Memory as the primary
managed store:** Default to
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for its built-in durability
and availability.
- **Implement fail-fast logic for memory
access:** Detect elevated error rates on memory
calls and route to fallback stores.
- **Maintain in-process fallback caches
for short-term memory:** Keep current sessions
moving through a last-resort cache that lets the task
complete.
- **Implement read-through caching for
long-term memory:** Serve cached copies of
frequently accessed items during temporary unavailability.
- **Test failover with AWS Fault
Injection Service:** Use
[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to validate degraded-mode
behavior against documented expectations on a regular
schedule.

## Resources

**Related best practices:**

- [AGENTREL01-BP02
Establish modular, fault-isolated layers](agentrel01-bp02.html)
- [AGENTREL03-BP01 Design
an information classification model to identify short-term and
long-term memories](agentrel03-bp01.html)
- [AGENTREL03-BP03
Implement comprehensive state management and checkpoint-based
recovery](agentrel03-bp03.html)
- [AGENTREL03-BP04
Implement graceful degradation for memory and state
operations](agentrel03-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
- [AWS fail-fast pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Fault
Injection Service](https://aws.amazon.com/fis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03-bp02.html*

---

# AGENTREL03-BP03 Implement comprehensive state management and checkpoint-based recovery

Long-running workflows without checkpoints pay the full restart cost
for every failure, no matter how late it happens. Persisting state
at natural boundaries and designing every step to be idempotent lets
an agent resume from the last completed checkpoint rather than redo
work.

**Desired outcome:**

- You have workflow state persisted at regular checkpoints, so
interruptions resume from the last completed point rather than
the beginning.
- You have idempotent workflow steps that produce the same result
when replayed with the same input.
- You have a checkpoint lifecycle with TTL-based expiration and
explicit cleanup after completion.

**Common anti-patterns:**

- Running long-duration agent workflows without intermediate state
persistence, forcing complete restarts on any failure.
- Implementing checkpoints without idempotency guarantees,
producing data corruption or duplicate side effects on resume.
- Skipping checkpoint cleanup, accumulating storage indefinitely.

**Benefits of establishing this best
practice:**

- Workflow restart cost drops because resume starts from the last
checkpoint.
- Duplicate work is prevented through idempotent checkpoint-based
recovery.
- Compute efficiency improves because recovery avoids redundant
recomputation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Checkpointing is only useful if recovery is safe, and recovery is
only safe if steps are idempotent. An idempotent step produces the
same result whether it runs once or five times with the same
input, which means a retry or a resume doesn't add duplicate side
effects. This constraint shapes everything downstream. External
calls need idempotency keys, state mutations need conditional
writes, and event emissions need deduplication logic. Without
idempotency guarantees, checkpoint-based recovery can produce
duplicate side effects or data corruption. Design each step to be
idempotent before implementing checkpointing.

Runtime choice determines how much checkpointing discipline you
need to build yourself.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) supports long-running workloads
with managed session storage that persists filesystem state across
stop and resume cycles, which covers the coarse-grained case. For
workflow-stage-aware checkpointing with redrive from specific
failure points, orchestrate through
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html). Step Functions persists execution state at
every transition and enables restart from the point of failure
rather than from the beginning. For dynamic workflows driven by
supervisor agents, callback patterns pause execution while the
supervisor decides the next action, preserving state persistence
benefits.

Lifecycle management keeps the checkpoint store from growing
without bound. TTL-based expiration handles the common case:
workflows that never complete eventually age out. Explicit cleanup
after successful completion reclaims space immediately. Use
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) to persist checkpoint state and
specification context for agents requiring custom checkpointing.
Monitor checkpoint store health through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so storage growth or access
latency surfaces before recovery starts failing.

### Implementation steps

- **Deploy agents on AgentCore Runtime
with managed session storage:** Use
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for filesystem-level state
persistence across stop and resume cycles.
- **Orchestrate multi-step workflows
through Step Functions:** Use
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for state persistence at every
transition with redrive capability from the point of
failure.
- **Design every workflow step to be
idempotent:** Require idempotency keys on external
calls and conditional writes on state mutations so retries
and resumes don't introduce duplicate side effects.
- **Use AgentCore Memory for custom
checkpoint state:** Persist checkpoint state and
specification context through
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for agents with bespoke
checkpointing needs.
- **Implement checkpoint lifecycle
management:** Set TTL-based expiration and explicit
cleanup after successful completion so the checkpoint store
stays bounded.

## Resources

**Related best practices:**

- [AGENTREL03-BP01 Design
an information classification model to identify short-term and
long-term memories](agentrel03-bp01.html)
- [AGENTREL03-BP02
Architect fault-tolerant memory stores with redundancy and
failover](agentrel03-bp02.html)
- [AGENTREL07-BP01
Design workflows in stages with incremental recovery](agentrel07-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03-bp03.html*

---

# AGENTREL03-BP04 Implement graceful degradation for memory and state operations

Treating every memory failure as fatal turns recoverable issues into
total outages. An explicit degradation hierarchy with documented
modes and automatic recovery keeps agents partially useful and
transparent about their reduced state.

**Desired outcome:**

- You have a memory degradation hierarchy with distinct
operational modes and documented behaviors for each.
- You transition modes automatically based on memory health
signals, and recover to full mode when stores return.
- You communicate degradation state to users and orchestration
systems so they know what to expect.

**Common anti-patterns:**

- Treating all memory failures as fatal, producing complete
unavailability for conditions that could be handled with reduced
functionality.
- Failing to communicate degraded memory state to users, who then
get confused when responses lack expected context.
- Implementing degradation without a recovery path, leaving agents
in degraded mode indefinitely after primary stores return.

**Benefits of establishing this best
practice:**

- Partial service availability persists through memory store
failures instead of becoming a full outage.
- Users and orchestrators see transparent indications of current
capability.
- Full capability returns automatically when memory stores come
back online.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start with the mode hierarchy. Three modes cover most agent
workloads. Full mode has all memory tiers available. Session-only
mode operates without long-term memory, using only session
context. Stateless mode has both tiers unavailable and processes
each request independently. For each mode, define the agent's
behavior explicitly:

- In session-only mode, inform users that previous session
context is unavailable
- In stateless mode, request all necessary context within the
current interaction.

Without this definition, the fallback path is whatever the code
happens to do, which is rarely what you want during an incident.

Health signals drive the transitions.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch
together track memory store availability and error rates.
Configure automated mode transitions when health degrades below
thresholds you set in advance, and automatic recovery when stores
return. For short-term memory degradation, in-process fallback
caches let the current session continue.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) session management maintains
working context even when long-term stores are degraded, which
keeps most conversations coherent through a partial outage.

Communicate degradation state through structured status indicators
so users and downstream systems understand the current
limitations. "I don't have access to your previous
conversations right now" is a better experience than an
agent that silently pretends it does and hallucinates. The same
signals feed orchestration systems that might choose to route
requests elsewhere or surface a banner to users.

### Implementation steps

- **Define a memory degradation
hierarchy with documented modes:** Specify full,
session-only, and stateless modes, with the agent behavior
each mode dictates.
- **Implement automated mode
transitions:** Trigger transitions through health
metrics from
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch.
- **Maintain in-process fallback caches
for short-term memory:** Allow active sessions to
continue when short-term memory degrades.
- **Communicate degradation state to
users:** Surface structured status indicators so
users see the reduced capability instead of guessing.
- **Configure automatic recovery
detection:** Return agents to full mode when stores
become available, without operator intervention.

## Resources

**Related best practices:**

- [AGENTREL03-BP01 Design
an information classification model to identify short-term and
long-term memories](agentrel03-bp01.html)
- [AGENTREL03-BP02
Architect fault-tolerant memory stores with redundancy and
failover](agentrel03-bp02.html)
- [AGENTREL08-BP04
Track agent memory utilization metrics](agentrel08-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03-bp04.html*

---

# AGENTREL04 — Multi-agent orchestration

**Pillar**: Reliability  
**Best Practices**: 4

---

# AGENTREL04-BP01 Implement the arbiter agent pattern for coordinated multi-agent systems

Peer-to-peer coordination among agents produces deadlocks and
conflicting actions at scale. A dedicated arbiter that activates
only for conflict resolution preserves agent autonomy for normal
work while providing a single authoritative place to resolve
contention over shared resources.

**Desired outcome:**

- You have an arbiter agent that activates for conflict resolution
while leaving routine coordination to the specialized agents
involved.
- You store conflict resolution policies in a configuration store
so policy updates don't require arbiter redeployment.
- You escalate unresolvable conflicts to human review
automatically.

**Common anti-patterns:**

- Letting agents coordinate directly without a central arbiter,
creating circular dependencies and deadlocks when requirements
conflict.
- Embedding conflict resolution logic inside specialized agents,
producing inconsistent arbitration across the system.
- Routing every agent interaction through the arbiter, turning it
into a performance bottleneck.

**Benefits of establishing this best
practice:**

- Deadlocks and conflicting actions get resolved by a single
authority instead of leaking into business logic.
- Consistent workflow behavior comes from arbitration policies
applied uniformly across the fleet.
- Specialized agents stay independent because coordination logic
is implemented in the arbiter, not in them.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design the arbiter as an event-driven component rather than a
synchronous dispatcher. The arbiter subscribes to coordination
events through Amazon EventBridge or Amazon SQS, activates only
when a specialized agent explicitly requests arbitration, and
publishes decisions back to the requesting agents. Synchronous
arbitration creates a bottleneck that reduces agent autonomy.

Policy shape matters as much as arbiter placement. Three
categories cover most real coordination conflicts. Priority-based
ordering handles resource contention, confidence scoring resolves
conflicting decisions, and rollback instructions address
constraint violations. Store the policies in Parameter Store, a
capability of AWS Systems Manager or Amazon DynamoDB so they can
be updated without redeploying the arbiter. When a policy turns
out to be wrong, the fix lands quickly rather than waiting for a
deployment cycle. For real-time arbitration needs, implement the
arbiter as a synchronous service invoked through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), accepting that those paths will
be slower but reserving them for cases where asynchrony isn't
acceptable.

Monitoring the arbiter keeps coordination healthy. Track conflict
frequency, arbitration latency, and escalation rates through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Use Amazon CloudWatch
Contributor Insights to identify which agent pairs or resource
types are most frequently involved in conflicts. Those are the
pairs where a coordination protocol redesign pays off the most.
Unresolvable conflicts escalate to human review through Amazon SNS
notifications or a ticketing integration so they are not silently
dropped.

### Implementation steps

- **Design the arbiter as an
event-driven agent on AgentCore Runtime:** Deploy
the arbiter on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) and have it subscribe to
coordination events through EventBridge, activating only for
conflict resolution.
- **Create conflict resolution policies
in a configuration store:** Store rules for
resource contention, conflicting decisions, and constraint
violations in Parameter Store (a capability of AWS Systems Manager) or Amazon DynamoDB.
- **Publish decisions through
EventBridge or AgentCore Gateway:** Route
arbitration decisions back to the affected agents through
EventBridge for asynchronous paths or direct invocation
through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) for synchronous needs.
- **Configure CloudWatch alarms and
Contributor Insights:** Alarm on abnormal conflict
frequency and use Contributor Insights to expose the most
contention-prone agent pairs and resource types.
- **Implement escalation to human
review:** Route unresolvable conflicts to Amazon SNS notifications or a ticketing integration so they reach
an operator.

## Resources

**Related best practices:**

- [AGENTREL04-BP02 Classify
agents with a thorough capability taxonomy](agentrel04-bp02.html)
- [AGENTREL04-BP03
Implement fallback mechanisms and graceful degradation for
collaborative workflows](agentrel04-bp03.html)
- [AGENTREL04-BP04
Implement resilient control planes for agent
coordination](agentrel04-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Customize
agent workflows with advanced orchestration techniques using
Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/)
- [Multi
Agent Collaboration with Strands](https://aws.amazon.com/blogs/devops/multi-agent-collaboration-with-strands/)

**Related videos:**

- [Breaking
multi-agent silos: A2A + MCP in action with Strands
Agents](https://www.youtube.com/watch?v=TjTgHA5DjDM)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Multi-agent
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel04-bp01.html*

---

# AGENTREL04-BP02 Classify agents with a thorough capability taxonomy

Orchestrators that pick agents by hardcoded identifiers can't adapt
when the preferred agent is unavailable or when a new equivalent
arrives. A structured capability taxonomy gives the orchestrator a
basis for routing decisions, and substitution becomes automatic
rather than a redeployment.

**Desired outcome:**

- You have every agent registered with capability categories,
skills, input/output constraints, performance profiles, and
dependencies.
- Your orchestrators consult the registry to select agents rather
than hardcoding identifiers.
- You keep the registry current through the CI/CD pipeline so it
reflects the deployed state.

**Common anti-patterns:**

- Hardcoding agent selection in orchestration logic without
consulting a capability registry, reducing the risk of dynamic
routing.
- Defining capabilities at too coarse a granularity, missing the
nuances of skills, limitations, and resource requirements.
- Letting the capability registry drift from the deployed state
when agents are updated.

**Benefits of establishing this best
practice:**

- Deterministic task routing through structured capability
matching rather than trial and error.
- Automatic agent substitution when preferred agents are
unavailable, without manual reconfiguration.
- Fewer task failures from capability mismatches through precise
capability-to-task matching.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A capability registry is only useful if it stays current. To keep
it current, integrate registration into the deployment pipeline.
An agent reaches production by going through a step that also
updates its entry in
[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html). Skip that step and the registry
becomes a documentation artifact that diverges from reality within
weeks.

AgentCore Registry's semantic capability search makes the registry
useful at runtime. Orchestrators discover agents through natural
language queries that match task requirements to agent
capabilities without hardcoded routing logic. The quality of
search results depends heavily on the quality of the record
descriptions. Descriptions that explain what each agent does and
the problems it solves in plain language produce good matches.
Descriptions that read like function signatures produce poor
matches.

Routing builds on top of registry data. The capability matching
layer accepts a task specification and returns ranked agents that
satisfy the requirements, ordered by match quality and operational
suitability. Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) to route invocations to the
selected agent. Monitor routing effectiveness through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Capability match failures
and routing decisions that result in errors are the signals you
use to find capability gaps.

### Implementation steps

- **Register every agent in AgentCore
Registry:** Populate
[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) with capability
categories, skills, constraints, and performance profiles
for each agent.
- **Automate registration in the CI/CD
pipeline:** Make the deployment step that updates
production also update the registry so the two stay in sync.
- **Use AgentCore Registry's hybrid
search to match tasks to agents:** Write record
descriptions in natural language that explain what each
agent does and the problems it solves, so semantic search
produces accurate matches.
- **Configure orchestrators to consult
the registry:** Replace hardcoded agent identifiers
with registry lookups.
- **Monitor routing
effectiveness:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to find capability
mismatches and gaps.

## Resources

**Related best practices:**

- [AGENTREL04-BP01
Implement the arbiter agent pattern for coordinated
multi-agent systems](agentrel04-bp01.html)
- [AGENTREL04-BP03
Implement fallback mechanisms and graceful degradation for
collaborative workflows](agentrel04-bp03.html)
- [AGENTREL04-BP04
Implement resilient control planes for agent
coordination](agentrel04-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [The
future of managing agents at scale: AWS Agent Registry now in
preview](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)

**Related videos:**

- [AWS 2025 - AgentCore Registry: Discover, Govern, and Reuse AI
Agents at Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel04-bp02.html*

---

# AGENTREL04-BP03 Implement fallback mechanisms and graceful degradation for collaborative workflows

One unavailable agent should not take down an entire workflow.
Pre-defined fallback chains let orchestrators swap in alternatives,
preserving forward progress with reduced quality rather than a
complete stall.

**Desired outcome:**

- You have fallback chains for each critical agent with ordered
alternatives and documented quality trade-offs.
- You check agent health proactively and skip unavailable agents
rather than waiting for timeout.
- You communicate degradation to downstream systems through
structured events so their behavior can adapt.

**Common anti-patterns:**

- Designing multi-agent workflows without fallback paths, so one
failed agent halts the entire workflow.
- Implementing fallbacks that silently degrade quality without
telling users or downstream systems.
- Skipping fallback testing, discovering gaps only during
production incidents.

**Benefits of establishing this best
practice:**

- Partial workflow functionality persists when an individual agent
fails.
- Transparent degradation reaches users and downstream systems so
they can adapt.
- Faster workflow completion through pre-defined fallback paths
that activate automatically.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Fallback chains give the orchestrator somewhere to go when the
preferred agent is down. Each chain is an ordered sequence. First,
a secondary agent with equivalent capabilities. Then, a simplified
agent with reduced capabilities. Next, a cached result from a
previous execution. Finally, a graceful failure response. The
ordering matters because it captures the quality trade-off. The
first few alternatives preserve most of the functionality, and the
later ones accept larger degradation in exchange for keeping the
workflow moving at all. Document the quality impact of each level
so orchestrators pick the best available option rather than the
first technically viable one.

Proactive health checking keeps fallback latency low. Without it,
the orchestrator waits for the preferred agent to time out before
trying the fallback, which stacks agent-level latency penalties on
top of the workflow. Check
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) metrics and
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)'s /ping
endpoint before invocation. When an agent reports degraded health,
skip it and move directly to the next alternative.

When a fallback activates, publish a structured degradation event
that identifies the failed agent, the activated fallback, and the
capability impact. Downstream systems subscribe and adapt by
flagging outputs for additional review, displaying degradation
notices to users, or routing around the affected workflow
entirely. Validate fallback mechanisms through chaos engineering
using
[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html). Inject agent failures in
non-production environments to confirm fallback chains activate
correctly and workflows complete with expected degraded outputs.

### Implementation steps

- **Design fallback chains for each
critical agent:** Define an ordered sequence of
alternatives with documented quality trade-offs at each
level.
- **Implement proactive health checking
before invocation:** Check
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) metrics and the
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) /ping
endpoint, and skip agents reporting degraded health.
- **Configure fallback transitions in
the orchestration layer:** Distinguish transient
failures (retry first) from permanent failures (immediate
fallback).
- **Publish structured degradation
events when fallbacks activate:** Emit events for
downstream systems to consume so the rest of the environment
can adapt.
- **Validate fallback mechanisms through
chaos engineering:** Use
[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to inject agent failures on a
regular schedule and confirm the chains still work.

## Resources

**Related best practices:**

- [AGENTREL04-BP01
Implement the arbiter agent pattern for coordinated
multi-agent systems](agentrel04-bp01.html)
- [AGENTREL04-BP02 Classify
agents with a thorough capability taxonomy](agentrel04-bp02.html)
- [AGENTREL04-BP04
Implement resilient control planes for agent
coordination](agentrel04-bp04.html)
- [AGENTREL08-BP03
Architect agent systems with resource isolation and contention
mitigation](agentrel08-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Multi-agent
collaboration with Strands](https://aws.amazon.com/blogs/devops/multi-agent-collaboration-with-strands/)
- [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Fault
Injection Service](https://aws.amazon.com/fis/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel04-bp03.html*

---

# AGENTREL04-BP04 Implement resilient control planes for agent coordination

A control plane that fails takes every agent with it. Applying the
same reliability principles used on agents, redundancy, durable
state, and loose coupling, to the coordination infrastructure keeps
workflows running during brief outages and preserves state across
restarts.

**Desired outcome:**

- You deploy agents on managed, highly available execution
infrastructure with multi-AZ redundancy.
- You persist workflow state durably so the control plane can
recover without losing progress.
- You design agents to complete in-flight work during brief
control plane outages rather than failing immediately.

**Common anti-patterns:**

- Implementing the control plane as a single point of failure
without redundancy, so outages take down the entire multi-agent
system.
- Holding control plane state in ephemeral memory, losing
coordination state whenever the control plane restarts.
- Coupling agent execution tightly to control plane availability,
reducing the ability for agents to complete in-progress work
during brief outages.

**Benefits of establishing this best
practice:**

- Multi-agent workflows keep running through control plane
component failures.
- Durable state persistence reduces workflow state loss during
outages.
- Loose coupling keeps agents productive during brief control
plane unavailability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AgentCore Runtime is designed as a regional service. Architect
your agents assuming the underlying compute is distributed across
Availability Zones, but validate this assumption for your specific
workload by confirming endpoint behavior during AZ impairment
(e.g., using AZ-isolated canary deployments). Don't rely solely on
service-level redundancy. Implement your own cross-AZ resilience
patterns (multi-AZ deployment of agent orchestrators, regional
failover for stateful components) to maintain availability targets
independent of any single service's internal architecture.

Durable state keeps recovery clean.
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) persists execution state at every
transition, providing built-in retry, error handling, and
resume-from-failure semantics for workflows that need explicit
state machines. Without durable state, every control plane restart
requires agents to recover the coordination context themselves,
which is error-prone and often incomplete.

Loose coupling is the third property, and the hardest to build in
after the fact. Agents should complete in-flight tasks
independently if the control plane is briefly unavailable, rather
than failing immediately on loss of connectivity. Heartbeat
mechanisms let agents periodically report status so the control
plane can detect missed heartbeats and reassign tasks, catching
the cases where an agent has genuinely stopped responding. Monitor
the AgentCore Runtime /ping endpoint for each
agent as the liveness signal, and configure the orchestration
layer to reassign tasks when agents stop responding. Composite
alarms through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) aggregate signals across
coordination components. Regular disaster recovery exercises
validate that automated failover actually works when you need it.

### Implementation steps

- **Deploy agents on AgentCore
Runtime:** Use
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) as the primary execution
infrastructure for its built-in multi-AZ redundancy.
- **Use AWS Step Functions for explicit
workflow state machines:** Run workflows on
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for durable state persistence and
automatic recovery.
- **Use AgentCore Gateway for agent
discovery and invocation:** Route agent calls
through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) for its built-in
availability characteristics.
- **Design agents to complete in-flight
work during brief control plane outages:** Avoid
patterns that require constant control plane connectivity.
- **Implement agent liveness detection
through the AgentCore Runtime /ping
endpoint:** Monitor the endpoint for each agent and
reassign tasks through the orchestration layer when agents
stop responding.
- **Run regular disaster recovery
exercises:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) composite alarms and
periodic DR drills to validate automated failover.

## Resources

**Related best practices:**

- [AGENTREL04-BP01
Implement the arbiter agent pattern for coordinated
multi-agent systems](agentrel04-bp01.html)
- [AGENTREL04-BP02 Classify
agents with a thorough capability taxonomy](agentrel04-bp02.html)
- [AGENTREL04-BP03
Implement fallback mechanisms and graceful degradation for
collaborative workflows](agentrel04-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)

**Related videos:**

- [AWS re:Invent 2024 - Architecting scalable and secure agentic AI
with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel04-bp04.html*

---

# AGENTREL05 — Agent cognition

**Pillar**: Reliability  
**Best Practices**: 3

---

# AGENTREL05-BP01 Design modular, fault-tolerant agentic reasoning components

A monolithic reasoning pipeline fails completely whenever any stage
fails. Splitting cognition into modular stages with clear interfaces
and stage-specific fallbacks lets an agent keep reasoning, with
reduced quality, even when one stage is degraded.

**Desired outcome:**

- You have the reasoning pipeline decomposed into modular stages
with explicit input/output schemas.
- You have stage-specific fallbacks that activate automatically
when error rates climb.
- You log the retrieval tier and model tier used in each
invocation so quality analysis is possible after the fact.

**Common anti-patterns:**

- Running agent cognition as a monolithic pipeline where any
component failure causes complete cognition failure.
- Skipping interfaces between reasoning components, reducing the
ability for independent testing and replacement.
- Treating all reasoning components as equally critical without
distinguishing essential from quality-enhancing components.

**Benefits of establishing this best
practice:**

- Partial cognition survives individual component failures through
modular fault isolation.
- Reasoning components can be optimized or replaced independently,
without full pipeline rewrites.
- Clear component boundaries isolate the source of errors and
speed up debugging.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The first architectural decision is where the stage boundaries go.
Useful boundaries for most agents are context retrieval, prompt
construction, model inference, output parsing, and action
selection. Each stage has a narrow contract: inputs, outputs, and
the error conditions it signals. Deploy each stage on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with its own error handling and
fallback behavior. Without this decomposition, all errors appear
as generic reasoning failures, making debugging difficult. Clear
stage boundaries enable precise error identification and faster
resolution.

Tiering is where the stages earn their modularity. For context
retrieval, primary tier uses
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for semantic search, with fallback
to simpler retrieval methods when the primary is unavailable. For
model inference, implement model tier fallback using
[Bedrock
cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for availability, substituting
alternative models when the primary is degraded. For multimodal
agents,
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) preprocesses documents, images,
audio, and video as a distinct reasoning stage before text-based
reasoning, with independent fallbacks per modality.

Track per-stage error rates, latency, and fallback activation
frequency through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Configure alarms that
trigger automatic cutoffs when stage health degrades. The cutoff
activates the fallback immediately rather than waiting for the
next failed invocation. Log the retrieval tier and model tier used
in each invocation so you can see, months later, which tier
produced the answer and whether the fallback path is being taken
more often than expected.

### Implementation steps

- **Decompose the reasoning pipeline
into distinct stages:** Define explicit
input/output schemas and deploy each stage on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html).
- **Implement automatic cutoffs between
stages:** Activate stage-specific fallbacks when
error rates exceed thresholds.
- **Build tiered context
retrieval:** Use
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) as primary with progressively
simpler fallbacks.
- **Implement model tier
fallback:** Use
[Bedrock
cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for availability during
primary model degradation.
- **Monitor per-stage health:**
Track error rates, latency, and fallback activation through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with alarms that
trigger automatic cutoffs.

## Resources

**Related best practices:**

- [AGENTREL01-BP02
Establish modular, fault-isolated layers](agentrel01-bp02.html)
- [AGENTREL05-BP02
Facilitate reliable adaptation through evaluation-driven
improvement cycles](agentrel05-bp02.html)
- [AGENTREL05-BP03 Ground
agent cognition in real information](agentrel05-bp03.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [AWS fail-fast pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html)
- [Strands
Agents Agent Loop](https://strandsagents.com/docs/user-guide/concepts/agents/agent-loop/)

**Related videos:**

- [AWS re:Invent 2024 - Using Strands Agents to build autonomous,
self-improving AI agents (AIM426)](https://www.youtube.com/watch?v=RQfW7eQsXqk)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel05-bp01.html*

---

# AGENTREL05-BP02 Facilitate reliable adaptation through evaluation-driven improvement cycles

Agents degrade quietly when no one is watching, and runtime
self-modification based on noisy feedback makes things worse.
Structured feedback collection with offline evaluation and validated
deployments keeps adaptation reliable because every change is
measured before it reaches users.

**Desired outcome:**

- You collect action-level, task-level, and session-level feedback
signals on every agent interaction.
- You run automated and LLM-as-a-judge evaluations periodically,
comparing current behavior against golden-path examples.
- You validate prompt and configuration changes offline before
deploying through gradual rollout.

**Common anti-patterns:**

- Deploying agents without feedback collection, missing the chance
to identify systematic errors.
- Applying automated behavioral changes at runtime without offline
validation, risking regression from noisy feedback.
- Skipping monitoring of the feedback loop itself, so silent
pipeline failures block adaptation from happening.

**Benefits of establishing this best
practice:**

- Task execution quality improves steadily through structured
feedback collection and validated adjustments.
- Systematic errors get identified and corrected faster because
automated analysis catches patterns humans miss.
- Manual intervention drops because evaluation-driven prompt
optimization with controlled rollout replaces manual tuning.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Feedback is only useful at the granularity you collect it. Three
tiers cover most of the signal. Action-level captures whether a
tool call succeeded, task-level captures whether the agent
completed the task correctly, and session-level captures whether
the interaction achieved the user's goal. Action-level feedback
tends to come from automated validators that compare outputs
against expected schemas. Task-level feedback can be automated for
deterministic success criteria and needs LLM-as-a-judge for
subjective quality dimensions. Session-level feedback usually
comes from users, either directly or through behavioral signals
like follow-up questions.

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs the periodic quality
assessments against representative task sets, comparing outputs
against golden-path examples and flagging regressions. Store
evaluation results alongside task records so the agent's
performance over time becomes a labeled dataset you can query.
When evaluations indicate systematic degradation, that is the
signal to trigger an offline prompt optimization workflow, test
alternative formulations against evaluation benchmarks and deploy
the highest-performing version through gradual rollout.

The discipline that keeps this reliable is validated before
deployed, not modified at runtime. Runtime self-modification is
tempting because it produces faster feedback, but noisy feedback
can push agents into worse behavior. The scope of impact of a bad
auto-update is the entire production fleet. Offline validation
with gradual rollout keeps improvements under control. Monitor
feedback loop health through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Track collection rates,
processing latency, and evaluation frequency, with alarms when
pipeline failures block the improvement cycle from operating.

### Implementation steps

- **Implement multi-tier feedback
collection:** Capture action-level, task-level, and
session-level signals for every interaction.
- **Deploy automated outcome validators
for deterministic criteria:** Compare outputs
against expected schemas where the success criteria are
unambiguous.
- **Use AgentCore Evaluations with
LLM-as-a-judge for subjective quality:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) on a periodic schedule
against golden-path examples.
- **Trigger offline prompt optimization
when evaluations show degradation:** Validate
candidates against benchmarks offline, then deploy through
gradual rollout rather than runtime self-modification.
- **Monitor feedback loop
health:** Track collection rates, processing
latency, and evaluation frequency through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with alarms for
pipeline failures.

## Resources

**Related best practices:**

- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTREL05-BP01 Design
modular, fault-tolerant agentic reasoning components](agentrel05-bp01.html)
- [AGENTREL05-BP03 Ground
agent cognition in real information](agentrel05-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Build
reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)

**Related videos:**

- [AWS re:Invent 2024 - Using Strands Agents to build autonomous,
self-improving AI agents (AIM426)](https://www.youtube.com/watch?v=RQfW7eQsXqk)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel05-bp02.html*

---

# AGENTREL05-BP03 Ground agent cognition in real information

Training data has a cutoff and an agent reasoning only from model
knowledge can hallucinate about the present. Retrieval-augmented
generation grounds each answer in current, domain-specific
information and reduces hallucination rates as a byproduct.

**Desired outcome:**

- You have retrieval pipelines that ground agent reasoning in
current, domain-specific information.
- You validate knowledge freshness and flag content that exceeds
staleness thresholds.
- You handle retrieval failures gracefully, letting agents
continue with model knowledge while communicating the
uncertainty.

**Common anti-patterns:**

- Relying only on model training data for domain-specific
knowledge, producing outputs that may be outdated or inaccurate.
- Running retrieval without freshness validation, causing agents
to reason from stale data.
- Treating retrieval as a hard dependency, so retrieval failures
cascade into agent failures.

**Benefits of establishing this best
practice:**

- Hallucination rates drop because reasoning is grounded in
retrieved factual information.
- Factual accuracy improves through access to current,
domain-specific knowledge.
- Reliability holds as the operational environment evolves through
knowledge base updates.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) handles the mechanics of RAG,
document ingestion, chunking, embedding, and vector storage, so
most of the setup is configuration rather than infrastructure.
Configure data sources that reflect the agent's domain and set up
automated synchronization to keep content current. S3 event
notifications trigger sync operations when source documents are
updated, and the Knowledge Bases direct ingestion API handles
programmatic content. Chunking strategy matters. Smaller chunks
produce precise factual retrieval, while larger chunks produce
better contextual understanding. Reranking models re-score
retrieved passages for higher-quality context.

A knowledge base populated at launch and never refreshed becomes a
source of wrong answers over time. Track ingestion timestamps and
flag content that exceeds staleness thresholds before it is
served. For information that requires real-time accuracy (prices,
inventory, and system status), caches are not sufficient.
Implement tool functions that agents invoke to retrieve data from
authoritative sources through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), and treat the authoritative
source as the single source of truth.

[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) extracts structured data from
documents, forms, and tables, so agents reason over extracted
content rather than raw images. Retrieved context quality
assessment filters low-relevance results and deduplicates
redundant passages before injection into prompts. Otherwise the
context window fills with noise that drowns out the signal. Handle
retrieval failures by allowing the agent to continue with model
knowledge while communicating uncertainty about information
currency. A transparent "I'm working from general knowledge
rather than current data" beats silent reliance on training
data.

### Implementation steps

- **Configure Amazon Bedrock Knowledge
Bases with automated synchronization:** Set up
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) with domain-appropriate data
sources and sync pipelines triggered by source changes.
- **Implement knowledge freshness
validation:** Track ingestion timestamps and flag
stale content before it is served.
- **Use Knowledge Bases
reranking:** Re-score retrieved passages for
higher-quality context injection.
- **Implement real-time data retrieval
tools through AgentCore Gateway:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) tool functions for
information that requires current accuracy.
- **Handle retrieval failures
gracefully:** Allow agents to continue with model
knowledge while communicating uncertainty about information
currency.

## Resources

**Related best practices:**

- [AGENTREL03-BP01
Design an information classification model to identify
short-term and long-term memories](agentrel03-bp01.html)
- [AGENTREL05-BP01 Design
modular, fault-tolerant agentic reasoning components](agentrel05-bp01.html)
- [AGENTREL05-BP02
Facilitate reliable adaptation through evaluation-driven
improvement cycles](agentrel05-bp02.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)

**Related videos:**

- [AWS re:Invent 2024 - Advanced agentic RAG Systems: Deep dive with
Bedrock (AIM425)](https://www.youtube.com/watch?v=bu2cD1pCFTs)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agent-samples - Knowledge Base
integration](https://github.com/awslabs/amazon-bedrock-agent-samples/tree/main/examples/agents/agent_with_knowledge_base_integration)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel05-bp03.html*

---

# AGENTREL06 — Legacy system integration

**Pillar**: Reliability  
**Best Practices**: 5

---

# AGENTREL06-BP01 Develop agent-based integrations with existing or legacy systems

Legacy systems expose interfaces built for synchronous,
deterministic callers, while agents are asynchronous and
probabilistic. Adapter layers translate between the two worlds so
agents can use existing capabilities without the legacy side needing
to change.

**Desired outcome:**

- You have integration adapters that expose MCP tool interfaces
designed for agent consumption and translate to legacy protocols
internally.
- You enforce canonical error handling that maps legacy error
codes into types agents can interpret uniformly.
- You rate-limit at the adapter layer so agent-driven invocation
speeds don't overwhelm legacy systems.

**Common anti-patterns:**

- Requiring legacy system modifications to support agent
integration, adding deployment risk and organizational friction.
- Coupling agents directly to legacy interfaces without adapters,
exposing agents to legacy-specific complexity.
- Skipping rate limiting on legacy system calls, producing
overload that degrades performance for every consumer.

**Benefits of establishing this best
practice:**

- Legacy system stability is preserved through adapter layers that
shield it from agent interaction patterns.
- Agents and legacy systems evolve on independent schedules
through abstraction interfaces.
- Agent adoption accelerates because integration doesn't require
legacy modifications.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Adapters resolve the impedance mismatch between agent and legacy.
Expose the legacy capability as an MCP tool with a schema an agent
can reason about. Internally, translate to whatever the legacy
system speaks: SOAP, screen scraping, database queries, or batch
files.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) registers adapters as
discoverable tools with consistent authentication policies. Agents
then invoke legacy capabilities through the same tool-call pattern
they use for cloud-based capabilities. The
[blog
on uniting MCP servers through AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/transform-your-mcp-architecture-unite-mcp-servers-through-agentcore-gateway/) covers the
pattern for unifying multiple adapters behind a single gateway
interface.

Error mapping makes the adapter actually useful. Legacy systems
emit error codes specific to their architecture, and exposing
those codes directly forces every agent to understand every legacy
system. A canonical error taxonomy (connection timeout,
authentication failure, rate limit exceeded, and system
unavailable) lets agents apply consistent handling logic without
knowing the specifics of each legacy system. The translation from
legacy code to canonical type happens inside the adapter.

Rate limiting helps protect the legacy side. Legacy systems were
sized for human-paced traffic, not for an agent that can invoke
tools as fast as the LLM generates tool calls. Application-level
rate limiting in the adapter layer throttles agent-driven
invocation speeds to something the legacy system can handle.
Combine this with
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies that restrict which
agents can invoke legacy adapters. Monitor adapter health through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to detect legacy
integration reliability issues before they become incidents.

### Implementation steps

- **Implement integration adapters
exposing MCP tool interfaces:** Translate to legacy
protocols internally so agents see a uniform tool-call
interface.
- **Register adapters in AgentCore
Gateway:** Expose adapters through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with authentication and
discovery for agent invocation.
- **Implement canonical error
mapping:** Translate legacy error codes into a
consistent taxonomy agents can handle uniformly.
- **Enforce access control and rate
limiting:** Use
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) for access control and
implement application-level rate limiting in the adapter to
protect legacy systems.
- **Monitor adapter health through
AgentCore Observability:** Detect legacy
integration reliability issues through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html).

## Resources

**Related best practices:**

- [AGENTREL06-BP02
Establish fallback mechanisms for legacy system
degradation](agentrel06-bp02.html)
- [AGENTREL06-BP03
Regularly test degraded system performance](agentrel06-bp03.html)
- [AGENTREL06-BP04
Implement idempotent task execution patterns](agentrel06-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Transform
your MCP architecture: Unite MCP servers through AgentCore
Gateway](https://aws.amazon.com/blogs/machine-learning/transform-your-mcp-architecture-unite-mcp-servers-through-agentcore-gateway/)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)

**Related videos:**

- [AWS re:Invent 2024 - Adding agentic AI to legacy apps with
AgentCore (MAM345)](https://www.youtube.com/watch?v=_-X-N0J02UI)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel06-bp01.html*

---

# AGENTREL06-BP02 Establish fallback mechanisms for legacy system degradation

Legacy systems carry lower availability SLAs than cloud-based
services, and their failure modes are often unpredictable.
Health-aware fallback paths, caches for reference data, queues for
transactions, graceful degradation for real-time, keep agent
workflows running through legacy outages.

**Desired outcome:**

- You have health monitoring on every legacy integration with
alarms that trigger fallback activation.
- You have cache-based fallbacks for reference data and
queue-based fallbacks for transactional operations.
- You recover automatically when legacy systems return, with
periodic probes deactivating the cutoff.

**Common anti-patterns:**

- Assuming legacy systems match cloud-based reliability, without
implementing fallbacks for their actual SLAs.
- Deploying fallbacks that silently return stale or incorrect data
without informing agents or users.
- Skipping legacy health monitoring, so outages become visible
only when agent tasks fail.

**Benefits of establishing this best
practice:**

- Agent functionality stays available during legacy outages
through pre-defined fallback paths.
- Proactive fallback activation through health monitoring replaces
reactive failure detection.
- Users and downstream systems see transparent indications of
degraded capability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Health monitoring is the prerequisite for any automatic fallback.
Without a health signal, the only way to know the legacy system is
down is to watch user-visible failures accumulate. Periodic probes
through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch check
endpoint availability and response time. Alarms on those probes
trigger fallback activation before the first user-facing failure
happens.

Fallback shape depends on the operation type. For reference data,
product catalogs, configuration values, mostly-static lookups,
cache-based fallbacks serve recently retrieved data during
outages. The accuracy cost is low because the data doesn't change
often. For transactional operations, queue-based fallbacks buffer
requests for replay when the system recovers, preserving the
intent of each operation without attempting it against an
unreachable system. For real-time data that can't be cached or
queued, live prices, current inventory, instantaneous system
state, graceful degradation means informing the user the
information is temporarily unavailable rather than returning a
plausible-but-wrong answer.

Automatic cutoffs need to unwind themselves, or every outage turns
into a permanent downgrade. Use CloudWatch alarms to detect when
error rates cross a threshold and trigger automated responses,
updating
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies to deny tool access
or activating Lambda-based circuit breaker logic. Configure
periodic probes that test availability and re-enable access when
the system recovers. Monitor fallback activation frequency through
AgentCore Observability to identify legacy systems causing
disproportionate reliability issues. Those systems are the
candidates for modernization investment.

### Implementation steps

- **Implement health monitoring for each
legacy integration:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch
probes to check endpoint availability and response time.
- **Configure alarms that trigger
fallback activation:** Alarm on health degradation
so fallbacks activate before user-visible failures
accumulate.
- **Implement operation-appropriate
fallbacks:** Cache-based fallbacks for reference
data, queue-based fallbacks for transactional operations,
and graceful degradation messages for real-time data.
- **Deploy automatic cutoffs with
recovery detection:** Use CloudWatch alarms to
trigger
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) updates or circuit breaker
logic, and run periodic probes to re-enable access when the
system recovers.
- **Monitor fallback activation
frequency:** Use AgentCore Observability to
identify legacy systems that consistently degrade, so
modernization effort can be prioritized.

## Resources

**Related best practices:**

- [AGENTREL04-BP03
Implement fallback mechanisms and graceful degradation for
collaborative workflows](agentrel04-bp03.html)
- [AGENTREL06-BP01 Develop
agent-based integrations with existing or legacy
systems](agentrel06-bp01.html)
- [AGENTREL06-BP03
Regularly test degraded system performance](agentrel06-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel06-bp02.html*

---

# AGENTREL06-BP03 Regularly test degraded system performance

Resilience claims that have never been tested under real failure
conditions are just aspirations. Regular chaos engineering, fault
injection, and load testing under constrained resources reveal the
gaps in fallback coverage while the environment is safe to break.

**Desired outcome:**

- You have experiment templates for the failure scenarios most
likely to affect agent reliability.
- You have documented acceptance criteria for each scenario,
covering expected fallback activation, acceptable degradation,
and recovery time.
- You run fault-injection experiments at least monthly and track
findings through a resilience improvement backlog.

**Common anti-patterns:**

- Testing only happy-path scenarios, discovering resilience gaps
only during production incidents.
- Running degraded testing infrequently, allowing resilience
regressions to accumulate between cycles.
- Testing individual components in isolation without full-workflow
failure scenarios.

**Benefits of establishing this best
practice:**

- Resilience gaps get discovered before they reach production
incidents.
- Fallback mechanisms are validated against real failure
conditions rather than hypothetical ones.
- Resilience assurance keeps pace with system evolution through
regular testing cycles.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) is the managed way to inject
controlled failures into agent infrastructure, throttling, node
failures, network partitions, and observe system behavior. The
experiment is only as useful as the acceptance criteria it is
compared against, so every scenario needs documented expectations.
Define which fallback should activate, what capability degradation
is acceptable, and how long recovery should take. Running the
experiment without criteria gives you an interesting demo. Running
it with criteria gives you a regression test.

Monthly is the minimum frequency that keeps resilience regressions
from accumulating between cycles. Integrating degraded testing
into CI/CD blocks production deployment when tests fail, which is
where resilience assurance actually gets enforced. Run the
experiments in non-production environments scoped tightly enough
that you are not causing incidents you were trying to prevent.

Game days extend the practice into operational readiness.
Quarterly game days where the operations team deliberately induces
failures in production-like environments validate more than
technical fallback mechanisms. They also exercise operational
runbooks, alerting configuration, and team response under time
pressure. The findings get documented in a resilience improvement
backlog and tracked to remediation.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) monitors system behavior
during tests and confirms that degradation detection triggers
correctly.

### Implementation steps

- **Create FIS experiment templates for
high-risk scenarios:** Build
[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) templates for the failure
modes most likely to affect agent reliability, scoped to
non-production environments.
- **Define acceptance criteria per
scenario:** Document expected fallback activation,
acceptable degradation, and recovery time so each experiment
has a pass/fail bar.
- **Integrate degraded testing into
CI/CD:** Block production deployment when tests
fail so resilience assurance is enforced rather than
aspirational.
- **Run experiments at least
monthly:** Schedule FIS experiments on a regular
cadence and track results to detect resilience regressions.
- **Run quarterly game days:**
Exercise operational runbooks, alerting, and team response
procedures under controlled but realistic failure
conditions.

## Resources

**Related best practices:**

- [AGENTREL06-BP01 Develop
agent-based integrations with existing or legacy
systems](agentrel06-bp01.html)
- [AGENTREL06-BP02
Establish fallback mechanisms for legacy system
degradation](agentrel06-bp02.html)
- [AGENTREL06-BP04
Implement idempotent task execution patterns](agentrel06-bp04.html)

**Related documents:**

- [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)

**Related services:**

- [AWS Fault
Injection Service](https://aws.amazon.com/fis/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel06-bp03.html*

---

# AGENTREL06-BP04 Implement idempotent task execution patterns

Retry is the most common recovery mechanism, and without idempotency
it can produce duplicate side effects. Deterministic idempotency
keys and conditional writes let operations be retried safely without
producing duplicate side effects.

**Desired outcome:**

- You generate deterministic idempotency keys from operation
inputs, so retries of the same logical operation always produce
the same key.
- You check for an existing result before executing any
side-effectful operation and return the cached result if the
operation already succeeded.
- You propagate idempotency keys through multi-step workflows and
to external systems that support built-in idempotency.

**Common anti-patterns:**

- Implementing retries without idempotency guarantees, producing
duplicate side effects when operations are retried after partial
completion.
- Using non-deterministic identifiers for idempotency keys, so
retries of the same operation generate different keys and defeat
the guarantee.
- Failing to propagate idempotency keys through multi-step
workflows, allowing duplicate effects at steps that don't
receive the original key.

**Benefits of establishing this best
practice:**

- Retry-based recovery from transient failures becomes safe
without duplicate side effects.
- Error handling simplifies because first-attempt and retry
executions look identical.
- Multi-step workflows recover reliably because idempotency keys
flow through every step.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Idempotency key generation is where most teams go wrong.
Non-deterministic keys (timestamps and UUIDs generated at retry
time) defeat the mechanism because the retry computes a different
key from the original attempt. Deterministic keys derived from
operation inputs work. Hash the workflow ID, task type, and
request body, and the same logical operation always produces the
same key. This is the single most important detail to get right
because everything else depends on it.

Once the key is stable, the pre-execution check becomes trivial.
Before executing an operation with side effects, query the
idempotency store for an existing result keyed on the same
identifier. If you find one and it succeeded, return the cached
result without re-executing. If you don't, run the operation and
record the result.
[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) with conditional writes makes this safe under
concurrency. Two parallel retries can't both create a record, and
TTL-based expiration keeps the store from growing without bound
while maintaining the guarantee within the expected retry window.

Propagation extends the guarantee across workflows. When an
orchestrator delegates a subtask, include the parent workflow's
key or a deterministic derivative so downstream agents maintain
idempotency through every step. For operations interacting with
external systems that support built-in idempotency mechanisms,
pass the agent's key to the external system. Monitor idempotency
store health through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), tracking cache hit rates.
Retries that return cached results are the signal the mechanism is
working as intended.

### Implementation steps

- **Design deterministic idempotency
keys:** Derive keys from operation inputs through
consistent hashing so retries generate the same key as the
original attempt.
- **Implement idempotency checking as a
pre-execution step:** Use
[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) with conditional writes and TTL-based
expiration to store idempotency records safely.
- **Propagate idempotency keys through
multi-step workflows:** Maintain idempotency across
all steps by passing the parent workflow's key or a
deterministic derivative to downstream steps.
- **Pass keys to external systems with
built-in idempotency:** Prevent duplicate
processing at the external system level by forwarding the
agent's key.
- **Monitor cache hit rates:**
Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to watch for retries
that return cached results, confirming the mechanism is
operating.

## Resources

**Related best practices:**

- [AGENTREL06-BP01 Develop
agent-based integrations with existing or legacy
systems](agentrel06-bp01.html)
- [AGENTREL06-BP03
Regularly test degraded system performance](agentrel06-bp03.html)
- [AGENTREL06-BP05
Implement dynamic capability toggling](agentrel06-bp05.html)

**Related documents:**

- [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)

**Related services:**

- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel06-bp04.html*

---

# AGENTREL06-BP05 Implement dynamic capability toggling

Taking an entire agent offline to fix one misbehaving feature is
disproportionate. Feature flags at the gateway boundary let
operators disable the affected capability immediately, keeping the
rest of the agent usable while fixes or investigations proceed.

**Desired outcome:**

- You have capability toggles that disable specific tools or
features without redeploying the agent.
- You have fallback behaviors defined for each capability so
agents continue operating when a feature is disabled.
- You monitor toggle state and fallback usage so capabilities
exhibiting silent degradation surface through elevated fallback
rates.

**Common anti-patterns:**

- Requiring redeployment to disable problematic capabilities,
extending time to remediation.
- Implementing toggles without fallback behaviors, so disabling a
capability triggers agent failures rather than reduced
functionality.
- Omitting user-facing communication when features are
unavailable, leaving users confused about current capability.

**Benefits of establishing this best
practice:**

- Capability-specific issues get remediated quickly without full
agent redeployment.
- Overall agent functionality survives capability toggles through
graceful fallbacks.
- New capabilities can be rolled out gradually and rolled back
immediately when problems appear.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Gateway-level toggling is the control point.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies can enable or
disable specific tool access for agents without redeployment,
providing immediate control over which capabilities are available.
Policy updates propagate quickly, so the toggle can be flipped
while an incident is still active rather than waiting for a
deployment window. For more granular runtime toggling within agent
logic, use a managed configuration service with local caching and
configurable polling intervals so agents respond to changes within
seconds.

Fallback behaviors are what make toggling safe. Define what the
agent does when a capability is disabled. Examples include
semantic search falling back to keyword search, complex reasoning
falling back to simpler rules, and real-time data falling back to
cached values. Document fallback behaviors alongside capability
definitions so operators know the impact of flipping each toggle.
Treat fallback paths as first-class code and test them alongside
the primary implementations so they actually work when you need
them.

Monitoring makes the system self-aware. Track capability toggle
state and fallback usage through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Alarms on fallback rates
that exceed baseline signal capabilities experiencing issues even
when not explicitly toggled off, giving operators early warning
before users report problems. This turns the toggle mechanism from
a manual lever into a proactive detection surface.

### Implementation steps

- **Implement capability toggling
through AgentCore Policy:** Use Cedar policies in
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to control tool access at
the gateway boundary.
- **Define and implement fallback
behaviors for each capability:** Document the
reduced-capability behavior that activates when a toggle is
flipped.
- **Test fallback paths alongside
primary implementations:** Validate that fallbacks
produce acceptable results, not just that they don't error.
- **Monitor toggle state and fallback
usage:** Track both through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html).
- **Configure alarms on elevated
fallback rates:** Detect capabilities experiencing
issues before users report them.

## Resources

**Related best practices:**

- [AGENTREL06-BP01 Develop
agent-based integrations with existing or legacy
systems](agentrel06-bp01.html)
- [AGENTREL06-BP02
Establish fallback mechanisms for legacy system
degradation](agentrel06-bp02.html)
- [AGENTREL06-BP04
Implement idempotent task execution patterns](agentrel06-bp04.html)
- [AGENTREL08-BP01
Establish consistent configuration management practices](agentrel08-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel06-bp05.html*

---

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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
