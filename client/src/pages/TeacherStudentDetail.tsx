import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../lib/api";
import type { CurriculumTree, StudentProfile, PieceLibraryItem, StudentSummary, AgeGroup, LessonStatus, PhaseStats, PracticeStats, Message } from "../lib/api";
import { PHASE_LABEL, PHASE_ORDER } from "../lib/phases";
import { IconFlame, IconClock, IconTarget, IconChat } from "../components/icons";
import { MessageThread } from "../components/MessageThread";

interface StudentDetailResponse {
  id: string;
  name: string;
  username: string | null;
  profile: StudentProfile;
  curriculum: CurriculumTree;
  badges: { code: string; name: string; icon: string; earnedAt: string }[];
  phaseStats: PhaseStats;
  practiceStats: PracticeStats;
}

const DAY_LETTERS = ["D", "L", "M", "X", "J", "V", "S"];

function formatMinutes(total: number): string {
  if (total < 60) return `${total} min`;
  const h = Math.floor(total / 60);
  const m = total % 60;
  return m === 0 ? `${h} h` : `${h} h ${m} min`;
}

interface SelectedPiece {
  piece: PieceLibraryItem;
  durationWeeks: number;
  teacherNote: string;
}

const AGE_FILTER_LABEL: Record<"ALL" | AgeGroup, string> = {
  ALL: "Todos",
  KIDS: "Kids",
  TEENS: "Junior",
  ADULTS: "Adultos",
};

function todayISO(): string {
  return new Date().toISOString().slice(0, 10);
}

const WEEK_STATUS_LABEL: Record<LessonStatus, { label: string; className: string }> = {
  COMPLETED: { label: "✅ Completada", className: "text-tclas-sage" },
  AVAILABLE: { label: "▶ Disponible, aun no hecha", className: "text-tclas-gold" },
  SCHEDULED: { label: "📅 Programada", className: "text-tclas-ink/40" },
  LOCKED: { label: "🔒 Bloqueada", className: "text-tclas-ink/30" },
};

function isOverdue(status: LessonStatus, scheduledDate: string): boolean {
  if (status !== "AVAILABLE") return false;
  const days = (Date.now() - new Date(scheduledDate).getTime()) / 86400000;
  return days > 7;
}

function formatShortDate(iso: string): string {
  return new Date(iso).toLocaleDateString("es-ES", { day: "numeric", month: "short" });
}

function suggestedNextDate(pieces: CurriculumTree["pieces"]): string {
  if (pieces.length === 0) return todayISO();
  const maxEnd = Math.max(...pieces.map((p) => new Date(p.startDate).getTime() + p.durationWeeks * 7 * 86400000));
  return new Date(maxEnd).toISOString().slice(0, 10);
}

export function TeacherStudentDetail() {
  const { id } = useParams<{ id: string }>();
  const [data, setData] = useState<StudentDetailResponse | null>(null);
  const [pieces, setPieces] = useState<PieceLibraryItem[] | null>(null);
  const [allStudents, setAllStudents] = useState<StudentSummary[] | null>(null);

  // Formulario "anadir una pieza" (rapido, ya existente)
  const [selectedPiece, setSelectedPiece] = useState("");
  const [startDate, setStartDate] = useState(todayISO());
  const [durationWeeks, setDurationWeeks] = useState<number | "">("");
  const [teacherNote, setTeacherNote] = useState("");
  const [saving, setSaving] = useState(false);

  // Constructor de repertorio (multiple piezas de golpe)
  const [ageFilter, setAgeFilter] = useState<"ALL" | AgeGroup>("ALL");
  const [selected, setSelected] = useState<SelectedPiece[]>([]);
  const [bulkStartDate, setBulkStartDate] = useState(todayISO());
  const [bulkSaving, setBulkSaving] = useState(false);

  // Duplicar repertorio de otro alumno
  const [duplicateFrom, setDuplicateFrom] = useState("");
  const [duplicateStartDate, setDuplicateStartDate] = useState(todayISO());
  const [duplicating, setDuplicating] = useState(false);

  // Mensajeria con este alumno
  const [messages, setMessages] = useState<Message[] | null>(null);

  function load() {
    if (!id) return;
    api.get<StudentDetailResponse>(`/teacher/students/${id}`).then((d) => {
      setData(d);
      setBulkStartDate(suggestedNextDate(d.curriculum.pieces));
    });
  }
  useEffect(load, [id]);
  useEffect(() => {
    api.get<PieceLibraryItem[]>("/teacher/pieces").then(setPieces);
    api.get<StudentSummary[]>("/teacher/students").then(setAllStudents);
  }, []);
  useEffect(() => {
    if (!id) return;
    setMessages(null);
    api.get<{ messages: Message[] }>(`/teacher/students/${id}/messages`).then((r) => setMessages(r.messages));
  }, [id]);

  async function sendMessage(body: string) {
    if (!id) return;
    const message = await api.post<Message>(`/teacher/students/${id}/messages`, { body });
    setMessages((prev) => [...(prev ?? []), message]);
  }

  const assignedPieceIds = new Set(data?.curriculum.pieces.map((p) => p.piece.id));
  const selectedIds = new Set(selected.map((s) => s.piece.id));
  const availablePieces = pieces?.filter((p) => !assignedPieceIds.has(p.id)) ?? [];
  const pickerPieces = availablePieces.filter((p) => (ageFilter === "ALL" ? true : p.ageGroup === ageFilter) && !selectedIds.has(p.id));

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

  function addToSelection(piece: PieceLibraryItem) {
    setSelected((s) => [...s, { piece, durationWeeks: piece.defaultWeeks, teacherNote: "" }]);
  }
  function removeFromSelection(idx: number) {
    setSelected((s) => s.filter((_, i) => i !== idx));
  }
  function moveSelection(idx: number, dir: -1 | 1) {
    setSelected((s) => {
      const copy = [...s];
      const target = idx + dir;
      if (target < 0 || target >= copy.length) return s;
      [copy[idx], copy[target]] = [copy[target], copy[idx]];
      return copy;
    });
  }
  function updateSelection(idx: number, patch: Partial<SelectedPiece>) {
    setSelected((s) => s.map((item, i) => (i === idx ? { ...item, ...patch } : item)));
  }

  async function submitBuilder() {
    if (!id || selected.length === 0) return;
    setBulkSaving(true);
    try {
      await api.post(`/teacher/students/${id}/repertoire/bulk`, {
        startDate: new Date(bulkStartDate).toISOString(),
        items: selected.map((s) => ({ pieceId: s.piece.id, durationWeeks: s.durationWeeks, teacherNote: s.teacherNote })),
      });
      setSelected([]);
      load();
    } finally {
      setBulkSaving(false);
    }
  }

  async function submitDuplicate() {
    if (!id || !duplicateFrom) return;
    const sourceName = allStudents?.find((s) => s.id === duplicateFrom)?.name ?? "ese alumno";
    if (!confirm(`¿Copiar todo el repertorio de ${sourceName} para ${data?.name}? Se añadira a partir del ${duplicateStartDate}.`)) return;
    setDuplicating(true);
    try {
      await api.post(`/teacher/students/${id}/repertoire/duplicate`, {
        fromStudentId: duplicateFrom,
        startDate: new Date(duplicateStartDate).toISOString(),
      });
      setDuplicateFrom("");
      load();
    } finally {
      setDuplicating(false);
    }
  }

  if (!data) return <p className="text-center mt-16 text-tclas-ink/50">Cargando...</p>;

  const otherStudents = allStudents?.filter((s) => s.id !== id && s.piecesAssigned > 0) ?? [];

  const weeklyActivity = data.curriculum.pieces
    .flatMap((entry) => entry.lessons.map((lesson) => ({ ...lesson, pieceTitle: entry.piece.title, pieceIcon: entry.piece.iconEmoji })))
    .sort((a, b) => a.weekNumber - b.weekNumber);
  const overdueCount = weeklyActivity.filter((w) => isOverdue(w.status, w.scheduledDate)).length;

  return (
    <div className="min-h-screen">
      <header className="px-4 py-4 flex items-center gap-4 border-b border-tclas-ink/10">
        <Link to="/teacher" className="text-tclas-ink/50 hover:text-tclas-ink">
          ← Alumnos
        </Link>
        <h1 className="font-display text-xl">{data.name}</h1>
        {data.username && <span className="text-xs text-tclas-ink/40 font-mono">usuario: {data.username}</span>}
      </header>

      <main className="max-w-3xl mx-auto px-4 py-8 grid grid-cols-1 gap-8">
        <section className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 flex flex-wrap gap-6">
          <div>
            <p className="text-xs text-tclas-ink/50">XP total</p>
            <p className="font-display text-2xl text-tclas-plum">{data.profile.xpTotal}</p>
          </div>
          <div>
            <p className="text-xs text-tclas-ink/50">Racha actual · récord</p>
            <p className="font-display text-2xl flex items-center gap-1.5">
              <IconFlame className="w-5 h-5 text-tclas-gold-shadow" /> {data.profile.streakCurrent} <span className="text-tclas-ink/30 text-lg">· {data.profile.streakLongest}</span>
            </p>
          </div>
          <div>
            <p className="text-xs text-tclas-ink/50">Practicado (total)</p>
            <p className="font-display text-2xl">{formatMinutes(data.practiceStats.totalMinutes)}</p>
          </div>
          <div>
            <p className="text-xs text-tclas-ink/50">Piezas terminadas</p>
            <p className="font-semibold text-2xl font-display">{data.practiceStats.piecesCompleted}</p>
          </div>
          <div>
            <p className="text-xs text-tclas-ink/50">Insignias</p>
            <p className="text-xl">{data.badges.map((b) => b.icon).join(" ") || "—"}</p>
          </div>
        </section>

        <section>
          <h2 className="font-display text-xl mb-1 flex items-center gap-2">
            <IconClock className="w-5 h-5 text-tclas-ink/40" /> Minutos practicados esta semana
          </h2>
          <p className="text-xs text-tclas-ink/50 mb-3 flex items-center gap-1.5">
            <IconTarget className="w-3.5 h-3.5" /> Objetivo diario de {data.name}: {data.profile.dailyGoalMinutes} min
          </p>
          <div className="bg-white/70 border border-tclas-ink/10 rounded-xl p-4">
            {(() => {
              const maxMinutes = Math.max(1, ...data.practiceStats.last7Days.map((d) => d.minutes));
              return (
                <div className="flex items-end justify-between gap-2 h-24">
                  {data.practiceStats.last7Days.map((d) => {
                    const date = new Date(d.date + "T00:00:00");
                    const reachedGoal = d.minutes >= data.profile.dailyGoalMinutes;
                    const pct = d.minutes === 0 ? 0 : Math.max(8, (d.minutes / maxMinutes) * 100);
                    return (
                      <div key={d.date} className="flex-1 flex flex-col items-center justify-end gap-1.5 h-full">
                        <span className="text-2xs text-tclas-ink/40 tabular-nums">{d.minutes > 0 ? d.minutes : ""}</span>
                        <div className="w-full rounded-t-md bg-tclas-plum/15 flex items-end" style={{ height: "100%" }}>
                          <div
                            className={`w-full rounded-t-md ${reachedGoal ? "bg-tclas-sage" : d.minutes > 0 ? "bg-tclas-gold" : "bg-transparent"}`}
                            style={{ height: `${pct}%`, transition: "height 300ms ease" }}
                          />
                        </div>
                        <span className="text-2xs font-semibold text-tclas-ink/50">{DAY_LETTERS[date.getDay()]}</span>
                      </div>
                    );
                  })}
                </div>
              );
            })()}
          </div>
        </section>

        <section>
          <h2 className="font-display text-xl mb-1 flex items-center gap-2">
            <IconChat className="w-5 h-5 text-tclas-ink/40" /> Mensajes con {data.name}
          </h2>
          <p className="text-xs text-tclas-ink/50 mb-3">Escríbele directamente aquí: comentarios sobre su práctica, ánimos, o lo que necesite.</p>
          <MessageThread messages={messages} otherName={data.name} onSend={sendMessage} />
        </section>

        <section>
          <h2 className="font-display text-xl mb-1">Rendimiento por bloque</h2>
          <p className="text-xs text-tclas-ink/50 mb-3">Porcentaje de acierto acumulado en cada tipo de bloque de la sesion, para ver donde flaquea {data.name}.</p>
          <div className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 grid grid-cols-1 gap-3">
            {PHASE_ORDER.every((p) => !data.phaseStats[p]?.total) ? (
              <p className="text-tclas-ink/50 text-sm">Aun no hay suficientes ejercicios respondidos.</p>
            ) : (
              PHASE_ORDER.map((phase) => {
                const stat = data.phaseStats[phase];
                if (!stat || stat.total === 0) return null;
                const pct = Math.round((stat.correct / stat.total) * 100);
                const barColor = pct >= 80 ? "bg-tclas-sage" : pct >= 55 ? "bg-tclas-gold" : "bg-tclas-rose";
                return (
                  <div key={phase}>
                    <div className="flex items-center justify-between text-xs mb-1">
                      <span className="font-semibold">{PHASE_LABEL[phase].label}</span>
                      <span className="text-tclas-ink/50">
                        {pct}% ({stat.correct}/{stat.total})
                      </span>
                    </div>
                    <div className="h-2.5 bg-tclas-ink/10 rounded-full overflow-hidden">
                      <div className={`h-full ${barColor}`} style={{ width: `${pct}%` }} />
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </section>

        <section>
          <h2 className="font-display text-xl mb-3">Repertorio del curso</h2>
          <div className="grid grid-cols-1 gap-2">
            {data.curriculum.pieces.length === 0 && <p className="text-tclas-ink/50 text-sm">Aun no tiene piezas asignadas.</p>}
            {data.curriculum.pieces.map((entry) => {
              const completedLessons = entry.lessons.filter((l) => l.status === "COMPLETED").length;
              return (
                <div key={entry.id} className="bg-white/60 border border-tclas-ink/10 rounded-lg p-3 flex items-center gap-3">
                  <span className="text-2xl shrink-0">{entry.piece.iconEmoji}</span>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-semibold truncate">{entry.piece.title}</p>
                    <p className="text-xs text-tclas-ink/50">
                      {new Date(entry.startDate).toLocaleDateString()} · {entry.durationWeeks} semanas · {completedLessons}/{entry.lessons.length} lecciones ·{" "}
                      <span className={entry.status === "COMPLETED" ? "text-tclas-sage" : entry.status === "ACTIVE" ? "text-tclas-gold" : ""}>{entry.status}</span>
                    </p>
                  </div>
                  <button onClick={() => removePiece(entry.id)} className="text-xs text-tclas-rose hover:underline shrink-0">
                    Quitar
                  </button>
                </div>
              );
            })}
          </div>
        </section>

        <section>
          <div className="flex items-center justify-between mb-1">
            <h2 className="font-display text-xl">Actividad semana a semana</h2>
            {overdueCount > 0 && <span className="text-xs font-semibold text-tclas-rose">⚠️ {overdueCount} semana(s) atrasada(s)</span>}
          </div>
          <p className="text-xs text-tclas-ink/50 mb-3">Aqui ves si {data.name} va haciendo su sesion cada semana, pieza por pieza.</p>
          {weeklyActivity.length === 0 ? (
            <p className="text-tclas-ink/50 text-sm">Aun no tiene semanas asignadas.</p>
          ) : (
            <div className="bg-white/70 border border-tclas-ink/10 rounded-xl divide-y divide-tclas-ink/5 max-h-80 overflow-y-auto">
              {weeklyActivity.map((w) => {
                const overdue = isOverdue(w.status, w.scheduledDate);
                const status = overdue ? { label: "⚠️ Atrasada, sin hacer", className: "text-tclas-rose font-semibold" } : WEEK_STATUS_LABEL[w.status];
                return (
                  <div key={w.id} className="flex items-center gap-3 px-4 py-2.5 text-sm">
                    <span className="text-xs text-tclas-ink/40 w-16 shrink-0">Sem. {w.weekNumber}</span>
                    <span className="text-lg">{w.pieceIcon}</span>
                    <span className="flex-1 min-w-0 truncate">{w.pieceTitle}</span>
                    <span className="text-xs text-tclas-ink/40 hidden sm:inline">{formatShortDate(w.scheduledDate)}</span>
                    {w.status === "COMPLETED" && (
                      <span className="text-xs whitespace-nowrap" title="Puntuacion de precision (0-1000)">
                        {"★".repeat(w.stars)} <span className="text-tclas-ink/40">{w.precisionScore}</span>
                      </span>
                    )}
                    <span className={`text-xs whitespace-nowrap ${status.className}`}>{status.label}</span>
                  </div>
                );
              })}
            </div>
          )}
        </section>

        <section>
          <h2 className="font-display text-xl mb-1">Constructor de repertorio</h2>
          <p className="text-xs text-tclas-ink/50 mb-3">Elige varias piezas de la biblioteca, en el orden que quieras (puedes mezclar Kids, Junior y Adultos), y añádelas todas de golpe. Las lecciones se generan solas.</p>

          <div className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 grid grid-cols-1 gap-4">
            <div className="flex flex-wrap gap-2">
              {(["ALL", "KIDS", "TEENS", "ADULTS"] as const).map((f) => (
                <button
                  key={f}
                  onClick={() => setAgeFilter(f)}
                  className={`text-xs font-semibold rounded-full px-3 py-1.5 border ${ageFilter === f ? "bg-tclas-plum text-tclas-cream border-tclas-plum" : "border-tclas-ink/20 text-tclas-ink/60"}`}
                >
                  {AGE_FILTER_LABEL[f]}
                </button>
              ))}
            </div>

            <div className="grid sm:grid-cols-2 gap-2 max-h-64 overflow-y-auto pr-1">
              {pickerPieces.map((p) => (
                <button
                  key={p.id}
                  onClick={() => addToSelection(p)}
                  className="text-left bg-tclas-cream/60 hover:bg-tclas-gold/10 border border-tclas-ink/10 rounded-lg px-3 py-2 flex items-center gap-2"
                >
                  <span className="text-xl">{p.iconEmoji}</span>
                  <span className="flex-1 min-w-0">
                    <span className="block text-sm font-semibold truncate">{p.title}</span>
                    <span className="block text-2xs text-tclas-ink/50">
                      {AGE_FILTER_LABEL[p.ageGroup]} · {p.defaultWeeks} sem.{p.seasonalTag ? ` · 🎄` : ""}
                    </span>
                  </span>
                  <span className="text-tclas-plum text-lg leading-none">+</span>
                </button>
              ))}
              {pickerPieces.length === 0 && <p className="text-xs text-tclas-ink/40 col-span-2">No hay mas piezas disponibles con este filtro.</p>}
            </div>

            {selected.length > 0 && (
              <div className="grid grid-cols-1 gap-2 border-t border-tclas-ink/10 pt-4">
                <p className="text-xs font-semibold text-tclas-ink/60">Repertorio a añadir, en orden ({selected.length}):</p>
                {selected.map((s, idx) => (
                  <div key={`${s.piece.id}-${idx}`} className="flex items-center gap-2 bg-tclas-plum/5 rounded-lg px-3 py-2">
                    <span className="text-xs text-tclas-ink/40 w-5 text-center">{idx + 1}</span>
                    <span className="text-lg">{s.piece.iconEmoji}</span>
                    <span className="flex-1 min-w-0 text-sm font-medium truncate">{s.piece.title}</span>
                    <input
                      type="number"
                      min={1}
                      max={12}
                      value={s.durationWeeks}
                      onChange={(e) => updateSelection(idx, { durationWeeks: parseInt(e.target.value, 10) || 1 })}
                      className="w-14 border border-tclas-ink/20 rounded px-1 py-1 text-xs text-center"
                      title="Semanas"
                    />
                    <span className="text-2xs text-tclas-ink/40">sem.</span>
                    <button onClick={() => moveSelection(idx, -1)} disabled={idx === 0} className="text-tclas-ink/40 hover:text-tclas-ink disabled:opacity-20 px-1">
                      ↑
                    </button>
                    <button onClick={() => moveSelection(idx, 1)} disabled={idx === selected.length - 1} className="text-tclas-ink/40 hover:text-tclas-ink disabled:opacity-20 px-1">
                      ↓
                    </button>
                    <button onClick={() => removeFromSelection(idx)} className="text-tclas-rose text-xs hover:underline px-1">
                      Quitar
                    </button>
                  </div>
                ))}

                <label className="text-sm font-semibold mt-2">
                  Fecha de inicio del repertorio
                  <input type="date" value={bulkStartDate} onChange={(e) => setBulkStartDate(e.target.value)} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1" />
                </label>

                <button
                  onClick={submitBuilder}
                  disabled={bulkSaving}
                  className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50"
                >
                  {bulkSaving ? "Añadiendo..." : `Añadir estas ${selected.length} piezas al repertorio`}
                </button>
              </div>
            )}
          </div>
        </section>

        {otherStudents.length > 0 && (
          <section>
            <h2 className="font-display text-xl mb-1">Duplicar repertorio de otro alumno</h2>
            <p className="text-xs text-tclas-ink/50 mb-3">Copia todas las piezas (y sus lecciones) de un alumno ya creado, como punto de partida para este.</p>
            <div className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 grid grid-cols-1 gap-3 sm:flex sm:items-end sm:gap-3">
              <label className="text-sm font-semibold flex-1">
                Copiar de
                <select value={duplicateFrom} onChange={(e) => setDuplicateFrom(e.target.value)} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1">
                  <option value="">— Elige un alumno —</option>
                  {otherStudents.map((s) => (
                    <option key={s.id} value={s.id}>
                      {s.name} ({s.piecesAssigned} piezas)
                    </option>
                  ))}
                </select>
              </label>
              <label className="text-sm font-semibold">
                Fecha de inicio
                <input type="date" value={duplicateStartDate} onChange={(e) => setDuplicateStartDate(e.target.value)} className="block border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1" />
              </label>
              <button
                onClick={submitDuplicate}
                disabled={!duplicateFrom || duplicating}
                className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 px-4 font-semibold hover:bg-tclas-plum-light disabled:opacity-50 whitespace-nowrap"
              >
                {duplicating ? "Copiando..." : "Duplicar repertorio"}
              </button>
            </div>
          </section>
        )}

        <section>
          <h2 className="font-display text-xl mb-3">Añadir una pieza suelta</h2>
          <form onSubmit={assignPiece} className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 grid grid-cols-1 gap-3">
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
              {saving ? "Añadiendo..." : "Añadir al repertorio"}
            </button>
          </form>
        </section>
      </main>
    </div>
  );
}
