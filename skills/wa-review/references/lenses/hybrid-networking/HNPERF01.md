# HNPERF01 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# HNPERF01-BP01 Determine and define your performance requirements using bandwidth, latency and jitter values.

Before you design the best performing architecture, define what
performance means for you and the parameters involved. Typically,
performance metrics are based around bandwidth (rate of data
transfer), latency (round trip time for a network packet to travel
form source to destination), and jitter (variation in latency).
Start by estimating the bandwidth and latency requirements of your
hybrid networking applications.  Match these estimates with the
options available from cloud providers such as dedicated connection
vs internet-based connection to determine which technology you
should choose, and the appropriate configuration.

**Desired outcome:**

- Establish clear, quantifiable performance requirements that
guide the selection of hybrid networking services.
- Provide seamless user experiences and efficient data transfer
between on-premises and cloud environments.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Make informed decisions about networking technology selection
and ensure appropriate resource allocation.
- Improve application performance, enhanced user experience, and
more efficient use of networking resources.

## Implementation guidance

- Consider leverage existing monitoring systems to gather
detailed performance data and engage stakeholders to define
performance expectations.
- Consider both average and peak performance needs
- Document specific bandwidth, latency, and jitter requirements
for each workload and map these requirements to available
cloud networking options.

## Resources

- [Example
Corp. Automotive use case](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/example-corp.-automotive-use-case.html)
- [Network
to Amazon VPC Connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf01-bp01..html*

---

# HNPERF01-BP02 Identify what applications and types of data will be transmitted over the network

Applications can have their own bandwidth considerations. Some
applications might require deterministic performance over a
high-bandwidth connection, while others can require both
deterministic performance and high bandwidth. An application may
need specific configuration to use multiple traffic flows in
parallel if it is hitting per traffic flow bandwidth limits,
allowing it to use more of the connection's bandwidth.

**Desired outcome:**

- Comprehensive understanding of application network requirements
and data transfer patterns across the hybrid infrastructure.
- Enables proper sizing of network connections, appropriate
selection of connectivity options.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Optimize network performance for different application types and
cost-effective selection of connectivity options
- Right-size network infrastructure, prevent bottlenecks, and
ensure smooth operations during varying workload conditions.

## Implementation guidance

- Inventory of applications that will utilize the hybrid
network, categorizing them based on their performance
requirements and criticality.
- Analyze application's bandwidth needs, sensitivity to latency,
and data transfer patterns.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnperf01-bp02.html*

---
