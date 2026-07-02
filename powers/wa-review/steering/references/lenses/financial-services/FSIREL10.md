**Pillar**: Reliability

# FSIREL10: How are backups retained?

## FSIREL10-BP01 Understand requirements for data backup and retention

An important task of determining the resilience requirements of a workload is to
identify data backup and retention needs. Financial institutions may have standards
for backup and retention of data in their systems, which may be informed by regulatory
requirements. Financial services customers must understand the requirements that apply
to the workloads that are running in their environments.

## FSIREL10-BP02 Back up logs as part of the backup strategy

In addition to the backup of workload data and databases, the system logs may
also fall under regulatory requirements. Include the AWS CloudTrail, CloudWatch Logs, workload, and
system logs in the log backup plan. In AWS, customers use Amazon S3, Amazon Glacier, Amazon EBS
snapshots, and Amazon RDS snapshots for backups of AWS services, and AWS Storage Gateway for
on-premises backup to AWS. The AWS Backup service centralizes the management of the
backups across the AWS environment by creating [tag-based policies to manage the backups](https://aws.amazon.com/blogs/storage/use-aws-backup-and-ci-cd-tools-to-automate-centralized-backup-across-aws-services/).

## FSIREL10-BP03 Incorporate anti-ransomware backups into your backup strategy

In addition to the normal backup cycle, short-lived anti-ransomware backups need
to be inserted into the backup cycle. Define a frequency and retention time on how
long these ransomware backups should be held that aligns with your corporate security
strategy. While a Regional copy of the data is sufficient for most cases, you can
consider replicating backups with AWS Backup into another Region and AWS account. For
a more detailed discussion around preventing ransomware, see [Protecting resources](https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/protecting-resources.html).

## FSIREL10-BP04 Create lifecycle policies for backups

Based on regulatory requirements, create lifecycle policies to retain and purge
data in AWS. You can use a lifecycle policy in Amazon S3 to allow for the automation of
migration of data to the most appropriate storage tier. AWS Backup allows for the
management of retention of data across the environment through tag-based policies.
AWS Backup also provides you with a [Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) mechanism to
help prevent changes to backup lifecycles, as well as help prevent manual deletion of backups,
helping you to align with your compliance requirements.

## FSIREL10-BP05 Use Glacier Vault Lock and S3 Object Lock for WORM storage

Financial institutions often need to retain records for many years in write-once
indelible storage. FSIs can use Glacier Vault Lock and S3 Object Lock mode to store
data using a write-once-read-many (WORM) model. Amazon S3 Object Lock has been assessed by
Cohasset Associates for use in environments that are subject to SEC 17a-4, CFTC, and
FINRA regulations. The Amazon S3 Object Lock mode applied to an object stops users
from modifying that object. To track which objects have S3 Object Lock, you can refer
to an Amazon S3 inventory report that includes the status of objects. Amazon S3 Object Lock
helps you adhere to regulatory requirements that require WORM storage, or add another layer
of protection against object changes and deletion. For more information about how Amazon S3
Object Lock relates to these regulations, see the [Cohasset Associates Compliance Assessment for Amazon S3 whitepaper](https://d1.awsstatic.com/r2018/b/S3-Object-Lock/Amazon-S3-Compliance-Assessment.pdf). AWS also
has partners that specialize in legal hold search and archive solutions that are
compatible with AWS, and often built on top of AWS WORM features. Refer to the
[AWS Partners
website](https://aws.amazon.com/partners/work-with-partners/) for information.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel10.html*
