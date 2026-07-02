**Saga**: Quality assurance
**Capability**: QA.ST — Security testing

---

# [QA.ST.8] Improve security testing accuracy using interactive application security testing

**Category:** OPTIONAL

Interactive Application Security Testing (IAST) offers an
inside-out approach to application security testing by
combining strengths of both Static Application Security
Testing (SAST) and Dynamic Application Security Testing
(DAST). While SAST examines source code to identify
vulnerabilities and DAST inspects a running system, IAST uses
embedded agents which has access to application code, system
memory, stack traces, and requests and responses to monitor
system behavior during runtime.

Unlike other automated security testing methods that can produce false alarms, IAST's
real-time observability from within the application provides a contextual understanding
that reduces false positive rates. When vulnerabilities are detected, IAST provides deeper
insight into how the system is impacted, providing proof that the vulnerabilities flagged
are genuine and actionable.

Include IAST agents to the system during the build process to actively monitor the
system in the testing environments. These agents provide additional observability to the
system that is used to validate vulnerabilities. After the application is deployed to
production, these agents should be turned off or set to a passive mode to avoid any
performance overhead. IAST is optional for DevOps adoption, as many organizations find
sufficient coverage with SAST and DAST.

**Related information:**

- [Security
in every stage of the CI/CD pipeline: IAST](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#interactive-application-security-testing-iast)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.8-improve-security-testing-accuracy-using-interactive-application-security-testing.html*
