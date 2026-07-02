**Pillar**: Security

# FSISEC02: How do you achieve, maintain, and monitor ongoing compliance with regulatory guidelines and mandates?

Companies in the financial sector have more demanding compliance
monitoring and implementation requirements than most other
sectors of the economy. Traditional methods of compliance
assessment do not keep pace with the dynamics of the agile cloud
environment. For this reason, the best practices and tools
required are specific to this type of environment. Regulations
ensure that consumers' personal and financial data are
protected. Compliance with these regulations helps prevent
identity theft, fraud, and unauthorized disclosure of personal
information. Compliance also helps maintain the integrity and
stability of the financial markets by ensuring that institutions
engage in responsible lending and investment practices and avoid
excessive risk-taking. The following best practices help
facilitate compliance in the cloud.

## FSISEC02-BP01 Automate your compliance management

AWS has services to help you identify, optimize and remediate
resource configurations for continuous compliance and
operational efficiency. AWS services help customers achieve
immutable resource configuration and offer configurable
logging for the auditing of user and API activity. Using
[AWS Config](https://aws.amazon.com/config/) and its

[proactive mode](https://aws.amazon.com/blogs/aws/new-aws-config-rules-now-support-proactive-compliance/)
helps you save time and remove the risk of human error when
you automate and scale compliance management. It helps FIs
(mainly the first line of defense) effectively manage risk for
their cloud resources.

## FSISEC02-BP02 Use ready-to-deploy templates for standards and best practices

Ready-to-deploy templates are a quick and assertive way to
measure what level of security is present in cloud
environments. These templates are available both for best
practices in technology such as database, serverless, and
networking, and are aligned to frameworks that are widely

accepted and recognized. Among the most suitable templates
are
[managed
rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html), AWS Config
[Conformance
Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) in AWS Config, and
[AWS Security Hub CSPM standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-available.html). FIs can benefit
from Conformance Packs that are available and ready to be
used for alignment to the financial services industry's
standards and regulatory requirements, such as PCI-DSS,
NYDFS, and FFIEC.

### Prescriptive guidance

- Use Amazon Bedrock Guardrails for automated response
validation and content filtering.
- Use pre-configured security controls for AI service
endpoints and model access.
- Use compliance templates for AI model governance
including model cards and documentation.
- Deploy standard configurations for secure prompt
management and version control.
- Use automated monitoring for AI system outputs and
potential security issues.

- A Conformance Pack can be deployed as is or it can be
edited to include your specific resources and use cases.
For more information, see
[Deploying
a Conformance Pack Using the AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-console.html)
[Console](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-console.html).
- When adding a new rule, choose how it evaluates your
resources, as well as how it is initiated. For more
information, see
[Evaluation
Mode and Trigger Types for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html).
- To determine if requirements in a standard are being
met, enable the controls from AWS Security Hub CSPM
standards. For more information, see
[Security
standards and controls in AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html).
- Leverage Amazon Bedrock's Prompt Management catalog for
secure prompt storage and version control.

## Resources

**Related documents:**

- [AWS Config Rules Now Support Proactive Compliance](https://aws.amazon.com/blogs/aws/new-aws-config-rules-now-support-proactive-compliance/)

**Related videos:**

- [Cloud compliance, assurance, and auditing](https://www.youtube.com/watch?v=xREhfrUqpd4&ab_channel=AWSEvents)
- [Setting up controls at scale in your AWS environment](https://www.youtube.com/watch?v=NkE9_okfPG8&t=1697s&ab_channel=AWSEvents)
- [Proactive governance and compliance for AWS
workloads](https://www.youtube.com/watch?v=PpUnH9Y52X0&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec02.html*
