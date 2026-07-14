import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api, ApiError } from "../lib/api";
import type { CategoryStat } from "../lib/api";

function levelFromAccuracy(accuracy: number | null): { label: string; color: string; bar: string } {
  if (accuracy === null) return { label: "Sin practicar", color: "text-slate-400", bar: "bg-slate-200" };
  if (accuracy >= 80) return { label: "Dominado", color: "text-t48-green-dark", bar: "bg-t48-green" };
  if (accuracy >= 60) return { label: "Mejorable", color: "text-amber-600", bar: "bg-t48-amber" };
  return { label: "Punto débil", color: "text-t48-red", bar: "bg-t48-red" };
}

export function CategoryStats() {
  const navigate = useNavigate();
  const [categories, setCategories] = useState<CategoryStat[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api
      .categoryStats()
      .then((r) => setCategories(r.categories))
      .catch((err) => setError(err instanceof ApiError ? err.message : "No se pudieron cargar las estadísticas"));
  }, []);

  function practiceCategory(slug: string, name: string) {
    navigate("/learn", { state: { categorySlug: slug, categoryName: name } });
  }

  return (
    <div className="mx-auto max-w-2xl px-4 py-8 sm:py-10">
      <button onClick={() => navigate("/dashboard")} className="text-sm font-semibold text-slate-500 transition-colors hover:text-t48-ink">
        ← Volver al panel
      </button>
      <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-t48-ink">Por categorías</h1>
      <p className="mt-1.5 text-slate-500">
        La precisión que llevas en cada bloque del temario, contando simulacros, repasos y Modo Aprendizaje. Empieza por donde peor vayas.
      </p>

      {error && <p className="mt-6 font-medium text-t48-red">{error}</p>}

      {!categories && !error && (
        <div className="mt-6 flex flex-col gap-2">
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="h-16 animate-pulse rounded-2xl border border-slate-200 bg-white" />
          ))}
        </div>
      )}

      {categories && (
        <div className="mt-6 flex anim-stagger flex-col gap-2.5">
          {categories.map((c) => {
            const level = levelFromAccuracy(c.accuracy);
            return (
              <div key={c.slug} className="card-lift flex items-center gap-4 rounded-2xl border border-slate-200 bg-white p-4">
                <div className="min-w-0 flex-1">
                  <div className="flex items-center justify-between gap-3">
                    <p className="font-bold text-t48-ink">{c.name}</p>
                    <span className={`shrink-0 text-sm font-extrabold tabular-nums ${level.color}`}>
                      {c.accuracy === null ? "—" : `${c.accuracy}%`}
                    </span>
                  </div>
                  <div className="progress-track mt-2 h-1.5 w-full rounded-full">
                    <div className={`h-1.5 rounded-full transition-all duration-500 ${level.bar}`} style={{ width: `${c.accuracy ?? 0}%` }} />
                  </div>
                  <p className="mt-1.5 text-xs text-slate-400">
                    {c.answered > 0 ? `${c.correct}/${c.answered} correctas · ${level.label}` : "Todavía sin practicar"}
                  </p>
                </div>
                <button onClick={() => practiceCategory(c.slug, c.name)} className="btn-secondary shrink-0 px-3.5 py-2 text-sm">
                  Practicar
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
