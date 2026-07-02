# EUCSUS05 — Software and architecture

**Pillar**: Sustainability  
**Best Practices**: 1

---

# EUCSUS05-BP01 Optimize machine image creation, copying, and sharing to each environment (like development, testing, and production)

Using automation with machine images facilitates scalability and
elasticity, minimizing over-provisioning and associated energy
consumption. Centralized management and compliance reporting
further support sustainability initiatives. Overall, automation
pipelines contribute to lower environmental impact and improved
resource optimization.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

Use a dedicated and separate account to create your Amazon AppStream images to manage your
changes and your image history. Push the image (copy or share) with other development or
production AWS accounts. For more detail, see [UpdateImagePermissions](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateImagePermissions.html) and [UpdateWorkspaceImagePermission](https://docs.aws.amazon.com/workspaces/latest/api/API_UpdateWorkspaceImagePermission.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus05-bp01.html*

---
