# HNSEC06 — Incident response

**Pillar**: Security  
**Best Practices**: 2

---

# HNSEC06-BP01 Monitor your environment for malicious behavior

Responding to any cyber incident requires the ability to detect
threats and establish a baseline for normal operations in a hybrid
environment. Continuously monitors your environment for malicious
behavior to protect your accounts and workloads.

**Desired outcome:** Quick detection
of malicious activity enables fast containment and limits the impact
of ransomware and other security incidents.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Early identification of threats and abnormal behaviors
- Reduces containment and remediation time
- Enhances overall security posture with automated, continuous
monitoring

## Implementation guidance

- Monitor flow logs, API activity, and DNS logs for threats,
such as using Amazon GuardDuty that monitors and reports
findings from these sources.
- Regularly review and baseline findings to distinguish normal
from abnormal activity.

## Resources

- [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp01.html*

---

# HNSEC06-BP02 Automate incident response

Implement automated response capabilities to enhance incident
containment speed and reliability while reducing manual intervention
requirements. This approach ensures consistent execution of response
procedures while minimizing human error during critical security
events.

**Desired outcome:** Faster, more
reliable containment and recovery from incidents with reduced
operational burden.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Shortens response times and limits damage
- Reduces alert fatigue and manual workload
- Ensures consistent, repeatable incident handling

## Implementation guidance

- Automate incident response by configuring security findings
with response actions. For example, you can achieve this by
integrating AWS Security Hub CSPM findings with AWS Lambda for
automated actions.
- Test and tune automation playbooks in non-production
environments.

## Resources

- [Using
EventBridge for automated response and remediation PDF
RSS](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/automating-security-responses.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp02.html*

---
