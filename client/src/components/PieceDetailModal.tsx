import { useEffect, useState } from "react";
import { api } from "../lib/api";
import type { PieceDetail } from "../lib/api";
import { StaffView } from "./StaffView";
import { PianoKeyboard } from "./PianoKeyboard";

interface Props {
  pieceId: string;
  onClose: () => void;
}

export function PieceDetailModal({ pieceId, onClose }: Props) {
  const [piece, setPiece] = useState<PieceDetail | null>(null);

  useEffect(() => {
    setPiece(null);
    api.get<PieceDetail>(`/pieces/${pieceId}`).then(setPiece);
  }, [pieceId]);

  return (
    <div className="fixed inset-0 bg-tclas-ink/40 backdrop-blur-sm z-50 flex items-start sm:items-center justify-center p-3 sm:p-6 overflow-y-auto" onClick={onClose}>
      <div
        className="bg-tclas-cream rounded-2xl w-full max-w-2xl my-6 sm:my-0 shadow-xl border border-tclas-ink/10"
        onClick={(e) => e.stopPropagation()}
      >
        {!piece ? (
          <p className="text-center py-16 text-tclas-ink/50">Cargando partitura...</p>
        ) : (
          <>
            <header className="px-5 sm:px-6 py-5 border-b border-tclas-ink/10 flex items-start gap-3">
              <span className="text-4xl leading-none">{piece.iconEmoji}</span>
              <div className="flex-1 min-w-0">
                <h2 className="font-display text-xl sm:text-2xl leading-tight">{piece.title}</h2>
                <p className="text-sm text-tclas-ink/60">
                  {piece.composer}
                  {piece.arranger ? ` · arr. ${piece.arranger}` : ""}
                </p>
                <div className="flex flex-wrap items-center gap-2 mt-2 text-xs text-tclas-ink/50">
                  <span className="bg-tclas-plum/10 text-tclas-plum rounded-full px-2 py-0.5">{piece.keySignature}</span>
                  <span className="bg-tclas-plum/10 text-tclas-plum rounded-full px-2 py-0.5">{piece.timeSignature}</span>
                  {piece.seasonalTag === "christmas" && <span className="bg-tclas-gold/15 rounded-full px-2 py-0.5">🎄 Navidad</span>}
                </div>
              </div>
              <button onClick={onClose} className="text-tclas-ink/40 hover:text-tclas-ink text-xl leading-none px-1">
                ✕
              </button>
            </header>

            <div className="px-5 sm:px-6 py-5 grid grid-cols-1 gap-6">
              <section>
                <h3 className="text-xs font-semibold uppercase tracking-wide text-tclas-ink/40 mb-2">Partitura (extracto)</h3>
                <div className="bg-white/70 rounded-xl border border-tclas-ink/10 p-3 sm:p-4 overflow-x-auto">
                  <StaffView clef={piece.content.clef === "bass" ? "bass" : "treble"} notes={piece.content.melody} />
                  {piece.content.bass && piece.content.clef === "grand" && (
                    <div className="mt-1">
                      <StaffView clef="bass" notes={piece.content.bass} />
                    </div>
                  )}
                </div>
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
          </>
        )}
      </div>
    </div>
  );
}
