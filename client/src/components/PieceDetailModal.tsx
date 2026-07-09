import { useEffect, useState } from "react";
import { api } from "../lib/api";
import type { PieceDetail } from "../lib/api";
import { PieceDetailContent } from "./PieceDetailContent";

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

            <div className="px-5 sm:px-6 py-5">
              <PieceDetailContent piece={piece} />
            </div>
          </>
        )}
      </div>
    </div>
  );
}
