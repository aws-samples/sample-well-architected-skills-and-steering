# GAMEPERF03 — Iterative development

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# GAMEPERF03-BP01 Use Amazon GameLift Anywhere and a GameLift testing toolkit

To enhance performance efficiency through an iterative development
process, utilize Amazon GameLift Anywhere along with the Amazon
GameLift Testing Toolkit to establish a comprehensive testing
environment.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

This approach allows rapid iteration, efficient data
collection, and detailed performance analysis. Key steps include:

**Create a test environment**

Use Amazon GameLift Anywhere to set up a local or cloud-based test
environment. This setup removes the need to upload each game
server build iteration to a managed fleet, reducing the activation
time.

**Integrate Amazon GameLift Testing
Toolkit**

Incorporate the Amazon GameLift Testing Toolkit into your
development workflow. The toolkit provides scripts, tools, and
libraries to visualize Amazon GameLift infrastructure, launch
virtual players, and iterate upon FlexMatch rule sets with the
FlexMatch simulator. It simplifies the integration and management
of Amazon GameLift resources, allowing you to automate common
tasks and gather necessary data for performance analysis.

**Rapid build and test cycles**

Quickly update the test fleet with new builds, start it, and
commence testing. This facilitates a fast build-test-repeat cycle,
enabling developers to validate various aspects of the game's
player experience, including multiplayer interactions.

**Comprehensive testing**

Test your game server integration with the Amazon GameLift server
SDK, backend service interactions, matchmaking configurations, and
other GameLift hosting features. Utilize the GameLift Testing
Toolkit to automate testing and gather detailed performance
metrics, making sure that game components work seamlessly
together.

**Analyze performance data**

Use the data collected by the GameLift Testing Toolkit to analyze
performance bottlenecks and optimize your game server. The toolkit
helps track key metrics, identify issues, and make data-driven
decisions to improve performance efficiency.

By incorporating Amazon GameLift Anywhere and the GameLift Testing
Toolkit into your iterative development process, you can
significantly enhance performance efficiency through rapid
testing, comprehensive integration checks, and detailed
performance analysis.

### Implementation steps

- Use Amazon GameLift Anywhere to create a test environment,
reducing activation time for game server builds and enabling
rapid iteration.
- Integrate the Amazon GameLift Testing Toolkit to automate
testing tasks, simulate players, and validate FlexMatch
configurations during development.
- Collect and analyze performance data with the GameLift
Testing Toolkit to identify bottlenecks, optimize game
servers, and enhance performance efficiency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf03-bp01.html*

---

# GAMEPERF03-BP02 Test performance and scalability of game servers

To test the performance and scalability of your game servers,
implement a robust testing framework using the Amazon GameLift
features and the GameLift Testing Toolkit.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Key practices include:

Iterative testing

Use an Amazon GameLift Anywhere fleet to create a cloud-based
hosted environment where you can iteratively build and test game
components. This environment should mirror real-world hosting
conditions, enabling realistic performance and scalability
testing.

Game server integration testing

Test the integration of your game server with the Amazon GameLift
server SDK, including starting new game sessions and tracking game
session events using AWS CLI or GameLift Testing Toolkit. This
verifies that the game server functions correctly within the
GameLift environment.

Use the GameLift Testing Toolkit to automate testing and gather
detailed performance metrics. The toolkit allows you to visualize
GameLift infrastructure, launch virtual players for load testing,
and iterate on FlexMatch rule sets with the FlexMatch simulator.
It is particularly useful for scaling ECS Fargate tasks, which
simulate player sessions by creating numerous concurrent game
sessions to stress test the server infrastructure.

Scalability testing

Experiment with game session queue designs, multi-location fleets,
Spot and On-Demand fleets, and multiple instance types. Test game
session placement options, latency policies, and fleet
prioritization settings. Configure capacity scaling to meet player
demand and validate that the system can handle the expected load
under different conditions.

### Implementation steps

- Use Amazon GameLift Anywhere to set up a realistic test
environment for iterative performance and scalability
testing.
- Test game server integration with the GameLift server SDK,
facilitating correct session management and event tracking
within the GameLift environment.
- Perform scalability testing with the GameLift Testing
Toolkit, simulating player load, testing session queues, and
validating fleet scaling, latency policies, and
prioritization settings.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf03-bp02.html*

---

# GAMEPERF03-BP03 Optimize resource utilization of GameLift containers

To optimize resource utilization of GameLift containers, design
your container fleet effectively and set precise resource limits.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Key guidelines include:

- **Container group design:**
Organize your software into container groups. The primary
container should bundle your game server application and the
Amazon GameLift Agent. Use sidecar containers for additional
software to manage dependencies and set container-specific
limits for memory and CPU usage.
- **Set resource limits:** For
each container group, determine the required memory and CPU
resources. Set optional limits for individual containers to
verify they have reserved resources but can also exceed these
limits if additional resources are available. This helps
prevent resource contention and potential container failures.
- **Daemon container group:**
Consider using a daemon container group for background or
monitoring processes that do not need to scale with the
primary container group. This verifies that essential
background tasks are handled efficiently without impacting the
primary game server processes.

### Implementation steps

- Design container groups with a primary container for the
game server and GameLift Agent, and sidecars for managing
dependencies, with specific memory and CPU limits.
- Set resource limits for each container group to reserve
required resources while allowing controlled resource usage
to avoid contention.
- Use a daemon container group for background or monitoring
tasks, making sure they operate efficiently without
affecting primary game server processes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf03-bp03.html*

---
