**Saga**: Development lifecycle
**Capability**: DL.CS — Cryptographic signing

---

# [DL.CS.1] Implement automated digital attestation signing

**Category:** RECOMMENDED

Digital attestations serve as verifiable evidence that
software components were built, tested, and conform to
organizational standards within a controlled environment.
Signatures associated with each attestation can be verified to
ensure that the component has not been tampered with and
originated from a trusted source. Generating attestations
throughout the development lifecycle provides a method of
ensuring software quality, origin, and authenticity.

Embed automated tools into the deployment pipeline to produce digital
attestations. Create an attestation for each action you want to create proof for, such as
a test being run, software being packaged, or even manual approval acceptance steps. Sign
these attestations using symmetric or asymmetric keys. Follow metadata frameworks such
as [in-toto](https://in-toto.io/) for best practices for formatting
attestations to include metadata about the software, the build environment, and the
authoring party. Store attestations either with build artifacts in a repository or within
governance tools for deeper analysis.

**Related information:**

- [Software
attestations](https://slsa.dev/attestation-model)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cs.1-implement-automated-digital-attestation-signing.html*
