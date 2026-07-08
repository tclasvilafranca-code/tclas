import { useState } from "react";
import type { FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function Register() {
  const { registerTeacher } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      await registerTeacher(name, email, password);
      navigate("/teacher");
    } catch (err: any) {
      setError(err.message || "No se pudo crear la cuenta");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="bg-white/70 rounded-2xl p-8 max-w-sm w-full border border-tclas-ink/10">
        <Link to="/" className="font-display text-xl text-tclas-plum">t-clas 🎹</Link>
        <h1 className="font-display text-2xl mt-4 mb-2">Crea tu cuenta de profesor/a</h1>
        <p className="text-sm text-tclas-ink/60 mb-6">Tus alumnos no necesitan registrarse: tú les creas su acceso desde tu panel.</p>

        <form onSubmit={handleSubmit} className="flex flex-col gap-3">
          <input required placeholder="Nombre" value={name} onChange={(e) => setName(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
          <input type="email" required placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
          <input type="password" required minLength={6} placeholder="Contrasena (min. 6 caracteres)" value={password} onChange={(e) => setPassword(e.target.value)} className="border border-tclas-ink/20 rounded-lg px-4 py-2" />
          {error && <p className="text-tclas-rose text-sm">{error}</p>}
          <button disabled={loading} className="bg-tclas-plum text-tclas-cream rounded-lg py-2.5 font-semibold hover:bg-tclas-plum-light disabled:opacity-50">
            {loading ? "Creando..." : "Crear cuenta"}
          </button>
        </form>
        <p className="text-sm text-tclas-ink/60 mt-4">
          ¿Ya tienes cuenta? <Link to="/" className="text-tclas-plum font-semibold">Entra aqui</Link>
        </p>
      </div>
    </div>
  );
}
