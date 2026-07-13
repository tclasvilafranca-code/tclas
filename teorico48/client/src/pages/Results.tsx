import { Link, useLocation, useNavigate } from "react-router-dom";
import type { SubmitResult } from "../lib/api";

export function Results() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = (location.state as { result?: SubmitResult } | null)?.result;

  if (!result) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <p className="text-slate-500">No hay resultados que mostrar.</p>
        <button onClick={() => navigate("/dashboard")} className="mt-4 rounded-lg bg-t48-blue px-4 py-2 font-semibold text-white">
          Volver al panel
        </button>
      </div>
    );
  }

  const fails = result.total - result.score;

  return (
    <div className="mx-auto max-w-2xl px-4 py-10">
      <div
        className={`rounded-xl border p-6 text-center ${
          result.passed ? "border-t48-green/40 bg-t48-green/10" : "border-t48-red/40 bg-t48-red/10"
        }`}
      >
        <p className="text-sm font-semibold uppercase tracking-wide text-slate-500">Resultado</p>
        <p className={`mt-1 text-4xl font-extrabold ${result.passed ? "text-t48-green" : "text-t48-red"}`}>
          {result.passed ? "¡Aprobado!" : "Suspenso"}
        </p>
        <p className="mt-2 text-slate-600">
          {result.score}/{result.total} correctas · {fails} fallo{fails !== 1 ? "s" : ""}
          {" "}(máx. 3 permitidos)
        </p>
      </div>

      <div className="mt-8 space-y-3">
        {result.results.map((r) => (
          <div
            key={r.questionId}
            className={`rounded-lg border p-4 ${r.correct ? "border-slate-200" : "border-t48-red/40 bg-t48-red/5"}`}
          >
            <p className="text-xs font-semibold uppercase tracking-wide text-t48-blue">{r.category}</p>
            <p className="mt-1 font-medium text-t48-ink">{r.text}</p>
            <p className="mt-2 text-sm">
              Tu respuesta:{" "}
              <span className={r.correct ? "text-t48-green" : "text-t48-red"}>
                {r.selectedIndex !== null ? r.options[r.selectedIndex] : "(sin responder)"}
              </span>
            </p>
            {!r.correct && (
              <p className="text-sm text-t48-green">Correcta: {r.options[r.correctIndex]}</p>
            )}
            <p className="mt-2 text-sm text-slate-600">{r.explanation}</p>
          </div>
        ))}
      </div>

      <div className="mt-8 flex justify-center gap-3">
        <Link to="/dashboard" className="rounded-lg border border-slate-300 px-5 py-2.5 font-semibold text-slate-700">
          Volver al panel
        </Link>
        <Link to="/exam" className="rounded-lg bg-t48-blue px-5 py-2.5 font-semibold text-white">
          Otro simulacro
        </Link>
      </div>
    </div>
  );
}
