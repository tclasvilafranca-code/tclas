import { Link } from "react-router-dom";

export function Footer() {
  return (
    <footer className="mt-auto border-t border-slate-200 py-6">
      <div className="mx-auto flex max-w-4xl flex-col items-center gap-2 px-4 text-xs text-slate-400 sm:flex-row sm:justify-between sm:px-6">
        <span>© {new Date().getFullYear()} Teórico48</span>
        <nav className="flex items-center gap-4">
          <Link to="/legal" className="hover:text-t48-ink">
            Aviso legal
          </Link>
          <Link to="/privacidad" className="hover:text-t48-ink">
            Privacidad
          </Link>
          <Link to="/terminos" className="hover:text-t48-ink">
            Términos de uso
          </Link>
        </nav>
      </div>
    </footer>
  );
}
