import { useState } from "react";
import type { FormEvent } from "react";
import { api } from "../lib/api";

interface Props {
  onClose: () => void;
}

export function ChangePasswordModal({ onClose }: Props) {
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);
  const [done, setDone] = useState(false);

  async function submit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    if (newPassword !== confirmPassword) {
      setError("Las dos contrasenas nuevas no coinciden");
      return;
    }
    setSaving(true);
    try {
      await api.post("/auth/change-password", { currentPassword, newPassword });
      setDone(true);
    } catch (err) {
      setError(err instanceof Error ? err.message : "No se pudo cambiar la contrasena");
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="fixed inset-0 bg-tclas-ink/40 backdrop-blur-sm z-50 flex items-center justify-center p-4" onClick={onClose}>
      <div className="bg-tclas-cream rounded-2xl w-full max-w-sm shadow-xl border border-tclas-ink/10 p-6" onClick={(e) => e.stopPropagation()}>
        <div className="flex items-center justify-between mb-4">
          <h2 className="font-display text-xl">Cambiar contrasena</h2>
          <button onClick={onClose} className="text-tclas-ink/40 hover:text-tclas-ink text-xl leading-none px-1">
            ✕
          </button>
        </div>

        {done ? (
          <div className="text-center py-4">
            <p className="text-tclas-sage font-semibold mb-4">Contrasena actualizada correctamente.</p>
            <button onClick={onClose} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 px-6 font-semibold hover:bg-tclas-plum-light">
              Cerrar
            </button>
          </div>
        ) : (
          <form onSubmit={submit} className="grid grid-cols-1 gap-3">
            <label className="text-sm font-semibold">
              Contrasena actual
              <input
                type="password"
                required
                value={currentPassword}
                onChange={(e) => setCurrentPassword(e.target.value)}
                className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1"
              />
            </label>
            <label className="text-sm font-semibold">
              Nueva contrasena
              <input
                type="password"
                required
                minLength={6}
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1"
              />
            </label>
            <label className="text-sm font-semibold">
              Repite la nueva contrasena
              <input
                type="password"
                required
                minLength={6}
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1"
              />
            </label>
            {error && <p className="text-tclas-rose text-sm">{error}</p>}
            <button disabled={saving} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50">
              {saving ? "Guardando..." : "Guardar nueva contrasena"}
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
