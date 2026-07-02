# IOTSEC03 — Security

**Pillar**: Security  
**Best Practices**: 2

---

## IOTSEC03-BP01 Implement authentication and authorization for users accessing IoT resources

This practice provides users with secure access to connected IoT
devices and equipment through different channels such as web or
mobile devices. Without valid authentication and authorization,
devices can be subjected to risks of unauthorized access.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC03-BP01-01** *Implement an identity
store to authenticate users of your IoT application.*

Implement an identity and access management solution for end
users. This solution should allow end users with temporary,
role-based credentials to access the IoT solution. For example,
you can use a service like Amazon Cognito to create user pools
for authentication. Or, you can use Amazon Cognito integration
with SAML 2.0 or OAuth 2.0 compliant identity providers for
authentication as well. If you host your own identity store, use
AWS IoT custom authorizers to validate tokens such as JWT and
SAML 2.0 for authenticating users. AVP can be used to define
fine-grained access control policies to specify who (identity)
can perform what actions on which resources (application, data,
and devices).

**Prescriptive guidance
IOTSEC03-BP01-02** *Grant least privilege
access*

Authorization is the process of granting permissions to perform
some operation or access some information by an authenticated
identity. If using AWS IAM credentials, you grant permissions to
your users in AWS IoT Core using data plane and control plane
IAM policies through the Identity broker. AWS IoT control plane
APIs allow you to perform administrative tasks like creating or
updating certificates, things, and rules. AWS IoT data plane
APIs allow you send data to and receive data from AWS IoT Core.

For example, if you are using Amazon Cognito, use federated
identities for user authentication and Amazon Cognito identity pools to
establish IAM credentials. If you are using a different Identity
provider than Amazon Cognito, use AWS IoT custom authorizers to
invoke lambda functions that will create the required IAM
policies. To define fine-grained permissions for Amazon Cognito
users, use AVP to define authorization policies in which the
principal is the Amazon Cognito user or group.

**Prescriptive guidance
IOTSEC03-BP01-03** *Adopt least privilege when
assigning user permissions.*

Adopt the least privilege principle and assign only the minimum
required permissions to each IAM role that is used in the
solution. This applies to both user and service (For example,
Lambda function) roles that are defined in the solution.

For example, with Amazon Cognito Identity Pools this can be
achieved by setting up role-based access through IAM policies
for authenticated users like consumers or administrators as well
as unauthenticated users. Consumers or unauthenticated users
should not be allowed to run adminstrative actions against IoT
services, such as detaching policies, deleting certificate
authorities (CAs), or deleting certificates.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/identity-and-access-management.html*

---

## IOTSEC03-BP02 Decouple access to your IoT infrastructure from the IoT applications

For implementing the decoupled view of telemetry for your users,
use a mobile service such as AWS AppSync or Amazon API Gateway.
With both of these AWS services, you can create an abstraction
layer that decouples your IoT data stream from your user's
device data notification stream. By creating a separate view of
your data for your external users in an intermediary datastore,
you can use AWS AppSync to receive user-specific notifications
based only on the allowed data in your intermediary store.
Examples of intermediate data stores are Amazon DynamoDB, Amazon Relational Database Service, and Amazon OpenSearch Service. In
addition to using external data stores with AWS AppSync, you can
define user specific notification topics that can be used to
push specific views of your IoT data to your external users.

If an external user needs to communicate directly to an AWS IoT
endpoint, make sure that the user identity is either an
authorized Amazon Cognito Federated Identity that is associated
to an authorized Amazon Cognito Identity Pool role and a
fine-grained IoT policy, or uses AWS IoT custom authorizer,
where the authorization is managed by your own authorization
service. With either approach, associate a fine-grained policy
to each user that limits what the user can connect as, publish
to, subscribe from, and receive messages from concerning MQTT
communication.

By decoupling the IoT infrastructure from the end-user IoT
applications, you can build an additional layer of security and
reliability.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC03-BP02-01** *Use an API layer between
the application and IoT layer.*

Build an application interface layer to insulate the IoT data
plane from end users. Fundamentally, the primary interface to
IoT data plane is MQTT topics. Protecting the data plane
essentially means protecting the MQTT topics from unwanted
communication.

For example, use Amazon API Gateway or AWS AppSync to provide a
REST or GraphQL API interface between the end user application
and the IoT layer. With this design, an API implementation,
often built using an AWS Lambda function, would communicate with
devices using the IoT data plane. This insulates the operations
on the IoT data plane from the end user interaction performed at
the REST or GraphQL API interfaces. Fine-grained permissions for
using the API interfaces can be defined using AVP.

IOTSEC04: How do you apply least
privilege to principals that interact with your IoT
application?

After registering a device and establishing its identity, it may
be necessary to add additional device information needed for
monitoring, metrics, telemetry, or command and control. Each
resource (for example, device, background task, service, API,
and user) requires its own assignment of access control rules.
By reducing the actions that a device or user can take in your
application, and making sure that each resource is secured
separately, you reduce the risks to your system in case a single
identity is compromised.

In AWS IoT, create fine-grained permissions by using a
consistent set of naming conventions in the IoT registry. The
first convention is to use the same unique identifier for a
device. Match the MQTT ClientID and AWS IoT thing name. By using
the same unique identifier in all these locations, you can
easily create an initial set of IoT permissions that can apply
to your devices using
[AWS IoT Thing Policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/thing-policy-variables.html). The second naming convention
is to embed the unique identifier of the device into the device
certificate. Continuing with this approach, store the unique
identifier as the `CommonName` naming element in the subject name
of the certificate so that
[Certificate Policy VariablesX.509 Certificate AWS IoT Core policy
variables](https://docs.aws.amazon.com/iot/latest/developerguide/cert-policy-variables.html) can be used to bind IoT permissions to each
unique device principal.

By using policy variables, you can create a few IoT policies
that can be applied to your device certificates while
maintaining least privilege. For example, the IoT policy below
would restrict devices to connect only using the unique
identifier of the device which is stored in the common name as
its MQTT ClientID (see policy variable inserted into Resource
name) and only if the certificate is attached to the device.
This policy also restricts a device to only publish on its
individual shadow (see policy variable inserted into MQTT
topic):

Attach your device identity (certificate or Amazon Cognito
Federated Identity) to the thing in the AWS IoT registry using
[AttachThingPrincipal](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachThingPrincipal.html)
and attach the policy to principals using
[AttachPolicy](https://docs.aws.amazon.com/iot/latest/apireference/API_AttachPolicy.html).

Although these scenarios apply to a single device communicating
with its own set of topics and device shadows, there are
scenarios where a single device needs to act upon the state or
topics of other devices. For example, you may be operating an
edge appliance in an industrial setting, creating a home gateway
to manage coordinating automation in the home, or allowing a
user to gain access to a different set of devices based on their
specific role. For these use cases, leverage a known entity,
such as a group identifier or the identity of the edge gateway
as the prefix for all of the devices that communicate to the
gateway. By making all of the endpoint devices use the same
prefix, you can make use of wildcards, `"*"`, in your
IoT policies. This approach balances MQTT topic security with
manageability.

In the preceding example, the IoT operator would associate the
policy with the edge gateway with the identifier,
edgegateway123. The permissions in this policy would then allow
the edge appliance to publish to other Device Shadows that are
managed by the edge gateway. This is accomplished by enforcing
that connected devices to the gateway all have a thing name that
is prefixed with the identifier of the gateway. For example, a
downstream motion sensor would have the identifier
`edgegateway123-motionsensor1`, and therefore can now be managed
by the edge gateway while still restricting permissions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/identity-and-access-management.html*

---
