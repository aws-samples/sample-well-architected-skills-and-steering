**Pillar**: Security

# FSISEC04: How do you accommodate separation of duties as part of your identity and access management design?

## FSISEC04-BP01 Implement the principle of separation of duties

Separation of duties, as it relates to security, has two
primary objectives. The first objective is the prevention of
conflict of interest, abuse, and errors. The second objective
is the detection of control failures that include security
breaches, information theft, and circumvention of security
controls.

While robust automation of infrastructure and application
deployments helps reduce the need for human access, there
can be instances where individuals need to complete key
functions. For users with increased privileges, it is
important to distribute system administration activities, so
no one administrator can hide their activities or control an
entire system. Separation of duties can help mitigate risk
on critical tasks by ensuring different people are required
to perform a task where the requestor and the approver can't
be the same person. A common example is the use of an
approver during the
[running
of an automation on AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-require-approvals.html).
This principle can be used to implement numerous tasks
including controlling access to your cloud resources.

For generative AI workloads, implement clear separation of
duties by creating distinct roles for prompt engineering,
security administration, and model governance, while
maintaining separate permissions for model access,
management and deployment as well as establishing dedicated
approval workflows for AI system changes, and enforcing
strict boundaries between development and production AI
environments.

## FSISEC04-BP02 Use AWS Config to view historical IAM configuration and changes over time

Use
[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource.html) to view the IAM policy that was
assigned to an IAM user, group, or role at any time in which
AWS Config was recording. This information can help you
determine the permissions that belonged to a user at a specific time. For example, it allows
you to view whether a user had permission to modify settings
on a specific date in the past.

## FSISEC04-BP03 Set up alerts for IAM configuration changes and perform audits

[Set
up alerts](https://aws.amazon.com/blogs/security/how-to-receive-alerts-when-your-iam-configuration-changes/)

to notify on IAM configuration
changes including when an
[IAM user is created](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html) or when conflicting
permissions are added to a user or role, such as being able to
approve its own requests on a given workflow. This is helpful
for monitoring activities by users with increased privileges.
The added notification can be set up using a combination of
[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html),

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html),

and
[Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

### Prescriptive guidance

- To manage changes for an entire organization or for a
single AWS account, you can use Change Manager, a
capability of AWS Systems Manager. For more details see,
[Setting up Change Manager at](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-setting-up.html)

[AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-setting-up.html).
- AWS Config is a service that helps you manage compliance
state changes for resources. For more details, see
[Viewing AWS Resource Configurations and History](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource.html).
- An approval process for changes can be deployed using
AWS Step Functions. To review the step-by- step
tutorial, see
[Deploying an Example Human Approval Project](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html).

## Resources

**Related documents:**

- [Apply the principle of separation of duties to shell access to your EC2 instances](https://aws.amazon.com/blogs/security/apply-the-principle-of-separation-of-duties-to-shell-access-to-your-ec2-instances/)
- [How to Record and Govern Your IAM Resource Configurations Using AWS Config](https://aws.amazon.com/blogs/security/how-to-record-and-govern-your-iam-resource-configurations-using-aws-config/)

**Related videos:**

- [Least Privilege & Separation of Duties for AWS ACM Private CA](https://www.youtube.com/watch?v=ifImMYHQbp0&ab_channel=AmazonWebServices)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec04.html*
