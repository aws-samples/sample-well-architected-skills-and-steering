# AGENTOPS01 — Operational practices for agentic AI systems

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# AGENTOPS01-BP01 Establish well-defined agent roles, responsibilities, and success criteria

An agent without a documented role can be difficult to evaluate and
improve. Provide each agent a clear purpose, scope, autonomy level,
and success criteria to change ambiguous behavior into something
teams can observe, measure, and hold accountable for.

**Desired outcome:**

- Every agent has a documented job description specifying role,
owned business outcomes, autonomy boundaries, and measurable
success criteria.
- Teams can objectively assess whether an agent performs as
intended, and stakeholders understand what value each agent
delivers.
- Failure handling and escalation procedures are defined before
deployment so out-of-scope requests and edge cases are handled
predictably.
- Success criteria map to business outcomes (task resolution rate,
customer satisfaction) alongside technical metrics.

**Common anti-patterns:**

- Deploying agents without documented scope boundaries, producing
unpredictable behavior when the agent encounters requests
outside its intended purpose.
- Defining success criteria using only technical metrics (latency,
uptime) without mapping to business outcomes, making it
impossible to assess whether the agent delivers value.
- Treating agent role definitions as one-time artifacts rather
than living documents that evolve with business requirements.
- Skipping the identification of stakeholders who depend on the
agent, so there is no clear owner when behavior needs
adjustment.

**Benefits of establishing this best
practice:**

- Documented intent and scope become the foundation for downstream
controls. Guardrails, monitoring thresholds, and escalation
paths all derive from the agent's stated purpose.
- Measurable success criteria enable data-driven evaluation,
giving the team empirical evidence for iterative refinement and
investment decisions.
- Out-of-scope requests and edge cases are handled gracefully
because failure paths are defined before the agent ships.
- Stakeholders and operators share a common understanding of what
the agent is supposed to do and who is accountable for its
behavior.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A written role definition is the simplest control an agent can
have, and the one most often skipped. Without it, guardrails get
tuned against assumed behavior, monitoring thresholds get set
against assumed workloads, and escalation triggers fire against
assumed failures. The document should name the agent's primary
purpose, the business process it supports, the stakeholders who
depend on it, and the outcomes it is accountable for. Keep the
document current as requirements evolve.

An agent that observes and reports is a different operational
commitment from one that takes autonomous action, and conflating
these two roles can become an oversight. The maturity progression
from observer to assistant to autonomous to orchestrator to
innovator gives stakeholders a common vocabulary for talking about
how much agency an agent has and how much human review it still
needs. Set the expectation on the right rung of that progression,
and the downstream controls follow.

Success criteria fail when they measure what is cheap to measure
rather than metrics that matter operationally. For example, a
customer support agent with a latency target and no resolution
rate is optimizing for the wrong thing. The SMART framework
(specific, measurable, achievable, relevant, time-bound) helps,
but the sharper test is to check if a metric improves alongside
the business outcome it's measuring. Business outcome metrics
(task resolution rate, escalation rate, customer satisfaction)
should be checked alongside technical ones and share equal weight.

Operationalize the role definition by wiring it into runtime
controls.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) turns documented topic restrictions,
content filters, and denied topics into enforcement at invocation
time. For no-code paths like
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/), the same role-definition discipline applies through
identity, instructions, and knowledge configuration. Publish agent
role definitions to
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) so that both human operators and other
agents can discover capabilities, understand scope, and route work
appropriately.

Failure handling specifies what the agent does when it encounters
requests outside scope, when tools are unavailable, or when it
can't produce a confident response. Graceful degradation paths,
confidence-based escalation, and structured logging for
out-of-scope requests keep edge cases from turning into incidents.
Review job descriptions quarterly or whenever business
requirements change.

### Implementation steps

- **Create an agent job description
template:** Include name and identifier, primary
purpose, stakeholder list, autonomy level on the maturity
model, success criteria with measurable targets,
out-of-scope topics, and escalation procedures.
- **Complete the job description for
each agent:** Engage technical and business
stakeholders together to validate scope and success-criteria
alignment, and capture sign-off from both.
- **Define measurable success
criteria:** Combine business outcome metrics (task
completion rate, escalation rate, user satisfaction) with
technical metrics, and apply the SMART framework to each.
- **Enforce scope at runtime with
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html):** Configure topic
restrictions, content filters, and denied topics that
reflect the agent's documented boundaries.
- **Publish agent definitions to
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html):** Register each agent's
capabilities, scope, and metadata so operators and other
agents can discover and route work appropriately.
- **Define failure handling and
escalation:** Document graceful degradation paths,
confidence-based human escalation triggers, and structured
logging requirements for out-of-scope requests.
- **Establish a quarterly review
cadence:** Update job descriptions as business
requirements change, and treat them as living operational
artifacts owned by a named individual.

## Resources

**Related best practices:**

- [AGENTOPS01-BP02 Design
multi-agent handoff procedures with human-in-the-loop
escalation](agentops01-bp02.html)
- [AGENTOPS02-BP01
Evolve agent prompts, tool calls, and configurations to
reflect evolving business needs](agentops02-bp01.html)
- [AGENTOPS03-BP01
Define an agent lifecycle with clear SME ownership, testing,
and governance](agentops03-bp01.html)
- [AGENTPERF01-BP01
Define performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [AI
agents in enterprises: Best practices with Amazon Bedrock
AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)
- [Kiro
Specs](https://kiro.dev/docs/specs/)

**Related videos:**

- [AWS re:Invent 2024 - Agentic AI Meets responsible AI: Strategy and
best practices (AIM422)](https://www.youtube.com/watch?v=OGvXA1dAh1U)
- [AWS re:Invent 2024 - Agents in the enterprise: Best practices with
AgentCore (AIM3310)](https://www.youtube.com/watch?v=w5XJxCpUADY)
- [AWS 2025 - Beginner-Friendly Amazon Bedrock AgentCore &
Strands Agents Tutorial](https://www.youtube.com/watch?v=j2wYT6jqXZY)
- [AWS re:Invent 2024 - Agentic AI and the journey to gen AI value
realization (AIM242)](https://www.youtube.com/watch?v=p_QuUrB3ONg)

**Related examples:**

- [GitHub:
Amazon Bedrock Samples, GenAI Quick-Start PoCs](https://github.com/aws-samples/genai-quickstart-pocs)
- [GitHub:
Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-getting-started/en-US)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops01-bp01.html*

---

# AGENTOPS01-BP02 Design multi-agent handoff procedures with human-in-the-loop escalation

Without a structured context package, the receiving agent re-derives
work the previous agent already finished. Lacking a defined
escalation path means that high-stakes or low-confidence decisions
can slip past human review.

**Desired outcome:**

- You have documented handoff protocols that transfer tasks
between agents with full context and clear accountability.
- You have escalation paths that route requests to the right agent
or human reviewer when an agent reaches its capability limits.
- You detect deadlocks and timeouts automatically and resolve them
through documented recovery procedures.
- You monitor handoff latency, context transfer completeness, and
collaboration success rates as first-class operational metrics.

**Common anti-patterns:**

- Implementing agent-to-agent handoffs without structured context
packages, forcing the receiving agent to re-derive context and
repeat work the delegating agent already completed.
- Relying solely on agent-to-agent escalation without defining
agent-to-human triggers, leaving high-stakes or low-confidence
decisions without human oversight.
- Deploying multi-agent workflows without deadlock detection or
timeout handling, allowing circular dependencies between agents
to stall the workflow indefinitely.
- Treating handoff failures as rare events, so no one tracks
success rates or context-transfer completeness until a customer
incident forces the investigation.

**Benefits of establishing this best
practice:**

- Documented handoff runbooks and escalation procedures create
repeatable collaboration patterns that reduce operational
complexity.
- Tasks requiring human judgment reliably reach human reviewers
without creating bottlenecks in routine agent-to-agent work.
- Context-rich handoffs help prevent duplicate reasoning, cutting
both latency and token cost in multi-agent workflows.
- Deadlock detection and timeout handling keep transient
coordination failures from becoming workflow-level outages.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A handoff is a data contract before it is a workflow step. The
sending agent must know what to include in the payload, while the
receiving agent must know what to expect. When that contract is
missing, each handoff becomes an improvised negotiation where the
receiver either asks for more information (adding round trips) or
guesses (adding errors). Standardized protocols such as Model
Context Protocol (MCP) and agent-to-agent (A2A) communication give
agents built on different frameworks a shared vocabulary for task
description, completed work, memory artifacts, and handoff reason,
so the contract stays stable across technology choices.

Discovery should be a part of the data contract. Agents need to
know which peers exist, what they can do, and whether they are
accepting work right now.
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides a centralized catalog that captures
capabilities, availability, and metadata for agents and tools,
making intelligent routing possible instead of hardcoded.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) then gives the workflow secure
connectivity and tool invocation across agents, with every
interaction auditable.

Escalation has two distinct triggers to consider:

- Agent-to-agent escalation happens when a task needs
capabilities outside the current agent's scope. This trigger
is a routing decision.
- Agent-to-human escalation happens when confidence drops below
a threshold, the stakes are high, or the retry budget has been
exhausted. This trigger is a judgment decision.

Mixing them together either sends too many routine tasks to humans
(creating fatigue and bottlenecks) or sends too many high-stakes
decisions through automated routing (creating risk). Dictate each
trigger separately and verify that you can see when each one
fires.

Deadlocks deserve their own attention because they are silent. Two
agents can wait for each other indefinitely while every individual
operation looks healthy.

A wait that exceeds a configurable timeout is a deadlock suspect,
but the response has to be automated: task reassignment, human
notification, or both. A deadlock that requires a human to notice
is a deadlock that lasts until someone notices.

### Implementation steps

- **Document handoff
runbooks:** Cover the top five agent-to-agent
collaboration scenarios, specifying context package format,
acceptance criteria, and expected outcomes.
- **Define a structured context package
schema:** Include task description, completed work,
memory artifacts, and handoff reason. Version the schema so
receivers can reject malformed handoffs.
- **Deploy an agent registry:**
Catalog agent capabilities, availability status, and handoff
acceptance criteria in
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) to enable runtime discovery and
intelligent routing.
- **Connect agents through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html):** Configure
secure connectivity, tool invocation, and authorization
across agents with auditable interaction records.
- **Define escalation
criteria:** Separate agent-to-agent triggers
(capability mismatch) from agent-to-human triggers
(confidence threshold, high-stakes decisions, retry budget
exhaustion), and instrument each.
- **Implement deadlock
detection:** Configure alarms on workflow execution
duration, and automate resolution through task reassignment
and human notification.
- **Monitor collaboration
health:** Track success rates, handoff latency, and
context-transfer completeness in
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), with alerting on handoff failure rates.

## Resources

**Related best practices:**

- [AGENTOPS01-BP01
Establish well-defined agent roles, responsibilities, and
success criteria](agentops01-bp01.html)
- [AGENTOPS04-BP01
Implement tool registry and catalog management](agentops04-bp01.html)
- [AGENTOPS04-BP02
Establish standardized tool integration protocols (MCP,
A2A)](agentops04-bp02.html)
- [AGENTOPS05-BP01
Establish end-to-end tracing and telemetry for agent
operations](agentops05-bp01.html)
- [AGENTPERF05-BP04
Implement efficient agent delegation and handoff
patterns](agentperf05-bp04.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Agentic
AI frameworks, platforms, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html)

**Related videos:**

- [AWS re:Invent 2024 - Amazon Bedrock Agents and AgentCore Design
Patterns (TNC322)](https://www.youtube.com/watch?v=GYlPFmrATjU)
- [AWS re:Invent 2024 - Building Scalable, Self-Orchestrating AI
Workflows with A2A and MCP (DEV415)](https://www.youtube.com/watch?v=9O9zZ1lQWiI)
- [AWS re:Invent 2024 - Anti-Money Laundering Multi-agent
Orchestration with AWS Strands (DEV326)](https://www.youtube.com/watch?v=VtrfpAVFKdE)

**Related examples:**

- [GitHub:
Sample Multi-Agent SaaS Workshop](https://github.com/aws-samples/sample-saas-multi-agents-workshop)
- [GitHub:
Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform)
- [GitHub:
Sample Bedrock AgentCore Multi-Tenant](https://github.com/aws-samples/sample-bedrock-agentcore-multitenant)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops01-bp02.html*

---

# AGENTOPS01-BP03 Develop test scenarios that accurately capture failures of dependent components, orchestration protocols, and business processes

Happy-path testing predicts how agents behave when everything works,
while failure testing predicts how they behave in the event of
unforeseen issues. A resilience posture built on injected failures,
deadlock scenarios, and disrupted business processes is the
difference between graceful degradation and an unexpected outage.

**Desired outcome:**

- You have a failure test suite for every agent covering
dependent-component failures, orchestration breakdowns, and
business-process disruptions.
- You can inject failures into agent workflows on demand and
verify that error handling, graceful degradation, and escalation
behave as designed.
- You maintain known failure patterns as regression tests that run
automatically on every behavioral change.
- You track failure test pass rates over time as a visible
resilience metric.

**Common anti-patterns:**

- Testing only the happy path without validating agent behavior
when tools are unavailable, APIs time out, or data sources
return errors.
- Running failure tests only in isolated unit environments without
simulating multi-agent coordination failures such as deadlocks,
message loss, or handoff timeouts.
- Treating failure test scenarios as a one-time exercise rather
than a living regression suite that grows with each production
incident.
- Skipping tests for business-process disruptions, upstream format
changes, delayed approvals, and downstream rejections, so agents
fail silently when the real world shifts.

**Benefits of establishing this best
practice:**

- Failure test suites become a stable benchmark for comparing
agent resilience across iterations, providing the empirical
basis for improvement decisions.
- Standardized testing helps assess every agent change for
resilience impact the same way, regardless of who made the
change or how urgent the timeline is.
- Known failure patterns captured as regression tests help prevent
recurrence of previously diagnosed issues.
- Visible resilience trends give leadership and operators a shared
view of whether the agent portfolio is getting more reliable or
more fragile.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Failure modes cluster into three categories, and each requires a
different testing posture.

Dependent-component failures are the most tractable. Tools return
5xx errors, APIs time out, knowledge bases return empty results,
and model inference throttles or degrades. These map cleanly to
agent evaluation and synthetic fault injection.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) provides automated assessment
of how agents handle edge cases and failure scenarios, using
built-in and custom evaluators to score agent behavior against
expected outcomes. For infrastructure-level fault injection such
as network latency or capacity exhaustion,
[AWS Fault Injection
Service](https://aws.amazon.com/fis/) complements agent evaluations by validating that
retry policies, fallbacks, and cutoffs behave as documented at the
infrastructure layer.

Orchestration breakdowns are harder because they require more than
a single failing component. Message loss, duplicate delivery,
out-of-order messages, deadlocks, handoff timeouts, and
context-package corruption all emerge from the interactions
between agents rather than any single agent's behavior. Test these
scenarios by simulating coordination failures in your multi-agent
workflows. Inject handoff timeouts, corrupt context packages, and
trigger concurrent requests that expose race conditions. Decide
whether to simulate these failures in a shared staging environment
or in a dedicated chaos environment. The former catches
regressions faster, while the latter reduces the scope of impact
during exploratory testing.

Business-process disruptions are the category most often missed
because they don't look like infrastructure failures. When an
upstream team changes an input schema, when a required approval is
delayed, or when a downstream system rejects an agent's output,
the agent's code is intact and every dependency responds, but the
workflow still fails. Test scenarios must cover how the agent
behaves when the business process shifts, like graceful failure,
meaningful error messages, appropriate escalation, and no silent
corruption. These tests protect against the failure mode where the
system looks healthy to monitoring but delivers wrong or
incomplete outcomes.

Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to maintain and run
evaluation datasets that capture known failure patterns as
regression tests. Integrate the evaluation suite into the CI/CD
pipeline as a mandatory gate so deployments are blocked when
failure-handling regression appears. Track pass rates in
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and configure alarms when resilience metrics
degrade. The operational benefit compounds, as every production
incident becomes an opportunity to add a test scenario, and the
suite gets sharper over time.

### Implementation steps

- **Catalog known failure modes per
agent:** Organize by dependent-component failures,
orchestration breakdowns, and business-process disruptions,
with a named owner for each category.
- **Create tests for dependent-component
failures:** Simulate tool unavailability, API
timeouts, data-source errors, and model inference
degradation using
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) dataset evaluations and
custom evaluators.
- **Create tests for orchestration
breakdowns:** Cover communication failures,
deadlock conditions, handoff errors, and context-package
corruption by simulating coordination failures in
multi-agent workflows.
- **Create tests for business-process
disruptions:** Simulate upstream process changes,
input format changes, and downstream system rejections, and
verify graceful failure and meaningful escalation.
- **Integrate infrastructure fault
injection where appropriate:** Use
[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) for infrastructure-level
failures (throttling, capacity exhaustion, network latency)
that affect agent workflows.
- **Gate deployments on failure-handling
regression:** Make the evaluation suite a mandatory
CI/CD stage that blocks promotion when resilience
regressions appear.
- **Maintain evaluation datasets as
living regression suites:** Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to track pass rates,
and alert on degradation via
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).
- **Review and expand scenarios
quarterly:** Incorporate failure patterns
discovered in production incidents so the suite grows with
the system.

## Resources

**Related best practices:**

- [AGENTOPS02-BP01
Evolve agent prompts, tool calls, and configurations to
reflect evolving business needs](agentops02-bp01.html)
- [AGENTOPS04-BP03
Develop fallback behavior and error handling for tool
invocations](agentops04-bp03.html)
- [AGENTOPS06-BP01
Design multi-layered testing frameworks](agentops06-bp01.html)
- [AGENTPERF01-BP01
Define performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)
- [Planning
for failure: How to make generative AI workloads more
resilient](https://aws.amazon.com/blogs/publicsector/planning-for-failure-how-to-make-generative-ai-workloads-more-resilient/)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)

**Related videos:**

- [AWS re:Invent 2024 - Best practices for generative AI
observability (COP404)](https://www.youtube.com/watch?v=sRjm6HS6yYU)
- [AWS re:Invent 2024 - Unlock the power of generative AI with AWS
Serverless (SVS319)](https://www.youtube.com/watch?v=y0jImhzqR1U)

**Related examples:**

- [GitHub:
Open Source Bedrock Agent Evaluation](https://github.com/aws-samples/open-source-bedrock-agent-evaluation)
- [GitHub:
Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform)

**Related services:**

- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [AWS Fault
Injection Service](https://aws.amazon.com/fis/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops01-bp03.html*

---
