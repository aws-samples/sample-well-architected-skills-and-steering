# AGENTSEC04 — Agent goal alignment and manipulation prevention

**Pillar**: Security  
**Best Practices**: 2

---

# AGENTSEC04-BP01 Implement guardrails and alignment controls

Instruction-following alone doesn't provide reliable enforcement.
Layered controls (deterministic where possible, probabilistic where
necessary) help keep agents inside operational boundaries even when
prompts are adversarial and model behavior is unpredictable.

**Desired outcome:**

- You define agent operational and policy boundaries up front and
enforce them through layered controls, with deterministic
controls (IAM, schema validation, technical policy checks)
handling what is expressible deterministically and probabilistic
controls (content filters, behavioral evaluation) handling what
isn't.
- Multiple validation layers at different stages of the agent call
chain can reduce the likelihood that a single control failure
results in a boundary violation.
- You log, alert on, and periodically review guardrail
interventions, policy violations, and behavioral evaluation
results to tune the controls and surface emerging patterns.

**Common anti-patterns:**

- Relying on a single guardrail configuration for all agent use
cases, applying the same constraints to low-risk informational
agents and high-risk operational agents.
- Applying content filtering only to model outputs without
validating inputs first, letting adversarial content reach the
model before any check runs.
- Defining operational boundaries in natural-language system
prompts alone, relying on the model's instruction-following as
the sole constraint, which can be bypassed through prompt
injection or adversarial framing.

**Benefits of establishing this best
practice:**

- Deterministic technical controls (IAM, schema validation)
combined with probabilistic content controls (Guardrails) at
distinct stages reduce reliance on instruction-following alone.
- Layered validation catches policy violations at multiple stages,
so a bypass at one layer is less likely to result in an
unchecked boundary violation.
- Logged guardrail interventions and evaluation results feed
policy updates as new patterns emerge, keeping boundaries
current with evolving use cases.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Operational boundaries written only in system prompts typically
don't provide reliable enforcement. A prompt can be overridden by
adversarial framing, prompt injection, or the model's own creative
reinterpretation, and none of those failure modes produces an
audit signal before the boundary has already been crossed. The
design pattern is layered. Express what can be expressed
deterministically as hard checks:

- IAM scoping
- Schema validation
- Cedar policies
- Permission boundaries

Use probabilistic controls (content filters, behavioral
evaluation) to cover the content-shaped risks that determinism
can't reach.

[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) is the probabilistic layer. Configure a
base guardrail with universal constraints (no generation of
harmful content, no disclosure of system prompts), then overlay
use-case-specific configurations for each agent's operational
context. Content filter strengths need calibration to use case
sensitivity: HIGH strength for consumer-facing agents handling
categories like hate speech, violence, and sexual content, MEDIUM
strength for internal enterprise agents, and custom thresholds for
specialized domains (medical, legal) with their own content norms.
Content moderation needs to apply to every output path, including
outputs used in internal agent workflows and inter-agent messages,
not just user-facing responses. Use Guardrails versioning for
change management with rollback.

Pre-execution validation matters for two reasons. Applying
Guardrails to user inputs before they reach the model blocks
adversarial content before it influences reasoning, and it rejects
bad inputs before they consume inference capacity. When an agent
invokes an Amazon Bedrock model with a guardrail attached, the
check runs automatically on inputs and outputs. The
ApplyGuardrail API runs the same policy
independently when the automatic path doesn't apply, agents that
invoke non-Amazon Bedrock models (third-party APIs, self-hosted
models), pipelines that need to filter content before deciding
whether to invoke a model at all (for example, checking retrieved
content before it enters the prompt), or additional validation
checkpoints beyond the model invocation.

Monitoring closes the feedback loop. The
[Amazon
Bedrock Guardrails CloudWatch metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html) include
InvocationsIntervened, broken down by
Operation (ApplyGuardrail)
and GuardrailContentSource
(Input / Output) so
input-side and output-side interventions are visible separately.
Amazon CloudWatch alarms on intervention rates route through
Amazon SNS to the security team. For the detail (what was blocked,
which policy triggered, which part of the content was affected),
enable Amazon Bedrock model invocation logging, which captures the
full guardrail trace for each call. Analyze intervention patterns
over time to find emerging techniques that require policy updates
and to catch filter categories generating excessive false
positives or false negatives.

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) assesses goal attainment
correctness and tracks whether agents are achieving their intended
objectives rather than drifting into misaligned goals. Built-in
evaluators cover correctness, helpfulness, tool selection
accuracy, and safety. Custom model-based evaluators extend
coverage to organization-specific alignment requirements. Run
evaluations on a regular cadence and after any significant change
to agent prompts, tools, or guardrail configurations. Results
publish to Amazon CloudWatch alongside AgentCore Observability
insights for a unified view, and CloudWatch alarms on evaluation
scores catch behavioral drift outside acceptable thresholds.

### Implementation steps

- **Map ethical constraints to guardrail
categories:** Define organizational ethical
constraints and operational boundaries per agent use case
and map them to guardrail policy categories with
risk-appropriate differentiation.
- **Build tiered guardrail
configurations:** Create base and use-case-specific
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) configurations, apply them to all
deployments, and use versioning for rollback capability.
- **Validate inputs before
inference:** Call the ApplyGuardrail API on inputs
before they reach the model, checking against denied topics,
word filters, and sensitive information patterns.
- **Alarm on intervention
metrics:** Configure Amazon CloudWatch alarms on
Guardrails metrics (especially
InvocationsIntervened), route alerts
through Amazon SNS, and enable Amazon Bedrock model
invocation logging for detailed intervention records.
- **Deploy AgentCore Evaluations with
drift alarms:** Deploy
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) with built-in and
custom evaluators, and configure Amazon CloudWatch alarms on
evaluation scores to detect behavioral drift.
- **Review intervention logs
monthly:** Establish a monthly review of guardrail
intervention logs to identify emerging patterns and update
policies accordingly.

## Resources

**Related best practices:**

- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [Amazon
Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon
Bedrock Guardrails content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filter.html)
- [Build
responsible AI applications with Amazon Bedrock
Guardrails](https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [AI
agents in enterprises: Best practices with Amazon Bedrock
AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04-bp01.html*

---

# AGENTSEC04-BP02 Human-in-the-loop for critical decisions

Routing every agent action through human review produces
rubber-stamp approvals. Routing none produces unbounded autonomy.
Risk-tiered approval pauses agents only for the decisions where
human judgment actually changes the outcome, with enough context to
make those decisions meaningful.

**Desired outcome:**

- You pause high-risk agent operations for human review before
execution, and reviewers receive enough context to make informed
decisions within a defined time window.
- Escalation paths handle cases where primary reviewers are
unavailable.
- You log human approval decisions with timestamps and reviewer
identities, creating an auditable record of human oversight for
compliance purposes.

**Common anti-patterns:**

- Routing all agent actions through human review regardless of
risk level, creating reviewer fatigue and rubber-stamp
approvals.
- Providing reviewers with insufficient context (the proposed
action only, without the reasoning chain, data sources, or
potential consequences), turning review into a formality.
- Implementing approval workflows without timeout policies or
escalation paths, so agent execution stalls indefinitely when
reviewers are unavailable.

**Benefits of establishing this best
practice:**

- Risk-tiered approval workflows focus reviewer attention on the
decisions where human judgment matters most.
- Logged approval decisions with reviewer identity and timestamps
produce an auditable record that satisfies compliance
requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A risk classification framework is what lets human attention go
where it adds value. Combine static properties of the operation
(what kind of action, against what resource) with dynamic signals
about the request (frequency, time of day, source location, recent
anomalies). Risk classification itself can't rely on an LLM
exposed to the same untrusted content as the request being
evaluated, because adversarial content could influence the
classifier into marking the request as low-risk. Use deterministic
logic (policy engines, rule-based classifiers) as the
authoritative signal, with LLM-assisted classification as an
optional input that a deterministic layer re-checks. As a
baseline: read-only operations proceed autonomously, low-risk
writes require single-reviewer approval, and higher-risk
operations (financial transactions, data deletion, external
communications) require stricter approval, which can be
single-reviewer, multi-reviewer, or out-of-band depending on your
risk policy. For established risk framing approaches to adapt, see
the
[AWS Agentic AI Security Scoping Matrix](https://aws.amazon.com/ai/security/agentic-ai-scoping-matrix/) and
[this
guide to building AI agents in GxP environments](https://aws.amazon.com/blogs/machine-learning/a-guide-to-building-ai-agents-in-gxp-environments/).

Persistent trust grants, where a reviewer approves a specific
operation pattern once and future operations matching the pattern
proceed without re-approval, are a useful escape valve for
genuinely routine operations, but they shift where human judgment
is applied from moment-to-moment to at-grant time. If you
implement persistent trust, bound each grant to a specific
command, parameter shape, or resource. Tier grants by risk so
higher-risk operations are ineligible for persistent trust or
require re-confirmation at a defined cadence, and make grants
themselves auditable and revocable. Wildcard trust grants
(approving all future operations of a given type with no parameter
scoping) effectively remove human oversight from an entire class
of operations and should not be issued.

Once the classifier says human approval is required, route the
request to the approval mechanism appropriate for the agent's
execution environment. Three patterns cover most deployments. For
agents embedded in step-function-driven workloads,
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html) .waitForTaskToken
callback pattern introduces an approval step. The workflow emits a
task token and pauses, the token is delivered to an approval
application through a channel appropriate to the reviewer
population (Amazon SNS to a queue that the approval app consumes,
Amazon SES to a reviewer mailbox, or a webhook endpoint on the
approval app), the application presents the decision to the
reviewer, and the application calls
SendTaskSuccess or
SendTaskFailure with the task token on the
reviewer's behalf. Reviewers don't typically call Step Functions
APIs directly. The approval app holds the credentials, and the
reviewer interacts with the app. See the
[human
approval in Step Functions tutorial](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html) for a worked example.

For agents built on
[Amazon
Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html), two built-in patterns handle
human-in-the-loop confirmation without external workflow
orchestration.
[User
confirmation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-userconfirmation.html) pauses the agent before executing a specific
function and returns the function name and parameter values to the
calling application for yes/no presentation to the user.
[Return
of control (ROC)](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html) goes further by returning the function
call itself so the application decides what to do (present to a
user, run validation, modify parameters, or reject). ROC is
configured at the action group level and covers all actions in
that group. Both patterns assume the application is the component
implementing the human approval UX. These are better suited for
interactive use cases where the end user of the application is
also the approver, while Step Functions callback patterns fit
asynchronous workflows with separate reviewer roles.

For agents that need long-running approval processing,
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html) supports both synchronous and
asynchronous processing through a unified API, enabling an agent
to start a task that may take minutes or hours, immediately
acknowledge the request, continue approval workflows in the
background, and let the user check back later for results. The SDK
provides explicit task lifecycle management through
add_async_task and
complete_async_task APIs, which track
processing status and report agent health through the
/ping endpoint. An agent reports
HealthyBusy while background approval tasks are
in progress and Healthy when idle. This is
particularly useful for multi-reviewer consensus workflows where
approval collection spans extended periods. Blocking operations
such as waiting for reviewer responses need to run in separate
threads or use async methods to avoid blocking the health-check
endpoint, which would cause the runtime session to terminate after
15 minutes of unresponsive pings.

Reviewers need enough context to make informed decisions without
wading through raw logs. Decisions involving agent reasoning often
produce a large volume of intermediate content (prompts, tool
outputs, retrieved documents, model responses) that is too much to
deliver in a notification payload and may be accessed by reviewers
who are not signed into the agent's application. Store the full
decision context in durable storage such as Amazon S3 before
sending the approval notification, including the agent's reasoning
chain, the proposed action, relevant data sources, and potential
consequences. Make the context available through the same
authenticated interface the reviewer uses to approve or deny. When
reviewers don't have access to the approval system's UI (for
example, approvals through email), presigned S3 URLs with short
expiration times provide temporary access to the context document.
Structure the context to highlight the key decision factors.

Timeout policies and escalation paths are specific to each
approval mechanism. In Step Functions,
TimeoutSeconds or
HeartbeatSeconds on the task state waiting for
the approval token triggers a timeout transition, and
Catch clauses route timed-out executions to an
escalation state (notify secondary reviewers, escalate to
management, or default to a safe fallback, typically blocking the
operation). See
[Step
Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) for the attribute details. For
Amazon Bedrock Agents user-confirmation and ROC flows, timeouts
and escalation are handled by the calling application. For
AgentCore Runtime async tasks, the underlying Step Functions
timeouts apply because the async task typically waits on a Step
Functions callback or equivalent external signal.

Approval decisions need to be logged for compliance and audit.
Capture reviewer identity, notification and response timestamps,
the operation under review, the decision, and any escalation
events. Step Functions emits execution history to Amazon CloudWatch Logs when logging is enabled at the workflow level (see
[Step
Functions logging](https://docs.aws.amazon.com/step-functions/latest/dg/monitoring-logging.html)). Augment this with application-level
logs from the approval app so reviewer identity and decision
rationale are captured alongside the
SendTaskSuccess/SendTaskFailure
calls. For AgentCore-based agents, the AgentCore Observability
session and trace hierarchy captures agent-side events and pairs
with the approval-app logs for a complete record. Retain logs
consistent with your compliance requirements and AGENTSEC05-BP01.

### Implementation steps

- **Define a deterministic risk
classifier:** Map agent operation types to approval
tier requirements (autonomous, single-reviewer,
multi-reviewer), combine static classification with dynamic
request-time signals, and implement the classifier as
deterministic logic rather than an LLM.
- **Match approval mechanism to
execution environment:** Use
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html) callbacks for step-function-driven
agents,
[Amazon
Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) user confirmation or return-of-control
for agents on Amazon Bedrock Agents, and
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html) async tasks for agents that
need long-running approval processing, and implement the
corresponding pattern for each tier that requires human
approval.
- **Bound any persistent trust
grants:** Scope each grant narrowly (specific
command, parameter shape, or resource), tier grants by risk,
and make them auditable and revocable.
- **Store decision context
durably:** Write full decision context to Amazon S3
before sending approval notifications, and make the context
available through the authenticated approval interface or
through short-lived presigned URLs when that isn't possible.
- **Configure timeouts with safe
fallbacks:** Implement timeout policies and
escalation paths for each approval mechanism, with safe
fallback actions (typically blocking the operation) when no
reviewer responds in the defined window.
- **Log every approval:**
Capture reviewer identity, timestamps, operation under
review, decision, and escalation events, aligned with
AGENTSEC05-BP01 retention and compliance requirements.
- **Review workflow metrics
periodically:** Look for patterns that suggest
reviewer fatigue or process inefficiencies and adjust
risk-tier thresholds accordingly.

## Resources

**Related best practices:**

- [AGENTSEC04-BP01
Implement guardrails and alignment controls](agentsec04-bp01.html)
- [AGENTSEC07-BP01
Implement cognitive load management](agentsec07-bp01.html)
- [AGENTSEC07-BP03
Multiple reviewers for critical operations](agentsec07-bp03.html)

**Related documents:**

- [AWS Step Functions callback patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html)
- [Human
approval in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html)
- [Step
Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
- [Step
Functions logging](https://docs.aws.amazon.com/step-functions/latest/dg/monitoring-logging.html)
- [Implement
human-in-the-loop confirmation with Amazon Bedrock
Agents](https://aws.amazon.com/blogs/machine-learning/implement-human-in-the-loop-confirmation-with-amazon-bedrock-agents/)
- [Amazon
Bedrock Agents user confirmation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-userconfirmation.html)
- [Amazon
Bedrock Agents return of control](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html)
- [Amazon
Bedrock AgentCore Runtime asynchronous processing](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html)
- [AWS Agentic AI Security Scoping Matrix](https://aws.amazon.com/ai/security/agentic-ai-scoping-matrix/)
- [A
guide to building AI agents in GxP environments](https://aws.amazon.com/blogs/machine-learning/a-guide-to-building-ai-agents-in-gxp-environments/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon SNS](https://aws.amazon.com/sns/)
- [Amazon SES](https://aws.amazon.com/ses/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04-bp02.html*

---
