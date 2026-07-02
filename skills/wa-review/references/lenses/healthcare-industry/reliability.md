# Reliability

**Pages**: 7

---

# Design principles

In the cloud, there are a number of principles that can help you
increase reliability:

- **Evaluate and understand availability
and latency implications:**Many healthcare
applications are latency-sensitive. Healthcare workloads may
also be life-critical, meaning that service interruptions
may lead to patient harm. Consider latency, connectivity,
and availability requirements in defining the cloud
architecture of your workload. Choose your deployment option
to meet those requirements based on modeling real-world
scenarios.
- **Address potential implications by
defining reliability and availability
requirements:** Understand the availability
requirements for your solutions and the consequences of
service disruptions before designing your architecture. From
that understanding, define the specific requirements for
reliability and availability.
- **Understand the end user
setting**: Document the settings your end users
will use for your solution.  Some healthcare solutions are
only used within hospitals, while others may be used by
providers working remotely.  Use your understanding of the
settings by which end users access your solution to meet
reliability requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/design-principles-2.html*

---

# Foundations

HCL_REL1. How does your system adapt
to changes in demand?

**Architect systems for
elasticity**

Healthcare applications often have time-based peaks in demand.
For example, clinical systems may need to respond to periods
of high demand using either time-based or usage-based metrics
to define automatic scaling rules.  An example of periods of
high demand could be daytime business hours or a known event
such as open-enrollment for an insurance provider.

Where possible, implement architectures that automatically
adapt to changes in demand. Embracing elasticity enables
healthcare organizations to *right-size*
performance during all hours of the day while minimizing
excess cost. General distributed systems recommendations
apply. Where possible, leverage AWS services that allow you to
scale with demand.

AWS Auto Scaling simplifies how you adapt to demand. In all
cases, you should be collecting metrics to inform your scaling
actions and detect events that could impact reliability. You
may either use default CloudWatch metrics or define custom
metrics that track specific aspects of utilization. For
example, software as a service (SaaS) applications may monitor
demand with custom CloudWatch metrics that capture the number
of concurrent active users, or open sessions supported by the
application.

Healthcare solutions implemented as distributed systems may
use multiple services that can scale elastically. In these
cases, implement automatic scaling for all relevant compute
and database services, using Amazon EC2 Auto Scaling and Application Auto Scaling for
[supported
AWS services](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html). You can leverage scaling plans to
simplify configuration of scaling rules, and follow auto
scaling
[best
practices](https://docs.aws.amazon.com/autoscaling/plans/userguide/best-practices.html) to maximize reliability.

Other managed services, such as Amazon Data Firehose,
allow you to operate at scale without worrying about capacity
or managing infrastructure.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/foundations.html*

---

# Workload architecture

HCL_REL2. How do you ensure
acceptable network availability for your healthcare
workloads?

**Architect redundant and
reliable network connections to ensure care
continuity**

Many healthcare applications, such as those in a hospital,
require secure connectivity between the cloud and on-premises
resources and users. When evaluating your network setup,
consider your business continuity and disaster recovery
requirements. Certain healthcare applications will be more
accepting of shifts in latency or availability compared to
others. For example, medical imaging or EHR systems may
require more consistent latency and connectivity compared to
other systems in a hospital.

Following the
[Well-Architected
Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-your-network-topology.html), redundant, encrypted connections
are critical to verify service continuity and, more
importantly, consistent patient care. Many best practices can
be found in the
[AWS Well-Architected Framework Hybrid Networking Lens](https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hybrid-networking-lens.html?did=wp_card&trk=wp_card).

AWS Direct Connect is key to establishing consistent,
redundant connections with your on-premises data sources.
Direct Connect establishes a dedicated network connection to
AWS. It is possible to create multiple connections to AWS from
a single location.

There are
[two
common approaches](https://docs.aws.amazon.com/directconnect/latest/UserGuide/disaster-recovery-resiliency.html) to establishing redundancy across
your network connection to AWS:

- Redundant Direct Connect connections: Use the
[AWS Direct Connect resiliency toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) to enable
resilient applications and achieve an SLA of 99.99%.
- [Failover
to public internet connection with VPN routing.](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-vpn.html)
Customers can either connect to Amazon VPCs using VPNs or
through AWS Transit Gateway.

In both cases, check that encryption is enabled for all
connections into AWS as well as within AWS. Encryption can be
enabled at multiple layers, such as at the network or
application layers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/workload-architecture.html*

---

# Change management

There are no reliability best practices for change management specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/change-management.html*

---

# Failure management

There are no reliability best practices for failure management specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/failure-management.html*

---

# Key AWS services

The AWS service that is key to ensuring reliability is Amazon CloudWatch, which monitors runtime metrics. Other services and
features that support the four areas of reliability are as
follows:

**Foundations:**

- [AWS Direct Connect](https://aws.amazon.com/directconnect/)

**Workload architecture:**

- N/A

**Change management:**

- [AWS Config](https://aws.amazon.com/config/)
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/), and
[Application Auto Scaling](https://aws.amazon.com/autoscaling/)

**Failure management:**

- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/key-aws-services-2.html*

---

# Resources

Refer to the following resources to learn more about our best
practices related to reliability.

**Video and analyst report:**

- [Connectivity
to AWS and hybrid AWS network architectures](https://www.youtube.com/watch?v=eqW6CPb58gs)

**Documentation and blogs:**

- [AWS Direct Connect User Guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

**Whitepapers:**

- [Building
a scalable and secure multi-VPC AWS network
infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html?did=wp_card&trk=wp_card)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/resources-2.html*

---
