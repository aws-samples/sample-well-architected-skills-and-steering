# GAMESEC04 — Access control

**Pillar**: Security  
**Best Practices**: 4

---

# GAMESEC04-BP01 Restrict access of downloadable content to authorized clients and users

Restrict access to game content by authorized applications and
clients. Consider using Amazon S3 as a cost-effective and scalable
origin for storing downloadable game content and Amazon CloudFront
to provide globally performant content delivery to players. Both
services provide built-in mechanisms for restricting access to
data that is stored, such as restricting access to authenticated
users.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Granting access to content that is stored
in Amazon S3**

When you need to grant access to content that is stored in S3,
there are several factors to consider. By default, only the AWS account that created an S3 bucket can access the objects stored
within it. To grant access to your internal applications and to
manage content stored in Amazon S3 buckets,
use [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) to create policies
that provide appropriate access.

[IAM
roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) can be associated with federated users, systems, or
applications hosted in services, such as Amazon EC2, AWS Lambda,
and container-based applications hosted in Amazon EKS and Amazon ECS. For example, you might use the AWS SDK or AWS CLI to publish
and manage game content assets in S3 buckets. To support this use
case, you can create an IAM role with appropriate access to read
and write game content to your S3 buckets and associate it with
the EC2 instances that host your software and scripts.

Resource-based policies can be defined for your bucket and for
specific objects.
[S3 bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)
are associated with an S3 bucket and can be used to restrict
access to the bucket and objects within it, as well as grant
access to your Amazon S3 resources from other accounts. For
example, in scenarios where multiple teams or separate game
development studios are working on the same game content
and require the same access to centrally hosted content in Amazon S3, you can use an S3 bucket policy to define permissions for
cross-account access to the S3 resources. Consider
using [S3
access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html), which can simplify managing data access to
shared data by creating access points with names and permissions
specific to each application or sets of applications. The Amazon S3
documentation contains
additional [best
practices for access control in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-best-practices.html#access-control-best-practices-store-share).

```
`**Granting short-term access to your content**`
```

When access is only need for a specific limited time, generate
temporary URLs that grant short term access to your content.
Amazon S3 provides support for
generating [presigned
URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html), which allow object owners to grant time-limited
access to objects in Amazon S3 without updating your bucket
policy. By doing so, the end user or application that is being
granted access is not required to have an account or IAM
permissions and instead uses the presigned URL to access the
content.

This is a best practice that is commonly used in a variety of
games use cases, such as granting authorized players access to
downloadable content that they have been entitled to and providing
temporary access to limited time game content. Presigned URLs can
also be used to provide temporary permissions for uploading
content to an S3 bucket. For example, you might consider using a
presigned URL to provide a player with access to upload client
logs for assisting your support team with troubleshooting a player
support case.

**Using a content delivery network to
provide access to your content**

While your applications, game developers, artists, and other
personnel may need direct access to the content in S3 buckets for
development and management purposes, use a content delivery
network to provide access to content that is publicly available to
players or other users over the internet. This approach improves
download performance and reduces costs by caching frequently
accessed content. Amazon CloudFront can globally distribute your
content by caching and delivering it closer to your players while
reducing the load on your game's download origin, such as Amazon S3.

Rather than serving your public content directly from S3 buckets,
it is recommended to keep this content private and serve it
publicly by using CloudFront. CloudFront can be configured to
require players to access your private content (such as a new game
download for paid players only) by using
either [signed
URLs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html) or
[signed
cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.html). You can then develop your application either to
create and distribute signed URLs to authenticated users, or to
send set-cookie headers that set signed cookies for authenticated
users. When you create signed URLs or signed cookies to control
access to your files, you can specify an ending date and time,
after which the URL and cookies are no longer valid.

Optionally, you can also specify the IP address or range of
addresses of the computers that can be used to access your
content, which is useful if you want to restrict access to specific
game development studio partners or contractor networks. Use
signed cookies when you want to provide access to multiple
restricted files, or if you don't want to change your current
URLs. Use signed URLs when you want to restrict access to
individual files or if your users are using a client that doesn't
support cookies. Signed URLs take precedence over signed cookies.

### Implementation steps

- Use IAM roles and bucket policies to grant appropriate
access to S3 buckets for internal applications, teams, or
cross-account scenarios.
- Generate presigned URLs for granting short-term access to S3
objects, suitable for downloadable content or temporary
uploads like client logs.
- Use Amazon CloudFront with signed URLs or cookies to more
securely serve private content to authenticated users

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec04-bp01.html*

---

# GAMESEC04-BP02 Limit origin access to authorized content delivery networks (CDNs)

Block users from circumventing your content delivery
networks to directly access content from your origin, such as your
Amazon S3 buckets. It is important to restrict access to your
origin to only your authorized CDNs, which reduces data transfer
costs from unnecessarily serving content out of the origin. It
also improves your security posture by flowing public access to
your origin content through the same entry point, where you can
deploy edge security controls such as AWS WAF layer 7 filtering,
injection and inspection of security-related HTTP request
parameters, and distributed denial of service (DDoS) protections.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To implement these controls for an Amazon S3 origin, you can use
an [Amazon CloudFront origin access identity (OAI)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), which verifies
that requests to your S3 objects are originating from your
CloudFront distribution. Associate AWS WAF with your CloudFront
distribution to provide layer-7 filtering. However, if you are
serving content from additional CDNs, you can configure the CDN to
insert one or more custom HTTP headers into origin requests which
can be inspected by AWS WAF to verify that the incoming traffic
originated from your authorized CDN provider.

This approach is also useful for helping prevent users from
circumventing your CDN providers when your origin is hosted behind
an [Application Load Balancer (ALB)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html). ALBs can be associated with AWS WAF
for layer-7 protections. You can configure AWS WAF to insert a
custom HTTP header that will be inspected by your ALB to process
and inspect incoming traffic to the load balancer by AWS WAF.

**Customer example**

AnyCompany Games implements origin access restrictions to help
protect their game assets, downloadable content, and patch files
from unauthorized direct access that could enable players to
bypass security checks or obtain premium content without proper
authentication. This approach allows them to monitor content
access patterns through a centralized point, making it
straightforward for them to identify suspicious download behaviors
that might indicate the presence of coordinated attacks or
unauthorized content redistribution.

### Implementation steps

- Use Amazon CloudFront origin access identity (OAI) to
restrict direct access to S3 objects
- Associate AWS WAF with CloudFront or ALB to provide layer-7
filtering and help protect against DDoS attacks and
malicious requests.
- Configure custom HTTP headers in Cloudfront to verify that
incoming traffic originates from authorized sources.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec04-bp02.html*

---

# GAMESEC04-BP03 Implement geographic restrictions to limit unauthorized access

When a player requests your content, Amazon CloudFront serves the
requested content from the nearest edge location, regardless of
where the player is located. However, there may be scenarios in
which you need to restrict how your content is accessible by users
in specific parts of the world. For example, you may have a rolling
game deployment strategy that releases content in phases on a
country-by-country basis, or you may have to abide by
country-specific access controls.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

You can use
[geographic
restrictions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html), also known as geo blocking, to block players
in specific geographic locations from accessing content that you're
distributing through a CloudFront distribution. This feature lets
you restrict access to files that are associated with a
distribution and restrict access at the country level.
Alternatively, you can use a third-party geo-location service to
restrict access to a subset of the files that are associated with a
distribution or to restrict access at a finer granularity than the
country level.

By using CloudFront geographic restrictions, you can allow your
players to only access your content if they're in one of the
countries that are on an allow list of approved countries. You can
also block your players from accessing your content if they're in
one of the countries that are on a deny list of banned countries.
If a request is received from a blocked geographic location,
CloudFront will return a 403 Forbidden HTTP status code to the
player. It is important to note that this works well for
non-sensitive content and should not be used as stand-alone
protection for PII or sensitive game artifacts.

### Implementation steps

- Use CloudFront geographic restrictions to allow or deny
content access based on country-level allow or deny lists.
- Return a 403 Forbidden HTTP status code for requests
originating from blocked geographic locations.
- Avoid relying solely on geo restrictions for protecting
sensitive content or PII

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec04-bp03.html*

---

# GAMESEC04-BP04 Restrict access to content with digital rights management (DRM) solutions

Consider restricting access to your game content by using strong
encryption tools such as a
[digital
rights management (DRM)](https://aws.amazon.com/marketplace/solutions/media-entertainment/drm/) solution. This type of solution can
be used to encrypt your private content and distribute the
decryption keys to authorized players.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

DRM solutions are recommended in situations where you want to
allow players to download game content early, but you do not want
them to be able to access or play the content until a
predetermined time. For example, this is common in situations
where players are allowed to pre-order a game and configure their
game client to automatically begin downloading the encrypted files
early. This strategy verifies that the game is downloaded and
ready to be played once the game has been officially
released. After the game is released, the player's game client can
request decryption keys from the DRM backend solution so that it
can decrypt the previously downloaded files and begin playing the
game.

DRM systems are also used to block unauthorized re-distribution
and manipulation of games after they have been downloaded and
installed by an authorized player. DRM systems require integration
with the origin for exchanging encryption keys and authorizing
players to retrieve the decryption key. Commercial DRM providers
offer a range of solutions with features and support for different
devices.

### Implementation steps

- Use DRM solutions to encrypt private game content and
distribute decryption keys to authorized players.
- Enable pre-download of encrypted files for pre-ordered
games, unlocking access with decryption keys at release
time.
- Integrate DRM systems with the origin to manage encryption
keys and block unauthorized redistribution or manipulation
of content.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec04-bp04.html*

---
