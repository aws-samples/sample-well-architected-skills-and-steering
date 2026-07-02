**Saga**: Automated governance
**Capability**: AG.SAD — Secure access and delegation

---

# [AG.SAD.8] Adopt a zero trust security model, shifting towards an identity-centric security perimeter

**Category:** RECOMMENDED

When operating under a zero trust security model, no user or
system is trusted by default. It requires all users and
systems, even those inside an organization's network, to be
authenticated, authorized, and continuously validated to
ensure secure configurations and posture. Only after
validation will they be granted access to applications and
data.

Zero trust is beneficial throughout the entire software
development lifecycle. From the initial stages of code
development as developers interact with source code
repositories, through continuous integration using internal
and external tools to build and test software, to the
deployment and maintenance of the workloads, each user,
pipeline, third-party, and service needs to be authenticated
and authorized with every request. In these scenarios, zero
trust enforces adherence to the principle of least privilege,
ensuring that all of these independent users and systems are
granted access to the right resources only when necessary.

Shifting to a zero trust model is not an all-or-nothing
endeavor, it is a gradual process consistent with the DevOps
principles of continuous improvement. Start small by
pinpointing use cases that align with your organization's
unique needs and the value and sensitivity of your systems and
data. This understanding will guide the selection of zero
trust principles, tools, and patterns that are most beneficial
for your organization. Adopting zero trust often involves
rethinking identity, authentication, and other
context-specific factors like user behavior and device health.
Enhance existing security practices over time, improving both
identity-based and network-based security measures that
complement each other to create a secure perimeter where
identity-centric controls can operate.

AWS provides several use cases that illustrate zero trust
principles:

- **Signing API requests:** Every AWS API request is
authenticated and authorized individually, regardless of the trustworthiness of the
underlying network.
- **Service-to-service interactions:** AWS services
authenticate and authorize calls to each other using the same security mechanisms used
by customers.
- **Zero trust for internet of things (IoT):** AWS IoT
extends the zero trust model to IoT devices, enabling secure communication over open
networks.

**Related information:**

- [Zero
Trust on AWS](https://aws.amazon.com/security/zero-trust/)
- [Zero
Trust Maturity Model](https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf)
- [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/)
- [AWS Verified Access](https://aws.amazon.com/verified-access)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.8-adopt-a-zero-trust-security-model-shifting-towards-an-identity-centric-security-perimeter.html*
