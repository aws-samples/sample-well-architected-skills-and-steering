**Saga**: Development lifecycle
**Capability**: DL.SCM — Software component management

---

# [DL.SCM.10] Generate a comprehensive software inventory for each build

**Category:** RECOMMENDED

Maintain a comprehensive inventory of the components and dependencies that make up
your software assists with identifying vulnerabilities and managing risks. This inventory,
often taking the form of a [Software Bill of Materials (SBOM)](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html), provides valuable insights into the
composition of your software.

Generate a comprehensive inventory as part of each build. This
forms a continuous record of your software's composition,
enabling quick and efficient identification and management of
potential vulnerabilities or risks. Tracking inventory that is
machine readable enhances visibility and aids in identifying
vulnerabilities and risks, enhancing the security posture of
your software at scale.

Use a tool to create and manage SBOMs, centralizing them with other build artifacts
for easier accessibility. Open-source tool sets provided by Open Worldwide Application
Security Project ([OWASP](https://owasp.org/)) and the [Linux Foundation](https://www.linuxfoundation.org/) offer options for
creating and managing SBOMs in standardized formats.

**Related information:**

- [Exporting
SBOMs with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/sbom-export.html)
- [SPDX
Becomes Internationally Recognized Standard for Software
Bill of Materials](https://www.linuxfoundation.org/press/featured/spdx-becomes-internationally-recognized-standard-for-software-bill-of-materials)
- [Software
Supply Chain Best Practices](https://project.linuxfoundation.org/hubfs/CNCF_SSCP_v1.pdf)
- [OWASP
CycloneDX](https://owasp.org/www-project-cyclonedx/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.10-generate-a-comprehensive-software-inventory-for-each-build.html*
