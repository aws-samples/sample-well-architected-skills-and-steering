**Saga**: Development lifecycle
**Capability**: DL.CS — Cryptographic signing

---

# [DL.CS.3] Enforce verification before using signed artifacts

**Category:** RECOMMENDED

Before using code artifacts, the cryptographic signature
should be inspected and validated. This verification step
enforces trust and security within the development lifecycle,
ensuring that software remains unchanged before it is used or
deployed.

Strictly enforce verification of cryptographic signatures each
time a code artifact is used or deployed. Use a managed
signing service
like [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) or the public key from your organization's
trusted Certificate Authority (CA) for signature verification.
Automate the verification process where possible, as manual
checks can be error-prone and may not be strictly enforced.
Some examples of this are integrating signature verification
into the deployment pipeline, enforcing verification at the
registry level as artifacts are distributed, or using the
Kubernetes admission controller to verify each container image
as they are pulled.

**Related information:**

- [Security
Considerations for Code Signing](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01262018.pdf)
- [Configuring
code signing for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html)
- [Kyverno
extension service for Notation and the AWS signer](https://github.com/nirmata/kyverno-notation-aws)
- [Announcing
Container Image Signing with AWS Signer and Amazon EKS](https://aws.amazon.com/blogs/containers/announcing-container-image-signing-with-aws-signer-and-amazon-eks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cs.3-enforce-verification-before-using-signed-artifacts.html*
