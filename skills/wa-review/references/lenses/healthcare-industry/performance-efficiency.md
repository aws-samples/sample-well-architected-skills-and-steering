# Performance efficiency

**Pages**: 10

---

# Design principles

The following design principles can help you achieve and maintain efficient workloads in the cloud.

- **Democratize advanced technologies**: Make advanced
technology implementation easier for your team by delegating complex tasks to your cloud
vendor. Rather than asking your IT team to learn about hosting and running a new
technology, consider consuming the technology as a service. For example, NoSQL
databases, media transcoding, and machine learning are all technologies that require
specialized expertise. In the cloud, these technologies become services that your team
can consume, allowing your team to focus on product development rather than resource
provisioning and management.
- **Go global in minutes**: Deploying your workload in
multiple AWS Regions around the world allows you to provide lower latency and a better
experience for your customers at minimal cost.
- **Use serverless architectures**: Serverless architectures
remove the need for you to run and maintain physical servers for traditional compute
activities. For example, serverless storage services can act as static websites
(removing the need for web servers) and event services can host code. This removes the
operational burden of managing physical servers, and can lower transactional costs
because managed services operate at cloud scale.
- **Experiment more often**: With virtual and automatable
resources, you can quickly carry out comparative testing using different types of
instances, storage, or configurations.
- **Consider mechanical sympathy**: Use the technology
approach that aligns best with your goals. For example, consider data access patterns
when you select database or storage approaches.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/design-principles3.html*

---

# Performance architecture

HCL_PERF1. How do you encrypt data
while ensuring performance?

**Offload encryption to
hardware**

Certain encryption approaches, such as VPN tunnels or IPsec
meshes, can impact performance when implemented at scale.
Where possible, offload encryption to hardware to maintain
security while improving performance.

The [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) provides hardware components that allow
for easy offloading of encryption services to the hardware.
For example, some instance types use the hardware capabilities
of the Nitro System hardware to encrypt in-transit traffic
between instances with no impact to network performance. This
allows healthcare organizations to enable encryption
in-transit for sensitive healthcare data. Use instance types
that support the Nitro System where possible.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/performance-architecture.html*

---

# Compute selection

HCL_PERF2. How do you select your
compute solution?

**Select compute services
that meet regulatory and performance requirements**

Healthcare requirements for compute are generally consistent
with other industries. Guidance from the
[Well-Architected
Framework Compute Architecture Selection](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/compute-architecture-selection.html) still applies.
Healthcare applications can take advantage of virtual
machines, containers, or serverless technologies.

Healthcare applications should enable encryption in-transit at
one of the OSI layers. Some legacy communication protocols,
such as Minimal Lower Layer Protocol (MLLP) for healthcare
interoperability, may not natively support encryption
in-transit. A common industry solution has been to overlay a
VPN or create an IPsec mesh on top of virtual machines in a
VPC to encrypt sensitive data in transit; however, such
approaches can create performance penalties. Instead, where
possible, use
[Amazon EC2 instances with encryption in-transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html) handled by the
underlying Amazon EC2 Nitro System to reduce any performance
penalties associated with inter-Amazon EC2 communication.

You can get a full list of Amazon EC2 instance types that
support this feature with the following CLI command:

```
`AWS ec2 describe-instance-types –filters
Name=network-info.encryption-in-transit-supported,Values=true
–query “InstanceTypes[*].[InstanceType]” –output text`
```

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/compute-selection.html*

---

# Network architecture

HCL_PERF3. How do you define and
test network performance requirements?

Healthcare requirements for compute are generally consistent
with other industries. Guidance from the
[Well-Architected
Framework Network Architecture Selection](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/network-architecture-selection.html) still applies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/network-architecture.html*

---

# Storage architecture

HCL_PERF4. How do you define and
test storage performance requirements?

Healthcare requirements for compute are generally consistent
with other industries. Guidance from the
[Well-Architected
Framework Storage Architecture Selection](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-storage.html) still applies.

AWS offers storage with extreme durability and performance.
For example, [Amazon S3](https://aws.amazon.com/s3)
provides 99.999999999% (11 nines) of data durability of objects
over a given year.
[Amazon EBS io2](https://aws.amazon.com/ebs/provisioned-iops/) block storage offers not only 99.999%
durability, but up to 500 IOPS per GiB, enabling high
performance and durability for healthcare workloads that
require higher performance, such as transactional databases.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/storage-architecture.html*

---

# Review

There are no performance efficiency best practices for review specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/review.html*

---

# Monitoring

There are no performance efficiency best practices for monitoring specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/monitoring.html*

---

# Trade-offs

There are no performance efficiency best practices for trade-offs specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/trade-offs.html*

---

# Key AWS services

The key AWS service for performance efficiency is Amazon CloudWatch, which monitors your resources and systems, providing
visibility into your overall performance and operational health.
The following services are important in the areas of performance
efficiency:

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)
- [AWS Client VPN](https://aws.amazon.com/vpn/client-vpn/)
- [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/key-aws-services-3.html*

---

# Resources

Refer to the following resources to learn more about our best
practices related to performance efficiency.

**Videos**

- [Powering
next-gen Amazon EC2: Deep dive on the Nitro System](https://www.youtube.com/watch?v=2uc1vaEsPXU)

**Documentation**

- [AWS Well-Architected Framework: Performance Efficiency Pillar:
Performance Architecture Selection](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/performance-architecture-selection.html)
- [Data
protection in Amazon EC2: Encryption in-transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/resources-3.html*

---
