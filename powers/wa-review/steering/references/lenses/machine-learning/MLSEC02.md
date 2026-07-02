# MLSEC02 — ML problem framing

**Pillar**: Security  
**Best Practices**: 1

---

# MLSEC02-BP01 Design data encryption and obfuscation

Consider how to protect personal data. Use field level encryption or
obfuscation to protect personally identifiable data.

**Desired outcome:** You establish
robust protection for sensitive information by implementing data
encryption and obfuscation techniques in your machine learning
workflows. You identify and secure personally identifiable
information (PII) through field-level encryption and data masking,
which improves your adherence to privacy regulations while
maintaining data utility for ML models.

**Common anti-patterns:**

- Storing personally identifiable information in plain text
format.
- Using the same encryption keys across different environments.
- Implementing inconsistent data protection policies across ML
pipelines.
- Overlooking data protection requirements during the design
phase.
- Failing to audit data for attributes requiring special
treatment.

**Benefits of establishing this best
practice:**

- Enhanced protection of sensitive and personally identifiable
data.
- Improves adherence to data privacy regulations.
- Reduced risk of data breaches and unauthorized access.
- Improved trust from users and stakeholders.
- Ability to utilize sensitive data for ML training while
maintaining privacy.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When designing machine learning workflows, protect personal and
sensitive data throughout the entire data lifecycle. You should
evaluate your data early in the process to identify fields
containing PII or other sensitive information requiring
protection. Implementing field-level encryption or data
obfuscation techniques maintains data utility for machine learning
while safeguarding individual privacy.

AWS provides multiple services to identify, classify, and protect
sensitive data within your ML workflows. Services like
[AWS Glue](https://aws.amazon.com/glue/)
can automatically detect PII, while
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) and
[AWS CloudHSM](https://aws.amazon.com/cloudhsm/) support robust encryption strategies. You should
establish consistent policies for handling sensitive data across
your organization and regularly audit your data protection
measures to improve your adherence to privacy regulations.

### Implementation steps

- **Audit data for attributes requiring
special treatment**. Identify fields containing
data requiring special treatment, such as field-level
encryption, data masking, or obfuscation. Use automated
tools like
[AWS Glue](https://aws.amazon.com/glue/) to identify PII and sensitive data patterns
within your datasets.
- **Establish a data classification
framework**. Develop a systematic approach to
categorize data based on sensitivity levels. Define which
categories require encryption, masking, or other protection
techniques, and document these requirements in your
organization's security policies.
- **Implement field-level
encryption**. Apply encryption selectively to
sensitive fields rather than entire datasets. Use
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) to manage encryption keys
and integrate with services like
[Amazon S3](https://aws.amazon.com/s3/) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) for transparent encryption of selected
fields.
- **Apply data obfuscation
techniques**. Use methods such as tokenization,
data masking, or anonymization to protect sensitive
information while preserving data utility for machine
learning. Consider using services like
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) for data transformation and masking
operations.
- **Establish key rotation
policies**. Implement regular rotation of
encryption keys to minimize the impact of potential key
compromises. Configure
[AWS KMS](https://aws.amazon.com/kms/) to automate key rotation according to your
security policies and regulatory requirements.
- **Secure ML model
artifacts**. Verify that trained models and their
associated metadata do not inadvertently expose sensitive
information. Use
[Amazon SageMaker AI's](https://aws.amazon.com/sagemaker/) security features to encrypt model
artifacts and secure API endpoints that serve predictions.
- **Implement access
controls**. Restrict access to sensitive data and
encryption keys using
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) policies. Apply the
principle of least privilege to verify that only authorized
personnel can access protected information.
- **Monitor and audit access
patterns**. Implement continuous monitoring to
detect unauthorized access attempts or unusual patterns that
might indicate a security breach. Configure
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) and
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track and alert on suspicious
activities.
- **Implement differential privacy
techniques**. When working with AI models, consider
implementing differential privacy techniques to add
statistical noise to training data, protecting individual
privacy while maintaining overall data utility.
- **Establish mechanisms to stop model
memorization**. Implement safeguards to block AI
models from memorizing and potentially reproducing sensitive
information from training data, especially when using large
language models.

## Resources

**Related documents:**

- [Detect
and process sensitive data](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html)
- [Security
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [Data
protection in Amazon SageMaker AI Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/data-protection.html)
- [Data
Privacy in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/data-privacy.html)
- [Data
Encryption](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/data-encryption.html)
- [Introducing
PII Data Identification and Handling Using AWS Glue
DataBrew](https://aws.amazon.com/blogs/big-data/introducing-pii-data-identification-and-handling-using-aws-glue-databrew/)
- [7
ways to improve security of your machine learning
workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/)
- [Secure
deployment of Amazon SageMaker AI resources](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/)

**Related videos:**

- [Privacy-preserving
machine learning](https://www.youtube.com/watch?v=ZQkB9XRqdnc)
- [Data
Protection Best Practices in Machine Learning](https://www.youtube.com/watch?v=1iZYmtFFLnw)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec02-bp01.html*

---
