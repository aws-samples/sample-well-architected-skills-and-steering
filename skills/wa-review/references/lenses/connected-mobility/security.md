# Security

**Pages**: 10

---

# Design principles

There are a number of principles that can help strengthen the security of your connected mobility solution in addition to the overall Well-Architected Framework security design principles:

**Identify automotive and general regulatory and compliance standards:** Design and architect solutions to help adhere to industry-standard security frameworks and regulations. The automotive industry has specific regulations and standards to consider. Automotive specific standards and frameworks that should be considered by you and your applicable stakeholders include, and are not limited to: ISO/SAE 21434 for cybersecurity, ISO 26262 for functional safety, ASPICE for software development lifecycle process, ISO 24089 for OTA, and regulations like UNR 155/156 for developing a cyber security management system and software update management system in automotive. It is important to consider and align to general standards when building connected mobility applications like ISO 27001, NIST Cybersecurity Framework, and privacy laws like GDPR. This helps to verify that the systems in scope are validated against the highest levels of safety, security, and privacy.

**You have a choice of protocols that can be used for vehicle connectivity to the cloud:** There are several protocols that can be used to for vehicle connectivity to the cloud. The protocols and services that you use can influence the security properties of the connection between vehicle to cloud. Common protocol patterns include HTTPS, MQTT/TLS, Kafka over TLS, Secure RTP, and gRPC over TLS. Consider cost, performance, bandwidth, business applicability, and more when deciding which protocol fits your connectivity use-case.

**Implement secure identity lifecycle management for vehicles and consumers**: An end-to-end identity management system should manage the entire lifecycle for vehicles, owners, drivers, operators and partner identities. There are unique considerations for electronic control units (ECUs) device certificates such as provisioning, expiry, rotation/revocation, validation, and certificate management. Consumer identities need to be considered as they interact with different vehicles and vehicle features. It is important to verify the validity and mapping between the different identity types (owner, driver, and vehicle) and pro-actively revoke or extend identities and the associated permissions over time.

**Establish least privilege permissions for vehicles and systems**: Vehicles should have fine-grained access permissions to backend systems and access to vehicles from other systems should follow the same guiding principle of least privilege. Vehicles receive communication from many endpoints such as charging stations, backend systems, and consumer applications. Scoping down the permissions will help reduce the risk of lateral movements from a compromised entity (vehicle or system). Vehicle ECUs should only be able to communicate with topics or endpoints that they are required to operate. Permissions of vehicle ECUs should be audited and reviewed continuously.

**Classify and protect data collected from systems and applications related to connected mobility:** Connected mobility applications interact with sensitive data including but not limited to personal identifiable information (PII), location data, VINs, and user data. Customers need to implement data protection mechanisms such as data encryption, data anonymization, and data access control to safeguard the sensitive data. Use secure communication channels such TLS to confirm that data transmitted between vehicles and the cloud is protected from interception, tampering, or other types of attacks. Vehicles, sensors, and systems should only collect the data necessary to facilitate their function.

**Design for continuous monitoring and verify trusted software and firmware:** implement continuous monitoring mechanisms of your connected mobility service such as in-vehicle and the vehicle environment (such as charging stations, and mobile applications) to detect and respond to security incidents and alert your purpose-built vehicle security operations center (VSOC). Use secure firmware and software update mechanisms to create timely security patches and updates over the air. Implement secure boot and chain of trust mechanisms to verify that only trusted software components are loaded and executed on the vehicle's hardware.

**Design for resiliency in-vehicle and in the cloud:** implement redundancy and resilient mechanisms to check that critical systems such as brakes, steering, and power train continue to operate even in the event of a security issue.

Confirm that backend systems in the cloud are also resilient and able to recover from such events. Consider implementing managed services and highly available backend systems by leveraging multiple Availability Zones and plan the disaster recovery for your solution in another AWS Region. Backup your critical data frequently to help meet the desired Recovery Point Objective (RPO) of the solution. Implement vehicle shadow logic to maintain state during loss of connectivity to the cloud.

**Define a vehicle and system threat model:** implement threat modeling to identify potential security risks and vulnerabilities in the system (vehicle, vehicle related infrastructure, applications, backend) and implement appropriate security controls to mitigate these risks. Confirm that you follow automotive threat modeling standards such as Threat Analysis and Risk Assessment (TARA) or another methodology to cover in-vehicle threats and measure appropriate risk ratings.

**Train your staff so that they are able
to address vehicle security risks and the impact across the
organizations:** Deliver a training program that can
provide your security team and developers with vehicle
cybersecurity and compliance training, cloud security training,
and fundamental information technology training. It is important
to evaluate program effectiveness and update periodically.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/design-principles-sec.html*

---

# Security foundations

CMSEC_1: How are you maintaining consumer privacy during actions such as
in-vehicle purchase transactions or data collection?

Vehicles today contain a multitude of sensors which enable many of the features we rely on for both convenience and safety. These sensors collect large amounts of data which must be both transmitted, stored, and potentially correlated between distributed systems which provide this functionality. When building these architectures, it is important to understand all applicable laws and compliance requirements which govern what data is necessary to collect, store or share with third parties, and how it should be anonymized to protect the privacy of consumers and their passengers. The system should be designed with these requirements in early stages and not after the system is in production.

**[CMSEC_BP1.1] Personally identifiable information (PII) and unique
identifiers (IDs) assigned to a vehicle or consumer should be anonymized.**

Information which can be used to directly or indirectly identify an individual must be protected from disclosure. This information includes but is not limited to name, address, location data, or combination of other data elements such as Vehicle Identification Number (VIN) and International Mobile Equipment Identity (IMEI). This data should be encrypted in transit using secure protocols such as TLS and at rest using your own robust encryption keys or those provided by [AWS Key Management Service](https://aws.amazon.com/kms/). Restrict access to data for authorized users by classifying data and creating separate views of this data according to the principles of least privilege using [AWS Identity and Access Management](https://aws.amazon.com/iam/) or masking sensitive data using third party solutions such as [DataMasque](https://aws.amazon.com/blogs/apn/how-to-mask-sensitive-data-on-aws-using-datamasque).

**[CMSEC_BP1.2] Location data collected from navigation systems should
be appropriately secured to protect anonymity.**

Data which can be used to locate a consumer or track travel routes should also be encrypted in transit and at rest. Location data which is sent to third parties should have any PII or IDs scrubbed from the request. In addition, the precision of coordinates for both latitude and longitude can be adjusted to provide additional privacy. As an example, [Amazon Location Service](https://aws.amazon.com/location/) supports up to 6 decimal points for these coordinates which is accurate up to approximately 4 inches from the object of interest. As the number of decimal points is decreased so does the precision and depending on the requirements for the service being provided this may be an acceptable threshold.

**[CMSEC_BP1.3] Data collected from cameras, microphones, biometric,
and other types of sensors should be appropriately secured.**

Sensors should only collect the minimum amount of data required to facilitate their function.
When possible, sensors such as microphones should leverage a wake word or activation of a
tactile button to begin the data collection process. These sensors should also contain idle
timeout logic to limit this collection. Still or video image captures should have
identifying features such as the faces of passengers and pedestrians for example blurred
using a proven process. The AWS blog post [Creating a serverless face blurring service for photos in Amazon S3](https://aws.amazon.com/blogs/compute/creating-a-serverless-face-blurring-service-for-photos-in-amazon-s3/) outlines how this
can be accomplished using Amazon S3. Data should use strong encryption in transit and at rest to
verify privacy when transmitting to OEM or third-party systems. Other types of sensors such
as those that collect biometric data may be subject to other compliance standards such as
the Health Insurance Portability and Accountability Act (HIPAA) and require different
configurations for data handling and retention.

CMSEC_2: Your risk management program should align to security standards, laws,
regulations, and frameworks in the connected vehicle space.

Your risk management program should be used to capture functional safety,
cybersecurity, privacy, and secure software development requirements throughout the
lifecycle of the vehicle. This can be accomplished by incorporating guidance from automotive
industry specific frameworks such as ISO-21434, information security standards like NIST
800-53 or ISO 27001, and the new UNR-155 and UNR-156 regulations concerning type approval
with regards to cyber security management systems and software update management systems.
These standards, frameworks, and regulations can inform your organization on how to design a
cyber security program that covers both the vehicle and the systems and resources that
interact with vehicles. This requires input and collaboration from a number of
cross-functional areas including but not limited to management, security, and legal to
address the needs that are specific to your organization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/security-foundations.html*

---

# Identity and access management

CMSEC_3: How do you manage the identities of your vehicles and individual
ECUs?

When working with connected vehicles, you must determine how you will manage the identities of your vehicles and individual
Electronic Control Units (ECUs). These identities can come in different forms and are used to authenticate and authorize access
to a variety of services in the connected vehicle environment. This includes other vehicles, charging stations, backend services,
OTA servers, and more. For example, an ECU can be uniquely identified with a private key (usually stored in a secure hardware module
such as a TPM or an HSM) and an X.509 certificate corresponding to that private key. These X.509 certificates may have subject names or
extensions with vehicle and ECU information such as VIN or ECU ID.

There are important considerations when provisioning, rotating, revoking, and managing the lifecycle of certificates on ECUs. Each ECU
can have several X.509 certificates, each used for different purposes such as an attestation certificate (or birth certificate) used
to authenticate an ECU, and one or more operational certificates. These operational certificates are used to authenticate to connected
vehicle services. For example, when the ECU connects to a connected vehicle service using Mutual TLS, it can present its client
certificate and cryptographically prove that it possesses the private key. The TLS server can validate the certificate to authenticate
that the connection originates from the ECU that owns the private key.

In addition to X.509 certificates, vehicles and ECUs may use other forms of identities such as tokens, API credentials, and HTTP cookies.
For example, a user signs in to a streaming music application on the in-vehicle infotainment (IVI) system and after the user's authorization,
the music application receives an OIDC Access Token that is used to authenticate requests to the backend APIs of the streaming music service.
In another example, an ECU may exchange its operational certificate for a set of time-limited cloud API credentials used to invoke cloud service APIs
such as uploading video or telemetry data.

The following best practices can help you manage identities for your vehicles and
ECUs.

**[CMSEC_BP3.1] Securely manage the lifecycle of identities and
credentials for your vehicles and ECUs**

It is important to check that each request or action on a
connected vehicle service is authenticated and authorized. The
security depends on appropriately managing the lifecycle
stages of the identities and credentials for your vehicles and
ECUs:

- **Provision**

This is the process of installing identities into your vehicles and ECUs. See
CM-S01 Vehicle and User Provisioning from scenarios section. Typically, this begins at
the manufacturing process where a unique Attestation X.509 certificate (also called a
Birth Certificate) is issued for the ECU to prove its authenticity and provenance. The
private key for the certificate can be generated within an on-board secure hardware
module such as a TPM or HSM, a Certificate Sign Request (CSR) is generated and presented
to a Certificate Authority (CA) that issues a certificate. The CA can be part of a
Private Key Infrastructure (PKI) owned and operated by the OEM or the supplier of the
ECU. For more information see [this blog
post](https://aws.amazon.com/blogs/iot/securing-modern-connected-vehicle-platforms-with-aws-iot/) that discusses provisioning certificates using AWS IoT. Additionally,
the ECU can have one or more operational certificates that are used to authenticate to
connected vehicle services. It is important to verify that the process of requesting and
issuing certificates is authenticated, authorized, and audited to check that only
genuine ECUs are issued certificates. If you are unable to generate private keys in an
on-board secure module and must generate private keys on a server, see that access to
these private keys is restricted and tracked as the security of client certificate-based
authentication relies on protecting the private keys. You have the option to design,
build and operate your own PKI and CAs, or you can take advantage of [AWS Private Certificate Authority](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) (AWS PCA) that allows you to create private certificate authority
(CA) hierarchies, including root and subordinate CAs, without the investment and
maintenance costs of operating an on-premises CA.
- **Enroll or register**

After certificates are issued and installed in ECUs, you may also need to enroll or
register the certificates with your backend services. For example, you can register the
ECU's certificate in an asset database associated with the ECU ID (serial number) and
corresponding authorization policies that are applied to requests from that ECU. You can
build your own asset database using a self-hosted database or an [AWS managed cloud database service](https://aws.amazon.com/products/databases/). If you are
using [AWS IoT Core](https://aws.amazon.com/iot-core/) to connect your ECUs to
the cloud, IoT Core provides a built-in [registry for Things](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html) and
their [registered X.509
certificates](https://docs.aws.amazon.com/iot/latest/developerguide/register-device-cert.html). Each certificate registered in IoT Core can be associated with
an [IoT
Core Policy](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) (either directly or via [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)) that
authorizes actions that the ECU can perform on the IoT Core service such as allowing
connections, publishing or subscribing to certain [MQTT topics](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html). IoT Core also allows
you to register certificates the first time an ECU connects using [Just-in-time-Registration](https://docs.aws.amazon.com/iot/latest/developerguide/auto-register-device-cert.html) by registering the Certificate Authority (CA) that
issued the certificate.
- **Validate**

Client certificates presented by ECUs are validated by the connected vehicle
service as part of the mutual TLS handshake. This process includes checking that the
certificate has not expired, validating the certificate chain to verify the certificate
is issued by a trusted Certificate Authority, checking for certificate revocation (see
below), and checking the certificate against an asset database to check that it is an
authentic and active ECU. AWS IoT verifies that a [client
certificate is active](https://docs.aws.amazon.com/iot/latest/developerguide/activate-or-deactivate-device-cert.html) when it authenticates a connection. You can create and
register client certificates without activating them so they can't be used until you
want to use them. You can also deactivate active client certificates to disable them
temporarily.
- **Renew**

Each X.509 certificate has a validity period (determined by the Not Before and Not
After fields) that is checked by servers before accepting the certificate as valid. One
strategy to avoid renewing is to issue certificates with a long validity period - such
as 100 years - that is beyond the expected service lifetime of the ECU using the
certificate. This strategy then relies entirely on the revocation process (see below) to
manage the validity of certificates. A second strategy is to issue certificates with a
medium validity period - typically 1 to 3 years. A third strategy is to issue
short-lived certificates - typically a few hours or days - especially for cases where it
is important to prevent tracking and attribution that can happen with static long-lived
certificates. In the latter two strategies, it is important to have a secure process for
renewing certificates **before** they expire. This process
must be secured to the same degree as the process used to originally issue and provision
certificates. On AWS, [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html) periodically
audits client certificates registered in IoT Core and publishes findings for [certificates that are expiring](https://docs.aws.amazon.com/iot/latest/developerguide/audit-chk-device-cert-approaching-expiration.html) within the next 30 days. You can send the
findings to a remediation workflow in [AWS Step Functions](https://aws.amazon.com/step-functions/), using Lambda functions and [IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) to trigger the ECU to
generate a new CSR, issue a new certificate, and send the new certificate to the ECU.
Once the ECU has successfully installed and tested the new operational certificate, the
workflow can revoke the old expiring certificate in IoT Core.
- **Revoke**

When you detect a security issue with a certificate (such as the private key is
compromised) or are notified that the ECU has been replaced, you may choose to
permanently revoke the certificates associated with the ECU. Certificates are revoked by
invoking the CA that issued the certificate. The CA publishes the revocation status of
certificates via Certificate Revocation Lists (CRLs) or via Online Certificate Status
Protocol (OCSP) or both. Connected vehicle services that validate client certificates
must check whether the certificate is revoked using the CA's supported method before
accepting the certificate as valid. [AWS Private CA supports both CRL and
OCSP](https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html) as revocation methods, and this [blog post](https://aws.amazon.com/blogs/security/choosing-the-right-certificate-revocation-method-in-acm-private-ca/) helps you choose the best method for your use-cases. You can also
revoke a certificate that was previously registered in IoT Core and this denies
connections that use that certificate.
- **Retire**

Finally, when the ECU has reached its end of life or has been replaced and you no
longer want the certificates to be trusted, you can choose revoke the certificate (see
above) and delete the certificate from your asset database. This will help validate that
no future connections or requests from the ECU are accepted by connected vehicle
services. IoT Core allows you to delete a [Thing](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThing.html) and [certificates](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCertificate.html).

**[CMSEC_BP3.2] Design and securely operate a PKI for vehicle
identities**

The previous section described how vehicle identities are often X.509 certificates issued by a
vehicle Private Key Infrastructure (PKI). The security of a scheme that relies on X.509
certificates for authentication and authorization depends on the security of the PKI that
issues the certificates. It is important to start by documenting your policies and practices
for operating your PKI including details of your Certificate Authority (CA) structure,
policies for the validity period of your CAs, the process for succession of CAs, description
of the administrative permissions and controls, roles and responsibilities. You can capture
this information in two documents, known as Certification Policy (CP) and Certification
Practices Statement (CPS). Refer to [RFC
3647](https://www.ietf.org/rfc/rfc3647.txt) for a framework for capturing important information about your PKI
operations.

Minimize the use of the root CA to only issue certificates for intermediate CAs. Store the
private key of the root CA in a secure Hardware Security Module (HSM) and tightly control
physical and logical access.

In some circumstances, as an OEM you may need to share parts of your PKI with suppliers and vendors.
example, you may create an intermediate CA for a supplier and allow that supplier to issue attestation and
operational certificates that are embedded in ECUs during manufacturing. In this case, you are relying on the policies and
processes of your supplier for the security of the ECU's identities. Review the supplier's Certification Policy (CP) and Certification Practices Statement (CPS)
to check that these meet your overall PKI requirements.

You can use [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) to create, manage, and operate a vehicle PKI on AWS. PCA allows you to
create a [CA structure with multiple levels and gives you fine-grained control over each CA](https://aws.amazon.com/blogs/security/how-to-secure-an-enterprise-scale-acm-private-ca-hierarchy-for-automotive-and-manufacturing/)
and whether and how it is shared with other entities such as suppliers.

**[CMSEC_BP3.3] Design a mechanism to tie various vehicle identities
together as necessary**

As described in CMSEC_BP3.2, a vehicle will have several identities, multiple
identities per ECU and multiple identities for the vehicle. Based on your application needs,
you may require the ability to tie these identities together so that you can map an
authenticated ECU identity to its ECU ID or serial number, and to the vehicle's VIN where
the ECU is installed. You can maintain an asset database that stores a record of the
different identities and their relationships. Because this database stores sensitive
information that can be used to identify, relate, and track identities, the database must be
secured and all accesses to the database must be authenticated, authorized, and audited. To
protect the privacy of your vehicles, owners and operators, check that only authorized staff
have access to this database and unauthorized or unusual query patterns are detected and
alerts are sent to the data owners. The asset database must be updated with changes such as
when certificates are renewed (see above) and ECUs are replaced in repair shops. Verify that
only authorized staff are allowed to update the database and changes are tracked and
associated with authorized work orders or repair bills of material.

**[CMSEC_BP3.4] Define a mechanism for how your vehicles will be
identified towards external entities**

You may have use-cases where you need to send information about your vehicles and ECUs to
external entities such as business partners (dealers, suppliers, repair shops, and vehicle
insurance providers or example). Consider designing a mechanism that maps stable unique
identifiers, such as VIN and ECU Serial Number (ESN), to anonymized or temporary identities
so that you can preserve the privacy of your vehicles, owners, and operators and prevent
unauthorized or unintended sharing of information with your partners. You may choose to
create a mapping database that stores the mapping from stable identifiers to the anonymized
or temporary identifiers sent to your partners. Validate that such a mapping database has
strong authentication, access control, audit and logging.

On AWS, you can choose from a number of [fully managed purpose-built database services](https://aws.amazon.com/products/databases/) to store mappings.

CMSEC_4: How do you manage the identities of the owners, drivers, and operators
of your vehicles and map them to the vehicle's identities?

Connected vehicle services often need information on the identities of users: owners, drivers, and operators of the
vehicles to provide service features corresponding to the user. For example, a vehicle is being driven by a teenaged family
member that is not the vehicle owner. The vehicle IVI invokes a personalization service to get the preferences of both the
owner and the family member to apply personalized preferences and restrictions. The teenaged driver is restricted to a top
speed limit configured by the vehicle owner but is able to see their favorite music applications on the IVI home screen.

To implement such features, the vehicle ECUs must recognize and identify the current driver, and the connected vehicle service
must authenticate and authorize requests based on the identities of the current driver and owner and other contextual
information such as the time of the day.

Consider the following best practices when managing the identities of owners, drivers and
operators of your vehicles.

**[CMSEC_BP4.1] Design an authentication mechanism for users of your
vehicles**

Design an authentication mechanism for users of your vehicles based on the
sensitivity and risk of the actions being performed. For example, unlocking a vehicle is a
high-risk action and should require the use of a physical key fob or a digital key from an
application on a phone. Setting IVI home screen preferences may be a low-risk action and may
be acceptable to use factors such as facial recognition of the driver. This allows physical
key fobs to be shared between family members but still recognizes the current driver of the
vehicle. The driver of a delivery vehicle that is part of a fleet is authenticated using an
application on a hand-held scanner device. The fleet operator uses the identity to track the
driver of each vehicle and the routes taken for safety, efficiency, and audit purposes.

In contrast to vehicle ECUs that are typically authenticated and authorized using X.509
certificates (see CMSEC3_BP5 regarding designing a PKI for vehicle identities), users are
usually authenticated using tokens. Consider using an identity provider that supports widely
adopted identity standards such as [OpenID
Connect](https://openid.net/connect/) (built on [OAuth 2.0](https://oauth.net/2/)) to
authenticate your users and generate tokens. OpenID Connect identity providers issue [JSON Web Tokens (JWT)](https://jwt.io/) that are cryptographically signed by
the identity provider and delivered to the in-vehicle ECUs that make requests to connected
vehicle services on behalf of the user. The ECUs provide the Java Web Tokens (JWTs) as part
of the request for example in the HTTPS request header and the tokens can be validated on
the connected vehicle service to authenticate the request, and the request is authorized
based on claims and scopes in the token. Because tokens are used directly to authenticate
requests to services, check that tokens are stored securely on ECUs and are not exposed to
unauthorized users. Consider the token lifecycle, using short-lived tokens to limit the
impact of an exposed token, use refresh tokens to obtain new tokens without requiring user
interaction, and revoke the token when you detect that a token is compromised.

Because the in-vehicle user interfaces such as the IVI may be limited in terms of user input
capabilities - lacking a physical keyboard for example asking the user to type a long,
complex password on a touch-screen may be impractical and error prone. In such cases,
consider implementing the OAuth 2.0 [Device Authorization grant](https://www.rfc-editor.org/rfc/rfc8628) (also called Device Flow) that allows devices that
have no built-in browser or limited input capability to get an access token by using a
browser on a different device such as a mobile phone or desktop. The user interacts with the
browser on the phone or desktop to authenticate to the identity provider and grant access to
the IVI.

You can build and operate your own identity provider or use a cloud SaaS identity provider.
[Amazon Cognito](https://aws.amazon.com/cognito/) is a fully
managed identity provider that allows you to add user sign-up and sign-in features and
control access to your web and mobile applications. [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)
provides an identity store that scales to millions of users, supports social and enterprise
identity federation, and offers advanced security features to protect your consumers and
business. You can implement [Device Authorization grant using Cognito and AWS Lambda](https://aws.amazon.com/blogs/security/implement-oauth-2-0-device-grant-flow-by-using-amazon-cognito-and-aws-lambda/). AWS services such as
[Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html) (ALB), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html), [AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html), and [IoT
Core](https://docs.aws.amazon.com/iot/latest/developerguide/cognito-identities.html) can authenticate and authorize requests using tokens issued by Cognito User
Pools.

**[CMSEC_BP4.2] Consider patterns for mapping a user's identity to the
vehicle's identities**

The connected vehicle service will often need to map between
the user's identity and vehicle's identities to provide
service features. For example, a personalization service needs
to know the identity of the current driver, the owner, and of
the vehicle's ECUs to respond with the corresponding policies
and preferences.

One approach is to combine two authentication schemes:

- **Vehicle ECUs:** Use X.509 client certificates to
authenticate vehicle ECUs when they connect to a connected vehicle service using mTLS,
and
- **Users:** Send JWT access or ID tokens in the request
(over mTLS) as HTTPS headers or the MQTT payload to authenticate users to a connected
vehicle service.

This approach inherently maps the user's identity to the vehicle ECU's identity and your backend service can validate each
identity cryptographically. The backend service can use the ECU's identity to query an asset database for information such as the
owner or operator of the vehicle.

Consider how mapping information is updated over the lifecycle of the vehicle. For example, information about the owner of a vehicle
must be updated in the asset database when a vehicle is sold.

Validate that access to the mapping between users and vehicles is stored securely and access to this mapping is restricted to
applications and administrators on a need-to-know basis.

CMSEC_5: How do you manage the identities of your business partners, such as
dealers, suppliers, service providers, or other third parties?

Connected vehicle services operate in a rich environment with multiple business partners such as dealers, suppliers,
repair shops, and service providers, to name only a few. In addition to managing the identities of your vehicles and users
it is equally important to manage the identities of your business partners that interact with connected vehicle services.
For example, a dealer for an OEM uses a connected vehicle service to set the owner for a vehicle when a vehicle is sold. As
this operation has security and safety implications, the dealer must be authenticated and authorized to perform this operation,
and all actions must be logged and audited.

Consider the following best practices to manage the identities of your business partners.

**[CMSEC_BP5.1] Separate identities of your external partners from
internal employees and contractors**

It is very common for a single connected vehicle service to have multiple types of users that interact with it: vehicle
drivers, owners, business partners, employees, and contractors. Consider creating strict segregation boundaries between the
identities of your employees and contractors on one side, and business partners on the other.

You can implement this separate by creating separate identity provider pools (also called domains, directories, or tenants - the
terminology depends on the identity provider software or service you are using) for the two types of users. This approach has the following benefits:

- Each identity provider pool can have different security policies such as whether
user sign-ups are allowed, password strengths enforced, and the use of multi-factor
authentication (MFA).
- You can configure federation for the employee identity
pool only to your corporate identity provider, allowing
your employees to single-sign on to your custom
applications.
- User tokens contain a unique issuer element and are signed
by a key that is unique to the identity provider pool.
This provides a cryptographic way to validate that a
particular identity originates from a particular pool.

On AWS, you can separate different types of users into separate [Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) and configure each pool with different properties and
policies.

**[CMSEC_BP5.2] Verify that application authorization is based on the
type of identity**

The simplest way to implement this is to segregate the identities into separate identity provider pools and have each connected
vehicle service API explicitly trust each identity provider pool to authenticate users from that pool. For example, your dealer-facing
APIs trust the dealer identity pool, but your employee facing APIs trust only the employee identity pool. A token issued to a dealer
from the dealer identity pool cannot be used to authenticate requests to the employee APIs, because the token validation fails.

A single API resource that trusts both the employee and business partner identity pools should be considered an exception. The
configuration and code of such an API must be closely reviewed to check that authorization is appropriately granted to each type of user.

As you design your application authorization scheme, verify that only information contained in a cryptographically verified token
(such as a JWT) or information queried from a trusted backend database is used for the authorization decision. Do not rely on
information for authorization that can be spoofed such as query parameters, the request body, or unsigned browser cookies that cannot
be cryptographically verified by the server for authenticity and integrity.

On AWS, you services such as [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html) (ALB), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html), [AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html), and [IoT
Core](https://docs.aws.amazon.com/iot/latest/developerguide/cognito-identities.html) can be configured to authenticate tokens issued by specific Cognito User
Pools. With API Gateway, you can also implement custom authorization logic using [Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html).

CMSEC_6: How do you manage access permissions to vehicle functions?

In the context of connected vehicle services, privileged actions are those that are initiated from the backend and can impact the safety and
security of the vehicle. For example, an owner speaks to a customer support agent in a call center and requests a remote unlock of their vehicle
because they lost their physical key fob. In another example, the driver of a vehicle authorizes the OEM's support engineers to remotely diagnose
and fix issues with their vehicle. As is evident in both these examples, the actions initiated from connected vehicle services backends can directly
impact the safety, security, and operation of the vehicle. Permissions to perform these actions must be carefully managed and audited.

The first step is to identify the use-cases that involve restricted or administrative actions
and focus on implementing the following best practices to manage accesses to those
actions:

**[CMSEC_BP6.1] Define a process for support staff to gain permissions
to perform administrative actions on vehicle functions**

The process that your support staff (such as engineers, and customer support agents)
follow to gain permissions to perform administrative actions must require appropriate
approvals and traceability to the context of the request, for example, the customer support
case ID or trouble ticket that corresponds to the access request. Access to human actors
must be granted for a limited time and for specific actions on specific ECUs: such as grant
the ability to remotely collect logs and diagnostic data from a specific vehicle's battery
management ECU for the next 30 minutes. Access must be granted only after obtaining required
approvals from managers and after passing validation rules: such as verify that the ECU ID
in the support case is the same as the ECU ID for which access is being requested, and the
support engineer is indeed on call for the current shift, and they belong to the appropriate
security groups in your directory. For highly sensitive and impactful actions, consider
implementing quorum approval processes (also called M of N approvals) where multiple
managers or peers must review and approve an access request before access permissions are
granted. It is recommended that this process is automated and based on requestor
entitlements to avoid the risk of collusion.

**[CMSEC_BP6.2] Implement fine-grained audit logging of every
privileged action on vehicles**

Validate that every privileged action on vehicles, whether initiated by a human actor or by an
automated system, is logged with details such as the identity of the human or system actor,
the timestamp, the action performed, the target of the action (for example, ECU ID, and
Vehicle ID) and the result of the action. Verify also that each step in the process to gain
access is also logged (request, review, approval, grant), so it can be audited and tracked.
Design a mechanism that protects the integrity of access audit logs by denying permissions
to modify, delete or overwrite log events, and by appending cryptographic signatures to log
events that can be used to verify their integrity. You must also check that the log events
are indexed and searchable for later audit and analysis.

A centralized logging solution is needed that aggregates and indexes such audit log events
from your fleet of compute servers. You can deploy and manage a log collection and indexing
solution or you can use a managed SaaS service. [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) enables you to
centralize the logs from all of your systems, applications, and AWS services that you use,
in a single, highly scalable service. You can then easily view them, search them for
specific error codes or patterns, filter them based on specific fields, or archive them
securely for future analysis. CloudWatch Logs also supports querying your logs with a powerful query
language, auditing and masking sensitive data in logs, and generating metrics from logs
using filters or an embedded log format. (See CMSEC_BP11.1)

**[CMSEC_BP6.3] Alert on unauthorized attempts to access privileged
actions on high-risk ECUs**

In addition to generating fine-grained audit log events for every privileged action
(see above), consider creating automated alert notifications when unauthorized attempts to
access privileged actions on high-risk ECUs such as the IVI or Head Unit. For example, you
can create a rule that triggers an alert notification when a single support staff performs
privileged actions on multiple ECUs in a short period of time. This can trigger your Vehicle
Security Operations Center (VSOC) to investigate the alert to determine if this is a case
of compromised credentials or identity being used in an unauthorized manner. (See CMSEC_BP22.1)

CMSEC_7: How do you verify that vehicles are granted least privilege access to
perform actions on your backend systems?

As your vehicle ECUs make requests to connected vehicle services, you must check that each ECU is authorized to
perform the smallest set of actions that it needs to fulfill its function. For example, you may want to authorize an ECU to
publish telemetry data to a MQTT topic named with its ECU ID, and to subscribe to real-time road condition updates from another
topic if the vehicle owner has subscribed to a premium service.

Consider the following best practices to grant least privilege authorization to ECUs:

**[CMSEC_BP7.1] Authorize every action taken by a vehicle ECU
individually.**

Validate that every action taken by a vehicle's ECU on your connected vehicle services is authorized individually. You can use the
identity of the ECU you defined in CMSEC_3 to define the baseline policies that grant specific actions to the ECU. You can enhance these
policies to grant or deny other actions based on dynamic context conditions such as the time of the day, location of the vehicle, and
state of subscription services.

You may consider externalizing the authorization policy evaluation logic into a shared, centralized policy evaluation service where policies
can be written in a domain specific language (DSL) such as [Cedar](https://www.cedarpolicy.com/en), that is easier to
author, understand and audit than programming language code. [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/)
is a scalable permissions management and fine-grained authorization service for the applications that you build. Amazon Verified Permissions uses the Cedar
open-source policy language This pattern splits the responsibilities for authorization: the connected vehicle service is responsible for gathering the
identity and context information and providing it to the policy evaluation service. The policy evaluation service implements the logic to parse the policy
DLS and respond with a allow or deny decision to the connected vehicle service. This pattern also splits the responsibilities of the team that authors
policies in the DLS from the developers that write the code for your connected vehicle service, allowing each team to be more efficient and deploy
changes at their own pace.

You can authorize requests on the connected vehicle services backends based on scopes in
access tokens, or fields from X.509 certificates. Several AWS services offer built-in
authorization features allowing you to define policies that control access to the service's
data plane. [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) allows you to define [IoT Core Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) that control
the actions a device connected to IoT Core can perform. You can attach policies to each
client X.509 certificate and to [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html) to control access
at multiple levels. [Amazon API Gateway](https://aws.amazon.com/api-gateway/) provides
[multiple ways
to control access to a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html). Specifically, the API Gateway [Lambda
authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) allows you to implement your custom business logic in Lambda function
code and return a policy that API Gateway will cache and use to authorize future requests. [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/) is a scalable, fine-grained
permissions management and authorization service for custom applications. The service
centralizes fine-grained permissions for custom applications and helps developers authorize
user actions within applications. Amazon Verified Permissions uses the [Cedar](https://www.cedarpolicy.com/) policy language to
define fine-grained permissions for application users.

CMSEC_8: How do you validate that your backend systems have least privilege
access to perform actions on vehicle functions?

As you design connected vehicle service backend systems, validate that each system is only granted the smallest set of
permissions to perform actions on vehicles. This is especially important for CMSEC_7 regarding privileged access, as this is
critical for backend systems that initiate privileged actions on vehicles because it can impact the safety, security, and operations of the vehicle.

Consider the following best practices:

**[CMSEC_BP8.1] Verify your backend systems are authenticated and
authorized for every action on vehicle functions.**

Implement secure authentication and authorization of every request from a backend system that results in actions on vehicles.
For example, a customer support uses a customer support application to initiate remote door unlock on behalf of the vehicle owner
who has lost their keys. In this scenario, check that the customer support agent is authenticated and authorized to perform the action,
and verify that the support application is authenticated and authorized to perform the unlock action on a connected vehicle service.

In another example, your software administrator has scheduled the roll-out of an Over the Air software update to a fleet of vehicles.
An OTA service executes this update by sending commands to each vehicle in the fleet to download the update files securely from an update service.
The OTA service must be authenticated and authorized before it is allowed to such a command to a vehicle ECU.

In both of the previous examples, one service interacts with another service to perform an
action on a vehicle. This is a type of machine-to-machine communication where the calling
service must be authenticated and authorized by the called service. You can choose several
approaches to [authenticate machine-to-machine application scenarios](https://aws.amazon.com/blogs/security/approaches-for-authenticating-external-applications-in-a-machine-to-machine-scenario/).

On AWS, you can choose [AWS Signature v4 (sigv4)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
that is supported by all AWS API endpoints, and can be used to authenticate and [authorize requests to your custom APIs created in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html#http-api-vs-rest.differences.authorization). You can use [sigv4 with
AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) to authenticate and authorize actions such as publish and subscribe to
MQTT topics using MQTT over WebSocket. If the backend service is deployed to AWS, you can
associate an IAM Role with the AWS compute service (for example, [Amazon EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html), [Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html), [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html), Amazon EKS) that provides temporary security credentials that can be used by
the backend service to sign sigv4 requests. If the backend service is deployed outside
AWS, consider using [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) as the
mechanism to obtain temporary security credentials in exchange for X.509
certificates.

**[CMSEC_BP8.2] Implement fine-grained audit logging of actions
performed by your backends on vehicle functions**

It is important to implement fine-grained audit logging of actions performed by your backend services on vehicle functions.
Having such an audit log will help you with operational troubleshooting and as security incident response investigations.

You can implement audit logging in your connected vehicle service by emitting log events when actions are invoked. You can
centrally aggregate and store these log events in a Security Incident and Event Management (SIEM) system that indexes the
events and allows you to search and create dashboards and visualizations of these events.

On AWS, consider enabling the built-in logging features of AWS services that you use to
implement your backend services. Enable [AWS IoT logging](https://docs.aws.amazon.com/iot/latest/developerguide/configure-logging.html) to
deliver [log
entries](https://docs.aws.amazon.com/iot/latest/developerguide/cwl-format.html) to [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) for
events on the IoT service such as a connect, publish, subscribe, and many others. You can
enable [CloudWatch logs for your custom APIs
in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html) to get both execution logging and access logging events delivered to
CloudWatch Logs. Consider ingesting these log events from CloudWatch Logs into your SIEM tool to be indexed and
analyzed. Or consider implementing the [centralized
logging with OpenSearch](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/welcome.html) solution.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/identity-and-access-management.html*

---

# Detection

CMSEC_9: How do you monitor your in-vehicle software, components, and network
for threats?

Monitoring in-vehicle activity from threats, vulnerabilities, and fraud is becoming
increasingly important as vehicles become connected. Standards like [ISO 21434](https://www.iso.org/standard/70918.html) and regulations like
[UNR 155](https://unece.org/transport/documents/2021/03/standards/un-regulation-no-155-cyber-security-and-cyber-security) have provisions for monitoring vehicles and systems where detecting,
reporting, refining, and analyzing vehicle related data is a requirement. Monitoring
in-vehicle events that may have security implications requires providing solutions both
on-board and off-board the vehicle. Before data collection, you must understand the sources
of data that you need to collect from. You then develop the people, processes, and
technology to address the data collection, ingestion, enrichment, and analysis of that data.
You can then understand the threat landscape, use threat intelligence to proactively address
risks, and monitor and analyze threats from collected data. The final step, triaging and
incident response will be covered in the "Incident Response" section.

Data collection requires the ability to gather and record data from the vehicle and vehicle environments. Some vehicle data may be stored
locally at smaller volumes and for specific use cases (e.g., crash event data) but is usually sent to an off-board system for refinement and analysis.
The collection of this data may require onboard components depending upon how much processing capability you want to implement onboard before
sending the data off-board.

Ingestion requires sending data to an off-board service.
Oftentimes this is referred to as a VSIEM (Vehicle Security
Information Event Management System) or VSOC (Vehicle Security
Operation Center). This data stream will be sent to other
backend systems for enrichment and refinement.

**[CMSEC_BP9.1] Collect and detect events using onboard components in
the vehicle.**

You must decide how you will collect data from the vehicle,
and how much processing of security events will be done at the
vehicle edge. It is recommended that you implement software
that can detect vehicle attacks and raise an event to an IDS
manager on the ECU. There may be some filtering by the IDS
manager at this stage depending upon vehicle software and
hardware capability. The events will then be passed to local
event memory for storage, where it can be analyzed by an
authorized user with a diagnostic tool. The majority of the
event data should be sent to the VSOC system from the vehicle
gateway for further refinement of raw logs sent from the
vehicle.

**[CMSEC_BP9.2] Ingest and enrich data by preparing, moving,
aggregating, normalizing, transforming, and analyzing the vehicle data.**

There are several mechanisms to send your vehicle data to the cloud (see [Design principles](./design-principles-sec.html)). As mentioned in
the [Identity and access management](./identity-and-access-management.html) section, we recommend using unique vehicle
identities and sending data using secure protocols (see data protection).

You must take a wide a range of actions on your data in order to provide valuable capability
to VSOC analysts. The typical pattern is to ingest, store, process, analyze/train, and then
visualize the data. At the same time, this flow can include response and remediation in
parallel, which is covered in the [Incident response](./incident-response.html) section of the pillar. In order to build out detection
capabilities, you need to:

**Ingest**: You can use [AWS IoT Fleetwise](https://aws.amazon.com/iot-fleetwise/) to send vehicle telemetry in [VSS
format, a COVESA specification](https://covesa.github.io/vehicle_signal_specification/introduction/overview/) standard for vehicle data that currently supports
CAN and OBD-II, or with any data logger in the vehicle. You may also send raw vehicle data
using protocols like HTTP or MQTT and build proprietary ingestion schemes on top of these
protocols. You also want to use Amazon CloudWatch metrics, which allows you to capture message broker metrics such as
number of connections and other metrics related to AWS IoT Core. [AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender.html) can capture cloud-side
metrics, which are agentless metrics generated from IoT devices. You can also capture
device-side metrics which are metrics generated from agents installed on the ECU.

**Store:** AWS provides the ability to easily securely send
vehicle data to AWS. You can use [AWS IoT Core Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) that can send
vehicle logs to over [20 different services](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html).
Commonly you will use IoT Core Rules to route vehicle data to [Amazon S3,](https://aws.amazon.com/pm/serv-s3/?trk=fecf68c9-3874-4ae2-a7ed-72b6d19c8034&sc_channel=ps&ef_id=CjwKCAjwl6OiBhA2EiwAuUwWZV9VeHMVbNw33crX1g54M7QdP12Xdc1Z9O-QWw5Tym30ddped2s9jhoCvsYQAvD_BwE:G:s&s_kwcid=AL!4422!3!536452728638!e!!g!!amazon%20s3!11204620052!112938567994) which is an object storage service that offers industry-leading
scalability, data availability, security, and performance. It is important to define storage
requirements based on your organization and risk determinations. AWS provides [storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) mechanisms in Amazon S3 to define data
lifecycle policies based on your retention and cost requirements. Customers can also use
[Amazon Security Lake](https://aws.amazon.com/security-lake/) to centralize security
logs from AWS and custom sources like the vehicle, charging stations, and more in an
open-source standard format called [OCSF](https://docs.aws.amazon.com/security-lake/latest/userguide/open-cybersecurity-schema-framework.html). Security Lake enables both the centralization of log data and helps customers extract
valuable insights quicker from normalizing to the open standard.

**Process:** You can then process and normalize that data in
any way that fits your business case. AWS provides a service called [AWS Glue](https://aws.amazon.com/glue/) to normalize, prepare, and integrate this
data into a catalog for analysis. This allows customers to build schemas and normalize data
to fit their needs.

**Analyze:** You can then run machine learning and analytics on
this data to understand vehicle related baselines and build models for detection using
services like [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/). Amazon SageMaker AI allows you
to build, train, and deploy machine learning (ML) models for any use case with fully managed
infrastructure, tools, and workflows.

**Visualize:** VSIEMs and VSOC can be used to identify security
patterns based on the data and analytics that are run on the large data sets. Selecting the
right visualization tool and strategy is an important aspect of identifying security trends
and KPIs. AWS provides a number of services to help with visualizing vehicle security
patterns in a detailed graph and report. [Quick](https://aws.amazon.com/quicksight/) is a cloud-native serverless business intelligence service that provides
data visuals, interactive dashboards, and data analytics powered by ML. [Amazon Managed Grafana](https://aws.amazon.com/grafana/) is a fully managed service for
open-source Grafana, a popular open-source analytics service for querying, visualizing, and
understanding your metrics no matter where they are stored. [AWS OpenSearch](https://aws.amazon.com/opensearch-service/) with Kibana gives you the ability to
aggregate logs from all your systems and applications, analyze these logs, and create
visualizations for application and infrastructure monitoring, faster troubleshooting,
security analytics, and more.

You can build a pipeline for vehicle data using the AWS services highlighted above. You can
also consider adopting partner services from [Argus Cyber
Security](https://aws.amazon.com/marketplace/seller-profile?id=c18d1099-5095-4d06-aee4-571c7fa75620) or [Upstream Security](https://upstream.auto/).

CMSEC_10: How do you correlate events from vehicles, backend systems,
suppliers, vendors, and AWS Partners to generate actionable findings?

Organizations must integrate data from many data sources as inputs to VSOCs. It is necessary
to gather information feeds from many relevant data sources that may be relevant when
analyzing vehicle logs and determining vulnerabilities. Correlation requires trained
expertise, proper tooling, and the correct data sources and learning models to provide
accurate true positive results from different vehicle scenarios. Based on the analysis
results, you can use runbooks to guide your response and recovery on the fleet or vehicle,
which is covered in the incident response section of the security pillar.

Analyzing baselines and threat intelligence feeds can provide information that a VSOC analyst can use to build common detection patterns that are
likely to occur. As the threat intelligence data is constantly changing and new threats and vulnerabilities emerge, it is important to provide a
mechanism to continuously monitor for false positives and improve rules based on new data. Organizations should focus on building monitoring
capability around the highest risks to safety and security, the scope of a possible security issue, and the plausibility of the security issue.

**[CMSEC_BP10.1] Gather relevant supplier, vendor, production, API, and
partner data to enhance detection mechanisms by adding further context.**

A vehicle environment contains several different systems that interact with the vehicle and
consumer. Log sources should be collected from any relevant system that can provide
important security and operational insights related to the connected vehicle. Data collected
from backend systems, companion APIs, charging stations, diagnostics databases, AUTOSAR XML
databases, production data, partners, and other custom databases that are relevant to a
connected mobility system. This data can also be stored in Amazon S3 or Amazon Security Lake in OCSF
format.

The goal is to correlate data and build rules based on the models that are trained on
this data. Lastly, correlating findings requires the ability to utilize threat intelligence
and threat hunting resources to inform your environment and your baselines, and this can be
done by integrating threat intelligence and vulnerability feeds to Amazon SageMaker AI mentioned above.
The data can then be integrated into Amazon OpenSearch Service for analytics and uncovering insights, or to
a central IT SOC on AWS or an AWS Partner such as [Datadog](https://www.datadoghq.com/), [Sumo Logic](https://www.sumologic.com/), [New Relic](https://newrelic.com/), [Honeycomb](https://www.honeycomb.io/), or [Splunk](https://www.splunk.com/)**.** Amazon OpenSearch Service makes it possible for you to perform interactive log
analytics, real-time application monitoring, website search, and usage of [Security Analytics
for OpenSearch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-analytics.html) that provides out of the box security visibility. These tools can
provide the ability to detect suspicious vehicle interactions. Commands from a vehicle might
be anomalous, or a vehicle may be communicating to a backend system that it shouldn't or
usually does not communicate to.

It is also important to collect logs from applications that interact with vehicles such
as companion or fleet applications. You can use API logs to determine issues such as an
unauthorized user gaining access to vehicles they are not authorized to interact with. You
can collect logs from sources like [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/view-cloudwatch-log-events-in-cloudwatch-console.html) and AWS IoT Core.

As previously stated, you can build a pipeline to gather relevant data to enhance detection
using the AWS services highlighted above. You can also consider adopting partner services
from [Argus Cyber
Security](https://aws.amazon.com/marketplace/seller-profile?id=c18d1099-5095-4d06-aee4-571c7fa75620) or [Upstream Security](https://upstream.auto/).

CMSEC_11: How do you monitor and detect unauthorized use of vehicle credentials
and identities?

You should be monitoring your ECUs for security best practices continuously. Due to the volume of ECUs and client certificates,
it is important to monitor certificate and CA expiration and revocation. Organizations must monitor ECU permissions to detect overly
permissive actions, and follow best practices when developing authentication and authorization mechanisms. It is also important to
track changes in vehicle patterns that are significantly anomalous and deviating from known expected baselines.

**[CMSEC_BP11.1] Detect security posture deviations and anomalous
behavior**

Monitoring certificate expiry and revocation can be a challenging process. Organizations must
create processes and policies around the distribution and management of CAs and client
certificates. [AWS IoT Device Defender Audit](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit-checks.html)
provides the ability to monitor CA and client certificates that are nearing expiration (30
days) or that have been revoked. Organizations must detect overly permissive ECUs and scope
down permissions as needed. AWS IoT Device Defender Audit can help to identify overly permissive policies
that may be granting access to a broad set of resources instead of just a few.

Finally, organizations must build out vehicle baselines and automated alerting on
anomalous behavior. Baselines might include expected number of connections, expected
subscribed topics, expected protocols, expected payloads, and more. If a vehicle is
deviating from those, such as sending suspicious commands, these should be detected. [AWS IoT Device Defender
Detect](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html) can help with the creation of rules or ML baselines to detect anomalous
traffic based on pre-defined or custom metrics specific to your fleets, or even a group of
devices in a profile.

For example, AWS IoT Device Defender Detect can provide you with visibility into ECU behavior such as the
ECU failing authorization to multiple topics which may indicate the ECU trying to gain
access to a topic that it is not authorized to publish or subscribe to. You can then trigger
an [Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) which allows you to watch CloudWatch metrics and to receive
notifications when the metrics fall outside of the levels (high or low thresholds) that you
configure.

Alarms can send [Amazon SNS](https://aws.amazon.com/sns/) notifications, which is
a web service that coordinates and manages the delivery or sending of messages to
subscribing endpoints or clients. Detect and Rule based findings integrate with [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/), which is a cloud security posture
management service that performs security best practice checks, aggregates alerts, and
enables automated remediation.

CMSEC_12: How do you stay current and monitor on new threats and
vulnerabilities after concept and design phase?

Organizations must continually ingest data from the vehicle and internal systems, as well as
public and private data sources. Vehicles have several potential vulnerabilities that are
unlike traditional IT systems. Defining a threat intelligence process and collecting data
from a wide range of relevant sources will provide information on expected and emerging
threats and vulnerabilities.

While protecting software and firmware from vulnerabilities is important, vehicle
security programs must also consider emerging threats such as sensor fusion risks to the
vehicle. An organization should develop mechanisms to consume a large variety of threat
intelligence as well as share and collaborate across a sharing body such as [Auto-ISAC](https://automotiveisac.com/) to share learnings in a timely manner.

**[CMSEC_BP12.1] Subscribe to threat intelligence feeds from many
different sources to detect threats and vulnerabilities**

You should analyze threat intelligence feeds from several data sources both public and private, beyond what is coming off of the vehicle or
what is in your environment. This can include things like governments, vendors, information sharing bodies, peers, suppliers, open-source
intelligence, and more. You may subscribe to specific vulnerability feeds regarding specific software and firmware running on the vehicle to
address emerging threats and further enhance detection baselines to respond when emerging threats and vulnerabilities are known. It is important
to maintain an inventory of embedded software and firmware, as well as operating systems, packages, and libraries that are used per vehicle model
and type so that you are aware of what is relevant to your environment based on threat intelligence feeds.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/detection.html*

---

# Infrastructure protection

CMSEC_13: How do you protect your systems and APIs from unauthorized access or
exposure?

**[CMSEC_BP13.1] Define a baseline of normal behavior for your vehicle as
a reference and reject and alert on any request patterns that deviate.**

Implement a solution to create a baseline of metrics for vehicles within your fleet. For
example, AWS IoT Device Defender can be used for devices which connect to AWS IoT Core. This baseline can help
in detecting anomalies such as impossible motion speeds, or a vehicle existing in multiple
locations simultaneously. Through the use of [Security Profiles](https://docs.aws.amazon.com/iot/latest/developerguide/detect-behaviors.html) within IoT
Core and the enablement of metrics by Device Defender a threshold can be established to
define this anomalous behavior. These thresholds can be either rule-based or use Machine
Learning to evaluate how these devices should behave. An alert is generated when the defined
threshold is crossed which can be used to perform automated mitigation actions you define
such as updating a policy or certificate and can also send notifications via Amazon Simple Notification Service
(SNS).

CMSEC_14: How do you test Electronic Control Units (ECUs) and implement
configuration changes to minimize vulnerabilities?

**[CMSEC_BP14.1] Conduct threat modeling using a formal methodology such
as the MITRE Threat Assessment and Threat Analysis Risk Assessment (TARA) on in-vehicle
systems.**

**[CMSEC_BP14.2] Conduct tests on ECUs to determine if there are any
unnecessary configurations such as open ports, default permissions, unnecessary services
running, or other vulnerabilities.**

**[CMSEC_BP14.3] Develop requirements and processes to address and
remediate vulnerabilities discovered through testing.**

CMSEC_15: How do you manage processes for updating the software of components
within your connected vehicles?

**CMSEC_BP15.1] Validate all software updates are cryptographically
signed upon release and verified before installation.**

For devices which use AWS IoT, software updates can be signed using AWS Signer a fully managed code-signing service. AWS Signer uses certificates imported to AWS Certificate Manager to sign software, AWS Identity Access Management (IAM) to assign roles to restrict who can sign and in what Region. All actions within AWS Signer are also captured in AWS CloudTrail for auditing purposes.

**[CMSEC_BP15.2] Test software packages for vulnerabilities and errors
prior to deployment.**

**[CMSEC_BP15.3] Perform controlled and secure deployment of software
to vehicle fleets with rollback capabilities in case of failures.**

CMSEC_16: How do you maintain an accurate inventory of your connected vehicles
and associated software or hardware components?

**[CMSEC_BP16.1] Maintain an accurate and continuously updated
inventory of vehicles and any versions of software packages or underlying hardware.**

This should include any applicable Software Bill of Material (SBOM) documents as
outlined by something such as [The Minimum Elements For a Software Bill of Materials (SBOM)](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf) pursuant to [Executive Order 14028](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) including any [Vulnerability
Exploitability eXchange (VEX)](https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf) documents as outlined by the United States
Department of Energy in coordination with the National Telecommunications and Information
Administration. A VEX document is an attestation and contains information about a product
and whether it is affected by a known vulnerability.

CMSEC_17: How do you verify the integrity of the software running within your
vehicles?

**[CMSEC_BP17.1] Use methods for ensuring integrity such as through
secure boot and software signing methodologies.**

CMSEC_18: How do you secure the Software Development Lifecycle (SDLC)?

**[CMSEC_BP18.1] Develop SDLC policies which govern these requirements
and provide prescriptive guidance for implementing required controls.**

CMSEC_19: How do you manage vulnerabilities for your connected
vehicles?

**[CMSEC_BP19.1] Continuously monitor informational feeds on threat
intelligence from vendors, suppliers, third-party intelligence providers, repositories,
and communities.**

Threat intelligence feeds provide additional insights into signatures of potentially
malicious activity such as malware, botnets, and phishing. This information helps to
supplement the tools already in use by security teams to understand the current threat
landscape at a broader scope. AWS Partners such as Recorded Future and Tenable provide
threat intelligence feeds and are readily available through the AWS Marketplace. IP based threat
lists from these providers can also be used to supplement detections within [AWS GuardDuty](https://aws.amazon.com/guardduty/) our purpose-built threat
detection service. Customers can also leverage an AWS partner like Argus Cyber Security to
help implement in-vehicle security systems like an Intrusion Detection System for Controller
Area Networks (CAN), vehicle vulnerability management, and firewall capabilities to protect
components. Industry specific feeds such as Auto-ISAC can provide additional insights based
on contributions from organizations within automotive.

**[CMSEC_BP19.2] Conduct vulnerability impact analysis and testing in
isolated and secure environments.**

When conducting tests of vulnerabilities on systems or investigating potentially compromised
systems an isolated and secure environment should be used. This verifies that other
resources are not inadvertently impacted or compromised by these activities. When conducting
this testing in AWS environments a separate Account should be created to provide
segmentation from other Accounts and resources. Strong defense-in-depth configurations
should also be used such as for forensic investigations. Some of these strategies are
outlined in the [Forensic investigation environment strategies in the AWS Cloud](https://aws.amazon.com/blogs/security/forensic-investigation-environment-strategies-in-the-aws-cloud/) blog post.

**[CMSEC_BP19.3] Define a process for classifying and prioritizing
vulnerabilities for remediation.**

Processes for classification, prioritization, and remediation of vulnerabilities should be
formally documented and readily accessible to stakeholders. Playbooks and runbooks specific
to your organizations technology stack and operational processes should be used as a means
of automating segments of the investigation and help minimize manual errors during a
potentially stressful situation. Automation can be accomplished through solutions such as
Jupyter Notebooks or running automation documents within AWS Systems Manager for example.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/infrastructure-protection.html*

---

# Data protection

CMSEC_20: What are your encryption requirements for vehicle data?

Vehicles can collect and generate data with different levels of sensitivity and risk to your
organization. You must check that the data is protected using appropriate means to comply
with applicable standards, regulations, and laws. Encrypting the data in transit and at rest
and controlling access to the encryption keys can be an effective technical means to help
meet your data protection requirements. Begin by [classifying the
data](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html) generated by the vehicle to determine the type of encryption required in
transit and at rest.

Consider the following best practices for encryption:

**[CMSEC_BP20.1] Implement TLS 1.2+ to encrypt data in
transit**

By implementing TLS 1.2+ from the ECU to the connected vehicle service backend you get
encryption in transit. With the addition of X.509 client certificates on the ECUs for mutual
TLS you also get authorization of requests. Verify that you follow the best practices on
managing the lifecycle of certificates as described above.

On AWS, you can use mutual TLS 1.2+ with [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html) and [Amazon API Gateway REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html) to authenticate ECUs using X.509 client certificates. You can
also terminate mutual TLS on software deployed to AWS compute services (Amazon EC2, Amazon EKS, or
Amazon ECS) behind a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
(NLB). Individual AWS service API requests are authenticated using the [sigv4](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html) algorithm.

**[CMSEC_BP20.2] Consider client-side encryption of highly sensitive
data at the ECU**

When highly sensitive data is transmitted from the vehicle to a connected vehicle backend, you may consider implementing client-side encryption
of the data. In this approach, the vehicle ECU encrypts the sensitive data payload ***before***
transmitting it to the connected vehicle backend service. The encrypted payload is transmitted via any intermediate systems to the backend system
that has access to the keys to decrypt the payload and recover the sensitive data in the clear. Note that message parts such as HTTP headers and MQTT
topic names should still be transmitted without client-side encryption so that intermediate nodes can route and queue messages. The benefit is that
any intermediate systems such as a load-balancer or message broker are unable to see the sensitive data payload in the clear as these systems do
not have permissions on the keys. This scheme relies on managing the encryption keys securely and granting least-privilege permissions on keys
to the ECU and backend servers.

An effective pattern for client-side encryption is envelope encryption in conjunction with a
key management system. In this pattern, the plaintext sensitive data is encrypted by the ECU
with a *data key* and the data key is encrypted under another key that is
managed in a key management system. The ECU transmits the encrypted data and the encrypted
data key to the backend service. The backend service invokes the key management system to
decrypt the encrypted data key, recovering the plaintext data key. It can then use the
plaintext data key to decrypt the encrypted data. The ECU can cache the data key for a
period of time or for a certain volume of data, improving performance by minimizing the need
to invoke the key management service for every sensitive data element. An intermediate
system that receives the encrypted data key does not have permissions to invoke the key
management system to decrypt the data key and as a consequence cannot decrypt the encrypted
data. The sensitive data payload remains encrypted end-to-end from the ECU to the backend
service in transit and at rest.

On AWS, you can use the [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) to
securely manage your encryption keys for [envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping). You
can use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html)
to implement envelope encryption with [data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/data-key-caching.html)
on the ECU and backend servers to improve performance, help reduce cost, and stay within the
AWS KMS service limits as your application scales. Your ECUs can obtain temporary AWS API
credentials to invoke AWS KMS API calls by using the [AWS IoT Credential
Provider](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html).

CMSEC_21: How do you identify and protect data in your connected vehicle
service?

Classify the data processed by your connected vehicle service as described in [Well-Architected
Security Data Protection](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-07.html). Specifically, consider how you will classify data such
as Vehicle Identifier (VIN), ECU serial number, vehicle location (coarse vs precise), and
operator identity. Consider the specific requirements that apply to your organization,
depending on factors such as where you conduct business, any industry-specific regulations,
the type of data, where or from whom the data originates, and where the content is stored
and processed.

Consider the following best practices to protect data.

**[CMSEC_BP21.1] Do not use sensitive data to name and reference
resources**

You may have several resources in your connected vehicle architecture that must be uniquely named.
Avoid using sensitive data such as the VIN, customer identity, location in these resources so that you can more effectively
control access to the data. For example, when using MQTT, avoid using the VIN in the topic names used to send and receive
messages from a vehicle's ECUs. MQTT topic names are often logged to audit log files, and can be used when subscribing to messages.
Using a hashed VIN or another unique identifier that cannot be mapped to a VIN will help you limit the number of locations,
systems and people that can see the VIN.

On AWS, you can use [Amazon Macie](https://aws.amazon.com/macie/) to discover and help protect your sensitive data.
Macie uses a combination of criteria and techniques, including machine learning and pattern matching, to detect sensitive data in
Amazon Simple Storage Service (Amazon S3) objects. Macie can detect a large and growing list of
[sensitive data types](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html)
for many countries and regions, including multiple types of credentials data, financial data, personal health information (PHI),
and personally identifiable information (PII). VIN can be detected using a managed data identifier. Additionally, you can
build [custom data identifiers](https://docs.aws.amazon.com/macie/latest/user/custom-data-identifiers.html)
using regular expressions (regex) to match vehicle specific identifiers, such as ECU IDs, and ECU serial numbers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/data-protection.html*

---

# Incident response

CMSEC_22: Does your team deploy a VSOC? If so, what are the required
capabilities of a VSOC?

A VSOC has become a compliance requirement for automotive
cybersecurity management systems very recently. An incident
may involve safety implications, making incident response a
critical component of a security program. A VSOC must contain
automotive specific playbooks that are relevant to your
business case, collaboration across IT SOC, cloud SOC, and
VSOC, continuous improvement and lessons learned. A VSOC must
have many of the detection mechanisms we described above
[refer to CM_SECBP20 for detection] as well as providing
triage, containment, recovery, and lessons learned to your
monitoring and remediation program. A VSOC also requires
trained personnel that are capable of addressing different
vehicle alerts with varying complexity.

**[CMSEC_BP22.1] Define VSOC capabilities and requirements, then
develop and test your VSOC incident response plan.**

To successfully respond to an incident, you must first define VSOC capabilities and
requirements. This aligns with compliance or risk-based security requirements. You then
prepare your incident response plan and runbooks that are referenced during a potential
security incident. The incident response plan contains several components that span across
an organization, and cover both business and technical steps. AWS provides [Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) which define the actions that Systems Manager performs on
your managed instances and other AWS resources when an automation runs. runbooks contain
one or more steps in sequential order. You can use runbooks for manual approvals or trigger
a workflow.

The VSOC should include security orchestration automation and response (SOAR) and
ticketing capability to provide timely responses and workflows that can prioritize and
address incidents. Customers can send findings to AWS Security Hub CSPM, which integrates with issue
tracking systems like [ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-config-security-hub.html) and [Jira](https://docs.aws.amazon.com/smc/latest/ag/jsmcloud-config-security-hub.html).
The incident response procedure must be consistent, accurate, and updated when necessary.
Running game days and tabletop exercises can provide insight about the ability to handle an
incident in a practice environment. Game days, also known as simulations or exercises, are
internal events that provide a structured opportunity to practice your incident management
plans and procedures during a realistic scenario.

**[CMSEC_BP22.2] Train or outsource personnel to manage security
incidents at multiple layers of complexity.**

One of the major observed gaps is a lack of expertise in vehicle incident response.
You must determine if your organization has the resources, processes, and skills in place to
address vehicle incidents and events at multiple tiers based on the severity and complexity
of the incident. Organizations might shift responsibility to an AWS Partner or vendor to manage
their VSOC and personnel to identify, prepare, analyze, contain, and recover from a vehicle
security incident. Argus Cyber Security provides consultive and managed VSOC services that
can help address those security needs.

CMSEC_23: How do you contain, recover, and learn from incidents that can span
vehicles, backend systems, APIs, IT, cloud, AWS Partners, and supplier
resources?

Organizations must be able effectively respond to an incident
and notify the organization of severity and scope. This
involves processes to triage and prioritize, response and
recovery activities, and properly monitoring and closing an
incident after confirming the incident has been fully
resolved. Organizations will then continuously improve by
going through lessons learned and using the process to inform
the next set of service improvements after the incident has
been mitigated and resolved.

**[CMSEC_BP23.1] Mitigate and respond to potential incidents by
creating and testing policies, procedures, and playbooks**

During a potential vehicle security issue, it is necessary to
attempt to automate and respond to an incident promptly. By
using runbooks, you can automate several workflow tasks like
notifying different stakeholders and creating a ticket. You
must be able to contain the scope of the issue. Depending on
the finding, you can issue APIs to AWS IoT Core where you can
automate changing a certificate status based on the incident.
If a vehicle is compromised, you can build a workflow that
will inactivate or revoke a certificate and block
communications to AWS IoT Core while you investigate the
incident. You should follow your incident response procedure
to then recover the vehicle back to a non-compromised state
which can vary in complexity depending on the incident.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/incident-response.html*

---

# Application security

CMSEC_24: How do you make sure that only trusted software components are
running on vehicle hardware?

**[CMSEC_BP24.1] Consider digitally signing software and firmware with a
certificate that can be verified by the vehicle hardware during runtime ensuring that only
trusted code can run on the vehicle.**

Code signing and secure boot are essential for ensuring the security and safety of vehicle
software. They help you validate authenticity and integrity of the software running in
vehicle making sure that it comes from a trusted source and its behavior has not been
altered. A secure boot mechanism helps prevent unauthorized code from running on the vehicle
hardware by verifying the integrity of the boot loader and operating system. You can
leverage [AWS Private Certificate Authority](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) (AWS Private CA) that allows you to create private certificate authority (CA)
hierarchies, including root, code signing certificates issuing CAs and code signing
certificates. If you are leveraging AWS IoT you can also use [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) to sign code that you
create for IoT devices supported by Amazon FreeRTOS and AWS IoT device management. Code
signing for AWS IoT is integrated with AWS Certificate Manager.

CMSEC_25: How do you check that you are writing, testing, validating, and
deploying vehicle software securely?

**[CMSEC_BP25.1] Implement a Secure Development Lifecycle (SDLC) for
your vehicle software following open standards.**

Start by identifying and creating a list of cybersecurity metrics and requirements that needs to be met to verify your
software security regarding ISO 21434 standard from conception, product development to cybersecurity validation.

Create and document early in the design phase a threat model for your in-vehicle software or
system such Head Units (HU) or Telematic Control Units (TCU). You can leverage established
frameworks such STRIDE (Spoofing, Tampering, Repudiability, Information Disclosure, Denial
of Service, and Elevation of Privilege) or the TARA framework in ISO 21434 for in-vehicle
products and services, from identifying assets in the target system, vulnerabilities and
attack scenarios and their impact, those most likely to be exploited and risk treatment
decision. AWS provides an example [threat modeling workshop](https://catalog.workshops.aws/threatmodel/en-US) and
corresponding [blog post](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/) to apply some principles when threat modeling a connected vehicle cloud
application.

Implement secure coding, development process and architectural design following open
standards guidelines such AUTOSAR and ASPICE (examples: input validation, buffer overflow
protection, error handling to prevent attacks such as SQL injection and cross-site scripting
and hardcoded credentials). Conduct code reviews and security audit of the code to identify
security vulnerabilities that may be missed during development. Test and validate the
software in simulated and real-world scenarios to check it is safe and reliable.

You can leverage the [KPIT Cloud Native Engineering Workbench](https://aws.amazon.com/blogs/industries/accelerating-sdv-development-with-kpit-cloud-native-engineering-workbench-on-aws/) solution on AWS to help accelerate your
software-defined vehicle (SDV) development and testing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/application-security.html*

---

# Key AWS services

- [Amazon Inspector](https://aws.amazon.com/inspector/)
- [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html)
- [AWS Private CA](https://aws.amazon.com/private-ca/)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [AWS WAF](https://aws.amazon.com/waf/)
- [AWS Shield](https://aws.amazon.com/shield/)
- [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [AWS IoT Family](https://aws.amazon.com/iot/)
- [Amazon Security Lake](https://aws.amazon.com/security-lake/)
- [AWS Key Management Service](https://aws.amazon.com/kms/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [Amazon Macie](https://aws.amazon.com/macie/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Quick](https://aws.amazon.com/quicksight/)
- [Amazon Managed Grafana](https://aws.amazon.com/grafana/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/key-aws-services-sec.html*

---

# Resources

**Documentation and blogs**

- [Securing Modern
Connected Vehicle Platforms with AWS IoT](https://aws.amazon.com/blogs/iot/securing-modern-connected-vehicle-platforms-with-aws-iot)
- [How to approach threat modeling](https://aws.amazon.com/blogs/security\how-to-approach-threat-modeling)
- [Best practices securing Amazon Location Services](https://aws.amazon.com/blogs/security\best-practices-securing-your-amazon-location-service-resources)
- [How to detect anomalies in device metrics and improve security posture with
AWS IoT Device Defender](https://aws.amazon.com/blogs/iot/how-to-detect-anomalies-in-device-metrics-and-improve-your-security-posture-using-aws-iot-device-defender-custom-metrics/)
- [Forensic investigation environment strategies in the AWS cloud](https://aws.amazon.com/blogs/security\forensic-investigation-environment-strategies-in-the-aws-cloud)

**AWS Partner solutions**

- [DataMasque](https://aws.amazon.com/blogs/apn/how-to-mask-sensitive-data-on-aws-using-datamasque/)
- [Argus Cyber
Security](https://aws.amazon.com/marketplace/seller-profile?id=c18d1099-5095-4d06-aee4-571c7fa75620)
- [Recorded
Future](https://aws.amazon.com/marketplace/seller-profile?id=0e798044-1f43-48fa-8621-cf2207e7e204)
- [Tenable](https://aws.amazon.com/marketplace/seller-profile?id=6d2fe217-0f2b-4853-bf6b-44b37d172a3d)
- [Upstream
Security](https://aws.amazon.com/marketplace/seller-profile?id=c2e4bab5-137c-4059-86e5-1acbca8bb7ba)

**Workshops**

- [Automating operations with Playbooks and Runbooks](https://https://catalog.workshops.aws/well-architected-operational-excellence/en-US/2-prepare/10-automating-operations-with-playbooks-and-runbooks/operational-excellence/200_labs/200_automating_operations_with_playbooks_and_runbooks/)
- [Incident Response labs](https://catalog.workshops.aws/well-architected-security/en-US/6-incident-response)
- [Threat modeling for
builders](https://catalog.workshops.aws/threatmodel/en-US)
- [Security for Developers](https://catalog.workshops.aws/sec4devs)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/resources-sec.html*

---
