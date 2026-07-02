**Saga**: Quality assurance
**Capability**: QA.FT — Functional testing

---

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
