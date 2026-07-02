# GAMEOPS05 — Load testing

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# GAMEOPS05-BP01 Choose the right stage, architecture, and load testing framework to meet your goals

The approach to load testing a game can vary significantly
depending on many factors, including the stage of the development
process it is performed in, the architecture of the
load-generating system itself, and the choice of load testing
framework. The timing of when it is conducted, whether in the
early phases, during iterative sprints, prior to production
deployment, or post-deployment, will shape the goals and focus of
the testing efforts. Different designs of load-generating
infrastructure have their own pros and cons, and the selection of
the load testing framework greatly influences the capabilities,
ease of use, and integrations available for the testing process.
By thoughtfully aligning these elements, development teams can
tailor the load testing approach to the unique characteristics of
the game, extract the most valuable performance insights, and
provide a smooth experience for their players.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Load testing in different development
stages**

Conducting exploratory load testing early in the development
phases can validate the underlying system architecture. This
assists developers to make informed decisions about the game's
infrastructure, database design, and network topology before
extensive implementation work is done. Load tests identify risks
and create a performance baseline, potentially minimizing the need
for costly rework and technical debt later in the development
lifecycle. They can also foster a shared understanding of the
game's performance requirements among the team, leading to
better collaboration and decision-making. Ultimately, load testing
during the initial phases builds a strong foundation for a
high-performing, scalable, and resilient game, helping enhance the
overall player experience.

At the end of each sprint or iteration, load testing can evaluate
the performance impact of the new features, bug fixes, and other
changes introduced in the latest cycle. This targeted approach
allows development teams to quickly identify regressions or
performance degradations introduced by the latest updates,
enabling them to address these issues before they are propagated
further down the pipeline and maintaining a consistent level of
quality and performance.

Before deploying to production, robust load testing assists
teams validate the system's ability to handle the anticipated
real-world traffic and load conditions. They can uncover
scalability bottlenecks or resource constraints within the
production infrastructure and provide the opportunity to optimize
the game's performance, creating a smooth and responsive user
experience from day one. The insights gained from pre-launch load
testing can mitigate launch-day risks and inform ongoing capacity
planning, which lays the foundation for the game's long-term
sustainability and scalability.

Load testing a game that is already live in production allows
teams to monitor the game's performance and identify performance
regressions or degradations that may occur over time. This enables
them to proactively address issues before they impact the player
experience and negatively affect user retention. Additionally,
load testing in production validates the effectiveness of
performance optimization efforts or infrastructure scaling that
has been implemented. This process provides a high-quality,
responsive, and scalable gaming experience for players even as the
game evolves and matures.

**Load-generating architectures**

The design of the load-generating architecture for game load
testing can take various forms, each with its own set of
advantages and considerations.

At the most basic level, self-managed
[Amazon EC2](https://aws.amazon.com/ec2/)
instances can be provisioned and configured to act as load
generators. With a control node and worker nodes approach, you can
set up multiple load-generating instances, each running their own
test script and overall managed by a single control instance. The
architecture can scale up and generate more load without
increasing complexity by spinning up additional worker nodes, but
this hands-on approach requires teams to handle the provisioning,
configuring, and managing of the underlying infrastructure.

For a more scalable and orchestrated approach, you can use
[Amazon EKS](https://aws.amazon.com/eks/)
Kubernetes clusters to manage and distribute the load testing
workload across a fleet of container-based load agents. Kubernetes
automatic scaling features can be used to handle the scaling of
the load-generating pods, while teams themselves configure and
manage the underlying EC2 instances in the cluster hosting the
pods.

Alternatively, the serverless nature of
[AWS Fargate](https://aws.amazon.com/fargate/) can speed up and simplify the load testing setup by
abstracting away the infrastructure management while still
providing the necessary scalability and flexibility. For hybrid
solutions where an on-premises, load-generating Kubernetes cluster
already exists but additional capacity might be needed,
[EKS
Anywhere](https://aws.amazon.com/eks/eks-anywhere/) can manage both clusters as one from the AWS Management Console.

You can also use
[AWS Lambda](https://aws.amazon.com/lambda/) functions depending on your requirements and goals.
Lambda functions are relatively straightforward to set up and
scale without the need to provision and manage additional
resources. They also allow the creation of more complex and
dynamic test scenarios due to deep integration with other AWS
services. However, Lambda functions do have limits on concurrent
functions and runtime (15 minutes), which may constrain the scale
and length of load testing that can be achieved. Cold start
latencies can also impact the accuracy of the results, and the
resource limitations of Lambda may not be suitable for highly
demanding load testing workloads.

Studios wishing to use a pre-built solution can use
[Distributed
Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/solution-overview.html). This solution uses the Amazon ECS on
AWS Fargate to deploy containers that can run simulations of tens
of thousands connected users. You can use this to quickly start
your load testing infrastructure in IAC fashion using AWS CloudFormation.

**Load testing frameworks**

No two load testing frameworks are built the same. Some have
intuitive graphical interfaces for test creation, while others are
entirely command line-based. One tool might be flexible and
performant but require time and effort to configure and manage,
and another might be serverless but limited in the tests it can
create and run. Some enjoy large communities and plenty of
tutorials while being unproven in the field, contrasting sharply
with others that might be battle-tested in production but lack
community support or documentation. Choose the framework that
strikes the right balance for you and your team. Some few popular
options are:

- **[Apache
JMeter](https://jmeter.apache.org/):** Popular Java-based, open-source load
testing framework due to its robust feature set and ease of
use. Its ability to simulate complex user scenarios, wide
range of supported protocols, comprehensive reporting, and
proven track record makes JMeter a reliable choice for load
testing.
- **[Locust](https://locust.io/):**
Modern, distributed load testing framework built on an
event-driven architecture, making it performant while
resource-efficient. Tests are written in Python, allowing
flexible testing scenarios that take advantage of thousands of
powerful third-party libraries, while remaining friendly and
simple to read.
- **[Grafana
K6](https://k6.io/):** Powerful load testing framework that
combines ease of use with advanced capabilities. Its support
for distributed load generation, flexible scripting, and
seamless integration with Grafana for data visualization make
Grafana K6 an attractive choice.
- **[Gatling](https://gatling.io/):**
Open-source load testing framework known for its performance
and scalability. Its Scala-based, domain-specific language
(DSL) allows developers to create concise, maintainable load
testing scripts, and its robust reporting and analysis
capabilities provide detailed insights of the system under
test.

### Implementation steps

- **Load testing stages:**
Conduct load testing at various development stages (early
development, sprints, pre-production, and post-deployment)
to validate system performance and identify issues.
- **Load-generating
architectures:** Choose appropriate load-generating
architectures (EC2, EKS, Fargate, or Lambda) based on
scalability needs, management preferences, and specific test
requirements.
- **Load testing frameworks:**
Select a load testing framework (like JMeter, Locust,
Grafana K6, or Gatling) that balances ease of use,
performance, flexibility, and community support to suit your
team's needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops05-bp01.html*

---
