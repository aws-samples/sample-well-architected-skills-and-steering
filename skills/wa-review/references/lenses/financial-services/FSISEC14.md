**Pillar**: Security

# FSISEC14: How do you monitor AI system outputs for security issues?

Continuous monitoring of AI system outputs is critical for
financial institutions to detect harmful responses, potential
data leakage, and security violations. Without proper
monitoring, AI systems may generate responses that expose
sensitive information, violate compliance requirements, or
create security vulnerabilities. Implementing comprehensive
monitoring across all AI interactions enables organizations to
identify and address security issues before they impact
customers or operations.

## FSISEC14-BP01 Implement automated response validation

Automated response validation is essential for ensuring AI
systems operate within defined security parameters. Deploy
guardrails for content filtering to detect and prevent
harmful, biased, or non-compliant responses from reaching
users. Monitor for prompt injection attempts where malicious
inputs might manipulate model behavior and implement
automated detection systems that flag potentially harmful
responses for review.

Establish clear response quality and safety metrics that
align with your organization's security and compliance
requirements. Create alert mechanisms that notify security
teams when suspicious AI system behavior is detected,
enabling rapid investigation and remediation of potential
security issues.

## FSISEC14-BP02 Monitor AI system interactions

Comprehensive monitoring of AI system interactions provides
visibility into potential security issues and enables
proactive threat detection. Track all model invocations and
user interactions to establish usage patterns and identify
anomalies that may indicate security incidents. Monitor for
unauthorized access patterns to AI services that could
signal credential compromise or insider threats.

Implement comprehensive logging of AI system events
including user inputs, model responses, and system actions.
Establish baseline behavior patterns for AI systems to
enable anomaly detection and monitor for potential data
leakage in model responses that could expose sensitive
financial information or intellectual property.

## FSISEC14-BP03 Establish AI incident response procedures

Financial institutions must develop specialized incident
response procedures for AI-specific security events. Develop
playbooks that address unique AI security incidents such as
prompt injection attacks, harmful model responses, or model
manipulation attempts. Include harmful model responses in
your incident classification system to ensure appropriate
escalation and response.

Establish clear procedures for handling model response
validation failures, including containment, investigation,
and remediation steps. Create escalation procedures for AI
security events that define roles, responsibilities, and
communication channels. Where appropriate, implement
automated response mechanisms that can take immediate action
when AI security issues are detected, such as blocking
suspicious requests or disabling compromised endpoints.

## Resources

### Documents

- [AWS Well-Architected Generative AI Lens - Governance](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/governance.html)
- [IAM
Best Practices for AI Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Amazon SageMaker AI Model Governance](https://docs.aws.amazon.com/sagemaker/latest/dg/model-governance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec14.html*
