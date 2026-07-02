**Saga**: Quality assurance
**Capability**: QA.FT — Functional testing

---

# [QA.FT.2] Validate system interactions and data flows with integration tests

**Category:** FOUNDATIONAL

Integration tests evaluate the interactions between multiple components that make up
the system, including infrastructure and external systems. The goal of integration testing
is to help ensure that these interactions and data flows work together, ensuring that recent
changes have not disrupted any interfaces or introduced undesired behaviors.

Integration tests often run much slower than unit testing due to the fact that they
interact with real system, such as databases, message queues, and external APIs. Strive to
make integration tests as efficient as possible by optimizing setup and tear down using
automation and infrastructure as code (IaC). Optimize test execution by running tests in
parallel where possible. This allows for quicker feedback loops and makes it possible to run
integration tests through continuous integration pipelines.

While integration tests should involve real components, they should still be isolated
from production or shared environments where possible. This helps ensure that tests do not
inadvertently affect real data or services. Consider using dedicated emulation, containers,
or cloud-based test environments to make tests more efficient, consistent, and safe.

Just as with unit tests, adopting [Test-Driven Development (TDD)](https://www.agilealliance.org/glossary/tdd/) by
writing tests before the software is developed helps to highlight potential integration pain
points early, and verifies that the interfaces between components are correctly implemented
from the start.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL12-BP03 Test
functional requirements](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_test_functional.html)
- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/application-pipeline/index.html)
- [Getting
started with testing serverless applications](https://aws.amazon.com/blogs/compute/getting-started-with-testing-serverless-applications/)
- [Amazon's
approach to high-availability deployment: Integration
testing](https://youtu.be/bCgD2bX1LI4?t=1480)
- [Building
hexagonal architectures on AWS - Write and run tests from
the beginning](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/best-practices.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.ft.2-validate-system-interactions-and-data-flows-with-integration-tests.html*
