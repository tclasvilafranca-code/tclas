import { useEffect, useState } from "react";
import type { FormEvent, ReactNode } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api, ApiError } from "../lib/api";
import type { Attempt, Stats } from "../lib/api";
import { badgeIcon } from "../lib/badgeIcons";
import { CheckCircle, Flame, Lock, Repeat, Star, Target } from "../components/Icons";

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
  const [stats, setStats] = useState<Stats | null>(null);
  const [examDateInput, setExamDateInput] = useState(user?.examDate?.slice(0, 16) ?? "");
  const [savingDate, setSavingDate] = useState(false);
  const [resendState, setResendState] = useState<"idle" | "sending" | "sent" | "error">("idle");

  async function handleResendVerification() {
    setResendState("sending");
    try {
      await api.resendVerification();
      setResendState("sent");
    } catch (err) {
      setResendState("error");
      if (!(err instanceof ApiError)) throw err;
    }
  }

  useEffect(() => {
    api.history().then((r) => setAttempts(r.attempts)).catch(() => {});
    api.stats().then(setStats).catch(() => {});
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

  const xpIntoLevel = stats ? stats.xp % 100 : 0;

  return (
    <div className="mx-auto max-w-3xl px-4 py-8 sm:py-10">
      <h1 className="text-2xl font-extrabold tracking-tight text-t48-ink">Hola de nuevo</h1>

      {user && !user.emailVerified && (
        <div className="mt-4 flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-amber-200 bg-amber-50 px-4 py-3 text-sm">
          <p className="text-amber-800">
            {resendState === "sent"
              ? "Te hemos enviado un nuevo enlace. Revisa tu bandeja de entrada (y spam)."
              : "Confirma tu email para proteger tu cuenta y poder recuperarla si lo necesitas."}
          </p>
          {resendState !== "sent" && (
            <button
              onClick={handleResendVerification}
              disabled={resendState === "sending"}
              className="shrink-0 rounded-md border border-amber-300 bg-white px-3 py-1.5 font-semibold text-amber-800 transition-colors hover:bg-amber-100 disabled:opacity-50"
            >
              {resendState === "sending" ? "Enviando..." : resendState === "error" ? "Reintentar" : "Reenviar email"}
            </button>
          )}
        </div>
      )}

      {stats && (
        <div className="mt-5 grid gap-3 sm:grid-cols-3">
          <StatCard icon={<Star className="h-4 w-4" />} label={`Nivel ${stats.level}`}>
            <div className="mt-1.5 h-1.5 w-full rounded-full bg-slate-100">
              <div className="h-1.5 rounded-full bg-t48-blue transition-all" style={{ width: `${xpIntoLevel}%` }} />
            </div>
            <p className="mt-1 text-xs text-slate-500">{stats.xp} XP</p>
          </StatCard>
          <StatCard icon={<Flame className="h-4 w-4" />} label={`${stats.currentStreak} día${stats.currentStreak === 1 ? "" : "s"} de racha`}>
            <p className="mt-1 text-xs text-slate-500">Récord: {stats.longestStreak}</p>
          </StatCard>
          <StatCard icon={<CheckCircle className="h-4 w-4" />} label={`${stats.totalPassed}/${stats.totalAttempts} aprobados`}>
            <p className="mt-1 text-xs text-slate-500">Tests completados</p>
          </StatCard>
        </div>
      )}

      <div className="mt-4 rounded-2xl border border-slate-200 bg-white p-6">
        <h2 className="font-bold text-t48-ink">Cuenta atrás hasta tu examen</h2>
        {countdown ? (
          countdown.past ? (
            <p className="mt-2 text-slate-500">¡Ya debería tocar tu examen! Actualiza la fecha si hace falta.</p>
          ) : (
            <p className="mt-2 text-3xl font-extrabold tabular-nums text-t48-blue">
              {countdown.hours}h {countdown.minutes}m {countdown.seconds}s
            </p>
          )
        ) : (
          <p className="mt-2 text-slate-500">Añade la fecha de tu examen para ver la cuenta atrás.</p>
        )}
        <form onSubmit={handleSaveDate} className="mt-4 flex flex-wrap items-end gap-3">
          <label className="text-sm font-semibold text-slate-600">
            Fecha y hora del examen
            <input
              type="datetime-local"
              value={examDateInput}
              onChange={(e) => setExamDateInput(e.target.value)}
              className="mt-1.5 block rounded-xl border border-slate-200 px-3.5 py-2.5 outline-none transition-colors focus:border-t48-blue focus:ring-2 focus:ring-t48-blue/25"
            />
          </label>
          <button
            type="submit"
            disabled={savingDate}
            className="rounded-md bg-t48-blue px-4 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark disabled:opacity-50"
          >
            Guardar
          </button>
        </form>
      </div>

      <div className="mt-4 grid gap-3 sm:grid-cols-2">
        <Link
          to="/exam"
          className="group rounded-2xl border border-slate-200 bg-white p-6 transition-all hover:-translate-y-0.5 hover:border-t48-blue hover:shadow-md"
        >
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue">
            <Target className="h-5 w-5" />
          </div>
          <h2 className="mt-3 font-bold text-t48-ink">Hacer un simulacro</h2>
          <p className="mt-1 text-sm text-slate-500">30 preguntas, como el examen real. Máx. 3 fallos.</p>
        </Link>
        <Link
          to="/review"
          className="group rounded-2xl border border-slate-200 bg-white p-6 transition-all hover:-translate-y-0.5 hover:border-t48-blue hover:shadow-md"
        >
          <div className="flex items-center justify-between">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue">
              <Repeat className="h-5 w-5" />
            </div>
            {!user?.isPremium && <Lock className="h-4 w-4 text-slate-300" />}
          </div>
          <h2 className="mt-3 font-bold text-t48-ink">Repasar mis fallos</h2>
          <p className="mt-1 text-sm text-slate-500">
            {user?.isPremium ? "Solo las preguntas que sueles fallar." : "Función del Pack 48h."}
          </p>
        </Link>
      </div>

      {!user?.isPremium && (
        <div className="mt-4 rounded-2xl border border-slate-200 bg-white p-5">
          <span className="inline-block rounded-md border border-amber-200 bg-amber-50 px-2 py-0.5 text-xs font-bold uppercase tracking-wide text-amber-700">
            Pack 48h
          </span>
          <p className="mt-2 font-bold text-t48-ink">Simulacros ilimitados + repaso de fallos</p>
          <p className="mt-1 text-sm text-slate-500">
            Con la cuenta gratis solo puedes hacer 1 simulacro al día.
          </p>
          <Link
            to="/paywall"
            className="mt-3 inline-block rounded-md bg-t48-blue px-4 py-2 text-sm font-semibold text-white transition-colors hover:bg-t48-blue-dark"
          >
            Ver Pack 48h
          </Link>
        </div>
      )}

      {stats && (
        <div className="mt-8">
          <h2 className="font-bold text-t48-ink">Medallas</h2>
          {stats.badges.every((b) => !b.unlocked) && (
            <p className="mt-1 text-sm text-slate-500">Haz tu primer test para empezar a desbloquearlas.</p>
          )}
          <div className="mt-3 flex flex-wrap gap-2">
            {stats.badges.map((b) => (
              <div
                key={b.id}
                title={b.label}
                aria-label={`${b.label}${b.unlocked ? "" : " (bloqueada)"}`}
                className={`flex items-center gap-1.5 rounded-md border px-3 py-1.5 text-sm font-medium ${
                  b.unlocked ? "border-slate-200 bg-white text-t48-ink" : "border-dashed border-slate-200 text-slate-300"
                }`}
              >
                <span className={b.unlocked ? "text-t48-blue" : ""}>{badgeIcon(b.id)}</span>
                {b.label}
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="mt-8">
        <h2 className="font-bold text-t48-ink">Historial reciente</h2>
        {attempts.length === 0 ? (
          <div className="mt-2 flex flex-wrap items-center gap-3">
            <p className="text-sm text-slate-500">Todavía no has hecho ningún test.</p>
            <Link to="/exam" className="text-sm font-bold text-t48-blue hover:text-t48-blue-dark">
              Hacer el primero →
            </Link>
          </div>
        ) : (
          <ul className="mt-3 divide-y divide-slate-100 rounded-2xl border border-slate-200 bg-white">
            {attempts.map((a) => (
              <li key={a.id} className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-slate-500">
                  {a.finishedAt ? new Date(a.finishedAt).toLocaleString() : "—"} · {a.mode === "exam" ? "Simulacro" : "Repaso"}
                </span>
                <span className={`font-bold ${a.passed ? "text-t48-green-dark" : "text-t48-red"}`}>
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

function StatCard({ icon, label, children }: { icon: ReactNode; label: string; children?: ReactNode }) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-4">
      <div className="flex items-center gap-2 text-t48-blue">
        {icon}
        <span className="font-bold text-t48-ink">{label}</span>
      </div>
      {children}
    </div>
  );
}
