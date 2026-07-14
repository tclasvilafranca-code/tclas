import { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import type { SubmitResult } from "../lib/api";
import { badgeIcon } from "../lib/badgeIcons";
import { Flame, Share, Star } from "../components/Icons";
import { ScoreRing } from "../components/ScoreRing";
import { renderShareCard } from "../lib/shareCard";

export function Results() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = (location.state as { result?: SubmitResult } | null)?.result;
  const [sharing, setSharing] = useState(false);
  const [shareError, setShareError] = useState<string | null>(null);

  if (!result) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <p className="text-slate-500">No hay resultados que mostrar.</p>
        <button onClick={() => navigate("/dashboard")} className="btn-primary mt-4 px-4 py-2.5">
          Volver al panel
        </button>
      </div>
    );
  }

  const fails = result.total - result.score;
  const pct = Math.round((result.score / result.total) * 100);
  const g = result.gamification;
  const isLearnMode = result.attempt?.mode === "learn";

  async function handleShare() {
    if (!result) return;
    setShareError(null);
    setSharing(true);
    try {
      const blob = await renderShareCard({
        percent: pct,
        score: result.score,
        total: result.total,
        passed: result.passed,
        isLearnMode,
        level: g?.level ?? 1,
        streak: g?.currentStreak ?? 0,
        xpGained: g?.xpGained ?? 0,
      });
      const file = new File([blob], "teorico48-resultado.png", { type: "image/png" });
      const shareData = { files: [file], title: "Teórico48", text: "Mi resultado en Teórico48" };
      if (navigator.canShare?.(shareData)) {
        await navigator.share(shareData);
      } else {
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "teorico48-resultado.png";
        a.click();
        URL.revokeObjectURL(url);
      }
    } catch (err) {
      if (err instanceof Error && err.name !== "AbortError") {
        setShareError("No se pudo generar la imagen para compartir. Inténtalo de nuevo.");
      }
    } finally {
      setSharing(false);
    }
  }

  return (
    <div className="mx-auto max-w-2xl px-4 py-10">
      <div
        className={`animate-[fadeIn_0.25s_ease-out] rounded-3xl border p-8 text-center ${
          isLearnMode ? "border-t48-blue/30 bg-t48-blue/5" : result.passed ? "border-t48-green/30 bg-t48-green/10" : "border-t48-red/30 bg-t48-red/10"
        }`}
      >
        <div className="flex justify-center">
          <ScoreRing percent={pct} passed={isLearnMode ? true : result.passed} />
        </div>
        <p
          className={`mt-3 animate-[fadeIn_0.4s_ease-out_0.2s_both] text-2xl font-extrabold ${
            isLearnMode ? "text-t48-blue-dark" : result.passed ? "text-t48-green-dark" : "text-t48-red"
          }`}
        >
          {isLearnMode ? "Sesión de aprendizaje completada" : result.passed ? "¡Aprobado!" : "Suspenso, pero cerca"}
        </p>
        <p className="mt-1 animate-[fadeIn_0.4s_ease-out_0.25s_both] text-slate-500">
          {result.score}/{result.total} correctas · {fails} fallo{fails !== 1 ? "s" : ""}
          {isLearnMode ? "" : " (máx. 3 para aprobar)"}
        </p>
        {isLearnMode && (
          <p className="mt-1 animate-[fadeIn_0.4s_ease-out_0.3s_both] text-xs text-slate-400">
            Esto no cuenta como simulacro real — para eso está el examen cronometrado.
          </p>
        )}

        {g && (
          <div className="mt-5 flex flex-wrap items-center justify-center gap-2 anim-stagger">
            <span className="rounded-md border border-slate-200 bg-white px-3 py-1 text-sm font-semibold text-t48-ink shadow-sm">
              +{g.xpGained} XP
            </span>
            {g.leveledUp && (
              <span className="flex items-center gap-1.5 rounded-md border border-slate-200 bg-white px-3 py-1 text-sm font-semibold text-t48-ink shadow-sm">
                <Star className="h-3.5 w-3.5 text-amber-500" /> Nivel {g.level}
              </span>
            )}
            {g.currentStreak > 1 && (
              <span className="flex items-center gap-1.5 rounded-md border border-slate-200 bg-white px-3 py-1 text-sm font-semibold text-t48-ink shadow-sm">
                <Flame className="h-3.5 w-3.5 text-slate-400" /> Racha de {g.currentStreak}
              </span>
            )}
          </div>
        )}

        {g && g.newBadges.length > 0 && (
          <div className="mt-4 flex flex-wrap justify-center gap-2 anim-stagger">
            {g.newBadges.map((b) => (
              <span
                key={b.id}
                className="flex items-center gap-1.5 rounded-md border border-slate-200 bg-white px-3 py-1.5 text-sm font-semibold text-t48-ink shadow-sm"
              >
                <span className="text-t48-blue">{badgeIcon(b.id)}</span> Nueva medalla: {b.label}
              </span>
            ))}
          </div>
        )}

        <button onClick={handleShare} disabled={sharing} className="btn-secondary mt-5 px-4 py-2 text-sm">
          <Share className="h-4 w-4" />
          {sharing ? "Generando..." : "Compartir resultado"}
        </button>
        {shareError && <p className="mt-2 text-xs font-medium text-t48-red">{shareError}</p>}
      </div>

      <div className="mt-8 space-y-3">
        {result.results.map((r, i) => (
          <div
            key={r.questionId}
            style={{ animationDelay: `${Math.min(i, 10) * 30}ms` }}
            className={`animate-[fadeIn_0.35s_ease-out_both] rounded-2xl border p-4 ${r.correct ? "border-slate-200" : "border-t48-red/30 bg-t48-red/5"}`}
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
        <Link to="/dashboard" className="btn-secondary px-5 py-2.5">
          Volver al panel
        </Link>
        <Link to="/exam" className="btn-primary px-5 py-2.5">
          {isLearnMode ? "Hacer el simulacro real" : "Otro simulacro"}
        </Link>
      </div>
    </div>
  );
}
