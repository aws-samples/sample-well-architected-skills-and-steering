# Security

**Pillar**: Security  
**Questions**: 6

---

# MLSEC01 — Business goal identification

**Pillar**: Security  
**Best Practices**: 1

---

# MLSEC01-BP01 Validate ML data permissions, privacy, software, and license terms

Machine learning implementations require careful consideration of
data permissions, privacy, and software licensing to adhere to
organizational and legal requirements. Validating these elements
throughout the ML lifecycle builds trusted ML systems that respect
data rights while delivering business value.

**Desired outcome:** Establish a
robust governance process that verifies that ML data usage and
software implementations meets your organization's requirements.
Maintain clear documentation of data permissions, approved software
packages, and license adherence. Operate ML implementations within a
framework that respects data subject rights, follows privacy
regulations, and avoids legal complications related to software
licensing.

**Common anti-patterns:**

- Assuming data collected for one purpose can automatically be
used for ML training without additional consent.
- Installing ML libraries and packages without reviewing their
license terms or data collection practices.
- Failing to document data permissions and consent mechanisms for
adherence verification.
- Ignoring the need for a process to handle withdrawn consent from
data subjects.
- Using third-party ML models without understanding their privacy
implications or license restrictions.

**Benefits of establishing this best
practice:**

- Reduces legal and regulatory risks related to data privacy and
software licensing.
- Enhances trust from data subjects and stakeholders through
ethical data handling.
- Avoids unexpected limitations on business plans due to
restrictive license terms.
- Improves documentation for audits and regulatory requirements.
- Streamlines deployment through pre-validated software and
container solutions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

ML libraries and packages handle various aspects of the machine
learning lifecycle, from data processing and model development to
training and hosting. Each component may come with specific
license terms, privacy considerations, and data handling
requirements. Validating these elements verifies your
organization's ML initiatives adhere to regulatory requirements
and don't introduce unexpected limitations.

When implementing ML systems, verify that data being used has
proper permissions for ML applications specifically. This often
means going beyond general data collection consent to verify
explicit permission for ML usage. For example, if you collected
customer data for service delivery, you may need additional
consent to use that data for training ML models.

Understanding license implications is critical for software
components. Some open-source ML libraries may have restrictions
that could affect your ability to commercialize models trained
with them. Similarly, third-party models or APIs might include
terms that grant the provider certain rights to your data or
restrict how you can deploy solutions.

Privacy considerations extend beyond initial data collection to
the entire ML lifecycle. Establish mechanisms to handle data
subject requests, including the right to withdraw consent or be
forgotten. Your ML implementation should respect these requests
without compromising the entire system.

### Implementation steps

- **Attain data permissions for
ML**. Verify whether your intended data can be used
for machine learning specifically. Document the legitimate
business purpose for using the data, and determine whether
you need additional consent from data owners or subjects.
Implement a process to handle data subjects who withdraw
their consent, including the ability to remove their data
from training sets or models when required. Maintain
comprehensive documentation of data permissions for
compliance-aligned purposes and potential audits.
- **Create a software license
inventory**. Develop and maintain an inventory of
ML libraries, packages, and dependencies used in your ML
pipeline. For each component, document the license type, key
terms, restrictions, and implications for your business
model. Use tools like
[AWS License Manager](https://aws.amazon.com/license-manager/) to track and manage software licenses
across your ML environments, improving adherence to
licensing agreements and optimizing license usage.
- **Bootstrap instances with lifecycle
management policies**. Create lifecycle
configurations with references to your approved package
repositories and scripts to install required packages. This
improves consistency across development environments and
avoids the introduction of unauthorized packages. Implement
[Amazon SageMaker AI Lifecycle Configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations.html) to automate the
setup of development environments with pre-approved software
packages and configurations.
- **Evaluate package integrations that
require external lookup services**. Based on your
data privacy requirements, opt out of data collection
features when necessary. Minimize data exposure by
establishing trusted relationships with service providers
and understanding their data handling practices. Evaluate
privacy policies and license terms for ML packages that
might collect telemetry or other data. For sensitive
implementations, consider creating private mirrors of
required packages to maintain control over external
connections.
- **Use prebuilt containers**.
Start with pre-packaged and verified containers to quickly
provide support for commonly used dependencies while
improving license adherence.
[AWS Deep Learning Containers](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html) contain several deep
learning framework libraries and tools including TensorFlow,
PyTorch, and Apache MXNet with pre-validated license terms.
These containers maintain consistency while reducing the
risk of introducing unauthorized or incompatible packages.
- **Establish a privacy-preserving ML
workflow**. Implement data minimization principles
by using only the data necessary for your ML tasks. Apply
anonymization or pseudonymization techniques to sensitive
data before using it for training. Consider using
privacy-preserving ML techniques such as differential
privacy or federated learning for highly sensitive
applications. Document your privacy-preserving measures for
compliance-aligned purposes and to build trust with
stakeholders.
- **Monitor for license and privacy
adherence**. Implement continuous monitoring of
your ML environments to detect potential license violations
or privacy issues. Create automated checks for package
versions and license changes during CI/CD processes.
Regularly audit data access patterns to verify that they
comply with documented permissions and privacy requirements.
Establish a process for addressing issues when they arise.
- **Consider synthetic data for training
and testing**. Create synthetic datasets that
preserve the statistical properties of real data while
avoiding privacy concerns.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides capabilities for generating
synthetic data for training and testing ML models when using
real data presents privacy or licensing challenges. Document
the use of synthetic data in your ML pipelines to
demonstrate privacy-preserving practices.

## Resources

**Related documents:**

- [Protecting
compute](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-compute.html)
- [What
is AWS Deep Learning Containers?](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html)
- [AWS License Manager](https://aws.amazon.com/license-manager/)
- [Lifecycle
configurations within Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lifecycle-configurations.html)
- [Data
Privacy in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/data-privacy.html)
- [Best
practices for endpoint security and health with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practice-endpoint-security.html)
- [Private
package installation in Amazon SageMaker AI running in
internet-free mode](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/)
- [Machine
Learning Best Practices in Financial Services](https://aws.amazon.com/blogs/machine-learning/machine-learning-best-practices-in-financial-services/)

**Related videos:**

- [Machine
Learning Best Practices in Financial Services](https://youtu.be/HlSEUvApDZE?t=578)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec01-bp01.html*

---

# MLSEC02 — ML problem framing

**Pillar**: Security  
**Best Practices**: 1

---

# MLSEC02-BP01 Design data encryption and obfuscation

Consider how to protect personal data. Use field level encryption or
obfuscation to protect personally identifiable data.

**Desired outcome:** You establish
robust protection for sensitive information by implementing data
encryption and obfuscation techniques in your machine learning
workflows. You identify and secure personally identifiable
information (PII) through field-level encryption and data masking,
which improves your adherence to privacy regulations while
maintaining data utility for ML models.

**Common anti-patterns:**

- Storing personally identifiable information in plain text
format.
- Using the same encryption keys across different environments.
- Implementing inconsistent data protection policies across ML
pipelines.
- Overlooking data protection requirements during the design
phase.
- Failing to audit data for attributes requiring special
treatment.

**Benefits of establishing this best
practice:**

- Enhanced protection of sensitive and personally identifiable
data.
- Improves adherence to data privacy regulations.
- Reduced risk of data breaches and unauthorized access.
- Improved trust from users and stakeholders.
- Ability to utilize sensitive data for ML training while
maintaining privacy.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When designing machine learning workflows, protect personal and
sensitive data throughout the entire data lifecycle. You should
evaluate your data early in the process to identify fields
containing PII or other sensitive information requiring
protection. Implementing field-level encryption or data
obfuscation techniques maintains data utility for machine learning
while safeguarding individual privacy.

AWS provides multiple services to identify, classify, and protect
sensitive data within your ML workflows. Services like
[AWS Glue](https://aws.amazon.com/glue/)
can automatically detect PII, while
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) and
[AWS CloudHSM](https://aws.amazon.com/cloudhsm/) support robust encryption strategies. You should
establish consistent policies for handling sensitive data across
your organization and regularly audit your data protection
measures to improve your adherence to privacy regulations.

### Implementation steps

- **Audit data for attributes requiring
special treatment**. Identify fields containing
data requiring special treatment, such as field-level
encryption, data masking, or obfuscation. Use automated
tools like
[AWS Glue](https://aws.amazon.com/glue/) to identify PII and sensitive data patterns
within your datasets.
- **Establish a data classification
framework**. Develop a systematic approach to
categorize data based on sensitivity levels. Define which
categories require encryption, masking, or other protection
techniques, and document these requirements in your
organization's security policies.
- **Implement field-level
encryption**. Apply encryption selectively to
sensitive fields rather than entire datasets. Use
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) to manage encryption keys
and integrate with services like
[Amazon S3](https://aws.amazon.com/s3/) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) for transparent encryption of selected
fields.
- **Apply data obfuscation
techniques**. Use methods such as tokenization,
data masking, or anonymization to protect sensitive
information while preserving data utility for machine
learning. Consider using services like
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) for data transformation and masking
operations.
- **Establish key rotation
policies**. Implement regular rotation of
encryption keys to minimize the impact of potential key
compromises. Configure
[AWS KMS](https://aws.amazon.com/kms/) to automate key rotation according to your
security policies and regulatory requirements.
- **Secure ML model
artifacts**. Verify that trained models and their
associated metadata do not inadvertently expose sensitive
information. Use
[Amazon SageMaker AI's](https://aws.amazon.com/sagemaker/) security features to encrypt model
artifacts and secure API endpoints that serve predictions.
- **Implement access
controls**. Restrict access to sensitive data and
encryption keys using
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) policies. Apply the
principle of least privilege to verify that only authorized
personnel can access protected information.
- **Monitor and audit access
patterns**. Implement continuous monitoring to
detect unauthorized access attempts or unusual patterns that
might indicate a security breach. Configure
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) and
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track and alert on suspicious
activities.
- **Implement differential privacy
techniques**. When working with AI models, consider
implementing differential privacy techniques to add
statistical noise to training data, protecting individual
privacy while maintaining overall data utility.
- **Establish mechanisms to stop model
memorization**. Implement safeguards to block AI
models from memorizing and potentially reproducing sensitive
information from training data, especially when using large
language models.

## Resources

**Related documents:**

- [Detect
and process sensitive data](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html)
- [Security
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [Data
protection in Amazon SageMaker AI Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/data-protection.html)
- [Data
Privacy in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/data-privacy.html)
- [Data
Encryption](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/data-encryption.html)
- [Introducing
PII Data Identification and Handling Using AWS Glue
DataBrew](https://aws.amazon.com/blogs/big-data/introducing-pii-data-identification-and-handling-using-aws-glue-databrew/)
- [7
ways to improve security of your machine learning
workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/)
- [Secure
deployment of Amazon SageMaker AI resources](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/)

**Related videos:**

- [Privacy-preserving
machine learning](https://www.youtube.com/watch?v=ZQkB9XRqdnc)
- [Data
Protection Best Practices in Machine Learning](https://www.youtube.com/watch?v=1iZYmtFFLnw)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec02-bp01.html*

---

# MLSEC03 — Data processing

**Pillar**: Security  
**Best Practices**: 5

---

# MLSEC03-BP01 Provide least privilege access

Protect resources across various phases of the ML lifecycle using
the principle of least privilege. These resources include: data,
algorithms, code, hyperparameters, trained model artifacts, and
infrastructure. Provide dedicated network environments with
dedicated resources and services to operate individual projects.

**Desired outcome:** You establish a
secure machine learning environment by implementing the principle of
least privilege for resources involved in your ML workflows. Your
organization controls access to sensitive data, models, and
infrastructure based on business roles, maintains clear separation
between development, test, and production environments, and uses
appropriate governance mechanisms to enforce security policies. This
approach minimizes your attack surface and protects valuable ML
assets.

**Common anti-patterns:**

- Granting excessive permissions to data scientists or developers
beyond what they need.
- Using a single AWS account for ML workloads without proper
separation.
- Not tagging sensitive data and resources for access control
purposes.
- Failing to isolate ML environments based on data sensitivity
requirements.
- Relying solely on manual access management without proper
governance structures.

**Benefits of establishing this best
practice:**

- Reduced risk of unauthorized access to sensitive data and ML
assets.
- Clear segregation of duties based on business roles.
- Improves adherence to regulatory requirements for data
protection.
- Simplified governance through standardized access patterns.
- Minimized potential impact of security breaches.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Protecting machine learning workflows requires a comprehensive
security approach that applies the principle of least privilege to
resources involved. By carefully controlling who has access to
data, code, and infrastructure, you can reduce the risk of
unauthorized access or data breaches.

When implementing least privilege for ML resources, consider the
different phases of the ML lifecycle and the types of access
needed by various roles. For example, data scientists might need
read access to training data but not production systems, while ML
engineers may need deployment permissions but limited access to
raw data.

Setting up a multi-account architecture with
[AWS Organizations](https://aws.amazon.com/organizations/) provides strong isolation between
environments with different security requirements. This allows you
to maintain separate development, testing, and production
environments with appropriate controls for each.

### Implementation steps

- **Define role-based access control for
ML teams**. Identify the distinct roles within your
ML workflow, such as data scientists, ML engineers, and
operations teams. Map these roles to specific access
patterns required for their daily tasks. Use
[Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html) to quickly create
persona-based IAM roles with preconfigured templates for
common ML roles including data scientists, MLOps engineers,
and business analysts. This reduces manual permissions
management and facilitates least privilege access by
default. Complement with
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) for custom role-based
policies. Implement regular access reviews to verify that
permissions remain appropriate as responsibilities change.
- **Implement account separation with
AWS Organizations**. Create a multi-account
architecture that segregates workloads between development,
test, and production environments. Use
[AWS Organizations](https://aws.amazon.com/organizations/) to centrally manage accounts and apply
consistent policies. Establish tagging strategies to
identify data sensitivity levels and resource ownership.
Apply these tags to relevant resources like S3 buckets
containing training data or SageMaker AI instances. Use
[Service
Catalog](https://aws.amazon.com/servicecatalog/) to create pre-provisioned environments that
align with security requirements.
- **Organize ML workloads by access
patterns**. Group ML workloads based on common
access requirements and security profiles. Create
organizational units (OUs) in AWS Organizations that reflect
these groupings. Delegate specific access permissions to
each group according to their needs. Apply service control
policies (SCPs) to enforce security guardrails at the
organizational unit level. Limit administrative access to
infrastructure to designated administrators only.
- **Isolate sensitive data
environments**. Create dedicated, isolated
environments for working with sensitive data. Implement
network controls such as security groups and network ACLs to
restrict data flow between environments. Use
[Amazon VPC](https://aws.amazon.com/vpc/) endpoints to provide private connectivity to AWS
services without traversing the public internet. Configure
[AWS PrivateLink](https://aws.amazon.com/privatelink/) for secure access to SageMaker AI endpoints
from within your VPC.
- **Implement automated security
controls**. Deploy
[AWS Config](https://aws.amazon.com/config/) rules to continuously monitor resource
configurations for adherence to security policies. Use
[Amazon GuardDuty](https://aws.amazon.com/guardduty/) for threat detection across your ML
infrastructure. Implement
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to log and monitor API calls related to ML
resources. Consider using
[Amazon Macie](https://aws.amazon.com/macie/) to automatically discover and protect sensitive
data stored in Amazon S3.
- **Use secure ML development
practices**. Implement code repositories with
appropriate access controls for ML code and models. Use
version control for artifacts including data, code, and
model parameters. Apply the principle of least privilege to
CI/CD pipelines that deploy ML models. Implement model
governance processes that include security reviews before
deployment to production.
- **Deploy ML guardrails with service
control policies**. Create SCPs that enforce
requirements across your ML environments. Define policies
that block storage of sensitive data in unencrypted formats.
Restrict network egress from environments containing
sensitive data. Limit which AWS Regions can be used for
specific types of ML workloads based on requirements.
- **Implement safeguards for AI
systems**. For AI workloads, implement additional
security controls to protect against input injection
attacks. Implement built-in guardrails for responsible AI
use. Apply input validation for user inputs to AI systems.
Implement output filtering to avoid inadvertent disclosure
of sensitive information. Consider using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) with governance features to enforce
compliance-aligned and responsible AI practices.

## Resources

**Related documents:**

- [Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [Build
a Secure Enterprise Machine Learning Platform on AWS](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.pdf)
- [Protecting
data at rest](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-data-at-rest.html)
- [Security
best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Building
secure Amazon SageMaker AI access URLs with Service
Catalog](https://aws.amazon.com/blogs/mt/building-secure-amazon-sagemaker-access-urls-with-aws-service-catalog/)
- [Setting
up secure, well-governed machine learning environments on
AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/)
- [ML
security: Using Amazon SageMaker AI with AWS PrivateLink](https://aws.amazon.com/blogs/machine-learning/connect-to-amazon-services-using-aws-privatelink-in-amazon-sagemaker/)

**Related videos:**

- [Architectural
best practices for machine learning applications](https://www.youtube.com/watch?v=fBytsYBVgbo)
- [Secure
and compliant machine learning for regulated industries](https://www.youtube.com/watch?v=8p-B3sTLmFg)
- [Amazon SageMaker AI Model Development in a Highly Regulated
Environment (SDD315)](https://youtu.be/cSYFqKRQ0j0?t=1051)

**Related examples:**

- [Build
your own Anomaly Detection ML Pipeline](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/build-your-own-anomaly-detection-ml-pipeline-ra.pdf?did=wp_card&trk=wp_card)
- [AWS MLOps Framework](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/aws-mlops-framework-sol.pdf?did=wp_card&trk=wp_card)
- [Secure
ML deployment architecture reference](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-ml-models-securely-on-aws.html)
- [Secure
Data Science Reference Architecture](https://github.com/aws-samples/secure-data-science-reference-architecture)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec03-bp01.html*

---

# MLSEC03-BP02 Secure data and modeling environment

Secure your machine learning data and development environments to
protect valuable information assets throughout the ML lifecycle. By
implementing proper security measures for storage, compute, and
network resources, you can maintain data integrity and
confidentiality while enabling data scientists to work effectively.

**Desired outcome:** You have a
secure foundation for storing, processing, and utilizing data for
machine learning workloads. Your data is encrypted at rest and in
transit, with access tightly controlled through identity management,
infrastructure isolation, and secure coding practices. Your
development environments are protected from unauthorized access
while providing the necessary tools for your ML practitioners.

**Common anti-patterns:**

- Storing unencrypted training data in publicly accessible
storage.
- Using default security configurations for ML environments.
- Allowing unrestricted internet access from ML environments.
- Using hard-coded credentials in ML code and notebooks.
- Installing ML packages from untrusted sources without
validation.
- Granting excessive permissions to development environments.

**Benefits of establishing this best
practice:**

- Protection of sensitive training data from unauthorized access
or exfiltration.
- Reduced risk of compromised ML models and systems.
- Improves adherence to regulatory requirements for data handling.
- Improved governance of ML development environments.
- Enhanced ability to detect and respond to security events.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Securing your ML environments requires a comprehensive approach
addressing data storage, compute resources, network isolation, and
access controls. The ML lifecycle involves multiple stages where
data could be exposed if proper security measures aren't
implemented. By establishing secure foundations for your ML
infrastructure, you can protect valuable intellectual property
while still enabling productivity.

Start by securing your data repositories with encryption and
access controls. Then build secure compute environments for model
development that maintain isolation through private networking.
Implement proper credential management to avoid exposure of
secrets. Finally, verify that your package management practices
block the introduction of malicious code into your ML pipeline.

Modern ML workloads often involve large datasets and complex
algorithms, making security even more critical as the impact of a
breach could be substantial. By implementing the measures in this
best practice, you create a secure foundation for your ML
initiatives.

### Implementation steps

- **Build a secure analysis
environment**. During the data preparation and
feature engineering phases, leverage secure data exploration
options on AWS. Use
[Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) managed environments or
[Amazon EMR](https://aws.amazon.com/emr/) for data processing. Alternatively, use managed
services like
[Amazon Athena](https://aws.amazon.com/athena/) and
[AWS Glue](https://aws.amazon.com/glue/) to explore data without moving it from your data
lake. For smaller datasets, use Amazon SageMaker AI Studio to
explore, visualize, and engineer features, then scale up
your feature engineering using managed ETL services like
Amazon EMR or AWS Glue.
- **Create dedicated IAM and KMS
resources**. Limit the scope and impact of
credentials and keys by creating dedicated
[AWS IAM](https://aws.amazon.com/iam/) roles and
[AWS KMS](https://aws.amazon.com/kms/) keys for ML workloads. Create private
[Amazon S3](https://aws.amazon.com/s3/) buckets with versioning enabled to protect your
data and intellectual property. Implement a centralized data
lake using
[AWS Lake Formation](https://aws.amazon.com/lake-formation/) on Amazon S3. Secure your data lake
using a combination of services to encrypt data in transit
and at rest. Monitor access with granular
[AWS IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html),
[S3
bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-bucket-policy.html),
[S3
Access Logs](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html),
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), and
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/).
- **Use Secrets Manager and Parameter
Store to protect credentials**. Replace hard-coded
secrets in your code with API calls to programmatically
retrieve and decrypt secrets using
[AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). Use
[AWS Systems Manager Parameter Store](https://aws.amazon.com/systems-manager/features/#Parameter_Store) to store application
configuration variables such as AMI IDs or license keys.
Grant permissions to your SageMaker AI IAM role to access these
services from your ML environments.
- **Automate managing
configuration**. Use lifecycle configuration
scripts to manage ML environments. These scripts run when
environments are created or restarted, allowing you to
install custom packages, preload datasets, and set up source
code repositories. Lifecycle configurations can be reused
across multiple environments and updated centrally. Use
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) infrastructure as code and
[Service Catalog](https://aws.amazon.com/servicecatalog/) to simplify configuration for end
users while maintaining security standards.
- **Create private, isolated, network
environments**. Use
[Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) to limit
connectivity to only essential services and users. Deploy
Amazon SageMaker AI resources in a VPC to enable network-level
controls and capture network activity in
[VPC
Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html). For distributed training workloads, use
[Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html) which provides managed, resilient
clusters with built-in VPC integration and multi-AZ
deployment for enhanced security and availability. This
deployment model also enables secure queries to data sources
within your VPC, such as
[Amazon RDS](https://aws.amazon.com/rds/) databases or
[Amazon Redshift](https://aws.amazon.com/redshift/) data warehouses. Use IAM to restrict access
to ML environment web UIs so they can only be accessed from
within your VPC. Implement
[AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.html) to privately connect your SageMaker AI
resources with supported AWS services, facilitating secure
communication within the AWS network. Use
[AWS KMS](https://aws.amazon.com/kms/) to encrypt data on the
[Amazon EBS](https://aws.amazon.com/ebs/) volumes attached to SageMaker AI resources.
- **Restrict access**. ML
development environments provide web-based access to the
underlying compute resources, typically with elevated
privileges. Restrict this access to remove the ability to
assume root permissions while still allowing users to
control their local environment. Implement least privilege
access controls for ML resources.
- **Secure ML algorithms**.
Amazon SageMaker AI uses container technology to train and host
algorithms and models. When creating custom containers,
publish them to a private container registry hosted on
[Amazon
Elastic Container Repository (Amazon ECR)](https://aws.amazon.com/ecr/). Encrypt
containers hosted on Amazon ECR at rest using AWS KMS.
Regularly scan containers for vulnerabilities and implement
a secure container update process.
- **Enforce code best
practices**. Use secure git repositories for
storing code. Implement code reviews, automated security
scanning, and version control for ML code. Integrate
security checks into your ML CI/CD pipeline to detect
potential security issues early in the development process.
- **Implement a package mirror for
consuming approved packages**. Evaluate license
terms to determine appropriate ML packages for your business
across the ML lifecycle phases. Common ML Python packages
include Pandas, PyTorch, Keras, NumPy, and Scikit-learn.
Build an automated validation mechanism to check packages
for security issues. Only download packages from approved
and private repos. Validate package contents before
importing. SageMaker AI supports
[modifying
package channel paths to a private repository](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/). When
appropriate, use an internal repository as a proxy for
public repositories to minimize network traffic and reduce
overhead.
- **Implement model security
monitoring**. Deploy continuous monitoring
solutions to detect unauthorized access attempts, unusual
data access patterns, and potential data exfiltration from
your ML environments. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/),
[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/), and
[Amazon GuardDuty](https://aws.amazon.com/guardduty/) to create a comprehensive security
monitoring solution for ML resources.
- **Implement additional security
controls for AI workloads**. For AI workloads,
implement additional security controls around input
validation and data leakage prevention. Implement
[Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) to detect drift in production
AI systems. Consider using
[Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) to document model security
characteristics and limitations.

## Resources

**Related documents:**

- [Prerequisites
for using SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites.html)
- [Storage
Best Practices for Data and Analytics Applications](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html)
- [Configure
security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security.html)
- [Protecting
compute](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-compute.html)
- [Protecting
data in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-data-in-transit.html)
- [7
ways to improve security of your machine learning
workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/)
- [Building
secure machine learning environments with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/)
- [Setting
up secure, well-governed machine learning environments on
AWS](https://aws.amazon.com/blogs/mt/setting-up-machine-learning-environments-aws/)
- [Private
package installation in Amazon SageMaker AI running internet-free
mode](https://aws.amazon.com/blogs/machine-learning/private-package-installation-in-amazon-sagemaker-running-in-internet-free-mode/)
- [Secure
Deployment of Amazon SageMaker AI resources](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/)
- [Apply
fine-grained data access controls with AWS Lake Formation and
Amazon EMR from Amazon SageMaker AI Studio](https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-data-access-controls-with-aws-lake-formation-and-amazon-emr-from-amazon-sagemaker-studio/)

**Related videos:**

- [Security
for AI/ML Models in AWS](https://www.youtube.com/watch?v=toDQL_c8Zug)
- [Security
best practices the AWS Well-Architected way](https://www.youtube.com/watch?v=wfIVI-M7lbQ)

**Related examples:**

- [Secure
Data Science Reference Architecture](https://github.com/aws-samples/secure-data-science-reference-architecture)
- [Amazon SageMaker AI Secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec03-bp02.html*

---

# MLSEC03-BP03 Protect sensitive data privacy

Protect sensitive data used in training against unintended
disclosure by implementing appropriate identification,
classification, and handling strategies. This practice improves data
privacy while maintaining model utility through techniques such as
data removal, masking, tokenization, and principal component
analysis (PCA).

**Desired outcome:** You establish
effective protocols to identify, classify, and protect sensitive
data throughout your machine learning workflows. Your sensitive data
is appropriately secured with encryption, access controls, and data
minimization techniques. Your organization maintains clear
documentation of governance practices for consistent application
across projects.

**Common anti-patterns:**

- Failing to identify sensitive data before using it for model
training.
- Using raw PII or other sensitive data when anonymized data would
suffice.
- Not implementing proper encryption for sensitive training data.
- Assuming cloud services automatically protect sensitive data
without proper configuration.
- Neglecting to document data handling processes for future
reference.

**Benefits of establishing this best
practice:**

- Reduced risk of data breaches and privacy violations.
- Improves adherence to data protection regulations.
- Increased trust from customers and stakeholders.
- Improved ability to use sensitive data for legitimate machine
learning purposes.
- Better governance through documented protocols.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Protecting sensitive data privacy in machine learning workflows
requires a systematic approach that begins with data
identification and classification. You need to understand what
data you have and its sensitivity levels before determining
appropriate protection mechanisms. Different types of sensitive
data may require different handling strategies—some might need
complete removal, while others can be effectively masked or
tokenized.

When working with sensitive data in ML workflows, you should adopt
a defense-in-depth approach. This means implementing multiple
layers of protection, including access controls, encryption, data
minimization techniques, and monitoring systems. For example, you
might use [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) to encrypt your training data,
implement role-based access controls, and use
[Amazon Macie](https://aws.amazon.com/macie/) to continuously monitor for sensitive data exposure.

Privacy-preserving machine learning techniques are increasingly
important as models become more sophisticated. Techniques like
differential privacy, federated learning, and secure multi-party
computation can allow you to train effective models while
minimizing exposure of sensitive data. These approaches maintain
privacy while still extracting valuable insights from your data.

### Implementation steps

- **Implement automated data discovery
and classification**. Use automated sensitive data
discovery in
[Amazon Macie](https://aws.amazon.com/macie/) to gain continuous, cost-efficient,
organization-wide visibility into where sensitive data
resides across your Amazon S3 environment. Macie
automatically inspects your S3 buckets for sensitive data
such as personally identifiable information (PII), financial
data, and AWS credentials, then builds and maintains an
interactive data map of sensitive data locations and
provides sensitivity scores for each bucket.
- **Apply resource tagging for sensitive
data tracking**. Tag resources and models that
contain or are derived from sensitive elements to quickly
differentiate between resources requiring protection and
those that do not. Use
[AWS resource tagging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html) to systematically identify and
manage resources containing sensitive data throughout their
lifecycle.
- **Implement comprehensive encryption
strategies**. Encrypt sensitive data using services
such as [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/), the
[AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/getting-started.html), or client-side encryption. Apply
encryption consistently across data at rest and in transit,
with appropriate key management practices.
- **Implement data minimization
techniques**. Evaluate and identify data for
anonymization or de-identification to reduce sensitivity.
Use techniques such as masking, tokenization, or principal
component analysis to reduce the risk associated with using
sensitive data for training. Consider using
[Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) with appropriate
transformation techniques to create privacy-preserving
feature representations.
- **Establish governance documentation
and processes**. Create comprehensive documentation
of your sensitive data handling practices, including
classification schemes, protection mechanisms, access
control policies, and incident response procedures.
Regularly review and update these documents to reflect
changes in regulations, technologies, and organizational
practices.
- **Implement differential privacy
techniques**. Apply differential privacy methods to
add controlled noise to your data or models to block the
extraction of individual data points while maintaining
overall statistical validity.
[AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) assist organizations with collaborating
on sensitive data while maintaining privacy and adherence to
regulations.
- **Perform regular privacy impact
assessments**. Conduct systematic evaluations of
how your ML workflows collect, use, and protect sensitive
data. Use the results to identify areas for improvement in
your privacy protection mechanisms and adhere to relevant
regulations.
- **Implement safeguards for large
language models**. When using large language
models, implement safeguards to block memorization and
exposure of sensitive training data. Use
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) with appropriate
privacy-preserving configurations and implement proper data
filtering and anonymization techniques during model training
and fine-tuning.

## Resources

**Related documents:**

- [Running
sensitive data discovery jobs in Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs.html)
- [Categorizing
your storage using tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html)
- [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Using
the AWS Encryption SDK with AWS KMS](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/getting-started.html)
- [7
ways to improve security of your machine learning
workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/)
- [Use
Macie to discover sensitive data as part of automated data
pipelines](https://aws.amazon.com/blogs/security/use-macie-to-discover-sensitive-data-as-part-of-automated-data-pipelines/)
- [Building
a Serverless Tokenization Solution to Mask Sensitive
Data](https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/)

**Related videos:**

- [Security
for AI/ML Models in AWS](https://www.youtube.com/watch?v=toDQL_c8Zug)
- [Security
best practices the AWS Well-Architected way](https://www.youtube.com/watch?v=wfIVI-M7lbQ)

**Related examples:**

- [Secure
Data Science Reference Architecture](https://github.com/aws-samples/secure-data-science-reference-architecture)
- [Amazon SageMaker AI Secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec03-bp03.html*

---

# MLSEC03-BP04 Enforce data lineage

Data lineage tracking allows you to monitor and track data origins
and transformations over time, enabling better visibility into your
machine learning workflows. By enforcing data lineage, you can trace
the root cause of data processing errors and and protect the
integrity of your ML models.

**Desired outcome:** You can trace a
data element back to its source, verify the transformations it
underwent, and verify data integrity throughout the ML lifecycle.
You have visibility into your entire ML workflow from data
preparation to model deployment, enabling you to reproduce
workflows, establish model governance standards, and demonstrate
audit adherence.

**Common anti-patterns:**

- Treating data lineage as an afterthought rather than a core
requirement.
- Failing to maintain records of data transformations during
preprocessing.
- Not implementing integrity checks for detecting data
manipulation or corruption.
- Neglecting to document code and infrastructure changes that
affect the ML pipeline.
- Relying on manual tracking methods that are prone to errors and
inconsistencies.

**Benefits of establishing this best
practice:**

- Improved troubleshooting through the ability to trace issues
back to their source.
- Improves adherence to regulatory requirements through
comprehensive audit trails.
- Greater confidence in model outputs by understanding the
provenance of training data.
- Faster iteration cycles by being able to reproduce workflows
efficiently.
- Better governance and risk management across ML operations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data lineage is a critical component of responsible ML operations.
By tracking the journey of your data from its source through
various transformations to model deployment, you create
accountability and transparency in your ML systems. Enforcing data
lineage involves implementing mechanisms to record metadata about
data origins, transformations, and access controls throughout the
ML lifecycle.

[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides built-in capabilities to track and
maintain data lineage through its MLflow tracking capabilities.
This system allows you to record the relationships between various
ML artifacts such as datasets, algorithms, hyperparameters, and
model artifacts. By utilizing these tracking capabilities, you can
establish a clear audit trail that assists with reproducibility,
governance, and troubleshooting.

Proper data lineage implementation also requires strict access
controls to block unauthorized data manipulation. Your tracking
system should record who accessed the data, what changes were
made, and when those changes occurred. Additionally, implement
integrity checks against your training data to detect unexpected
deviations caused by data corruption or malicious manipulation.

### Implementation steps

- **Set up Amazon SageMaker AI MLflow
Tracking**. Enable tracking capabilities in your
SageMaker AI environment to automatically capture metadata
about your ML workflows. Configure SageMaker AI to track
artifacts, associations, and context information using
[Amazon SageMaker AI MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html). MLflow in SageMaker AI allows you to
create, manage, analyze, and compare experiments, providing
comprehensive tracking of training runs, model versions, and
associated metadata.
- **Implement automated metadata
collection**. Configure your ML pipelines to
automatically record metadata at each stage of processing.
Use
[SageMaker AI
Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) jobs to track data transformations and
record preprocessing steps. Apply
[SageMaker AI
Pipeline](https://aws.amazon.com/sagemaker/pipelines/) steps to document the flow of data from one
stage to another, creating a complete record of the data
journey.
- **Establish data access
controls**. Implement strict access controls to
protect data integrity. Use
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) roles and policies to
restrict access to specific datasets and models. Configure
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to detect unauthorized access
or changes to your data.
- **Create integrity verification
mechanisms**. Implement data validation steps in
your pipeline to detect anomalies or unexpected changes. Use
checksums, statistical analysis, or machine learning-based
anomaly detection to identify potential data corruption.
Store integrity verification results as part of your lineage
tracking records.
- **Document code and infrastructure
changes**. Track changes to your code repositories
and infrastructure configurations that affect the ML
workflow. Use version control systems like Git integrated
with
[AWS CodeCommit](https://aws.amazon.com/codecommit/) to maintain a history of code changes, and
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) or
[AWS CDK](https://aws.amazon.com/cdk/) to version your infrastructure as code.
- **Implement end-to-end
traceability**. Verify that your lineage tracking
system can trace model predictions back to the original data
sources used for training. Use
[SageMaker AI
MLflow Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to catalog your models and
associate them with their training data lineage. This
enables you to understand exactly which data influenced
specific model behaviors.
- **Establish audit and
compliance-aligned reporting**. Create automated
reports that demonstrate data lineage for compliance-aligned
purposes. Use
[Quick](https://aws.amazon.com/quicksight/) to visualize data lineage graphs and
[Amazon Athena](https://aws.amazon.com/athena/) to query lineage metadata for audit reports.
Regularly review these reports to improve your adherence to
your governance requirements.
- **Implement foundation model
tracking**. For foundation model workflows, track
not only the data but also the foundation models used, their
versions, and fine-tuning parameters. Use
[Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) to document model
characteristics and
[Amazon SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html) to monitor model
performance. Implement comprehensive traceability features
to document model provenance and usage.
- **Track model input
variations**. Maintain a record of input variations
used with models, as these influence model outputs. Use
[Amazon SageMaker AI MLflow tracking server](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html) with enhanced MLflow
3.0 capabilities to track different input variations and
their effectiveness, treating inputs as critical components
of your data lineage system. The managed MLflow service
provides robust experiment management at scale for ML
projects with comprehensive tracking of training runs, model
versions, and associated metadata.

## Resources

**Related documents:**

- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [SageMaker AI
MLflow Tracking Server](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html)
- [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/)
- [Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)
- [Accelerating
generative AI development with fully managed MLflow 3.0 on
Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/)
- [Building,
automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)

**Related videos:**

- [How
To Efficiently Manage ML experiments using Amazon SageMaker AI ML
Flow](https://www.youtube.com/watch?v=3xkz_5HOP6k)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec03-bp04.html*

---

# MLSEC03-BP05 Keep only relevant data

Reduce data exposure risks by preserving only use-case relevant data
across computing environments. Implementing data lifecycle
management and privacy-preserving techniques maintains data security
while enabling effective machine learning workflows.

**Desired outcome:** You maintain a
streamlined dataset across development, staging, and production
environments that contains only the data elements needed for your
machine learning use cases. You have implemented automated data
lifecycle management processes that properly identify data, redact
it when necessary, and remove it when no longer needed. This
approach reduces your security risk exposure while maintaining data
usability for ML operations.

**Common anti-patterns:**

- Keeping collected data indefinitely in case it might be useful
later.
- Failing to implement data redaction for personally identifiable
information (PII) in ML datasets.
- Using production data with sensitive information in development
environments.
- Not establishing clear timelines for data retention and removal.
- Ignoring privacy regulations when designing ML workflows.

**Benefits of establishing this best
practice:**

- Reduced risk of data breaches and privacy violations.
- Lower storage and computational costs from processing only
necessary data.
- Improved adherence to data privacy regulations.
- Enhanced ML model performance through focus on relevant
features.
- Streamlined data management processes across environments.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Managing data exposure is crucial for machine learning security.
The more data you collect and store, the greater your attack
surface and potential for data breaches. By focusing on data
minimization principles, you can reduce these risks while still
achieving your ML objectives.

Your data lifecycle management strategy should begin with a
thorough assessment of what data is truly needed for your ML use
cases. This requires close collaboration between data scientists,
security professionals, and business stakeholders to identify
essential features and acceptable levels of data granularity. Once
identified, implement mechanisms to maintain only the necessary
data elements across environments.

When working with potentially sensitive information, apply
privacy-preserving techniques like anonymization,
pseudonymization, or redaction of PII. AWS services like
[Amazon Comprehend](https://aws.amazon.com/comprehend/) and
[Amazon Macie](https://aws.amazon.com/macie/) can identify sensitive data automatically, while
[Amazon Transcribe](https://aws.amazon.com/transcribe/) offers automatic redaction capabilities. For
more advanced scenarios, consider techniques like differential
privacy or federated learning that allow you to derive insights
from sensitive data without exposing the raw information.

Regular data audits and automated cleanup processes are essential
components of an effective data lifecycle management strategy. By
implementing automated policies for data retention and deletion,
you can verify that data doesn't linger unnecessarily in your
systems after its useful life has ended.

### Implementation steps

- **Assess data requirements**.
Begin by thoroughly analyzing your ML use case to determine
exactly which data elements are required for model training,
validation, and inference. Document the minimum data
requirements for each stage of your ML pipeline and justify
the need for each attribute. Consider using techniques like
feature importance analysis to identify which data elements
contribute most to model performance.
- **Develop a comprehensive data
lifecycle plan**. Create a documented plan that
defines how data will flow through your ML pipeline,
including data collection, processing, storage, usage, and
eventual deletion. Identify usage patterns and requirements
for debugging and operational tasks. Specify retention
periods based on business needs, regulatory requirements,
and the purpose of the data.
- **Implement data minimization
techniques**. Design your data collection and
preprocessing pipelines to capture only the necessary data
attributes identified in your assessment. Use
[AWS Glue](https://aws.amazon.com/glue/) or similar ETL services to filter out
unnecessary fields before storage. Consider implementing
record-level filtering in addition to column-level
filtering.
- **Set up automated PII detection and
redaction**. Deploy solutions to automatically
identify and redact sensitive information. Use
[Amazon Comprehend](https://aws.amazon.com/comprehend/) for detecting PII in text data and
[Amazon Rekognition](https://aws.amazon.com/rekognition/) for identifying sensitive elements in
images. Implement
[Amazon Transcribe's automatic redaction feature](https://aws.amazon.com/blogs/aws/now-available-in-amazon-transcribe-automatic-redaction-of-personally-identifiable-information/) for audio
transcriptions.
- **Establish data governance
controls**. Implement access controls and
encryption mechanisms using
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) and
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/). Use
[Amazon Macie](https://aws.amazon.com/macie/) to automatically discover, classify, and
protect sensitive data in AWS. Apply data classification
tags to facilitate appropriate handling of different data
types.
- **Configure automated data lifecycle
policies**. Set up
[S3
Lifecycle configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to automatically transition
or expire data based on your retention policies. Implement
similar mechanisms for other storage systems used in your ML
pipeline. Create automated jobs to periodically review and
remove stale data from environments.
- **Implement privacy-preserving ML
techniques**. Where possible, use privacy-enhancing
technologies like differential privacy, federated learning,
or encrypted computation. Consider using
[AWS Lake Formation](https://aws.amazon.com/lake-formation/) to centrally define and enforce
fine-grained access controls. For sensitive use cases,
explore options for machine learning on encrypted data.
- **Monitor and audit data
usage**. Set up logging and monitoring using
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) and
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track data access patterns.
Periodically audit data usage against documented
requirements to identify and avoid unnecessary data
collection. Use
[Amazon Athena with user-defined functions](https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/) for analyzing and
redacting sensitive information in logs and audit trails.
- **Implement responsible data practices
for AI models**. When using AI models, be
especially careful with training data to block memorization
of sensitive information. Utilize
[Amazon SageMaker AI's feature store](https://aws.amazon.com/sagemaker/feature-store/) for centralized feature
management with built-in security controls. Consider data
poisoning risks and implement appropriate data validation
before model training.

## Resources

**Related documents:**

- [Reference
Guide: Extract More Value from your Data](https://pages.awscloud.com/data-lifecycle-reference-guide.html?sc_channel=bl&sc_campaign=datalifecycleandanalyticsintheawscloud&sc_geo=mult&sc_country=global&sc_outcome=multi)
- [Data
Privacy Center](https://aws.amazon.com/compliance/data-privacy/)
- [Building
a data analytics practice across the data lifecycle](https://aws.amazon.com/blogs/publicsector/building-a-data-analytics-practice-across-the-data-lifecycle/)
- [Detecting
and redacting PII using Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/detecting-and-redacting-pii-using-amazon-comprehend/)
- [Now
available in Amazon Transcribe: Automatic Redaction of
Personally Identifiable Information](https://aws.amazon.com/blogs/aws/now-available-in-amazon-transcribe-automatic-redaction-of-personally-identifiable-information/)
- [Redacting
sensitive information with user-defined functions in Amazon Athena](https://aws.amazon.com/blogs/big-data/redacting-sensitive-information-with-user-defined-functions-in-amazon-athena/)

**Related videos:**

- [Privacy-preserving
machine learning](https://www.youtube.com/watch?v=ZQkB9XRqdnc)
- [Best
practices for Amazon S3](https://youtu.be/HT3QiuzgjZg?t=524)

**Related examples:**

- [Field
Notes: Redacting Personal Data from Connected Cars Using
Amazon Rekognition](https://aws.amazon.com/blogs/architecture/field-notes-redacting-personal-data-from-connected-cars-using-amazon-rekognition/)
- [How
to Create a Modern CPG Data Architecture with Data Mesh](https://aws.amazon.com/blogs/industries/how-to-create-a-modern-cpg-data-architecture-with-data-mesh/)
- [Building
a secure enterprise machine learning platform on AWS](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec03-bp05.html*

---

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

# MLSEC05 — Deployment

**Pillar**: Security  
**Best Practices**: 1

---

# MLSEC05-BP01 Protect against adversarial and malicious activities

Machine learning systems must be robust against adversarial inputs
designed to manipulate their behavior. Implementing protection
mechanisms both inside and outside of your deployed models can
detect malicious inputs that could lead to incorrect predictions,
allowing you to automatically identify unauthorized changes, repair
compromised inputs, and validate data before it's used for further
training.

**Desired outcome:** You can detect,
mitigate, and protect your ML models from adversarial exploits that
attempt to manipulate inputs, preserving model integrity and
providing reliable predictions. Your ML systems incorporate robust
validation processes, ensemble approaches, and monitoring
capabilities that maintain consistent performance even when faced
with deliberately perturbed or malicious inputs.

**Common anti-patterns:**

- Implementing ML models without considering potential adversarial
threats.
- Focusing solely on model performance metrics without evaluating
robustness.
- Using single model architectures that are vulnerable to targeted
threats.
- Retraining models with unvalidated inputs that may contain
adversarial examples.
- Exposing ML models through unsecured endpoints without
monitoring capabilities.

**Benefits of establishing this best
practice:**

- Improved model robustness against input manipulation attempts.
- Enhanced detection of potential security threats targeting ML
systems.
- Greater reliability in model predictions even under adversarial
conditions.
- Protection against data poisoning during model retraining.
- Reduced vulnerability to model extraction and inference threats.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Adversarial threats against machine learning models involve
deliberately crafting inputs to cause incorrect predictions or
undesirable behaviors. These threats can range from subtle
perturbations that are imperceptible to humans but cause model
errors, to more sophisticated techniques that exploit model
vulnerabilities. Building protection against adversarial
activities requires a multi-layered approach combining robust
model design, comprehensive monitoring, and secure deployment
strategies.

When implementing defenses, you need to understand the specific
vulnerabilities in your models and the potential impact of
adversarial threats on your business outcomes. This requires
conducting thorough evaluations of model behavior under different
threats scenarios and implementing appropriate countermeasures
based on your risk profile. Both pre-deployment testing and
continuous monitoring during production are essential components
of a comprehensive protection strategy.

Adversarial robustness should be considered from the beginning of
your ML development process rather than as an afterthought. By
incorporating adversarial training, ensemble methods, and input
validation techniques during model development, you can create
systems that are inherently more resistant to threats.
Additionally, implementing proper access controls, monitoring
systems, and incident response procedures can establish a secure
operational environment for your ML models.

### Implementation steps

- **Evaluate the robustness of your
algorithm**. Conduct sensitivity analysis to
understand how your model responds to perturbed inputs. Test
your model with increasingly modified data points to
identify decision boundaries that might be vulnerable to
manipulation. Use adversarial testing frameworks to simulate
potential threats and measure their impact on model
performance. Document the types of perturbations that cause
incorrect predictions to inform your defense strategy.
- **Build for robustness from the
start**. Select diverse features during model
design to improve resilience against outliers and
adversarial examples. Implement ensemble methods by
combining multiple models with different architectures or
training approaches to increase decision diversity. Consider
techniques like adversarial training where you intentionally
incorporate adversarial examples into your training data to
make your models more resistant to threats.
- **Identify repeats and suspicious
patterns**. Deploy
[Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) to continuously analyze
inference data and detect unusual patterns such as repeated
similar inputs that may indicate probing threats. Set up
alerts for anomalous input distributions that differ from
training data. Monitor for evidence of model brute-forcing,
where bad actors systematically vary limited sets of input
features to determine decision boundaries and derive feature
importance.
- **Implement experiment and model
tracking**. Maintain comprehensive records of data
provenance and model versions to trace model skew back to
potentially compromised data sources. Before retraining
models with new data, implement validation processes to
identify and remove adversarial examples. Use
[Amazon SageMaker AI MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to document relationships between
datasets, algorithms, and model artifacts throughout the ML
lifecycle.
- **Use secure inference API
endpoints**. Host models behind properly secured
API endpoints that implement authentication, authorization,
and input validation. Configure
[Amazon SageMaker AI endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-manage.html) with appropriate security
controls including VPC isolation,
[AWS IAM](https://aws.amazon.com/iam/) roles with least privilege, and encryption for
data in transit and at rest. Implement rate limiting and
request validation to block abuse of model APIs. Monitor API
usage patterns to detect potential exploitation attempts.
- **Implement continuous model
monitoring**. Set up
[Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) to track data and concept
drift that may indicate adversarial manipulation. Configure
automatic alerts when inference data patterns deviate from
training baselines. Periodically reevaluate model robustness
as new threat techniques emerge in the security landscape.
- **Establish incident response
procedures**. Develop clear protocols for
responding to detected adversarial threats against your ML
systems. Define procedures for model rollback, data
quarantine, and forensic analysis when suspicious activities
are identified. Document lessons learned from security
incidents to continuously improve protection strategies.
- **Apply input validation
guardrails**. For AI models, implement robust input
validation and filtering mechanisms to block injection
exploits. Implement custom guardrails to protect against
harmful inputs that may manipulate model behavior. Monitor
input patterns and responses to detect attempts to bypass
security controls.

## Resources

**Related documents:**

- [Deep
ensembles](https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-quantifying-uncertainty/deep-ensembles.html)
- [Empirical
demonstration of deterministic overconfidence](https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-quantifying-uncertainty/app-b.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Security
and compliance](https://docs.aws.amazon.com/whitepapers/latest/ml-best-practices-public-sector-organizations/security-and-compliance.html)
- [7
ways to improve security of your machine learning
workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/)
- [Run
ensemble ML models on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/part-7-model-hosting-patterns-in-amazon-sagemaker-run-ensemble-ml-models-on-amazon-sagemaker/)
- [Securing
Amazon SageMaker AI Studio connectivity using a private
VPC](https://aws.amazon.com/blogs/machine-learning/securing-amazon-sagemaker-studio-connectivity-using-a-private-vpc/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec05-bp01.html*

---

# MLSEC06 — Monitoring

**Pillar**: Security  
**Best Practices**: 2

---

# MLSEC06-BP01 Restrict access to intended legitimate consumers

Use least privilege permissions to invoke the deployed model
endpoint. For consumers who are external to the workload
environment, provide access using a secure API.

**Desired outcome:** You establish
secure inference API endpoints that allow only authorized parties to
access your ML models. You create a controlled environment where
model access is restricted based on legitimate business needs, while
maintaining monitoring capabilities to track interactions with your
models. Your ML endpoints are protected using the same security
principles applied to other HTTPS APIs, providing data protection in
transit and proper authentication.

**Common anti-patterns:**

- Allowing public access to model endpoints without proper
authentication.
- Using overly permissive IAM roles for model endpoint access.
- Failing to implement network controls for inference endpoints.
- Not monitoring or logging model inference activities.
- Using the same credentials for development and production model
access.

**Benefits of establishing this best
practice:**

- Reduced risk of unauthorized model access and potential data
exfiltration.
- Enhanced control over who can use your ML models and when.
- Improved monitoring and auditability of model usage.
- Protection of intellectual property embedded in models.
- Improves adherence to regulatory requirements for data security.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Securing your ML model endpoints is critical to protect both your
intellectual property and the data processed by these models. By
treating ML inference endpoints with the same security rigor as
other HTTPS APIs, you can maintain a strong security posture while
enabling legitimate business use. You need to implement proper
authentication, network controls, and monitoring to verify that
only authorized parties can access your models.

When deploying machine learning models in production, you should
consider the model as a valuable asset that requires protection.
This means implementing layers of security controls including
network isolation through VPC configuration, strong authentication
mechanisms, and continuous monitoring of inference activities. For
external consumers, create a dedicated API layer that enforces
security policies and controls access.

### Implementation steps

- **Plan your access control
strategy**. Define which users or applications need
access to your model endpoints and what specific permissions
they require. Follow the principle of least privilege,
granting only the minimum permissions necessary for each
consumer to perform their required tasks.
- **Set up secure inference API
endpoints**. Host your ML models so that consumers
can perform inference against them securely. Use
[Amazon SageMaker AI endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-manage.html) with proper authentication and
authorization controls. Use
[Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to automatically
benchmark and optimize your model deployments for the best
security-performance balance, and select optimal compute
instances and configurations while maintaining security
controls. This approach defines the relationship between the
model and its consumers, restricts access to the base model,
and provides monitoring capabilities for model interactions.
- **Implement network security
controls**. Configure your SageMaker AI inference
endpoints within a VPC to isolate network traffic. Use
security groups to define inbound and outbound traffic
rules, and consider using
[AWS PrivateLink](https://aws.amazon.com/privatelink/) for private connectivity to your
endpoints. Follow guidance from the
[AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) to implement proper
network controls, such as restricting access to specific IP
ranges and implementing bot protection.
- **Configure authentication and
authorization**. Sign HTTPS requests for API calls
so that requester identity can be verified. Use
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) to control who has access
to your SageMaker AI resources and what actions they can
perform. Consider using
[Amazon Cognito](https://aws.amazon.com/cognito/) for managing user identities if your API is
accessed by external users.
- **Deploy endpoints in a secure VPC
configuration**. Use
[VPC
endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) to privately connect your VPC to supported
AWS services without requiring an internet gateway. Follow
the guidance in
[Give
SageMaker AI Hosted Endpoints Access to Resources in Your
Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html) to configure your endpoint for VPC access.
- **Implement encryption for data in
transit and at rest**. Configure your endpoints to
use HTTPS for API calls. Encrypt model artifacts and data at
rest using
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/). Use client-side encryption
for sensitive data when appropriate.
- **Set up monitoring and
logging**. Configure
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor your endpoints and
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to log API calls. Implement
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to detect drift and data quality issues
in your production models.
- **Use model registry for
governance**. Implement
[SageMaker AI
MLflow Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to catalog and manage versions
of your models, control which model versions are deployed,
and maintain an audit trail of model approvals and
deployments.
- **Implement proper API design
patterns**. Design your inference API following
REST best practices. Include proper input validation, error
handling, and rate limiting to protect against abuse.
Consider implementing an
[API Gateway](https://aws.amazon.com/api-gateway/) in front of your SageMaker AI endpoint for
additional controls.
- **Conduct regular security
reviews**. Periodically review the security
configuration of your endpoints, check for over-permissive
policies, and validate that access logs show only expected
patterns of usage.
- **Implement guardrails for AI
models**. For AI endpoints, implement content
filtering and validation controls to provide responsible
outputs, stop harmful content generation, and maintain
appropriate use of the models.

## Resources

**Related documents:**

- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Real-time
Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)
- [Give
SageMaker AI Hosted Endpoints Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Integrating
machine learning models into your Java-based
microservices](https://aws.amazon.com/blogs/awsmarketplace/integrating-machine-learning-models-into-your-java-based-microservices/)
- [How
Financial Institutions can use AWS to Address Regulatory
Reporting](https://aws.amazon.com/blogs/architecture/how-banks-can-use-aws-to-meet-compliance/)
- [Secure
deployment of Amazon SageMaker AI resources](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/)
- [Accelerating
Machine Learning Development with Data Science as a Service
from Change Healthcare](https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/)

**Related videos:**

- [End-to-End
machine learning using Spark and Amazon SageMaker AI](https://www.youtube.com/watch?v=FKgivdwzO5g)

**Related examples:**

- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec06-bp01.html*

---

# MLSEC06-BP02 Monitor human interactions with data for anomalous activity

Implement comprehensive monitoring of data access events to detect
unauthorized or suspicious activities. By auditing user interactions
with data, you can identify potential security threats such as
unusual access patterns, abnormal locations, or activity that
exceeds normal baselines. Use specialized AWS services for anomaly
detection alongside data classification to assess risks and protect
your machine learning assets.

**Desired outcome:** You have
comprehensive visibility into human interactions with your data,
with logging enabled for create, read, update, and delete
operations. You can identify who accessed specific data elements,
what actions they took, and when those actions occurred. Your
monitoring system automatically flags anomalous activities based on
established baselines and alerts you to potential security threats.
Data classification is integrated with your monitoring approach to
prioritize security events based on data sensitivity.

**Common anti-patterns:**

- Implementing logging without monitoring or analysis
capabilities.
- Focusing only on system-level access without tracking specific
data interactions.
- Failing to establish user activity baselines for anomaly
detection.
- Not classifying data to differentiate between access to
sensitive and non-sensitive information.
- Monitoring access events without automated alerting mechanisms.

**Benefits of establishing this best
practice:**

- Early detection of potential data breaches or insider threats.
- Improved ability to investigate security incidents with
comprehensive audit trails.
- Improves adherence to data protection regulations and
requirements.
- Better visibility into how data is being used across your ML
systems.
- Reduced risk of unauthorized data access or exfiltration.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Protecting your machine learning data requires visibility into who
is accessing it and how it's being used. By monitoring human
interactions with your data, you can identify potential security
threats before they lead to data breaches or misuse. This involves
implementing comprehensive logging for data access events,
classifying your data based on sensitivity, and using automated
tools to detect anomalous behavior.

Start by enabling logging for data interactions, particularly
focusing on human access rather than just system-to-system
communications. Your logs should capture details about who
accessed the data, what specific elements they accessed, what
actions they took, and when those interactions occurred. This
creates an audit trail that serves as the foundation for your
monitoring strategy.

Next, classify your data based on sensitivity and importance. By
knowing which datasets contain personally identifiable information
(PII), intellectual property, or other sensitive information, you
can prioritize monitoring efforts and apply appropriate security
controls. This classification details the potential impact of
unauthorized access to different datasets.

Finally, implement anomaly detection to identify unusual patterns
that might indicate security threats. These anomalies could
include access from unusual locations, outside normal working
hours, excessive access volume, or access to data that's not
typically needed for an employee's role. When anomalies are
detected, your system should generate alerts to prompt
investigation.

### Implementation steps

- **Enable data access
logging**. Verify that you have data access logging
for human CRUD (create, read, update, and delete)
operations, including the details of who accessed what
elements, what action they took, and at what time. Leverage
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to capture API calls and user activities
across your AWS environment. Configure CloudTrail to log
data events for
[Amazon S3](https://aws.amazon.com/s3/) buckets containing your training and inference
data. For SageMaker AI environments, use
[Amazon SageMaker AI Logging and Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html) capabilities to
track access to ML models and datasets.
- **Classify your data**. Use
[Amazon Macie](https://aws.amazon.com/macie/) for protecting and classifying training and
inference data in
[Amazon S3](https://aws.amazon.com/s3/). Amazon Macie is a fully managed security service
that uses ML to automatically discover, classify, and
protect sensitive data in AWS. The service recognizes
sensitive data, such as personally identifiable information
(PII) or intellectual property. Configure Macie to perform
regular automated scans of your S3 buckets to identify and
tag sensitive data. Create custom data identifiers in Macie
to recognize organization-specific sensitive data patterns
beyond the standard patterns Macie detects.
- **Monitor and protect**. Use
[Amazon GuardDuty](https://aws.amazon.com/guardduty/) to monitor for malicious and unauthorized
activities. This will enable protecting AWS accounts,
workloads, and data stored in
[Amazon S3](https://aws.amazon.com/s3/). Configure GuardDuty to analyze CloudTrail logs,
VPC flow logs, and DNS logs to detect suspicious activities.
Pay special attention to the
[GuardDuty
S3 Finding Types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html) which can detect anomalous access
patterns to your S3-stored data.
- **Set up anomaly detection**.
Implement automated anomaly detection for data access
patterns using
[Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html). Create CloudWatch
metrics for access frequency, data volume transferred,
access times, and other relevant metrics. Configure
CloudWatch alarms to alert when anomalies are detected based
on these metrics.
- **Establish data access
baselines**. Create baseline profiles of normal
user access patterns using
[AWS CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor access trends over time. Set up
dashboards that visualize normal patterns of data access by
team, role, or time period. Use these baselines to fine-tune
anomaly detection thresholds and reduce false positives.
- **Implement alerting
mechanisms**. Configure
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) to trigger automated responses when
suspicious access events are detected. Route alerts to your
security team through notification channels like
[Amazon SNS](https://aws.amazon.com/sns/) for immediate response. Create different alerting
thresholds based on data classification and sensitivity.
- **Centralize logging and
monitoring**. Use
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) (formerly Amazon OpenSearch Service) to create a centralized repository for log analysis
and visualization. Build comprehensive dashboards to monitor
data access patterns across your organization. Implement log
retention policies that comply with your regulatory
requirements.
- **Control and audit data exploration
activities**. Implement
[AWS Lake Formation](https://aws.amazon.com/lake-formation/) with
[Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) to provide fine-grained access
controls for data exploration. Configure Lake Formation
permissions to restrict data access based on user roles and
data classification. Use
[AWS IAM](https://aws.amazon.com/iam/) to enforce least-privilege access to sensitive
data.
- **Monitor access to AI training
data**. Implement specialized monitoring for
datasets used to train AI models, as these may contain
particularly sensitive information or be subject to greater
privacy concerns. Use
[Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) to detect drift in model
behavior that might indicate data access issues. Implement
enterprise-ready security and privacy controls for
foundation models.

## Resources

**Related documents:**

- [CloudWatch Logs for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html)
- [GuardDuty
S3 Protection finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/)
- [Configure
security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security.html)
- [Building
a Self-Service, Secure, & Continually Compliant
Environment on AWS](https://aws.amazon.com/blogs/architecture/building-a-self-service-secure-continually-compliant-environment-on-aws/)
- [How
to Use New Advanced Security Features for Amazon Cognito user pools](https://aws.amazon.com/blogs/security/how-to-use-new-advanced-security-features-for-amazon-cognito-user-pools/)
- [Best
practices for setting up Amazon Macie with AWS Organizations](https://aws.amazon.com/blogs/security/best-practices-for-setting-up-amazon-macie-with-aws-organizations/)

**Related videos:**

- [Protect
Your Data in S3 with Amazon Macie and Amazon GuardDuty - AWS
Online Tech Talks](https://www.youtube.com/watch?v=lvPT71jAIXk)
- [Protecting
sensitive data with Amazon Macie and Amazon GuardDuty](https://www.youtube.com/watch?v=h7pq95RMuEQ)

**Related examples:**

- [AWS Security Hub CSPM automated response and remediation](https://github.com/aws-solutions/aws-security-hub-automated-response-and-remediation)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec06-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
