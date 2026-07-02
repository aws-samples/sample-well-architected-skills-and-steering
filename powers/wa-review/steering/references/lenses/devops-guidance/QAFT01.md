**Saga**: Quality assurance
**Capability**: QA.FT — Functional testing

---

# [QA.FT.1] Ensure individual component functionality with unit tests

**Category:** FOUNDATIONAL

Unit tests evaluate the functionality of one individual part of an application,
called *units*. The goal of unit tests is to provide fast, thorough
feedback while reducing the risk of introducing flaws when making changes. This feedback is
accomplished by writing tests cases that cover a sufficient amount of the code. These test
cases run the code using predefined inputs and set expectations for a specific output.

Unit tests should be isolated to a single class, function, or method within the code.
Fakes or mocks are used in place of external or infrastructure components to help ensure
that the scope is isolated. These tests should be fast, repeatable, and provide assertions
that lead to a pass or fail outcome. Teams should be able to run unit tests locally as well
as through continuous integration pipelines.

Ideally, teams adopt [Test-Driven Development (TDD)](https://www.agilealliance.org/glossary/tdd/) practices and write tests before the software is
developed. This approach can lead to faster feedback, more effective tests, and introducing
less defects when writing code.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL12-BP03 Test
functional requirements](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_test_functional.html)
- [Building
hexagonal architectures on AWS - Write and run tests from
the beginning](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/best-practices.html)
- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/application-pipeline/index.html)
- [Testing
software and systems at Amazon: Unit tests](https://youtu.be/o1sc3cK9bMU?t=930)
- [Adopt
a test-driven development approach using AWS CDK](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/development-best-practices.html)
- [Getting
started with testing serverless applications](https://aws.amazon.com/blogs/compute/getting-started-with-testing-serverless-applications/)
- [TestDouble](https://martinfowler.com/bliki/TestDouble.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.ft.1-ensure-individual-component-functionality-with-unit-tests.html*
