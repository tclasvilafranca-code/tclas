import { useMemo, useState } from "react";
import type { Exercise } from "../lib/api";
import { StaffView } from "../components/StaffView";

interface Props {
  exercise: Exercise;
  onSubmit: (pairs: { left: string; right: string }[]) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

function Cell({ value }: { value: string }) {
  if (value.startsWith("STAFF:")) {
    const [, note, clef] = value.split(":");
    // Alto fijo y pequeno (no un transform CSS, que solo escala visualmente
    // y deja el hueco original reservado en el documento): asi cada celda
    // ocupa solo el espacio que realmente se ve, y la lista no se alarga
    // mucho mas de lo necesario obligando a bajar la pagina.
    return <StaffView clef={clef as "treble" | "bass"} notes={[note]} height={44} />;
  }
  return <span>{value}</span>;
}

export function MatchingExercise({ exercise, onSubmit, feedback }: Props) {
  const leftItems: string[] = exercise.data.leftItems;
  const rightItems: string[] = exercise.data.rightItems;

  const [matched, setMatched] = useState<{ left: string; right: string }[]>([]);
  const [selectedLeft, setSelectedLeft] = useState<string | null>(null);
  const done = matched.length === leftItems.length;

  const usedRights = useMemo(() => new Set(matched.map((m) => m.right)), [matched]);

  function chooseLeft(left: string) {
    if (feedback || matched.some((m) => m.left === left)) return;
    setSelectedLeft(left === selectedLeft ? null : left);
  }

  function chooseRight(right: string) {
    if (feedback || usedRights.has(right) || !selectedLeft) return;
    const next = [...matched, { left: selectedLeft, right }];
    setMatched(next);
    setSelectedLeft(null);
    if (next.length === leftItems.length) {
      onSubmit(next);
    }
  }

  function undo(left: string) {
    if (feedback) return;
    setMatched((prev) => prev.filter((m) => m.left !== left));
  }

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-4">{exercise.prompt}</p>
      <div className="grid grid-cols-2 gap-4 sm:gap-6 max-w-md mx-auto">
        <div className="flex flex-col gap-2">
          {leftItems.map((left) => {
            const pair = matched.find((m) => m.left === left);
            return (
              <button
                key={left}
                onClick={() => (pair ? undo(left) : chooseLeft(left))}
                className={`rounded-xl border-2 py-1.5 px-3 font-semibold min-h-[2.5rem] flex items-center justify-center transition-colors
                  ${pair ? "border-tclas-sage bg-tclas-sage/15" : selectedLeft === left ? "border-tclas-gold bg-tclas-gold/15" : "border-tclas-ink/15 hover:border-tclas-gold"}`}
              >
                <Cell value={left} />
              </button>
            );
          })}
        </div>
        <div className="flex flex-col gap-2">
          {rightItems.map((right) => (
            <button
              key={right}
              onClick={() => chooseRight(right)}
              disabled={usedRights.has(right)}
              className={`rounded-xl border-2 py-1.5 px-3 font-semibold min-h-[2.5rem] flex items-center justify-center transition-colors
                ${usedRights.has(right) ? "border-tclas-sage bg-tclas-sage/15 opacity-60" : "border-tclas-ink/15 hover:border-tclas-gold"}`}
            >
              <Cell value={right} />
            </button>
          ))}
        </div>
      </div>
      {!done && <p className="text-xs text-tclas-ink/50 mt-4">Toca un elemento de la izquierda y luego su pareja a la derecha.</p>}
      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
