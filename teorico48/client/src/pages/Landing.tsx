import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function Landing() {
  const { user } = useAuth();

  return (
    <div className="mx-auto max-w-3xl px-4 py-16 text-center">
      <p className="mb-3 inline-block rounded-full bg-t48-blue/10 px-4 py-1 text-sm font-semibold text-t48-blue-dark">
        ¿Examen a la vuelta de la esquina?
      </p>
      <h1 className="text-4xl font-extrabold leading-tight text-t48-ink sm:text-5xl">
        Aprueba el teórico del carnet en <span className="text-t48-blue">48 horas</span>
      </h1>
      <p className="mx-auto mt-4 max-w-xl text-lg text-slate-600">
        Simulacros de examen reales, repaso automático de tus fallos y un plan de estudio con cuenta atrás
        hasta tu examen. Sin rollos, directo a aprobar.
      </p>

      <div className="mt-8 flex flex-col items-center justify-center gap-3 sm:flex-row">
        <Link
          to={user ? "/dashboard" : "/register"}
          className="w-full rounded-lg bg-t48-blue px-6 py-3 text-lg font-semibold text-white shadow-sm hover:bg-t48-blue-dark sm:w-auto"
        >
          {user ? "Ir a mi panel" : "Empezar gratis"}
        </Link>
        <Link
          to="/login"
          className="w-full rounded-lg border border-slate-300 px-6 py-3 text-lg font-semibold text-slate-700 hover:bg-slate-50 sm:w-auto"
        >
          Ya tengo cuenta
        </Link>
      </div>

      <div className="mt-16 grid gap-6 text-left sm:grid-cols-3">
        <Feature
          title="Simulacros reales"
          text="Tests de 30 preguntas con las mismas reglas que el examen oficial (máx. 3 fallos)."
        />
        <Feature
          title="Repasa tus fallos"
          text="El modo repaso se centra solo en lo que sueles fallar, para aprender el doble de rápido."
        />
        <Feature
          title="Cuenta atrás a tu examen"
          text="Dinos cuándo te examinas y te organizamos el estudio en las horas que te quedan."
        />
      </div>
    </div>
  );
}

function Feature({ title, text }: { title: string; text: string }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-5">
      <h3 className="font-bold text-t48-ink">{title}</h3>
      <p className="mt-1 text-sm text-slate-600">{text}</p>
    </div>
  );
}
