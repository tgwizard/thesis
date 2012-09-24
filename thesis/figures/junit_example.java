// required imports removed for brevity

public class TestSomeClass
		extends TestCase {
	private Environment;

	@Before
	public void setUp() {
		// setup the fixture for each test
		Environment = new Environment();
	}

	@After
	public void tearDown() {
		// clean up the fixture, free memory, etc.
	}

	@Test
	public void testSimpleAddition() {
		// use the language assertion construct
		assert 1+1 == 2
			// use JUnit's assertion functions
			assertEquals(4+7, 11)
	}

	@Test
	public void testThatDoWorkReturnsX() {
		// do setup for this test
		Target t = new Target(...);
		// exercise the object under test
		t.doWork(...);
		// do verification
		assert t.getValues() == x;
	}
}
