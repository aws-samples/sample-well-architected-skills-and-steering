**Saga**: Automated governance
**Capability**: AG.ACG — Automated compliance and guardrails

---

# [AG.ACG.6] Implement auto-remediation for non-compliant findings

**Category:** RECOMMENDED

Manual identification and remediation of non-compliance issues
can be time-consuming and prone to errors. Automated systems
can rapidly respond to non-compliant resources,
misconfigurations, and insecure defaults as soon as they are
detected.

In the event of a non-compliance issue, an auto-remediation
process should be triggered, which not only resolves the
immediate issue but also initiates an alert to the developers.
This is important because, while the auto-remediation resolves
the problem at the system level, the developers need to be
made aware of the problem so that they can correct the source
of the error and prevent its recurrence. This dual approach of
auto-remediation and developer notification promotes a
learning environment and reduces the likelihood of recurring
non-compliance issues. It allows developers to address the
root cause of the configuration drift or non-compliance to
prevent the continual reintroduction of the same error.

While recommended for its efficiency and rapid response,
auto-remediation is not universally applicable to all
compliance issues. Certain issues might require manual
intervention or a more nuanced approach. Use preventative
guardrails and implementing detective and preventative
controls directly within the development lifecycle where
possible, with auto-remediation being a third best option.
These measures, when used together, yield a more compliant
environment.

The goal of auto-remediation should not just be the swift
resolution of issues, but also the continued education of
developers while reducing the overall incidence of
non-compliance.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP06 Monitor
and alarm proactively](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_monitor_instances_post_launch_proactive.html)
- [AWS Well-Architected Reliability Pillar: REL06-BP04 Automate
responses (Real-time processing and alarming)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_automate_response_monitor.html)
- [Remediating
Noncompliant Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [Automated
Security Response on AWS](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/)
- [Automating
ongoing OS patching - AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/automating-os-patching.html)
- [Decommission
resources - Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/decommission-resources.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.6-implement-auto-remediation-for-non-compliant-findings.html*
