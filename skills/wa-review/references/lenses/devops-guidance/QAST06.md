**Saga**: Quality assurance
**Capability**: QA.ST — Security testing

---

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
