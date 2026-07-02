**Pillar**: Security

# FSISEC01: How does your governance enable secure cloud adoption at scale?

Cloud infrastructure provides more agility and responsiveness
than traditional IT environments. This requires organizations
to think differently about how they design, build, and manage
applications. Cloud resources can be disposable. Because it is
a pay-per-use model, it often requires a strong integration
between IT governance and organizational governance. Financial
services companies need to operate in a cloud environment
that's agile and safe at the same time. With the adoption of
generative AI capabilities, organizations need to implement
comprehensive security controls across AI components while
maintaining agility and innovation.

## FSISEC01-BP01 Consider and leverage a Cloud Center of Excellence (CCoE)

When it comes to cloud adoption and governance, CCoEs (also
referred as Cloud Enablement Engine (CEE)) are known drivers
of change across the enterprise and the focal point for its
transformation. CCoEs should have a functional model that is
more aligned to provisioning and operating cloud resources,
or they should act as the advisory group for cloud
migrations and security baseline definitions. CCoEs help
create and manage governance and security policies in
collaboration with a cross-functional team and select
governance tools to provide financial and risk management.

When implementing generative AI workloads, CCoEs should
establish comprehensive governance frameworks that
encompass:

- AI model lifecycle management and approval processes
- Data governance for training datasets and model inputs
- Model performance monitoring and drift detection
- Compliance tracking for AI regulatory requirements
- Risk assessment frameworks for AI model deployment
- Guardrails to control system behaviors
- Standardized resource management for prompts and models

The following tenets are key guiding principles for
[creating
a CCoE](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/):

- The CCoE structure evolves as the organization changes.
- Treat the cloud as your product and application team
leaders as the customers you are serving.
- Build company culture into everything you do.
- Organizational change management is central to business
transformation. Use intentional and targeted
organizational change management to change company culture
and norms.
- Embrace a change-as-normal mindset. Security policies and
procedures must be flexible enough to keep up with the
changes in applications, IT systems, and business
direction over the time and should be aligned with the
financial services industry regulations and best practices.
- Operating model decisions determine how people fill roles
that achieve business outcomes.

Traditionally, companies in the financial sector have
distributed internal teams with distinct roles, as part of
their division of duties policies. Even so, you can still
get the benefits described here if the duties of a CCoE are
distributed among multidisciplinary teams.

## FSISEC01-BP02 Use cloud-native services for management and governance

Financial sector organizations focus on achieving security and
compliance objectives in balance with faster innovation and
agility.
[AWS Management and Governance native services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/management-governance.html)
takes advantage of both innovation and control as you can
provision resources and applications to help meet your
policies and operate your environment for business agility and
governance control. These services are designed to make it
easier to manage your AWS environment at scale, facilitating
the secure adoption of cloud services without losing control
of the environment growth.

The following articles and blogs provide advice for improving
the overall security of your workloads and to hone the
security posture of your internal IT resources.

The section
[Building
a CCOE to transform the entire enterprise](https://docs.aws.amazon.com/whitepapers/latest/public-sector-cloud-transformation/building-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise.html),
from AWS documentation describes the benefits of creating a
Cloud Center of Excellence (CCOE) within your organization.
This allows you to adopt a number of policies that helps you
evolve your security measures across several dimensions over
time and scope.

The whitepaper
[Cloud
Enablement Engine: A Practical Guide](https://d1.awsstatic.com/whitepapers/cloud-enablement-engine-practical-guide.pdf)
describes the step-by-step process for the initial setup
activities for a CCOE, and the top ten best practices gleaned
by AWS while working across a large number of customers.

By using a Service Catalog, your organization can create
and manage catalogs of IT services that are approved for AWS.
These IT services can include everything from virtual machine
images, servers, software, databases, to complete multi-tier application
architectures. For more information, see
[Manage pre-approved services for secure adoption at scale with Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html).

[AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) can offer a straightforward way
to set up and govern an AWS multi-account environment,
following prescriptive best practices. AWS Control Tower
orchestrates the capabilities of several other
[AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html), including AWS Organizations, Service Catalog, and AWS IAM Identity Center. It allows you to
build a landing zone in less than an hour.

## Resources

**Related documents:**

- [Using a Cloud Center of Excellence (CCOE) to Transform the Entire Enterprise](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/)
- [7
Pitfalls to Avoid When Building a CCOE](https://aws.amazon.com/blogs/enterprise-strategy/7-pitfalls-to-avoid-when-building-a-ccoe/)
- [AWS Control Tower and AWS Security Hub CSPM – Powerful Enterprise Twins](https://aws.amazon.com/blogs/enterprise-strategy/aws-control-tower-and-aws-security-hub-powerful-enterprise-twins/)

**Related videos:**

- [Transform your organization's culture with a Cloud Center of Excellence](https://www.youtube.com/watch?v=VN1vj0d3Z1Y&ab_channel=AWSEvents)
- [How to Build Your Cloud Enablement Engine with the People You Already Have](https://pages.awscloud.com/How-to-Build-Your-Cloud-Enablement-Engine-with-the-People-You-Already-Have_2019_0617-ENT_OD.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec01.html*
