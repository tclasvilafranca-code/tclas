import { useState } from "react";
import type { FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { adminApi, AdminApiError } from "../../lib/adminApi";

export function AdminLogin() {
  const navigate = useNavigate();
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setBusy(true);
    try {
      await adminApi.login(password);
      navigate("/admin");
    } catch (err) {
      setError(err instanceof AdminApiError ? err.message : "No se pudo iniciar sesión");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="mx-auto max-w-sm px-4 py-20">
      <h1 className="mb-6 text-center text-2xl font-extrabold tracking-tight text-t48-ink">Panel de administrador</h1>
      <form onSubmit={handleSubmit} className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
        <label className="block text-sm font-semibold text-slate-600">
          Contraseña
          <input
            type="password"
            required
            autoFocus
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="mt-1.5 w-full rounded-xl border border-slate-200 px-3.5 py-2.5 outline-none transition-colors focus:border-t48-blue focus:ring-2 focus:ring-t48-blue/25"
          />
        </label>
        {error && <p className="mt-3 text-sm font-medium text-t48-red">{error}</p>}
        <button
          type="submit"
          disabled={busy}
          className="mt-6 w-full rounded-md bg-t48-blue px-4 py-3 font-semibold text-white transition-colors hover:bg-t48-blue-dark disabled:opacity-50"
        >
          {busy ? "Entrando..." : "Entrar"}
        </button>
      </form>
    </div>
  );
}
