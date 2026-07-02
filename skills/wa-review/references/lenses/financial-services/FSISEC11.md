**Pillar**: Security

# FSISEC11: How are you protecting against ransomware?

Ransomware refers to a business model and a wide range of
associated technologies that bad actors use to extort money.
The bad actors use a range of tactics to gain unauthorized
access to their victims data and systems, including exploiting
unpatched vulnerabilities, taking advantage of weak or stolen
credentials, and using social engineering. Access to the data
and systems is restricted by the bad actors, and a ransom
demand is made for the safe return of these digital assets.
Protection against ransomware now includes securing AI models,
model registries, prompts, prompt catalogs and training data
from manipulation or compromise.

## FSISEC11-BP01 Prevent malware infiltration by securing compute resources

To detect malware that may be the source of a ransomware
incident, enable
[malware
protection in](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html)
[Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html). This feature automatically
initiates an agentless scan on the Amazon Elastic Block Store (EBS) volumes attached to the impacted EC2 instance or
container workload to detect the presence of malware. For AI
workloads, implement secure prompts, prompt catalogs and
validate user inputs while monitoring for potential model
manipulation and enforcing response filtering mechanisms.

### Prescriptive guidance

- Use
[Amazon S3 Object Lock](https://aws.amazon.com/s3/features/object-lock/) for object storage
immutability and ransomware protection within cloud
storage.
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
- Enable
[AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html), which enforces
WORM (write-once-read-many) setting for the backups
you store and create in a backup vault.

- Because many ransomware events arise from unintended
disclosure of static IAM access keys, AWS recommends
that you use IAM roles that provide short-term
credentials, rather than using long-term IAM access
keys. This includes using
[identity
federation](https://aws.amazon.com/identity/federation/) for your developers who are
accessing AWS, using IAM roles for system-to-system
access, and using
[IAM
Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) for hybrid access.
- Enable
[Amazon S3 protection in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html).
With Amazon S3 protection, GuardDuty monitors
object-level API operations to identify potential
security risks for data in your Amazon S3 buckets. This
includes findings related to anomalous API activity and
unusual behavior related to your data in Amazon S3, and
can help you identify a security event early on.
- Enable
[Amazon GuardDuty Malware Protection](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html) across
all AWS accounts in your organization, to help you
detect the potential presence of malware by scanning the
Amazon EBS volumes that are attached to the Amazon EC2
instances and container workloads.

## FSISEC11-BP02 Prevent threats from accessing your data stores

Scoping access to data based on the principal of minimum
privileges helps prevent as well as limit the blast radius of
an exploit. An effective data classification scheme, along with
enforcement and monitoring based on that scheme can help
prevent an bad actor from having accessing and encrypting your
data.

Network isolation and segregation is another effective
protection as compromised systems cannot reach deep into your
network. Leverage the best practices recommended in the
Infrastructure protection section to funnel access to data
stores over a private network, from a limited number of hosts.

## FSISEC11-BP03 Use frequent backups to recover from a threat

Because ransomware makes itself known quickly, incorporate
short-lived anti-ransomware backups into your backup cycle.
AWS take snapshots of data stores, so back up often and keep
these around for only a few days to limit costs.

For more information on how to protect from Ransomware at AWS,
see
[Ransomware Risk Management on AWS Using the NIST Cyber Security Framework (CSF)](https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/ransomware-risk-management-on-aws-using-nist-csf.html).

### Prescriptive guidance

- Use
[Amazon S3 Object Lock](https://aws.amazon.com/s3/features/object-lock/) for object storage
immutability and ransomware protection within cloud
storage.
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
- Enable
[AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html), which enforces
WORM (write-once-read-many) setting for the backups
you store and create in a backup vault.

- Because many ransomware events arise from unintended
disclosure of static IAM access keys, AWS recommends
that you use IAM roles that provide short-term
credentials, rather than using long-term IAM access
keys. This includes using
[identity
federation](https://aws.amazon.com/identity/federation/) for your developers who are
accessing AWS, using IAM roles for system-to-system
access, and using
[IAM
Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) for hybrid access.
- Enable
[Amazon S3 protection in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html).
With Amazon S3 protection, GuardDuty monitors
object-level API operations to identify potential
security risks for data in your Amazon S3 buckets.

This includes findings related to anomalous API activity
and unusual behavior related to your data in Amazon S3,
and can help you identify a security event early on.

- Enable
[Amazon GuardDuty Malware Protection](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html) across
all AWS accounts in your organization, to help you
detect the potential presence of malware by scanning the
Amazon EBS volumes that are attached to the Amazon EC2
instances and container workloads.

## Resources

**Related documents:**

- [Protecting
against ransomware](https://aws.amazon.com/security/protecting-against-ransomware/)
- [GuardDuty findings that initiate Malware Protection scans](https://docs.aws.amazon.com/guardduty/latest/ug/gd-findings-initiate-malware-protection-scan.html)
- [Ransomware Risk Management on AWS Using the NIST Cyber Security Framework (CSF)](https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/ransomware-risk-management-on-aws-using-nist-csf.html)
- [Ransomware mitigation: Top 5 protections and recovery preparation actions](https://aws.amazon.com/blogs/security/ransomware-mitigation-top-5-protections-and-recovery-preparation-actions/)
- [Workshop: Ransomware on S3 - Simulation and Detection](https://catalog.workshops.aws/aws-cirt-ransomware-simulation-and-detection/en-US)

**Related videos:**

- [What is Amazon GuardDuty Malware Protection? | Amazon Web Services](https://www.youtube.com/watch?v=xKAp5lx1Sb0&ab_channel=AmazonWebServices)
- [AWS re:Invent 2021 - Backup, disaster recovery, and ransomware protection with AWS](https://www.youtube.com/watch?v=Ru4jxh9qazc&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec11.html*
