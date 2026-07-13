import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function NavBar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  return (
    <header className="sticky top-0 z-10 border-b border-slate-200/70 bg-white/90 backdrop-blur">
      <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-3.5 sm:px-6">
        <Link to="/" className="text-lg font-extrabold tracking-tight text-t48-ink transition-opacity hover:opacity-80">
          Teórico<span className="text-t48-blue">48</span>
        </Link>
        <nav className="flex items-center gap-2 text-sm font-semibold sm:gap-3">
          {user ? (
            <>
              {user.currentStreak > 0 && (
                <span className="hidden items-center gap-1 rounded-full bg-orange-50 px-2.5 py-1 text-orange-600 sm:inline-flex">
                  🔥 {user.currentStreak}
                </span>
              )}
              <span className="hidden items-center gap-1 rounded-full bg-t48-blue/10 px-2.5 py-1 text-t48-blue-dark sm:inline-flex">
                ⭐ Nivel {user.level}
              </span>
              <Link to="/dashboard" className="rounded-full px-3 py-1.5 text-slate-600 transition-colors hover:bg-slate-100 hover:text-t48-ink">
                Panel
              </Link>
              {!user.isPremium && (
                <Link
                  to="/paywall"
                  className="rounded-full bg-t48-amber px-3 py-1.5 text-t48-ink transition-transform hover:scale-105 active:scale-95"
                >
                  Pack 48h
                </Link>
              )}
              <button
                onClick={() => {
                  logout();
                  navigate("/");
                }}
                className="rounded-full px-3 py-1.5 text-slate-500 transition-colors hover:bg-red-50 hover:text-t48-red"
              >
                Salir
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className="rounded-full px-3 py-1.5 text-slate-600 transition-colors hover:bg-slate-100 hover:text-t48-ink">
                Entrar
              </Link>
              <Link
                to="/register"
                className="rounded-full bg-t48-blue px-4 py-1.5 text-white transition-transform hover:scale-105 hover:bg-t48-blue-dark active:scale-95"
              >
                Empieza gratis
              </Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
