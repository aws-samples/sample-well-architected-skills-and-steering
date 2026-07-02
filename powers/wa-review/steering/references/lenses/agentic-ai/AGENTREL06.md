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
