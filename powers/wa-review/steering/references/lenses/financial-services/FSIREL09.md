**Pillar**: Reliability

# FSIREL09: How are you backing up data in the cloud?

Not all backups are created equal, and not all have equal value. Ensure that the
data you're backing up, and the way in which it is stored, is commensurate with the
value of the data backup.

## FSIREL09-BP01 Implement a backup strategy

A comprehensive backup strategy is an essential part of an organization's data
protection plan to withstand, recover from, and reduce any impact that might be
sustained due to a security event. You should create an extensive backup strategy that
defines which data must be backed up, how often data must be backed up, and monitoring
of backup and recovery tasks. It is equally important to highlight which data should
not be backed up; your backup strategy should balance the cost of implementing a
backup strategy and the cost of backup retention with the value of the backups. If
data is non-essential or could be reconstructed from other sources, make it clear to
teams that not everything has to be backed up.

## FSIREL09-BP02 Maintain backups in a secondary Region

When you develop a comprehensive strategy for backing up and restoring data,
consider backing up your data into another AWS Region allowing you to recover
quickly in the case of a disaster recovery scenario. For those applications with
criticality, requiring them to operate in multiple Regions makes sure that you replicate
your backups from the primary to the secondary Region. Copying backups between Regions
can be done using custom tooling or the original features of various AWS services
such as [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html).
Alternatively, management of backups between Regions, including the management of
encryption keys for cross-Region replication, can be automated and performed using
[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel09.html*
