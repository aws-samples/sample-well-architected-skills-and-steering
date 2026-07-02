# EUCSUS07 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# EUCSUS07-BP01 Identify the volume and data requirement for your user profiles

Each user persona may require different volume and performance to
align with your business case.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Limit user data to application data and mandatory user data
profile. It is a best practice to monitor the storage usage of
home folders, application settings persistence, or other storage
solutions like FSLogix, OneDrive, and Google Drive. With
FSLogix, enable de-duplication in FSx and VHD disk compaction.
Fsx for Windows / Fsx on tap.

For more information, see:

- [How
Application Settings Persistence Works](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-it-works-app-settings-persistence.html)
- [Use
Amazon FSx for Windows File Server and FSLogix to Optimize Application Settings Persistence on Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/use-amazon-fsx-and-fslogix-to-optimize-application-settings-persistence-on-amazon-appstream-2-0/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus07-bp01.html*

---
