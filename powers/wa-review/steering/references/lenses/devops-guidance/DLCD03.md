**Saga**: Development lifecycle
**Capability**: DL.CD — Continuous delivery

---

# [DL.CD.3] Integrate quality assurance into deployments

**Category:** FOUNDATIONAL

Integrating quality assurance (QA) processes into continuous delivery pipelines tests
that the whole system is ready for release. This differs from previous quality checks in the
development lifecycle as these tests validate that the software changes behave as expected
when deployed into real-world environments. This provides the ability to test integration
with other live systems, check for configuration errors, and test in environments that more
closely mirror production.

Incorporate QA stages into your delivery pipeline to
automatically conduct required functional, non-functional,
security, and data tests after deployments occur. Deployments
to environments is the ideal enforcement point for quality
assurance, with QA requirements being scoped to the
environment being deployed to. If a test fails for one
environment, it is a signal that deployment to subsequent
environments might carry the same risk. Provide immediate
feedback to the development team upon any test failures, so
they can rectify issues quickly and maintain the integrity of
the deployment pipeline.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL08-BP02 Integrate
functional testing as part of your deployment](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_functional_testing.html)
- [AWS Well-Architected Reliability Pillar: REL08-BP03 Integrate
resiliency testing as part of your deployment](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_resiliency_testing.html)
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

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.3-integrate-quality-assurance-into-deployments.html*
