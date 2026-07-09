import { useState } from "react";
import { api } from "../lib/api";
import { IconCheck } from "./icons";

interface Props {
  minutesToday: number;
  goalMinutes: number;
  onGoalChange: (newGoal: number) => void;
}

const SIZE = 88;
const STROKE = 8;
const RADIUS = (SIZE - STROKE) / 2;
const CIRCUMFERENCE = 2 * Math.PI * RADIUS;

// Anillo de objetivo diario, al estilo "racha" de Duolingo: motiva a completar
// unos minutos concretos cada dia, no solo a "hacer una leccion cualquiera".
export function DailyGoalRing({ minutesToday, goalMinutes, onGoalChange }: Props) {
  const [editing, setEditing] = useState(false);
  const [saving, setSaving] = useState(false);
  const pct = Math.min(1, minutesToday / Math.max(1, goalMinutes));
  const reached = minutesToday >= goalMinutes;
  const offset = CIRCUMFERENCE * (1 - pct);

  async function changeGoal(delta: number) {
    const next = Math.min(180, Math.max(5, goalMinutes + delta));
    if (next === goalMinutes) return;
    setSaving(true);
    try {
      await api.patch<{ dailyGoalMinutes: number }>("/me/daily-goal", { dailyGoalMinutes: next });
      onGoalChange(next);
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="bg-white/70 border border-tclas-ink/10 rounded-xl px-4 py-3 flex flex-col items-center text-center">
      <div className="relative" style={{ width: SIZE, height: SIZE }}>
        <svg width={SIZE} height={SIZE} className="-rotate-90">
          <circle cx={SIZE / 2} cy={SIZE / 2} r={RADIUS} strokeWidth={STROKE} className="fill-none stroke-tclas-ink/10" />
          <circle
            cx={SIZE / 2}
            cy={SIZE / 2}
            r={RADIUS}
            strokeWidth={STROKE}
            strokeLinecap="round"
            strokeDasharray={CIRCUMFERENCE}
            strokeDashoffset={offset}
            className={`fill-none transition-all duration-500 ${reached ? "stroke-tclas-sage" : "stroke-tclas-gold"}`}
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          {reached ? <IconCheck className="w-6 h-6 text-tclas-sage" /> : <span className="text-lg font-display leading-none">{minutesToday}</span>}
          {!reached && <span className="text-[9px] text-tclas-ink/40">de {goalMinutes}</span>}
        </div>
      </div>
      <p className="text-[11px] uppercase tracking-wide text-tclas-ink/40 mt-2">Objetivo de hoy</p>

      {editing ? (
        <div className="flex items-center gap-2 mt-1.5">
          <button
            onClick={() => changeGoal(-5)}
            disabled={saving || goalMinutes <= 5}
            className="w-6 h-6 rounded-full bg-tclas-ink/5 hover:bg-tclas-ink/10 text-xs font-bold disabled:opacity-30"
          >
            −
          </button>
          <span className="text-xs font-semibold tabular-nums w-14">{goalMinutes} min</span>
          <button
            onClick={() => changeGoal(5)}
            disabled={saving || goalMinutes >= 180}
            className="w-6 h-6 rounded-full bg-tclas-ink/5 hover:bg-tclas-ink/10 text-xs font-bold disabled:opacity-30"
          >
            +
          </button>
          <button onClick={() => setEditing(false)} className="text-[11px] text-tclas-plum underline underline-offset-2 ml-1">
            Listo
          </button>
        </div>
      ) : (
        <button onClick={() => setEditing(true)} className="text-[11px] text-tclas-ink/40 hover:text-tclas-ink/70 underline underline-offset-2 mt-0.5">
          Cambiar objetivo
        </button>
      )}
    </div>
  );
}
