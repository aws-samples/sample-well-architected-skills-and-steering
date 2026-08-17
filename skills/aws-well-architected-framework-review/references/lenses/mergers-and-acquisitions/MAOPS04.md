# MAOPS04 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

## MAOPS04-BP01 Standardize documented operational processes (like CI/CD and deployment)

Organizations incur operational tech debt during mergers and acquisitions.
Organizations should remove manual processes and focus on automation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

## MAOPS04-BP02 Retire or consolidate redundant apps and data-stores

Perform technical analysis during mergers and acquisitions. Otherwise, data and systems
can be duplicated, or even potentially orphaned. Both organizations should agree on a
consistent data model, consistent accesses, and compliance needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

## MAOPS04-BP03 Have a process in place for customer migration (if necessary)

Customer retention and migration is of utmost importance during mergers and
acquisitions. It is critical to support existing customers with optimal costs and negligible
impact. The AWS ISV Workload Migration Program (WMP) supports software partners that have
a SaaS offering on AWS to drive and deliver workload migrations. Use funding, technical
enablement, and go-to-market support to rapidly migrate customers to your SaaS offering.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

## MAOPS04-BP04 Understand third-party integrations and dependencies

It might happen that companies merge or multiple platforms get developed over time and
duplicate some of the same needed subsystems. Being service oriented and consolidating
services reduces the amount of code to be maintained.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

## MAOPS04-BP05 Perform all customizations through configuration, and change them as self-serve or company-controlled feature flags

Customizations that are done with configuration do not require a code recompile or
reload. It is a way to get away from the legacy practice of making hard-coded customizations
per individual customers or segments. Use feature flags that are temporary or permanent.
These flags help during testing or canary release.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
