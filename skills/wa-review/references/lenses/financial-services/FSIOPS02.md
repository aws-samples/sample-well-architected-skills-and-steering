**Pillar**: Operational Excellence

# FSIOPS2: Have you completed an operational risk assessment?

Financial services workloads should be continually reviewed and prioritized with regard
to their risk impact to the overall business (for example, based on their reputational,
financial, or regulatory impact).

## FSIOPS02-BP01 Understand the Shared Responsibility Model and how it applies to services and workloads you run in the cloud

In connection with your use of the cloud, you must understand how the [AWS Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) affects your control environment. For example, certain
controls may be the responsibility of AWS, but certain controls remain the
responsibility of the financial services institution. Review the AWS Shared
Responsibility Model and map AWS responsibilities and customer responsibilities
according to each AWS service you use and your control environment. For those controls
that are the responsibility of AWS, you can use [AWS Artifact](https://aws.amazon.com/artifact/) to access audit reports and review the implementation and
operating effectiveness of AWS security controls.

### Prescriptive guidance

Review and understand the [AWS Shared Responsibility
Model](https://aws.amazon.com/compliance/shared-responsibility-model/), and the different demarcation points that apply to AWS infrastructure
services (such as EC2), container services (such as RDS), and abstracted services (such
as S3). If your organization has central functions (like a Cloud Center of Excellence or
governance team), publish a shared responsibility model for your organization, which
clearly defines the roles of AWS, the central team, and distributed teams.

## FSIOPS02-BP02 Develop an enterprise cloud risk plan

Map the interactions between business consumers of cloud services and the internal
stakeholders that shape this consumption, including risk and control considerations.
Integrate across the three lines of defense functions, and provide necessary resources and
training to satisfy their mandates for operating and protecting your business in the cloud
while you strive to achieve your strategic goals.

This integration can be achieved by carrying out a risk-based assessment of your
operating model, and is especially effective when complemented with a review of
decision-making processes and authority to determine if they are cloud-appropriate. As
requirements are translated into controls, pay attention to the strength of the controls
to mitigate the identified risks. Another key risk factor includes the ability to control
design and performance to facilitate independent assessment by internal risk management
and audit functions. Focus on control design helps you incorporate key control
requirements into the design from the start.

### Prescriptive guidance

Evaluate existing risk models in use, and related policies, for relevance in a
cloud environment. Many risk models are focused on on-premises architectures and do not
account for advantages of cloud-based workloads. Reach out to your AWS account team to
leverage AWS expertise in risk and compliance.

## FSIOPS02-BP03 Evaluate data privacy and security requirements for generative AI

Generative AI models require careful consideration of data handling, especially when processing sensitive financial information. Implement data classification, tokenization, and privacy-preserving techniques when using foundation models. Adhere to data residency requirements and understand the data processing practices of third-party model providers. Establish data retention policies and ensure generative AI systems support regulatory requirements including data subject rights.

### Prescriptive guidance

Use Amazon Bedrock with AWS PrivateLink to implement network isolation for generative AI inference. Implement data masking and tokenization before sending sensitive data to foundation models. Configure Amazon Bedrock Guardrails to prevent unauthorized data exposure in model outputs. Use AWS KMS for encryption of prompts and responses containing sensitive information. Document data flow diagrams showing how sensitive data moves through generative AI pipelines including retention periods and deletion schedules.

Implement AWS CloudTrail and Amazon CloudWatch for comprehensive audit logging of data access and model interactions.

Define specific data retention periods for prompts, responses, and model training data in accordance with regulatory requirements.

## FSIOPS02-BP04 Establish prompt engineering standards and version control

Prompts are critical operational assets in generative AI systems requiring comprehensive governance frameworks. Implement version control, testing, and approval processes for prompt templates used in production. Establish prompt engineering best practices and security guidelines to prevent prompt injection attacks.

### Prescriptive guidance

Store production prompts in AWS CodeCommit or similar version control systems with change tracking and approval workflows.

Implement automated testing for prompt templates using representative test cases. Use AWS Lambda and AWS Step Functions to create controlled prompt execution pipelines with automated rollback capabilities.

Establish prompt security guidelines including input validation, sanitization and protection against prompt injection attacks.

Establish prompt performance monitoring to track effectiveness and model response quality over time with automated alerting.

Define escalation procedures for prompt-related security incidents and integrate with existing incident response frameworks.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops2.html*
