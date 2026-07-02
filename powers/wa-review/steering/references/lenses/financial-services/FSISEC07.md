**Pillar**: Security

# FSISEC07: How are you inspecting your financial services infrastructure and network for unauthorized traffic?

Monitor network traffic for expected and unexpected traffic to
identify irregularities and gain key insights into the
security of the system. For example, a poorly-performing
network can indicate that the network is under threat, and
irregular attempts to contact unexpected external systems can
indicate that an internal host has been compromised. With
generative AI services, inspection includes monitoring AI
endpoint access and authentication attempts, model
invocations, and data flow patterns.

## FSISEC07-BP01 Monitor instance traffic

Amazon EC2 instances automatically track aggregate network
inbound and outbound traffic with Amazon CloudWatch.
[Use
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) and push log files to Amazon CloudWatch for storage, aggregation, reporting, and alert
notification.
[Create
profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) for the expected network behavior
for each EC2 instance and
[generate
alarms when deviations are detected](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html). For
example, system or web logs sent to Amazon CloudWatch Logs
could generate alarms based on the number of login failures
or web request latencies. Similarly, TCP connection or
outstanding connection request counts could be stored in
Amazon CloudWatch and used to detect security threats like
SYN flood threats.

For AI workloads, implement comprehensive monitoring of
model endpoint access and API usage patterns while
establishing private network communication and tracking data
access across AI systems.

## FSISEC07-BP02 Use VPC Traffic Mirroring

Use
[VPC
Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html) to copy network traffic from
an elastic network interface of Amazon EC2 instances and
forward that traffic to security and monitoring appliances for
use cases such as content inspection, threat monitoring, and
troubleshooting. These security and monitoring appliances can
be deployed on a fleet of instances behind a Network Load
Balancer (NLB) with a User Datagram Protocol (UDP) listener.
Amazon VPC traffic mirroring supports traffic
[filtering](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html)
and packet truncation, allowing you to extract traffic that you
are interested in monitoring. It also addresses challenges
around having to install and run packet-forwarding agents on
EC2 instances. Packets are captured at the Elastic Network
Interface level, which cannot be tampered with from the user
space, thus offering better security posture.

## FSISEC07-BP03 Use immutable infrastructure with no human access

Immutable infrastructure is a model in which no updates,
security patches, or configuration changes happen in place on
production systems. If changes are needed, a new version of
the architecture is built and deployed. Because changes aren't
allowed in immutable infrastructure, you can be confident in
the deployed system. Immutable infrastructures are more
consistent, reliable, and predictable, and they simplify many
aspects of software development and operations by minimizing
common issues related to mutability.

Adopt
[immutable
infrastructure](https://aws.amazon.com/blogs/mt/leveraging-immutable-infrastructure-nubank/) practices with no human
access to better adhere to your audit and compliance needs.
You can version control your infrastructure, and handling
failure becomes a routine and continual way of doing business.

## FSISEC07-BP04 Allow interactive access for emergencies only

Tightly control and monitor interactive access to EC2
instances. Interactive access should typically be provided for
emergency-only,
[break-glass](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/break-glass-access.html)
scenarios.

Test and review these pre-staged emergency user accounts,
which normally are highly privileged and could be limited to
read only. Limit the time duration of break-glass procedure
and the password time duration. Have a ticketing system with
procedures requiring that an acceptable form of authentication
be provided by the requester and recorded before the accounts
are made available. This helps control and reduce the account's misuse, having only pre-approved
personnel who complete a certain emergency task. The
break-glass accounts and distribution procedures must be
documented and tested as part of implementation and carefully
managed to provide timely access when needed. A special audit
trail needs to be in place to monitor such emergency access
for later audit and review.

Use
[AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) to provide
an interactive, one-click browser-based shell to your Amazon EC2 instances, on-premises instances, and virtual machines
(VMs). Session Manager provides secure and auditable instance management without the
need to open inbound ports, maintain bastion hosts, or manage
SSH keys.

### Prescriptive guidance

- Publish and view statistical graphs of your own metrics
with Amazon CloudWatch. For more details, see
[Publishing
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html).
- You can use the CloudWatch feature of Anomaly Detection,
which analyzes past metric data to create a model of
expected values. The steps for that implementation is
described in the following documentation:
[Implement CloudWatch alarms based on anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html).
- Enable traffic mirroring to analyze the selected traffic
from a mirror source sent to a mirror target. For more
information, see
[Get
started with Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-getting-started.html).
- To adopt a strategy of immutable servers, see the
following blog post:
[Create immutable servers using EC2 Image Builder and AWS CodePipeline](https://aws.amazon.com/blogs/mt/create-immutable-servers-using-ec2-image-builder-aws-codepipeline/).

## Resources

**Related documents:**

- [Leveraging AWS CloudFormation to create an immutable infrastructure](https://aws.amazon.com/blogs/mt/leveraging-immutable-infrastructure-nubank/)
- [Managing temporary elevated access to your AWS environment](https://aws.amazon.com/blogs/security/managing-temporary-elevated-access-to-your-aws-environment/)

**Related videos:**

- [AWS re:Invent 2022 - A deep dive on the current security threat landscape with AWS](https://www.youtube.com/watch?v=h7WvCyygb8U)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec07.html*
