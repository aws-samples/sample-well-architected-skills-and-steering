# MIDASUS04 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS04-BP01 Design backup strategies that focus on critical data

Manufacturing data varies in criticality from essential production recipes and regulatory
compliance records to temporary operational logs. Design backup strategies that prioritize
truly valuable data while minimizing resource consumption.

**Desired outcome:** A data backup system that balances business continuity needs with sustainability goals,
reducing storage requirements, energy consumption, and carbon footprint while maintaining
manufacturing operational resilience.

**Benefits of establishing this best practice:**

- Reduced storage costs and energy consumption
- Lower carbon footprint from decreased data center resources
- Optimized network bandwidth usage
- Improved recovery time for truly critical manufacturing data

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Categorize data by importance (critical production recipes, compliance records,
operational logs) to determine appropriate backup strategies for each category.
- Establish tiered backup strategies based on data importance, with more frequent and
comprehensive backups for critical data while implementing less resource intensive
approaches for lower priority data.
- Implement data compression, deduplication, and efficient formats to minimize
storage footprint and processing requirements for backups across the data categories.
- Store manufacturing data in AWS Regions closest to production facilities to reduce
energy used for data transfer and improve access speeds for operational systems.

### Implementation steps

- **Data classification and assessment:**

Conduct comprehensive data audits across Amazon EBS volumes, Amazon EFS file
systems, and on-premises data connected through AWS Storage Gateway
- Document recovery time objectives (RTOs) and recovery point objectives (RPOs)
for each data category in AWS Backup

- **Tiered backup strategy design:**

Configure AWS Backup plans with different frequencies for critical EBS
volumes, EFS file systems, and Storage Gateway volumes
- Implement lifecycle policies in Amazon S3 to automatically transition
infrequently accessed backups to cold storage classes

- **Storage optimization configuration:**

Enable compression and deduplication features in AWS Backup for EBS snapshots
and EFS backups
- Configure Amazon EFS Infrequent Access storage class for rarely accessed file
data
- Implement AWS Storage Gateway with deduplication enabled to reduce backup
data footprint

- **Geographic distribution setup:**

Deploy EBS and EFS backups to AWS Regions closest to primary usage locations
- Configure AWS Storage Gateway to cache frequently accessed data locally while
storing backups in energy-efficient regions

- **Performance monitoring:**

Create CloudWatch dashboards to track backup storage utilization across EBS,
EFS, and Storage Gateway
- Establish quarterly review processes using AWS Trusted Advisor storage
recommendations

## Key AWS services

- AWS Backup
- Amazon S3
- Amazon Glacier
- Amazon EBS
- Amazon EFS
- AWS Storage Gateway
- Amazon CloudWatch
- AWS Trusted Advisor

## Resources

- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Amazon Simple Storage Service: Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Cloud Storage on AWS](https://aws.amazon.com/storage/)
- [Optimize
Siemens Teamcenter with Amazon FSx for NetApp ONTAP](https://d1.awsstatic.com/fsx/FSxONTAP-whitepaper-PLM.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus04-bp01..html*

---
