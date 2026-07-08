import { useEffect, useState } from "react";
import { api } from "../lib/api";
import type { PhaseStats } from "../lib/api";
import { PHASE_LABEL, PHASE_ORDER } from "../lib/phases";

export function MyPerformance() {
  const [stats, setStats] = useState<PhaseStats | null>(null);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    api.get<{ phaseStats: PhaseStats }>("/me/stats").then((r) => setStats(r.phaseStats));
  }, []);

  const hasData = stats && PHASE_ORDER.some((p) => (stats[p]?.total ?? 0) > 0);

  return (
    <div className="max-w-md mx-auto mb-6">
      <button
        onClick={() => setOpen((v) => !v)}
        className="w-full flex items-center justify-between text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 hover:text-tclas-ink/70 px-1 py-1"
      >
        <span>Cómo vas</span>
        <span>{open ? "▲" : "▼"}</span>
      </button>

      {open && (
        <div className="bg-white/70 border border-tclas-ink/10 rounded-xl p-4 mt-1">
          {!hasData ? (
            <p className="text-sm text-tclas-ink/50 text-center py-2">Completa algunas lecciones y aquí verás en qué eres más fuerte.</p>
          ) : (
            <div className="grid gap-3">
              {PHASE_ORDER.map((phase) => {
                const stat = stats?.[phase];
                if (!stat || stat.total === 0) return null;
                const pct = Math.round((stat.correct / stat.total) * 100);
                const barColor = pct >= 80 ? "bg-tclas-sage" : pct >= 55 ? "bg-tclas-gold" : "bg-tclas-rose";
                return (
                  <div key={phase}>
                    <div className="flex items-center justify-between text-xs mb-1">
                      <span className="font-semibold">{PHASE_LABEL[phase].label}</span>
                      <span className="text-tclas-ink/50">{pct}%</span>
                    </div>
                    <div className="h-2 bg-tclas-ink/10 rounded-full overflow-hidden">
                      <div className={`h-full ${barColor}`} style={{ width: `${pct}%` }} />
                    </div>
                  </div>
                );
              })}
              <p className="text-[11px] text-tclas-ink/40 text-center mt-1">
                Lo que esté en {""}
                <span className="text-tclas-rose font-semibold">rojo</span> es lo que más te ayudaría practicar.
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
