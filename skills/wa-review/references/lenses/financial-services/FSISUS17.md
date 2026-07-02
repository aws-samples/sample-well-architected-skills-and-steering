**Pillar**: Sustainability

# FSISUS17: How do you minimize your test, staging, sandbox instances?

## FSISUS17-BP01 Use infrastructure as code (IaC) code base to snapshot your environment allowing you to decommission test infrastructure

### Prescriptive guidance

Reducing the number, frequency, and use of test and staging environments can reduce
your environmental impact. If you use [infrastructure as code (IaC)](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) with AWS Event Engine or Workshop Studio to
snapshot your environments, you can break down the infrastructure once your testing is
complete. This allows you to reduce the unneeded resources. If the test environment is
required later, you can use IaC to restore it when needed.

Instead of creating separate instances to test several environments, use snapshots
to test only the required workload using the same instance. You can queue your testing
based on development priorities to reduce the use of test and staging instances.

Use infrastructure as code (IaC) to snapshot generative AI development
environments. Implement shared generative AI model testing environments rather than
individual instances. Schedule automatic shutdown of unused generative AI development
instances.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus17.html*
