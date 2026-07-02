# EUCCOST06 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# EUCCOST06-BP01 Explore a bring your own license (BYOL) approach

If you already have suitable license agreements with Microsoft
in place for Operating Systems or Microsoft Remote Desktop
Client Access Licenses, consider bringing these licenses for use
with AWS EUC services to reduce the cost.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

If you meet the requirements stated in [Amazon WorkSpaces FAQs](https://aws.amazon.com/workspaces/faqs/?nc1=h_ls#Windows_BYOL), Amazon WorkSpaces
allows you to [Bring Your Own Windows
desktop licenses in WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html) (BYOL) for Windows 10 and 11. This can reduce
your monthly or hourly WorkSpaces charges. When calculating the TCO, consider that BYOL
requires a certain minimum commitment of WorkSpaces per AWS Region that you want to deploy
in.

When using Amazon WorkSpaces Applications, you'll be charged a monthly user fee in the form of a
Microsoft RDS SAL fee. For more information , see [Amazon WorkSpaces Applications pricing](https://aws.amazon.com/appstream2/pricing/?nc1=h_ls). If you have
Microsoft License Mobility, you may be eligible to bring your own Microsoft RDS Client
Access License (CAL) licenses and use them with Amazon WorkSpaces Applications. For users covered by your own
licenses, you won't incur monthly WorkSpaces Applications user fees.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost06-bp01.html*

---
