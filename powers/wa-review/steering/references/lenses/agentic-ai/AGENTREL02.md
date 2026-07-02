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
