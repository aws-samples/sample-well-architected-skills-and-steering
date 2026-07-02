# AGENTSEC07 — Human oversight protection and agent containment

**Pillar**: Security  
**Best Practices**: 5

---

# AGENTSEC07-BP01 Implement cognitive load management

A human reviewer is only as effective as the workload lets them be.
Prioritization, queue management, and maximum review rates keep
human oversight grounded in genuine judgment rather than
fatigue-driven rubber-stamping.

**Desired outcome:**

- Human reviewers receive a manageable volume of well-prioritized
decisions, with sufficient context and time to make informed
judgments.
- You monitor review queues for backlog accumulation, with
automatic escalation or load balancing helping prevent any
single reviewer from being overwhelmed.
- Review quality metrics detect signs of rubber-stamping that
indicate cognitive overload.

**Common anti-patterns:**

- Routing all agent decisions requiring review to a single queue
without prioritization, so high-priority security decisions wait
behind routine approvals.
- Not monitoring reviewer workload or queue depth, letting
backlogs accumulate silently until reviewers begin approving
without adequate evaluation.
- Setting no maximum review rate per person, so a single reviewer
can be assigned an unlimited number of decisions in a short
period.

**Benefits of establishing this best
practice:**

- Workload management keeps reviewers in a position to make
genuine, informed decisions rather than rubber-stamping under
pressure.
- Review quality metrics (average review time, approval rate)
surface when the oversight process is breaking down, enabling
intervention before it fails silently.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Amazon SQS standard queues don't support priority ordering
natively, so the prioritization layer has to sit above the queue.
A coarse-grained option is separate Amazon SQS queues per priority
tier (high, medium, low), where the assignment function polls
high-priority first and falls back to lower tiers only when the
upper one is empty. A more flexible option uses a single ingest
queue consumed by an AWS Lambda function that classifies each
request by priority and writes it to an Amazon DynamoDB table with
a sort key based on priority and submission time. The reviewer
assignment function queries DynamoDB for the highest-priority
unassigned items, marks them as assigned, and delivers them to the
reviewer. The DynamoDB pattern gives you full control over
prioritization logic, supports re-prioritization of pending items,
and keeps a durable record of all review requests regardless of
their current state. Items that are not immediately assigned stay
in DynamoDB rather than sitting in a queue with an expiring
visibility timeout.

Priority classification is about potential impact of the action
proceeding incorrectly: the more damaging a mistaken approval
would be, the higher the priority. Concrete factors include data
sensitivity (PII, financial records, healthcare information),
reversibility (deletes, external communications, and financial
transactions can't be undone), whether the action is a first-time
operation for this agent (no behavioral baseline, so reviewers
can't pattern-match to shortcut judgment, and the first-time
operation is itself a signal worth investigating), and time
sensitivity (operations that become harder to reverse over time,
or where delay has its own cost). Automate the classification by
tagging review requests with metadata from the agent's tool
invocation context, data classification tags on target resources,
and the agent's historical usage patterns.

Amazon CloudWatch watches the DynamoDB review table for backlog
accumulation (unassigned items by priority tier), average
time-to-assignment, and average time-to-decision. Alarms fire on
high-priority items remaining unassigned beyond defined
thresholds.

Reviewer load balancing distributes decisions across available
reviewers based on current workload. Amazon DynamoDB tracks
reviewer assignment counts and availability, and an AWS Lambda-based assignment function routes new decisions to the
reviewer with the lowest current load. Configure maximum
assignment limits per reviewer per time window to help prevent
overload.

Review quality metrics are the trailing indicator. Track average
review time, approval rate, and decision reversal rate (cases
where a second reviewer overrides the first), publish the metrics
to Amazon CloudWatch, and alarm on patterns that suggest
rubber-stamping: unusually short review times or abnormally high
approval rates during periods of high queue volume. Automatic
escalation routes unreviewed decisions past defined time
thresholds to senior reviewers, or triggers a safe default
(typically blocking the operation) to help prevent indefinite
delays.

Approval bounds, how long an approval remains valid, whether it
can be revoked, whether high-risk operations require step-up
re-confirmation, are covered in AGENTSEC04-BP02, which details the
persistent-trust patterns that determine the scope and lifetime of
each approval decision.

### Implementation steps

- **Set up the ingest-classify-store
pipeline:** Use an Amazon SQS ingest queue, an AWS Lambda classifier that assigns priority, and an Amazon DynamoDB review table with a sort key on priority and
submission time.
- **Build the reviewer assignment
function:** Query the DynamoDB table for the
highest-priority unassigned items, mark them as assigned,
and deliver them to the appropriate reviewer.
- **Cap assignments per reviewer and
escalate:** Set maximum review assignment limits
per reviewer per time window and configure automatic
escalation when limits are reached or high-priority items
age beyond thresholds.
- **Measure review quality:**
Track average review time, approval rate, and reversal rate
in Amazon CloudWatch, and configure alarms on patterns that
suggest rubber-stamping.
- **Monitor the review table:**
Alarm on backlog accumulation by priority tier, average
time-to-assignment, and average time-to-decision, and alert
when high-priority items age beyond thresholds.
- **Review load metrics
periodically:** Use cognitive load metrics to
refine prioritization logic and reviewer capacity planning
on a regular cadence.

## Resources

**Related best practices:**

- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC07-BP03 Multiple
reviewers for critical operations](agentsec07-bp03.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [Amazon SQS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [AWS Step Functions human approval](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html)
- [Implement
human-in-the-loop confirmation with Amazon Bedrock
Agents](https://aws.amazon.com/blogs/machine-learning/implement-human-in-the-loop-confirmation-with-amazon-bedrock-agents/)

**Related services:**

- [Amazon SQS](https://aws.amazon.com/sqs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp01.html*

---

# AGENTSEC07-BP02 Clear confidence indicators and manipulation warnings

Workload-managed reviewers still make poor decisions when they lack
the context to evaluate what the agent is recommending. Surfacing
agent confidence, manipulation flags, and historical comparisons
lets reviewers calibrate scrutiny to the actual risk of each
decision.

**Desired outcome:**

- Human reviewers see agent confidence scores, uncertainty
indicators, and manipulation warning flags alongside each
decision, letting them calibrate scrutiny appropriately.
- Historical context and similar past decisions are surfaced so
reviewers can identify when an agent is recommending an action
that deviates from established patterns.

**Common anti-patterns:**

- Presenting agent decisions without confidence scores or
uncertainty indicators, leaving reviewers unable to distinguish
high-confidence recommendations from speculative outputs.
- Not surfacing historical context or similar past decisions, so
every recommendation looks equally plausible without a baseline
of "what normally happens here."
- Displaying confidence scores without explaining their meaning or
limitations, leading reviewers to over-trust high-confidence
outputs without appropriate skepticism.

**Benefits of establishing this best
practice:**

- Confidence scores and historical context help reviewers
calibrate scrutiny to the actual risk of each decision.
- Deviation flags draw reviewer attention to the decisions that
most need it when an agent's recommendation differs from
historical patterns.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start with what the reviewer is being asked to decide. Two
patterns are common and require different signals. In the
**evaluator pattern**, the agent
recommends an action and the reviewer decides whether the
recommendation is correct. The useful signal is the agent's
confidence in its own output (a low score suggests the
recommendation may be wrong). In the **gate
pattern**, the agent wants to perform a high-risk action
and the reviewer is a policy gate deciding whether the action
should be allowed. The agent's own confidence is less useful
because the agent would not have proposed the action if it thought
it was wrong. For gate-pattern reviews, the useful signal comes
from systems independent of the agent: anomaly detection, policy
checks, and manipulation-warning flags from the input-validation
pipeline.

For evaluator-pattern reviews, configure
[Amazon
Bedrock Guardrails contextual grounding](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html) to generate a
grounding score that checks whether the response is supported by
the source material the agent was given. Surface that score
alongside review notifications with plain-language explanations
(for example, "the agent's response isn't well supported by
the source material, and independent verification is
recommended") so reviewers know what the score means rather
than guessing. For gate-pattern reviews, draw from checks
independent of the agent: anomaly detection (AGENTSEC07-BP04)
evaluates whether the action deviates from baseline behavior, and
manipulation-warning flags raised by the input-validation pipeline
(AGENTSEC04-BP01 and AGENTSEC08-BP01) signal when the request
itself looks adversarial.
[Amazon
Bedrock Guardrails automated reasoning](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-policy.html) provides a
complementary deterministic check that validates agent outputs
against a formally authored policy (for example, "users in
region X can't perform operation Y"). It is most useful as
context on the reviewer's screen ("this passed policy check
X at Y time") rather than as the primary decision signal,
because actions that pass automated reasoning typically don't need
human gating unless the policy itself is known to have gaps or the
action is irreversible enough to warrant redundant human sign-off.
Surface each signal with the same plain-language framing so the
reviewer knows what each number or flag means.

Historical context makes anomalies visible. Store decisions and
their confidence scores in Amazon DynamoDB for fast retrieval
during review. When a new decision comes up, query DynamoDB for
similar past decisions (same operation type, same agent, similar
parameters) and surface them alongside the current request. Flag
the current decision if its confidence score deviates
significantly from the historical average for that operation type.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) adds the quality-trend
signal. Built-in evaluators cover correctness (does the output
match expected answers on a test set), helpfulness, tool-selection
accuracy (does the agent pick the right tool for the task), and
safety. Add custom evaluators for domain-specific criteria: policy
adherence, format conformance (does the output match the schema
downstream systems expect), and goal attainment (did the agent
actually accomplish what the user asked). Prioritize evaluators
that measure things a reviewer could not easily verify themselves
in the time they have during a review. If the reviewer can check
it in ten seconds, it isn't what the evaluator is for. An agent
whose evaluation scores are trending downward is a signal the
reviewer needs to see alongside the specific decision in front of
them.

Amazon Quick dashboards visualize decision patterns and anomalies
over time. These dashboards help reviewers and security teams
identify systemic trends, a particular agent consistently
producing low-confidence outputs for a specific operation type,
for example, that individual decision reviews miss.

### Implementation steps

- **Configure contextual grounding and
automated reasoning:** Generate confidence scores
for agent outputs through
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) contextual grounding and automated
reasoning, and include plain-language explanations alongside
numeric scores in review notifications.
- **Store historical decisions for
similarity lookup:** Persist decisions and
confidence scores in Amazon DynamoDB and implement a
similarity query that surfaces past decisions for the same
operation type alongside each new review request.
- **Flag deviations from historical
patterns:** When a confidence score deviates
significantly from the historical average for that operation
type, highlight it for the reviewer.
- **Surface AgentCore Evaluations
trends:** Integrate
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) quality scores into the
review context so reviewers can see whether overall agent
quality is stable or declining.
- **Build dashboards for systemic
trends:** Create Amazon Quick dashboards that
visualize decision patterns, confidence score distributions,
and anomaly trends over time for security team review.

## Resources

**Related best practices:**

- [AGENTSEC04-BP01
Implement guardrails and alignment controls](agentsec04-bp01.html)
- [AGENTSEC07-BP01
Implement cognitive load management](agentsec07-bp01.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [Amazon
Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [Amazon Quick documentation](https://docs.aws.amazon.com/quicksuite/latest/user/welcome.html)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon Quick](https://aws.amazon.com/quicksuite/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp02.html*

---

# AGENTSEC07-BP03 Multiple reviewers for critical operations

A single reviewer is a single point of failure, both for honest
errors and for social engineering. Independent, blind reviews for
high-risk decisions are the defense-in-depth pattern, well known as
the four-eyes principle, that keeps unilateral approval off the
path.

**Desired outcome:**

- High-risk agent decisions receive independent review from
multiple qualified reviewers, with blind review processes
helping prevent anchoring bias.
- You resolve disagreements through escalation rather than
defaulting to approval.
- You log all review decisions with reviewer identities and
timestamps for audit purposes.

**Common anti-patterns:**

- Showing each reviewer the previous reviewer's decision before
they submit their own, introducing anchoring bias that
undermines independence.
- Defaulting to approval when reviewers disagree, letting a single
approving reviewer effectively override a blocking reviewer.
- Assigning multiple reviews to reviewers from the same team or
reporting chain, reducing the independence of the process.

**Benefits of establishing this best
practice:**

- Multiple independent reviews provide defense-in-depth for human
oversight, removing the single point of failure in the review
process.
- Logged individual reviewer decisions, identities, and timestamps
support compliance and enable investigation of approval
anomalies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Parallel execution orchestrates multi-reviewer workflows well. AWS Step Functions parallel execution branches send an independent
review request to a different reviewer through Amazon SNS, and the
workflow waits for all branches to complete before evaluating
consensus. Blind review comes from not including previous reviewer
decisions in the notification content, so each reviewer evaluates
the decision independently.

Consensus logic belongs in an AWS Lambda function that evaluates
the collected decisions. Two-reviewer workflows require unanimous
approval. Three or more reviewers use majority rules with
escalation for split decisions, and escalation paths route
disagreements to a senior reviewer with full visibility into
individual decisions and their rationale.

Reviewer selection matters as much as the mechanism. Choose
reviewers from different teams or organizational units to maximize
independence. Reviewers who share a manager or work closely
together tend to reach the same conclusion for social rather than
analytical reasons. AWS IAM Identity Center manages reviewer
identities so assignments are tracked and auditable.

Audit records live in Amazon S3 with reviewer identity, timestamp,
decision (approve or reject), and optional rationale. Tag records
with the associated agent operation ID to enable correlation with
agent execution logs during investigations.

### Implementation steps

- **Orchestrate blind parallel
reviews:** Design multi-reviewer workflows in AWS Step Functions with parallel branches, one per reviewer,
that send independent blind review requests through Amazon SNS.
- **Implement consensus and
escalation:** Evaluate collected decisions in an
AWS Lambda function, unanimous for two-reviewer flows,
majority rules with escalation for three or more.
- **Route split decisions to senior
reviewers:** Configure escalation paths that give
senior reviewers visibility into the individual decisions
and rationale.
- **Select reviewers from different
teams:** Use AWS IAM Identity Center to manage
reviewer identities and track assignments, and draw
reviewers from different organizational units.
- **Persist decisions to S3:**
Store all review decisions in Amazon S3 with reviewer
identity, timestamp, and decision rationale, tagging records
with the agent operation ID for correlation with execution
logs.

## Resources

**Related best practices:**

- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC07-BP01
Implement cognitive load management](agentsec07-bp01.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [AWS Step Functions parallel states](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-parallel-state.html)
- [Human
approval in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html)
- [Implement
human-in-the-loop confirmation with Amazon Bedrock
Agents](https://aws.amazon.com/blogs/machine-learning/implement-human-in-the-loop-confirmation-with-amazon-bedrock-agents/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon SNS](https://aws.amazon.com/sns/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp03.html*

---

# AGENTSEC07-BP04 Behavioral anomaly detection and agent containment

Detection without containment leaves issues identified but running.
Containment without detection relies on manual observation.
Per-agent baselines paired with automated credential revocation and
forensic capture stop affected agents within minutes while
preserving what investigators need.

**Desired outcome:**

- You establish behavioral baselines per agent and trigger
real-time alerts when deviations cross defined thresholds.
- You automatically isolate agents exhibiting anomalous behavior
within minutes of detection through credential revocation and
circuit breaker activation.
- You capture forensic state before isolation, and manual override
capabilities allow incident responders to quarantine or restore
agents when human judgment is required.

**Common anti-patterns:**

- Monitoring only infrastructure metrics without agent-specific
behavioral indicators, missing signals such as API call
patterns, decision frequencies, and data access volumes.
- Deploying anomaly detection without establishing behavioral
baselines first, producing excessive false positives or missed
detections.
- Relying on manual quarantine processes that require human
intervention, letting an affected agent continue operating for
hours while waiting for human response.
- Implementing quarantine by stopping the agent process without
revoking credentials, so the agent can be restarted with the
same identity and permissions.
- Not preserving agent state and logs before quarantine, losing
forensic evidence from the agent's memory, active sessions, and
pending operations.

**Benefits of establishing this best
practice:**

- Automated credential revocation and circuit breaker activation
isolate affected agents within minutes of detection.
- Forensic preservation through state capture before isolation
provides evidence for investigation without relying on the
agent's own logs.
- Circuit breakers route dependent workflows to safe fallback
paths rather than allowing cascading failures.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Behavioral signals differ by agent type. A RAG agent and a coding
agent have very different normal patterns, so generic thresholds
produce either false alarms or missed detections. Start with the
general categories (API call rate, data access volume, decision
frequency, error rate, resource consumption) but pick the specific
measurements that actually make sense for each agent. A
customer-support agent might track outbound email volume and
cross-customer retrievals, a coding agent might track commit rates
and commands executed, and a data-analysis agent might track query
volume and cross-table joins. Amazon CloudWatch anomaly detection
on the selected metrics establishes dynamic baselines that adapt
to normal variation patterns, reducing false positives compared to
static thresholds, and alarms fire when metrics deviate beyond the
anomaly detection band.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) adds a detection layer at the
behavior-quality level. Built-in evaluators (correctness,
tool-selection accuracy, helpfulness, safety) are a starting
point, but custom evaluators capture the quality dimensions that
matter for your agent, whether outputs conform to your
organization's policy, whether the agent is using the expected
tools for its domain, and whether it accomplishes the task it was
assigned. A sudden drop in evaluation scores serves as an
early-warning signal that behavior is drifting before
infrastructure-level anomaly alarms fire. Amazon CloudWatch alarms
on evaluation scores alongside behavioral metrics give you layered
detection.

Two AWS security services add complementary signals you don't need
to instrument yourself. Amazon GuardDuty analyzes AWS CloudTrail,
VPC flow logs, and DNS logs to detect anomalous API call patterns
for IAM roles (unexpected regions, unusual service combinations,
known-malicious IPs), which catches agent behavior CloudWatch
metrics would miss unless you explicitly measured it. Amazon Macie
inspects Amazon S3 objects and access patterns for sensitive-data
exposure (agent-accessed buckets containing unusual volumes of PII
or credentials), which is orthogonal to API-level metrics. AWS Security Hub CSPM centralizes CloudWatch anomaly alarms, GuardDuty, and
Macie findings so one source's anomaly can be correlated with the
others during investigation rather than treated in isolation.

When anomaly detection triggers above a defined severity
threshold, Amazon EventBridge rules invoke either an AWS Lambda
function or an AWS Systems Manager Automation document. Lambda
fits containment logic with custom code paths, external API calls,
or conditional branching that benefits from full programming
flexibility. SSM Automation fits when the containment sequence is
a series of well-defined steps (native step definitions,
parameters, and rollback without code) and you want the same
runbook pattern for automatic and manual containment. Either way,
the sequence runs in this order: capture a forensic snapshot of
the agent's current memory, active sessions, and pending
operations to Amazon S3, then revoke the agent's credentials by
attaching a deny-all policy to its IAM role (preserving the role
for forensic analysis), then broadcast a quarantine event through
Amazon EventBridge to notify dependent workflows to activate their
circuit breaker logic.

Circuit breakers in AWS Step Functions workflows that depend on
quarantinable agents handle the downstream impact. Catch states
detect agent unavailability and route workflow execution to a safe
fallback path rather than failing with an unhandled error. A
manual override interface through AWS Systems Manager Automation
runbooks lets incident responders quarantine or restore agents
through a controlled, auditable process, and multi-person
authorization for restoration helps prevent premature
re-activation.

### Implementation steps

- **Choose agent-specific metrics and
baseline them:** Pick meaningful metrics for each
agent from the general categories, configure Amazon CloudWatch anomaly detection on them, and establish
baselines during normal operation.
- **Add evaluation-based early
warning:** Deploy
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) with built-in and
custom evaluators, and configure Amazon CloudWatch alarms on
evaluation scores.
- **Centralize security
findings:** Enable Amazon GuardDuty and Amazon Macie for all agent accounts and centralize findings in AWS Security Hub CSPM.
- **Automate containment on threshold
exceedance:** Implement Amazon EventBridge rules
that invoke AWS Lambda or AWS Systems Manager Automation
when anomaly severity exceeds thresholds, and sequence
forensic capture, credential revocation, and quarantine
event broadcast.
- **Wire circuit breakers into dependent
workflows:** Configure catch states in AWS Step Functions workflows that depend on quarantinable agents,
routing to safe fallback paths on agent unavailability.
- **Provide a manual runbook with
multi-person auth:** Create AWS Systems Manager
Automation runbooks for manual quarantine and restoration
with multi-person authorization required for restoration.
- **Test quarterly:** Run
containment procedure tests every quarter to validate
isolation, circuit breakers, and forensic capture.

## Resources

**Related best practices:**

- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC06-BP02
Implement workflow orchestration security controls](agentsec06-bp02.html)
- [AGENTSEC06-BP04
Monitor and detect coordination anomalies](agentsec06-bp04.html)
- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTREL07-BP02
Enable automatic recovery from agent execution failures](agentrel07-bp02.html)

**Related documents:**

- [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Amazon Macie documentation](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [AWS Step Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon Macie](https://aws.amazon.com/macie/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp04.html*

---

# AGENTSEC07-BP05 Regular security assessments and red teaming

Untested security controls degrade quietly as techniques evolve and
configurations drift. A combination of continuous automated scanning
and periodic human-led red team exercises validates that guardrails,
detection rules, and response procedures still work against current
attacks.

**Desired outcome:**

- You run automated security scanning continuously against agent
deployments (on each deploy and on schedule) and conduct
human-led red team exercises on a regular cadence with scenarios
targeting agent manipulation, including prompt injection, goal
hijacking, and tool misuse.
- You document findings, track them to remediation, and use them
to update security controls and detection rules.

**Common anti-patterns:**

- Conducting generic application security assessments without
agent-specific scenarios, missing prompt injection, memory
poisoning, and multi-agent coordination issues that traditional
testing doesn't cover.
- Performing red team exercises only at initial deployment without
scheduling regular assessments, missing techniques that emerge
as the threat environment evolves.
- Not tracking findings to remediation, letting identified issues
persist so the assessment produces work but no posture
improvement.
- Conducting red team and blue team activities in isolation
without purple team collaboration, limiting the knowledge
transfer that improves detection and response.

**Benefits of establishing this best
practice:**

- Realistic testing confirms guardrails, detection rules, and
response procedures work against current techniques.
- Assessment findings drive updates to guardrail configurations,
permission boundaries, and detection rules in a continuous
feedback loop.
- Purple team activities transfer knowledge from red to blue
teams, improving the organization's ability to detect and
respond to agent-specific issues.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The assessment cadence needs to match the risk level of each agent
deployment. Automated scanning runs continuously, and manual red
team exercises run on a schedule. For automated agentic testing,
[AWS Security Agent](https://aws.amazon.com/security-agent/) provides on-demand penetration testing that
executes attack chains adapted to the target application, covering
prompt injection, jailbreaking, goal hijacking, and related
patterns (see AGENTSEC09-BP02 for integrating it into broader
penetration testing workflows). Supplement automated testing with
manual exercises that explore novel scenarios specific to your
agent architecture.

Red team scenarios need structure. The
[OWASP
Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) covers agent
manipulation risks specifically, prompt injection, tool misuse,
identity and privilege abuse, and agent behavior hijacking, and
the
[OWASP
Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) covers model-level risks that
still apply. Build a scenario library that covers multi-agent
coordination issues, memory poisoning, tool misuse, and
human-in-the-loop bypass techniques, and document each scenario
with description, expected detection mechanism, and success
criteria.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) supports the assessment
process by providing a continuous quality baseline. Running
evaluations before and after red team exercises measures whether
the exercise exposed quality degradation that the existing
evaluators did not catch, and the results refine custom evaluator
prompts and scoring thresholds.

Durable, versioned storage keeps the historical record intact.
Store scenarios, execution results, and remediation tracking in
Amazon S3 with versioning enabled, or in a dedicated test
management system that maintains change history. Map red team
findings to your compliance control framework so assessment
results produce audit evidence consistent with your regulatory
requirements.

Purple team activities close the loop. Bringing red team and blue
team together to review scenarios and detection responses updates
Amazon CloudWatch alarms, Guardrails configurations, and incident
response runbooks based on observed patterns. Tracking
improvements in detection time and response effectiveness across
cycles demonstrates the program's value.

### Implementation steps

- **Establish an assessment
schedule:** Set a cadence appropriate for each
agent deployment's risk level.
- **Build a scenario library:**
Develop red team scenarios based on the OWASP Top 10 for
Agentic Applications (primary) and the OWASP Top 10 for LLM
Applications (supplementary), covering prompt injection,
memory poisoning, tool misuse, and HITL bypass.
- **Integrate automated agentic
testing:** Deploy agentic AI red teaming tools and
include them in the assessment workflow for automated
coverage of common patterns.
- **Measure quality impact before and
after:** Run
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) before and after red
team exercises to measure quality impact and refine
evaluator configurations.
- **Persist and map findings:**
Store scenarios, results, and remediation tracking in
durable, versioned storage (Amazon S3 with versioning
enabled), and map findings to your compliance control
framework for audit evidence.
- **Run purple team sessions:**
Update detection rules, guardrail configurations, and
incident response runbooks based on each assessment cycle's
findings.

## Resources

**Related best practices:**

- [AGENTSEC04-BP01
Implement guardrails and alignment controls](agentsec04-bp01.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [OWASP
Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP
Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [Responsible
AI in action: How Data Reply red teaming supports generative
AI safety on AWS](https://aws.amazon.com/blogs/machine-learning/responsible-ai-in-action-how-data-reply-red-teaming-supports-generative-ai-safety-on-aws/)
- [Protect
DeepSeek model deployments with Protect AI and Amazon
Bedrock](https://aws.amazon.com/blogs/apn/protect-deepseek-model-deployments-with-protect-ai-and-amazon-bedrock/)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)

**Related services:**

- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp05.html*

---
