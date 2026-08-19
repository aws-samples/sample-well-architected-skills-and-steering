# Security

**Pillar**: Security  
**Questions**: 10

---

# GAMESEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 5

---

# GAMESEC01-BP01 Use roles and federated access, rather than the account root user, to perform actions on your AWS environment

When you first create an AWS account, you begin with an identity
known as the root user, which is accessed using the email address
and password associated with the account. The root user has
complete access to AWS services and resources within that account.
In most cases, you should avoid using the root user for day-to-day
tasks. When root-level access is required, confirm that it's
absolutely necessary and verify that additional logging and
guardrails are in place to track its use.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

In an AWS Organizations configuration, each account still has its
own root user, but day-to-day access should instead be managed
through IAM roles and IAM Identity Center users. Create role-based
access tailored to your game's lifecycle stages and teams. For
example, the live operations team might need permissions to manage
in-game events, while developers need access to push updates. When
working with third-party services or partners, use federated
access to enable secure collaboration without exposing sensitive
infrastructure. This approach verifies that each user or partner
has only the access they need while maintaining the security of
your game's infrastructure and player data.

**Customer example**

AnyCompany Games implemented role-based access control when
developing their new game. By using specific IAM roles for their
diverse development teams, they avoid using shared credentials.
This setup allows a dev team to assume a role for core game
systems, while the content team's role is only able to access
asset management services.

### Implementation steps

- Do not use the root user after setting up an account unless
absolutely necessary. Create the account, secure the root
user, and immediately create the required administration IAM
roles and assign that role to federated user.
- Only use the root user when you need to perform
[a
limited number of tasks that are only available to the root
user](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html). Examples of these tasks include changing your
root user email address and changing your AWS support plan.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp01-use-roles-and-federated-access-rather-than-the-account-root-user-to-perform-actions-on-your-aws-environment.html*

---

# GAMESEC01-BP02 Use AWS Control Tower to quickly set up a multi-account environment on AWS

If you start using AWS with just a single account, you might find
your game studio growing out of it as your game development
process advances. For example, with a single AWS account, you
might begin to reach service limits, or your costs for different
projects and workloads may become more complex. Creating different
accounts for different game titles and environments allows teams
to experiment with new features, bypass service limits, and
maintain security posture and compliance. By implementing a
multi-account strategy in AWS, you can benefit from distributing
service limits across multiple accounts and gain insights into
your AWS costs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

It is a common misconception that using multiple AWS accounts will
automatically be more confusing and time consuming. Rather, using
AWS services that are designed to facilitate the governance of
multiple accounts can assist your game studio to spend less time
managing your accounts.

You can use AWS Control Tower is a service to securely provision a
multi-account AWS environment. Control Tower is recommended if you
are building a new AWS environment, starting your journey on AWS,
or are completely new to AWS. During the short setup process , you
can integrate with other AWS services that are involved with
managing accounts and user access, such as AWS Organizations, Service Catalog, and AWS IAM Identity Center.

**Customer example**

AnyCompany Games initially operated from a single AWS account, and
they hit multiple roadblocks when one of their games' development
team reached EC2 service limits during a crucial beta test. At the
same time, their development team for a different game struggled
with resource allocation for their automated testing pipeline. The
situation reached a breaking point when AnyCompany Games couldn't
accurately separate costs between projects, making it difficult to
budget for each game's development.

AnyCompany Games then implemented a multi-account strategy using
AWS Control Tower. They created separate accounts for each game
project, with distinct development, QA, and production
environments. This account level separation isolates each projects
data and assets, so teams working on one game can't access or
modify resources from another. Through AWS Organizations, they
established a centralized billing structure that clearly showed
each game's infrastructure costs and also created
organization-wide access polices.

### Implementation steps

- Use AWS Control tower to set up an automated multi-account
environment.
- Organize accounts based on environments (like development,
QA, and production).
- Use AWS IAM Identity Center and Service Catalog to
centralize user permissions and streamline resource
provisioning across accounts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp02-use-aws-control-tower-to-quickly-set-up-a-multi-account-environment-on-aws.html*

---

# GAMESEC01-BP03 Use least privilege role policies that are tailored to specific job functions

Configuring IAM policies is an essential part of establishing a strong security
foundation. When you set permissions with IAM policies, grant only the permissions required
to perform a task. You do this by defining the actions that can be taken on specific resources
under specific conditions, also known as least-privilege permissions. For example, QA teams
need access to change things in the testing environments but should not have the ability to
modify the production environment.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

You might start with broad permissions, like [managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html),
while you explore the permissions that are required for your workload or use case. As your use
case matures, you can work to reduce the permissions that you grant to work toward least
privilege.

### Implementation steps

- Follow the practice of least privilege permissions for create IAM roles for users
and applications.
- Use AWS-managed policies to quickly provide broad access while identifying the
specific permissions teams or applications need to perform their tasks.
- Studios can also use [IAM
access analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_reduce-permissions-edit-policy.html) to generate custom IAM policies based on
CloudTrail events that identify actions and services used by an IAM entry.
- Regularly review IAM policies and edit overly permissive policies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp03-use-least-privilege-role-policies-that-are-tailored-to-specific-job-functions.html*

---

# GAMESEC01-BP04 Use roles and federated access policies together with account level access policies to grant access to your AWS resources

New AWS users often use IAM policies only when granting access to
others. However, if you are using AWS Organizations, consider how
to use service control policies together with IAM policies to
grant your studio team members and contractors the necessary
levels of access.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

You can create IAM policies to allow or deny access to AWS
services or API actions that work with AWS Identity and Access Management. They can only be applied to IAM identities, such as
users, groups, or roles. For example, an IAM policy might be used
to provide a user read-only access to Amazon S3.

Service control policies (SCPs) are guardrails for your AWS accounts. An SCP doesn't grant permissions, they are used to
restrict actions on AWS services for individual member accounts.
For example, an SCP can deny an AWS account from accessing a
particular Region.

When an action is taken, the relevant IAM policy is evaluated in
combination with the SCPs. Following up on the previous example,
is a role is attempts to run an EC2 instance, IAM indicates is
they are permitted ("Allow" for ec2:RunInstances) and
the SCPs will determine if their choice of Region is valid
("us-east-1" is permitted, but "us-west-1" is
denied by the SCP).

Layering IAM policies and SCPs can verify that anyone who accesses
your AWS resources will only be given the appropriate permissions
that they need. This is especially important to consider if your
AWS accounts and resources span multiple Regions, but not everyone
within your game studio needs to access all of them.

You can tailor IAM policies to grant specific teams specific
permissions for updating things like game configurations, managing
player data, configuring promotional events, and moderating
user-generated content. Meanwhile, you can use SCPs to enforce
organization-wide controls crucial for game operations. These
might include restricting deployment to only approved Regions
where the game operates, helping prevent unauthorized access to
sensitive player data stores, enforcing compliance requirements,
and controlling costs by limiting service usage across development
accounts.

### Implementation steps

- Use IAM policies to manage permissions for individual users,
groups, or roles.
- Use service control policies (SCPs) in AWS Organizations to
enforce account-level permissions.
- Combine IAM policies and SCPs to grant only the required
access for specific users and accounts.

### Resources

- [Policies
and permissions in AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Service
control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp04.html*

---

# GAMESEC01-BP05 Use a central identity provider

A central identity provider acts as a single source for storing and
managing user credentials, identities, permissions, and
authentication.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use a central identity provider to streamline your user
authentication process, enforce consistent security polices, and
simplify your user management across your AWS accounts and
applications. Having a centralized approach removes the need to
manage user identities and credentials separately, which reduces
the risk of inconsistencies, redundancies, and other security
vulnerabilities. Consolidating user identities and authentication
into one place also allows for better visibility, control, and
auditability for your entire AWS environment.

**Customer example**

AnyCompany Games faced significant challenges with managing
developer access across their rapidly expanding AWS
infrastructure. Their development team grew from 50 to 200 people
across three major titles. Initially, each project team managed
their own AWS access credentials, resulting in inconsistent
security practices, delayed onboarding for new developers, and
occasional security incidents.

The studio implemented AWS IAM Identity Center as their central
identity provider, consolidating user management into a single
system. They connected it with their existing corporate directory,
enabling developers to use their same company credentials for AWS
access. Now developers use their single, existing company login to
gain the AWS access they require to complete their work

### Implementation steps

- Consider using AWS IAM Identity Center as your central
identity provider. This provides consistent access
management across your AWS accounts, provides your employees
with single sign-on authentication, and simplifies user
access auditing to your AWS applications. IAM Identity Center also connects with existing corporate identities from
supported identity providers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp05.html*

---

# GAMESEC02 — Ongoing security

**Pillar**: Security  
**Best Practices**: 1

---

# GAMESEC02-BP01 Use ready to deploy templates for standard security practices

Ready-to-deploy templates provide a proactive and agile way to assess your security posture
in the cloud. Pre-configured templates evaluate your cloud security and implement necessary
changes promptly. The templates encompass a wide range of best practices across various
technologies and widely accepted security frameworks. Using templates can assist game studios to
maintain consistent infrastructure configurations, especially as they may scale and add
additional AWS accounts to support new workloads.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

By using AWS services and implementing ready-to-deploy templates, game developers can
proactively assess and strengthen their cloud security posture, safeguarding their
intellectual property, protecting player data, and fostering a secure gaming landscape through
regular security assessments and continuous monitoring to promptly identify and address
potential vulnerabilities.

**Customer example**

AnyCompany Games faced a significant challenge when preparing to launch their next title
in the European industry. They realized that their existing data handling practices didn't
meet GDPR requirements. They turned to AWS Security Hub CSPM and AWS Config and its ready-to-deploy
templates for a solution. The team implemented the GDPR-specific conformance pack in AWS Config,
which automatically assessed their existing infrastructure against GDPR standards. This
initial scan revealed several critical gaps, such as improper data retention policies and
inadequate access controls on where player data was stored. Using the template's predefined
rules, AnyCompany Games rapidly implemented the necessary changes. Moreover, the ongoing
automated compliance checks provided by the template allowed the small team to maintain GDPR
compliance effortlessly, even as they continued to update and expand the game.

### Implementation steps

- Use templates for standard security practices, such as managed rules and
conformance packs in AWS Config and standards in AWS Security Hub CSPM.
- Review the details of the [Security Hub CSPM standards](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html) to
determine which ones align most with the security needs of your game studio.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec02-bp01.html*

---

# GAMESEC03 — Identity and access management

**Pillar**: Security  
**Best Practices**: 5

---

# GAMESEC03-BP01 Determine your approach to identify and control player access to your game's environment and resources

This decision is influenced by your player acquisition and
monetization strategy, player experience, and other factors such
as the existing capabilities that might be provided by your game
publishing partners. For example, a game might require purchases
and require a player to create a user profile to associate
real-money payment methods with their account.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Alternatively, a game may desire to reduce the barrier to entry
for first-time player experiences by removing the need to create a
user account before playing the game, thereby improving the chance
that a player will try the game for the first time. Typically,
games will implement one or more combinations of player identity
and access management approaches for their game.

**Unauthenticated or anonymous
access**

This access level is useful in situations where a game does not
require a player to create a new user account or link with their
identity on social networks and gaming systems. This is the
simplest and quickest way for a player to start playing a game and
is particularly useful in mobile games where a game developer may
want to reduce the barrier to entry for the initial experience.

In this access scenario, if you want to identify usage from the
game installation, you can program the game client to generate and
store a unique identifier onto the player's device. This unique
identifier is used to identify the player across game sessions on
their device and allow analytics reporting on usage over
time. Later, if a player chooses to create an account, you can
associate their new user account with their previously-generated
unique identifier. This will link their new player identity to
their historical usage, which might include stats and game
achievements.

If a player does not eventually create and link an account, the
device that the player uses to interact with the game can be
uniquely identified, but recoverable information about the player
is not collected and stored. Thus, if the player breaks or loses
their device, the previous stored data associated with the device
is also lost and might not be recoverable.

**Authentication with username and
password**

A game may allow players to create their own user accounts with a
username and password that are stored within the game's
backend. This might occur when a game developer is collaborating
with a game publisher who already has an existing player account
system that the developer can integrate with. Alternatively, a
developer who publishes their own games might want to simplify the
player experience by allowing players to create a single user
account for access across the games that they publish.

**Authentication and account linking with
third-party social networks and gaming systems**

It is common for online games and games with social features to
provide third-party identity provider federation to simplify the
player experience. Instead of asking players to create a username
and password combination to authenticate, you can use identity
federation to allow players to authenticate using their
third-party accounts with social networks and gaming systems. This
login process simplifies the sign-in and registration experience
for players. It also provides a convenient alternative to
mandatory account creation and a frictionless method for players
to access games.

For game developers, a federated login process can offer a
streamlined player verification workflow. It may also provide a
more reliable way to manage player data that is used for
personalization. This is because you do not need to ask players to
provide you with certain data that they likely have already
provided to the third-party identity provider. Additionally, these
systems provide integration with additional social features such
as the ability to link players with their friends.

### Implementation steps

- Use unauthenticated or anonymous access to reduce barriers
for first-time players by generating a unique device
identifier to track usage and enabling account linking
later.
- Implement username and password authentication for dedicated
user accounts, using existing player account systems or
creating a unified experience across games.
- Integrate third-party identity providers for federated
authentication, simplifying login processes and enabling
access to social features and personalization data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec03-bp01.html*

---

# GAMESEC03-BP02 Authenticate requests that are sent to your game backend service

Authenticating requests that are sent to your game backend service
can block unwanted requests from succeeding.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

You should provide an authentication service for players to log
in, which should return secure short-lived tokens, such as a JSON
Web Token (JWT), to the game client when a player successfully
authenticates.

These tokens can include claim assertions that contain player
attributes and other relevant metadata. This relevant metadata can
be used in subsequent requests that are sent from the game client
to your game backend to authenticate requests and authorize them
in the context of the authenticated player.

You have the option to either design and build your own player
authentication system, which would require ongoing improvement and
maintenance, or you can use the scalable and secure user sign-up,
sign-in, and access control features provided
by [Amazon Cognito](https://aws.amazon.com/cognito/).

Amazon Cognito user pools include a user directory for
authentication and authorization. A user pool provides APIs that
you can integrate into your game for sign-up, sign-in, and
password reset workflows, which can be integrated with third-party
identity
providers. [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html)
and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) both provide integrations with Cognito to
integrate user authentication for requests sent to your custom
game backends hosted with these services.

If your game supports anonymous access and you cannot authenticate
a player, you can use a client authentication approach to provide
a more secure experience when integrating with your game backend.
If your game client uses AWS services directly, requests to these
services must be signed using credentials. To provide credentials
to your game client for unauthenticated users, you can use the AWS
SDK to retrieve short-lived credentials
from [Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) that can be used to sign your
requests to AWS services. These credentials can be refreshed from
your game client.

In addition to directly integrating with the AWS SDK from the game
client, you can also build your own game backend, using a service
such as
[Amazon API Gateway](https://aws.amazon.com/api-gateway/), which supports custom authorization. By designing
your own game backend service, you can gain authoritative control
over requests with custom server-side logic.

For more information on building a backend service for games
hosted using Amazon GameLift, see
[Design
your game client service](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend.html).

**Customer example**

AnyCompany Games enhanced the security of their next title by
adopting a managed authentication and authorization approach.
Instead of maintaining a custom username and password system, they
used Amazon Cognito user pools to handle player sign-up and
sign-in, and identity pools to support anonymous access for
players trying the training mode before creating an account. They
also implemented custom authorization logic within the game to
recognize administrator roles defined in Cognito, granting those
users access to special in-game management features.

### Implementation steps

- Use Amazon Cognito user pools to manage authentication with
secure tokens like JWTs, enabling features like sign-up,
sign-in, and password resets.
- Retrieve short-lived credentials from Amazon Cognito
identity pools for anonymous users to securely interact with
AWS services.
- Implement custom game backends using Amazon API Gateway for
custom server-side authentication logic.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec03-bp02.html*

---

# GAMESEC03-BP03 Use your game backend service to validate player requests to join a multiplayer game

Typically, in multiplayer games, a player will join a game session
by selecting an option directly from a list of available sessions,
or they will submit a request to find a match. The latter approach
places the responsibility on the game developer to locate an
eligible game session and provide the connection information
(usually an IP address and port number) back to the player's game
client. The implementation may vary depending on the genre of game
you are developing, but regardless, it is a security best practice
to perform server-side validation of a player's request to join a
game.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

For example, in a session-based multiplayer game, a request from a
player to join a game session should be validated by your game
server software with your game backend matchmaking service before
authorizing their connection to the server. When a player requests
to join a game session, the game server should check the request
for a unique identifier, such as a player session ID and
server-generated ticket that was previously provided to the game
client by your game backend matchmaking service.

Upon initiating the connection to the game server, your
server-side software can use this information to verify with the
matchmaking service that the player's connection request is valid
and verify that the player is not joining a spot that was
previously reserved in the game session for another player.

For games that are hosted on Amazon GameLift, see
[Game
client/server interactions with Amazon GameLift Servers](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-interactions.html) for
an example of how this type of server-side validation can be
implemented.

**Customer example**

During AnyCompany Games' initial beta launch, they discovered that
players were bypassing their matchmaking system by directly
connecting to game servers, leading to serious competitive
integrity issues. When highly-ranked players found that they could
share server IP addresses with friends, they began circumventing
the skill-based matchmaking system, resulting in experienced
players joining novice matches and creating a frustrating
experience for new players. AnyCompany Games responded by
implementing a server-side validation system that generated unique
session tickets for each matchmaking request. The system required
both the player IDs and matchmaking request tickets and verified
connection attempts against their backend matchmaking service.

### Implementation steps

- Validate player join requests server-side using unique
identifiers like player session IDs and server-generated
tickets.
- Confirm the validity of connection requests with the
matchmaking service to block unauthorized access.
- Verify that reserved spots in game sessions are not accessed
by unauthorized players during the validation process.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec03-bp03.html*

---

# GAMESEC03-BP04 Enforce a strict security policy for player user accounts by requiring a strong password

If a game provides players with the ability to create a user
account with a password, you should require players' passwords to
adhere to strong policies. For example, Amazon Cognito user pools
provide you with the ability
to [define password
requirements](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html) for user accounts. Establishing a strong
password policy can protect your players' accounts from being
overtaken through social engineering and brute force attacks.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Customer example**

AnyCompany Games faced a crisis when their popular title
experienced a wave of account hijackings due to weak password
policies. Players who were using simple passwords like
"password123" were becoming victims of automated brute
force attacks, resulting in lost items and compromised in-game
currency. To combat this, AnyCompany Games revamped their login
system and mandated that passwords not be previously used, include
at least one uppercase letter, one number, one special character,
and a minimum length of 15 characters.

### Implementation steps

- Require strong password policies for player accounts to
enhance security.
- Use Amazon Cognito user pools to define and enforce password
requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec03-bp04.html*

---

# GAMESEC03-BP05 Provide an option for players to set up multi-factor authentication (MFA) on their accounts

Player accounts can be an asset to bad actors, particularly in
games that support in-game currency and purchases. Due to the
pervasiveness of player account hacking and social engineering
attacks, provide players with the option to enhance the security
of their accounts by configuring multi-factor authentication
(MFA).

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When a player attempts to access their account by using MFA, a
temporary code is sent to their email address, phone number, or a
purpose-built multi-factor authentication mobile app. To
successfully authenticate, the player must then enter the code
into the login system within a limited time frame.

MFA can also be used to help protect accounts that are attempting
to authenticate from a new geo-location, accounts that have been
flagged by player support for potential malicious activity, and
even for accounts that have not logged into the game for an
extended period.

For example, Amazon Cognito user pools can
[configure multi-factor
authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) on user directories.

### Implementation steps

- Enable multi-factor authentication (MFA) to enhance player
account security.
- Use temporary codes sent via email, phone, or MFA apps to
verify account access.
- Apply MFA for new geo-locations, flagged accounts, or
accounts with extended inactivity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamsec03-bp05.html*

---

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

# GAMESEC05 — Detection

**Pillar**: Security  
**Best Practices**: 2

---

# GAMESEC05-BP01 Implement a comprehensive data collection strategy to monitor player behavior

To maintain a positive player experience, implement a
comprehensive data collection and analysis strategy. Capturing,
storing, and analyzing relevant data provides insights into how
players interact with your game's features and with each other.
This data-driven approach can guide decision-making, enhance
player engagement and retention, optimize monetization strategies,
and ultimately improve the overall player experience.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement data collection systems to capture and log relevant
player actions, such as gameplay sessions, progress, achievements,
purchases, interactions with game elements, and social activities.
Collect server-side data like server load, network traffic, and
error logs to monitor the technical performance and identify
potential issues. Gather player feedback through surveys, forums,
support tickets, and social media channels to understand their
experiences and preferences.

When storing your game data, establish a centralized data
warehouse or data lake to store and organize the collected data
and implement pipelines for data cleaning, transformation, and
aggregation to prepare the data for efficient analysis.

After storing the data, analyze it to gain insights such as player
retention and churn, monetization strategies, and feature usage
through data visualization tools.

### Implementation steps

- Capture and log player actions, server-side metrics, and
feedback to monitor interactions and technical performance.
- Use a centralized data warehouse like Amazon Redshift or S3
data lake to store, clean, transform, and organize game data
for analysis.
- Analyze collected data with visualization tools, like Amazon Quicksight, to gain insights into player retention,
monetization, and feature usage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec05-bp01.html*

---

# GAMESEC05-BP02 Collect, store, and analyze player usage logs to detect inappropriate behavior

Instrument your game to collect logs to understand how players use
the features of your game and how they interact with other players.
You can then block unauthorized activities that can degrade the
player experience.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Send structured log events to
the [Game
Analytics Pipeline](https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/), by using a logging solution such as
[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) or
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), or through a solution from an AWS
Partner such
as [Datadog](https://www.datadoghq.com/),
[Sumo Logic](https://www.sumologic.com/),
[New Relic](https://newrelic.com/),
[Honeycomb.io](https://www.honeycomb.io/),
or [Splunk](https://www.splunk.com/).
Structure these player usage logs so that they can be used to
detect when specific actions by players need to be investigated.

After you have captured the data, consider implementing tools to
detect inappropriate usage behavior. For example, if your game has
social features such as in-game player messaging, voice chat, or
online forums, save logs from these player engagements in a format
that can be analyzed for moderation purposes.

Configure your game's voice chat feature to export recordings to
Amazon S3 and
use [Amazon Transcribe](https://aws.amazon.com/transcribe) to convert the audio speech to text format which
can be stored for processing. Alternatively, you can perform
real-time streaming transcription by integrating your game backend
voice chat service directly with the Transcribe API
to [transcribe
streaming audio](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html) in real time. Moderation teams can manually
review the content, and once the content is in a standard format,
you can also use AWS AI/ML services to perform moderation
automatically.
[Amazon Comprehend](https://aws.amazon.com/comprehend/) can be used to perform natural language
processing (NLP) to uncover information from the unstructured
text, which can classify and organize the conversations into
relevant topics and identify inappropriate behavior such as
profanity.

### Implementation steps

- Collect, store, and analyze player usage logs.
- Use AWS services for artificial intelligence and machine
learning to more efficiently review and gain insights into
your player usage logs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamsec05-bp02.html*

---

# GAMESEC06 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 3

---

# GAMESEC06-BP01 Use tools for detecting and responding to threats to your infrastructure

To continuously monitor for malicious activities and unauthorized
behaviors within your AWS environment, consider
using [Amazon GuardDuty](https://aws.amazon.com/guardduty/). GuardDuty identifies threats by monitoring
account behavior, network activity, and data access patterns
within your environment. It analyzes events across multiple data
sources, such as CloudTrail event logs, Amazon VPC Flow Logs, and
DNS logs for potential threats. By integrating with Amazon CloudWatch Events and Lambda, GuardDuty alerts can be
automatically forwarded to relevant security teams for further
analysis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) provides a comprehensive view of your security
state in AWS and check your environment against security industry
standards and best practices. Security Hub CSPM collects security data
from across AWS accounts, services, and supported third-party
partner products and analyzes your security trends and identify
the highest priority security issues.
The [Amazon GuardDuty](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html)
[integration
with Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html) enables you to send findings from
GuardDuty to Security Hub CSPM. Security Hub CSPM can then include those
findings in its analysis of your security posture.

It's common for bad actors to employ bots to take over accounts
and cheat in
games. [WAF
Bot Control](https://aws.amazon.com/waf/features/bot-control/) gives you visibility and control over common
and pervasive bot traffic that can consume excess resources, skew
metrics, cause downtime, or perform other undesired activities.

Ransomware is malicious code designed to gain unauthorized access
to systems and datasets and encrypt that data to block access by
legitimate players. After ransomware has locked players out of
their systems and encrypted their sensitive data, cyber criminals
demand a ransom before providing a decryption key to unlock the
data. Organizations can be completely shut down by a malicious
event, incurring significant costs and loss of business
productivity. Refer
to [Securing
your AWS Cloud environment from ransomware](https://d1.awsstatic.com/WWPS/pdf/AWSPS_ransomware_ebook_Apr-2020.pdf) for best
practices that you can apply to strengthen your ability to fight
ransomware before, during, and after an incident takes place.

Your game may provide players with the ability to contact player
support agents through a call center such
as [Amazon
Connect](https://aws.amazon.com/connect/) or chat bots using Amazon Lex. Amazon Connect
provides support
for [monitoring
live and](https://docs.aws.amazon.com/connect/latest/adminguide/monitoring-amazon-connect.html)
[recorded
conversations](https://docs.aws.amazon.com/connect/latest/adminguide/monitoring-amazon-connect.html). To analyze interactions between players and
player support chat bots built with Amazon Lex, you can store the
[conversation
logs](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-cw.html) from these interactions in Amazon CloudWatch Logs
which can be exported to Amazon S3 and analyzed as described
previously.

Finally, conduct penetration testing exercises as part of your
infrastructure protection strategy. Whether you are performing
these assessments in-house or through an AWS Partner, adhere to
the
[AWS customer support policies for penetration testing](https://aws.amazon.com/security/penetration-testing/).

### Implementation steps

- Use Amazon GuardDuty to monitor account behavior, network
activity, and data access patterns for threats, and
integrate with Security Hub CSPM for a unified security view.
- Implement AWS WAF Bot Control to help detect and mitigate
bot traffic that can harm resources and player experiences.
- Conduct penetration testing exercises regularly, adhering to
AWS customer support policies, to assess and strengthen your
security posture.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec06-bp01.html*

---

# GAMESEC06-BP02 Use artificial intelligence and machine learning tools to automate aspects of your infrastructure protection strategy

[Amazon
Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/) uses machine learning to automatically
detect and diagnose anomalies in your business and operational
data and monitors the metrics that are most important to your
businesses with greater speed and accuracy. The service also makes
it straightforward to diagnose the root cause of anomalies, such
as a sudden dip in revenue, logins, transactions, or retention. It
does not require game developers to have ML experience to set up
and can connect to popular data sources including Amazon S3,
Amazon CloudWatch, Amazon RDS, Amazon Redshift, as well as many
SaaS applications. For example, you
can [integrate
Amazon Lookout for Metrics with the Game Analytics
Pipeline](https://aws.amazon.com/blogs/gametech/detect-game-anomalies-amazon-lookout-for-metrics-game-analytics-pipeline/) and other data sources to begin analyzing behavior
to detect anomalies.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Alternatively, you may choose to build, train, and host a custom
machine learning model using
[Amazon SageMaker AI AI](https://aws.amazon.com/sagemaker/) to address use cases such as content
moderation, toxicity detection, cheat detection, fraud detection,
and more.

**Customer example**

AnyCompany Games uses Amazon Lookout for Metrics to automatically
detect unusual patterns in server performance, player login
attempts, or transaction volumes that could indicate threats from
bad actors. Additionally, they have used Amazon SageMaker AI to
develop custom machine learning models that continually analyze
network traffic patterns and player behavior to help identify
coordinated threats, such as bot networks that are attempting to
exploit their virtual economy.

This automated approach allows their security team to focus on
investigating and responding to genuine threats rather than
manually monitoring thousands of metrics, while making sure that
emerging threat patterns are detected and addressed before they
can significantly impact game availability or player safety.

### Implementation steps

- Use Amazon Lookout for Metrics to help automatically detect
and diagnose anomalies in key business and operational data
- Integrate Amazon Lookout for Metrics with data sources like
the Game Analytics Pipeline, Amazon S3, or CloudWatch to
monitor metrics such as revenue, logins, and retention.
- Use Amazon SageMaker AI to build, train, and host custom
machine learning models for advanced use cases like cheat
detection, fraud prevention, and content moderation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec06-bp02.html*

---

# GAMESEC06-BP03 Use insights from system-level logs to continuously improve your infrastructure protection strategy

Capture and store system-level logs from relevant services, such
as [S3
server access logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html),
[CloudFront
access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html), and
[ALB
access](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)
[logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html).
These logs can be stored in an S3 bucket in your account and are
useful for associating your player usage information from within
the game with system-level information including connection
details such as IP addresses, request headers, and relevant
request manipulation and filtering that you may have configured
within your game backend. You can send these logs to the same
logging solutions mentioned earlier, and you can
[analyze
them using SQL queries with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html) without requiring
the logs to be moved out of Amazon S3.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Access
Analyzer for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-analyzer.html) is a feature that monitors your bucket
access policies, making sure that the policies provide only the
intended access to your Amazon S3 resources. Access Analyzer for
S3 evaluates your bucket access policies and allows you to
discover and swiftly remediate buckets with potentially unintended
access.

### Implementation steps

- Use AWS services for threat detection and incident response
to automate aspects of your infrastructure protection
strategy.
- Gain insights into your infrastructure protection through
system-level logs and AWS services for artificial
intelligence and machine learning.

## Data protection

When developing and architecting your game, consider what type of
data your studio is gathering and how you have decided to approach
protecting it. Topics to explore within this aspect of security
include:

- How you have chosen to identify and classify your data
- How you are protecting data at rest
- How you are protecting data in transit

There are no data protection best practices specific to the Games
Lens. Refer to the Well-Architected Framework whitepaper for best
practices
in [data
protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html) for security.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec06-bp03.html*

---

# GAMESEC07 — Incident response

**Pillar**: Security  
**Best Practices**: 2

---

# GAMESEC07-BP01 Implement an incident response plan to handle bad actors and abusive behavior

Create a plan of action for responding to bad actors and abusive
behavior in your game.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Consider factors such as when to
temporarily suspend or permanently ban players and how long to
disable credentials for temporarily suspended players.

**Customer example**

AnyCompany Games creates a tiered incident response system in
which minor infractions like inappropriate chat messages result in
automatic 24-hour account suspensions, while more severe
violations such as cheating or harassment trigger immediate 7-day
suspensions with mandatory review by human moderators.

Additionally, AnyCompany Games establishes escalation procedures
in which repeat offenders face progressively longer suspensions.
They create appeal processes that allow falsely flagged players to
contest automated actions while maintaining security through
identity verification requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec07-bp01.html*

---

# GAMESEC07-BP02 Ban accounts that are associated with bad actors

If left unmitigated, abusive behaviors in a game can continue to
have a negative impact on the gaming experience for others and
should be mitigated as soon as possible. Implement a process to
impose bans or other forms of restrictions on bad actors who are
confirmed to be in violation of your terms of service.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Typically, the rules and evaluation process for determining the
circumstances for imposing these types of restrictions will be
determined by personnel such as a player community team or trust
and safety team within your organization. After you've flagged bad
actors, run a pre-determined workflow to act on the identified
players.

For example,
[AWS Step Functions](https://aws.amazon.com/step-functions/) and
[AWS Lambda](https://aws.amazon.com/lambda/) functions can be used to run an automated workflow
that accepts a batch of player accounts as input. The workflow
then updates entries in an
[Amazon DynamoDB](https://aws.amazon.com/dynamodb) table called Bans, which can include details about
the player account, the ban reason, and duration.

Depending on the design of your game and account management system
and the type of abuse that you encounter from bad actors, maintain
a banning system of record that is separate from your account
management system. You may not want to turn off the player's
account from your account management system, opting instead to
simply turn off their ability to play your game. This can be useful
in situations where the player's account credentials are used to
access multiple games with different terms of service or policies.

### Implementation steps

- Define and enforce policies for responding to abusive
behaviors from bad actors.
- Use AWS services to automate your responses to bad actors.

### Resources

- [AWS Security Incident Response Technical Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html)
- [AWS Machine Learning Blog: Detect real and live users and deter
bad actors using Amazon Rekognition Face Liveness](https://aws.amazon.com/blogs/machine-learning/detect-real-and-live-users-and-deter-bad-actors-using-amazon-rekognition-face-liveness/)
- [AWS Solutions for Games: Community Health](https://aws.amazon.com/solutions/games/community-health/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec07-bp02.html*

---

# GAMESEC08 — Application security

**Pillar**: Security  
**Best Practices**: 1

---

# GAMESEC08-BP01 Apply security at every stage of the CI/CD pipeline

Guardrails such as access controls, separation of duties, and
audit trails provide protection against unauthorized access or
malicious activities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Your people, processes, and technology
should secure the pipeline as well. The people closest to the code
must establish secure coding practices and make sure they follow
them. Iterate on your processes continuously to verify that there
is consistency in the level of security throughout the pipeline.
Lastly, implement technology to verify that best practices and
processes are not bypassed.

**Customer example**

AnyCompany Games implements role-based access controls in which
only senior developers can approve changes to their anti-cheat
system code, while requiring mandatory code reviews from security
team members for components that handle player payment data.

Their CI/CD pipeline automatically runs threat model validation
checks, making sure that new features like a player trading
marketplace are tested against previously identified attack
vectors such as item duplication exploits or fraudulent
transaction attempts.

### Implementation steps

- Provide users permissions bases on the principle of least
privilege.
- Use AWS CloudTrail to audit API calls made across the
services used in the pipeline.
- Employ pre-commit hooks to verify that code is following
general practices and company policies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec08-bp01.html*

---

# GAMESEC09 — Automate security

**Pillar**: Security  
**Best Practices**: 1

---

# GAMESEC09-BP01 Integrate tooling and automation to reduce the mean time of security reviews

To identify security vulnerabilities, organizations can use a variety of different tools
and services like Static Application Security Testing (SAST) and Dynamic Application Security
Testing (DAST). SAST is a way to review the source code and determine security vulnerability.
DAST is a black box way of testing your code which tests your applications without looking at
the source code.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Another tool that organizations can use is Software Composition Analysis (SCA), which
assesses the security of your third-party or open source dependencies. For a more manual
approach, secure code reviews can be implemented throughout the pipeline.

**Customer example**

AnyCompany Games uses SAST tools to automatically flag potential security flaws during
the development process. They also use DAST tools to simulate threats against running game
builds to validate that security controls are working as intended. Additionally, AnyCompany
Games integrates dependency scanning tools into their development process to automatically
identify known vulnerabilities in third-party libraries and game engines.

### Implementation steps

- Use Amazon CodeGuru as a SAST tool.
- Use open-source tools like OWASP Dependency Check, SonarQube, or OWASPZap.

### Resources

- [Security for Developers](https://catalog.us-east-1.prod.workshops.aws/workshops/66275888-6bab-4872-8c6e-ed2fe132a362/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec09-bp01.html*

---

# GAMESEC10 — Threat modeling

**Pillar**: Security  
**Best Practices**: 1

---

# GAMESEC10-BP01 Determine when and how to complete threat modeling exercises throughout your application development lifecycle

There is no one single best way to approach threat modeling. Details for when and how to do this will vary based on the unique needs of your game studio. For example, depending on the size of your studio, you may have team members who are involved in one or multiple aspects of the threat modeling process.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The [AWS Security Blog](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/) provides an overview for considerations to keep in mind when devising your strategy for threat modeling, such as:

- Which of your team members and personas should be involved in
threat modeling
- How to determine the appropriate workflow tools to use
- How to determine ownership of various aspects of threat
modeling
- How to identify and evaluate security controls to be used
within your workload design

**Customer example**

AnyCompany Games begins by cataloging valuable assets such as
player data, game code and algorithms, in-game currencies,
user-generated content, and intellectual property like unreleased
content or proprietary engines. They consider different types of
potential bad actors such cheaters seeking unfair advantages, bad
actors attempting to steal personal or financial data, and
malicious users trying to disrupt gameplay.

Throughout the development process, AnyCompany Games uses threat
models to guide secure coding practices and influence testing
strategies to focus on high-risk areas. Before a game launch, they
conduct comprehensive threat modeling reviews to assess readiness
for anticipated player loads and unauthorized access attempts, and
to prepare incident response procedures.

### Implementation steps

- Implement guardrails at every stage of your CI/CD pipeline.
- Use automation and tools to improve the efficiency of your
application security reviews.
- Use threat modeling as a process for improving the security
of your applications.

### Resources

- [AWS Security Blog: How to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)
- [NIST:
Guide to Data-Centric System Threat Modeling](https://csrc.nist.gov/pubs/sp/800/154/ipd)
- [Threat
modeling the right way for builders – AWS Skill Builder
virtual self-paced training](https://explore.skillbuilder.aws/learn/course/external/view/elearning/13274/threat-modeling-the-right-way-for-builders-workshop)
- [Threat
modeling for builders – AWS Workshop](https://catalog.workshops.aws/threatmodel)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec10-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
