**Saga**: Automated governance
**Capability**: AG.ACG — Automated compliance and guardrails

---

# [AG.ACG.11] Digital attestation verification for zero trust deployments

**Category:** RECOMMENDED

Digital attestations are recommended to be created for each action that occurs during the development lifecycle. Attestations serve as evidence of compliance, which can be verified either during or post-deployment. Authorizing deployments by verifying attestations extends a zero trust security model to the development lifecycle. If attestations for the required quality assurance tests, pipeline stages, or manual approvals are missing or invalid, meaning that compliance and change management requirements were not met during the development lifecycle, the deployment can be either prevented or subjected to an exception mechanism for risk acceptance.

Incorporate the creation of digital attestations into the development lifecycle. Before deployment, verify that the required attestations have been digitally signed by trusted cryptographic keys and that they meet the change management and compliance policies. If a deployment is found to be non-compliant, you can choose to respond in several ways depending on your security and governance requirements. It can be used as a detective control which allows the deployment to proceed while keeping an audit log of the non-compliance for future investigation. It can also be used as a preventive control, stopping the deployment from proceeding entirely. Pairing this with an exception mechanism you could enforce directive controls to accept the identified risks for a period of time.

This approach to automated governance and change management continuously assesses the integrity of the software throughout the development lifecycle. It provides a method of authorizing deployment based on adherence to governance and compliance requirements, extending zero trust security model principles to the deployment process.

**Related information:**

- [Software attestations](https://slsa.dev/attestation-model)
- [in-toto Attestation Framework Spec](https://github.com/in-toto/attestation/blob/main/spec/README.md#in-toto-attestation-framework-spec)
- [Zero Trust on AWS](https://aws.amazon.com/security/zero-trust/)
- [Zero Trust Maturity Model](https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.11-digital-attestation-verification-for-zero-trust-deployments.html*
