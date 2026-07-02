# EUCOPS09 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# EUCOPS09-BP01 Maintain an up to date matrix of all EUC service owners and quick access links to the support plans for each service

Amazon WorkSpaces and Amazon WorkSpaces Applications, although easier to implement and administer than
traditional on-premises alternatives, still require specific knowledge to deploy, manage,
and support. To simplify the process of routing issues to the right owners, you should be
able to quickly identify the teams who are responsible for implementation and support along
with clear support plans for each application being delivered, expediting time to
resolution.

Each application delivered by WorkSpaces or WorkSpaces Applications should have a formalized support
plan with designated business and technical owners who are responsible for and involved in
the deployment, maintenance, and support of each application and its dependent technology
stacks.

Each application set should have its own designated level of criticality, with
associated SLAs that are clearly understood by the support teams involved. For disaster
recovery purposes, the business should be able to identify relevant RTO and RPO parameters
which each service should be engineered to accommodate so that critical business services
can be delivered even under the most challenging circumstances.

If you are delivering WorkSpaces or WorkSpaces Applications across multiple AWS Regions, verify that
a support and escalation mechanism exists that documents the transfer of responsibility
between regions when required. This documentation is important to sustain support efforts
across time zones, maximizing service continuity.

Note: Your business RPO and RTO requirements may be more aggressive than the service
can provide, and discrete groups of users may have different RPO and RTO requirements.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Create a process to quickly identify roles and responsibilities for each application
stack so that support teams can quickly identify the resources that need to be employed
and address any issues in service delivery.

## Resources

- [WorkSpaces Service Level Agreement](https://aws.amazon.com/workspaces/sla/)
- [WorkSpaces Applications Service Level
Agreement](https://aws.amazon.com/appstream2/sla/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops09-bp01.html*

---

# EUCOPS09-BP02 Allocate training time so your teams can build and maintain their skills to deploy and manage your AWS EUC environment

Training and enablement are key to maintaining a reliable, successfully-evolving EUC
deployment.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Provide targeted training on the AWS Cloud, Amazon WorkSpaces, and WorkSpaces Applications to verify
that architects, administrators, and support personnel all have the relevant skills to
design, deploy, and maintain the AWS EUC environment. Give this training through
authorized training courses and professional accreditations and create a training
environment that can be used for evaluation and self-instruction, augmenting official
coursework.

The core tenets are the same for WorkSpaces and WorkSpaces Applications as they are for delivering a
remotely accessed, centralized, and virtualized desktop and application delivery service,
either on-premises or from an alternate cloud vendor. Skills in these areas are
transferrable to deploying and managing AWS EUC services. It is essential for your
deployment teams to have a good understanding of compute, networking, storage,
virtualization, and application delivery, at a minimum.

Technical teams may need to be prepared in different ways depending on the nature of
the adoption of Amazon WorkSpaces and WorkSpaces Applications services:

**Greenfield a net new deployment with no prior cloud or EUC
skills**

Teams need to be trained, and they should iteratively maintain their skills in AWS
core competencies such as cloud delivery, compute, networking, and storage, in addition to
specific training and exposure to Amazon WorkSpaces and WorkSpaces Applications. Focus on understanding the
core tenets of cloud delivery such as reducing costs, increasing scalability and
resilience, and taking advantage of the global reach of AWS Cloud services. This may be
an area where AWS Professional Services or an AWS Partner may be able to add
significant value until your technical teams are familiar with the technologies involved.

**A net new deployment with existing EUC skills, but no prior cloud
infrastructure skills**

Teams need to be trained, and they should iteratively maintain their skills in AWS
core competencies such as cloud delivery, compute, networking, and storage. Focus on
understanding the core tenets of cloud delivery such as reducing costs, increasing
scalability and resilience, and taking advantage of the global reach of AWS Cloud
services.

Teams should still be trained on and exposed to Amazon WorkSpaces and WorkSpaces Applications, but
technical teams with prior experience deploying and managing EUC solutions will find this
relatively straightforward.

**Migration from an on-premises deployment of an existing vendors EUC
solution**

Teams need to be trained, and they should iteratively maintain their skills in AWS
core competencies such as cloud delivery, compute, networking, and storage. Focus on
understanding the core tenets of cloud delivery such as reducing costs, increasing
scalability and resilience, and taking advantage of the global reach of AWS Cloud
services.

Teams should still be trained on and exposed to Amazon WorkSpaces and WorkSpaces Applications, but
technical teams with prior experience deploying and managing EUC solutions will find this
relatively straightforward.

Pay particular attention on the training and preparation needed to accommodate the
differences between the incumbent solution and the way AWS EUC services are deployed and
managed. Differences in image lifecycle management, application delivery, user access and
peripheral support will be key.

**Migration from an existing cloud or hybrid deployment of EUC
services**

Technical teams with existing expertise deploying cloud solutions from other vendors
will have transferrable skills that shortcut training requirements. While AWS Cloud and
EUC service training will still be required, the time to absorb and apply this knowledge
will require less time and effort.

Pay particular attention on the training and preparation needed to accommodate the
differences between the incumbent cloud and EUC solutions and the way AWS Cloud and EUC
services are deployed and managed.

While Amazon WorkSpaces and WorkSpaces Applications deliver standard Windows desktops and applications,
which are created, managed, and maintained in a similar way to many other EUC and VDI
systems, there are a few specific differences that need to be considered:-

**Amazon WorkSpaces and Amazon WorkSpaces Applications service specifics**

Amazon WorkSpaces and Amazon WorkSpaces Applications are fully managed services, meaning that there is
no customer access to the control plane. While this reduces control plane hardware
requirements and simplifies deployment, there are some specific differences that need to
be considered:

- **Connectivity**: User connectivity to each of the
services is typically through an AWS-controlled point of presence on the public
internet. Both streaming authentication and streaming traffic are delivered in this
fashion. For Amazon WorkSpaces Applications, streaming traffic can be routed to a
customer-configured VPC endpoint.

[WorkSpaces Applications Interface VPC Endpoints](https://docs.aws.amazon.com/appstream2/latest/developerguide/interface-vpc-endpoints.html)

- **Compute instances**: Amazon WorkSpaces and Amazon WorkSpaces Applications
instances are a specifically engineered version of equivalent EC2 instances. As a
result, the storage and networking configuration is subtly different.
- **Instance availability**: Customers already familiar
with the AWS Cloud and Amazon EC2 may be accustomed to a large selection of available
instance types. While Amazon WorkSpaces and Amazon WorkSpaces Applications offer a range of compute
instances to deliver most typical EUC use cases, these are only a subset of the
instance types available on EC2.
- **Cost management**: Minimizing cost is a key
consideration for most customers when adopting AWS EUC services. All personnel
involved in deploying, managing, and maintaining the environment need to adopt a
mindset that active resources add to the solution costs. For example, optimizing the
running mode of WorkSpaces (Always-On or AutoStop), and managing the scale up and down
policies and running mode for WorkSpaces Applications (Always-On or On-Demand) verifies that you
are managing costs effectively.

Both WorkSpaces and WorkSpaces Applications have cost optimizers that can be used to reduce costs by
automating the shutdown or running mode of compute resources:

- [Cost Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/)
- [Cost Optimizer for Amazon WorkSpaces Applications](https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2)
- [Cost Optimization for WorkSpaces Applications
Fleets](https://aws.amazon.com/blogs/desktop-and-application-streaming/optimizing-costs-using-amazon-appstream-2-0-fleet-options/)

**Amazon WorkSpaces and WorkSpaces Applications targeted training**

While a basic knowledge of AWS services, such as deploying VPCs, subnets,
networking, and storage, is required to deploy AWS EUC services, the following training,
specific to AWS EUC services, is also available:

- [An Introduction to AWS End User
Computing](https://explore.skillbuilder.aws/learn/course/external/view/elearning/504/introduction-to-aws-end-user-computing-services)
- [Amazon WorkSpaces Primer](https://explore.skillbuilder.aws/learn/course/external/view/elearning/517/amazon-workspaces-primer)
- [Amazon WorkSpaces Deep Dive](https://explore.skillbuilder.aws/learn/course/external/view/elearning/1723/amazon-workspaces-deep-dive)
- [Amazon AppStream Primer](https://www.aws.training/Details/Curriculum?id=67990&redirect=false)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops09-bp02.html*

---
