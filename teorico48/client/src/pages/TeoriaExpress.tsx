import { useEffect, useMemo, useState } from "react";
import type { ReactNode } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api, ApiError } from "../lib/api";
import { THEORY_EXPRESS } from "../content/theoryExpress";
import type { TheoryChapter, TheoryIconKey, TheorySession } from "../content/theoryExpress";
import {
  BookOpen,
  Bolt,
  CheckCircle,
  Child,
  Drop,
  Leaf,
  Lightbulb,
  Lock,
  Medal,
  Overtake,
  Parking,
  Radar,
  Road,
  Scooter,
  ShieldCheck,
  Sign,
  Star,
  Target,
  Users,
  Wrench,
  XCircle,
} from "../components/Icons";

const ICONS: Record<TheoryIconKey, (props: { className?: string }) => ReactNode> = {
  BookOpen,
  Target,
  Sign,
  Bolt,
  Overtake,
  Parking,
  Lightbulb,
  Drop,
  Medal,
  Wrench,
  Radar,
  Child,
  Users,
  Leaf,
  Road,
  Scooter,
  ShieldCheck,
};

type Step =
  | { kind: "card"; chapter: TheoryChapter; cardIndex: number }
  | { kind: "check"; chapter: TheoryChapter };

function buildSteps(session: TheorySession): Step[] {
  const steps: Step[] = [];
  for (const chapter of session.chapters) {
    chapter.cards.forEach((_, cardIndex) => steps.push({ kind: "card", chapter, cardIndex }));
    steps.push({ kind: "check", chapter });
  }
  return steps;
}

function storageKey(sessionId: string) {
  return `teorico48:teoria:${sessionId}:step`;
}

export function TeoriaExpress() {
  const navigate = useNavigate();
  const { user, refreshUser } = useAuth();
  const [activeSessionId, setActiveSessionId] = useState<string | null>(null);
  const [completion, setCompletion] = useState<{ xpGained: number; newBadges: { id: string; label: string; emoji: string }[] } | null>(null);

  const completedSessions = new Set(user?.theoryCompletedSessions ?? []);

  if (completion) {
    return <SessionCompleteScreen completion={completion} onContinue={() => { setCompletion(null); setActiveSessionId(null); }} />;
  }

  if (activeSessionId) {
    const session = THEORY_EXPRESS.find((s) => s.id === activeSessionId)!;
    return (
      <SessionPlayer
        session={session}
        onExit={() => setActiveSessionId(null)}
        onFinish={async () => {
          try {
            const result = await api.completeTheorySession(session.id);
            localStorage.removeItem(storageKey(session.id));
            await refreshUser();
            setCompletion({ xpGained: result.xpGained, newBadges: result.newBadges });
          } catch (err) {
            if (!(err instanceof ApiError)) throw err;
            setCompletion({ xpGained: 0, newBadges: [] });
          }
        }}
      />
    );
  }

  return (
    <div className="mx-auto max-w-2xl px-4 py-8 sm:py-10">
      <button onClick={() => navigate("/dashboard")} className="text-sm font-semibold text-slate-500 hover:text-t48-ink">
        ← Volver al panel
      </button>
      <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-t48-ink">Teoría Express</h1>
      <p className="mt-1.5 text-slate-500">
        Lo esencial del temario, en 3 sesiones cortas. Nada de relleno: solo lo que decide el examen y lo que te hace mejor conductor.
      </p>

      <div className="mt-6 flex flex-col gap-3">
        {THEORY_EXPRESS.map((session, i) => {
          const done = completedSessions.has(session.id);
          const prevDone = i === 0 || completedSessions.has(THEORY_EXPRESS[i - 1].id);
          const locked = !prevDone && !done;
          return (
            <button
              key={session.id}
              disabled={locked}
              onClick={() => setActiveSessionId(session.id)}
              className={`group flex items-center gap-4 rounded-2xl border p-5 text-left transition-all ${
                locked
                  ? "border-slate-200 bg-slate-50 opacity-60"
                  : "border-slate-200 bg-white hover:-translate-y-0.5 hover:border-t48-blue hover:shadow-md"
              }`}
            >
              <div
                className={`flex h-11 w-11 shrink-0 items-center justify-center rounded-xl ${
                  done ? "bg-t48-green/10 text-t48-green-dark" : locked ? "bg-slate-100 text-slate-400" : "bg-t48-blue/10 text-t48-blue"
                }`}
              >
                {locked ? <Lock className="h-5 w-5" /> : done ? <CheckCircle className="h-5 w-5" /> : <BookOpen className="h-5 w-5" />}
              </div>
              <div className="min-w-0 flex-1">
                <p className="font-bold text-t48-ink">{session.title}</p>
                <p className="mt-0.5 text-sm text-slate-500">{session.subtitle}</p>
                <p className="mt-1 text-xs font-semibold uppercase tracking-wide text-slate-400">
                  ~{session.estimatedMinutes} min
                  {done ? " · Completada" : ""}
                </p>
              </div>
            </button>
          );
        })}
      </div>
    </div>
  );
}

function SessionPlayer({ session, onExit, onFinish }: { session: TheorySession; onExit: () => void; onFinish: () => void }) {
  const steps = useMemo(() => buildSteps(session), [session]);
  const [stepIndex, setStepIndex] = useState(() => {
    const saved = Number(localStorage.getItem(storageKey(session.id)) ?? 0);
    return Number.isFinite(saved) && saved >= 0 && saved < steps.length ? saved : 0;
  });
  const [checkSelection, setCheckSelection] = useState<number | null>(null);

  useEffect(() => {
    localStorage.setItem(storageKey(session.id), String(stepIndex));
  }, [session.id, stepIndex]);

  const step = steps[stepIndex];
  const isLastStep = stepIndex === steps.length - 1;

  function goNext() {
    setCheckSelection(null);
    if (isLastStep) {
      onFinish();
    } else {
      setStepIndex((i) => i + 1);
    }
  }

  function goPrev() {
    setCheckSelection(null);
    setStepIndex((i) => Math.max(0, i - 1));
  }

  const Icon = ICONS[step.chapter.icon];

  return (
    <div className="mx-auto max-w-2xl px-4 py-8">
      <div className="mb-3 flex items-center justify-between text-sm font-semibold text-slate-500">
        <button onClick={onExit} className="hover:text-t48-ink">
          ← Salir
        </button>
        <span>
          {stepIndex + 1} / {steps.length}
        </span>
      </div>
      <div className="h-2 w-full rounded-full bg-slate-100">
        <div
          className="h-2 rounded-full bg-t48-blue transition-all duration-300"
          style={{ width: `${((stepIndex + 1) / steps.length) * 100}%` }}
        />
      </div>

      <div key={stepIndex} className="mt-6 animate-[fadeIn_0.15s_ease-out] rounded-2xl border border-slate-200 bg-white p-6 sm:p-8">
        <p className="mb-4 flex items-center gap-2 text-xs font-bold uppercase tracking-wide text-t48-blue">
          <Icon className="h-4 w-4" />
          {step.chapter.title}
        </p>

        {step.kind === "card" ? (
          <div className="text-center sm:text-left">
            <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-t48-blue/10 text-t48-blue sm:mx-0">
              <Icon className="h-7 w-7" />
            </div>
            <h2 className="mt-4 text-xl font-extrabold leading-snug text-t48-ink">{step.chapter.cards[step.cardIndex].title}</h2>
            <p className="mt-2 text-slate-600 leading-relaxed">{step.chapter.cards[step.cardIndex].body}</p>
          </div>
        ) : (
          <CheckCard chapter={step.chapter} selection={checkSelection} onSelect={setCheckSelection} />
        )}
      </div>

      <div className="mt-6 flex items-center justify-between">
        <button
          onClick={goPrev}
          disabled={stepIndex === 0}
          className="rounded-md border border-slate-200 px-4 py-2.5 font-semibold text-slate-600 transition-colors hover:bg-slate-50 disabled:opacity-30"
        >
          Anterior
        </button>
        <button
          onClick={goNext}
          disabled={step.kind === "check" && checkSelection === null}
          className="rounded-md bg-t48-blue px-5 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark disabled:opacity-40"
        >
          {isLastStep ? "Terminar sesión" : "Siguiente"}
        </button>
      </div>
    </div>
  );
}

function CheckCard({ chapter, selection, onSelect }: { chapter: TheoryChapter; selection: number | null; onSelect: (i: number) => void }) {
  const { question, options, correctIndex } = chapter.check;
  return (
    <div>
      <p className="text-lg font-bold leading-snug text-t48-ink">{question}</p>
      <div className="mt-5 flex flex-col gap-2">
        {options.map((opt, i) => {
          const chosen = selection === i;
          const revealed = selection !== null;
          const isCorrect = i === correctIndex;
          let style = "border-slate-200 hover:border-t48-blue/50 hover:bg-slate-50";
          if (revealed && isCorrect) style = "border-t48-green bg-t48-green/10 font-semibold text-t48-green-dark";
          else if (revealed && chosen && !isCorrect) style = "border-t48-red bg-t48-red/10 font-semibold text-t48-red";
          return (
            <button
              key={i}
              onClick={() => selection === null && onSelect(i)}
              disabled={selection !== null}
              className={`flex items-center justify-between rounded-xl border px-4 py-3 text-left transition-all duration-150 disabled:cursor-default ${style}`}
            >
              <span>{opt}</span>
              {revealed && isCorrect && <CheckCircle className="h-4 w-4 shrink-0" />}
              {revealed && chosen && !isCorrect && <XCircle className="h-4 w-4 shrink-0" />}
            </button>
          );
        })}
      </div>
    </div>
  );
}

function SessionCompleteScreen({
  completion,
  onContinue,
}: {
  completion: { xpGained: number; newBadges: { id: string; label: string; emoji: string }[] };
  onContinue: () => void;
}) {
  return (
    <div className="mx-auto max-w-md px-4 py-16 text-center">
      <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-t48-green/10 text-t48-green-dark">
        <Star className="h-7 w-7" />
      </div>
      <h1 className="mt-4 text-xl font-extrabold text-t48-ink">Sesión completada</h1>
      {completion.xpGained > 0 ? (
        <p className="mt-2 text-slate-500">
          Has ganado <span className="font-bold text-t48-blue">+{completion.xpGained} XP</span>.
        </p>
      ) : (
        <p className="mt-2 text-slate-500">Ya habías completado esta sesión antes.</p>
      )}

      {completion.newBadges.length > 0 && (
        <div className="mt-4 flex flex-wrap justify-center gap-2">
          {completion.newBadges.map((b) => (
            <span key={b.id} className="flex items-center gap-1.5 rounded-md border border-slate-200 bg-white px-3 py-1.5 text-sm font-medium text-t48-ink">
              <Medal className="h-4 w-4 text-t48-blue" />
              {b.label}
            </span>
          ))}
        </div>
      )}

      <button
        onClick={onContinue}
        className="mt-6 rounded-md bg-t48-blue px-5 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark"
      >
        Volver a Teoría Express
      </button>
    </div>
  );
}
