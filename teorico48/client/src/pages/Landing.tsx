import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function Landing() {
  const { user } = useAuth();

  return (
    <div className="mx-auto max-w-3xl px-4 py-20 text-center sm:py-28">
      <p className="mb-4 inline-flex items-center gap-1.5 rounded-full bg-t48-blue/10 px-4 py-1.5 text-sm font-bold text-t48-blue-dark">
        ⚡ Aprende. Practica. Aprueba.
      </p>
      <h1 className="text-5xl font-extrabold tracking-tight text-t48-ink sm:text-6xl">
        Aprueba el teórico<br />en <span className="text-t48-blue">48 horas</span>
      </h1>
      <p className="mx-auto mt-5 max-w-lg text-lg text-slate-500">
        Tests reales, repaso de tus fallos y un método que funciona. Sin rollos.
      </p>

      <div className="mt-9 flex flex-col items-center justify-center gap-3 sm:flex-row">
        <Link
          to={user ? "/dashboard" : "/register"}
          className="w-full rounded-2xl bg-t48-blue px-7 py-3.5 text-lg font-bold text-white shadow-lg shadow-t48-blue/25 transition-transform hover:scale-[1.03] hover:bg-t48-blue-dark active:scale-95 sm:w-auto"
        >
          {user ? "Ir a mi panel" : "Empieza gratis"}
        </Link>
        <Link
          to="/login"
          className="w-full rounded-2xl px-7 py-3.5 text-lg font-bold text-slate-500 transition-colors hover:bg-slate-100 hover:text-t48-ink sm:w-auto"
        >
          Ya tengo cuenta
        </Link>
      </div>

      <div className="mt-20 grid gap-4 text-left sm:grid-cols-3">
        <Feature emoji="🎯" title="Tests reales" text="30 preguntas, mismas reglas que el examen. Máx. 3 fallos." />
        <Feature emoji="🔥" title="Repasa tus fallos" text="Lo que fallas, vuelve. Así se aprende el doble de rápido." />
        <Feature emoji="⏱️" title="Cuenta atrás" text="Dinos cuándo te examinas y organizamos tu estudio." />
      </div>

      <p className="mt-16 text-xs text-slate-400">
        El método funciona si tú le pones las horas — no prometemos magia, solo un buen atajo.
      </p>
    </div>
  );
}

function Feature({ emoji, title, text }: { emoji: string; title: string; text: string }) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-5 transition-transform hover:-translate-y-0.5 hover:shadow-md">
      <div className="text-2xl">{emoji}</div>
      <h3 className="mt-2 font-bold text-t48-ink">{title}</h3>
      <p className="mt-1 text-sm text-slate-500">{text}</p>
    </div>
  );
}
