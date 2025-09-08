// sum.test.ts
import { sum } from "./sum";

describe("sum", () => {
  it("adds two numbers correctly", () => {
    expect(sum(2, 3)).toBe(5);
  });

  it("works with negative numbers", () => {
    expect(sum(-2, -3)).toBe(-5);
  });
});
