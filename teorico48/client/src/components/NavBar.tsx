import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { startLicenseCheckout } from "../lib/checkout";
import { Flame, Star } from "./Icons";

export function NavBar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [busy, setBusy] = useState(false);

  async function handleStart() {
    setBusy(true);
    const err = await startLicenseCheckout();
    if (err) setBusy(false);
  }

  return (
    <header className="sticky top-0 z-10 border-b border-slate-200 bg-white/95 backdrop-blur">
      <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-3.5 sm:px-6">
        <Link to="/" className="text-lg font-extrabold tracking-tight text-t48-ink transition-opacity hover:opacity-80">
          Teórico<span className="text-t48-blue">48</span>
        </Link>
        <nav className="flex items-center gap-1 text-sm sm:gap-1.5">
          {user ? (
            <>
              <div className="mr-1 hidden items-center gap-3 border-r border-slate-200 pr-3 text-slate-500 sm:flex">
                {user.currentStreak > 0 && (
                  <span className="flex items-center gap-1.5">
                    <Flame className="h-4 w-4 text-slate-400" />
                    <span className="font-semibold text-t48-ink">{user.currentStreak}</span>
                  </span>
                )}
                <span className="flex items-center gap-1.5">
                  <Star className="h-4 w-4 text-slate-400" filled={false} />
                  <span className="font-semibold text-t48-ink">Nivel {user.level}</span>
                </span>
              </div>
              <Link
                to="/dashboard"
                className="rounded-md px-3 py-1.5 font-medium text-slate-600 transition-colors hover:bg-slate-100 hover:text-t48-ink"
              >
                Panel
              </Link>
              {!user.isPremium && (
                <Link
                  to="/paywall"
                  className="rounded-md border border-amber-200 bg-amber-50 px-3 py-1.5 text-xs font-bold uppercase tracking-wide text-amber-700 transition-colors hover:bg-amber-100"
                >
                  Pack 48h
                </Link>
              )}
              <button
                onClick={() => {
                  logout();
                  navigate("/");
                }}
                className="rounded-md px-3 py-1.5 font-medium text-slate-500 transition-colors hover:bg-slate-100 hover:text-t48-ink"
              >
                Salir
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className="rounded-md px-3 py-1.5 font-medium text-slate-600 transition-colors hover:bg-slate-100 hover:text-t48-ink">
                Entrar
              </Link>
              <button
                onClick={handleStart}
                disabled={busy}
                className="rounded-md bg-t48-blue px-4 py-1.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark disabled:opacity-60"
              >
                {busy ? "Un momento..." : "Empieza ahora"}
              </button>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
