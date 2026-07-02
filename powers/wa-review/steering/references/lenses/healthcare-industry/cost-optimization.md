# Cost optimization

**Pages**: 7

---

# Practice cloud financial management

There are no cost optimization best practices for practicing cloud financial management specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/practice-cloud-financial-management.html*

---

# Data retention

HCL_COST1. How do you define and
enforce data retention policies?

**Determine applicable
regulatory frameworks and controls as it pertains to data
retention**

Healthcare organizations may be subject to regulatory and
company requirements dictating how long they must store both
health data as well as logs detailing access to that data. Over
time, storage requirements can reach petabyte scale for an
individual organization. New imaging modalities, such as digital
pathology, have the potential to push data volumes even higher.
Developing strategies for data retention is imperative to
maintain compliance while minimizing cost.

Healthcare organizations should establish a data retention
policy identifying the types and duration that data should be
retained in accordance with internal and external requirements.

**Implement data lifecycle
policies**

As healthcare data ages, its access frequency declines.
Implement lifecycle policies that transition
infrequently-accessed data to lower-cost storage tiers. When
designing your policies for each type of data, be sure to factor
the size of the data, the frequency of access, and expectations
for retrieval time; these are the three predominant
cost-drivers. For example, use Amazon S3 Lifecycle
configurations to archive infrequently accessed data after some
period of time, automatically reducing storage costs.
Alternatively, use Amazon S3 Intelligent-Tiering to shift the
archival policies to focus on time of last access instead of
time the object has been in Amazon S3.

**Centralize automated
policy enforcement**

Adopting infrastructure as code, as discussed in the operational
excellence pillar, enables you to define and test your data
retention policies before they make it into production. For
example, if regulatory requirements specify that you must retain
certain medical images for 10 years, you can verify that no Amazon S3
lifecycle policy expires an object before that time.
Additionally, consider AWS Backup for centralized backup
management, which enables you to back up application data in a
consistent and compliant manner.

**Validate lifecycle
policies are enforced**

Because the cloud is API-driven, you can monitor changes to your
environment as described in the operational excellence and
security tiers. Set up alerts for when an API action alters a
data retention policy so you can quickly review the change to
make sure it was authorized and operating correctly. If using
AWS Backup, use AWS Backup Audit Manager to automatically detect
when your AWS Backup policies violate your data retention
requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/data-retention.html*

---

# Cost-effective resources

There are no cost optimization best practices for cost-effective resources specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/cost-effective-resources.html*

---

# Manage demand and supply resources

There are no cost optimization best practices for managing demand and supplying resources specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/manage-demand-and-supply-resources.html*

---

# Optimize over time

There are no cost optimization best practices for optimizing over time specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/optimize-over-time.html*

---

# Key AWS services

The key AWS feature that supports cost optimization is cost
allocation tags, which help you to understand the costs of a
system. The following services and features are important in the
four areas of cost optimization:

**Cost-effective resources:**

- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)

**Expenditure and usage awareness:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) – For monitoring access frequency
statistics for objects stored on Amazon S3, like medical
images.
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/key-aws-services-4.html*

---

# Resources

Refer to the following resources to learn more about our best practices related to cost optimization.

**Videos**

- [Simplify Your Data Lifecycle
and Optimize Storage Costs With Amazon S3 Lifecycle](https://www.youtube.com/watch?v=53eHNSpaMJI)
- [Simplify Backup Auditing and
Compliance with AWS Backup Audit Manager - AWS Online Tech Talk](https://www.youtube.com/watch?v=gZron55So0A)

**Documentation and blogs**

- [How to manage retention periods in bulk using Amazon S3 Batch Operations](https://aws.amazon.com/blogs/storage/how-to-manage-retention-periods-in-bulk-using-amazon-s3-batch-operations/)
- [Amazon S3 cost optimization for predictable and dynamic access patterns](https://aws.amazon.com/blogs/storage/amazon-s3-cost-optimization-for-predictable-and-dynamic-access-patterns/)
- [Amazon S3: Managing your
storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Audit backups and
create reports with AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html)

**Whitepapers**

- [Storage
Best Practices for Data and Analytics Applications](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lake-aws.html)
- [Data
Classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/resources-4.html*

---
