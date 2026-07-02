# SCPERF04 — Network architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# SCPERF04-BP01 Use performance requirements to drive the selection of network components and architecture

Bring the hosted solution closer to your users' Region to provide
a better user experience and make the data safer while hosted or
in transit.

**Desired outcome:** Better user
experience and safer data while at rest or in transit.

**Benefits of establishing this best
practice:** Secured data while hosted or in-transit, and
low latency by using Amazon backbone network and infrastructure.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Use AWS Direct Connect to provide the shortest and most reliable
path to AWS resources for components hosted outside of AWS. Use
Amazon CloudFront to cache static content closer to use cases,
and AWS Global Accelerator to route connections to the closest
possible source, using the AWS backbone network and bringing
your solutions closer to industries, users, and data. When using
multiple AWS Regions, use Route 53 latency-based routing to
serve requests from the AWS Region with the lowest latency.

### Implementation steps

- Analyze network performance requirements and identify
optimal AWS regions based on user and supplier locations.
- Implement AWS Direct Connect for dedicated, high-bandwidth
connections between on-premises supply chain systems and
AWS.
- Deploy Amazon CloudFront to cache frequently accessed
content and reduce latency for global supply chain users.
- Configure AWS Global Accelerator to optimize network paths
and improve application performance for distributed supply
chain operations.
- Implement Route 53 latency-based routing to automatically
direct traffic to the best-performing AWS region.
- Monitor network performance metrics and optimize routing
configurations to maintain optimal user experience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf04-bp01.html*

---
