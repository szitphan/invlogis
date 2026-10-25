[ApiController]
[ApiVersion("1.0")]
[Authorize]
[Route("items")]
public sealed class ItemsController(IFacade f) : ControllerBase
{
    private const PermissionLogic _any = PermissionLogic.Or;

    /// <summary>[HttpGet("ghost")] in comment</summary>
    [HttpGet]
    [HasPermission(DemoPermissionCodes.ItemsView)]
    [WorkingContextRequirement(WorkingContextRequirement.NoModuleContext)]
    public async Task<IActionResult> ListAsync() { return Ok("{not a brace"); }

    [HttpPost("{id:long}/submit")]
    [HasPermission(_any, DemoPermissionCodes.ItemsView, DemoPermissionCodes.ItemsMaintain)]
    public IActionResult Submit(long id) => Ok();

    [HttpDelete("/abs/{id}")]
    [AllowAnonymous]
    public IActionResult Remove(long id) { return Ok(); }
}
