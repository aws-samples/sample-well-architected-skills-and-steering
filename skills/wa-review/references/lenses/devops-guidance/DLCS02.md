**Saga**: Development lifecycle
**Capability**: DL.CS — Cryptographic signing

---

# [DL.CS.2] Sign code artifacts after each build

**Category:** RECOMMENDED

Code signing is the process of attaching a digital signature
to build artifacts like binaries, containers, and other forms
of packaged code to enable verifying its integrity and
authenticity. Signing code artifacts minimizes risk of using
or distributing tampered or counterfeit software.

Cryptographically sign code artifacts during the build
process. Ideally this occurs after testing and before
publishing to production. Follow
[best
practices for timestamping](https://www.digicert.com/blog/best-practices-timestamping) while signing. Timestamping
provides a verified date and time of the signing, serving as
evidence that the code artifact existed and met the signature
criteria while the certificate was still valid. To safeguard
operations, ensure that the validity of the signed code
artifact is recognized even after the signing certificate
itself has expired.

Store signatures in a location accessible to users and systems
that need to verify signed code artifacts. When
using [Open
Containers Initiative (OCI)](https://opencontainers.org/) compliant artifact
registries, it is encouraged to store digital signatures
alongside the build artifacts being signed. This enables a
consolidated retrieval process and allows verification systems
to easily locate and validate signatures. Just as with
artifacts, signatures can accumulate over time. Implement a
lifecycle policy that archives or deletes older signatures
that are no longer needed to help manage storage costs.

After a signature has been stored, it should be immutable so that the signature
cannot be tampered with or replaced. Use fine-grained access controls to ensure that only
authorized entities can push or modify artifacts and their corresponding signatures.
Regularly back up your digital signatures. Having a backup ensures you can still verify
the integrity and authenticity of your artifacts in the event of storage failures. All
access and operations on stored signatures should be logged to support forensic analysis
and to adhere to compliance requirements.

Implement cryptographic signing of artifacts during the build
process. Ideally this occurs after testing and before
publishing to production. This helps ensure the integrity of
the artifacts and confirms their authenticity. We recommend
using a managed service like
[AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) to reduce the complexity that comes with
managing public key infrastructure. Refer
to [AWS Signer workflows](https://docs.aws.amazon.com/signer/latest/developerguide/workflows.html) for guidance that fits your use case.

For more control over the signing process or for complex use
cases, you can create and manage your own code signing
platform using Public Key Infrastructure (PKI). While this
approach offers precise control, it requires consistent upkeep
and adherence to best practices.
[AWS Private Certificate Authority](https://aws.amazon.com/private-ca/) is a managed private CA
service that helps you manage the lifecycle of your private
certificates easily, without the investment and ongoing
maintenance costs of operating your own private CA.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS05-BP03 Use
managed services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a4.html)
- [Using
AWS Signer workflows](https://docs.aws.amazon.com/signer/latest/developerguide/workflows.html)
- [Configuring
code signing for AWS SAM applications - AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/authoring-codesigning.html)
- [Security
Considerations for Code Signing](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01262018.pdf)
- [Code
signing using AWS Certificate Manager Private CA and AWS Key Management Service asymmetric keys](https://aws.amazon.com/blogs/security/code-signing-aws-certificate-manager-private-ca-aws-key-management-service-asymmetric-keys/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cs.2-sign-code-artifacts-after-each-build.html*
