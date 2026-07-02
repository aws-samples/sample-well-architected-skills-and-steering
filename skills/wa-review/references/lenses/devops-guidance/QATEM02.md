**Saga**: Quality assurance
**Capability**: QA.TEM — Test environment management

---

# [QA.TEM.2] Ensure consistent test case execution using test beds

**Category:** FOUNDATIONAL

Test cases require specific conditions and test data to
run in a predetermined state. Test beds, configured within
broader testing environments, provide the conditions necessary
to ensure reproducible and accurate test case execution. While
a single testing environment, such as a staging environment,
can host multiple test beds, each test bed is tailored with
the infrastructure and data suitable for specific test
scenarios. Being able to start each test case with the correct
configuration and data setup makes testing reliable,
consistent, and confirms that anomalies or failures can be
attributed to code changes rather than data inconsistencies.

Integrate test bed preparation into the delivery pipeline, leveraging infrastructure
as code (IaC) to help guarantee consistent test bed setup. Rather than updating or patching
test beds, use immutable infrastructure and treat them as ephemeral environments. When a
test is run, create a new test bed using IaC tools to help ensure that it is clean and
consistent. It is advantageous to have a fresh environment for each test. However, after
running the tests, while the test bed can be deleted, it is important to avoid deleting logs
and data that can aid with debugging the testing process. This data may be required for
analyzing failures. Deleting it prematurely can lead to wasted time and the potential need
for rerunning lengthy tests.

Use data restoration techniques to automate populating
test beds with test data specific to the test case being
run. Depending on the complexity, the test data can be
generated on-demand or sourced from a centralized test data
store for scalability and consistency. For tests that modify
data and require reruns, use a caching system to quickly and
cost-effectively revert the dataset, minimizing bottlenecks in
the testing process. Automating test data restoration saves
time and effort for teams, enabling them to focus on actual
testing activities instead of manually test data management.

Continually monitor the speed, accuracy, and relevance of test bed setup and
execution. As testing requirements evolve or data volume and complexity grow, make necessary
adjustments. Provide immediate feedback to the development team if there is a failure
arising from test bed setup, data inconsistency, or test execution.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS06-BP03
Increase utilization of build environments](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a4.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.tem.2-ensure-consistent-test-case-execution-using-test-beds.html*
