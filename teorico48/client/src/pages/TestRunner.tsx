import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api, ApiError } from "../lib/api";
import type { Question, SubmitResult } from "../lib/api";

export function TestRunner({ mode }: { mode: "exam" | "review" }) {
  const navigate = useNavigate();
  const [attemptId, setAttemptId] = useState<string | null>(null);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<Record<string, number | null>>({});
  const [current, setCurrent] = useState(0);
  const [error, setError] = useState<string | null>(null);
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
        setError(err instanceof ApiError ? err.message : "No se pudo iniciar el test");
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

  if (loading) return <div className="p-8 text-center text-slate-500">Preparando tu test...</div>;

  if (error) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <p className="text-t48-red">{error}</p>
        <button onClick={() => navigate("/dashboard")} className="mt-4 rounded-lg bg-t48-blue px-4 py-2 font-semibold text-white">
          Volver al panel
        </button>
      </div>
    );
  }

  const q = questions[current];
  const answeredCount = Object.keys(answers).length;

  return (
    <div className="mx-auto max-w-2xl px-4 py-8">
      <div className="mb-4 flex items-center justify-between text-sm text-slate-500">
        <span>Pregunta {current + 1} de {questions.length}</span>
        <span>{answeredCount}/{questions.length} respondidas</span>
      </div>
      <div className="h-2 w-full rounded-full bg-slate-200">
        <div
          className="h-2 rounded-full bg-t48-blue transition-all"
          style={{ width: `${((current + 1) / questions.length) * 100}%` }}
        />
      </div>

      {q && (
        <div className="mt-6 rounded-xl border border-slate-200 bg-white p-6">
          <p className="mb-1 text-xs font-semibold uppercase tracking-wide text-t48-blue">{q.category}</p>
          <p className="text-lg font-medium text-t48-ink">{q.text}</p>
          <div className="mt-4 flex flex-col gap-2">
            {q.options.map((opt, i) => (
              <button
                key={i}
                onClick={() => select(q.id, i)}
                className={`rounded-lg border px-4 py-3 text-left ${
                  answers[q.id] === i
                    ? "border-t48-blue bg-t48-blue/10 font-semibold text-t48-blue-dark"
                    : "border-slate-200 hover:border-t48-blue"
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
          className="rounded-lg border border-slate-300 px-4 py-2 font-medium text-slate-700 disabled:opacity-40"
        >
          Anterior
        </button>
        {current < questions.length - 1 ? (
          <button
            onClick={() => setCurrent((c) => Math.min(questions.length - 1, c + 1))}
            className="rounded-lg bg-t48-blue px-4 py-2 font-semibold text-white"
          >
            Siguiente
          </button>
        ) : (
          <button
            onClick={handleSubmit}
            disabled={submitting}
            className="rounded-lg bg-t48-green px-5 py-2 font-semibold text-white disabled:opacity-50"
          >
            {submitting ? "Enviando..." : "Terminar y corregir"}
          </button>
        )}
      </div>
    </div>
  );
}
