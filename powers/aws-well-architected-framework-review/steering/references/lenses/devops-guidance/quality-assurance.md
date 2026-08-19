# Quality assurance

**Saga**: Quality assurance  
**Best Practices**: 31

---

**Capability**: QA.DT — Data testing

# [QA.DT.1] Ensure data integrity and accuracy with data quality tests

**Category:** RECOMMENDED

Data quality tests assess the accuracy, consistency, and overall quality of the data
used within the application or system. These tests typically involve validating data
against predefined rules and checking for duplicate or missing data to ensure the dataset
remains reliable. While data quality testing might not fall under the traditional
definitions of functional or non-functional testing, it's still an essential aspect of
ensuring that an application or system functions correctly, as the quality of data can
significantly impact the overall performance, user experience, and reliability of the
software.

We recommend data quality tests because they enable rapid
software delivery and continuous improvement of data driving
systems. Using data quality tests, teams can spend more of
their time focusing on how data should appear rather than
continually checking it for accuracy, streamlining the
development and deployment process. To calculate data quality
metrics on your dataset, define and verify data quality
constraints, and be informed about changes in the data
distribution. Instead of implementing checks and verification
algorithms on your own, you can focus on describing how your
data should look.

**Related information:**

- [Getting
started with AWS Glue Data Quality from the AWSAWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/)
- [Deequ
- Unit Tests for Data](https://github.com/awslabs/deequ)
- [Test
data quality at scale with Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/)
- [How
to Architect Data Quality on the AWS Cloud](https://aws.amazon.com/blogs/industries/how-to-architect-data-quality-on-the-aws-cloud/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.1-ensure-data-integrity-and-accuracy-with-data-quality-tests.html*

---

**Capability**: QA.DT — Data testing

# [QA.DT.2] Enhance understanding of data through data profiling

**Category:** OPTIONAL

Use data profiling tools to examine, analyze, and understand
the data including its content, structure, and relationships
to identify issues such as inconsistencies, outliers, and
missing values. By performing data profiling, teams can gain
deeper insights into the characteristics and quality of their
data, enabling them to make informed decisions about data
management, data governance, and data integration strategies.
This data is often used to enable or improve other types of
data testing.

To integrate data profiling into a DevOps environment,
consider automating the process using data profiling tools
such as
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/), open-source tools, or custom scripts
that analyze data regularly. Incorporate the profiling results
into your data management, governance, and integration
strategies, allowing your team to proactively address data
quality issues and maintain consistent data standards
throughout the development lifecycle.

**Related information:**

- [Build
an automatic data profiling and reporting solution with
Amazon EMR, AWS Glue, and Quick](https://aws.amazon.com/blogs/big-data/build-an-automatic-data-profiling-and-reporting-solution-with-amazon-emr-aws-glue-and-amazon-quicksight/)
- [Test
data quality at scale with Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/)
- [Deequ
single column profiling](https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/examples/data_profiling_example.md)
- [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.2-enhance-understanding-of-data-through-data-profiling.html*

---

**Capability**: QA.DT — Data testing

# [QA.DT.3] Validate data processing rules with data logic tests

**Category:** OPTIONAL

Data logic tests verify the accuracy and reliability of data
processing and transformation within your application,
ensuring that it functions as intended.

Establish test cases for data processing workflows and transformation functions,
confirming that expected outcomes are achieved. Use version control systems to track
changes in data logic and collaborate effectively with team members. Implement automated
data logic tests in development and staging environments, which can be triggered by code
commits or scheduled intervals, to proactively identify and fix issues before they reach
production environments.

**Related information:**

- [Test
data quality at scale with Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/)
- [Deequ
automatic suggestion of constraints](https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/examples/constraint_suggestion_example.md)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.3-validate-data-processing-rules-with-data-logic-tests.html*

---

**Capability**: QA.DT — Data testing

# [QA.DT.4] Detect and mitigate data issues with anomaly detection

**Category:** OPTIONAL

Data anomaly detection is a specialized form of anomaly
detection which focuses on identifying unusual patterns or
behaviors in data quality metrics that may indicate data
quality issues.

Consider integrating machine learning algorithms and
statistical methods into your data quality monitoring
processes. Use tools that can detect and address data
anomalies in real-time and incorporate them into your
development and deployment workflows. This enables automated
assessment of the accuracy and reliability of data processing
and analysis, enhancing the overall performance of your
applications and systems.

**Related information:**

- [What
Is Anomaly Detection?](https://aws.amazon.com/what-is/anomaly-detection/)
- [Test
data quality at scale with Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/)
- [Deequ
anomaly detection](https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/examples/anomaly_detection_example.md)
- [Amazon
Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/)
- [Introducing
Amazon Lookout for Metrics: An anomaly detection service
to proactively monitor the health of your business](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-lookout-for-metrics-an-anomaly-detection-service-to-proactively-monitor-the-health-of-your-business/)
- [Quick: ML-powered anomaly detection for
outliers](https://docs.aws.amazon.com/quicksight/latest/user/anomaly-detection-function.html)
- [Amazon Kinesis: Detecting Data Anomalies on a Stream](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/app-anomaly-detection.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.4-detect-and-mitigate-data-issues-with-anomaly-detection.html*

---

**Capability**: QA.DT — Data testing

# [QA.DT.5] Utilize incremental metrics computation

**Category:** OPTIONAL

Incremental metrics computation allows teams to efficiently
monitor and maintain data quality without needing to recompute
metrics on the entire dataset every time data is updated. Use
this method to significantly reduce computational resources
and time spent on data quality testing, allowing for more
agile and responsive data management practices.

Start by identifying the specific data quality metrics that
are essential for your system. This could include metrics
related to accuracy, completeness, timeliness, and
consistency. Depending on your dataset's size and complexity,
select a tool or framework that supports incremental
computation. Some modern data processing tools, such
as [Apache
Spark](https://spark.apache.org/)
and [Deequ](https://github.com/awslabs/deequ),
provide built-in support for incremental computations.

Segment your data into logical partitions, often based on
time, such as daily or hourly partitions. As new data is
added, it becomes a new partition. Automate the computation
process by setting up triggers that initiate the metric
computation whenever new data is added or an existing
partition is updated.

Continuously monitor the updated metrics to help ensure they reflect the true state
of your data. Periodically validate the results of the incremental metrics computation
against a full computation to ensure accuracy. As you get more familiar with the process,
look for ways to optimize the computation to save even more on computational resources.
This could involve refining your partitions or improving the computation logic.

**Related information:**

- [Deequ
stateful metrics computation](https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/examples/algebraic_states_example.md)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.5-utilize-incremental-metrics-computation.html*

---

**Capability**: QA.FT — Functional testing

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

---

**Capability**: QA.FT — Functional testing

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

---

**Capability**: QA.FT — Functional testing

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

---

**Capability**: QA.FT — Functional testing

# [QA.FT.4] Balance developer feedback and test coverage using advanced test selection

**Category:** OPTIONAL

In traditional software models, regression testing was a distinct form of functional
testing, designed to ensure that new code integrations did not disrupt existing system
functionalities. In a DevOps model, there is a new perspective: regression testing is no
longer a testing activity with human involvement. Instead, every change triggers automated
pipelines that conduct a new cycle of tests, making each pipeline execution effectively a
*regression test*. As systems become more complex over time, so do
the test suites. Running all tests every time a change is made can become time-consuming
and inefficient as test suites grow, slowing down the development feedback loop.

Before choosing to implement advanced test selection methods using machine learning
(ML). you should first optimize test execution through parallelization, reducing stale or
ineffective tests, improving the infrastructure the tests are run on, and changing the
order of tests to optimize for faster feedback. If these methods do not produce sufficient
outcomes, there are algorithmic and ML methods that provide advanced test selection
capabilities.

Test Impact Analysis (TIA) offers a structured approach to
advanced test selection. By examining the differences in the
codebase, TIA determines the tests that are most likely to be
affected by the recent changes. This results in running only a
relevant subset of the entire test suite, ensuring efficiency
without the need for machine learning models.

Predictive test selection is an evolving approach to test
selection which uses ML models trained on historical code
changes and test outcomes to determine how likely a test is to
reveal errors based on the change. This results in a subset
of tests to run tailored to the specific change that are
most likely to detect regressions. Predictive test selection
strikes a balance between providing faster feedback to
developers and thorough test coverage.

Using ML for this purpose introduces a level of uncertainty
into the quality assurance process. If you do choose to
implement predictive test selection, we recommend putting
additional controls in place, including:

- Add manual approval stages that require developers to
assess and accept the level of tests that will be run
before they run. These manual approvals allow the team
to decide if the test coverage trade-off makes sense and
to accept the risk for the given change.
- Provide eventual consistency of test results by running
the full set of tests asynchronously outside of the
development workflow. If there are tests that fail at this
stage, provide feedback to the development team so that
they can triage the issues and decide if they need to roll
back the change.
- We do not recommend using predictive test selection to
exclude security-related tests or relying on this approach
for sensitive systems which are critical to your business.

**Related information:**

- [Predictive
Test Selection](https://research.facebook.com/publications/predictive-test-selection/)
- [Machine
Learning - Amazon Web Services](https://aws.amazon.com/sagemaker/)
- [The
Rise of Test Impact Analysis](https://martinfowler.com/articles/rise-test-impact-analysis.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.ft.4-balance-developer-feedback-and-test-coverage-using-advanced-test-selection.html*

---

**Capability**: QA.NT — Non-functional testing

# [QA.NT.1] Evaluate code quality through static testing

**Category:** FOUNDATIONAL

Static testing is a proactive method of assessing the quality of code without needing
to run it. It can be used to test application source code, as well as other design
artifacts, documentation, and infrastructure as code (IaC) files. Static testing allows
teams to spot misconfigurations, security vulnerabilities, or non-compliance with
organizational standards in these components before they get applied in a real environment.

Static testing should be available to developers on-demand in local environments, as
well as automatically run in automated pipelines. Use static testing to run automated code
reviews and detect defects early on to provide fast feedback to developers. This feedback
enables developers to fix and remove bugs before deployment, which is much easier and cost
effective than fixing them after deployment.

Use specialized static analysis tools tailored to the type of
code you are using. For example, tools
like [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) and
[cfn-lint](https://github.com/aws-cloudformation/cfn-lint)
are designed to catch issues in
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates. These tools can be configured
to detect issues like insecure permissions, enforcing tagging
standards, or misconfigurations that could make infrastructure
vulnerable. Keep your static analysis tools updated and
regularly review their findings to adapt to changing
infrastructure security and compliance best practices.

**Related information:**

- [What
is Amazon CodeGuru Reviewer?](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html)
- [Checkov](https://www.checkov.io/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.1-evaluate-code-quality-through-static-testing.html*

---

**Capability**: QA.NT — Non-functional testing

# [QA.NT.2] Validate system reliability with performance testing

**Category:** RECOMMENDED

Performance testing evaluates the responsiveness, throughput, reliability, and
scalability of a system under a specific load. It helps ensure that the application
performs adequately when it is subjected to both expected and peak loads without impacting
user experience. Different performance tests should be run based on the nature of changes
made to the system:

- **Load testing:** Performance tests evaluating the
system's behavior under expected load, such as the typical number of concurrent users
or transactions. Integrate automated load testing into your deployment pipeline,
ensuring every change undergoes validation of system behavior under expected
scenarios.
- **Stress testing:** Performance tests challenging the
system by increasing the load beyond its normal operational capacity. Stress tests
identify the system's breaking points, ensuring that even under extreme conditions,
the system maintains functionality without abrupt crashes. Schedule stress tests after
significant application changes, infrastructure modifications, or periodically—such as
once a month—to prepare for unpredictable spikes in traffic or potential DDoS attacks.
- **Endurance testing:** Performance tests that monitor
system behavior over extended periods of time under a specific load. Endurance tests
help ensure that there are no latent issues, such as slow memory leaks or performance
degradation, which might occur after prolonged operations. Monitor key performance
indicators over time and compare against established benchmarks to identify latent
issues. Schedule endurance tests after significant changes to the system, especially
those that might introduce memory leaks or other long-term issues. Consider running
them periodically—such as quarterly or biannually—to ensure system health over
prolonged operations.

All performance tests should be run against a test
environment mirroring the production setup. Use tailored
performance testing tools for your application's architecture
and deployment environment. Regularly analyze test results
against historical benchmarks and take proactive measures to
counteract performance regressions.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF01-BP07 Load test
your workload](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_performing_architecture_load_test.html)
- [AWS Well-Architected Sustainability Pillar: SUS03-BP03
Optimize areas of code that consume the most time or resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html)
- [AWS Well-Architected Reliability Pillar: REL07-BP04 Load test
your workload](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_load_tested_adapt.html)
- [AWS Well-Architected Reliability Pillar: REL12-BP04 Test
scaling and performance requirements](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_test_non_functional.html)
- [Ensure
Optimal Application Performance with Distributed Load
Testing on AWS](https://aws.amazon.com/blogs/architecture/ensure-optimal-application-performance-with-distributed-load-testing-on-aws/)
- [Stress
Testing Tools - AWS Fault Injection Service](https://aws.amazon.com/fis/)
- [Find
Expensive Code – Amazon CodeGuru Profiler](https://aws.amazon.com/codeguru/features/)
- [Load
test your applications in a CI/CD pipeline using CDK
pipelines and AWS Distributed Load Testing Solution](https://aws.amazon.com/blogs/devops/load-test-applications-in-cicd-pipeline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.2-validate-system-reliability-with-performance-testing.html*

---

**Capability**: QA.NT — Non-functional testing

# [QA.NT.3] Prioritize user experience with UX testing

**Category:** RECOMMENDED

User experience (UX) testing provides insight into the
system's user interface and overall user experience, ensuring
that they align with the diverse requirements of its user
base. Adopting UX testing ensures that as the system evolves,
its design remains intuitive, functional, and inclusive for
end users.

Recognize that UX is subjective and can vary based on
demographics, tech proficiency, and individual preferences.
Segment your tests to understand the diverse needs and
preferences of your user base. This means creating different
user profiles and scenarios, ensuring that the software is
tested from multiple perspectives. There are various forms of
non-functional UX tests which should be utilized to target
specific improvements:

- **Usability testing:** UX tests determines the ease with
which users can perform tasks using the application and evaluates if the interface is
intuitive and user-friendly. Usability testing helps identify issues related to the
application's design, navigation, and overall ease of use, ultimately leading to
building a better product. Conduct usability testing by recruiting a diverse group of
testing participants that represent the broader user base. Provide these users with
typical tasks they would perform when using the application. Observe the testing
participants and their interactions, note areas where they encounter challenges,
confusion, or get frustrated. During observation, encourage the participants to
verbalize their thought process as they perform the tasks. After the tasks are
completed, conduct a brief feedback session to gather additional perspective on their
use of the application. Use this data to drive user experience improvements and to fix
any bugs that were discovered. To continuously gather feedback over time, ensure that
there are mechanisms for users to provide feedback as they interact with the system.
- **Accessibility testing:** UX tests that evaluate the
application to ensure that it can be accessed and used by everyone. Regularly review
web content accessibility guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) to ensure
compliance with the latest standards. To get started quickly, consider adopting an
existing design system which incorporates accessibility best practices and a framework
to create accessible applications, such as the [Cloudscape Design System](https://cloudscape.design/). Automate accessibility tests as a part of the
development lifecycle using tools like [Axe](https://www.deque.com/axe/) or [WAVE](https://wave.webaim.org/). Adopt tools that
evaluate specific accessibility standards, such as color contrast analyzing tools like
[WebAim](https://webaim.org/resources/contrastchecker/). Consider
regularly conducting manual exploratory tests using assistive technologies to capture
issues that automated tools might miss.

**Related information:**

- [Usability
Evaluation Methods](https://www.usability.gov/how-to-and-tools/methods/usability-evaluation/index.html)
- [W3C
standards](https://www.w3.org/WAI/fundamentals/accessibility-principles/)
- [WCAG
2.1 AA](https://www.w3.org/WAI/WCAG21/Understanding/conformance#levels)
- [Web
Accessibility Initiative (WAI)](https://www.w3.org/WAI/design-develop/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.3-prioritize-user-experience-with-ux-testing.html*

---

**Capability**: QA.NT — Non-functional testing

# [QA.NT.4] Enhance user experience gradually through experimentation

**Category:** RECOMMENDED

Enhancing user experience requires taking a methodical
approach to assessing how users behave when using your
application and developing features that resonate with users.
The goal of running experiments is to identify and implement
the best possible user experience based on indirect user
behavior. With experiments, teams can proactively assess the
impact of new features on a subset of users before a
full-scale rollout, reducing the risk of making the change and
negatively impacting user experience.

A popular technique for conducting experiments is A/B testing,
also known as split testing. To run split testing experiments,
present different versions of the application to a small
segment of real users to gather detailed feedback on specific
changes. This testing is done in a production environment
alongside the production application. By directing only a
small subset of the users to the version of the application
with the change, teams are able to conduct experiments while
hiding the new feature from the majority of the user base not
included in the test. Testing a feature within a smaller
sample, rather than the entire user group, minimizes potential
disruptions and yields more detailed data in a real-world
setting.

Teams can control the experiment
using [feature
flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) or dedicated tools
like [CloudWatch
Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.html) to control variables and traffic to the
different versions of the application. Ensure the experiment
runs for the necessary duration to achieve statistical
significance and use consistent metrics to track customer
behavior across the variations to maintain accuracy. Compare
the metrics after the experiment to make decisions.

**Related information:**

- [Perform
launches and A/B experiments with CloudWatch
Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.html)
- [Feature
Flags - AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [Business
Value is IT's Primary Measure of Progress](https://aws.amazon.com/blogs/enterprise-strategy/business-value-is-its-primary-measure-of-progress/)
- [Blog: Using
A/B testing to measure the efficacy of recommendations
generated by Amazon Personalize](https://aws.amazon.com/blogs/machine-learning/using-a-b-testing-to-measure-the-efficacy-of-recommendations-generated-by-amazon-personalize/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.4-enhance-user-experience-gradually-through-experimentation.html*

---

**Capability**: QA.NT — Non-functional testing

# [QA.NT.5] Automate adherence to compliance standards through conformance testing

**Category:** RECOMMENDED

Conformance testing, often referred to as compliance testing, verifies that a system
meets internal and external compliance requirements. It compares the system's behaviors,
functions, and capabilities with predefined criteria from recognized standards or
specifications.

Conformance testing acts as a safeguard, ensuring that while agility is prioritized,
compliance isn't compromised. There are many regulated industries, such as finance,
healthcare, or aerospace, that have a strict set of compliance requirements which must be
met when delivering software. Historically, balancing fast software delivery with
stringent compliance was a challenge in these industries. Generating the documentation and
proof required to maintain compliance was often a manual, time-intensive step that created
a bottleneck at the end of the development lifecycle.

Conformance testing integrated into deployment pipelines provides a solution to this
problem by automating the creation of compliance attestations and documentation. It can be
used to meet both internal and external compliance requirements. Start by determining both
internal (for example, risk assessment policies, or change management procedures) and
external standards (for example, [GxP](https://aws.amazon.com/compliance/gxp-part-11-annex-11/) for life sciences). Prioritize and
choose the relevant parts of the standards which can be automated (for example, GxP
Installation Qualification report). Ensure that conformance tests remain current by
updating them according to evolving standards.

Use the data at your disposal, including APIs, output from other forms of testing,
and possibly additional data from IT Service Management (ITSM) and Configuration
Management Databases (CMDB). Embed conformance testing scripts into deployment pipelines
to generate real-time compliance attestations and documentation using this data. Consider
using machine-readable markup languages, such as JSON and YAML, to store the compliance
artifacts. If the markup languages are not considered sufficiently human readable by
auditors, then retain the ability to convert these markdown files into another format.
This conversion can then be done when needed, not as a default step, removing the burden
of document management where it is not absolutely necessary.

**Related information:**

- [Wikipedia
- Conformance testing](https://en.wikipedia.org/wiki/Conformance_testing)
- [Qualification
Strategy for Life Science Organizations](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/qualification-strategy-for-life-science-organizations.html)
- [Automating
the Installation Qualification (IQ) Step to Expedite GxP
Compliance](https://aws.amazon.com/blogs/industries/automating-the-installation-qualification-iq-step-to-expedite-gxp-compliance/)
- [Automating
GxP compliance in the cloud: Best practices and
architecture guidelines](https://aws.amazon.com/blogs/industries/automating-gxp-compliance-in-the-cloud-best-practices-and-architecture-guidelines/)
- [Automating
GxP Infrastructure Installation Qualification on AWS with
Chef InSpec](https://aws.amazon.com/blogs/industries/automating-gxp-infrastructure-installation-qualification-on-aws-with-chef-inspec/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.5-automate-adherence-to-compliance-standards-through-conformance-testing.html*

---

**Capability**: QA.NT — Non-functional testing

# [QA.NT.6] Experiment with failure using resilience testing to build recovery preparedness

**Category:** RECOMMENDED

Resilience testing deliberately introduces controlled failures
into a system to gauge its ability to withstand failure and
recover during disruptive scenarios. Simulating failures in
different parts of the system provides insight into how
failures propagate and affect other components. This helps
identify bottlenecks or single points of failure in the
system.

Before initiating any resilience tests, especially in
production, understand the potential impact on the system,
dependent systems, and the operating environment. Start small
with less invasive tests and gradually expand the scope and
frequency of these tests. This iterative approach allows you
to understand the ramifications of a particular failure and
ensures that you don't accidentally cause a significant
disruption.

There are various types of resilience testing:

- **Chaos engineering:** Resilience tests using fault
injection to introduce controlled failures into the system. This can include
simulating service failures, region outages, single node failures, network outages, or
complete failovers of connected systems. Controlled failures enable teams to identify
system vulnerabilities, ensuring weaknesses introduced by deployments and
infrastructure changes are mitigated. Fault injection tools, such as [AWS Fault Injection Service](https://aws.amazon.com/fis/) and [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/), can assist in conducting these experiments.
Embed the use of these tools into automated pipelines to run fault injection tests
after deployment.
- **Data recovery testing:** Resilience tests that verify
that specific datasets can be restored from backups. Data recovery tests ensure that
the backup mechanism is effective and that the restore process is reliable and
performant. Schedule data recovery tests periodically, such as monthly, quarterly, or
after major data changes or migrations. Initiate these tests through deployment
pipelines. For example, after a database schema deployment, run a test to ensure that
the new schema doesn't compromise backup integrity.
- **Disaster recovery testing:** Resilience tests that help
ensure the entire system can be restored and made operational after large scale
events, such as data center outages. This includes activities such as restoring
systems from backups, switching to redundant systems, or transitioning traffic to a
disaster recovery environment. These tests are extensive and therefore run less
frequently, such as semi-annually or annually. When running in production
environments, these tests are usually performed during maintenance windows or off-peak
hours, and stakeholders are informed well in advance. Use disaster recovery tools,
such as [AWS Elastic Disaster
Recovery](https://aws.amazon.com/disaster-recovery/) and [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/), to assist with planning, coordinating, and performing recovery
actions. While integrating these tests fully into deployment pipelines is rare, it is
possible to automate sub-tasks or preliminary checks. For example, after significant
infrastructure changes, a test might check the functionality of failover mechanisms to
ensure they still operate as expected. It can often be more effective to trigger these
tests based on events or manual triggers, especially earlier on in your DevOps
adoption journey.

Before running resilience tests in either test or production environments, consider
the use case, the benefits of the test, and the system's readiness. Regardless of the
target environment, always inform all stakeholders of the system before executing
significant resilience tests. Have a pre-prepared, comprehensive communication plan in the
event of unforeseen challenges or downtime. We recommend initially running resilience
tests in a test environment to get an understanding of their effects, refine the testing
process, and train the team.

After gaining confidence in the testing process and building the necessary
observability and rollback mechanisms to run them safely, consider running controlled
tests in production to gain the most accurate representation of recovery scenarios in
real-world settings. When executing in production, limit the impact of your tests. For
example, if you are testing the resilience of a multi-Region application, don't bring down
all Regions at once. A better approach would be to start with one Region, observe its
behavior, and learn from the results. After running resilience tests, conduct a
retrospective to understand what went well, any unexpected behaviors, improvements that
can be made, and to plan work to enhance both the system's resilience and the testing
process itself.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL09-BP04 Perform
periodic recovery of the data to verify backup integrity and processes](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html)
- [AWS Well-Architected Reliability Pillar: REL12-BP05 Test
resiliency using chaos engineering](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_failure_injection_resiliency.html)
- [AWS Well-Architected Reliability Pillar: REL13-BP03 Test
disaster recovery implementation to validate the implementation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_dr_tested.html)
- [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html)
- [Well-Architected
Lab - Testing for Resiliency](https://wellarchitectedlabs.com/reliability/300_labs/300_testing_for_resiliency_of_ec2_rds_and_s3/)
- [Fault
testing on Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fis.html)
- [Chaos
experiments on Amazon RDS using AWS Fault Injection Service](https://aws.amazon.com/blogs/devops/chaos-experiments-on-amazon-rds-using-aws-fault-injection-simulator/)
- [Chaos
Testing with AWS Fault Injection Service and AWS CodePipeline](https://aws.amazon.com/blogs/architecture/chaos-testing-with-aws-fault-injection-simulator-and-aws-codepipeline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.6-experiment-with-failure-using-resilience-testing-to-build-recovery-preparedness.html*

---

**Capability**: QA.NT — Non-functional testing

# [QA.NT.7] Verify service integrations through contract testing

**Category:** RECOMMENDED

Contract testing helps ensure that different system components
or services can seamlessly communicate and are compatible with
each other. This involves creating contracts that detail
interactions between services, capturing everything from
request structures to expected responses. As changes are made,
these contracts can be used by producing (teams that expose
the API) and consuming (teams that use the API) services to
ensure they remain compatible. Contract testing provides a
safety net for both producers and consumers by ensuring
changes in one do not adversely impact the other. This creates
a culture of collaboration between teams while providing
faster feedback for identifying integration issues earlier in
the development lifecycle.

There are different types of contract testing. In
consumer-driven contract testing, the consumer of a service
dictates the expected behaviors of the producer. This is
contrasted with provider-driven approaches, where the producer
service determines its behaviors without explicit input from
its consumers. Consumer-driven contract testing is the type we
generally recommend, as designing contracts with the consumer
in mind ensures that APIs are tailored to the customer's
actual needs, making integrations more intuitive.

Begin by clearly defining contracts between your services. Use
purpose-built contract testing tools, such
as [Pact](http://Pact.io)
or [Spring
Cloud Contract](https://spring.io/projects/spring-cloud-contract/), to simplify managing and validating
contracts. When any modification is made in a producer
service, run contract tests to assess the contracts'
validity. Similarly, before a consumer service integrates with
a producer, run the relevant contract tests to guarantee
they'll interact correctly. This process allows producers to
maintain backwards compatibility, while allowing consumers to
identify and fix potential integration issues early in the
development lifecycle. Embed contract testing into your
deployment pipeline. This ensures continuous validation of
contracts as changes are made to services, promoting a
continuous and consistent integration process.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL03-BP03 Provide
service contracts per API](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_service_architecture_api_contracts.html)
- [Introduction
To Contract Testing With Examples](https://www.softwaretestinghelp.com/contract-testing/)
- [CloudFormation
Command Line Interface: Testing resource types using
contract tests](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.7-verify-service-integrations-through-contract-testing.html*

---

**Capability**: QA.NT — Non-functional testing

# [QA.NT.8] Practice eco-conscious development with sustainability testing

**Category:** OPTIONAL

Sustainability testing ensures that software products contribute to eco-conscious and
energy-efficient practices that reflect a growing demand for environmentally responsible
development. It is a commitment to ensuring software development not only meets
performance expectations but also contributes positively to the organization's
environmental goals. In specific use cases, such as internet of things (IoT) and smart
devices, software optimizations can directly translate to energy and cost savings while
also improving performance.

Sustainability testing encompasses:

- **Energy efficiency**: Create sustainability tests which
ensure software and infrastructure minimize power consumption. For instance, [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) are designed
for enhanced energy efficiency. They offer up to 60% less energy consumption for
similar performance compared to other EC2 instances. Write static analysis tests that
focus on improving sustainability by verifying that infrastructure as code (IaC)
templates are configured to use energy efficient infrastructure.
- **Resource optimization:** Sustainable software leverages
hardware resources, such as memory and CPU, without waste. Sustainability tests can
enforce right-sizing when deploying infrastructure. For example, [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) ensures compute resources
align with actual needs, preventing over-provisioning. Similarly, [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) offers actionable insights into resource provisioning based
on actual consumption patterns.
- **Data efficiency:** Sustainability testing can assess
the efficiency of data storage, transfer, and processing operations, ensuring minimal
energy consumption. Tools like the [AWS Customer Carbon
Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) offer insights into the carbon emissions associated with
various AWS services, such as Amazon EC2 and Amazon S3. Teams can use these insights to make
informed optimizations.
- **Lifecycle analysis:** The scope of testing extends
beyond immediate software performance. For instance, the [AWS Customer Carbon
Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) can provide insights into how using AWS services impacts
carbon emissions. This information can be used to compare this usage with traditional
data centers. Metrics from this tool can be used to inform decisions throughout the
software lifecycle, ensuring that environmental impact remains minimal from inception
to decommissioning of resources.

Sustainability testing should use data provided by profiling
applications to measure their energy consumption, CPU usage,
memory footprint, and data transfer volume. Tools such
as [Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html)
and [SusScanner](https://github.com/awslabs/sustainability-scanner)
can be helpful when performing analysis and promotes writing
efficient, clean, and optimized code. Combining this data with
suggestions from AWS Trusted Advisor and AWS Customer Carbon
Footprint Tool can lead to writing tests which can enforce
sustainable development practices.

Sustainability testing is still an emerging quality assurance
practice. This indicator is beneficial for organizations
focusing on environmental impact. We think that by making
sustainability a core part of the software development
process, not only do we contribute to a healthier planet, but
often, we also end up with more efficient and cost-effective
solutions.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF02-BP04 Determine
the required configuration by right-sizing](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_select_compute_right_sizing.html)
- [AWS Well-Architected Performance Pillar: PERF02-BP06
Continually evaluate compute needs based on metrics](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_select_compute_use_metrics.html)
- [AWS Well-Architected Sustainability Pillar: SUS03-BP03
Optimize areas of code that consume the most time or resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html)
- [AWS Well-Architected Sustainability Pillar: SUS06-BP01 Adopt
methods that can rapidly introduce sustainability improvements](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a2.html)
- [AWS Well-Architected Cost Optimization Pillar: COST09-BP03
Supply resources dynamically](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_dynamic.html)
- [Sustainability
Scanner (SusScanner)](https://github.com/awslabs/sustainability-scanner)
- [AWS Well-Architected Framework - Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/sustainability.html)
- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [Sustainable
Cloud Computing](https://aws.amazon.com/sustainability/)
- [Reducing
carbon by moving to AWS](https://www.aboutamazon.com/news/sustainability/reducing-carbon-by-moving-to-aws)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.8-practice-eco-conscious-development-with-sustainability-testing.html*

---

**Capability**: QA.ST — Security testing

# [QA.ST.1] Evolve vulnerability management processes to be conducive of DevOps practices

**Category:** FOUNDATIONAL

Vulnerability management requires an ongoing, iterative process consistent with agile
development practices. The goal is to discover potential vulnerabilities across networks,
infrastructures, and applications, and to prioritize and take action on them.

Automated vulnerability scanning must be integrated into deployment pipelines to
provide feedback to developers regarding security vulnerabilities and improvements early on.
This minimizes extensive security evaluations during deployment and is consistent with the
DevOps *shift left* approach—addressing security problems early on in the
development process. Choose vulnerability scanning tools that are compatible with your
existing technology and platforms. For instance, if [Amazon CodeCatalyst](https://aws.amazon.com/codecatalyst/) is your pipeline tool of choice, verify that the
chosen vulnerability scanning tool has a CodeCatalyst plugin or API integration capability. If
vulnerabilities are detected during a build, the pipeline should automatically generate
alerts, allowing developers to address issues quickly.

If you use issue-tracking systems like Jira or [CodeCatalyst Issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues.html), it can be
beneficial to automatically generate tickets to assist developers with tracking issues. When
a vulnerability is detected, an automated ticket should be generated, tagged with severity,
and assigned to the appropriate developer or team. Use vulnerability management dashboards
to consistently monitor and analyze threats. Regular reports should detail vulnerability
trends, ensuring vulnerabilities are not reintroduced and pinpointing recurrent security
challenges.

To effectively practice vulnerability management in a DevOps environment, it's
important to adopt a culture where security is everyone's responsibility. Development and
security teams need collaboration, with clear delineations for security issue handoff and
ownership. In a DevOps model, distributed development teams take on security
responsibilities for their products. Centralized security teams often become enabling teams,
offering training, insights, and support. They can also take on the responsibilities of a
security platform team, producing reusable components, improving efficiency, reducing
duplication of work, and overall providing autonomy to distributed teams so that they can
efficiently secure their products.

**Related information:**

- [Enterprise
DevOps: Why You Should Run What You Build](https://aws.amazon.com/blogs/enterprise-strategy/enterprise-devops-why-you-should-run-what-you-build/)
- [Automated
Software Vulnerability Management - Amazon Inspector](https://aws.amazon.com/inspector/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.1-evolve-vulnerability-management-processes-to-be-conducive-of-devops-practices.html*

---

**Capability**: QA.ST — Security testing

# [QA.ST.2] Normalize security testing findings

**Category:** FOUNDATIONAL

Effective vulnerability management requires clarity and
consistency. Given the diversity of security testing tools in
a DevOps environment, findings often emerge from different
sources and in different formats. This diversity of tooling
can introduce confusion and inefficiency into risk management
processes.  Having a common framework for normalizing the
interpretation and ranking of vulnerabilities from diverse
security testing tools provides a systematic approach to risk
management and mitigation. Normalization is not just about
consistency, it helps ensure that every identified
vulnerability is understood, categorized, and managed
according to its threat level.

Begin by selecting a recognized scoring system, such as the
Common Vulnerability Scoring System
([CVSS](https://nvd.nist.gov/vuln-metrics/cvss)),
as the baseline for vulnerability ranking. This will provide a
universal language for risk assessment and
prioritization. Many modern security tools have built-in
integrations with popular scoring systems. Configure your
tools to automatically map their findings to the chosen
system, ensuring uniformity across all results. It is
important to periodically review the normalization process,
updating it as required and ensuring alignment with industry
best practices.

Use tools that can automatically translate findings into the
standardized format. Integrations like the Static Analysis
Results Interchange Format
([SARIF](https://sarifweb.azurewebsites.net/))
or [OCSF
Schema](https://schema.ocsf.io/) can assist with this. These tools can enable
centralizing findings from different sources into a single
dashboard or reporting platform to create a unified view of
the security posture which can streamline the prioritization
and remediation process.

By adopting a systematic approach to normalization, organizations can verify that
their response to vulnerabilities is consistent, effective, and aligned with the actual
risks posed to the system. Ensure that everyone involved in the security process understands
the chosen scoring system and knows how to interpret it. Regular workshops or training
sessions can help ensure ongoing alignment.

**Related information:**

- [NIST
Common Vulnerability Scoring System (CVSS)](https://nvd.nist.gov/vuln-metrics/cvss)
- [MITRE Common
Weakness Scoring System (CWSS™)](https://cwe.mitre.org/cwss/cwss_v1.0.1.html)
- [Static
Analysis Results Interchange Format (SARIF)](https://sarifweb.azurewebsites.net/)
- [OCSF
Schema](https://schema.ocsf.io/)
- [OCSF
GitHub](https://github.com/ocsf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.2-normalize-security-testing-findings.html*

---

**Capability**: QA.ST — Security testing

# [QA.ST.3] Use application risk assessments for secure software design

**Category:** FOUNDATIONAL

Application risk assessments integrate security considerations
directly into the software development lifecycle. At the
earliest stages of the development lifecycle, design reviews
focus on the planned architecture, features, and flow of the
application. During these reviews, security experts should
assist with making design choices to prevent introducing weak
points that could introduce vulnerabilities. The primary goal
is to make security-centric design decisions, eliminating
vulnerabilities before they're developed.

After the design phase, threat modeling dives deeper into
potential security threats that the finalized design might
face. This results in a list of possible attack vectors,
identifying how an attacker might exploit vulnerabilities. An
inverse approach to threat modeling is attack modeling, which
identifies specific attacks or vulnerabilities and examines
how they can be exploited. Both methods offer insights into
possible vulnerabilities and guide developing protective
measures.

Once vulnerabilities are identified through design reviews and
potential threats through modeling, these insights should
directly inform the software's security requirements. As
applications evolve or as new threats emerge, periodically
revisit and update both functional and non-functional
requirements. Functional requirements involves measures like
input validation, session management, or error handling.
Non-functional requirements includes making changes that
impact to performance, scalability, and reliability under
security threats.

Translate identified risks into actionable user stories that detail potential abuse
or misuse scenarios. Add these stories into the backlog for the team to address during
development. Attach a test case to each story to validate its effective resolution,
establishing a clear *definition of done* for developers to adhere to.

**Related information:**

- [Threat
Composer](https://awslabs.github.io/threat-composer)
- [Threat
modeling for builders](https://catalog.workshops.aws/threatmodel/)
- [AWS Security Maturity Model - Threat Modeling](https://maturitymodel.security.aws.dev/en/3.-efficient/threat-modeling/)
- [How
to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.3-use-application-risk-assessments-for-secure-software-design.html*

---

**Capability**: QA.ST — Security testing

# [QA.ST.4] Enhance source code security with static application security testing

**Category:** FOUNDATIONAL

Static Application Security Testing (SAST) is a proactive measure to identify
potential vulnerabilities in your source code before they become part of a live application.
SAST is a specialized form of non-functional static testing that enables you to analyze the
source or binary code for security vulnerabilities, without the need for the code to be
running.

Choose a SAST tool, such as
[Amazon CodeGuru Security](https://aws.amazon.com/codeguru/), and use it to scan your application
using an automated continuous integration pipeline. This
enables identifying security vulnerabilities in the source
code early in the development process. When selecting a SAST
tool, consider its compatibility with your application's
languages and frameworks, its ease of integration into your
existing toolsets, its ability to provide actionable insights
to fix vulnerabilities, and false positive rates. False
positive rate is one of the most important metrics to focus on
when selecting a SAST tool, as this can result in findings and
alerts of potential security issues that are not actually
exploitable. False positives can erode trust in the adoption
of security testing.

To prevent developer burnout and backlash due to overwhelming
false positives or a high rate of alerts in existing
applications, introduce SAST rulesets incrementally. Start
with a core set of rules and expand as your team becomes more
accustomed to addressing security testing feedback. This
iterative approach also allows teams to validate the tool's
findings and fine-tune its sensitivity over time. Regularly
update and refine enabled SAST rules to maintain its
effectiveness in identifying potential security issues.

**Related information:**

- [Security
in every stage of the CI/CD pipeline: SAST](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#static-application-security-testing-sast)
- [Amazon CodeGuru Security](https://aws.amazon.com/codeguru/)
- [Security
scans - CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security-scans.html)
- [Blog:
Building end-to-end AWS DevSecOps CI/CD pipeline with open
source SCA, SAST and DAST tools](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.4-enhance-source-code-security-with-static-application-security-testing.html*

---

**Capability**: QA.ST — Security testing

# [QA.ST.5] Evaluate runtime security with dynamic application security testing

**Category:** FOUNDATIONAL

While other forms of security testing identifies potential vulnerabilities in code
that hasn't been run, dynamic application security testing (DAST) detects vulnerabilities in
a running application. DAST works by simulating real-world attacks to identify potential
security flaws while the application is running, enabling uncovering vulnerabilities that
may not be detectable through static testing. By proactively uncovering security weaknesses
during runtime, DAST reduces the likelihood of vulnerabilities being exploited in production
environments.

Begin by choosing a DAST tool that offers broad vulnerability coverage, including
recognition of threats listed in the [OWASP Top 10](https://owasp.org/www-project-top-ten/). When selecting a tool, verify that it can integrate seamlessly with
your existing toolsets, authentication mechanisms, and protocols used by your systems. With
DAST, false positive rates are generally lower than other forms of security testing since it
actively exploits known vulnerabilities. Still, pay attention to false positive rates and
the tool's ability to provide actionable insights. False positives can erode developer trust
in security testing while detracting from genuine threats and consuming unnecessary
resources.

**Related information:**

- [Security
in every stage of the CI/CD pipeline: DAST](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#dynamic-application-security-testing-dast)
- [Building
end-to-end AWS DevSecOps CI/CD pipeline with open source
SCA, SAST and DAST tools](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.5-evaluate-runtime-security-with-dynamic-application-security-testing.html*

---

**Capability**: QA.ST — Security testing

# [QA.ST.6] Validate third-party components using software composition analysis

**Category:** FOUNDATIONAL

The use of open-source software and third-party components accelerates the software
development process, but it also introduces new security and compliance risks. Software
Composition Analysis (SCA) is used to assess these risks and verify that
external dependencies being used do not have known vulnerabilities. SCA works by scanning
software component inventories, such as software bill of materials [software bill of materials](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html) (SBOM) and dependency manifest files.

When selecting a SCA tool, focus on tools that provide the most comprehensive
vulnerability database, pulling from sources such as the [National Vulnerability Database](https://nvd.nist.gov/) (NVD) and [Common Vulnerabilities and Exposures](https://www.cve.org/) (CVE). The tool will need to integrate with
your existing toolsets, frameworks, and pipelines, as well as provide both detection and
remediation guidance for vulnerabilities. These feedback mechanisms enable teams to detect
and mitigate vulnerabilities, maintaining the software's integrity without impacting
development velocity.

Integrate SCA into the continuous integration pipeline to automatically scan changes
for vulnerabilities. Use SCA to scan existing repositories periodically to verify that
existing codebases maintain the same security standards as newer developments. Centrally
storing SBOMs also offers unique advantages for assessing vulnerabilities at scale. While
scanning repositories and pipelines can capture vulnerabilities in active projects,
centralized SBOMs act as a consistent, versioned record of all software components used
across various projects and versions. It provides a holistic view of all dependencies across
different projects, making it easier to manage and mitigate risks at an organizational
level. Instead of scanning every repository individually, centralized scanning of SBOMs
offers a consolidated method to assessing and remediating vulnerabilities.

**Related information:**

- [Security
in every stage of the CI/CD pipeline: SCA](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#software-composition-analysis-sca)
- [Building
end-to-end AWS DevSecOps CI/CD pipeline with open source
SCA, SAST and DAST tools](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.6-validate-third-party-components-using-software-composition-analysis.html*

---

**Capability**: QA.ST — Security testing

# [QA.ST.7] Conduct proactive exploratory security testing activities

**Category:** RECOMMENDED

Conduct frequent exploratory security testing activities,
encompassing penetration testing, red teaming, and
participation in vulnerability disclosure or bug bounty
programs.

Penetration tests use ethical hackers to detect vulnerabilities in system or networks
by mimicking potential threat actor actions. These exploratory security tests reveal
weaknesses in the system using the ingenuity of human testers. Deployment pipelines can
trigger the penetration testing process and wait for an approval to help ensure that
vulnerabilities are identified and fixed before code moves to the next stage. Automation
can be used to run repetitive, baseline tests, such as dynamic application security
testing, to enable human testers to focus on more complex scenarios. Review the [AWS Customer Support Policy for
Penetration Testing](https://aws.amazon.com/security/penetration-testing/) before running penetration tests against AWS
infrastructure. Penetration testing is most effective when you need a broad review of the
application or system against known vulnerabilities.

Going beyond the scope of penetration tests, red
teaming emulates real-world adversaries in a full-scale
simulation, targeting the organization's technology, people,
and processes. Red teaming is more focused than penetration
testing, targeting specific vulnerabilities by allocating more
resources, spending more time, and examining additional attack
vectors. This includes potential threats from internal
sources, such as lost devices, external sources like phishing
campaigns, and those arising from social engineering tactics.
This approach provides insights into how threat actors might
exploit weaknesses and bypass defenses in a real-world
scenario. Red teaming evaluates the broader resilience of an
application or system, including its resistance to
sophisticated attacks that span the entire organization's
security posture.

Vulnerability disclosure and bug bounty programs invite external researchers to
examine your software, complementing and often surpassing internal security evaluations.
Researchers who participate in these programs not only identify potential exploits but
also verify them, resulting in higher fidelity findings. The person who identified the
vulnerability does not disclose it publicly for a set amount of time, allowing a patch to
be rolled out before the information is disclosed publicly, and in some cases will receive
compensation for their efforts. These programs foster a culture of openness and continuous
improvement, emphasizing the importance of external feedback in maintaining secure
systems.

The findings from exploratory security testing should be
communicated to development teams as soon as findings are
available, allowing for quick remediation and learning.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC11-BP03 Perform
regular penetration testing](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_perform_regular_penetration_testing.html)
- [Security
in every stage of the CI/CD pipeline: Penetration Testing
and Red Teaming](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#penetration-testing)
- [AWS Penetration Testing: A DIY Guide for Beginners](https://www.getastra.com/blog/security-audit/aws-penetration-testing/)
- [AWS Customer Support Policy for Penetration Testing](https://aws.amazon.com/security/penetration-testing/)
- [AWS Cloud Security - Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/)
- [AWS BugBust](https://aws.amazon.com/bugbust/)
- [AWS CloudSaga - Simulate security events in AWS](https://github.com/awslabs/aws-cloudsaga)
- [RFC
9116 - A File Format to Aid in Security Vulnerability
Disclosure](https://www.rfc-editor.org/rfc/rfc9116)
- [Amazon's
approach to security during development: Penetration
Testing](https://youtu.be/NeR7FhHqDGQ?t=1432)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.7-conduct-proactive-exploratory-security-testing-activities.html*

---

**Capability**: QA.ST — Security testing

# [QA.ST.8] Improve security testing accuracy using interactive application security testing

**Category:** OPTIONAL

Interactive Application Security Testing (IAST) offers an
inside-out approach to application security testing by
combining strengths of both Static Application Security
Testing (SAST) and Dynamic Application Security Testing
(DAST). While SAST examines source code to identify
vulnerabilities and DAST inspects a running system, IAST uses
embedded agents which has access to application code, system
memory, stack traces, and requests and responses to monitor
system behavior during runtime.

Unlike other automated security testing methods that can produce false alarms, IAST's
real-time observability from within the application provides a contextual understanding
that reduces false positive rates. When vulnerabilities are detected, IAST provides deeper
insight into how the system is impacted, providing proof that the vulnerabilities flagged
are genuine and actionable.

Include IAST agents to the system during the build process to actively monitor the
system in the testing environments. These agents provide additional observability to the
system that is used to validate vulnerabilities. After the application is deployed to
production, these agents should be turned off or set to a passive mode to avoid any
performance overhead. IAST is optional for DevOps adoption, as many organizations find
sufficient coverage with SAST and DAST.

**Related information:**

- [Security
in every stage of the CI/CD pipeline: IAST](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#interactive-application-security-testing-iast)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.8-improve-security-testing-accuracy-using-interactive-application-security-testing.html*

---

**Capability**: QA.TEM — Test environment management

# [QA.TEM.1] Establish dedicated testing environments

**Category:** FOUNDATIONAL

Use testing environments to detect and correct issues earlier
on in the development lifecycle. Deploy integrated changes
into these environments before they are deployed to
production. These environments are as production-like as
possible, providing the ability to simulate real-world
conditions which can validate that changes are ready for
production deployment.

Design your testing environments to mimic production qualities
that you need to test, such as monitoring settings or regional
variants. At a minimum, have a staging environment that you
monitor closely to catch potential issues early. More testing
environments, such as beta or zeta, can be added as needed.
Infrastructure as code (IaC) should be used for managing and
deploying these environments, ensuring consistent and
predictable provisioning. Minimize direct human intervention
in these environments, similar to how you would treat
production environments. Instead, rely on automated delivery
pipelines with stages that deploy to the testing environment.
Human access should be strictly controlled, auditable, and
granted only in exceptional circumstances.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS06-BP04 Use
managed device farms for testing](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a5.html)
- [Development
and Test on Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/testing-phase.html)
- [Test
environments in AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-environments.html)
- [Deployment
Pipeline Reference Architecture](https://pipelines.devops.aws.dev/application-pipeline/index.html#test-gamma)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.tem.1-establish-dedicated-testing-environments.html*

---

**Capability**: QA.TEM — Test environment management

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

---

**Capability**: QA.TEM — Test environment management

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

---

**Capability**: QA.TEM — Test environment management

# [QA.TEM.4] Implement a unified test data repository for enhanced test efficiency

**Category:** RECOMMENDED

Test data refers to specific input datasets designed for
testing purposes to simulate real-world scenarios.
Centralizing test datasets in a unified storage location, such
as a data lake or source code repository, ensures they are
stored, normalized, and managed effectively.

Test data might be stored differently depending on your specific use case. It can be
stored centrally for a single team who maintains multiple microservices or related
products, or centrally governed for multiple teams to source test data from. By
centralizing, teams can reuse the same test data across different test cases, minimizing
the time and effort spent preparing test data for usage.

Create a centralized, version-controlled system to store test
datasets, such as a data lake or source code
repository. Ensure the data in this central repository is
sanitized and approved for non-production environments. When
test environments are set up and test cases are run, use
delivery pipelines and automated tools to source test data
directly from this centralized source.

Outdated test datasets can result in ineffective tests and inaccurate results.
Regularly maintain the centralized test data source by updating it either periodically or
when there are changes in systems data schemas, features, functions, or dependencies.
Treat the test data as a shared resource with contracts in place to prevent disrupting
other teams or systems. Document any changes made to test data and notify any dependent
teams of these changes. Maintaining up-to-date test data allows for more effective issue
identification and resolution, leading to higher-quality software.

We recommend automating the update process where feasible using data pipelines, for
example, by pulling recent production data and obfuscating it as changes are made. Protect
sensitive data by implementing a data obfuscation plan that transforms sensitive
production data into similar, but non-sensitive, test data. Use obfuscation techniques,
such as masking, encrypting, or tokenizing, to sanitize the production data prior to it
being used in non-production environments. This approach helps uphold data privacy and
mitigates potential security risks during testing.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS04-BP06 Use
shared file systems or storage to access common data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a7.html)
- [AWS Well-Architected Sustainability Pillar: SUS04-BP07
Minimize data movement across networks](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a8.html)
- [AWS Well-Architected Cost Optimization Pillar: COST08-BP02
Select components to optimize data transfer cost](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_optimized_components.html)
- [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/)
- [Identifying
and handling personally identifiable information
(PII)](https://docs.aws.amazon.com/databrew/latest/dg/personal-information-protection.html)
- [Data
Obfuscation](https://www.imperva.com/learn/data-security/data-obfuscation/)
- [Data
Masking using AWS DMS (AWS Data Migration Service)](https://aws.amazon.com/blogs/database/data-masking-using-aws-dms/)
- [Data
Lake Governance - AWS Lake Formation](https://aws.amazon.com/lake-formation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.tem.4-implement-a-unified-test-data-repository-for-enhanced-test-efficiency.html*

---

**Capability**: QA.TEM — Test environment management

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

---

**Capability**: QA.TEM — Test environment management

# [QA.TEM.6] Enhance developer experience through scalable quality assurance platforms

**Category:** RECOMMENDED

As team structures and operating models change within the organization to support
distributed teams with value stream ownership, the roles and responsibility of quality
assurance teams also evolve. In a DevOps environment with supportive team dynamics,
individual stream-aligned teams take ownership of quality assurance and security within
their value stream and products. This approach removes the handoff of responsibility and
accountability to centralized quality assurance or testing teams within the organization.
These quality assurance functions are still extremely important to sustainably practicing
DevOps and can be distributed to make them more effective in supporting stream-aligned
teams.

One method of distributing a centralized quality assurance function is to form
platform teams. These platform teams offer scalable testing services to stream-aligned
teams to enhance the developer experience and expedite test environment set up. Platforms
managed by these teams can feature self-service options, automated test environment
management, test bed provisioning, and equipping teams with the tools to produce, manage,
and use test data and infrastructure. Additionally, these platforms can integrate device
farms, allowing for testing across a variety of devices such as mobile phones or web
browsers such as Chrome and Firefox on diverse operating systems.

Quality assurance platforms can also be created to provide
security related capabilities which enable continuous
visibility into the security posture of applications
throughout the development lifecycle, such as Application
Security Posture Management (ASPM). Stream-aligned teams can
leverage these capabilities to prioritize and address
vulnerabilities identified during testing, contributing to
overall risk reduction and improved application security. By
providing a platform for consistent testing procedures and
security controls, quality assurance platform teams can help
support the organization's observability and automated
governance goals.

Another method of distributing quality assurance teams is to
form enabling teams. These teams can help stream-aligned teams
onboard to quality assurance platforms and teach teams to
become self-sufficient with test design and execution. It is
important that enabling teams do not take ownership over
testing for a value stream or product. They provide
just-in-time guidance and knowledge sharing, but ultimately
move on to help other teams. If long-term quality assurance
support is needed within a development team, cross-train the
quality assurance member so that they gain development skills
and permanently embed them into the stream-aligned team.

**Related information:**

- [The
Amazon Software Development Process: Self-Service
Tools](https://youtu.be/52SC80SFPOw?t=579)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.tem.6-enhance-developer-experience-through-scalable-quality-assurance-platforms.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
