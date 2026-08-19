# Security

**Pillar**: Security  
**Questions**: 8

---

# ADVSEC01 — Identity and access management

**Pillar**: Security  
**Best Practices**: 4

---

# ADVSEC01-BP01 Implement user authentication and access control to protect bidding process and content

Authenticate the approved SSPs (supply-side platforms) and
advertisers. Based on this authentication, DSPs can provide them
with least-privileged authorization and access to the relevant
resources and data.

## Implementation guidance

AWS offers multiple services to provide SSPs and DSPs secured
and scalable user management across all parts of the workload.
Consider using
[Amazon Cognito](https://aws.amazon.com/cognito/) to provide scalable authentication,
authorization, and user management to your applications.
Implementing federated identity integration with trusted
identity providers can allow for ideal single sign on (SSO) for
both publishers and advertisers. SSPs and DSPs can either use
SAML 2.0 or OpenID Connect (OIDC) to create a trusted identity
provider. From there, roles and permissions can be configured by
a trusted administrator for users from the identity provider.

Additionally, you can use
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) for fine-grained access control
for users and different AWS services that may interact with
advertising workloads. Enforce strict IAM policies that define
permissions to help control access within AWS workloads. IAM
policies define permissions for an action regardless of the
method used to perform the operation.

Consider implementing role-based access control to determine
which access to resources may align with a role based on
business requirements. Use specific roles for different
advertising services, including DSPs and SSPs, to verify that
services operate with limited least privileged access.

## Resources

- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp01.html*

---

# ADVSEC01-BP02 Restrict DSP access to allow only authorized SSPs

Provide a mechanism to control and manage third-party access to
each part of your cloud network environment.

## Implementation Guidance

Consider using
[AWS WAF](https://aws.amazon.com/waf/) to
allow access for authorized IPs for traffic that arrives at your
[Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html),
[Amazon API Gateway](https://aws.amazon.com/api-gateway/), and Amazon CloudFront distributions. AWS WAF helps
protect your web applications against common web exploits that
may compromise security. Using AWS WAF rules, you can define a
set of inspection criteria and review when incoming requests
meets the set criteria. It is recommended to use AWS WAF rules
to inspect incoming traffic based on several factors like source
IP or originating geographic location.

Additionally, consider using AWS PrivateLink to restrict access to
your AWS services. AWS PrivateLink allows for the private connection
between your AWS VPCs and AWS services without exposing your
network traffic to the public internet. If you cannot use
AWS PrivateLink, consider using IAM to control access to your AWS
services.

## Resources

- [Configure
security groups for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-vpc-security-groups.html)
- [How
do I use AWS WAF to create IP set rules to restrict IPv4 and
IPv6 access?](https://repost.aws/knowledge-center/waf-allow-my-ip-block-other-ip)
- [Update
the security groups for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-security-groups.html)
- [Controlling
access to Amazon Kinesis Data Streams resources using
IAM](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html)
- [Introducing
Amazon API Gateway Private Endpoints](https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/)
- [Use
interface VPC endpoints for Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/vpc.html)
- [Private
Amazon AppFlow flows](https://docs.aws.amazon.com/appflow/latest/userguide/private-flows.html)
- [Create
a server in a virtual private cloud](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html)
- [Configuring
VPC endpoints as AWS Database Migration Service source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_VPC_Endpoints.html)
- [Creating
an interface VPC endpoint for AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/vpc-interface-endpoints.html)
- [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html)
- [Considerations
for AWS Glue VPC endpoints](https://docs.aws.amazon.com/glue/latest/dg/vpc-interface-endpoints.html)
- [Amazon MSK multi-VPC private connectivity in a single Region](https://docs.aws.amazon.com/msk/latest/developerguide/aws-access-mult-vpc.html)
- [Changing
an Amazon MSK cluster's security group](https://docs.aws.amazon.com/msk/latest/developerguide/change-security-group.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp02.html*

---

# ADVSEC01-BP03 Restrict DSP outbound traffic to authorized SSPs only

Address the risk of DSP unintentional data disclosure to SSPs that
were not approved.

## Implementation guidance

Consider using an
[Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/) to restrict outgoing traffic from
instances to the authorized DSP endpoints. VPCs can to define
access to verify that all ports, protocols, and destination IP
addresses meet your organizations security needs. Use VPC
security groups to permit access from trusted sources or
specific IP ranges. Use a protocol with encryption when
transmitting data to maintain data confidentiality and mitigate
the risk of unauthorized access to the data.

Additionally, implement
[AWS Network Firewall](https://aws.amazon.com/network-firewall/) to provide control over outbound traffic from
your VPCs to approved destinations only. Network Firewall allows
you to define and enforce rules to inspect and filter outgoing
traffic against malware or unauthorized data exfiltration. Using
Network Firewall rule groups, you can prevent data loss, meet
compliance requirements, or block any known malware
communications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp03.html*

---

# ADVSEC01-BP04 Implement authorization by setting access policies, and implement least privilege access to protect programmatic workloads

Address the risk of authenticated advertisers and SSPs access to
data they should not reach.

## Implementation guidance

Implement strong
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam) policies when you deploy a global
advertising technology workload. Use the principle of least
privilege, and enforce the separation of duties for good
security posture. Administrative access should only be given to
a small number of secured administrators.

Use [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) to validate IAM policies and verify that
they match IAM best practices and your organization's security
standards.

IAM Access Analyzer can help your organization review and
removed unused or external access across your AWS resources with
continuous monitoring. IAM Access Analyzer can also assist
administrators by validating your IAM policies against IAM
policy grammar and AWS best practices.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec01-bp04.html*

---

# ADVSEC02 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS

Protect data in transit by using encrypted communication channel
at the network communication level.

## Implementation guidance

Protecting data that is transmitted from network to network
remains a top security priority. Data confidentiality,
integrity, and authenticity of the supported workloads are
crucial for securing sensitive information, preventing
unauthorized access, and enabling reliable operations within the
workload.

Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to establish connectivity between Amazon VPCs
and other services without exposing the data to the public
internet. If you have on-premises resources, consider using
[AWS Direct Connect](https://aws.amazon.com/directconnect/). Direct Connect can make it easy to
establish private connectivity between an AWS datacenter and
your internal network. Implementing MACsec security on your
Direct Connect connection provides point-to-point encryption for
your traffic.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec02-bp01.html*

---

# ADVSEC03 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC03-BP01 Use distributed denial of service (DDoS) protection service to maintain platform availability

Deploying DDoS protection helps create strategies for robust
system reliability against potential threats.

## Implementation guidance

AWS Shield Standard protects against most DDoS attacks by
protecting your AWS resources. AWS Shield Standard is
automatically enabled to all AWS customer accounts by default.
AWS Shield defends against common volumetric and exhaustion
attacks and can help protect advertising endpoints such as API's
and websites. AWS Shield can protect advertisement servers or
DSPs APIs that may be accessed by advertisers and publishers
globally.

To additional features to help you protect against DDoS attacks, consider implementing
[AWS Shield Advanced](https://aws.amazon.com/shield/) to provide additional DDoS protection. Shield Advanced includes continual proactive support and increased
bandwidth to protect from DDoS attacks. Shield Advanced can
provide advanced monitoring and protection to Amazon CloudFront
distributions, Route 53 hosted zones, and Amazon ELBs.

Additionally, [AWS WAF](https://aws.amazon.com/waf/) can help protect login and provider sign-in pages
against credential stuffing or creation of fake accounts. By
deploying AWS WAF rules, companies can implement protection
against commonly deployed web-based attacks. These attacks
include bad bots and SQLi. AWS WAF helps prevent those web
requests from hitting your CloudFront edge distributions. You
can use AWS WAF to implement bad actor deny lists, which can
help prevent certain denial of service (DOS) or bad actors
trying to implement malicious ad injection.

## Resources

- [AWS Shield Advanced overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec03-bp01.html*

---

# ADVSEC04 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC04-BP01 Implement secure data collaboration with least privileged access and privacy controls

## Implementation guidance

Raw data that is used in collaboration with SSPs, DSPs, and
third-party systems need to be carefully shared to verify
consumer privacy and data protection. Consider using AWS
Clean Rooms, which enables more secure data collaboration
without potentially exposing raw data and allows different
parties to review and analyze data while maintaining strict
privacy controls. With AWS Clean Rooms, you can create a
more secure data clean room in minutes and collaborate with
other companies to generate unique insights about
advertising campaigns, investment decisions, and research
and development. AWS Clean Rooms automatically encrypts
service metadata at rest without requiring additional
configurations. AWS Clean Rooms allows for you to have
granular control on the type of information you may want to
share.

Use IAM to provide least privileged access to approved
parties with AWS Clean Rooms. Use IAM policies to define
which users and roles can access which data, analyses, and
collaborations. This allows for the precise control of how
data is created, modified, and queried within AWS Clean
Rooms.

### Key AWS services

- AWS Clean Rooms
- AWS IAM

### Resources

- [Solutions for Advertising and Marketing](https://aws.amazon.com/solutions/advertising-marketing/)
- [AWS Clean Rooms proof of concept scoping part 1: media measurement](https://aws.amazon.com/blogs/big-data/aws-clean-rooms-proof-of-concept-scoping-part-1-media-measurement/)
- [How AWS Clean Rooms works with IAM](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security_iam_service-with-iam.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec04-bp01.html*

---

# ADVSEC05 — Fraud detection

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC05-BP01 Validate and sanitize content before running a campaign

Content validation is essential to mitigate ad fraud and block
unwanted content from reaching ad audience.

## Implementation guidance

Consider using
Amazon S3 which can serve as a secure, scalable storage
solution for advertising content. It allows for simple
management and distribution of assets. S3 can be configured
with strict access controls and encryption to maintain the
security of the advertisement files. Additionally, Amazon
Rekognition can be utilized to analyze images and videos in
advertisements, verifying they meet solution standards and
don't contain inappropriate content. This AI-powered service
can detect objects, scenes, and activities in visual content.
For additional monitoring and auditing, consider using AWS
CloudTrail to provide a record of actions taken by users,
roles, or AWS services in the ad serving solution, which is
essential for security analysis and compliance audits.

## Key AWS services

- Amazon S3
- Amazon Rekognition
- AWS CloudTrail

## Resources

- [Checking object integrity in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html)
- [Amazon Rekognition](https://aws.amazon.com/rekognition/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec05-bp01.html*

---

# ADVSEC06 — Regulatory adherence

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC06-BP01 Verify your advertising workload remains adherent to data protection regulations

Maintaining compliance is essential to operate and grow your
solution. Data encryption is a key requirement for several
compliance programs; you can utilize AWS KMS to facilitate
data encryption and key management for your solution. KMS
allows for the creation and management of cryptographic keys
which can be used to encrypt data at rest and in transit. It
simply integrates with other AWS services and maintains an
audit trail for key usage. KMS also maintains validation and
certifications from multiple compliance regimes including
FIPS, PCI DSS, and HIPAA.

## Implementation guidance

To assist with data governance consider using Amazon Macie.
Macie can automatically scan and identify sensitive data
across AWS environments. The service can categorize data based
on content type and sensitivity level. Based on the data
classification Macie provides a risk score for different
datasets and storage locations. Amazon Macie can assist to
meet regulatory requirements including GDPR, CCPA, HIPAA, by
generating detailed reports on data types and locations for
regulatory audits.

## Key AWS services

- AWS KMS
- Amazon Macie

## Resources

- [Compliance validation for Macie](https://docs.aws.amazon.com/macie/latest/user/compliance-validation.html)
- [Compliance validation for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-compliance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec06-bp01.html*

---

# ADVSEC07 — User privacy

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC07-BP01 Enable secure data privacy and collaboration between advertisers while protecting user privacy

Delivering a privacy-centric advertising infrastructure
assists to optimize your system to keep privacy which focuses
on data minimization and secure processing.

## Implementation guidance

Consider
implementing AWS Clean Rooms as the service makes it simple
for you and your partners to analyze and collaborate on
collective datasets to gain insights without revealing
underlying data to one another. AWS Clean Rooms enable you to
share secure data between different parties while maintaining
data privacy and control. It has configurable data access
controls and differential privacy options. AWS Clean Rooms
serves as a privacy-enhanced alternative to traditional
cookie-based tracking, aligning well with privacy sandbox
principles.

## Key AWS Service

- AWS Clean Rooms

## Resources

- [AWS Clean Rooms FAQs](https://aws.amazon.com/clean-rooms/faqs/#topic-0)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec07-bp01.html*

---

# ADVSEC08 — Brand safety

**Pillar**: Security  
**Best Practices**: 2

---

# ADVSEC08-BP01 Create guardrails and controls to maintain brand safety and content moderation within your workload

Brand reputation protection can block brand association with
inappropriate or otherwise harmful content. Having guardrails
can maintain customer trust and potential business
relationships while avoiding reputational damage and negative
publicity.

## Implementation guidance

Consider implementing Amazon SageMaker AI, with the
custom model development capability of SageMaker AI, you can
build, train, and deploy custom machine learning models.
Designing a guardrail for brand safety could allow you to
develop a model that could detect inappropriate imagery in
advertisements, classify text within content for sentiment and
safety, and predict the likelihood of an ad placement being
brand appropriate. With the real time inference capability of
SageMaker AI, you can deploy your models deemed brand safe for
real time content analysis, allowing for quick decision making
for your solution.

Additionally, consider using AWS Config, to
assess, audit, and evaluate resource configurations within
your AWS environment. Config can track changes to underlying
resources with your advertising solution to verify that
security settings and access controls remain
compliance-aligned for brand safety.

## Key AWS services

- AWS Config
- Amazon SageMaker AI

## Resources

- [Examples and More Information: Use Your Own Algorithm or Model](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-notebooks.html)
- [Compliance](https://docs.aws.amazon.com/config/latest/APIReference/API_Compliance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec08-bp01.html*

---

# ADVSEC08-BP02 Look for opportunities to block ad fraud and enhance transparency in your advertising solution

DSP’s need to verify their advertisers and agencies are
purchasing legitimate advertising inventory across potentially
multiple exchanges in real time. Consider implementing an
ads.txt file, designed by IAB tech labs, is designed to enable
additional transparency within the advertising solution by
allowing DSPs to review legitimate companies authorized to
market their advertisement inventory.

## Implementation guidance

Adding an `ads.txt` file
lets ad publishers declare which services can market their ad
space. Retailers can verify incoming advertisement inventory
against the list to verify authenticity. This aids in fraud
prevention by blocking domain spoofing threats by bad actors
impersonating legitimate publishers. The file also aids in
protecting DSP’s budgets and campaigns performance. Ads.txt
may also aid in compliance by meeting certain criteria large
advertisers require within their best practices.

Consider
using Amazon S3 to host your `ads.txt` file for highly available
and simple access. Amazon S3 allows for version control and
accessible updates to the file if needed. Lastly, within Amazon S3,
you can block object version deletion using S3 object lock.
This defined retention period can be used as an extra layer of
data protection.

## Key AWS services

- Amazon S3

## Resources

- [Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec08-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
