# AGENTSEC02 — Secure agent tool usage

**Pillar**: Security  
**Best Practices**: 3

---

# AGENTSEC02-BP01 Implement tool authorization

An agent with unconstrained tool access has no meaningful privilege
boundary. Externally enforced authorization at the gateway, combined
with identity propagation and human review for mutating operations,
enforces bounded autonomy at the tool layer.

**Desired outcome:**

- You authorize every tool invocation against a defined policy
before execution, with agent identity and user context
propagated through the authorization chain.
- Agents can invoke only the tools within their approved scope,
and attempts to access unauthorized tools are blocked and
logged.
- Human-in-the-loop checkpoints intercept high-risk mutating
operations so consequential actions receive review before
execution.

**Common anti-patterns:**

- Granting agents blanket access to every available tool rather
than scoping access to the tools each agent requires.
- Relying on the agent's own judgment to decide whether a tool
invocation is appropriate, with no independent check at the tool
or API layer.
- Failing to propagate user identity context through tool
invocations, so downstream services can't enforce user-level
access controls and every call runs with the agent's
permissions.
- Skipping human-in-the-loop controls for mutating operations
because they add latency, accepting unbounded risk for actions
that are difficult or impossible to reverse.

**Benefits of establishing this best
practice:**

- RBAC policies scope each agent to the tools its defined tasks
require, implementing least-privilege tool access.
- Identity propagation lets downstream services enforce user-level
access controls on resources reached through agent tool calls.
- Rate limiting and human-in-the-loop controls constrain
autonomous execution to operations with acceptable risk
profiles.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Authorization implemented only through prompt instructions is
insufficient because prompts can be manipulated through
adversarial phrasing or prompt injection. Implement authorization
as an external, deterministic check that happens before the tool
executes, regardless of how the agent arrived at the call.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) is the enforcement point, and
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) is the rules engine.

Gateway runs a dual-sided security model. On the inbound side, it
follows the MCP authorization specification and acts as an OAuth
resource server, working with Amazon Cognito, Okta, Auth0, or your
own OAuth provider. You configure approved client IDs and
audiences to control which applications and agents can reach your
tools, and Gateway supports both authorization code flow (3LO) and
client credentials flow (2LO) for service-to-service
communication. On the outbound side, the authentication model
depends on target type: AWS Lambda and Smithy model targets use
IAM-based authorization through a role you configure with scoped
permissions, and OpenAPI targets support API key or OAuth 2LO
client credentials grant.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) resource credentials providers
handle token caching and secure storage, and each target is
associated with exactly one authentication configuration for clear
boundaries and auditability.

Policy is where fine-grained authorization lives. Cedar policies
evaluate every agent-to-tool request at the gateway before
execution, with a default-deny posture where forbid always wins
over permit. Conditions can reference OAuth claims from the JWT
token (user role, scopes, tenant-level identifiers like patient
ID), tool input parameters, and runtime context such as time of
day. That lets you express rules like "role=clinician can
reschedule appointments for patients in their own panel" as
a deterministic policy rather than a hope about the prompt.
Policies can be authored directly in Cedar or generated from
natural language, and Gateway supports a LOG_ONLY mode so you can
validate policy behavior against live traffic before switching to
enforce mode.

Tool overload is its own risk. Presenting an agent with hundreds
of tools increases the chance it selects the wrong one or follows
an inefficient execution path. Gateway's built-in
x_amz_bedrock_agentcore_search tool exposes
semantic tool discovery so agents locate relevant tools through
natural language rather than seeing the full inventory. That
reduces the surface the model reasons across on any given turn.

For tools that perform mutating operations (writes to databases,
outbound emails, financial transactions), human-in-the-loop review
belongs in the execution path, not the prompt. AWS Step Functions
callback patterns let an agent pause and wait for approval. The
workflow sends an approval request through Amazon SNS or Amazon SES and resumes only after a human responds within a defined
timeout. Configure escalation paths for timeouts so a non-response
doesn't silently block a legitimate action. Rate limiting at both
the Gateway and tool API levels helps prevent resource exhaustion:
Amazon API Gateway usage plans and throttling enforce per-agent
rate limits, and AWS Lambda reserved concurrency caps the maximum
parallel tool invocations. Gateway publishes usage, invocation,
performance, and error metrics to Amazon CloudWatch and integrates
with AWS CloudTrail for a full audit trail, so runaway loops and
unexpected call patterns surface as signal.

### Implementation steps

- **Configure Gateway inbound
OAuth:** Create an
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) and wire inbound OAuth
authorization to your identity provider (Amazon Cognito,
Okta, Auth0, or your own OAuth provider), specifying
approved client IDs and audiences.
- **Add targets with scoped outbound
credentials:** Register tool APIs as gateway
targets, configuring IAM roles for Lambda and Smithy targets
and API key or OAuth 2LO for OpenAPI targets, and manage
outbound credentials through
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) resource credentials
providers.
- **Author Cedar policies for
authorization:** Create a policy engine in
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) and define Cedar policies
with identity-aware conditions on OAuth claims (user role,
scopes, user ID) and tool input parameters. Author directly
in Cedar or generate policies from natural language
descriptions.
- **Validate policies in LOG_ONLY before
enforcing:** Associate the policy engine with
Gateway in LOG_ONLY mode, review observability logs to
confirm the policies produce the expected permit and deny
decisions, then switch to enforce mode.
- **Enable semantic tool
discovery:** Opt in to the built-in
x_amz_bedrock_agentcore_search tool so
agents locate relevant tools through natural language
queries rather than reasoning over the full inventory.
- **Add human-in-the-loop approvals for
mutating tools:** Wire AWS Step Functions callback
patterns for high-risk tools, send approval requests through
Amazon SNS or Amazon SES, and configure escalation paths for
reviewer timeouts.
- **Cap concurrency and request
rates:** Enforce per-agent rate limits through
Amazon API Gateway usage plans and cap parallel invocations
with AWS Lambda reserved concurrency to help prevent
resource exhaustion.
- **Monitor authorization
decisions:** Use Gateway's Amazon CloudWatch
metrics and AWS CloudTrail integration to track tool
invocations, authorization failures, and rate-limit events,
and configure alarms for authorization-failure spikes.
- **Review tool authorization
quarterly:** Remove unused permissions and tighten
access boundaries on a regular cadence as workloads and
tools evolve.

## Resources

**Related best practices:**

- [AGENTSEC02-BP02 Validate
tool inputs and outputs](agentsec02-bp02.html)
- [AGENTSEC02-BP03 Maintain
approved tool registry with security assessments](agentsec02-bp03.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTREL02-BP02
Limit agent permissions to minimum required access](agentrel02-bp02.html)
- [AGENTCOST04-BP01
Design cost effective tool selection to minimize unnecessary
invocations](agentcost04-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html)
- [Introducing
Amazon Bedrock AgentCore Gateway: Transforming enterprise AI
agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [Apply
fine-grained access control with Bedrock AgentCore Gateway
interceptors](https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-access-control-with-bedrock-agentcore-gateway-interceptors/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [Amazon
Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html)

**Related examples:**

- [Healthcare
appointment agent with Policy enforcement (GitHub)](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/02-use-cases/healthcare-appointment-agent)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02-bp01.html*

---

# AGENTSEC02-BP02 Validate tool inputs and outputs

Agents generate tool parameters from model output, which means
malformed or adversarial inputs can reach tools through ordinary
reasoning, not just through unauthorized callers. Schema-driven
validation on inputs and sanitization on outputs keep tools
operating inside their intended parameter space and help prevent
error messages from disclosing internal system details.

**Desired outcome:**

- You validate every parameter passed to tools against a defined
schema before execution, and sanitize tool outputs before
returning them to the agent.
- Injection through tool parameters is blocked, oversized inputs
are prevented from exhausting resources, and error messages are
sanitized to avoid leaking sensitive system information.
- Tool invocations operate predictably within defined boundaries,
and validation failures are logged for security analysis.

**Common anti-patterns:**

- Passing raw agent-generated parameters directly to tools without
type checking or range validation, letting malformed inputs
cause unexpected behavior or injection.
- Returning raw tool error messages to the agent without
sanitization, exposing internal system details, stack traces, or
infrastructure information usable for further probing.
- Validating only user-provided inputs and skipping validation for
parameters produced by the agent's reasoning, on the assumption
the model can't generate malformed output.

**Benefits of establishing this best
practice:**

- Schema-enforced input validation helps prevent tools from
operating outside their intended parameter space.
- Sanitized error responses return failure categories without
exposing internal system details.
- Timeout controls, memory limits, and output-size enforcement
help prevent resource exhaustion from oversized or long-running
tool invocations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Validation is more useful when it happens at several layers than
when any single layer tries to do all the work. The cheapest and
most specific layer is at the model itself. Amazon Bedrock
structured outputs with strict tool use constrain the model's
decoding so that generated tool parameters always conform to the
defined input schema. Setting strict: true on
the tool definition, together with
additionalProperties: false and
enum constraints on fields with a closed set of
values, helps prevent malformed parameters as a class before they
ever reach the tool. That doesn't replace application validation,
but it removes a large chunk of the work from it. The
[Structured
outputs on Amazon Bedrock blog](https://aws.amazon.com/blogs/machine-learning/structured-outputs-on-amazon-bedrock-schema-compliant-ai-responses/) covers the parameter shapes
and the model-level enforcement.

The next layer is schema validation in the tool invocation
pipeline. For tools deployed as AWS Lambda functions, a JSON
Schema check inside the Lambda handler, or a shared Lambda Layer,
enforces type constraints, value ranges, string length limits, and
format patterns before the function logic runs. This is the place
to catch the edge cases strict tool use doesn't cover, anything
involving relationships between fields, external-state
constraints, or values the model can't know.

Policy in Amazon Bedrock AgentCore provides a third layer at the
gateway. Cedar policies can evaluate conditions on tool input
parameters through context.input, so business
rules like "financial amount below an approved
threshold" or "date parameter within an acceptable
range" are enforced deterministically at the gateway before
the call reaches the backend. The value of this layer is that the
rules are auditable and managed independently of tool code. The
value of keeping it separate from the first two layers is that
changes to business rules don't require redeploying tools.

Logical constraints that are not expressible as schema or simple
comparisons need a different mechanism.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) Automated Reasoning checks verify that
tool parameters conform to logical constraints, a date range with
start before end, a set of values that must be mutually
consistent. Apply Guardrails at the AWS Organization level where
consistent policy enforcement is required across all agent
deployments.

Resource protection and error sanitization complete the picture.
AWS Lambda function timeout and memory limits, sized to each
tool's measured execution profile, bound what any single call can
consume, and Lambda reserved concurrency caps total parallel
invocations. Tool outputs that return large datasets need size
limits and pagination. Truncation events belong in the log so an
agent doesn't silently reason on a partial response. Error
handling catches exceptions and returns structured responses that
describe the failure category without exposing internal details,
stack traces, or infrastructure information. AWS WAF managed rule
groups on API-based tool endpoints add a network-layer filter for
common injection patterns before requests reach tool code.

### Implementation steps

- **Constrain parameters at the model
layer:** Enable strict tool use
(strict: true) on tool definitions in
Amazon Bedrock, set
additionalProperties: false on all input
schemas, and define enum constraints for
fields with a limited set of valid values to block malformed
parameters at decoding.
- **Enforce schemas in the invocation
pipeline:** Define JSON Schema specifications for
every tool and validate parameters as a middleware layer
inside the Lambda handler or a shared Lambda Layer before
the tool function runs.
- **Add Cedar policy checks at the
gateway:** Define policies in AgentCore Policy with
conditions on context.input to enforce
business rules and parameter constraints deterministically,
complementing application-level schema validation.
- **Use Automated Reasoning for logical
constraints:** Configure
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) Automated Reasoning policies for
tool inputs and outputs that require logical constraint
validation beyond schema and Cedar rules.
- **Right-size Lambda limits per
tool:** Set AWS Lambda timeout and memory limits
based on measured execution profiles, with conservative
limits that help prevent resource exhaustion, and use
reserved concurrency to cap parallel invocations.
- **Sanitize errors:**
Implement structured error handling in every tool that
returns sanitized responses without internal system details,
stack traces, or infrastructure information.
- **Paginate and truncate large
outputs:** Apply output size limits for tools that
may return large datasets, truncate responses before
returning them to the agent, and log every truncation event.
- **Add AWS WAF in front of API-based
tools:** Deploy AWS WAF with managed rule groups on
API-based tool endpoints to filter common injection patterns
at the network layer.
- **Alarm on validation-failure
rates:** Publish Amazon CloudWatch metrics for
validation outcomes and configure alarms for elevated
failure rates that suggest active injection attempts or
misconfigured parameters.

## Resources

**Related best practices:**

- [AGENTSEC02-BP01
Implement tool authorization](agentsec02-bp01.html)
- [AGENTSEC02-BP03 Maintain
approved tool registry with security assessments](agentsec02-bp03.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [Amazon
Bedrock Guardrails automated reasoning checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning.html)
- [Structured
outputs on Amazon Bedrock: Schema-compliant AI
responses](https://aws.amazon.com/blogs/machine-learning/structured-outputs-on-amazon-bedrock-schema-compliant-ai-responses/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS WAF](https://aws.amazon.com/waf/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02-bp02.html*

---

# AGENTSEC02-BP03 Maintain approved tool registry with security assessments

Every tool an agent can reach is part of its effective privilege
surface. A version-controlled registry with documented security
boundaries, enforced at invocation time, keeps unvetted or
deprecated tools off the agent's call path.

**Desired outcome:**

- You maintain a centralized, version-controlled registry of
approved tools, each with documented security boundaries,
required permissions, data classification levels, and a current
vulnerability assessment.
- Agents can access only tools present in the registry, and
unapproved tools are blocked by default.
- You continually validate the registry for compliance, and
deprecated tools are removed from agent access automatically.

**Common anti-patterns:**

- Allowing agents to discover and invoke any available tool or MCP
server without prior security review and registry approval.
- Maintaining the tool registry as a static document rather than
an enforced control, so agents can bypass it and invoke
unapproved tools directly.
- Failing to distinguish between locally hosted tools and remote
MCP servers in the risk assessment, underestimating the expanded
scope from external network connectivity.
- Skipping version pinning for approved tools, so agents pick up
new versions that have not undergone security review.

**Benefits of establishing this best
practice:**

- A deny-by-default posture constrains agent capabilities to a
pre-approved, security-reviewed set of tools and operations.
- Version control helps prevent agents from using tool versions
that have not been reviewed and provides an audit trail of which
versions were approved and when.
- Automated compliance checks detect drift from the approved
registry and trigger remediation workflows.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A tool registry must be enforced at runtime to be effective.
Document approved tools in a registry and configure the invocation
path to refuse tools that are not on the list. The design pattern
is a registry that agents can't bypass: tools reachable only
through a gateway target, agents authorized only through a policy
engine with default-deny semantics, and an out-of-band compliance
process that detects drift between the registry and what is
actually configured.

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) provides the consolidation point
for agent-to-tool traffic. Each gateway target represents a
backend service or group of APIs exposed as tools to agents, with
defined tool schemas, authentication configurations, and access
controls. Gateway alone isn't deny-by-default, however: adding a
target makes it immediately accessible as an MCP tool to any agent
that reaches the gateway endpoint. To restrict which agents can
invoke which tools, layer
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) Cedar policies with a
default-deny posture, Gateway Interceptor for custom Lambda-based
access logic, or both. The policy layer is what turns a populated
registry into enforced authorization.

Development environments need a second control. When developers
and agents interact with MCP servers through IDE-based tools, an
MCP registry, a JSON allowlist of approved servers hosted on an
HTTPS endpoint such as Amazon S3 or an internal web server, gives
clients a list of servers to fetch at startup and re-sync
periodically (typically every 24 hours). Servers not in the
registry are blocked, and if a locally installed server is removed
from the registry, the client terminates it and helps prevent it
from being re-added. The registry supports version pinning so that
a new version automatically relaunches clients with the updated
version, and the file format follows the
[MCP
Registry open standard](https://github.com/modelcontextprotocol/registry) so the investment isn't tied to a
single tool or provider. MCP registry governance can be configured
at the organization level with account-level overrides, for
example disabling MCP for the organization by default but enabling
it with a specific allowlist for certain teams.

At enterprise scale, a centralized MCP server hub consolidates
what would otherwise become a proliferation of team-specific
connections. Teams develop MCP servers for their specific
functions, but servers are hosted centrally and accessible across
the organization through a shared registry or discovery API backed
by Amazon DynamoDB that catalogs available servers with their
descriptions, tool definitions, and access requirements.
Network-level access uses AWS PrivateLink and VPC endpoints so
agents connect only to trusted organization-hosted servers, and
each server runs as an isolated container on Amazon ECS with AWS Fargate for independent scaling without impact on other servers.

Remote MCP servers need a heightened security review. They
introduce network connectivity to external services, expanding
scope beyond the organization's direct control. Assess
authentication mechanisms, data handling practices, and network
exposure, and apply network controls such as VPC endpoints and
security groups to restrict connectivity to the required
endpoints. When onboarding tools to Gateway or the MCP registry,
scan API specifications for security risks, validate
authentication, assess data handling, enrich tool metadata with
descriptions, usage examples, and performance characteristics, and
group APIs into gateway targets by business domain, outbound
authorization requirements, and API type.

Gateway supports six target types:

- Lambda functions
- API Gateway REST APIs
- OpenAPI schemas
- Smithy models
- External MCP servers
- Built-in templates from integration providers

Built-in templates provide pre-configured, curated integrations
for popular SaaS platforms including Salesforce, Slack, Jira,
Asana, Zendesk, and ServiceNow, with a vetted subset of provider
APIs exposed through the gateway. Routing all tool access through
Gateway (internal services, external MCP servers, and native SaaS
integrations) consolidates authentication, schema enforcement, and
policy evaluation under one endpoint. IDEs such as Kiro, Claude
Code, and Cursor connect through the Amazon Bedrock AgentCore MCP
Server, which bridges IDE-based MCP clients to the gateway
endpoint.

Continuous compliance detection keeps the registry enforceable
over time. Maintain a configuration store in Parameter Store, a
capability of AWS Systems Manager or AWS AppConfig alongside the
gateway configuration, with entries for tool name, approved
version, required IAM permissions, data classification level,
security review date, and expiration date. Use AWS Config rules to
validate that agent deployments reference only registry-approved
tools, and trigger Amazon EventBridge notifications for
non-compliance. Automated deprecation workflows remove expired
tools from the registry, update agent configurations, and help
prevent continued use.

### Implementation steps

- **Build the structured
registry:** Create a tool registry in Parameter
Store, a capability of AWS Systems Manager or AWS AppConfig
with entries for each approved tool covering version,
permissions, data classification, and review metadata.
- **Add approved tools as Gateway
targets:** For agent-to-tool traffic, register
approved tools as
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) targets with defined tool
schemas, outbound authentication configurations, and access
controls. Group targets by business domain, authorization
requirements, and API type.
- **Publish an MCP registry for
development:** Create an MCP registry JSON file
that follows the
[MCP
Registry open standard](https://github.com/modelcontextprotocol/registry), host it on an HTTPS endpoint,
and configure it in your organization's admin settings with
version pinning for each server entry.
- **Define the security review
process:** Establish a review covering API
specification scanning, permission assessment, data flow
mapping, and authentication mechanism validation, with
findings documented in the registry entry and a review
expiration date.
- **Build a centralized hub at
enterprise scale:** For multi-LOB deployments,
implement a centralized MCP server hub with an Amazon DynamoDB-backed discovery API, network-level access through
AWS PrivateLink and VPC endpoints, and isolated container
hosting on Amazon ECS with AWS Fargate.
- **Enforce default-deny through
Policy:** Configure Cedar policies in AgentCore
Policy so only explicitly permitted tools can be invoked,
providing a second enforcement layer beyond Gateway target
configuration.
- **Apply heightened review to remote
MCP servers:** Assess network exposure and external
authentication, and apply VPC endpoints and security groups
to restrict connectivity.
- **Detect registry drift
continually:** Deploy AWS Config rules to detect
agent configurations referencing unapproved tools, and
trigger Amazon EventBridge notifications for remediation.
- **Automate deprecation:**
Expire tools past their review date, remove them from
Gateway targets and the MCP registry, and update agent
configurations to help prevent continued use.

## Resources

**Related best practices:**

- [AGENTSEC02-BP01
Implement tool authorization](agentsec02-bp01.html)
- [AGENTSEC02-BP02 Validate
tool inputs and outputs](agentsec02-bp02.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html)
- [Introducing
Amazon Bedrock AgentCore Gateway: Transforming enterprise AI
agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [Transform
your MCP architecture: Unite MCP servers through AgentCore
Gateway](https://aws.amazon.com/blogs/machine-learning/transform-your-mcp-architecture-unite-mcp-servers-through-agentcore-gateway/)
- [Enterprise
governance: control your MCP servers and models](https://kiro.dev/blog/enterprise-governance-mcp-and-models/)
- [MCP
governance for Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-governance.html)
- [Accelerating
AI innovation: Scale MCP servers for enterprise workloads with
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/accelerating-ai-innovation-scale-mcp-servers-for-enterprise-workloads-with-amazon-bedrock/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [Parameter
Store, a capability of AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

**Related examples:**

- [Accelerating
AI Innovation: Scaling Model Context Protocol Servers for
Enterprise Workloads on AWS (GitHub)](https://github.com/aws-samples/sample-deploy-mcp-servers-at-scale-on-aws)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Config](https://aws.amazon.com/config/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02-bp03.html*

---
