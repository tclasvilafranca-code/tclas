import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../lib/api";
import type { StudentSummary } from "../lib/api";
import { useAuth } from "../context/AuthContext";

function timeAgo(dateStr: string | null): string {
  if (!dateStr) return "Sin actividad";
  const diffMs = Date.now() - new Date(dateStr).getTime();
  const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
  if (days <= 0) return "Hoy";
  if (days === 1) return "Ayer";
  return `Hace ${days} dias`;
}

export function TeacherDashboard() {
  const { me, logout } = useAuth();
  const [students, setStudents] = useState<StudentSummary[] | null>(null);

  useEffect(() => {
    api.get<StudentSummary[]>("/teacher/students").then(setStudents);
  }, []);

  return (
    <div className="min-h-screen">
      <header className="px-4 py-4 flex items-center justify-between border-b border-tclas-ink/10">
        <div className="font-display text-xl text-tclas-plum">t-clas · Panel de {me?.name}</div>
        <button onClick={logout} className="text-sm text-tclas-ink/50 hover:text-tclas-ink">
          Salir
        </button>
      </header>

      <main className="max-w-4xl mx-auto px-4 py-8">
        <h1 className="font-display text-2xl mb-1">Tus alumnos</h1>
        <p className="text-tclas-ink/60 text-sm mb-6">Sigue el progreso de cada alumno y enlaza tareas de la app con tus clases presenciales.</p>

        {!students && <p className="text-tclas-ink/50">Cargando...</p>}
        {students && students.length === 0 && <p className="text-tclas-ink/50">Aun no hay alumnos registrados.</p>}

        <div className="grid gap-3">
          {students?.map((s) => {
            const pct = s.totalLessons > 0 ? Math.round((s.completedLessons / s.totalLessons) * 100) : 0;
            return (
              <Link
                key={s.id}
                to={`/teacher/students/${s.id}`}
                className="bg-white/70 border border-tclas-ink/10 rounded-xl p-4 flex items-center gap-4 hover:border-tclas-gold transition-colors"
              >
                <div className="w-12 h-12 rounded-full bg-tclas-plum text-tclas-cream flex items-center justify-center font-display text-lg">
                  {s.name.charAt(0).toUpperCase()}
                </div>
                <div className="flex-1 min-w-0">
                  <p className="font-semibold truncate">{s.name}</p>
                  <p className="text-xs text-tclas-ink/50">
                    {s.trackName ?? "Sin camino asignado"} · {timeAgo(s.lastActivityDate)}
                  </p>
                  {s.totalLessons > 0 && (
                    <div className="h-1.5 bg-tclas-ink/10 rounded-full mt-2 overflow-hidden max-w-xs">
                      <div className="h-full bg-tclas-gold" style={{ width: `${pct}%` }} />
                    </div>
                  )}
                </div>
                <div className="text-right text-sm">
                  <p className="font-semibold text-tclas-plum">{s.xpTotal} XP</p>
                  <p className="text-tclas-ink/50">🔥 {s.streakCurrent}</p>
                </div>
              </Link>
            );
          })}
        </div>
      </main>
    </div>
  );
}
