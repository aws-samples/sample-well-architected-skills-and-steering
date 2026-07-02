**Saga**: Development lifecycle
**Capability**: DL.EAC — Everything as code

---

# [DL.EAC.1] Organize infrastructure as code for scale

**Category:** FOUNDATIONAL

Infrastructure as code (IaC) provides consistent and automated infrastructure
management capabilities which are important to DevOps adoption. Effectively organizing and
scaling IaC within your organization enhances flexibility, readability, and reusability
across multiple teams, while streamlining infrastructure provisioning and maintenance.

When working with IaC files and artifacts, apply modern
practices such as modular design for improved management and
reuse, and maintain thorough in-code documentation for
clarity. Adopt IaC-specific design patterns, like breaking
down infrastructure templates into reusable modules. Treat IaC
testing with the same rigor as other software, focusing on
security risks like excessive privileges or open security
groups, while upholding quality standards. Use version
control for IaC templates to ensure traceable changes,
reliable rollbacks, and efficient sharing across the
organization.

You must carefully consider your organization's governance structure when deciding
how to implement IaC at scale. Depending on the specific needs, your organization might find
one model more suitable than the other, or even adopt a hybrid approach that combines
elements of both. The right approach to scaling is dependent on factors such as team
dynamics, operating model, application type, and the desired rate of change.

For example, services like [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) and [AWS Proton](https://aws.amazon.com/proton/) provide
distinct methods to distribute and consume secure-by-default software components and IaC in
different ways. Service Catalog suits organizations favoring predefined deployment standards and
centrally defined resource provisioning, while AWS Proton is ideal for organizations that
allow development teams to maintain infrastructure and application autonomy. Some
organizations might prefer to adopt a fully decentralized approach, where individual teams
provision and manage their own [AWS CloudFormation](https://aws.amazon.com/cloudformation/) IaC templates. Choose the tools and distribution methods that best
support your governance model and business goals.

**Related information:**

- [Infrastructure
as code - Introduction to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)
- [Infrastructure
as Code on AWS - An Introduction](https://blog.awsfundamentals.com/infrastructure-as-code-on-aws-an-introduction)
- [Accelerate
deployments on AWS with effective governance](https://aws.amazon.com/blogs/architecture/accelerate-deployments-on-aws-with-effective-governance/)
- [Source
Control concepts](https://aws.amazon.com/devops/source-control/)
- [Design
Patterns](https://refactoring.guru/design-patterns)
- [Amazon's
approach to security during development: Octane](https://youtu.be/NeR7FhHqDGQ?t=1571)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.1-organize-infrastructure-as-code-for-scale.html*
