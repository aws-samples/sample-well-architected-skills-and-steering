# AGENTSUS03 — Agent governance

**Pillar**: Sustainability  
**Best Practices**: 4

---

# AGENTSUS03-BP01 Maintain organizational skills and competencies

Organizations that automate without deliberately preserving the
human expertise behind the automation lose the capacity to train new
staff, handle edge cases, and recover when automated systems reach
their limits. Keeping a clear distinction between what agents handle
autonomously and what stays with human experts sustains
organizational capability across the whole lifetime of the
deployment.

**Desired outcome:**

- You have a competency taxonomy that separates human-owned,
agent-augmented, and fully automated tasks, with documented
criteria for each tier.
- Routing in the agent layer escalates high-stakes, ambiguous, or
edge-case decisions to human experts automatically.
- Rotation programs and workshops keep subject matter experts
proficient with the workflows agents otherwise execute.
- You monitor escalation rates and expert task distribution to
confirm critical competencies stay actively practiced.

**Common anti-patterns:**

- Automating domain workflows without maintaining documented
runbooks or periodic manual execution exercises, reducing the
organization's capacity to operate when agent systems are
unavailable.
- Running agents without clear boundaries between autonomous
action and human oversight, producing cases where agents make
high-stakes decisions that should have routed to experts.
- Scaling agent adoption without workforce planning to preserve
critical skills, so short-term productivity gains erode
long-term organizational capacity.
- Treating escalation as an exception rather than an expected
outcome, so the hand-off paths between agents and human experts
are undertested and fail when they are needed most.

**Benefits of establishing this best
practice:**

- The organization retains the capacity to operate manually when
agent systems are unavailable or encounter situations beyond
their training.
- Critical expertise stays available for onboarding, edge cases,
and evolving business processes that automation has not caught
up to.
- Adoption paces the organization's ability to maintain oversight,
rather than outrunning it.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The threshold question is which competencies must stay with humans
and which can move to agents or automation. A three-tier taxonomy,
human-owned, agent-augmented, and fully automated, gives teams a
shared vocabulary for that decision. The categorization criteria
matter more than the labels:

- Human-owned means decisions where error tolerance is low and
context is highly variable (regulatory judgment, customer
escalations, and strategic trade-offs)
- Agent-augmented means work where an agent accelerates human
output but the human remains the decision-maker (code review,
document drafting, and data analysis)
- Fully automated means routine tasks where agent accuracy
exceeds the cost of errors (routing, classification, and
standard form processing)

Categorization is reviewed as agent capabilities improve and as
organizational priorities shift.

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with Policies and code
interceptors can invoke human-in-the-loop workflows based on
complexity thresholds, confidence scores, or stakes assessment.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) enforces the decision boundaries so that
high-stakes cases escalate automatically rather than depending on
the agent to self-report low confidence.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs agent outputs against
expert-generated baselines, which is how you detect drift in
categories where the agent was trusted but is now degrading.

The automation that removes a task from expert workflows also
removes the practice that kept expertise sharp. Rotation programs
assign experts to handle a fraction of cases manually on a
recurring basis. For business-critical competencies, a defined
minimum (a percentage of cases per quarter, a weekly shift, or a
monthly workshop) keeps practice active. Document runbooks for
workflows agents now execute so the manual path remains viable
when the automated one is unavailable.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks escalation rates and
task distribution, showing whether experts are being kept in the
loop often enough to stay sharp.

### Implementation steps

- **Define a competency
taxonomy:** Categorize organizational skills into
human-owned, agent-augmented, and fully automated tiers with
documented criteria and a review cadence.
- **Configure automated
escalation:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) Policies and
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to route high-stakes, ambiguous,
or low-confidence decisions to human experts.
- **Establish rotation
programs:** Assign subject matter experts to handle
a defined percentage of cases manually each quarter for
competencies critical to business resilience, and maintain
runbooks for manual execution.
- **Validate agent outputs against
expert baselines:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against baselines
produced by subject matter experts to detect drift in
categories that have been trusted to automation.
- **Monitor escalation and task
distribution:** Track escalation rates and expert
task distribution through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to confirm that
critical competencies remain actively practiced.

## Resources

**Related best practices:**

- [AGENTSUS03-BP02 Build
agents to mirror your organizational skills and
competencies](agentsus03-bp02.html)
- [AGENTSUS03-BP03 Maintain
comprehensive specifications for agents and agentic
systems](agentsus03-bp03.html)
- [MLPERF06-BP01
Include human-in-the-loop monitoring](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf-06.html)

**Related documents:**

- [Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Human-in-the-loop
(HITL) - Amazon Nova Act](https://docs.aws.amazon.com/nova/latest/userguide/nova-act-hitl.html)
- [Build
reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03-bp01.html*

---

# AGENTSUS03-BP02 Build agents to mirror your organizational skills and competencies

Agents built to codify proven workflows deliver immediate value.
Agents built to automate processes the organization has not mastered
itself usually waste resources learning what could have been
documented first. Focusing automation on well-understood work is the
difference between agent adoption that pays back quickly and
adoption that consumes resources on untested methodology.

**Desired outcome:**

- You select processes for automation where steps, decision
criteria, and success metrics are documented and consistently
executed by human experts.
- Agents mirror the decision trees, validation checkpoints, and
escalation paths that experts already use.
- Institutional knowledge is captured in knowledge bases that
ground agent decisions, rather than relying solely on foundation
model training data.
- Readiness criteria, minimum documentation maturity, gate agent
development projects before resources are committed.

**Common anti-patterns:**

- Building agents to automate unfamiliar or poorly understood
processes where steps, decision criteria, and success metrics
are not documented, so the automation becomes an experiment
rather than a productivity gain.
- Skipping the step of codifying expert practices before writing
agent logic, missing the opportunity to replicate proven
approaches.
- Generating agent code without understanding it, producing
implementations the team can't maintain or evolve and
accumulating technical debt.
- Automating processes that vary widely in execution across
experts, so the agent picks one variant and discovers at runtime
that the choice did not match the business context.

**Benefits of establishing this best
practice:**

- Agent automation starts from proven practice, so the automation
runs correctly at deployment instead of being debugged in
production.
- Human expertise remains the source of truth and is amplified
rather than replaced, preserving adaptation capacity.
- Development resources flow to workflows where ROI is defensible,
rather than being spent on speculative automation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The criterion for a good automation candidate is straightforward.
The process is well understood, the steps are documented, the
decision criteria are explicit, and multiple experts execute it
the same way. Processes that fail that test should not be the
first things an organization automates. The agent will replicate
whichever variant the documentation captures, and if the
documentation captures the wrong variant, every agent invocation
reinforces the error. The documentation exercise itself is the
first return on investment. Writing down what experts do
encourages consistency even before any agent is built.

Once the documentation exists, the agent is a translation of it.
You configure Amazon Bedrock AgentCore agents to follow the same
decision trees, validation checkpoints, and escalation paths as
human experts. This gives the automation the same runtime behavior
as the manual process.
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) holds the documented expertise as a
RAG source, which grounds agent decisions in institutional
knowledge rather than leaving them to foundation model training
data.
[Amazon
Bedrock AgentCore tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/tools.html) mirror the external systems experts
use (the same APIs, the same data sources, and the same validation
services), so the agent's view of the task matches the expert's.

Routing creates a distinction between automated and human-owned
work.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) can direct routine tasks to full
automation while escalating complex or ambiguous work to human
experts, implementing the three-tier taxonomy described in
[AGENTSUS03-BP01 Maintain
organizational skills and competencies](agentsus03-bp01.html) at runtime.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) assesses whether agent
outputs match expert-generated baselines, and
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes patterns where
agent behavior has drifted from documented practice. Gate agent
development projects behind readiness criteria, inputs, outputs,
decision criteria, and success metrics need to be specified before
development starts, so the documentation discipline becomes a
precondition rather than an afterthought.

Spec-driven development tools like Kiro apply the same discipline
to the implementation side. Agent code written from a
specification is more maintainable, more reviewable, and less
likely to bake in assumptions no one can trace later. The tradeoff
is upfront effort on the specification, which is generally
recouped during review, debugging, and evolution.

### Implementation steps

- **Document workflows before automating
them:** Capture the following from subject matter
experts before approving agent development:

Decision logic
- Exception handling
- Success criteria
- Readiness criteria (inputs, outputs, decision criteria,
and metrics)

- **Store institutional knowledge as RAG
sources:** Load documented expertise into
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) so agent decisions ground in
the organization's knowledge rather than foundation model
defaults.
- **Mirror expert system
access:** Configure
[Amazon
Bedrock AgentCore tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/tools.html) to give agents the same
external systems and data sources human experts use.
- **Route routine vs. complex
work:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) to send routine tasks to
full automation and escalate complex or ambiguous work to
human experts.
- **Validate behavior against expert
baselines:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against
expert-generated baselines and monitor drift through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html).

## Resources

**Related best practices:**

- [AGENTSUS03-BP01 Maintain
organizational skills and competencies](agentsus03-bp01.html)
- [AGENTSUS03-BP03 Maintain
comprehensive specifications for agents and agentic
systems](agentsus03-bp03.html)
- [OPS08-BP01
Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock AgentCore tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/tools.html)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [AI
agents in enterprises: Best practices with Amazon Bedrock
AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03-bp02.html*

---

# AGENTSUS03-BP03 Maintain comprehensive specifications for agents and agentic systems

Agents without specifications become systems that only their
original developers understand. Thorough documentation, purpose,
boundaries, integration points, and decision logic keep
institutional knowledge available to the whole team and verify that
agent behavior is traceable as teams and business processes change.

**Desired outcome:**

- Each deployed agent has a specification covering business
purpose, operational boundaries, decision criteria, and
escalation paths.
- Specifications are stored in version-controlled artifacts
alongside the agent implementation.
- A centralized agent catalog lets team members discover, review,
and reuse agent capabilities.
- Runtime behavior is documented automatically and compared
against design specifications to detect drift.
- Governance requires specification validation before agents reach
production.

**Common anti-patterns:**

- Deploying agents without thorough documentation of purpose,
boundaries, or decision-making logic, so institutional knowledge
is held only by the original developers.
- Letting documentation fall out of date as agents evolve,
producing specifications that describe yesterday's behavior
rather than today's.
- Treating agent configuration as code only, without capturing the
expert decision-making patterns and business logic rationale
that informed the design.
- Skipping specification validation in the promotion path, so
agents reach production with documentation that doesn't match
their actual behavior.

**Benefits of establishing this best
practice:**

- Institutional knowledge survives personnel changes and
organizational restructuring, preserved in documentation rather
than memory.
- Teams develop against specifications informed by business
process, reducing the experimentation cost of each new agent.
- Documented decision logic and operational boundaries make
oversight of automated processes tractable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A specification decouples the agent's behavior from its author.
When the original developer moves on, the next maintainer picks up
the system through the specification rather than through reverse
engineering. Amazon Bedrock AgentCore enables declarative
specifications that capture prompt templates, tool definitions,
guardrail policies, and orchestration logic as version-controlled
artifacts. The documentation and the configuration are the same
artifact rather than two copies that drift.

Spec-driven development tools like Kiro extend the discipline into
how agents get written in the first place. When specifications are
the starting point rather than an afterthought, documentation is
produced as a byproduct of development rather than a retrospective
task. The upfront investment in writing the specification is
recovered during code review, testing, and ongoing evolution,
because every subsequent change happens against a clear baseline.

Discovery needs a central home, like a catalog based on
[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) registry capabilities that makes
agents discoverable, governable, and reusable across the
organization. Each entry captures business purpose, version
history, dependencies, and operational characteristics, so a team
evaluating whether to build something new can check what already
exists.

Specifications can drift if an organization lacks validation
mechanisms.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) generates runtime
documentation from actual execution patterns. When runtime
behavior diverges from design specifications, the telemetry shows
it before the divergence becomes undocumented institutional
knowledge.

For multi-agent systems, document coordination protocols and
delegation patterns explicitly, because the emergent behavior of a
multi-agent system is rarely obvious from any individual agent's
specification. Portfolio-level monitoring, specification
compliance, documentation currency, and behavioral drift, keeps
documentation usable as the agent count scales.

### Implementation steps

- **Set documentation
standards:** Require each agent to carry
specifications using AgentCore's declarative configuration
artifacts. Each specification must cover:

Business purpose
- Operational boundaries
- Decision criteria
- Escalation paths

- **Adopt spec-driven
development:** Use Kiro or similar spec-driven
tools so documentation is produced as a natural byproduct of
the development process rather than a retrospective task.
- **Register agents in a central
catalog:** Record each agent in
[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) with the following
metadata:

Purpose
- Version history
- Dependencies
- Operational characteristics

- **Generate runtime
documentation:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to produce runtime
documentation that can be compared against design
specifications to detect drift.
- **Gate promotion on specification
validation:** Require documentation validation as
part of the pipeline that promotes agents to production, so
production agents always have current specifications.

## Resources

**Related best practices:**

- [AGENTSUS03-BP01 Maintain
organizational skills and competencies](agentsus03-bp01.html)
- [AGENTSUS03-BP04
Decommission unused agents and prevent agent sprawl](agentsus03-bp04.html)
- [OPS11-BP01
Have a process for continuous improvement](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_process_cont_imp.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [The
future of managing agents at scale: AWS Agent Registry now in
preview](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock Agents Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - End-to-end use
cases](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/02-use-cases)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03-bp03.html*

---

# AGENTSUS03-BP04 Decommission unused agents and prevent agent sprawl

Every agent that stays deployed past its usefulness consumes
infrastructure, expands the attack surface, and adds operational
overhead that never shows up as an explicit line item. Active
portfolio management helps prevent the silent accumulation of cost
and complexity that comes with scaled adoption.

**Desired outcome:**

- Every deployed agent has a documented owner, a clear business
purpose, and measurable usage.
- Agents that no longer deliver value move through a structured
decommissioning lifecycle and are retired.
- Teams search the agent registry for existing capabilities before
initiating new agent development.
- Portfolio health, total agent count, percentage with active
usage, percentage with current documentation, is visible at the
organizational level.

**Common anti-patterns:**

- Deploying agents without ownership assignment or usage tracking,
so no one can tell which agents still deliver value.
- Allowing abandoned agents to persist indefinitely because no
decommissioning process exists, accumulating infrastructure cost
and expanding the attack surface.
- Building new agents for capabilities that already exist in
deployed agents elsewhere in the organization, creating
redundant implementations.
- Relying on informal knowledge of which agents are still useful
instead of automated usage tracking, so the decommissioning
decision depends on whoever happens to remember which agents are
deployed.

**Benefits of establishing this best
practice:**

- Portfolio-level decisions about resource consumption are tied to
actual business value delivered, rather than historical
deployment patterns.
- Decommissioning reclaims infrastructure resources and reduces
the operational surface area.
- Discoverability of existing capabilities reduces redundant
implementations and reinforces reusable architecture patterns.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides the authoritative
catalog of deployed agents, with each entry capturing business
purpose, designated owner, deployment date, dependencies, and
usage metrics. Semantic capability search lets teams discover
existing agents before building new ones, which is the preventive
side of avoiding agent sprawl. Pair the registry with
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) metrics tracking invocation frequency and
last-invocation timestamp for each agent. Inactive agents then
surface automatically for owner review instead of being discovered
during audits.

Decommissioning becomes routine when it has a defined lifecycle.
Active, under review, deprecated, and decommissioned stages give
owners clear transitions and give the organization consistent
visibility into which agents are on the path to retirement. When
an agent is flagged for low usage, the owner's first question is
whether it serves a seasonal or infrequent-but-critical purpose.
Tax-season agents, quarterly reporting agents, and
disaster-recovery agents appear idle most of the time but are
essential when they are invoked. A structured review makes that
distinction before deprecation happens.

During quarterly portfolio rationalization, teams evaluate the
full agent inventory against current business priorities, identify
overlapping capabilities, and merge redundant implementations into
shared patterns (following
[AGENTSUS01-BP02
Implement reusable workflow patterns](agentsus01-bp02.html)). They retire agents
whose business context has changed. Portfolio health metrics
tracked through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), total agent count,
percentage with active usage, and percentage with current
documentation, make sustainability outcomes visible at the
organizational level.

### Implementation steps

- **Register every deployed agent with
ownership metadata:** Record each agent in
[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) with the following:

Business purpose
- Designated owner
- Deployment date
- Dependencies

- **Track invocation metrics and flag
inactive agents:** Instrument agents with
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) metrics capturing invocation frequency and
last-invocation timestamp, and flag agents that cross a
defined inactivity threshold for owner review.
- **Define a decommissioning
lifecycle:** Establish the following stages with
transition criteria and owner responsibilities at each:

Active
- Under review
- Deprecated
- Decommissioned

- **Require registry search before new
agent development:** Add a pre-development check to
the intake process so teams discover and evaluate existing
capabilities before initiating new work.
- **Run quarterly portfolio
reviews:** Evaluate the full agent inventory
against current business priorities, consolidate overlapping
capabilities into shared patterns, and retire agents whose
business context has changed.

## Resources

**Related best practices:**

- [AGENTSUS01-BP02
Implement reusable workflow patterns](agentsus01-bp02.html)
- [AGENTSUS03-BP03 Maintain
comprehensive specifications for agents and agentic
systems](agentsus03-bp03.html)
- [AGENTSUS02-BP04
Measure and optimize the environmental footprint of agent
workloads](agentsus02-bp04.html)
- [SUS03-BP02
Remove or refactor workload components with low or no
use](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a3.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [The
future of managing agents at scale: AWS Agent Registry now in
preview](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)

**Related videos:**

- [AgentCore
Registry: Discover, Govern, and Reuse AI Agents at
Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03-bp04.html*

---
