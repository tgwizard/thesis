public class OrderInteractionTester
		extends MockObjectTestCase {
	private static String TALISKER = "Talisker";

	public void testFillingRemovesInventoryIfInStock() {
		// setup - data
		Order order = new Order(TALISKER, 50);
		Mock warehouseMock = new Mock(Warehouse.class);

		// setup - expectations
		warehouseMock.expects(once())
			.method("hasInventory")
			.with(eq(TALISKER),eq(50))
			.will(returnValue(true));
		warehouseMock.expects(once())
			.method("remove")
			.with(eq(TALISKER), eq(50))
			.after("hasInventory");

		// exercise
		order.fill((Warehouse) warehouseMock.proxy());

		// verify
		warehouseMock.verify();
		assertTrue(order.isFilled());
	}
}
