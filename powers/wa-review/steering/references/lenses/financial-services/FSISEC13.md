**Pillar**: Security

# FSISEC13: How do you secure AI/ML models and protect training data?

Financial institutions implementing generative AI must
establish comprehensive security controls throughout the AI
lifecycle, from data preparation to model deployment and
monitoring. This includes protecting training data integrity,
securing model development environments, and implementing
robust controls for inference to prevent unauthorized access,
model manipulation, and data poisoning attacks.

## FSISEC13-BP01 Implement comprehensive model security controls

Securing AI/ML models requires implementing multiple layers
of protection to maintain model integrity and prevent
unauthorized access. Establish least privilege access to
foundation model endpoints and implement private network
communication between AI components using VPC endpoints or
AWS PrivateLink. Use customer-managed encryption keys for
model artifacts and training data, implement model
versioning with integrity checking mechanisms, and establish
secure model storage with strict access controls and audit
logging.

## FSISEC13-BP02 Protect training data integrity

The integrity of training data directly impacts the security
and compliance of AI models. Implement data purification
filters to detect harmful inputs, establish data lineage
tracking for regulatory compliance, and apply classification
schemes for sensitive financial data. Deploy continuous
monitoring to detect data poisoning attempts and implement
backup and recovery procedures aligned with your
organization's data protection strategy.

## FSISEC13-BP03 Secure model deployment and inference

Securing deployment and inference stages is critical for
preventing unauthorized access and protecting against
AI-specific attacks. Implement version-controlled prompt
catalogs with security review processes, establish model
access controls using IAM policies, and deploy monitoring
for anomalous invocation patterns. Implement response
filtering mechanisms like Amazon Bedrock Guardrails and
secure API gateways with appropriate authentication,
authorization, and comprehensive logging.

## Resources

### Documents

- [AWS Well-Architected Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/wellarchitected-generative-ai-lens.html)
- [Securing
Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html)
- [AI/ML
for Security](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/ai-ml.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec13.html*
