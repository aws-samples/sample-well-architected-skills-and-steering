# AGENTOPS04 — Tool integration and management practices

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# AGENTOPS04-BP01 Implement tool registry and catalog management

Agents that can't discover tools end up with hardcoded integrations,
inconsistent documentation, and a maintenance tax that grows with
every new capability. A centralized registry makes the tool catalog
queryable, versioned, and governable.

**Desired outcome:**

- A centralized tool registry provides a single authoritative
source for tool capabilities, current versions, and operational
status.
- Tool documentation is standardized and complete so agents can
select and invoke tools without guesswork.
- Tool versioning and compatibility tracking help prevent agents
from invoking deprecated or incompatible versions.
- Tool deprecation procedures remove sunset tools cleanly without
disrupting dependent agents.

**Common anti-patterns:**

- Allowing each team to manage tool definitions independently
without a shared registry, producing duplicate tools,
inconsistent documentation, and agents that can't discover tools
built by other teams.
- Registering tools without documentation standards, leaving
agents to guess at parameter formats and error codes through
trial and error.
- Deprecating tools without notifying dependent agents, causing
runtime failures when agents attempt to invoke tools that no
longer exist.
- Letting the registry drift out of step with reality, so health
status in the registry contradicts actual tool availability.

**Benefits of establishing this best
practice:**

- A single source of truth for tool capabilities and status means
all agents discover and use tools consistently, and updates
propagate reliably.
- Centralized visibility into the tool catalog lets teams track
availability, version distribution, and dependency relationships
across the agent portfolio.
- Documentation standards reduce invocation errors by giving
agents complete, structured information about each tool.
- Deprecation workflows give dependent agents time to migrate
before tools are removed, helping prevent outages.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start with what
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides before building custom.
AgentCore Gateway includes semantic tool discovery and MCP server
capabilities that handle cataloging, versioning, and discovery
without custom infrastructure. For many teams this covers the
registry requirement completely. Evaluate AgentCore Gateway
against the discovery workflow you need, including capability
search, version tracking, and dependency metadata, before
investing in parallel infrastructure.

A gap for most organizations is documentation standards, not the
registry mechanism. A tool entry can be invoked incorrectly
without a purpose statement, parameter schemas, error codes, rate
limits, and authentication requirements. Enforce completeness as a
gate in the onboarding process rather than as a post-registration
suggestion. The cost of rejecting an undocumented tool during
registration is lower than the cost of debugging misuse after
deployment.

Semantic versioning with compatibility guarantees helps agents and
tools evolve at different speeds. A new version of a tool should
not silently break agents that were written against the previous
version, and a new agent should not be blocked on tools that have
not exposed the version it needs. Maintain multiple active
versions during transitions, and implement deprecation workflows
that notify dependent agents before they are deprecated. Health
checks update tool operational status so that the registry is
updated with realistic data.

### Implementation steps

- **Evaluate
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) as the primary
registry:** Use its semantic tool discovery and MCP
server capabilities, and supplement with custom
infrastructure only where a specific capability is missing.
- **Define tool documentation
standards:** Require purpose, parameter schemas,
error codes, rate limits, and authentication requirements.
Enforce completeness as a gate in the tool onboarding
process.
- **Implement semantic
versioning:** Use compatibility guarantees and
maintain multiple active versions during transitions so
agents and tools can evolve independently.
- **Configure health checks and
deprecation workflows:** Update operational status
automatically and notify dependent agents before sunset
dates.

## Resources

**Related best practices:**

- [AGENTOPS04-BP02
Establish standardized tool integration protocols (MCP,
A2A)](agentops04-bp02.html)
- [AGENTOPS04-BP03 Develop
fallback behavior and error handling for tool
invocations](agentops04-bp03.html)
- [AGENTOPS01-BP01
Establish well-defined agent roles, responsibilities, and
success criteria](agentops01-bp01.html)
- [AGENTSEC02-BP03
Maintain approved tool registry with security
assessments](agentsec02-bp03.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Agentic
AI frameworks, platforms, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html)
- [AI
agents in enterprises: Best practices with Amazon Bedrock
AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)
- [Introducing
Amazon Bedrock AgentCore Gateway: Transforming enterprise AI
agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)

**Related videos:**

- [AWS re:Invent 2024 - Scale agent tools with AgentCore Gateway
(AIM3313)](https://www.youtube.com/watch?v=DlIHB8i6uyE)
- [AWS re:Invent 2024 - Build agentic workflows with third-party
agents and tools (AIM3311)](https://www.youtube.com/watch?v=kfgt1uJE-E4)
- [AWS re:Invent 2024 - Modernize containers for AI agents using
AgentCore Gateway (CNS422)](https://www.youtube.com/watch?v=6autfsn1fy8)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops04-bp01.html*

---

# AGENTOPS04-BP02 Establish standardized tool integration protocols (MCP, A2A)

Point-to-point integrations between every agent and every tool
produce a maintenance burden that grows with the number of
integrations. Standardized protocols like MCP and A2A replace this
with a shared contract, which defaults to interoperability instead
of tools that are custom-made for specific integrations.

**Desired outcome:**

- Agents integrate with tools through standardized protocols (MCP
for tool invocation, A2A for agent-to-agent) that support
interoperability, consistent behavior, and portability across
providers.
- Tool invocations run with secure patterns: least-privilege
access, consistent error handling, and complete audit logs.
- Agents invoke tools reliably across varying network conditions
and tool availability, with fallback mechanisms that maintain
service continuity.
- Error handling follows a standardized taxonomy so every agent
responds to transient, permanent, and authorization failures the
same way.

**Common anti-patterns:**

- Building custom point-to-point integrations for every agent-tool
pair instead of adopting standard protocols, creating a
maintenance burden that grows with scale.
- Implementing tool invocations without standardized error
handling, so each agent handles failures differently and
inconsistently.
- Skipping authentication and audit logging for tool invocations,
making it impossible to trace which agent invoked which tool or
whether it was authorized.
- Treating protocol versioning as an afterthought, so a tool
upgrade silently breaks the agents that depended on the previous
version.

**Benefits of establishing this best
practice:**

- Standardized tool integration with least-privilege access
enforces operational boundaries at the invocation layer, not
just at the agent's internal logic.
- Audit logging of every tool invocation creates the evidentiary
record required for compliance and security reviews.
- Shared error handling patterns mean operators debug tool
failures the same way across every agent.
- Protocol-based integration lets tool providers change backends
without breaking agent consumers, and the reverse.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) is the primary integration layer
for MCP-compatible tool access. It provides managed
authentication, authorization, and tool discovery through a
standardized interface, so agents don't each reimplement those
pieces. For agent-to-agent communication,
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) supports A2A protocol endpoints
with agent discovery through Agent Cards, task lifecycle
management, and structured message exchange. The two together
cover most integration surfaces without custom infrastructure.

Least privilege enforcement needs to happen at the protocol layer,
not at the application layer.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) applies Cedar policies that scope
each agent's tool permissions at the Gateway boundary. Agents can
invoke only the tools their policy allows, regardless of what
their internal code tries to do. The check runs at traffic time,
not at review time. Establish audit logging through
[AgentCore
Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), which produces compliance records without
requiring custom instrumentation.

Error handling benefits a taxonomy of transient errors (retry with
exponential backoff and jitter), permanent errors (fail
gracefully), and authorization errors (escalate to human review).
Each class calls for different agent behavior, and conflating
them, such as retrying a permanent error or escalating a transient
timeout, produces the wrong response at scale. For critical tools,
implement fallback chains that attempt alternatives when the
primary tool is unavailable. Monitor per-tool error rates and
latency through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), and configure alarms so
degradation is detected before it becomes an incident.

Protocol versioning through capability negotiation preserves
backward compatibility as protocols evolve. Version mismatches
should result in the older side operating at its known capability
rather than failing, and both sides should declare supported
versions during handshake.

### Implementation steps

- **Expose tools through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html):** Publish MCP
server capabilities with
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) enforcing per-agent access
controls.
- **Implement A2A protocol
endpoints:** Use
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for standardized
inter-agent communication.
- **Define protocol versioning
strategies:** Use capability negotiation so older
and newer sides interoperate at the common supported
version.
- **Implement standardized error
handling:** Apply the
transient/permanent/authorization taxonomy and fallback
chains for critical tools across every agent.
- **Monitor per-tool health through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html):** Track
error rates and latency, and configure alarms for proactive
detection.

## Resources

**Related best practices:**

- [AGENTOPS04-BP01
Implement tool registry and catalog management](agentops04-bp01.html)
- [AGENTOPS04-BP03 Develop
fallback behavior and error handling for tool
invocations](agentops04-bp03.html)
- [AGENTOPS01-BP01
Establish well-defined agent roles, responsibilities, and
success criteria](agentops01-bp01.html)
- [AGENTPERF06-BP02
Implement efficient tool invocation patterns](agentperf06-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Open
Protocols for Agent Interoperability Part 1: Inter-Agent
Communication on MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp)
- [Open
Protocols for Agent Interoperability Part 4: Inter-Agent
Communication on A2A](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/)
- [Introducing
agent-to-agent protocol support in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/)
- [Open
Protocols for Agent Interoperability Part 2: Authentication on
MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-2-authentication-on-mcp/)
- [Agentic
AI frameworks: Protocol-based tools](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/protocol-based-tools-detailed.html)

**Related videos:**

- [AWS re:Invent 2024 - Building Scalable, Self-Orchestrating AI
Workflows with A2A and MCP (DEV415)](https://www.youtube.com/watch?v=9O9zZ1lQWiI)
- [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8)
- [AWS 2025 - Integrating MCP Tools with Strands Agents](https://www.youtube.com/watch?v=bHSbjCZZFjE)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore, Gateway](https://catalog.workshops.aws/agentcore-deep-dive/en-US/30-agentcore-gateway)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops04-bp02.html*

---

# AGENTOPS04-BP03 Develop fallback behavior and error handling for tool invocations

Tools failing is a reality in modern architectures. The question is
whether the agent degrades gracefully to an alternative, falls back
to a manual process, or returns an error and halts. Well-designed
fallback chains and automatic cutoffs keep tool failures from
becoming agent failures.

**Desired outcome:**

- When tools fail or become unavailable, agents degrade gracefully
to alternative tools, degraded-mode operations, or manual
process escalation.
- Automatic cutoffs help prevent cascading failures from
propagating through the agent environment.
- Retry strategies with exponential backoff handle transient
errors transparently without amplifying load on degraded
systems.
- Per-tool success rates, latency, and error patterns are
monitored in real time so degradation is detected before it
impacts users.

**Common anti-patterns:**

- Implementing identical retry strategies for all tools regardless
of failure characteristics, applying aggressive retries to
permanently failed tools or insufficient retries to transiently
degraded ones.
- Operating without automatic cutoffs, so agents repeatedly invoke
degraded tools that consistently time out, wasting time and
resources on calls unlikely to succeed.
- Having no fallback path when a tool fails, forcing the agent to
return an error to the user or halt the workflow entirely.
- Treating tool runbooks as optional documentation, so operators
start from scratch on each incident.

**Benefits of establishing this best
practice:**

- Per-tool monitoring with error pattern analysis gives deep
visibility into tool reliability across the catalog.
- Operational runbooks help drive consistent incident response,
reducing mean time to resolution and helping prevent ad-hoc
responses that introduce new problems.
- Automatic cutoffs break cascading failures at their source
rather than allowing them to propagate across agents.
- Graceful degradation through fallback chains maintains business
continuity during partial outages.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Automatic cutoffs are the single most effective control for
helping prevent cascading failure. When a tool starts returning
errors above a threshold, continuing to invoke it compounds the
problem. The agent wastes time, the tool gets more load, and
upstream latency climbs while nothing is accomplished. An
automatic cutoff transitions the tool from normal operation to
blocked when error rates exceed a threshold (for example, 50%
errors in a 60-second window) or when timeouts exceed a threshold
(for example, 5 consecutive timeouts). It transitions to probing
after a configurable recovery interval (for example, 30 seconds).
Apply the state machine to every external dependency rather than
the ones that have already caused incidents.

Retry and timeout policies should be per-tool rather than global.
Exponential backoff with jitter handles transient errors without
amplifying the problem. Fallback chains, like primary to secondary
to degraded-mode to manual escalation, give the agent a path
forward when the primary tool is unavailable for critical
operations. The fallback order should live in the tool registry so
it evolves with the tool inventory rather than embedded in each
agent's code.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks invocation count,
success rate, error rate by type, and latency percentiles on a
per-tool basis. Composite alarms correlate multiple metrics. A
tool with rising latency and increasing timeout rate is a tool
approaching cutoff, regardless of whether either signal would fire
an alarm individually. The composite view often catches
degradation earlier than single-metric thresholds would.

Develop operational runbooks for the top five most common tool
failure scenarios, and generate weekly SLA reports shared with
tool owners so reliability trends stay visible.

### Implementation steps

- **Implement automatic
cutoffs:** Configure error rate and timeout
thresholds for the transition from normal to blocked, plus
probing recovery timeouts, for every external dependency.
- **Define per-tool timeout and retry
policies:** Use exponential backoff with jitter
appropriate to each tool's failure characteristics.
- **Build fallback chains for critical
tools:** Store fallback order in the tool registry
so chains evolve with the tool inventory rather than being
hardcoded in each agent.
- **Monitor per-tool health through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html):** Use
composite alarms that correlate multiple metrics for earlier
detection.
- **Develop operational runbooks for
common tool failure scenarios:** Include diagnostic
steps and escalation paths so operators start from a known
baseline.

## Resources

**Related best practices:**

- [AGENTOPS04-BP01
Implement tool registry and catalog management](agentops04-bp01.html)
- [AGENTOPS04-BP02
Establish standardized tool integration protocols (MCP,
A2A)](agentops04-bp02.html)
- [AGENTOPS05-BP01
Establish end-to-end tracing and telemetry for agent
operations](agentops05-bp01.html)
- [AGENTPERF06-BP02
Implement efficient tool invocation patterns](agentperf06-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Planning
for failure: How to make generative AI workloads more
resilient](https://aws.amazon.com/blogs/publicsector/planning-for-failure-how-to-make-generative-ai-workloads-more-resilient/)
- [Effectively
building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops04-bp03.html*

---
