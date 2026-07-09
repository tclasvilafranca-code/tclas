import { useState } from "react";
import type { FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { MascotBubble } from "../components/MascotBubble";
import { landingMessage } from "../lib/misol";

// Entrada unica por usuario+PIN, para alumnado y profesora por igual: la app
// ya sabe a que panel llevar a cada quien por el rol real de su cuenta, sin
// tener que elegir de antemano quien eres ni acordarte de un email/contrasena
// aparte.
export function Landing() {
  const { loginWithPin } = useAuth();
  const navigate = useNavigate();
  const [welcome] = useState(landingMessage);

  const [username, setUsername] = useState("");
  const [pin, setPin] = useState("");

  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const me = await loginWithPin(username, pin);
      navigate(me.role === "TEACHER" ? "/teacher" : "/app");
    } catch (err: any) {
      setError(err.message || "No se pudo iniciar sesion");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-4 py-10 gap-8">
      <div className="text-center max-w-md">
        <h1 className="font-display text-4xl text-tclas-plum mb-2">t-clas</h1>
        <p className="text-tclas-ink/70">Aprende piano jugando, entre clase y clase con Azucena.</p>
        <div className="flex justify-center gap-4 mt-4 text-xs text-tclas-ink/50">
          <span>🧒 Para cada edad</span>
          <span>🎮 Como un juego</span>
          <span>🎹 Piano de verdad</span>
        </div>
        <MascotBubble message={welcome} align="center" className="mt-5 text-left" />
      </div>

      <div className="bg-white/70 rounded-2xl p-8 max-w-sm w-full border border-tclas-ink/10">
        <form onSubmit={handleSubmit} className="flex flex-col gap-3">
          <input required placeholder="Usuario" value={username} onChange={(e) => setUsername(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
          <input required placeholder="PIN" inputMode="numeric" value={pin} onChange={(e) => setPin(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
          {error && <p className="text-tclas-rose text-sm">{error}</p>}
          <button
            disabled={loading}
            className="btn-push bg-tclas-plum border-tclas-plum-shadow text-tclas-cream rounded-2xl py-3 font-bold uppercase tracking-wide text-sm hover:bg-tclas-plum-light"
          >
            {loading ? "Entrando..." : "Entrar"}
          </button>
        </form>

        <p className="text-xs text-tclas-ink/40 mt-4 text-center">Tu usuario y PIN te los da tu profesor/a (o los configuraste tu misma).</p>
      </div>

      <footer className="text-center text-xs text-tclas-ink/40">t-clas · Azucena, profesora de piano</footer>
    </div>
  );
}
