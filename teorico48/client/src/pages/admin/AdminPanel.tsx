import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { adminApi, AdminApiError } from "../../lib/adminApi";
import type { AccessCode } from "../../lib/adminApi";

function codeStatus(c: AccessCode): { label: string; className: string } {
  if (c.usedAt) return { label: `Usado (${c.usedByEmail ?? "—"})`, className: "text-slate-400" };
  if (c.expiresAt && new Date(c.expiresAt).getTime() < Date.now()) {
    return { label: "Caducado", className: "text-t48-red" };
  }
  return { label: "Disponible", className: "text-t48-green-dark" };
}

export function AdminPanel() {
  const navigate = useNavigate();
  const [codes, setCodes] = useState<AccessCode[]>([]);
  const [loading, setLoading] = useState(true);
  const [count, setCount] = useState(1);
  const [note, setNote] = useState("");
  const [expiresInDays, setExpiresInDays] = useState("");
  const [generating, setGenerating] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [copiedCode, setCopiedCode] = useState<string | null>(null);

  async function loadCodes() {
    try {
      const { codes } = await adminApi.listCodes();
      setCodes(codes);
    } catch (err) {
      if (err instanceof AdminApiError && err.status === 401) {
        navigate("/admin/login");
        return;
      }
      throw err;
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadCodes();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function handleGenerate(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setGenerating(true);
    try {
      await adminApi.generateCodes({
        count,
        note: note.trim() || undefined,
        expiresInDays: expiresInDays ? Number(expiresInDays) : undefined,
      });
      setNote("");
      await loadCodes();
    } catch (err) {
      setError(err instanceof AdminApiError ? err.message : "No se pudieron generar los códigos");
    } finally {
      setGenerating(false);
    }
  }

  function copyCode(code: string) {
    navigator.clipboard.writeText(code);
    setCopiedCode(code);
    setTimeout(() => setCopiedCode(null), 1500);
  }

  function handleLogout() {
    adminApi.logout();
    navigate("/admin/login");
  }

  const available = codes.filter((c) => !c.usedAt && (!c.expiresAt || new Date(c.expiresAt).getTime() > Date.now()));

  return (
    <div className="mx-auto max-w-3xl px-4 py-8 sm:py-10">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-extrabold tracking-tight text-t48-ink">Códigos de acceso</h1>
        <button onClick={handleLogout} className="text-sm font-medium text-slate-500 hover:text-t48-ink">
          Salir
        </button>
      </div>
      <p className="mt-1 text-sm text-slate-500">{available.length} código(s) disponibles ahora mismo.</p>

      <form onSubmit={handleGenerate} className="mt-5 rounded-2xl border border-slate-200 bg-white p-5">
        <div className="grid gap-3 sm:grid-cols-3">
          <label className="text-sm font-semibold text-slate-600">
            Cuántos
            <input
              type="number"
              min={1}
              max={50}
              value={count}
              onChange={(e) => setCount(Number(e.target.value))}
              className="mt-1.5 w-full rounded-xl border border-slate-200 px-3 py-2 outline-none focus:border-t48-blue focus:ring-2 focus:ring-t48-blue/25"
            />
          </label>
          <label className="text-sm font-semibold text-slate-600 sm:col-span-2">
            Nota (opcional)
            <input
              type="text"
              placeholder="p. ej. compra 14/07, regalo..."
              value={note}
              onChange={(e) => setNote(e.target.value)}
              className="mt-1.5 w-full rounded-xl border border-slate-200 px-3 py-2 outline-none focus:border-t48-blue focus:ring-2 focus:ring-t48-blue/25"
            />
          </label>
        </div>
        <label className="mt-3 block text-sm font-semibold text-slate-600">
          Caduca en (días, opcional)
          <input
            type="number"
            min={1}
            placeholder="Sin caducidad si se deja vacío"
            value={expiresInDays}
            onChange={(e) => setExpiresInDays(e.target.value)}
            className="mt-1.5 w-full rounded-xl border border-slate-200 px-3 py-2 outline-none focus:border-t48-blue focus:ring-2 focus:ring-t48-blue/25 sm:w-56"
          />
        </label>
        {error && <p className="mt-3 text-sm font-medium text-t48-red">{error}</p>}
        <button
          type="submit"
          disabled={generating}
          className="mt-4 rounded-md bg-t48-blue px-4 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark disabled:opacity-50"
        >
          {generating ? "Generando..." : "Generar código(s)"}
        </button>
      </form>

      <div className="mt-6">
        {loading ? (
          <p className="text-sm text-slate-500">Cargando...</p>
        ) : codes.length === 0 ? (
          <p className="text-sm text-slate-500">Todavía no has generado ningún código.</p>
        ) : (
          <ul className="divide-y divide-slate-100 rounded-2xl border border-slate-200 bg-white">
            {codes.map((c) => {
              const status = codeStatus(c);
              return (
                <li key={c.id} className="flex flex-wrap items-center justify-between gap-2 px-4 py-3 text-sm">
                  <div className="flex items-center gap-2">
                    <code className="rounded-md bg-slate-100 px-2 py-1 font-mono font-semibold tracking-wide text-t48-ink">
                      {c.code}
                    </code>
                    <button
                      onClick={() => copyCode(c.code)}
                      className="text-xs font-semibold text-t48-blue hover:text-t48-blue-dark"
                    >
                      {copiedCode === c.code ? "¡Copiado!" : "Copiar"}
                    </button>
                    {c.note && <span className="text-slate-400">· {c.note}</span>}
                  </div>
                  <span className={`font-semibold ${status.className}`}>{status.label}</span>
                </li>
              );
            })}
          </ul>
        )}
      </div>
    </div>
  );
}
