# EUCCOST02 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# EUCCOST02-BP01 Monitor your EUC cost and usage proactively

[AWS Cost and Usage
Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html) help you gain detailed insights onboth your WorkSpaces Applications and your WorkSpaces service
usage and cost. In addition, WorkSpaces Applications offers separate [Usage Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-usage-reports.html)
with further detail. Amazon WorkSpaces comes with a [WorkSpaces CloudWatch automatic
dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html) that provides insight into the performance of your WorkSpaces resources and
helps you identify performance issues. [Amazon WorkSpaces Applications Fleet Usage and
Instance/Session Performance Metrics](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html) are available in the WorkSpaces Applications Console and
Amazon CloudWatch.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

For WorkSpaces, enable [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html) with
resource IDs to analyze and visualize your cost and usage. Resource IDs help you see the
cost and usage data for an individual WorkSpace. Consider building an [Build an enterprise cost and usage dashboard for Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/build-an-enterprise-cost-and-usage-dashboard-for-amazon-workspaces/).

Furthermore, the [Cloud
Intelligence Dashboards](https://www.wellarchitectedlabs.com/cloud-intelligence-dashboards/) section of AWS Well-Architected Labs explores how to
build a CUDOS Dashboard that includes Amazon WorkSpaces cost and usage data. The Cost
Optimizer for Amazon WorkSpaces referred to in EUCCOST-BP05 also generates basic usage
reports in Amazon S3.

WorkSpaces Applications also offers built-in usage reports. Enable [WorkSpaces Applications Usage
Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-usage-reports.html) to gain valuable insights into your WorkSpaces Applications usage. For details on
visualizing your WorkSpaces Applications usage, see [Analyze your WorkSpaces Applications usage reports using Amazon Athena and Quick](https://aws.amazon.com/blogs/desktop-and-application-streaming/analyze-your-amazon-appstream-2-0-usage-reports-using-amazon-athena-and-amazon-quicksight/). If you are using
Amazon WorkSpaces Applications features such as [Enable Application
Settings Persistence for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html) or [Enable and Administer Home
Folders for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders.html), include the underlying Amazon S3 buckets in
your cost and usage monitoring.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost02-bp01.html*

---
