# EUCOPS04 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# EUCOPS04-BP01 Identify the key capabilities and features that deliver business value and drive project success

While AWS EUC services may offer feature parity with your incumbent vendor, achieving
this parity may require additional engineering effort to integrate with existing operational
or support systems.

Planning for the proof of concept (PoC) or pilot phase of a migration project is an
opportunity to document acceptance criteria and define a list of the features and
functionality currently being delivered by your existing vendor. When moving into pilot and
production, these documents help you verify that all mandatory functionality has been tested
and can be successfully delivered.

Sacrificing features in order to take advantage of a more flexible cost and delivery
model for some user personas may be an acceptable approach. It may be feasible to deliver a
high percentage of your existing use cases, covering most of your user population using
built-in functionality and leaving just a small amount of engineering or the adoption of
third-party solutions to accommodate the remaining use cases.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

A PoC or pilot may reveal that it is not possible to deliver all of the features and
functionality offered by the incumbent EUC system. It may still be possible to roll out a
significant part of the project and reduce costs or realize many of the other benefits of
cloud delivery while investigating ways to bridge functionality gaps in areas where
feature parity cannot be maintained.

Following are some examples of where it may be possible to dispense with bundled EUC
functionality which is either no longer required or has been deprecated by new and
improved capabilities:

- Many existing EUC or VDI system features, such as those that optimize compute
resources, network bandwidth, or audio and video delivery, may no longer be required,
as compute, network, and media capabilities have vastly improved over time.
- Accessing your desktop or application resources from an HTML5 browser as standard
may be a significant change for the user experience, but standardization may offer
operational and support savings in the medium to longer term.
- Deploying WorkSpaces with Ubuntu for developers may reduce development costs for a
large population of users, moving away gradually from an incumbent, more costly EUC
solution.
- Using a vendor-supplied profile management solution may now be less functional
and performant than using a standard Microsoft solution such as FSLogix.
- It may be possible to dispense with complex legacy remote access solutions that
have evolved over time in favor of the pervasive and secure capabilities available
with the current generation of Amazon WorkSpaces and AppStream remoting protocols.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops04-bp01.html*

---
