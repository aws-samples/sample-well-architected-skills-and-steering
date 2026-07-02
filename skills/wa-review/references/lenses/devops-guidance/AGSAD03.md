**Saga**: Automated governance
**Capability**: AG.SAD — Secure access and delegation

---

# [AG.SAD.3] Treat pipelines as production resources

**Category:** FOUNDATIONAL

Pipelines become pivotal in every aspect of the software
development lifecycle when practicing DevOps, as they become
the sole method of moving code from development to production.
During the process of building, testing, and deploying
software, pipelines require access to all software components
involved, including libraries, frameworks, repositories,
modules, artifacts, and third-party dependencies. Due to this
level of access and their role in deploying to potentially
sensitive environments, pipelines should be recognized as
integral components of your overall system and must be secured
and managed to the same degree as the environments and data
they interact with.

The [application of least-privilege principles](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), commonly applied
to human users, should be extended to pipelines. To reduce the potential for pipelines to
become a security threat, their roles and permissions should be confined to align with their
precise responsibilities. Emphasizing pipeline governance and treating pipelines as
first-class citizens within your security infrastructure can substantially decrease your
potential attack surface and reinforce the security of your overall DevOps environment.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC11-BP07 Regularly
assess security properties of the pipelines](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_regularly_assess_security_properties_of_pipelines.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.3-treat-pipelines-as-production-resources.html*
