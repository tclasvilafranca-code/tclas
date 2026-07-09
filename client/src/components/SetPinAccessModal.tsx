import { useState } from "react";
import type { FormEvent } from "react";
import { api, ApiError } from "../lib/api";

interface Props {
  currentUsername: string | null;
  onClose: () => void;
  onSaved?: () => void;
}

// Autoservicio para que la profesora configure su propio usuario+PIN (igual
// que ya tiene cada alumno) y pueda entrar sin email ni contrasena la
// proxima vez. Requiere estar ya autenticada (con su email+contrasena de
// siempre), asi que nunca puede dejarla fuera de su propia cuenta.
export function SetPinAccessModal({ currentUsername, onClose, onSaved }: Props) {
  const [username, setUsername] = useState(currentUsername ?? "");
  const [pin, setPin] = useState("");
  const [confirmPin, setConfirmPin] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);
  const [done, setDone] = useState(false);

  async function submit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    if (pin !== confirmPin) {
      setError("Los dos PIN no coinciden");
      return;
    }
    setSaving(true);
    try {
      await api.post("/auth/set-pin-access", { username, pin });
      setDone(true);
      onSaved?.();
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "No se pudo guardar");
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="fixed inset-0 bg-tclas-ink/40 backdrop-blur-sm z-50 flex items-center justify-center p-4" onClick={onClose}>
      <div className="bg-tclas-cream rounded-2xl w-full max-w-sm shadow-xl border border-tclas-ink/10 p-6" onClick={(e) => e.stopPropagation()}>
        <div className="flex items-center justify-between mb-4">
          <h2 className="font-display text-xl">Usuario y PIN</h2>
          <button onClick={onClose} className="text-tclas-ink/40 hover:text-tclas-ink text-xl leading-none px-1">
            ✕
          </button>
        </div>

        {done ? (
          <div className="text-center py-4">
            <p className="text-tclas-sage font-semibold mb-2">¡Listo! Ya puedes entrar con usuario y PIN.</p>
            <p className="font-mono text-lg mb-2">
              usuario: <b>{username}</b>
            </p>
            <p className="text-xs text-tclas-ink/50 mb-4">Este PIN ya es definitivo: la próxima vez entra directamente con usuario y PIN.</p>
            <button onClick={onClose} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 px-6 font-semibold hover:bg-tclas-plum-light">
              Cerrar
            </button>
          </div>
        ) : (
          <form onSubmit={submit} className="grid grid-cols-1 gap-3">
            <p className="text-xs text-tclas-ink/50 -mt-1">
              Configura un usuario y un PIN propios (como los de tus alumnos) para entrar rapido, sin email ni contraseña.
            </p>
            <label className="text-sm font-semibold">
              Usuario
              <input
                required
                minLength={3}
                maxLength={16}
                pattern="[a-zA-Z0-9]+"
                title="Solo letras y numeros, sin espacios"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1"
              />
            </label>
            <label className="text-sm font-semibold">
              PIN (4 a 6 numeros)
              <input
                required
                inputMode="numeric"
                pattern="\d{4,6}"
                title="Entre 4 y 6 numeros"
                value={pin}
                onChange={(e) => setPin(e.target.value)}
                className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1"
              />
            </label>
            <label className="text-sm font-semibold">
              Repite el PIN
              <input
                required
                inputMode="numeric"
                value={confirmPin}
                onChange={(e) => setConfirmPin(e.target.value)}
                className="block w-full border border-tclas-ink/20 rounded-lg px-3 py-2 mt-1"
              />
            </label>
            {error && <p className="text-tclas-rose text-sm">{error}</p>}
            <button disabled={saving} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50">
              {saving ? "Guardando..." : "Guardar usuario y PIN"}
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
