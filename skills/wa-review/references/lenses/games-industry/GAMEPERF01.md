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
