import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../lib/api";
import type { CurriculumTree } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import { GamificationBar } from "../components/GamificationBar";

export function Home() {
  const { me, logout } = useAuth();
  const [tree, setTree] = useState<CurriculumTree | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    api.get<CurriculumTree>("/curriculum").then(setTree);
  }, []);

  if (!me?.studentProfile) return null;

  return (
    <div className="min-h-screen">
      <header className="sticky top-0 bg-tclas-cream/90 backdrop-blur border-b border-tclas-ink/10 px-4 py-3 flex items-center justify-between z-10">
        <div className="font-display text-xl text-tclas-plum">t-clas 🎹</div>
        <GamificationBar profile={me.studentProfile} />
        <button onClick={logout} className="text-sm text-tclas-ink/50 hover:text-tclas-ink">
          Salir
        </button>
      </header>

      {!tree && <p className="text-center mt-16 text-tclas-ink/50">Cargando tu camino musical...</p>}

      {tree && (
        <main className="max-w-2xl mx-auto px-4 py-8">
          <h1 className="font-display text-2xl mb-1">{tree.name}</h1>
          <p className="text-tclas-ink/60 text-sm mb-8">{tree.description}</p>

          {tree.levels.map((level) => (
            <section key={level.id} className="mb-10">
              <div className="flex items-center gap-3 mb-4">
                <span className="text-3xl">{level.iconEmoji}</span>
                <div>
                  <h2 className="font-display text-xl">{level.title}</h2>
                  <p className="text-xs text-tclas-ink/50">{level.description}</p>
                </div>
                {level.completed && <span className="ml-auto text-tclas-sage text-sm font-semibold">Completado ✓</span>}
              </div>

              {level.units.map((unit) => (
                <div key={unit.id} className="mb-6 pl-2 border-l-2 border-tclas-ink/10 ml-4">
                  <h3 className="text-sm font-semibold text-tclas-ink/70 mb-3 pl-4">{unit.title}</h3>
                  <div className="flex flex-wrap gap-4 pl-2">
                    {unit.lessons.map((lesson) => {
                      const locked = lesson.status === "LOCKED";
                      const completed = lesson.status === "COMPLETED";
                      return (
                        <button
                          key={lesson.id}
                          disabled={locked}
                          onClick={() => navigate(`/app/lesson/${lesson.id}`)}
                          title={lesson.title}
                          className={`w-20 h-20 rounded-full flex flex-col items-center justify-center border-2 font-semibold text-xs text-center px-1 transition-transform
                            ${completed ? "bg-tclas-gold border-tclas-gold text-tclas-ink" : locked ? "bg-tclas-ink/5 border-tclas-ink/10 text-tclas-ink/30" : "bg-tclas-plum border-tclas-plum text-tclas-cream hover:scale-105"}`}
                        >
                          {completed ? (
                            <span className="text-lg">{"★".repeat(lesson.stars)}</span>
                          ) : locked ? (
                            <span className="text-lg">🔒</span>
                          ) : (
                            <span className="text-lg">▶</span>
                          )}
                          <span className="leading-tight mt-0.5 line-clamp-2">{lesson.title}</span>
                        </button>
                      );
                    })}
                  </div>
                </div>
              ))}
            </section>
          ))}
        </main>
      )}
    </div>
  );
}
