import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function NotFound() {
  const { user } = useAuth();

  return (
    <div className="mx-auto max-w-md px-4 py-24 text-center">
      <p className="text-sm font-bold uppercase tracking-wide text-t48-blue">Error 404</p>
      <h1 className="mt-2 text-3xl font-extrabold tracking-tight text-t48-ink">Esta página no existe</h1>
      <p className="mt-3 text-slate-500">Puede que el enlace esté roto o que la página se haya movido.</p>
      <Link
        to={user ? "/dashboard" : "/"}
        className="mt-6 inline-block rounded-md bg-t48-blue px-5 py-2.5 font-semibold text-white transition-colors hover:bg-t48-blue-dark"
      >
        {user ? "Ir a mi panel" : "Volver al inicio"}
      </Link>
    </div>
  );
}
