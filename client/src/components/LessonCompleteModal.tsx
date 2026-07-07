interface Props {
  stars: number;
  xpAwarded: number;
  passed: boolean;
  newBadges: { code: string; name: string; icon: string }[];
  onContinue: () => void;
  onRetry: () => void;
}

export function LessonCompleteModal({ stars, xpAwarded, passed, newBadges, onContinue, onRetry }: Props) {
  return (
    <div className="fixed inset-0 bg-tclas-ink/50 flex items-center justify-center z-50 p-4">
      <div className="bg-tclas-cream rounded-2xl shadow-2xl max-w-sm w-full p-6 text-center animate-pop-in border border-tclas-gold/30">
        <div className="text-5xl mb-2">{passed ? "🎉" : "💪"}</div>
        <h2 className="font-display text-2xl mb-1">{passed ? "¡Leccion completada!" : "Casi lo tienes"}</h2>
        <div className="flex justify-center gap-1 my-3 text-3xl">
          {[1, 2, 3].map((s) => (
            <span key={s} className={s <= stars ? "text-tclas-gold" : "text-tclas-ink/15"}>
              ★
            </span>
          ))}
        </div>
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
          className="w-full bg-tclas-plum text-tclas-cream font-semibold rounded-xl py-3 hover:bg-tclas-plum-light transition-colors"
        >
          {passed ? "Continuar" : "Reintentar leccion"}
        </button>
      </div>
    </div>
  );
}
