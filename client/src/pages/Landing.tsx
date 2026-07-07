import { Link } from "react-router-dom";

export function Landing() {
  return (
    <div className="min-h-screen flex flex-col">
      <header className="flex items-center justify-between px-6 py-5 max-w-5xl mx-auto w-full">
        <div className="font-display text-2xl text-tclas-plum">t-clas 🎹</div>
        <nav className="flex gap-3">
          <Link to="/login" className="px-4 py-2 rounded-full font-semibold text-tclas-plum hover:bg-tclas-plum/10">
            Entrar
          </Link>
          <Link to="/register" className="px-4 py-2 rounded-full font-semibold bg-tclas-plum text-tclas-cream hover:bg-tclas-plum-light">
            Empezar gratis
          </Link>
        </nav>
      </header>

      <main className="flex-1 max-w-5xl mx-auto w-full px-6 py-12 flex flex-col items-center text-center gap-6">
        <span className="bg-tclas-gold/20 text-tclas-plum text-sm font-semibold px-4 py-1 rounded-full">
          El complemento perfecto para tus clases con Azucena
        </span>
        <h1 className="font-display text-5xl md:text-6xl leading-tight max-w-3xl">
          Aprende piano jugando, <span className="text-tclas-plum">entre clase y clase</span>
        </h1>
        <p className="text-lg text-tclas-ink/70 max-w-2xl">
          t-clas es la app que practica contigo cada dia: lecciones cortas y divertidas de teoria, ritmo, oido y
          repertorio, pensadas para preparar y reforzar tus clases presenciales de piano.
        </p>
        <div className="flex gap-3">
          <Link to="/register" className="px-6 py-3 rounded-full font-semibold bg-tclas-plum text-tclas-cream hover:bg-tclas-plum-light text-lg">
            Crear mi cuenta
          </Link>
          <Link to="/login" className="px-6 py-3 rounded-full font-semibold border-2 border-tclas-plum text-tclas-plum hover:bg-tclas-plum/10 text-lg">
            Ya tengo cuenta
          </Link>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mt-12 text-left">
          {[
            { icon: "🧒", title: "Para cada edad", text: "Caminos distintos para ninos, adolescentes y adultos, con el ritmo y el estilo que mejor conecta con cada uno." },
            { icon: "🎮", title: "Como un juego", text: "XP, rachas, corazones e insignias para que practicar en casa se sienta ligero y motivador." },
            { icon: "🎹", title: "Piano de verdad", text: "Toca con el raton, el teclado del ordenador o conecta tu piano digital por MIDI para practicar con notas reales." },
          ].map((f) => (
            <div key={f.title} className="bg-white/60 rounded-2xl p-5 border border-tclas-ink/10">
              <div className="text-3xl mb-2">{f.icon}</div>
              <h3 className="font-display text-xl mb-1">{f.title}</h3>
              <p className="text-sm text-tclas-ink/70">{f.text}</p>
            </div>
          ))}
        </div>
      </main>

      <footer className="text-center text-xs text-tclas-ink/40 py-6">t-clas · Azucena, profesora de piano</footer>
    </div>
  );
}
