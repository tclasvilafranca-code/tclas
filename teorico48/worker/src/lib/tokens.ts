function toHex(bytes: Uint8Array): string {
  return Array.from(bytes)
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

/** Token aleatorio para enlaces de un solo uso (reset de contraseña, verificación de email). */
export function randomToken(bytes = 32): string {
  return toHex(crypto.getRandomValues(new Uint8Array(bytes)));
}

/** Solo se guarda el hash del token en la base de datos, nunca el token en claro. */
export async function hashToken(rawToken: string): Promise<string> {
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(rawToken));
  return toHex(new Uint8Array(digest));
}

const CODE_ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; // sin O/0/I/1, para no confundirse al copiar a mano

/** Código de acceso legible (8 caracteres) para canjear en el registro. */
export function generateAccessCode(): string {
  const values = crypto.getRandomValues(new Uint32Array(8));
  let code = "";
  for (const v of values) {
    code += CODE_ALPHABET[v % CODE_ALPHABET.length];
  }
  return code;
}
