import { useEffect, useState } from "react";
import { Outlet, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api } from "../lib/api";
import { GamificationBar } from "./GamificationBar";
import { BottomNav } from "./BottomNav";
import { MessagesModal } from "./MessagesModal";
import { IconChat } from "./icons";

// Envoltorio comun de las 4 secciones principales del alumno (Inicio, Aprender,
// Practicar, Perfil): cabecera con racha/XP/corazones siempre visible arriba,
// contenido de la seccion en medio, navegacion inferior siempre visible abajo.
export function AppShell() {
  const { me, logout } = useAuth();
  const location = useLocation();
  const [showMessages, setShowMessages] = useState(false);
  const [unread, setUnread] = useState(0);

  useEffect(() => {
    api.get<{ count: number }>("/me/messages/unread-count").then((r) => setUnread(r.count));
  }, []);

  if (!me?.studentProfile) return null;

  return (
    <div className="min-h-screen pb-20">
      <header className="sticky top-0 bg-tclas-cream/90 backdrop-blur border-b border-tclas-ink/10 px-4 py-3 flex items-center justify-between gap-2 z-10">
        <div className="font-display text-xl text-tclas-plum shrink-0">t-clas 🎹</div>
        <GamificationBar profile={me.studentProfile} />
        <div className="flex items-center gap-3 shrink-0">
          <button onClick={() => setShowMessages(true)} className="relative text-tclas-ink/50 hover:text-tclas-ink" title="Mensajes">
            <IconChat className="w-5 h-5" />
            {unread > 0 && (
              <span className="absolute -top-1.5 -right-1.5 bg-tclas-rose text-white text-[10px] font-bold rounded-full min-w-[1.1rem] h-[1.1rem] flex items-center justify-center px-0.5">
                {unread}
              </span>
            )}
          </button>
          <button onClick={logout} className="text-sm text-tclas-ink/50 hover:text-tclas-ink">
            Salir
          </button>
        </div>
      </header>

      <div key={location.pathname} className="animate-page-enter">
        <Outlet />
      </div>

      <BottomNav />

      {showMessages && (
        <MessagesModal otherName={me.teacherName ?? "tu profesor/a"} onClose={() => setShowMessages(false)} onRead={() => setUnread(0)} />
      )}
    </div>
  );
}
