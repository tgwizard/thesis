describe("simple test of the adder module", function() {
  var adder;

  beforeEach(function() {
    adder = new Adder();
  });

  it("should return the sum of two values", function() {
    expect(adder.add(2, 7)).toEqual(9);
  });
});
