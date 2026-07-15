import bcrypt from "bcryptjs";

// Cloudflare Workers (plan gratuito) limita cada petición a 10ms de CPU.
// bcrypt (usado en la versión Node/Express) es JS puro y con coste 10 supera
// ese presupuesto por sí solo. PBKDF2 vía WebCrypto nativo es una función de
// derivación de clave igual de reconocida y corre en C++ dentro del propio
// runtime, no en JavaScript, así que es mucho más rápida en este entorno.
const ITERATIONS = 100_000;
const SALT_BYTES = 16;
const HASH_BITS = 256;

function toHex(buffer: ArrayBuffer): string {
  return Array.from(new Uint8Array(buffer))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

function fromHex(hex: string): Uint8Array {
  const bytes = new Uint8Array(hex.length / 2);
  for (let i = 0; i < bytes.length; i++) {
    bytes[i] = parseInt(hex.substring(i * 2, i * 2 + 2), 16);
  }
  return bytes;
}

/** Comparación en tiempo constante: evita filtrar por temporización cuánto
 * coincide un hash con otro, aunque aquí ya operamos sobre hashes derivados
 * (no la contraseña en claro), así que es una capa extra de precaución. */
function timingSafeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) {
    diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  }
  return diff === 0;
}

async function derive(password: string, salt: Uint8Array, iterations: number): Promise<string> {
  const keyMaterial = await crypto.subtle.importKey("raw", new TextEncoder().encode(password), "PBKDF2", false, ["deriveBits"]);
  const derivedBits = await crypto.subtle.deriveBits({ name: "PBKDF2", salt, iterations, hash: "SHA-256" }, keyMaterial, HASH_BITS);
  return toHex(derivedBits);
}

export async function hashPassword(password: string): Promise<string> {
  const salt = crypto.getRandomValues(new Uint8Array(SALT_BYTES));
  const hash = await derive(password, salt, ITERATIONS);
  return `pbkdf2$${ITERATIONS}$${toHex(salt.buffer)}$${hash}`;
}

export async function verifyPassword(password: string, stored: string): Promise<boolean> {
  // Compatibilidad hacia atrás: si la cuenta se creó antes de migrar a
  // Cloudflare, su hash sigue en formato bcrypt (empieza por $2a$/$2b$/$2y$).
  // Se verifica igual con bcryptjs para no dejar fuera a nadie que ya se
  // hubiera registrado; toda cuenta nueva usa PBKDF2 desde el principio.
  if (/^\$2[aby]\$/.test(stored)) {
    return bcrypt.compare(password, stored);
  }

  const parts = stored.split("$");
  if (parts.length !== 4 || parts[0] !== "pbkdf2") return false;
  const iterations = Number(parts[1]);
  if (!Number.isInteger(iterations) || iterations <= 0) return false;
  const salt = fromHex(parts[2]);
  const expected = parts[3];
  const actual = await derive(password, salt, iterations);
  return timingSafeEqual(actual, expected);
}
