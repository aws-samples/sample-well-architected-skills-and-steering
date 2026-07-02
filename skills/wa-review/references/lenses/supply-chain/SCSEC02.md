# SCSEC02 — Security foundations

**Pillar**: Security  
**Best Practices**: 2

---

# SCSEC02-BP01 Track cloud resources and enforce compliance with automation

Implement automated monitoring systems to continuously track and
inventory all cloud resources throughout your supply chain
environment. Establish compliance guardrails with automated
enforcement mechanisms that validate configurations against
security and regulatory requirements before deployment.

Use automation to regularly audit existing resources, detect drift
from approved configurations, and remediate non-compliant
resources without manual intervention. This approach maintains
consistent governance across your supply chain while reducing the
operational burden of compliance management.

**Desired outcome:** Continuous
compliance tracking and automated remediation across multiple
accounts and regions.

**Benefits of establishing this best
practice:** Real-time detection, automated fixing of
non-compliant configurations, reduced risk of non-compliance and
improved efficiency in managing regulatory requirements.

**Level of risk exposed if this best
practice is not established:** high

## Implementation guidance

Configure AWS Config rules to evaluate resources on a periodic
or real-time basis for continuous compliance monitoring, while
utilizing AWS Config and its proactive mode to automatically
track and remediate resource configurations for continuous
compliance across accounts and regions.

Enable AWS Security Hub CSPM standards and controls to continuously
evaluate if security requirements are met across your supply
chain environments, and Implement automated workflows to route
security findings from AWS Security Hub CSPM to your incident
response and remediation processes.

### Implementation steps

- Deploy AWS Config across the accounts and regions in your
supply chain environment, configuring both periodic and
change-triggered evaluation rules to monitor resource
configurations against compliance standards.
- Activate AWS Config's proactive mode to automatically
remediate non-compliant resources, making sure
configurations consistently meet security requirements
without manual intervention.
- Enable relevant AWS Security Hub CSPM standards (such as CIS
AWS Foundations, AWS Foundational Security Best Practices,
and industry-specific frameworks) to comprehensively
evaluate security posture across your supply chain
accounts.
- Create custom Security Hub CSPM insights that focus
specifically on supply chain-critical resources and
configurations to prioritize security findings relevant to
your business operations.
- Implement automated workflows using EventBridge and Lambda
to route Security Hub CSPM findings to appropriate teams,
ticketing systems, and remediation processes based on
severity and resource type.
- Establish dashboards and regular reporting mechanisms that
provide visibility into compliance status, trends, and
remediation effectiveness across your supply chain
environment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec02-bp01.html*

---

# SCSEC02-BP02 Aggregate findings and metrics to maintain centralized visibility

Centralizing security findings and metrics across your distributed
supply chain environment provides comprehensive visibility into
your overall security posture and enables more effective risk
management. By aggregating data from multiple sources, accounts,
and regions into unified dashboards, security teams can quickly
identify patterns, prioritize threats, and coordinate response
efforts across the entire supply chain environment.

This consolidated approach minimizes blind spots that often exist
between different supply chain components and trading partners,
allowing for faster detection of potential security incidents and
compliance issues. Maintaining centralized visibility also
supports more informed decision-making by providing executives and
stakeholders with clear, actionable insights into the security
health of the supply chain network.

**Desired outcome:** Consolidated
view of compliance status across the entire supply chain
infrastructure.

**Benefits**
**of establishing this best
practice:** Enhanced decision-making capabilities and
faster response to compliance issues.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use AWS Config's aggregated view to get a consolidated
compliance picture across multiple AWS accounts and Regions,
while AWS Security Hub CSPM provides a comprehensive view of your
high-priority security alerts and compliance findings from
across AWS accounts.

Integrate compliance data from AWS services into centralized
dashboards and reporting tools for visibility into your overall
supply chain security posture.

### Implementation steps

- Configure AWS Config aggregators to consolidate compliance
data from all supply chain accounts and regions into a
designated security account, providing a unified view of
resource configurations and compliance status.
- Enable AWS Security Hub CSPM in all accounts and establish a
central administrator account to aggregate security
findings, with customized security standards specific to
supply chain operations.
- Implement automated tagging strategies for all resources
to categorize them by supply chain function, allowing for
more granular filtering and analysis of security findings.
- Create custom Amazon CloudWatch dashboards that integrate
metrics from multiple AWS services (Config, Security Hub CSPM,
Amazon GuardDuty, and Amazon Inspector) to visualize
security trends and compliance status across your supply
chain.
- Develop automated reporting workflows using Amazon EventBridge, AWS Lambda, and Quick to generate
and distribute regular security posture summaries to
stakeholders based on their roles and responsibilities.
- Establish integration points between AWS security services
and external SIEM or GRC systems to incorporate supply
chain security data into enterprise-wide risk management
processes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec02-bp02.html*

---
