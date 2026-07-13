import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function NavBar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  return (
    <header className="border-b border-slate-200 bg-white">
      <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-3">
        <Link to="/" className="text-lg font-extrabold text-t48-blue-dark">
          Teórico<span className="text-t48-blue">48h</span>
        </Link>
        <nav className="flex items-center gap-4 text-sm font-medium">
          {user ? (
            <>
              <Link to="/dashboard" className="text-slate-600 hover:text-t48-blue">Panel</Link>
              {!user.isPremium && (
                <Link to="/paywall" className="rounded-full bg-t48-amber px-3 py-1.5 text-white">Pack 48h</Link>
              )}
              <button
                onClick={() => {
                  logout();
                  navigate("/");
                }}
                className="text-slate-500 hover:text-t48-red"
              >
                Salir
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className="text-slate-600 hover:text-t48-blue">Entrar</Link>
              <Link to="/register" className="rounded-full bg-t48-blue px-3 py-1.5 text-white">Empezar</Link>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
