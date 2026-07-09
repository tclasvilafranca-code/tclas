import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../lib/api";
import type { CurriculumTree } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import { PathMap } from "../components/PathMap";
import { PieceDetailModal } from "../components/PieceDetailModal";

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

      {!tree && <p className="text-center mt-16 text-tclas-ink/50">Cargando tu camino musical...</p>}

      {tree && tree.pieces.length === 0 && (
        <p className="text-center text-tclas-ink/50 mt-16">Todavía no tienes piezas asignadas. ¡Pronto tu profesor/a añadirá tu repertorio!</p>
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
