**Saga**: Development lifecycle
**Capability**: DL.CD — Continuous delivery

---

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
