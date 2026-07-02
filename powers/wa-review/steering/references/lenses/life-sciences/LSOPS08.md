# LSOPS08 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS08-BP01 Continuously generate and maintain evidence

Use appropriate IT tooling to generate evidence used for regulatory
requirements. Maintain audit trails of the changes, approvals, and
validations. Store the data in an immutable store. Generate reports
as needed from the data. Enable immediate access to evidence during
inspections or audits.

**Desired outcome:** You have a body
of evidence ready for auditors.

**Benefits of establishing this best
practice:** Smoother audit process with less wasted time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Start with a clear understanding of what is required, and build
audit readiness practices around those requirements.

### Implementation steps

- Define evidence requirements based on regulatory
obligations:

- Map evidence needs to specific regulations like 21 CFR Part
11, GxP, or HIPAA.
- Consider AWS Audit Manager for creating custom evidence
collection frameworks.

- Implement automated evidence collection mechanisms:

- Configure AWS Config to capture resource configurations and
changes.
- Enable AWS CloudTrail for comprehensive API activity
logging.
- Consider Amazon CloudWatch for operational metrics and logs.

- Establish centralized, secure evidence repositories:

- Use Amazon S3 with appropriate encryption and access
controls.
- Consider S3 Object Lock for immutable evidence storage.
- Implement AWS Backup for evidence protection and retention.

- Create structured evidence organization with metadata:

- Implement Amazon S3 metadata tagging for evidence
classification.
- Consider AWS Glue for cataloging and organizing audit
artifacts.

- Generate reports for audits and inspections:

- Use AWS Audit Manager for automated report generation.
- Consider Quick for audit visualization and
reporting.

- Implement appropriate retention policies for documentation:

- Configure S3 Lifecycle policies for evidence retention.
- Consider AWS Backup for long-term archival of documentation.

## Resources

**Related documents:**

- [Guidance
for Change Management on AWS](https://aws.amazon.com/solutions/guidance/change-management-on-aws/)
- [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html)
- [Logging
AWS Account Management API calls using AWS CloudTrail](https://docs.aws.amazon.com/accounts/latest/reference/monitoring-cloudtrail.html)
- [How
can I secure the files in my Amazon S3 bucket?](https://repost.aws/knowledge-center/secure-s3-resources)

**Related examples:**

- [Streamline
and automate compliance monitoring and reporting with AWS Backup Audit Manager](https://aws.amazon.com/blogs/storage/streamline-and-automate-compliance-monitoring-and-reporting-with-aws-backup-audit-manager/)
- [Leveraging
AWS CloudTrail Insights for Proactive API Monitoring and Cost
Optimization](https://aws.amazon.com/blogs/mt/leveraging-aws-cloudtrail-insights-for-proactive-api-monitoring-and-cost-optimization/)

**Related tools:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [Quick](https://aws.amazon.com/quicksight/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops08-bp01.html*

---
