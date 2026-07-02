**Saga**: Automated governance
**Capability**: AG.ACG — Automated compliance and guardrails

---

# [AG.ACG.8] Conduct regular scans to identify and remove unused resources

**Category:** RECOMMENDED

Over time, unused resources can often be a byproduct of
experimentation and more frequent deployments, including
dormant servers, unused deployment resources, idle containers,
redundant environments, and unused serverless functions. These
resources can pile up to create a less than ideal operating
environment if not managed effectively, leading to
inefficiencies, inflated costs, system unreliability, and
heightened security risks.

Perform automated scans scoped to all deployed resources in
your environment and pinpoint unused or outdated resources.
This can be accomplished by using health check endpoints,
reviewing logs, using metadata elements such as tags, or
checking billing dashboards for utilization.

Verify the status and compatibility of software running on these resources,
especially if they have been disconnected or powered off for extended periods of time.
These checks are especially useful for preventing *zombie servers*,
which have the potential to be rebooted after long periods of disconnection and might be
running outdated or incompatible software.

Based on the verification results and the organization's
policies, take action to remediate these resources, such as
updating the software, decommissioning the resources, or
integrating them back into the environment. Frequently
performing these scans can prevent potential service
disruptions, maintain up-to-date software across all
resources, and ensure the overall integrity of the DevOps
environment.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST02-BP06
Track project lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage_track_lifecycle.html)
- [Implementing
health checks](https://aws.amazon.com/builders-library/implementing-health-checks/)
- [Decommission
resources - Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/decommission-resources.html)
- [Identifying
your unused resources - DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_UnusedResources.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.8-conduct-regular-scans-to-identify-and-remove-unused-resources.html*
