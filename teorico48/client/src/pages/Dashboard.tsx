import { useEffect, useState } from "react";
import type { FormEvent, ReactNode } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api, ApiError } from "../lib/api";
import type { Attempt, CategoryStat, Stats } from "../lib/api";
import { badgeIcon } from "../lib/badgeIcons";
import { computeReadiness } from "../lib/readiness";
import { BarChart, BookOpen, Calendar, CheckCircle, Flame, Repeat, Star, Target } from "../components/Icons";
import { AnimatedNumber } from "../components/AnimatedNumber";
import { PlanCard } from "../components/PlanCard";
import { InstallAppPrompt } from "../components/InstallAppPrompt";
import { ScoreRing } from "../components/ScoreRing";
import { THEORY_EXPRESS } from "../content/theoryExpress";

function readinessColor(percent: number): string {
  if (percent >= 80) return "var(--color-t48-green-dark)";
  if (percent >= 50) return "var(--color-t48-amber)";
  return "var(--color-t48-red)";
}

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
  const [categories, setCategories] = useState<CategoryStat[]>([]);
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
    api.categoryStats().then((r) => setCategories(r.categories)).catch(() => {});
  }, []);

  const readiness = computeReadiness(attempts, categories);

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

      <InstallAppPrompt />

      <PlanCard stats={stats} />

      {stats && (
        <div className="mt-5 grid anim-stagger gap-3 sm:grid-cols-3">
          <StatCard icon={<Star className="h-4 w-4" />} label={<>Nivel <AnimatedNumber value={stats.level} /></>}>
            <div className="progress-track mt-1.5 h-1.5 w-full rounded-full">
              <div className="progress-fill h-1.5 rounded-full" style={{ width: `${xpIntoLevel}%` }} />
            </div>
            <p className="mt-1 text-xs text-slate-500">
              <AnimatedNumber value={stats.xp} /> XP
            </p>
          </StatCard>
          <StatCard
            icon={<Flame className={`h-4 w-4 ${stats.currentStreak > 0 ? "text-t48-amber" : ""}`} />}
            label={<><AnimatedNumber value={stats.currentStreak} /> día{stats.currentStreak === 1 ? "" : "s"} de racha</>}
          >
            <p className="mt-1 text-xs text-slate-500">
              Récord: <AnimatedNumber value={stats.longestStreak} />
            </p>
          </StatCard>
          <StatCard icon={<CheckCircle className="h-4 w-4" />} label={<><AnimatedNumber value={stats.totalPassed} />/{stats.totalAttempts} aprobados</>}>
            <p className="mt-1 text-xs text-slate-500">Tests completados</p>
          </StatCard>
        </div>
      )}

      <div className="card-lift mt-4 rounded-2xl border border-slate-200 bg-white p-6">
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
          <button type="submit" disabled={savingDate} className="btn-primary px-4 py-2.5">
            Guardar
          </button>
        </form>
      </div>

      <Link to="/pedir-examen" className="card-lift group mt-4 flex items-center justify-between gap-4 rounded-2xl border border-slate-200 bg-white p-5 hover:border-t48-blue">
        <div className="flex min-w-0 items-center gap-4">
          <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue transition-transform duration-200 group-hover:scale-105">
            <Calendar className="h-5 w-5" />
          </div>
          <div className="min-w-0 flex-1">
            <h2 className="font-bold text-t48-ink">Pide tu cita para el examen real</h2>
            <p className="mt-0.5 text-sm text-slate-500">Cuando te sientas listo, así se pide de verdad en la DGT.</p>
          </div>
        </div>
        {readiness && (
          <div className="flex shrink-0 flex-col items-center">
            <ScoreRing percent={readiness.percent} color={readinessColor(readiness.percent)} size={56} />
            <span className="mt-1 whitespace-nowrap text-[10px] font-semibold uppercase tracking-wide text-slate-400">
              Preparación
            </span>
          </div>
        )}
      </Link>

      <Link to="/teoria" className="card-lift group mt-4 flex items-center gap-4 rounded-2xl border border-slate-200 bg-white p-5 hover:border-t48-blue">
        <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue transition-transform duration-200 group-hover:scale-105">
          <BookOpen className="h-5 w-5" />
        </div>
        <div className="min-w-0 flex-1">
          <h2 className="font-bold text-t48-ink">Teoría Express</h2>
          <p className="mt-0.5 text-sm text-slate-500">
            Lo esencial del temario en 3 sesiones cortas
            {user ? ` · ${(user.theoryCompletedSessions ?? []).length}/${THEORY_EXPRESS.length} completadas` : ""}
          </p>
        </div>
      </Link>

      <Link to="/learn" className="card-lift group mt-4 flex items-center gap-4 rounded-2xl border border-slate-200 bg-white p-5 hover:border-t48-blue">
        <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue transition-transform duration-200 group-hover:scale-105">
          <CheckCircle className="h-5 w-5" />
        </div>
        <div className="min-w-0 flex-1">
          <h2 className="font-bold text-t48-ink">Modo Aprendizaje</h2>
          <p className="mt-0.5 text-sm text-slate-500">Corrección al instante, pregunta a pregunta. Gratis y sin límite.</p>
        </div>
      </Link>

      <Link to="/categorias" className="card-lift group mt-4 flex items-center gap-4 rounded-2xl border border-slate-200 bg-white p-5 hover:border-t48-blue">
        <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue transition-transform duration-200 group-hover:scale-105">
          <BarChart className="h-5 w-5" />
        </div>
        <div className="min-w-0 flex-1">
          <h2 className="font-bold text-t48-ink">Por categorías</h2>
          <p className="mt-0.5 text-sm text-slate-500">Descubre en qué fallas más y practica justo eso.</p>
        </div>
      </Link>

      <div className="mt-4 grid gap-3 sm:grid-cols-2">
        <Link to="/exam" className="card-lift group rounded-2xl border border-slate-200 bg-white p-6 hover:border-t48-blue">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue transition-transform duration-200 group-hover:scale-105">
            <Target className="h-5 w-5" />
          </div>
          <h2 className="mt-3 font-bold text-t48-ink">Hacer un simulacro</h2>
          <p className="mt-1 text-sm text-slate-500">30 preguntas, como el examen real. Máx. 3 fallos.</p>
        </Link>
        <Link to="/review" className="card-lift group rounded-2xl border border-slate-200 bg-white p-6 hover:border-t48-blue">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue transition-transform duration-200 group-hover:scale-105">
            <Repeat className="h-5 w-5" />
          </div>
          <h2 className="mt-3 font-bold text-t48-ink">Repasar mis fallos</h2>
          <p className="mt-1 text-sm text-slate-500">Solo las preguntas que sueles fallar.</p>
        </Link>
      </div>

      {stats && (
        <div className="mt-8">
          <h2 className="font-bold text-t48-ink">Medallas</h2>
          {stats.badges.every((b) => !b.unlocked) && (
            <p className="mt-1 text-sm text-slate-500">Haz tu primer test para empezar a desbloquearlas.</p>
          )}
          <div className="mt-3 flex flex-wrap gap-2 anim-stagger">
            {stats.badges.map((b) => (
              <div
                key={b.id}
                title={b.label}
                aria-label={`${b.label}${b.unlocked ? "" : " (bloqueada)"}`}
                className={`flex items-center gap-1.5 rounded-md border px-3 py-1.5 text-sm font-medium transition-transform duration-150 ${
                  b.unlocked ? "border-slate-200 bg-white text-t48-ink hover:-translate-y-0.5 hover:shadow-sm" : "border-dashed border-slate-200 text-slate-300"
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
              <li key={a.id} className="flex items-center justify-between px-4 py-3 text-sm transition-colors hover:bg-slate-50">
                <span className="text-slate-500">
                  {a.finishedAt ? new Date(a.finishedAt).toLocaleString() : "—"} ·{" "}
                  {a.mode === "exam" ? "Simulacro" : a.mode === "learn" ? "Aprendizaje" : "Repaso"}
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

function StatCard({ icon, label, children }: { icon: ReactNode; label: ReactNode; children?: ReactNode }) {
  return (
    <div className="card-lift rounded-2xl border border-slate-200 bg-white p-4">
      <div className="flex items-center gap-2 text-t48-blue">
        {icon}
        <span className="font-bold tabular-nums text-t48-ink">{label}</span>
      </div>
      {children}
    </div>
  );
}
