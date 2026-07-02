# MLSEC04 — Model development

**Pillar**: Security  
**Best Practices**: 3

---

# MLSEC04-BP01 Secure governed ML environment

Creating a secure and governed ML environment allows you to protect
valuable data and models while enabling teams to innovate
efficiently. By implementing proper guardrails, monitoring, and
security practices, you maintain control while providing the
flexibility ML practitioners need to deliver business value.

**Desired outcome:** You establish a
secure ML operational environment using AWS managed services that
incorporates best practices for security, governance, and
monitoring. You create development environments that allow data
scientists to explore data safely while maintaining organizational
security standards. Your ML environments are centrally managed with
proper access controls, yet offer self-service capabilities to
improve productivity. This balance between security and flexibility
enables your organization to innovate while protecting sensitive
assets.

**Common anti-patterns:**

- Using a single shared account for ML workloads regardless of
sensitivity or access requirements.
- Allowing unrestricted access to ML infrastructure and production
environments.
- Implementing manual provisioning processes that create
bottlenecks for data scientists.
- Neglecting to isolate environments containing sensitive data.
- Failing to implement continuous monitoring and detection
controls for ML operations.

**Benefits of establishing this best
practice:**

- Reduced security risks through proper isolation and access
controls.
- Improved governance with enforced security guardrails.
- Enhanced productivity through self-service capabilities.
- Improves adherence to regulatory requirements.
- Simplified management of ML environments.
- Faster time-to-market for ML initiatives.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Securing your ML environment requires thoughtful architecture that
balances security with productivity. You need to consider how
different teams interact with ML resources and implement controls
appropriate to their roles and the sensitivity of data being
processed. AWS provides managed services like
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) that can be configured with security best
practices in mind.

Begin by understanding your organization's access patterns and
data sensitivity levels. This knowledge assists you when
determining how to structure your AWS accounts and implementing
appropriate security controls. For example, you might separate
development, testing, and production environments across different
accounts with increasing security restrictions. This multi-account
strategy allows you to implement tailored security controls for
each environment while maintaining proper isolation.

Once you've established your account structure, implement
preventive guardrails using
[AWS Organizations](https://aws.amazon.com/organizations/) and service control policies (SCPs) to
enforce security boundaries. Detective controls using services
like [AWS Config](https://aws.amazon.com/config/) and
[Amazon GuardDuty](https://aws.amazon.com/guardduty/) provide continuous monitoring to identify
potential security issues. By combining preventive and detective
controls, you create defense-in-depth protection for your ML
environments.

For environments handling sensitive data, implement additional
security measures like network isolation, encryption, and
fine-grained access controls. Amazon SageMaker AI can be deployed
within a VPC to limit network access, while
[AWS KMS](https://aws.amazon.com/kms/)
provides robust encryption capabilities for data at rest and in
transit. These measures protect sensitive information throughout
the ML lifecycle.

### Implementation steps

- **Break out ML workloads by
organizational unit access patterns**. Create a
multi-account strategy that aligns with your organization's
structure and security requirements. For example, create
separate accounts for data science development, model
training, and production model deployment. This separation
allows you to implement role-based access control (RBAC)
with appropriate permissions for each team. Use
[Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html) to quickly define
persona-based IAM roles for different user types (data
scientists, MLOps engineers, business analysts) with
preconfigured templates that provide least privilege access.
Use
[AWS Organizations](https://aws.amazon.com/organizations/) to manage your multi-account
environment efficiently.
- **Use guardrails and service control
policies (SCPs) to enforce best practices**.
Implement SCPs through
[AWS Organizations](https://aws.amazon.com/organizations/) to establish preventive guardrails that
restrict actions across accounts. For example, create
policies that block the disabling of security services,
limit the AWS regions that can be used, or restrict the
creation of public resources. Complement SCPs with
[AWS Config](https://aws.amazon.com/config/) rules to detect non-compatible resources and
automatically remediate issues. Limit infrastructure
management access to administrators while allowing data
scientists to focus on model development.
- **Verify that sensitive data has
access through restricted, isolated environments**.
Implement
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) within a private VPC to control network
traffic to and from your ML environment. Configure security
groups and network ACLs to restrict access to authorized
sources. Use
[AWS PrivateLink](https://aws.amazon.com/privatelink/) to access AWS services without traversing
the public internet. Enable encryption for sensitive data
using [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) for both data at rest and in
transit. Review service dependencies to verify that they
meet your security requirements.
- **Secure ML algorithm implementation
using a restricted development environment**.
Deploy
[Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) with appropriate security controls
to provide data scientists with a secure development
environment. Implement
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) roles with least
privilege permissions for each development environment. Use
[Amazon SageMaker AI Domain](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html) configurations to manage user access
to resources. Scan container images for vulnerabilities
before deploying them for model training or hosting using
[Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html).
- **Implement centralized management and
monitoring**. Use
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to track API activity across your ML
environments. Deploy
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for operational monitoring of your ML
resources. Implement
[Amazon GuardDuty](https://aws.amazon.com/guardduty/) to detect suspicious activity. Centralize
logs in a dedicated security account for comprehensive
visibility across your ML environments. Create automated
alerts for security-related events that require
investigation.
- **Enable self-service provisioning
with guardrails**. Implement
[Service Catalog](https://aws.amazon.com/servicecatalog/) to provide pre-approved, secure
templates for ML resources like SageMaker AI environments.
Configure lifecycle policies to automatically shut down idle
resources and reduce costs. Use
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) or
[AWS CDK](https://aws.amazon.com/cdk/) to define infrastructure as code with security
best practices built in. This allows data scientists to
provision resources quickly while maintaining adherence to
organizational standards.
- **Secure model artifacts and ML
pipelines**. Implement version control for models
and code using
[Amazon SageMaker AI MLflow Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html). Configure
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) with appropriate access controls
to automate the ML lifecycle. Use
[AWS CodePipeline](https://aws.amazon.com/codepipeline/) and
[AWS CodeBuild](https://aws.amazon.com/codebuild/) to implement CI/CD for ML applications with
security checks built into the deployment process.
- **Implement foundation model security
controls**. When using large language models (LLMs)
or other foundation models, implement guardrails to block
the generation of harmful content. Implement content
filtering to verify responsible AI usage. For enterprise
governance of foundation models, implement
[SageMaker AI
JumpStart Private Model Hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html) to create curated
repositories of approved models with centralized access
controls and version management. Use
[SageMaker AI
Catalog](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates-custom.html) as a central metadata hub for secure sharing
and governed access to ML assets across business units.
Implement
[Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) to document model limitations,
ethical considerations, and intended uses. Monitor model
outputs for drift and bias using
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html).

## Resources

**Related documents:**

- [Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html)
- [Private
curated hubs for foundation model access control in
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html)
- [Admin
guide for private model hubs in Amazon SageMaker AI
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide.html)
- [Configure
security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security.html)
- [Build
a secure enterprise machine learning platform on AWS](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.html)
- [Security
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [Model
governance to manage permissions and track model
performance](https://docs.aws.amazon.com/sagemaker/latest/dg/governance.html)
- [Setting
up secure, well-governed machine learning environments on
AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws)
- [Securing
Amazon SageMaker AI Studio connectivity using a private
VPC](https://aws.amazon.com/blogs/machine-learning/securing-amazon-sagemaker-studio-connectivity-using-a-private-vpc/)
- [Enable
self-service, secured data science using Amazon SageMaker AI and
Service Catalog](https://aws.amazon.com/blogs/mt/enable-self-service-secured-data-science-using-amazon-sagemaker-notebooks-and-aws-service-catalog/)
- [Accelerating
Machine Learning Development with Data Science as a Service
from Change Healthcare](https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/)

**Related videos:**

- [Architectural
best practices for machine learning applications](https://www.youtube.com/watch?v=fBytsYBVgbo)
- [Secure
and compliant machine learning for regulated industries](https://www.youtube.com/watch?v=8p-B3sTLmFg)
- [Amazon SageMaker AI Model Development in a Highly Regulated
Environment (SDD315)](https://youtu.be/cSYFqKRQ0j0?t=1051)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec04-bp01.html*

---

# MLSEC04-BP02 Secure inter-node cluster communications

Machine learning frameworks require secure communications between
computational nodes to maintain data integrity and protect sensitive
information during model training. By implementing encryption for
inter-node communications, you safeguard coefficient exchanges and
protect synchronized information across distributed environments.

**Desired outcome:** You establish
encrypted communication channels between computational nodes in your
machine learning clusters, protecting sensitive model data,
parameters, and training information as it traverses networks. This
improves data integrity and confidentiality during distributed
training operations while maintaining the performance requirements
of your machine learning workloads.

**Common anti-patterns:**

- Assuming internal network communications are inherently secure
and don't require encryption.
- Implementing encryption only for external communications but
neglecting inter-node traffic.
- Using outdated or weak encryption protocols for performance
reasons.
- Neglecting to rotate encryption certificates and credentials
regularly.

**Benefits of establishing this best
practice:**

- Protection of proprietary algorithms and model parameters during
training.
- Prevention of data leakage and unauthorized access to training
data.
- Improves adherence to data protection regulations and security
requirements.
- Consistent security posture across your ML infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For machine learning frameworks like TensorFlow that rely on
distributed computing, secure inter-node communication is
essential to protect the integrity and confidentiality of the
training process. During distributed training, nodes exchange
critical information like model coefficients, gradients, and
parameter updates. This information contains valuable intellectual
property about your models and potentially sensitive insights
derived from your training data.

When implementing distributed machine learning workloads, encrypt
that data transmitted between computational nodes using
industry-standard protocols. This is particularly important when
your infrastructure spans across different networks, availability
zones, or even Regions. Encryption in transit stops unauthorized
parties from intercepting or tampering with model data as it moves
between nodes.

AWS services like
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) and
[Amazon EMR](https://aws.amazon.com/emr/)
provide built-in capabilities to secure inter-node communications,
making it more straightforward to implement this best practice
without extensive custom configuration.

### Implementation steps

- **Enable inter-node encryption in
Amazon SageMaker AI**. Amazon SageMaker AI provides
automatic encryption for inter-container communication
during training jobs. When configuring your training job,
enable encryption to verify that data passed between
containers traverses over an encrypted tunnel. For
large-scale distributed training, use
[Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html) which provides managed, resilient
clusters with built-in security features including VPC
integration, automatic health checks, and secure
node-to-node communication for foundation model training.
This protects your model parameters and gradients during the
training process without requiring additional configuration.
- **Configure TLS for distributed
TensorFlow workloads**. For TensorFlow-based
distributed training, implement Transport Layer Security
(TLS) to secure communications between worker nodes.
TensorFlow supports TLS configuration through environment
variables and configuration parameters. Use properly signed
certificates and configure both client and server-side
authentication for maximum security.
- **Enable encryption in transit in
Amazon EMR**. When using
[Amazon EMR](https://aws.amazon.com/emr/) for machine learning workloads, implement
security configurations that enable encryption in transit.
Amazon EMR makes it simple to create security configurations
that specify the use of Transport Layer Security (TLS)
certificates for encrypting data in transit between cluster
nodes. This protects data whether it's stored locally on the
cluster or in Amazon S3.
- **Implement secure key
management**. Use
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) to manage the encryption
keys used for securing inter-node communications. This
provides centralized control, auditing, and automatic key
rotation, enhancing your security posture while simplifying
key management operations.
- **Configure secure cluster
authentication**. Implement strong authentication
mechanisms to verify that only authorized nodes can join
your cluster and participate in the distributed training
process. Use certificate-based authentication where possible
and implement node identity verification as part of your
security configuration.
- **Regularly rotate security
credentials**. Establish a process for regularly
rotating TLS certificates, encryption keys, and other
security credentials used in your distributed training
environment. This limits the potential impact of compromised
credentials and aligns with security best practices.
- **Monitor encrypted
communications**. Implement logging and monitoring
for your encrypted communications channels to detect
potential security issues. Configure alerts for unusual
traffic patterns or authentication failures that might
indicate attempted security breaches.
- **Secure foundation model
communication**. When using distributed training
for large language models or other foundation models,
encrypt parameter server communications, as these contain
valuable intellectual property. For AI workloads on Amazon SageMaker AI, enable inter-container encryption to protect
model weights and gradients during the training process.

## Resources

**Related documents:**

- [Amazon SageMaker AI HyperPod Prerequisites](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html)
- [Protect
Communications Between ML Compute Instances in a Distributed
Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/train-encrypt.html)
- [Encryption
options for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-data-encryption-options.html)
- [Configure
security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security.html)
- [Security
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [Encrypt
data in transit using a TLS custom certificate provider with
Amazon EMR](https://aws.amazon.com/blogs/big-data/encrypt-data-in-transit-using-a-tls-custom-certificate-provider-with-amazon-emr/)
- [Building
secure machine learning environments with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/)
- [Amazon SageMaker AI Studio Admin Best Practices](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/data-protection.html)

**Related videos:**

- [Architectural
best practices for machine learning applications](https://www.youtube.com/watch?v=fBytsYBVgbo)
- [Secure
and compliant machine learning for regulated industries](https://www.youtube.com/watch?v=8p-B3sTLmFg)

**Related examples:**

- [Amazon SageMaker AI secure distributed training examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-python-sdk)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec04-bp02.html*

---

# MLSEC04-BP03 Protect against data poisoning threats

Protect your machine learning models and data by implementing
security measures against data poisoning attacks, which can
compromise model performance and accuracy. Data poisoning occurs
through data injection (adding corrupt training data) or data
manipulation (changing existing data like labels), resulting in
inaccurate and weakened predictive capabilities. By identifying and
addressing corrupt data using security methods and anomaly detection
algorithms, you can maintain data integrity and protect against
threats including ransomware and malicious code in third-party
packages.

**Desired outcome:** You have
implemented robust protection mechanisms for your machine learning
training data and models. These protections include data validation
procedures, monitoring for data drift, version control for both data
and models, and rollback capabilities. Your ML systems can detect
potential poisoning attempts and maintain model performance
integrity through security best practices that protect data
throughout its lifecycle.

**Common anti-patterns:**

- Collecting training data from untrusted or unverified sources
without validation.
- Neglecting to monitor data distributions for unexpected shifts.
- Deploying updated models without thorough testing against
baseline performance.
- Failing to implement version control for both training data and
models.
- Not having a rollback strategy for compromised models.

**Benefits of establishing this best
practice:**

- Improved model reliability and accuracy through clean, trusted
data.
- Early detection of potential security breaches targeting
training data.
- Reduced risk of deploying compromised models to production.
- Ability to quickly recover from poisoning incidents through
rollback mechanisms.
- Enhanced overall ML system security and resilience.

**Risk level for not implementing this
practice:** High

## Implementation guidance

Data poisoning represents a security threat to machine learning
systems. When malicious actors manipulate training data, they can
compromise model integrity and cause downstream impacts on
decisions or predictions made by those models. You need to
implement comprehensive protections throughout your ML pipeline,
from data collection to model deployment and monitoring.

Start by establishing strict controls over data sources and
implementing validation procedures to detect anomalies before
training. During model development, implement monitoring for data
drift that could indicate poisoning attempts. Before deployment,
thoroughly compare new models against previous versions to
identify unexpected behavior changes. Finally, maintain versioned
copies of both training data and models to enable rapid recovery
from compromise.

By combining these defensive approaches, you create multiple
layers of protection that make your ML systems resilient against
data poisoning attempts.

### Implementation steps

- **Use only trusted data sources for
training data**. Verify the provenance of data used
for training and implement audit controls that allow you to
track changes to training data. This includes recording who
made changes, what changes were made, and when they
occurred. Before using data for training, validate its
quality to identify potential outliers and incorrectly
labeled samples that could indicate poisoning attempts.
- **Look for underlying shifts in the
patterns and distributions in training data**.
Implement continuous monitoring for data drift to detect
unexpected changes in data distributions. Use tools like
[Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) to track these changes
automatically. Deviations from established patterns can
serve as early warning signs of unauthorized access or
manipulation targeting training data.
- **Identify model updates that
negatively impact the results before moving them to
production**. Compare newly trained models against
previous versions using consistent test datasets. Look for
unexpected performance changes, especially degradations in
specific areas that weren't present in earlier model
iterations. Use
[Amazon SageMaker AI MLflow Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to track model
versions and their performance metrics.
- **Have a rollback plan**.
Implement versioning for both training data and models to
enable quick recovery from compromised states. Use
[Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) to maintain secure, versioned
features for your ML models. The Feature Store provides a
centralized repository for features with built-in security
controls. Configure Amazon SageMaker AI MLflow Model Registry
to support rollback capabilities so you can quickly revert
to a known good model version if issues are detected with a
newly deployed model.
- **Use low-entropy classification
cases**. Establish performance thresholds and
monitor for unexpected classification patterns. Define
boundaries for acceptable model behavior and create alerts
when outputs deviate from expected patterns. This can
identify subtle poisoning attempts that might otherwise go
undetected through conventional testing.
- **Implement end-to-end encryption for
ML data**. Secure your training data, feature sets,
and models using encryption both at rest and in transit. Use
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) to manage encryption keys
and apply them consistently across your ML pipeline.
Encryption protects against unauthorized access that could
lead to data poisoning.
- **Regularly scan for vulnerabilities
in ML dependencies**. Use tools like
[Amazon Inspector](https://aws.amazon.com/inspector/) to detect vulnerabilities in the software
packages and dependencies used in your ML environment. Data
poisoning can occur through compromised third-party
libraries, so regular scanning can identify potential entry
points for bad actors.
- **Implement input validation for AI
systems**. For AI models, validate inputs for
potential poisoning attempts. Implement filtering and
sanitization of inputs to block adversarial inputs that
could manipulate model behavior or extract sensitive
information.

## Resources

**Related documents:**

- [Bias
drift for models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Automated
monitoring of your machine learning models with Amazon SageMaker AI Model Monitor and sending predictions to human
review workflows using Amazon A2I](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/)
- [Amazon SageMaker AI Model Monitor– Fully Managed Automatic Monitoring
for Your Machine Learning Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/)
- [7
ways to improve security of your machine learning
workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/)
- [Building
secure machine learning environments with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/)

**Related videos:**

- [Detect
machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w)
- [Inawisdom:
Machine Learning and Automated Model Retraining with SageMaker AI](https://www.youtube.com/watch?v=1kbWvlHBYLk&t=7s)

**Related examples:**

- [Amazon SageMaker AI Model Monitor Examples](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops)
- [Amazon SageMaker AI Feature Store Examples](https://github.com/aws-samples/amazon-sagemaker-feature-store-examples)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec04-bp03.html*

---
