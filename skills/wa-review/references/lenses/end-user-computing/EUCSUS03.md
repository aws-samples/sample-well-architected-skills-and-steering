# EUCSUS03 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 2

---

# EUCSUS03-BP01 Adapt your WorkSpaces Applications fleet timeout

Configure timeouts for WorkSpaces Applications fleets to minimize unnecessary resource consumption
whilst also factoring in usability. Minimize resource consumption by verifying that
instances are not consuming resources unnecessarily when users are not using them or
unlikely to use them.

Usability is an important consideration when shortening
timeouts. Setting them too low results in sessions being
terminated too early with the risk of impacting user
productivity, whereas setting them too high results in instances
running without any users, which incurs a higher carbon
footprint as well as higher costs.

Strike an appropriate balance in timeout durations to maintain
user productivity while reducing resource consumption in periods
of low usage.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

You can select a session duration to configure a maximum active session for a user,
which defaults to 16 hours. Disconnect timeout and idle disconnect timeout determine when
to log off an existing user session. By default, they are both configured at 15 minutes
each. The default value can be reduced without disrupting the end user experience.

For example, you can set the idle disconnect timeout for five minutes. You can set
timecout configurations in the [fleet console](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus03-bp01.html*

---

# EUCSUS03-BP02 Adapt the AutoStop timeout and idle disconnect timeout for Amazon DCV

The AutoStop timeout in WorkSpaces is only available with AutoStop. This is not applicable
to AlwaysOn WorkSpaces. In WorkSpaces, you can configure how long a user can be inactive while
connected to a WorkSpace before they are disconnected. Amazon DCV (Desktop Cloud Virtualization)
is the remote display protocol used by Amazon WorkSpaces to stream pixels, keystrokes and mouse
movements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

By default, AutoStop time (in
hours**)** is set to one hour,
which means that the WorkSpace stops automatically an hour
after the WorkSpace is disconnected.  Keep the AutoStop time
at the default value, as this is the lowest value offered.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus03-bp02.html*

---
