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
