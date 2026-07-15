import { describe, expect, it } from "vitest";
import bcrypt from "bcryptjs";
import { hashPassword, verifyPassword } from "./password";

describe("hashPassword / verifyPassword", () => {
  it("verifica correctamente una contraseña con su propio hash", async () => {
    const hash = await hashPassword("mi-contraseña-123");
    expect(await verifyPassword("mi-contraseña-123", hash)).toBe(true);
  });

  it("rechaza una contraseña incorrecta", async () => {
    const hash = await hashPassword("mi-contraseña-123");
    expect(await verifyPassword("otra-contraseña", hash)).toBe(false);
  });

  it("genera un hash distinto cada vez (salt aleatorio)", async () => {
    const a = await hashPassword("misma-contraseña");
    const b = await hashPassword("misma-contraseña");
    expect(a).not.toBe(b);
    expect(await verifyPassword("misma-contraseña", a)).toBe(true);
    expect(await verifyPassword("misma-contraseña", b)).toBe(true);
  });

  it("rechaza un hash con formato desconocido en vez de lanzar un error", async () => {
    expect(await verifyPassword("cualquiera", "no-es-un-hash-valido")).toBe(false);
  });

  it("sigue verificando cuentas antiguas creadas con bcrypt (antes de migrar a Cloudflare)", async () => {
    const legacyHash = await bcrypt.hash("contraseña-de-antes", 10);
    expect(await verifyPassword("contraseña-de-antes", legacyHash)).toBe(true);
    expect(await verifyPassword("otra-cosa", legacyHash)).toBe(false);
  });
});
