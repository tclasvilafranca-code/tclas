import { Link, useLocation, useNavigate } from "react-router-dom";
import type { SubmitResult } from "../lib/api";
import { badgeIcon } from "../lib/badgeIcons";
import { Flame, Star } from "../components/Icons";

export function Results() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = (location.state as { result?: SubmitResult } | null)?.result;

  if (!result) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <p className="text-slate-400">No hay resultados que mostrar.</p>
        <button
          onClick={() => navigate("/dashboard")}
          className="mt-4 rounded-xl bg-t48-blue px-4 py-2.5 font-bold text-white transition-transform hover:scale-[1.02] active:scale-95"
        >
          Volver al panel
        </button>
      </div>
    );
  }

  const fails = result.total - result.score;
  const pct = Math.round((result.score / result.total) * 100);
  const g = result.gamification;

  return (
    <div className="mx-auto max-w-2xl px-4 py-10">
      <div
        className={`animate-[popIn_0.35s_ease-out] rounded-3xl border p-8 text-center ${
          result.passed ? "border-t48-green/30 bg-t48-green/10" : "border-t48-red/30 bg-t48-red/10"
        }`}
      >
        <p className="text-6xl font-extrabold tabular-nums text-t48-ink">{pct}%</p>
        <p className={`mt-2 text-2xl font-extrabold ${result.passed ? "text-t48-green-dark" : "text-t48-red"}`}>
          {result.passed ? "¡Aprobado!" : "Suspenso, pero cerca"}
        </p>
        <p className="mt-1 text-slate-500">
          {result.score}/{result.total} correctas · {fails} fallo{fails !== 1 ? "s" : ""} (máx. 3 para aprobar)
        </p>

        {g && (
          <div className="mt-5 flex flex-wrap items-center justify-center gap-2">
            <span className="rounded-full bg-t48-blue/10 px-3 py-1 text-sm font-bold text-t48-blue-dark">
              +{g.xpGained} XP
            </span>
            {g.leveledUp && (
              <span className="flex items-center gap-1.5 rounded-full bg-t48-amber/20 px-3 py-1 text-sm font-bold text-amber-700">
                <Star className="h-3.5 w-3.5" /> Nivel {g.level}
              </span>
            )}
            {g.currentStreak > 1 && (
              <span className="flex items-center gap-1.5 rounded-full bg-orange-50 px-3 py-1 text-sm font-bold text-orange-600">
                <Flame className="h-3.5 w-3.5" /> Racha de {g.currentStreak}
              </span>
            )}
          </div>
        )}

        {g && g.newBadges.length > 0 && (
          <div className="mt-4 flex flex-wrap justify-center gap-2">
            {g.newBadges.map((b) => (
              <span
                key={b.id}
                className="animate-[popIn_0.4s_ease-out] flex items-center gap-1.5 rounded-full bg-white px-3 py-1.5 text-sm font-bold text-t48-ink shadow-sm"
              >
                {badgeIcon(b.id)} Nueva medalla: {b.label}
              </span>
            ))}
          </div>
        )}
      </div>

      <div className="mt-8 space-y-3">
        {result.results.map((r) => (
          <div
            key={r.questionId}
            className={`rounded-2xl border p-4 ${r.correct ? "border-slate-200" : "border-t48-red/30 bg-t48-red/5"}`}
          >
            <p className="text-xs font-bold uppercase tracking-wide text-t48-blue">{r.category}</p>
            <p className="mt-1 font-semibold text-t48-ink">{r.text}</p>
            <p className="mt-2 text-sm">
              Tu respuesta:{" "}
              <span className={r.correct ? "font-medium text-t48-green-dark" : "font-medium text-t48-red"}>
                {r.selectedIndex !== null ? r.options[r.selectedIndex] : "(sin responder)"}
              </span>
            </p>
            {!r.correct && (
              <p className="text-sm font-medium text-t48-green-dark">Correcta: {r.options[r.correctIndex]}</p>
            )}
            <p className="mt-2 text-sm text-slate-500">{r.explanation}</p>
          </div>
        ))}
      </div>

      <div className="mt-8 flex justify-center gap-3">
        <Link
          to="/dashboard"
          className="rounded-xl border border-slate-200 px-5 py-2.5 font-bold text-slate-600 transition-colors hover:bg-slate-50"
        >
          Volver al panel
        </Link>
        <Link
          to="/exam"
          className="rounded-xl bg-t48-blue px-5 py-2.5 font-bold text-white transition-transform hover:scale-[1.02] active:scale-95"
        >
          Otro simulacro
        </Link>
      </div>
    </div>
  );
}
