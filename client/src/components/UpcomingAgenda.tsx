import type { CurriculumTree } from "../lib/api";
import { IconCalendarDate } from "./icons";

interface Props {
  tree: CurriculumTree;
  nextClassAt: string | null;
}

interface AgendaItem {
  date: Date;
  icon: string;
  label: string;
}

function formatRelative(date: Date): string {
  const days = Math.round((date.setHours(0, 0, 0, 0) - new Date().setHours(0, 0, 0, 0)) / 86400000);
  const dateLabel = date.toLocaleDateString("es-ES", { day: "numeric", month: "short" });
  if (days === 0) return `Hoy · ${dateLabel}`;
  if (days === 1) return `Mañana · ${dateLabel}`;
  return dateLabel;
}

// Agenda sencilla: proxima clase presencial (si la profesora la ha puesto) y
// las proximas semanas del camino que todavia estan por desbloquear, en
// orden. No es un calendario completo con eventos/conciertos - solo lo que
// hay datos reales para mostrar.
export function UpcomingAgenda({ tree, nextClassAt }: Props) {
  const items: AgendaItem[] = [];

  if (nextClassAt) {
    items.push({ date: new Date(nextClassAt), icon: "🎹", label: "Clase con tu profesor/a" });
  }

  const scheduled = tree.pieces
    .flatMap((entry) => entry.lessons.map((l) => ({ ...l, pieceTitle: entry.piece.title })))
    .filter((l) => l.status === "SCHEDULED")
    .sort((a, b) => new Date(a.scheduledDate).getTime() - new Date(b.scheduledDate).getTime())
    .slice(0, 3);

  for (const lesson of scheduled) {
    items.push({ date: new Date(lesson.scheduledDate), icon: "🔓", label: `Semana ${lesson.weekNumber} de ${lesson.pieceTitle}` });
  }

  items.sort((a, b) => a.date.getTime() - b.date.getTime());

  if (items.length === 0) return null;

  return (
    <section className="max-w-md mx-auto mb-6">
      <h2 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2 px-1 flex items-center gap-1.5">
        <IconCalendarDate className="w-3.5 h-3.5" /> Próximamente
      </h2>
      <div className="bg-white/70 border border-tclas-ink/10 rounded-xl divide-y divide-tclas-ink/5">
        {items.map((item, i) => (
          <div key={i} className="flex items-center gap-3 px-4 py-2.5 text-sm">
            <span className="text-lg shrink-0">{item.icon}</span>
            <span className="flex-1 min-w-0 truncate">{item.label}</span>
            <span className="text-xs text-tclas-ink/50 shrink-0">{formatRelative(item.date)}</span>
          </div>
        ))}
      </div>
    </section>
  );
}
