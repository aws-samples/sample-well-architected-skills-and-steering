# GAMEOPS06 — Optimize over time

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# GAMEOPS06-BP01 Monitor key game metrics to identify player trends and patterns, and use the information to improve the game

In addition to game client system usage, app usage, exceptions,
and crash data, capture game telemetry data that is sent to a game
backend system. This data should represent player activity so that
you can understand how players interact with various features in
the game.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Depending on its implementation, game clients can collect
telemetry data at predefined game features or locations in a game
world. The data is sent to the backend ingestion service for
processing. If the backend service is unreachable, the clients can
store the data locally on the local device until the backend
service is available again. The game designers use this telemetry
data to review how players are playing the game, and if there are
anomalies in the game.

For example, player movements and interactions with items in a map
can be extracted from telemetry data and plotted as a heat map of
activities in-game by players over a set window of time. Such data
assists the game designers identify the need to balance various
elements in the game, such as the power of a weapon, the power of
an in-game character, or the complexity of a map. The raw
telemetry data is generally stored and then processed to extract
analytics that can be visualized by analysts.

The
[Game
AnalyticsPipeline](https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/) solution implementation assists game
developers launch a scalable serverless data pipeline to ingest,
store, and analyze telemetry data generated from games and
services. The solution supports streaming ingestion of data,
allowing users to gain insights from their games and other
applications within minutes.

For custom game telemetry data ingestion, storage, processing and
analytics, AWS also offers a number
of [specialized
services for big data processing and Analytics](https://aws.amazon.com/big-data/datalakes-and-analytics/).

### Implementation steps

- **Capture game telemetry
data:** Collect data on player activity, system
usage, exceptions, and crashes to understand player
interactions and identify issues.
- **Implement telemetry
collection:** Use predefined game features or
locations to collect telemetry data and send it to backend
services, storing locally if the backend is unreachable.
- **Use AWS analytics
solutions:** Use AWS services like the Game
Analytics Pipeline for scalable data ingestion, storage, and
analysis, as well as specialized big data processing and
analytics services.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops06-bp01.html*

---

# GAMEOPS06-BP02 Update and adapt the load testing approach as the game changes

Optimizing the load testing approach is a continuous process that
should evolve alongside the game development cycle. As the game
grows in complexity, user base, and feature set, the load testing
strategy must adapt to verify that it accurately simulates
real-world conditions and provides actionable insights.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Consider
the following:

**Missing or outdated testing
scenarios**

As new functionality is added to a game during the development
process, create and run new load testing scenarios to validate the
performance and scalability of the new features. Similarly,
features and functionality are often refactored to improve
performance, address player feedback, or align with new design
goals, requiring testing scenarios to be continuously updated to
keep pace with the changes and truly test and reflect the state of
the system.

**New load testing frameworks**

Developers might need to change load testing frameworks for a
variety of reasons:

- The initial framework may no longer be able to adequately
simulate the user load or provide the necessary level of
insight into the system's performance
- New game features might require load testing support for new
protocols, APIs, or integration points
- Developers might desire more advanced features as they become
more comfortable with the load testing process
- Preference for frameworks that better align with the team's
technical expertise, programming languages, or existing
toolchains

By carefully evaluating and adapting over time, developers can
align the load testing process with the game's changing
requirements and continue to provide the requisite insights to
optimize and improve the overall user experience.

**Optimizing cost**

The ease and convenience of using managed AWS services can be
highly beneficial, especially in the early stages of development.
These services abstract the underlying infrastructure management,
allowing teams to quickly set up their solution and focus solely
on crafting load testing scenarios and analyzing the results.
However, using managed services can often come at a higher cost
because of the additional value and convenience they provide, like
provisioning, configuring, and maintaining infrastructure, as well
as providing high availability, scaling, and monitoring
capabilities.

As teams mature and grow more comfortable and confident with their
load testing process, there may come a time when self-managing the
infrastructure can provide additional optimization and cost
savings. While this hands-on approach increases the operational
overhead, having direct control over the compute resources,
configurations, scaling behaviors, and resource utilization can
unlock new opportunities for fine tuning and reducing cost. For
example, it might make sense for teams to start their load testing
journey with an AWS Fargate serverless architecture, then move to
self-managing the underlying nodes in an Amazon EKS cluster later.

### Implementation steps

- **Update testing scenarios:**
Continuously create and update load test scenarios to
validate new features and refactored functionalities, and
verify that they reflect the current state of the game.
- **Evaluate load testing
frameworks:** Adapt to new frameworks as needed to
simulate user load, support new protocols, and align with
the team's expertise and toolchains.
- **Optimize costs:** Start
with managed AWS services for ease and convenience, then
consider self-managing infrastructure for cost savings as
the team grows more comfortable with the load testing
process.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops06-bp02.html*

---
