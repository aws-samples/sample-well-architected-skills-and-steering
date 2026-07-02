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
