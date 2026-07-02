**Saga**: Quality assurance
**Capability**: QA.TEM — Test environment management

---

# [QA.TEM.5] Run tests in parallel for faster results

**Category:** RECOMMENDED

Parallelized test execution is the practice of concurrently
running multiple test cases or suites to accelerate test
results and expedite feedback. As software grows and becomes
more modular, especially in architectures like microservices,
the number of test cases also increases. Running these tests
sequentially could significantly slow down delivery pipelines.
By creating many test beds and distributing test cases across
them asynchronously, tests can be run in parallel to allow for
faster iterations and more frequent deployments.

Adopt a scaling-out strategy to test bed provisioning to establish multiple test beds
tailored for specific test scenarios. Each test bed, provisioned through infrastructure as
code (IaC), should have the necessary infrastructure and data setup for its designated
test cases. Serverless infrastructure or container orchestration tools combined with state
machines, such as [AWS Step Functions](https://aws.amazon.com/step-functions/), can
improve your ability to dynamically provision and run tests in a scalable and
cost-effective way. Test operations should not impact the data or outcome of other test
beds. As tests are parallelized across multiple test beds, ensure data isolation to
maintain test integrity. Use monitoring solutions to track parallelized test runs,
ensuring each test bed is performing optimally and to help in debugging any anomalies.

**Related information:**

- [Run
Selenium tests at scale using AWS Fargate](https://aws.amazon.com/blogs/opensource/run-selenium-tests-at-scale-using-aws-fargate/)
- [Runs
in AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-runs.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.tem.5-run-tests-in-parallel-for-faster-results.html*
