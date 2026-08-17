# Reliability

**Pillar**: Reliability  
**Questions**: 4

---

# TELCOREL01 — Foundations

**Pillar**: Reliability  
**Best Practices**: 1

---

# TELCOREL01-BP01 Conduct regular load and failure tests to validate resilience on node, interface, and infrastructure levels

Implement a comprehensive testing strategy that evaluates network resilience through
simulated failures of nodes, interfaces, and infrastructure components. This includes testing in
both lower environments and production during maintenance windows to identify potential
weaknesses, validate redundancy measures, and verify recovery procedures. The testing should
cover both individual component failures and complex failure scenarios that could impact network
services.

**Desired outcomes**

- Identify single points of failure in terms of critical nodes and interfaces that, if
they fail, could impact network availability.
- Evaluate network resilience measures and ability to continue providing services to the
end user in case of multiple failure scenarios.
- To identify potential performance degradations that may arise due to increased traffic
loads.
- Verify effectiveness of redundancy and failover mechanisms.
- Document system behavior and recovery patterns.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

It is essential to regularly test and validate the system's ability to withstand
failures, maintaining a reliable and resilient telecom network. This includes defining the
test scenarios that cover both network function, interfaces and infrastructure-level failures.
Automate the testing and monitoring processes utilizing fault and traffic simulator functions.
Define clear success criteria, measurement metrics, and standard documentation practices, to
analyze the test results and identify patterns and vulnerabilities. By proactively validating
the network's ability to withstand and recover from various failure scenarios, CSPs can verify
continuous service availability and meet regulatory requirements for reliability.

### Implementation steps

- Define test scenarios for both network function and infrastructure failures:

For the network function connectivity failures, Amazon CloudWatch can be used to
monitor connectivity, latency, and error rates for your network interfaces and
connections.
- For infrastructure failures, you could leverage Amazon CloudWatch to track the metrics
and alarms on your critical AWS resources like EC2 instances, EBS volumes, and
network interfaces.

- Create inventory of critical components:

Use AWS Config to maintain a comprehensive inventory of your AWS resources and
their dependencies.
- Document interconnections and potential failure impacts using AWS CloudFormation
templates or other standard infrastructure as code (IaC) configuration files.

- Design individual component failure tests:

Automate failure simulations using AWS Lambda functions or AWS Fault Injection Service to test
hardware, software, and network issues.
- Define expected behavior and recovery procedures using Amazon CloudWatch alarms, and
AWS CloudFormation stacks.

- Develop complex failure scenarios:

Use auto scaling to model cascading failures, regional outages, and
multi-component disruptions.
- Test resilience by injecting faults across your AWS infrastructure using the
AWS Fault Injection Service.

- Establish success criteria:

Measure downtime, recovery time, and service quality metrics using Amazon CloudWatch
dashboards and alarms.
- Use Amazon CloudWatch alarms to set thresholds.

- Document and analyze results:

Define templates and formats for recording
test results, observations, and findings. Include detailed information about test
conditions, system behavior, and performance metrics.
- Review test results to identify common failure modes,
systemic issues, and potential vulnerabilities. Look for patterns that might
indicate underlying architectural or operational weaknesses.
- Document and analyze the time required for system
recovery under various failure scenarios. Compare results against service level
objectives and identify areas for improvement.
- Assess the effectiveness of automated recovery
mechanisms, failover procedures, and list down manual interventions. Identify gaps
in current procedures and opportunities for enhancement.
- Create a prioritized list of areas requiring
attention, including system improvements, process changes, and documentation
updates.

## Resources

**Key AWS services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Fault Injection Service](https://aws.amazon.com/fis/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel01-bp01.html*

---

# TELCOREL02 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 5

---

# TELCOREL02-BP01 Deploy user plane functions in a distributed architecture and highly available configuration

Follow a distributed architecture approach to deploy user plane nodes across multiple
geographical locations with built-in redundancy. Such a design maintains service continuity
through redundant instances and geographical distribution, minimizing the impact of localized
failures or outages while optimizing network performance through efficient load distribution.

**Desired outcome:**

- Achieve high availability on critical network functions.
- Minimized impact from localized failures.
- Optimized network performance.
- Reduced exposure to regional outages.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Implement a distributed and redundant architecture for the user plane functions that can
withstand regional service degradations or outages. This involves deploying redundant
instances of user plane network functions across multiple geographical locations. Within each
site, utilize strategies such as active-active or active-standby configurations, automated
health monitoring, and failover strategy. Comprehensive monitoring and data visualization
tools provide visibility into the network's performance and availability, enabling
rapid identification and response to potential issues. Geographical distribution of these
functions, based on user demands and regulatory requirements enhance the resilience and
responsiveness of the telecom infrastructure by reducing exposure in case of failure.
Automating failover mechanisms, with thresholds and triggers defined by the network management
systems, verifies that the network can quickly recover from failures without disrupting
service to end users.

### Implementation steps

- Deploy redundant instances across multiple Availability Zones:

Deploy your 5G network architecture across multiple AWS Regions, Availability
Zones, and Outposts where possible.
- Use AWS Auto Scaling and Amazon CloudWatch to monitor and scale your network function
instances based on real-time and projected traffic patterns.

- Implement redundancy patterns:

Deploy your user plane functions as Auto Scaling groups with Amazon EC2 instances in
an active-active or active-standby configuration.
- Use Amazon CloudWatch for automated instance health monitoring and failover.

- Establish monitoring:

Deploy Amazon CloudWatch to capture and analyze performance and availability metrics
across your distributed instances.

- Implement geographical distribution:

Choose AWS Regions and Availability Zones based on user distribution,
regulatory requirements, and disaster recovery needs.
- Evaluate AWS network connectivity options, such as AWS Direct Connect and Site-to-Site VPN,
to optimize inter-region communication.

- Configure automatic failover:

Use Amazon CloudWatch alarms and metrics to define infrastructure and application-level
thresholds for initiating automated failover.
- Integrate with your 5G network management systems to correlate failures and
trigger appropriate responses.

## Resources

**Key AWS services:**

- [Amazon EKS](https://aws.amazon.com/pm/eks/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [AWS Local
Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp01.html*

---

# TELCOREL02-BP02 Implement full mesh between control plane and user plane functions

Implement a resilient architecture design where each control plane node can manage user
plane functions in a mesh configuration. For each user plane function, one control plane node
will be active at a time. The control plane node should be designed to have enough capacity to
control the user plane nodes, when needed. This verifies that if one or multiple control plane
nodes fail, the remaining nodes can manage user plane functions without service interruption.
The design incorporates high-capacity centralized control components with distributed user plane
functions.

**Desired outcome:**

- Enhanced system resilience through redundant connectivity.
- Remove single points of failure in control plane.
- Seamless failover during node failures.
- Maintained service continuity.

**Level of risk exposed if this best practice is not established:**
Low

## Implementation guidance

A full mesh connectivity design between the control plane and user plane components is
recommended for a highly available Telcom network. Implementing diverse routing paths and
continuously monitoring the status of these connectivity routes are key steps. Defining clear
failover triggers and thresholds, along with automated recovery procedures, allows the network
to quickly respond to and recover from failures. Thorough documentation of these processes,
including integration with incident management and troubleshooting guides, further enhances
the reliability of the overall system. Comprehensive monitoring and observability solutions
provide the necessary visibility into the network's performance and health, enabling proactive
identification and mitigation of potential issues.

### Implementation steps

- Design mesh topology:

Use AWS Transit Gateway to enable connectivity between your control and user plane
network functions in a star topology, enabling each control plane node to be able to
manage the user plane node, when needed.
- Verify capacity planning and failure domain considerations using Amazon CloudWatch and
AWS Auto Scaling.

- Implement connectivity paths:

Deploy control plane and user plane instances across multiple AWS
Availability Zones and Regions where possible.
- Configure diverse routing paths using AWS VPC routing tables and AWS Transit Gateway
routing policies.
- Leverage AWS Direct Connect for physical path separation and high-performance
connectivity with the on-premises systems including Access Network (RAN) functions.

- Configure routing policies:

Implement routing policies using AWS Transit Gateway route tables and AWS Lambda-based
custom routing logic to recover services in case of a control plane node failure.

- Define failover triggers:

Use Amazon CloudWatch alarms and metrics to define the conditions and thresholds for
triggering automated failover processes.
- Provide manual override capabilities through AWS Lambda functions or Amazon API Gateway.

- Document procedures:

Store the detailed failover and recovery procedures in AWS Systems Manager for secure
access and versioning.
- Integrate the documentation with your incident management processes and provide
troubleshooting guides and escalation procedures.

## Resources

**Key AWS services:**

- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
- [Amazon VPC](https://aws.amazon.com/vpc/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Direct Connect](https://aws.amazon.com/directconnect/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp02.html*

---

# TELCOREL02-BP03 Implement a flexible network function (NF) design to leverage available infrastructure resources for autoscaling

Designing a flexible network function design enables the telecom network to dynamically
scale its resources based on the availability of suitable instance types in the deployment
region. This approach avoids issues like `Insufficient Capacity Error` that can occur when
the required instance type is not available, by using alternative instance types that
can be provisioned. The architecture should be able to automatically adapt to the most
suitable instance types that are present, allowing the network to scale up or down as needed
without being constrained by the availability of a specific instance configuration.

**Desired outcome:**

- Improving the probability of a successful on-demand scale-out in case of traffic surge
or failover trigger.
- Network functions can scale seamlessly by utilizing the most suitable instance types
that are available in the deployment region.
- Remove the risk of scaling failures due to `Insufficient Capacity Error` when
the preferred instance type is not available.
- Verifies continued service availability and responsiveness by maintaining the ability
to scale the network functions as needed.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

To build a flexible and scalable telecom network architecture, a modular and
containerized approach to network functions is recommended. This involves decomposing network
functions into independently scalable components, packaged as container images, and
orchestrating them on a Kubernetes-based solution. Dynamic scaling and efficient resource
utilization are enabled using a Kubernetes cluster autoscaler, which provisions appropriate
instance types based on component requirements. Flexible scaling policies, comprehensive
monitoring, failover mechanisms, and thorough documentation verify the network can adapt to
changing demands, optimize resource utilization, and maintain overall resilience and
reliability.

### Implementation steps

- Design a modular and containerized network function architecture:

Use a microservices-based approach to decompose network functions into smaller,
independently scalable components.
- Package each network function component as a container image to enable
flexibility in deployment and scaling.

- Implement Kubernetes-based orchestration for network functions:

Deploy the network function components on Amazon EKS.
- Integrate the Karpenter open-source Kubernetes cluster autoscaler with your EKS
cluster.
- Configure Karpenter to automatically provision the appropriate instance types
based on the resource requirements of the network function components.

- Monitor resource utilization and scaling events:

Use Amazon CloudWatch to monitor the performance and resource utilization of the network
function components.
- Analyze scaling events, instance provisioning, and capacity fluctuations to
optimize the scaling policies and Karpenter configurations.

- Implement failover and self-healing mechanisms:

Configure Kubernetes health checks and readiness probes to detect and replace
unhealthy network function instances.

- Document scaling procedures and best practices:

Maintain comprehensive documentation on the flexible network function
architecture, scaling policies, and Karpenter configuration.
- Establish guidelines for updating the scaling policies and Karpenter
configurations as the instance type availability changes over time.

## Resources

**Key AWS services:**

- [Amazon EKS (Elastic Kubernetes Service)](https://aws.amazon.com/pm/eks/)
- [Karpenter
(open-source Kubernetes cluster autoscaler)](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html)
- [Amazon CloudWatch for monitoring and
observability](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp03.html*

---

# TELCOREL02-BP04 Introduce an SCTP load balancer designed for control-plane network functions, carrier-grade performance, and high availability

The major public cloud services providers lack native support for load balancing of the
Telecom services that rely on control-plane signaling protocols like SCTP (Stream Control
Transmission Protocol). It is recommended to introduce a cloud-based SCTP Load Balancer for
control plane network functions, designed specifically for telco workloads in the public cloud.
Such a solution will provide SCTP protocol awareness, including support for multi-homing and
association management, along with carrier-grade performance. The load balancer should also
deliver high availability through failover and health checks, maintaining reliable and scalable
operation of critical telecommunications components deployed in the public cloud.

**Desired outcome:**

- Provide a cloud-based SCTP load balancing solution specifically designed for telco
control plane workloads.
- Offer built-in support for the SCTP protocol in the network functions, including
features like multi-homing, stream multiplexing, and association management.
- Verify high availability through redundancy, failover capabilities, and health
monitoring.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

To enhance the reliability of telecom networks, an SCTP load balancing solution should be
onboarded and deployed. This load balancer should incorporate SCTP-specific features, verify
high throughput and low latency, and be implemented with high availability and fault tolerance
through redundant deployments and automated failover. Integrate the load balancer with
Kubernetes-based network functions, optimize for carrier-grade performance, and implement
comprehensive monitoring and automation practices to deliver a reliable and responsive telecom
infrastructure.

### Implementation steps

- Select an SCTP load balancer:

Research and evaluate available SCTP load balancer solutions that offer the
required features, such as multi-homing, stream management, and association
tracking. Verify the selected product can scale to handle the throughput and latency
requirements of telco control plane workloads.

- Implement high availability and fault tolerance:

Deploy the SCTP load balancer across multiple AWS Availability Zones for
redundancy.
- Configure health checks and automated failover mechanisms to verify continuous
service availability.
- Use AWS Auto Scaling to dynamically scale the load balancer instances based on
traffic patterns.

- Optimize for carrier-grade performance:

Configure the SCTP load balancer to optimize for the specific requirements of
telco control plane workloads.

- Implement comprehensive monitoring and observability:

Use Amazon CloudWatch to monitor the SCTP load balancer's performance, availability,
and error metrics.
- Configure Amazon CloudWatch alarms and Amazon SNS notifications for proactive alerting and
incident management.

## Resources

**Key AWS services:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp04.html*

---

# TELCOREL02-BP05 Optimize failure recovery timers for the shared tenancy and potential for transient network issues in cloud environments

Many telecom network function vendors implement health monitoring thresholds based on
on-premises architectural assumptions, where redundant network interfaces and multiple physical
network paths may exist between components. However, when these telecom network functions are
deployed in cloud environments, the underlying network is a shared resource with a single
connection. This can lead to frequent connection alarms and service disruptions due to transient
network issues or single point of failure events, even though the network function itself may
remain functional. It is recommended to proactively engage with telecom ISVs and Network
Function developers to optimize the timers and behaviors used for health monitoring and failure
recovery. This includes designing network architecture to be resilient to packet losses or
higher latencies over the underlying network.

**Desired outcome:**

- Verify the network functions can effectively detect, react, and recover from network
issues and failures.
- Optimize the health monitoring and failure recovery timers to strike the right balance
between prompt failure detection and resilience against false positives.
- Use cloud capabilities to supplement vendor-provided failure detection and
recovery mechanisms.
- Maintain high availability and service continuity for critical telco network functions
despite the dynamic and shared nature of the cloud infrastructure.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Work closely with network function vendors to optimize health monitoring and failure
recovery mechanisms for cloud-based deployments. Implement multi-layered monitoring,
dynamically adjust failure detection timers, and integrate vendor-provided recovery procedures
with cloud-based automation. Validate and test the failure recovery processes, then
continuously monitor performance and collaborate with vendors to further refine the
configurations over time.

### Implementation steps

- Collaborate with network function vendors:

Engage with the network function vendors to understand their default health
monitoring and failure recovery mechanisms.
- Work with the vendors to customize and optimize the monitoring and recovery
timers based on the cloud solutions and NF failure modes.

- Implement multi-layered health monitoring:

Leverage Amazon CloudWatch to set up comprehensive monitoring of the network function
instances, including resource utilization, network performance, and
application-level metrics.
- Configure Amazon CloudWatch alarms to detect anomalies and potential failure conditions,
with customized thresholds and rules.
- Implement AWS Lambda-based health check functions to perform more advanced
application-level checks, accounting for the specific requirements of the telco
network functions.

- Optimize failure detection timers:

Work with the network function vendors to fine-tune the health check intervals,
failure detection thresholds, and recovery timeouts.
- Balance the need for prompt failure detection with resilience against transient
issues that can trigger false positives.
- Use Amazon CloudWatch and AWS Lambda to implement dynamic timer adjustments based on
observed patterns and cloud infrastructure conditions.

- Enhance failure recovery mechanisms:

Integrate the network function vendor-provided recovery procedures with
AWS-native capabilities, such as Amazon EC2 Auto Scaling, Amazon EKS, and AWS Lambda.
- Develop automated recovery workflows using AWS Step Functions or AWS Lambda to handle
different types of failures and verify consistent, reliable recovery.
- Implement rollback and self-healing mechanisms to verify that the network
functions can recover to a known good state.

- Validate and test the failure recovery:

Use AWS Fault Injection Service to inject various types of failures and network issues into
the environment.
- Monitor the health monitoring and failure recovery mechanisms, and fine-tune
the timers and thresholds based on the observed behavior.
- Document the optimized health monitoring and recovery configurations, including
vendor-specific customizations.

## Resources

**Key AWS services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon EKS](https://aws.amazon.com/pm/eks/)
- [AWS Fault Injection Service](https://aws.amazon.com/fis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp05.html*

---

# TELCOREL03 — Change management

**Pillar**: Reliability  
**Best Practices**: 2

---

# TELCOREL03-BP01 Use a controlled change management mechanism for software updates in production

Follow a controlled change management approach that blocks automatic updates in production
environments while maintaining changes are thoroughly tested in lower environments. This
includes establishing proper testing procedures, implementing structured change management, and
maintaining comprehensive rollback capabilities to minimize service disruption during system
updates.

**Desired outcome:**

- Minimized risk of service disruptions from updates.
- Validated changes before production deployment.
- Controlled deployment processes.
- Documented change procedures.
- Verified update effectiveness.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Prevent automatic software updates in production environments on the infrastructure and
network function levels. Implement a controlled change management process for the system and
service updates. Identify update mechanisms, configure update policies to disable automatic
updates while maintaining security adherence, and document detailed manual update procedures.
Establish comprehensive change control processes, including approval workflows, testing
requirements, and documentation standards. Maintain a centralized tracking system for updates
and develop robust rollback capabilities with automated and manual recovery procedures.
Continuously monitor the update process, define clear criteria for triggering rollbacks, and
validate the effectiveness of the recovery mechanisms.

### Implementation steps

- Disable automatic updates in production:

Use AWS Systems Manager Patch Manager to manage and control operating system
and application updates across your AWS environment.
- Use AWS Config to monitor and audit the configuration of your systems,
including the update settings.

- Configure update policies:

Use AWS Config to define and enforce specific configurations for
disabling automatic updates while maintaining security.
- Use AWS Systems Manager Parameter Store to centrally manage and store your
updated policies and configurations.

- Establish change controls:

Use AWS Config Rules to implement comprehensive change management processes,
including approval workflows, testing requirements, and documentation standards.
- Use AWS CloudTrail to track and audit update-related activities across your
AWS environment.

- Create a tracking system:

Use AWS Config to track and monitor update-related changes, including
pending updates, approved changes, and implementation status.
- Use Amazon DynamoDB to store update-related data and provide an audit trail
of activities.

- Maintain rollback procedures:

Use AWS Systems Manager Automation to design and implement the rollback
mechanisms, including both automated and manual rollback capabilities.
- Use Amazon CloudWatch to establish the clear criteria for determining when
rollback procedures should be initiated, including both automated triggers and
manual decision points.
- Use AWS Config to verify the effectiveness of the rollback procedures by
validating system stability and functionality after rollback completion.

## Resources

**Key AWS services:**

- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Config](https://aws.amazon.com/config/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel03-bp01.html*

---

# TELCOREL03-BP02 Design a stateful, session-aware load balancing solution for cloud network functions (CNFs) to enable scaling and resilience

Cloud network functions (CNFs) such as AMF, SMF, and UPF in 5G architectures are typically
designed to be horizontally scalable. However, these components maintain subscriber session
state, and scaling events (up and down) can disrupt session continuity, leading to call drops,
session re-establishment delays, or degraded user experience. To address this challenge, it is
recommended to design a stateful, session-aware load balancing solution for CNFs that enables
seamless scaling and resilience. This can be achieved by collaborating with the CNF vendors and
relevant CNF communities to explore how cloud-based services can be adapted to support
seamless session handling.

**Desired outcome:**

- Provide a highly available and scalable load balancing solution that can maintain
session state for telco network functions deployed as cloud-based workloads.
- Verify seamless failover and state preservation during scaling events or instance
failures, minimizing service disruptions for end users.
- Enable efficient load distribution and resource utilization by intelligently routing
traffic based on current capacity and workload patterns.
- Integrate with Kubernetes-based deployment models and service abstractions used by
telco CNFs.
- Deliver carrier-grade performance and availability to meet the stringent requirements
of telco control plane and signaling workloads.

## Implementation guidance

Design a stateful load balancing architecture that maintains session state and seamless
failover, leveraging in-memory data stores or distributed databases to replicate session data
across instances. Integrate the load balancing solution with Kubernetes-based cloud-based
network functions, providing a standardized interface and allowing CNFs to configure load
balancing parameters. Implement a highly available and fault-tolerant design, with automated
failover and dynamic scaling capabilities. Enhance observability and monitoring to maintain
visibility into the load balancing system's performance, errors, and configuration changes.
Automate the deployment and lifecycle management of the load balancing solution to verify
consistency.

### Implementation steps

- Design a stateful load balancing architecture:

Use AWS application load balancing services, such as Application Load Balancer (ALB) and
Network Load Balancer (NLB), to handle the traffic routing and load distribution.
- Implement session stickiness and connection tracking mechanisms to maintain
session state and verify seamless failover.
- Utilize Amazon ElastiCache (For example, Redis) or Amazon DynamoDB to store and
replicate session data across the load balancing instances.

- Integrate with Kubernetes-based CNFs:

Develop a Kubernetes Ingress Controller or Gateway API implementation to
provide a standardized interface for telco CNFs to leverage the stateful load
balancing solution.
- Implement custom annotations or custom resource definitions (CRDs) to allow
telco CNFs to configure load balancing parameters, such as session timeouts and
stickiness.
- Verify the load balancing solution can discover and register telco CNF
instances through Kubernetes service discovery mechanisms.

- Optimize for carrier-grade performance:

Configure the load balancing instances to leverage high-performance AWS
instance types, such as C5 or M5 families, to handle the throughput and latency
requirements of telco workloads.
- Use AWS Nitro System-based instances for optimized networking and CPU
performance.
- Integrate with AWS Direct Connect and AWS Global Accelerator to provide low-latency connections
and Regional load distribution.

- Implement high availability and fault tolerance:

Deploy the load balancing solution across multiple AWS Availability Zones for
redundancy and resilience.
- Configure health checks, automated failover, and connection draining to verify
seamless failover during instance or Availability Zone failures.
- Leverage AWS Auto Scaling to dynamically scale the load balancing capacity based on
traffic patterns and resource utilization.

- Enhance observability and monitoring:

Integrate the load balancing solution with Amazon CloudWatch for comprehensive
monitoring of performance metrics, error rates, and health status.
- Implement Amazon CloudWatch dashboards and alarms to provide visibility into load
balancing behavior and trigger alerts for anomalies or potential issues.
- Use AWS CloudTrail and AWS Config to track configuration changes and maintain an
audit trail of load balancing activities.

- Automate deployment and lifecycle management:

Package the load balancing solution as an AWS CloudFormation template or Terraform
configuration for consistent and repeatable deployment.
- Integrate the solution with AWS CodePipeline and AWS CodeBuild for automated CI/CD
workflows, including testing and deployment.
- Use AWS Config and AWS Systems Manager to manage the configuration of the load balancing
components and verify adherence with defined policies.

## Resources

**Key AWS services:**

- [Application Load Balancer
(ALB)](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
- [Network Load
Balancer (NLB)](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/) (For example, [Redis](https://aws.amazon.com/elasticache/redis/))
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Kubernetes Ingress
Controller](https://aws.amazon.com/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [AWS CodeBuild](https://aws.amazon.com/codebuild/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel03-bp02.html*

---

# TELCOREL04 — Failure management

**Pillar**: Reliability  
**Best Practices**: 3

---

# TELCOREL04-BP01 Implement the Bypass Mode on peripheral network devices such as firewalls and network probes while connecting to the cloud

Implementing bypass mode on network peripheral devices like firewalls and network probes is
crucial for maintaining service continuity during device failures or power outages. This
mechanism automatically creates a direct connection between incoming and outgoing network ports
when a device fails, maintaining that critical network traffic continues to flow without
interruption. By deploying bypass-capable devices while connecting to the cloud-based network
infrastructure, telecom operators can block service disruptions that could occur during device
failures, maintenance windows, or unexpected outages. This approach is particularly important
for maintaining high availability in telecommunications networks where continuous service is
essential for customer satisfaction and regulatory adherence.

**Desired outcome:**

- Verify continuous network traffic flow during device level failures.
- Minimize service disruptions during maintenance or unexpected outages.
- Maintain high availability for critical network services.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Design your network architecture to include redundant paths and automated routing updates
that can quickly respond to device failures. Implement comprehensive health monitoring and
automated recovery procedures to minimize service disruptions. Establish clear operational
procedures for managing bypass events, including notification workflows and post-event
analysis to block recurring issues.

Regular testing of the bypass functionality is crucial to verify it will work as expected
during actual failures. This includes conducting controlled failure scenarios during
maintenance windows and validating that traffic continues to flow without interruption.
Document bypass events and maintain historical data to identify patterns and potential
improvements to the bypass implementation.

### Implementation steps

- Deploy AWS Network Firewall with fail-open configurations across multiple Availability Zones
to verify continuous traffic flow during failures.
- Configure AWS Transit Gateway for centralized network management with automatic routing
failover capabilities.
- Use Amazon CloudWatch to monitor device health and performance metrics, with automated
alerts for potential failures on AWS services involved.

## Resources

**Key AWS services:**

[AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel04-bp01.html*

---

# TELCOREL04-BP02 Implement dual network planes for signaling or control plane

A resilient network architecture implementing two independent and redundant signaling
networks that operate in parallel. Each signaling plane handles messages and controls network
resources independently, with logical and physical separation to verify that failures in one
plane do not impact the other plane's operations.

**Desired outcome:**

- Enhanced fault tolerance through dual planes.
- Independent operation capability.
- Seamless failover between planes.
- Maintained service continuity.
- Isolated failure domains.
- Verified redundancy effectiveness.
- Documented recovery procedures.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Design a resilient network architecture with separate signaling planes for control plane
traffic, maintaining comprehensive logical and physical separation. Enforce strict network
access controls and security zoning to maintain the separation. Configure robust failover
mechanisms, with automated triggers, recovery procedures, and comprehensive health monitoring
across the planes. Test the failover functionality under various failure scenarios and
document the recovery steps. Deploy advanced monitoring and observability tools to track the
performance, availability, and security of both signaling planes, establish key metrics and
alerting thresholds, and regularly review the monitoring strategy for continuous improvement.

### Implementation steps

- Design separate signaling planes:

Use AWS Transit Gateway and AWS Network Firewall to implement a
vendor-neutral strategy for logical and physical separation between control and user
plane traffic. Configure AWS Network ACLs and security groups to enforce network
zoning, traffic classification, and security controls.

- Verify physical separation:

Use AWS Config to specify and enforce the
technical requirements for network isolation, including network segments,
addressing, and security controls. Use AWS Config Rules to monitor and enforce requirements
affecting the separation.
- Deploy the separate network infrastructure for
each plane using Amazon VPC and AWS Direct Connect. Utilize AWS Transit Gateway and AWS Network Firewall to
implement network virtualization and segmentation.
- Configure AWS Network Firewall and Amazon VPC security groups to
enforce strict network access controls and security policies. Define and enforce the
security zones and trust boundaries using AWS IAM and AWS Service Control
Policies.

- Configure failover mechanisms:

Use Amazon CloudWatch alarms and AWS Lambda functions to
establish the conditions and thresholds for automated failover.
- Deploy Amazon CloudWatch and AWS Lambda to monitor the health of
the planes and trigger the appropriate failover responses.
- Use AWS Fault Injection Service to regularly test the failover
functionality under various failure conditions. Document the test procedures and
success criteria in AWS Systems Manager.
- Create detailed recovery procedures for different
failure scenarios. Include troubleshooting guides and contact information.

- Monitor plane status:

Use Amazon CloudWatch to monitor the performance,
availability, and security metrics for both planes.
- Establish key performance indicators using Amazon CloudWatch
that reflect service health, including latency, throughput, error rates, and
resource utilization. Set appropriate thresholds and baselines.
- Configure Amazon CloudWatch alarms and Amazon SNS to implement a notification
system for critical events and threshold violations. Define alert severity levels
and response procedures.
- Regularly evaluate monitoring strategy effectiveness and
adjust based on operational experience. Update metrics and thresholds as needed.

## Resources

**Key AWS services:**

- [Amazon VPC](https://aws.amazon.com/vpc/)
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel04-bp02.html*

---

# TELCOREL04-BP03 Implement default configuration to bypass billing and charging services in case the system is down

Implementing a default configuration to bypass billing and charging services in a telecom
network maintains service continuity for customers in the event of a failure or outage in the
billing or charging system. The network is configured with a failover mechanism that continues
providing critical communication services while bypassing the charging/billing component if they
become unavailable or unresponsive. This bypass mode allows customers to continue accessing and
using the telecom services without interruption, even when the billing or charging systems are
down.

**Desired outcome:**

- Verify customer experience and service availability take precedence over billing and
charging functions.
- Allow customers to continue using services while their usage and session data is
temporarily stored or cached within the network.
- Process cached usage data once the billing and charging systems are restored, verifying
revenue is not lost.

## Implementation guidance

Implement a default configuration on the control plane functions that allows the network
to bypass the billing and charging systems in the event of a failure or outage. Configure the
network functions to continue call setup or session establishment even when the charging
system is unresponsive. When the billing or charging systems are restored, they process the
cached usage data to verify revenue is not lost despite the temporary bypass of these systems.

### Implementation steps

- Define bypass triggers and thresholds:

Use monitoring tools to detect failures or unresponsiveness in the billing
and charging systems
- Establish clear criteria and thresholds for triggering the bypass mode, such as
connection timeouts, error rates, or system availability metrics

- Implement bypass configuration:

Configure network functions with a default method to continue call setup or
session setup in case the charging system is unresponsive.

- Use data records and call records for offline charging/billing:

Once the billing or charging systems are back online, the cached usage data can
be processed and the end user is billed accordingly, verifying that revenue is not
lost despite the temporary bypass of these systems.

## Resources

**Key AWS services:**

- [Amazon CloudWatch for monitoring and alerting](https://aws.amazon.com/cloudwatch/)
- [AWS Lambda for implementing custom bypass logic and
data processing](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel04-bp03.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
