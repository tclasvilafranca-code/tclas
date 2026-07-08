import { useRef, useState } from "react";
import type { PointerEvent } from "react";
import type { Exercise } from "../lib/api";
import { positionToNote } from "../lib/staff";
import { needsLedgerLines } from "../lib/staff";

interface Props {
  exercise: Exercise;
  onSubmit: (note: string) => void;
  feedback: { correct: boolean; explanation: string; correctAnswer?: unknown } | null;
}

const LINE_Y = [100, 88, 76, 64, 52];

export function DragStaffExercise({ exercise, onSubmit, feedback }: Props) {
  const { clef, noteLabel } = exercise.data as { clef: "treble" | "bass"; noteLabel: string };
  const [pos, setPos] = useState<number | null>(null);
  const [dragging, setDragging] = useState(false);
  const svgRef = useRef<SVGSVGElement>(null);
  const submitted = !!feedback;

  function posFromClientY(clientY: number): number {
    const rect = svgRef.current!.getBoundingClientRect();
    const scaleY = 160 / rect.height;
    const svgY = (clientY - rect.top) * scaleY;
    const raw = (100 - svgY) / 6;
    return Math.max(-6, Math.min(14, Math.round(raw)));
  }

  function handlePointerDown(e: PointerEvent<SVGSVGElement>) {
    if (submitted) return;
    setDragging(true);
    setPos(posFromClientY(e.clientY));
  }
  function handlePointerMove(e: PointerEvent<SVGSVGElement>) {
    if (!dragging || submitted) return;
    setPos(posFromClientY(e.clientY));
  }
  function handlePointerUp() {
    if (!dragging || submitted || pos === null) return;
    setDragging(false);
    onSubmit(positionToNote(pos, clef));
  }

  const cy = pos !== null ? 100 - pos * 6 : 132;
  const color = feedback ? (feedback.correct ? "#6f8a6e" : "#c65b6c") : "#d4a94c";

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-2">{exercise.prompt}</p>
      <p className="text-sm text-tclas-ink/60 mb-4">
        Arrastra la nota hasta su sitio en el pentagrama: <strong className="text-tclas-plum">{noteLabel}</strong>
      </p>
      <svg
        ref={svgRef}
        viewBox="0 0 300 160"
        width="100%"
        height="200"
        className="max-w-sm mx-auto touch-none select-none cursor-grab active:cursor-grabbing"
        onPointerDown={handlePointerDown}
        onPointerMove={handlePointerMove}
        onPointerUp={handlePointerUp}
      >
        {LINE_Y.map((y) => (
          <line key={y} x1={10} y1={y} x2={290} y2={y} stroke="currentColor" strokeWidth={1.5} className="text-tclas-ink/70" />
        ))}
        <text x={16} y={clef === "treble" ? 96 : 84} fontSize={clef === "treble" ? 58 : 40} className="fill-tclas-plum font-display">
          {clef === "treble" ? "𝄞" : "𝄢"}
        </text>
        {pos !== null &&
          needsLedgerLines(pos).map((lp) => (
            <line key={lp} x1={141} y1={100 - lp * 6} x2={159} y2={100 - lp * 6} stroke="currentColor" strokeWidth={1.5} className="text-tclas-ink/70" />
          ))}
        <ellipse cx={150} cy={cy} rx={9} ry={7} fill={color} transform={`rotate(-15 150 ${cy})`} />
      </svg>
      {pos === null && <p className="text-xs text-tclas-ink/40 mt-2">Toca y arrastra dentro del pentagrama</p>}
      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
