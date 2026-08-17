# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 6

---

# TELCOCOST01 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# TELCOCOST01-BP01 Implement attribution of cost to each telco domain hosted on the AWS (access, core, edge, OSS, and BSS)

Telcos with workloads running on AWS can take advantage of AWS' detailed cost and usage
reporting to attribute costs to each of their domains (like access, core, edge, OSS, and BSS). By
tagging resources appropriately, costs can be allocated to each domain.

**Desired outcome:**

- Gain visibility into the cost breakdown of your telco workload across different
domains.
- Identify high-cost areas and make informed decisions to optimize spending.
- Improve cost transparency and accountability across your telco organization.

**Common anti-patterns:**

- Lack of cost tagging and tracking for resources, leading to unclear cost attribution.
- Siloed cost management, with different teams responsible for distinct domains.
- Reliance on high-level consolidated billing reports without granular cost breakdowns.

**Benefits of establishing this best practice:**

- Enables data-driven cost optimization decisions.
- Improves cross-team collaboration and accountability for cost management.
- Facilitates chargeback or show back models for internal cost allocation.
- Supports regulatory adherence and auditing requirements.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Accurately attributing costs to different telco domains is essential for effective cost
optimization. By using AWS's detailed cost and usage reporting capabilities, you can
gain visibility into the specific costs associated with each of your telco domains. This information can assist you to identify areas of high
spending and make informed decisions to optimize costs.

### Implementation steps

- Verify you have enabled detailed billing and cost allocation reports in your AWS account.
- Create AWS Cost and Usage tags for your resources to categorize costs by domain.
- Apply the appropriate tags to your AWS resources, such as EC2 instances, S3
buckets, and Lambda functions.
- Configure AWS Cost Explorer to analyze and visualize your costs by the tagged
domains.
- Set up AWS Budgets and alerts to monitor and receive notifications on cost trends
for each domain.
- Regularly review the cost allocation reports and optimize costs in high-spend
domains.

## Resources

**Key AWS services:**

- [AWS Cost and Usage Reports](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost01-bp01.html*

---

# TELCOCOST02 — Cost-effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# TELCOCOST02-BP01 Implement dynamic CNF sizing and scaling strategies based on actual subscriber demands and usage patterns

In traditional on-premises environments, CNF infrastructure is typically sized for peak
capacity expected over the hardware lifetime. To optimize costs in cloud environments,
organizations should implement dynamic sizing strategies that align infrastructure capacity with
actual subscriber demands. This includes utilizing cloud-based auto scaling capabilities,
implementing rightsizing based on usage patterns, and designing CNF architectures that support
horizontal scaling. The approach should balance performance requirements with cost efficiency
while maintaining the ability to handle growth in subscriber demand through elastic
infrastructure scaling.

**Desired outcome:**

- Optimize the cost of your cloud-based network functions (CNFs) by right-sizing
resources based on actual usage.
- Verify CNF performance meets service-level objectives while minimizing
over-provisioning.
- Achieve cost savings by dynamically scaling CNF resources up and down in response to
changing demand.

**Common anti-patterns:**

- Static, one-size-fits-all provisioning of CNF resources without considering variable
demand.
- Over-provisioning of CNF resources to handle peak capacity, leading to excess costs
during off-peak periods.
- Lack of visibility into CNF resource utilization and performance, hindering effective
scaling decisions.

**Benefits of establishing this best practice:**

- Significant cost savings by aligning CNF resources with actual subscriber needs.
- Improved CNF performance and reliability by adapting to changing demand patterns.
- Enhanced operational efficiency through automated scaling and resource management.
- Increased agility in responding to growth or seasonal fluctuations in subscriber base.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Implementing dynamic sizing and scaling strategies for your cloud-based Network Functions
(CNFs) is crucial for optimizing costs in a cloud-based telco environment. Unlike traditional
on-premises deployments, the cloud provides the opportunity to right-size your CNF resources
based on actual subscriber demands and usage patterns, rather than provisioning peak capacity.

By using cloud-based auto scaling capabilities, you can dynamically adjust the
resources allocated to your CNFs, verifying performance requirements are met while minimizing
over-provisioning and associated costs. This approach allows you to scale resources up and
down in response to changes in subscriber demand, improving cost-efficiency without
compromising the user experience.

### Implementation steps

- Profile the performance and resource utilization characteristics of your cloud-based network functions (CNFs).
- Use AWS Auto Scaling to automatically scale CNF resources up and down based on
real-time metrics like CPU, memory, and network utilization.
- Configure Amazon CloudWatch alarms to trigger auto scaling actions when thresholds are
breached.
- Use Amazon EC2 Auto Scaling groups with a dynamic target tracking scaling policy to maintain
optimal performance at the lowest cost.
- Analyze historical usage patterns and seasonality to set appropriate scaling
thresholds and policies.
- Continuously monitor and refine your autoscaling configurations to verify they
adapt to changing traffic patterns.

## Resources

**Key AWS services:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost02-bp01.html*

---

# TELCOCOST02-BP02 Choose the most efficient compute resource for your Network Function

When implementing cloud-based network functions (CNFs), it is important to benchmark your
applications on different compute types to determine the optimal balance of performance and
cost-efficiency. CNFs have diverse compute requirements, so gravitating to the lowest cost
option may result in poor performance. Older compute architectures and hardware can hamper
efficiency and drive-up expenses over time.

**Desired outcome:**

- Identify the most cost-effective compute resources that meet the performance
requirements of your cloud-based network functions (CNFs).
- Optimize the balance between cost and performance for your CNF workloads.
- Avoid over-provisioning or under-provisioning of compute resources, which can lead to
increased costs.

**Common anti-patterns:**

- Selecting compute resources solely based on the lowest cost, without considering
performance requirements.
- Relying on outdated compute architectures and hardware that are less efficient and
cost-effective.
- Lack of benchmarking and profiling of CNF workloads on different compute options.

**Benefits of establishing this best practice:**

- Significant cost savings by selecting the most optimal compute resources for your CNFs.
- Improved CNF performance and reliability by matching compute capabilities to workload
needs.
- Enhanced operational efficiency by right-sizing compute resources to avoid
over-provisioning.
- Increased agility in responding to changing compute requirements for your CNF
workloads.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

When implementing cloud-based network functions (CNFs), it is crucial to carefully
evaluate the compute resource options to strike the right balance between cost and
performance. CNFs often have diverse compute requirements, and simply selecting the
lowest-cost compute option may result in poor performance and sub-optimal outcomes.

By benchmarking your CNF applications on different compute types, you can identify the
most efficient resources that meet your performance needs. This may involve evaluating various
AWS compute services, such as Amazon EC2 instances with different processor architectures, memory
configurations, and storage options. Older compute architectures and hardware can also hamper
efficiency and drive-up expenses over time, so it is important to consider the long-term costs
and benefits of your compute choices.

The goal is to optimize the cost-performance tradeoff for your CNF workloads, verifying
you are not over-provisioning or under-provisioning compute resources, which can lead to
increased costs.

### Implementation steps

- Profile the performance and resource utilization characteristics of your
cloud-based network functions (CNFs).
- Benchmark your CNF applications on a variety of AWS compute instances, including
different processor architectures, memory configurations, and storage options.
- Analyze the performance and cost data to identify the most efficient compute
resources that meet your CNF's requirements.
- Consider the long-term implications of your compute choices, evaluating factors
like energy efficiency, hardware lifecycle, and future performance trends.
- Implement mechanisms to dynamically adjust the compute resources allocated to your
CNFs based on changing demands and workload characteristics.
- Continuously monitor and optimize your CNF compute resource allocations to verify
cost-effectiveness while maintaining performance.

## Resources

**Key AWS services:**

- [Amazon EC2](https://aws.amazon.com/pm/ec2/)
- [AWS Graviton Processor](https://aws.amazon.com/ec2/graviton/)
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost02-bp02.html*

---

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

# TELCOCOST04 — Data storage

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# TELCOCOST04-BP01 Choose the appropriate type of storage for network functions backups, metrics, KPIs and the event records to reduce costs

Telecom companies generate and store massive amounts of data to support their business and
customer operations. However, data is accessed or needed at various frequencies. By aligning
storage choices with data access needs and lifecycles, Telecoms can significantly reduce their
storage costs. For actively accessed data that needs high performance, flash storage or cache
are good options despite their higher costs. For medium-term data that is accessed occasionally,
lower-cost options like object storage, SAN or NAS storage are suitable. For long-term archive
data with infrequent access, cold storage options like tape or cloud archival storage are the
most cost-efficient.

**Desired outcome:**

- Align storage choices with the access patterns and retention requirements of different
data types.
- Achieve cost savings by utilizing the most cost-effective storage options for each data
category.
- Verify appropriate performance and durability characteristics for the various data
workloads.

**Common anti-patterns:**

- One-size-fits-all storage approach, with the same storage solution used for each data
type.
- Overreliance on high-cost storage options for data that does not require frequent
access.
- Lack of visibility and control over storage usage and costs across the organization.

**Benefits of establishing this best practice:**

- Significant cost savings by optimizing storage costs based on data access patterns.
- Improved storage efficiency and resource utilization.
- Enhanced data management through appropriate retention and tiering strategies.
- Increased agility in responding to changing storage requirements.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Telecom companies generate and store large volumes of data to support their business and
customer operations. However, data is accessed or needed at different frequencies. By aligning
storage choices with data access needs and lifecycles, telecoms can significantly reduce their
storage costs.

For actively accessed data that needs high performance, flash storage or cache are good
options despite their higher costs. For medium-term data that is accessed occasionally,
lower-cost options like object storage, SAN, or NAS storage are suitable. For long-term
archive data with infrequent access, cold storage options like tape or cloud archival storage
are the most cost-efficient.

### Implementation steps

- Categorize your data based on access frequency, performance requirements, and
retention needs (for example, active, medium-term, and long-term archive).
- For active data that requires high performance, use Amazon EBS Provisioned IOPS SSD
volumes or Amazon EFS.
- For medium-term data that is accessed occasionally, use Amazon S3 Intelligent-Tiering or
Amazon EFS.
- For long-term archive data with infrequent access, use Amazon Glacier or Amazon Glacier Deep
Archive.
- Implement lifecycle policies to automatically transition data between storage tiers
as access patterns change.
- Monitor storage usage and costs and adjust your storage tiering strategy as needed
to optimize costs.

## Resources

**Key AWS services:**

- [Amazon EBS](https://aws.amazon.com/ebs/)
- [Amazon EFS](https://aws.amazon.com/efs/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/)
- [Amazon Glacier Deep Archive](https://aws.amazon.com/s3/storage-classes/glacier/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost04-bp01.html*

---

# TELCOCOST04-BP02 Use ETSI ENI based architectures to implement intelligent network slicing

The European Telecommunications Standards Institute (ETSI) Experiential Networked
Intelligence (ENI) is an architectural framework that defines standards for cognitive network
management and implementation of 5G use cases based on environmental context and user
requirements. It allows Telcos to take advantage of cloud-based technologies like network
slicing, service mesh, and microservices to build more agile and automated networks.

**Desired outcome:**

- Improve network resource utilization and efficiency through dynamic, context-aware
network slicing.
- Enhance the customer experience by automatically allocating network resources based
on user and application requirements.
- Achieve cost savings by right-sizing network capacity to match evolving demands.

**Common anti-patterns:**

- Static, one-size-fits-all network provisioning without considering variable user and
application needs.
- Lack of real-time visibility into network conditions and user/application demands.
- Inability to rapidly adapt network resource allocation in response to changing
requirements.

**Benefits of establishing this best practice:**

- Optimized network resource utilization and efficiency.
- Improved customer experience through tailored network capabilities.
- Reduced network operating costs by aligning capacity with actual demands.
- Increased network agility and responsiveness to evolving requirements.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

The European Telecommunications Standards Institute (ETSI) Experiential Networked
Intelligence (ENI) architecture provides a framework for implementing intelligent,
context-aware network slicing. By using the key components of the ENI architecture,
such as the policy management function and the context awareness function, telecoms can
build cloud-based, microservices-based network slicing solutions that dynamically allocate
resources based on user and application needs.

This approach enables telecoms to improve network resource utilization and
cost-effectiveness by right-sizing network capacity to match actual demands, rather than
provisioning for peak requirements. Additionally, the context-aware nature of the ENI
architecture allows the network to automatically adapt to changing conditions, user
behavior, and application requirements, enhancing the overall customer experience.

### Implementation steps

- Familiarize yourself with the ETSI ENI architecture and its key components, such
as the Policy Management Function (PMF) and the Context Awareness Function (CAF).
- Design your network slicing architecture using the ETSI ENI principles, including
the use of microservices, service mesh, and cloud-based technologies.
- Use AWS services like Amazon EKS, AWS App Mesh, and AWS Lambda to implement
the ENI-based network slicing components.
- Develop policies and rules within the PMF to dynamically allocate network
resources based on user and application requirements.
- Use the CAF to gather contextual information about network conditions, user
behavior, and application demands to drive intelligent resource allocation.
- Continuously monitor the performance and cost-effectiveness of your ENI-based
network slicing implementation and adjust as needed.

## Resources

**Key AWS services:**

- [Amazon EKS](https://aws.amazon.com/pm/eks/)
- [AWS App Mesh](https://aws.amazon.com/app-mesh/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost04-bp02.html*

---

# TELCOCOST05 — Interoperability

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# TELCOCOST05-BP01 Explore open interface-based technology like RAN or vRAN to reduce network-related costs

To examine O-RAN in more detail and understand the best practices for O-RAN architectures
on AWS, see [Open Radio Access Network Architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/open-radio-access-network-architecture-on-aws/open-radio-access-network-architecture-on-aws.html).

**Desired outcome:**

- Achieve cost savings through the adoption of open interface-based RAN or vRAN
technologies.
- Increase flexibility and vendor independence in the radio access network.
- Improve scalability and agility in deploying new RAN capabilities.

**Common anti-patterns:**

- Reliance on proprietary, vendor-locked RAN solutions that limit flexibility and
drive-up costs.
- Lack of consideration for open interface-based RAN architectures and their potential
benefits.
- Inability to rapidly adapt the RAN to changing business and technology requirements.

**Benefits of establishing this best practice:**

- Significant cost savings through the adoption of open interface-based RAN/vRAN
technologies.
- Increased flexibility and vendor independence, reducing lock-in and enabling faster
innovation.
- Improved scalability and agility in deploying new RAN capabilities to meet evolving
demands.
- Enhanced ability to use cloud-based technologies and services to manage the RAN.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Open Radio Access Network (O-RAN) is an industry initiative that defines open interface
specifications for the radio access network (RAN). By adopting O-RAN and vRAN architectures,
telecoms can reduce network-related costs and increase flexibility in their RAN
infrastructure.

The O-RAN approach allows telecoms to decouple the different RAN components, such as the
Radio Unit (O-RU), Distributed Unit (O-DU), and Central Unit (O-CU), and use diverse
vendors and cloud-based technologies to build and manage their RAN. This reduces vendor
lock-in and enables faster innovation and adaptation to change requirements.

AWS provides various services and solutions, such as Amazon EC2, AWS Outposts, and AWS Wavelength,
that can support the deployment and management of O-RAN and vRAN components, making it easier for
telecoms to explore and adopt this open interface-based technology.

### Implementation steps

- Review the Open Radio Access Network (O-RAN) architecture and understand its key
components, such as the O-RAN Radio Unit (O-RU), O-RAN Distributed Unit (O-DU), and
O-RAN Central Unit (O-CU).
- Assess the feasibility of adopting an O-RAN and vRAN architecture for your telco
network, considering factors like performance, scalability, and cost-effectiveness.
- Evaluate AWS services and solutions that support the deployment and management of
O-RAN/vRAN components, such as Amazon EC2, AWS Outposts, and AWS Wavelength.
- Pilot an O-RAN and vRAN implementation in your network, focusing on a specific use case
or geographic region to validate the approach.
- Analyze the cost savings and other benefits achieved using open interface-based RAN
technologies.
- Based on the pilot results, develop a roadmap for the wider adoption of O-RAN and vRAN
across your telco network infrastructure.

## Resources

**Key AWS services:**

- [Amazon EC2](https://aws.amazon.com/pm/ec2/)
- [AWS Outposts](https://aws.amazon.com/outposts/)
- [AWS Wavelength](https://aws.amazon.com/wavelength/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost05-bp01.html*

---

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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
