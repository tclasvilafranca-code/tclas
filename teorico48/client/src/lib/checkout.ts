import { api, ApiError } from "./api";

/** Crea la sesión de pago de la licencia y redirige a Stripe. Devuelve un
 * mensaje de error si algo falla, o null si la redirección ya está en marcha. */
export async function startLicenseCheckout(): Promise<string | null> {
  try {
    const { url } = await api.checkoutLicense();
    window.location.href = url;
    return null;
  } catch (err) {
    return err instanceof ApiError ? err.message : "No se pudo iniciar el pago";
  }
}
