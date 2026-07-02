# EUCPERF10 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# EUCPERF10-BP01 Align the instance type and instance size of a fleet with the workload

As needed, user environments can be updated on a pre-determined schedule or in response
to periodic changes in performance to satisfy a change in the anticipated demand for
resources.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Determine the optimal instance family and size for your applications.

- The non-graphics instance families can utilize the same image across them. This
provides image portability across these instance families and the instance sizes
associated with them and allows varying requirements for compute resources to be
catered for.
- Images created for a graphics instance family (for example, stream.graphics.g5)
can only be associated with that family due to the specific GPU drivers for the
associated GPU. Consequently, choose a graphics instance family carefully from the
outset to avoid the need to create a new image for a different GPU family.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp01.html*

---

# EUCPERF10-BP02 Enable self-service WorkSpaces Personal management capabilities, and allow users to request changes by an administrator

The WorkSpaces Personal self-service options allow users to ramp up or down instance
performance over time.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Enable user self-service where possible to optimize processes.

- Identify the most flexible compute types for users to anticipate required changes
in performance. Consider the following:

You can change the compute type from Graphics.g4dn to GraphicsPro.g4dn, or
from GraphicsPro.g4dn to Graphics.g4dn.
- However, you cannot change the compute type of Graphics.g4dn and
GraphicsPro.g4dn to other types.
- You cannot change the compute type of Graphics and GraphicsPro to another
type.

- Consider these capabilities and limitations when initially configuring your
users' environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp02.html*

---

# EUCPERF10-BP03 Install only the application features required by end users

Some applications provide the ability to tailor an installation to remove features that
are not required by users.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Do not install application features not required by users. Install the minimal set of
features in applications that are required by users to perform their roles. This helps to
reduce compute requirements and also helps to remove potential security risks that may
arise that are associated with those features.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp03.html*

---

# EUCPERF10-BP04 Remove caches, temporary data, log files, and unneeded files such as tutorials and sample data before creating an image

Remove non-required files that are installed, downloaded, or created by applications to
optimize storage consumption.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Remove unneeded files from images to optimize storage consumption.

Unnecessary files included in an Amazon WorkSpaces golden image use space for each WorkSpace
provisioned using that image. Similarly, for Amazon WorkSpaces Applications where the image builder
volume size is limited, removing unneeded files can provide additional storage space for
other applications.

Consider data access patterns and whether data not included in an image can be
downloaded when needed. For example, if 10% of users access an application library that
can be downloaded when needed, omit the library from images.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp04.html*

---

# EUCPERF10-BP05 Tune application performance where possible to optimize compute resource usage

To provide the optimal access to compute resource for your applications, consider
tuning the performance of applications or software where possible to reduce their compute
resource utilization.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

By reducing the compute resource utilization for software used to provide non-end
user facing functionality, such as security agents, additional resources are made
available to benefit the applications users interact with. The disabling of non-essential
functionality within software can yield a performance benefit for end user software.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp05.html*

---
