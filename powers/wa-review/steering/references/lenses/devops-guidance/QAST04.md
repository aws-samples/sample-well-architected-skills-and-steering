**Saga**: Quality assurance
**Capability**: QA.ST — Security testing

---

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
