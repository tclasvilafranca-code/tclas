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
import { WeeklyChallenges } from "../components/WeeklyChallenges";
import { UpcomingAgenda } from "../components/UpcomingAgenda";
import { Skeleton } from "../components/Skeleton";
import { IconFlame, IconPlay } from "../components/icons";
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
          <p className="flex items-center gap-1.5 text-2xl font-display text-tclas-gold-shadow">
            {me.studentProfile.streakCurrent} <IconFlame className="w-5 h-5" />
          </p>
          <p className="text-2xs uppercase tracking-wide text-tclas-ink/40">días de racha</p>
        </div>
      </div>

      <div className="max-w-md mx-auto flex justify-center mb-6">
        <NotificationsToggle />
      </div>

      <ReviewBanner due={reviewsDue} onOpenLesson={(id) => navigate(`/app/lesson/${id}`)} />

      {!tree && (
        <div className="w-full max-w-md mx-auto flex items-center gap-4 rounded-2xl px-5 py-4 bg-white/70 border border-tclas-ink/10">
          <Skeleton className="w-11 h-11 rounded-full shrink-0" />
          <div className="flex-1 min-w-0 flex flex-col gap-2">
            <Skeleton className="h-2.5 w-24" />
            <Skeleton className="h-4 w-40" />
            <Skeleton className="h-2.5 w-32" />
          </div>
        </div>
      )}

      {tree && next && (
        <button
          onClick={() => navigate(`/app/lesson/${next.lesson.id}`)}
          className="btn-push w-full max-w-md mx-auto flex items-center gap-4 bg-tclas-plum border-2 border-b-4 border-tclas-plum-light border-b-tclas-plum-shadow rounded-2xl px-5 py-4 text-left"
        >
          <span className="text-4xl shrink-0">{next.iconEmoji}</span>
          <span className="flex-1 min-w-0 text-tclas-cream">
            <span className="block text-2xs uppercase tracking-wide text-tclas-cream/60">Continuar lección</span>
            <span className="block font-display text-lg leading-tight truncate">{next.pieceTitle}</span>
            <span className="block text-xs text-tclas-cream/70">Semana {next.lesson.weekNumber} · {next.lesson.title}</span>
          </span>
          <IconPlay className="text-tclas-cream w-6 h-6 shrink-0" />
        </button>
      )}

      {tree && <WeeklyChallenges />}

      {tree && <UpcomingAgenda tree={tree} nextClassAt={me.studentProfile.nextClassAt} />}

      {tree && !next && tree.pieces.length > 0 && (
        <p className="text-center text-sm text-tclas-ink/50 max-w-md mx-auto mt-4">
          Has completado todo lo que tienes disponible por ahora. ¡Vuelve mañana o repasa alguna pieza en Practicar!
        </p>
      )}

      {tree && tree.pieces.length === 0 && (
        <div className="max-w-sm mx-auto mt-10">
          <MascotBubble
            message="Todavía no tienes piezas asignadas. En cuanto tu profesor/a añada tu repertorio, aparecerá aquí."
            mood="encourage"
            align="center"
            className="justify-center text-left"
          />
        </div>
      )}
    </main>
  );
}
