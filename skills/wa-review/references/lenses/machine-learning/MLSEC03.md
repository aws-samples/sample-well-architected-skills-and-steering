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
