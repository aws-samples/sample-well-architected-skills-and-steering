# EUCOPS12 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# EUCOPS12-BP01 Deploy alerting mechanisms that quickly identify anomalous metrics

AWS EUC services provide access to desktops and applications which can be highly
variable in their resource requirements over time. Weekly, monthly, quarterly, and year-end
activities can cause spikes in resource consumption that might result in unnecessary alerts
and a degraded user experience.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

The design and pilot phases of an AWS EUC project should identify resource
requirements for each application set over a typical business cycle. Identify the peak
activity levels to verify that the compute instance types selected for both Amazon WorkSpaces and
WorkSpaces Applications can deliver performance that maintains a good user experience and improves
productivity.

Third party tools from vendors such as ControlUp, Nuvens, LiquidWare, Lakeside
Software, and Aternity can be used to collect resource usage trends and build baselines
for key applications. Some of these can be found on the AWS Marketplace.

AWS and the AWS Partner Network offer many services and automation capabilities you can use
to automatically and elastically scale backend application services or to provide
increased compute capabilities during periods of heavy utilization**.**

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops12-bp01.html*

---

# EUCOPS12-BP02 Define and maintain an alerting chain of command that quickly communicates issues in real time

As important as gathering relevant service metrics and alerts is expediting the
propagation of those alerts to the right teams, individuals, or automated processes. This
propagation helps you quickly surface and remediate associated issues.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Accelerate the awareness of key events, and check that the notification to initiate
the appropriate process of remediation is quickly followed.

There are several ways to verify that both operations and support teams in addition
to internal and external users and management teams are appraised of service health:

- **Health dashboards**: Build a set of centralized service
health dashboards that are tailored to provide the right information to the right
people from operations, support, users, or management. Dashboards help your teams
quickly identify and track issues to resolution. User-level dashboards promote
transparency, reduce support calls, and increase user engagement as new production
services are introduced.
- **Effective communication**: Develop a communications
protocol to effectively communicate about extended outages as they are identified to
internal and external customers. Keeping customers informed, specifically around
outage timelines, is key to building trust and engagement.
- **Effective routing**: Automate the process of
prioritizing and effectively routing the right alerts to the right teams at the right
time, which increases operational efficiency and contributes to an improved user
experience and higher productivity.
- Consider the following factors when identifying roles and responsibilities for
event response, escalation, and propagation:

**Roles and responsibilities**: Define clear lines of
responsibility for escalation, problem resolution, and root cause analysis.
- **Incident assignment**: Identify alert categories so
that specific events can be directed to the team most appropriate to resolve. For
example, first, second, and third lines of support.
- **RPO and RTO requirements**: Involve the business in
understanding and calculating RTO and RPO requirements to prioritize problem
tracking and remediation accordingly.
- **Cost of outages**: Quantify the cost to the
business of specific categories of outage and use this data to inform the
escalation and notification process. It may be pertinent to revise support
processes to involve more skilled support teams to react to specific event types
that have higher business impact.
- **Tool**s: Map out a matrix that identifies the right
tools, metrics, and notification processes to verify that critical events are
surfaced and distributed effectively to the appropriate teams and individuals.
- **Alert fatigue**: Filter out duplicate alerts and
false positives, as they can lead to alert fatigue and loss of focus on important
issues.
- **Geographic reporting**: For multi-Region
deployments, dynamically adjust notification distribution lists to accommodate
support in applicable time zones and geographic areas.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops12-bp02.html*

---
