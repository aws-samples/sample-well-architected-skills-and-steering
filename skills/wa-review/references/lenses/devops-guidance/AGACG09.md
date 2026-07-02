**Saga**: Automated governance
**Capability**: AG.ACG — Automated compliance and guardrails

---

# [AG.ACG.9] Integrate software provenance tracking throughout the development lifecycle

**Category:** RECOMMENDED

Software provenance tracking inspects the origin and evolution
of software components throughout their lifecycle to
understand where a piece of software originated, its
development and update history, and its distribution.
Provenance tracking ensures the integrity of software,
maintains compliance, and enhances the security of the
software supply chain throughout the development
lifecycle. Effective provenance tracking can prevent the
introduction of insecure components, offer early detection of
potential vulnerabilities, and provide insights for timely
remediation.

Developers are encouraged to use the best tools for the task
at hand, often including third-party software components.
These third-party elements can introduce an additional layer
of complexity and potential risk. Implementing software
provenance tracking mitigates these risks by promoting better
visibility into the lifecycle of software components, thereby
increasing accountability, transparency, and trust.

Provenance tracking should be integrated into all stages of
the development lifecycle. For instance, source code
provenance should be tracked at the time of code check-in or
commit into Version Control Systems like Git, while the
provenance of third-party components should be verified at the
time of component acquisition and usage using tools like
Software Composition Analysis (SCA). A
[Software
Bill of Materials (SBOM)](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html) can be used as a detailed list
of all components within your software, including the exact
version, digital signatures, and origin of each one.

Verify provenance at build and deploy time. Use digital signatures and hashing
algorithms to verify the integrity and provenance of software artifacts as part of the
deployment pipeline, validating the signature of an artifact against a trusted source
before it is used. It can also be useful to check running software continuously to
identify compromised or outdated software components post-deployment.

**Related information:**

- [SLSA
specification](https://slsa.dev/spec/v1.0/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.9-integrate-software-provenance-tracking-throughout-the-development-lifecycle.html*
