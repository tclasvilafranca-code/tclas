import { NavLink } from "react-router-dom";
import { IconHome, IconPath, IconPiano, IconProfile } from "./icons";

const TABS = [
  { to: "/app", label: "Inicio", Icon: IconHome, end: true },
  { to: "/app/aprender", label: "Aprender", Icon: IconPath, end: false },
  { to: "/app/practicar", label: "Practicar", Icon: IconPiano, end: false },
  { to: "/app/perfil", label: "Perfil", Icon: IconProfile, end: false },
];

// Barra de navegacion inferior persistente (estilo Duolingo): siempre visible
// para las 4 secciones principales del alumno, para que nunca se sienta
// "atrapado" dentro de una pantalla sin saber como volver.
export function BottomNav() {
  return (
    <nav
      className="fixed bottom-0 inset-x-0 z-20 bg-tclas-cream/95 backdrop-blur border-t border-tclas-ink/10 pb-[env(safe-area-inset-bottom)]"
      aria-label="Navegación principal"
    >
      <div className="max-w-md mx-auto grid grid-cols-4">
        {TABS.map((tab) => (
          <NavLink
            key={tab.to}
            to={tab.to}
            end={tab.end}
            className={({ isActive }) =>
              `flex flex-col items-center gap-0.5 py-2.5 text-2xs font-semibold transition-colors ${
                isActive ? "text-tclas-plum" : "text-tclas-ink/40 hover:text-tclas-ink/60"
              }`
            }
          >
            {({ isActive }) => (
              <>
                <tab.Icon className={`w-6 h-6 transition-transform ${isActive ? "scale-110" : ""}`} />
                {tab.label}
              </>
            )}
          </NavLink>
        ))}
      </div>
    </nav>
  );
}
