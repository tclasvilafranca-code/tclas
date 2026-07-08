import type { StudentProfile } from "../lib/api";

export function GamificationBar({ profile }: { profile: StudentProfile }) {
  return (
    <div className="flex items-center gap-1.5 sm:gap-2 text-sm font-bold">
      <div
        className={`flex items-center gap-1 rounded-full px-2.5 py-1 ${profile.streakCurrent > 0 ? "bg-tclas-gold/15 text-tclas-gold-shadow" : "bg-tclas-ink/5 text-tclas-ink/40"}`}
        title="Racha de dias practicando"
      >
        <span>🔥</span>
        <span>{profile.streakCurrent}</span>
      </div>
      <div className="flex items-center gap-1 rounded-full px-2.5 py-1 bg-tclas-plum/10 text-tclas-plum" title="Puntos de experiencia">
        <span>⭐</span>
        <span>{profile.xpTotal}</span>
      </div>
      <div className="flex items-center gap-0.5 rounded-full px-2.5 py-1 bg-tclas-rose/10" title="Corazones (vidas)">
        {Array.from({ length: profile.heartsMax }).map((_, i) => (
          <span key={i} className={i < profile.heartsCurrent ? "text-tclas-rose" : "text-tclas-ink/15"}>
            ♥
          </span>
        ))}
      </div>
    </div>
  );
}
