# Security

**Pages**: 8

---

# Design principles

The security pillar of the AWS Well-Architected Framework sets
out principles that can help strengthen the security of your
workload:

- **Implement a strong identity
foundation:** Implementing the principle of least
privilege is foundational to the security and compliance of
healthcare workloads. Centralize identity management, and
aim to avoid reliance on long-term static credentials.
- **Enable traceability:**
Monitor, alert, and audit actions and changes to your
environment in real time. Integrate log and metric
collection with systems to investigate and remediate issues
automatically.
- **Apply security at all
layers:** Apply a defense in depth approach with
multiple security controls.  Security should apply to all
layers, from the edge of the network to the application and
code.
- **Automate security best
practices:** Automated software-based security
mechanisms improve your ability to scale more securely,
rapidly, and cost-effectively.
- **Encrypt data in transit and at
rest:** Classify your data to identify health data
and other sensitive data.  Use encryption, tokenization, and
de-identification to decrease the sensitivity of data, and
implement access controls.
- **Keep people away from
data:**  Use mechanisms and tools to reduce the
need for direct access or manual processing of health data,
consistent with the principle of least privilege.
- **Prepare for security
events:** Prepare for an incident by having
incident management and investigation policy and processes
that align to your organizational requirements and
applicable regulatory frameworks.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/design-principles-1.html*

---

# Identity and access management

HCL_SEC1. How do you identify where
health data is in your environment?

**Determine applicable
regulatory frameworks and controls as it pertains to data
classification**

It is critical that organizations understand what types of
data are being hosted and processed, and where that data
resides. This understanding is a basis for ensuring that the
right controls are in place for aligning with relevant
regulatory frameworks and standards. Data classification also
aids in traceability and access monitoring of sensitive data.

You can start by creating policies and procedures that align
to the relevant regulatory frameworks. The policies and
procedures should outline a data classification strategy that
fits your business and regulatory requirements.

**Create and document a
data classification strategy**

Based on the business requirements, and any applicable
regulatory frameworks, implement a data classification policy.
This policy should extend beyond simply marking health data,
but should include other sensitive or confidential data, as
well as public data. The [Data
Classification: Secure Cloud Adoption](https://docs.aws.amazon.com/whitepapers/latest/data-classification/welcome.html) whitepaper
provides examples of how to categorize data, and how to
implement a data classification strategy that implements the
appropriate controls based on the data category.  Make sure
that health data is classified in accordance with the proper
regulatory frameworks that your business aligns to.

**Select the appropriate
cloud deployment model according to your specific needs, the
type of data you handle, and the assessed risk**

As outlined in the
[Data
Classification: Secure Cloud Adoption](https://docs.aws.amazon.com/whitepapers/latest/data-classification/welcome.html) whitepaper,
select the appropriate cloud deployment model according to
your specific needs, the type of data you handle, and the
assessed risk. Depending on the classification of the data,
apply the relevant security controls (such as encryption) within
your cloud environment. AWS also recommends that health data
be classified and labeled as such, simplifying audits and
ensuring that the proper technical controls can be
implemented.

If your environment uses multiple AWS accounts, designate
specific accounts to host and process health data to simplify
managing where health data is located. For example, if your
account structure mirrors your software development lifecycle
with accounts designated for development, testing, staging,
and production, the production and staging accounts may be
designated as “health data” accounts and are therefore
documented as containing health data. Then, implement
procedures and controls in the development and testing
accounts to prevent health data from being stored there.

You can also assign
[tags](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
to your AWS resources, which consist of a user-defined key and
value. Tags help you manage, identify, organize, search for,
and filter resources. Create tags to categorize resources by
purpose, owner, environment, or other criteria. Use tags to
help identify and document resources and objects that contain
sensitive health data in accordance you’re your data
classification strategy. Do not store sensitive health data in
tags, as they are not intended to be used for private or
sensitive data. Finally, access to resources can be
[controlled
through tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html).

**Implement automated data
classification**

[Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) is a fully managed data security service that can
help you identify sensitive data residing in Amazon S3. Macie
automates the discovery of sensitive data, such as personally
identifiable information (PII), to provide you with a better
understanding of the data that your organization stores in Amazon S3.
Macie also provides you with an inventory of your Amazon S3 buckets,
and it automatically evaluates and monitors those buckets for
security and access control.

You can use Amazon Comprehend (PII) and Amazon Comprehend
Medical (PHI) to evaluate unstructured text data in your
environment. Amazon Comprehend will provide a confidence score
to measure the confidence that the data contains PHI as
defined by HIPAA. This score can help you determine the
sensitivity of the data reviewed.

HCL_SEC2. How are you implementing
least privilege access to health data?

The ability to access health data should be limited to the
people or systems who require the access to perform specific
tasks. This covers access to the data itself, and access the
systems that host health data.

**Use identity and access
management to control access to systems, resources, and
data**

Use AWS Identity and Access Management to control access
to AWS services and resources. Use IAM to control who is
authenticated to the environment and who is authorized to use
services and resources. As outlined in the
[IAM
grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) documentation, start with a
minimum set of permissions, and grant additional permissions
as necessary. This approach exposes you to less risk than
starting with permissions that are too lenient and then trying
to tighten them later.

Health data on the cloud is typically stored in databases, file
systems, and object storage services. The optimal storage
service is determined by the data type (for example,
structured vs. unstructured) and access patterns required by
the workload.  For each data store, use a combination of IAM
permissions and any additional authorization methods to secure
stored health data.

For object storage on Amazon S3, use access policies attached
to your resources (buckets and objects) to implement
additional authorization if necessary. More information can be
found at [identity
and access management in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html). Health data
residing in a data lake based in Amazon S3, including those managed
by AWS Lake Formation, should consider implementing column,
row, and cell-level authorization controls where appropriate.

Use operating system file system permissions to limit access
to health data stored on instance storage, including when
using managed storage services such as Amazon Elastic File System and Amazon FSx for Lustre. Additionally,
use resource and condition statements within IAM policies to
limit IAM principal access to file systems when using managed
storage services.

Control access to managed file systems through narrowly scoped
security groups to prevent unauthorized resources from
connecting to the file system.

Sensitive data stored in managed database services, such as
Amazon Aurora, Amazon Relational Database Service, Amazon Redshift, and Amazon DynamoDB, implement
authorization rules using a combination of IAM permissions and
any additional authorization mechanisms available in the AWS
service. For example, Amazon Redshift supports access controls
as the column-level to limit users access to columns that may
contain sensitive data. The AWS documentation for each managed
database service contains a section titled Identity and Access
Management which documents the access configuration options.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/identity-and-access-management.html*

---

# Detective controls

HCL_SEC3. How are you logging access
to health data?

**Log access to systems,
resources, and data in accordance with your policies and
procedures**

If your workload hosts health data, then under the
[Architecting
for HIPAA Security and Compliance on Amazon Web Services
whitepaper](https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/auditing-back-ups-and-disaster-recovery.html) you must implement and maintain logging of
access to that data in accordance with the regulatory
frameworks applicable to your workload. AWS makes it easy to
log access to health data stored in many services with AWS
CloudWatch and AWS CloudTrail. AWS also provides
service-specific mechanism to audit access to health data and
health data systems. For audit logging details, see the [Architecting
for HIPAA Security and Compliance on Amazon Web Services
whitepaper](https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/auditing-back-ups-and-disaster-recovery.html).

**Configure audit logs to
be centralized and immutable**

Environments that host and process health data should record
and audit any person or system that accesses the data. Such
logging provides evidence that the proper people and systems
are accessing health data, and can be helpful in investigating
a security incident. Configure logging to save to a
centralized location and the logs made immutable to verify
their integrity in the event of a forensic requirement.
Prevent modification of log data by creating an AWS account in
your organization that is designated to host audit logs and
implement strict authorization rules. AWS audit and logging
services, such as CloudWatch and CloudTrail, can save logs to
a central location, yielding one set of logs that encompass an
entire IT environment.

Use CloudTrail to log actions taken by users, roles, and AWS
services across your AWS infrastructure. Enable CloudTrail log
file integrity validation to prevent modification, deletion,
or forgery of CloudTrail log files without detection.

Enable AWS Config in all AWS accounts to assess, audit, and
evaluate resources within your AWS environment. AWS Config
maintains a database of resources, and their associated
configurations. This provides an audit record of AWS resource
configurations over time.

Capture network layer logs to track the transport layer
activity going to and from network interfaces in your VPC
using VPC Flow Logs. When using Elastic Load Balancing, enable
access logs to capture detailed information about the requests
received and processed by one or more load balancers,
including client IP addresses, request paths, and server
responses. Similar approaches should be employed for other AWS
services, such as Amazon API Gateway, which offer similar
functionality.

Configure operating system and application logs, including
managed compute services like AWS Lambda, Amazon Elastic Container Service, and Amazon Elastic Kubernetes Service,
to send logs to CloudWatch log groups.  CloudWatch log
groups can be configured to forward logs to a centralized
account for long-term retention. Develop processes and coding
standards to avoid putting sensitive information into logs.
Additionally, use AWS encryption services to encrypt log data.
When using managed database services to store health data,
such as Amazon RDS and Amazon Redshift, enable database level
audit logging to collect information about connections and
user activity within the database.  You can use service
features to publish database logs to CloudWatch, simplifying
centralized log management.

Enable and configure Amazon S3 access logging for any Amazon S3 buckets that
may contain sensitive health data. Amazon S3 Access Logs record every
upload, download, and modification to stored objects.

Refer to the AWS documentation for each AWS service to find
the supported service-specific logging options.

HCL_SEC4. How often do you review
audit logs?

**Create, document, and
follow a policy and procedure to regularly review audit
logs**

In addition to the creation and documentation of an audit log
review policy and procedure, organizations who are auditing
access to health data should also have systems and procedures
in place to review the audit logs on a regular basis.
Facilitate audits by collecting all logs in a centralized
location. For example, AWS CloudTrail can be configured to
deliver logs from multiple accounts to a single Amazon S3 bucket.
This provides both an easier location allowing regular review
of the logs, while limiting the scope of access required for the
reviewer by limiting them to a single location rather than
multiple accounts.

Enable
[CloudTrail
Insights](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.html) to identify unusual activity in CloudTrail
logs in order to help improve the audit log review process.

**Automate alerts for
potential anomalies detected in logs**

Additionally, use automated systems that will generate
alerts if anomalies are detected in logs.  For example, create
[CloudWatch
alarms based on anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html) that uses previously
recorded metrics to create a model of expected results.  You
can also use [the
Amazon OpenSearch Service to detect anomalies in logs](https://aws.amazon.com/blogs/big-data/preprocess-logs-for-anomaly-detection-in-amazon-opensearch/).
Enable CloudTrail Insights to detect unusual operational
activity that is recorded in your CloudTrail audit logs.
Review all applicable regulatory frameworks and standards and
ensuring the specific requirements are being met.  Configure
all alarms to be received by an identified owner, ensuring
that the alarm is acknowledged, triaged, and actioned.
Finally, create and follow a procedure that outlines a
regular cadence to review all automation configurations for
continued accuracy, sufficiency, and relevance of the alerts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/detective-controls.html*

---

# Infrastructure protection

HCL_SEC5. How does your organization
protect critical systems?

Follow Well-Architected best practices for
[infrastructure
protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) when designing and managing your
transactional systems of record.

**Implement security
controls necessary to protect the infrastructure within the
AWS account**

Migrated healthcare workloads may have dependencies on
technologies, older software applications, and host operating
systems. For such systems, limit network access to sensitive
hosts, apply the latest available security patches, and the
employ monitoring practices described above.

Enable [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) in accounts that
host and process PHI to add intelligent threat detection to
your environment. GuardDuty continuously monitors
your AWS accounts and workloads for malicious activity and
provides detailed security findings. You can also create
custom, automated [responses
to GuardDuty findings using Amazon CloudWatch Events](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html).

For details on workload protection, see the [security
pillar of the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/infrastructure-protection.html*

---

# Data protection

HCL_SEC6. How do you determine and
enforce data residency requirements?

**Determine applicable
regulatory frameworks and controls as it pertains to data
locality**

Many healthcare organizations fall under data locality
requirements or regulations on where data may be physically
located.  Begin by reviewing these requirements within any
applicable regulatory frameworks. To determine applicable
regulatory frameworks, start with local regulations and
frameworks for the country where your sensitive healthcare
data is generated, hosted, and processed. Engage with legal
counsel who can help you define the scope of the local
regulations, as well as any additional regulation frameworks
that may apply to you.

**Enforce data locality
requirements by implementing controls**

Once the determination of requirements has been made and
documented, technical controls can be put in place to enforce
them.

The AWS Cloud spans many Availability Zones and geographic
Regions around the world. Each AWS Region is fully isolated,
and comprised of multiple Availability Zones. You can choose
to use one or many AWS Regions in your environment. AWS stores
and processes your content in the AWS Regions you select,
using the services you select. AWS will not move your content
without your consent, except as legally required. This allows
you to establish environments in a location or locations of
their choice. For example, AWS customers in Germany can choose
to deploy their AWS services exclusively in one AWS Region,
such as the Europe (Frankfurt) Region, and store their content
onshore in Germany.

AWS also provides mechanisms for customers to allow or deny
access to specific Regions.  When using AWS Organizations,
implement service control policies (SCP) to limit access to
specific AWS services or resources. SCPs can be used with
[AWS Control Tower data residency controls](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-control-tower-controls-data-residency-requirements/) to create
additional guardrails to enforce data locality requirements.
Continuing the example above, you can implement a service
control policy that allows only access to the Europe
(Frankfurt) Region and denies access to all others.  A sample
service control policy, or SCP, can be found
[here](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html).
Additionally, if you are using AWS Control Tower, implement
the [Region
deny guardrail](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html) to deny access to specific Regions.

HCL_SEC7. How are you protecting
health data at rest and in transit?

**Encrypt sensitive health
data at rest and in transit at all times**

Protect all sensitive data stored and transmitted within a
cloud environment with AWS encryption services. The AWS
Business Associate Addendum (BAA), applicable to customers who
align with the Health Insurance Portability and Accountability
Act (HIPAA), requires the encryption of protected health
information (PHI) as defined by HIPAA at rest and in transit.
Encryption at rest and in transit may be required by other
applicable frameworks.

As documented in the
[data
encryption](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/data-encryption.html) section of the
[Introduction
to AWS Security](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html) whitepaper and the
[Encrypting
Data-at-Rest and -in-Transit](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.html) section of the
[Logical
Separation on AWS](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/welcome.html) whitepaper, AWS allows you to add a
layer of security to your data at rest in the cloud, providing
scalable and efficient encryption features. These include:

- Data at rest encryption capabilities available in most AWS
services, such as Amazon Elastic Block Store (Amazon EBS),
Amazon S3, Amazon RDS, Amazon Redshift, Amazon ElastiCache, AWS Lambda, and Amazon SageMaker AI
- Flexible key management options, including AWS Key Management Service (AWS KMS), that allow you to choose
whether to have AWS manage the encryption keys or enable
you to keep complete control over your own keys
- Dedicated, hardware-based cryptographic key storage using
AWS CloudHSM, allowing you to help satisfy your compliance
requirements
- Encrypted message queues for the transmission of sensitive
data using server-side encryption (SSE) for Amazon Simple Queue Service (Amazon SQS)

In addition, AWS provides APIs for you to integrate encryption
and data protection with any of the services you develop or
deploy in an AWS environment.

**Implement encryption
controls as part of the infrastructure
architecture**

Use infrastructure as code to declare encryption as a
configuration when creating an environment template. Use
alerts and automated remediation, where possible, with AWS Config that can detect when a resource is not configured to
use encryption. Where automated remediation is not available,
verify that alerts are generated and sent to the appropriate
parties.

Amazon EBS, block-storage for use with Amazon EC2 Auto Scaling, uses AWS KMS keys to encrypt storage
volumes and snapshots. Encryption operations occur on the
servers that host Amazon EC2 instances, ensuring the security of data
at rest and data in transit between an instance and attached
Amazon EBS volumes. Consider configuring your AWS accounts for Amazon EBS
[encryption
by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html), enforcing that any created Amazon EBS volumes are
encrypted automatically.

Amazon RDS uses configuration policies that can enforce
encrypted connections to a hosted database. The Amazon RDS
documentation contains information on
[using
SSL/TLS to encrypt a connection to the database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html),
including options for enforcing the connection through either
parameter groups (Amazon RDS for Postgres, Aurora for Postgres, Amazon RDS
for MariaDB, or Amazon RDS for Microsoft SQL Server) or option groups
(Amazon RDS for Oracle).

Amazon S3 buckets that may contain health data should be configured
to require secure connections with the use of a bucket policy,
and require encryption of data at rest. Below is an example of
a bucket policy that explicitly denies access when a secure
transport connection is not used:

Encryption in transit between systems must be identified and
enforced where possible. AWS services provide HTTPS endpoints
using TLS for communication, providing encryption in transit
when communicating with the AWS APIs. Insecure protocols, such
as HTTP, can be blocked in a VPC through the use of security
groups. HTTP requests can also be
[automatically
redirected to HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html) in Amazon CloudFront or on an
[Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html).

When hosting applications on Amazon EC2 instances, use open standard
transport encryption mechanisms such as Transport Layer
Security (TLS) to encrypt data during transit between
instances and endpoints. Certain Amazon EC2 instance types can
offload encrypting traffic between instances to the underlying
Nitro System hardware, using Authenticated Encryption with
Associated Data (AEAD) algorithms with 256-bit encryption. For more detail and a list of supported instance
types, see [encryption
in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html).

Microservice architectures should also consider controls to
enforce encryption of data between services when hosting and
processing health data. AWS App Mesh, a service mesh that
makes it easy to monitor and control service, features
Transport Layer Security (TLS) encrypts communication between
the Envoy proxies deployed on compute resources that are
represented in App Mesh. When the proxy is deployed with an
application, your application code is not responsible for
negotiating a TLS session. The proxy negotiates TLS on your
application's behalf. For more detail, see
[Transport
Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html).

HCL_SEC8. How do you isolate
sensitive data?

**Isolate health data from
non-health data**

Organizations working with health data should take steps to
isolate and segment health data from non-health data. In
conjunction with the recommendations around data discovery and
classification, it is important to separate health data so the
organization can implement the necessary technical and
administrative controls.

Isolation can be accomplished through a variety of methods
depending on the cloud environment. AWS recommends beginning
with using multiple AWS accounts and designating specific
accounts as containing health data. AWS accounts provide a
level of segmentation that allows strict controls to be put in
place for workloads that host and process health data.
[AWS Organizations](https://docs.aws.amazon.com/organizations/), an account management service that
enables you to consolidate multiple AWS accounts into an
organization that you create and centrally manage, provides
management capabilities that allow you to group like accounts
into organizational units (OUs) and apply policies at the OU
level. This verifies that all accounts within that OU are
using a standardized set of policies and controls, which can
help organizations align to their specific compliance needs.

Furthermore, as outlined in the
[Organizing
Your AWS Environment Using Multiple Accounts
whitepaper](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html), when you limit sensitive data stores to an
account that is built to manage it, you can more easily
constrain the number of people and processes that can access
and manage the data. This approach simplifies the process of
achieving least privilege access. Limiting access at the
coarse-grained level of an account helps contain exposure to
highly sensitive data.

**Limit access to health
data**

It is also important to limit access to health data within an
account. Use resource isolation, such as designated Amazon S3
buckets, to separate health data from non-health data.
Resource isolation can also be used to isolate tenants and
tenant-specific data. Resource isolation and tenant isolation
reinforce the benefits to account isolation, limiting access
to sensitive data to only the people and systems that require
it, without unnecessarily blocking access to less sensitive
data. Refer to the Security pillar section of the
[Well-Architected
Framework SaaS Lens](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html) for additional recommendations on
tenant isolation.

Tagging allows limiting access to specific resources through
the use of
[conditional
statements](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in IAM policies. By adding a specific
resource tag to an IAM policy, such as `data type: health`,
organizations can allow or deny access to resources with that
tag. This approach adds an additional layer of authorization
to resources that host and process health data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/data-protection.html*

---

# Incident response

HCL_SEC9. What is your disaster recovery for
critical systems?

**Mitigate and respond to
potential incidents by creating policies, procedures, and
playbooks**

Healthcare, and heath data, are valuable targets for malicious
actors. Create policies, procedures, and playbooks designed to
respond to and mitigate the potential impact of a security
event or natural disaster. This includes exercises that
practice the response to a simulated incident using the
defined policies, procedures, and playbooks to prepare your
organization.

As malicious actors continue to target healthcare and health
data owners with attacks such as ransomware, implement a data
availability strategy to help reduce the potential impact.
This can include backups that are stored in a separate AWS account with authorization controls in place to prevent
modifying the backup (such as setting the backup as read only)
or a [pilot
light disaster recovery environment](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html). Create specific
policies, procedures, and playbooks for ransomware to prepare
your organization.

The
[incident
response section of the security pillar in the AWS
Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/incident-response.html) contains further details on
preparing for and responding to security incidents in the
cloud.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/incident-response.html*

---

# Key AWS services

The AWS service that is essential to security is AWS Identity and Access Management, which allows you to securely
control access to AWS services and resources for your users. The
following services and features support the four areas of
security:

**Identity and access
management:**

- [AWS Identity and Access Management;](https://aws.amazon.com/iam/)
- [AWS IAM Identity Center](https://aws.amazon.com/single-sign-on/)
- [AWS Directory Service](https://aws.amazon.com/directoryservice)
- [Amazon Cognito](https://aws.amazon.com/cognito/)

**Detection:**

- [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/)
- [Amazon Detective](https://aws.amazon.com/detective/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon Inspector](https://aws.amazon.com/inspector/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)

**Infrastructure protection:**

- [AWS Key Management Service](https://aws.amazon.com/kms/)
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

**Data protection:**

- [Amazon Macie](https://aws.amazon.com/macie)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Network Firewall](https://aws.amazon.com/systems-manager/)
- [AWS Virtual Private Network](https://aws.amazon.com/vpn/)

**Incident response:**

- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon Detective](https://aws.amazon.com/detective/)
- [Amazon Inspector](https://aws.amazon.com/inspector/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/key-aws-services-1.html*

---

# Resources

Refer to the following resources to learn more about our best
practices for security.

**Documentation and blogs:**

- [Encryption-in-transit
for public sector workloads with AWS Nitro Enclaves and AWS Certificate Manager](https://aws.amazon.com/blogs/publicsector/encryption-in-transit-public-sector-workloads-aws-nitro-enclaves-aws-certificate-manager/)

**Whitepapers:**

- [Architecting
for HIPAA Security and Compliance on Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/welcome.html?did=wp_card&trk=wp_card)
- [Introduction
to AWS Security](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html?did=wp_card&trk=wp_card)
- [Data
residency: AWS policy perspectives](https://aws.amazon.com/blogs/security/addressing-data-residency-with-aws/)
- [Logical
Separation on AWS](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/welcome.html)

**Videos:**

- [AWS Security Webinar: The Key to Effective Cloud
Encryption](https://www.youtube.com/watch?v=78qFK-r7WBI)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/resources-1.html*

---
