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
