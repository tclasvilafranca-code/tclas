import { Outlet, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { GamificationBar } from "./GamificationBar";
import { BottomNav } from "./BottomNav";

// Envoltorio comun de las 4 secciones principales del alumno (Inicio, Aprender,
// Practicar, Perfil): cabecera con racha/XP/corazones siempre visible arriba,
// contenido de la seccion en medio, navegacion inferior siempre visible abajo.
export function AppShell() {
  const { me, logout } = useAuth();
  const location = useLocation();
  if (!me?.studentProfile) return null;

  return (
    <div className="min-h-screen pb-20">
      <header className="sticky top-0 bg-tclas-cream/90 backdrop-blur border-b border-tclas-ink/10 px-4 py-3 flex items-center justify-between z-10">
        <div className="font-display text-xl text-tclas-plum">t-clas 🎹</div>
        <GamificationBar profile={me.studentProfile} />
        <button onClick={logout} className="text-sm text-tclas-ink/50 hover:text-tclas-ink">
          Salir
        </button>
      </header>

      <div key={location.pathname} className="animate-page-enter">
        <Outlet />
      </div>

      <BottomNav />
    </div>
  );
}
