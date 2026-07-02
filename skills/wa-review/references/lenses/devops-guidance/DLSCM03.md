**Saga**: Development lifecycle
**Capability**: DL.SCM — Software component management

---

# [DL.SCM.3] Use artifact repositories with enforced authentication and authorization

**Category:** FOUNDATIONAL

Artifact repositories and registries offer secure storage and
management for artifacts generated during the build stage of
the development lifecycle. Examples of artifacts that are
stored in these repositories are container images, compiled
software artifacts, third-party modules, and other shared code
modules. Using an artifact repository streamlines artifact
versioning, access control, traceability, and dependency
management, contributing to efficient and reliable software
releases. They can significantly improve the auditability,
security, and organization of your software artifacts, leading
to higher-quality software deliveries.

Artifact repositories are in the critical path for ensuring
the integrity of the software that is deployed into your
environments. All artifacts in the repository should be
expected to be built and tested using trusted automated
processes in an effort to prevent errors or bugs from being
introduced into the system. Artifact repositories should not
contain manually produced artifacts or allow existing
artifacts to be altered by users. Altering artifacts in the
artifact repository degrades the integrity of the artifact and
repository, so artifact repositories should enforce that
artifacts are immutable.

Use role-based or attribute-based access control to limit which users and systems can
store and modify artifacts in artifact repositories. Access to create, update, or delete
artifacts should remain restricted to emergencies, security use cases, and build and
deployment processes.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC11-BP05 Centralize
services for packages and dependencies](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_centralize_services_for_packages_and_dependencies.html)
- [Artifact
Repository - AWS CodeArtifact](https://aws.amazon.com/codeartifact/)
- [Fully
Managed Container Registry - Amazon Elastic Container Registry](https://aws.amazon.com/ecr/)
- [Code
Repositories and Artifact Management | AWS Marketplace](https://aws.amazon.com/marketplace/solutions/devops/code-repositories-and-artifact-management?aws-marketplace-cards.sort-by=item.additionalFields.headline&aws-marketplace-cards.sort-order=asc&awsf.aws-marketplace-devops-store-use-cases=*all)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.3-use-artifact-repositories-with-enforced-authentication-and-authorization.html*
