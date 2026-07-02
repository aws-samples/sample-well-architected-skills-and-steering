**Saga**: Quality assurance
**Capability**: QA.ST — Security testing

---

# [QA.ST.1] Evolve vulnerability management processes to be conducive of DevOps practices

**Category:** FOUNDATIONAL

Vulnerability management requires an ongoing, iterative process consistent with agile
development practices. The goal is to discover potential vulnerabilities across networks,
infrastructures, and applications, and to prioritize and take action on them.

Automated vulnerability scanning must be integrated into deployment pipelines to
provide feedback to developers regarding security vulnerabilities and improvements early on.
This minimizes extensive security evaluations during deployment and is consistent with the
DevOps *shift left* approach—addressing security problems early on in the
development process. Choose vulnerability scanning tools that are compatible with your
existing technology and platforms. For instance, if [Amazon CodeCatalyst](https://aws.amazon.com/codecatalyst/) is your pipeline tool of choice, verify that the
chosen vulnerability scanning tool has a CodeCatalyst plugin or API integration capability. If
vulnerabilities are detected during a build, the pipeline should automatically generate
alerts, allowing developers to address issues quickly.

If you use issue-tracking systems like Jira or [CodeCatalyst Issues](https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues.html), it can be
beneficial to automatically generate tickets to assist developers with tracking issues. When
a vulnerability is detected, an automated ticket should be generated, tagged with severity,
and assigned to the appropriate developer or team. Use vulnerability management dashboards
to consistently monitor and analyze threats. Regular reports should detail vulnerability
trends, ensuring vulnerabilities are not reintroduced and pinpointing recurrent security
challenges.

To effectively practice vulnerability management in a DevOps environment, it's
important to adopt a culture where security is everyone's responsibility. Development and
security teams need collaboration, with clear delineations for security issue handoff and
ownership. In a DevOps model, distributed development teams take on security
responsibilities for their products. Centralized security teams often become enabling teams,
offering training, insights, and support. They can also take on the responsibilities of a
security platform team, producing reusable components, improving efficiency, reducing
duplication of work, and overall providing autonomy to distributed teams so that they can
efficiently secure their products.

**Related information:**

- [Enterprise
DevOps: Why You Should Run What You Build](https://aws.amazon.com/blogs/enterprise-strategy/enterprise-devops-why-you-should-run-what-you-build/)
- [Automated
Software Vulnerability Management - Amazon Inspector](https://aws.amazon.com/inspector/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.1-evolve-vulnerability-management-processes-to-be-conducive-of-devops-practices.html*
