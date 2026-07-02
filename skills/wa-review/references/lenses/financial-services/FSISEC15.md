**Pillar**: Security

# FSISEC15: How do you implement AI model governance and access controls?

Effective AI governance requires comprehensive access
controls, model lifecycle management, and continuous oversight
to adhere to regulatory requirements and organizational
policies. Financial institutions must establish structured
governance frameworks that define roles, responsibilities, and
processes for managing AI systems throughout their lifecycle.
Without proper governance and access controls, organizations
risk unauthorized model changes, compliance violations, and
security breaches.

## FSISEC15-BP01 Establish an AI model governance framework

A comprehensive AI model governance framework provides
structure and oversight for all AI activities within the
organization. Implement model approval workflows and change
management processes that ensure proper review and
authorization before models are deployed or modified. These
workflows should include security reviews, compliance
assessments, and performance validation.

Establish model performance monitoring and drift detection
capabilities to identify when models deviate from expected
behavior, which could indicate security issues or degraded
performance. Create standardized model documentation
requirements including model cards that capture key
information about model purpose, limitations, training data,
and security considerations.

Implement model retirement and lifecycle management
procedures that ensure secure decommissioning of outdated
models and proper transition to new versions. Establish AI
ethics and responsible AI guidelines that align with your
organization's values and regulatory requirements, providing
clear direction for AI development and deployment.

## FSISEC15-BP02 Implement comprehensive access controls

Granular access controls are essential for maintaining the
security and integrity of AI systems. Create distinct roles
for prompt engineering and security administration to
enforce separation of duties and prevent unauthorized
modifications. Maintain separate permissions for model
access and management using IAM policies, resource-based
policies, and permission boundaries.

Establish dedicated approval workflows for AI system changes
that ensure proper review and authorization before
modifications are implemented. Enforce strict boundaries
between development and production AI environments to
prevent unauthorized changes from affecting production
systems. Implement permissions boundaries for agentic
workflows to control how AI agents can interact with other
systems and data.

## FSISEC15-BP03 Monitor and audit AI system governance

Continuous monitoring and auditing of AI governance
activities improves ongoing regulatory adherence and
effectiveness. Track adherence to AI governance policies
through automated checks and regular assessments. Monitor
model performance against established baselines to detect
anomalies that could indicate security issues.

Audit AI system access patterns and permissions to identify
potential security risks or unauthorized activities.
Establish regular governance reviews and assessments that
evaluate the effectiveness of your AI governance framework
and identify areas for improvement. Implement automated
compliance checking for AI systems that can verify adherence
to security policies, regulatory requirements, and
organizational standards.

## Resources

### Documents

- [AWS Well-Architected Generative AI Lens - Governance](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/governance.html)
- [IAM
Best Practices for AI Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Amazon SageMaker AI Model Governance](https://docs.aws.amazon.com/sagemaker/latest/dg/model-governance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec15.html*
