import { useState } from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api, ApiError } from "../lib/api";
import { CheckCircle } from "../components/Icons";

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
        <p className="text-2xl font-extrabold text-t48-green-dark">Ya tienes el Pack 48h activo</p>
        <button onClick={() => navigate("/dashboard")} className="btn-primary mt-4 px-4 py-2.5">
          Ir al panel
        </button>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-md px-4 py-16">
      {params.get("success") && (
        <p className="mb-4 animate-[fadeIn_0.3s_ease-out] rounded-xl bg-t48-green/10 p-3 text-center font-medium text-t48-green-dark">
          Pago recibido, confirmando tu acceso...{" "}
          <button onClick={() => refreshUser()} className="underline">Actualizar</button>
        </p>
      )}
      {params.get("canceled") && (
        <p className="mb-4 rounded-xl bg-t48-amber/10 p-3 text-center font-medium text-amber-700">Pago cancelado.</p>
      )}

      <div className="card-lift overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-sm">
        <div className="relative h-28 overflow-hidden">
          <img src="/images/wheel-dusk.jpg" alt="" aria-hidden="true" className="h-full w-full object-cover" />
          <div className="absolute inset-0 bg-gradient-to-t from-white via-white/10 to-transparent" />
        </div>
        <div className="-mt-8 px-7 pb-7 text-center">
          <span className="inline-block rounded-md border border-amber-200 bg-amber-50 px-2.5 py-1 text-xs font-bold uppercase tracking-wide text-amber-700 shadow-sm">
            Pack 48h
          </span>
          <p className="mt-3 text-5xl font-extrabold tracking-tight text-t48-ink">9,99 €</p>
          <p className="mt-1 text-sm text-slate-500">Pago único · sin suscripción</p>
          <ul className="mt-6 anim-stagger space-y-2.5 text-left text-sm font-medium text-slate-600">
            <li className="flex items-center gap-2">
              <CheckCircle className="h-4 w-4 shrink-0 text-t48-green-dark" /> Simulacros ilimitados
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle className="h-4 w-4 shrink-0 text-t48-green-dark" /> Modo repaso centrado en tus fallos
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle className="h-4 w-4 shrink-0 text-t48-green-dark" /> Plan de estudio con cuenta atrás
            </li>
          </ul>
          <button onClick={handleCheckout} disabled={busy} className="btn-primary mt-7 w-full py-3">
            {busy ? "Un momento..." : "Desbloquear ahora"}
          </button>
          {error && <p className="mt-3 text-sm font-medium text-t48-red">{error}</p>}
        </div>
      </div>
    </div>
  );
}
