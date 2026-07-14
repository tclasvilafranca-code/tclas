import { describe, expect, it } from "vitest";
import { isPassed } from "./generator";

describe("isPassed", () => {
  it("aprueba con 0 fallos", () => {
    expect(isPassed(30, 30)).toBe(true);
  });

  it("aprueba con exactamente 3 fallos (el límite real de la DGT)", () => {
    expect(isPassed(27, 30)).toBe(true);
  });

  it("suspende con 4 fallos", () => {
    expect(isPassed(26, 30)).toBe(false);
  });

  it("funciona igual con totales distintos de 30", () => {
    expect(isPassed(7, 10)).toBe(true); // 3 fallos
    expect(isPassed(6, 10)).toBe(false); // 4 fallos
  });
});
