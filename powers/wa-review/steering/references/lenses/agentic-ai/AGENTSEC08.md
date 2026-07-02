# AGENTSEC08 — Secure agent inputs and outputs

**Pillar**: Security  
**Best Practices**: 2

---

# AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense

Agents take input from many surfaces and only one needs to be
unvalidated for adversarial content to reach the agent's reasoning
process. A layered validation architecture covers every surface, and
in particular catches the indirect prompt injection embedded in
retrieved external content.

**Desired outcome:**

- Every input surface has a validation layer appropriate to its
risk profile, and no input reaches the agent's reasoning process
without passing through at least one validation control.
- You specifically address indirect prompt injection through
retrieved external content, which is the surface most commonly
missed when validation is applied only to direct user inputs.

**Common anti-patterns:**

- Applying input validation only to direct user inputs while
skipping validation for data retrieved from external sources,
letting embedded instructions in web pages, documents, and API
responses bypass user-facing validation.
- Validating at one input surface but not others (for example,
validating user inputs with Guardrails but not validating tool
outputs before they enter the agent's context), creating gaps
that can be targeted.
- Defining denied topics with vague or overly broad descriptions
that generate false positives on legitimate content, eroding
trust and prompting teams to weaken or disable guardrails
entirely.

**Benefits of establishing this best
practice:**

- Defense-in-depth architecture where each input surface has
validation appropriate to its risk profile helps cover every
surface.
- Validation of external content before it enters the agent's
context closes the most commonly missed gap: indirect prompt
injection.
- Confidence-based assessment modes let organizations tune
validation strictness per filter category based on the
likelihood and impact of each risk scenario.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Input surfaces to an agent are not one thing. Direct user
messages, tool outputs, inter-agent messages, retrieved external
content (web pages, documents, API responses), and memory reads
are all paths by which data reaches the agent's context, and each
needs a validation control. Surface-specific guidance lives in
AGENTSEC01-BP02 (memory inputs), AGENTSEC02-BP02 (tool
parameters), and AGENTSEC04-BP01 (goal alignment guardrails). This
best practice is the architectural framing and focuses on the
cross-cutting concern those others don't cover: indirect prompt
injection through external content retrieval.

External content retrieval is the most commonly missed surface.
When an agent uses RAG, web browsing, or API calls to gather
information during task execution, the retrieved content becomes
part of the agent's context, and adversarial instructions embedded
in that content (indirect prompt injection) influence the agent's
behavior as effectively as a direct user injection. Apply
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with prompt attack detection to all
retrieved content before it enters the agent's context, and
implement content source validation that restricts the agent to
retrieving content from approved domains or data sources where
feasible.

Guardrails provides a unified validation mechanism that can be
applied across multiple input surfaces through the ApplyGuardrail
API. Configure a guardrail with prompt attack detection, denied
topics, and word filters once, and apply it at each input
boundary. That gives you consistent policy enforcement across
surfaces with surface-specific tuning through guardrail
versioning.

Two assessment modes matter: block mode returns a binary allow or
deny decision, and detect mode returns confidence scores for each
filter category without blocking the request. Use block mode for
prompt attack detection, where even low-confidence matches warrant
intervention given the severity of potential impact. For content
safety filters on internal or lower-risk applications, detect mode
lets the application make risk-proportionate decisions based on
the confidence scores returned. Score each risk scenario by
likelihood and impact to determine appropriate confidence
thresholds per filter category rather than applying uniform
thresholds.

Denied topics use probabilistic, LLM-based evaluation to determine
whether content matches a topic definition, and definition quality
drives accuracy. Use the full 1,000-character limit for each
denied topic definition with specific and unambiguous
descriptions, and populate all five sample prompt fields (up to
200 characters each) with representative examples that illustrate
the boundary between restricted and permitted content. Vague or
broad definitions inflate false positive rates, which erodes user
trust and pressures teams to weaken or disable guardrails.

When using the ApplyGuardrail API directly (rather than through
the Converse API or Amazon Bedrock Agents), guardrail assessment
results are not automatically published to Amazon CloudWatch. You
are responsible for the telemetry pipeline that captures
assessment outcomes, confidence scores, and blocked content. Set
the outputScope parameter to
full on ApplyGuardrail API calls to receive
complete assessment data including per-filter confidence scores,
which are essential for adjusting thresholds and feeding the
Guardrails Optimizer. Log both the request content and the
assessment response for blocked items, this data is required for
ongoing configuration refinement and false-positive analysis.

The Amazon Bedrock Guardrails Optimizer is a reference
implementation on AWS Samples that automates guardrail
configuration refinement. It uses a Strands Agent to iteratively
adjust denied topic definitions, sample prompts, and filter
thresholds based on annotated test data. As opposed to model
fine-tuning, this is policy configuration optimization. The agent
analyzes failed test cases, rewrites the guardrail configuration,
re-evaluates against the test dataset, and repeats until target
accuracy is reached. Prepare a representative dataset annotated
with expected outcomes (allow or deny for each filter category),
run the Optimizer during initial guardrail setup, and schedule
periodic re-runs (monthly or quarterly) using samples from
production traffic to adapt to evolving content patterns and
reduce false positive rates over time.

### Implementation steps

- **Map input surfaces and assign
controls:** Identify all input surfaces for each
agent and the validation control covering each surface,
flagging any that are currently unvalidated.
- **Validate retrieved external
content:** Configure
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with prompt attack detection and
apply it to external content (RAG results, web content, API
responses) before it enters the agent's context.
- **Pick assessment mode by
risk:** Use block mode for prompt attack detection
filters and consider detect mode for content safety filters
on lower-risk applications, implementing application-level
logic to make risk-proportionate decisions based on returned
confidence scores.
- **Write precise denied
topics:** Use the full 1,000-character limit for
each denied topic definition and populate all five sample
prompt fields with representative examples that illustrate
the boundary between restricted and permitted content.
- **Capture ApplyGuardrail
telemetry:** Set outputScope to
full on all ApplyGuardrail API calls and
implement a telemetry pipeline to capture assessment
outcomes, confidence scores, and blocked content in Amazon CloudWatch.
- **Run the Guardrails
Optimizer:** Run the Amazon Bedrock Guardrails
Optimizer with an annotated test dataset during initial
setup, then schedule periodic re-optimization (monthly or
quarterly) using samples from production traffic.
- **Restrict content sources where
feasible:** Implement content source validation
that restricts agents to retrieving content from approved
domains or data sources.
- **Verify surface-specific controls
exist:** Confirm that the controls described in
AGENTSEC01-BP02 (memory inputs), AGENTSEC02-BP02 (tool
parameters), and AGENTSEC04-BP01 (goal alignment guardrails)
are implemented for each applicable agent.
- **Log and review blocked
inputs:** Log all blocked inputs across surfaces
and review patterns periodically to identify new techniques
and surfaces that may need additional coverage.

## Resources

**Related best practices:**

- [AGENTSEC01-BP02
Validate and sanitize memory inputs](agentsec01-bp02.html)
- [AGENTSEC02-BP02
Validate tool inputs and outputs](agentsec02-bp02.html)
- [AGENTSEC04-BP01
Implement guardrails and alignment controls](agentsec04-bp01.html)
- [AGENTSEC08-BP02 Output
filtering for sensitive information](agentsec08-bp02.html)

**Related documents:**

- [Amazon
Bedrock Guardrails prompt attack detection](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html)
- [Amazon
Bedrock Guardrails denied topics](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-denied-topics.html)
- [Amazon
Bedrock Guardrails ApplyGuardrail API reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ApplyGuardrail.html)
- [Build
responsible AI applications with Amazon Bedrock
Guardrails](https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/)
- [Best
practices with Amazon Bedrock Guardrails filter
configuration](https://aws.amazon.com/blogs/machine-learning/build-safe-generative-ai-applications-like-a-pro-best-practices-with-amazon-bedrock-guardrails/)
- [Amazon
Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html)

**Related examples:**

- [Amazon
Bedrock Guardrails Evaluation and Optimization
Framework](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/responsible_ai/bedrock-guardrails-optimizer)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec08-bp01.html*

---

# AGENTSEC08-BP02 Output filtering for sensitive information

Filtering user-facing responses leaves internal data paths
(inter-agent messages, memory writes, audit logs) as open channels
for PII and credentials to escape. Scanning every output path with a
data classification policy keeps sensitive content inside the
agent's authorized handling scope.

**Desired outcome:**

- You scan agent outputs for PII, credentials, and other sensitive
data before returning them to users or downstream systems, with
content masked or blocked based on data classification policies.
- Agent outputs containing credentials, private keys, or regulated
PII are blocked or masked before they reach end users or
external systems.
- You log output filtering decisions for compliance auditing.

**Common anti-patterns:**

- Relying on the model to self-censor sensitive information, when
models do generate outputs containing PII or credentials
(especially when that information is in the agent's context from
tool outputs or retrieved documents).
- Applying output filtering only to user-facing responses while
skipping filtering for outputs passed to other agents or stored
in memory, creating data-leakage paths through internal
communications.
- Using overly broad masking rules that mask legitimate content
alongside sensitive data, degrading output quality to the point
users work around the filter.

**Benefits of establishing this best
practice:**

- Data classification enforcement at the agent boundary helps keep
sensitive information within the agent's authorized
data-handling scope regardless of what the model generates.
- Logged filtering decisions support compliance with data
protection regulations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Every output path is a potential exfiltration path. User-facing
responses are the obvious one, but an agent also writes to memory,
passes content to other agents, and emits logs. Filtering only the
user-facing path leaves the others as open channels for sensitive
data, and adversarial inputs designed to exfiltrate data don't
consistently target the user-facing channel. The architectural
requirement is that every output surface passes through the same
filter, not just the ones users see.

[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html) sensitive information filters cover the
data types relevant to most use cases:

- PII categories (names, addresses, phone numbers, email
addresses, SSNs, and financial account numbers)
- Credentials (API keys, passwords, and private keys)
- Custom entity types specific to your organization

Configure the filter action as MASK for most sensitive data types
to preserve output utility while protecting sensitive content, and
BLOCK for the most sensitive categories such as credentials and
private keys where masking isn't enough.

Apply the filter as middleware in the agent output pipeline, so
every output destination, user-facing responses, inter-agent
messages,
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) writes through the
create_event API, and audit logs, flows through
it. AgentCore Memory's built-in long-term memory strategies
already filter PII from extracted long-term records by default,
but short-term memory (raw events) retains original content, so
compliance requirements that prohibit PII in any stored form
require applying Guardrails sensitive information filters before
writing events to short-term memory as well.

For organization-specific sensitive data types not covered by
built-in categories, Amazon Comprehend custom entity recognizers
extend coverage. Train recognizers on examples of your sensitive
data types and integrate them into the output filtering pipeline
through AWS Lambda functions that call the Amazon Comprehend API
before returning outputs.

Logging every filtering decision (the type of sensitive data
detected, the action taken (mask or block), the output
destination) produces the data loss prevention report and catches
patterns where the agent is systematically generating outputs
containing sensitive data (a signal of prompt injection or data
exfiltration). Amazon CloudWatch alarms on elevated detection
rates turn that signal into an active alert.

### Implementation steps

- **Configure sensitive information
filters:** Set up
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html) with filters for all relevant PII
and credential categories, choosing MASK or BLOCK per
category based on data classification policy.
- **Filter every output path:**
Apply output filtering as a middleware layer for user-facing
responses, inter-agent messages, memory writes, and audit
logs.
- **Filter before short-term memory
writes when required:** For compliance requirements
that prohibit PII in any stored form, apply Guardrails
filtering before writing events to
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) short-term storage.
- **Extend with Amazon Comprehend custom
entities:** Train Amazon Comprehend custom entity
recognizers for organization-specific sensitive data types
and integrate them into the filtering pipeline.
- **Log and alarm on
detections:** Log all output filtering decisions
with data type, action, and destination metadata, and
configure Amazon CloudWatch alarms for elevated sensitive
data detection rates.
- **Review configurations
periodically:** Adjust output filtering to match
evolving data classification policies and new regulated data
types.

## Resources

**Related best practices:**

- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [Amazon
Bedrock Guardrails sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html)
- [Amazon
Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html)
- [Amazon Comprehend documentation](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon Comprehend](https://aws.amazon.com/comprehend/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec08-bp02.html*

---
