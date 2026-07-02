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
