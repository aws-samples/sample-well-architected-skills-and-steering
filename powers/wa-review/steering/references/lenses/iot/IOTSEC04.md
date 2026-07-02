# IOTSEC04 — Security

**Pillar**: Security  
**Best Practices**: 1

---

## IOTSEC04-BP01 Assign least privilege access to devices

Permissions (or policies) allow an authenticated identity to
perform various control plane and data plane operations against
AWS IoT Core, such as creating devices or certificates via the
control plane, and connecting, publishing, or subscribing via
the data plane.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC04-BP01-01** *Grant least privilege
access to reduce the scope and impact of the potential
events.*

Use granular device permissions to enable least privilege
access, which can help limit the impact of an error or
misconfiguration. Define a mechanism so that devices can only
communicate with specific resources such as MQTT topics. If
permissions are generated dynamically, make sure that similar
practices are followed. For example, create an AWS IoT policy as
a JSON document that contains a statement with the following:

- `Effect`, which specifies whether the action is allowed or
denied.
- `Action`, which specifies the action the policy is allowing or
denying.
- `Resource`, which specifies the resource or resources upon
which the action is allowed or denied.

**Prescriptive guidance
IOTSEC04-BP01-02** *Consider scaling granular
permissions across the IoT fleet.*

Reuse permissions across principals where possible rather than
creating specific permissions for each individual principal.
This helps you avoid creating redundant permissions per device
and streamlines applying similar permission changes across
multiple devices.

For example, consider an AWS IoT policy allows access based on
various thing attributes such as `ThingName`, `ThingTypeName`, and `Thing
Attributes`. To allow a device to access its own
information, use a policy variable rather than specifying a
specific ClientId value and creating a IoT policy for each
device.

- Recommended:
`arn:aws:iot:us-east-1:123456789012:client/${iot:Connection.Thing.ThingName}`

- Not recommended:
`arn:aws:iot:us-east-1:123456789012:client/foo.`

As another example, consider an AWS IoT policy also allows
access based on various certificate attributes such as `Subject`,
`Issuer`, `Subject Alternate Name`, `Issuer Alternate Name`, and
others. Again, use a policy variable rather than specifying a
specific `CertificateId` and creating a IoT policy for each
device.

- Recommended:
`arn:aws:iot:us-east-1:123456789012:topic/${iot:CertificateId}`
- Not recommended:
`arn:aws:iot:us-east-1:123456789012:topic/xxxxxxxxxxx`

IOTSEC05: How do you manage device
certificates, including installation, validation, revocation,
and rotation?

To authenticate IoT device to AWS IoT Core and authenticate AWS IoT Core to an IoT device, AWS IoT Core supports TLS-based
mutual authentication using X.509 certificates. TLS-based mutual
authentication authenticates both client and server to one
another during the TLS handshake processing of setting up an
encrypted TLS communications channel.

To enable TLS-based mutual authentication, device makers must
provision a unique identity, including a unique private key and
X.509 certificate, into each device. Certificates are relatively
long-lived identifiers of principals and are managed using a
customer-owned Certificate Authority (CA), a third-party CA, or
the AWS IoT Core CA. Any hosted CA chosen must provide you the
ability to create (activate), revoke (deactivate), validate, and
refresh or rotate certificates. Authentication using
certificates requires, at authentication time, that the
principal identified by the certificate can prove that it holds
the private key associated with the public key found in the
certificate.

Authenticated identities are the focal point of device trust and
authorization to your IoT application. It's vital to be able to
manage identities, such as certificates, centrally. Valid
certificates are those which are not revoked, expired, made
inactive, and not issued by a CA which has had its certificate
revoked or invalidated. As part of a well-architected
application, you must have a process for identifying any invalid
certificates and have an automated response in place to take
some action to address the finding.

In addition to the ability of capturing the events where an
invalid certificate is presented, your devices should also have
a secondary means of establishing secure communications to your
IoT system if mutually-authenticated TLS communications is not
possible. This may involve manual, local interaction with the
device, either by a consumer or service technician.

A well-architected IoT solution establishes a certificate
revocation list (CRL) that tracks all revoked device
certificates or certificate authorities (CAs). Use your own
trusted CA for on-boarding devices and synchronize the CRL in
the device and in your IoT application on a regular basis. Your
IoT application must reject connections from identities
(certificates or tokens) that are no longer valid.

With AWS, you do not need to manage your entire PKI on-premises.
Use AWS Certificate Manager (ACM) or AWS Private Certificate Authority (PCA) to host your CA in the cloud. Or, you can work
with an APN Partner to add preconfigured secure elements to your
IoT device hardware specification. ACM has the capability to
export a certificate revocation list (CRL) to a file in an S3
bucket. The CRL can be used to programmatically revoke
certificates configured in AWS IoT Core.

Another state for certificates is to be near their expiry date
but still valid. The device certificate must be valid for at
least the service lifetime of the device. If a device
certificate is nearing its expiration date and the device is to
remain in operation, then your IoT application must take some
action to update the device certificate with a certificate that
has a later expiration date. Use the AWS IoT Jobs or OTA to
perform the necessary operations to carry out this refresh. Be
sure to log information about the certificate refresh operations
performed for auditing purposes.

Enable AWS IoT Device Defender audits related to device and CA
certificate expiry. Device Defender produces an audit log of
certificates that are set to expire within 30 days. Use this
list to programmatically update devices before certificates are
no longer valid. You may also choose to build your own expiry
store to manage certificate expiry dates and programmatically
query, identify, and trigger an IoT Jobs and OTA for device
certificate replacement or renewal.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/identity-and-access-management.html*

---
