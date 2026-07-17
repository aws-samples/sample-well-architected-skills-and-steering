# Performance efficiency

**Pages**: 6

---

# Definition

There are four best practice areas for performance efficiency in
the cloud:

- Selection (compute, storage, database, network)
- Review
- Monitoring
- Tradeoffs

Take a data-driven approach to selecting a high-performance
architecture. Gather data on all aspects of the architecture,
from the high-level design to the selection and configuration of
resource types. By reviewing your choices on a cyclical basis,
you will ensure that you are taking advantage of the continually
evolving AWS Cloud.

Monitoring will ensure that you are aware of any deviance from
expected performance and can take action on it. Finally, your
architecture can make tradeoffs to improve performance, such as
using compression or caching, or relaxing consistency
requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/definition-3.html*

---

# Selection

SaaS PERF 1: How do you prevent one tenant from adversely
impacting the experience of another tenant?

In a multi-tenant environment, tenants might have profiles and
use cases that impose significantly different loads on your
system. New tenants with new workload profiles might also be
continually added to the system. These factors can make it very
challenging for SaaS companies to build an architecture that can
meet the rapidly evolving performance requirements each of these
tenants.

Handling and managing these variations in tenant load is key to
the performance profile of a SaaS environment. A SaaS
architecture must be able to successfully detect these tenant
consumption trends and apply strategies that can scale
effectively to meet tenant demands or restrict the activity of
individual tenants.

There are a variety of strategies that can be used to manage
these scenarios where a tenant might be placing a
disproportionate load on your system. This can be achieved
through isolation of high-demand resources, introduction of
scaling strategies, or the application of throttling policies.

In the simplest and most extreme case, you might consider
creating tenant-specific deployments for parts of your
application. The diagram in Figure 22 illustrates one way that
you might decompose your system to address performance
challenges.

*Figure 22: Addressing performance with siloed services*
In this example, you’ll notice that we have two distinct
deployment footprints (some in a silo model and some in a pool
model). On the left side of the diagram, you’ll see that
separate instances of Product, Order, and Cart microservices
have been deployed for each tenant. Meanwhile, on the right side
of the diagram, you’ll see a collection of microservices that
are shared by all tenants.

The basic idea behind the approach is to carve out specific
services that are seen as critical to the performance profile of
our application. By separating them out, your system can ensure
that the load of any one tenant won’t impact the performance of
other tenants (for this set of services). This strategy can
increase costs and decrease the operational agility of your
environment, but still represents a valid way to target
performance areas. This same approach may also be applied to
address compliance and isolation requirements.

You might, for example, deploy an order management microservice
for each tenant to limit any ability for one tenant to adversely
impact another tenant’s order processing experience. This adds
operational complexity and reduces cost efficiency, but can be
used as a brute force way to selectively target cross-tenant
performance issues for key areas of your application.

Ideally, you should try to address these performance
requirements through constructs that can address tenant load
issues without absorbing the overhead and cost of separately
deployed services. Here you would focus on creating a scaling
profile that allows your shared infrastructure to effectively
respond to shifts in tenant load and activity.

A container-based architecture, such as Amazon EKS or Amazon ECS, could be configured to scale your services based on tenant
demand without requiring any significant over-provisioning of
resources. The ability for containers to scale rapidly enhances
your system’s ability to respond effectively to spikey tenant
loads. Combining the scaling speed of containers with the cost
profile of AWS Fargate often represents a solid blend of
elasticity, operational agility, and cost efficiency that can
help organizations address the spikey loads of tenants without
over-provisioning environments.

A serverless SaaS architecture built with AWS Lambda could also
be a good fit for addressing the spikey tenant loads. The
managed nature of AWS Lambda allows your application’s services
to scale rapidly to address spikes in tenant load. There might
be concurrency and cold start factors you’d need to factor into
this approach. However, it can represent an effective strategy
for limiting cross-tenant performance impacts.

While a responsive scaling strategy can help with this problem,
you might want to put other measures in place to simply prevent
tenants from imposing loads that would have cross-tenant
impacts. In these scenarios, you might choose to detect and
constrain the activity of the tenants by setting limits
(potentially by tier) that would apply throttling to control the
level of load the place on your system. This would be achieved
by introducing throttling policies that would examine the load
of tenants, identify and activity that exceeds limits, and
throttle their experience.

SaaS PERF 2: How are you ensuring that the consumption of
infrastructure resources aligns with the activity and workloads
of tenants?

The business model of SaaS companies often relies heavily on a
strategy that allows them to align the costs of their
infrastructure with the actual activity of their tenants. Since
the load and makeup of the tenants in a SaaS system is
continually changing, you need an architecture strategy that can
effectively scale the consumption of resources in a pattern a
pattern that very much mirrors these real-time, unpredictable
patterns of consumption that are part of the SaaS experience.

The graph in Figure 23 provides a hypothetical example of an
environment that has aligned infrastructure consumption and
tenant activity. Here the blue solid line represents the actual
activity trends of tenants spanning a window of time. The red
dashed line represents the actual infrastructure that’s being
provisioned to address the load of tenants.

*Figure 23: Aligning tenant activity and consumption*
Our strategy here, in an ideal environment, would be to keep the
gap between the red a blue line as small as possible. You’ll
always have some margin for error here where you have some
cushion to ensure that you’re not impacting the availability or
performance of the system. At the same time, you want to be able
to deliver just enough infrastructure to support the
*current* performance needs of your tenants.

The key challenge here is that the load shown in this diagram is
often unpredictable. While there may be some general trends,
your architecture and scaling strategies can’t assume that the
load today will be the same tomorrow or even in the next hour.

The simplest approach to aligning consumption with activity is
to use AWS services that provide a serverless experience. The
classic example of this would be AWS Lambda. With AWS Lambda,
you can build a model where servers and scaling policies are no
longer your responsibility. With serverless, your SaaS
application will only incur those charges that are directly
correlated with tenant consumption. If there’s no load on your
SaaS system, there will be no AWS Lambda costs.

AWS Fargate also enables a container-based version of this this
serverless mindset. By using Fargate with Amazon EKS or Amazon ECS, you only pay for the container compute costs that are
actually consumed by your application.

This ability to use a serverless model extends beyond compute
constructs. For example, the storage pieces of your solution can
rely on serverless technology as well. Amazon Aurora Serverless
allows you to store relational data without needing to size the
instances that are running your database. Instead, Amazon Aurora
Serverless will size your environment based on actual load and
only charge for what your application consumes.

Any model that lets you move away from a need to create scaling
policies is going to streamline your operational and cost
experience. Instead of continually chasing the elusive perfect
automatic scaling configuration, you can focus more of your time
and energy on the features and functions of your application.
This also enables the business to grow and accept new tenants
without being concerned about unexpected jumps in its AWS bill.

For scenarios where serverless may not be an option, you’ll need
to fall back to traditional scaling strategies. In these
scenarios, you’ll need to capture and publish tenant consumption
metrics and define scaling policies based on these metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pe-selection.html*

---

# Review

There are no performance practices unique to SaaS
applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/review.html*

---

# Monitoring

SaaS PERF 3: How do you enable varying levels of performance
for different tenant tiers and plans?

SaaS solutions are often offered in a tiered model where
tenants will have access to different experiences. Performance
can often be an area that is used to differentiate tiers of a
SaaS environment, using performance as a way to create a value
boundary that would compel tenants to move to higher level
tiers.

In this model, your architecture will introduce constructs
that will monitor and control the experience of each tier.
This isn’t just about maximizing performance—it’s also about
limiting the consumption of lower tiered tenants. Even if your
system could accommodate the load of these tenants, you might
choose to limit this load purely based on cost or business
considerations. This is often part of ensuring that the cost
footprint of a tenant correlates with the revenue that tenant
contributes to the business.

The least complex way to approach this problem is to introduce
throttling policies that are associated with individual tenant
tiers. As a tenant reaches a limit, you would apply the
throttling and limit their consumption.

There are also scenarios where you can use specific AWS
configurations to configure the consumption profile of a
tenant tiers. For example, in AWS Lambda, you can use reserve
concurrency to limit the consumption of a given tenant tier.
The diagram in Figure 24 provides an example of how this could
be realized.

*Figure 24: Controlling tenant performance with reserve concurrency*
In this example, we’ve created three separate tenant tiers and
deployed three separate collections of our SaaS application’s
microservices for each of these tiers. These collections are
also configured with separate reserve concurrency settings
which are used to determine how many concurrent function
invocations can be running for that group of functions. The
Basic tier has a reserve concurrency of 100 and the Advanced
tier has 300. The idea here is that the consumption of my
lower end tiers will be capped, leaving all the remain
concurrency for the premium tier.

This approach aligns nicely with our goal of offering the best
experience our preferred tiers while also limiting a lower
tier’s ability to consume excess resources and impact the
performance of our higher tier tenants.

Containers also have unique strategies for addressing tiering for performance. Within
Amazon EKS, for example, you can configure separate `ResourceQuotas` and
`LimitRanges` to control the amount of resources that are available in a
namespace.

While these constraints are helpful in configuring a tenant’s
performance experience, some SaaS applications will actually
address performance through application design and
decomposition strategies. This might be achieved by deploying
siloed microservices for higher tier tenants, eliminating any
noisy neighbor considerations for these specific services. In
fact, you might find that the decomposition of your system
into microservices might be directly influenced by the tiering
and performance profile you are targeting.

In some cases, your SaaS application might also introduce
architectural constructs that optimize the experience of
higher tier tenants. Imagine, for example, offering caching of
key data to premium tier tenants. By limiting the cache to
just these users, you avoid the expense of having a cache that
must support all users. The effort to introduce these
optimizations should be offset with enough value to the
customer and the business to warrant the investment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/monitoring.html*

---

# Tradeoffs

There are no performance practices unique to SaaS
applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pe-tradeoffs.html*

---

# Resources

Refer to the following resources to learn more about our best
practices related to performance efficiency.

**Documentation and blogs**

- [Optimizing
SaaS Tenant Workflows and Costs Blog](https://aws.amazon.com/blogs/apn/optimizing-saas-tenant-workflows-and-costs/)
- [Using
Amazon SQS in a Multi-Tenant SaaS Solution](https://aws.amazon.com/blogs/apn/using-amazon-sqs-in-a-multi-tenant-saas-solution/)
- [Importance
of Service Level Agreement for SaaS Providers](https://aws.amazon.com/blogs/apn/importance-of-service-level-agreement-for-saas-providers/)
- [Amazon API Gateway: Throttle API requests for better throughput](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- [Creating
and using usage plans with API keys](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html)
- [Monitoring
CloudWatch metrics for your Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html)
- [Dynamic
scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)

**Whitepapers**

- [SaaS
Storage Strategies Building a Multi-tenant Storage Model on AWS](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/multi-tenant-saas-storage-strategies.html)
- [SaaS
Tenant Isolation Strategies whitepaper](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html)

**Videos**

- [AWS
re:Invent 2018: SaaS Reference: Review of Real-World Patterns & Strategies](https://www.youtube.com/watch?v=O3L-dSyqA7g)
- [AWS
re:Invent 2016: Optimizing SaaS Solutions for AWS](https://www.youtube.com/watch?v=D-8fTCz8_Yo&t=121s)
- [SaaS
Metrics: The Ultimate View of Tenant Consumption](https://www.youtube.com/watch?v=X2SgoAl1vK8)
- [Microservices
decomposition for SaaS environments (ARC210)](https://www.youtube.com/watch?v=AOfuZN5yo38)
- [SaaS
tenant isolation patterns](https://youtu.be/fuDZq-EspNA?t=1519)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/resources-3.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
