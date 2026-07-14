import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { api, ApiError } from "../lib/api";
import type { LearnQuestion, Question, SubmitResult } from "../lib/api";
import { CheckCircle, XCircle } from "../components/Icons";

type Mode = "exam" | "review" | "learn";

export function TestRunner({ mode }: { mode: Mode }) {
  const navigate = useNavigate();
  const location = useLocation();
  const categorySlug = (location.state as { categorySlug?: string; categoryName?: string } | null)?.categorySlug;
  const categoryName = (location.state as { categorySlug?: string; categoryName?: string } | null)?.categoryName;
  const [attemptId, setAttemptId] = useState<string | null>(null);
  const [questions, setQuestions] = useState<Question[] | LearnQuestion[]>([]);
  const [answers, setAnswers] = useState<Record<string, number | null>>({});
  const [revealed, setRevealed] = useState<Record<string, boolean>>({});
  const [current, setCurrent] = useState(0);
  const [direction, setDirection] = useState<"next" | "prev">("next");
  const [error, setError] = useState<string | null>(null);
  const [noFailsYet, setNoFailsYet] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [loading, setLoading] = useState(true);

  const isLearn = mode === "learn";

  useEffect(() => {
    const start = mode === "exam" ? api.startExam() : mode === "review" ? api.startReview() : api.startLearn(categorySlug);
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
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [mode]);

  function select(questionId: string, index: number) {
    if (isLearn && revealed[questionId]) return;
    setAnswers((prev) => ({ ...prev, [questionId]: index }));
    if (isLearn) {
      setRevealed((prev) => ({ ...prev, [questionId]: true }));
    }
  }

  function goTo(index: number, dir: "next" | "prev") {
    setDirection(dir);
    setCurrent(index);
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

  if (loading) {
    return (
      <div className="mx-auto max-w-2xl px-4 py-8">
        <div className="h-2 w-full animate-pulse rounded-full bg-slate-100" />
        <div className="mt-6 animate-pulse rounded-2xl border border-slate-200 bg-white p-6">
          <div className="h-3 w-24 rounded bg-slate-100" />
          <div className="mt-3 h-5 w-3/4 rounded bg-slate-100" />
          <div className="mt-5 flex flex-col gap-2">
            <div className="h-11 rounded-xl bg-slate-100" />
            <div className="h-11 rounded-xl bg-slate-100" />
            <div className="h-11 rounded-xl bg-slate-100" />
            <div className="h-11 rounded-xl bg-slate-100" />
          </div>
        </div>
      </div>
    );
  }

  if (noFailsYet) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-t48-green/10 text-t48-green-dark">
          <CheckCircle className="h-6 w-6" />
        </div>
        <p className="mt-4 font-bold text-t48-ink">Todavía no has fallado ninguna pregunta</p>
        <p className="mt-1 text-sm text-slate-500">Haz un simulacro y, si fallas algo, aparecerá aquí para repasarlo.</p>
        <button onClick={() => navigate("/dashboard")} className="btn-primary mt-5 px-4 py-2.5">
          Volver al panel
        </button>
      </div>
    );
  }

  if (error) {
    return (
      <div className="mx-auto max-w-md px-4 py-16 text-center">
        <p className="font-medium text-t48-red">{error}</p>
        <button onClick={() => navigate("/dashboard")} className="btn-primary mt-4 px-4 py-2.5">
          Volver al panel
        </button>
      </div>
    );
  }

  const q = questions[current];
  const answeredCount = Object.keys(answers).length;
  const questionRevealed = isLearn && !!q && revealed[q.id];
  const learnQuestion = isLearn ? (q as LearnQuestion) : null;
  const canAdvance = !isLearn || questionRevealed;

  return (
    <div className="mx-auto max-w-2xl px-4 py-8">
      <div className="mb-3 flex items-center justify-between text-sm font-semibold text-slate-500">
        <span className="tabular-nums">{current + 1} / {questions.length}</span>
        {isLearn ? (
          <span className="flex items-center gap-1.5 rounded-md bg-t48-blue/10 px-2 py-0.5 text-xs font-bold uppercase tracking-wide text-t48-blue">
            Modo Aprendizaje{categoryName ? ` · ${categoryName}` : ""}
          </span>
        ) : (
          <span className="tabular-nums">{answeredCount}/{questions.length} respondidas</span>
        )}
      </div>
      <div className="progress-track h-2 w-full rounded-full">
        <div
          className="progress-fill h-2 rounded-full"
          style={{ width: `${((current + 1) / questions.length) * 100}%` }}
        />
      </div>

      {q && (
        <div
          key={q.id}
          role="group"
          aria-label={`Pregunta ${current + 1} de ${questions.length}`}
          className={`mt-6 rounded-2xl border border-slate-200 bg-white p-6 ${direction === "next" ? "anim-slide-right" : "anim-slide-left"}`}
        >
          <p className="mb-1.5 text-xs font-bold uppercase tracking-wide text-t48-blue">{q.category}</p>
          <p className="text-lg font-bold leading-snug text-t48-ink">{q.text}</p>
          <div className="mt-5 flex flex-col gap-2">
            {q.options.map((opt, i) => {
              const selected = answers[q.id] === i;
              let style = selected
                ? "is-selected border-t48-blue bg-t48-blue/10 font-semibold text-t48-blue-dark shadow-sm"
                : "border-slate-200 hover:border-t48-blue/50 hover:bg-slate-50";
              const isCorrectOption = learnQuestion && i === learnQuestion.correctIndex;
              if (questionRevealed && isCorrectOption) {
                style = "border-t48-green bg-t48-green/10 font-semibold text-t48-green-dark";
              } else if (questionRevealed && selected && !isCorrectOption) {
                style = "border-t48-red bg-t48-red/10 font-semibold text-t48-red";
              }
              return (
                <button
                  key={i}
                  onClick={() => select(q.id, i)}
                  disabled={questionRevealed}
                  aria-pressed={selected}
                  className={`option-btn flex items-center justify-between rounded-xl border px-4 py-3 text-left disabled:cursor-default focus-visible:ring-2 focus-visible:ring-t48-blue/40 focus-visible:outline-none ${style}`}
                >
                  <span>{opt}</span>
                  {questionRevealed && isCorrectOption && <CheckCircle className="option-check h-4 w-4 shrink-0" />}
                  {questionRevealed && selected && !isCorrectOption && <XCircle className="option-check h-4 w-4 shrink-0" />}
                </button>
              );
            })}
          </div>

          {questionRevealed && learnQuestion && (
            <div className="anim-slide-right mt-4 rounded-xl border border-slate-200 bg-slate-50 p-4 text-sm text-slate-600">
              <p className="font-semibold text-t48-ink">
                {answers[q.id] === learnQuestion.correctIndex ? "¡Correcto!" : "No era esa."}
              </p>
              <p className="mt-1">{learnQuestion.explanation}</p>
            </div>
          )}
        </div>
      )}

      <div className="mt-6 flex items-center justify-between">
        <button
          onClick={() => goTo(Math.max(0, current - 1), "prev")}
          disabled={current === 0}
          className="btn-secondary px-4 py-2.5"
        >
          Anterior
        </button>
        {current < questions.length - 1 ? (
          <button
            onClick={() => goTo(Math.min(questions.length - 1, current + 1), "next")}
            disabled={!canAdvance}
            className="btn-primary px-5 py-2.5"
          >
            Siguiente
          </button>
        ) : (
          <button onClick={handleSubmit} disabled={submitting || !canAdvance} className="btn-success px-5 py-2.5">
            {submitting ? "Un momento..." : "Terminar"}
          </button>
        )}
      </div>
    </div>
  );
}
