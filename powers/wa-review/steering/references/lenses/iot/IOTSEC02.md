# IOTSEC02 — Security

**Pillar**: Security  
**Best Practices**: 3

---

## IOTSEC02-BP01 Use a separate hardware or a secure area on your devices to store credentials

A secure element (SE) is any hardware feature you can use to
protect information on the device. A common use of an SE is to
securely store the device's identity. Secure storage at rest
helps reduce the risk of unauthorized use of the device
identity. Never store or cache device credentials outside of the
SE. If supported, generate public or private key pairs using the
SE, and generate the Certificate Signing Requests (CSRs) on the
device. With this method, the private key never leaves the SE.
If this is not possible, generate and transmit the credentials
to the SE in a secure manufacturing facility with Common
Criteria EAL certification. Import or install the private key
material into the SE in the secure facility. Securely handling a
device's identity helps make sure that your hardware and
application are resilient to potential security issues that
occur in unprotected systems. A SE provides encrypted storage of
private information (such as cryptographic keys) at rest and can
be implemented as separate specialized hardware or as part of a
system on a chip (SoC).

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC02-BP01-01** *Use tamper-resistant
hardware that offloads the cryptographic operations for
encryption and communication from the IoT
application.*

Device credentials must always reside in a SE, which facilitates
usage of the credentials. Using the SE to facilitate the use of
device credentials further limits the risk of unauthorized use.
As an example, AWS IoT Greengrass supports using a SE to store
AWS IoT certificates and private keys.

**Prescriptive guidance
IOTSEC02-BP01-02** *Use cryptographic API
operations provided by the secure element hardware for
protecting the secrets on the device.*

Only access security modules using the latest security
protocols. For example, in FreeRTOS, use the PKCS#11 APIs
provided in the corePKCS11 library for protecting secrets.

**Prescriptive guidance
IOTSEC02-BP01-03** *Use the AWS Partner Device
Catalog to find AWS Partners that offer hardware security
modules.*

If you are getting devices that have not been deployed in the
field, AWS recommends reviewing the AWS Partner Device Catalog
to find AWS IoT hardware partners that either implement a SE or
trusted platform module (TPM). Use AWS IoT Partners that offer
qualified SEs for storing IoT device identities.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/identity-and-access-management.html*

---

## IOTSEC02-BP02 Use a trusted platform module (TPM) to implement cryptographic controls

Generally, a TPM is used to hold, secure, and manage
cryptographic keys and certificates for services such as disk
encryption, Root of Trust booting, verifying the authenticity of
hardware (as well as software), and password management. The TPM
has the following characteristics:

- TPM is a dedicated crypto-processor to help make sure the
device boots into a secure and trusted state.
- The TPM chip contains the manufacturer's keys and software
for device encryption.
- The Trusted Computing Group (TCG) defines
hardware-roots-of-trust as part of the Trusted Platform
Module (TPM) specification.

A hardware identity refers to an immutable, unique identity for
a platform that is inseparable from the platform. A hardware
embedded cryptographic key, also referred to as a hardware root
of trust, can be an effective device identifier. Vendors such as
Microchip, Texas Instruments, and many others have TPM-based
hardware solutions.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC02-BP02-01** *Perform cryptographic
operations inside the TPM to avoid a third party gaining
unauthorized access.*

Store all secret keys from the manufacturer required for secure
boot, such as attestation keys, storage keys, and application
keys, in the secure enclave of the chip. For example, a device
running AWS IoT Greengrass can be used with an Infineon OPTIGA
TPM.

**Prescriptive guidance
IOTSEC02-BP02-02** *Use a trusted execution
environment (TEE) along with a TPM to act as a baseline defense
against rootkits.*

TEE is a separate execution environment that provides security
services and isolates access to hardware and software security
resources from the host operating system and applications.
Various hardware architectures support TEE such as:

- ARM TrustZone divides hardware into secure and non-secure
worlds. TrustZone is a separate microprocessor from the
non-secure microprocessor core.
- Intel Boot Guard is a hardware-based mechanism that provides
a verified boot, which cryptographically verifies the
initial boot block or uses a measuring process for
validation.

**Prescriptive guidance
IOTSEC02-BP02-03** *Use physical unclonable
function (PUF) technology for cryptographic
operations.*

A PUF technology is a physical object that provides a physically
defined digital fingerprint to serve as a unique identifier for
an IoT device. As a different class of security primitive, PUFs
normally have a relatively simple structure. It makes them ideal
candidates for affordable security solutions for IoT networks.
Generally, a hardware root of trust based on PUF is virtually
impossible to duplicate, clone, or predict. This makes them
suitable for applications such as secure key generation and
storage, device authentication, flexible key provisioning, and
chip asset management. Refer to
[AWS Partner Device Catalog](https://partners.amazonaws.com/qualified-devices/) which has various device solutions
with PUFs such as LPC54018 IoT Solution by NXP.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/identity-and-access-management.html*

---

## IOTSEC02-BP03 Use protected boot and persistent storage encryption

When a device performs a secure boot, it validates that the
device is not running unauthorized code from the filesystem.
This helps make sure that the boot process starts from a trusted
combination of hardware and software, and continues until the
host operating system has fully booted and applications are
running.

Choose devices with TPM (or TEE) for new deployments. Secure
boot also makes sure that if even a single bit in the software
boot-loader or application firmware is modified after
deployment, the modified firmware will not be trusted, and the
device will refuse to run this untrusted code.

Full disk encryption makes sure that the storage and
cryptographic elements are secured in absence of a TPM or SE.
The disk controller needs to make sure that read accesses to the
disk are transparently decrypted and write operations are
encrypted at runtime.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC02-BP03-01** *Boot devices using a
cryptographically verified operating system image.*

Use digitally signed binaries that have been verified using an
immutable root of trust, such as a master root key (MRK) that's
stored securely in a non-modifiable memory, to boot devices.

**Prescriptive guidance
IOTSEC02-BP03-02** *Create separate filesystem
partitions for the boot-loader and the applications.*

As an example, configure the device boot-loader to use a
read-only partition, and applications to use a separate writable
partition for separation of concerns and reducing risks.

**Prescriptive guidance
IOTSEC02-BP03-03** *Use encryption utilities
provided by the host operating system to encrypt the writable
filesystem.*

For example, use crypt utilities for Linux such as dm-crypt or
GPG, and use BitLocker or Amazon EFS for Microsoft Windows.

**Prescriptive guidance
IOTSEC02-BP03-04** *Use services that can push
signed application code from a trusted source to the
device.*

You can use AWS IoT Jobs to push signed software binaries from
the cloud to the device. For microcontrollers using FreeRTOS,
make sure that the firmware images are signed before deployment.
Signature verification should also verify that the signer of the
package is trusted and the signer's certificate and any
intermediate certificate authorities' certificates have not been
revoked.

IOTSEC03: How do you authenticate and
authorize user access to your IoT application?

Although many applications focus on the device aspect of IoT, in
almost all industries using IoT, there is also a human component
that needs the ability to communicate to and receive
notifications from devices.

For example, consumer IoT generally requires users to onboard
their devices by associating them with an online account.
Industrial IoT typically entails the ability to analyze hardware
telemetry in near real time. In either case, it is essential to
determine how your application will identify, authenticate, and
authorize users that require the ability to interact with the
solution and with particular devices.

Controlling user access to your IoT assets begins with identity.
Your IoT application must have in place a store (typically a
user registry or identity provider) that keeps track of a user's
identity and also how a user authenticates using that identity.
The identity store may include additional user attributes that
can be used at authorization time. For example, the user's group
memberships.

When using AWS to authenticate and authorize IoT application
users, you have several options to implement your identity store
and how that store maintains user attributes. For your own
applications, use Amazon Cognito for your identity store. Amazon Cognito provides a standard mechanism to express identity and to
authenticate users. Amazon Cognito enables usage of user
identity in a way that can be directly consumed by your app and
other AWS services in order to make authorization decisions.
When using AWS IoT, you can choose from several identity and
authorization services including Amazon Cognito Identity Pools,
AWS IoT policies, and AWS IoT custom authorizer to validate
tokens (such as JWT or SAML 2.0) for authenticating users.
Amazon Cognito supports federation to third party identity
providers using the OpenID Connect (OIDC) and SAML 2.0
protocols.

An alternative to using AWS IAM-based role permissions for user
interaction with an IoT solution is to define a separate
authorization layer for the application which uses Amazon Verified Permissions. Verified Permissions allows for the
definition of fine-grained access control policies for accessing
resources which are specific to an application. Principals used
in AVP policy statements can be defined from Amazon Cognito user pools.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/identity-and-access-management.html*

---
