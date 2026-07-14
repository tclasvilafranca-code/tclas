import type { ReactNode } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { Bolt, CheckCircle, Clock, Flame, Star, Target } from "../components/Icons";

export function Landing() {
  const { user } = useAuth();

  return (
    <div>
      {/* ---------- Hero ---------- */}
      <section className="relative overflow-hidden bg-t48-ink">
        <img
          src="/images/hero-road.jpg"
          alt=""
          aria-hidden="true"
          className="absolute inset-0 h-full w-full object-cover opacity-45"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-t48-ink via-t48-ink/70 to-t48-ink/30" />
        <div className="absolute inset-0 bg-gradient-to-r from-t48-ink/60 via-transparent to-transparent" />

        <div className="relative mx-auto max-w-3xl px-4 py-24 text-center sm:py-32">
          <p className="mb-5 inline-flex animate-[fadeIn_0.5s_ease-out_both] items-center gap-1.5 rounded-full border border-white/15 bg-white/10 px-4 py-1.5 text-sm font-bold text-white backdrop-blur-sm">
            <Bolt className="h-3.5 w-3.5 text-t48-amber" /> Aprende. Practica. Aprueba.
          </p>
          <h1 className="animate-[fadeIn_0.6s_ease-out_0.05s_both] text-balance text-5xl font-extrabold tracking-tight text-white sm:text-6xl">
            Aprueba el teórico<br />en <span className="bg-gradient-to-r from-sky-300 to-t48-amber bg-clip-text text-transparent">48 horas</span>
          </h1>
          <p className="mx-auto mt-5 max-w-lg animate-[fadeIn_0.6s_ease-out_0.1s_both] text-lg text-slate-200">
            Tests reales, repaso de tus fallos y un método que funciona. Sin rollos.
          </p>

          <div className="mt-9 flex animate-[fadeIn_0.6s_ease-out_0.15s_both] flex-col items-center justify-center gap-3 sm:flex-row">
            <Link
              to={user ? "/dashboard" : "/register"}
              className="btn-primary w-full px-7 py-3.5 text-lg sm:w-auto"
            >
              {user ? "Ir a mi panel" : "Empieza gratis"}
            </Link>
            <Link
              to="/login"
              className="w-full rounded-md border border-white/15 px-7 py-3.5 text-lg font-semibold text-white/90 transition-colors hover:bg-white/10 sm:w-auto"
            >
              Ya tengo cuenta
            </Link>
          </div>
        </div>
      </section>

      {/* ---------- Prueba social / stats rápidas ---------- */}
      <section className="border-b border-slate-100 bg-white">
        <div className="mx-auto grid max-w-3xl grid-cols-3 gap-4 px-4 py-8 text-center">
          <Stat value="500" label="preguntas originales" />
          <Stat value="30" label="preguntas por simulacro" />
          <Stat value="3" label="fallos máx. para aprobar" />
        </div>
      </section>

      {/* ---------- Features ---------- */}
      <section className="mx-auto max-w-3xl px-4 py-20">
        <div className="anim-stagger grid gap-4 sm:grid-cols-3">
          <Feature icon={<Target className="h-5 w-5" />} title="Tests reales" text="30 preguntas, mismas reglas que el examen. Máx. 3 fallos." />
          <Feature icon={<Flame className="h-5 w-5" />} title="Repasa tus fallos" text="Lo que fallas, vuelve. Así se aprende el doble de rápido." />
          <Feature icon={<Clock className="h-5 w-5" />} title="Cuenta atrás" text="Dinos cuándo te examinas y organizamos tu estudio." />
        </div>

        <div className="mt-6 anim-stagger">
          <Feature
            icon={<Star className="h-5 w-5" />}
            title="Teoría Express"
            text="Lo esencial del temario en 3 sesiones cortas y visuales, antes de lanzarte a los simulacros."
            wide
          />
        </div>

        <div className="mt-16 flex items-center justify-center gap-2 text-sm text-slate-500">
          <CheckCircle className="h-4 w-4 text-t48-green-dark" />
          El método funciona si tú le pones las horas — no prometemos magia, solo un buen atajo.
        </div>
      </section>
    </div>
  );
}

function Stat({ value, label }: { value: string; label: string }) {
  return (
    <div>
      <p className="text-3xl font-extrabold tabular-nums tracking-tight text-t48-blue">{value}</p>
      <p className="mt-1 text-xs font-semibold uppercase tracking-wide text-slate-400">{label}</p>
    </div>
  );
}

function Feature({ icon, title, text, wide }: { icon: ReactNode; title: string; text: string; wide?: boolean }) {
  return (
    <div className={`card-lift rounded-2xl border border-slate-200 bg-white p-5 text-left ${wide ? "sm:flex sm:items-center sm:gap-5" : ""}`}>
      <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-t48-blue/10 text-t48-blue">{icon}</div>
      <div className={wide ? "sm:mt-0" : ""}>
        <h3 className="mt-3 font-bold text-t48-ink sm:mt-3">{title}</h3>
        <p className="mt-1 text-sm text-slate-500">{text}</p>
      </div>
    </div>
  );
}
