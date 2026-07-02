**Saga**: Development lifecycle
**Capability**: DL.CI — Continuous integration

---

# [DL.CI.3] Ensure automated quality assurance for every build

**Category:** FOUNDATIONAL

As code changes become more frequent in a DevOps environment,
it becomes important to reduce the time it takes to get
feedback on those changes. Adding automated quality assurance
(QA) tests into the continuous integration pipeline enables
rapidly validating changes and receiving fast feedback.

Add stages to the pipeline which run pre-deployment checks to
validate that code changes work alongside the existing code
base. These checks should automatically trigger functional,
non-functional, and security tests against the integrated code
base and build artifacts.

*Breaking-the-build*, which stops the integration pipeline process
due to test failures, is a powerful feedback mechanism. However, it should be used
judiciously. Reserve breaking-the-build for critical issues, such as actual build failures,
high severity security findings, or non-negotiable compliance findings, that demand
immediate developer attention. Overuse can disrupt the continuous flow of development,
leading to unforeseen delays, bottlenecks, and poor developer experience.  Instead, continue
to provide feedback to developers in tools they already use, such as IDEs, chat clients, or
email, and let them decide if they should stop the process.

It is often more practical to automate enforcement of quality
assurance findings as part of the continuous delivery process.
This allows enforcement to be objectively targeted based on
the environment to which the build is being deployed into.
Have an exception mechanism and escalation plans prepared that
developers can use if the continuous integration or continuous
deployment prevent deployments which they do not agree with.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL08-BP02 Integrate
functional testing as part of your deployment](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_functional_testing.html)
- [AWS Well-Architected Security Pillar: SEC11-BP02 Automate
testing throughout the development and release lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_automate_testing_throughout_lifecycle.html)
- [Testing
stages in continuous integration and continuous
delivery](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/testing-stages-in-continuous-integration-and-continuous-delivery.html)
- [Amazon's
approach to high-availability deployment: Release guidance
lifecycle](https://youtu.be/bCgD2bX1LI4?t=855)
- [Testing
software and systems at Amazon: Continuous integration and
deployment](https://youtu.be/o1sc3cK9bMU?t=1206)
- [The
Amazon Software Development Process: Automated
Testing](https://youtu.be/52SC80SFPOw?t=1340)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.3-ensure-automated-quality-assurance-for-every-build.html*
