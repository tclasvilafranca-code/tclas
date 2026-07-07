import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../lib/api";
import type { Assignment, CurriculumTree, StudentProfile } from "../lib/api";

interface StudentDetailResponse {
  id: string;
  name: string;
  email: string;
  profile: StudentProfile;
  curriculum: CurriculumTree | null;
  assignments: Assignment[];
  badges: { code: string; name: string; icon: string; earnedAt: string }[];
}

export function TeacherStudentDetail() {
  const { id } = useParams<{ id: string }>();
  const [data, setData] = useState<StudentDetailResponse | null>(null);
  const [selectedLesson, setSelectedLesson] = useState("");
  const [classDate, setClassDate] = useState(() => new Date().toISOString().slice(0, 10));
  const [note, setNote] = useState("");
  const [saving, setSaving] = useState(false);

  function load() {
    if (!id) return;
    api.get<StudentDetailResponse>(`/teacher/students/${id}`).then(setData);
  }

  useEffect(load, [id]);

  const allLessons = data?.curriculum
    ? data.curriculum.levels.flatMap((l) => l.units.flatMap((u) => u.lessons.map((les) => ({ id: les.id, label: `${l.title} · ${u.title} · ${les.title}` }))))
    : [];

  async function createAssignment(e: FormEvent) {
    e.preventDefault();
    if (!id) return;
    setSaving(true);
    try {
      await api.post("/teacher/assignments", {
        studentId: id,
        lessonId: selectedLesson || undefined,
        classDate: new Date(classDate).toISOString(),
        note,
      });
      setNote("");
      setSelectedLesson("");
      load();
    } finally {
      setSaving(false);
    }
  }

  async function toggleDone(a: Assignment) {
    await api.patch(`/teacher/assignments/${a.id}`, { status: a.status === "DONE" ? "PENDING" : "DONE" });
    load();
  }

  if (!data) return <p className="text-center mt-16 text-tclas-ink/50">Cargando...</p>;

  return (
    <div className="min-h-screen">
      <header className="px-4 py-4 flex items-center gap-4 border-b border-tclas-ink/10">
        <Link to="/teacher" className="text-tclas-ink/50 hover:text-tclas-ink">
          ← Alumnos
        </Link>
        <h1 className="font-display text-xl">{data.name}</h1>
      </header>

      <main className="max-w-3xl mx-auto px-4 py-8 grid gap-8">
        <section className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 flex flex-wrap gap-6">
          <div>
            <p className="text-xs text-tclas-ink/50">XP total</p>
            <p className="font-display text-2xl text-tclas-plum">{data.profile.xpTotal}</p>
          </div>
          <div>
            <p className="text-xs text-tclas-ink/50">Racha actual</p>
            <p className="font-display text-2xl">🔥 {data.profile.streakCurrent}</p>
          </div>
          <div>
            <p className="text-xs text-tclas-ink/50">Camino</p>
            <p className="font-semibold">{data.curriculum?.name ?? "Sin asignar"}</p>
          </div>
          <div>
            <p className="text-xs text-tclas-ink/50">Insignias</p>
            <p className="text-xl">{data.badges.map((b) => b.icon).join(" ") || "—"}</p>
          </div>
        </section>

        {data.curriculum && (
          <section>
            <h2 className="font-display text-xl mb-3">Progreso por nivel</h2>
            <div className="grid gap-2">
              {data.curriculum.levels.map((level) => {
                const totalLessons = level.units.reduce((a, u) => a + u.lessons.length, 0);
                const completed = level.units.reduce((a, u) => a + u.lessons.filter((l) => l.status === "COMPLETED").length, 0);
                const pct = totalLessons > 0 ? Math.round((completed / totalLessons) * 100) : 0;
                return (
                  <div key={level.id} className="bg-white/60 border border-tclas-ink/10 rounded-lg p-3">
                    <div className="flex items-center justify-between text-sm mb-1">
                      <span className="font-semibold">
                        {level.iconEmoji} {level.title}
                      </span>
                      <span className="text-tclas-ink/50">
                        {completed}/{totalLessons}
                      </span>
                    </div>
                    <div className="h-1.5 bg-tclas-ink/10 rounded-full overflow-hidden">
                      <div className="h-full bg-tclas-gold" style={{ width: `${pct}%` }} />
                    </div>
                  </div>
                );
              })}
            </div>
          </section>
        )}

        <section>
          <h2 className="font-display text-xl mb-3">Asignar tarea ligada a una clase</h2>
          <form onSubmit={createAssignment} className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 grid gap-3">
            <label className="text-sm font-semibold">
              Fecha de la clase
              <input type="date" value={classDate} onChange={(e) => setClassDate(e.target.value)} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1" />
            </label>
            <label className="text-sm font-semibold">
              Leccion de la app (opcional)
              <select value={selectedLesson} onChange={(e) => setSelectedLesson(e.target.value)} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1">
                <option value="">— Sin leccion especifica —</option>
                {allLessons.map((l) => (
                  <option key={l.id} value={l.id}>
                    {l.label}
                  </option>
                ))}
              </select>
            </label>
            <label className="text-sm font-semibold">
              Nota para el alumno
              <textarea value={note} onChange={(e) => setNote(e.target.value)} rows={3} placeholder="Ej: Repasa esta leccion antes del jueves y trae dudas sobre..." className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1" />
            </label>
            <button disabled={saving} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50">
              {saving ? "Guardando..." : "Asignar tarea"}
            </button>
          </form>
        </section>

        <section>
          <h2 className="font-display text-xl mb-3">Historial de tareas asignadas</h2>
          <div className="grid gap-2">
            {data.assignments.length === 0 && <p className="text-tclas-ink/50 text-sm">Aun no hay tareas asignadas.</p>}
            {data.assignments.map((a) => (
              <div key={a.id} className="bg-white/60 border border-tclas-ink/10 rounded-lg p-3 flex items-start gap-3">
                <button
                  onClick={() => toggleDone(a)}
                  className={`shrink-0 w-6 h-6 rounded-full border-2 mt-0.5 flex items-center justify-center text-xs ${a.status === "DONE" ? "bg-tclas-sage border-tclas-sage text-white" : "border-tclas-ink/30"}`}
                >
                  {a.status === "DONE" ? "✓" : ""}
                </button>
                <div className="flex-1">
                  <p className="text-xs text-tclas-ink/50">{new Date(a.classDate).toLocaleDateString()}</p>
                  {a.lesson && <p className="text-sm font-semibold">{a.lesson.title}</p>}
                  {a.note && <p className="text-sm text-tclas-ink/70">{a.note}</p>}
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}
