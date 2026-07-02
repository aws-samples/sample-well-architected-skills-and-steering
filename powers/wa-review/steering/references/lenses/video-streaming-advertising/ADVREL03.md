# ADVREL03 — Design for single- and Multi-Region deployments

**Pillar**: Reliability  
**Best Practices**: 4

---

# ADVREL03-BP01 Use a full Regional deployment for compute resources through Auto Scaling groups and compute container orchestrators

Deploy compute resources across multiple Availability Zones (AZs) and
Regions to enhance application resilience. Implement zone-aware
architectures to optimize performance and manage costs, and focus
on intra-AZ communication and load balancing configurations.

## Implementation guidance

Increase resiliency of real-time advertising applications by
distributing resources across multiple Availability Zones or
Regions, but maintain awareness of cross-AZ and cross-Region
data transfer costs. When you use a full Regional deployment,
implement zone-aware architectures within each Region to
optimize performance and costs. When distributing resources
across multiple Availability Zones for resilience, implement
logic to prefer intra-AZ communication, when possible, and use
features like AZ-aware load balancing to minimize cross-AZ
traffic. By being zone-aware, companies can reduce costs and
improve performance even when they need to operate in multiple
Regions.

## Key AWS services

- [Amazon EC2 Auto Scaling](https://aws.amazon.com/autoscaling/) groups can be configured
to span multiple AZs
- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) clusters
can also be deployed across multiple AZs

## Resources

- [Regions
and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [Distribute
instances across Availability Zones](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html#arch-AutoScalingMultiAZ)
- [EC2
Instance Meta-Data Retrieval](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)
- [Creating
Kubernetes Auto Scaling Groups for Multiple Availability Zones | Containers](https://aws.amazon.com/blogs/containers/amazon-eks-cluster-multi-zone-auto-scaling-groups/index.html)
- [Add
an Availability Zone - Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-az-console.html)
- [Simplify
node lifecycle with managed node groups - Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel03-bp01.html*

---

# ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements

Select AWS Regions based on compliance and disaster recovery
needs. It emphasizes the importance of understanding data
jurisdiction requirements, particularly for advertising systems,
and explains how regional choices impact both regulatory
compliance (like GDPR) and system redundancy.

## Implementation guidance

Depending on the resiliency design of your advertising system,
some components may reside in a different Region for redundancy
purposes. Consider compliance needs for your in-transit and at-rest data.

## Key AWS services

- [AWS Control Tower](https://aws.amazon.com/controltower/) provides Region-deny
capabilities
- [AWS Managed Microsoft AD](https://aws.amazon.com/directoryservice/) supports multi-Region
deployment, allowing AD-aware applications and AWS services
to connect to the local instances of the global directory
- [AWS KMS](https://aws.amazon.com/kms/) allows you to replicate multi-Region
keys into other Regions
- AWS services like
[Amazon S3](https://aws.amazon.com/s3/) and

[Amazon RDS](https://aws.amazon.com/rds/) are designed to be resilient by
spreading requests and data across multiple

[Availability
Zones within a Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). However, for
additional redundancy, you can deploy these services across
multiple Regions to achieve isolation and avoid correlated
failures

## Resources

- [Accelerate
your multi-region strategy with Amazon DynamoDB: Part 1](https://aws.amazon.com/blogs/database/part-1-accelerate-your-multi-region-strategy-with-amazon-dynamodb/)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Understand
resiliency patterns and trade-offs to architect efficiently in the cloud](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/)
- [Deny
services and operations for AWS Regions of your choice with AWS Control Tower](https://aws.amazon.com/about-aws/whats-new/2021/11/deny-services-operations-aws-regions-control-tower/index.html)
- [Design
consideration for AWS Managed Microsoft Active Directory - Active Directory Domain Services on AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/design-consideration-for-aws-managed-microsoft-active-directory.html)
- [Creating
multi-Region replica keys - AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-replicate.html)
- [Regional
services - AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/regional-services.html)
- [Navigating
GDPR Compliance on AWS](https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel03-bp02.html*

---

# ADVREL03-BP03 Configure databases to span across multiple Availability Zones

Explore database configuration strategies for reliability and
disaster recovery, such as periodic snapshots to warm standby
solutions. Evaluate trade-offs between single-AZ and multi-AZ
deployments, costs considerations, and specific recovery time
objectives (RTO).

## Implementation guidance

Carefully consider the trade-offs between disaster recovery
strategies when configuring databases in multi-AZ and single-AZ
deployments. While multi-AZ deployments offer high availability,
they can incur significant cross-AZ data transfer costs.

For cost-sensitive workloads, consider implementing a single-AZ
database cluster with the following resilience strategies:

- **Periodic snapshots:**
Implement frequent automated snapshots of your database.
This approach provides point-in-time recovery capabilities
with a relatively low RTO, typically in the range of 15-60
minutes, depending on the database size and recovery
process.
- **Read replicas:** Deploy
read replicas in a different Availability Zone. While this
incurs some cross-AZ data transfer costs, it's generally
less expensive than a full multi-AZ deployment. In case of a
primary Availability Zone failure, promote the read replica
to become the new primary. This can reduce RTO to between
five and 15 minutes.
- **Cold standby:** Maintain a
stopped database instance in another Availability Zone, and
periodically update it with snapshots. This approach
balances cost and recovery time, with an RTO of
approximately 10-30 minutes.

For mission-critical applications, where minimal downtime is
essential, consider:

- **Warm standby:** Keep an
active, scaled-down secondary database in another
Availability Zone continuously updated using asynchronous
replication. This approach offers a lower RTO (between one
and five minutes), but at a higher cost than cold standby.

Choose the strategy that best aligns with your specific RTO
requirements and budget constraints. Implement and regularly
test your chosen disaster recovery process to verify that it
meets your RTO targets.

For AdTech customers who require multi-region deployment for
global resilience, use services like Amazon Aurora Global
Database or Amazon DynamoDB global tables. These services
provide Region-wide resilience with minimal impact on
performance and manageable costs.

Regularly review and optimize your database architecture as your
workload and requirements evolve. Always weigh the costs of
potential downtime against the ongoing expenses of more
resilient configurations.

## Key AWS services

- [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/)
provides a Multi-AZ deployment option
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon Aurora](https://aws.amazon.com/rds/aurora/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)

## Resources

- [Amazon RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/)
- [Protect
critical workload with Pod Disruption Budgets](https://docs.aws.amazon.com/eks/latest/best-practices/application.html#_recommendations_3)
- [Using
Amazon Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)
- [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/)
- [What
is Amazon Relational Database Service (Amazon RDS)?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [Multi-AZ
DB instance deployments for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel03-bp03.html*

---

# ADVREL03-BP04 Reserve appropriate capacity of services in the supported Regions

Manage service capacity across multiple Regions. Perform regular
load testing at five times your baseline RTB traffic levels to
validate capacity requirements. Validate that appropriate
reservations are made to handle normal operations, peak loads, and
potential disruptions.

## Implementation guidance

If your application is designed to scale out over multiple
Regions, service could be disrupted by temporary resource
constraints or other issues impacting a single Availability Zone
or Region. Regularly perform load tests with at least five times
the baseline of RTB traffic expectations to validate that
allocated capacity meets low water mark, mean, and peak capacity
projections. Based on the results of your load tests, make
capacity reservation.

## Key AWS services

- [Amazon Route 53](https://aws.amazon.com/route53/)
- [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/)
- [Amazon S3](https://aws.amazon.com/s3/)

## Resources

- [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
- [Quotas
and constraints for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html)
- [What
to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/)
- [Creating
a Multi-Region Application with AWS Services – Part 1, Compute, Networking, and Security](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-1-compute-and-security/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel03-bp04.html*

---
