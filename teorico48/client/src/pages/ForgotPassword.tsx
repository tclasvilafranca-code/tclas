import { useState } from "react";
import type { FormEvent } from "react";
import { Link } from "react-router-dom";
import { api, ApiError } from "../lib/api";

export function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [sent, setSent] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setBusy(true);
    try {
      await api.forgotPassword(email);
      setSent(true);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "No se pudo procesar la solicitud");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="mx-auto max-w-sm px-4 py-20">
      <h1 className="mb-6 text-center text-2xl font-extrabold tracking-tight text-t48-ink">Recuperar contraseña</h1>
      <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
        {sent ? (
          <p className="text-sm text-slate-600">
            Si existe una cuenta con ese email, te hemos enviado un enlace para elegir una nueva contraseña. Revisa
            también la carpeta de spam.
          </p>
        ) : (
          <form onSubmit={handleSubmit}>
            <label className="block text-sm font-semibold text-slate-600">
              Email
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="mt-1.5 w-full rounded-xl border border-slate-200 px-3.5 py-2.5 outline-none transition-colors focus:border-t48-blue focus:ring-2 focus:ring-t48-blue/25"
              />
            </label>
            {error && <p className="mt-3 text-sm font-medium text-t48-red">{error}</p>}
            <button
              type="submit"
              disabled={busy}
              className="mt-6 w-full rounded-md bg-t48-blue px-4 py-3 font-semibold text-white transition-colors hover:bg-t48-blue-dark disabled:opacity-50"
            >
              {busy ? "Enviando..." : "Enviar enlace"}
            </button>
          </form>
        )}
      </div>
      <p className="mt-4 text-center text-sm text-slate-500">
        <Link to="/login" className="font-semibold text-t48-blue">
          Volver a entrar
        </Link>
      </p>
    </div>
  );
}
