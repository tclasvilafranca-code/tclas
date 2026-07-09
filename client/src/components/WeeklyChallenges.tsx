import { useEffect, useState } from "react";
import { api } from "../lib/api";
import type { Challenge } from "../lib/api";
import { IconCheck } from "./icons";

// Retos de la semana: 3 objetivos sencillos calculados de datos reales (dias
// practicados, lecciones completadas, minutos totales), sin tienda ni monedas
// -  solo un empujon extra de XP al cumplirlos.
export function WeeklyChallenges() {
  const [challenges, setChallenges] = useState<Challenge[] | null>(null);

  useEffect(() => {
    api.get<{ challenges: Challenge[] }>("/me/challenges").then((r) => setChallenges(r.challenges));
  }, []);

  if (!challenges || challenges.length === 0) return null;

  return (
    <section className="max-w-md mx-auto mt-6 mb-6">
      <h2 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2 px-1">Retos de esta semana</h2>
      <div className="bg-white/70 border border-tclas-ink/10 rounded-xl p-4 grid gap-3">
        {challenges.map((c) => {
          const pct = Math.min(100, Math.round((c.progress / c.target) * 100));
          return (
            <div key={c.code} className="flex items-center gap-3">
              <span className="text-xl shrink-0">{c.icon}</span>
              <div className="flex-1 min-w-0">
                <div className="flex items-center justify-between text-xs mb-1">
                  <span className={`font-semibold ${c.completed ? "text-tclas-sage" : "text-tclas-ink"}`}>{c.label}</span>
                  <span className="text-tclas-ink/40 shrink-0 ml-2">
                    {Math.min(c.progress, c.target)}/{c.target}
                  </span>
                </div>
                <div className="h-2 bg-tclas-ink/10 rounded-full overflow-hidden">
                  <div className={`h-full ${c.completed ? "bg-tclas-sage" : "bg-tclas-gold"}`} style={{ width: `${pct}%`, transition: "width 300ms ease" }} />
                </div>
              </div>
              {c.completed ? (
                <IconCheck className="w-5 h-5 text-tclas-sage shrink-0" />
              ) : (
                <span className="text-2xs text-tclas-gold-shadow font-semibold shrink-0">+{c.xpReward}</span>
              )}
            </div>
          );
        })}
      </div>
    </section>
  );
}
