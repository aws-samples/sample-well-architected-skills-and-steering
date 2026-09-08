# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 8

---

# GAMEPERF01 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# GAMEPERF01-BP01 Evaluate game server resource requirements and scalability needs

Evaluate server requirements against your scalability needs to verify that you are selecting a hosting option that both meets your requirements and provides optimal performance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When selecting the appropriate hosting option for your game
servers, consider the following factors:

**Game server resource
requirements**

Assess the CPU, memory, network, and storage requirements of your
game server processes to determine what your game consumes.
Do not overlook networking; each frame requires CPU cycles to
receive player actions, update the state of the game, and send it
back to the player. Offloading packet processing can free up CPU
for core game functions. Networking is the foundation for smooth
and responsive game play so testing it early in the process
defines a baseline performance profile for a game.

A first person shooter game might have high actions per second
which the CPU needs to quickly move off to the network which may
favor compute optimized C family instances, while a turn-based
strategy game which can spend more CPU cycles processing per turn
may need increased memory from R family instances to locally store
and update the state of the game on the server before sending it
back to players. Use a data-driven approach like
[the
Utilization Saturation and Errors (USE) Method](https://www.brendangregg.com/usemethod.html) to make well
informed architectural choices.

**Scalability and elasticity**

Evaluate how quickly and smoothly each hosting option can scale to
meet player demand without compromising performance. Consider the
level of automation and flexibility required for your game's
workload to maintain a smooth gaming experience during peak times.
A game server might scale quickly by increasing utilization
through adding additional game server processes on the same
instance, where a game backend may scale slower based on the
rising active user count and games being played. Your fleet should
scale with demand to minimize cost while facilitating minimal wait
time for the players to get into game. Review Amazon EC2 Spot
Instance Advisor to gain insight into cost effective available
capacity for game server fleets.

### Implementation steps

- Evaluate game server resource requirements for CPU, memory,
network, and storage to select suitable instance types,
considering game-specific performance needs such as high
network throughput for FPS games or memory optimization for
turn-based strategy games.
- Compare different hosting options such as containers,
instances, bare-metal, and managed services by analyzing
performance data using frameworks like the USE method. Use
these insights to make better decisions about your system
architecture.
- Design fleets for scalability and elasticity, leveraging
tools like EC2 Spot Instance Advisor to optimize costs while
facilitating quick scaling to meet player demand during peak
times.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf01-bp01.html*

---

# GAMEPERF01-BP02 Consider operational overhead for scaling game servers

Consider the management and operational overhead associated with
each hosting option.

Level of risk exposed if this best practice is not established: High

## Implementation guidance

**Operational overhead**

Self-hosted solutions on EC2 or containers
can provide more control but also will require more management.
Container orchestrators like ECS or EKS can reduce launch times
for containerized servers while also increasing networking
complexity and maintenance orchestration overhead.

As an example,
[EKS
managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html) can automate provisioning and lifecycle
management of your game servers but do not respect pod disruption
budgets when terminating a node, if your game requires longer than
the 15 minute termination period to safely complete games, you may
need to create lifecycle hooks or consider self-managed nodes with
custom controllers to block game interruption.

Managed services like Amazon Game Lift may handle most of the
operational overhead but reduce the amount of visibility and
control over special requirements for low level networking and
security configuration. Choosing a game server solution is a
trade-off between the level of customization, control and
responsibility you will have for tuning game server performance
and scaling behavior.

### Implementation steps

- Assess operational overhead for hosting options, balancing
control and management effort between self-hosted solutions
like EC2, ECS, or EKS and managed services like Amazon Game
Lift.
- Use EKS managed node groups for automation but implement
lifecycle hooks or custom controllers if your game servers
require longer termination periods than the default.
- Weigh the trade-offs between customization, visibility, and
operational responsibility when selecting a game server
solution.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf01-bp02.html*

---

# GAMEPERF01-BP03 Evaluate integration with other AWS services, development environments, target CPU architectures, and features

Evaluate how well each hosting option integrates with other AWS
services your game relies on, such as databases, analytics, or
content delivery services.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Integration with other AWS
services**

Seamless integration between services
provides operational benefits like improved performance monitoring
and efficient secure data delivery between game components, game
servers, game backend services and observability solutions.

For example, Coordinating traffic shifts for live games can be
complex. Amazon Route 53 will help keep your DNS records up to
date which simplifies coordinated traffic shifts. AWS Global Accelerator traffic dials enable you to send a percentage of
traffic to another Region and keep your game running during
maintenance.

**Development environment and
tools**

Consider the development tools, frameworks, and environments
supported by each architecture option. Verify that your chosen
option aligns with your game development solution and programming
languages, as this can impact your team's ability to optimize and
maintain game server performance. Delivering a game across mobile,
console, and PC will increase tooling and testing complexity.
Cross-system support is particularly important for multi-game
studios where centralized services can standardize development
best practices across titles.

**Target CPU architecture and
features**

Consider the performance profile of your game engine and game
server processes and the level of ARM support available. Evaluate
if you can benefit from improved price performance of ARM based
Graviton or x86 based AMD64 processors. Do you need to use Intel
features like AES-NI encryption, AVX or Turbo Boost? Review
[Dedicated
Host types](https://aws.amazon.com/ec2/dedicated-hosts/pricing/) to identify single versus multi-socket instance
families. When using a multi-socket instance family, consider NUMA
pinning and L3 cache sharing in your game server processes. Use
[C-state
and P-state](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html) configuration to get the best performance for
your game by tuning frequency clock and reducing sleep levels.

### Implementation steps

- Select hosting options with seamless integration with AWS
services like AWS Secrets Manager, ACM, and others to help
streamline performance monitoring, secure data delivery, and
reduce manual operational tasks.
- Verify compatibility between your hosting option and your
development environment, frameworks, and programming
languages to optimize and maintain server performance
effectively.
- Evaluate CPU architecture requirements, leveraging Graviton
for price-performance or x86 for specific features like
AES-NI, AVX, and Turbo Boost, and optimize server
performance with NUMA pinning and C-state/P-state tuning.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf01-bp03.html*

---

# GAMEPERF02 — Region selection

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GAMEPERF02-BP01 Select a home Region that is near your players

For an initial game launch, you should determine where to deploy
infrastructure based on discussions with your business
stakeholders, such as publishing teams who determine where the
game is expected to be made available to players, and where they
are focusing their pre-launch marketing and advertising efforts.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Your business stakeholders should also have mechanisms to
stimulate demand to gain a better understanding of player
reception and viability. For example, these teams will have
mechanisms such as game pre-orders, marketing events and
campaigns, public email lists for players to register interest
before launch, and other approaches to establish relevant signals
to determine where the game will likely have the most players at
launch. The game may also use a regional roll out strategy that
includes play test and soft-launch phases to determine regional
player demand.

[Select
a home Region](https://aws.amazon.com/about-aws/global-infrastructure/) that is near your player base and your
developers and has the AWS services and features you need to host
your game. The home RSegion will be where the game backend
services will run, and it may also run game servers. Evaluate a
home Region based on services supported, connectivity to edge
locations, proximity to failover Regions, and number of
Availability Zones. If you are using a Local Zone, consider the
parent Region is sometimes located in a different geographic area.
As an example: Santiago, Chile Local Zone us-east-1-scl-1a has N.
Virginia us-east-1 as its parent Region even though it is
geographically closer to Sao Paulo sa-east-1.

### Implementation steps

- Identify deployment Regions based on player demand signals
from pre-launch activities like pre-orders, marketing
campaigns, and interest registrations.
- Choose a home Region close to the primary player base and
developers, making sure it supports required AWS services,
edge locations, and failover Regions.
- Evaluate Local Zones carefully, considering that the parent
Region may differ geographically from the location of the
Local Zone.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf02-bp01.html*

---

# GAMEPERF02-BP02 Design an approach that supports placing latency-sensitive game infrastructure close to players to improve performance

Separate placement for latency sensitive infrastructure like game
servers minimizes the impact of long network routes. Repeatable
deployments can make it simple to maintain multiple locations that
are more performant for your players. Ping is a common metric that
is surfaced in game UI and low ping can be a differentiating
capability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When first launching a game, you may not yet have enough
information about your player base to adequately know where best
to deploy infrastructure closest to the players that are most
interested in playing your game. This is a common challenge, and
you should prepare for this scenario by designing an architecture
that allows you to rapidly adjust your hosting placement strategy
to deploy servers where they are needed closer to players. It is
typical for game developers to regularly assess their game
infrastructure deployment as a recurring post-launch analysis to
incrementally invest in improvements over time with an iterative
approach.

A best practice is to use infrastructure-as-code templates, such
as AWS CloudFormation or Terraform by Hashicorp, for the
configuration of your infrastructure such as VPCs, subnet
configurations, and dependencies required to launch critical game
services so that you can refer to these templates, quickly
customize them if needed, and deploy them into locations where
additional infrastructure is needed to support your players.

You should also make sure you understand how your current
deployment strategy could be evolved to allow future expansion.
IaC templates are repeatable but are not a substitute for network
planning.
[IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
manages your VPCs. Subnet sizing, Availability Zone selection, and
IP inventory and cross-account Availability Zone alignment. The
network is important to consider and can be disruptive to players
when changed. Game servers deployed across multiple geographic
locations will connect to your game backend, which is more common
to be hosted in a single or multiple home Regions which can
require additional configuration to support private connectivity.
These considerations should be continuously evaluated over time so
that you can make changes to your game hosting strategy as your
game's requirements evolve or your player requirements change.

When determining how many game hosting locations to use for your
game, consider the following factors:

- **Quality of player experience
improvement:** How much of a player experience
improvement can you introduce by adding additional game
hosting locations? What is the incremental performance gain
that you can achieve by doing so? How will you measure this
performance improvement?
- **Which player populations to
prioritize:** How many players can you improve the
experience for if you add additional game hosting locations?
Which player populations, or geographic locations, will you
prioritize?
- **Downstream impacts of
change:** If you change your game hosting strategy,
how will this influence your matchmaking wait times for
players? Can the match sizes, skill balance or number of
players in the player pool accommodate a game hosting location
strategy change? Supporting more locations can potentially
fragment the player pool and add increased cost and
complexity.

Each of these considerations should be evaluated as you determine
where you add or remove game hosting locations. For example, you
may choose to prioritize improving the experience for players in
geographic locations with the least performant gameplay
experience, or for players who express the most vocal public
feedback. You may also choose to factor the player monetization
into your priorities, for example by focusing attention on
improving the experience for players in geographic locations that
generate a significant source of revenue for your game or have the
potential to generate incremental revenue if you introduce
performance improvements.

In addition to hosting infrastructure in AWS Regions, you can use
[Local
Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), which are an extension of an AWS Region, to host
your game servers and other latency sensitive applications such as
voice chat servers closer to your players. You might also choose
to run game development infrastructure in Local Zones to improve
the experience for your game development teams. For example, you
can use Local Zones to address use cases such as hosting replicas
of your self-managed source control servers closer to your game
developers, and to offer game development virtual workstations and
content storage to users using Amazon EC2 instances, EBS volumes,
and Amazon FSx file systems deployed into one or more Local Zones
near your development studios without requiring you to host the
infrastructure on-premises.

[Outposts](https://aws.amazon.com/outposts/)
are a good choice when Regions or Local Zones are not available in
the same geographic area. Connectivity from your data center to
AWS should be considered to enable game server to backend system
reliability. AWS Outposts and Outpost Servers are purpose-built to
run AWS in your datacenter using the same services and APIs to
help create a consistent deployment model wherever you run your
game. Multiple racks can be combined into a logical Outpost, and
the infrastructure can be shared across AWS accounts. The hardware
lifecycle is managed by AWS and the lead time can be as short as 3
months.

If you are building games using containers and want the flexibility
to adopt a hybrid deployment architecture using open-source
software that can be deployed on your own on-premise
infrastructure, you can use
[ECS
Anywhere](https://aws.amazon.com/ecs/anywhere/), or
[EKS
Anywhere](https://aws.amazon.com/eks/eks-anywhere/) as an alternative to AWS Outposts or Local Zones.
If you host with Amazon GameLift;
[Amazon
GameLift Anywhere can be used to run your server build on local
hardware](https://aws.amazon.com/blogs/gametech/hybrid-game-server-hosting-with-amazon-gamelift-anywhere/) which can speed up your development process,
enabling you to use Local Zones or register your own metal as part
of the your fleet.

### Implementation steps

- Use infrastructure-as-code tools like AWS CloudFormation or
Terraform for repeatable deployments, enabling quick
customization and scaling of game hosting locations based on
player needs.
- Evaluate player experience improvements, player population
priorities, and downstream impacts such as matchmaking times
when adding or removing game hosting locations.
- Use AWS Local Zones, Outposts, or hybrid options like ECS
Anywhere, EKS Anywhere, or GameLift Anywhere to optimize
latency-sensitive infrastructure and support diverse
deployment needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf02-bp02.html*

---

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

# GAMEPERF04 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GAMEPERF04-BP01 Monitor game server processes to detect issues

You might run multiple game server processes per instance to
efficiently utilize the resources on your game server instances.
If so, design your architecture so that an individual game server
process hosting a game session cannot cause adverse impact to
other game sessions hosted on the same instance. Use metrics to
understand how game placement and game mode type can impact the
performance of game server instances. Incorporate a mix of low
load (lobby, shop, or single player tutorial) and high load
(ranked, multi-player, or high skill gameplay) processes to avoid
hot spotting the game server instance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Monitor the player experience through client side and server-side
metrics by collecting telemetry for ping time and jitter, frame
drops, API response time, errors and successful game loop
completion. Correlate time stamps for these events with player
support issues and server logs to identify performance
bottlenecks. Tools like
[Dtrace](https://en.wikipedia.org/wiki/DTrace),
[ftrace](https://en.wikipedia.org/wiki/Ftrace),
[uperf](https://uperf.org), and
[eBPF](https://www.brendangregg.com/ebpf.html)
can be used for deep investigation and analysis of system
performance.

Implement monitoring of the limited resources available to your
game server instances so that you can generate alerts when
individual game server processes are breaching pre-determined
resource budget thresholds. When thresholds are breached, you may
want to configure your game server software to dump relevant
system and game server logs out to durable storage, such as a
central logging solution, so that your game server engineers can
investigate this behavior. Additionally, your game server instance
should be configured to report metrics from each of the game
server processes running on the instance so that you can monitor
these individual game server processes in addition to the overall
metrics for the game server instance.

For example, GameLift provides metrics for
[monitoring
game sessions](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html), which can be augmented with custom
game-specific metrics and logs collected using the
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
[Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
which you can configure on your game server instance. Your metrics
can be viewed in CloudWatch or exported to other tools such as
[Amazon Managed Grafana](https://aws.amazon.com/grafana/) which is integrated with Single Sign-On to make it
straightforward to access metrics by users who may not have access
to the Management Console. Refer to the following best practices
for
[managing
logs and metrics using Amazon GameLift](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift_quickstart_customservers_metrics.html), which also provides
support for viewing individual
[game
session logs](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetGameSessionLogUrl.html).

### Implementation steps

- Run multiple game server processes per instance and mix low
and high-load game modes to avoid hot spotting and verify
balanced resource utilization.
- Monitor client-side and server-side metrics like ping,
jitter, frame drops, and API response times, and correlate
these with server logs and issues reported by players to
identify bottlenecks.
- Configure resource monitoring for each game server process,
generate alerts for threshold breaches, and store logs in
durable storage for analysis using tools like CloudWatch and
Amazon Managed Grafana.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf04-bp01.html*

---

# GAMEPERF04-BP02 Performance test your game server with simulated and real gameplay scenarios

Conduct performance testing and evaluate various
gameplay scenarios to determine whether the game server process
handles the utilization of fixed resources appropriately, such as
EC2 instance memory, CPU, and network bandwidth.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Creating simulated gameplay tests with bots that can mirror common
gameplay paths and behaviors of your players can determine how
your game server processes handle this under different usage
scenarios. For example, you can implement a solution, such as
[Distributed
Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) that you can customize to run game
client simulations or game client builds to generate gameplay
scenarios. Run internal play tests and use QA teams to stress test
the various features of your game so that you can develop
confidence that your game is designed to perform optimally.
[AWS Device Farm](https://aws.amazon.com/device-farm/) can be used to perform mobile and web testing for your
iOS, Android, and browser games on multiple device types.

### Implementation steps

- Conduct performance testing with bots simulating common
player behaviors to evaluate game server resource
utilization under different scenarios.
- Use solutions like Distributed Load Testing on AWS to
customize and simulate gameplay scenarios for stress
testing.
- Perform internal playtests and use tools like AWS Device Farm for mobile and browser game testing on various devices.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf04-bp02.html*

---

# GAMEPERF05 — Compute selection

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GAMEPERF05-BP01 Benchmark your game performance across multiple compute types

For game server workloads, there is no singular approach to
identifying the optimal compute solution for hosting your game
server. A common strategy for benchmarking game servers is to
start with compute-optimized EC2 'c' instances, because this
instance family provides high performance for workloads that are
computationally intensive. Alternatively, if your game requires a
significant amount of memory to implement specific features, the
memory-optimized instances may be most suitable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

If your workload utilizes significant network resources, consider
implementing instances that are network-optimized which is
typically indicated using an 'n' in the instance name, avoid
burstable instance types 't' as after credits are exhausted
performance will decrease. Games are sensitive to latency and
dropped packets, so it is recommended to use EC2 enhanced
networking to help improve the network performance of your game
servers. Enhanced networking uses single root I/O virtualization
([SR-IOV](https://docs.aws.amazon.com/whitepapers/latest/ec2-networking-for-telecom/overview-of-performance-optimization-options.html))
to provide high-performance networking capabilities on
[supported](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html#supported_instances)
[instance
types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html#supported_instances) . SR-IOV is a method of device virtualization that
provides higher I/O performance and lower CPU utilization when
compared to traditional virtualized network interfaces. Enhanced
networking provides higher bandwidth, higher packet per second
(PPS) performance, and consistently lower inter-instance
latencies. Enhanced networking with Elastic Network Adapter is
available for most recent EC2 instance types and is important to
[regularly
update](https://github.com/amzn/amzn-drivers/tree/master) to benefit from performance enhancements from newer
instances and improvements to the
[AWS Nitro hypervisor.](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html)

If your game performs similarly across multiple EC2 instance
types, then you should consider using multiple instance types to
host your game servers. Monitor performance over time and perform
further optimization after you have hosted enough production game
sessions to be able to identify performance trends. Remember that
your compute requirements may change as you add new features into
your game that require different allocation of resources. You can
[configure
EC2 Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) to use multiple instance types, or
you can use separate Auto Scaling groups to host game server
instances that run separate instance types which may make it
simpler to manage correlation and aggregation of metrics.

Evaluate how your game performs on different types of processors
such as Intel-based instances, AMD-based instances, and ARM-based
Graviton instances. Unreal Engine 5.1.1 or
[newer
can compile game servers for Graviton](https://aws.amazon.com/blogs/gametech/compiling-unreal-engine-5-dedicated-servers-for-aws-graviton-ec2-instances/) and can improve price
performance for your game. Perform sweep and saturation testing at
various sizes within each family to determine the sweet spot where
utilization and performance are consistent.

You should also benchmark how your game performance is impacted
when it is hosted using containers and Lambda functions. For use
cases where long-lived game server processes are not required,
such as asynchronous games and for game backend services, consider
using a serverless architecture with Lambda which can simplify
management and operations for game operations teams, as well as
allow you to more quickly deploy your game globally to many AWS Regions. For serverless best practices, refer to
the [Serverless
Applications Lens - Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html).

### Implementation steps

- Benchmark game servers on compute-optimized 'c' instances
for CPU intensive workloads, memory-optimized instances for
memory heavy task, and network-optimized 'n' instances for
high network throughput.
- Use enhanced networking with Elastic Network Adapter (ENA)
on supported instances to improve network performance,
reduce latency, and increase packet processing rates.
- Evaluate and test multiple instance types, processors
(Intel, AMD, Graviton), and container or Lambda hosting
options, adjusting compute solutions as game features
evolve.

For more information, see
[Choose
the right compute strategy for your global game servers](https://aws.amazon.com/blogs/gametech/choose-the-right-compute-strategy-for-your-global-game-servers/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf05-bp01.html*

---

# GAMEPERF05-BP02 Move non-latency-sensitive compute tasks to asynchronous workflows

When you are optimizing the performance for your game, it is
important to keep in mind that only some of the interactions
between the client and the game backend must be performed in a
synchronous manner. You should consider each feature from the
perspective of the player experience and determine whether certain
interactions require synchronous communications, which are
blocking and resource intensive, or whether those features can be
implemented in an asynchronous manner. When you implement network
calls, use an asynchronous, non-blocking approach. Additionally,
your game backend should also be configured to perform work in an
efficient manner by offloading tasks to queues and prioritizing fast
responses to clients where possible.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For example, updating a leader board at the end of a player
session can be implemented asynchronously so that the client does
not need to wait for the leader board update to complete. Instead,
implement this asynchronously on the game client, and consider
designing your backend service to push these types of operations
into queues, such as Amazon SQS. With this architecture, configure
your backend to accept the request, enqueue it in SQS which helps
durably store messages for asynchronous processing, and promptly
reply to the client. When the leader board update is completed,
the backend can send an update to the game client so that the
player's view of the leader board is updated.

Alternatively, the player can simply visit your game's leader
board screen to retrieve the latest data, which can issue a web
request to your backend to retrieve the latest data from cache.

### Implementation steps

- Determine if client-backend interactions require synchronous
communication; implement asynchronous, non-blocking
approaches where possible to optimize resource usage.
- Use Amazon SQS to offload non-critical tasks like
leaderboard updates.
- Allow the client to fetch updated data asynchronously, such
as retrieving the latest leaderboard data on demand or via
background updates.

### Resources

- [Understanding
asynchronous messaging for microservices](https://aws.amazon.com/blogs/compute/understanding-asynchronous-messaging-for-microservices/)
- [Lambda
- Using service integrations and asynchronous
processing](https://docs.aws.amazon.com/lambda/latest/operatorguide/integrations-asynchronous.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf05-bp02.html*

---

# GAMEPERF06 — Data management

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# GAMEPERF06-BP01 Centralize log collection and storage

Implement a centralized log collection and storage solution to gather logs from game server
instances and GameLift.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Use services like Amazon CloudWatch Logs to collect, monitor, and store log data from your game
servers and GameLift instances. CloudWatch Logs provides a scalable and fully managed solution for log
management, facilitating efficient storage and retrieval of log data without impacting game
server performance. If you are running the [CloudWatch Logs agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), consider the
various install types and configuration options like batch size, buffer duration to minimize
impact to the game server. Consider the game server instances ephemeral and reduce dependency
on localized logging where possible. Establish a centralized policy for implementation of
[Logging best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-best-practices.html).

### Implementation steps

- Use Amazon CloudWatch Logs to collect, monitor, and store log data from game server instances
and GameLift, facilitating centralized and scalable log management.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp01.html*

---

# GAMEPERF06-BP02 Categorize and store game data based on access patterns

Categorize your game data into different types based on their
access patterns and storage requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Common categories
include player data, game saves, persistent world storage, and
analytics data.

### Implementation steps

Use appropriate storage solutions for each data type to optimize
performance and cost-efficiency:

- **Player data:** Use Amazon DynamoDB, a fast and scalable NoSQL database, to store
player profiles, preferences, and progression data. The
low-latency access and automatic scaling capabilities of
DynamoDB provide efficient retrieval and update of player
data.
- **Game saves:** Use Amazon S3
to store game saves and checkpoints. S3 provides high
durability and scalability for storing large amounts of game
save data. Consider using S3 Transfer Acceleration or Amazon CloudFront for faster uploads and downloads of game saves.
- **Persistent world storage:**
For games with persistent world states or shared game data,
consider using Amazon DynamoDB, Amazon ElastiCache or Amazon MemoryDB. ElastiCache and MemoryDB provide in-memory
key-value store while DynamoDB is an SSD backed NoSQL
database. These services provide fast access to stored data,
reducing the time it takes for the game server process to
save game state which improves overall process performance.
- **Analytics data:** Use
Amazon Managed Streaming for Apache Kafka or Kinesis Data Streams
to ingest data streams from your game data producers. Amazon
Managed Service for Apache Flink can be used for real-time
transformation and analysis and sent to Amazon Data Firehose
for processing and delivery into backend data lakes,
warehouses and analytics services.
[Guidance
for Game Analytics Pipeline on AWS](https://aws.amazon.com/solutions/guidance/game-analytics-pipeline-on-aws/) illustrates how
the services work together to provide near real-time and
batch analytics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp02.html*

---

# GAMEPERF06-BP03 Enable efficient log formatting and batching

Configure your game server processes to generate logs in a structured and in a format that
can be parsed, such as JSON.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Implement log batching techniques to minimize the frequency of log data transfers from
your game servers to the centralized log storage. Batching logs reduces network overhead and
improves game server performance. Use verbose or debug level logs as an exception and not a
default, as they can incur a performance and cost penalty that should be avoided when
possible.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp03.html*

---

# GAMEPERF06-BP04 Implement log rotation and retention policies

Establish log rotation and retention policies to manage the growth
of log data and optimize storage utilization.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Configure your game
servers to automatically rotate logs based on size or time
intervals. Define log retention policies in Amazon CloudWatch Logs
to automatically archive or delete older log data that is no
longer needed for active analysis or troubleshooting.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp04.html*

---

# GAMEPERF06-BP05 Use monitoring and visualization tools

Use monitoring and visualization tools to gain insights into your
game server performance and identify optimization opportunities.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use Amazon CloudWatch to monitor key metrics and set up alarms for
proactive notifications. Utilize tools like Amazon Managed Service for Prometheus and Amazon Managed Grafana to collect,
query, and visualize metrics from your game servers and
infrastructure. Create informative dashboards to track
performance, identify bottlenecks, and make data-driven
optimizations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp05.html*

---

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

# GAMEPERF08 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GAMEPERF08-BP01 Inform and include the player in your process

Provide an option to display in game metrics like latency, frames
per second and dropped packets. Surface infrastructure issues and
maintenance downtime through player facing communication like
status pages. Celebrate new game locations with player comms
including dev blogs and set expectations for expected player
experience improvements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Include the player**

Provide a simple diagnostic submission process that collects
relevant files and attaches them to a player support ticket from
your game client. Enable a support forum where players can help
each other and become a part of improving the game experience

**Consider trade-offs versus player
expectations**

Moving backend systems for cost efficiency may not be noticeable
to players but moving game servers can change ping time. Be
consistent and fair to players with reasoning for expansion and
reduction of your game hosting locations.

Player communities and geographies will have their own
characteristics that may impact expectations of your game. For
example, South Korea has some of the fastest internet on the
planet and the expectation for gameplay is single digit latency
which drives highly competitive play. Casual gameplay on mobile
devices creates a different performance profile and use pattern in
comparison to console and PC session play.

Login and lobby are a part of the experience and should feel
responsive, even if the server is offline for maintenance. Raid
night planning or hanging out in the lobby is part of the player
experience and is important to consider when choosing focus areas
for performance efficiency. Players may leave your game client
open for months, sometimes they may just log in occasionally to
read the patch notes. A Live Ops game needs to keep the entire
player experience in mind as a part of engineering process and
culture.

### Implementation steps

- Provide in-game metrics such as latency, FPS, and packet
loss, and communicate infrastructure issues and maintenance
schedules via status pages and player-facing updates.
- Implement a diagnostic dump and submission feature in the
game client and create a support forum to foster
community-driven troubleshooting and improvement.
- Tailor performance optimizations to player community
expectations, such as low latency for competitive Regions or
responsive login/lobby experiences for casual and
long-session players.
- Design Live Ops workflows to account for the entire player
experience, from active gameplay to idle client behavior,
facilitating seamless engagement.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf08-bp01.html*

---

# GAMEPERF08-BP02 Align solution selection with engineering team skills and expertise

Assess your team's skills and expertise in managing and optimizing
game server performance when choosing your hosting option.
Self-hosted solutions like EC2 and containers require more
knowledge of infrastructure management, performance tuning, and
scaling. If your team lacks these skills, a managed service like
GameLift may be more suitable, as it abstracts away many of the
complexities and allows your team to focus on game-specific
optimizations.

**Level of risk exposed if this best
practice is not established: High**

## Implementation guidance

By evaluating these factors and conducting performance tests
across different hosting options, you can select the most
appropriate solution that meets your game's specific requirements
while optimizing for performance efficiency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf08-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
