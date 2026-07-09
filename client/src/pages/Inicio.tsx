import { useEffect, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../lib/api";
import type { CurriculumTree, LessonNode, ReviewDue, ProfileStats } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import { MascotBubble } from "../components/MascotBubble";
import { StreakCalendar } from "../components/StreakCalendar";
import { ReviewBanner } from "../components/ReviewBanner";
import { NotificationsToggle } from "../components/NotificationsToggle";
import { DailyGoalRing } from "../components/DailyGoalRing";
import { greetingMessage } from "../lib/misol";

interface NextLesson {
  lesson: LessonNode;
  pieceTitle: string;
  iconEmoji: string;
}

function findNextLesson(tree: CurriculumTree): NextLesson | null {
  for (const entry of tree.pieces) {
    const lesson = entry.lessons.find((l) => l.status === "AVAILABLE");
    if (lesson) return { lesson, pieceTitle: entry.piece.title, iconEmoji: entry.piece.iconEmoji };
  }
  return null;
}

export function Inicio() {
  const { me, refresh } = useAuth();
  const [tree, setTree] = useState<CurriculumTree | null>(null);
  const [reviewsDue, setReviewsDue] = useState<ReviewDue[]>([]);
  const [stats, setStats] = useState<ProfileStats | null>(null);
  const navigate = useNavigate();
  const [greeting] = useState(() => greetingMessage(me?.name ?? "", me?.studentProfile?.streakCurrent ?? 0));

  useEffect(() => {
    api.get<CurriculumTree>("/curriculum").then(setTree);
    api.get<{ due: ReviewDue[] }>("/reviews/due").then((r) => setReviewsDue(r.due));
    api.get<ProfileStats>("/me/profile-stats").then(setStats);
  }, []);

  const next = useMemo(() => (tree ? findNextLesson(tree) : null), [tree]);
  const minutesToday = stats?.last7Days[stats.last7Days.length - 1]?.minutes ?? 0;

  if (!me?.studentProfile) return null;

  return (
    <main className="px-4 py-8">
      <MascotBubble message={greeting} mood="cheer" align="center" className="mb-2 text-left" />
      <StreakCalendar streakCurrent={me.studentProfile.streakCurrent} lastActivityDate={me.studentProfile.lastActivityDate} />

      <div className="max-w-md mx-auto grid grid-cols-2 gap-3 mt-5 mb-6">
        <DailyGoalRing
          minutesToday={minutesToday}
          goalMinutes={me.studentProfile.dailyGoalMinutes}
          onGoalChange={() => refresh()}
        />
        <div className="bg-white/70 border border-tclas-ink/10 rounded-xl px-4 py-3 flex flex-col items-center justify-center text-center">
          <p className="text-2xl font-display text-tclas-gold-shadow">{me.studentProfile.streakCurrent}🔥</p>
          <p className="text-[11px] uppercase tracking-wide text-tclas-ink/40">días de racha</p>
        </div>
      </div>

      <div className="max-w-md mx-auto flex justify-center mb-6">
        <NotificationsToggle />
      </div>

      <ReviewBanner due={reviewsDue} onOpenLesson={(id) => navigate(`/app/lesson/${id}`)} />

      {!tree && <p className="text-center mt-10 text-tclas-ink/50">Cargando tu camino musical...</p>}

      {tree && next && (
        <button
          onClick={() => navigate(`/app/lesson/${next.lesson.id}`)}
          className="btn-push w-full max-w-md mx-auto flex items-center gap-4 bg-tclas-plum border-2 border-b-4 border-tclas-plum-light border-b-tclas-plum-shadow rounded-2xl px-5 py-4 text-left"
        >
          <span className="text-4xl shrink-0">{next.iconEmoji}</span>
          <span className="flex-1 min-w-0 text-tclas-cream">
            <span className="block text-[11px] uppercase tracking-wide text-tclas-cream/60">Continuar lección</span>
            <span className="block font-display text-lg leading-tight truncate">{next.pieceTitle}</span>
            <span className="block text-xs text-tclas-cream/70">Semana {next.lesson.weekNumber} · {next.lesson.title}</span>
          </span>
          <span className="text-tclas-cream text-2xl shrink-0">▶</span>
        </button>
      )}

      {tree && !next && tree.pieces.length > 0 && (
        <p className="text-center text-sm text-tclas-ink/50 max-w-md mx-auto mt-4">
          Has completado todo lo que tienes disponible por ahora. ¡Vuelve mañana o repasa alguna pieza en Practicar!
        </p>
      )}

      {tree && tree.pieces.length === 0 && (
        <p className="text-center text-tclas-ink/50 mt-16">Todavía no tienes piezas asignadas. ¡Pronto tu profesor/a añadirá tu repertorio!</p>
      )}
    </main>
  );
}
