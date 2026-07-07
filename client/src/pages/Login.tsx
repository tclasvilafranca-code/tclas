import { useState } from "react";
import type { FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const me = await login(email, password);
      navigate(me.role === "TEACHER" ? "/teacher" : me.studentProfile?.onboarded ? "/app" : "/onboarding");
    } catch (err: any) {
      setError(err.message || "No se pudo iniciar sesion");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="bg-white/70 rounded-2xl p-8 max-w-sm w-full border border-tclas-ink/10">
        <Link to="/" className="font-display text-xl text-tclas-plum">t-clas 🎹</Link>
        <h1 className="font-display text-2xl mt-4 mb-6">Bienvenido de nuevo</h1>
        <form onSubmit={handleSubmit} className="flex flex-col gap-3">
          <input type="email" required placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
          <input type="password" required placeholder="Contrasena" value={password} onChange={(e) => setPassword(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
          {error && <p className="text-tclas-rose text-sm">{error}</p>}
          <button disabled={loading} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50">
            {loading ? "Entrando..." : "Entrar"}
          </button>
        </form>
        <p className="text-sm text-tclas-ink/60 mt-4">
          ¿No tienes cuenta? <Link to="/register" className="text-tclas-plum font-semibold">Registrate</Link>
        </p>
        <p className="text-xs text-tclas-ink/40 mt-6">
          Demo alumno: alumno@t-clas.com / alumno123 <br /> Demo profesora: azucena@t-clas.com / profesora123
        </p>
      </div>
    </div>
  );
}
