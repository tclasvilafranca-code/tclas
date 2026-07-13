import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api } from "../lib/api";
import type { Attempt } from "../lib/api";

function useCountdown(examDate: string | null) {
  const [now, setNow] = useState(Date.now());
  useEffect(() => {
    const id = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(id);
  }, []);
  if (!examDate) return null;
  const diffMs = new Date(examDate).getTime() - now;
  if (diffMs <= 0) return { hours: 0, minutes: 0, seconds: 0, past: true };
  const totalSeconds = Math.floor(diffMs / 1000);
  return {
    hours: Math.floor(totalSeconds / 3600),
    minutes: Math.floor((totalSeconds % 3600) / 60),
    seconds: totalSeconds % 60,
    past: false,
  };
}

export function Dashboard() {
  const { user, refreshUser } = useAuth();
  const countdown = useCountdown(user?.examDate ?? null);
  const [attempts, setAttempts] = useState<Attempt[]>([]);
  const [examDateInput, setExamDateInput] = useState(user?.examDate?.slice(0, 16) ?? "");
  const [savingDate, setSavingDate] = useState(false);

  useEffect(() => {
    api.history().then((r) => setAttempts(r.attempts)).catch(() => {});
  }, []);

  async function handleSaveDate(e: FormEvent) {
    e.preventDefault();
    setSavingDate(true);
    try {
      await api.setExamDate(examDateInput ? new Date(examDateInput).toISOString() : null);
      await refreshUser();
    } finally {
      setSavingDate(false);
    }
  }

  return (
    <div className="mx-auto max-w-3xl px-4 py-10">
      <h1 className="text-2xl font-bold text-t48-ink">Hola de nuevo</h1>

      <div className="mt-6 rounded-xl border border-slate-200 bg-white p-6">
        <h2 className="font-semibold text-t48-ink">Cuenta atrás hasta tu examen</h2>
        {countdown ? (
          countdown.past ? (
            <p className="mt-2 text-slate-600">¡Ya debería tocar tu examen! Actualiza la fecha si hace falta.</p>
          ) : (
            <p className="mt-2 text-3xl font-extrabold text-t48-blue">
              {countdown.hours}h {countdown.minutes}m {countdown.seconds}s
            </p>
          )
        ) : (
          <p className="mt-2 text-slate-500">Añade la fecha de tu examen para ver la cuenta atrás.</p>
        )}
        <form onSubmit={handleSaveDate} className="mt-4 flex flex-wrap items-end gap-3">
          <label className="text-sm font-medium text-slate-700">
            Fecha y hora del examen
            <input
              type="datetime-local"
              value={examDateInput}
              onChange={(e) => setExamDateInput(e.target.value)}
              className="mt-1 block rounded-lg border border-slate-300 px-3 py-2"
            />
          </label>
          <button
            type="submit"
            disabled={savingDate}
            className="rounded-lg bg-t48-blue px-4 py-2 font-semibold text-white hover:bg-t48-blue-dark disabled:opacity-50"
          >
            Guardar
          </button>
        </form>
      </div>

      <div className="mt-6 grid gap-4 sm:grid-cols-2">
        <Link
          to="/exam"
          className="rounded-xl border border-slate-200 bg-white p-6 hover:border-t48-blue"
        >
          <h2 className="font-bold text-t48-ink">Hacer un simulacro</h2>
          <p className="mt-1 text-sm text-slate-600">30 preguntas, como el examen real (máx. 3 fallos para aprobar).</p>
        </Link>
        <Link
          to="/review"
          className="rounded-xl border border-slate-200 bg-white p-6 hover:border-t48-blue"
        >
          <h2 className="font-bold text-t48-ink">Repasar mis fallos {!user?.isPremium && "🔒"}</h2>
          <p className="mt-1 text-sm text-slate-600">
            {user?.isPremium
              ? "Test centrado solo en las preguntas que sueles fallar."
              : "Función del Pack 48h — desbloquéala para repasar solo tus fallos."}
          </p>
        </Link>
      </div>

      {!user?.isPremium && (
        <div className="mt-6 rounded-xl border border-t48-amber/40 bg-t48-amber/10 p-5">
          <p className="font-semibold text-t48-ink">Simulacros ilimitados + repaso de fallos</p>
          <p className="mt-1 text-sm text-slate-600">
            Con la cuenta gratis solo puedes hacer 1 simulacro al día. Desbloquea el Pack 48h para no tener límites.
          </p>
          <Link to="/paywall" className="mt-3 inline-block rounded-lg bg-t48-amber px-4 py-2 font-semibold text-white">
            Ver Pack 48h
          </Link>
        </div>
      )}

      <div className="mt-8">
        <h2 className="font-semibold text-t48-ink">Historial reciente</h2>
        {attempts.length === 0 ? (
          <p className="mt-2 text-sm text-slate-500">Todavía no has hecho ningún test.</p>
        ) : (
          <ul className="mt-3 divide-y divide-slate-200 rounded-xl border border-slate-200 bg-white">
            {attempts.map((a) => (
              <li key={a.id} className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-slate-600">
                  {a.finishedAt ? new Date(a.finishedAt).toLocaleString() : "—"} · {a.mode === "exam" ? "Simulacro" : "Repaso"}
                </span>
                <span className={`font-semibold ${a.passed ? "text-t48-green" : "text-t48-red"}`}>
                  {a.score}/{a.total} {a.passed ? "Aprobado" : "Suspenso"}
                </span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
