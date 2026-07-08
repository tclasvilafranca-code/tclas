import { useMemo } from "react";
import { MascotOwl } from "./MascotOwl";
import { lessonCompleteMessage } from "../lib/misol";

interface Props {
  stars: number;
  score: number;
  xpAwarded: number;
  passed: boolean;
  pieceTitle: string;
  newBadges: { code: string; name: string; icon: string }[];
  onContinue: () => void;
  onRetry: () => void;
}

const CONFETTI_COLORS = ["#d4a94c", "#4a1942", "#6f8a6e", "#c65b6c", "#e8c97a"];

function Confetti() {
  const pieces = useMemo(
    () =>
      Array.from({ length: 22 }).map((_, i) => ({
        left: Math.random() * 100,
        delay: Math.random() * 0.3,
        duration: 1.4 + Math.random() * 0.8,
        color: CONFETTI_COLORS[i % CONFETTI_COLORS.length],
        size: 6 + Math.random() * 5,
        rotate: Math.random() * 360,
      })),
    []
  );
  return (
    <div className="pointer-events-none absolute inset-x-0 top-0 h-0 overflow-visible" aria-hidden="true">
      {pieces.map((p, i) => (
        <span
          key={i}
          className="absolute top-0 animate-confetti"
          style={{
            left: `${p.left}%`,
            width: p.size,
            height: p.size * 0.5,
            backgroundColor: p.color,
            animationDelay: `${p.delay}s`,
            animationDuration: `${p.duration}s`,
            transform: `rotate(${p.rotate}deg)`,
          }}
        />
      ))}
    </div>
  );
}

export function LessonCompleteModal({ stars, score, xpAwarded, passed, pieceTitle, newBadges, onContinue, onRetry }: Props) {
  const message = useMemo(() => lessonCompleteMessage(stars, pieceTitle), [stars, pieceTitle]);
  return (
    <div className="fixed inset-0 bg-tclas-ink/50 flex items-center justify-center z-50 p-4">
      <div className="relative bg-tclas-cream rounded-2xl shadow-2xl max-w-sm w-full p-6 text-center animate-pop-in border border-tclas-gold/30 overflow-hidden">
        {passed && <Confetti />}
        <MascotOwl mood={stars >= 1 ? "celebrate" : "encourage"} size={84} className="mx-auto mb-2" />
        <h2 className="font-display text-2xl mb-1">{passed ? "¡Leccion completada!" : "Casi lo tienes"}</h2>
        <div className="flex justify-center gap-1 my-3 text-3xl">
          {[1, 2, 3].map((s) => (
            <span key={s} className={s <= stars ? "text-tclas-gold" : "text-tclas-ink/15"}>
              ★
            </span>
          ))}
        </div>
        <p className="text-sm text-tclas-ink/70 italic mb-3">"{message}"</p>
        <p className="font-mono text-3xl font-bold text-tclas-plum mb-1 tabular-nums">
          {score}
          <span className="text-base font-sans font-normal text-tclas-ink/40"> / 1000</span>
        </p>
        {passed && <p className="text-tclas-plum font-semibold mb-3">+{xpAwarded} XP</p>}
        {!passed && <p className="text-tclas-ink/70 mb-3 text-sm">Necesitas al menos un 40% de aciertos para superar la leccion. ¡Intentalo de nuevo!</p>}

        {newBadges.length > 0 && (
          <div className="bg-tclas-gold/10 rounded-xl p-3 mb-4">
            <p className="text-xs uppercase tracking-wide text-tclas-plum/70 mb-2">Nueva insignia</p>
            {newBadges.map((b) => (
              <div key={b.code} className="flex items-center justify-center gap-2 text-tclas-ink font-semibold">
                <span className="text-2xl">{b.icon}</span> {b.name}
              </div>
            ))}
          </div>
        )}

        <button
          onClick={passed ? onContinue : onRetry}
          className={`w-full btn-push font-bold uppercase tracking-wide text-sm rounded-2xl py-3.5 transition-colors
            ${passed ? "bg-tclas-sage border-tclas-sage-shadow text-white hover:bg-tclas-sage/90" : "bg-tclas-plum border-tclas-plum-shadow text-tclas-cream hover:bg-tclas-plum-light"}`}
        >
          {passed ? "Continuar" : "Reintentar leccion"}
        </button>
      </div>
    </div>
  );
}
