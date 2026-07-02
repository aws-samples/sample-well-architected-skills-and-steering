**Saga**: Development lifecycle
**Capability**: DL.ADS — Advanced deployment strategies

---

# [DL.ADS.1] Test deployments in pre-production environments

**Category:** FOUNDATIONAL

Progressively validate software changes across multiple environments, including
development (alpha) and testing (beta) before deploying into production. Additional staging
environments can be introduced as needed, such as staging (gamma). These additional
environments help to prevent the introduction of bugs in production environments, validates
backwards compatibility, and increases the confidence in the quality of the deployment.

Each non-production deployment serves as a gate, only allowing changes to progress to
the next stage after they pass all validations. Early issue detection and isolation prevent
propagation to later stages or production. A controlled deployment process includes
strategies to manage risk and support rollback if issues are identified during these test
deployments.

One-box testing can be used to test backward compatibility to ensure new code changes
coexist with and function properly with the existing code base. One-box refers to the
testing of changes in a single unit of deployment, such as a single container or instance,
which is configured to use production endpoints. This form of testing can be used to help
ensure the changes interact efficiently with production endpoints of other services. This
can be done by creating a dedicated staging environment for cross-service backward
compatibility (zeta) testing. Services deployed to the zeta stage interact exclusively with
production endpoints to identify potential integration issues before the code reaches the
production stage.

**Related information:**

- [What
is Continuous Integration?](https://aws.amazon.com/devops/continuous-integration/)
- [What
is Continuous Delivery?](https://aws.amazon.com/devops/continuous-delivery/)
- [Going
faster with continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery?did=ba_card&trk=ba_card)
- [Automating
safe, hands-off deployments: Test deployments in
pre-production environments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/#Test_deployments_in_pre-production_environments)
- [Amazon's
approach to high-availability deployment](https://youtu.be/bCgD2bX1LI4)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.1-test-deployments-in-pre-production-environments.html*
