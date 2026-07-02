**Saga**: Quality assurance
**Capability**: QA.ST — Security testing

---

# [QA.ST.7] Conduct proactive exploratory security testing activities

**Category:** RECOMMENDED

Conduct frequent exploratory security testing activities,
encompassing penetration testing, red teaming, and
participation in vulnerability disclosure or bug bounty
programs.

Penetration tests use ethical hackers to detect vulnerabilities in system or networks
by mimicking potential threat actor actions. These exploratory security tests reveal
weaknesses in the system using the ingenuity of human testers. Deployment pipelines can
trigger the penetration testing process and wait for an approval to help ensure that
vulnerabilities are identified and fixed before code moves to the next stage. Automation
can be used to run repetitive, baseline tests, such as dynamic application security
testing, to enable human testers to focus on more complex scenarios. Review the [AWS Customer Support Policy for
Penetration Testing](https://aws.amazon.com/security/penetration-testing/) before running penetration tests against AWS
infrastructure. Penetration testing is most effective when you need a broad review of the
application or system against known vulnerabilities.

Going beyond the scope of penetration tests, red
teaming emulates real-world adversaries in a full-scale
simulation, targeting the organization's technology, people,
and processes. Red teaming is more focused than penetration
testing, targeting specific vulnerabilities by allocating more
resources, spending more time, and examining additional attack
vectors. This includes potential threats from internal
sources, such as lost devices, external sources like phishing
campaigns, and those arising from social engineering tactics.
This approach provides insights into how threat actors might
exploit weaknesses and bypass defenses in a real-world
scenario. Red teaming evaluates the broader resilience of an
application or system, including its resistance to
sophisticated attacks that span the entire organization's
security posture.

Vulnerability disclosure and bug bounty programs invite external researchers to
examine your software, complementing and often surpassing internal security evaluations.
Researchers who participate in these programs not only identify potential exploits but
also verify them, resulting in higher fidelity findings. The person who identified the
vulnerability does not disclose it publicly for a set amount of time, allowing a patch to
be rolled out before the information is disclosed publicly, and in some cases will receive
compensation for their efforts. These programs foster a culture of openness and continuous
improvement, emphasizing the importance of external feedback in maintaining secure
systems.

The findings from exploratory security testing should be
communicated to development teams as soon as findings are
available, allowing for quick remediation and learning.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC11-BP03 Perform
regular penetration testing](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_perform_regular_penetration_testing.html)
- [Security
in every stage of the CI/CD pipeline: Penetration Testing
and Red Teaming](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/security-in-every-stage-of-cicd-pipeline.html#penetration-testing)
- [AWS Penetration Testing: A DIY Guide for Beginners](https://www.getastra.com/blog/security-audit/aws-penetration-testing/)
- [AWS Customer Support Policy for Penetration Testing](https://aws.amazon.com/security/penetration-testing/)
- [AWS Cloud Security - Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/)
- [AWS BugBust](https://aws.amazon.com/bugbust/)
- [AWS CloudSaga - Simulate security events in AWS](https://github.com/awslabs/aws-cloudsaga)
- [RFC
9116 - A File Format to Aid in Security Vulnerability
Disclosure](https://www.rfc-editor.org/rfc/rfc9116)
- [Amazon's
approach to security during development: Penetration
Testing](https://youtu.be/NeR7FhHqDGQ?t=1432)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.7-conduct-proactive-exploratory-security-testing-activities.html*
