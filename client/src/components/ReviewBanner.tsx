import type { ReviewDue } from "../lib/api";
import { IconRepeat } from "./icons";

interface Props {
  due: ReviewDue[];
  onOpenLesson: (lessonId: string) => void;
}

export function ReviewBanner({ due, onOpenLesson }: Props) {
  if (due.length === 0) return null;

  return (
    <div className="max-w-md mx-auto mb-6 bg-tclas-gold/10 border-2 border-dashed border-tclas-gold/40 rounded-2xl px-4 py-4">
      <p className="flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wide text-tclas-gold-shadow mb-2">
        <IconRepeat className="w-3.5 h-3.5" /> Repaso de hoy · mantén vivas tus piezas
      </p>
      <div className="flex flex-col gap-2">
        {due.map((r) => (
          <button
            key={r.entryId}
            onClick={() => onOpenLesson(r.lessonId)}
            className="btn-push flex items-center gap-3 bg-white border-2 border-b-4 border-tclas-gold-light border-b-tclas-gold-shadow rounded-xl px-3 py-2.5 text-left"
          >
            <span className="text-2xl shrink-0">{r.iconEmoji}</span>
            <span className="flex-1 min-w-0">
              <span className="block text-sm font-semibold truncate">{r.pieceTitle}</span>
              <span className="block text-[11px] text-tclas-ink/50">Repasarla ahora te ayuda a no olvidarla</span>
            </span>
            <span className="text-xs font-bold text-tclas-gold-shadow shrink-0">Repasar ›</span>
          </button>
        ))}
      </div>
    </div>
  );
}
