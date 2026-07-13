import { useState } from "react";
import type { FormEvent } from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { api, ApiError } from "../lib/api";

export function ResetPassword() {
  const [params] = useSearchParams();
  const navigate = useNavigate();
  const uid = params.get("uid");
  const token = params.get("token");

  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [done, setDone] = useState(false);
  const [busy, setBusy] = useState(false);

  if (!uid || !token) {
    return (
      <div className="mx-auto max-w-sm px-4 py-20 text-center">
        <p className="font-medium text-t48-red">Este enlace no es válido.</p>
        <Link to="/forgot-password" className="mt-4 inline-block font-semibold text-t48-blue">
          Pedir un enlace nuevo
        </Link>
      </div>
    );
  }

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    if (password !== confirmPassword) {
      setError("Las contraseñas no coinciden");
      return;
    }
    setBusy(true);
    try {
      await api.resetPassword(uid as string, token as string, password);
      setDone(true);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "No se pudo restablecer la contraseña");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="mx-auto max-w-sm px-4 py-20">
      <h1 className="mb-6 text-center text-2xl font-extrabold tracking-tight text-t48-ink">Elige una nueva contraseña</h1>
      <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
        {done ? (
          <div className="text-center">
            <p className="text-sm text-slate-600">Tu contraseña se ha actualizado correctamente.</p>
            <button
              onClick={() => navigate("/login")}
              className="mt-4 w-full rounded-md bg-t48-blue px-4 py-3 font-semibold text-white transition-colors hover:bg-t48-blue-dark"
            >
              Ir a entrar
            </button>
          </div>
        ) : (
          <form onSubmit={handleSubmit}>
            <label className="block text-sm font-semibold text-slate-600">
              Nueva contraseña
              <input
                type="password"
                required
                minLength={6}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="mt-1.5 w-full rounded-xl border border-slate-200 px-3.5 py-2.5 outline-none transition-colors focus:border-t48-blue focus:ring-2 focus:ring-t48-blue/25"
              />
            </label>
            <label className="mt-4 block text-sm font-semibold text-slate-600">
              Repite la contraseña
              <input
                type="password"
                required
                minLength={6}
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="mt-1.5 w-full rounded-xl border border-slate-200 px-3.5 py-2.5 outline-none transition-colors focus:border-t48-blue focus:ring-2 focus:ring-t48-blue/25"
              />
            </label>
            {error && <p className="mt-3 text-sm font-medium text-t48-red">{error}</p>}
            <button
              type="submit"
              disabled={busy}
              className="mt-6 w-full rounded-md bg-t48-blue px-4 py-3 font-semibold text-white transition-colors hover:bg-t48-blue-dark disabled:opacity-50"
            >
              {busy ? "Guardando..." : "Guardar nueva contraseña"}
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
