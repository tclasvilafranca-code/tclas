import { useState } from "react";
import type { FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function Login() {
  const { loginTeacher, loginStudent } = useAuth();
  const navigate = useNavigate();
  const [mode, setMode] = useState<"student" | "teacher">("student");

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");
  const [pin, setPin] = useState("");

  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      if (mode === "teacher") {
        await loginTeacher(email, password);
        navigate("/teacher");
      } else {
        await loginStudent(username, pin);
        navigate("/app");
      }
    } catch (err: any) {
      setError(err.message || "No se pudo iniciar sesion");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="bg-white/70 rounded-2xl p-8 max-w-sm w-full border border-tclas-ink/10">
        <Link to="/" className="font-display text-xl text-tclas-plum">
          t-clas 🎹
        </Link>
        <h1 className="font-display text-2xl mt-4 mb-4">Bienvenido de nuevo</h1>

        <div className="flex gap-2 mb-5">
          <button
            type="button"
            onClick={() => setMode("student")}
            className={`flex-1 rounded-lg py-2 text-sm font-semibold border-2 ${mode === "student" ? "border-tclas-plum bg-tclas-plum/10" : "border-tclas-ink/15"}`}
          >
            Soy alumno/a
          </button>
          <button
            type="button"
            onClick={() => setMode("teacher")}
            className={`flex-1 rounded-lg py-2 text-sm font-semibold border-2 ${mode === "teacher" ? "border-tclas-plum bg-tclas-plum/10" : "border-tclas-ink/15"}`}
          >
            Soy profesor/a
          </button>
        </div>

        <form onSubmit={handleSubmit} className="flex flex-col gap-3">
          {mode === "student" ? (
            <>
              <input required placeholder="Usuario" value={username} onChange={(e) => setUsername(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
              <input required placeholder="PIN" inputMode="numeric" value={pin} onChange={(e) => setPin(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
            </>
          ) : (
            <>
              <input type="email" required placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
              <input type="password" required placeholder="Contrasena" value={password} onChange={(e) => setPassword(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
            </>
          )}
          {error && <p className="text-tclas-rose text-sm">{error}</p>}
          <button disabled={loading} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50">
            {loading ? "Entrando..." : "Entrar"}
          </button>
        </form>

        {mode === "teacher" && (
          <p className="text-sm text-tclas-ink/60 mt-4">
            ¿No tienes cuenta? <Link to="/register" className="text-tclas-plum font-semibold">Registrate</Link>
          </p>
        )}
        {mode === "student" && <p className="text-xs text-tclas-ink/40 mt-4">Tu usuario y PIN te los da tu profesor/a.</p>}

        <p className="text-xs text-tclas-ink/40 mt-6">
          Demo alumno: usuario "arnau" / PIN 1234 <br /> Demo profesora: azucena@t-clas.com / profesora123
        </p>
      </div>
    </div>
  );
}
