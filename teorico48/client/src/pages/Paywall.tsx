import { useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api, ApiError } from "../lib/api";

export function Paywall() {
  const { user, refreshUser } = useAuth();
  const [params] = useSearchParams();
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function handleCheckout() {
    setError(null);
    setBusy(true);
    try {
      const { url } = await api.checkout();
      window.location.href = url;
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "No se pudo iniciar el pago");
    } finally {
      setBusy(false);
    }
  }

  if (user?.isPremium) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <p className="text-2xl font-bold text-t48-green">Ya tienes el Pack 48h activo 🎉</p>
        <button onClick={() => navigate("/dashboard")} className="mt-4 rounded-lg bg-t48-blue px-4 py-2 font-semibold text-white">
          Ir al panel
        </button>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-md px-4 py-16">
      {params.get("success") && (
        <p className="mb-4 rounded-lg bg-t48-green/10 p-3 text-center text-t48-green">
          Pago recibido, confirmando tu acceso...{" "}
          <button onClick={() => refreshUser()} className="underline">Actualizar</button>
        </p>
      )}
      {params.get("canceled") && (
        <p className="mb-4 rounded-lg bg-t48-amber/10 p-3 text-center text-t48-amber">Pago cancelado.</p>
      )}

      <div className="rounded-xl border border-slate-200 bg-white p-6 text-center">
        <p className="text-sm font-semibold uppercase tracking-wide text-t48-amber">Pack 48h</p>
        <p className="mt-2 text-4xl font-extrabold text-t48-ink">9,99 €</p>
        <p className="mt-1 text-sm text-slate-500">Pago único, sin suscripción</p>
        <ul className="mt-5 space-y-2 text-left text-sm text-slate-600">
          <li>✔ Simulacros ilimitados</li>
          <li>✔ Modo repaso centrado en tus fallos</li>
          <li>✔ Plan de estudio con cuenta atrás</li>
        </ul>
        <button
          onClick={handleCheckout}
          disabled={busy}
          className="mt-6 w-full rounded-lg bg-t48-amber px-4 py-2.5 font-semibold text-white disabled:opacity-50"
        >
          {busy ? "Un momento..." : "Desbloquear ahora"}
        </button>
        {error && <p className="mt-3 text-sm text-t48-red">{error}</p>}
      </div>
    </div>
  );
}
