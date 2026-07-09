import { IconFlame } from "./icons";

interface Props {
  streakCurrent: number;
  lastActivityDate: string | null;
}

const DAY_LETTERS = ["D", "L", "M", "X", "J", "V", "S"];

function startOfDay(d: Date): Date {
  const copy = new Date(d);
  copy.setHours(0, 0, 0, 0);
  return copy;
}

export function StreakCalendar({ streakCurrent, lastActivityDate }: Props) {
  const anchor = lastActivityDate ? startOfDay(new Date(lastActivityDate)) : null;
  const today = startOfDay(new Date());

  const days = Array.from({ length: 7 }).map((_, i) => {
    const offset = 6 - i;
    const date = new Date(today);
    date.setDate(date.getDate() - offset);
    const dayDiff = anchor ? Math.round((anchor.getTime() - date.getTime()) / 86400000) : null;
    const lit = anchor !== null && dayDiff !== null && dayDiff >= 0 && dayDiff < streakCurrent;
    const isToday = date.getTime() === today.getTime();
    return { date, lit, isToday };
  });

  return (
    <div className="flex items-center justify-center gap-2 mt-4">
      {days.map((d, i) => (
        <div key={i} className="flex flex-col items-center gap-1">
          <div
            className={`w-8 h-8 rounded-full flex items-center justify-center text-sm transition-colors
              ${d.lit ? "bg-tclas-gold/20" : "bg-tclas-ink/5"}
              ${d.isToday && !d.lit ? "ring-2 ring-tclas-gold/50" : ""}`}
          >
            {d.lit && <IconFlame className="w-4 h-4 text-tclas-gold-shadow" />}
          </div>
          <span className={`text-[10px] ${d.isToday ? "font-bold text-tclas-plum" : "text-tclas-ink/40"}`}>{DAY_LETTERS[d.date.getDay()]}</span>
        </div>
      ))}
    </div>
  );
}
