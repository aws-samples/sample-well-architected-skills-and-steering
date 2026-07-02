**Saga**: Automated governance
**Capability**: AG.ACG — Automated compliance and guardrails

---

# [AG.ACG.4] Strengthen security posture with ubiquitous preventative guardrails

**Category:** FOUNDATIONAL

Perform rapid and consistent detection of potential security issues or
misconfigurations by deploying automated, centralized detective controls. Automated
detective controls are guardrails that continuously monitor the environment, quickly
identifying potential risks, and potentially mitigating them.

Guardrails can be placed at various stages of the development lifecycle, including
being directly enforceable within the environment itself—providing the most control and
security assurance. To provide a balance between agility and governance, use multiple layers
of guardrails. Use environmental guardrails, such as access control limitations or API
conditions, which enforce security measures and compliance ubiquitously across an
environment. Embed similar detective and preventative checks within the deployment pipeline,
which will provide faster feedback to development teams.

The actual implementation of environmental guardrails can vary
based on the specific tools and technologies used within the
environment. An example of preventative guardrails in AWS are
Service Control Policies (SCPs) and IAM conditions.

**Related information:**

- [Example
service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.4-strengthen-security-posture-with-ubiquitous-preventative-guardrails.html*
