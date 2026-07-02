# EUCOPS16 — Evolve

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS16-BP01 Implement automated processes to verify that service updates can be repeatably deployed, updated, and rolled back

Selecting an automation toolset and defining the processes that facilitate repeatable,
predictable delivery and maintenance of AWS EUC services is key to achieving simplified
administration, reduced support overheads, end user satisfaction and positive business
outcomes.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Although Amazon WorkSpaces and Amazon WorkSpaces Applications are fully managed services, there are a
number of touch points when maintenance the associated infrastructure and the desktop and
applications delivered by the service requires periodic updates.

Every AWS EUC environment is unique. Verify that you understand each area of your
AWS EUC deployment that may need to be updated over time and develop a formalized plan
on how each of these areas need to be managed.

The following questions and discussions can provide you steps for improvement.

**What updates are required?**

- **Amazon WorkSpaces**: For WorkSpaces, the custom bundles created to
deliver persistent desktops to users will require updates over time in the form of
operating system patches, hotfixes, and security and application updates. Once your
WorkSpaces have been deployed, they must be individually managed, as each WorkSpace can be
uniquely changed and reconfigured by its assigned user if they are given the
appropriate rights. The customer is responsible for making these changes. Amazon WorkSpaces
have a regular automatic maintenance schedule which keeps the WorkSpaces specific agents
aligned with the service control plane. For detail on the maintenance process for
Always-On and AutoStop WorkSpaces, see [Maintenance in WorkSpaces
Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html).
- **Amazon WorkSpaces Applications**: For WorkSpaces Applications, each private
image used to deploy a non-persistent desktop or application experience will
periodically require updates in the form of operating system patches, hotfixes, and
security and application updates. As WorkSpaces Applications instances are deployed from a
common image, only the private image for each fleet version needs to be updated. New
instances launched when users log in will automatically inherit the changes made to
the private image. The customer is responsible for making these changes.
- Maintenance of the agent software installed on each image can be automated or
controlled by the customer if specific versions are required. For more information on
the processes of maintaining agent versions for each image, see:

[Update Management
in Amazon WorkSpaces Applications PDF RSS Focus mode](https://docs.aws.amazon.com/appstream2/latest/developerguide/update-management.html)
- [Manage AppStream
2.0 Agent Versions](https://docs.aws.amazon.com/appstream2/latest/developerguide/base-images-agent.html)

- Amazon WorkSpaces Applications also offers an application delivery option called elastic
fleets that you can use to quickly deploy and manage portable applications. For more
information, see [Applications
Manager](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks-applications.html).

**How do you manage updates?**

Creating and delivering updates that are consistent and repeatable is the best way of
reducing problems and frustration for users when configuration changes are made to the
workloads delivered by AWS EUC services. You can use software deployment tools to build
new software packages, perform unit and interoperability testing, and roll out or roll
back changes without touching each desktop or application server individually. This form
of automation drastically reduces the chance of human error and configuration drift across
large desktop and application estates, saving on support costs, reducing downtime, and
maximizing productivity.

- **WorkSpaces**: Workspaces provides a management console and a
corresponding API, which can be used to create and configure new WorkSpace bundles.
Once created from a custom bundle, each WorkSpace is persistent but decoupled from the
custom image and requires discrete management and maintenance.
- To update existing WorkSpaces, use the customer-facing network interface attached to
each WorkSpace to integrate with software deployment toolsets such as AWS Systems Manager or
existing on-premises tools such as Microsoft Endpoint Configuration Manager (MECM),
Puppet Enterprise, or Ansible.

[Software deployment to Amazon WorkSpaces using AWS Systems Manager](https://aws.amazon.com/blogs/mt/software-deployment-to-amazon-workspaces-using-aws-systems-manager/)
- [Automatically create customized Amazon WorkSpaces Windows images](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-create-customized-amazon-workspaces-windows-images/)

- **WorkSpaces Applications**: WorkSpaces Applications provides a management
console and a corresponding API, which can be used to automate the delivery of an
image builder that updates each version of a private image. As the image builder has a
network interface in a customer-managed VPC, traditional software distribution tools
and automation frameworks can also be used to push updates to this instance from where
a new version of an image is created and assigned to fleets.
- WorkSpaces Applications also offers an automated option called Managed Image Updates, which
automates and simplifies the process of updating AppStream agent software and OS
patches. For more information, see the following:

[Administer Your Amazon WorkSpaces Applications Images](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html#keep-image-updated-managed-image-updates)
- [Automatically create customized WorkSpaces Applications Windows images](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-create-customized-appstream-2-0-windows-images/)
- [Automate the creation of WorkSpaces Applications resources using AWS CloudFormation](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation.html)

**How will you test and validate updates?**

- **WorkSpaces**: Before production rollout, any OS or
application updates need to be tested on a WorkSpace created from the same custom
bundle as the WorkSpace group being updated. Several custom bundles may exist with
different application combinations that need to be independently tested. Once testing
is complete, you can roll out changes to each WorkSpace created from the initial
custom bundle, either manually or using automation tools such as Microsoft WSUS or
Microsoft MECM (SCCM).
- If WorkSpace users have been given full administrative access to their desktop,
it is possible that they may have updated their WorkSpace OS or application
independently, making the process of applying consistent, reliable updates across the
WorkSpace estate challenging. Unless strictly necessary, we don't recommend allowing
users to update their own WorkSpaces.
- Should an update fail, a snapshot of the two WorkSpaces storage volumes is taken every
12 hours, which may provide a recovery position. WorkSpaces can be rebuilt or [recovered](https://docs.aws.amazon.com/workspaces/latest/adminguide/restore-workspace.html). For more information, see [Rebuild a WorkSpace in
WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/rebuild-workspace.html).

For more flexible backup and recovery options, consider using traditional backup and
recovery tools and techniques, or consider [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html).

- **WorkSpaces Applications**: As WorkSpaces Applications delivers tens,
hundreds, or thousands of instances from a common private image, testing can be done
by creating a single instance test or development fleet from a new version of an
image, allowing administrators to fully test changes before assigning the image to a
production fleet and making it available to users.
- Multiple fleets or fleet versions can be created from a private image, allowing
administrators to roll forward or roll back to a known operational state if problems
occur. Multiple versions of an image can also be deployed in parallel if extended user
testing is preferred.

**How do you track changes and manage releases?**

Track specific changes to your AWS EUC environments by date and time to maintain a
paper trail that can be used to pinpoint and cross reference if a specific change was
responsible for a positive or negative change in functionality or performance. For
example, creating a retrospective back-out or remediation plan in the event of an issue
that occurs days or weeks after a change is made to the environment will be much easier if
comprehensive change management is observed.

For both Amazon WorkSpaces and Amazon WorkSpaces Applications specifically, adopt a version numbering
scheme and capturing a log of changes made to each custom bundle or private image to trace
issues back to a specific image version, if required.

You can use AWS CloudTrail to log API calls used to make changes to both Amazon WorkSpaces and
WorkSpaces Applications environments.

- [Logging
WorkSpaces Applications API calls with AWS CloudTrail](https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-using-cloudtrail.html)
- [Logging WorkSpaces API Calls by Using CloudTrail](https://docs.aws.amazon.com/workspaces/latest/api/cloudtrail_logging.html)

**Automating changes to Amazon WorkSpaces and Amazon WorkSpaces Applications**

By using automation, you can avoid many of the configuration drift and image
consistency problems seen with manual deployments. The following articles provide some
options for automating the creation and management of AWS EUC services.

- [Automating the provisioning of AWS WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/automate-provisioning-of-amazon-workspaces-using-aws-lambda/)
- [Automatically create customized WorkSpaces Applications Windows images](https://aws.amazon.com/blogs/desktop-and-application-streaming/automatically-create-customized-appstream-2-0-windows-images/)
- [Best practices for automating your AWS End User Computing deployments](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0210-EUC_Slide-Deck.pdf)
- [Amazon WorkSpaces and WorkSpaces Applications Terraform Resources](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Deploying and Managing Amazon WorkSpaces applications with Ansible](https://aws.amazon.com/blogs/desktop-and-application-streaming/deploying-and-managing-amazon-workspaces-applications-with-ansible/)
- [DXC Technology creates DevSecOps and CI/CD for mainframe and Java using Amazon
WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/dxc-technology-devsecops-cicd-mainframe-amazon-appstream-2-0/)
- [Announcing the Amazon WorkSpaces dynamic inventory plugin for Ansible®](https://aws.amazon.com/blogs/desktop-and-application-streaming/announcing-the-amazon-workspaces-dynamic-inventory-plugin-for-ansible/)
- [Terraform resources for AWS WorkSpaces](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/workspaces_workspace)
- [Automation of infrastructure and application deployment for Amazon WorkSpaces Applications
with Terraform](https://aws.amazon.com/blogs/desktop-and-application-streaming/automation-of-infrastructure-and-application-deployment-for-amazon-appstream-2-0-with-terraform/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops16-bp01.html*

---
