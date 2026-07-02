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
