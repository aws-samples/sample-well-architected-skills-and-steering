# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 7

---

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

# AGENTOPS02 — Prompt and configuration lifecycle management

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# AGENTOPS02-BP01 Evolve agent prompts, tool calls, and configurations to reflect evolving business needs

A prompt shapes agent behavior more directly than almost any other
configuration artifact. Create a prompt lifecycle that applies
code-grade discipline, versioning, review, evaluation, and rollback
to prompts, which helps avoid unnoticed prompt drift and degraded
decisions in agent interactions.

**Desired outcome:**

- You manage agent prompts through a defined lifecycle: authoring,
review, testing, deployment, monitoring, and retirement.
- Every production prompt has a documented version history, an
evaluation record, and a clear owner.
- You deploy prompt updates independently of application code and
roll back to a previous version within minutes.
- You track the performance impact of each prompt change over time
and can attribute quality shifts to specific versions.

**Common anti-patterns:**

- Hardcoding prompts directly in application code, making it
impossible to update agent behavior without a full code
deployment and blocking independent prompt iteration.
- Deploying prompt changes directly to production without
evaluation against quality benchmarks, discovering regressions
only after users report them.
- Operating without prompt version history, making it impossible
to determine which prompt change caused a behavioral regression
or to roll back to a known-good version.
- Treating prompt changes as too small to require review, letting
ad-hoc edits accumulate into drift that no one owns.

**Benefits of establishing this best
practice:**

- Behavioral changes follow a consistent, auditable path from
authoring to deployment, reducing operational risk and enabling
reliable rollback.
- Prompt performance tracking and evaluation create an empirical
basis for iteration. Each update is validated against measurable
quality criteria before reaching production.
- Teams can deploy prompt changes independently of application
code, shortening the feedback loop between business need and
runtime behavior.
- Failed prompt updates revert in minutes rather than requiring an
incident response.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Treat prompts as first-class operational artifacts with the same
discipline applied to application code. Application code moves
through version control, code review, automated tests, staged
deployment, and documented rollback. Most organizations apply none
of these to prompts, which can result in agent behavior drifts.
Apply the same lifecycle to prompts as you do to code, where you
name the stages explicitly and require changes to follow them.

[Amazon
Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) provides versioning, metadata,
and integration with
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html). For no-code paths built with
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/), the same stages apply through the identity and
instructions configuration. A four-stage lifecycle works for most
teams:

- Draft (under development, not deployed)
- Review (under peer review and evaluation)
- Active (deployed to production)
- Archived (retired but retained for audit)

Gate stage transitions by approval workflows implemented in
[AWS CodePipeline](https://aws.amazon.com/codepipeline/) or
[AWS Step Functions](https://aws.amazon.com/step-functions/), not by convention.

Every prompt entry needs required metadata: purpose, target agent,
expected behavior, evaluation criteria, and owner.
Parameterization should be used to reduce duplication across
related agents. Steering files in Kiro or equivalent conventions
codify these standards so they are applied automatically during
development rather than enforced after the fact.

[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) runs each prompt version against a
standardized dataset and produces scores for task success,
response relevance, and adherence to behavioral guidelines. A
prompt that can't meet its minimum thresholds doesn't advance from
review to active. Once in production, quality metrics published to
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) as custom metrics give the team an early warning
when a prompt that passed evaluation starts degrading in the real
world, triggering a review workflow.

### Implementation steps

- **Stand up the central prompt
repository:** Configure
[Amazon
Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) with four lifecycle stages
(draft, review, active, archived) and required metadata
fields (purpose, target agent, expected behavior, evaluation
criteria, owner).
- **Define prompt authoring
standards:** Specify required metadata, formatting
conventions, and documentation requirements. Apply them
through shared templates or steering files so they are
enforced during development.
- **Build versioned evaluation
datasets:** Create datasets for each agent's
primary use cases and store them with versioning enabled so
evaluation results are reproducible.
- **Gate transitions on automated
evaluation:** Configure an
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) pipeline that runs on every
transition from draft to review, with minimum quality
thresholds.
- **Enforce lifecycle stages in
CI/CD:** Use
[AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) to block promotion to active without
approval and evaluation threshold checks.
- **Reference prompts by ID, not by
value:** Deploy agents with parameterized
references to the prompt repository rather than hardcoded
strings, so prompts evolve independently of application
code.
- **Monitor active prompts in
production:** Publish quality metrics to
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), build dashboards per agent, and configure
alarms that trigger review workflows when thresholds are
exceeded.

## Resources

**Related best practices:**

- [AGENTOPS01-BP03 Develop test scenarios that accurately capture failures of dependent components, orchestration protocols, and business processes](agentops01-bp03.html)
- [AGENTOPS02-BP03
Implement agent behavior versioning and rollback capabilities](agentops02-bp03.html)
- [AGENTOPS06-BP01
Design multi-layered testing frameworks](agentops06-bp01.html)
- [AGENTREL02-BP04
Develop clear instruction protocols for agents](agentrel02-bp04.html)

**Related documents:**

- [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evolving software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [AI agents in enterprises: Best practices with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)
- [Kiro](https://kiro.dev/)
- [Kiro
Steering](https://kiro.dev/docs/steering/)

**Related videos:**

- [AWS 2025 - Amazon Bedrock Prompt Management Demo](https://www.youtube.com/watch?v=CE_-zrMvcuk)
- [AWS re:Invent 2024 - Responsible generative AI: Evaluation best practices and tools (AIM342)](https://www.youtube.com/watch?v=wuVpCc5a81Y)

**Related examples:**

- [GitHub:
Sample Bedrock Evaluation Adapter](https://github.com/aws-samples/sample-bedrock-evaluation-adapter)
- [GitHub:
Sample Bedrock Model Evaluation](https://github.com/aws-samples/sample-bedrock-model-evaluation)
- [GitHub:
Amazon Bedrock Samples, GenAI Quick-Start PoCs](https://github.com/aws-samples/genai-quickstart-pocs)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops02-bp01.html*

---

# AGENTOPS02-BP02 Implement configuration drift detection and remediation

Configurations can drift, creating outdated or unstable versions
over time. For example, a manual tweak in one environment, a
guardrail flag changed during an incident, or an experimental
override never reverted can produce agents that behave differently
in production than in testing. Automated drift detection catches
these events before they turn into incidents.

**Desired outcome:**

- Agent configurations stay consistent with approved baselines
across every environment.
- Unauthorized or unintended changes are detected and remediated
automatically.
- Every configuration change follows a documented approval
workflow with a full audit trail.
- Cross-environment consistency is validated continually so
development, staging, and production don't drift apart.

**Common anti-patterns:**

- Managing agent configurations through manual console changes
without version control, making it impossible to track what
changed, when, and by whom.
- Allowing different environments to drift apart without automated
consistency checks, so agents behave differently in production
than in testing.
- Detecting configuration drift only after it causes a production
incident rather than through proactive monitoring.
- Treating behavioral configurations (system prompts, guardrail
settings) as low-risk and skipping approval workflows for
changes that fundamentally alter agent behavior.

**Benefits of establishing this best
practice:**

- Automated drift detection helps keep agent configurations inside
approved boundaries continually, supporting audit requirements
and reducing the risk of unauthorized behavioral change.
- Configuration monitoring provides visibility beyond runtime
metrics, exposing issues at the configuration layer before they
manifest as behavioral problems.
- Cross-environment consistency validation helps detect failures
that passed in testing or staging environments by detecting
divergence between environments early.
- Change events are captured with full attribution, making
root-cause analysis faster when incidents do occur.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

First, determine your source of truth for configuration. If
approved baselines live in a wiki, a shell history, or in the AWS
console, then drift detection has nothing to compare against.
Storing baselines as infrastructure as code (IaC) in
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) or the
[AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) gives every deployment a reproducible
reference point and makes the IaC definition the single artifact
that authoritatively determines what resources should look like.

[AWS CloudFormation drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) reveals when deployed
resources have diverged from their stack definitions.
[AWS Config](https://aws.amazon.com/config/) rules add the runtime layer, monitoring agent
infrastructure continuously and triggering automated remediation
when deviations appear.
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) captures every configuration change event with
full attribution, so when drift is detected, the team can
determine exactly how a change was made without reconstructing
events.

Behavioral configurations, system prompts, guardrail settings,
tool permissions, and decision boundaries need a parallel track
because they don't consistently sit in CloudFormation-manageable
resources. A versioned configuration store with strict access
controls and change notifications handles this layer. Production
changes should require documented justification and sign-off.

The goal isn't to slow teams down but to send a prompt adjustment
that alters downstream behavior through the same review as a code
change. Teams using steering files in Kiro or equivalent can
codify configuration standards so drift is less likely to be
introduced at the source.

Scheduled cross-environment validation catches the slow category
of drift that single-event detection misses. Snapshot the
configuration of each environment on a cadence, compare the
snapshots, and alert on any discrepancy that isn't explained by an
approved change. This check reveals drift that accumulated
gradually over months rather than arriving in a single event.

### Implementation steps

- **Define configuration baselines as
IaC:** Store agent infrastructure definitions in
[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or
[AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) under version control, with the IaC definition as
the single source of truth.
- **Configure drift
detection:** Use
[AWS CloudFormation drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) for infrastructure and
[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) rules for agent-specific configurations
(guardrail settings, model parameters) against approved
baselines.
- **Enable change event capture with
full attribution:** Turn on
[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and route change events to alerting and
automated remediation workflows.
- **Version behavioral
configurations:** Store prompts, guardrail
settings, and decision boundaries in a versioned
configuration store with access controls and mandatory
approval workflows for production changes.
- **Validate cross-environment
consistency on a schedule:** Compare configuration
snapshots across development, staging, and production, and
alert on unexplained discrepancies.

## Resources

**Related best practices:**

- [AGENTOPS02-BP01 Evolve
agent prompts, tool calls, and configurations to reflect
evolving business needs](agentops02-bp01.html)
- [AGENTOPS02-BP03
Implement agent behavior versioning and rollback
capabilities](agentops02-bp03.html)
- [AGENTOPS03-BP01
Define an agent lifecycle with clear SME ownership, testing,
and governance](agentops03-bp01.html)
- [AGENTREL08-BP01
Establish consistent configuration management practices](agentrel08-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)
- [Kiro
Steering](https://kiro.dev/docs/steering/)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)

**Related videos:**

- [AWS re:Invent 2024 - Architecting scalable and secure agentic AI
with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc)

**Related examples:**

- [GitHub:
Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform)

**Related services:**

- [AWS Config](https://aws.amazon.com/config/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops02-bp02.html*

---

# AGENTOPS02-BP03 Implement agent behavior versioning and rollback capabilities

Teams with versioned behavior and tested rollback can recover in
minutes when an agent behaves unexpectedly, while teams without
spend hours debugging under pressure. Rapid reversibility improves
your organization's ability to confidently iterate on an agentic
system.

**Desired outcome:**

- Every agent behavioral configuration (system prompts, reasoning
instructions, tool permissions, and decision boundaries) is
versioned with a complete change history.
- You can roll back to any previous behavioral version within
minutes when a change produces undesired outcomes.
- Rollback procedures are automated and tested regularly, not
improvised during incidents.
- Staged rollouts limit the scope of impact of behavioral changes,
and A/B testing supports data-driven comparison of variants
before full deployment.

**Common anti-patterns:**

- Deploying behavioral changes to 100% of traffic immediately
without staged rollout, maximizing the scope of impact when a
change produces undesired outcomes.
- Operating without a defined behavioral baseline, the last
known-good configuration, so rollback becomes a manual search
for which previous version was stable.
- Treating prompt changes as low-risk because they don't involve
code changes, skipping evaluation and staged rollout for
modifications that can fundamentally alter agent behavior.
- Running A/B tests without statistical discipline, making
deployment decisions from noise rather than signal.

**Benefits of establishing this best
practice:**

- Systematic versioning and rollback create a safety net that lets
teams iterate on agent behavior confidently, knowing any change
can be reversed quickly.
- A/B testing frameworks and behavioral baselines provide the
empirical foundation for continuous improvement, validating that
each iteration produces measurable gains.
- Staged rollouts limit the users affected by a regression, giving
the team detection and correction time before full exposure.
- Change impact assessment ties quality metric shifts to specific
behavioral versions, making attribution direct instead of
inferred.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) handles prompt-based
configurations with built-in semantic versioning, metadata, and
integration with evaluation. Non-prompt configurations (tool
permissions, decision boundaries, and escalation thresholds)
should be stored in a versioned configuration store with change
tracking. Each version should carry a semantic version number, a
change description, an author, and a reference to its evaluation
results.

A behavioral baseline is a version that the team has explicitly
designated as known-good, not just the previous version, because
the previous version might have been shipped an hour ago and never
proven stable. Rollback should restore the baseline, not the last
change, unless the team has explicitly promoted that change to
baseline status. Without a designated baseline, rollback requires
searching through multiple versions to find a stable
configuration.

Rollback itself should be automated and rehearsed. Design rollback
as an automated workflow triggered by either manual approval or by
automated quality threshold violations from
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms. The target time-to-restore should be
under five minutes for behavioral changes. Anything longer means
the workflow has too many manual steps or too many dependencies
that aren't pre-staged. Exercise the rollback quarterly so the
procedure stays current with the runtime. For example, a rollback
that was written six months ago and never run is a rollback that
may not work.

Staged rollout limits the scope of impact before rollback is ever
needed.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) endpoint-based weighted routing
makes this straightforward. Start a new behavioral version at
5–10% of traffic, monitor quality metrics, and promote only when
the signal is clean. A/B testing uses the same machinery for
different ends, splitting traffic between variants to measure
which performs better. The critical additions are per-variant
metrics in CloudWatch and statistical significance testing before
deployment decisions. Document the evaluation criteria and results
alongside the behavioral version record so the comparison is
reproducible.

Perform impact assessments where you correlate version deployment
timestamps with changes in quality metrics to attribute metric
shifts to specific behavioral updates. When a metric moves, the
team should quickly determine which version caused the issue as
opposed to pattern-matching different dashboards to find the
problematic version.

### Implementation steps

- **Enable semantic versioning for
prompts:** Configure
[Amazon
Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) with metadata fields for
change description, author, and evaluation results on every
version.
- **Version non-prompt
configurations:** Store tool permissions, decision
boundaries, and escalation thresholds in a versioned
configuration store with change tracking and notifications.
- **Designate behavioral
baselines:** Tag and document the last known-good
configuration for each agent as the rollback target,
distinct from the most recent version.
- **Automate rollback:** Build
workflows that restore baselines within five minutes,
triggered by manual approval or automated quality threshold
violations from
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms.
- **Configure staged rollout:**
Use
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) endpoint-based weighted
routing starting at 5–10% traffic for new behavioral
versions, with automated promotion gates.
- **Set up A/B testing
infrastructure:** Capture per-variant metrics in
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) with statistical significance tracking
before deployment decisions.
- **Correlate deployments to metric
shifts:** Record deployment timestamps alongside
quality metric trends so changes can be attributed to
specific versions.

## Resources

**Related best practices:**

- [AGENTOPS02-BP01 Evolve
agent prompts, tool calls, and configurations to reflect
evolving business needs](agentops02-bp01.html)
- [AGENTOPS02-BP02
Implement configuration drift detection and remediation](agentops02-bp02.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [Deploy
AI agents on Amazon Bedrock AgentCore using GitHub
Actions](https://aws.amazon.com/blogs/machine-learning/deploy-ai-agents-on-amazon-bedrock-agentcore-using-github-actions/)

**Related videos:**

- [AWS re:Invent 2024 - Architecting scalable and secure agentic AI
with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc)
- [AWS re:Invent 2024 - Amazon Bedrock Agents and AgentCore Design
Patterns (TNC322)](https://www.youtube.com/watch?v=GYlPFmrATjU)

**Related examples:**

- [GitHub:
Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform)
- [GitHub:
Amazon Bedrock Samples, GenAI Quick-Start PoCs](https://github.com/aws-samples/genai-quickstart-pocs)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops02-bp03.html*

---

# AGENTOPS02-BP04 Maintain feedback control loops for continuous improvement

Agents that improve in step with real-world usage outperform agents
frozen at deployment. A working feedback loop connects quality
signals, user feedback, behavioral cues, and business outcomes to
prioritized improvement actions.

**Desired outcome:**

- You collect and correlate agent performance data, user feedback,
and business outcome metrics systematically, not through ad-hoc
surveys.
- Feedback loops operate continually, detecting quality trends in
near real time rather than through quarterly reviews.
- Improvement actions are tracked from identification through
implementation and validation.
- Feedback signals are attributable to specific agent versions, so
teams know which improvements are responding to which problems.

**Common anti-patterns:**

- Collecting user feedback (like thumbs up and down or ratings)
without connecting it to specific agent behaviors or prompt
versions, making it impossible to attribute quality changes to
improvements.
- Relying solely on periodic manual reviews rather than continuous
automated feedback processing, allowing quality degradation to
persist for weeks before detection.
- Collecting feedback data without a defined process for turning
insights into improvement actions, creating a growing backlog of
signals that never translate into agent changes.
- Mixing signal types into a single bucket, so a surge in
automated quality alerts drowns out a handful of high-severity
user reports that deserve immediate attention.

**Benefits of establishing this best
practice:**

- Structured feedback turns operational data into a continuous
source of improvement signals, so agents evolve in response to
real usage rather than staying static after deployment.
- Feedback-driven prioritization directs development effort toward
changes with the greatest measurable impact.
- Trend tracking over time reveals patterns (data drift, concept
drift, and scope drift) that inform targeted refinement rather
than scattershot tweaking.
- Improvement validation gives the team evidence that each change
delivered the expected gain.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Feedback loops should watch more than one signal to be truly
useful.

Automated quality metrics from
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) show measurable shifts in output quality.

To watch subjective perception, consider checking:

- Explicit user feedback
- Thumbs up and down
- Ratings
- Free-text comments

To determine whether users are finding what they need, consider
checking:

- Implicit behavioral signals
- Task abandonment
- Escalation rates
- Retry patterns

To determine if the agent is adhering to your organization's
goals, consider checking:

- Business outcome metrics
- Conversion rate
- Resolution time
- Customer satisfaction

Each channel catches failures the others miss, so collecting all
four of these metric pathways and routing them through a unified
processing pipeline is the minimum viable design.

Use event-driven ingestion to keep your pipeline scalable.
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) or an equivalent event bus takes feedback
events from every channel and routes them to a processing layer
that classifies by type (quality issue, capability gap, tool
failure, behavioral misalignment), severity, and affected
component. Storing processed feedback in
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with indexing by agent, feedback type, and time
period makes trend analysis and querying practical instead of
painful.

Consider implementing severity-based routing to avoid drowning
your teams in constant alerts. High-severity feedback, a user
reporting the agent did something dangerous, or a sudden drop in a
quality metric goes straight to an immediate-review queue.
Lower-severity feedback aggregates into batch reviews that surface
patterns over days rather than requiring immediate reactions.

Verify that you have an effective improvement tracking workflow.
To keep your feedback process useful and actionable, you need:

- A durable workflow
- Identification
- Root cause analysis
- Improvement design
- Implementation
- Validation
- Correlation to the specific feedback that prompted the action
- Metrics compared before and after each change

Validation is the step most often skipped, and the one that tells
the team whether an improvement was truly effective.

Dashboards help you address visibility of both feedback and
improvements. Feedback trends alongside improvement outcomes
provide a clear view of whether the agent's quality trajectory is
rising, flat, or falling, and which improvements are responsible
for each inflection.

### Implementation steps

- **Implement multi-channel feedback
collection:** Cover automated quality metrics
(through
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)), explicit user feedback, implicit
behavioral signals, and business outcome metrics.
- **Classify feedback at
ingestion:** Categorize by type (quality issue,
capability gap, tool failure, behavioral misalignment),
severity, and affected component.
- **Store processed feedback for trend
analysis:** Use
[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) indexed by agent, feedback type, and time
period.
- **Route by severity:** Send
high-severity feedback to immediate review queues through
[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). Aggregate lower-severity items for batch
review.
- **Track improvements end to
end:** Build a workflow that moves each item from
identification through root-cause analysis, implementation,
and validation, with metrics compared before and after.
- **Build visibility into trends and
outcomes:** Create dashboards that show feedback
trends, improvement outcomes, and quality trajectory over
time.

## Resources

**Related best practices:**

- [AGENTOPS02-BP01 Evolve
agent prompts, tool calls, and configurations to reflect
evolving business needs](agentops02-bp01.html)
- [AGENTOPS05-BP02
Monitor agent behavior patterns and detect anomalies](agentops05-bp02.html)
- [AGENTPERF01-BP01
Define performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)

**Related videos:**

- [AWS re:Invent 2024 - Elevate application and generative AI
observability (COP326)](https://www.youtube.com/watch?v=vxzq8GthOLs)
- [AWS re:Invent 2024 - Responsible generative AI: Evaluation best
practices and tools (AIM342)](https://www.youtube.com/watch?v=wuVpCc5a81Y)

**Related examples:**

- [GitHub:
Open Source Bedrock Agent Evaluation](https://github.com/aws-samples/open-source-bedrock-agent-evaluation)
- [GitHub:
Sample Bedrock Evaluation Adapter](https://github.com/aws-samples/sample-bedrock-evaluation-adapter)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops02-bp04.html*

---

# AGENTOPS03 — Agent lifecycle and deployment processes

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# AGENTOPS03-BP01 Define an agent lifecycle with clear SME ownership, testing, and governance

An agent portfolio without lifecycle discipline becomes a graveyard
of undocumented services with forgotten owners. Explicit lifecycle
stages, named SME ownership, and clean decommissioning keep the
portfolio tractable as it grows from a handful of agents to dozens
or hundreds.

**Desired outcome:**

- Every agent has a documented lifecycle state (development,
pilot, production, deprecated, and decommissioned) with defined
transition criteria.
- Onboarding follows a standardized provisioning process that
configures required resources, permissions, and monitoring
before an agent handles production traffic.
- Decommissioning cleanly removes retired agents, no orphaned
resources, dangling permissions, or undocumented dependencies
left behind.
- Each agent has a named SME owner accountable for its behavior,
performance, and eventual retirement.

**Common anti-patterns:**

- Deploying agents to production without a defined lifecycle state
or designated owner, so no one is accountable when behavior
needs attention.
- Operating without decommissioning procedures, leaving retired
agents running with active permissions and consuming resources
long after they were replaced.
- Skipping the pilot stage and pushing agents from development
directly to full production, missing the chance to validate
behavior under real traffic with enhanced monitoring.
- Treating the agent registry as a one-time artifact that nobody
updates once the agent is live.

**Benefits of establishing this best
practice:**

- Standardized lifecycle procedures produce consistent
provisioning, operation, and retirement, reducing operational
complexity as the portfolio grows.
- Documented lifecycle states and transition criteria create an
auditable record of each agent's history for compliance and
governance.
- Named owners accelerate incident response. When an agent
misbehaves, the team knows who to engage without a search.
- Clean decommissioning helps prevent the slow accumulation of
abandoned resources that becomes a cost and security problem
over time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Five stages cover the operational arc of almost any agent:

- Development (under active development, not serving production
traffic)
- Pilot (limited production use with enhanced monitoring and
cost validation)
- Production (full deployment with standard operational
procedures)
- Deprecated (scheduled for decommissioning, no new
integrations)
- Decommissioned (removed from service, resources cleaned up)

Each transition should carry explicit criteria, required
approvals, validation gates, and documentation requirements, so
stage changes are decisions rather than drift.

Pilot validates economic viability and identifies issues before
full deployment, reducing the cost of addressing problems. For
teams using spec-driven development with tools like Kiro, the spec
workflow produces the documentation needed for lifecycle
governance as a byproduct. This is a useful side effect worth
using rather than rebuilding.

An agent registry is a durable artifact that makes this process
coherent. It should track agent ID, lifecycle state, owner,
dependencies, capabilities, and operational metadata. Without a
registry, lifecycle state exists only in people's heads, making it
difficult to track and manage consistently across the
organization. The registry becomes the input for portfolio
reviews, decommissioning dependency analysis, and emergency
response.

Emergency lifecycle transitions deserve their own processes.
Automated emergency termination switch mechanisms allow immediate
revocation of an agent's permissions and halting of operations,
enabling rapid response to operational issues. The decommissioning
runbook does similar work for the planned case. It removes
resources, revokes permissions, updates the registry, and notifies
dependent systems as automated steps rather than as checklist
items. For agents built through no-code platforms like
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/), the same lifecycle rules apply. The registry tracks
them, portfolio reviews consider them, and decommissioning cleans
them up.

### Implementation steps

- **Document the five lifecycle
stages:** Specify transition criteria, required
approver roles, and validation gates for each stage.
- **Build the agent registry:**
Track agent ID, lifecycle state, owner, dependencies,
capabilities, and operational metadata in a durable store.
- **Automate lifecycle state
transitions:** Validate criteria, trigger
stage-specific actions, and record transitions with
attribution, deployments, permission changes, monitoring
setup, and decommissioning steps.
- **Create standardized provisioning
templates:** Configure required resources,
permissions, and monitoring automatically so new agents
enter production with a consistent baseline.
- **Implement emergency termination
switch and decommissioning runbooks:** Include
dependency analysis before running so decommissioning
doesn't break upstream consumers.
- **Establish quarterly portfolio
reviews:** Identify agents for deprecation or
decommissioning, including those built with no-code
platforms like
[Amazon Quick](https://aws.amazon.com/quicksuite/).

## Resources

**Related best practices:**

- [AGENTOPS01-BP01
Establish well-defined agent roles, responsibilities, and
success criteria](agentops01-bp01.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTOPS03-BP03
Implement agent-specific scaling policies and capacity
planning](agentops03-bp03.html)
- [AGENTOPS02-BP02
Implement configuration drift detection and remediation](agentops02-bp02.html)
- [AGENTCOST06-BP02
Cost optimize versioning and deployment through efficient
artifact management](agentcost06-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Focus
area 5: Manage the lifecycle](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/focus-areas-lifecycle.html)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [Preparing
the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [Kiro
Specs](https://kiro.dev/docs/specs/)
- [Operationalizing
Agentic AI Part 1: A Stakeholder's Guide](https://aws.amazon.com/blogs/machine-learning/operationalizing-agentic-ai-part-1-a-stakeholders-guide/)

**Related videos:**

- [AWS re:Invent 2024 - Agents in the enterprise: Best practices with
AgentCore (AIM3310)](https://www.youtube.com/watch?v=w5XJxCpUADY)
- [AWS re:Invent 2024 - Cox Automotive's Blueprint for Agentic AI on
AgentCore (IND3329)](https://www.youtube.com/watch?v=ICA8-d_Nt9Q)
- [AWS re:Invent 2024 - Bridging from POC to production: Intro to
AgentCore (AIM2204)](https://www.youtube.com/watch?v=oDjESsByBmM)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-getting-started/en-US)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp01.html*

---

# AGENTOPS03-BP02 Implement CI/CD pipelines tailored to agentic system deployment (AgentOps)

Manual agent deployments and informal testing can keep a project
stuck in the pilot phase. An agent-aware pipeline, with behavioral
evaluation gates, staged rollout, and automated rollback can help
your organization realize the goal of daily deployment of behavioral
improvements.

**Desired outcome:**

- Agent deployments run fully through CI/CD with agent-specific
validation gates for prompt quality, tool integration
correctness, behavioral regression, and security.
- Deployment strategies (blue/green, canary) limit the scope of
impact when a regression does slip through.
- Automated rollback restores the previous version within minutes
if quality thresholds are exceeded.
- Infrastructure is defined as code so deployments are
reproducible and environments stay consistent.

**Common anti-patterns:**

- Deploying agent changes through manual console clicks or one-off
scripts without automated validation gates, making deployments
inconsistent and error-prone.
- Running only traditional unit tests without agent-specific
behavioral evaluation (prompt quality, tool selection accuracy,
hallucination rate), missing regressions that unit tests can't
detect.
- Deploying directly to production without staged rollout (canary,
blue/green), maximizing the scope of impact of any regression.
- Treating rollback as a theoretical capability that has never
been exercised, so the first time anyone uses it is during an
incident.

**Benefits of establishing this best
practice:**

- Automated pipelines help every deployment follow the same
validated path regardless of who starts it, reducing deployment
inconsistency.
- Behavioral validation gates provide empirical evidence that each
deployment meets quality standards before reaching production.
- Staged rollout and automated rollback compress incident response
time from hours to minutes when regressions appear.
- Infrastructure as code makes deployments reproducible across
environments, removing a common source of failures.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Agent CI/CD shares most of its structure with software CI/CD, with
one substantive addition: behavioral evaluation. The stages that
fit most agent workloads are:

- Source (code, prompts, configurations, and evaluation
datasets)
- Build (package artifacts and run unit tests)
- Evaluate (run behavioral evaluation through
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html))
- Security scan (prompt injection vulnerabilities and IAM scope)
- Deploy to production

Task completion accuracy, hallucination rate, and tool selection
accuracy need explicit thresholds that block promotion when
exceeded. Thresholds that are set too loose produce false passes,
but thresholds that are set too tight block legitimate iteration.
To calibrate, start with thresholds tuned to the current baseline,
then tighten them as the agent's quality track record grows.

Production deployment uses
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for managed scaling, versioning,
and observability. agentcore deploy pushes new
versions, and endpoint-based weighted routing handles blue/green
and canary patterns.
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms watch quality metrics post-deployment and
trigger automated rollback when thresholds are exceeded. The same
alarms that run during staged rollout double as rollback triggers.
Infrastructure as code through
[AWS CDK](https://aws.amazon.com/cdk/) or
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) helps make every resource reproducible.

A rollback procedure that has never been exercised is a procedure
that may not work when the team needs it. Deliberate rollback
drills during pipeline validation confirm the revert works before
the team is depending on it.

### Implementation steps

- **Build the pipeline
stages:** Configure source, build, behavioral
evaluation, security scan, and production deployment stages
with the appropriate tools for each.
- **Set behavioral evaluation as a
gate:** Integrate
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) with task completion accuracy and
hallucination rate thresholds that block promotion when
exceeded.
- **Deploy to
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html):** Use built-in
versioning and endpoint-based weighted routing for
blue/green or canary rollouts.
- **Automate rollback on quality
threshold exceedance:** Wire
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms to revert-deployment workflows so
quality threshold violations trigger immediate revert.
- **Version all deployment
artifacts:** Tag each artifact set with the
pipeline run ID for traceability, and store in a durable
versioned store.
- **Validate the full
pipeline:** Deliberately trigger a rollback during
pipeline validation to confirm revert procedures work before
they are needed for real.

## Resources

**Related best practices:**

- [AGENTOPS03-BP01 Define
an agent lifecycle with clear SME ownership, testing, and
governance](agentops03-bp01.html)
- [AGENTOPS02-BP03
Implement agent behavior versioning and rollback
capabilities](agentops02-bp03.html)
- [AGENTOPS06-BP03
Establish SME-driven validation and business approval
workflows](agentops06-bp03.html)
- [AGENTCOST06-BP02
Cost optimize versioning and deployment through efficient
artifact management](agentcost06-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [Deploy
AI agents on Amazon Bedrock AgentCore using GitHub
Actions](https://aws.amazon.com/blogs/machine-learning/deploy-ai-agents-on-amazon-bedrock-agentcore-using-github-actions/)
- [Strands
Agents](https://strandsagents.com/)
- [CI/CD
and automation for serverless AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html)
- [Kiro
Hooks](https://kiro.dev/docs/hooks/)

**Related videos:**

- [AWS 2025 - Deploy Production-Ready Agents in 22 Minutes with
AgentCore Runtime](https://www.youtube.com/watch?v=Q-tYIAuv9WI)
- [AWS 2025 - Deploy ANY AI Agent to Production in Minutes -
AgentCore Tutorial](https://www.youtube.com/watch?v=N7FGbBq1mI4)
- [AWS 2025 - Strands Agents Observability, Evaluation, &
Deployment](https://www.youtube.com/watch?v=VgN-6_tmQHE)
- [AWS re:Invent 2024 - Building AI Agents with Serverless, Strands,
and MCP (NTA405)](https://www.youtube.com/watch?v=LwubRSoJcIM)
- [AWS re:Invent 2024 - Develop AI Agents faster with SageMaker AI
Studio & AgentCore (AIM388)](https://www.youtube.com/watch?v=UL_7a2GEu10)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore, Lab 4: Deploy to
Production](https://catalog.workshops.aws/agentcore-getting-started/en-US/60-add-runtime)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp02.html*

---

# AGENTOPS03-BP03 Implement agent-specific scaling policies and capacity planning

Scaling policies designed for typical web workloads don't fit
agents. Model inference latency, tool dependency availability, and
downstream service capacity all shape the right response to load,
and a policy that ignores them either over-provisions during quiet
hours or under-provisions during peaks.

**Desired outcome:**

- Agent compute scales dynamically in response to demand while
respecting cost, performance, and governance constraints.
- Scaling decisions account for agent-specific factors: model
inference latency, tool availability, and downstream service
capacity.
- Per-environment scaling boundaries help prevent runaway scaling
in development while preserving capacity headroom in production.
- Monthly capacity reviews keep deployments right-sized as usage
patterns evolve.

**Common anti-patterns:**

- Using identical scaling configurations across all environments,
either over-provisioning development or under-provisioning
production during traffic spikes.
- Scaling based solely on CPU and memory utilization without
considering agent-specific metrics like request queue depth or
inference latency, missing the real bottleneck.
- Setting scaling policies once at deployment and never revisiting
them as usage patterns evolve.
- Treating capacity planning as a quarterly finance exercise
rather than an ongoing operational one, so policies fall out of
step with reality.

**Benefits of establishing this best
practice:**

- Scaling policies adapt to deployment context and agent compute
model, keeping capacity appropriate as workloads move from
prototype to production scale.
- Per-environment boundaries and centralized configuration make
scaling behavior consistent, auditable, and governed across
environments.
- Monthly reviews catch drift between configured capacity and
actual usage patterns before it becomes a cost or latency
problem.
- Agent-specific scaling metrics expose the real bottleneck, often
downstream service capacity or model throttling, that generic
metrics hide.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) handles the scaling question for
most teams through its built-in consumption-based scaling and
pricing model. AgentCore Runtime allocates compute automatically
based on demand, so custom scaling policies are not required. For
agents deployed outside AgentCore Runtime, on
[AWS Lambda](https://aws.amazon.com/lambda/) or
[Amazon ECS](https://aws.amazon.com/ecs/)
for example, scaling triggers must be configured against
agent-specific signals: request queue depth, average response
latency, and concurrent invocation count. CPU and memory alone
miss the mark because agents often wait on model inference or
downstream tools rather than saturating local compute.

Configure environment-appropriate maximums to control cost in
development and maintain performance in production. Development
can run with permissive minimums and tight maximums. Cost is the
first consideration, so the policy should expect spikes and
throttle them. In production, maximums should be generous enough
to absorb traffic bursts without latency degradation, and minimums
should hold enough warm capacity to avoid cold starts during
demand ramps. Staging is the midpoint between development and
production, so maximums and minimums should match that as well.

Store scaling configurations centrally (like in a parameter store
integrated with the agent registry) so boundaries adjust
automatically when an agent transitions between lifecycle stages.
A configuration store also gives the team a single place to audit
and adjust policies, instead of chasing them through individual
service consoles.

The operations team should perform monthly reviews, analyzing
scaling event history, peak utilization patterns, and capacity
headroom across the portfolio using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics. The outputs are concrete:

- Agents to scale down
- Agents to increase ceilings for
- Demand forecasts for the upcoming period

Without this review, scaling policies drift from the workload they
were tuned against. For fleet-level operational visibility
including dashboards, anomaly detection, and behavioral
monitoring, see
[AGENTOPS05-BP05
Create workflow-specific dashboards for operational health](agentops05-bp05.html).

### Implementation steps

- **Choose the right scaling
foundation:** Deploy agents on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for built-in scaling, or
configure auto scaling policies with agent-specific metrics
for non-Runtime deployments.
- **Set per-environment
boundaries:** Use permissive policies for
development, moderate for staging, and production with
higher minimums to absorb traffic spikes.
- **Centralize scaling
configurations:** Store policies in a parameter
store integrated with the agent registry so boundaries
adjust as agents transition between lifecycle stages.
- **Review capacity monthly:**
Analyze scaling events, peak utilization, and capacity
headroom in
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to right-size deployments and forecast
demand.

## Resources

**Related best practices:**

- [AGENTOPS03-BP01 Define
an agent lifecycle with clear SME ownership, testing, and
governance](agentops03-bp01.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTOPS02-BP02
Implement configuration drift detection and remediation](agentops02-bp02.html)
- [AGENTOPS05-BP04
Define and track KPIs for agent workflows](agentops05-bp04.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Preparing
the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [Introducing
Amazon Bedrock AgentCore: Securely deploy and operate AI
agents at any scale](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Securely
launch and scale your agents and tools on Amazon Bedrock
AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp03.html*

---

# AGENTOPS03-BP04 Implement organizational agent portfolio management and governance at scale

A handful of agents built by one team is a project. Dozens of agents
built by multiple teams is a portfolio, and portfolios need
different operational mechanisms. Without cross-organizational
visibility, teams build redundant agents, break each other's
integrations, and lose track of which agents still earn their keep.

**Desired outcome:**

- A centralized catalog gives the organization a current view of
every agent, owner, capabilities, dependencies, lifecycle state,
cost profile, and business value.
- Teams discover existing agents before building new ones, so
effort goes to capability gaps rather than duplicates.
- Cross-team dependencies are tracked and managed through
coordinated deprecation processes.
- Quarterly portfolio reviews reveal underutilized agents for
consolidation or retirement, keeping the portfolio aligned with
business priorities.

**Common anti-patterns:**

- Allowing teams to build agents independently without checking
for existing capabilities, creating redundant agents that
duplicate development cost, infrastructure cost, and operational
burden.
- Maintaining agent registries only within individual teams, so no
one has the cross-organizational view needed to identify
redundancy or assess overall system health.
- Deprecating or modifying agents without notifying dependent
teams, causing cascading failures when orchestrators or
delegating agents invoke agents that have changed.
- Treating agent creation as a no-justification-required activity,
so the portfolio grows faster than the organization's ability to
operate, monitor, and maintain it.
- Failing to measure business value relative to operational cost,
reducing the risk of data-driven decisions about which agents
warrant continued investment.

**Benefits of establishing this best
practice:**

- Portfolio governance scales operational practices from
individual agents to enterprise environments, so governance
overhead grows sub-linearly with agent count.
- A centralized catalog with ownership, dependency tracking, and
lifecycle state provides the auditable record needed for
compliance and organizational accountability.
- Capability search before build reduces redundant development,
freeing engineering effort for capability gaps.
- Quarterly reviews help prevent sprawl by revealing candidates
for consolidation and retirement before the portfolio becomes
unmanageable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Portfolio governance extends the team-level registry into an
organizational catalog that spans team boundaries (for more
detail, see [AGENTOPS03-BP01
Define an agent lifecycle with clear SME ownership, testing, and
governance](agentops03-bp01.html)). The fields added at this layer are the ones
that support cross-team decisions:

- Owning team
- Business domain
- Upstream dependencies (agents or systems that invoke this
agent)
- Downstream dependencies (agents, tools, or services this agent
invokes)
- Cost-per-month (derived from CloudWatch and Cost Explorer)
- Business value indicators (task completion volume, business
outcome metrics).

[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides the centralized catalog with
built-in approval workflows, flexible metadata, and hybrid search
(semantic and keyword) so cross-organizational queries run
efficiently. Enrich registry records with dependency metadata,
cost attribution, and business value indicators so the catalog
supports portfolio-level decisions beyond simple discovery.

The pre-creation review gate helps prevent duplicate builds. Teams
searching for specific agents by purpose will not find one through
keyword matching against agent names.
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides built-in hybrid search that
combines semantic understanding with keyword matching, so
natural-language capability queries reveal existing agents with
overlapping capabilities. When overlap exists, the requesting team
documents why the existing agent is insufficient before
proceeding.

This applies to code-based agents (Strands Agents, LangGraph) and
no-code agents built through
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/) alike. A lightweight CI/CD gate that checks the
registry and flags potential duplicates is enough for most
organizations, while heavy approval processes encourage bypass.

Implement cross-team dependency tracking as a managed practice.
Agents declare their upstream and downstream dependencies at
registration and update declarations when dependencies change.
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) publishes events when agents are deprecated,
modified, or decommissioned so downstream teams receive advance
notice. Agents exposed through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) benefit from Gateway's tool
registration metadata, which automatically tracks which agents
consume which tools and reduces manual declaration burden. A
dependency graph in
[Amazon Neptune](https://aws.amazon.com/neptune/) enables impact analysis for determining how a
change to one agent will affect others.

Quarterly portfolio reviews help prevent gradual drift. The review
assesses four dimensions:

- Utilization (which agents are actively used and which are
idle)
- Cost efficiency (which agents deliver business value
proportional to cost)
- Redundancy (which agents overlap with others)
- Health (which agents show elevated error rates, degraded
performance, or stale configurations)

The catalog is the primary data source, enriched with
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics,
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) attribution, and the dependency graph.
Reviews produce concrete recommendations. These include agents to
consolidate, deprecate, or invest in, and cross-team dependency
risks to address.

### Implementation steps

- **Extend the agent registry into an
organizational catalog:** Use
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) to catalog agents with metadata for
owning team, business domain, upstream and downstream
dependencies, cost-per-month, and business value indicators.
- **Enable semantic capability
search:** Use Agent Registry's built-in hybrid
search so natural-language queries reveal overlapping
capabilities before new development begins.
- **Gate new agent creation on registry
search:** Add a pre-creation CI/CD check that
requires justification when overlapping agents exist.
- **Track cross-team
dependencies:** Use
[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to notify downstream teams when upstream
agents are deprecated, modified, or decommissioned.
- **Build a dependency graph:**
Use
[Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html) to answer impact-analysis questions before
agent modifications.
- **Run quarterly portfolio
reviews:** Assess utilization, cost efficiency,
redundancy, and health, producing specific recommendations
for consolidation, deprecation, and investment.

## Resources

**Related best practices:**

- [AGENTOPS03-BP01 Define
an agent lifecycle with clear SME ownership, testing, and
governance](agentops03-bp01.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTOPS04-BP01
Implement tool registry and catalog management](agentops04-bp01.html)
- [AGENTOPS05-BP04
Define and track KPIs for agent workflows](agentops05-bp04.html)
- [AGENTCOST06-BP01
Implement lightweight discovery and registry for
cost-effective collaboration](agentcost06-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Preparing
the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [AI
agents in enterprises: Best practices with Amazon Bedrock
AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)

**Related videos:**

- [AWS re:Invent 2024 - Agents in the enterprise: Best practices with
AgentCore (AIM3310)](https://www.youtube.com/watch?v=w5XJxCpUADY)
- [AWS 2025 - AgentCore Registry: Discover, Govern, and Reuse AI
Agents at Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk)
- [AWS re:Invent 2024 - Cox Automotive's Blueprint for Agentic AI on
AgentCore (IND3329)](https://www.youtube.com/watch?v=ICA8-d_Nt9Q)

**Related services:**

- [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon Neptune](https://aws.amazon.com/neptune/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp04.html*

---

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

# AGENTOPS06 — Testing, evaluation, and validation frameworks

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# AGENTOPS06-BP01 Design multi-layered testing frameworks

Traditional software testing, like exact-match assertions and
green-or-red unit tests, can miss important failure modes in agentic
systems. A testing pyramid that covers unit, integration, end-to-end
tests, and shadow layers helps teams catch behavioral regressions
before they reach users.

**Desired outcome:**

- Agent systems are covered by a testing pyramid that includes
unit tests, integration tests, end-to-end tests, and shadow
tests in production environments.
- Automated testing pipelines run on every code and configuration
change, providing rapid feedback on regressions.
- Test coverage metrics are tracked and maintained above defined
thresholds for all agent capabilities.
- Tests use semantic quality assessment rather than exact-match
comparison, so non-deterministic outputs don't break the suite.

**Common anti-patterns:**

- Testing only the happy path without covering edge cases, error
conditions, and adversarial inputs.
- Relying exclusively on unit tests without integration and
end-to-end tests, missing failures that only emerge when
components interact with real tools and services.
- Treating agent testing as equivalent to traditional software
testing without accounting for non-deterministic LLM outputs,
using exact string matching instead of semantic equivalence
checks.
- Running tests only in isolated environments without shadow
testing in production, missing environment-specific behaviors
that only manifest with real data and traffic patterns.
- Failing to maintain test datasets as capabilities evolve, so
tests become stale and lose regression-detection value.

**Benefits of establishing this best
practice:**

- A thorough testing framework provides the empirical evidence
needed to validate each behavioral iteration, enabling confident
deployment.
- Standardized testing procedures help validate every change
consistently, regardless of who made it or how urgent the
timeline.
- Semantic evaluation accepts legitimate output variation while
still catching regressions.
- Shadow testing validates behavioral changes against real traffic
without exposing users to the new version.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Four layers cover the testing surface for most agent systems.

Unit tests, the base layer, test individual components in
isolation: prompt templates, tool invocation logic, memory
retrieval, decision routing. LLM responses can be mocked where
determinism is needed, so unit tests stay fast and reproducible.

Integration tests, the second layer, validate agent-tool and
agent-to-agent interactions in a staging environment with real
endpoints, which is where many of the interesting failures emerge.

End-to-end tests, the third layer, validate complete workflows,
and this is where semantic evaluation matters more than exact
matching.
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) handle the semantic quality
assessment that end-to-end tests need. AgentCore Evaluations' 13
built-in evaluators provide standardized quality gates in CI/CD
pipelines (correctness, helpfulness, safety, and tool selection
accuracy), so regressions in output quality are detectable without
requiring bit-exact comparison. Custom evaluators cover
business-specific requirements.

Shadow tests, the top layer, run new versions in parallel with
production on real traffic using traffic mirroring, comparing
outputs without serving the new version's responses. This catches
environment-specific behavior that staging can't reproduce. The
cost is the infrastructure to run parallel inferences, and the
value is catching issues before users ever encounter them. For
teams developing agents with Kiro, hooks can trigger test runs on
file save and before deployment.

Integrate automated testing into CI/CD pipelines so every layer
blocks deployment on failure. Maintain test datasets with
versioning, and review them regularly to add new use cases and
failure modes discovered in production. The pyramid gets stronger
over time only if the suite grows with the system.

### Implementation steps

- **Define the four testing
layers:** Scope, tooling, and success criteria for
unit, integration, end-to-end, and shadow tests.
- **Implement unit and integration
tests:** Mock dependencies at the unit layer. Use
real staging endpoints for integration tests.
- **Create end-to-end scenarios with
semantic evaluation:** Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) for quality assessment
rather than exact-match assertions.
- **Add shadow testing with traffic
mirroring:** Validate behavioral changes against
real-world inputs without exposing users.
- **Integrate tests into
CI/CD:** Run the full suite on every commit and
block deployment on failures.

## Resources

**Related best practices:**

- [AGENTOPS06-BP02 Evaluate
and track ongoing agent performance](agentops06-bp02.html)
- [AGENTOPS06-BP03
Establish SME-driven validation and business approval
workflows](agentops06-bp03.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTPERF01-BP01
Define performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)
- [LLM-as-a-judge
on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Evaluating
AI agents for production: A practical guide to Strands
Evals](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-for-production-a-practical-guide-to-strands-evals/)
- [From
AI agent prototype to product: Lessons from building AWS
DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent)
- [Kiro
Hooks](https://kiro.dev/docs/hooks/)

**Related videos:**

- [AWS 2025 - Strands Agents Observability, Evaluation, &
Deployment](https://www.youtube.com/watch?v=VgN-6_tmQHE)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples, Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)
- [GitHub:
awslabs/amazon-bedrock-agent-samples, RAGAS evaluation](https://github.com/awslabs/amazon-bedrock-agent-samples/tree/main/examples/agents/ragas_evaluation_bedrock_agents)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore, Lab 5: Evaluate Agent
Performance](https://catalog.workshops.aws/agentcore-getting-started/en-US/65-evaluation)
- [Diving
Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06-bp01.html*

---

# AGENTOPS06-BP02 Evaluate and track ongoing agent performance

Pre-deployment evaluation validates that an agent is ready to ship.
Post-deployment evaluation validates that it still works. Without
continuous assessment, gradual quality degradation from data drift,
model updates, and shifting user patterns goes unnoticed until it is
expensive to fix.

**Desired outcome:**

- Agent performance is continually evaluated against defined
quality benchmarks.
- Automated pipelines detect degradation in output quality,
reasoning accuracy, and business outcome alignment.
- Teams have clear visibility into performance trends over time
and can correlate quality changes with specific configuration,
model, or data updates.
- Evaluation results drive prioritized improvement actions and
provide objective evidence for stakeholder reporting.

**Common anti-patterns:**

- Evaluating agent performance only at deployment time without
continuous post-deployment assessment, missing gradual
degradation from data drift, model updates, or changing user
patterns.
- Relying solely on automated metrics without periodic human
evaluation, missing quality dimensions that automated metrics
can't fully capture (like nuance, appropriateness, and business
context alignment).
- Using generic evaluation criteria across all agents without
tailoring metrics to each agent's specific use case and business
objectives, producing evaluation results that don't reflect
actual value.
- Treating evaluation as separate from operations rather than
integrating it into the operational workflow, creating
evaluation debt that accumulates over time.

**Benefits of establishing this best
practice:**

- Continuous evaluation provides an empirical foundation for
evidence-based improvement, identifying which agents need
attention and which changes produce measurable gains.
- Performance trend tracking reveals patterns that inform
systematic improvement, turning evaluation data into practical
insights.
- Multi-dimensional scoring catches quality issues that a single
metric would miss.
- Correlation between quality shifts and configuration changes
compresses root-cause analysis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) is an evaluation service for
continuous assessment. Its on-demand mode runs benchmarks during
development, and its online mode samples and evaluates live
interactions in production without requiring manual triggers.
Thirteen built-in evaluators cover correctness, helpfulness,
safety, and tool selection accuracy, with custom evaluators
available for business-specific requirements.
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) supplements this with model-level
assessment, and periodic human evaluation covers the dimensions
automated metrics miss.

Evaluation frameworks need multiple dimensions because a single
metric misses too much. For example:

- Output quality (relevance, accuracy, coherence) measures
whether responses are good.
- Safety (hallucination rate, toxicity, guardrail adherence)
measures whether responses are safe.
- Efficiency (task completion rate, tool invocation success)
measures whether the agent is economical.
- Business alignment (outcome achievement, user satisfaction,
SLA compliance) measures whether the agent delivers value.

Weighting depends on the use case. For instance, a
customer-support agent might weigh satisfaction higher than
efficiency, while an internal automation agent might weigh
efficiency higher than relevance. Generic weighting produces
generic results.

Dashboards that show evaluation scores over time make degradation
visible before it becomes an incident. Alerting on threshold
violations and on persistent negative trends, as opposed to
single-point dips, catches the slow-moving problems that are
hardest to diagnose after the fact. Correlate evaluation shifts
with configuration and model changes so attribution is fast when a
metric moves.

LLM-as-a-Judge patterns can use multiple evaluator prompts
covering different quality dimensions to produce a composite score
that is more reliable than any single prompt. Periodic human
review validates the automated scores and catches the blind spots.

### Implementation steps

- **Configure
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html):** Use
on-demand mode for development benchmarking and online mode
for continuous production monitoring.
- **Define a multi-dimensional
evaluation framework:** Apply use-case-specific
weighting across quality, safety, efficiency, and business
alignment.
- **Implement LLM-as-judge
patterns:** Use multiple evaluator prompts and
supplement with periodic human evaluation.
- **Build evaluation
dashboards:** Show trends over time with alerting
for threshold violations and persistent negative trends.
- **Correlate evaluation results with
change events:** Tag deployments, configuration
updates, and model changes so quality shifts can be
attributed quickly.

## Resources

**Related best practices:**

- [AGENTOPS06-BP01 Design
multi-layered testing frameworks](agentops06-bp01.html)
- [AGENTOPS06-BP03
Establish SME-driven validation and business approval
workflows](agentops06-bp03.html)
- [AGENTOPS02-BP04
Maintain feedback control loops for continuous
improvement](agentops02-bp04.html)
- [AGENTOPS05-BP04
Define and track KPIs for agent workflows](agentops05-bp04.html)
- [AGENTPERF01-BP01
Define performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Build
reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [LLM-as-a-judge
on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)
- [Evaluating
AI agents for production: A practical guide to Strands
Evals](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-for-production-a-practical-guide-to-strands-evals/)
- [From
AI agent prototype to product: Lessons from building AWS
DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore, Lab 5: Evaluate Agent
Performance](https://catalog.workshops.aws/agentcore-getting-started/en-US/65-evaluation)
- [Diving
Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06-bp02.html*

---

# AGENTOPS06-BP03 Establish SME-driven validation and business approval workflows

Heavy approval processes slow routine work and get bypassed in
emergencies. On the other hand, a lack of approval processes can
produce unforeseen incidents. To keep your teams moving while
protecting against the changes that actually warrant scrutiny,
implement risk-tiered validation (light for minor changes, thorough
for autonomy increases).

**Desired outcome:**

- Significant agent changes pass through documented validation and
approval workflows before reaching production.
- Validation checkpoints verify that changes meet quality
thresholds, maintain behavioral alignment, and comply with
operational boundaries.
- Rollback procedures are defined and tested for every change
type.
- Approval burden scales with change risk, not uniformly across
all changes.

**Common anti-patterns:**

- Applying the same lightweight approval process to all changes
regardless of risk, treating a minor prompt wording adjustment
the same as a change that increases agent autonomy or adds new
tool access.
- Implementing approval workflows that require human sign-off for
every change without risk-based tiering, creating bottlenecks
that slow iteration and incentivize bypass.
- Defining validation checkpoints without specifying the criteria
that must be met to pass, leaving approvers without objective
standards and producing inconsistent decisions.
- Failing to test rollback procedures before they are needed,
discovering that rollback is broken only when an incident
requires rapid recovery.
- Treating validation as a one-time deployment gate rather than a
continuous process, missing quality degradation after
deployment.

**Benefits of establishing this best
practice:**

- Risk-tiered approval workflows help route changes with
significant potential impact to appropriate human scrutiny,
while low-risk changes proceed with minimal friction.
- Documented validation and approval create an auditable record of
every change decision for compliance purposes.
- Tested rollback procedures compress incident response time when
validated changes still produce unexpected outcomes.
- Automated validation gates catch regressions before human
approvers ever see the change.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Risk tiering creates a workable approval process.

- Tier 1, low risk, covers minor prompt wording changes, logging
configuration adjustments, and similar edits that can't
materially alter agent behavior. These require automated
validation only.
- Tier 2, medium risk, covers new tool integrations, prompt
structural changes, and model parameter adjustments. These
require automated validation plus peer review.
- Tier 3, high risk, covers autonomy level increases, new tool
categories, model changes, and guardrail modifications. These
require automated validation plus multi-stakeholder approval
including technical lead and business owner.

Automated validation should run before any human approval.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) score thresholds, behavioral
regression tests, security scans, and performance benchmarks all
gate promotion. A change that fails automated validation never
consumes human review time, as the team stays focused on the
decisions that genuinely require judgment.

Approval routing needs to handle timeouts. A change waiting on an
unavailable approver for multiple days risks being bypassed or
dropped. Timeout escalation, either through automatic approval for
low-risk changes or escalation to a backup approver for
higher-risk ones, keeps the process moving.

Rollback is a recovery path for changes that passed validation and
still produced unexpected outcomes. Automated rollback triggered
by post-deployment quality threshold violations is the default,
while manual rollback remains available for edge cases. For tiered
human oversight patterns in reliability contexts, see
[AGENTREL02-BP05
Establish tiered human oversight and approval workflows](agentrel02-bp05.html).

### Implementation steps

- **Define a risk-tiered change
classification:** Spell out the criteria for Tier
1, Tier 2, and Tier 3 so changes are classified
consistently.
- **Define automated validation
checkpoints:** Include evaluation score thresholds
from
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html), regression tests,
security scans, and performance benchmarks.
- **Implement approval
workflows:** Route changes by tier with timeout
escalation for non-responsive approvers.
- **Automate rollback on quality
threshold exceedance:** Wire post-deployment
quality metrics to revert workflows.
- **Test rollback procedures
quarterly:** Document results and update procedures
as the runtime evolves.

## Resources

**Related best practices:**

- [AGENTOPS06-BP01 Design
multi-layered testing frameworks](agentops06-bp01.html)
- [AGENTOPS06-BP02 Evaluate
and track ongoing agent performance](agentops06-bp02.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTREL02-BP05
Establish tiered human oversight and approval workflows](agentrel02-bp05.html)
- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Operationalizing
agentic AI, Part 1: A stakeholder's guide](https://aws.amazon.com/blogs/machine-learning/operationalizing-agentic-ai-part-1-a-stakeholders-guide/)
- [Preparing
your business for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [Advancing
AI agent governance with Boomi and AWS: A unified approach to
observability and compliance](https://aws.amazon.com/blogs/machine-learning/advancing-ai-agent-governance-with-boomi-and-aws-a-unified-approach-to-observability-and-compliance)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06-bp03.html*

---

# AGENTOPS07 — Operational recovery and consumption monitoring

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# AGENTOPS07-BP01 Implement automated response and recovery mechanisms

Agents that recover from failure without human intervention keep
service running and give the team the failure data they need to help
prevent recurrence. Manual-only recovery scales poorly and can turn
routine degradations into incidents.

**Desired outcome:**

- Agent systems detect and recover from common failure scenarios
automatically, maintaining service availability and user
experience continuity.
- Automatic cutoffs help prevent cascading failures from
propagating across the agent environment.
- Fallback strategies keep agents degrading gracefully rather than
failing completely when primary capabilities are unavailable.
- Recovery time objectives are defined, met, and tested regularly.

**Common anti-patterns:**

- Implementing retry logic without automatic cutoffs, causing
agents to repeatedly invoke failing services and amplifying load
on degraded systems rather than failing fast.
- Designing fallback strategies that silently degrade quality
without notifying users, producing a poor experience where users
receive low-quality responses without understanding why.
- Failing to define recovery time objectives for different failure
scenarios, making it impossible to assess whether recovery
mechanisms meet operational requirements.
- Implementing recovery mechanisms that work in isolation but fail
in combination, missing failure scenarios where multiple
components degrade simultaneously.
- Never testing recovery procedures under realistic failure
conditions, discovering problems only during actual production
incidents.

**Benefits of establishing this best
practice:**

- Automated recovery captures detailed failure data that drives
systematic improvement of agent resilience, letting teams
address root causes rather than repeatedly responding to the
same incidents.
- Self-healing capabilities adapt to different failure contexts,
transient tool unavailability, complete service outages, and
model degradation, with recovery strategies proportional to
severity.
- Automatic cutoffs break cascading failures at the source rather
than allowing them to propagate.
- Chaos engineering exercises validate that recovery works under
realistic conditions, not just in theory.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establish automatic cutoffs for every external dependency. Store
state for the cutoff (healthy, degraded, and open) in a fast data
store where every agent can read it. Thresholds depend on each
dependency's reliability characteristics. Set an error rate
threshold (for example, 50% errors in a 60-second window), a
timeout threshold (for example, 5 consecutive timeouts), and a
recovery probe interval (for example, attempt recovery every 30
seconds). Emit
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics on state transitions so cutoff health
becomes visible across the environment.

Fallback strategies need to be designed for each capability, not
copied from a template. Tool failures get fallback chains:
alternative tools with equivalent capabilities, then graceful
degradation, and then manual escalation. LLM inference failures
get model fallback chains that route to alternative models (Claude
3.5 Sonnet to Claude 3 Haiku, for example) when the primary is
unavailable. Multi-agent coordination failures get single-agent
fallback modes that handle tasks with reduced capability rather
than failing completely. Each fallback should notify users when
quality is degraded, not silently return a worse answer.

[AWS Step Functions](https://aws.amazon.com/step-functions/) or equivalent durable workflow orchestration
handles recovery workflows with built-in error handling, retry
logic, and compensating transactions. Health check endpoints for
each agent verify dependency availability and report overall
health status.

Monitoring actual recovery times against objectives tells the team
whether the mechanisms actually meet operational requirements.
Quarterly chaos engineering exercises validate that recovery works
under realistic conditions rather than just in the happy-path
scenarios the original design anticipated. For reliability-focused
automated recovery with classify-route-escalate patterns, see
[AGENTREL07-BP02
Enable automatic recovery from agent execution failures](../../reliability-pillar/agentrel07/agentrel07-bp02.xml).

### Implementation steps

- **Implement automatic cutoffs for
every external dependency:** Define thresholds for
error rate, timeout count, and recovery probing per
dependency.
- **Design fallback chains per agent
capability:** Specify alternative tools, models,
and degraded-mode operations, and notify users when quality
is degraded.
- **Build durable recovery
workflows:** Use
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) or equivalent with error handling,
retry logic, and compensating transactions.
- **Configure health check
endpoints:** Verify dependency availability and
report overall health status for each agent.
- **Define RTOs per failure
scenario:** Monitor actual recovery times against
objectives in
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).
- **Run quarterly chaos engineering
exercises:** Inject failures in non-production
environments to validate recovery mechanisms under realistic
conditions.

## Resources

**Related best practices:**

- [AGENTOPS07-BP03 Augment
change management to accommodate technical improvements and
business requirements](agentops07-bp03.xml)
- [AGENTOPS04-BP03
Develop fallback behavior and error handling for tool
invocations](../agentops04/agentops04-bp03.xml)
- [AGENTOPS05-BP02
Monitor agent behavior patterns and detect anomalies](../agentops05/agentops05-bp02.xml)
- [AGENTREL07-BP02
Enable automatic recovery from agent execution failures](../../reliability-pillar/agentrel07/agentrel07-bp02.xml)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Agentic
AI in the Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html)
- [From
AI agent prototype to product: Lessons from building AWS
DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent)
- [Introducing
Amazon Bedrock AgentCore: Securely deploy and operate AI
agents at any scale](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops07-bp01.html*

---

# AGENTOPS07-BP02 Establish operational knowledge management systems

Teams that capture what they learn from incidents build
institutional memory that survives personnel changes. Teams that
don't lose the insight the moment the person who had it leaves, and
pay the same lesson twice.

**Desired outcome:**

- Operational knowledge about agent behavior, failure modes, and
resolution procedures is captured systematically and accessible
to all team members.
- Post-incident reviews consistently produce practical insights
incorporated into runbooks and operational procedures.
- Institutional knowledge survives personnel changes, enabling new
team members to become effective quickly.
- Knowledge about successful interventions is captured alongside
failure modes, so what works is remembered as reliably as what
failed.

**Common anti-patterns:**

- Relying on knowledge held by individual team members rather than
documented operational knowledge, creating single points of
failure when people leave.
- Conducting post-incident reviews that produce reports but don't
result in practical changes to runbooks or procedures.
- Storing operational knowledge in team-specific repositories
inaccessible to other teams, reducing the risk of sharing and
creating duplicate effort.
- Treating knowledge management as a documentation exercise rather
than an active operational practice, producing documents that
are created once and never updated.
- Failing to capture knowledge about successful interventions
alongside failure modes, missing the opportunity to document
what works and why.

**Benefits of establishing this best
practice:**

- A systematic knowledge management system captures individual
operational experience as organizational learning, making the
whole team more effective over time.
- Documented operational knowledge enables consistent responses to
common scenarios, reducing variability in how team members
handle similar situations.
- Semantic search exposes relevant knowledge even when users don't
know exact document names or categories.
- Quarterly audits keep the knowledge base current as systems and
procedures evolve.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A centralized knowledge repository is the starting point, but the
search experience decides whether anyone uses it.
[Amazon
Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) provides semantic search over
operational documentation, so natural-language queries return
relevant entries even when users don't know the exact title.
Structure the knowledge base with categories for agent behavioral
patterns, common failure modes and resolutions, operational
procedures, and post-incident learnings. Amazon Bedrock
retrieval-augmented generation turns the knowledge base into
something queryable through natural language rather than keyword
matching.

Structured, post-incident reviews that capture timeline, root
cause, resolution steps, and preventive measures convert each
significant incident into durable knowledge. Tie review outputs
directly to knowledge base entries so that a new failure mode gets
documented the same week it was diagnosed.

Quarterly audits validate accuracy and completeness. Agent
behaviors change, services evolve, and procedures that worked last
year may no longer apply. Without periodic validation, the
knowledge base slowly becomes less trustworthy. Consider building
an internal operational assistant using
[Amazon
Bedrock Agents](https://aws.amazon.com/bedrock/agents/) that team members can query for guidance on
common scenarios. This is especially valuable for onboarding and
for incident response when timely guidance matters more than
document discovery.

### Implementation steps

- **Deploy a centralized knowledge
repository:** Use
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for semantic search over
operational documentation.
- **Define categories and
templates:** Cover behavioral patterns, failure
modes, procedures, and post-incident learnings with
consistent structure.
- **Establish a post-incident review
process:** Use structured templates that feed
directly into the knowledge base so learning captured during
review lands as durable knowledge.
- **Implement contribution
workflows:** Make it straightforward for team
members to add and update entries without heavy process
overhead.
- **Audit quarterly:** Review
accuracy, completeness, and relevance, and retire outdated
entries.

## Resources

**Related best practices:**

- [AGENTOPS07-BP03 Augment
change management to accommodate technical improvements and
business requirements](agentops07-bp03.xml)
- [AGENTOPS05-BP03
Implement structured logging and comprehensive audit
trails](../agentops05/agentops05-bp03.xml)
- [AGENTOPS02-BP04
Maintain feedback control loops for continuous
improvement](../agentops02/agentops02-bp04.xml)
- [AGENTCOST07-BP03
Create systematic optimization feedback loops for continuous
improvement](../../cost-optimization-pillar/agentcost07/agentcost07-bp03.xml)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)
- [Preparing
your business for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [Introducing
Amazon Bedrock AgentCore: Securely deploy and operate AI
agents at any scale](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon S3](https://aws.amazon.com/s3/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops07-bp02.html*

---

# AGENTOPS07-BP03 Augment change management to accommodate technical improvements and business requirements

A change management process built only for technical changes doesn't
account for how agents actually evolve. Prompt tweaks, tool
additions, and model upgrades all carry business implications that
pure technical review doesn't catch. A process that engages both
technical and business stakeholders, proportional to change scope,
keeps agents aligned with the objectives they exist to serve.

**Desired outcome:**

- Every agent change, technical improvement or business
requirement follows a documented change management process.
- Technical and business stakeholders are engaged appropriately
based on change scope and impact.
- The business justification for each change is documented and
traceable, so agent evolution is purposeful.
- Agents evolve in sync with organizational changes rather than
drifting out of alignment.

**Common anti-patterns:**

- Managing agent changes through purely technical change
management processes without business stakeholder involvement,
allowing agents to drift out of alignment with business
objectives.
- Treating all agent changes as technical changes without
assessing business impact, missing changes that affect business
processes, customer experience, or compliance requirements.
- Implementing change management processes so heavyweight that
teams bypass them for urgent changes, creating an informal
shadow process that lacks governance and traceability.
- Failing to synchronize agent changes with broader organizational
changes (like process updates, policy changes, and regulatory
updates), causing agents to operate based on outdated business
rules.

**Benefits of establishing this best
practice:**

- Documented change management with business justification creates
an auditable record of purposeful, governed agent evolution.
- Change management captures business justification and impact
assessment, creating a feedback loop that informs future
prioritization.
- Two-dimensional classification (technical scope, business
impact) helps the right stakeholders engage with the right
changes rather than everyone reviewing everything.
- Synchronization with organizational changes helps prevent agents
from operating under outdated business rules.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Classifying changes along two dimensions, technical scope and
business impact, helps keep your processes proportional.

Technical scope captures what kind of change it is, like prompt
update, tool change, model change, or architecture change.
Business impact captures what it affects, like none, minor
adjustment, significant process change, or compliance-affecting.
The combination determines required approval workflows,
documentation depth, and testing rigor. A prompt wording tweak
with no business impact moves through the process quickly, while a
new tool integration with compliance implications triggers the
full review.

Business alignment reviews help you catch slow configuration
drift. Agent capabilities that worked when the business process
was X may not work when the business process is Y, and if no one
periodically validates the alignment, the drift accumulates
unnoticed. A periodic review, for example quarterly, validates
whether agent capabilities remain aligned with current business
processes, policies, and regulatory requirements. Establish a
review mechanism where an agent-to-business-process mapping
maintained in the portfolio catalog, with notifications routed to
dependent agent owners when business processes are updated.

Tracking change volume, approval cycle times, and alignment
metrics keeps the process itself under observation for continual
improvement. Processes that take too long or catch too few
problems should be reviewed and updated as needed. Monitoring the
metrics validates the current tiering.

### Implementation steps

- **Define a change classification
matrix:** Map technical scope and business impact
to required approvals and documentation.
- **Implement change request
workflows:** Use structured templates capturing
both technical and business justification.
- **Establish periodic business
alignment reviews:** Validate that agent
capabilities match current business processes, policies, and
regulatory requirements.
- **Maintain agent-to-business-process
mappings:** Configure notifications when processes
are updated so dependent agents can be reviewed.
- **Track change management
metrics:** Monitor change volume, approval cycle
times, and alignment measures to keep the process
proportional.

## Resources

**Related best practices:**

- [AGENTOPS07-BP01
Implement automated response and recovery mechanisms](agentops07-bp01.xml)
- [AGENTOPS07-BP02
Establish operational knowledge management systems](agentops07-bp02.xml)
- [AGENTOPS06-BP03
Establish SME-driven validation and business approval
workflows](../agentops06/agentops06-bp03.xml)
- [AGENTOPS03-BP01
Define an agent lifecycle with clear SME ownership, testing,
and governance](../agentops03/agentops03-bp01.xml)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [Operationalizing
agentic AI, Part 1: A stakeholder's guide](https://aws.amazon.com/blogs/machine-learning/operationalizing-agentic-ai-part-1-a-stakeholders-guide/)
- [Advancing
AI agent governance with Boomi and AWS: A unified approach to
observability and compliance](https://aws.amazon.com/blogs/machine-learning/advancing-ai-agent-governance-with-boomi-and-aws-a-unified-approach-to-observability-and-compliance)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops07-bp03.html*

---

# AGENTOPS07-BP04 Implement break-glass operational runbooks

Write and test emergency runbooks before they are needed. Rehearsed
manual fallback procedures, accessible escalation paths, and current
contact information turn a complete agent failure into a brief
manual period rather than a prolonged outage.

**Desired outcome:**

- When agents fail completely or behave unexpectedly, human
operators execute well-documented manual procedures that
maintain business continuity.
- Break-glass runbooks are tested regularly, and operators are
trained and confident in the manual procedures.
- Escalation paths and contact information stay current.
- Emergency response times meet defined objectives because
procedures are documented, accessible, and practiced.

**Common anti-patterns:**

- Assuming agent systems will always be available and not
documenting manual fallback procedures, leaving operators
without guidance when agents fail during critical business
operations.
- Creating break-glass runbooks once and never testing or updating
them, resulting in procedures that reference outdated systems,
incorrect contacts, or steps that no longer work.
- Storing emergency procedures in locations inaccessible during
the outage scenarios they are designed to address (for example,
in systems that depend on the failing agent infrastructure).
- Designing manual fallback processes that require specialized
knowledge held by only one or two team members, creating single
points of failure in emergency response.
- Failing to define clear triggers for when break-glass procedures
should be activated, causing delays as operators debate whether
the situation warrants manual intervention.

**Benefits of establishing this best
practice:**

- Documented break-glass procedures support consistent emergency
responses regardless of who is on call.
- Break-glass runbooks formalize the transition from automated
agent operations to human-driven processes, keeping business
continuity intact when agent systems can't function.
- Regular drills keep procedures current and operators ready, so
response quality doesn't depend on which person happens to be on
call.
- Clear activation triggers remove hesitation that delays
response.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Inventory your system by identifying every critical business
process that depends on agent systems and assess the impact of
agent unavailability for each. The output is a ranked list of
processes that need break-glass coverage, from brief
inconveniences to service-stopping issues. Processes at the top of
the list get runbooks first.

Each runbook should cover trigger conditions, step-by-step manual
execution instructions, required access credentials, escalation
contacts with primary and backup personnel, expected completion
times, and criteria for returning to automated operations. The
most common failure mode, and the most dangerous, is runbooks
stored in systems that depend on the very infrastructure they are
designed to work around. An emergency runbook stored in a wiki
that depends on the same agent infrastructure is a runbook you
can't read during the outage. Store runbooks in a highly
available, agent-independent location, with offline copies
accessible to on-call operators.

Single-person knowledge is the other common single point of
failure. Designing manual procedures that only one or two people
can execute produces a plan that collapses when those people are
unavailable. Broaden the knowledge base through tabletop
exercises, documentation that doesn't assume expertise, and
regular cross-training.

Activation triggers remove hesitation from response. Clear
conditions, for example, "agent error rate exceeds 50% for
15 minutes" or "complete agent infrastructure
unavailability for 5 minutes", tell operators when to
switch to manual procedures without waiting for judgment calls
under pressure. Automated alerts that explicitly name the trigger
conditions they have met make the decision obvious.

Testing keeps runbooks alive. Tabletop exercises quarterly,
operators walking through runbook steps without executing them,
catch outdated references and missing steps. Full drills
semi-annually, operators actually executing manual procedures in a
non-production environment, catch everything tabletop exercises
miss. Drill results become input for runbook revisions, not just
training feedback.

### Implementation steps

- **Inventory critical business
processes:** Assess the impact of agent
unavailability for each to produce a ranked list.
- **Document manual fallback
procedures:** Cover each critical process assuming
no agent system availability, with step-by-step
instructions.
- **Establish escalation
paths:** Include primary and backup contacts, with
a process for keeping contact information current.
- **Store runbooks
independently:** Use a highly available,
agent-independent location with offline copies accessible to
on-call operators.
- **Define clear activation
triggers:** Configure automated alerts that notify
operators when trigger conditions are met.
- **Conduct exercises on a
cadence:** Run tabletop exercises quarterly and
full drills semi-annually, and update procedures based on
findings.

## Resources

**Related best practices:**

- [AGENTOPS07-BP01
Implement automated response and recovery mechanisms](agentops07-bp01.xml)
- [AGENTOPS07-BP02
Establish operational knowledge management systems](agentops07-bp02.xml)
- [AGENTOPS07-BP03 Augment
change management to accommodate technical improvements and
business requirements](agentops07-bp03.xml)
- [AGENTOPS04-BP03
Develop fallback behavior and error handling for tool
invocations](../agentops04/agentops04-bp03.xml)
- [AGENTREL07-BP02
Enable automatic recovery from agent execution failures](../../reliability-pillar/agentrel07/agentrel07-bp02.xml)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)
- [Agentic
AI in the Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html)
- [From
AI agent prototype to product: Lessons from building AWS
DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent)

**Related services:**

- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops07-bp04.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
