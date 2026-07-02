**Saga**: Quality assurance
**Capability**: QA.TEM — Test environment management

---

# [QA.TEM.3] Store and manage test results

**Category:** FOUNDATIONAL

When tests are run, the results offer insights into the system's health, providing
actionable feedback for developers. Establish a structured test result storage strategy to
maintain the integrity, relevance, and availability of these results.

Store test results in a centralized system or platform using a
machine-readable format, such as JSON or XML. This simplifies
comparison and analysis of test results across various test
iterations. Configure automated deployment pipelines and
individual testing tools to publish test results to this
platform immediately upon test completion. Each set of test
outcomes should be both timestamped and versioned to enable
historical tracking of changes, improvements, or potential
regressions.

Test results must be encrypted both at rest and in transit to
protect against sensitive data inadvertently being stored in
test results. Access to raw test result files should be
limited and idempotent, with write access explicitly
restricted. To view results on a regular basis, implement
tools that allow for visualizations, such as dashboards,
charts, or graphs, which provide a summarized view of test
results. Grant users and roles access to these tools to review
results, identify trends or anomalies, and build reports.

Old test results, while useful for historical context, might not always be necessary
to retain indefinitely. Define a policy for test result retention that aligns to your
governance and compliance requirements. Ideally, this includes automatically archiving or
delete test results to help ensure the system remains uncluttered and cost efficient.

**Related information:**

- [Viewing
the results of a test action - Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/test-view-results.html)
- [Working
with test reporting in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/test-reporting.html)
- [Test
Reports with AWS CodeBuild](https://aws.amazon.com/blogs/devops/test-reports-with-aws-codebuild/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.tem.3-store-and-manage-test-results.html*
