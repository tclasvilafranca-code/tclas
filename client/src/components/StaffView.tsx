import { staffPosition, needsLedgerLines, accidentalSymbol } from "../lib/staff";

interface StaffViewProps {
  clef: "treble" | "bass";
  notes: string[];
  activeIndex?: number;
  correctness?: ("pending" | "correct" | "wrong")[];
}

const LINE_Y = [100, 88, 76, 64, 52];
const NOTE_SPACING = 46;
const LEFT_MARGIN = 70;

export function StaffView({ clef, notes, activeIndex, correctness }: StaffViewProps) {
  const width = LEFT_MARGIN + notes.length * NOTE_SPACING + 30;

  return (
    <svg viewBox={`0 0 ${width} 160`} width="100%" height="160" className="max-w-xl mx-auto select-none">
      {LINE_Y.map((y) => (
        <line key={y} x1={10} y1={y} x2={width - 10} y2={y} stroke="currentColor" strokeWidth={1.5} className="text-tclas-ink/70" />
      ))}
      <text x={16} y={clef === "treble" ? 96 : 84} fontSize={clef === "treble" ? 58 : 40} className="fill-tclas-plum font-display">
        {clef === "treble" ? "𝄞" : "𝄢"}
      </text>

      {notes.map((note, i) => {
        const pos = staffPosition(note, clef);
        const cy = 100 - pos * 6;
        const cx = LEFT_MARGIN + i * NOTE_SPACING;
        const ledgers = needsLedgerLines(pos);
        const accidental = accidentalSymbol(note);
        const state = correctness?.[i] ?? "pending";
        const color = state === "correct" ? "#6f8a6e" : state === "wrong" ? "#c65b6c" : "#241a2e";
        const isActive = activeIndex === i;

        return (
          <g key={i}>
            {ledgers.map((lp) => (
              <line key={lp} x1={cx - 14} y1={100 - lp * 6} x2={cx + 14} y2={100 - lp * 6} stroke="currentColor" strokeWidth={1.5} className="text-tclas-ink/70" />
            ))}
            {isActive && <circle cx={cx} cy={cy} r={13} fill="#d4a94c" opacity={0.35} />}
            {accidental && (
              <text x={cx - 20} y={cy + 6} fontSize={20} fill={color}>
                {accidental}
              </text>
            )}
            <ellipse cx={cx} cy={cy} rx={8.5} ry={6.5} fill={color} transform={`rotate(-15 ${cx} ${cy})`} />
          </g>
        );
      })}
    </svg>
  );
}
