# HNPERF02 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# HNPERF02-BP01 Use tradeoffs to improve network performance

When deciding on which technology to choose (VPN vs dedicated
circuits) or which termination endpoint to choose, Consider how
performance, cost, and deployment effort compare across your
options. Understanding the tradeoffs will help you choose the right
tool for the right job. To avoid a one-size-fits-all solution in
your workload, use trade-offs to achieve the peak performance based
on your business and technical requirements.

**Desired outcome:**

- Well-balanced hybrid network architecture that effectively meets
specific business requirements while optimizing cost,
performance, and operational efficiency.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Optimized costs and improved performance
- Faster deployment where needed while ensuring high performance
for critical workloads

## Implementation guidance

- Evaluate workload requirements including bandwidth needs,
latency sensitivity, setup time constraints, and budget
limitations.
- For rapid network connectivity needs, consider service like
AWS Site-to-Site VPN solutions that can be quickly deployed.
- For critical workloads requiring high-performance networking
with consistent low latency, such as real-time transactions or
large-scale data processing, consider dedicated connection
solutions such as AWS Direct Connect that provides reliability
and speed.
- Monitor to validate that chosen solutions meet performance and
cost objectives.

## Resources

- [Connect
your VPC to remote networks using AWS Virtual Private Network](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html)
- [Network
to Amazon VPC Connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp01.html*

---

# HNPERF02-BP02 Choose the right physical PoP location for dedicated connectivity

Points of Presence (PoPs) serve as strategic interconnection
locations between on-premises and cloud environments. These physical
connection points are distributed across various geographic
locations to enable low-latency private network connectivity.
Organizations should understand how PoP locations impact network
performance, as the distance between your infrastructure and these
interconnection points directly affects latency and overall
application performance. For mission-critical applications requiring
consistent, high-performance connectivity, leveraging multiple PoPs
can provide both reduced latency and enhanced reliability

**Desired outcome:**

- Select appropriate termination endpoints that align with current
and future network requirements
- Balance performance needs with cost considerations
- Maintain network isolation while enabling necessary connectivity
- Support scalable network growth without major architectural
changes

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Delivers substantial operational performance advantages for
hybrid architectures.
- Achieve consistently low network latency, which is crucial for
latency-sensitive applications and real-time data processing.

## Implementation guidance

- Assessment of workload requirements and geographical
distribution of resources.
- Select dedicated connection locations that minimize the
physical distance to your on-premises infrastructure while
ensuring adequate port capacity is available.
- Connect to cloud network through preferred PoP.
- Consider latency you get when choosing dedicated connection as
your hybrid connectivity option is dependent on two factors –
the distance between your data center and the dedicated
connection location.

## Resources

- [AWS direct connect locations](https://aws.amazon.com/directconnect/locations/)
- [Point
of presence](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/points-of-presence.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp02.html*

---

# HNPERF02-BP03 Choose the right termination endpoint in the cloud

When establishing cloud connectivity through Points of Presence
(PoPs), organizations carefully choose their network termination
endpoints. There are options available to connect to directly to one
cloud network or through transit cloud constructs for multiple cloud
networks. Each option offers different benefits in terms of cost,
performance, scalability, and management complexity.

**Desired outcome:**

- Optimal network connectivity between on-premises environments
and cloud resources by selecting the most appropriate
termination endpoint.
- Maintain flexibility for future network expansion, ensuring
consistent performance, and managing costs effectively.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Optimized network performance and reduced latency
- Multi-region connectivity through a single connection, reducing
complexity and costs.
- Cost-effective connectivity based on actual requirements
- Simplified network management and operations
- Enhanced network security through proper isolation
- Flexible architecture that supports business growth

## Implementation guidance

- Assess your current and future network requirements, including
geographic distribution, bandwidth needs, and application
latency requirements.
- Use direct connectivity to single cloud network connectivity
to avoid additional cloud transit costs, For example, you can
use Direct Connect private VIF to connect directly to VPC.
- Use cloud transit connectivity to connect to multiple cloud
networks. For example, you can use Direct Connect transit VIF
to connect to Transit Gateway for VPCs in the same region, or
Cloud WAN core network for VPCs in multiple regions.

## Resources

- [Building
a Scalable and Secure Multi-VPC AWS Network
Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/direct-connect.html)
- [Simplify
global hybrid connectivity with AWS Cloud WAN and AWS Direct Connect integration](https://aws.amazon.com/blogs/networking-and-content-delivery/simplify-global-hybrid-connectivity-with-aws-cloud-wan-and-aws-direct-connect-integration/)
- [Transit
gateway attachments to a Direct Connect gateway in AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-dcg-attachments.html)
- [Network-to-Amazon VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp03.html*

---

# HNPERF02-BP04 Select the most appropriate region for your workloads

Selecting the optimal region for your workloads in a hybrid
networking environment requires careful consideration of latency,
data residency requirements, and connectivity options to your
on-premises infrastructure. Choose regions geographically proximate
to your physical data centers and end users to minimize network
latency while ensuring compliance with data sovereignty regulations
specific to your industry. The region selection will ultimately
balance performance needs with compliance requirements and cost
considerations for your hybrid architecture

**Desired outcome:**

- Achieve optimal workload performance by strategically placing
cloud infrastructure closer to end-users and on-premises
resources.
- Ensures minimal latency for latency-sensitive applications while
maintaining secure and reliable connectivity between your data
center and Cloud resources.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Single-digit millisecond latency for latency-sensitive
applications like media rendering, real-time gaming, virtual
desktop solutions or any other latency sensitive applications.
- Maintain data residency requirements while leveraging services
closer to their physical location.

## Implementation guidance

- Identify workloads that require ultra-low latency or local
data processing.
- Select the infrastructure such as AWS local zones which are
closer to your end users to run latency-sensitive
applications.
- Implement dedicated connection such as Direct Connect with a
private virtual interface through Direct Connect gateway for
optimal performance.
- Track the application and network performance through
monitoring solutions like Amazon CloudWatch

## Resources

- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
- [Extend
a VPC to a Local Zone, Wavelength Zone, or Outpost](https://docs.aws.amazon.com/vpc/latest/userguide/Extend_VPCs.html)
- [AWS Direct Connect and AWS Local Zones interoperability
patterns](https://aws.amazon.com/blogs/networking-and-content-delivery/aws-direct-connect-and-aws-local-zones-interoperability-patterns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp04.html*

---

# HNPERF02-BP05 Plan for bandwidth scaling

High-speed dedicated connections can offer bandwidth up to hundreds
of gigabits per second. LAG enables bundling multiple physical
connections to increase total available bandwidth. Additionally,
implementing load balancing across multiple connections using ECMP
routing provides enhanced bandwidth scaling and improved
reliability. For virtual private network implementations, similar
scaling can be achieved by establishing multiple VPN connections and
utilizing ECMP to distribute traffic effectively across these paths.
Understanding these scaling options and their appropriate use cases
is crucial for designing network architectures that can grow with
business demands while maintaining performance and reliability.

**Desired outcome:**

- Achieve optimal network performance and capacity that meets
growing business demands.
- Scalable network infrastructure capable of increasing traffic
volumes

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables strategic bandwidth scaling decisions based on actual
business needs while optimizing costs.
- Provides flexibility to adjust network capacity through various
technical approaches as requirements evolve.
- Load balancing across multiple connections using BGP ECMP,
ensuring optimal traffic distribution.

## Implementation guidance

- Assess current and projected bandwidth requirements,
considering both peak usage patterns and growth trajectories.
- Evaluate infrastructure limitations and compatibility at both
connection endpoints, including port speeds, hardware
capabilities, and routing protocol support.
- Design for operational efficiency with centralized management,
monitoring, and clear maintenance procedures.
- Consider cost implications and geographical requirements when
choosing between scaling approaches, such as dedicated
connections vs IPSec VPNs.

## Resources

- [AWS Direct Connect link aggregation groups (LAGs)](https://docs.aws.amazon.com/directconnect/latest/UserGuide/lags.html)
- [AWS Direct Connect routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html)
- [Active/Active
and Active/Passive Configurations in AWS Direct Connect](https://docs.aws.amazon.com/architecture-diagrams/latest/active-active-and-active-passive-configurations-in-aws-direct-connect/active-active-and-active-passive-configurations-in-aws-direct-connect.html)
- [Scaling
your VPN throughput using Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf02-bp05.html*

---
