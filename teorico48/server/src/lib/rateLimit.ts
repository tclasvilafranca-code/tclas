import rateLimit from "express-rate-limit";

/** Login y registro: limita intentos de fuerza bruta por IP. */
export const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 20,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "Demasiados intentos. Espera unos minutos y vuelve a intentarlo." },
});

/** Recuperación de contraseña: más restrictivo, evita usarlo para bombardear emails. */
export const forgotPasswordLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  limit: 5,
  standardHeaders: true,
  legacyHeaders: false,
  message: { error: "Demasiadas solicitudes. Espera unos minutos y vuelve a intentarlo." },
});
