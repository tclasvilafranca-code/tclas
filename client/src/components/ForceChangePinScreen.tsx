import { useState } from "react";
import type { FormEvent } from "react";
import { api, ApiError } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import { MascotBubble } from "./MascotBubble";
import { IconKey } from "./icons";

// Pantalla obligatoria (no se puede saltar) para cambiar un PIN por defecto
// (1234, tanto de un alumno recien creado como de la profesora al configurar
// su acceso rapido) por uno propio, antes de dejar entrar al resto de la app.
export function ForceChangePinScreen() {
  const { refresh, logout } = useAuth();
  const [newPin, setNewPin] = useState("");
  const [confirmPin, setConfirmPin] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);

  async function submit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    if (newPin === "1234") {
      setError("Elige un PIN distinto al de por defecto (1234)");
      return;
    }
    if (newPin !== confirmPin) {
      setError("Los dos PIN no coinciden");
      return;
    }
    setSaving(true);
    try {
      await api.post("/auth/change-pin", { newPin });
      await refresh();
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "No se pudo guardar el PIN");
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-4 py-10 gap-6">
      <MascotBubble message="Antes de nada, ponte un PIN propio (el 1234 es solo temporal)." mood="encourage" align="center" className="max-w-sm text-left" />

      <div className="bg-white/70 rounded-2xl p-8 max-w-sm w-full border border-tclas-ink/10">
        <div className="flex items-center gap-2 mb-4">
          <IconKey className="w-5 h-5 text-tclas-plum" />
          <h1 className="font-display text-xl">Elige tu PIN</h1>
        </div>
        <form onSubmit={submit} className="flex flex-col gap-3">
          <label className="text-sm font-semibold">
            PIN nuevo (4 a 6 numeros)
            <input
              required
              inputMode="numeric"
              pattern="\d{4,6}"
              value={newPin}
              onChange={(e) => setNewPin(e.target.value)}
              className="block w-full border border-tclas-ink/20 rounded-lg px-4 py-2 mt-1"
              autoFocus
            />
          </label>
          <label className="text-sm font-semibold">
            Repite el PIN
            <input
              required
              inputMode="numeric"
              value={confirmPin}
              onChange={(e) => setConfirmPin(e.target.value)}
              className="block w-full border border-tclas-ink/20 rounded-lg px-4 py-2 mt-1"
            />
          </label>
          {error && <p className="text-tclas-rose text-sm">{error}</p>}
          <button
            disabled={saving}
            className="btn-push bg-tclas-plum border-tclas-plum-shadow text-tclas-cream rounded-2xl py-3 font-bold uppercase tracking-wide text-sm hover:bg-tclas-plum-light disabled:opacity-50"
          >
            {saving ? "Guardando..." : "Guardar y continuar"}
          </button>
        </form>
        <button onClick={logout} className="text-xs text-tclas-ink/40 hover:text-tclas-ink/70 underline underline-offset-2 mt-4 block mx-auto">
          Salir
        </button>
      </div>
    </div>
  );
}
