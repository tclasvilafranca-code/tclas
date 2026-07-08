import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../lib/api";
import type { CurriculumTree } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import { GamificationBar } from "../components/GamificationBar";
import { PathMap } from "../components/PathMap";
import { PieceDetailModal } from "../components/PieceDetailModal";
import { MascotBubble } from "../components/MascotBubble";
import { greetingMessage } from "../lib/misol";

export function Home() {
  const { me, logout } = useAuth();
  const [tree, setTree] = useState<CurriculumTree | null>(null);
  const [openPieceId, setOpenPieceId] = useState<string | null>(null);
  const navigate = useNavigate();
  const [greeting] = useState(() => greetingMessage(me?.name ?? "", me?.studentProfile?.streakCurrent ?? 0));

  useEffect(() => {
    api.get<CurriculumTree>("/curriculum").then(setTree);
  }, []);

  if (!me?.studentProfile) return null;

  return (
    <div className="min-h-screen">
      <header className="sticky top-0 bg-tclas-cream/90 backdrop-blur border-b border-tclas-ink/10 px-4 py-3 flex items-center justify-between z-10">
        <div className="font-display text-xl text-tclas-plum">t-clas 🎹</div>
        <GamificationBar profile={me.studentProfile} />
        <button onClick={logout} className="text-sm text-tclas-ink/50 hover:text-tclas-ink">
          Salir
        </button>
      </header>

      {!tree && <p className="text-center mt-16 text-tclas-ink/50">Cargando tu camino musical...</p>}

      {tree && (
        <main className="px-4 py-8">
          <MascotBubble message={greeting} mood="cheer" align="center" className="mb-8 text-left" />

          {tree.pieces.length === 0 ? (
            <p className="text-center text-tclas-ink/50 mt-16">Todavia no tienes piezas asignadas. ¡Pronto tu profesor/a anadira tu repertorio!</p>
          ) : (
            <PathMap pieces={tree.pieces} onOpenLesson={(id) => navigate(`/app/lesson/${id}`)} onOpenPiece={setOpenPieceId} />
          )}
        </main>
      )}

      {openPieceId && <PieceDetailModal pieceId={openPieceId} onClose={() => setOpenPieceId(null)} />}
    </div>
  );
}
