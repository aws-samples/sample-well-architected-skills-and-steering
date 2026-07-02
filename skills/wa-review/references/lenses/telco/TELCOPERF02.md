# TELCOPERF02 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# TELCOPERF02-BP01 Implement containers to achieve optimal performance and resource utilization

Implementing containers in your telco architecture is a crucial step towards achieving
optimal performance and resource utilization. When adopting this approach, it is essential to
carefully consider your instance type and hardware selection. For example, User Plane Function
(UPF) components require specific performance capabilities to handle high data plane throughput,
while Radio Access Network (RAN) elements may benefit from specialized hardware accelerators.

**Desired outcome:**

- Achieve greater agility, scalability, and efficiency in the telco network
infrastructure using containers.
- Optimize resource utilization and manage the compute footprint dynamically to handle
traffic spikes and evolving demands.
- Use advanced container orchestration features to improve the reliability and fault
tolerance of telco workloads.

**Common anti-patterns:**

- Relying solely on traditional virtual machine-based deployments without adopting
containers.
- Failing to consider the specific performance and resource requirements of telco
workloads when implementing containers.
- Lacking the appropriate container orchestration solution and features needed to manage
the scale and complexity of telco networks.

**Benefits of establishing this best practice:**

- Improved performance and throughput for latency-sensitive telco workloads like User
Plane Function (UPF) and Radio Access Network (RAN).
- Better resource utilization and cost optimization through right-sizing and dynamic
scaling of container-based telco components.
- Increased agility and flexibility to deploy, update, and manage telco network functions.
- Enhanced reliability and fault tolerance through container orchestration capabilities.
- Simplified operations and reduced maintenance overhead for the telco infrastructure.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Implementing containers in your telco architecture is a crucial step towards achieving
optimal performance and resource utilization. When adopting this approach, it is essential to
carefully consider your instance type and hardware selection to meet the specific requirements
of telco workloads.

For example, User Plane Function (UPF) components require specific performance
capabilities to handle high data plane throughput, while Radio Access Network (RAN) elements
may benefit from specialized hardware accelerators. Optimizing your compute footprint is
another key aspect of container implementation, involving careful management of resource
allocation to avoid over-provisioning and verify efficient utilization.

Selecting the optimal container control plane and orchestration characteristics is also
crucial for telco workloads. This is particularly important for control plane components,
where factors such as Transactions Per Second (TPS) and session requirements play a
significant role. Choose a container orchestration solution that can handle the scale and
complexity of telco networks, providing features like service mesh for improved communication
between microservices, and robust monitoring and logging capabilities for effective
troubleshooting and performance optimization. By carefully implementing containers with these
considerations in mind, telco operators can achieve greater agility, scalability, and
efficiency in their network infrastructure, leading to improved service quality and reduced
operational costs.

### Implementation steps

- Use Amazon EKS to deploy your telco workloads in a managed Kubernetes environment,
allowing you to take advantage of container-based architectures.
- Select EC2 instance types that are optimized for the performance and resource
requirements of your telco user plane and control plane components, such as high-memory
or compute-optimized instances.
- Integrate AWS Fargate, a serverless compute engine for containers, to manage the
scaling and provisioning of the container infrastructure without the need to manage
underlying EC2 instances.
- Configure AWS App Mesh, a service mesh for microservices, to enhance communication,
observability, and security between the containerized telco components.
- Use Amazon CloudWatch and AWS X-Ray to monitor the performance, resource utilization, and
health of your containerized telco workloads, triggering auto scaling actions as needed.

## Resources

Key AWS services:

- [Amazon EKS (Elastic Kubernetes Service)](https://aws.amazon.com/pm/eks/)
- [AWS Fargate](https://aws.amazon.com/fargate/)
- [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/)
- [AWS App Mesh](https://aws.amazon.com/app-mesh/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoperf02-bp01.html*

---
