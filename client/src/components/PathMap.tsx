import type { RepertoireNode } from "../lib/api";

interface Props {
  pieces: RepertoireNode[];
  onOpenLesson: (lessonId: string) => void;
}

// Patron de zigzag tipo "camino de juego": desplazamiento horizontal ciclico por nodo.
const ZIGZAG = [0, 60, 96, 60, 0, -60, -96, -60];

const SEASONAL_LABEL: Record<string, string> = { christmas: "🎄 Navidad" };

function formatDate(iso: string): string {
  return new Date(iso).toLocaleDateString("es-ES", { day: "numeric", month: "short" });
}

export function PathMap({ pieces, onOpenLesson }: Props) {
  let globalIndex = 0;

  return (
    <div className="max-w-md mx-auto pb-16">
      {pieces.map((entry) => (
        <section key={entry.id} className="mb-4">
          <div
            className={`mx-auto mb-6 max-w-xs rounded-2xl px-5 py-4 text-center border-2 shadow-sm
              ${entry.completed ? "bg-tclas-sage/10 border-tclas-sage/40" : entry.status === "ACTIVE" ? "bg-tclas-gold/10 border-tclas-gold/50" : "bg-white/50 border-tclas-ink/10"}`}
          >
            <div className="text-4xl mb-1">{entry.piece.iconEmoji}</div>
            <h2 className="font-display text-lg leading-tight">{entry.piece.title}</h2>
            {entry.piece.composer && <p className="text-xs text-tclas-ink/50">{entry.piece.composer}</p>}
            <div className="flex items-center justify-center gap-2 mt-2 text-xs text-tclas-ink/50">
              <span>{entry.piece.keySignature}</span>
              <span>·</span>
              <span>{entry.piece.timeSignature}</span>
              {entry.piece.seasonalTag && SEASONAL_LABEL[entry.piece.seasonalTag] && (
                <>
                  <span>·</span>
                  <span>{SEASONAL_LABEL[entry.piece.seasonalTag]}</span>
                </>
              )}
            </div>
            {entry.teacherNote && <p className="text-xs text-tclas-plum mt-2 italic">"{entry.teacherNote}"</p>}
          </div>

          <div className="flex flex-col items-center gap-5">
            {entry.lessons.map((lesson) => {
              const offset = ZIGZAG[globalIndex % ZIGZAG.length];
              globalIndex++;
              const locked = lesson.status === "LOCKED";
              const scheduled = lesson.status === "SCHEDULED";
              const completed = lesson.status === "COMPLETED";
              const disabled = locked || scheduled;
              return (
                <div key={lesson.id} style={{ transform: `translateX(${offset}px)` }}>
                  <button
                    disabled={disabled}
                    onClick={() => onOpenLesson(lesson.id)}
                    title={scheduled ? `Disponible el ${formatDate(lesson.scheduledDate)}` : lesson.title}
                    className={`relative w-20 h-20 rounded-full flex flex-col items-center justify-center border-4 font-bold text-xs transition-transform piano-key-shadow
                      ${completed ? "bg-tclas-gold border-tclas-gold-light text-tclas-ink" : disabled ? "bg-tclas-ink/5 border-tclas-ink/10 text-tclas-ink/30" : "bg-tclas-plum border-tclas-plum-light text-tclas-cream hover:scale-110 animate-pop-in"}`}
                  >
                    {completed ? (
                      <span className="text-xl">{"★".repeat(lesson.stars)}</span>
                    ) : scheduled ? (
                      <span className="text-2xl">📅</span>
                    ) : locked ? (
                      <span className="text-2xl">🔒</span>
                    ) : (
                      <span className="text-2xl">▶</span>
                    )}
                  </button>
                  <p className="text-center text-[11px] text-tclas-ink/50 mt-1 w-24 leading-tight">
                    Semana {lesson.weekNumber}
                    {scheduled && (
                      <>
                        <br />
                        {formatDate(lesson.scheduledDate)}
                      </>
                    )}
                  </p>
                </div>
              );
            })}
          </div>
        </section>
      ))}
    </div>
  );
}
