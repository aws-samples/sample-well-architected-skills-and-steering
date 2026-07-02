# GAMEREL02 — Change management

**Pillar**: Reliability  
**Best Practices**: 2

---

# GAMEREL02-BP01 Implement a scaling strategy that incorporates the state of active player game sessions

Implement a solution for automatically scaling your game
infrastructure in a manner that incorporates the stateful nature
of your actively connected player sessions and gracefully handles
scaling activities without disrupting gameplay.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

One of advantages of developing a game in the cloud is the
elasticity that can be achieved by automatically scaling server
infrastructure as needed to meet demand. While stateless or
asynchronous games and backend services can be dynamically scaled
using [Amazon EC2 Auto Scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html),
[EKS
autoscaling](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html), or similar techniques typically adopted for
scalable web applications, game developers typically require a
more customized approach for scaling stateful or synchronous games
to help block disruptions to active player sessions.

### Implementation steps

- For stateful games, generate custom metrics that can be used
to monitor the state of your player sessions and available
game server capacity, which can be reported to Amazon CloudWatch as custom metrics. Exercise features with
application monitoring, such as CloudWatch Synthetics,
checking the game for impairment of functions that simple up
and down health monitoring may not detect.
- Using custom metrics, implement game server scaling
software, for example, as a serverless application using AWS Lambda function or AWS Fargate, to manage the fleet of
dedicated game server instances by using the AWS SDK to make
API calls to update the minimum, maximum, and desired
capacity settings for the
EC2 [Auto
Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) hosting your game server build.
- Use Amazon GameLift to host your game servers and use
the [out-of-the-box
game server auto scaling capabilities](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-manage-capacity.html) to manage this
scaling process for you.

The automatic scaling capabilities of Amazon GameLift are aware
of active player sessions and can be configured to block the
termination or scale-in of game server instances that are
actively hosting players. For more information,
see [Monitor
Amazon GameLift Servers with Amazon CloudWatch](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel02-bp01.html*

---

# GAMEREL02-BP02 Support the use of multiple EC2 instance types for your game

When hosting your game using EC2 instances, or if you use
containers hosted on EC2 instances in your AWS account, use
multiple instance types in your hosting strategy. By using
multiple instance types, you can increase the number of compute
options that can be used when your game is scaling to add more
servers to support player growth, which improves reliability in
case your preferred instance type is unavailable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When hosting your game using Spot Instances, use multiple instance
types since the availability of Spot Instances fluctuates based on
customer demand.

Test your game on multiple instance types to meet your cost and
performance requirements and determine a prioritized ranking of
instance types. Amazon EC2 Auto Scaling supports using multiple
instance types and sizes as well
as [assigning
weights to each instance type](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) in your configuration so that
you can implement prioritized ranking of compute options.

When hosting your game using Amazon GameLift managed hosting,
decide what type of instances your game needs and how to run game
server processes on them (using a runtime configuration). When
choosing resources for a fleet, consider several factors,
including game operating system, instance type (the computing
hardware), and whether to use On-Demand Instances, Spot Instances,
or both. Hosting costs with Amazon GameLift primarily depend on
the type of instances you use. For more information,
see [Choose
compute resources for a managed fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-compute.html).

### Implementation steps

- Use multiple EC2 instance types to improve reliability and
scaling options when hosting your game on EC2 or containers.
- Configure Amazon EC2 Auto Scaling or GameLift fleets with
prioritized instance types and weights to optimize cost and
performance.
- Test your game on various instance types to verify that
performance meets requirements and adjust your hosting
strategy
accordingly***.***

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel02-bp02.html*

---
