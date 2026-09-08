# Reliability

**Pillar**: Reliability  
**Questions**: 11

---

# EUCREL01 — Foundations

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL01-BP01 Add redundancy and remove single points of failure in your environment

The principle of assuming that failures will occur represents a
paradigm shift in the approach to designing Amazon WorkSpaces
and WorkSpaces Applications environments. By adopting this mindset,
organizations can prioritize resilience and develop strategies
that minimize the impact of failures, thereby reducing downtime
and mitigating potential business disruptions.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

When designing an Amazon WorkSpaces or WorkSpaces Applications
environment, the approach should prioritize resilience and
minimize the impact of failures by assuming that failures will
occur and implementing robust strategies.

Implement redundancy at every layer of your architecture. This
includes network paths, storage, and virtual desktops. Use
multiple instances of Amazon WorkSpaces or WorkSpaces Applications so
that if one fails, others can take over seamlessly. For
WorkSpaces Applications, use automatic scaling to match the number of
running instances to user demand, keeping performance
consistent even during usage spikes.

Regularly test your failure recovery procedures. Use AWS tools
such as AWS Fault Injection Service to simulate different
failure scenarios and validate your recovery strategies.

Implement robust data backup and disaster recovery plans.
Regularly back up user data and configurations, and verify
that you have a tested recovery plan in place to restore
operations quickly in case of a failure.

Set up comprehensive monitoring using Amazon CloudWatch to
keep track of the performance and health of your WorkSpaces
and WorkSpaces Applications environments. Create alarms and automated
responses to detect and remediate detected issues promptly.

Continuously review and improve your architecture and
operational procedures. Learn from historical incidents and
update your strategies to help prevent future occurrences.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel01-bp01.html*

---

# EUCREL02 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL02-BP01 Use multiple regions for your EUC environment to minimize downtime

[Amazon WorkSpaces Multi-Region Resilience](https://docs.aws.amazon.com/workspaces/latest/adminguide/multi-region-resilience.html) offers cost-effective,
easy-to-manage operational continuity solutions that keep your
users online and productive . Organizations should proactively
design their environment to anticipate failure and plan for a
fast recovery.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Implement Amazon WorkSpaces Multi-Region Resilience to enable
cost-effective and smoothly managed operational continuity.
This approach verifies that users remain online and productive
with minimal recovery time through standby WorkSpaces in
alternative AWS Regions during disruptive events.
Additionally, regularly test your multi-Region setup to verify
its effectiveness in supporting operational continuity.
Conduct failover drills and simulations to validate the RTO
and identify any potential areas of improvement in your
resilience strategy. By using Multi-Region Resilience, you can
minimize service interruptions and provide uninterrupted
access to Amazon WorkSpaces for your users, even during
disruptive events.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel02-bp01.html*

---

# EUCREL03 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL03-BP01 Add redundancy to networking connections

Use a redundant networking architecture for Amazon WorkSpaces and WorkSpaces Applications,
incorporating multiple Active Directory (AD) Controllers, AD connectors, DNS servers,
gateways, VPNs, or AWS Direct Connect links. This approach supports continuous
connectivity by providing alternative pathways for network traffic, reducing the risk of
service disruptions due to network incidents and enhancing overall system resilience.
Redundant networking helps mitigate the impact of network failures and supports
uninterrupted access to WorkSpaces environments.

**Level of risk exposed if this best practice is not
established:**High

## Implementation guidance

Enhance the resilience of Amazon WorkSpaces and WorkSpaces Applications by configuring
redundant networking components such as VPN connections or AWS Direct Connect links.
This setup provides alternative paths for network traffic, mitigating the impact of
network incidents and supporting continuous access to WorkSpaces environments. Verify
that you have multiple AD controllers and connectors across multiple Availability Zones.

Additionally, regularly monitor and test the redundant networking setup to check
its effectiveness in maintaining continuous connectivity. Conduct failover tests and
simulations to validate the redundancy configuration and identify any potential areas
for improvement. By implementing redundant networking architecture, you can strengthen
the resilience of your EUC environment and reduce the risk of downtime caused by network
disruptions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel03-bp01.html*

---

# EUCREL04 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL04-BP01 Establish data integrity with replication and backup strategies

Implement data replication and backup strategies to safeguard user data and
configurations. Use automated backup solutions such as Amazon WorkSpaces Automated
Snapshots to create regular backups of WorkSpaces volumes. Store data backups securely and
verify that you can promptly restore backups in the event of data loss or
corruption.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

To fortify resilience and safeguard data within Amazon WorkSpaces environments, adopt a comprehensive approach to
data replication and backup strategies. Use automated
solutions to regularly capture backups of user data. Store
backups are stored securely, and check that you can readily
access them for prompt restoration in the event of data loss
or corruption.

Additionally, establish a backup retention policy to determine
how long backups are retained, and verify your compliance with
regulatory requirements. Regularly test the effectiveness of
your backup and restoration processes and identify any
potential areas for improvement proactively. By implementing
robust data protection practices, you can strengthen the
resilience of your WorkSpaces infrastructure and protect
valuable user data and configurations, supporting operational
continuity and reducing the risk of data loss.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel04-bp01.html*

---

# EUCREL06 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL06-BP01 Plan for disaster recovery of EUC through testing and procedures

Develop and regularly test disaster recovery plans for Amazon WorkSpaces and AppStream
2.0 deployments. Document procedures for restoring user data and configurations in the
event of disruptive incidents or data loss. Conduct periodic disaster recovery drills to
assess the effectiveness of recovery procedures and verify that you are ready to respond
to unexpected incidents.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

To improve readiness for significant incidents or data loss
incidents in Amazon WorkSpaces and WorkSpaces Applications deployments,
organizations must prioritize the development and regular
testing of disaster recovery plans.

Document procedures for restoring user data and
configurations, including backup and restoration processes,
and verify that this documentation is quickly accessible to
relevant personnel. Additionally, conduct periodic disaster
recovery drills to simulate real-world scenarios and validate
the effectiveness of recovery procedures. Use these drills to
identify areas for improvement in the disaster recovery plan
and take proactive measures to address them.

By investing in proactive disaster recovery planning and
testing, organizations can mitigate the impact of unexpected
events, provide business continuity, and protect valuable data
and resources in their Amazon WorkSpaces and WorkSpaces Applications
environments. These best practices help organizations
strengthen the resilience and availability of their EUC
environments, minimize the impact of potential incidents, and
support continuous access to virtual desktop resources for
users.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel06-bp01.html*

---

# EUCREL07 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL07-BP01 Document changes for transparency and traceability

Maintain comprehensive documentation of all modifications made
to the EUC environment. Document the details of each change,
including the rationale, implementation steps, and anticipated
outcomes. Documentation helps promote transparency and
traceability and provides a reference for future troubleshooting
or auditing purposes.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Thoroughly document all changes made to the Amazon EUC
environment to promote transparency and shared responsibility.
This documentation serves as a valuable resource for
troubleshooting and auditing purposes, providing insights into
the history of changes and facilitating the identification of
potential areas of improvement.

Additionally, consider establishing version control mechanisms
and documentation guidelines to maintain consistency and
facilitate collaboration among team members. By prioritizing
comprehensive change documentation, organizations can enhance
transparency, foster shared responsibility, and streamline
troubleshooting and auditing processes in their WorkSpaces and
WorkSpaces Applications environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel07-bp01.html*

---

# EUCREL08 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL08-BP01 Test and validate changes to promote reliable deployment

Thoroughly test and validate changes in an isolated environment
before implementing them in the production environment for
Amazon WorkSpaces and WorkSpaces Applications. By conducting testing in a
controlled environment, organizations can assess the impact of
changes on WorkSpaces and application availability under
conditions that closely resemble real-world usage scenarios.
This approach evaluates whether the changes achieve the desired
outcomes before deployment.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Before implementing changes in the production environment for
Amazon WorkSpaces and WorkSpaces Applications, test and validate the
changes in a controlled testing environment. Test changes
under conditions resembling real-world usage scenarios to
assess their impact on availability, performance, and
functionality.

Validate that changes achieve desired outcomes and identify
any potential areas for improvement or dependencies.
Additionally, consider implementing automated testing
frameworks and deployment pipelines to streamline the testing
and validation process and maintain consistency in testing
procedures across different environments.

By prioritizing comprehensive testing and validation,
organizations can reduce the risk of service interruptions and
issues during deployment, supporting smooth transitions and
maintaining the stability and performance of their EUC
environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel08-bp01.html*

---

# EUCREL09 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL09-BP01 Implement and test rollback plan for every change you make in EUC environments

Develop rollback plans for changes in Amazon WorkSpaces and
WorkSpaces Applications to anticipate and address potential failures and
their impacts to system stability or resilience. By establishing
these plans, businesses can proactively address unforeseen
situations that may arise during implementation, creating a
smooth transition back to previous configurations if needed.
Test rollback procedures beforehand to gain insights into their
effectiveness and identify any potential areas of improvement.
This proactive approach minimizes service interruptions and
facilitates prompt recovery from incidents or failures,
supporting continuous service delivery and reducing impact on
users.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Develop rollback plans for changes that could potentially
impact WorkSpaces and WorkSpaces Applications resiliency or stability.
Define procedures for reverting to the previous state if a
change causes unexpected incidents or service disruptions.
Test and validate rollback plansto verify their effectiveness
and minimize the time required to restore service in such
situations in the event of a rollback.

Additionally, consider implementing automated rollback
mechanisms where feasible to streamline the recovery process
and reduce manual intervention. By prioritizing rollback
planning and testing, organizations can enhance their ability
to respond effectively to unexpected challenges and maintain
continuous operations in their EUC environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel09-bp01.html*

---

# EUCREL10 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL10-BP01 Implement communication plans with EUC environment stakeholders

Include WorkSpaces and WorkSpaces Applications users, administrators, and
support teams in your communications. Provide advance notice of
scheduled maintenance windows or change activities to minimize
potential service interruptions for users. Coordinate with other
teams or departments as necessary to implement changes smoothly
and with minimal impact on related systems or services.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Effective communication and coordination are critical
components in minimizing service interruptions for end users
during periods of change. Establish clear communication
channels.

Begin by identifying all stakeholders involved, including
users, administrators, support teams, and any other relevant
parties. Develop a comprehensive communication plan outlining
how and when stakeholders will be informed of changes. Use
various channels such as email, in- system announcements, or
dedicated communication systems to facilitate timely
notifications.

Transparency is key, so communicate changes clearly, and
provide rationale, expected impact, and necessary
instructions. Additionally, establish a feedback mechanism for
stakeholders to express concerns or ask questions. Keep
stakeholders informed with regular updates on implementation
progress and timelines.

By prioritizing communication and coordination, you can
minimize disruptions and support a smooth transition process
for all involved.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel10-bp01.html*

---

# EUCREL11 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL11-BP01 Implement post-change assessment to evaluate impact and optimize performance

After implementing changes, conduct a post-change assessment
to assess their impact on the resiliency and performance of
your EUC services. Monitor key metrics and user feedback to
identify any potential areas for optimization or adjustment
that may have resulted from the changes. Use post-change
evaluations to inform continuous improvement efforts and
refine future change management processes.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

In the post-change evaluation process, establish clear
objectives to focus on while you assesse the impact of your
changes on resiliency and performance. Continually monitor key
metrics such as latency, resource utilization, and system
stability to evaluate the effects of changes on your EUC
environments accurately.

Additionally, gather feedback from users regarding their
experience with the implemented changes to gain valuable
insights into usability and functionality. Comparing
post-change metrics with baseline data helps identify
significant deviations or improvements, facilitating a
thorough assessment of change impact.

Ultimately, the insights gained from post-change evaluations
should drive continuous improvement in change management
processes. By using evaluation results to refine procedures
and enhance the resilience and performance of EUC environments
over time, organizations can effectively adapt to evolving
needs and challenges.

By following these change management practices, organizations
can effectively manage changes to their EUC environments,
maintain service availability and resiliency, and reduce the
risk of service interruptions or incidents that could impact
users' access to virtual desktop resources.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel11-bp01.html*

---

# EUCREL12 — Failure management

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL12-BP01 Develop an EUC-specific incident response plan that improves reliability in your environment

When developing incident response plans for Amazon WorkSpaces
and WorkSpaces Applications, it's important to address their unique
characteristics such as the session-based nature of AppStream
2.0 and the persistent data in WorkSpaces. Plans should include
strategies for handling issues with scaling, session failures,
and network dependencies like VPCs or AWS Direct Connect. Active
Directory integration is crucial for both services, so steps for
troubleshooting authentication failures or AD synchronization
must be detailed. The plan should also account for
Region-specific outages, using cross-Region backups or failover
mechanisms for user data and application availability.

Additionally, document user connectivity issues and regular
backups to provide seamless recovery and data protection. Verify
that the incident response plans are comprehensive, covering
procedures for responding to various types of incidents or
events specific to WorkSpaces and WorkSpaces Applications. Collaborate
with key stakeholders in the process to gather insights into
potential scenarios and verify alignment with organizational
goals. Regularly review and refine these plans to incorporate
lessons learned and evolving requirements, maintaining their
effectiveness and relevance over time.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

When developing incident response plans for Amazon WorkSpaces
and WorkSpaces Applications, customize them to suit the specific
features and challenges posed by these cloud services. Verify
that these plans are thorough, encompassing procedures for
addressing various incidents or situations specific to
WorkSpaces and WorkSpaces Applications.

Collaborate with key stakeholders to gather valuable insights
and align plans with organizational objectives. Document
comprehensive procedures, clearly define roles and
responsibilities, establish effective communication channels,
prioritize incidents based on severity, and set response
timelines.

Regularly review and update these plans to incorporate lessons
learned and evolving requirements, improving their ongoing
effectiveness and relevance. This structured and inclusive
approach fosters readiness to respond swiftly and effectively,
bolstering overall system reliability and resilience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel12-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
