# HNOPS04 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# HNOPS04-BP01 Monitor network service provider maintenance events

Implementing a proactive monitoring and response system for
scheduled network maintenance activities is crucial for minimizing
service disruptions. By establishing a methodical framework to track
maintenance notifications and planned network events, teams can
prepare effectively, strategically schedule necessary changes during
designated maintenance windows, and ensure continuous network
connectivity throughout the process. This systematic approach
enhances operational resilience while reducing the impact of
essential maintenance on critical services

**Desired outcome:**

- Get timely notifications about links connecting the on-premises
data center to the cloud.
- Enables proper planning for scheduled activities, minimizes
service disruptions, and ensures optimal management of hybrid
network connectivity.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Proactive maintenance planning and reduces the risk of
unexpected service disruptions.
- Better coordination during maintenance windows with business
operations, minimizing impact on critical workloads.
- Enhanced visibility into service health and upcoming changes

## Implementation guidance

- Integrate service provider notifications into monitoring and
observability platforms. For example, you can achieve this
using Amazon EventBridge to send AWS Direct Connect
maintenance messages.

## Resources

- [AWS Direct Connect maintenance](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dx-maintenance.html)
- [Monitoring
events in AWS Health with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
- [How
can I get notifications for AWS Direct Connect scheduled
maintenance or events](https://aws.amazon.com/premiumsupport/knowledge-center/get-direct-connect-notifications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops04-bp01.html*

---

# HNOPS04-BP02 Develop automated runbooks and maintain clear documentations

Developing automated runbooks and maintaining clear, comprehensive
documentation ensures that your team can respond effectively to
network events, perform routine maintenance, and troubleshoot issues
across your cloud and on-premises infrastructure.

**Desired outcome:**

- Create a robust, efficient, and consistent operational framework
for managing hybrid network environments.
- Consider comprehensive set of procedures that can be easily
followed and automated where possible, ensuring quick and
accurate responses to network events, routine maintenance tasks,
and troubleshooting scenarios.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Ensures consistency in operations across diverse environments,
reducing the likelihood of errors and improving overall service
quality.
- Enable faster onboarding of new team members and reduce
dependency on specific individuals.

## Implementation guidance

- Identify critical network operational processes and common
incident scenarios in your hybrid network environment.
- Develop clear, step-by-step procedures for each identified
process, ensuring they cover both AWS and on-premises
components.
- Ensure that documentation is easily accessible, regularly
updated, and includes both technical details and business
context.

## Resources

- [OPS07-BP03
Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops04-bp02.html*

---
