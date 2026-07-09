import { useEffect, useState } from "react";
import { api } from "../lib/api";
import type { CurriculumTree, PieceDetail, RepertoireNode } from "../lib/api";
import { PieceDetailContent } from "../components/PieceDetailContent";
import { MascotBubble } from "../components/MascotBubble";
import { Skeleton } from "../components/Skeleton";
import { IconCheck } from "../components/icons";

function PieceGridSkeleton() {
  return (
    <div className="max-w-md mx-auto grid grid-cols-2 gap-3">
      {Array.from({ length: 4 }).map((_, i) => (
        <div key={i} className="flex flex-col items-center gap-2 bg-white/60 border border-tclas-ink/10 rounded-2xl px-3 py-4">
          <Skeleton className="w-9 h-9 rounded-full" />
          <Skeleton className="h-3 w-20" />
        </div>
      ))}
    </div>
  );
}

function PieceDetailSkeleton() {
  return (
    <div className="max-w-2xl mx-auto flex flex-col gap-3">
      <Skeleton className="h-40 w-full rounded-xl" />
      <Skeleton className="h-40 w-full rounded-xl" />
      <Skeleton className="h-24 w-full rounded-xl mt-3" />
    </div>
  );
}

// Seccion de practica libre: elige cualquier pieza que ya hayas empezado (o
// terminado) y prueba su partitura y su piano sin exigencias ni corazones en
// juego. Antes esto estaba escondido dentro del modal de "ver pieza"; ahora
// es un destino propio de la navegacion, como pide el nuevo enfoque de la app.
export function Practicar() {
  const [tree, setTree] = useState<CurriculumTree | null>(null);
  const [selected, setSelected] = useState<RepertoireNode | null>(null);
  const [piece, setPiece] = useState<PieceDetail | null>(null);

  useEffect(() => {
    api.get<CurriculumTree>("/curriculum").then(setTree);
  }, []);

  useEffect(() => {
    if (!selected) return;
    setPiece(null);
    api.get<PieceDetail>(`/pieces/${selected.piece.id}`).then(setPiece);
  }, [selected?.id]);

  const practicable = tree?.pieces.filter((p) => p.status === "ACTIVE" || p.status === "COMPLETED") ?? [];

  if (selected) {
    return (
      <main className="px-4 py-8">
        <div className="max-w-2xl mx-auto mb-5 flex items-center gap-3">
          <button onClick={() => setSelected(null)} className="text-tclas-ink/50 hover:text-tclas-ink text-sm shrink-0">
            ‹ Volver
          </button>
          <div className="min-w-0">
            <h1 className="font-display text-xl leading-tight truncate">
              {selected.piece.iconEmoji} {selected.piece.title}
            </h1>
          </div>
        </div>
        {!piece ? <PieceDetailSkeleton /> : <div className="max-w-2xl mx-auto"><PieceDetailContent piece={piece} showIntro={false} /></div>}
      </main>
    );
  }

  return (
    <main className="px-4 py-8">
      <div className="max-w-md mx-auto mb-6 text-center">
        <h1 className="font-display text-2xl text-tclas-plum">Practicar</h1>
        <p className="text-sm text-tclas-ink/50">Elige una pieza y tócala libremente, sin corazones ni presión.</p>
      </div>

      {!tree && <PieceGridSkeleton />}

      {tree && practicable.length === 0 && (
        <div className="max-w-sm mx-auto text-center mt-10">
          <MascotBubble
            message="Todavía no tienes ninguna pieza empezada. En cuanto completes tu primera lección aquí podrás practicar libremente."
            mood="encourage"
            align="center"
            className="justify-center text-left"
          />
        </div>
      )}

      {tree && practicable.length > 0 && (
        <div className="max-w-md mx-auto grid grid-cols-2 gap-3">
          {practicable.map((entry) => (
            <button
              key={entry.id}
              onClick={() => setSelected(entry)}
              className="btn-push flex flex-col items-center gap-1.5 bg-white/70 border-2 border-b-4 border-tclas-ink/10 border-b-tclas-ink/15 rounded-2xl px-3 py-4 text-center hover:-translate-y-0.5 transition-transform"
            >
              <span className="text-3xl">{entry.piece.iconEmoji}</span>
              <span className="text-sm font-semibold leading-tight line-clamp-2">{entry.piece.title}</span>
              {entry.status === "COMPLETED" && (
                <span className="flex items-center gap-1 text-2xs text-tclas-sage font-semibold">
                  <IconCheck className="w-3 h-3" /> Completada
                </span>
              )}
            </button>
          ))}
        </div>
      )}
    </main>
  );
}
