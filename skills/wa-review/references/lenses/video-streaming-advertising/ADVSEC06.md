# ADVSEC06 — Regulatory adherence

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC06-BP01 Verify your advertising workload remains adherent to data protection regulations

Maintaining compliance is essential to operate and grow your
solution. Data encryption is a key requirement for several
compliance programs; you can utilize AWS KMS to facilitate
data encryption and key management for your solution. KMS
allows for the creation and management of cryptographic keys
which can be used to encrypt data at rest and in transit. It
simply integrates with other AWS services and maintains an
audit trail for key usage. KMS also maintains validation and
certifications from multiple compliance regimes including
FIPS, PCI DSS, and HIPAA.

## Implementation guidance

To assist with data governance consider using Amazon Macie.
Macie can automatically scan and identify sensitive data
across AWS environments. The service can categorize data based
on content type and sensitivity level. Based on the data
classification Macie provides a risk score for different
datasets and storage locations. Amazon Macie can assist to
meet regulatory requirements including GDPR, CCPA, HIPAA, by
generating detailed reports on data types and locations for
regulatory audits.

## Key AWS services

- AWS KMS
- Amazon Macie

## Resources

- [Compliance validation for Macie](https://docs.aws.amazon.com/macie/latest/user/compliance-validation.html)
- [Compliance validation for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-compliance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec06-bp01.html*

---
