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
