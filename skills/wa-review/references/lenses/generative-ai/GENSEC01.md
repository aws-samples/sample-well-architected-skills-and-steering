# GENSEC01 — Endpoint security

**Pillar**: Security  
**Best Practices**: 4

---

# GENSEC01-BP01 Grant least privilege access to foundation model endpoints

Granting least privilege access to foundation model endpoints helps
limit unintended access and encourages a zero-trust security
framework. This best practice describes how to secure foundation
model endpoints associated with generative AI workloads.

**Desired outcome:** When
implemented, this best practice reduces the risk of unauthorized
access to a foundation model endpoint and helps create a process to
verify continuous adherence to least-privilege principle.

**Benefits of establishing this best
practice:**

- [Implement
a strong identity foundation](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - Least privilege access
permissions foster access to foundation model endpoints only for
authorized identities.
- [Apply
security at all layers](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - Least privilege access permissions
on endpoints provides an identity-based layer of security,
regardless of the hosting paradigm.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Least privilege access is important to establish an
identity-based layer of security for generative AI workloads.
It helps verify that access to foundation model endpoints is
granted to authorized identities only while also helping
verify the data received matches the authorization boundary of
their role in their organization. Organization AI policy
documents should describe permission boundaries for AI
systems, related data stores, and other related components to
a generative AI workflow. This policy document should be
reviewed as part of a regular access review for AI workloads.

Amazon Bedrock, the Amazon Q family of applications, and
Amazon SageMaker AI feature endpoint APIs. Client applications
can access the APIs directly through SDKs, open source
frameworks or custom abstraction layers. You can use AWS Identity and Access Management to limit access to foundation
model endpoints to IAM roles. These roles should be granted
least privilege access and utilize session durations and
permissions boundaries to further control access.

[AWS PrivateLink](https://aws.amazon.com/privatelink/) connections can be established from
customer VPCs to Amazon generative AI services to further
secure communication. For endpoints hosted on an Amazon SageMaker AI inference endpoint, employ least privileged network
access to the inference endpoint, and verify that only the
systems allowed to perform inference on the endpoint can do
so.

Amazon SageMaker AI Hyperpod defines two primary roles: cluster
admin users and data scientist users.

Cluster admins are responsible for creating, configuring, and
managing HyperPod clusters, including setting up IAM roles,
orchestrator access (EKS or Slurm), and permissions for
cluster resources.

Data scientist users focus on running ML workloads, connecting
to clusters, and submitting jobs using the orchestrator CLI or
HyperPod CLI.

To help protect these roles following the best practice of
least privilege, each role should be granted only the
permissions necessary for their tasks. Cluster admins should
have granular IAM policies that allow them to manage clusters
and assign roles, but not unrestricted access to all AWS
resources. Data scientists should be assigned roles that
permit only the actions needed to submit and monitor jobs,
such as starting sessions or accessing specific S3 buckets.

HyperPod clusters themselves must assume roles with the
minimum required permissions (like
`AmazonSageMaker AIHyperPodServiceRolePolicy`)
to interact with AWS services such as Amazon S3, Amazon CloudWatch, and Amazon EC2 Systems Manager. Using IAM condition keys, RBAC (for
EKS), and resource tagging further refines access control,
verifying that both cluster admins and data scientists operate
within tightly scoped permissions and reducing the risk of
unauthorized access to foundation model endpoints and
sensitive resources.

Additionally, model access can be controlled at the
organization layer through other policy types such as service
control policies, resource control policies, session policies,
and permission boundaries. These policy types can provide ways
to block or restrict models your organization has not approved
in addition to services you may want to restrict by accounts,
Regions, organization, and the maximum permissible boundary
allowed for IAM users.

[Other
policy types](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html#security_iam_access-manage) offered by Amazon Q Developer manage
access through a subscription model. When provisioning
subscription-level access to a generative AI service, confirm
that the user needs that access and that subscription level
matches the required access level to the service.
Identity-based permissions and subscription-based service
access can be managed through single-sign-on (SSO) to
integrate with your enterprise identity provider.

### Implementation steps

- Create a custom policy document granting least-privilege
access to set of specific foundation model endpoints.

Limit access to specific resource ARNs and to a specific
set of actions.
- Consider defining conditions to further restrict the
allowable traffic, such as requests coming from a specific
VPC.

- Create an IAM role to be used by users or services to access
the endpoint and attach the custom policy to it. If more
permissions are needed for this role, attach the required
policies on as-needed bases.

Utilize permission boundaries at the role level to set the
maximum permissions that an identity-based policy can
grant.
- Conditions can be added to a role's trust policy to
further limit access to who can assume the role.

- Verify the new role for API calls to endpoints are protected
by this policy.

An example of an endpoint to protect might be a production
Amazon Bedrock endpoint servicing real-time inference
through a VPC-Hosted application.

- For a generative AI subscription based generative AI
application such as Amazon Q Developer, provision
subscription-level access matching the subscriber's business
needs.

## Resources

**Related best practices:**

- [SEC02-BP01](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_enforce_mechanisms.html)
- [SEC02-BP02](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_unique.html)
- [SEC02-BP06](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_groups_attributes.html)
- [SEC03-BP01](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define.html)
- [SEC03-BP02](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html)

**Related documents:**

- [AWS re:Invent 2023-Use new IAM Access Analyzer features on your
jouney to least privilege](https://www.youtube.com/watch?v=JpemUkU8INA)
- [Understanding
Subscriptions in Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-understanding.html)
- [Amazon Q Business Subscription Tiers and Index Types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html)
- [OWASP
Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [AWS Identity and Access Management for SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites-iam.html)
- [IAM users for cluster admin](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites-iam.html#sagemaker-hyperpod-prerequisites-iam-cluster-admin)
- [IAM users for scientists](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites-iam.html#sagemaker-hyperpod-prerequisites-iam-cluster-user)
- [IAM
role for SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites-iam.html#sagemaker-hyperpod-prerequisites-iam-role-for-hyperpod)

**Related examples:**

- [Techniques
for Writing Least Privilege IAM Policies](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/)
- [When
and Where to use IAM Permissions Boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/)
- [Example
Permissions Boundaries](https://github.com/aws-samples/example-permissions-boundary)
- [Overseeing
AI Risk in a Rapidly Changing Landscape](https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/)
- [Configure
Amazon Q Business with AWS IAM Identity Center trusted
identity propagation](https://aws.amazon.com/blogs/machine-learning/configuring-amazon-q-business-with-aws-iam-identity-center-trusted-identity-propagation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec01-bp01.html*

---

# GENSEC01-BP02 Implement private network communication between foundation models and applications

Implementing a scoped down data perimeter on foundation model
endpoints helps reduce the surface-area of potential threat vectors
and encourages a zero-trust security architecture. This best
practice describes how to implement private network communications
for your generative AI workloads.

**Desired outcome:** When
implemented, this best practice reduces the risk of unauthorized
access to a foundation model endpoint. It also helps create a
process to grant least privileged access to authorized parties.

**Benefits of establishing this best
practice:**

- [Apply
security at all layers](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - Private network communications
facilitate an additional layer of security within your application.
- [Protect
data in transit and at rest](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - Using private networks instead
of the default public endpoints helps to protect data in transit,
especially when combined with encryption techniques.

**Level of risk exposed if this practice is
not established:** High

## Implementation guidance

Without private network communication between foundation model
endpoints and generative AI applications, access to these
endpoints would be available through the public internet,
increasing exposure. Implementing a private network between a
foundation model and a generative AI application requires full
control over application hosting and network traffic
configuration.

AWS PrivateLink supports a range of AWS generative AI managed
services, including Amazon Bedrock and the Amazon Q family of
services. AWS PrivateLink facilitates private network
communications for customers across the AWS network within
their own account. This capability enables customers to
maintain private network communication between generative AI
managed services and applications making the request without
using the public internet. AWS PrivateLink works for
self-managed services as well, like Amazon SageMaker AI.
Hosted inference endpoints in Amazon SageMaker AI can be
deployed in a Virtual Private Cloud (VPC). In addition to
network controls which help protect and secure infrastructure,
endpoints deployed in a VPC can be made private using AWS PrivateLink. AWS PrivateLink enables VPC instances to
communicate with service resources without the need for public
IP addresses, reducing potential threats from public internet
exposure.

In Amazon SageMaker AI HyperPod using both EKS and Slurm
orchestrators, deploy your clusters within a private VPC and
configure the necessary subnets and security groups to
restrict access. For EKS, place your EKS cluster and SageMaker AI
HyperPod cluster in the same VPC, using private subnets and
security groups that only allow required internal
communication. For Slurm, similarly, launch your HyperPod
cluster in a VPC with private networking, and isolate all
compute nodes and storage (such as FSx for Lustre) from the
public internet. In both orchestrators, you can use AWS PrivateLink (VPC Endpoint, VPCE) to securely connect to
SageMaker AI endpoints, Amazon S3, and other AWS services without
traversing the public internet.

Verify that foundation models have private network access to
supporting infrastructure as well, such as vector stores or
external tools for agents. Retrieval-augmented generation
workflows commonly access data from vector databases, and you
should provide this access over a private network connection.
The same is true for external tools or APIs that may be called
by an agent. Keeping these network connections private helps
reduce exposure to external threats.

### Implementation steps

- Determine the VPC you need to create a private endpoint
in.
- Select the service you wish to create a private route to
from your VPC.
- Configure the endpoint to allow least privilege access
for your services.

- Network access to the interface endpoint is controlled
using security groups and policy documents.

## Resources

**Related best practices:**

- [SEC05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html)
- [SEC05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html)

**Related documents:**

- [AWS Expert Paper on PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/aws-privatelink.html)
- [Encryption
best practices for Amazon S3](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/s3.html)
- [Getting
started with Amazon EKS support in SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-prerequisites.html)
- [Orchestrating
SageMaker AI HyperPod clusters with Slurm](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-slurm.html)

**Related examples:**

- [Use
AWS PrivateLink to Set Up Private Access to Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/use-aws-privatelink-to-set-up-private-access-to-amazon-bedrock/)
- [Overseeing
AI Risk in a Rapidly Changing Landscape](https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec01-bp02.html*

---

# GENSEC01-BP03 Implement least privilege access permissions for foundation models accessing data stores

Foundation models can aggregate and generate rich insights from data
they have been trained on or interact with from the APIs providing
inputs and outputs. It is important to treat generative AI systems
and their foundation models just as you would treat privileged users
when providing access to data. This best practice describes how to
provide generative AI APIs and services with appropriate access to
data.

**Desired outcome:** When
implemented, this best practice reduces the risk of accidentally
using unauthorized internal data when training and fine-tuning
foundation models. Additionally, a process will be implemented to
make sure that foundation models and workloads are granted only the
minimum necessary access to data, following the principle of least
privilege

**Benefits of establishing this best
practice:**

- [Implement
a strong identity foundation](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - least privilege access
permissions foster model access to only the required data.
- [Apply
security at all layers](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - least privilege data access for
foundation models provides an identity-based layer of data security.
- [Protect
data in transit and at rest](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - least privilege data access
for foundation models offers an added protection for data via access
controls.
- [Keep
people away from data](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - least privilege data access for
foundation offers helps prevent sweeping access to data for
foundation models.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Generative AI architecture patterns like Retrieval Augmented
Generation (RAG) or generative business intelligence (BI) use
external data to correlate with the foundation models output
and address user prompts. In many cases, a single vector
database may store data intended for several use cases, some
of which require additional authorizations to access. While
controls can be implemented at the foundation model layer,
this approach alone is insufficient. Addressing access to data
requires a multi-layered strategy. This is necessary not only
for RAG use cases but also for model customization and
pre-training processes.

When securing foundation models and protecting sensitive data,
customers should deploy data stores in a VPC with strong
access controls. Implementing zero-trust security principles
and enforcing least privilege access for users and
applications reduces the risks of unauthorized access. In the
software layer, customers should regularly update data stores
with the latest security patches to stay protected. Using
temporary, least privilege credentials for application access
reduces the risk of unauthorized access even if credentials
are unintentionally exposed. Keeping data store drivers and
SDKs up to date maintains compatibility and helps to mitigate
known issues. For the data layer, implementing granular
controls over foundational model elements allows for precise
management of sensitive information like personally
identifiable information (PII) using controls such as
guardrails in both Amazon Bedrock and Amazon SageMaker AI.

When using data for model training, especially in generative
AI scenarios, applying robust data obfuscation and
anonymization techniques can avoid unintended exposure of
sensitive data through model outputs. Vector databases
supported with services such as Amazon OpenSearch Service
offers efficient ways to sanitize and manage large-scale data
for AI workloads, improving both performance and security. At
the application layer, customers should regularly review and
refine Access Control Lists to stop unauthorized access to
data. Utilizing metadata filtering capabilities in vector
stores and knowledge bases can enable more granular access
control, allowing for data segregation based on user roles or
project requirements. For Identity and Access Management,
creating IAM roles with precision, such as attribute based
access controls, helps maintain the principle of least
privilege. Designing IAM policy documents with properly scoped
permissions can help stop improper access. Amazon Bedrock
Knowledge Bases can add a layer of abstraction to data access,
simplifying permission management across multiple data
sources.

When designing the overall architecture, aligning data access
permissions with data architecture decisions can lead to a
more coherent and manageable security posture. This approach
simplifies auditing and reduces the risk of misconfiguration.
Setting up a dedicated process for preparing training data and
using separate data stores and classification designed for
generative AI workloads, helps isolate sensitive data and
provides an additional layer of protection against
unauthorized access or misuse.

When using Amazon SageMaker AI HyperPod on both Amazon EKS and
Slurm, assign IAM roles to each workload or user that grant
only the specific permissions needed to access required data
stores, such as S3 buckets or databases.

For Amazon EKS, use Kubernetes service accounts mapped to IAM
roles (IRSA) to verify that pods have only the minimum access
needed.

In Slurm, configure IAM roles for each compute group or job,
and restrict permissions to only the necessary resources.

Regularly audit these roles and policies using tools like AWS
IAM Access Analyzer and update them as requirements evolve.
Apply resource-level policies on S3 buckets and databases to
further limit access, and use security groups to control
network communication between nodes and data sources. Verify
that both users and foundation models in SageMaker AI HyperPod
clusters can only access the data they are explicitly
authorized for, reducing the risk of accidental or malicious
data exposure.

### Implementation steps

- Classify data by its usage. Data can belong to several
usage patterns such as training, RAG, analytics, etc.
Classification of data helps to prevent and identify
misuse.
- Deploy a vector data store into a secure VPC, setting
appropriate access controls on the datastore for various
roles (for example, administrator, read-only, or
power-user). Consider extending role definitions to
encompass generative AI workloads (like
model-XX-RAG).
- Develop a data ingestion pipeline which obfuscates or
removes data that should not be processed by a
foundation model. Examples of this data might be
personal information. The scope of this data is informed
largely by the workload use case. Ingest this data from
your data lake into the vector store lake house.

A use case for a customer service assistant may require
access to handbooks, documentation, and customer service
material, not company financials, staff information or
HR policies.
- Sanitizing for prohibited material should happen before
the model accesses the data, at time of ingestion.

- Create least-privilege access policies for foundation
model and generated AI workloads. This Policy Document
should contain resource identifiers granting explicit
access to specific data in the vector datastore.
- Test access to data using curated prompts designed to
confirm models are not allowed to access sensitive
information.
- Similar principles apply for model training and model
customization workloads, though data used for model
training and model customization typically resides in a
data lake, separate from a compute engine.

## Resources

**Related best practices:**

- [SEC03-BP01](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_define.html)
- [SEC03-BP02](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html)
- [SEC07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_identify_data.html)
- [SEC07-BP02](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_define_protection.html)
- [SEC08-BP04](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_access_control.html)

**Related documents:**

- [AWS re:Invent 2023 - Use new IAM Access Analyzer features on your
journey to least privilege](https://www.youtube.com/watch?v=JpemUkU8INA)
- [AWS re:Inforce 2022 - Strategies for achieving least privilege
(IAM303)](https://www.youtube.com/watch?v=j57tBC6U4kk)
- [AWS Prescriptive Guidance: Creating a data strategy on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/aws-architecture.html)
- [Identity
and Access Management in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html)
- [Fine-Grained
Access Control in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html)
- [Amazon Bedrock Knowledge Bases Meta-Data Filtering](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)
- [Protect
Data at Rest Using Encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest.html)
- [Data Protection in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/data-protection.html)

**Related examples:**

- [Techniques
for Writing Least Privilege IAM Policies](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/)
- [When
and Where to use IAM Permissions Boundaries](https://aws.amazon.com/blogs/security/when-and-where-to-use-iam-permissions-boundaries/)
- [Example
Permissions Boundaries](https://github.com/aws-samples/example-permissions-boundary)
- [Overseeing
AI Risk in a Rapidly Changing Landscape](https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec01-bp03.html*

---

# GENSEC01-BP04 Implement access monitoring to generative AI services and foundation models

Generative AI services and foundation models can be resource
intensive to use and can be misused. Implementing access monitoring
on these services and models helps to identify, triage and resolve
unintended access quickly.

**Desired outcome:** When
implemented, this current guidance monitors access to sensitive
generative AI systems and foundation models. Unintended and
unauthorized use of generative AI services and foundation models can
be identified quickly and further action can be taken if
appropriate.

**Benefits of establishing this current
guidance:** [Maintain
traceability](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) - Access monitoring traces access to generative
AI services and foundation models.

**Level of risk exposed if this current
guidance is not established:** High

## Implementation guidance

AWS CloudTrail can be used to monitor access to AWS services.
To track service-level access to generative AI services such
as Amazon Bedrock, customers can utilize AWS CloudTrail. In
Amazon Bedrock, customers can additionally turn on model
invocation logging to collect metadata, requests and responses
for model invocations in an AWS account. Similar capabilities
exist for the Amazon Q family of services.

For additional controls, consider implementing guardrails to
mask or remove sensitive data elements (like personal data) in
the prompts before foundation model invocations are made. This
additional step helps to mitigate the unintended or
unauthorized access to private or restricted data and makes
sure your organization policies and responsible AI governance
are followed.

When using Amazon SageMaker AI HyperPod environments using Amazon EKS or Slurm, enable AWS CloudTrail to log API calls and
resource access events related to SageMaker AI, EKS, and Slurm
workloads. Configure Amazon CloudWatch Logs to capture
detailed logs from training jobs, inference endpoints, and
orchestration layers, and record user actions and model
invocations.

Set up centralized log storage in Amazon S3 or CloudWatch Logs
for secure retention and analysis. Use CloudWatch Alarms or
AWS Security Hub CSPM to automatically alert on suspicious or
unauthorized activities, and regularly review logs to detect
unusual patterns or potential security incidents.

These strategies provide comprehensive traceability, help
support compliance, and enable rapid detection and response to
unauthorized access, fully aligning with AWS Well-Architected
security best practices for generative AI workloads.

Consider implementing access or query logging on data stores
or generative business intelligence (BI) solutions. For
traceability purposes, log both name of the generative AI
application and the end-user making the request. Agentic
workloads will require additional logging for each agent
called. Generative AI workloads should be architected with
application identities for traceability purposes. Consider
recording these identities in your organization's AI policy
document alongside other relevant security information such as
workload owner or permission boundaries.

### Implementation steps

- In Amazon Bedrock, configure model invocation logging to
track model invocations and store the logs in Amazon S3,
Amazon CloudWatch Logs, or both.
- In Amazon Q Developer, capture user activity by enabling
user activity capture in the settings.
- In Amazon Q Business, configure log delivery for
analysis and review into Amazon S3, Amazon CloudWatch Logs, or Amazon Data Firehose.
- For self-hosted models on Amazon SageMaker AI Inference
Endpoints, configure logging using your preferred
logging solution.
- Introduce logging, monitoring and telemetry capture in
additional application layers, depending on your
specific workload.

## Resources

**Related best practices:**

- [SEC03-BP08](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_share_securely.html)

**Related documents:**

- [Monitoring
Amazon Q Business and Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/monitoring-overview.html)
- [Monitoring
Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/monitoring-overview.html)

**Related examples:**

- [Monitoring
Generative AI Applications using Amazon Bedrock and Amazon CloudWatch Integration](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/)
- [Overseeing
AI Risk in a Rapidly Changing Landscape](https://aws.amazon.com/blogs/enterprise-strategy/overseeing-ai-risk-in-a-rapidly-changing-landscape/)
- [Observability
for SageMaker AI HyperPod Cluster Orchestrated by Amazon EKS](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability.html)
- [SageMaker AI
HyperPod Cluster Resources Monitoring (Slurm)](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm.html)
- [Logging
Amazon SageMaker AI API Calls Using AWS CloudTrail](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-using-cloudtrail.html)
- [Amazon SageMaker AI HyperPod Now Integrates with Amazon EventBridge](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-sagemaker-hyperpod-integrates-amazon-eventbridge-status-change-events)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec01-bp04.html*

---
