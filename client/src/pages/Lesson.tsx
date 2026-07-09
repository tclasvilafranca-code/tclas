import { useEffect, useRef, useState } from "react";
import { useNavigate, useParams, Link } from "react-router-dom";
import { api, ApiError } from "../lib/api";
import type { LessonDetail, AttemptResult, CompleteLessonResult, ExerciseType } from "../lib/api";
import { ExercisePlayer } from "../exercises/ExercisePlayer";
import { LessonCompleteModal } from "../components/LessonCompleteModal";
import { playSuccessChime, playErrorBuzz } from "../lib/audio";
import { useAuth } from "../context/AuthContext";
import { MascotBubble } from "../components/MascotBubble";
import { correctMessage, wrongMessage } from "../lib/misol";
import { msUntilNextHeart, formatCountdown } from "../lib/hearts";
import { timerSecondsFor, autoAdvanceDelayFor } from "../lib/pacing";
import { PHASE_LABEL } from "../lib/phases";

// Segundos de respuesta para los tipos de pregunta rapida (opcion multiple/escribir).
// Los demas tipos (tocar, ritmo, relacionar, ordenar, tramos...) llevan su propio ritmo.
const TIMED_TYPES: Partial<Record<ExerciseType, number>> = {
  NOTE_NAME: 6,
  THEORY_MCQ: 8,
  EAR_TRAINING: 8,
  INTERVAL: 8,
  CHORD: 8,
  WRITE_ANSWER: 12,
  DRAG_STAFF: 10,
  FILL_BLANK: 10,
};

export function Lesson() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { me, refresh } = useAuth();
  const ageGroup = me?.studentProfile?.ageGroup ?? "TEENS";

  const [lesson, setLesson] = useState<LessonDetail | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [noHearts, setNoHearts] = useState<{ heartsMax: number; heartsUpdatedAt: string } | null>(null);
  const [index, setIndex] = useState(0);
  const [feedback, setFeedback] = useState<AttemptResult | null>(null);
  const [correctCount, setCorrectCount] = useState(0);
  const [result, setResult] = useState<CompleteLessonResult | null>(null);
  const [loadKey, setLoadKey] = useState(0);
  const [misolReaction, setMisolReaction] = useState("");
  const [timeLeft, setTimeLeft] = useState<number | null>(null);
  const [showSkip, setShowSkip] = useState(false);

  const feedbackRef = useRef<AttemptResult | null>(null);
  const advancingRef = useRef(false);
  const sessionStartRef = useRef(Date.now());

  useEffect(() => {
    if (!id) return;
    setLesson(null);
    setLoadError(null);
    setNoHearts(null);
    setIndex(0);
    setFeedback(null);
    setCorrectCount(0);
    setResult(null);
    sessionStartRef.current = Date.now();
    api
      .get<LessonDetail>(`/lessons/${id}`)
      .then(setLesson)
      .catch((err) => {
        if (err instanceof ApiError && err.data?.code === "NO_HEARTS") {
          setNoHearts({ heartsMax: err.data.heartsMax, heartsUpdatedAt: err.data.heartsUpdatedAt });
        } else {
          setLoadError(err.message || "No se pudo cargar la leccion");
        }
      });
  }, [id, loadKey]);

  const exercise = lesson?.exercises[index];

  useEffect(() => {
    feedbackRef.current = feedback;
  }, [feedback]);

  // Cuenta atras para los tipos de pregunta rapida (ajustada al ritmo de la franja de edad).
  useEffect(() => {
    if (!exercise) return;
    const baseLimit = TIMED_TYPES[exercise.type];
    if (!baseLimit || feedbackRef.current) {
      setTimeLeft(null);
      return;
    }
    const limit = timerSecondsFor(ageGroup, baseLimit);
    setTimeLeft(limit);
    const start = performance.now();
    let raf: number;
    function tick() {
      if (feedbackRef.current) return;
      const elapsed = (performance.now() - start) / 1000;
      const remaining = Math.max(0, limit - elapsed);
      setTimeLeft(remaining);
      if (remaining <= 0) {
        handleSubmit("__TIMEOUT__");
        return;
      }
      raf = requestAnimationFrame(tick);
    }
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [exercise?.id]);

  useEffect(() => {
    advancingRef.current = false;
  }, [index]);

  // Auto-avanza tras responder: rapido si acierta, con mas tiempo para leer si falla
  // (ajustado al ritmo de la franja de edad del alumno).
  useEffect(() => {
    if (!feedback) return;
    const delay = autoAdvanceDelayFor(ageGroup, feedback.correct);
    const t = setTimeout(() => {
      handleNext();
    }, delay);
    return () => clearTimeout(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [feedback]);

  // Red de seguridad: los ejercicios de "toca la secuencia correcta" no tienen
  // cuenta atras ni boton de enviar manual, asi que si algo falla (una nota
  // que nunca coincide, un cuelgue...) el alumno podria quedarse atascado sin
  // poder avanzar NI retroceder. Pasados unos segundos se ofrece la opcion de
  // saltar el ejercicio, para que nunca sea un callejon sin salida.
  useEffect(() => {
    setShowSkip(false);
    if (!exercise || TIMED_TYPES[exercise.type]) return;
    const t = setTimeout(() => setShowSkip(true), 8000);
    return () => clearTimeout(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [exercise?.id]);

  if (loadError) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center px-4 text-center gap-4">
        <p className="text-tclas-ink/70 max-w-sm">{loadError}</p>
        <Link to="/app" className="bg-tclas-plum text-tclas-cream rounded-full px-6 py-2 font-semibold hover:bg-tclas-plum-light">
          Volver a tu camino
        </Link>
      </div>
    );
  }

  if (noHearts) {
    return (
      <div className="min-h-screen flex flex-col items-center justify-center px-4 text-center gap-5">
        <MascotBubble
          message="¡Ups! Te has quedado sin corazones. Descansa un poco, se van recargando solos con el tiempo."
          mood="encourage"
          size={72}
        />
        <div className="flex gap-1 text-3xl">
          {Array.from({ length: noHearts.heartsMax }).map((_, i) => (
            <span key={i} className="text-tclas-ink/15">
              ♥
            </span>
          ))}
        </div>
        <p className="text-sm text-tclas-ink/60">
          Proximo corazon en <strong className="text-tclas-ink">{formatCountdown(msUntilNextHeart(noHearts.heartsUpdatedAt))}</strong>
        </p>
        <p className="text-xs text-tclas-ink/40 max-w-xs">
          Mientras tanto puedes repasar cualquier pieza que ya hayas completado, eso no gasta corazones.
        </p>
        <Link to="/app" className="bg-tclas-plum text-tclas-cream rounded-full px-6 py-2 font-semibold hover:bg-tclas-plum-light">
          Volver a tu camino
        </Link>
      </div>
    );
  }

  if (!lesson || !exercise) return <p className="text-center mt-16 text-tclas-ink/50">Cargando leccion...</p>;

  const progressPct = Math.round((index / lesson.exercises.length) * 100);
  const phase = PHASE_LABEL[exercise.phase] ?? PHASE_LABEL.SHEET_PRACTICE;
  const baseTimeLimit = TIMED_TYPES[exercise.type];
  const timeLimit = baseTimeLimit ? timerSecondsFor(ageGroup, baseTimeLimit) : undefined;

  async function handleSubmit(answer: unknown) {
    const res = await api.post<AttemptResult>(`/exercises/${exercise!.id}/attempt`, { answer });
    setFeedback(res);
    if (res.correct) {
      playSuccessChime();
      setCorrectCount((c) => c + 1);
      setMisolReaction(correctMessage());
    } else {
      playErrorBuzz();
      setMisolReaction(wrongMessage());
    }
  }

  async function handleNext() {
    if (advancingRef.current) return;
    advancingRef.current = true;
    if (index + 1 < lesson!.exercises.length) {
      setIndex((i) => i + 1);
      setFeedback(null);
    } else {
      const finalCorrect = correctCount;
      const practiceSeconds = Math.round((Date.now() - sessionStartRef.current) / 1000);
      const res = await api.post<CompleteLessonResult>(`/lessons/${lesson!.id}/complete`, {
        correctCount: finalCorrect,
        totalCount: lesson!.exercises.length,
        practiceSeconds,
      });
      setResult(res);
      await refresh();
    }
  }

  const timerPct = timeLimit && timeLeft !== null ? Math.max(0, timeLeft / timeLimit) : null;
  const timerColor = timerPct === null ? "" : timerPct > 0.5 ? "bg-tclas-sage" : timerPct > 0.2 ? "bg-tclas-gold" : "bg-tclas-rose";

  return (
    <div className="min-h-screen flex flex-col">
      <header className="px-4 py-4 flex items-center gap-4 border-b border-tclas-ink/10">
        <Link to="/app" className="text-tclas-ink/50 hover:text-tclas-ink text-xl">
          ✕
        </Link>
        <div className="flex-1 h-3 bg-tclas-ink/10 rounded-full overflow-hidden">
          <div className="h-full bg-tclas-gold transition-all" style={{ width: `${progressPct}%` }} />
        </div>
        <span className="text-xs text-tclas-ink/50 whitespace-nowrap">
          {index + 1}/{lesson.exercises.length}
        </span>
      </header>

      <main className="flex-1 flex items-center justify-center px-4 py-10">
        <div className="w-full max-w-xl">
          <div className="text-center mb-6">
            <p className="text-xs uppercase tracking-wide text-tclas-ink/40 mb-2">
              {lesson.pieceTitle} · Semana {lesson.weekNumber}
            </p>
            <span className={`inline-block text-xs font-semibold rounded-full px-3 py-1 ${phase.className}`}>{phase.label}</span>
            {timerPct !== null && !feedback && (
              <div className="max-w-[10rem] mx-auto mt-3">
                <div className="h-1.5 bg-tclas-ink/10 rounded-full overflow-hidden">
                  <div className={`h-full ${timerColor}`} style={{ width: `${timerPct * 100}%`, transition: "width 120ms linear" }} />
                </div>
              </div>
            )}
          </div>
          <ExercisePlayer exercise={exercise} onSubmit={handleSubmit} feedback={feedback} />
          {showSkip && !feedback && (
            <p className="text-center mt-6">
              <button onClick={() => handleSubmit("__SKIP__")} className="text-xs text-tclas-ink/40 hover:text-tclas-ink/70 underline underline-offset-2">
                ¿Te cuesta este ejercicio? Saltarlo
              </button>
            </p>
          )}
        </div>
      </main>

      {feedback && (
        <div className={`px-4 py-4 border-t ${feedback.correct ? "bg-tclas-sage/10 border-tclas-sage/30" : "bg-tclas-rose/10 border-tclas-rose/30"}`}>
          <div className="max-w-xl mx-auto flex items-center justify-between gap-4">
            <MascotBubble message={misolReaction} mood={feedback.correct ? "cheer" : "encourage"} size={44} />
            <button
              onClick={handleNext}
              className={`btn-push rounded-2xl px-6 py-2.5 font-bold uppercase tracking-wide text-sm shrink-0
                ${feedback.correct ? "bg-tclas-sage border-tclas-sage-shadow text-white hover:bg-tclas-sage/90" : "bg-tclas-plum border-tclas-plum-shadow text-tclas-cream hover:bg-tclas-plum-light"}`}
            >
              Continuar
            </button>
          </div>
          {!feedback.correct && feedback.correctAnswer !== undefined && (
            <p className="max-w-xl mx-auto mt-2 text-xs text-tclas-ink/60">
              Respuesta correcta:{" "}
              <strong className="text-tclas-ink">{Array.isArray(feedback.correctAnswer) ? feedback.correctAnswer.join(", ") : String(feedback.correctAnswer)}</strong>
            </p>
          )}
        </div>
      )}

      {result && (
        <LessonCompleteModal
          stars={result.stars}
          score={result.score}
          xpAwarded={result.xpAwarded}
          passed={result.stars >= 1}
          pieceTitle={lesson.pieceTitle}
          newBadges={result.newBadges}
          isReview={result.isReview}
          onContinue={() => navigate("/app")}
          onRetry={() => setLoadKey((k) => k + 1)}
        />
      )}
    </div>
  );
}
