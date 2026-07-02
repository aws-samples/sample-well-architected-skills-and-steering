# GAMEPERF07 — Networking and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# GAMEPERF07-BP01 Define network latency thresholds for your game

When developing a multiplayer game, verify that your game
infrastructure does not introduce unnecessary latency for players.
If your game is sensitive to network latency, then you should set
latency thresholds in your matchmaking logic to prioritize placing
players on game server sessions that are hosted in nearby game
server locations or AWS Regions that meet your objective for ideal
player experience.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

In many latency-sensitive games it is common to instrument the
game clients to ping each of the game's infrastructure locations
to gather performance data such as network latency, jitter, and
packet loss, and report this data to the metrics collection
backend so that it can be analyzed. When matching players into
game sessions, you can configure your game to incorporate the game
client's perceived network latency to your game server
infrastructure as one of the inputs used in your matchmaking
service logic.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp01.html*

---

# GAMEPERF07-BP02 Run a separate matchmaking service for each gameplay mode and game hosting Region

If your game offers multiple gameplay modes for players to choose
from, you should separate the matchmaking systems for each of them
so that you can independently tune the performance for each
gameplay mode based on its unique requirements and reduce resource
contention. Each gameplay mode will likely have unique
requirements for acceptable latency, match size, as well as other
customize game-specific matchmaking logic. They will also likely
attract different types of players. Run each game mode's
matchmaking service as a separate software deployment so that you
can performance test and operate the game modes independently.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

For example, you might run these as separate Lambda functions for
each game mode, or you might operate them as separate
container-based service deployments.

Deploy your matchmaking services to multiple Regions near your
game server locations. Player traffic will take many routes, so it
is important for the matchmaking service to maintain an up-to-date
latency profile across multiple ISPs to improve the efficiency of
low latency game session placement. GameLift FlexMatch provides
additional guidance for selecting Regions for matchmakers, and
includes the ability to integrate your matchmakers with
[multi-Region
game session queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp02.html*

---

# GAMEPERF07-BP03 Regularly monitor matchmaking performance

One of the most noticeable ways to optimize the performance of a
game for players is to reduce the time that they must wait before
they can enter a game session. Long wait times can cause players
to lose interest and lead to attrition, so it is important to
consider this when designing your matchmaking solution.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When you are designing your matchmaking configuration for your
game, create rules that determine the conditions that are applied
to form a match. You should consider the impact that these rules
will have on the performance of the system, particularly the wait
times for players. Before deploying changes to your matchmaking
implementation, such as the addition of new matchmaking conditions
or filters, test this beforehand or consider releasing this change
gradually to a small sample population of players as a canary or
A/B test to gather performance metrics before introducing this
change to the entire player population.

Configure your matchmaking service to generate detailed logs to
understand the conditions or rules that were applied to each
matchmaking request. This assists in the review and to adjust
matchmaking implementation as necessary.

For example,
[Amazon GameLift
FlexMatch](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-intro.html) provides a fully managed matchmaking service
which can be used as a standalone service with your own game
server hosting or used with game servers hosted on Amazon
GameLift. FlexMatch can generate event notifications to Amazon EventBridge, see
[Set
up FlexMatch event notifications](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-notification.html). Use Amazon Simple Notification Service (Amazon SNS) to receive matchmaking data in
JSON format, allowing you to automatically process and store this
information for analysis to improve matchmaking performance.

Set up metrics to track how long your matchmaking service takes to
find a suitable game session for players. Review matchmaking
duration metrics regularly and correlate these times with player
behavior and community sentiment. Use this data to develop
suitable thresholds for matchmaking timeouts that can be included
in your matchmaking rule configuration.

For example, Amazon GameLift FlexMatch provides support for
defining matchmaking request timeouts as well as creating
matchmaking rules that can
[allow
requirements to relax over time](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-design-ruleset.html#match-rulesets-components-expansion). This feature allows you to
create matchmaking that can adapt to make it straightforward to
create matches and place players into game sessions when matches
are difficult to find.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp03.html*

---

# GAMEPERF07-BP04 Regularly monitor networking performance

For competitive games, it is important to have a consistent player
experience.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A game that is reliably 50ms for a larger player base
is fairer and more fun than a match where one player has 10ms ping
and another who has 70ms ping. ISP routing changes may impact part
of the player population, and your matchmaking system will need to
adapt.
[Amazon CloudWatch Network Monitoring](https://aws.amazon.com/cloudwatch/features/network-monitoring/) assists in determining
whether the issue is with your game or the player internet
provider.

### Implementation steps

- Use Amazon Cloudwatch Network Monitoring to track network
performance and identify routing issues.
- Use VPC Flow Logs to identify abnormal traffic patterns or
dropped packets, which can indicate network congestion, ISP
issues, or misconfigurations impacting player latency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp04.html*

---

# GAMEPERF07-BP05 Use network acceleration technology to improve performance across the internet

In addition to physically placing latency-sensitive game
infrastructure closer to players, you can also improve the player
experience by optimizing the network performance for your game.
AWS uses the BGP protocol to influence
[internet
routing](https://aws.amazon.com/blogs/architecture/internet-routing-and-traffic-engineering/) to use the fastest path to our border network from
Internet Service Providers. If you operate your own network and
need more control and observability over routing behavior and BGP
advertisement, you can use private
[Peering](https://aws.amazon.com/peering/) or Direct Connect to route traffic from the internet to your
game running on AWS.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Consider the following reference architecture to support improved
internet performance and responsiveness.

**Enhanced network performance for gaming
using Global Accelerator**

For a fully managed solution to network routing,
[AWS Global Accelerator](https://aws.amazon.com/global-accelerator) improves your application's network
performance using the AWS global network, which can be used to
accelerate your gameplay traffic, voice chat, and real-time
messaging traffic, as well as other latency-sensitive applications
while providing fast failover to your game servers. Global Accelerator
[custom
routing accelerators](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-global-accelerator-custom-routing-accelerators/) can be integrated with your
matchmaking service to provide deterministic routing of multiple
players to the same game session using static anycast IP addresses
and ports.

Your game development teams may be distributed around the world
and require performant access to shared content or assets. To
improve the performance for shared content stored in Amazon S3
buckets, you can setup bi-directional replication of your data
across Regions using
[S3
Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) so that users can access data from
buckets closer to them. To simplify this access pattern, use
[S3
Multi-](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html)
[Region
Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html) which accelerates requests to S3 over the
global network using Global Accelerator.

For more information, refer to
[Improving
the Player Experience by Leveraging AWS Global Accelerator and
Amazon GameLift FleetIQ](https://aws.amazon.com/blogs/gametech/improving-the-player-experience-by-leveraging-aws-global-accelerator-and-amazon-gamelift-fleetiq/).

### Implementation steps

- Use AWS Global Accelerator to help improve network
performance for gameplay traffic, voice chat, and real-time
messaging, while facilitating fast failover to game servers.
- Configure Global Accelerator custom routing accelerators to
integrate with your matchmaking service, enabling
deterministic routing of players to game sessions using
static anycast IPs.
- Enable S3 Cross-Region Replication to replicate shared
content across Regions for distributed game development
teams.
- Use S3 Multi-Region Access Points to accelerate S3 data
access over the AWS global network for globally distributed
users.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf07-bp05.html*

---
