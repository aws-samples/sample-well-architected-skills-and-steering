**Pillar**: Operational Excellence

# FSIOPS4: How do you assess your ability to operate a workload in the cloud?

Financial services institutions often have a robust set of operating policies that
govern behaviors and decision-making for activities such as disaster recovery planning,
capacity management, security and compliance guardrails, and data backup and recovery. Cloud
services support new technologies, architectural patterns, and automations which are not
possible or practical for on-premises environments. Policies which were originally created
for on-premise environments should be revisited from a cloud perspective, rather than
assumed to be necessary and relevant.

## FSIOPS04-BP01 Implement a change management process for cloud resources

Cloud IT change management processes facilitate changes to IT systems in order to
minimize risks to production environments while adhering to policies, audit, and risk
controls. It is not uncommon, especially within financial services institutions, to see a
gated change management process often requiring a review by external change advisory
boards, which can take days or even weeks. As organizations take advantage of
configuration management, infrastructure as code (IaC), automated testing and validation,
and continuous integration and delivery, they can implement lightweight approval processes
that are tightly integrated into CI/CD pipeline tools.

By automating detection and rejection of bad changes, many manual approval steps can
be fully automated with a higher degree of confidence. Even in highly regulated industries
where external reviews are required, such as financial services, reviews should still be
integrated with the overall pipeline, even if they are manual steps initially. Regulatory
requirements such as the Sarbanes-Oxley Act requires all financial reports to include an
internal controls report that documents every change made to your workloads. Performing
operations as code provides the capability to test, model, and simulate scenarios before
rollout, which limits the potential for human error. Additionally, it satisfies regulatory
requirements by providing auditors a complete record of all applied changes, including the
environment in which tests and validations were run and the identity and timestamp of each
change approval. This speeds up deployment cycles and innovation, while preserving
security controls and guardrails.

A good change management process delivers business value while balancing risk against
business value. It should do so in a way that maximizes productivity and minimizes wasted
effort or cost for all participants in the process. Automation, integration, and
deployment tools in the cloud allow businesses to make small, frequent changes that reduce
risk and deliver business value at an increased rate. For additional guidance, see [Change Management in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/change-management-in-the-cloud/change-management-in-the-cloud.html).

### Prescriptive guidance

Financial services institutions must develop cloud capabilities in layers,
producing approved, reusable artifacts at each layer, such as:

- [golden Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-update-patch-golden-ami.html),
- [CloudFormation
Templates](https://aws.amazon.com/cloudformation/),
- [Service Catalog](https://aws.amazon.com/servicecatalog/) Products,
- [container base
images](https://aws.amazon.com/blogs/containers/designing-a-secure-container-image-registry/),
- software packages,
- and [Lambda deployment
packages](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html).

Artifacts at foundational layers must go through a change control process so that
they comply with enterprise guidelines, which can then be repurposed as building blocks
by the rest of the organization. AWS Systems Manager Change Manager provides tracking and
approval, and allows for the implementation of operational changes to application
configurations and infrastructures. As the organization builds higher-level applications
on a foundation of certified artifacts, you can expedite the change control process, as
it only needs to focus on the higher-level artifacts, accelerating change while
minimizing risk and ensuring compliance. Over time, organizations develop capabilities
to administer most of the changes in automated fashion, with only a subset of changes
that require manual intervention.

## FSIOPS04-BP02 Implement infrastructure as code

The benefit of the cloud and infrastructure as code is the ability to build and tear
down entire environments programmatically and automatically. If architected with
resiliency in mind, a recovery environment can be implemented in minutes using AWS CloudFormation
templates or AWS Systems Manager automation. Automation is critical for maintaining high
availability and fast recovery.

### Prescriptive guidance

AWS offers a wide breadth of automation tools to accomplish resiliency
objectives. AWS Systems Manager helps automate complete runbooks that are used during the
recovery of an application during a disaster. You can sequence a complete set of
operations to automatically initiate on detection of an event. With Systems Manager
automation documents, you can manage these runbooks similar to the way you manage code.
You can version them and update them along with every release. This helps keep your
recovery plan in sync with released code and updates to infrastructure.

## FSIOPS04-BP03 Prevent configuration drift

Drift of infrastructure configuration between primary and secondary sites can lead to
failure in recovery during a disaster event. Implementation of code-based management
practices across your infrastructure, applications, and operational procedures provides a
high degree of version control, testing, validation, and mitigation of human error and
configuration drift, which is necessary to limit the introduction of errors into your
environment and to reduce the mean time to recover (MTTR).

### Prescriptive guidance

Financial services institutions should monitor changes to application
infrastructure by using:

- [AWS CloudFormation
drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html),
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/),
- and [AWS Config](https://aws.amazon.com/config/).

These services monitor activity within your AWS account, including actions taken
through the [AWS Management Console](https://aws.amazon.com/console/), [AWS SDKs](https://aws.amazon.com/developer/tools/), command line tools, and
other AWS services. Once detected, you can automate the reactive action by defining
workflows using [AWS EventBridge](https://aws.amazon.com/eventbridge/)
integration and [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops4.html*
