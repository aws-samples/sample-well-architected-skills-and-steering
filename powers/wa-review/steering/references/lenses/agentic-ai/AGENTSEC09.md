# AGENTSEC09 — Agent vulnerability scanning and penetration testing

**Pillar**: Security  
**Best Practices**: 5

---

# AGENTSEC09-BP01 Integrate AI-powered vulnerability scanning across the development lifecycle

Pattern-matching scanners find common bugs but miss
context-dependent flaws in agent orchestration, tool interactions,
and authorization chains. AI-powered scanning that reasons about
code and design documents the way a human security researcher does
catches these issues at the phase when remediation is cheapest.

**Desired outcome:**

- Vulnerability scanning is embedded at every phase of the agentic
AI development lifecycle, covering design documents, pull
requests, and deployed applications.
- You review design documents for security risks before code is
written, analyze pull requests for common and agent-specific
vulnerabilities during development, and continually scan
deployed applications for emerging threats.
- Findings carry severity ratings, confidence scores, and
practical remediation guidance so teams can prioritize and fix
issues efficiently.

**Common anti-patterns:**

- Relying on rule-based static analysis that matches known
vulnerability patterns, missing context-dependent issues in
agent orchestration logic, insecure tool parameter handling, or
broken access control in multi-agent delegation chains.
- Performing security scanning only at deployment time rather than
across design and development phases, letting vulnerabilities
accumulate and making late-discovery remediation expensive.
- Treating AI-generated code the same as human-written code for
security review, ignoring the distinct vulnerability patterns AI
coding assistants introduce (hallucinated API calls, insecure
default configurations, and outdated library usage).

**Benefits of establishing this best
practice:**

- Design-phase security reviews identify architectural risks
before code is written, reducing remediation cost and
development delays.
- AI-powered scanning that reasons about application context and
agent behavior catches complex vulnerabilities that
pattern-matching tools miss.
- Automated scanning integrated into CI/CD pipelines scales
security expertise across development teams without creating
bottlenecks.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Pattern matching against known signatures isn't enough for agentic
systems. A SQL injection signature doesn't catch a broken
multi-agent authorization chain, and a missing-input-validation
rule doesn't catch a tool parameter manipulated through a prompt
injection. The scanning that reaches those issues has to reason
about how components interact, trace data flows through the
orchestration layer, and understand what the agent was actually
intended to do. That is the capability AI-powered scanning adds,
and why it is effective on agent-specific flaws.

Deploy scanning across the full lifecycle. At the design phase,
use tools that analyze architecture documents, product
specifications, and technical designs for security risks before
code is written. During development, integrate scanning into code
review workflows to analyze pull requests for both common
vulnerabilities (SQL injection, missing input validation) and
agent-specific issues (insecure tool invocations, insufficient
permission scoping). At deployment, run on-demand scans against
running applications to validate that security controls hold under
realistic conditions.

[AWS Security Agent](https://aws.amazon.com/security-agent/) provides this lifecycle coverage as a single
capability. Security teams define organizational security
requirements once in the AWS Management Console (approved authorization
libraries, logging standards, data access policies), and AWS
Security Agent enforces them throughout development, evaluating
design documents and code against the standards and providing
specific guidance when it detects violations. For code security
reviews, configure AWS Security Agent to monitor repositories and
analyze pull requests so evaluation scales across codebases while
keeping oversight on critical issues.

AI-generated code needs extra scrutiny. AI coding assistants
introduce vulnerability patterns that differ from typical
human-written code (hallucinated API calls, insecure default
configurations, outdated dependency usage), and scanning tools
need to flag these explicitly. Tools like Claude Code Security use
multi-stage verification where findings are re-examined to prove
or disprove results and filter out false positives before they
reach analysts, which reduces noise and lets teams focus on
validated issues.

### Implementation steps

- **Codify security requirements
centrally:** Define organizational security
requirements (approved libraries, logging standards, data
access policies) and configure them in
[AWS Security Agent](https://aws.amazon.com/security-agent/) for automated enforcement across
development teams.
- **Run design-phase reviews:**
Configure AWS Security Agent to analyze architecture
documents and technical specifications before development
begins.
- **Enable PR-level code
review:** Connect AWS Security Agent to your code
repositories to cover both human-written and AI-generated
code on every pull request.
- **Configure multi-stage
verification:** Set up AI-powered scanning with
multi-stage verification to reduce false positives and
assign severity ratings to validated findings.
- **Triage and track to
resolution:** Route validated vulnerabilities to
the appropriate team with remediation guidance, and track
findings through to resolution.

## Resources

**Related best practices:**

- [AGENTSEC07-BP05
Regular security assessments and red teaming](agentsec07-bp05.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)
- [AGENTSEC09-BP02 Conduct
context-aware penetration testing with multi-agent attack
simulation](agentsec09-bp02.html)

**Related documents:**

- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [Security
Considerations for AWS Security Agent and AI assisted
penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html)
- [Claude
Code Security, Making frontier cybersecurity capabilities
available to defenders](https://www.anthropic.com/news/claude-code-security)
- [OWASP
Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon CodeGuru Security](https://aws.amazon.com/codeguru/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp01.html*

---

# AGENTSEC09-BP02 Conduct context-aware penetration testing with multi-agent attack simulation

Generic scanners miss vulnerabilities that only surface in agent
orchestration, tool parameter construction, and inter-agent
delegation. Context-aware testing driven by specialized attacker
agents that adapt to what the application reveals finds the chained
exploits that static scripts can't reach.

**Desired outcome:**

- You use context-aware, multi-agent attack simulation for
penetration testing that adapts to the specific application
under test.
- The testing system develops deep understanding of the
application's architecture, data flows, and agent interactions,
then executes sophisticated attack chains combining multiple
vulnerability types.
- Findings are validated through actual exploitation, prioritized
by real-world exploitability, and documented with reproducible
attack paths and ready-to-implement fixes.

**Common anti-patterns:**

- Running generic vulnerability scanners against agentic AI
systems without adapting test scenarios to the agent's specific
capabilities and tool integrations, missing tool parameter
injection, memory poisoning, and delegation-chain privilege
escalation.
- Testing individual agent components in isolation without
exercising multi-agent coordination paths, missing trust
boundary violations and cascading failures from a compromised
agent in an orchestration chain.
- Relying on predefined test scripts that don't adapt based on
application responses, missing vulnerabilities that require
dynamic exploration because agentic systems behave differently
based on context and prior interactions.

**Benefits of establishing this best
practice:**

- Context-aware testing adapts to the specific application,
discovering vulnerabilities that static test scripts and generic
scanners miss.
- Actual exploitation validates findings, reducing false positives
and letting teams prioritize based on real risk.
- Specialized agents collaborate on reconnaissance, vulnerability
analysis, exploit validation, and finding prioritization,
identifying chained vulnerabilities that combine information
disclosure with privilege escalation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Penetration testing that chases agent vulnerabilities has to look
like the attack it is simulating. Attacker agents don't run the
same script on every target. They map the surface, probe for
weaknesses, adapt to responses, and chain findings. Testing tools
need to do the same or they miss exactly the scenarios that matter
most for agentic systems.

A multi-agent penetration testing system orchestrates specialized
security agents collaboratively. The system begins with baseline
scanning to establish coverage, then conducts broad reconnaissance
to map the application surface and identify initial attack
vectors. Building on these findings, it dynamically generates
focused test tasks tailored to the specific application context,
reasoning about discovered endpoints, business logic patterns, and
potential vulnerability chains.

[AWS Security Agent](https://aws.amazon.com/security-agent/) provides on-demand penetration testing with
this multi-agent approach. It deploys specialized AI agents that
develop application context from provided documentation and
credentials, then execute attack chains to identify complex
vulnerabilities conventional tools miss. The architecture includes
agents for attack surface mapping, business logic analysis,
finding validation, and vulnerability prioritization based on
actual exploitability scored using the Common Vulnerability
Scoring System (CVSS). The system performs chained attacks,
combining an information disclosure flaw with privilege escalation
to reach sensitive resources, or chaining insecure direct object
references with authentication bypass, rather than stopping at
single-vulnerability detection.

AWS Security Agent starts with the OWASP Top 10 and then
customizes its approach based on the context it learns from
documents and code. The agent adapts to the responses it receives,
building a custom attack plan for each application. Provide target
URLs, authentication details, source code, and documentation so
the agent can develop deep application understanding before
testing begins.

Agent-specific scenarios need manual supplementation. Prompt
injection chains across agent boundaries, tool parameter
manipulation, memory poisoning through crafted tool outputs, and
human-in-the-loop bypass techniques all require scenarios that go
beyond the OWASP baseline. Use the findings from AGENTSEC07-BP05
to inform the scenario library.

### Implementation steps

- **Provide application context to the
testing agent:** Configure
[AWS Security Agent](https://aws.amazon.com/security-agent/) with target application details
including URLs, authentication credentials (stored in AWS Secrets Manager), source code, and architecture
documentation.
- **Run tests across the full
surface:** Execute on-demand penetration tests that
exercise agent orchestration endpoints, tool invocation
paths, and multi-agent communication channels.
- **Triage validated findings by
exploitability:** Review findings with reproducible
attack paths, impact analysis, and suggested code fixes, and
prioritize remediation based on CVSS scores and actual
exploitability.
- **Add agent-specific scenarios
manually:** Supplement automated testing with
scenarios targeting prompt injection chains, tool parameter
manipulation, and multi-agent trust boundary violations.
- **Track posture over time:**
Store penetration test results and compare them across test
cycles to measure security posture improvement.

## Resources

**Related best practices:**

- [AGENTSEC07-BP05
Regular security assessments and red teaming](agentsec07-bp05.html)
- [AGENTSEC02-BP02
Validate tool inputs and outputs](agentsec02-bp02.html)
- [AGENTSEC09-BP01
Integrate AI-powered vulnerability scanning across the
development lifecycle](agentsec09-bp01.html)

**Related documents:**

- [Inside
AWS Security Agent: A multi-agent architecture for automated
penetration testing](https://aws.amazon.com/blogs/security/inside-aws-security-agent-a-multi-agent-architecture-for-automated-penetration-testing/)
- [AWS Security Agent FAQs](https://aws.amazon.com/security-agent/faqs/)
- [Security
Considerations for AWS Security Agent and AI assisted
penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html)
- [OWASP
Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

**Related services:**

- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp02.html*

---

# AGENTSEC09-BP03 Implement continuous security validation with automated remediation

Periodic assessments leave newly deployed agent capabilities exposed
for weeks or months. On-demand validation integrated into the
development pipeline, paired with automated fix suggestions,
compresses the discovery-to-resolution loop from weeks to hours.

**Desired outcome:**

- You run security validation continually or on-demand as part of
the development and deployment pipeline rather than only during
periodic assessment windows.
- Validated findings arrive with ready-to-implement code fixes and
configuration recommendations, so development teams remediate
issues without waiting for security team intervention.
- You track remediation progress automatically, and regression
testing confirms fixes are effective and don't introduce new
vulnerabilities.

**Common anti-patterns:**

- Limiting penetration testing to annual or quarterly cycles,
leaving newly deployed agent capabilities untested for long
periods because agentic systems evolve rapidly with new tool
integrations and capability expansions.
- Delivering vulnerability findings without practical remediation
guidance, creating a bottleneck where development teams wait for
security expertise to understand how to fix issues.
- Treating remediation as separate from discovery, losing context
between the team that identified the issue and the team that
must fix it and leading to incomplete fixes that address
symptoms rather than root causes.

**Benefits of establishing this best
practice:**

- On-demand testing validates security whenever new capabilities
are deployed or significant changes are made, compressing the
exposure window.
- Automated fix suggestions give development teams
ready-to-implement code changes, closing the loop between
discovery and resolution.
- Automated re-testing confirms fixes are effective and don't
introduce new vulnerabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The value of security validation is proportional to how fast it
runs relative to how fast the application changes. Quarterly
testing against a code base that changes weekly leaves most of the
application untested most of the time, and agentic systems change
faster than traditional applications because new tool integrations
and capability expansions ship continuously. Integrating
validation into CI/CD pipelines so it runs on every significant
change keeps testing coverage aligned with application evolution.

Configure triggers for on-demand testing when new agent
capabilities are added, tool integrations are modified, or
permission boundaries are changed.
[AWS Security Agent](https://aws.amazon.com/security-agent/) transforms penetration testing from a
weeks-long manual process into an on-demand capability that
completes in hours. Each validated finding carries impact
analysis, a reproducible attack path, and a ready-to-implement
code fix, which is what lets development teams remediate without
waiting for specialized security expertise. Security teams define
organizational requirements once and AWS Security Agent validates
them during every design and code review, providing consistent
enforcement at scale.

Remediation tracking monitors fix progress from discovery through
resolution. Store test results and remediation status in a
centralized system, and configure automated regression testing
that re-runs relevant test scenarios after fixes are applied to
confirm effectiveness. Amazon CloudWatch captures the security
validation metrics that matter: time-to-detection,
time-to-remediation, and fix effectiveness rates.

Agentic systems need validation triggers that traditional
applications don't. Trigger security validation whenever agent
system prompts are modified, new tools are registered, permission
scopes are changed, or multi-agent orchestration patterns are
updated. These changes introduce vulnerabilities that are not
caught by standard code-level scanning because they affect agent
behavior at the reasoning and orchestration layer.

### Implementation steps

- **Wire validation into
CI/CD:** Integrate
[AWS Security Agent](https://aws.amazon.com/security-agent/) into CI/CD pipelines with triggers for
on-demand security validation when agent capabilities, tool
integrations, or permission boundaries change.
- **Run code and design review on every
PR:** Configure automated code and design security
reviews that run on every pull request, giving developers
real-time feedback during development.
- **Route findings with fixes to
owners:** Establish a remediation workflow that
routes validated findings with suggested code fixes to the
appropriate development team and tracks progress to
resolution.
- **Re-test after fixes
automatically:** Implement regression testing that
re-runs relevant security test scenarios after fixes are
applied to confirm effectiveness.
- **Measure and improve:**
Monitor security validation metrics (time-to-detection,
time-to-remediation, fix effectiveness) in Amazon CloudWatch
and review trends to identify process improvements.

## Resources

**Related best practices:**

- [AGENTSEC09-BP01
Integrate AI-powered vulnerability scanning across the
development lifecycle](agentsec09-bp01.html)
- [AGENTSEC09-BP02 Conduct
context-aware penetration testing with multi-agent attack
simulation](agentsec09-bp02.html)
- [AGENTSEC07-BP05
Regular security assessments and red teaming](agentsec07-bp05.html)

**Related documents:**

- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [AWS Security Agent FAQs](https://aws.amazon.com/security-agent/faqs/)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp03.html*

---

# AGENTSEC09-BP04 Establish scoped and controlled testing environments for agent security assessments

Penetration testing that runs real exploit attempts against
production agents can trigger tool calls, corrupt memory, or expose
sensitive data. Scoped test environments with dedicated credentials
and isolated agent state let teams run thorough assessments without
risking production impact.

**Desired outcome:**

- You conduct security assessments for agentic AI systems in
controlled environments with clearly defined scope, dedicated
credentials, and isolation from production systems.
- You manage test credentials through secure vaulting services
with automatic rotation, and testing activities are logged in
your account for full auditability.
- The testing environment replicates production agent behavior
closely enough to produce valid findings while containing the
scope of exploit attempts.

**Common anti-patterns:**

- Running penetration tests directly against production agentic
systems without scope controls, risking agents executing tool
calls against production databases, sending messages to real
users, or triggering downstream workflows in response to test
inputs.
- Using shared or long-lived credentials for security testing,
creating credential exposure risk where test credentials could
be captured in logs, test artifacts, or finding reports.
- Not isolating test agent instances from production agent memory
and state, letting test inputs and attack payloads pollute
production agent memory and influence future agent behavior for
real users.

**Benefits of establishing this best
practice:**

- Environment isolation allows thorough security assessment,
including real exploit attempts, without risking production
impact or data corruption.
- Vaulting services limit credential exposure during testing and
support automatic rotation after assessment cycles.
- Test logs stored in your account provide full visibility into
testing activities for compliance and incident investigation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

An agent under security test is an agent executing exploit
attempts. In production, an agent running an exploit payload will
actually call the tool it was told to call, send the email it was
told to send, and write to the memory it was told to modify. The
containment requirement is therefore structural: the test
environment needs to look enough like production to produce valid
findings, and it needs to be separated enough from production that
exploit attempts can't reach real resources.

Provision dedicated testing environments that replicate the agent
architecture, tool integrations, and data flows of production
while maintaining isolation. Use separate agent instances with
their own memory stores, tool endpoints, and permission
boundaries. Configure test environments to use mock or sandboxed
versions of external services where full production connectivity
isn't required for valid testing results.

Manage test credentials through AWS Secrets Manager, storing
static credentials (username and password) securely and supporting
dynamic credential provisioning through AWS Lambda functions for
more complex authentication scenarios.
[AWS Security Agent](https://aws.amazon.com/security-agent/) supports both static credentials stored in
AWS Secrets Manager and dynamic credentials accessed through AWS Lambda functions, giving flexible authentication that adapts to
different application architectures. Rotate test credentials after
each assessment cycle and audit credential access logs to detect
any unauthorized usage.

Scope definition is a precondition, not an afterthought. Specify
before each assessment which agent endpoints, tool integrations,
and data stores are in scope and which are explicitly excluded.
For AWS Security Agent penetration testing, provide target URLs,
authentication details, source code, and documentation so the
agent can develop application context within the defined scope.
All test logs are stored in Amazon CloudWatch in your account for
full visibility.

For multi-agent systems, test agent-to-agent communication paths
in isolation before testing the full orchestration chain. That
approach identifies trust boundary violations and delegation
issues at the individual interaction level before they compound in
complex multi-agent scenarios. Network segmentation and IAM
policies help prevent test agent instances from reaching
production resources.

### Implementation steps

- **Provision isolated test
environments:** Replicate production agent
architecture with isolated memory stores, tool endpoints,
and permission boundaries.
- **Manage credentials in Secrets Manager:** Store test credentials in AWS Secrets Manager with automatic rotation policies, or use AWS Lambda
functions for dynamic credential provisioning for complex
authentication scenarios.
- **Define and document test
scope:** Specify in-scope agent endpoints, tool
integrations, and data stores for each assessment, with
explicit exclusions for sensitive production resources.
- **Contain the scope at the network and
IAM layers:** Configure network segmentation and
IAM policies that help prevent test agent instances from
accessing production resources.
- **Verify test logging in
CloudWatch:** Confirm all test logs are captured in
Amazon CloudWatch in your account, and review logs after
each assessment to confirm scope adherence and identify
unintended interactions.

## Resources

**Related best practices:**

- [AGENTSEC09-BP02 Conduct
context-aware penetration testing with multi-agent attack
simulation](agentsec09-bp02.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [Security
Considerations for AWS Security Agent and AI assisted
penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html)
- [AWS Security Agent FAQs](https://aws.amazon.com/security-agent/faqs/)
- [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [AWS Well-Architected Framework, Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

**Related services:**

- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp04.html*

---

# AGENTSEC09-BP05 Implement runtime threat detection, security event correlation, and automated remediation for agents

Scanning finds latent weaknesses. Runtime detection catches the
attacks happening now. Correlating events across agent interaction
surfaces and triggering automated remediation compresses the gap
between an active exploit and the response that contains it.

**Desired outcome:**

- You continually monitor security events from agent activity,
correlate them across interaction surfaces, and analyze them for
multi-step attack sequences.
- You detect active threats targeting agentic systems within
minutes, with critical attack sequences surfaced at the highest
severity.
- Automated remediation workflows trigger containment actions and
generate ready-to-implement fixes, reducing mean time to
detection and mean time to remediation.
- Security teams have a unified view of agent-related threats
alongside findings from vulnerability scanning and penetration
testing.

**Common anti-patterns:**

- Treating agent security events in isolation rather than
correlating them across interaction surfaces, missing multi-step
attack sequences where individual events look benign but
together constitute a coordinated attack.
- Relying on pre-deployment vulnerability scanning alone without
runtime threat detection, leaving a gap where vulnerabilities
introduced through configuration drift, new tool integrations,
or novel attack techniques go undetected until the next
scheduled assessment.
- Generating security alerts without automated remediation
workflows, creating alert fatigue where security teams are
overwhelmed by findings but lack the tooling to act quickly.
- Not correlating penetration testing findings with runtime threat
detection signals, missing the connection between known
vulnerabilities and active exploitation attempts that together
provide a high-confidence remediation prioritization signal.

**Benefits of establishing this best
practice:**

- AI/ML-powered event correlation identifies coordinated attacks
spanning multiple agent interaction surfaces, time periods, and
resources.
- Automated workflows trigger containment actions and generate fix
recommendations when threats are detected, closing the loop
between detection and response.
- Centralized findings from vulnerability scanning, penetration
testing, and runtime threat detection enable risk-based
prioritization across the full threat lifecycle.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Scanning and penetration testing find weaknesses before exploit.
Runtime detection catches the exploit as it happens. Both are
necessary because neither alone is sufficient. An agentic system
adds surface area (tools, APIs, memory stores, other agents) that
is exploited through prompt injection chains, credential misuse,
data exfiltration sequences, and privilege escalation paths.
Detection has to correlate across that surface, not treat each
channel in isolation.

Deploy Amazon GuardDuty across all accounts where agents operate
to provide continuous threat detection for agent IAM roles, API
activity, and data access patterns.
[GuardDuty
Extended Threat Detection](https://aws.amazon.com/blogs/aws/introducing-amazon-guardduty-extended-threat-detection-aiml-attack-sequence-identification-for-enhanced-cloud-security/) correlates security signals to
identify active attack sequences (privilege discovery followed by
API manipulation, persistence activities, and data exfiltration)
and surfaces them as critical-severity attack sequence findings
with natural language summaries, MITRE ATT&CK mapping, and
prescriptive remediation recommendations.

For agent-specific threat detection, configure GuardDuty
monitoring across the data sources most relevant to agentic
workloads:

- AWS CloudTrail management events for API call patterns
- Amazon VPC Flow Logs for network behavior
- DNS logs for command-and-control detection
- Amazon S3 data events for data access monitoring

Enable GuardDuty Runtime Monitoring for compute resources running
agent workloads to detect threats at the operating system level,
including suspicious process execution and network connections.

AWS Security Hub CSPM is the aggregation layer. Findings from Amazon GuardDuty (runtime threats),
[AWS Security Agent](https://aws.amazon.com/security-agent/) (vulnerability scanning and penetration
testing), Amazon Macie (sensitive data exposure), and Amazon Inspector (software vulnerability scanning) normalize into the AWS
Security Finding Format (ASFF) for consistent prioritization and
automated response regardless of source. Security Hub CSPM insights
correlate penetration testing findings with runtime detection
signals, identifying cases where known vulnerabilities are being
actively exploited (a high-confidence prioritization signal).

Amazon EventBridge rules trigger AWS Lambda functions or AWS Step Functions workflows when high-severity findings are generated. For
agent-specific threats, the remediation workflow captures forensic
state (agent memory, active sessions, recent tool invocations) to
Amazon S3, applies containment actions (credential revocation,
network isolation) as described in AGENTSEC07-BP04, generates
remediation recommendations based on the finding type, and creates
tracked remediation tasks. Findings from AWS Security Agent
penetration testing that include suggested code fixes route
directly to development teams through the existing remediation
tracking workflow.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) adds a complementary
detection layer. Continuous evaluation scoring detects behavioral
drift that precedes or accompanies security incidents. A sudden
drop in safety or correctness scores combined with a GuardDuty
finding for the same agent is a high-confidence signal that
warrants immediate investigation. Amazon CloudWatch composite
alarms triggered when both evaluation score degradation and a
GuardDuty finding occur within the same time window surface those
cases automatically.

### Implementation steps

- **Enable GuardDuty across agent
accounts:** Turn on Amazon GuardDuty with
monitoring configured for AWS CloudTrail events, Amazon VPC
Flow Logs, DNS logs, Amazon S3 data events, and GuardDuty
Runtime Monitoring for agent compute resources.
- **Centralize findings in Security Hub CSPM:** Aggregate findings from Amazon GuardDuty,
[AWS Security Agent](https://aws.amazon.com/security-agent/), Amazon Macie, and Amazon Inspector in
AWS Security Hub CSPM, and configure Security Hub CSPM insights to
correlate penetration testing findings with runtime threat
detection signals.
- **Automate containment on
high-severity findings:** Use Amazon EventBridge
rules and AWS Lambda functions to trigger containment
actions and generate fix recommendations when high-severity
findings are generated.
- **Combine evaluation drift with
GuardDuty findings:** Configure Amazon CloudWatch
composite alarms that combine
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) score degradation with
GuardDuty findings to surface high-confidence threat
signals.
- **Route fixes to developers and
measure MTTR:** Route remediation recommendations,
including code fixes from AWS Security Agent, to development
teams through a tracked workflow, and monitor mean time to
detection and mean time to remediation as key security
metrics.
- **Tune detection quarterly:**
Review detection rules, remediation workflows, and finding
correlation logic quarterly based on observed threat
patterns and false positive rates.

## Resources

**Related best practices:**

- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)
- [AGENTSEC09-BP01
Integrate AI-powered vulnerability scanning across the
development lifecycle](agentsec09-bp01.html)
- [AGENTSEC09-BP02 Conduct
context-aware penetration testing with multi-agent attack
simulation](agentsec09-bp02.html)

**Related documents:**

- [Amazon GuardDuty Extended Threat Detection](https://aws.amazon.com/blogs/aws/introducing-amazon-guardduty-extended-threat-detection-aiml-attack-sequence-identification-for-enhanced-cloud-security/)
- [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [AWS Security Hub CSPM documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
- [Automate
cloud security vulnerability assessment and alerting using
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/automate-cloud-security-vulnerability-assessment-and-alerting-using-amazon-bedrock/)
- [How
government agencies can transform cybersecurity operations
with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/publicsector/how-government-agencies-can-transform-cybersecurity-operations-with-amazon-bedrock-agentcore/)
- [AWS Security Agent](https://aws.amazon.com/security-agent/)

**Related services:**

- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon Macie](https://aws.amazon.com/macie/)
- [Amazon Inspector](https://aws.amazon.com/inspector/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp05.html*

---
