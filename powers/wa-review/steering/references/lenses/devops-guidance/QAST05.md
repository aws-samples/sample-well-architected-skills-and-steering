**Saga**: Quality assurance
**Capability**: QA.ST — Security testing

---

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
