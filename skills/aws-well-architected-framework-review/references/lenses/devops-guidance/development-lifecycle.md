# Development lifecycle

**Saga**: Development lifecycle  
**Best Practices**: 60

---

**Capability**: DL.ADS — Advanced deployment strategies

# [DL.ADS.1] Test deployments in pre-production environments

**Category:** FOUNDATIONAL

Progressively validate software changes across multiple environments, including
development (alpha) and testing (beta) before deploying into production. Additional staging
environments can be introduced as needed, such as staging (gamma). These additional
environments help to prevent the introduction of bugs in production environments, validates
backwards compatibility, and increases the confidence in the quality of the deployment.

Each non-production deployment serves as a gate, only allowing changes to progress to
the next stage after they pass all validations. Early issue detection and isolation prevent
propagation to later stages or production. A controlled deployment process includes
strategies to manage risk and support rollback if issues are identified during these test
deployments.

One-box testing can be used to test backward compatibility to ensure new code changes
coexist with and function properly with the existing code base. One-box refers to the
testing of changes in a single unit of deployment, such as a single container or instance,
which is configured to use production endpoints. This form of testing can be used to help
ensure the changes interact efficiently with production endpoints of other services. This
can be done by creating a dedicated staging environment for cross-service backward
compatibility (zeta) testing. Services deployed to the zeta stage interact exclusively with
production endpoints to identify potential integration issues before the code reaches the
production stage.

**Related information:**

- [What
is Continuous Integration?](https://aws.amazon.com/devops/continuous-integration/)
- [What
is Continuous Delivery?](https://aws.amazon.com/devops/continuous-delivery/)
- [Going
faster with continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery?did=ba_card&trk=ba_card)
- [Automating
safe, hands-off deployments: Test deployments in
pre-production environments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/#Test_deployments_in_pre-production_environments)
- [Amazon's
approach to high-availability deployment](https://youtu.be/bCgD2bX1LI4)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.1-test-deployments-in-pre-production-environments.html*

---

**Capability**: DL.ADS — Advanced deployment strategies

# [DL.ADS.2] Implement automatic rollbacks for failed deployments

**Category:** FOUNDATIONAL

Implement an automatic rollback strategy to enhance system
reliability and minimize service disruptions. The strategy
should be defined as a proactive measure in case of an
operational event, which prioritizes customer impact
mitigation even before identifying whether the new deployment
is the cause of the issue.

Rollback should be initiated based on alarms linked to key
metrics like fault rates, latency, CPU usage, memory usage,
disk usage, and log errors. Additionally, consider both the
service's overall health and instance-specific
metrics. Incorporate a waiting period after a deployment to
closely monitor the system. This allows time to identify
potential issues that might not be evident immediately,
especially when the system is under low load. Establish
methods to prevent deployments during higher-risk times or
when there are active system issues. This could include
blocking deployments during when high-severity aggregate
alarms are raised or during specific time windows.

The rollback process should include the redeployment of the last successful code
revision, artifact version, or container image, and should employ methods like rolling or
blue/green deployments, or [feature flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) for a swift
rollback with minimal disruption. Consider using the advanced deployment methods introduced
in this capability for more granular control over deployments. Rollback considerations
should not be limited to the latest deployments, but also account for latent changes that
may be the source of current issues. To handle these situations, provide the ability for
developers to select a specific previously deployed release for rollback.

After the rollback, depending on the specific issue being addressed, consider
proactively rolling back other environments that could potentially also be affected, even
if they aren't currently showing any customer impact. Alternatively, if the issue appears to
be environment-specific, wait for the pipeline to roll forward a new release that includes a
bug fix. These operational decisions should be supported by the ability to compare the
changes between the current release and the selected rollback release's deployment
artifacts, including source code changes and changes in library versions.

**Related information:**

- [Ensuring
rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)
- [My
CI/CD pipeline is my release captain: Easy and automatic
rollbacks](https://aws.amazon.com/builders-library/cicd-pipeline/#Easy_and_automatic_rollbacks)
- [Automating
safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/?did=ba_card&trk=ba_card)
- [Amazon's
approach to high-availability deployment: Rollback
alarms](https://youtu.be/bCgD2bX1LI4?t=1669)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.2-implement-automatic-rollbacks-for-failed-deployments.html*

---

**Capability**: DL.ADS — Advanced deployment strategies

# [DL.ADS.3] Use staggered deployment and release strategies

**Category:** FOUNDATIONAL

Staggered deployments strategies make use of techniques like
progressive wave-based deployments, one-box deployments, and
rolling deployments. These techniques contribute to safer and
more reliable software deployment and release processes.
Staggered deployments are beneficial as they balance the
safety of small-scoped deployments with the speed of
delivering changes to customers.

Progressive deployments, for instance, involve deploying changes to deployment
groups, or *waves*, of increasing size. This method helps to achieve a
balance between deployment risk and speed, promoting changes from wave to wave. The initial
waves build confidence in the change by starting with a low number of requests and then
gradually increasing.

Each production wave of the staggered deployment starts with a limited deployment,
one-box stage, where the new code is first deployed to a single unit called a
*box*. A box could be a single server or container instance which is
deployed to a specific environment, AWS Region, single AWS Availability Zone, or within
a single cell in a [cell-based architecture](https://aws.amazon.com/solutions/guidance/cell-based-architecture-on-aws/).
This approach minimizes the potential impact of changes by initially limiting the requests
served by the new code. The box should be served a fraction of canary tests while its
performance is being closely monitored before a broader rollout.

Following the limited deployment stage, rolling deployments are typically used to
deploy to the wave's main production fleet. This approach helps ensure that the service has
enough capacity to serve the production load throughout the deployment. A typical rolling
deployment to an environment replaces at most 33% of the system's fleet in that environment
with the new code. By maintaining at least 66% of the overall capacity healthy and serving
requests, the impact of changes is limited. If necessary, fast rollbacks can be implemented
where the system replaces 33% of the system's fleet with the previous code to speed up the
rollback process.

If you require more control over the release of the change,
consider using blue/green deployments rather than one-box and
rolling deployments. In a blue/green deployment, two identical
production environments are maintained, and the inactive
environment (either blue or green) is updated. Once fully
tested and ready, traffic is switched from the active to the
inactive environment, thus minimizing downtime and risk

These strategies reduce the risk of introducing issues into
the system and allow for monitoring, swift rollback, and issue
tracking. However, they require careful planning, thorough
testing, and detailed monitoring. Their benefits to system
reliability and resilience are substantial and are recommended
for any organization.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL08-BP04 Deploy
using immutable infrastructure](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.html)
- [Automating
safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/?did=ba_card&trk=ba_card)
- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/application-pipeline/)
- [Overview
of Deployment Options on AWS](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/welcome.html)
- [Deployment
methods](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html)
- [Using
Amazon RDS Blue/Green Deployments for database
updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html)
- [Amazon's
approach to high-availability deployment: Canary
deployments](https://youtu.be/bCgD2bX1LI4?t=1624)
- [Hands-off:
Automating continuous delivery pipelines at Amazon](https://www.youtube.com/watch?v=ngnMj1zbMPY)
- [The
Amazon Software Development Process: Pessimistic
Deployments](https://youtu.be/52SC80SFPOw?t=1024)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.3-use-staggered-deployment-and-release-strategies.html*

---

**Capability**: DL.ADS — Advanced deployment strategies

# [DL.ADS.4] Implement Incremental Feature Release Techniques

**Category:** RECOMMENDED

Incremental feature releases gradually roll out new features
to users, reducing risk and maintaining system stability.
Techniques include dark launching, two-phase deployments,
feature flags, and canary releases. These techniques enable
safe, controlled, and iterative changes to distributed systems
which reduces risk associated with concurrent updates and
maintaining system stability.

[Dark
launches](https://martinfowler.com/bliki/DarkLaunching.html) allow teams to integrate and test new features
in a live environment, without needing to make them visible to
the entire user base. This approach allows for monitoring and
analyzing the impact and performance of new features under
real-world conditions, while mitigating the risk of widespread
disruptions. Depending on system implementation and team
preferences, dark launches can be implemented using
versioning, A/B testing, canary releases, or most commonly,
using feature flags.

[Feature
flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) allow developers to turn on or off certain
features in their code base without affecting other
functionality. This allows for testing of new features with a
subset of users, limiting potential negative impacts. Feature
flags provide an additional layer of control over the feature
rollout process and can be used for A/B testing, canary
releases, and dark launches.

[Two-phase
deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments#Two-phase_deployment_technique) complement dark launching, focusing
primarily on managing read and write changes in a systematic
and phased manner. Changes should first be prepared to handle
a new update without actively implementing it (Prepare phase),
followed by a second deployment that activates the new changes
(Activate phase). This approach requires careful planning and
coordination, but pays off by prioritizing data integrity and
preventing stale records that could emerge from concurrent
changes.

The specific choice of technique, be it dark launching, two-phase deployments,
feature flags, canary releases, or a combination, depends on your unique needs, the nature
of the changes, the complexity of the system, and the degree of control required over the
release process. Each of these methods offers its own advantages, and their strategic
implementation can significantly enhance the resilience and efficiency of your
deployments.

**Related information:**

- [Amazon CloudWatch Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently)
- [Feature
Flags - AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [My
CI/CD pipeline is my release captain: Multiple inflight
releases](https://aws.amazon.com/builders-library/cicd-pipeline/#Multiple_inflight_releases)
- [Ensuring
rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)
- [Using
AWS AppConfig Feature Flags](https://aws.amazon.com/blogs/mt/using-aws-appconfig-feature-flags/)
- [The
Only Guide to Dark Launching You'll Ever Need](https://launchdarkly.com/blog/guide-to-dark-launching/)
- [Deployment
Pipeline Reference Architecture: Dynamic Configuration
Pipeline](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/dynamic-configuration-pipeline/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.4-implement-incremental-feature-release-techniques.html*

---

**Capability**: DL.ADS — Advanced deployment strategies

# [DL.ADS.5] Ensure backwards compatibility for data store and schema changes

**Category:** RECOMMENDED

Backwards compatibility in data stores and schemas ensures
that as changes are made, previous versions of the system
continue to operate as expected. This requires careful
planning, thorough testing, and detailed monitoring. As
modifications, additions, or deletions are made to data
structures and schemas, these changes should be designed to
coexist with previous data structures, allowing both old and
new versions to operate concurrently. Maintaining backwards
compatibility helps to avoid breaking changes that could
disrupt continuous integration and delivery pipelines.

One way to achieve backwards compatibility is by implementing
versioning in your data schemas. With this method, new changes
are incorporated into a new version, while older versions
remain functional for existing applications.
[Feature
flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) can also be used to conceal new alterations until
they're fully ready, facilitating testing and phased rollout
of updates without affecting existing users.

To ensure the safe implementation of these changes, they
should be thoroughly tested in a non-production
environment. Testing typically involves three stages to detect
potential issues: initially, the change is deployed to a
fraction of the servers to verify coexistence of software
versions; next, the deployment is completed across all
servers; and finally, a rollback deployment is initiated. If
no errors or unexpected behavior occur during these stages,
the test is considered successful.

In scenarios involving changes that require coordination between different
microservices, it is important to maintain consistency in the order of deployments across
environments. For example, in serialization contexts, readers are typically deployed
before writers during roll-forward, while writers precede readers during rollbacks.

**Related information:**

- [Ensuring
rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)
- [Using
Amazon RDS Blue/Green Deployments for database
updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.5-ensure-backwards-compatibility-for-data-store-and-schema-changes.html*

---

**Capability**: DL.ADS — Advanced deployment strategies

# [DL.ADS.6] Use cell-based architectures for granular deployment and release

**Category:** OPTIONAL

A cell-based architecture segments a larger system into isolated, independently
functioning replicas, or *cells*. These cells are smaller components of
the system that contain all application logic and storage. They have their own monitoring
and alerting systems, are automated for creation and update, and can be managed and scaled
individually. This approach offers advantages including scalability, fault isolation,
testing, and operational resilience.

A cell-based architecture is a natural fit for DevOps as it
enables small, frequent changes, reduces the risk from
problematic deployments, and enables rapid recovery. It allows
teams to deliver incremental updates to individual cells
without risking the entire system's stability.

Start by defining your cells, each of which should be a
complete, independently deployable unit of your system. You
should limit the maximum size of a cell and maintain this
consistency across different regions or installations. You
then need to establish a routing layer that redirects client
requests to the appropriate cell. You can store the routing
information, such as user-to-cell mapping, in a low-latency
database. Every cell should have its own monitoring and
alerting system.

You will need to automate the lifecycle of your cells, including initial deployment
and subsequent updates. A *canary cell* can be helpful in initial
deployment of updates and assessing their impact. Ensure that you implement a central
dashboard to provide an aggregated view of the state of your cells, enabling easy
system-wide monitoring. Stream changes to a central data lake for centralized querying and
analysis of changes across all cells. Finally, implement an operational tool to move users
between cells and create new cells as needed. This step optimizes load distribution across
cells by updating the user-to-cell assignment.

Cell-based architectures are optional. While beneficial for
complex systems, smaller systems might not require such
architectural complexity.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL10-BP04 Use
bulkhead architectures to limit scope of impact](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_use_bulkhead.html)
- [Guidance
for Cell-based Architecture on AWS](https://aws.amazon.com/solutions/guidance/cell-based-architecture-on-aws/)
- [Minimizing
correlated failures in distributed systems](https://aws.amazon.com/builders-library/minimizing-correlated-failures-in-distributed-systems#Noninfrastructure_causes_of_correlated_failures)
- [Journey
to cell-based microservices architecture on AWS for
hyperscale](https://www.youtube.com/watch?v=ReRrhU-yRjg)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.6-utilize-cell-based-architectures-for-granular-deployment-and-release.html*

---

**Capability**: DL.CD — Continuous delivery

# [DL.CD.1] Deploy changes to production frequently

**Category:** FOUNDATIONAL

Frequent deployments to production encourages small, rapid, and iterative changes to
the code base. Deploying small and validated changes regularly helps mitigate the risk
associated with each deployment. Frequent deployments not only streamlines the testing and
validation process, but also expedites the feedback loop, leading to quicker resolution of
issues.

Use a pipeline to automate the deployment of validated changes across various
environments, including production. This pipeline should be automatically triggered, such as
by the completion of continuous integration or an updated artifact in an artifact
repository. Once invoked, the pipeline should automatically begin to deploy changes to
non-production environments for further testing and validation. Upon successful validation,
changes can be deployed to the production environment.

When working in a DevOps environment, it is important to distinguish between
*deploying* and *releasing*. Even after deploying
changes to production, these changes might not necessarily be visible or accessible to all
users. By using advanced deployment strategies and employing [feature flags](https://aws.amazon.com/systems-manager/features/appconfig/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc#Feature_flags), teams can deploy code to production and decide when to release or
rollback specific features in real time, offering more granular control over releasing new
features to end users.

Teams should focus on deploying small changes rather than
bundling multiple changes into a single, large batch
deployment. Accumulating changes complicates testing and
validation, and it becomes challenging to ensure that all
components interact correctly. The practice of deploying small
changes demands discipline and commitment, but it improves
deployment frequency, security, and enhanced collaboration
while ensuring that the code base remains up-to-date and
releasable at all times.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.1-deploy-changes-to-production-frequently.html*

---

**Capability**: DL.CD — Continuous delivery

# [DL.CD.2] Deploy exclusively from trusted artifact repositories

**Category:** FOUNDATIONAL

All artifacts involved in the delivery process should
originate from a trusted artifact repository. These
repositories contain validated, tested, and integrated
artifacts that have been deemed safe for deployment. By using
trusted artifact repositories, teams can ensure the security
of deployed workloads, maintain quality and security
standards, and promote trust in the delivery pipeline.

The delivery pipeline should be restricted to using only
trusted artifact repositories, which could be enforced through
mechanisms such as allow lists, IP restrictions, or
authentication controls. Additionally, we recommend using
cryptographic signing to validate artifacts and including a
validation stage in the pipeline to verify that the artifacts
meet the necessary standards before deployment. In this way,
the integrity and security of the deployed workloads are
maintained consistently.

**Related information:**

- [Artifact
Repository - AWS CodeArtifact](https://aws.amazon.com/codeartifact/)
- [Fully
Managed Container Registry - Amazon Elastic Container Registry](https://aws.amazon.com/ecr/)
- [Code
Repositories and Artifact Management | AWS Marketplace](https://aws.amazon.com/marketplace/solutions/devops/code-repositories-and-artifact-management?aws-marketplace-cards.sort-by=item.additionalFields.headline&aws-marketplace-cards.sort-order=asc&awsf.aws-marketplace-devops-store-use-cases=*all)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.2-deploy-exclusively-from-trusted-artifact-repositories.html*

---

**Capability**: DL.CD — Continuous delivery

# [DL.CD.3] Integrate quality assurance into deployments

**Category:** FOUNDATIONAL

Integrating quality assurance (QA) processes into continuous delivery pipelines tests
that the whole system is ready for release. This differs from previous quality checks in the
development lifecycle as these tests validate that the software changes behave as expected
when deployed into real-world environments. This provides the ability to test integration
with other live systems, check for configuration errors, and test in environments that more
closely mirror production.

Incorporate QA stages into your delivery pipeline to
automatically conduct required functional, non-functional,
security, and data tests after deployments occur. Deployments
to environments is the ideal enforcement point for quality
assurance, with QA requirements being scoped to the
environment being deployed to. If a test fails for one
environment, it is a signal that deployment to subsequent
environments might carry the same risk. Provide immediate
feedback to the development team upon any test failures, so
they can rectify issues quickly and maintain the integrity of
the deployment pipeline.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL08-BP02 Integrate
functional testing as part of your deployment](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_functional_testing.html)
- [AWS Well-Architected Reliability Pillar: REL08-BP03 Integrate
resiliency testing as part of your deployment](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_resiliency_testing.html)
- [AWS Well-Architected Security Pillar: SEC11-BP02 Automate
testing throughout the development and release lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_automate_testing_throughout_lifecycle.html)
- [Testing
stages in continuous integration and continuous
delivery](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/testing-stages-in-continuous-integration-and-continuous-delivery.html)
- [Amazon's
approach to high-availability deployment: Release guidance
lifecycle](https://youtu.be/bCgD2bX1LI4?t=855)
- [Testing
software and systems at Amazon: Continuous integration and
deployment](https://youtu.be/o1sc3cK9bMU?t=1206)
- [The
Amazon Software Development Process: Automated
Testing](https://youtu.be/52SC80SFPOw?t=1340)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.3-integrate-quality-assurance-into-deployments.html*

---

**Capability**: DL.CD — Continuous delivery

# [DL.CD.4] Automate the entire deployment process

**Category:** FOUNDATIONAL

Automate as many stages of the delivery process as possible. Exceptions for
continuous delivery might include optional manual approval gates. Automation reduces the
risk of human error, brings consistency to deployments, and accelerates the delivery
process.

Use the delivery pipeline to automate every stage of deploying changes, from copying
the build artifact to setting up any required configurations. While optional manual approval
gates can exist, all other stages should be automated, maintaining the integrity of the
artifact and reducing the likelihood of errors. Humans should not have access to the target
environments or have the ability to inject code, parameters, configuration, or interfere
with the integrity of the artifact in any way.

Some organizations might still require manual oversight at certain stages as they
evolve their DevOps capabilities. If the organization is early in its DevOps adoption or
operates in a highly regulated environment, there might be a need for manual interventions
or approvals at certain stages. These could be due to governance or regulatory requirements
or simply the need for a human decision at a critical point in the deployment process. Over
time, even for these organizations, the goal should be to have no manual deployment stages
in the deployment of changes.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL08-BP05 Deploy
changes with automation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_automated_changemgmt.html)
- [AWS Well-Architected Security Pillar: SEC11-BP06 Deploy
software programmatically](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_deploy_software_programmatically.html)
- [What
is Continuous Delivery?](https://aws.amazon.com/devops/continuous-delivery/)
- [Amazon CodeCatalyst](https://codecatalyst.aws/explore)
- [Building
the pipeline](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/building-the-pipeline.html)
- [Going
faster with continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery/)
- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture)
- [Deploy
container applications in a multicloud environment using
Amazon CodeCatalyst](https://aws.amazon.com/blogs/devops/deploy-container-applications-in-a-multicloud-environment-using-amazon-codecatalyst/)
- [Amazon's
approach to high-availability deployment: Release guidance
lifecycle](https://youtu.be/bCgD2bX1LI4?t=855)
- [Testing
software and systems at Amazon: Continuous integration and
deployment](https://youtu.be/o1sc3cK9bMU?t=1206)
- [The
Amazon Software Development Process: Continuous
Delivery](https://youtu.be/52SC80SFPOw?t=814)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.4-automate-the-entire-deployment-process.html*

---

**Capability**: DL.CD — Continuous delivery

# [DL.CD.5] Ensure on-demand deployment capabilities

**Category:** FOUNDATIONAL

Continuous delivery relies on the ability to ensure that every change is considered
deliverable and can be deployed to production environments at any time. While the actual
decision to deploy to production may still be manual, deployments should be able to occur
on-demand as needed.

Deployments should be able to occur during normal working
hours without causing significant downtime or disruption to
the business. Changes should not require synchronization with
other systems and deployments should be able to occur
regardless of the interdependence of other systems. By
decoupling deployments from other systems and being able to
perform them during normal business hours, teams can receive
fast feedback and respond to any issues that arise, leading to
quicker fixes and less disruption to users.

To enable on-demand deployments, teams should employ advanced deployment strategies,
such as blue/green deployments, canary releases, feature flags, or rolling updates. The
ability to gradually roll out changes, coupled with modern application architectures and
integrated QA processes, enables iterative delivery. Iterative delivery reduces the impact
of potential issues throughout the deployment and allows for quick rollback if necessary. By
using the right tools and strategies, deployments can be automated and run seamlessly,
allowing for faster and more efficient delivery of applications and services.

**Related information:**

- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.5-ensure-on-demand-deployment-capabilities.html*

---

**Capability**: DL.CD — Continuous delivery

# [DL.CD.6] Refine delivery pipelines using metrics for continuous improvement

**Category:** RECOMMENDED

Use key metrics—whether sourced from this guidance, established frameworks
like [DORA](https://dora.dev/) or [SPACE](https://queue.acm.org/detail.cfm?id=3454124), or custom to your
organization—to continually optimize the development lifecycle. Metrics such as deployment
frequency, change lead time, failure rate, and time to recover serve as outcome-based
lagging indicators. These indicators span many DevOps capabilities to provide insights
into the efficiency and reliability of the full delivery process. While individual metrics
offer granular insights to optimize specific continuous delivery capabilities, these
aggregated metrics present a holistic overview of the end-to-end development
lifecycle. Both granular and holistic metrics are important for continuous improvement.

Use observability practices to continuously monitor the
development lifecycle, including incorporating monitoring and
logging into your delivery pipelines. Use logs to generate
metrics, and use these metrics to identify areas for
improvement. Make these metrics visible to all team members
and use them to drive your continuous improvement efforts.

Putting an emphasis on continually optimizing pipelines using
metrics is recommended. When getting started with DevOps
adoption, initial efforts should prioritize the establishment
of a stable and effective delivery pipeline, with subsequent
enhancements to the pipeline being driven by metrics.

**Related information:**

- [Deployment
Pipeline Reference Architecture](https://pipelines.devops.aws.dev/application-pipeline/)
- [AWS Observability Best Practices: Key Performance
Indicators](https://aws-observability.github.io/observability-best-practices/guides/operational/business/key-performance-indicators/)
- [DevOps Research and
Assessment (DORA)](https://dora.dev/)
- [SPACE](https://queue.acm.org/detail.cfm?id=3454124)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.6-refine-delivery-pipelines-using-metrics-for-continuous-improvement.html*

---

**Capability**: DL.CD — Continuous delivery

# [DL.CD.7] Remove manual approvals to practice continuous deployment

**Category:** OPTIONAL

Fully automate all stages of the deployment process, allowing developers to push new
code into the production environment using fully automated delivery pipelines—with no
manual approval stages required. This is referred to as continuous deployment. Removing
all manual deployment steps reduces potential errors and increases deployment speed. It
allows developers to focus more on coding and less on deployment logistics, improving
efficiency and productivity.

Create fully automated pipelines which perform continuous
integration and continuous deployment. A pipeline should
trigger upon code changes being merged into the main release
branch. This pipeline should perform all necessary quality
assurance tests, build the application, and deploy the new
version to the production environment. Automated governance
capabilities ensure that guardrails are being followed, while
observability functions such as alerts and logs provide
visibility.

This level of automation is a hallmark of mature DevOps
practices. However, it is an optional capability as it is not
always achievable or desired, especially in heavily regulated
industries or in organizations with strict governance
controls.

**Related information:**

- [Continuous
Delivery vs. Continuous Deployment](https://aws.amazon.com/devops/continuous-delivery/)
- [Practicing
Continuous Integration and Continuous Delivery on
AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/implementing-continuous-integration-and-continuous-delivery.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.7-remove-manual-approvals-to-practice-continuous-deployment.html*

---

**Capability**: DL.CI — Continuous integration

# [DL.CI.1] Integrate code changes regularly and frequently

**Category:** FOUNDATIONAL

Working in small batches, characterized by regular, small changes to a code base,
enhances software delivery performance. It reduces the time to receive feedback on changes,
which is required to enable continuous integration. This way of working is an improvement
over traditional phased development approaches, which often leads to delayed feedback due to
large batches of work. By making smaller, more frequent changes, teams can uncover and fix
bugs earlier in the development lifecycle, simplifying the process of updating, testing, and
releasing software.

Features should be broken down into independent work units
that align with the agile
[INVEST](https://www.agilealliance.org/glossary/invest/)
checklist. Splitting features into small increments of value,
ramping up the frequency of deployment, and practicing Test
Driven Development (TDD) all contribute to ensuring small
batch sizes. Developers should strive to integrate multiple
small, releasable changes to the code base at least once per
day. Techniques like
[dark
launching](https://martinfowler.com/bliki/DarkLaunching.html), [branch
by abstraction](https://trunkbaseddevelopment.com/branch-by-abstraction/), and
[feature
flags](https://aws.amazon.com/systems-manager/features/appconfig/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc#Feature_flags) allow incomplete features to be integrated in a
reversible way without impacting end users.

Working in small batches requires discipline and commitment,
but leads to improvements in speed, security, collaboration,
and code base consistency. In mature teams, developers commit
changes multiple times per day and merge code frequently to
prevent accumulating large changes. These teams yield better
collaboration and success in maintaining an up-to-date,
releasable version of the code base.

**Related information:**

- [What
is continuous integration and continuous
delivery/deployment?](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/what-is-continuous-integration-and-continuous-deliverydeployment.html)
- [What
does INVEST Stand For?](https://www.agilealliance.org/glossary/invest/)
- [Testing
software and systems at Amazon: Continuous Integration and
Deployment](https://youtu.be/o1sc3cK9bMU?t=1313)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.1-integrate-code-changes-regularly-and-frequently.html*

---

**Capability**: DL.CI — Continuous integration

# [DL.CI.2] Trigger builds automatically upon source code modifications

**Category:** FOUNDATIONAL

Continuous integration (CI) tools should be configured to
regularly monitor the source code repository for any changes.
Alternatively, set up the source code repository to send an
event upon each commit. This implementation creates an
environment where developers can focus on coding and commit
their changes, leaving the system to handle building, testing,
and deploying the application.

Having this process in place aligns with the continuous integration principle of
*failing fast*. It offers immediate feedback on the impact of changes,
whether they cause a minor regression or a major bug, allowing for prompt correction. If a
build fails, it becomes immediately visible to the team. Fixing a broken build is then
prioritized, fostering a culture of discipline and continuous improvement. This approach
minimizes the risk of integration conflicts and bugs while reducing the likelihood of
unexpected outcomes that can arise from manual processes or irregular updates. It also
streamlines the development process, promotes productivity, and contributes to delivering a
higher-quality outcome.

**Related information:**

- [Amazon CodeCatalyst](https://codecatalyst.aws/explore)
- [Building
the pipeline](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/building-the-pipeline.html)
- [Deploy
container applications in a multicloud environment using
Amazon CodeCatalyst](https://aws.amazon.com/blogs/devops/deploy-container-applications-in-a-multicloud-environment-using-amazon-codecatalyst/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.2-trigger-builds-automatically-upon-source-code-modifications.html*

---

**Capability**: DL.CI — Continuous integration

# [DL.CI.3] Ensure automated quality assurance for every build

**Category:** FOUNDATIONAL

As code changes become more frequent in a DevOps environment,
it becomes important to reduce the time it takes to get
feedback on those changes. Adding automated quality assurance
(QA) tests into the continuous integration pipeline enables
rapidly validating changes and receiving fast feedback.

Add stages to the pipeline which run pre-deployment checks to
validate that code changes work alongside the existing code
base. These checks should automatically trigger functional,
non-functional, and security tests against the integrated code
base and build artifacts.

*Breaking-the-build*, which stops the integration pipeline process
due to test failures, is a powerful feedback mechanism. However, it should be used
judiciously. Reserve breaking-the-build for critical issues, such as actual build failures,
high severity security findings, or non-negotiable compliance findings, that demand
immediate developer attention. Overuse can disrupt the continuous flow of development,
leading to unforeseen delays, bottlenecks, and poor developer experience.  Instead, continue
to provide feedback to developers in tools they already use, such as IDEs, chat clients, or
email, and let them decide if they should stop the process.

It is often more practical to automate enforcement of quality
assurance findings as part of the continuous delivery process.
This allows enforcement to be objectively targeted based on
the environment to which the build is being deployed into.
Have an exception mechanism and escalation plans prepared that
developers can use if the continuous integration or continuous
deployment prevent deployments which they do not agree with.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL08-BP02 Integrate
functional testing as part of your deployment](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_functional_testing.html)
- [AWS Well-Architected Security Pillar: SEC11-BP02 Automate
testing throughout the development and release lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_automate_testing_throughout_lifecycle.html)
- [Testing
stages in continuous integration and continuous
delivery](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/testing-stages-in-continuous-integration-and-continuous-delivery.html)
- [Amazon's
approach to high-availability deployment: Release guidance
lifecycle](https://youtu.be/bCgD2bX1LI4?t=855)
- [Testing
software and systems at Amazon: Continuous integration and
deployment](https://youtu.be/o1sc3cK9bMU?t=1206)
- [The
Amazon Software Development Process: Automated
Testing](https://youtu.be/52SC80SFPOw?t=1340)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.3-ensure-automated-quality-assurance-for-every-build.html*

---

**Capability**: DL.CI — Continuous integration

# [DL.CI.4] Provide consistent, actionable feedback to developers

**Category:** FOUNDATIONAL

To identify and address issues as quickly as possible, it's important that developers
receive consistent and actionable feedback, regardless of the technologies and tools being
used. This consistency streamlines the process of addressing failures across diverse
development environments, contributing to more efficient DevOps practices. Implement this by
configuring your CI pipeline to send automatic failure notifications, offering clear,
actionable resolution guidance.

Any failures in the process should send feedback to the
developer automatically, describing the failure clearly with
actionable guidance for resolution. Feedback mechanisms should
be tailored to fit within tools already used by developers,
such as IDEs, chat clients, or email, reducing the learning
curve and aiding early problem detection.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.4-provide-consistent-actionable-feedback-to-developers.html*

---

**Capability**: DL.CI — Continuous integration

# [DL.CI.5] Sequence build actions strategically for prompt feedback

**Category:** RECOMMENDED

By optimizing the sequence of actions or tasks in your
continuous integration pipeline, feedback can be timely,
allowing developers to quickly react and make necessary
changes. This practice reduces the risk of delayed releases
due to late detection of issues.

Initiate long-duration actions earlier and run them in
parallel with other actions, preventing bottlenecks. Tasks
less prone to failure or of lower importance should be
scheduled later to prioritize higher impact tasks. Regularly
reviewing and adjusting action sequences ensures they
effectively identify issues early and provide actionable
feedback.

Strategically sequencing build actions is categorized as
recommended as the foundational focus should first be on
establishing a solid continuous integration pipeline and then
later enhancing it by optimizing the build.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.5-sequence-build-actions-strategically-for-prompt-feedback.html*

---

**Capability**: DL.CI — Continuous integration

# [DL.CI.6] Refine integration pipelines with build metrics

**Category:** RECOMMENDED

Use key metrics—whether sourced from this guidance, established frameworks
like [DORA](https://dora.dev/) or [SPACE](https://queue.acm.org/detail.cfm?id=3454124), or custom to your
organization—to optimize your continuous integration process. Metrics such as deployment
frequency, change lead time, failure rate, and time to recover serve as outcome-based
lagging indicators. These indicators span many DevOps capabilities to provide insights
into the efficiency and reliability of the full delivery process. While individual metrics
offer granular insights to optimize specific continuous integration capabilities, these
aggregated metrics present a holistic overview of the end-to-end development lifecycle.
Both granular and holistic metrics are important for continuous improvement.

Embed observability practices into your integration pipelines,
incorporating monitoring and logging observability
capabilities. By transforming logs into metrics, you gain
actionable insights into areas needing refinement. Prioritize
making these metrics accessible to all team members to create
an environment where teams can proactively monitor, analyze,
and improve based on these metrics.

Putting an emphasis on continually optimizing pipelines using
metrics is recommended. When getting started with DevOps
adoption, initial efforts should prioritize the establishment
of a stable and effective integration pipeline, with
subsequent enhancements to the pipeline being driven by
metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.6-refine-integration-pipelines-with-build-metrics.html*

---

**Capability**: DL.CI — Continuous integration

# [DL.CI.7] Validate the reproducibility of builds

**Category:** OPTIONAL

Every build for a specific version of source code should
ideally be able to generate the same outputs from the same
inputs. The implementation of reproducible builds primarily
involves the creation of an immutable and consistently created
build environment and controlling the inputs for each and
every build.

Between each build, the environment should be destroyed and recreated so that it is
immutable. Use infrastructure as code (IaC) and containerization to help with automating
the creation of the environment in a repeatable and consistent way. Have controls in place
to detect and prevent configuration drift that may alter the build environment
post-creation. All dependencies and software components used to create the environment and
perform the build should be version pinned and recorded.

Any manual intervention during the build can introduce
variability. Every step in the build process needs to be
automated. Factors that can render the build nondeterministic,
such as unrestricted network access and the use of random
generators or timestamps that modify the build artifact, must
be limited.

Verify the reproducibility by establishing processes that
regularly check the reproducibility of the builds. This can
involve triggering builds from the same source code in
different environments and comparing the results. Adopt
mechanisms like binary diffing or checksum comparison to
validate the reproducibility of the build. Set up alarms that
raise alerts when discrepancies occur to provide fast feedback
when there are inconsistencies.

Having reproducible builds is optional and not recommended for
all organizations or workloads. While striving for
reproducibility is encouraged, it may not be achievable in
every context. For example, some builds may depend on specific
environmental parameters or timing elements that make
reproducibility difficult.

**Related information:**

- [Reproducible
builds](https://reproducible-builds.org/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.7-validate-the-reproducibility-of-builds.html*

---

**Capability**: DL.CR — Code review

# [DL.CR.1] Standardize coding practices

**Category:** FOUNDATIONAL

Coding standards promote uniformity and consistency across the organization.
Individual teams can also extend this standard to adopt specific practices that align with
the team's preferences. Having standards not only helps ensure consistency across
distributed teams, but can also make code reviews more efficient, support knowledge sharing,
and lead to faster issue resolution.

Identify or develop coding standards that align with the primary programming
languages used across the organization. This does not mean that other languages cannot be
used, but does lead to a structured approach to development for new teams and new employees.
The coding standards are meant to facilitate error detection, improve code readability,
simplify maintenance, and enhance the overall efficiency of builders, not prevent
innovation.

These standards can be codified into linters and code quality tools to improve
developer experience. This approach provides fast feedback to developers and evaluate their
adherence to the standards automatically. Hold training sessions for developers on these
standards, store them in centralized knowledge sharing spaces, and create mechanisms to
gather feedback to continuously improve the standard over time. We recommend getting started
by adopting industry-specific standards, such as the [Secure Coding
Guidelines for Java SE](https://www.oracle.com/java/technologies/javase/seccodeguide.html), [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for Git,
or the [PEP8](https://pypi.org/project/pep8/) styling guide for Python.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.1-standardize-coding-practices.html*

---

**Capability**: DL.CR — Code review

# [DL.CR.2] Perform peer review for code changes

**Category:** FOUNDATIONAL

A peer review process for code changes is a strategy for
ensuring code quality and shared responsibility. To support
separation of duties in a DevOps environment, every change
should be reviewed and approved by at least one other person
before merging. Once approved, a pipeline with sufficient
access will deploy the change.

Most version control systems support protection rules
enforcing certain workflows, like requiring at least one peer
review, before merging into designated branches. Use these
rules to enforce this workflow and provide assurance that all
code changes adhere to this mandatory review process.

Incorporating [pair
programming](https://www.agilealliance.org/glossary/pair-programming/), where two programmers collaboratively work side-by-side or through
screen sharing, is method of peer review. By integrating this approach, reviews can be
integrated into the development lifecycle earlier—while the code is being written, reducing
the time taken to identify and fix issues. This accelerates review timelines, reduces the
introduction of bugs or issues, promotes knowledge sharing, and creates a culture
of quality and continuous improvement.

Some companies require multiple reviewers, or require more
proof than just pair-programming to adhere to compliance
requirements. Pick a code review process that works for your
organization, and enforce it through policies, processes, and
technology.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC11-BP04 Manual code
reviews](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_manual_code_reviews.html)
- [Team
Collaboration with Amazon CodeCatalyst](https://aws.amazon.com/blogs/devops/team-collaboration-with-amazon-codecatalyst/)
- [Code
review](https://en.wikipedia.org/wiki/Code_review)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.2-perform-peer-review-for-code-changes.html*

---

**Capability**: DL.CR — Code review

# [DL.CR.3] Establish clear completion criteria for code tasks

**Category:** FOUNDATIONAL

A clear definition of done ensures that developers understand
the requirements of their task, can consistently meet those
requirements, and that reviewers have a sense of what they are
reviewing. It provides the team with shared clarity of purpose
for each change that they will be making to the code base.

To implement a clear definition of done, initiate discussions among all team members
during the design phase to identify and agree on the criteria that should be included.  The
done criteria should include the types of testing that need to be done (like functional,
non-functional, or security tests), any required documentation (like code comments or user
manuals), and the standards the code needs to meet (such as performance, availability, or
team style guides).

Once these criteria are defined and agreed upon, document them, and make this
definition of done available and visible to all team members. It should be used as a
checklist during the code review process to ensure that all changes meet the established
criteria. Having a clear definition of done can streamline the review process and reduce the
number of issues that need to be addressed in later stages of the development lifecycle.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.3-establish-clear-completion-criteria-for-code-tasks.html*

---

**Capability**: DL.CR — Code review

# [DL.CR.4] Comprehensive code reviews with an emphasis on business logic

**Category:** FOUNDATIONAL

Use automated code review tools to detect potential issues before they are merged
into the code base. This approach provides fast feedback to developers to fix issues before
a manual review takes place. This also frees manual reviewers from needing to review for
trivial issues like code style inconsistencies or syntax errors. Reviewers can instead focus
on more on complex aspects of the code such as business logic, maintainability, and
scalability, which may be difficult to automate. This accelerates the review process,
reduces the feedback loop, and promotes rapid iteration.

Start by identifying the types of issues that can be automated (like code formatting,
syntax errors, and potential security vulnerabilities). Then, choose suitable tools that fit
your code base and your team's needs. Integrate these quality assurance (QA) tools into your
development lifecycle so that the checks are automatically run when code changes are being
developed and merged.

Using automated code review tools is recommended for improved
efficiency and consistency, but is not absolutely required for
code reviews as DevOps teams can function and conduct manual
code reviews without them.

**Related information:**

- [Create
code reviews in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-code-reviews.html)
- [Automate
code reviews with Amazon CodeGuru Reviewer](https://aws.amazon.com/blogs/devops/automate-code-reviews-with-amazon-codeguru-reviewer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.4-comprehensive-code-reviews-with-an-emphasis-on-business-logic.html*

---

**Capability**: DL.CR — Code review

# [DL.CR.5] Foster a constructive and inclusive review culture

**Category:** FOUNDATIONAL

Code reviews should be respectful and collaborative
interactions that cultivate a positive and inclusive culture.
Good code reviews involve asking open-ended questions,
suggesting alternatives, and assuming good intentions. Reviews
should be empathetic and kind, recognizing the effort put into
the code changes and promoting positivity.

The tone and approach of code reviews can greatly impact the
efficiency of the process, team morale, and ultimately the
quality of the product. A positive and inclusive review
culture encourages more open discussion, facilitates knowledge
sharing, and can lead to improved code quality.

To implement a positive and inclusive review culture, teams
should establish clear guidelines on the expectations for code
reviews, including language use and constructive feedback.
Regularly reinforce these expectations through team meetings
and training. Encourage team members to focus on the code and
not the coder, to be respectful and patient, and to frame
suggestions as questions or alternatives rather than absolute
critiques. Use the available escalation paths and mutually
agreed upon team guiding principles to quickly resolve team
differences and act as tie breakers during disagreement.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.5-foster-a-constructive-and-inclusive-review-culture.html*

---

**Capability**: DL.CR — Code review

# [DL.CR.6] Initiate code reviews using pull requests

**Category:** RECOMMENDED

[Pull
requests](https://docs.aws.amazon.com/codecommit/latest/userguide/pull-requests.html) are a method of integrating changes from one
branch of a repository into another. They can be used to
propose, review, and integrate changes from a feature branch
into the main releasable branch. Modern branching strategies,
including
[GitHub
flow](https://docs.github.com/en/get-started/quickstart/github-flow) and
[trunk-based
development](https://trunkbaseddevelopment.com/continuous-review/), support this workflow to initiate code
review.

A pull request workflow is recommended for organizations and teams which have
enhanced code review requirements. This workflow could include requiring multiple peer
reviewers, or enforcing that reviews must take place before code is integrated into the
main releasable branch. We recommend adopting trunk-based development paired with a pull
request workflow utilizing [short-lived
feature branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/). This method uses feature branches solely to trigger code
review processes through a pull request workflow. These short-lived feature branches
should not be used as a source for code deployments.

There should be clearly defined steps to standardize creating,
reviewing, and merging pull requests. Store these guidelines
in a shared, easily accessible location to ensure all team
members understand the process. The guidelines should include:

- **Useful descriptions and titles:** The pull request
descriptions should guide the reviewer through the changes, grouping related files and
concepts. A well-crafted title gives a high-level summary of the changes, providing
the reviewer with the necessary context.
- **Descriptive commit messages:** Each commit message
should clearly communicate what changed and why. This can make auto-generated pull
requests more useful, provide a bullet-point summary of the changes, and aid reviewers
who read the commits along with the diff.
- **Inline comments:** Leaving comments on the pull request
can guide the reviewer through the changes. These comments can provide the reviewer
with the necessary context, such as files that were simply re-indented or files where
the main bulk of changes occurred.
- **Visual cues:** For user interface (UI) changes,
consider including screenshots, GIFs, or videos. Visual representations can make it
easier for reviewers to understand the changes.

Pull request workflows are recommended, but not strictly
required for DevOps adoption. Some organizations and smaller
teams may choose to strictly follow trunk-based development
practices and commit
changes [directly
to the main releasable branch](https://trunkbaseddevelopment.com/committing-straight-to-the-trunk/). In this workflow, code
reviews are performed
through [pair
programming]( https://www.agilealliance.org/glossary/pair-programming) or initiated through custom post-commit
processes. Choose the right method for performing code review
based on your organization requirements and individual team
preferences.

**Related information:**

- [Reviewing
a pull request - Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/pull-requests-review.html)
- [Team
Collaboration with Amazon CodeCatalyst](https://aws.amazon.com/blogs/devops/team-collaboration-with-amazon-codecatalyst/)
- [Code
review](https://en.wikipedia.org/wiki/Code_review)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.6-initiate-code-reviews-using-pull-requests.html*

---

**Capability**: DL.CR — Code review

# [DL.CR.7] Create consistent and descriptive commit messages using a specification

**Category:** RECOMMENDED

Use a well-documented specification, descriptive commit message format that clearly
explain what changes were made and why. Clear and consistent communication support the
fast-paced, iterative nature of DevOps. Consistent commit messages improve collaboration,
make it easier to track and understand changes, aid in debugging, and can be used to
automatically generate change logs.

Adopt a specification, such as Conventional Commits, to
indicate code features, fixes, and breaking changes through
commit messages. Ideally, this would be enforced using
pre-commit hooks and the developer experience improved through
IDE integrations. Training and documentation can also be used
to educate developers on the importance and use of this
specification. If done consistently, this information could be
used to automatically generate legible change log records for
non-developer consumers and users of the system.

Adopting a commit specification is recommended as it greatly
enhances communication and collaboration by clearly
documenting the changes being made and why they are important
to the overall system. This can significantly boost efficiency
and transparency but isn't required as DevOps teams can
function without it.

**Related information:**

- [Conventional
Commits](https://www.conventionalcommits.org/en/v1.0.0/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.7-create-consistent-and-descriptive-commit-messages-using-a-specification.html*

---

**Capability**: DL.CR — Code review

# [DL.CR.8] Designate code owners for expert review

**Category:** OPTIONAL

A code owners process assigns a designated owner, usually the
person or team with the most knowledge or expertise, to each
part of the code base. In a DevOps environment, this helps
ensure that there is an expert reviewer available for specific
or complex parts of the system at all times.

To implement a code owners process, determine who the code owners should be based on
expertise and distribute the ownership equally amongst the team to avoid bottlenecks. You
can use features in version control systems that automatically assign code owners to
review code changes in their area of expertise. One example of this would be to use a
`CODEOWNERS` file stored along with the code in the repository. This file
defines individuals or teams that are responsible for code in a repository.

While this practice is optional and not beneficial for all organizations, it can be
particularly useful for larger teams or those with complex, distributed systems as it
provides an additional layer of control and can prevent potential issues from going
unnoticed if all reviewers are not equally experienced with a specific or complex part of
the code base.

**Related information:**

- [About
code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.8-designate-code-owners-for-expert-review.html*

---

**Capability**: DL.CS — Cryptographic signing

# [DL.CS.1] Implement automated digital attestation signing

**Category:** RECOMMENDED

Digital attestations serve as verifiable evidence that
software components were built, tested, and conform to
organizational standards within a controlled environment.
Signatures associated with each attestation can be verified to
ensure that the component has not been tampered with and
originated from a trusted source. Generating attestations
throughout the development lifecycle provides a method of
ensuring software quality, origin, and authenticity.

Embed automated tools into the deployment pipeline to produce digital
attestations. Create an attestation for each action you want to create proof for, such as
a test being run, software being packaged, or even manual approval acceptance steps. Sign
these attestations using symmetric or asymmetric keys. Follow metadata frameworks such
as [in-toto](https://in-toto.io/) for best practices for formatting
attestations to include metadata about the software, the build environment, and the
authoring party. Store attestations either with build artifacts in a repository or within
governance tools for deeper analysis.

**Related information:**

- [Software
attestations](https://slsa.dev/attestation-model)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cs.1-implement-automated-digital-attestation-signing.html*

---

**Capability**: DL.CS — Cryptographic signing

# [DL.CS.2] Sign code artifacts after each build

**Category:** RECOMMENDED

Code signing is the process of attaching a digital signature
to build artifacts like binaries, containers, and other forms
of packaged code to enable verifying its integrity and
authenticity. Signing code artifacts minimizes risk of using
or distributing tampered or counterfeit software.

Cryptographically sign code artifacts during the build
process. Ideally this occurs after testing and before
publishing to production. Follow
[best
practices for timestamping](https://www.digicert.com/blog/best-practices-timestamping) while signing. Timestamping
provides a verified date and time of the signing, serving as
evidence that the code artifact existed and met the signature
criteria while the certificate was still valid. To safeguard
operations, ensure that the validity of the signed code
artifact is recognized even after the signing certificate
itself has expired.

Store signatures in a location accessible to users and systems
that need to verify signed code artifacts. When
using [Open
Containers Initiative (OCI)](https://opencontainers.org/) compliant artifact
registries, it is encouraged to store digital signatures
alongside the build artifacts being signed. This enables a
consolidated retrieval process and allows verification systems
to easily locate and validate signatures. Just as with
artifacts, signatures can accumulate over time. Implement a
lifecycle policy that archives or deletes older signatures
that are no longer needed to help manage storage costs.

After a signature has been stored, it should be immutable so that the signature
cannot be tampered with or replaced. Use fine-grained access controls to ensure that only
authorized entities can push or modify artifacts and their corresponding signatures.
Regularly back up your digital signatures. Having a backup ensures you can still verify
the integrity and authenticity of your artifacts in the event of storage failures. All
access and operations on stored signatures should be logged to support forensic analysis
and to adhere to compliance requirements.

Implement cryptographic signing of artifacts during the build
process. Ideally this occurs after testing and before
publishing to production. This helps ensure the integrity of
the artifacts and confirms their authenticity. We recommend
using a managed service like
[AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) to reduce the complexity that comes with
managing public key infrastructure. Refer
to [AWS Signer workflows](https://docs.aws.amazon.com/signer/latest/developerguide/workflows.html) for guidance that fits your use case.

For more control over the signing process or for complex use
cases, you can create and manage your own code signing
platform using Public Key Infrastructure (PKI). While this
approach offers precise control, it requires consistent upkeep
and adherence to best practices.
[AWS Private Certificate Authority](https://aws.amazon.com/private-ca/) is a managed private CA
service that helps you manage the lifecycle of your private
certificates easily, without the investment and ongoing
maintenance costs of operating your own private CA.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS05-BP03 Use
managed services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a4.html)
- [Using
AWS Signer workflows](https://docs.aws.amazon.com/signer/latest/developerguide/workflows.html)
- [Configuring
code signing for AWS SAM applications - AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/authoring-codesigning.html)
- [Security
Considerations for Code Signing](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01262018.pdf)
- [Code
signing using AWS Certificate Manager Private CA and AWS Key Management Service asymmetric keys](https://aws.amazon.com/blogs/security/code-signing-aws-certificate-manager-private-ca-aws-key-management-service-asymmetric-keys/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cs.2-sign-code-artifacts-after-each-build.html*

---

**Capability**: DL.CS — Cryptographic signing

# [DL.CS.3] Enforce verification before using signed artifacts

**Category:** RECOMMENDED

Before using code artifacts, the cryptographic signature
should be inspected and validated. This verification step
enforces trust and security within the development lifecycle,
ensuring that software remains unchanged before it is used or
deployed.

Strictly enforce verification of cryptographic signatures each
time a code artifact is used or deployed. Use a managed
signing service
like [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) or the public key from your organization's
trusted Certificate Authority (CA) for signature verification.
Automate the verification process where possible, as manual
checks can be error-prone and may not be strictly enforced.
Some examples of this are integrating signature verification
into the deployment pipeline, enforcing verification at the
registry level as artifacts are distributed, or using the
Kubernetes admission controller to verify each container image
as they are pulled.

**Related information:**

- [Security
Considerations for Code Signing](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01262018.pdf)
- [Configuring
code signing for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html)
- [Kyverno
extension service for Notation and the AWS signer](https://github.com/nirmata/kyverno-notation-aws)
- [Announcing
Container Image Signing with AWS Signer and Amazon EKS](https://aws.amazon.com/blogs/containers/announcing-container-image-signing-with-aws-signer-and-amazon-eks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cs.3-enforce-verification-before-using-signed-artifacts.html*

---

**Capability**: DL.CS — Cryptographic signing

# [DL.CS.4] Enhance traceability using commit signing

**Category:** OPTIONAL

Commit signing involves attaching a digital signature to code
commits, certifying the integrity of changes and the identity
of the committer. While not universally adopted by all
organizations, commit signing enhances trust and traceability
as developers make code changes, making it easier to track the
origin of changes and ensure their authenticity.

Have developers sign their code changes when submitting to
version control using personal private keys from tools
like [GPG](https://gnupg.org/).
Developers should be encouraged to sign both commits and tags
with their private keys. This can be particularly valuable for
open-source projects or where code originates from diverse
sources.

For this approach to be effective in practice, developers require an understanding of
certificates and using them for signing. Developers must ensure that their private keys
remain confidential, taking measures to store them securely and avoid potential
exposure. They also should be trained to recognize signs of key compromise, such as
unexpected commits. When compromise is detected, the associated key should be revoked
immediately to mitigate potential risks.

**Related information:**

- [Signing
Commits](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work#_signing_commits)
- [The GNU Privacy
Guard](https://gnupg.org/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cs.4-enhance-traceability-using-commit-signing.html*

---

**Capability**: DL.EAC — Everything as code

# [DL.EAC.1] Organize infrastructure as code for scale

**Category:** FOUNDATIONAL

Infrastructure as code (IaC) provides consistent and automated infrastructure
management capabilities which are important to DevOps adoption. Effectively organizing and
scaling IaC within your organization enhances flexibility, readability, and reusability
across multiple teams, while streamlining infrastructure provisioning and maintenance.

When working with IaC files and artifacts, apply modern
practices such as modular design for improved management and
reuse, and maintain thorough in-code documentation for
clarity. Adopt IaC-specific design patterns, like breaking
down infrastructure templates into reusable modules. Treat IaC
testing with the same rigor as other software, focusing on
security risks like excessive privileges or open security
groups, while upholding quality standards. Use version
control for IaC templates to ensure traceable changes,
reliable rollbacks, and efficient sharing across the
organization.

You must carefully consider your organization's governance structure when deciding
how to implement IaC at scale. Depending on the specific needs, your organization might find
one model more suitable than the other, or even adopt a hybrid approach that combines
elements of both. The right approach to scaling is dependent on factors such as team
dynamics, operating model, application type, and the desired rate of change.

For example, services like [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) and [AWS Proton](https://aws.amazon.com/proton/) provide
distinct methods to distribute and consume secure-by-default software components and IaC in
different ways. Service Catalog suits organizations favoring predefined deployment standards and
centrally defined resource provisioning, while AWS Proton is ideal for organizations that
allow development teams to maintain infrastructure and application autonomy. Some
organizations might prefer to adopt a fully decentralized approach, where individual teams
provision and manage their own [AWS CloudFormation](https://aws.amazon.com/cloudformation/) IaC templates. Choose the tools and distribution methods that best
support your governance model and business goals.

**Related information:**

- [Infrastructure
as code - Introduction to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)
- [Infrastructure
as Code on AWS - An Introduction](https://blog.awsfundamentals.com/infrastructure-as-code-on-aws-an-introduction)
- [Accelerate
deployments on AWS with effective governance](https://aws.amazon.com/blogs/architecture/accelerate-deployments-on-aws-with-effective-governance/)
- [Source
Control concepts](https://aws.amazon.com/devops/source-control/)
- [Design
Patterns](https://refactoring.guru/design-patterns)
- [Amazon's
approach to security during development: Octane](https://youtu.be/NeR7FhHqDGQ?t=1571)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.1-organize-infrastructure-as-code-for-scale.html*

---

**Capability**: DL.EAC — Everything as code

# [DL.EAC.2] Modernize networks through infrastructure as code

**Category:** FOUNDATIONAL

The practice of managing networking configurations through code, including network
automation, version control, and rigorous testing to ensure quality and stability. Apply
DevOps practices to networking systems to streamline network operations, reduce human
errors, and speed up network deployments. *Networking as code* enables
the predictable and repeatable provisioning of networking components, making
infrastructure more modular and less prone to error.

Managing networking components as code requires cultural, process, and tool changes.
Shift from a centralized, manual model of network management to a more autonomous model
where individual teams can operate independently. Loosely couple networking architectures
to create modular components that can be managed, maintained, and scaled individually. Use
infrastructure as code (IaC) tools to define network infrastructure and configurations and
use development lifecycle capabilities like continuous integration and continuous delivery
(CI/CD) for deploying networking changes. Like other systems, networking changes should
undergo automated testing to provide assurance that they meet functional, non-functional,
and security requirements before deployment.

Often, platform teams manage network components on behalf of
individual teams when possible so that all teams do not need
to become networking experts. However, for cases where this is
not possible, use shared resources or predefined network
configuration templates which have embedded best practices and
secure defaults. This approach encourages predictable and
repeatable provisioning of self-service networking components.
Have guardrails in place within the environment to enforce
compliance of networking requirements.

**Related information:**

- [NetDevOps:
A modern approach to AWS networking deployments](https://aws.amazon.com/blogs/networking-and-content-delivery/netdevops-a-modern-approach-to-aws-networking-deployments/)
- [NetDevSecOps
to modernize AWS networking deployments](https://aws.amazon.com/blogs/networking-and-content-delivery/netdevsecops-to-modernize-aws-networking-deployments/)
- [Field
Notes: Using Infrastructure as Code to Manage Your AWS
Networking Environment](https://aws.amazon.com/blogs/architecture/field-notes-using-infrastructure-as-code-to-manage-your-aws-networking-environment/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.2-modernize-networks-through-infrastructure-as-code.html*

---

**Capability**: DL.EAC — Everything as code

# [DL.EAC.3] Codify data operations

**Category:** FOUNDATIONAL

Codifying data operations in a DevOps environment extends the infrastructure as code
(IaC) principle to data management, which involves treating database schemas, data
transformations, and data pipelines as code. Codifying data operations enables other DevOps
capabilities including the use of data management pipelines for data lifecycle management,
enforcing quality assurance and governance standards, providing auditability of changes, and
the ability to rollback changes when necessary.

Store database schemas, along with any related procedures,
views, and triggers, in version control systems alongside your
application code. This enables the ability to track, review,
and test schema changes before deploying them to your
production environment. To start managing existing data source
schemas as code, database migration and event analysis tools
like
[AWS DMS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/) and
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) can help to infer schemas from existing
data sources.

**Related information:**

- [Converting
database schemas using DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html)
- [Creating
an Amazon EventBridge schema](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema-create.html)
- [Using
Amazon RDS Blue/Green Deployments for database
updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.3-codify-data-operations.html*

---

**Capability**: DL.EAC — Everything as code

# [DL.EAC.4] Implement continuous configuration for enhanced application management

**Category:** RECOMMENDED

*Configuration as code* is the practice of managing and tracking
configuration changes as code, providing an audit trail and reducing errors from manual
changes. [Continuous configuration](https://www.allthingsdistributed.com/2021/08/continuous-configuration-on-aws.html) uses configuration as code to enhance configuration
management by allowing configuration changes to be made independently of application code
deployments.

Configuration should be separated from application code to allow for independent
tracking and management. Use tools designed for managing configurations as code, such
as [AWS
AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/), to manage configuration externally from the application. Create fully
automated pipelines that perform continuous integration and continuous delivery (CI/CD)
based on changes to the configuration code. Just like with application deployment
pipelines, these configuration deployment pipelines should run quality assurance tests,
followed by deployment in a non-production environment before deploying to production.

It's important to distinguish between static and dynamic configuration types. Static
configurations do not change during the software's runtime and are specific to each
environment. Dynamic configurations can be adjusted at runtime without downtime. [Feature
flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) are examples of dynamic configurations that can be used to control which
features are enabled per environment to decouple release from deployment. Operational
configurations, such as log level, throttling thresholds, connection/request limits,
alerts, and notifications, can be static or dynamic depending on the use case and need to
be managed. Application modes, which toggle the application to run as either
*development*, *test*, or
*production*, are typically considered to be static configuration
that is set at startup and do not change.

General use cases for continuous configuration include application integration
tuning, feature toggling, allowing access to premium content through allow lists, and
addressing operational issues and troubleshooting. To manage your configurations
effectively, establish a routine to prevent configuration bloat. While it can seem
tempting to externalize as many variables as possible, an excessively complex
configuration file can lead to confusion and errors. Carefully evaluate the necessity,
frequency of change, and runtime requirements of each value to decide if it should be
included as dynamic configuration.

For large-scale deployment of configuration as code, a [Dynamic Configuration Pipeline](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/dynamic-configuration-pipeline/index.html) is recommended. This allows centralized
management of the entire workload configuration and its components across all
environments. It ensures that all configurations are version-controlled, adhere to quality
assurance and code review processes, and is capable of progressively deploying
configuration changes and performing rollbacks as necessary to minimize system
disruptions.

Continuous configuration is beneficial in DevOps environments, as it improves
operational efficiency and scalability. However, not every system requires the complexity
associated with continuous configuration. Therefore, each workload should be evaluated
depending on architecture choice, team preferences, and service level objective
requirements.

**Related information:**

- [AWS Cloud Adoption Framework: Operations Perspective
- Configuration management](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/configuration-management.html)
- [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [Continuous configuration](https://www.allthingsdistributed.com/2021/08/continuous-configuration-on-aws.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.4-implement-continuous-configuration-for-enhanced-application-management.html*

---

**Capability**: DL.EAC — Everything as code

# [DL.EAC.5] Integrate technical and operational documentation into the development lifecycle

**Category:** RECOMMENDED

Integrating documentation and code involves creating,
maintaining, and publishing documentation using the same tools
and processes used for application development. With this
approach, changes to systems should be immediately reflected
in documentation, reducing the risk of discrepancies between
system behavior and documentation. By making documentation
part of the development lifecycle, it becomes a living
document that evolves with the system over time.

Documentation should be stored in a versioned source code repository and written in a
machine-readable markup language, such as Markdown. The documentation can be made directly
accessible through the repository or through knowledge sharing tools capable of rendering
the markup language, like Git-based wikis, static site generators, or directly in
developers' integrated development environments (IDEs).

Code should include clear, insightful comments and commit
messages should be structured using a machine-readable
specification, such
as [Conventional
Commits](https://www.conventionalcommits.org/en/v1.0.0/). This information can be used as a source to
generate detailed documentation and change logs using tools
specific to the programming language and platforms being used.
Many of these tools can create API references, class diagrams,
or other technical documents from inline comments in your
source code, ensuring the documentation is always in line with
the most recent changes. Automate this process by adding a
stage to the deployment pipeline to generate documentation
with every change to a main, releasable branch.

This approach is not only limited to documenting code, but also can be used to store
operational documentation like incident response procedures, disaster recovery plans,
training material, and onboarding processes. While some aspects of these documents still
likely require manual effort to create, the benefits of incorporating these documents into
the development lifecycle include enforced reviews of changes, ability to write tests to
suggest updating documentation when changes are significant or made to important
components, and versioning the documents for auditability.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL12-BP01 Use
playbooks to investigate failures](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_playbook_resiliency.html)
- [Write
the Docs: Docs as Code](https://www.writethedocs.org/guide/docs-as-code/)
- [One
AWS team's move to docs as code](https://www.youtube.com/watch?v=Cxuo3udElcE)
- [AWS Incident Response Playbook Samples](https://github.com/aws-samples/aws-incident-response-playbooks)
- [Using
code as documentation to save time and share
context](https://github.com/readme/guides/code-as-documentation)
- [DocFx](https://dotnet.github.io/docfx/)
- [How
to build an automated C# code documentation generator
using AWS DevOps](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-build-an-automated-c-code-documentation-generator-using-aws-devops/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.5-integrate-technical-and-operational-documentation-into-the-development-lifecycle.html*

---

**Capability**: DL.EAC — Everything as code

# [DL.EAC.6] Use general-purpose programming languages to generate Infrastructure-as-Code

**Category:** RECOMMENDED

Developing infrastructure as code (IaC) using general-purpose programming languages
aligns closely with modern software development practices and DevOps principles. IaC has
traditionally been implemented as predefined templates modeled through domain-specific
languages using markup languages like JSON or YAML. During deployment, these templates are
provided parameters which specify environment-specific details. While parameterized
templates are still a best practice for traditional IaC templates, this approach can
become difficult to develop, troubleshoot, and manage as infrastructure and environments
become more complex.

Using general-purpose programming languages changes how we develop, manage, and
deploy IaC. It is no longer a collection of parameterized templates, but instead
infrastructure is written in common programming languages such as TypeScript, Python, or
Java, and can be treated the same as other code throughout the development lifecycle.
Instead of providing environment-specific configuration during deployment, tools
like [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html#best-practices-apps-stages)
generate separate templates for each environment using configurations defined in source
code. This provides a more predictable, consistent, and reproducible deployment process.

Transitioning to using general-purpose programming languages
for IaC can also change how you govern IaC at scale. For
example, AWS CDK includes the ability to consume, publish, and
version software components called AWS CDK
[constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html)
through private artifact registries or the
open-source [Construct
Hub](https://constructs.dev/) registry.

**Related information:**

- [Best
practices for developing and deploying cloud
infrastructure with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html)
- [CDK
for Terraform (CDKtf)](https://www.terraform.io/docs/cdktf/index.html)
- [CDK for Kubernetes
(CDK8s)](https://cdk8s.io/)
- [AWS Solutions Constructs](https://docs.aws.amazon.com/solutions/latest/constructs/welcome.html)
- [Artifact
Repository - AWS CodeArtifact](https://aws.amazon.com/codeartifact/)
- [Infrastructure
IS Code with the AWS CDK](https://www.youtube.com/watch?v=Lh-kVC2r2AU)
- [Best
practices for using the AWS CDK in TypeScript to create
IaC projects](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/introduction.html)
- [Adding
the "AWS CDK bootstrap" action in Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/cdk-boot-action.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.6-use-general-purpose-programming-languages-to-generate-infrastructure-as-code.html*

---

**Capability**: DL.EAC — Everything as code

# [DL.EAC.7] Automate compute image generation and distribution

**Category:** OPTIONAL

The management of compute images, including containers and machine images, can be
optimized and made more reliable through a code-driven approach. Compute images generally
include a base image, libraries, environment variables, application code, and
configuration files. Similar to other forms of infrastructure as code (IaC), compute
images can be codified, stored in version control systems, tested, and distributed as part
of the development lifecycle.

Establish automated pipelines for building, testing, and distributing compute images.
The build stage creates the image based on its code definition, the
*test* stage validates the functionality and security compliance of
the image, and the *distribution* stage ensures the image is readily
available for teams to use in their environments and workloads. Updates to the images
should be automated, accounting for software patches, security enhancements, and other
modifications.

Given the diverse range of applications and infrastructure
requirements, especially when using managed cloud-based
services, not all organizations or workloads necessitate using
dedicated compute images or codifying them.

**Related information:**

- [Amazon EC2 Image Builder](https://aws.amazon.com/image-builder/)
- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture)
- [What
is AWS App2Container?](https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.7-automate-compute-image-generation-and-distribution.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.1] Establish development environments for local development

**Category:** FOUNDATIONAL

Create development environments that provide individual developers with a safe space
to test changes and receive immediate feedback without impacting others on the team or
shared environments. Development environments are small scale, production-like environments
that provide a balance between providing developers with accurate feedback and being low
cost and easy to manage. Development environments serve a [different purpose](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/sandbox-ou.html#sandbox-and-development-environments) than sandbox environments and should be used for day-to-day
development and experimentation that requires access to your software components and
services.

Development environments can take the form of dedicated cloud environments, local
emulations of infrastructure, or be hosted on a local workstation. While most cloud
providers, open-source tools, and third parties provide options for emulating infrastructure
locally on development machines, these tools might not have full feature parity, leaving
them to only be suitable for a subset of use cases. Using cloud-based development
environments provides the most reliable, accurate, and complete coverage when working with
cloud workloads. We recommend providing a cloud-based development environment to each
developer, with each environment being in a separate AWS account.

Developers should be encouraged to use their own development environments for testing
and debugging to reduce the chance of problems occurring in environments shared by the
broader team. To keep the development environment as close to the production setup as
possible, deployments to the development environment should be sourced from the main
releasable branch, rather than from long-lived development branches. The development
environment setup should be well-documented in an up-to-date playbook that is readily
available to all members of the team. For this to be effective, the playbook must be updated
as the needs of the team and environment change over time. Ideally, the full lifecycle of
these environments, including provisioning, are managed through automated governance
processes.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS02-BP05
Optimize team member resources for activities performed](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a6.html)
- [Setting
Up Your AWS Environment](https://aws.amazon.com/getting-started/guides/setup-environment/)
- [Dev
Environments in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html)
- [Best
practices for testing serverless applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-application-testing/best-practices.html)
- [Improving
the development cycle - Testing in the cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-dev-cycle.html)
- [Improving
the development cycle - Testing locally](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-dev-cycle.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.1-establish-development-environments-for-local-development.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.2] Consistently provision local environments

**Category:** FOUNDATIONAL

Standardize and automate the process for setting up local development environments
using managed services, infrastructure as code (IaC), and scripted automation. This approach
permits environments to be reliably replicated across different systems and teams, ensuring
uniformity. Consistent local environments help to reduce issues that occur only on particular machines.

Create a baseline configuration for your local development environment that mirrors
the production setup as closely as possible. Use IaC tools to define this environment, and
script the provisioning process. All IaC and scripts should be version-controlled, helping
to ensure that any changes are tracked and can be rolled back if necessary. Educate
developers on the importance of using the provisioned environments and provide documentation
on how to set up and troubleshoot these environments. Regularly review and update the
baseline configuration to keep it aligned with changes in the production environment.
Consider allowing developers to request local environments on-demand through a self-service
developer portal.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.2-consistently-provision-local-environments.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.3] Commit local changes early and often

**Category:** FOUNDATIONAL

While developing locally, developers should begin to make
small, frequent commits to save versions of their code changes
as they develop. Unlike pushing code changes so that they are
accessible to other team members, local commits deal
specifically with a developer's individual progress as they
develop locally. This practice makes local development safer,
enabling developers to freely innovate without fear of losing
completed work by capturing snapshots of iterative changes to
the code base.

Use version control tools, like Git, local testing tools for fast feedback,
and [conventional
commit](https://www.conventionalcommits.org/en/v1.0.0/) messages that describe the nature and rationale behind the changes for.
Strive to make it a habit to locally commit changes as soon as a logical unit of work is
completed. This can be after fixing a bug, adding a new function, or refining an existing
piece of code.

Placing emphasis on the significance of making frequent local commits adapts
developers to the idea of breaking down work into smaller, more manageable batches of work.
This translates into streamlined integration processes when working in a team and is
critical for practicing [continuous integration](https://aws.amazon.com/devops/continuous-integration/) and [continuous delivery](https://aws.amazon.com/devops/continuous-delivery/) (CI/CD).

**Related information:**

- [Git
Basics - Recording Changes to the Repository](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [Continuous
Integration - Martin Fowler](https://martinfowler.com/articles/continuousIntegration.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.3-commit-local-changes-early-and-often.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.4] Enforce security checks before commit

**Category:** FOUNDATIONAL

Pre-commit hooks can be an effective tool for maintaining security best practices.
These hooks can help in the early detection of potential security risks, such as exposed
sensitive data or publishing code to untrusted repositories. At a minimum, use pre-commit
hooks to identify hidden secrets, like passwords and access keys, before code is published
to a shared repository. When discovering secrets, the code push should fail
immediately—effectively preventing a security incident from occurring.

Select security tools compatible with your chosen programming languages and customize
them to uphold your specific governance and compliance requirements. It is best to integrate
these security tools into pre-commit hooks, integrated development environments (IDEs), and
continuous integration pipelines so that changes are continuously checked before code is
committed into a shared repository.

**Related information:**

- [Security
in every stage of CI/CD pipeline: Pre-commit hooks](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#pre-commit-hooks)
- [Security
scans - CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security-scans.html)
- [Pre-commit](https://pre-commit.com/)
- [Husky](https://typicode.github.io/husky/)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [GitGuardian](https://docs.gitguardian.com/ggshield-docs/integrations/git-hooks/pre-commit)
- [AWS-IA
opinionated pre-commit hooks](https://github.com/aws-ia/pre-commit-configs)
- [Blog: Extend
your pre-commit hooks with AWS CloudFormation Guard](https://aws.amazon.com/blogs/security/extend-your-pre-commit-hooks-with-aws-cloudformation-guard/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.4-enforce-security-checks-before-commit.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.5] Enforce coding standards before commit

**Category:** RECOMMENDED

Identify common style, formatting, and other flaws before they
are published to a repository. Use static code scanning tools,
such as linters, to improve code quality and consistency
before pushing committed code. This process can be automated
using pre-commit hooks. Upon discovery, pushing the commit
should ideally fail and require immediate correction by the
developer. Automatically and consistently enforcing coding
standards during the local development process directly
improves the code review process by removing common errors
before manual review.

Select scanning tools compatible with your chosen programming
language and customize them to uphold specific coding
standards and styles. It is best to integrate these tools into
pre-commit hooks, integrated development environments (IDEs),
and continuous integration pipelines so that changes are
consistently and continuously checked at all stages of the
development lifecycle.

**Related information:**

- [Amazon CodeGuru Reviewer](https://aws.amazon.com/codeguru/)
- [AWS CloudFormation Linter](https://github.com/aws-cloudformation/cfn-lint)
- [Pre-commit](https://pre-commit.com/)
- [Husky](https://typicode.github.io/husky/)
- [Validate
your AWS SAM applications with AWS CloudFormation
Linter](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/validate-cfn-lint.html)
- [Workshop: AWS CloudFormation Workshop - Linting and-testing](https://catalog.workshops.aws/cfn101/en-US/basics/templates/linting-and-testing)
- [Blog: Use
Git pre-commit hooks to avoid AWS CloudFormation
errors](https://aws.amazon.com/blogs/infrastructure-and-automation/use-git-pre-commit-hooks-avoid-aws-cloudformation-errors/)
- [Blog: Automate
code reviews with Amazon CodeGuru Reviewer](https://aws.amazon.com/blogs/devops/automate-code-reviews-with-amazon-codeguru-reviewer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.5-enforce-coding-standards-before-commit.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.6] Leverage extensible development tools

**Category:** RECOMMENDED

Extensible software development tools, primarily integrated
development environments (IDEs) or text editors, can be
augmented with plugins or extensions. These plugins enhance
the functionalities of the software, allowing for improved and
tailored developer experiences.

Choose development tools that work well with your primary programming languages and
technologies in your stack. Choosing a widely adopted IDE or text editor enables
leveraging support communities and extension ecosystems. Teams should be encouraged to
experiment with and adopt plugins that enhance code quality, simplify integrations, or
speed up routine tasks. Over time, curate a list of preferred, approved extensions that
align with your DevOps objectives and security requirements. Verify that there is a
process in place for regularly updating these tools and extensions to benefit from the
latest improvements and security patches.

**Related information:**

- [Security
in every stage of CI/CD pipeline: IDE tools and
plugins](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#pre-commit-hooks#ide-tools-and-plugins)
- [Tools
to Build on AWS](https://aws.amazon.com/developer/tools/)
- [Dev
Environments in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.6-leverage-extensible-development-tools.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.7] Establish sandbox environments with spend limits

**Category:** RECOMMENDED

Sandbox environments are dedicated spaces for developers to
explore, experiment, and innovate with new technologies or
ideas. Unlike development environments, which are meant for
more structured day-to-day development, they allow more fewer controls, while ensuring no connectivity to
internal networks or other environments.

Create a comprehensive sandbox usage policy. This policy must
set clear boundaries on the kinds of data permissible with the
sandbox, ensuring no leakage of sensitive information or
code. Establish rules for access controls. Some environments
might be tailored for individual developers, while others
could serve small teams. Rules regarding network connectivity
should ensure that the sandbox remains isolated, preventing
any unintended interactions with other internal networks or
environments. Set tagging strategies which can aid in managing
automation and cost tracking. Overall, ensure that this policy
makes a distinction between sandbox environments and
development environments, and lays out the use cases best
suited for each.

Educate developers on the sandbox usage policy, including
responsible and cost-effective resource management techniques.
Encourage shutting down or deleting unnecessary resources,
especially when they're not in active use. Sandbox
environments should be treated ephemerally, with automated
governance processes managing the lifecycle to create, manage,
clean up resources, and destroy sandbox environments as
required.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST02-BP05
Implement cost controls](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_controls.html)
- [Sandbox
per builder or team with spend limits](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/sandbox-ou.html#sandbox-per-builder-or-team-with-spend-limits)
- [AWS Innovation Sandbox](https://aws.amazon.com/solutions/implementations/aws-innovation-sandbox/)
- [Cloud
Financial Management with AWS](https://aws.amazon.com/aws-cost-management/)
- [Sandbox
Accounts for Events](https://github.com/awslabs/sandbox-accounts-for-events)
- [Best
practices for creating and managing sandbox accounts in
AWS](https://aws.amazon.com/blogs/mt/best-practices-creating-managing-sandbox-accounts-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.7-establish-sandbox-environments-with-spend-limits.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.8] Generate mock datasets for local development

**Category:** OPTIONAL

Mock datasets are synthetic or modified datasets that
developers can use during the development process, eliminating
the need to interact with real, sensitive production
data. Using mock datasets ensures tests are thorough and
realistic, without compromising security.

Use data generating tools to create mock datasets. These tools
can range from random data generators to more advanced methods
like generative AI. Generative AI can be used to generate
synthetic datasets that can be used to test applications and
is especially useful for generating data that is not often
included in testing datasets, such as defects or edge cases.

If using real-world data is necessary for local development, ensure it is obfuscated.
Methods such as masking, encrypting, or tokenizing production datasets can transform real
datasets into mock datasets that are safe for local development. It might be useful to
store already prepared mock datasets that can be shared between teams or systems to
perform testing with. This approach creates a realistic local testing environment without
risking developers handling actual production data.

**Related information:**

- [Testing
software and systems at Amazon: Developer
environment](https://youtu.be/o1sc3cK9bMU?t=1017)
- [Generate
test data using an AWS Glue job and Python](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-test-data-using-an-aws-glue-job-and-python.html)
- [Foundation
Model API Service - Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [What
is Generative AI?](https://aws.amazon.com/what-is/generative-ai/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.8-generate-mock-datasets-for-local-development.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.9] Share tool configurations

**Category:** OPTIONAL

Sharing tool configuration among project or team members helps ensure a uniform set
up of integrated development environment (IDE) settings, text editor preferences, and
pre-commit hooks. Having these configurations tailored to each code base can reduce
discrepancies in code styles and promote seamless collaboration and a predictable
developer experience. This enables any developer working within that repository to begin
working in the environment quickly while maintaining team norms.

Commit tool configuration files to a shared repository.
Periodically review these shared configurations, ensuring they
remain updated as tools and practices evolve. While the idea
promotes consistency, be mindful of the need to occasionally
tailor configurations for specific tasks and preferences.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.9-share-tool-configurations.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.10] Manage unused development environments

**Category:** OPTIONAL

Properly managing unused environments prevents unnecessary
resource utilization and potential security threats. When
development environments are not in use, the environment and
associated resources should be disabled or deleted.

Managing unused development environments requires tracking,
disabling, or removing development setups that are dormant or
no longer in active use. Regularly audit the active and
inactive development environments. Implement automated tools
or scripts that monitor activity and provide notifications
regarding dormant environments.

Once identified, these environments should be archived,
disabled, or removed, depending on the future needs of the
project. Treat development environments as ephemeral
environments to reduces the risk of incurring unexpected cost
and leaving potentially insecure resources running.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS02-BP03 Stop
the creation and maintenance of unused assets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html)
- [AWS Well-Architected Cost Optimization Pillar: COST04-BP03
Decommission resources](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_decommission.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.10-manage-unused-development-environments.html*

---

**Capability**: DL.LD — Local development

# [DL.LD.11] Implement smart code completion with machine-learning

**Category:** OPTIONAL

Use machine learning (ML) algorithms within development tools to predict and suggest
code as developers write, based on patterns and commonly used syntax. This can improve
development experience, speed up the coding process, and reduce the potential for errors.

Incorporate ML-powered code generators into your developer tools, such as IDEs or
text editors, for real-time, intelligent code recommendations. Train and refine these
tools with regular feedback to ensure they align with your specific coding patterns and
practices.

**Related information:**

- [Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.11-implement-smart-code-completion-with-machine-learning.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.1] Use a version control system with appropriate access management

**Category:** FOUNDATIONAL

Version control systems enable tracking and managing of
changes to code over time. They allow multiple developers to
work on a project concurrently, provide a history of changes,
and make it possible to revert to a previous version if
necessary. Version control systems play a role in maintaining
the integrity of software components, as they provide an
auditable trail of all modifications made to the code base,
authorizes users as they access the code base, and help to
ensure that changes to the code base can be reverted or rolled
back.

Implement access management policies on the version control
systems which supports a culture of code sharing and
collaboration amongst teams in your organization. Having a mix
of both open and private repositories allows for a balance
between promoting code reuse and collaboration, and
safeguarding sensitive information. For open repositories,
developers can share code freely to encourage collaboration
and learning, while confidential projects or sensitive parts
of the code base can use private repositories.

Consider implementing role-based access control (RBAC) in your
version control system. Using RBAC, you can restrict write
(commit) access to specific roles or individuals and can
protect the main code base from inadvertent or inappropriate
alterations. This also allows granting broad,
organization-wide read access to open repositories, while
reserving the ability to limit access to sensitive or
confidential private repositories.

**Related information:**

- [What
Is Repo?](https://aws.amazon.com/what-is/repo/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.1-use-a-version-control-system-with-appropriate-access-management.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.2] Keep feature branches short-lived

**Category:** FOUNDATIONAL

In version control systems, feature branches provide a structured way to develop new
functions or address defects. These branches are carved out with the intent of eventually
merging changes into the main code base for release. Traditional branching methods, such as
GitFlow, lean towards creating long-lived feature branches which can introduce challenges
including complex merges and divergent code bases. Modern branching strategies, including
[GitHub
flow](https://docs.github.com/en/get-started/quickstart/github-flow) and [trunk-based
development](https://trunkbaseddevelopment.com/), emphasize the significance of keeping feature branches short-lived to
avoid these challenges. We recommend trunk-based development paired with a pull request
workflow utilizing [short-lived feature
branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/) as the most effective branching strategy when practicing DevOps.

The core benefit of short-lived feature branches is the
promotion of continuous integration. By frequently integrating
code changes into the main releasable branch of the
repository, teams discover integration problems early on. This
approach prevents last-minute chaos when merging code bases
leading to software that can be reliably released at any time.
We recommend merging into the main releasable branch at least
once per day.

Smaller teams might prefer committing directly to the trunk of
the releasable branch. Larger teams or those working on
complex software might lean towards a Pull-Request workflow
that uses short-lived branches. Regardless of the branching
strategy you choose to use, the principle remains: branches
should be transient, preferably representing a single
contributor's work. To enforce this, put a process in place to
remove branches that are already merged and prevent long-lived
branches by actively deleting branches that surpass a specific
retention period.

**Related information:**

- [Trunk-based
Development: Short-Lived Feature Branches](https://trunkbaseddevelopment.com/short-lived-feature-branches)
- [GitHub
flow](https://guides.github.com/introduction/flow/)
- [A
successful Git branching model: Note of reflection](https://nvie.com/posts/a-successful-git-branching-model/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.2-keep-feature-branches-short-lived.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.3] Use artifact repositories with enforced authentication and authorization

**Category:** FOUNDATIONAL

Artifact repositories and registries offer secure storage and
management for artifacts generated during the build stage of
the development lifecycle. Examples of artifacts that are
stored in these repositories are container images, compiled
software artifacts, third-party modules, and other shared code
modules. Using an artifact repository streamlines artifact
versioning, access control, traceability, and dependency
management, contributing to efficient and reliable software
releases. They can significantly improve the auditability,
security, and organization of your software artifacts, leading
to higher-quality software deliveries.

Artifact repositories are in the critical path for ensuring
the integrity of the software that is deployed into your
environments. All artifacts in the repository should be
expected to be built and tested using trusted automated
processes in an effort to prevent errors or bugs from being
introduced into the system. Artifact repositories should not
contain manually produced artifacts or allow existing
artifacts to be altered by users. Altering artifacts in the
artifact repository degrades the integrity of the artifact and
repository, so artifact repositories should enforce that
artifacts are immutable.

Use role-based or attribute-based access control to limit which users and systems can
store and modify artifacts in artifact repositories. Access to create, update, or delete
artifacts should remain restricted to emergencies, security use cases, and build and
deployment processes.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC11-BP05 Centralize
services for packages and dependencies](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_centralize_services_for_packages_and_dependencies.html)
- [Artifact
Repository - AWS CodeArtifact](https://aws.amazon.com/codeartifact/)
- [Fully
Managed Container Registry - Amazon Elastic Container Registry](https://aws.amazon.com/ecr/)
- [Code
Repositories and Artifact Management | AWS Marketplace](https://aws.amazon.com/marketplace/solutions/devops/code-repositories-and-artifact-management?aws-marketplace-cards.sort-by=item.additionalFields.headline&aws-marketplace-cards.sort-order=asc&awsf.aws-marketplace-devops-store-use-cases=*all)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.3-use-artifact-repositories-with-enforced-authentication-and-authorization.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.4] Grant access only to trusted repositories

**Category:** FOUNDATIONAL

To maintain the security, integrity, and quality of your software, restrict the usage
of untrusted source code and artifact repositories. Untrusted repositories present risks,
including potentially introducing vulnerabilities into your software and leaking sensitive
code or information. As a safer alternative, only use trusted repositories that offer
secure, vetted libraries, and dependencies.

Implement policies that control where developers can publish
code, to prevent accidental exposure or internal threats. This
should apply to both artifact and source code repositories
across the organization. Protect against internal threat
actors or inadvertently sharing code to public or untrusted
git repositories by limiting the allowed repositories that
developers can publish code to. Hosting your own repositories
might be advantageous depending on your needs, enabling
complete control over available code. Methods such as
pre-commit hooks for git repositories can be used to enforce
these rules effectively.

By enforcing usage of trusted repositories, you ensure that
only secure, vetted code components and artifacts are used,
enhancing software lifecycle stability and security. It also
minimizes the risk of sensitive information being leaked into
untrusted repositories.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.4-grant-access-only-to-trusted-repositories.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.5] Maintain an approved open-source software license list

**Category:** FOUNDATIONAL

Manage and regularly update an allowed and forbidden
open-source software (OSS) licenses list. This list should
reflect which licenses are, or are not, compliant with laws,
regulations, and security requirements applicable to your
organization. Use this list to detect and prevent legal issues
while using open-source components.

Enforce the allowed and forbidden OSS licenses list by continuously assessing all OSS
usage automatically as part of the build process. This can be enforced through quality
assurance testing processes, like scanning the [Software Bill of Materials (SBOM)](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html) with Software Composition Analysis (SCA)
tooling. Continuous enforcement helps to ensure that only approved OSS licenses are used in
the code base, reducing the risk of legal issues and license violations while providing
developers with fast feedback.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.5-maintain-an-approved-open-source-software-license-list.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.6] Maintain informative repository documentation

**Category:** FOUNDATIONAL

Maintaining well-structured and informative repository documentation directly within
the code base promotes collaboration, simplifies onboarding new team members, and improves
the ability to maintain software over time. This documentation, often in the form of
markdown files like `README.md` and `CONTRIBUTING.md`, contains
information about reviewing, building, contributing to, and otherwise using the project and
helps ensure that this knowledge lives where the code does, making it easily accessible and
versioned alongside the code it is applicable to.

Every repository should contain detailed documentation
providing an overview of the project, its purpose,
instructions for building and deploying the project,
guidelines for contributions, and methods for submitting
feedback or issues. For complex projects, the creation of
additional, focused documentation files addressing specific
areas can be beneficial.

**Related information:**

- [What
Is Repo?](https://aws.amazon.com/what-is/repo/)
- [About
READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Common
special files found in the root directory of a
repository](https://github.com/kmindi/special-files-in-repository-root)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.6-maintain-informative-repository-documentation.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.7] Standardize vulnerability disclosure processes

**Category:** RECOMMENDED

A standard vulnerability disclosure policy helps ensure consistent reporting and
handling of potential vulnerabilities, which in turn enhances the security of the software
development lifecycle. Implementing standardized vulnerability disclosure practices is
recommended for optimizing DevOps, as it promotes security, helps manage risk effectively,
and encourages the responsible reporting and handling of discovered vulnerabilities.

A method for implementation is provided in RFC 9116, *A File Format to Aid
in Security Vulnerability Disclosure* (Foudil, Shafranovich, & Nightwatch
Cybersecurity, 2022). This guidance provides a standardized process for vulnerability
disclosure using a machine readable `security.txt` file, which contains contact
details and the vulnerability disclosure policy. This file is to be placed in
the `/.well-known/` path of  a domain name or IP address to enable security
researchers to find the right information to report vulnerabilities they discover easily.

**Related information:**

- [RFC
9116 - A File Format to Aid in Security Vulnerability
Disclosure](https://www.rfc-editor.org/rfc/rfc9116)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.7-standardize-vulnerability-disclosure-processes.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.8] Use a versioning specification to manage software components

**Category:** RECOMMENDED

Apply a versioning specification across all software
components within your development lifecycle. Use a versioning
specification, such as Semantic Versioning (SemVer), to
significantly simplify governance of software governance by
providing a systematic approach to tracking different types of
releases (major, minor, and patch). A well-organized,
versioned code base offers a clear chronological history of
modifications, enhancing manageability, maintainability, and
navigability.

Implementing version pinning for dependencies is a practical use case enabled by
using a versioning specification. By locking dependencies to a specific version or version
range, build reproducibility is ensured. This approach helps ensure the reproducibility of
software builds, but complicates dependency management as developers then need to make
updates to stay up-to-date with security fixes, bug fixes, or other improvements.

Use automated governance dependency management tools to maintain the balance between
stable builds and timely updates. Consider integrating automation mechanisms that can
update versions based on commit messages. For example, if a commit message contains the
keyword `major`, it could trigger an update to the major version number. This
automated approach ensures that versions are updated while minimizing chance for human
error.  It's also possible to automate nightly or weekly upgrades of third-party
dependencies to ensure they are regularly updated and kept secure.

**Related information:**

- [Semantic Versioning
2.0.0](https://semver.org/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.8-use-a-versioning-specification-to-manage-software-components.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.9] Implement plans for deprecating and revoking outdated software components

**Category:** RECOMMENDED

Maintaining an up-to-date and secure code base requires the proactive management of
components, including removing outdated artifacts, libraries, and repositories. Not only
does their removal reduce storage costs, but it also mitigates risks associated with
deploying outdated or potentially vulnerable software. The removal process of outdated
components should comply with the organization's data retention policies.

Develop clear plans for the deprecation and revocation of outdated components. These
plans should include regular audits of the code base to identify deprecated or unused
artifacts, libraries, and repositories. Establish timelines for deprecation and final
removal of identified components. Communicate these plans to your development team and
ensure that they are aware of the timelines.

Consider automating the removal process where feasible, for example, by using scripts
or automated governance tools that support such functionality. By implementing such plans,
you can streamline the code base, making it easier to manage and less prone to errors,
while ensuring security and reducing the risk of system failures.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST04-BP05
Enforce data retention policies](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_data_retention.html)
- [AWS Well-Architected Sustainability Pillar: SUS02-BP03 Stop
the creation and maintenance of unused assets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.9-implement-plans-for-deprecating-and-revoking-outdated-software-components.html*

---

**Capability**: DL.SCM — Software component management

# [DL.SCM.10] Generate a comprehensive software inventory for each build

**Category:** RECOMMENDED

Maintain a comprehensive inventory of the components and dependencies that make up
your software assists with identifying vulnerabilities and managing risks. This inventory,
often taking the form of a [Software Bill of Materials (SBOM)](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html), provides valuable insights into the
composition of your software.

Generate a comprehensive inventory as part of each build. This
forms a continuous record of your software's composition,
enabling quick and efficient identification and management of
potential vulnerabilities or risks. Tracking inventory that is
machine readable enhances visibility and aids in identifying
vulnerabilities and risks, enhancing the security posture of
your software at scale.

Use a tool to create and manage SBOMs, centralizing them with other build artifacts
for easier accessibility. Open-source tool sets provided by Open Worldwide Application
Security Project ([OWASP](https://owasp.org/)) and the [Linux Foundation](https://www.linuxfoundation.org/) offer options for
creating and managing SBOMs in standardized formats.

**Related information:**

- [Exporting
SBOMs with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/sbom-export.html)
- [SPDX
Becomes Internationally Recognized Standard for Software
Bill of Materials](https://www.linuxfoundation.org/press/featured/spdx-becomes-internationally-recognized-standard-for-software-bill-of-materials)
- [Software
Supply Chain Best Practices](https://project.linuxfoundation.org/hubfs/CNCF_SSCP_v1.pdf)
- [OWASP
CycloneDX](https://owasp.org/www-project-cyclonedx/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.10-generate-a-comprehensive-software-inventory-for-each-build.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
