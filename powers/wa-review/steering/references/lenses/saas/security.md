# Security

**Pages**: 12

---

# Definition

There are five best practice areas for security in the cloud:

- Identity and access management
- Detective controls
- Infrastructure protection
- Data protection
- Incident response

Multi-tenancy adds a layer of additional considerations to your
SaaS architecture. With SaaS, you have users that are now
accessing a shared environment in the context of a given tenant.
This context must be captured and conveyed across all the layers
of your application’s architecture and plays a fundamental role
in securing the overall footprint of your environment.

From a security perspective, you need to look at how tenancy is
introduced into your environment and how it is used to secure
tenant resources. Overall, you need to ensure that each tenant
has a carefully constrained experience that prevents them from
accessing any other tenant’s resources.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/definition-1.html*

---

# Identity and access management

SaaS SEC 1: How are you associating tenant context with users
and applying that context within your SaaS architecture?

The move to a multi-tenant architecture often begins with
identity. Each user that accesses your application must be
connected with a tenant. This binding of a user identity to a
tenant is informally referred to as a *SaaS
identity*. The key attribute of the SaaS identity is
that it elevates tenant context to a first-class construct,
connecting it directly to the overall authentication and
authorization model of your SaaS application.

This approach allows tenant context to flow through all the
layers of the architecture using the same architecture
constructs that are used to convey and access user identity.
For example, if you have 100 microservices in your
application, you want each of those services to be able to
acquire and apply tenant context without requiring a roundtrip
to another service. Managing this context through another
service adds latency and often creates bottlenecks in your
architecture.

Injecting tenant context into your identity can be achieved
through multiple patterns. The identity provider and
technology you select for your application will directly shape
the approach and strategies that you’ll end up applying to
introduce this context into your experience. While the tools
might change, the fundamental need is to introduce tenancy
into the overall authentication experience of your environment
where tenancy is injected at the point where a user enters
your application.

The diagram in Figure 15 provides an example of how this is
commonly achieved using AWS services. This example includes
the common components and technologies that would be used to
inject tenant context into a SaaS environment. This is
illustrated on the left side of the diagram, where a tenant
completes a sign-up form, and triggers a call to your
application’s registration service.

*Figure 15: Injecting tenant content*
This registration service creates a tenant and then creates a
user in Amazon Cognito. As part of this process, you introduce
custom claims into user’s attributes that hold information
about the user’s relationship to a tenant. These custom claims
become part of the identity signature of your user, connecting
them directly with a tenant as a first-class construct.

After the onboarding is completed, you then can look at how
these user and tenant attributes are applied when a user logs
in (the right-hand side of the diagram). Here you’ll see that
the user authenticates against Amazon Cognito and, as part of
that process, returns a JSON web token (JWT) that includes the
custom claims created during the onboarding process.

Now you have a token that has all the information that you
need to inject tenant context into the interactions with
multi-tenant application services. In this example, we show
the JWT being passed as a bearer token in the header of each
request to the Product microservice. This service can now
acquire and apply the context from this token without calling
another service.

Finally, this Product microservice makes a call to an Order
microservice, passing the JWT in the header of the request.
This illustrates how the tenant context can flow across all of
your microservice calls without adding any additional lookups
or latency.

This example happens to rely on Amazon Cognito to connect the
user and tenant identities. However, this same model could be
implemented with other identity providers or alternate
authentication schemes. The key here is that you’re building
an authentication experience that can yield a representation
that connects tenant and users. This representation should
then be available to all the layers of your solution.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/identity-and-access-management.html*

---

# Detective controls

There are no security practices unique to SaaS applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/detective-controls.html*

---

# The isolation mindset

At the conceptual level, many SaaS providers would agree on
the importance and value of protecting and isolating tenant
resources. However, as you dig into the details of
implementing an isolation strategy, you’ll often find that
each SaaS ISV has their own definition of what is
*enough* isolation.

Given these varying perspectives, we have outlined some tenets
below that will help guide your overall value system for
tenant isolation. Every SaaS provider should establish a clear
set of high-level isolation requirements that will guide their
teams as they define the isolation footprint of their SaaS
environment. The following are some key tenets that typically
shape the overall SaaS tenant isolation model:

**Isolation is not optional** –
Isolation is a foundational element of SaaS and every system
that delivers a solution in a multi-tenant model should ensure
that their systems take measures to ensure that tenant
resources are isolated.

**Authentication and authorization are
not equal to isolation** – While it is expected that
you will control access to your SaaS environments through
authentication and authorization, getting beyond the entry
points of a login screen or an API does not mean you have
achieved isolation. This is just one piece of the isolation
puzzle and is not enough on its own.

**Isolation enforcement should not be
left to service developers** – While developers are
never expected to introduce code that might violate isolation,
it’s unrealistic to expect that they will never
unintentionally cross a tenant boundary. To mitigate this,
scoping of access to resources should be controlled through
some shared mechanism that is responsible for applying
isolation rules (outside the view of developers).

**If there’s not an out-of-the box
isolation solution, you may have to build it
yourself** – There are a number of security
mechanisms, such as AWS Identity and Access Management (IAM),
that can help you simplify the path to tenant isolation.
Combining these tools with your broader security scheme can
help make isolation an easier process.. However, there might
be scenarios where your isolation model is not directly
addressed by a corresponding tool or technology. The absence
of a clear solution should not represent an opportunity to
lower your isolation requirements—even if that means building
something of your own.

**Isolation is not a resource-level
construct** – In the world of multi-tenancy and
isolation, some will view isolation as a way to draw a hard
boundary between concrete infrastructure resources. This often
translates into isolation model where you might have separate
databases, compute instances, accounts, or virtual private
clouds (VPCs) for each tenant. While these are common forms of
isolation, they are not the only way to isolate tenants. Even
in scenarios where resources are shared—in fact, especially in
environments where resources are shared—there are ways to
achieve isolation. In this shared resource model, isolation
can be a logical construct that is enforced by runtime applied
policies. The key point here is that isolation should not be
equated to having siloed resources.

**Domains may impose specific isolation
requirements** – While there are many approaches to
achieving tenant isolation, the realities of a given domain
might impose constraints that will require a specific flavor
of isolation. For example, some high compliance industries may
require that every tenant have its own database. In these
cases, the shared, policy-based approaches to isolation may
not be adequate.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/isolation-mindset.html*

---

# Silo isolation

While SaaS providers are often focused on the value of sharing
resources, there are still scenarios where a SaaS provider
might choose to have some (or all) of their tenants deployed
in a model where each tenant is running a fully siloed stack
of resources. Some would say that this full-stack model does
not represent a SaaS environment. However, if you’ve
surrounded these separate stacks with shared identity,
onboarding, metering, metrics, deployment, analytics, and
operations, then this is a valid variant of SaaS that trades
economies of scale and operational efficiency for compliance,
business, or domain considerations. With this approach,
isolation is an end-to-end construct that spans an entire
customer stack. The diagram in Figure 16 provides a conceptual
view of this view of isolation.

*Figure 16: Silo isolation model*
This diagram highlights the basic footprint of the siloed
deployment model. The technologies that are used to run these
stacks are mostly irrelevant here. This could be a monolith,
it could be serverless, or it could be any mix of the various
application architecture models. The key concept is to take
whatever stack the tenant has and surround it with some
construct to encapsulate all the moving parts of that stack.
This becomes the boundary for isolation. As long as you can
prevent a tenant from escaping their fully encapsulated
environment, you’ve achieved the isolation.

Generally, this model of isolation is much simpler to enforce.
There are often well-defined constructs that will enable you
to implement a robust isolation model. While this model
presents some real challenges to the cost and agility goals of
a SaaS environment, it can be appealing to those that have
very strict isolation requirements.

## Silo model pros and cons

Each SaaS environment and business domain has its own unique
set of requirements that might make silo a fit. However, if
you’re leaning in this direction, you’ll definitely want to
factor in some of the challenges and overhead associated with
the silo model. These are some of the pros and cons that you
need to consider if you are exploring a silo model for your
SaaS solution:

### Pros

- **Supporting challenging compliance models** – Some
SaaS providers are selling into regulated environments that impose strict isolation
requirements. The silo model provides these ISVs with an option that enables them to
offer to some or all of their tenants the option of being deployed in a dedicated
model.
- **No noisy neighbor concerns** – While all SaaS
providers should be attempting to limit the impacts of noisy neighbor conditions,
some customers will still express reservations about the potential of having their
workloads impacted by the activity of other tenants using the system. The silo model
addresses this concern by offering a dedicated environment with no potential for
noisy neighbor scenarios.
- **Tenant cost tracking** – SaaS providers are often
highly focused on understanding how each tenant is impacting their infrastructure
costs. Calculating a cost-per-tenant can be challenging in some SaaS models.
However, the coarse-grained nature of the silo model provides you with a simpler way
to capture and associate infrastructure costs with each tenant.
- **Reduced scope of impact** – The silo model generally
reduces your exposure when there might be some outage or event that surfaces in your
SaaS solution. Since each SaaS provider is running in its own environment, any
failures that occur within a given tenant’s environment will likely be constrained
to that environment. While one tenant may experience an outage, the error cannot
cascade through the remaining tenants that are using your system.

### Cons

- **Scaling issues** – There are limits on the number of
accounts that can be provisioned. This limit might prevent you from selecting the
account-based model. There are also general concerns about how a rapidly growing
number of accounts might undermine the management and operational experience of your
SaaS environment. For example, having 20 siloed accounts for each of your tenants
might be manageable. However, if you have a thousand tenants, that number would
likely begin to impact operational efficiency and agility.
- **Cost** – With every tenant running in its own
environment, much of the cost efficiency that is traditionally associated with SaaS
solutions is not realized. Even if these environments scale dynamically, you’ll
likely have periods of the day when you’ll have idle resources that are going
unconsumed. While this is a completely acceptable model, it undermines the ability
of your organization to achieve the economies of scale and margin benefits that are
essential to the SaaS model.
- **Agility** – The move to SaaS is often directly
motivated by a desire to innovate at a faster pace. This means adopting a model that
enables the organization to respond and react to market dynamics at a rapid pace. A
key part of this is being able to unify the customer experience and quickly deploy
new features and capabilities. While there are measures you can take with the silo
model to try to limit its impact on agility, the highly decentralized nature of the
silo model adds complexity that impacts your ability to easily manage, operate, and
support your tenants.
- **Onboarding automation** – SaaS environments place a
premium on automating the introduction of new tenants. Whether these tenants are
being onboarded in a self-service model or using an internally managed provisioning
process, you will still need to automate onboarding. And, when you have separate
siloes for each tenant, this often becomes a much more heavyweight process. The
provisioning of a new tenant will require the provisioning of new infrastructure
and, potentially, the configuration of new account limits. These added moving parts
introduce overhead that introduces additional dimensions of complexity into the
overall onboarding automation, enabling you to focus less time on your customers.
- **Decentralized management and monitoring** – The goal
with SaaS is to have a single pane of glass that enables you to manage and monitor
all tenant activity. This requirement is especially important when you have siloed
tenant environments. The challenge here is that you must now aggregate the data from
a more decentralized tenant footprint. While there are mechanisms that will enable
you to create an aggregate view of your tenants, the effort and energy needed to
build and manage this experience is more complex in a siloed model.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-isolation.html*

---

# Pool isolation

You can see how the silo model of isolation maps very nicely for many SaaS
companies. Many companies that are moving to SaaS are seeking out the efficiency,
agility, and cost benefits of being able to have their tenants share some or all of
their underlying infrastructure. This shared infrastructure approach, which is referred
to as a pool model, adds a level of complexity to the isolation story. The diagram in
Figure 17 provides an illustration of the challenge associated with implementing
isolation in a pooled model.

*Figure 17: Pool isolation model*
In this model, you’ll notice that our tenants are consuming infrastructure that is
shared by all tenants. This enables the resources to scale in direct proportion to the
actual load being imposed by the tenants. The right side of the diagram narrows in on
the compute aspect of one of the services, highlighting the fact that tenants 1-N might
all be running side-by-side within your shared compute at any given time. The storage in
this example is also shared and is represented as a table indexed by individual tenant
identifiers.

This model can work well for SaaS providers, however, it has the potential to
complicate the overall isolation story. With shared resources, implementing isolation is
not as clear and typical networking and IAM constructs cannot be relied upon to create
boundaries between tenants.

The key here is that—even though this is a more challenging environment to
isolate—you cannot use this as a rationale to relax the isolation requirements of your
environment. The shared model increases the chance for cross-tenant access and, as such,
it represents an area that requires you to be especially diligent about ensuring that
resources are isolated.

As we dig deeper into the pool isolation model, you’ll see how this architectural
footprint introduces a unique blend of challenges—each of which requires its own type of
isolation constructs to successfully isolate a tenant’s resources.

## Pool model pros and cons

While having everything shared can enable a lot of efficiency and optimization, it
also requires SaaS providers to weigh some of the tradeoffs that come with adopting this
model. In many cases, the pros and cons of the pool model end up surfacing as the
inverse of pros and cons we covered for the silo model. These are the key pros and cons
that are typically associated with the pool isolation model.

### Pros

- **Agility** – When you move your tenants into a shared
infrastructure model, you can leverage the natural efficiencies and simplicity that
help streamline the agility of your SaaS offering. At its core, the pool model is
all about enabling SaaS providers to manage, scale, and operate all of their tenants
with one unified experience. Centralizing and standardizing the experience is
foundational to enabling SaaS providers to more easily manage and apply changes to
all tenants without having to perform one-off tasks on a tenant-by-tenant basis.
This operational efficiency is key to the overall agility footprint of your SaaS
environment.
- **Cost efficiency** – Many companies are drawn to SaaS
for its cost efficiency. A big part of this cost efficiency is commonly associated
with the pool model of isolation. In a pooled environment, your system will scale
based on the actual load and activity of all of your tenants. If all the tenants are
offline, your infrastructure costs should be minimal. The key concept here is that
pooled environments can adjust to tenant load dynamically and enable you to better
align tenant activity with resource consumption.
- **Simplified management and operations** – The pool
model of isolation gives you one view into all the tenants in a system. You can
manage, update, and deploy all of your tenants through a single experience that
touches all your tenants in the system. This makes most aspects of the management
and operations footprint simpler.
- **Innovation** – The agility that is enabled by the
pooled isolation model also tends to be core to enabling SaaS providers to innovate
at a faster pace. The more you move away from distributed management and the
complexity of the silo model, the more you’re free to focus on the features and
functions of your product.

### Cons

- **Noisy neighbor** – The more resources are shared, the
more chances there are for one tenant to impact the experience of another. For
example, any activity from one tenant that puts a heavy load on the system has the
potential to impact other tenants. A good multi-tenant architecture and design will
try to limit these impacts, but there’s always some chance of a noisy neighbor
condition impacting one or more of your tenants in a pooled isolation model.
- **Tenant cost tracking** – In a silo model, it’s much
easier to attribute consumption of a resource to a specific tenant. However, in a
pooled model, the attribution of resources consumption becomes more challenging.
Each SaaS provider should look for ways to instrument their systems and surface the
granular data needed to effectively associate consumption with individual tenants.
- **Increased scope of impact** – Sharing all resources
shared also introduces some operational risk. In the silo model, when one tenant has
a failure, the impact of that failure could likely be limited to that one tenant.
However, in a pooled environment, an outage will likely impact all the tenants in
your system, which can have a significant impact on your business. This usually
requires an even deeper commitment to building a resilient environment that can
identify, surface, and gracefully recover from failures.
- **Compliance pushback** – While there are measures you
can take to isolate your tenants in a pool model, the notion of sharing
infrastructure can create situations where you may be unwilling to run in this
model. This is especially true in environments with compliance or regulatory rules
for a domain impose strict constraints on the accessibility and isolation of
resources. Even in these cases, though, this might mean some portion of the system
will need to be siloed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html*

---

# The bridge model

While the silo and pool models have very distinct approaches to isolation, the
isolation landscape for many SaaS providers is less absolute. As you look at real
application problems and you decompose your systems into smaller services, you will
often discover that your solution will require a mix of the silo and pool models. This
mixed model is what we would refer to as the bridge model of isolation. The diagram in
Figure 18 provides an example of how the bridge model might be realized in a SaaS
solution.

*Figure 18: Bridge isolation model*
This diagram highlights how the bridge model enables you to combine the silo and
pool models. Here we have a monolithic architecture with classic web and application
tiers. The web tier, for this solution, is deployed in a pool model that is shared by
all tenants. While the web tier is shared, the underlying business logic and storage of
our application are actually deployed in a silo model where each tenant has its own
application tier and storage.

If the monolith was broken into microservices, each of the various microservices in
your system could leverage combinations of the silo and pool models. More detail on this
approach will follow in the description of specifics of applying silo and pool models
with different AWS constructs. The key takeaway here is that your view of the silo and
pool models will be much more granular for environments that are decomposed into a
collection of services that have varying isolation requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/bridge-model.html*

---

# Tier-based isolation

While most of our discussion of isolation focuses on the mechanics of preventing
cross-tenant access, there are also scenarios where the tiering of your offering might
influence your isolation strategy. In this case, it’s less about how you’re isolating
tenants and more about how you might package and offer different flavors of isolation to
different tenants with different profiles. Still, this is another consideration that
could determine which models of isolation you’ll need to support to address the full
spectrum of customers you want to engage. The diagram in Figure 19 provides an example
of how isolation might vary across tiers.

The below example uses a mix of silo and pool isolation models that have been
offered up as tiers to the tenants. Tenants in the Silver tier are running in the pooled
environment. While these tenants are running in a shared infrastructure model, they
still fully expect that their resources will be protected from any cross-tenant access.
The tenant on the right has required that a completely dedicated (silo) environment be
offered. To support this, the SaaS provider has created a Premium tier model that
enables tenants to run in this dedicated model likely at a substantially higher price
point.

While SaaS providers generally try to limit offering a silo model to their
customers, many SaaS businesses have this notion of a private pricing where these
tenants offer to pay a premium to be deployed in this model. In fact, SaaS companies
will not publish this as an option or identify it as a tier to limit the number of
customers that chose this option. If too many of your tenants fall into this model,
you’ll begin to fall back to a fully siloed model and inherit many of the challenges
that are outlined previously.

*Figure 19: Tier-based isolation*
To limit the impact of these one-off environments, SaaS providers will often
require these premium customers to run the same version of the product that is deployed
to the pooled environment. This enables the ISV to continue to manage and operate both
environments through a single pane of glass. Essentially, the silo environment becomes a
clone of the pooled environment that happens to be supporting one tenant.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tier-based-isolation.html*

---

# Targeted isolation

It’s important to note that the isolation choices in your system can be quite
granular. Each microservice of your system and each resource those services touch has
the option of being configured with a different model of isolation. Let’s look at some
sample microservices to better understand how you might vary the isolation model across
a varying microservices. The diagram in Figure 20 provides a view of microservices that
use both the silo and pool models of isolation.

In this diagram, you’ll see a system that has implemented three different
microservices: product, order, and account. The deployment and storage models of each of
these microservices highlights how isolation (for security or noisy neighbor) could land
in a SaaS environment.

Let’s review the isolation model for each of these services. The Product
microservice at the top right was deployed in a complete pooled model where both the
compute and the storage are shared for all tenants. The table here reflects that tenants
all land here as separate items that are indexed in the same table. The assumption is
that the data will be isolated with policies that can restrict access to tenant items in
this table. The Order microservice is only for tenants 1 through 3 and also implemented
in a pooled model. The only difference here is that it’s supporting a subset of tenants.
Essentially, any tenant that doesn’t get a dedicated (silo) deployment of the Order
microservice would be running in this pooled deployment (think of it as tenants 1..N
with the exception of the few that get pulled out as silo microservices).

For the purposes of this discussion, let’s focus on the siloed services which are
represented by the dedicated *order* microservices (top right) and
the Account microservice (bottom). You’ll notice that we’ve deployed standalone
instances of the Order microservice for tenants 4 and 5. The idea here is that these
tenants had some requirements for the order processing (compliance, noisy neighbor,
etc.) that required this service to be deployed in a silo model. Here the compute and
storage are both dedicated entirely to each of these tenants.

Finally, at the bottom is the Account microservice which represents a silo model
but only at the storage level. The compute of the microservice is shared by all tenants
but each tenant has a dedicated *database* that holds its account
data. In this scenario, the isolation concern is focused exclusively on separating the
data. The compute is still enabled to be shared.

*Figure 20: Targeted isolation*
This model shows how the silo discussion becomes much more granular. Security,
noisy neighbor, and a variety of factors will determine how and when you might adopt a
silo isolation model for your services. The key takeaway here is that the silo model is
not an all-or-nothing decision. You can think about applying the silo model to specific
components of your application and only absorb this model’s challenges where it’s
actually needed, such as when a potential customer demands its use. In this case, a more
detailed discussion with the customer, you find out that there are only a few specific
areas of storage and processing that are of concern. Doing so will enable you to get the
efficiencies of the pool model for those parts of the system that do not require silo
isolation and also give you the flexibility to offer a tiered structure to support a mix of
both silo and pool models for individual services.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/targeted-isolation.html*

---

# Data protection

There are no security practices unique to SaaS applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/data-protection.html*

---

# Incident response

There are no security practices unique to SaaS applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/incident-response.html*

---

# Resources

Refer to the following resources to learn more about our best
practices for security.

**Documentation and blogs**

- [Isolating
SaaS Tenants with Dynamically Generated IAM Policies](https://aws.amazon.com/blogs/apn/isolating-saas-tenants-with-dynamically-generated-iam-policies/)
- [Partitioning
Pooled Multi-Tenant SaaS Data with Amazon DynamoDB](https://aws.amazon.com/blogs/apn/partitioning-pooled-multi-tenant-saas-data-with-amazon-dynamodb/)
- [Multi-tenant
data isolation with PostgreSQL Row Level Security](https://aws.amazon.com/blogs/database/multi-tenant-data-isolation-with-postgresql-row-level-security/)
- [Identity
Federation and SSO for SaaS on AWS](https://aws.amazon.com/blogs/apn/identity-federation-and-sso-for-saas-on-aws/)
- [Managing
SaaS Identity Through Custom Attributes and Amazon Cognito](https://aws.amazon.com/blogs/apn/managing-saas-identity-through-custom-attributes-and-amazon-cognito/)
- [Onboarding
and Managing Agents in a SaaS Solution](https://aws.amazon.com/blogs/apn/onboarding-and-managing-agents-in-a-saas-solution/)
- [Amazon Cognito API Reference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AddCustomAttributes.html)
- [Building
Serverless SaaS with Lambda layers](https://github.com/aws-samples/aws-serverless-saas-layers) (GitHub)
- [Modeling
SaaS Tenant Profiles on AWS](https://aws.amazon.com/blogs/apn/modeling-saas-tenant-profiles-on-aws/)

**Whitepapers**

- [SaaS
Tenant Isolation Strategies whitepaper](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html)
- [SaaS
Storage Strategies whitepaper](https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/multi-tenant-saas-storage-strategies.html)

**Videos**

- [AWS
re:Invent 2017: SaaS and OpenID Connect: The Secret Sauce of
Multi-Tenant Identity](https://youtu.be/jnFZGX2_T9U)
- [AWS
re:Invent 2016: The Secret to SaaS (Hint: It's
Identity)](https://www.youtube.com/watch?v=mi2whB6rIlw&list=PL4gOMYuwtVJsOA06mbpSuF6NxXersZWCB&index=6&t=10s)
- [AWS
re:Invent 2019: SaaS tenant isolation patterns](https://www.youtube.com/watch?v=fuDZq-EspNA)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/resources-1.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
