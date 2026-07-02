**Pillar**: Security

# FSISEC10: How are you handling data loss prevention in the cloud environment?

Data loss as part of a security event, accident or business
process can affect both your operation and state of compliance.
The following recommendations can help with the protection
from theft and inadvertent or malicious loss. Generative AI
systems introduce new considerations for data loss prevention,
including model outputs, prompt security, training data, model
artifacts, and AI-generated content.

## FSISEC10-BP01 Prevent modifications and deletions of logs and data

Financial services agencies around the world, including the
Securities and Exchange Commission (SEC) and the Financial
Industry Regulatory Authority (FINRA) in the US, have
created rules

that require a broker-dealer to maintain and preserve
electronic records exclusively in a non- rewriteable,
non-erasable format, also known as a write once, read many
(WORM) format.

For object data, Amazon
[S3
Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) allows you to store objects
using a WORM model. You can use WORM protection for
scenarios where it is imperative that data is not changed or
deleted after it has been written. With S3 Object lock, you
can securely deliver logs to a designated S3 bucket, and use
the S3 Object Lock feature to make the logs immutable. It
blocks object version deletion during a customer- defined
retention period so that you can enforce retention policies.
In

conjunction with
[S3
versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), which protects objects from
being overwritten, you're able to keep objects immutable for
as long as S3 Object Lock protection is applied.

For file data, use
[SnapLock](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock.html),
a feature on
[Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html) that allows you to
store files using a WORM model, helping prevent accidental or
malicious attempts at modification and deletion for a
customizable retention period. You can also back up data on
FSx for ONTAP using AWS Backup and WORM-protect your backups
using
[AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html).

For AI systems, implement secure prompt catalogs and
validate model responses for potential data leakage while
protecting training data integrity and maintaining
continuous monitoring of AI system outputs and establishing
audit trails for all AI data interactions.

## FSISEC10-BP02 Limit and monitor key deletes

Once encrypted, the data is protected by cryptographic keys
that must be kept as long as the data is to be accessed. Only
[key
administrators](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-adding-permission.html) should perform key deletion.
Review all destruction requests within the safety window, as a
key cannot be destroyed immediately. Instead, it is disabled,
which prevents use, and is deleted at the expiry of the
window.

To help validate that the key deletion won't impact your
company,
[set
up an alarm](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html) that detects use of an AWS KMS
key pending deletion.

### Prescriptive guidance

- Make sure that the Amazon S3 buckets are configured to
use the
[Object
Lock feature](https://aws.amazon.com/blogs/storage/protecting-data-with-amazon-s3-object-lock/) to help prevent the
objects they store from being deleted, and help meet
regulatory compliance needs.
- Make sure that
[Amazon S3 object versioning is enabled](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) for
your Amazon S3 buckets in order to preserve and recover
overwritten and deleted Amazon S3 objects as an extra
layer of data protection or data retention.
- Set up
[AWS Config managed rule](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-versioning-enabled.html) to identify Amazon S3 buckets that do not have versioning enabled, and

[implement
automatic remediation](https://aws.amazon.com/blogs/storage/automate-amazon-s3-versioning-using-aws-config-rules/) to configure
versioning on non-compliant Amazon S3 buckets.
- Implement backup and restore processes to help you
restore data to a point in time before data corruption,
modification or destruction. AWS
[provides
several solutions](https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/) for backups to
integrate with your operational and security incident
recovery procedures.

Use
[AWS Backup](https://aws.amazon.com/backup/) with AWS Organizations to
centrally deploy data protection policies to
configure, manage, and govern your backup activities
across your AWS accounts and resources.
- Beyond creating and storing your backups,
[AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) can
continuously evaluate backup activity and generate
audit reports that can help you demonstrate
compliance with regulatory requirements. These
reports also provide you with more visibility into
your backup activities, helping you monitor your
operational posture and identify failures that may
need further action.

- Deleting an AWS KMS key is destructive and potentially
dangerous. After an AWS KMS key is deleted, you can no
longer decrypt the data that was encrypted under that
AWS KMS key, which means that data becomes
unrecoverable.

Delete an AWS KMS key only when you are sure that
you don't need to use it anymore.
- If you are not sure, consider
[disabling
the AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) instead of
deleting it.
- [Control
access to key deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-adding-permission.html) by creating
fine-grained access control policies and allow only
authorized principals with the ability to
[schedule
key deletion](https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html).

- Create an alarm to detect and notify on AWS KMS key
deletion events.
- [Create an alarm to detect usage of an AWS KMS key that is scheduled for deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html).

## Resources

**Related documents:**

- [How to manage retention periods in bulk using Amazon S3 Batch Operations](https://aws.amazon.com/blogs/storage/how-to-manage-retention-periods-in-bulk-using-amazon-s3-batch-operations/)

**Related videos:**

[Data protection strategies for the cloud - AWS Online Tech Talks](https://www.youtube.com/watch?v=4PgoBjqpm8U&ab_channel=AWSOnlineTechTalks)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec10.html*
