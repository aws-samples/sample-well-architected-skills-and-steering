# EUCCOST03 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# EUCCOST03-BP01 Determine the level of self-service capabilities to provide your users

Amazon WorkSpaces offers self-service capabilities that you can
enable for your users. Assess the impact of granting access to
these self-service capabilities and selectively disable or
enable them based on your requirements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Evaluate the cost impact of enabling certain self-service WorkSpaces management
capabilities for your users, and then select which of these self-service capabilities you
want to provide to your users. For more information, see [Enable self-service WorkSpaces management capabilities for your users in WorkSpaces
Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html) . Consider creating internal policies to govern which capabilities are
allowed. Changing the compute type (bundle), increasing the root and user volume size, and
changing the running mode may increase your cost. Instead of enabling these capabilities
for your users, you may consider providing these capabilities through your IT service
management so that changes requested by a user requires prior approval.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost03-bp01.html*

---

# EUCCOST03-BP02 Use a self-service portal to request your ITSM

Instead of enabling self-service capabilities for your users, use a self-service portal to allow users to request resources, or enable workflow-based request for EUC resources with your ITSM. This gives you better control and limits the exposure to unforeseen cost increases.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Consider implementing a self-service portal to request
WorkSpaces or changes to your existing WorkSpaces, like
running mode, bundle, or storage. A self-service portal can
allow your users to provision and terminate their EUC services
as required. For an example for Amazon WorkSpaces, see
[Creating
a self-service portal for Amazon WorkSpaces end users](https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-a-self-service-portal-for-amazon-workspaces-end-users/).

Additionally, consider using your ITSM solution to enable
workflow-based requests for new WorkSpaces or changes to
existing WorkSpaces, like running mode, bundle, or storage.
For examples of integrating with ServiceNow, see
[How
to enable self-service Amazon WorkSpaces by using Service Catalog Connector for ServiceNow](https://aws.amazon.com/blogs/mt/how-to-enable-self-service-amazon-workspaces-by-using-aws-service-catalog-connector-for-servicenow/) and

[Managing
Amazon WorkSpaces by integrating Service Catalog with ServiceNow](https://aws.amazon.com/blogs/mt/managing-amazon-workspaces-by-integrating-aws-service-catalog-with-servicenow/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost03-bp02.html*

---
