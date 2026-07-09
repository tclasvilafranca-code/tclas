import { useEffect, useState } from "react";
import { api } from "../lib/api";
import type { ProfileStats, Badge } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import { StreakCalendar } from "../components/StreakCalendar";
import { MyPerformance } from "../components/MyPerformance";
import { MascotOwl } from "../components/MascotOwl";

const DAY_LETTERS = ["D", "L", "M", "X", "J", "V", "S"];

function formatMinutes(total: number): string {
  if (total < 60) return `${total} min`;
  const h = Math.floor(total / 60);
  const m = total % 60;
  return m === 0 ? `${h} h` : `${h} h ${m} min`;
}

export function Perfil() {
  const { me } = useAuth();
  const [stats, setStats] = useState<ProfileStats | null>(null);
  const [badges, setBadges] = useState<Badge[]>([]);

  useEffect(() => {
    api.get<ProfileStats>("/me/profile-stats").then(setStats);
    api.get<Badge[]>("/badges").then(setBadges);
  }, []);

  if (!me?.studentProfile) return null;

  const maxMinutes = stats ? Math.max(1, ...stats.last7Days.map((d) => d.minutes)) : 1;

  return (
    <main className="px-4 py-8">
      <div className="max-w-md mx-auto flex flex-col items-center text-center mb-6">
        <MascotOwl mood="cheer" size={72} />
        <h1 className="font-display text-2xl mt-2">{me.name}</h1>
        <p className="text-sm text-tclas-ink/50">{me.studentProfile.ageGroup === "KIDS" ? "Nivel infantil" : me.studentProfile.ageGroup === "TEENS" ? "Adolescente" : "Adulto"}</p>
      </div>

      <div className="max-w-md mx-auto grid grid-cols-3 gap-3 mb-6">
        <div className="bg-white/70 border border-tclas-ink/10 rounded-xl px-3 py-3 text-center">
          <p className="text-xl font-display text-tclas-plum">{stats ? formatMinutes(stats.totalMinutes) : "…"}</p>
          <p className="text-[10px] uppercase tracking-wide text-tclas-ink/40">practicados</p>
        </div>
        <div className="bg-white/70 border border-tclas-ink/10 rounded-xl px-3 py-3 text-center">
          <p className="text-xl font-display text-tclas-gold-shadow">{me.studentProfile.xpTotal}</p>
          <p className="text-[10px] uppercase tracking-wide text-tclas-ink/40">XP total</p>
        </div>
        <div className="bg-white/70 border border-tclas-ink/10 rounded-xl px-3 py-3 text-center">
          <p className="text-xl font-display text-tclas-sage">{stats?.piecesCompleted ?? "…"}</p>
          <p className="text-[10px] uppercase tracking-wide text-tclas-ink/40">piezas terminadas</p>
        </div>
      </div>

      <section className="max-w-md mx-auto mb-6">
        <h2 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2 px-1">Racha</h2>
        <div className="bg-white/70 border border-tclas-ink/10 rounded-xl p-4">
          <StreakCalendar streakCurrent={me.studentProfile.streakCurrent} lastActivityDate={me.studentProfile.lastActivityDate} />
          <p className="text-center text-xs text-tclas-ink/40 mt-3">
            Racha actual: <strong className="text-tclas-ink">{me.studentProfile.streakCurrent} días</strong> · Récord:{" "}
            <strong className="text-tclas-ink">{me.studentProfile.streakLongest} días</strong>
          </p>
        </div>
      </section>

      <section className="max-w-md mx-auto mb-6">
        <h2 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2 px-1">Minutos practicados esta semana</h2>
        <div className="bg-white/70 border border-tclas-ink/10 rounded-xl p-4">
          {!stats ? (
            <p className="text-center text-sm text-tclas-ink/40 py-4">Cargando...</p>
          ) : (
            <div className="flex items-end justify-between gap-2 h-28">
              {stats.last7Days.map((d) => {
                const date = new Date(d.date + "T00:00:00");
                const pct = d.minutes === 0 ? 0 : Math.max(8, (d.minutes / maxMinutes) * 100);
                return (
                  <div key={d.date} className="flex-1 flex flex-col items-center justify-end gap-1.5 h-full">
                    <span className="text-[10px] text-tclas-ink/40 tabular-nums">{d.minutes > 0 ? d.minutes : ""}</span>
                    <div className="w-full rounded-t-md bg-tclas-plum/15 flex items-end" style={{ height: "100%" }}>
                      <div
                        className={`w-full rounded-t-md ${d.minutes > 0 ? "bg-tclas-gold" : "bg-transparent"}`}
                        style={{ height: `${pct}%`, transition: "height 300ms ease" }}
                      />
                    </div>
                    <span className="text-[10px] font-semibold text-tclas-ink/50">{DAY_LETTERS[date.getDay()]}</span>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </section>

      <div className="max-w-md mx-auto mb-2">
        <MyPerformance />
      </div>

      <section className="max-w-md mx-auto mb-6">
        <h2 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2 px-1">
          Insignias {badges.length > 0 && `(${badges.length})`}
        </h2>
        {badges.length === 0 ? (
          <p className="text-sm text-tclas-ink/40 bg-white/70 border border-tclas-ink/10 rounded-xl p-4 text-center">
            Todavía no has ganado ninguna insignia. ¡Sigue practicando!
          </p>
        ) : (
          <div className="grid grid-cols-3 gap-3">
            {badges.map((b) => (
              <div key={b.code} title={b.description} className="bg-white/70 border border-tclas-ink/10 rounded-xl p-3 text-center">
                <span className="text-3xl block mb-1">{b.icon}</span>
                <span className="text-[11px] font-semibold leading-tight block">{b.name}</span>
              </div>
            ))}
          </div>
        )}
      </section>
    </main>
  );
}
