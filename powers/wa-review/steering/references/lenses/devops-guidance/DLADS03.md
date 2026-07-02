**Saga**: Development lifecycle
**Capability**: DL.ADS — Advanced deployment strategies

---

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
