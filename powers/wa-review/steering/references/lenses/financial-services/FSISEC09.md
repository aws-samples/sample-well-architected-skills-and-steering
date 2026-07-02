**Pillar**: Security

# FSISEC09: How are you managing your encryption keys?

In addition to implementing the
[data
protection recommendations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html) applicable to any
company seen in the AWS Well-Architected Framework Security
Pillar, financial institutions often have additional
industry-specific requirements that can influence the management
of cryptographic keys. With generative AI systems, key
management extends to protecting model artifacts, training
data, knowledge bases, sensitive prompts and prompt catalogs.

## FSISEC09-BP01 Consider compliance obligations regarding location of cryptographic keys

AWS Key Management Service (AWS KMS) uses an
[envelope
encryption strategy](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html), which
consists of encrypting plaintext data with a data key, and
then encrypting the data key with another key. AWS KMS keys
are created in AWS KMS and never leave AWS KMS unencrypted.

AWS KMS supports three types of keys: customer-managed keys,
AWS managed keys, and AWS owned keys (for more information,
see the
[AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)). For many FSI customers,
customer- managed keys are the preferred option, because
they allow for control of the permissions to use keys from
their applications or AWS services. It also provides added
flexibility for key generation and storage.

Although it's less common, AWS customers who have a
compliance or regulatory need to store and use their
encryption keys on-premises or outside of the AWS Cloud can
do so by using
[external
key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html).

### Prescriptive guidance

- Work backwards from your company's compliance objectives
and security standards in order to determine the right
encryption method for your use case.

Leverage AWS audit reports, available for download
at
[AWS Artifact](https://aws.amazon.com/artifact/), to understand the
controls implemented by AWS, and tested for
operating effectiveness by third-party auditors on
AWS KMS.
- Review the list of services that you are using for
your workload to understand
[how
AWS KMS integrates
with the service](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html).
- Review
[AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) with AWS KMS
integration if your application needs to encrypt
data client-side.

- Evaluate the differences between
[different
key types in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt).
- When using customer managed keys, consider the default
key store to provide the best balance between agility,
security, data sovereignty, and availability.
- Consider using custom key stores with
[AWS CloudHSM](https://aws.amazon.com/cloudhsm/) or the
[external
key store](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) to adhere to specific
compliance obligations.
- For AI workloads, implement comprehensive encryption for
model artifacts and sensitive training data while
protecting prompt catalogs and verifying compliant key
management across all AI data flows.

## Resources

**Related documents:**

- [How Financial Institutions can Select the Appropriate Controls to Protect Sensitive Data](https://aws.amazon.com/blogs/industries/how-financial-institutions-can-select-the-appropriate-controls-to-protect-sensitive-data/)
- [Announcing
AWS KMS External Key Store (XKS)](https://aws.amazon.com/blogs/aws/announcing-aws-kms-external-key-store-xks/)

**Related videos:**

- [AWS re:Invent 2022 – Protecting secrets, keys, and data: Cryptography for the long term](https://www.youtube.com/watch?v=9vr3oMODIUE&t=2535s&ab_channel=AWSEvents)
- [AWS re:Invent 2022 – AWS data protection: Using locks, keys, signatures, and certificates](https://www.youtube.com/watch?v=lD34wbc7KNA&ab_channel=AWSEvents)
- [AWS re:Invent 2022 – Introducing AWS KMS external keys](https://www.youtube.com/watch?v=prj6xgpHFTo&t=672s&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec09.html*
