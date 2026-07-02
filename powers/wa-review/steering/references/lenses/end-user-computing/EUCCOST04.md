# EUCCOST04 — Cost effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# EUCCOST04-BP01 Tag your Amazon WorkSpaces and Amazon WorkSpaces Applications resources

[Tagging your Amazon WorkSpaces Applications resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html) or [tagging WorkSpaces
resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html) helps you allocate your cost to logical groups, such as departments or
business entities.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Plan your tagging strategy before you start deploying your EUC resources. You may
think of tagging EUC resources with information such as cost center, department,
usernames, projects, location, or deployment types (like development, test, and
production). The more dimensions you add with your tags, the easier it will be to report
and break down the cost once you are in production.

If you already use tagging in your organization, implement a standardized approach
for tagging that aligns with the approach being used by the rest of the organization,
which results in a standardized format for the key value pairs being used for tags in the
organization. Using [Service control
policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) with AWS Organizations enforces tags to restrict resource creation
unless they are correctly tagged.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost04-bp01.html*

---
