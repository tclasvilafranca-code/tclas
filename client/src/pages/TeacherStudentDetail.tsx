import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../lib/api";
import type { CurriculumTree, StudentProfile, PieceLibraryItem } from "../lib/api";

interface StudentDetailResponse {
  id: string;
  name: string;
  username: string | null;
  profile: StudentProfile;
  curriculum: CurriculumTree;
  badges: { code: string; name: string; icon: string; earnedAt: string }[];
}

function todayISO(): string {
  return new Date().toISOString().slice(0, 10);
}

export function TeacherStudentDetail() {
  const { id } = useParams<{ id: string }>();
  const [data, setData] = useState<StudentDetailResponse | null>(null);
  const [pieces, setPieces] = useState<PieceLibraryItem[] | null>(null);
  const [selectedPiece, setSelectedPiece] = useState("");
  const [startDate, setStartDate] = useState(todayISO());
  const [durationWeeks, setDurationWeeks] = useState<number | "">("");
  const [teacherNote, setTeacherNote] = useState("");
  const [saving, setSaving] = useState(false);

  function load() {
    if (!id) return;
    api.get<StudentDetailResponse>(`/teacher/students/${id}`).then(setData);
  }
  useEffect(load, [id]);
  useEffect(() => {
    api.get<PieceLibraryItem[]>("/teacher/pieces").then(setPieces);
  }, []);

  const assignedPieceIds = new Set(data?.curriculum.pieces.map((p) => p.piece.id));
  const availablePieces = pieces?.filter((p) => !assignedPieceIds.has(p.id)) ?? [];

  async function assignPiece(e: FormEvent) {
    e.preventDefault();
    if (!id || !selectedPiece) return;
    setSaving(true);
    try {
      await api.post(`/teacher/students/${id}/repertoire`, {
        pieceId: selectedPiece,
        startDate: new Date(startDate).toISOString(),
        durationWeeks: durationWeeks === "" ? undefined : durationWeeks,
        teacherNote,
      });
      setSelectedPiece("");
      setTeacherNote("");
      setDurationWeeks("");
      load();
    } finally {
      setSaving(false);
    }
  }

  async function removePiece(entryId: string) {
    if (!id) return;
    if (!confirm("¿Quitar esta pieza del repertorio del alumno? Se perdera su progreso en ella.")) return;
    await api.delete(`/teacher/students/${id}/repertoire/${entryId}`);
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
        {data.username && <span className="text-xs text-tclas-ink/40 font-mono">usuario: {data.username}</span>}
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
            <p className="text-xs text-tclas-ink/50">Piezas en repertorio</p>
            <p className="font-semibold">{data.curriculum.pieces.length}</p>
          </div>
          <div>
            <p className="text-xs text-tclas-ink/50">Insignias</p>
            <p className="text-xl">{data.badges.map((b) => b.icon).join(" ") || "—"}</p>
          </div>
        </section>

        <section>
          <h2 className="font-display text-xl mb-3">Repertorio del curso</h2>
          <div className="grid gap-2">
            {data.curriculum.pieces.length === 0 && <p className="text-tclas-ink/50 text-sm">Aun no tiene piezas asignadas.</p>}
            {data.curriculum.pieces.map((entry) => {
              const completedLessons = entry.lessons.filter((l) => l.status === "COMPLETED").length;
              return (
                <div key={entry.id} className="bg-white/60 border border-tclas-ink/10 rounded-lg p-3 flex items-center gap-3">
                  <span className="text-2xl">{entry.piece.iconEmoji}</span>
                  <div className="flex-1">
                    <p className="text-sm font-semibold">{entry.piece.title}</p>
                    <p className="text-xs text-tclas-ink/50">
                      {new Date(entry.startDate).toLocaleDateString()} · {entry.durationWeeks} semanas · {completedLessons}/{entry.lessons.length} lecciones ·{" "}
                      <span className={entry.status === "COMPLETED" ? "text-tclas-sage" : entry.status === "ACTIVE" ? "text-tclas-gold" : ""}>{entry.status}</span>
                    </p>
                  </div>
                  <button onClick={() => removePiece(entry.id)} className="text-xs text-tclas-rose hover:underline">
                    Quitar
                  </button>
                </div>
              );
            })}
          </div>
        </section>

        <section>
          <h2 className="font-display text-xl mb-3">Anadir pieza al repertorio</h2>
          <form onSubmit={assignPiece} className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 grid gap-3">
            <label className="text-sm font-semibold">
              Pieza
              <select required value={selectedPiece} onChange={(e) => setSelectedPiece(e.target.value)} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1">
                <option value="">— Elige una pieza —</option>
                {availablePieces.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.iconEmoji} {p.title} ({p.defaultWeeks} sem.)
                  </option>
                ))}
              </select>
            </label>
            <div className="grid grid-cols-2 gap-3">
              <label className="text-sm font-semibold">
                Fecha de inicio
                <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1" />
              </label>
              <label className="text-sm font-semibold">
                Semanas (opcional)
                <input
                  type="number"
                  min={1}
                  max={12}
                  placeholder="por defecto"
                  value={durationWeeks}
                  onChange={(e) => setDurationWeeks(e.target.value ? parseInt(e.target.value, 10) : "")}
                  className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1"
                />
              </label>
            </div>
            <label className="text-sm font-semibold">
              Nota para el alumno (opcional)
              <textarea value={teacherNote} onChange={(e) => setTeacherNote(e.target.value)} rows={2} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1" />
            </label>
            <button disabled={saving || !selectedPiece} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50">
              {saving ? "Anadiendo..." : "Anadir al repertorio"}
            </button>
          </form>
        </section>
      </main>
    </div>
  );
}
