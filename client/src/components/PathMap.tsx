import type { RepertoireNode } from "../lib/api";
import { msUntilNextHeart, formatCountdown } from "../lib/hearts";
import { IconStar, IconHeart, IconCalendarDate, IconLock, IconPlay } from "./icons";

interface Props {
  pieces: RepertoireNode[];
  onOpenLesson: (lessonId: string) => void;
  onOpenPiece: (pieceId: string) => void;
  heartsCurrent: number;
  heartsUpdatedAt: string;
}

// Patron de zigzag tipo "camino de juego": desplazamiento horizontal ciclico por nodo.
const ZIGZAG = [0, 60, 96, 60, 0, -60, -96, -60];
const PITCH = 140; // distancia vertical aproximada entre el centro de un nodo y el siguiente

const SEASONAL_LABEL: Record<string, string> = { christmas: "🎄 Navidad" };

function formatDate(iso: string): string {
  return new Date(iso).toLocaleDateString("es-ES", { day: "numeric", month: "short" });
}

export function PathMap({ pieces, onOpenLesson, onOpenPiece, heartsCurrent, heartsUpdatedAt }: Props) {
  let globalIndex = 0;
  const outOfHearts = heartsCurrent <= 0;

  return (
    <div className="max-w-md mx-auto pb-16">
      {pieces.map((entry) => (
        <section key={entry.id} className="mb-4">
          <button
            onClick={() => onOpenPiece(entry.piece.id)}
            title="Ver partitura, informacion y tips"
            className={`group flex items-center gap-4 w-full mx-auto mb-8 max-w-xs rounded-2xl px-5 py-4 text-left border-2 border-b-4 shadow-sm transition-transform hover:-translate-y-0.5 cursor-pointer
              ${
                entry.completed
                  ? "bg-tclas-sage/10 border-tclas-sage/40 border-b-tclas-sage-shadow/50"
                  : entry.status === "ACTIVE"
                    ? "bg-tclas-gold/10 border-tclas-gold/50 border-b-tclas-gold-shadow/60"
                    : "bg-white/60 border-tclas-ink/10 border-b-tclas-ink/15"
              }`}
          >
            <div className="w-16 h-16 rounded-full bg-white flex items-center justify-center text-3xl shrink-0 shadow-sm">{entry.piece.iconEmoji}</div>
            <div className="min-w-0 flex-1">
              <h2 className="font-display text-lg leading-tight truncate">{entry.piece.title}</h2>
              {entry.piece.composer && <p className="text-xs text-tclas-ink/50 truncate">{entry.piece.composer}</p>}
              <div className="flex items-center gap-2 mt-1 text-xs text-tclas-ink/50 flex-wrap">
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
              {entry.teacherNote && <p className="text-xs text-tclas-plum mt-1 italic truncate">"{entry.teacherNote}"</p>}
            </div>
            <span className="text-tclas-ink/25 text-2xl shrink-0 group-hover:text-tclas-plum group-hover:translate-x-0.5 transition-all">›</span>
          </button>

          <div className="flex flex-col items-center gap-4">
            {entry.lessons.map((lesson, i) => {
              const offset = ZIGZAG[globalIndex % ZIGZAG.length];
              const nextOffset = i < entry.lessons.length - 1 ? ZIGZAG[(globalIndex + 1) % ZIGZAG.length] : null;
              globalIndex++;
              const locked = lesson.status === "LOCKED";
              const scheduled = lesson.status === "SCHEDULED";
              const completed = lesson.status === "COMPLETED";
              const noHearts = lesson.status === "AVAILABLE" && outOfHearts;
              const disabled = locked || scheduled || noHearts;

              let connectorAngle = 0;
              let connectorLength = 0;
              if (nextOffset !== null) {
                const dx = nextOffset - offset;
                connectorLength = Math.sqrt(dx * dx + PITCH * PITCH);
                connectorAngle = Math.atan2(PITCH, dx);
              }

              return (
                <div key={lesson.id} className="relative" style={{ transform: `translateX(${offset}px)` }}>
                  {nextOffset !== null && (
                    <div
                      aria-hidden="true"
                      className="absolute z-0 border-t-[3px] border-dotted border-tclas-ink/20"
                      style={{ left: "50%", top: 48, width: connectorLength, transformOrigin: "0 0", transform: `rotate(${connectorAngle}rad)` }}
                    />
                  )}
                  <button
                    disabled={disabled}
                    onClick={() => onOpenLesson(lesson.id)}
                    title={
                      noHearts
                        ? `Sin corazones. Proximo corazon en ${formatCountdown(msUntilNextHeart(heartsUpdatedAt))}`
                        : scheduled
                          ? `Disponible el ${formatDate(lesson.scheduledDate)}`
                          : lesson.title
                    }
                    className={`relative z-10 w-24 h-24 rounded-full flex flex-col items-center justify-center border-4 border-b-[6px] font-bold text-xs btn-push
                      ${
                        completed
                          ? "bg-tclas-gold border-tclas-gold-light border-b-tclas-gold-shadow text-tclas-ink"
                          : disabled
                            ? "bg-tclas-ink/5 border-tclas-ink/10 border-b-tclas-ink/10 text-tclas-ink/30"
                            : "bg-tclas-plum border-tclas-plum-light border-b-tclas-plum-shadow text-tclas-cream hover:scale-105 animate-pop-in"
                      }`}
                  >
                    {completed ? (
                      <span className="flex gap-0.5">
                        {Array.from({ length: lesson.stars }).map((_, si) => (
                          <IconStar key={si} className="w-4 h-4" />
                        ))}
                      </span>
                    ) : noHearts ? (
                      <IconHeart className="w-7 h-7" filled={false} />
                    ) : scheduled ? (
                      <IconCalendarDate className="w-7 h-7" />
                    ) : locked ? (
                      <IconLock className="w-7 h-7" />
                    ) : (
                      <IconPlay className="w-7 h-7 ml-0.5" />
                    )}
                  </button>
                  <p className="relative z-10 text-center text-2xs text-tclas-ink/50 mt-1 w-24 leading-tight">
                    {noHearts ? (
                      <span className="text-tclas-rose/70">Sin corazones</span>
                    ) : (
                      <>
                        Semana {lesson.weekNumber}
                        {scheduled && (
                          <>
                            <br />
                            {formatDate(lesson.scheduledDate)}
                          </>
                        )}
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
