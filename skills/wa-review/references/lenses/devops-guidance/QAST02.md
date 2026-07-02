**Saga**: Quality assurance
**Capability**: QA.ST — Security testing

---

# [QA.ST.2] Normalize security testing findings

**Category:** FOUNDATIONAL

Effective vulnerability management requires clarity and
consistency. Given the diversity of security testing tools in
a DevOps environment, findings often emerge from different
sources and in different formats. This diversity of tooling
can introduce confusion and inefficiency into risk management
processes.  Having a common framework for normalizing the
interpretation and ranking of vulnerabilities from diverse
security testing tools provides a systematic approach to risk
management and mitigation. Normalization is not just about
consistency, it helps ensure that every identified
vulnerability is understood, categorized, and managed
according to its threat level.

Begin by selecting a recognized scoring system, such as the
Common Vulnerability Scoring System
([CVSS](https://nvd.nist.gov/vuln-metrics/cvss)),
as the baseline for vulnerability ranking. This will provide a
universal language for risk assessment and
prioritization. Many modern security tools have built-in
integrations with popular scoring systems. Configure your
tools to automatically map their findings to the chosen
system, ensuring uniformity across all results. It is
important to periodically review the normalization process,
updating it as required and ensuring alignment with industry
best practices.

Use tools that can automatically translate findings into the
standardized format. Integrations like the Static Analysis
Results Interchange Format
([SARIF](https://sarifweb.azurewebsites.net/))
or [OCSF
Schema](https://schema.ocsf.io/) can assist with this. These tools can enable
centralizing findings from different sources into a single
dashboard or reporting platform to create a unified view of
the security posture which can streamline the prioritization
and remediation process.

By adopting a systematic approach to normalization, organizations can verify that
their response to vulnerabilities is consistent, effective, and aligned with the actual
risks posed to the system. Ensure that everyone involved in the security process understands
the chosen scoring system and knows how to interpret it. Regular workshops or training
sessions can help ensure ongoing alignment.

**Related information:**

- [NIST
Common Vulnerability Scoring System (CVSS)](https://nvd.nist.gov/vuln-metrics/cvss)
- [MITRE Common
Weakness Scoring System (CWSS™)](https://cwe.mitre.org/cwss/cwss_v1.0.1.html)
- [Static
Analysis Results Interchange Format (SARIF)](https://sarifweb.azurewebsites.net/)
- [OCSF
Schema](https://schema.ocsf.io/)
- [OCSF
GitHub](https://github.com/ocsf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.2-normalize-security-testing-findings.html*
