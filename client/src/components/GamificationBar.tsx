import type { StudentProfile } from "../lib/api";

export function GamificationBar({ profile }: { profile: StudentProfile }) {
  return (
    <div className="flex items-center gap-4 text-sm font-semibold">
      <div className="flex items-center gap-1" title="Racha de dias practicando">
        <span>🔥</span>
        <span>{profile.streakCurrent}</span>
      </div>
      <div className="flex items-center gap-1" title="Puntos de experiencia">
        <span className="text-tclas-gold">⭐</span>
        <span>{profile.xpTotal} XP</span>
      </div>
      <div className="flex items-center gap-1" title="Corazones (vidas)">
        {Array.from({ length: profile.heartsMax }).map((_, i) => (
          <span key={i} className={i < profile.heartsCurrent ? "text-tclas-rose" : "text-tclas-ink/15"}>
            ♥
          </span>
        ))}
      </div>
    </div>
  );
}
