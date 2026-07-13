import type { ReactNode } from "react";
import { Link } from "react-router-dom";

export function LegalLayout({ title, updated, children }: { title: string; updated: string; children: ReactNode }) {
  return (
    <div className="mx-auto max-w-2xl px-4 py-12">
      <Link to="/" className="text-sm font-semibold text-t48-blue hover:text-t48-blue-dark">
        ← Volver al inicio
      </Link>
      <h1 className="mt-4 text-3xl font-extrabold tracking-tight text-t48-ink">{title}</h1>
      <p className="mt-1 text-sm text-slate-400">Última actualización: {updated}</p>
      <div className="prose-legal mt-8 space-y-5 text-sm leading-relaxed text-slate-600">{children}</div>
    </div>
  );
}

export function LegalPlaceholder({ children }: { children: ReactNode }) {
  return <mark className="rounded bg-amber-100 px-1 py-0.5 font-medium text-amber-800">{children}</mark>;
}
