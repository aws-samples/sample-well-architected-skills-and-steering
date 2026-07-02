# TELCOCOST06 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# TELCOCOST06-BP01 Implement load-balancing techniques to achieve better utilization of hybrid network resources

Establish a comprehensive traffic classification system that identifies different types of
network traffic (for example, real-time communications, bulk data transfers, best-effort
traffic). Monitor the utilization of your hybrid network connections in real-time. Utilize
load-balancing mechanisms to distribute network traffic across multiple hybrid network
connections, both on-premises and in the cloud.

**Desired outcome:**

- Optimize the utilization of networking resources across your hybrid infrastructure.
- Verify critical network traffic is prioritized and routed efficiently.
- Improve overall network performance and cost-effectiveness.

**Common anti-patterns:**

- Static routing configurations that do not adapt to changing network conditions.
- Lack of visibility into network traffic patterns and resource utilization.
- Inability to dynamically adjust traffic flows based on real-time performance metrics.

**Benefits of establishing this best practice:**

- Improved networking resource utilization and cost-effectiveness.
- Enhanced performance and reliability for latency-sensitive network traffic.
- Increased agility in managing network capacity and traffic flows.
- Better alignment of network capabilities with evolving business requirements.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Implementing effective load-balancing techniques across your hybrid networking
infrastructure is crucial for optimizing resource utilization and cost-effectiveness. By
leveraging advanced load-balancing capabilities, you can intelligently route network traffic
based on real-time conditions, prioritize critical applications and services, and verify
efficient use of your networking resources.

AWS provides various load-balancing services, such as Network Load Balancer and Application Load Balancer,
that can assist you to distribute traffic across your hybrid network connections, both
on-premises and in the cloud. These load balancers can leverage dynamic routing algorithms to
route traffic based on performance metrics like latency, jitter, and packet loss, verifying
that traffic is directed to the most optimal path.

Additionally, services like AWS Global Accelerator can be used to optimize the routing of user's
voice traffic to the closest available network endpoint, further reducing data transfer costs
and improving the user experience.

### Implementation steps

- Establish a comprehensive traffic classification system that identifies different
types of network traffic (for example, real-time communications, bulk data transfers,
best-effort traffic).
- Deploy Network Load Balancer or Application Load Balancer to distribute voice traffic across your
hybrid network connections, both on-premises and in the cloud.
- Configure the load balancers to use dynamic routing based on network metrics,
such as latency, jitter, and packet loss, to intelligently route traffic.
- Leverage AWS Global Accelerator to optimize the routing of user traffic to the closest
available network endpoint, reducing data transfer costs.
- Monitor the utilization of your hybrid network connections in real-time using
Amazon CloudWatch and set up alarms to trigger load balancing adjustments.
- Continuously review and refine your load balancing policies to verify optimal
utilization of your hybrid network resources.

Resources

**Key AWS services:**

- [AWS Network
Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/)
- [AWS
Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
- [AWS](https://aws.amazon.com/global-accelerator/) Global Accelerator
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost06-bp01.html*

---
