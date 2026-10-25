public class ItemsTests
{
    [Fact]
    public void A() { /* DM-IT-AC-001 */ }

    [Theory]
    [InlineData(1)]
    [InlineData(2)]
    public void B(int x) { }
}
