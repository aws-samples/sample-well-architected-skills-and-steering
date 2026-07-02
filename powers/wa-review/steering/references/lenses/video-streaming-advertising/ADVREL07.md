# ADVREL07 — Failure and recovery

**Pillar**: Reliability  
**Best Practices**: 3

---

# ADVREL07-BP01 Design your workloads to withstand failures of individual components, such as compute instances, queues, databases, and caches

Build building resilient advertising systems by identifying
critical components, and implement fault tolerance through
cell-based architectures and distributed resources across
Availability Zones.

## Implementation guidance

Determine which components of your workload are in a critical
path to maintain operations for real-time bidding, ad serving,
and other crucial functions. Identify AWS services that provide
built-in fault tolerance mechanisms which are within your
workload's response time, RTO, and RPO targets. Use cell-based
architectures, with resources spread across multiple
availability zones, to reduce the scope of a disruptive event.
Where consistent communications are necessary, implement static
stability mechanisms to reduce the dependency on control plane
actions.

## Key AWS services

- [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [AWS Availability Zones and Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
- [Monitoring
and Alerting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Resources

- [Reducing
the Scope of Impact with Cell-Based Architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html)
- [Static
stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/)
- [Control
planes and data planes](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel07-bp01.html*

---

# ADVREL07-BP02 Implement a backup strategy which would meet RTO and RPO objectives

Develop comprehensive backup strategies, focusing on data
classification and meeting Recovery Time Objective (RTO) and
Recovery Point Objective (RPO) requirements through appropriate
service selection.

## Implementation guidance

Review the data related to your workload and classify the data
according to usage, retention, and availability needs. Example
classifications might be user profile info, campaign data,
reporting data. Consider how those different data classes are
used within your workload and how the availability of that data
can impact your workload's operation. Use those classifications
to determine the RPO and RTO requirements for your workload.
Identify the AWS services that can meet your requirements, and
deploy resources to the Regions or Availability Zones that can
achieve your RTO and RPO targets. Test the backup and
restoration process to verify that your backup and recovery
strategies will work during a disruptive event.

## Key AWS services

- [AWS Backup](https://aws.amazon.com/backup/)
- [Amazon EBS](https://aws.amazon.com/ebs/)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Amazon Relational Database Service](https://aws.amazon.com/rds/)
- [Amazon Elastic File System](https://aws.amazon.com/efs/)

## Resources

- [Disaster
Recovery (DR) Architecture on AWS, Part II: Backup and Restore with Rapid Recovery](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-ii-backup-and-restore-with-rapid-recovery/index.html)
- Establishing
RPO and RTO Targets for Cloud Applications

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel07-bp02.html*

---

# ADVREL07-BP03 Back up data in multiple locations with consideration for your regulatory or legal requirements

Back up data in multiple locations, and consider how consumer privacy laws may impact your data replication and storage plans.

## Implementation guidance

Select AWS Regions for backup locations that satisfy your legal
and business requirements. Consider how consumer privacy laws may impact your ability to replicate data which
could contain personal data. Be
aware of how countries where your workload operates regulate
advertising and related data, and seek legal consultation when
you are unsure of how regulations might apply to your workload.
Use your understanding of those regulations to select AWS
services and Regions. Seek legal counsel when in doubt.

## Key AWS services

- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)

## Resources

- [Cloud
security guidance](https://www.ncsc.gov.uk/collection/cloud)
- [Protecting
your data with backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html)
- [Amazon DynamoDB now helps you meet regulatory compliance and business continuity requirements through enhanced backup features in AWS Backup](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-dynamodb-requirements-aws-backup/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel07-bp03.html*

---
