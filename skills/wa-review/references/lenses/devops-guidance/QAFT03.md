**Saga**: Quality assurance
**Capability**: QA.FT — Functional testing

---

# [QA.FT.3] Confirm end-user experience and functional correctness with acceptance tests

**Category:** FOUNDATIONAL

Acceptance tests evaluate the observable functional behavior
of the system from the perspective of the end user in a
production-like environment. These tests encompass functional
correctness of user interfaces, general application behavior,
and ensuring that user interface elements lead to expected
user experiences.

By considering all facets of user interactions and expectations, acceptance testing
provides a comprehensive evaluation of an application's readiness for production deployment.
There are various forms of functional acceptance tests which should be used throughout
development lifecycle:

- **End-To-End (E2E) Testing:** Acceptance tests performed by
the development team through delivery pipelines to validate integrated components and
user flows. Begin by identifying the most impactful user flows and create test cases for
them. Ideally, teams practice [Behavior-Driven Development (BDD)](https://www.agilealliance.org/glossary/bdd/) to define how the system will be designed
to be tested before code is written. Next, adopt a suitable automated testing framework,
such as [AWS Device Farm](https://aws.amazon.com/device-farm/) or [Selenium](https://www.selenium.dev/documentation/). Using the continuous
delivery pipeline, trigger the testing tool to run scripted tests cases against the
system while it is running in the test environment.
- **User Acceptance Testing (UAT):** Acceptance tests
performed by external end-users of the system to validate that the system aligns with
business needs and requirements. The users measure the application against defined
acceptance criteria by interacting with the system and providing feedback based on if
the system behaves as expected. The development team engages, instructs, and supports
these users as they test the system. Log the results of the test by gathering feedback
from the users, using the acceptance criteria as a guide. Feedback should highlight
areas where the system met or exceeded expectations as well as areas where the system
did not meet expectations.
- **Synthetic Testing:** Continuously run simulations of user
behavior in a live testing environment to proactively spot issues. Define the metrics
you want to test, such as response times or error rates. Choose a preferred tool that
integrates well with your desired programming tools and frameworks. Write automated test
scripts which simulate user interactions against the user interface and APIs of the
system. These scripts should be regularly run by the synthetic testing tool in the
testing environment. Synthetic tests can also be used to perform continuous application
performance monitoring in production environments for observability purposes.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF01-BP06 Benchmark
existing workloads](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_performing_architecture_benchmark.html)
- [AWS Well-Architected Reliability Pillar: REL12-BP03 Test
functional requirements](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_test_functional.html)
- [Behavior
Driven Development (BDD)](https://www.agilealliance.org/glossary/bdd/)
- [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/application-pipeline/index.html)
- [Getting
started with testing serverless applications](https://aws.amazon.com/blogs/compute/getting-started-with-testing-serverless-applications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.ft.3-confirm-end-user-experience-and-functional-correctness-with-acceptance-tests.html*
