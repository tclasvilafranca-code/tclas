import { useMemo } from "react";
import type { PieceDetail } from "../lib/api";
import { StaffView } from "./StaffView";
import { PianoKeyboard } from "./PianoKeyboard";
import { MascotBubble } from "./MascotBubble";
import { ListenButton } from "./ListenButton";
import { pieceIntroMessage } from "../lib/misol";

interface Props {
  piece: PieceDetail;
  showIntro?: boolean;
}

function chunk<T>(arr: T[], size: number): T[][] {
  const out: T[][] = [];
  for (let i = 0; i < arr.length; i += size) out.push(arr.slice(i, i + size));
  return out;
}

// Contenido completo de una pieza: partitura, info, tips y piano libre para
// probarla. Se usa tanto dentro del modal de Aprender como en la pantalla
// de Practicar (a pantalla completa, sin chrome de modal).
export function PieceDetailContent({ piece, showIntro = true }: Props) {
  const intro = useMemo(() => pieceIntroMessage(piece.title), [piece.id]);

  return (
    <div className="grid grid-cols-1 gap-6">
      {showIntro && <MascotBubble message={intro} mood="cheer" size={44} />}

      <section>
        <div className="flex items-center justify-between mb-2">
          <h3 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40">Partitura completa</h3>
          <ListenButton notes={piece.content.melody} rhythm={piece.content.melodyRhythm} label="Escuchar la pieza" />
        </div>
        <div className="bg-white/70 rounded-xl border border-tclas-ink/10 p-3 sm:p-4 grid gap-1 overflow-x-auto">
          {chunk(piece.content.melody, 8).map((row, i) => (
            <StaffView key={i} clef={piece.content.clef === "bass" ? "bass" : "treble"} notes={row} />
          ))}
        </div>
        {piece.content.bass && piece.content.clef === "grand" && (
          <div className="bg-white/70 rounded-xl border border-tclas-ink/10 p-3 sm:p-4 grid gap-1 mt-2 overflow-x-auto">
            <p className="text-[10px] uppercase tracking-wide text-tclas-ink/30 mb-1">Mano izquierda</p>
            {chunk(piece.content.bass, 8).map((row, i) => (
              <StaffView key={i} clef="bass" notes={row} />
            ))}
          </div>
        )}
        {piece.content.isDuet && piece.content.duetPart && (
          <div className="bg-tclas-plum/5 rounded-xl border border-tclas-plum/20 p-3 sm:p-4 grid gap-1 mt-2 overflow-x-auto">
            <p className="text-[10px] uppercase tracking-wide text-tclas-plum/50 mb-1">🎹 Parte de tu profesora o familia (dúo)</p>
            {chunk(piece.content.duetPart, 8).map((row, i) => (
              <StaffView key={i} clef="bass" notes={row} />
            ))}
          </div>
        )}
        {piece.content.lyricsHook && <p className="text-sm italic text-tclas-ink/60 mt-2 text-center">"{piece.content.lyricsHook}"</p>}
      </section>

      {piece.aboutText && (
        <section>
          <h3 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2">Sobre esta pieza</h3>
          <p className="text-sm leading-relaxed text-tclas-ink/80">{piece.aboutText}</p>
        </section>
      )}

      {piece.tips && (
        <section>
          <h3 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2">🎹 Tips para tocarla</h3>
          <p className="text-sm leading-relaxed text-tclas-ink/80 bg-tclas-gold/10 border border-tclas-gold/30 rounded-lg p-3">{piece.tips}</p>
        </section>
      )}

      <section>
        <h3 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2">Pruébala libremente</h3>
        <PianoKeyboard highlightNotes={piece.content.featuredNotes} compact />
      </section>
    </div>
  );
}
