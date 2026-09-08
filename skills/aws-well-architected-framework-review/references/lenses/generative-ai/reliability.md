# Reliability

**Pillar**: Reliability  
**Questions**: 6

---

# GENREL01 — Manage throughput quotas

**Pillar**: Reliability  
**Best Practices**: 1

---

# GENREL01-BP01 Scale and balance foundation model throughput as a function of utilization

Collect information on the generative AI workload's utilization,
and implement dynamic scaling strategies to match capacity with
demand. Use this information to determine the required
throughput for your foundation model and establish appropriate
quotas and scaling policies.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by matching the configured or provisioned
throughput to your foundation models to the workload's demand.
This results in optimal resource utilization and consistent
performance under varying loads.

**Benefits of establishing this best
practice:**
[Stop
guessing capacity](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - By understanding the throughput needs
of your generative AI workload, you remove the need to guess at
throughput capacity.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

When managing throughput for foundation models, consider
implementing a comprehensive monitoring and scaling strategy.
Use a robust monitoring system that provides detailed insights
for tracking throughput metrics and creating alarms for quota
utilization.

To handle traffic spikes and maintain consistent performance,
implement request buffering using a message queue service,
which can help smooth out irregular traffic patterns and avoid
overwhelming the model endpoints. Use a service quota
management system to adjust service limits based on your
workload requirements, while implementing auto-scaling
mechanisms to enable dynamic capacity management based on
demand.

Consider placing queues between generative AI applications and
models so that models do not deny or drop requests due to
throughput constraints. This architecture lends itself to
event-driven messaging patterns, making it a particularly
robust option for architectures with high demand.

For handling common throughput bottlenecks, consider
implementing token bucket algorithms for rate limiting or
using provisioned throughput options when dealing with token
rate limits. To address concurrent request limits, implement
request queuing or distribute requests across multiple
Regions. For model loading overhead, maintain a warm pool of
model instances or implement model caching strategies. Each of
these solutions should be monitored for effectiveness using
your chosen metrics and monitoring system.

Provisioned Throughput endpoints or cross-Region inference
profiles on Amazon Bedrock may help to alleviate scaling
bottlenecks for fully-managed inference hosting. Provisioned
Throughput provides dedicated infrastructure that can achieve
higher, more stable throughput than allowed through default
quotas for on demand models hosted on Amazon Bedrock.
Provisioned Throughput capacity can be monitored in Amazon CloudWatch, which helps you proactively scale when capacity
nears critical thresholds.

Cross-Region inference profiles distribute inference demand
over a region of availability. For model endpoints hosted on
Amazon SageMaker AI Inference Endpoints, consider using
traditional throughput scaling techniques like EC2 Autoscaling
groups behind a load balancer. If your increased throughput
needs are periodic and predictable, consider deploying larger
instance types in advance of the increased need. Ultimately,
it is encouraged to proactively engage with AWS support to
increase service quotas based on known workload demands.

### Implementation steps

- Set up comprehensive monitoring using CloudWatch:

Create custom dashboards for throughput metrics
- Configure alarms for quota utilization
- Enable detailed monitoring for critical resources

- Implement request management:

Deploy queue-based architecture for request buffering
- Set up rate limiting at the application layer
- Configure retry mechanisms with exponential backoff

- Configure scaling mechanisms:

Set up auto-scaling policies based on demand
- Configure provisioned throughput where appropriate
- Implement cross-region request distribution

- Establish ongoing optimization:

Regular review of utilization patterns
- Periodic adjustment of quotas and scaling parameters
- Continuous monitoring and refinement of thresholds

## Resources

**Related best practices:**

- [REL01-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_aware_quotas_and_constraints.html)
- [REL01-BP02](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_limits_considered.html)
- [REL01-BP03](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_aware_fixed_limits.html)

**Related documents:**

- [Increase throughput with cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)

**Related examples:**

- [Enable
Amazon Bedrock cross-Region inference in multi-account
environments](https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/)
- [Building
well-architected serverless applications: Regulating inbound
request rates – part 1](https://aws.amazon.com/blogs/compute/building-well-architected-serverless-applications-regulating-inbound-request-rates-part-1/)
- [Getting Started with cross-Region inference in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel01-bp01.html*

---

# GENREL02 — Network reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

# GENREL02-BP01 Implement redundant network connections among model endpoints and supporting infrastructure

Implement network connection redundancy among components in your
generative AI application.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by reducing the likelihood of performance
degradation due to network issues.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)
across multiple components using a reliable network backbone.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement network connection redundancy between components in
your generative AI application to provide high availability
and fault tolerance. This involves creating multiple network
paths between critical components, using technologies such as
multi-AZ deployments, cross-Region connectivity, and
software-defined networking. Consider implementing load
balancers to distribute traffic across redundant connections
and automatically route around failures.

Deploy your generative AI application across multiple subnets
within a VPC. Use AWS PrivateLink or a similar network
technology to facilitate secure, private network
communications between VPC-hosted applications and other AWS
services. Use a multi-AZ architecture, with applications
deployed across at least two Availability Zones.

In addition to deploying applications with high availability,
deploy vector databases and agentic systems across multiple
Availability Zones as well. With vector database solutions
like Amazon OpenSearch Service Serverless, you can configure
your OpenSearch cluster deployment across multiple
Availability Zones, creating VPC Endpoints to have reliable
network connectivity to the cluster.

Similar considerations should be extended to agentic
workflows. On Amazon Bedrock, agent workflows make calls to
API endpoints and AWS Lambda functions. Consider deploying
these capabilities in a multi-AZ deployment as well.

For multi-Region deployments, implement a global traffic
management solution to route requests to the nearest available
endpoint. Use private network connections where possible to
improve security and reduce latency. Implement automatic
failover mechanisms to reroute traffic in case of network
issues. Continue deploying resources into VPCs, but consider
using one of the various multi-Region VPC communication
services to facilitate secure, reliable network connectivity
for your services and applications.

Use network configuration tools like VPC peering, AWS Transit Gateway, or Amazon VPC Lattice to connect your applications
and services in VPCs across Regions. Consider combining this
capability with Amazon Bedrock's cross-Region inference
capabilities for high availability network connectivity across
Regions.

### Implementation steps

- Identify critical network paths in your generative AI architecture:

Map dependencies between foundation models, databases, and other components
- Determine required bandwidth and latency for each connection

- Design redundant network topology:

Implement multi-AZ deployments for high availability
- Set up cross-Region connectivity for disaster recovery
- Configure load balancers for traffic distribution

- Implement private networking:

Use VPC peering or transit gateways for secure inter-component communication
- Set up VPN or direct connect for on-premises integration if required

- Configure automatic failover:

Implement health checks for network paths
- Set up automated failover mechanisms using DNS or overlay networking

- Test and validate redundancy:

Conduct failure simulations to verify failover effectiveness
- Perform regular failover drills to verify operational readiness

## Resources

**Related best practices:**

- [REL02-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_network_topology_ha_conn_users.html)
- [REL02-BP02](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_manage_service_limits_limits_considered.html)

**Related documents:**

- [Securely Access Services Over AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/aws-privatelink.html)

**Related examples:**

- [Connect
to Amazon services using AWS PrivateLink in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/connect-to-amazon-services-using-aws-privatelink-in-amazon-sagemaker/)
- [Use AWS PrivateLink to set up private access to Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/use-aws-privatelink-to-set-up-private-access-to-amazon-bedrock/)
- [Overseeing
AI Risk in a Rapidly Changing Landscape](https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel02-bp01.html*

---

# GENREL03 — Prompt remediation and recovery actions

**Pillar**: Reliability  
**Best Practices**: 2

---

# GENREL03-BP01 Use logic to manage prompt flows and gracefully recover from failure

Leverage conditions, loops, and other logical structures at the
prompt management or application layer to reduce the risk of an
unreliable experience.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by reducing the likelihood of performance
degradation logical errors in your prompt flows.

**Benefits of establishing this best
practice:**
[Automatically
recover from failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing recovery logic in
generative AI workflows helps to reduce potentially blocking
failures, while encouraging generative AI applications to gracefully
recover automatically.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Define expected behavior for generative AI applications
before, during, and after prompts. Create layers of
abstraction between users and models to facilitate retries,
error handling, and graceful failures. For multi-step prompt
flows, implement logic statements to check if your prompts
contain the expected information. Apply similar logic to
verify your model's respond with expected content.

For prompt flows containing data from external sources,
implement logic to verify the relevant data from the external
source exists. Define a fallback action or default modality in
the absence of relevant data. Apply similar reasoning to model
responses enriched with embeddings from a vector search
engine. Consider applying checks on the model's response to
identify the relevance of the returned data or a fallback
action if no data is returned at all.

Agentic workflows commonly make calls to external systems.
Develop agents with error handling in mind. Consider how
errors are propagated back up to agents. Upon receiving an
error, an agent should take appropriate action to retry or
gracefully fail. One way to accomplish this is to have the
agent classify responses from external systems as actionable
or not. Actionable responses are anticipated and
well-understood responses (for example, a database query
returning at least one result). An inactionable response
traditionally requires error handling at the software layer
(for example, error codes or empty responses). Agents can be
prompted to classify responses in these cases and take action
appropriately. This method may serve to reduce non-determinism
and increase reliability of agent workflows.

When developing multistep prompt flows or prompt chains,
consider using Amazon Bedrock Flows to orchestrate multistep
prompts. Bedrock Flows enables graceful failure and recovery
for long prompt chains, which allows your applications to take
appropriate action on failure. Bedrock Flows has nodes for
controlling flow logic, which include iterator nodes and
condition nodes. Customers may consider using these nodes to
implement graceful recovery instead of developing a custom
abstraction layer.

### Implementation steps

- Establish error classification system:

Categorize common failure types
- Define severity levels
- Create response templates for each error category
- Set up automated detection mechanisms

- Implement recovery mechanisms:

Design retries strategies with exponential backoff
- Create fallback prompt templates
- Develop circuit breaker implementations
- Set up automated recovery workflows

- Configure monitoring and alerting:

Track recovery success rates
- Monitor remediation effectiveness
- Set up alerts for repeated failures
- Implement performance tracking

- Create continuous improvement process:

Analyze failure patterns
- Update remediation strategies
- Refine prompt templates
- Optimize recovery workflows

## Resources

**Related best practices:**

- [REL05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html)

**Related documents:**

- [Demo
- Amazon Bedrock Flows](https://www.youtube.com/watch?v=_Bmk6peAHao)
- [Build
an end-to-end generative AI workflow with Amazon Bedrock
Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)

**Related examples:**

- [Amazon Bedrock Flows is now generally available with enhanced safety
and traceability](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-flows-is-now-generally-available-with-enhanced-safety-and-traceability/)
- [Simplifying
the Prompts Lifecycle with Prompt Management and Prompt Flows
for Amazon Bedrock Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/c81935bc-0b43-4bd6-bd01-db45f847d6bd/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel03-bp01.html*

---

# GENREL03-BP02 Implement timeout mechanisms on agentic workflows

Implement controls to detect and terminate long-running unexpected
workflows.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by freeing resources that might have been
consumed by unexpected long-running execution loops.

**Benefits of establishing this best
practice:**
[Automatically
recover from failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing agent timeouts helps to
reduce the likelihood of blocking failures on agentic workflows and
executions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Agentic workflows act on behalf of a user by making calls to
external systems. External systems may themselves perform
several time-consuming tasks which the agent is not aware of,
resulting in idle agents that could run for an extended
period. To maintain a reliable agentic system, implement
controls to manage agentic timeout.

One approach to controlling agentic runtime or lifecycle is to
implement runtime timeouts on the external infrastructure. For
example, if an agent makes a call to a function through an
Action Group, consider applying a timeout to the corresponding
function. The timeout should be set to include the maximum
allowable time needed to complete a process, accounting for
additional latency for edge cases such as cold starts. You may
consider rounding this value up to avoid unnecessary early
terminations.

Alternatively, consider connecting agentic workflows to an
event system, developing an asynchronous process management
architecture. Introducing an asynchronous event system gives
users the most flexibility and visibility into agent process
lifecycle or flow. By requiring the compute underpinning an
Action Group to publish events, workload owners maintain
insight into where an agent may encounter stalled flow or
process. Consider using events to publish agent updates and
act appropriately to stop long-running invocations.

Error handling at the agent layer should be transparent to
users. When errors occur, communicate clear details about the
issue while maintaining system security by avoiding exposure
of sensitive internal information. The response should outline
specific next steps so that users can complete their tasks
independently if the agent remains unavailable. This approach
promotes operational resilience while maintaining security
best practices, as users receive actionable guidance without
compromising system integrity.

### Implementation steps

- Create an agent workflow configuration:

Define maximum runtime thresholds
- Set up timeout controls at function and workflow levels
- Configure event publishing for process monitoring

- Implement timeout mechanisms:

Add timeouts at the agent layer to terminate sessions waiting for user input
- Configure timeouts on external compute resources
- Set up dead letter queues for timed-out processes

- Establish monitoring and alerting:

Track agent execution times
- Monitor timeout frequency
- Alert on repeated timeouts

- Define recovery procedures:

Create graceful termination processes
- Implement cleanup routines for timed-out sessions
- Set up automated retry mechanisms where appropriate

## Resources

**Related best practices:**

- [REL05-BP05](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_client_timeouts.html)

**Related documents:**

- [AWS re:Invent 2023
- Simplify generative AI app development with Agents for
Amazon Bedrock (AIM353)](https://www.youtube.com/watch?v=JNZPW82uv7w)
- [Automate tasks in
your application using AI agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

**Related examples:**

- [Best
practices for building robust generative AI applications with
Amazon Bedrock Agents - Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/)
- [Best
practices for building robust generative AI applications with
Amazon Bedrock Agents - Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel03-bp02.html*

---

# GENREL04 — Prompt management

**Pillar**: Reliability  
**Best Practices**: 2

---

# GENREL04-BP01 Implement a prompt catalog

Prompt catalogs store and manage prompts and prompt versions. They
act as a reliable store for prompts for generative AI workloads.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by creating a central store for prompts that
can be used for generative AI workloads.

**Benefits of establishing this best
practice:**
[Manage
change through automation](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing a prompt catalog
helps to automate the process of deploying and rolling back prompt
versions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Prompt catalogs function as a centralized system for
developing, testing, and managing prompts. Implement a prompt
catalog to maintain different versions of prompts. Prompts
should be released to a live version once passing the
appropriate testing thresholds and benchmarks. In the case
where a prompt results in unexpected or undesirable behavior,
a prompt catalog enables the ability to roll back to the
previous version.

Additionally, maintain versioned information on hyperparameter
ranges for prompts. Prompt behavior can change drastically
when tuning hyperparameters such as temperature, top_p, or
top_k. Value ranges for these hyperparameters should be paired
with and validated against prompt versions as part of the
prompt engineering process.

Prompt catalogs should maintain test results for a prompt
against several model versions. A given foundation model can
have several versions, and prompt test results for each model
version can vary accordingly. Consider developing a catalog
that maintains prompt versions for each of the available
models.

### Implementation steps

- Design catalog structure:

Define prompt metadata schema (like version, author, and purpose)
- Create categorization system for different prompt types
- Establish naming conventions and tagging standards
- Define access control requirements

- Implement version control:

Set up version tracking for prompts
- Create changelog management process
- Define rollback procedures
- Establish backup and recovery processes

- Create testing framework:

Define success criteria for prompts
- Establish validation procedures
- Create test suites for different use cases
- Set up automated testing pipelines

- Configure prompt metadata:

Document hyperparameter ranges
- Track performance metrics
- Record model compatibility
- Maintain usage statistics

- Establish governance processes:

Define approval workflows
- Create audit trails
- Set up review procedures
- Implement quality controls
- Codify in your organizations AI usage or policy document

## Resources

**Related best practices:**

- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)
- [REL08-BP02](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_functional_testing.html)
- [REL08-BP04](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.html)

**Related documents:**

- [AWS re:Invent 2023
- Prompt Engineering Best Practices for LLMs on Amazon Bedrock
(AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY)

**Related examples:**

- [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel04-bp01.html*

---

# GENREL04-BP02 Implement a model catalog

Model catalogs store and manage model versions. They act as a
reliable store for models which may need to be deployed or rolled
back at any time. They also facilitate decoupled deployment
automation.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by helping to make sure the deployed model is
the appropriate model for the given use case.

**Benefits of establishing this best
practice:**
[Manage
change through automation](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing a model catalog
helps to automate the process of deploying and rolling back model
versions.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Model catalogs provide a centralized location to review
models, model versions, and model cards. Traditionally, model
catalogs are meant to store model artifacts developed by
customers. Foundation models are rarely developed from
scratch, and as a result, foundation model catalogs should
maintain first-party models, third-party models, and custom
models developed from third-party models.

Consider implementing a model catalog for foundation models
that records and tracks model access, model versions, and
model card information. Maintain a model catalog in your
environment to track available models. Model catalogs should
provide a central location for model management, particularly
if there is a need to roll back to a particular model or model
version.

AI policy documents should provide clear details regarding the
usage, maintenance, and updating of the model catalog. The AI
policy document is intended to be the central authority for
operational questions pertaining to AI workloads and
supporting infrastructure. Keep this document up to date with
the appropriate materials necessary to scale the usage of the
model catalog throughout the organization.

### Implementation steps

- Set up catalog structure:

Create model classification system (by type, purpose, and provider)
- Define model metadata schema
- Establish versioning conventions
- Design access control framework

- Configure model tracking:

Record model lineage and dependencies
- Track model versions and updates
- Document model customizations
- Maintain performance benchmarks

- Implement model cards:

Define required model information
- Document model capabilities and limitations
- Record training data characteristics
- Specify intended use cases and constraints
- Include ethical considerations and biases

- Establish model governance:

Create model approval workflows
- Define deployment procedures
- Set up model monitoring
- Implement security controls
- Track model usage and access

- Create maintenance procedures:

Define model update process
- Establish deprecation policies
- Create archival procedures
- Set up backup and recovery

- Implement validation framework:

Create model testing procedures
- Define acceptance criteria
- Set up performance benchmarking
- Establish quality gates

## Resources

**Related best practices:**

- [REL04-BP02](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system.html)
- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)

**Related documents:**

- [Amazon Bedrock API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)
- [Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html)
- [Find
serverless models with the Amazon Bedrock model catalog](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/model-catalog.html)
- [Bring
your own endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.html)

**Related examples:**

- [Amazon Bedrock Marketplace: Access over 100 foundation models in one
place](https://aws.amazon.com/blogs/aws/amazon-bedrock-marketplace-access-over-100-foundation-models-in-one-place/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel04-bp02.html*

---

# GENREL05 — Distributed availability

**Pillar**: Reliability  
**Best Practices**: 3

---

# GENREL05-BP01 Load-balance inference requests across all regions of availability

Inference to a foundation model may be available over a local or
large area of availability. Verify that you have resources
available across that area to service inference requests
reliably regardless of where they are coming from.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by creating a highly available
environment for serving inference requests.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)
- Load-balanced inference requests across horizontally scaled
infrastructure enable inference requests to be serviced evenly
across a region of availability.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use load balancing and multi-Region deployment strategies to
distribute inference requests across multiple AWS Regions and
Availability Zones. This helps maintain consistent performance
and availability in the face of regional disruptions or
network issues. Consider using Amazon Bedrock's cross-Region
inference profiles to route requests to the nearest available
endpoint. For self-hosted models on Amazon SageMaker AI,
implement a multi-AZ deployment with an Amazon SageMaker AI
Inference Endpoint configured for auto-scaling to
automatically distribute and scale traffic across Regions.

This strategy provides improved reliability, reduced risk of
single points of failure, and better geographic coverage for
global users. Potential trade-offs include increased network
latency and operational complexity.

### Implementation steps

- Configure Amazon Bedrock cross-Region inference profiles
or deploy self-hosted models on Amazon SageMaker AI
Inference Endpoints across multiple Availability Zones.
- Set up an Amazon SageMaker AI Inference Endpoint with
auto-scaling enabled to distribute traffic based on
health and latency.
- Implement health checks and automated failover to
maintain availability.
- Monitor performance metrics like latency, error rates,
and throughput across Regions.

## Resources

**Related best practices:**

- [REL04-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_identify.html)
- [REL10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)

**Related documents:**

- [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)

**Related examples:**

- [Getting Started with cross-Region inference in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05-bp01.html*

---

# GENREL05-BP02 Replicate embedding data across all regions of availability

Inference to a foundation model may be available over a local availability region, or could
be a large region of availability. Make sure your data is available across all regions of
availability to adequately service inference requests.

**Desired outcome:** When implemented, this best practice improves
the reliability of your generative AI workload by validating that models have access to the
appropriate data to service inference requests across an entire Region of availability.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) -
Data replication across a region of availability enables horizontal
scaling of the data access infrastructure and supports consistent
serving of inference requests.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Replicate the data required for generative AI workloads, such
as embeddings and knowledge bases, and make that data readily
available across all designated Regions. This helps prevent
data access from becoming a bottleneck and maintains
consistent performance for users regardless of their location.
Use solutions like Amazon S3 cross-Region replication, Amazon OpenSearch Service cross-cluster replication, and AWS Glue
data pipelines to distribute data efficiently.

Consider data sovereignty requirements and regulatory
restrictions that may limit your ability to freely replicate
data, including embeddings, across all Regions. Carefully
review the data residency and compliance needs for your
specific use case and workload. Implement data distribution
strategies that respect these constraints, such as keeping
embeddings within a defined geographic area or using
Region-specific data stores.

Replicating data across Regions can incur additional storage
and data transfer costs. Optimize data partitioning and
compression to minimize the overall storage footprint. Use
Amazon S3 Intelligent Tiering to automatically move less
frequently accessed data to more cost-effective storage
classes. Replicating data provides improved data availability
and reduced latency for users. If done properly, this practice
helps you maintain compliance with data sovereignty
regulations. Trade-offs may include increased costs and
potential consistency challenges within the allowed Regions.

### Implementation steps

- Assess data sovereignty requirements and regulatory
constraints for your generative AI workload, including
the distribution of embeddings.
- Identify the Regions where you can freely replicate
embeddings and other data based on your compliance
needs.
- Set up cross-Region replication for embedding data
stores like Amazon S3 and Amazon OpenSearch Service
within the allowed Regions.
- Implement data ingestion pipelines using AWS Glue to
keep the allowed Regions synchronized for embeddings and
other data.
- Configure monitoring and alerting to detect data
replication issues and compliance violations.
- Optimize data partitioning, compression, and storage
tiering to minimize the cost of cross-Region data
replication.

## Resources

**Related best practices:**

- [REL04-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_identify.html)
- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)
- [REL10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)

**Related documents:**

- [Supported
Regions and Models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)

**Related examples:**

- [Ensure
availability of your data using cross-cluster replication with
Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/ensure-availability-of-your-data-using-cross-cluster-replication-with-amazon-opensearch-service/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05-bp02.html*

---

# GENREL05-BP03 Verify that agent capabilities are available across all regions of availability

Agents require supporting infrastructure to service requests from
foundation models. Using agents across a region of availability
requires the supporting infrastructure to be available in that
region.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by verifying that agents have access to the
appropriate supporting infrastructure such as APIs or functions, so
they may service a wider region of availability.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) -
Data replication across a region of availability horizontally scales
data access infrastructure, enabling foundation models to
consistently service inference requests across a region of
availability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Agents for Amazon Bedrock can be made available across
regions, so long as the models and supporting infrastructure
exist in the desired regions. Amazon Bedrock Agents make API
calls on behalf of a user. Once deployed to a new region,
these agents must have access to the same or
regionally-equivalent API. Consider deploying your APIs across
multiple regions behind a CloudFront distribution with
latency-based routing. When possible, leverage Amazon Route 53
with latency-based routing to direct traffic within your VPC
(and on the Amazon backbone) rather than taking private
traffic public to route to an internal service. If your agent
is not making calls to a foundation model using a cross-region
inference profile, be sure to configure model access in all
required regions.

When using agents in your generative AI architecture, make the
supporting infrastructure, such as APIs and functions,
available across all Regions where your agents are deployed.
This involves replicating the necessary components and
configuring appropriate routing mechanisms to maintain
consistent agent functionality regardless of user location.

### Implementation steps

- Deploy supporting agent infrastructure (APIs, functions)
in primary and secondary Regions.
- Implement latency-based routing or similar mechanisms to
distribute agent requests.
- Verify that agents can access the required resources in
all Regions.
- Monitor agent performance and resource utilization
across Regions.

## Resources

**Related best practices:**

- [REL04-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_identify.html)
- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)
- [REL10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)

**Related documents:**

- [Latency-based
routing](https://docs.aws.amazon.com/Route%C2%A053/latest/DeveloperGuide/routing-policy-latency.html)

**Related examples:**

- [Using
latency-based routing with Amazon CloudFront for a
multi-Region active-active architecture](https://aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05-bp03.html*

---

# GENREL06 — Distributed compute tasks

**Pillar**: Reliability  
**Best Practices**: 1

---

# GENREL06-BP01 Design for fault-tolerance for high-performance distributed computation tasks

Fault-tolerant infrastructure identifies issues in long-running,
high-performance distributed computation tasks and remediates them
before they can disrupt the task. Because these tasks are expensive
and time-consuming, use fault-tolerant infrastructure to reliably
perform model customization jobs.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
model customization workloads, automating recovery during
fine-tuning, pre-training, and other model customization workloads.

**Benefits of establishing this best
practice:**
[Automatically
recover from failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Fault-tolerant infrastructure can
automatically recover from failure, improving the reliability of
long-running, high-performance, distributed computation tasks like
model customization.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model pre-training, continuous pre-training, fine-tuning, and
distillation are some of the many high-performance distributed
computation tasks sometimes required to optimize foundation
models for generative AI workloads. These tasks require the
orchestration of dozens or hundreds of virtual machines,
running workloads over days, weeks, months or longer. These
tasks are particularly susceptible to disruptions, which could
delay or stop training progress. Consider a managed or
automated process that provisions and orchestrates the
infrastructure on your behalf, handles errors, and preserves
the workload's integrity.

Amazon SageMaker AI HyperPod clusters allow customers to
pre-train or fine-tune large language models using managed
infrastructure. Amazon EC2 UltraClusters facilitate large
language model hosting for purpose-built machine learning
accelerators. Additionally, Amazon Bedrock offers managed
fine-tuning, continuous pre-training, or model distillation
for a selection of third-party models.

Amazon SageMaker AI HyperPod, with both Amazon EKS and Slurm
orchestration, establishes comprehensive checkpointing
mechanisms that automatically save training state at regular
intervals to persistent storage like Amazon S3 or FSx for Lustre.

For EKS-based HyperPod, use fault tolerance capabilities by
implementing application-level checkpointing in your training
scripts, and store checkpoints on shared persistent volumes
that survive pod restarts and node failures. Configure
Kubernetes health checks and restart policies to automatically
detect and recover from failed training pods while preserving
progress from the last checkpoint.

For Slurm-based HyperPod, use the auto-resume functionality to
provide zero-touch resiliency infrastructure that
automatically recovers training jobs from the last saved
checkpoint when hardware failures occur. Configure your
training jobs to run inside exclusive allocations using salloc
or sbatch, and verify that your entrypoint scripts maintain
environment consistency across node replacements. Both systems
benefit from SageMaker AI HyperPod's built-in cluster health
monitoring that continuously checks GPU health with DCGM
policies, network connectivity with EFA health checks, and
automatically replaces faulty nodes. The multi-head node
support in Slurm further enhances fault tolerance by providing
backup head nodes that automatically take over if the primary
head node fails.

When implementing fault-tolerant distributed training
manually, evaluate options that can recover the training and
customization progress. Create training job recovery points by
checkpointing model training. Keep track of training progress,
and determine when to halt training based on observed metrics.
Consider leveraging performant storage solutions (like Amazon FSx for Lustre) that provide distributed compute tasks rapid
access to large data volumes at scale. Managed training and
model customization solutions provide these capabilities, but
you can also consider self-hosting for some model training and
customization initiatives.

Use managed services and purpose-built infrastructure to
handle the complexity and resource requirements of distributed
model customization workloads. AWS offers several solutions
that can help improve the reliability and efficiency of these
tasks:

- **Amazon SageMaker AI
HyperPod:** A managed service that automates the
provisioning and orchestration of distributed training
infrastructure, including handling node failures,
checkpointing, and other fault-tolerance mechanisms.
HyperPod is optimized for large language model training
and can use specialized hardware like AWS Trainium
instances.
- **Amazon Bedrock:**
Provides managed workflows for fine-tuning, continued
pre-training, and model distillation, abstracting away the
underlying infrastructure management and failure handling.
- **AWS Batch:** A
fully-managed batch processing service that can run
distributed computational tasks, including model
customization, with automatic scaling, retry logic, and
resource optimization.

When implementing fault tolerance manually, focus on
strategies like checkpointing, progress tracking, and
automated recovery. Use high-performance storage solutions
like Amazon FSx for Lustre to provide rapid access to training
data. Configure your workflow to handle node failures, spot
instance interruptions, and other disruptions gracefully.

Continuously monitor the distributed workloads for
performance, resource utilization, and failures. Use Amazon CloudWatch to set alerts and thresholds, and use Amazon EventBridge to run automated remediation actions. Analyze logs
and metrics to identify bottlenecks and optimize the
distributed architecture over time.

### Implementation steps

- Evaluate managed services like SageMaker AI HyperPod,
Bedrock, and Batch for your model customization needs.
- If implementing a custom distributed workflow, provision
high-performance storage and compute resources.
- Implement checkpointing, progress tracking, and
automated retry mechanisms to handle failures.
- Configure monitoring, alerting, and automated
remediation for the distributed workloads.
- Continuously analyze performance, costs, and reliability
to optimize the distributed architecture.

## Resources

**Related best practices:**

- [REL10-BP02](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_single_az_system.html)
- [REL11-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_monitoring_health.html)
- [REL11-BP03](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_auto_healing_system.html)

**Related documents:**

- [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
- [Customize
your model to improve its performance for your use case](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)
- [Resilience-related
Kubernetes labels by SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency-node-labels.html)

**Related examples:**

- [Speed
up training on Amazon SageMaker AI using Amazon FSx for Lustre
and Amazon EFS file systems](https://aws.amazon.com/blogs/machine-learning/speed-up-training-on-amazon-sagemaker-using-amazon-efs-or-amazon-fsx-for-lustre-file-systems/)
- [Customize
models in Amazon Bedrock with your own data using fine-tuning
and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)
- [Amazon BedrockModel Customization Workshop Notebooks](https://github.com/aws-samples/amazon-bedrock-customization-workshop)
- [Amazon SageMaker AI Hyperpod Recipes](https://github.com/aws/sagemaker-hyperpod-recipes)
- [Introducing Amazon SageMaker AI HyperPod: a purpose-built infrastructure for distributed training
at scale](https://aws.amazon.com/blogs/aws/introducing-amazon-sagemaker-hyperpod-a-purpose-built-infrastructure-for-distributed-training-at-scale/)
- [Introducing
Amazon SageMaker AI HyperPod, a purpose-built infrastructure
for distributed training at scale](https://aws.amazon.com/blogs/aws/introducing-amazon-sagemaker-hyperpod-a-purpose-built-infrastructure-for-distributed-training-at-scale/)
- [Ray
jobs on Amazon SageMaker AI HyperPod: scalable and resilient
distributed AI](https://aws.amazon.com/blogs/machine-learning/ray-jobs-on-amazon-sagemaker-hyperpod-scalable-and-resilient-distributed-ai/)
- [SageMaker AI
HyperPod cluster resiliency](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-resiliency-slurm.html)
- [Reduce
ML training costs with Amazon SageMaker AI HyperPod](https://aws.amazon.com/blogs/machine-learning/reduce-ml-training-costs-with-amazon-sagemaker-hyperpod/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel06-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
