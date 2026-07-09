import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { Link } from "react-router-dom";
import { api } from "../lib/api";
import type { StudentSummary, AgeGroup, NewStudentCredentials } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import { ChangePasswordModal } from "../components/ChangePasswordModal";
import { SetPinAccessModal } from "../components/SetPinAccessModal";
import { IconGear, IconKey, IconFlame, IconChat, IconCalendarDate } from "../components/icons";

function timeAgo(dateStr: string | null): string {
  if (!dateStr) return "Sin actividad";
  const diffMs = Date.now() - new Date(dateStr).getTime();
  const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
  if (days <= 0) return "Hoy";
  if (days === 1) return "Ayer";
  return `Hace ${days} dias`;
}

function formatNextClass(dateStr: string | null): string | null {
  if (!dateStr) return null;
  const d = new Date(dateStr);
  const days = Math.round((d.setHours(0, 0, 0, 0) - new Date().setHours(0, 0, 0, 0)) / 86400000);
  const dateLabel = d.toLocaleDateString("es-ES", { day: "numeric", month: "short" });
  if (days === 0) return `Hoy (${dateLabel})`;
  if (days === 1) return `Mañana (${dateLabel})`;
  if (days > 1) return dateLabel;
  return `${dateLabel} (pasada)`;
}

const AGE_GROUP_LABEL: Record<AgeGroup, string> = { KIDS: "Kids (6-11)", TEENS: "Junior (12-17)", ADULTS: "Adultos (18+)" };

export function TeacherDashboard() {
  const { me, logout, refresh } = useAuth();
  const [students, setStudents] = useState<StudentSummary[] | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [name, setName] = useState("");
  const [ageGroup, setAgeGroup] = useState<AgeGroup>("KIDS");
  const [saving, setSaving] = useState(false);
  const [newCreds, setNewCreds] = useState<NewStudentCredentials | null>(null);
  const [showChangePassword, setShowChangePassword] = useState(false);
  const [showPinAccess, setShowPinAccess] = useState(false);

  function load() {
    api.get<StudentSummary[]>("/teacher/students").then(setStudents);
  }
  useEffect(load, []);

  async function createStudent(e: FormEvent) {
    e.preventDefault();
    setSaving(true);
    try {
      const creds = await api.post<NewStudentCredentials>("/teacher/students", { name, ageGroup });
      setNewCreds(creds);
      setName("");
      setShowForm(false);
      load();
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="min-h-screen">
      <header className="px-4 py-4 flex items-center justify-between border-b border-tclas-ink/10">
        <div className="font-display text-xl text-tclas-plum">t-clas · Panel de {me?.name}</div>
        <div className="flex items-center gap-3">
          <button onClick={() => setShowPinAccess(true)} className="flex items-center gap-1.5 text-sm text-tclas-ink/50 hover:text-tclas-ink" title="Entrar con usuario y PIN">
            <IconKey className="w-4 h-4" /> {me?.username ? "Usuario y PIN" : "Configurar PIN"}
          </button>
          <button onClick={() => setShowChangePassword(true)} className="flex items-center gap-1.5 text-sm text-tclas-ink/50 hover:text-tclas-ink" title="Cambiar contrasena">
            <IconGear className="w-4 h-4" /> Contraseña
          </button>
          <button onClick={logout} className="text-sm text-tclas-ink/50 hover:text-tclas-ink">
            Salir
          </button>
        </div>
      </header>

      {showChangePassword && <ChangePasswordModal onClose={() => setShowChangePassword(false)} />}
      {showPinAccess && (
        <SetPinAccessModal
          currentUsername={me?.username ?? null}
          onClose={() => setShowPinAccess(false)}
          onSaved={refresh}
        />
      )}

      <main className="max-w-4xl mx-auto px-4 py-8">
        <div className="flex items-center justify-between mb-1">
          <h1 className="font-display text-2xl">Tus alumnos</h1>
          <button onClick={() => setShowForm((v) => !v)} className="bg-tclas-plum text-tclas-cream rounded-full px-4 py-2 text-sm font-semibold hover:bg-tclas-plum-light">
            + Nuevo alumno
          </button>
        </div>
        <p className="text-tclas-ink/60 text-sm mb-6">Crea el acceso de cada alumno y gestiona su repertorio personal.</p>

        {showForm && (
          <form onSubmit={createStudent} className="bg-white/70 border border-tclas-ink/10 rounded-xl p-5 grid grid-cols-1 gap-3 mb-6 max-w-sm">
            <label className="text-sm font-semibold">
              Nombre del alumno/a
              <input required value={name} onChange={(e) => setName(e.target.value)} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1" />
            </label>
            <label className="text-sm font-semibold">
              Grupo
              <select value={ageGroup} onChange={(e) => setAgeGroup(e.target.value as AgeGroup)} className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1">
                <option value="KIDS">Kids (6-11)</option>
                <option value="TEENS">Junior (12-17)</option>
                <option value="ADULTS">Adultos (18+)</option>
              </select>
            </label>
            <button disabled={saving} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50">
              {saving ? "Creando..." : "Crear acceso"}
            </button>
          </form>
        )}

        {newCreds && (
          <div className="bg-tclas-gold/10 border-2 border-tclas-gold/40 rounded-xl p-5 mb-6 max-w-sm">
            <p className="text-sm font-semibold mb-2">¡Acceso creado para {newCreds.name}! Guarda estos datos, no se volveran a mostrar:</p>
            <p className="font-mono text-lg">
              usuario: <b>{newCreds.username}</b>
            </p>
            <p className="font-mono text-lg">
              PIN: <b>{newCreds.pin}</b>
            </p>
            <p className="text-xs text-tclas-ink/50 mt-2">Al entrar por primera vez, le pedirá cambiar este PIN por uno propio.</p>
            <button onClick={() => setNewCreds(null)} className="text-xs text-tclas-ink/50 underline mt-3">
              Cerrar
            </button>
          </div>
        )}

        {!students && <p className="text-tclas-ink/50">Cargando...</p>}
        {students && students.length === 0 && <p className="text-tclas-ink/50">Aun no hay alumnos. Crea el primero con el boton de arriba.</p>}

        <div className="grid grid-cols-1 gap-3">
          {students?.map((s) => {
            const pct = s.totalLessons > 0 ? Math.round((s.completedLessons / s.totalLessons) * 100) : 0;
            return (
              <Link
                key={s.id}
                to={`/teacher/students/${s.id}`}
                className="bg-white/70 border border-tclas-ink/10 rounded-xl p-4 flex items-center gap-4 hover:border-tclas-gold transition-colors"
              >
                <div className="relative shrink-0">
                  <div className="w-12 h-12 rounded-full bg-tclas-plum text-tclas-cream flex items-center justify-center font-display text-lg">
                    {s.name.charAt(0).toUpperCase()}
                  </div>
                  {s.unreadMessages > 0 && (
                    <span className="absolute -top-1 -right-1 bg-tclas-rose text-white rounded-full w-5 h-5 flex items-center justify-center" title="Mensajes sin leer">
                      <IconChat className="w-3 h-3" />
                    </span>
                  )}
                </div>
                <div className="flex-1 min-w-0">
                  <p className="font-semibold truncate">{s.name}</p>
                  <p className="text-xs text-tclas-ink/50">
                    {s.ageGroup ? AGE_GROUP_LABEL[s.ageGroup] : ""} · {s.piecesAssigned} piezas · {timeAgo(s.lastActivityDate)}
                  </p>
                  {formatNextClass(s.nextClassAt) && (
                    <p className="text-2xs text-tclas-plum flex items-center gap-1 mt-0.5">
                      <IconCalendarDate className="w-3 h-3" /> Próxima clase: {formatNextClass(s.nextClassAt)}
                    </p>
                  )}
                  {s.totalLessons > 0 && (
                    <div className="h-1.5 bg-tclas-ink/10 rounded-full mt-2 overflow-hidden max-w-xs">
                      <div className="h-full bg-tclas-gold" style={{ width: `${pct}%` }} />
                    </div>
                  )}
                </div>
                <div className="text-right text-sm shrink-0">
                  <p className="font-semibold text-tclas-plum">{s.xpTotal} XP</p>
                  <p className="text-tclas-ink/50 flex items-center justify-end gap-1">
                    <IconFlame className="w-3.5 h-3.5" /> {s.streakCurrent}
                  </p>
                  <p
                    className={`text-2xs mt-0.5 ${s.weeklyMinutes > 0 ? "text-tclas-sage" : "text-tclas-ink/30"}`}
                    title="Minutos practicados esta semana"
                  >
                    {s.weeklyMinutes} min esta semana
                  </p>
                  <p className="text-2xs text-tclas-ink/40 mt-0.5" title="Retos semanales cumplidos">
                    🎯 {s.challengesCompleted}/{s.challengesTotal} retos
                  </p>
                </div>
              </Link>
            );
          })}
        </div>
      </main>
    </div>
  );
}
