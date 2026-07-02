# AGENTSEC03 — Agent identity and permission management

**Pillar**: Security  
**Best Practices**: 4

---

# AGENTSEC03-BP01 Implement strong authentication for agent identities

Shared API keys and one-way TLS give agents enough network
reachability to be useful and enough ambiguity to be impersonated.
Cryptographic identity for both sides of every call, with automated
lifecycle and immediate revocation, is the control that makes every
agent communication auditable and reversible.

**Desired outcome:**

- You authenticate all agent-to-agent and agent-to-service
communications using strong cryptographic mechanisms, with
mutual authentication that helps prevent impersonation and
interception.
- You automate certificate lifecycle management so expired
certificates don't cause authentication failures or security
gaps.
- You can revoke affected agent identities immediately, cutting
off unauthorized access within minutes.

**Common anti-patterns:**

- Using shared API keys or static tokens for agent authentication
instead of certificate-based or OAuth mechanisms, producing
credentials that are hard to rotate and straightforward to
exfiltrate.
- Implementing one-way TLS (server authentication only) without
mutual authentication, so any client on a permitted network path
can reach the endpoint without proof of its agent identity.
- Managing certificate lifecycles manually, leading to expired
certificates that either cause outages or are renewed without
proper security review.

**Benefits of establishing this best
practice:**

- Certificate-based or OAuth authentication provides cryptographic
proof of identity for both parties in every agent communication.
- Automated certificate lifecycle management reduces the risk of
expired certificates causing outages or security gaps.
- CRL and OCSP revocation provides the ability to cut off
unauthorized access within minutes when an agent identity is
affected.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Authentication for agents has two distinct jobs: proving the agent
is who it claims to be, and proving that to the receiver
cryptographically rather than through network-path heuristics.
Static credentials fail both tests. They are trivial to copy, hard
to rotate, and their holder is indistinguishable from their
issuer. The design pattern is cryptographic identity managed
centrally, with lifecycle automation and revocation as first-class
operations rather than afterthoughts.

[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) handles the OAuth side of that
pattern. It provides managed OAuth 2.0 flows and identity
federation for agentic workloads, issuing, validating, and
rotating tokens without the operational burden of running that
infrastructure. Each agent registers in the centralized agent
identity directory and receives a unique identity. The
GetWorkloadAccessTokenForJWT API issues
agent-specific access tokens bound to the requesting agent's
identity. The token vault secures OAuth tokens with AWS KMS
encryption (customer-managed keys supported) and enforces
per-agent access controls so one agent can't retrieve another's
tokens.

For services that require certificate-based authentication rather
than OAuth, AWS Private Certificate Authority (AWS Private CA) is
the managed path for issuing internal mTLS client and server
certificates. AWS Private CA handles issuance and supports
automated renewal lifecycles, and certificate revocation through
CRL or OCSP provides the cutoff when an identity is affected.
Mutual TLS (mTLS) on AWS Application Load Balancers or Amazon API Gateway configurations gives agent-to-agent traffic symmetric
proof: both sides present certificates, both sides verify. Private
keys live in AWS Secrets Manager or Parameter Store, a capability
of AWS Systems Manager with AWS KMS encryption at rest and
automatic rotation policies, so the key itself never becomes a
long-lived static credential.

Detection rounds out the pattern. Amazon GuardDuty flags unusual
authentication patterns, agents authenticating from unexpected IP
addresses or at unusual times, and findings route into AWS Security Hub CSPM for centralized event management. That gives the
security team a single place to see when an identity is being used
in ways that don't match its normal profile, whether the
credentials themselves have been revoked.

### Implementation steps

- **Deploy AgentCore
Identity:** Deploy
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) for agent authentication,
configure identity federation for cross-service access, and
register each agent in the centralized identity directory
for unique, trackable identities.
- **Secure tokens in the
vault:** Configure the AgentCore Identity token
vault for OAuth token storage using customer-managed AWS KMS
keys for encryption, and enforce strict per-agent access
controls for credential retrieval.
- **Issue agent certificates from AWS Private CA:** Set up AWS Private Certificate Authority for agent identity certificates, with automated
renewal lifecycles configured.
- **Enforce mutual TLS
end-to-end:** Configure mTLS on all agent-to-agent
communication endpoints through Application Load Balancers
or Amazon API Gateway with mTLS authentication.
- **Store keys in Secrets Manager with
rotation:** Store all agent private keys and
credentials in AWS Secrets Manager with encryption at rest
and automatic rotation policies enabled.
- **Turn on revocation
checking:** Implement certificate revocation
through CRL or OCSP so affected agent certificates can be
invalidated immediately.
- **Alarm on authentication
anomalies:** Configure Amazon GuardDuty to detect
unusual authentication patterns and route findings to AWS Security Hub CSPM for centralized security event management.
- **Review certificate inventory
quarterly:** Identify and remediate certificates
approaching expiration or using deprecated algorithms on a
quarterly cadence.

## Resources

**Related best practices:**

- [AGENTSEC03-BP02 Separate
agent and human user permission](agentsec03-bp02.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC06-BP01
Encrypt and sign inter-agent messages](agentsec06-bp01.html)

**Related documents:**

- [Securing
AI agents with Amazon Bedrock AgentCore Identity](https://aws.amazon.com/blogs/security/securing-ai-agents-with-amazon-bedrock-agentcore-identity/)
- [Amazon
Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html)
- [AgentCore
Identity supported authentication patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/common-use-cases.html)
- [AWS Private CA documentation](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Private CA](https://aws.amazon.com/private-ca/)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp01.html*

---

# AGENTSEC03-BP02 Separate agent and human user permission

Identity propagation alone isn't enough when agents act on behalf of
users. Distinct agent service identities, with hard trust boundaries
helping prevent assumption of human-designated roles, keep audit
attribution unambiguous and stop a misconfigured agent from
escalating into a human identity space.

**Desired outcome:**

- Agent actions and human actions are distinguishable in audit
logs, with separate identities that help prevent agents from
inheriting or assuming human user permissions.
- Dedicated agent service identities are scoped to only the
permissions required for automated operations, and audit logs
attribute every action unambiguously to either an agent or a
human actor.
- Trust policies help prevent agents from assuming
human-designated identities, with organization-level guardrails
providing a secondary boundary in multi-account environments.

**Common anti-patterns:**

- Reusing human user IAM credentials or roles for agent
authentication, making it impossible to distinguish agent
actions from human actions in audit logs.
- Allowing agents to assume human IAM roles through role chaining,
enabling access to resources that should be restricted to human
users and creating a privilege-escalation path.
- Using a single shared service account for multiple agents,
reducing the risk of attribution of specific actions to
individual agents and complicating incident response.
- Relying only on agent-level IAM policies without role trust
policy restrictions or multi-account guardrails, leaving open
the assumption path where an affected agent role could still
assume a human role.

**Benefits of establishing this best
practice:**

- Separate identities produce unambiguous audit attribution that
clearly distinguishes agent actions from human actions.
- Trust policies refuse assumption by agent principals, with
optional organization-level guardrails adding a multi-account
ceiling.
- Consistent agent identity tagging and naming conventions enable
filtering and analysis of agent activity patterns during
incident investigations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Two separations matter here and they are often collapsed in
practice. Identity separation means the agent operates under a
service identity distinct from any human identity, whether that
human is an operator managing AWS resources or an application user
interacting with the agent's service. Permission separation means
the agent's identity carries only the permissions it needs for its
tasks and never inherits the permissions of human identities.
These apply to both patterns (agents acting autonomously and
agents acting on behalf of a user), but the way user context flows
through a call differs: autonomous agents operate under their
service identity alone, while agents acting on behalf of a user
carry that user's context forward as token claims without the
agent ever assuming the user's credentials. Human operator
identities (which authenticate through IAM Identity Center for AWS
access) and application user identities (which authenticate
through a separate customer-facing identity provider and have no
AWS identity at all) are themselves distinct layers.

For agents that operate on AWS, create dedicated IAM roles for
each agent type as the agent's service identity, with a naming
convention (for example,
agent-role-) that
distinguishes them from human operator roles, and apply
PrincipalType: Agent as a consistent tag.
Principal tags surface in AWS CloudTrail events primarily for
management-plane API calls made with session tags. For
service-specific events that don't surface principal tags, filter
by the agent role ARN naming convention as the primary signal and
treat the tag as a secondary filter. Use AWS IAM Identity Center
for all human operator access and migrate any human operators
still using account-specific IAM users off those identities.
Application users are typically outside this migration, they
authenticate through the application's own identity provider, and
their identity flows into agent calls as token claims. Configure
Service Control Policies (SCPs) in AWS Organizations that
explicitly deny agents (identified by tag) from assuming roles in
the human operator identity boundary, for example denying
sts:AssumeRole for any principal tagged as an
agent attempting to assume roles tagged as human-operator.

Amazon Bedrock AgentCore introduces two identity constructs that
support this separation. The AgentCore Runtime
**execution role** is a regular IAM
role assumed by the Runtime process to reach AWS services the
agent depends on (model invocations, tool calls to AWS APIs,
memory reads and writes). The AgentCore
**Workload Identity** is an
agent-specific identity registered in the AgentCore Identity
directory, distinct from any IAM role, and used to issue and
verify agent-scoped tokens and vault third-party tokens obtained
on behalf of users. When an agent acts on behalf of an application
user, it calls GetWorkloadAccessTokenForJWT
with the user's access token from the application's identity
provider.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) verifies the user token and
returns an agent-specific workload access token that embeds the
user context as claims, so the call chain carries both "who
the agent is" and "who the user is" without
the agent ever assuming the user's credentials or an IAM role on
the user's behalf.

For agents that need to reach third-party OAuth resources on
behalf of users, AgentCore Identity orchestrates the authorization
code grant flow and secures the resulting access tokens in a token
vault scoped per agent identity and per user. One agent can't
retrieve tokens obtained for a different user, and as long as the
third-party access token remains valid the agent can retrieve it
from the vault without requiring the user to re-authenticate.

Amazon Cognito provides an alternative for organizations already
standardized on Cognito user pools. The same principle (the agent
carries both its own identity and the user's context as token
claims) can be implemented outside AgentCore Identity. The pattern
described in
[Empower
AI agents with user context using Amazon Cognito](https://aws.amazon.com/blogs/security/empower-ai-agents-with-user-context-using-amazon-cognito/) uses
[Amazon Cognito](https://aws.amazon.com/cognito/) user pools: the agent authenticates through the
client credentials flow while passing the user's token as
additional context through the
aws_client_metadata request parameter, and a
[pre-token-generation
Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) verifies the user token and injects an
onBehalfOf claim into the agent's access token
before issuance. The resulting JWT identifies the agent in its
sub claim and the user in its
onBehalfOf claim, producing a single token that
downstream authorization layers can evaluate. This is a custom
extension built on Cognito trigger hooks, not a native Cognito
feature, and it complements the AgentCore pattern rather than
replacing it. For authorization on top of the resulting token,
resource servers can evaluate claims directly, or externalize
policy to a service such as
[Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/) using Cedar (a choice orthogonal to
whether you use AgentCore Identity or the Cognito pattern).

When an agent invokes a tool through AgentCore Gateway, the
gateway operates under its own execution role (one per gateway)
and the outbound authentication applied to the target depends on
the target type (see the
[AgentCore
Gateway outbound auth reference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html) for details). User context
propagates through the gateway so downstream services can enforce
user-level authorization, and the gateway never substitutes an IAM
identity for the user or re-authenticates as the user against
downstream services.

Configure
[CloudTrail
with advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) to capture agent API calls,
including data events for agent-invoked services where visibility
beyond management-plane events matters. Enable AgentCore data
events so operations against AgentCore Memory, Gateway, and
Runtime are logged alongside management-plane events. Amazon CloudWatch Logs Insights queries filtered by agent role ARN
patterns give dedicated agent activity dashboards. For SQL-based
analysis over time, deliver CloudTrail logs to Amazon S3 and query
them with Amazon Athena (see AGENTSEC05-BP01).

For multi-agent systems where a parent agent directly assumes a
sub-agent's IAM role (for example, calling
sts:AssumeRole before invoking the sub-agent in
the same account), use role session names that include the parent
agent's identifier so the chain is visible in CloudTrail. For A2A
communication that routes through AgentCore Runtime, each agent
runs under its own independent execution role session and there is
no IAM role chain. Use correlation identifiers propagated through
the A2A message (see AGENTSEC05-BP02) to reconstruct the
agent-to-agent call graph.

### Implementation steps

- **Audit and rename agent
roles:** Identify any IAM roles shared between
agents and human users, and create dedicated agent-specific
roles with a consistent naming convention (for example,
agent-role-).
- **Tag agent roles
consistently:** Apply
PrincipalType: Agent and
AgentName: tags to every
agent IAM role for filtering and monitoring.
- **Move human operators to IAM Identity Center:** Configure AWS IAM Identity Center for all
human operator access and migrate any operators still on
account-specific IAM users.
- **Enforce the agent-to-human boundary
through SCPs:** Deploy Service Control Policies in
AWS Organizations that deny agents (identified by tag) from
assuming human-operator roles, creating a hard boundary
between the identity spaces.
- **Register Workload Identities for
on-behalf-of flows:** Register agent Workload
Identities in
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) for agents that act on
behalf of users, and use
GetWorkloadAccessTokenForJWT to create
agent-scoped tokens that embed user context as claims for
downstream authorization.
- **Enable CloudTrail with AgentCore
data events:** Turn on advanced event selectors
including AgentCore data events, and build Amazon CloudWatch Logs Insights queries filtered by agent role ARN patterns
for dedicated agent activity dashboards.
- **Analyze with Athena over
time:** Deliver AWS CloudTrail logs to Amazon S3
and use Amazon Athena for SQL-based analysis of agent
compared to human activity patterns over time for compliance
reporting and long-term trend analysis.
- **Name sessions for
attribution:** Implement role session naming
conventions that include agent identifiers (and parent agent
identifiers for delegation chains) for clear attribution in
multi-agent systems.

## Resources

**Related best practices:**

- [AGENTSEC03-BP01
Implement strong authentication for agent identities](agentsec03-bp01.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)

**Related documents:**

- [AWS CloudTrail best practices](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html)
- [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Securing
AI agents with Amazon Bedrock AgentCore Identity](https://aws.amazon.com/blogs/security/securing-ai-agents-with-amazon-bedrock-agentcore-identity/)
- [Empower
AI agents with user context using Amazon Cognito](https://aws.amazon.com/blogs/security/empower-ai-agents-with-user-context-using-amazon-cognito/)
- [Amazon
Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html)
- [AgentCore
Identity supported authentication patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/common-use-cases.html)

**Related services:**

- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Organizations](https://aws.amazon.com/organizations/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon Cognito](https://aws.amazon.com/cognito/)
- [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp02.html*

---

# AGENTSEC03-BP03 Implement least privilege with dynamic boundaries

Broad permissions grant an affected agent access well beyond the
task it was asked to do. Scoping privilege at each identity layer,
backing it with temporary credentials, and layering contextual IAM
conditions limits the scope of any single compromised or misprompted
call.

**Desired outcome:**

- Agents operate with the minimum permissions required to complete
their defined tasks, with temporary credentials that expire
automatically and dynamic permission boundaries that tighten
when handling sensitive data or high-risk operations.
- Just-in-time access patterns help limit elevated permissions to
the duration of the operation that requires them.
- You continually validate policy scoping as workloads evolve,
removing drift before it accumulates.

**Common anti-patterns:**

- Assigning broad IAM policies (for example,
s3:* or *) to agent roles
for convenience, granting far more access than any individual
task requires.
- Using long-lived static credentials instead of temporary
credentials from AWS STS, extending the window of exposure if
credentials are inadvertently disclosed.
- Failing to implement IAM permission boundaries, allowing agents
to create or modify IAM policies and escalate their own
privileges.
- Expanding agent permissions in response to access errors without
investigating whether the access pattern is legitimate,
accumulating excessive permissions through reactive grants that
are never revoked.

**Benefits of establishing this best
practice:**

- Least-privilege IAM roles limit an affected agent to only the
resources required for its current task.
- Temporary AWS STS credentials with short session durations
reduce the risk of long-lived credential exposure.
- IAM Conditions on region, resource tags, time windows, and
source network add defense-in-depth that limits the impact of
credential exposure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

An agent operates under multiple identity layers, and each is a
separate place to apply scoping. The **agent
identity** is what this specific agent is as an entity in
your directory (for example, an AgentCore Workload Identity with a
unique ARN). The **service
identity** is what the agent runs as when it invokes AWS
services (for AgentCore Runtime. This is the IAM execution role
assumed by the Runtime process). The
**transaction identity** is the
per-invocation context carried with a single agent call, typically
expressed through AWS STS session credentials with session tags
and session policies. When an agent acts on behalf of a user, a
**user identity** is additionally
carried in the call context as token claims propagated through the
agent's call chain. Permission scoping applies differently at each
layer:

- Broad capability limits belong on the service identity (IAM
role, permission boundary)
- Per-operation constraints belong on the transaction (session
policy, session tags, and IAM Conditions)
- User-context constraints belong on the user identity
(token-based authorization evaluated at the resource)

At the service identity layer, design agent IAM roles using the
principle of least privilege, starting with no permissions and
adding only what is required for each specific task. AWS IAM Access Analyzer generates least-privilege policies based on actual
access patterns observed in AWS CloudTrail logs, giving you a
data-driven baseline for scoping. IAM permission boundaries on all
agent roles establish a maximum permission ceiling that can't be
exceeded even if the agent's policies are modified, which matters
because it is the control that helps prevent privilege escalation
when something about the policy itself changes.

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) operates under a single execution
role per gateway, with outbound authentication that depends on
target type (see the
[AgentCore
Gateway outbound auth reference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html)). Scope the gateway
execution role to only the actions and resources the set of
targets collectively requires, and constrain per-target access
through the target-specific outbound auth configuration. User
context propagated through the gateway lets downstream services
enforce user-level access controls in addition to the
gateway-level role, so operations are further constrained by the
originating user's permissions even if the gateway role has access
to a target.

Temporary credentials are how the transaction layer stays scoped.
AWS STS AssumeRole with session policies generates credentials
scoped to the specific permissions required for each task
execution, and short session durations (15 to 60 minutes) make
expiration automatic. For agents that require elevated permissions
for specific operations, just-in-time access through AWS IAM Identity Center or custom Lambda-based access request workflows
grants and revokes permissions programmatically.

IAM Conditions are the defense-in-depth layer that makes exposed
credentials less useful. aws:RequestedRegion
limits agent actions to approved regions.
aws:ResourceTag restricts access to resources
tagged for agent use. aws:CurrentTime enforces
time-window restrictions. aws:SourceVpc
requires that agent API calls originate from approved VPCs. These
conditions don't reduce the policy's stated permissions, but they
bound the contexts under which those permissions apply. At the
organization level, Service Control Policies in AWS Organizations
establish organization-wide guardrails that apply to all agent
accounts, helping prevent agents from accessing services or
performing actions that are never appropriate regardless of
task-level permissions.

### Implementation steps

- **Generate least-privilege policies
from usage data:** Audit existing agent IAM roles
with AWS IAM Access Analyzer to identify overly permissive
policies and generate least-privilege recommendations based
on actual access patterns in AWS CloudTrail logs.
- **Apply permission
boundaries:** Set IAM permission boundaries on all
agent roles to establish a maximum permission ceiling that
can't be exceeded even if the agent's task-level policies
are modified.
- **Scope the Gateway execution
role:** Restrict the
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) execution role to only the
actions and resources its targets require, configure
target-specific outbound auth per target type, and use
AgentCore Identity to propagate user context for downstream
user-level enforcement.
- **Issue temporary credentials with
session policies:** Use AWS STS AssumeRole with
session policies and short session durations (15 to 60
minutes) for all agent credential issuance.
- **Add contextual IAM
Conditions:** Restrict access by region
(aws:RequestedRegion), resource tags
(aws:ResourceTag), time windows
(aws:CurrentTime), and source network
(aws:SourceVpc).
- **Deploy organization-wide
SCPs:** Establish organization-wide guardrails
through Service Control Policies in AWS Organizations that
apply to all agent accounts.
- **Implement just-in-time access for
elevated permissions:** Use IAM Identity Center or
custom Lambda-based access request workflows with automatic
revocation when the operation completes or the session
expires.
- **Review IAM drift
quarterly:** Schedule IAM Access Analyzer reviews
every quarter to detect permission drift, identify unused
access, and remove permissions that are no longer required.

## Resources

**Related best practices:**

- [AGENTSEC02-BP01
Implement tool authorization](agentsec02-bp01.html)
- [AGENTSEC03-BP01
Implement strong authentication for agent identities](agentsec03-bp01.html)
- [AGENTSEC03-BP02 Separate
agent and human user permission](agentsec03-bp02.html)
- [AGENTSEC03-BP04 Regular
permission audits and access reviews](agentsec03-bp04.html)
- [AGENTREL02-BP02
Limit agent permissions to minimum required access](agentrel02-bp02.html)

**Related documents:**

- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [Amazon
Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html)
- [Amazon
Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html)
- [Service
control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Related services:**

- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [AWS IAM Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/)
- [AWS Organizations](https://aws.amazon.com/organizations/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp03.html*

---

# AGENTSEC03-BP04 Regular permission audits and access reviews

Agent roles accumulate permissions over time. Scheduled automated
analysis paired with periodic human-led reviews catches drift before
it turns into significant over-privilege and produces the documented
audit trail that compliance needs.

**Desired outcome:**

- You continually monitor agent permissions and review them on a
cadence matched to the agent's risk profile, identifying and
removing unused access regularly.
- Automated alerts fire immediately when agent permissions are
modified, enabling rapid detection of unauthorized policy
changes.
- You document access reviews with timestamped findings and
remediation actions for compliance purposes.

**Common anti-patterns:**

- Conducting permission reviews only annually or in response to
incidents, letting drift accumulate undetected for months.
- Setting a single review cadence for every agent regardless of
risk, so high-risk agents (those with broad permissions,
mutating tool access, or production data reach) receive the same
scrutiny as low-risk informational agents.
- Reviewing permissions manually without tooling support, making
it impractical to assess the full scope of agent access across
dozens or hundreds of roles.
- Treating IAM Access Analyzer findings as informational rather
than as practical remediation items, so identified
over-privilege persists indefinitely.
- Not alerting on permission changes in real time, discovering
unauthorized policy modifications only during the next scheduled
review cycle weeks or months later.

**Benefits of establishing this best
practice:**

- Ongoing permission monitoring detects drift before it
accumulates into significant over-privilege.
- Timestamped findings and remediation actions support compliance
requirements and security investigations.
- Usage-based evidence from AWS CloudTrail drives permission
reduction with data rather than guesswork about which
permissions are still needed.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Two review modes are both necessary. Automated analysis provides
speed and coverage, the ability to scan every agent role across
every account every day. Periodic human-led reviews provide the
context that automation can't supply, such as whether a
technically unused permission is still needed for upcoming work,
whether a recent policy change was expected, and whether the
current privilege level matches the current role of the agent in
the business. Running only one of the two leaves a gap: automation
alone produces findings no one acts on, and manual-only reviews
happen too infrequently to catch drift in time.

AWS IAM Access Analyzer at the organization level continually
analyzes agent IAM policies and generates findings for permissions
that grant access to resources outside the intended scope. Its
unused-permissions analysis uses AWS CloudTrail activity data to
identify access that has not been exercised, giving a data-driven
basis for permission reduction rather than a guess. Weekly review
and remediation of Access Analyzer findings, prioritized by
severity, keeps the backlog bounded and turns findings into change
tickets.

AWS Config rules detect changes to agent IAM policies, roles, and
permission boundaries in near real time. Configure managed rules
such as
iam-policy-no-statements-with-admin-access
along with custom rules that validate agent-specific policy
constraints, and route rule violations through Amazon EventBridge
to an Amazon SNS topic so the security team is notified
immediately rather than during the next scheduled review.

For the formal periodic review, correlate Access Analyzer findings
with CloudTrail usage data to identify permissions that have not
been exercised in the period. The review cadence should match the
risk profile of the agent: high-risk agents (those with broad
permissions, write access to production data, or mutating tool
privileges) warrant frequent review, while low-risk informational
agents can be reviewed less often.
[AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) provides queryable long-term retention for
this analysis, and AWS Lambda functions can automate the
generation of review reports by querying IAM and CloudTrail data
and publishing results to Amazon S3. The output feeds the review
meeting and produces the documented evidence compliance requires.

AWS Security Hub CSPM is the aggregation layer for large agent fleets.
Findings from IAM Access Analyzer, AWS Config, and Amazon GuardDuty flow into a single view where severity and business
impact drive prioritization, so the team is working from one list
instead of three consoles.

### Implementation steps

- **Enable organization-level IAM Access Analyzer:** Turn on AWS IAM Access Analyzer at the
organization level and configure it to analyze all agent IAM
roles for unused and overly permissive access.
- **Detect policy changes with AWS Config:** Deploy AWS Config rules to detect changes
to agent IAM policies and trigger Amazon EventBridge
notifications for immediate alerting to the security team.
- **Retain activity data in CloudTrail
Lake:** Configure AWS CloudTrail Lake for long-term
retention of agent API activity data, supporting access
review correlation and compliance reporting.
- **Automate weekly finding
reviews:** Implement automated weekly reviews of
Access Analyzer findings, generating reports that prioritize
high-severity findings for remediation.
- **Run a formal access review on a
risk-based cadence:** Set the review cadence per
agent based on its risk profile (high-risk agents reviewed
frequently, low-risk informational agents reviewed less
often). Correlate Access Analyzer findings with CloudTrail
usage data, document findings and remediation actions, and
record sign-off for each review cycle.
- **Aggregate findings in Security Hub CSPM:** Pull IAM findings from Access Analyzer, AWS Config, and Amazon GuardDuty into AWS Security Hub CSPM for a
unified view of permission-related issues across the agent
fleet.

## Resources

**Related best practices:**

- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC03-BP02 Separate
agent and human user permission](agentsec03-bp02.html)
- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)

**Related documents:**

- [AWS IAM Access Analyzer documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)

**Related services:**

- [AWS IAM Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/)
- [AWS Config](https://aws.amazon.com/config/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp04.html*

---
