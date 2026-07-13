import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api, ApiError } from "../lib/api";
import type { Question, SubmitResult } from "../lib/api";
import { CheckCircle } from "../components/Icons";

export function TestRunner({ mode }: { mode: "exam" | "review" }) {
  const navigate = useNavigate();
  const [attemptId, setAttemptId] = useState<string | null>(null);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<Record<string, number | null>>({});
  const [current, setCurrent] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [noFailsYet, setNoFailsYet] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const start = mode === "exam" ? api.startExam() : api.startReview();
    start
      .then((r) => {
        setAttemptId(r.attemptId);
        setQuestions(r.questions);
      })
      .catch((err) => {
        if (err instanceof ApiError && err.status === 404) {
          setNoFailsYet(true);
        } else {
          setError(err instanceof ApiError ? err.message : "No se pudo iniciar el test");
        }
      })
      .finally(() => setLoading(false));
  }, [mode]);

  function select(questionId: string, index: number) {
    setAnswers((prev) => ({ ...prev, [questionId]: index }));
  }

  async function handleSubmit() {
    if (!attemptId) return;
    setSubmitting(true);
    try {
      const payload = questions.map((q) => ({ questionId: q.id, selectedIndex: answers[q.id] ?? null }));
      const result: SubmitResult = await api.submitAttempt(attemptId, payload);
      navigate("/results", { state: { result } });
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "No se pudo enviar el test");
    } finally {
      setSubmitting(false);
    }
  }

  if (loading) return <div className="p-16 text-center text-slate-500">Preparando tu test...</div>;

  if (noFailsYet) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-t48-green/10 text-t48-green-dark">
          <CheckCircle className="h-6 w-6" />
        </div>
        <p className="mt-4 font-bold text-t48-ink">Todavía no has fallado ninguna pregunta</p>
        <p className="mt-1 text-sm text-slate-500">Haz un simulacro y, si fallas algo, aparecerá aquí para repasarlo.</p>
        <button
          onClick={() => navigate("/dashboard")}
          className="mt-5 rounded-md bg-t48-blue px-4 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark"
        >
          Volver al panel
        </button>
      </div>
    );
  }

  if (error) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <p className="font-medium text-t48-red">{error}</p>
        <button
          onClick={() => navigate("/dashboard")}
          className="mt-4 rounded-md bg-t48-blue px-4 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark"
        >
          Volver al panel
        </button>
      </div>
    );
  }

  const q = questions[current];
  const answeredCount = Object.keys(answers).length;

  return (
    <div className="mx-auto max-w-2xl px-4 py-8">
      <div className="mb-3 flex items-center justify-between text-sm font-semibold text-slate-500">
        <span>{current + 1} / {questions.length}</span>
        <span>{answeredCount}/{questions.length} respondidas</span>
      </div>
      <div className="h-2 w-full rounded-full bg-slate-100">
        <div
          className="h-2 rounded-full bg-t48-blue transition-all duration-300"
          style={{ width: `${((current + 1) / questions.length) * 100}%` }}
        />
      </div>

      {q && (
        <div
          key={q.id}
          role="group"
          aria-label={`Pregunta ${current + 1} de ${questions.length}`}
          className="mt-6 animate-[fadeIn_0.15s_ease-out] rounded-2xl border border-slate-200 bg-white p-6"
        >
          <p className="mb-1.5 text-xs font-bold uppercase tracking-wide text-t48-blue">{q.category}</p>
          <p className="text-lg font-bold leading-snug text-t48-ink">{q.text}</p>
          <div className="mt-5 flex flex-col gap-2">
            {q.options.map((opt, i) => (
              <button
                key={i}
                onClick={() => select(q.id, i)}
                aria-pressed={answers[q.id] === i}
                className={`rounded-xl border px-4 py-3 text-left transition-all duration-150 focus-visible:ring-2 focus-visible:ring-t48-blue/40 focus-visible:outline-none ${
                  answers[q.id] === i
                    ? "border-t48-blue bg-t48-blue/10 font-semibold text-t48-blue-dark"
                    : "border-slate-200 hover:border-t48-blue/50 hover:bg-slate-50"
                }`}
              >
                {opt}
              </button>
            ))}
          </div>
        </div>
      )}

      <div className="mt-6 flex items-center justify-between">
        <button
          onClick={() => setCurrent((c) => Math.max(0, c - 1))}
          disabled={current === 0}
          className="rounded-md border border-slate-200 px-4 py-2.5 font-semibold text-slate-600 transition-colors hover:bg-slate-50 disabled:opacity-30"
        >
          Anterior
        </button>
        {current < questions.length - 1 ? (
          <button
            onClick={() => setCurrent((c) => Math.min(questions.length - 1, c + 1))}
            className="rounded-md bg-t48-blue px-5 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark"
          >
            Siguiente
          </button>
        ) : (
          <button
            onClick={handleSubmit}
            disabled={submitting}
            className="rounded-md bg-t48-green px-5 py-2.5 font-semibold text-white transition-colors hover:bg-t48-green-dark disabled:opacity-50"
          >
            {submitting ? "Corrigiendo..." : "Terminar y corregir"}
          </button>
        )}
      </div>
    </div>
  );
}
