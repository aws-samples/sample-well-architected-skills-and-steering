# TELCOCOST03 — Data transfer

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# TELCOCOST03-BP01 Use edge-zones and services to implement cloud workloads made up of containers and microservices

Telecom companies can take advantage of the cloud's ability to replicate resources across
Availability Zones (AZs) within the same Region to reduce data transfer costs. When launching
infrastructure, telecoms should distribute workloads across multiple Availability Zones but use transit
gateways to interconnect them. This allows for high availability without paying for data
transfer between Availability Zones, since this is free.

**Desired outcome:**

- Reduce data transfer costs by minimizing traffic between regional and edge locations.
- Improve application performance and user experience by serving content from the
network edge.
- Achieve high availability and fault tolerance through distributed,
microservices-based architectures.

**Common anti-patterns:**

- Monolithic application architectures with centralized data and processing.
- Lack of edge computing capabilities to bring services closer to users.
- Inefficient communication patterns between distributed components, leading to high
data transfer costs.

**Benefits of establishing this best practice:**

- Significant reduction in data transfer costs by utilizing edge locations and private
connectivity.
- Enhanced application performance and responsiveness through edge-based processing and
content delivery.
- Improved resilience and fault tolerance through a distributed, microservices-based
design.
- Increased agility in scaling and deploying new features and services.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Adopting a cloud-based, microservices-based architecture and using edge computing
capabilities can be highly effective in optimizing data transfer costs for your telco
workloads. By distributing your application components across multiple Availability Zones
and edge locations, you can reduce the need for data to traverse long distances across the
network, thereby minimizing data transfer charges.

AWS services like Amazon ECS, Amazon EKS, AWS PrivateLink, and AWS Global Accelerator
can assist you to implement this approach. By using these services, you can deploy your
containerized microservices in a distributed manner, use private connectivity between
them to avoid public data transfers, and route user traffic to the closest edge location,
further reducing data transfer costs.

### Implementation steps

- Design your application architecture using a microservices approach with
containers.
- Deploy your containerized microservices across multiple Availability Zones within
an AWS Region using Amazon ECS or Amazon EKS.
- Use AWS PrivateLink to enable private connectivity between your
microservices without incurring data transfer costs.
- Use AWS Global Accelerator to route user traffic to the closest edge location,
minimizing latency and data transfer costs.
- Implement service discovery using AWS Cloud Map to enable efficient communication
between microservices.
- Monitor your application's traffic patterns and adjust your edge and regional
deployment strategy to optimize data transfer costs.

## Resources

**Key AWS services:**

- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon EKS](https://aws.amazon.com/pm/eks/)
- [AWS PrivateLink](https://aws.amazon.com/privatelink/)
- [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)
- [AWS Cloud Map](https://aws.amazon.com/cloud-map/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost03-bp01.html*

---
