**Saga**: Automated governance
**Capability**: AG.DLM — Data lifecycle management

---

# [AG.DLM.7] Ensure data safety with automated backup processes

**Category:** RECOMMENDED

Data loss can be catastrophic for any organization. Automated backup mechanisms help
to ensure that your data is not only routinely backed up, but also that these backups are
maintained and readily available when needed.  As data is constantly being created and
modified, these processes minimize the risk for data loss and reduce the manual,
error-prone manual approach of backing up data.

Define a backup policy that outlines the types of data to be
backed up, the frequency of backups, and the duration for
which backups should be retained. This policy should also
cover data restoration processes and timelines. Create backup
policies that best fit the classification of the data to avoid
backing up unnecessary data.

Choose backup tools that support automation and can be
integrated into your DevOps pipelines and environments. These
tools should have capabilities to schedule backups, maintain
and prune older backups, and ensure the integrity of the
backed-up data. For instance, during the development
lifecycle, trigger backups before altering environments with
business-critical data and in the case of rollbacks ensure
that the data was not impacted.

Regularly test the data restoration process to ensure that the
backed-up data can be effectively restored when required.
Regular audits and reviews of the backup policy and the
effectiveness of the backup process can help identify any gaps
or potential improvements. Alerts and reports should be
configured to provide visibility into the backup process and
notify teams about any issues.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS04-BP08 Back up
data only when difficult to recreate](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a9.html)
- [AWS Well-Architected Reliability Pillar: REL09-BP03 Perform
data backup automatically](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_automated_backups_data.html)
- [Centrally
manage and automate data protection - AWS Backup](https://aws.amazon.com/backup/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.7-ensure-data-safety-with-automated-backup-processes.html*
