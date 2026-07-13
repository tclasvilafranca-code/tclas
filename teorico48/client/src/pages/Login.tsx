import { useState } from "react";
import type { FormEvent, ReactNode } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { ApiError } from "../lib/api";

export function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setBusy(true);
    try {
      await login(email, password);
      navigate("/dashboard");
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Error al iniciar sesión");
    } finally {
      setBusy(false);
    }
  }

  return (
    <AuthForm title="Entrar" onSubmit={handleSubmit} error={error} busy={busy} submitLabel="Entrar">
      <Fields email={email} setEmail={setEmail} password={password} setPassword={setPassword} />
      <p className="mt-4 text-center text-sm text-slate-500">
        ¿No tienes cuenta? <Link to="/register" className="font-semibold text-t48-blue">Regístrate</Link>
      </p>
    </AuthForm>
  );
}

export function Register() {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setBusy(true);
    try {
      await register(email, password);
      navigate("/dashboard");
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Error al crear la cuenta");
    } finally {
      setBusy(false);
    }
  }

  return (
    <AuthForm title="Crear cuenta gratis" onSubmit={handleSubmit} error={error} busy={busy} submitLabel="Crear cuenta">
      <Fields email={email} setEmail={setEmail} password={password} setPassword={setPassword} />
      <p className="mt-4 text-center text-sm text-slate-500">
        ¿Ya tienes cuenta? <Link to="/login" className="font-semibold text-t48-blue">Entra</Link>
      </p>
    </AuthForm>
  );
}

function Fields(props: { email: string; setEmail: (v: string) => void; password: string; setPassword: (v: string) => void }) {
  return (
    <>
      <label className="block text-sm font-medium text-slate-700">
        Email
        <input
          type="email"
          required
          value={props.email}
          onChange={(e) => props.setEmail(e.target.value)}
          className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"
        />
      </label>
      <label className="mt-4 block text-sm font-medium text-slate-700">
        Contraseña
        <input
          type="password"
          required
          minLength={6}
          value={props.password}
          onChange={(e) => props.setPassword(e.target.value)}
          className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"
        />
      </label>
    </>
  );
}

function AuthForm(props: {
  title: string;
  onSubmit: (e: FormEvent) => void;
  error: string | null;
  busy: boolean;
  submitLabel: string;
  children: ReactNode;
}) {
  return (
    <div className="mx-auto max-w-sm px-4 py-16">
      <h1 className="mb-6 text-center text-2xl font-bold text-t48-ink">{props.title}</h1>
      <form onSubmit={props.onSubmit} className="rounded-xl border border-slate-200 bg-white p-6">
        {props.children}
        {props.error && <p className="mt-3 text-sm text-t48-red">{props.error}</p>}
        <button
          type="submit"
          disabled={props.busy}
          className="mt-6 w-full rounded-lg bg-t48-blue px-4 py-2.5 font-semibold text-white hover:bg-t48-blue-dark disabled:opacity-50"
        >
          {props.busy ? "Un momento..." : props.submitLabel}
        </button>
      </form>
    </div>
  );
}
