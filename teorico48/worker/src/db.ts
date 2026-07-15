import { Pool } from "pg";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "@prisma/client";
import type { Env } from "./types";

/** Crea un cliente Prisma nuevo por petición, usando el pool de conexiones
 * que da Cloudflare Hyperdrive (necesario porque un Worker no puede mantener
 * una conexión TCP abierta entre peticiones como sí puede un servidor Node
 * normal). Hyperdrive.connectionString ya resuelve la contraseña real de la
 * base de datos: nunca hace falta guardarla aparte como secreto del Worker. */
export function createPrisma(env: Env) {
  const pool = new Pool({ connectionString: env.HYPERDRIVE.connectionString });
  const adapter = new PrismaPg(pool);
  return new PrismaClient({ adapter });
}
