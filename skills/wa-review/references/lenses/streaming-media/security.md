# Security

**Pages**: 6

---

# Identity and access management

Streaming media workloads carry audio and video for many
different purposes. In entertainment, these streams often carry
high-value, licensed content delivered to large audiences. In a
corporate setting, where streaming media is increasingly used to
connect with employees, streams can carry commercially sensitive
material. A strong identity foundation protects your content,
viewers, and confidential business information.

SM_SEC1: How do you authorize access to content and content ingest?

**SM_ SBP1 – Use an identity provider to authenticate
viewers and access policies to implement least privilege access to protected
content**

**SM_SBP2 – Restrict content origin access to allow only
authorized content distribution networks**

Whether on mobile, desktop, or SmartTV, web applications serve
as the box office for audiences interested in your content.
Authentication and authorization systems help ensure that only
authorized users can access content in the way you intend. For
example, a user authenticates through sign-up/sign-in and is
authorized to access only *free* or
*ad supported* content tiers based on their
current subscription plan. Identity is essential for a
centralized strategy on authorizing access to resources.

Access to private content should be granted only to
authenticated and authorized viewers using an identity provider
(IdP). On AWS, Amazon Cognito can be used as an IdP to
authenticate users and authorize access to content hosted on
Amazon S3, AWS Elemental MediaPackage, AWS Elemental MediaStore,
or on a custom origin service built on Amazon EC2. You can also
establish trust between identity providers to avoid sharing
credentials and simplify the authentication flow for your media
player. Amazon Cognito provides both temporary AWS credentials
as AWS STS (Security Token Service) tokens, as well as JWTs
(JSON Web Tokens), to access protected resources. Amazon Cognito
also allows you to federate an identity pool or user pool with
different identity providers, such as SAML providers like Active
Directory Federation Services or Okta, OIDC providers such as
Auth0, and other public identity providers such as Google,
Twitter, or Facebook.

In addition to leveraging an IdP, centralize resource access
control based on the identity established by IdP through the
application API layer. For example, Amazon API Gateway and AWS AppSync allow you to specify an Amazon Cognito User Pool as an
IdP for the resources being protected, so that bearer tokens can
be validated before granting access. Amazon API Gateway and AWS AppSync also allow you to create custom authorizers, so that you
can perform additional application logic to allow or deny access
to a resource based on claims in the access token, or if a
non-supported token, such as SAML, is provided to the API.

Even authenticated users can act maliciously with your
workloads, so you should consider how to secure the data path of
your video streams. Tokenization schemes such as signed-URLs,
signed-cookies, or JWTs (JSON Web Tokens) should be used to
grant only temporary access to content by approved front-end
applications. Amazon CloudFront can protect access to content
origin through signed URLs and signed cookies with a short
duration to live, and Lambda@Edge can validate bearer tokens
during viewer request.

When using content distribution networks to accelerate
distribution to viewers, help to protect your content origin
from unauthorized origin access by validating a secret header
injected by the CDN transmitted over TLS at the time of request
and use a policy that prevents access from all other entities.

When using AWS Elemental MediaStore as an origin, you can
configure MediaStore to accept requests to your container only
if the user-agent header value is set to a shared secret value
with
[IAM
Policy Conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html). With Amazon CloudFront, your
distribution can identify itself by injecting the user-agent
header secret value during requests for objects within the
MediaStore container. This method can also be applied to content
origin services running on Amazon EC2. You can apply this secret
check on the service itself and employ a web application
firewall, such as AWS WAF, to perform the check on your behalf.

When serving video-on-demand content from Amazon S3, configure
Amazon CloudFront to use an origin access identity (OAID) and
then restrict access to your Amazon S3 bucket by placing an S3
bucket policy to allow access from your Amazon CloudFront
distribution only if it identifies itself with that OAID. OAID,
when combined with Signed URLs and user authentication, is
designed to ensure that only requests through Amazon CloudFront
will return successfully and prevent any direct requests to your
bucket origin, and will negate the need for direct access to
your buckets.

```
`{
"Version": "2012-10-17",
"Id": "PolicyForCloudFrontPrivateContent",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity 111122223333"
},
"Action": "s3:GetObject",
"Resource": "arn:aws:s3:::DOC-EXAMPLE-BUCKET/*"
}
]
}`
```

*Example S3 bucket policy for CloudFront origin access
identity (OAID)*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/identity-and-access-management.html*

---

# Detective controls

You can use detective controls to identify a potential security
threat or incident.  Viewer access patterns provide streaming
platforms with a rich data source that can help publishers
create engaging content, improve playback experiences, and
identify potential security risks. However, unwanted user
behaviors, such as credentials sharing and credential
compromise, can lead to unauthorized access to your content. A
combination of client and infrastructure logging can be used to
baseline expected content access behaviors and alert upon
deviations.

SM_SEC2: How do you monitor access to your media distribution workload?

**SM_SBP3 – Monitor for fraudulent access
attempts**

**SM_SEC3 – How do you monitor unauthorized re-distribution
of your content?**

**SM_SBP4 – Implement content or sessions
forensics**

For example, content requests through Amazon CloudFront can be
logged and aggregated into Amazon S3. Amazon Athena can then
query this access data for abnormalities like:

- **Request location** — Are
requests only coming from geographic Regions where you would
expect? Is the user location obfuscated by a downstream
provider?
- **Request IP** —Is a specific
IP address requesting content in a pattern that reflects
normal viewing habits?
- **User Agent** —Is the
user-agent string from the device one that is known and
valid?

Monitor activities such as sign-in attempts from new locations
and devices, assign a risk score based on the activity, and
decide to either prompt users for additional verification or
block the sign-in request. You can notify users of suspicious
sign-in attempts and prompt them to secure their accounts. You
can also view a history of sign-in attempts and their risk
scores. The advanced security features in Amazon Cognito can
also help you identify password sharing, reuse, or theft.

While monitoring can help to protect from unauthorized platform
access, you should implement controls that can help you when
valued content is distributed without consent. It is unlikely
that you can completely prevent a viewer from copying content,
but forensic controls can greatly improve incident response when
improper distribution is detected.

As a simple example, you might have seen content on an inflight
entertainment system that had the name of the airline embedded
on the content. This overlay might appear periodically or
throughout the entire piece of content and is used by content
owners to determine if leaked content originated from
an airline. Video encoders like AWS Elemental MediaConvert can
burn in these visible watermarks into your content as an
identifiable image overlay. While simple and effective for a few
unique watermarks, this method requires a unique piece of
content for each watermark and is therefore limited by the cost
of storing multiple versions of the same content.

For large-scale per-viewer, implement a content identification
strategy that allows you to trace back to specific clients, such
as per-user session-based watermarking. With this approach,
media is conditioned during transcoding and the origin serves a
uniquely identifiable pattern of media segments to the end user.
A session to a user-mapping service receives encrypted user ID
information in the header or cookies of the request context and
uses this information to determine the uniquely identifiable
pattern of media segments to serve to the viewer. This approach
requires multiple distinctly watermarked copies of content to be
transcoded, with a minimum of two sets of content for A/B
watermarking. Forensic watermarking also requires YUV
decompression, so encoding time for 4K feature length content
can take upwards of 20 hours. DRM service providers in the AWS Partner Network (APN) are available to aid in the deployment of
per-viewer content forensics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/detective-controls.html*

---

# Infrastructure protection

Infrastructure protection for streaming media involves securing
all resources from end to end, which includes the ingest
endpoints, content origin endpoints, DRM services, and the
client, from unintended or unauthorized access or potential
vulnerabilities.

SM_SEC4: How do you protect content ingest endpoints?

**SM_SBP5 – Encrypt content ingest traffic using
TLS**

**SM_SBP6 – Use private connectivity when working with
partners**

**SM_SBP7 – Encrypt content at rest when delivering via
physical medium**

Streaming media services depend on a reliable content ingest
endpoint to upload, process, and deliver engaging content. These
endpoints need to support transit protection to ensure that
content being uploaded can’t be intercepted or intentionally
degraded during transit. Live and file-based content uploads can
be accomplished in several ways:

- Direct upload over the public network to a custom
processing fleet or a cloud service
- Private network connectivity for direct uploading to a
custom processing fleet or a cloud service
- Offline delivery of content to a remote facility to store
and process

To help ensure that content cannot be intercepted between the
publisher and ingest endpoints, you should encrypt uploads in
transit and use TLS at both the source and destination. To
simplify configuration for global connectivity over public
network paths, you should use anycast networks, such as AWS Global Accelerator, which helps clients connect to the closest
available endpoint.

You can use AWS Direct Connect and Direct Connect Gateway to
connect your network to an AWS Region and bypass public network
paths between content source and cloud infrastructure. With
Direct Connect, you establish a dedicated connection between a
provider network and one of the Direct Connect locations.
Established connections from a Direct Connect location to any
other AWS Region around the world communicate over the AWS
managed backbone—improving performance for geo-diverse media
workloads while limiting the routers, networks, and parties
involved in the physical transmission layer.

AWS PrivateLink is recommended to establish connectivity when
working with partners that also use AWS. With AWS PrivateLink, a
service provider can expose their service endpoint to you within
Region, avoiding communication over the public networks. When a
service provider provisions a PrivateLink endpoint in the
consumer’s VPC, traffic can never initiate from that endpoint,
and only receive requests from the consumer’s resources. Traffic
flowing through the AWS PrivateLink VPC endpoint will adhere to
routing rules and network access control lists placed on that
subnet in which the endpoint resides.

When working with large content libraries, it’s possible that
transmitting content over the network is not feasible. This is
especially important to consider if the connectivity between the
studio and the video processing infrastructure is non-existent
or if the bandwidth requirement to transmit the footage is
beyond the available bandwidth the network provider can provide.
AWS offers **AWS Snowball Edge Edge**,
a petabyte-scale data transport solution that uses secure
appliances to transfer large amounts of data into and out of the
AWS Cloud. AWS Snowball Edge Edge encrypts all data with 256-bit
encryption. You manage your encryption keys by using the
**AWS Key Management Service**
(AWS KMS). Your keys are never stored on the device and all
memory is erased when it is disconnected and returned to AWS. A
user must have access to the customer managed key (AWS KMS key)
that is associated with the Snowball Edge Edge device when it was
requested to access the data stored in the Snowball Edge Edge device,
which reduces concerns of data being intercepted in transit.
Snowball Edge Edge devices come with an electronic screen that
displays the customer and AWS shipping destination, which
minimizes shipping discrepancies. Lastly, after your data has
been transferred to AWS, your data is erased from the device
using standards defined by National Institute of Standards and
Technology.

SM_SEC5: How do you protect content origin from unauthorized access and
malicious attacks?

**SM_SBP8 – Use DDoS protection service to maintain content
availability**

**SM_SBP9 – Restrict content origin access to only allow
known entities**

**SM_SBP10 – Use a web application firewall to monitor and
control content access**

**SM_SBP11 – Encrypt origin to client communication in
transit using TLS**

Protect your content origin layer from distributed denial of
service (DDoS) attacks at both the network level (Layer 3) and
application level (Layer 7), in addition to preventing
unauthorized origin access. Protecting your content origin from
unauthorized access or malicious attacks can help prevent
improper re-distribution of private content and increase service
reliability.

A DDoS attack is when multiple systems intentionally flood your
resources, which can render your content origin unavailable or
hidden to your viewers. It is important to use a DDoS protection
tool, such as AWS Shield, to protect your resources. AWS Shield
protects AWS resources such as **Amazon CloudFront** distributions and
**Amazon Route 53** so that your
content can be located and reached globally.
**AWS Shield Advanced** protects
resources built upon services such as
**Elastic Load Balancing, Amazon EC2**, and **AWS Global Accelerator** against common and most frequently
occurring infrastructure (layer 3 and 4) attacks like SYN/UDP
floods, reflection attacks, and others to support high
availability of your applications on AWS. If you need to protect
resources that you are hosting privately, put a CDN, such as a
CloudFront distribution, in front of it.

To reduce the likelihood of impact on your content origin from a
volumetric attack such as a DDoS attack, limit the allowed
traffic sources to trusted client IP addresses, such as the IP
address ranges for your CDN.

When using **AWS Elemental MediaPackage** or a content origin built on
**Amazon EC2**, restrict requests
to originate only from known IP addresses of the CDN PoPs and,
if applicable, use security groups to restrict incoming
traffic. To isolate access to known
**Amazon CloudFront** IP
addresses, AWS provides
[a
JSON resource](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html) that includes those address ranges, which
is regularly updated.

If you are using AWS Application Load Balancers or Amazon CloudFront, you can also use **AWS WAF** (Web Application Firewall) to validate requests
originating from known IP addresses. **AWS WAF** lets you create rules to filter web traffic based
on conditions that include IP addresses, HTTP headers and body,
or custom URIs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/infrastructure-protection.html*

---

# Data protection

SM_SEC6: How do you protect content at-rest and in-transit to prevent
unauthorized distribution?

**SM_SBP12 – Collaborate with business and legal
stakeholders to align on content protection requirements**

**SM_SBP13 – Select a content protection scheme that meets
business objectives**

The Well-Architected Framework covers best practices for any
workload when protecting data in transit and at rest, but when
you serve copyrighted materials or high-value content, you
should also consider the technologies available to protect these
works from unlawful access, replication, and re-distribution. In
general, practices that protect valuable digital assets are
referred to as Content Protection or Digital Rights Management
(DRM). There are varying degrees of complexity and systems
involved in Content Protection, but these components are common
to most implementations:

- **Key Provider** — Manages
customer master keys and content keys.
- **Encryptor** — Encrypts
media. This is often an encoder or an origin responsible for
packaging.
- **Authentication Service** —
Manages subscriber access and generates temporary access
tokens requests to content and keys.
- **Client** — Authenticates
viewer, retrieves content from an origin, keys from a key
provider, decrypts, and renders media.

In practice, there are two common content protection schemes —
Clear Key Content Encryption and DRM systems. Both systems use
AES-128 to encrypt the content, but differ in how keys are
managed and delivered.  If you’ve licensed content from a third
party, you might be commercially obligated to implement a DRM
system. This is true of most film and television content. Always
implement the solution that is in alignment with your business
and legal requirements.

**Clear key content encryption and
tokenized access**

A clear key implementation is common for applications that don’t
require *Hollywood-grade* DRM systems, but
want a pragmatic content protection scheme that makes it
difficult for outright theft or improper sharing of content by
paying users. By encrypting content with AES-128 encryption, we
can control who can decrypt the content through key access
policies. When combined with techniques like OAID and tokenized,
temporary, access URLs, you can control who can retrieve the
decryption keys and for how long the content endpoint will
service requests for encrypted content. This method is called
*clear key* because the content key is
eventually *in the clear* within the
user-space of the client and could theoretically be accessed by
an unauthorized user. Though, with tokenized content endpoints,
having the key does not necessarily mean that an unauthorized
user would have access to retrieve and decrypt the content.

On AWS, clear key encryption can be accomplished by generating
an AWS KMS key and then using the API to create data keys that
can be used by an encryptor (typically an encoder or packager)
to apply encryption to the content. These data keys are then
stored in a scalable persistence layer like
**Amazon S3** or
**Amazon DynamoDB.** Data key
access can be granted to your audience through a combination of
**Amazon Cognito** and
**Amazon IAM** policies for user
authentication and authorization. Delivery of these keys should
always be over an encrypted transport with tokenization.

**DRM systems**

Organizations working in the media and entertainment industry or
with high-value content, might have strict content protection
objectives for content keys, content decryption, or both to be
run only within hardware modules or trusted execution
environments (TEEs) that exist outside of the user-space on the
client. These organizations might also have requirements to
facilitate key revocation, offline playback, single-use keys, or
multi-key encryption levels for the same asset. These complex
organizational objectives can be achieved through the
implementation of a DRM system, such as Apple FairPlay, Google
Widevine, or Microsoft PlayReady.

While DRM systems add an additional layer of key protection and
business control to your content protection, implementation of
DRM varies by playback device. Though the industry is making
strides to simplify DRM implementations, in practice, it’s
common to see multiple DRM systems implemented to achieve device
compatibility across playback devices—increasing cost and
complexity.

With the **AWS Media Services**,
DRM systems are integrated into media processing and origination
though the Secure Packager and Encoder Key Exchange or SPEKE.
SPEKE provides an open standard proxy interface for any key
provider to exchange key material and metadata. You can
implement your own key service or use one of many DRM system
providers that are part of the AWS Partner Network (APN).

*Secure Packager and Encoder Key Exchange (SPEKE)
architecture*

No number of content protection schemes can ever fully protect
content from being exploited by an attacker and, in fact,
complex schemes can even increase the risk of problems for your
paying viewers. Commit time to determine the appropriate content
protection schemes for your specific content balancing cost with
content value. Be sure to balance cost of additional resources
on software licensing or operational burden versus the business
value of the content being protected.

**Clear Key Content Encryption and
Tokenized Access**

**Digital Rights Management (DRM)
System**

(PRO) Supported by all browsers through EME and mobile
players

(CON) Support varies by device and browser, often
requiring multi-DRM approach and increased costs

(PRO) Encryption implementation can be done with
standards-based, open sources tools and most encoding
and packaging systems

(CON) Encryption implementation varies by DRM system
provider and may require A commercial agreement to
implement

(PRO) Simple backend implementation

(PRO) Decryption key is only transferred to a protected
space in device memory or in browser memory (EME) TEE

(CON) Decryption key is supplied to player *in
the clear* at some point in the playback

(PRO) Support application of complex business rules. For
example - offline playback, revocation, single-use
tokens, multi-key encryption to enforce separate
policies

*Comparison of clear key and DRM systems for content
protection*

**Player integrity**

Take proper measures to prevent discovery of the controls put in
place to prevent usage of a tampered player or unauthorized
access to your media assets and distribution system. When you
choose to create your own media player, you should determine
which platforms will help you check the integrity of your
software packages.

Many platforms, such as FireOS, Android, iOS, macOS, and
Microsoft Windows, provide the capability for developers to sign
their application packages as part of the process of uploading
them to the platform’s software or app store. The purpose of
signing application packages is to verify that the package has
not been tampered with or compromised between the time you
uploaded your application and when the package has been
installed on a client device. It’s important to note that
although signature checks provide clear assurances that your
player has not been tampered with since you signed it, it does
not prevent the tampering or reverse engineering of your
player.  Some platforms strictly forbid installation of software
packages outside the platform’s software store, minimizing the
risk of loading a compromised player.

The certificates that are used to sign your media player should
be protected with limited access, ideally only within an
automated build pipeline that’s out of reach of any human
operator, and should never be shared outside your organization.
Use a private certificate authority, such as AWS Certificate
Manager Private Certificate Authority (ACM Private CA), that
provides strict access control to authorized issuers that will
perform issuance of signing certificates.  The pipeline that
will build and sign your media player package should strictly
control the process such that only authorized code will be built
and signed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/data-protection.html*

---

# Incident response

Even with mature preventive and detective controls in place,
your organization should still put processes in place to respond
to and mitigate security incidents. Logging, event processing,
clean rooms, and game days are effective techniques to help you
protect your content within your workload, but many
organizations continue to protect content rights after delivery.
In media applications where you are designing system to carry
high value, copyrighted material, you should have a response
plan that also includes illegal re-distribution of your content
and intellectual property.

License holders and distributors often work with a third-party
forensic security firm to embed and trace watermarks to the
point of origin on a newsgroup, torrent, or piracy website. The
report furnished can often be used to take legal action, which
might include, but is not limited to, DMCA takedowns and
monetary fines.

It is against the
[AWS Acceptable
Use Policy](https://aws.amazon.com/aup/) for users to transmit, store, display,
distribute, or otherwise make available content that is illegal,
harmful, fraudulent, infringing, or offensive. If you suspect
that your content is being illegally distributed using AWS
services, your incident response plan should include steps to
contact AWS Support and
to [follow
our abuse reporting process](https://aws.amazon.com/contact-us/report-abuse/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/incident-response.html*

---

# Resources

Refer to the following resources to learn more about our best
practices for security.

## Documents

- [AWS MPAA
and Studio Compliance](https://aws.amazon.com/compliance/mpaa/)
- [AWS Well-Architected Framework Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
- [Secure
Content Delivery with Amazon CloudFront](https://docs.aws.amazon.com/whitepapers/latest/secure-content-delivery-amazon-cloudfront/secure-content-delivery-with-amazon-cloudfront.html)
- [Serving
Private Content Using Amazon CloudFront and AWS Lambda@Edge](https://aws.amazon.com/blogs/networking-and-content-delivery/serving-private-content-using-amazon-cloudfront-aws-lambdaedge/)
- [Protecting
your video stream with Amazon CloudFront and serverless
technologies](https://aws.amazon.com/blogs/media/part-1-protecting-your-video-stream-with-amazon-cloudfront-and-serverless-technologies/)
- [Using
Amazon CloudFront and AWS Media Services](https://aws.amazon.com/blogs/media/using-amazon-cloudfront-and-aws-media-services/)
- [Analyze
Your CloudFront Logs at Scale](https://aws.amazon.com/blogs/big-data/analyze-your-amazon-cloudfront-access-logs-at-scale/)
- [Secure
Packager and Encoder Key Exchange (SPEKE) Reference
Server](https://github.com/awslabs/speke-reference-server)

## Videos

- [Secure
Media Streaming and Delivery](https://www.youtube.com/watch?v=zzeho2uLpHM)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/resources-sec.html*

---
