import { useEffect, useState } from "react";
import { useNavigate, useParams, Link } from "react-router-dom";
import { api } from "../lib/api";
import type { LessonDetail, AttemptResult, CompleteLessonResult } from "../lib/api";
import { ExercisePlayer } from "../exercises/ExercisePlayer";
import { LessonCompleteModal } from "../components/LessonCompleteModal";
import { playSuccessChime, playErrorBuzz } from "../lib/audio";
import { useAuth } from "../context/AuthContext";

export function Lesson() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { refresh } = useAuth();

  const [lesson, setLesson] = useState<LessonDetail | null>(null);
  const [index, setIndex] = useState(0);
  const [feedback, setFeedback] = useState<AttemptResult | null>(null);
  const [correctCount, setCorrectCount] = useState(0);
  const [result, setResult] = useState<CompleteLessonResult | null>(null);
  const [loadKey, setLoadKey] = useState(0);

  useEffect(() => {
    if (!id) return;
    setLesson(null);
    setIndex(0);
    setFeedback(null);
    setCorrectCount(0);
    setResult(null);
    api.get<LessonDetail>(`/lessons/${id}`).then(setLesson);
  }, [id, loadKey]);

  if (!lesson) return <p className="text-center mt-16 text-tclas-ink/50">Cargando leccion...</p>;

  const exercise = lesson.exercises[index];
  const progressPct = Math.round((index / lesson.exercises.length) * 100);

  async function handleSubmit(answer: unknown) {
    const res = await api.post<AttemptResult>(`/exercises/${exercise.id}/attempt`, { answer });
    setFeedback(res);
    if (res.correct) {
      playSuccessChime();
      setCorrectCount((c) => c + 1);
    } else {
      playErrorBuzz();
    }
  }

  async function handleNext() {
    if (index + 1 < lesson!.exercises.length) {
      setIndex((i) => i + 1);
      setFeedback(null);
    } else {
      const finalCorrect = correctCount;
      const res = await api.post<CompleteLessonResult>(`/lessons/${lesson!.id}/complete`, {
        correctCount: finalCorrect,
        totalCount: lesson!.exercises.length,
      });
      setResult(res);
      await refresh();
    }
  }

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
          <p className="text-xs uppercase tracking-wide text-tclas-ink/40 text-center mb-6">
            {lesson.levelTitle} · {lesson.unitTitle}
          </p>
          <ExercisePlayer exercise={exercise} onSubmit={handleSubmit} feedback={feedback} />
        </div>
      </main>

      {feedback && (
        <div className={`px-4 py-4 border-t ${feedback.correct ? "bg-tclas-sage/10 border-tclas-sage/30" : "bg-tclas-rose/10 border-tclas-rose/30"}`}>
          <div className="max-w-xl mx-auto flex items-center justify-between gap-4">
            <p className={`font-semibold ${feedback.correct ? "text-tclas-sage" : "text-tclas-rose"}`}>
              {feedback.correct ? "¡Correcto!" : "No es correcto"}
            </p>
            <button onClick={handleNext} className="bg-tclas-plum text-tclas-cream rounded-full px-6 py-2 font-semibold hover:bg-tclas-plum-light">
              Continuar
            </button>
          </div>
        </div>
      )}

      {result && (
        <LessonCompleteModal
          stars={result.stars}
          xpAwarded={result.xpAwarded}
          passed={result.stars >= 1}
          newBadges={result.newBadges}
          onContinue={() => navigate("/app")}
          onRetry={() => setLoadKey((k) => k + 1)}
        />
      )}
    </div>
  );
}
