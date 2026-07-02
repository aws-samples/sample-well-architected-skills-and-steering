**Saga**: Development lifecycle
**Capability**: DL.SCM — Software component management

---

# [DL.SCM.5] Maintain an approved open-source software license list

**Category:** FOUNDATIONAL

Manage and regularly update an allowed and forbidden
open-source software (OSS) licenses list. This list should
reflect which licenses are, or are not, compliant with laws,
regulations, and security requirements applicable to your
organization. Use this list to detect and prevent legal issues
while using open-source components.

Enforce the allowed and forbidden OSS licenses list by continuously assessing all OSS
usage automatically as part of the build process. This can be enforced through quality
assurance testing processes, like scanning the [Software Bill of Materials (SBOM)](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html) with Software Composition Analysis (SCA)
tooling. Continuous enforcement helps to ensure that only approved OSS licenses are used in
the code base, reducing the risk of legal issues and license violations while providing
developers with fast feedback.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.5-maintain-an-approved-open-source-software-license-list.html*
