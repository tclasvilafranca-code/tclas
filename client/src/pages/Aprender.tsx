import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../lib/api";
import type { CurriculumTree } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import { PathMap } from "../components/PathMap";
import { PieceDetailModal } from "../components/PieceDetailModal";
import { MascotBubble } from "../components/MascotBubble";
import { Skeleton } from "../components/Skeleton";

function PathMapSkeleton() {
  return (
    <div className="max-w-md mx-auto flex flex-col items-center gap-8">
      <div className="w-full max-w-xs flex items-center gap-4 rounded-2xl px-5 py-4 bg-white/60 border border-tclas-ink/10">
        <Skeleton className="w-16 h-16 rounded-full shrink-0" />
        <div className="flex-1 flex flex-col gap-2">
          <Skeleton className="h-4 w-32" />
          <Skeleton className="h-2.5 w-20" />
        </div>
      </div>
      <Skeleton className="w-24 h-24 rounded-full" />
      <Skeleton className="w-24 h-24 rounded-full opacity-60" />
    </div>
  );
}

export function Aprender() {
  const { me } = useAuth();
  const [tree, setTree] = useState<CurriculumTree | null>(null);
  const [openPieceId, setOpenPieceId] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    api.get<CurriculumTree>("/curriculum").then(setTree);
  }, []);

  if (!me?.studentProfile) return null;

  return (
    <main className="px-4 py-8">
      <div className="max-w-md mx-auto mb-6 text-center">
        <h1 className="font-display text-2xl text-tclas-plum">Tu camino musical</h1>
        <p className="text-sm text-tclas-ink/50">Cada pieza es un tramo del camino. Ve paso a paso, semana a semana.</p>
      </div>

      {!tree && <PathMapSkeleton />}

      {tree && tree.pieces.length === 0 && (
        <div className="max-w-sm mx-auto mt-10">
          <MascotBubble
            message="Todavía no tienes piezas asignadas. En cuanto tu profesor/a añada tu repertorio, aparecerá aquí."
            mood="encourage"
            align="center"
            className="justify-center text-left"
          />
        </div>
      )}

      {tree && tree.pieces.length > 0 && (
        <PathMap
          pieces={tree.pieces}
          onOpenLesson={(id) => navigate(`/app/lesson/${id}`)}
          onOpenPiece={setOpenPieceId}
          heartsCurrent={me.studentProfile.heartsCurrent}
          heartsUpdatedAt={me.studentProfile.heartsUpdatedAt}
        />
      )}

      {openPieceId && <PieceDetailModal pieceId={openPieceId} onClose={() => setOpenPieceId(null)} />}
    </main>
  );
}
