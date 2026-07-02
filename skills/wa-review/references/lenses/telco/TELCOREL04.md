# TELCOREL04 — Failure management

**Pillar**: Reliability  
**Best Practices**: 3

---

# TELCOREL04-BP01 Implement the Bypass Mode on peripheral network devices such as firewalls and network probes while connecting to the cloud

Implementing bypass mode on network peripheral devices like firewalls and network probes is
crucial for maintaining service continuity during device failures or power outages. This
mechanism automatically creates a direct connection between incoming and outgoing network ports
when a device fails, maintaining that critical network traffic continues to flow without
interruption. By deploying bypass-capable devices while connecting to the cloud-based network
infrastructure, telecom operators can block service disruptions that could occur during device
failures, maintenance windows, or unexpected outages. This approach is particularly important
for maintaining high availability in telecommunications networks where continuous service is
essential for customer satisfaction and regulatory adherence.

**Desired outcome:**

- Verify continuous network traffic flow during device level failures.
- Minimize service disruptions during maintenance or unexpected outages.
- Maintain high availability for critical network services.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Design your network architecture to include redundant paths and automated routing updates
that can quickly respond to device failures. Implement comprehensive health monitoring and
automated recovery procedures to minimize service disruptions. Establish clear operational
procedures for managing bypass events, including notification workflows and post-event
analysis to block recurring issues.

Regular testing of the bypass functionality is crucial to verify it will work as expected
during actual failures. This includes conducting controlled failure scenarios during
maintenance windows and validating that traffic continues to flow without interruption.
Document bypass events and maintain historical data to identify patterns and potential
improvements to the bypass implementation.

### Implementation steps

- Deploy AWS Network Firewall with fail-open configurations across multiple Availability Zones
to verify continuous traffic flow during failures.
- Configure AWS Transit Gateway for centralized network management with automatic routing
failover capabilities.
- Use Amazon CloudWatch to monitor device health and performance metrics, with automated
alerts for potential failures on AWS services involved.

## Resources

**Key AWS services:**

[AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel04-bp01.html*

---

# TELCOREL04-BP02 Implement dual network planes for signaling or control plane

A resilient network architecture implementing two independent and redundant signaling
networks that operate in parallel. Each signaling plane handles messages and controls network
resources independently, with logical and physical separation to verify that failures in one
plane do not impact the other plane's operations.

**Desired outcome:**

- Enhanced fault tolerance through dual planes.
- Independent operation capability.
- Seamless failover between planes.
- Maintained service continuity.
- Isolated failure domains.
- Verified redundancy effectiveness.
- Documented recovery procedures.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Design a resilient network architecture with separate signaling planes for control plane
traffic, maintaining comprehensive logical and physical separation. Enforce strict network
access controls and security zoning to maintain the separation. Configure robust failover
mechanisms, with automated triggers, recovery procedures, and comprehensive health monitoring
across the planes. Test the failover functionality under various failure scenarios and
document the recovery steps. Deploy advanced monitoring and observability tools to track the
performance, availability, and security of both signaling planes, establish key metrics and
alerting thresholds, and regularly review the monitoring strategy for continuous improvement.

### Implementation steps

- Design separate signaling planes:

Use AWS Transit Gateway and AWS Network Firewall to implement a
vendor-neutral strategy for logical and physical separation between control and user
plane traffic. Configure AWS Network ACLs and security groups to enforce network
zoning, traffic classification, and security controls.

- Verify physical separation:

Use AWS Config to specify and enforce the
technical requirements for network isolation, including network segments,
addressing, and security controls. Use AWS Config Rules to monitor and enforce requirements
affecting the separation.
- Deploy the separate network infrastructure for
each plane using Amazon VPC and AWS Direct Connect. Utilize AWS Transit Gateway and AWS Network Firewall to
implement network virtualization and segmentation.
- Configure AWS Network Firewall and Amazon VPC security groups to
enforce strict network access controls and security policies. Define and enforce the
security zones and trust boundaries using AWS IAM and AWS Service Control
Policies.

- Configure failover mechanisms:

Use Amazon CloudWatch alarms and AWS Lambda functions to
establish the conditions and thresholds for automated failover.
- Deploy Amazon CloudWatch and AWS Lambda to monitor the health of
the planes and trigger the appropriate failover responses.
- Use AWS Fault Injection Service to regularly test the failover
functionality under various failure conditions. Document the test procedures and
success criteria in AWS Systems Manager.
- Create detailed recovery procedures for different
failure scenarios. Include troubleshooting guides and contact information.

- Monitor plane status:

Use Amazon CloudWatch to monitor the performance,
availability, and security metrics for both planes.
- Establish key performance indicators using Amazon CloudWatch
that reflect service health, including latency, throughput, error rates, and
resource utilization. Set appropriate thresholds and baselines.
- Configure Amazon CloudWatch alarms and Amazon SNS to implement a notification
system for critical events and threshold violations. Define alert severity levels
and response procedures.
- Regularly evaluate monitoring strategy effectiveness and
adjust based on operational experience. Update metrics and thresholds as needed.

## Resources

**Key AWS services:**

- [Amazon VPC](https://aws.amazon.com/vpc/)
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel04-bp02.html*

---

# TELCOREL04-BP03 Implement default configuration to bypass billing and charging services in case the system is down

Implementing a default configuration to bypass billing and charging services in a telecom
network maintains service continuity for customers in the event of a failure or outage in the
billing or charging system. The network is configured with a failover mechanism that continues
providing critical communication services while bypassing the charging/billing component if they
become unavailable or unresponsive. This bypass mode allows customers to continue accessing and
using the telecom services without interruption, even when the billing or charging systems are
down.

**Desired outcome:**

- Verify customer experience and service availability take precedence over billing and
charging functions.
- Allow customers to continue using services while their usage and session data is
temporarily stored or cached within the network.
- Process cached usage data once the billing and charging systems are restored, verifying
revenue is not lost.

## Implementation guidance

Implement a default configuration on the control plane functions that allows the network
to bypass the billing and charging systems in the event of a failure or outage. Configure the
network functions to continue call setup or session establishment even when the charging
system is unresponsive. When the billing or charging systems are restored, they process the
cached usage data to verify revenue is not lost despite the temporary bypass of these systems.

### Implementation steps

- Define bypass triggers and thresholds:

Use monitoring tools to detect failures or unresponsiveness in the billing
and charging systems
- Establish clear criteria and thresholds for triggering the bypass mode, such as
connection timeouts, error rates, or system availability metrics

- Implement bypass configuration:

Configure network functions with a default method to continue call setup or
session setup in case the charging system is unresponsive.

- Use data records and call records for offline charging/billing:

Once the billing or charging systems are back online, the cached usage data can
be processed and the end user is billed accordingly, verifying that revenue is not
lost despite the temporary bypass of these systems.

## Resources

**Key AWS services:**

- [Amazon CloudWatch for monitoring and alerting](https://aws.amazon.com/cloudwatch/)
- [AWS Lambda for implementing custom bypass logic and
data processing](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel04-bp03.html*

---
