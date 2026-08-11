# Reliability

**Pillar**: Reliability  
**Pages**: 1

---

# MD_REL 1 How do you safely retain data for future generations?

Māori data is often considered taonga, and it is critical that this data is available for
future generations. Whakapapa (genealogy) or mātauranga Māori (Māori knowledge) are examples
where long-term retention and protection is important.

- **MD_REL01-BP01: Design storage systems with multi-generational
durability in mind**. Multi-generational durability focuses on the reliability
of having access to that data across generations. This applies to the data that you are
storing, but also associated metadata that provides context for that data. The
Well-Architected Reliability Pillar provides guidance on best practices for architecting
resilient workloads, backing up data, and planning for disasters. By understanding what
kinds of data you are storing and the possible need for the long-term preservation of that
data, you can choose appropriate architectural patterns and services such as Amazon S3, which
creates six copies of your data and is designed to provide 99.999999999% (11 nines) of
durability. In practice, 11 nines of durability means that if you stored ten million
objects, you might expect to lose a single object every 10,000 years.
- **MD_REL01-BP02: Consider how your organisational archive and
retention processes apply to Māori data.** Many organisations have data
retention and archiving processes that govern how long data is retained and how and where
it is stored.
- **MD_REL01-BP03: Configure your AWS account for long term
continuity**. Within each of your AWS accounts, it is important to have
accurate and up-to-date contact details, payment/credit card information, and multi-factor
authentication (MFA) for users. Keeping your contact information up-to-date helps ensure
that you receive important notifications from AWS on topics like security, billing, and
operations. It is a best practice to use an email distribution list, rather than depending
on an individual's email address. This can help avoid scenarios where important
notifications from AWS are missed if an individual is on leave or has left the
organisation.
- **MD_REL01-BP04: Implement backup mechanisms**. The
Reliability Pillar provides guidance on designing, implementing, and operating a backup
solution for your data and applications. The nature of the Māori data being captured,
processed, or stored influences the design of the backup solution. For example, an iwi
register application or a digital archive application might call for multiple copies of
backups to be stored in different locations, with different access controls due to the
value of those datasets. While it may seem redundant, it's important to store backups
across multiple different types of storage and in multiple different locations. This helps
ensure there's always an available backup, no matter the circumstances. Where
irreplaceable digital taonga is identified, it is important to consider offline
replication in addition to the appropriate security and reliability controls.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_rel-1-how-do-you-safely-retain-data-for-future-generations.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
