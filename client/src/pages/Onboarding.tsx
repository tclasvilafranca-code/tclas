import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../lib/api";
import type { Track, AgeGroup } from "../lib/api";
import { useAuth } from "../context/AuthContext";

const CODE_TO_AGE_GROUP: Record<string, AgeGroup> = { kids: "KIDS", teens: "TEENS", adults: "ADULTS" };

export function Onboarding() {
  const [tracks, setTracks] = useState<Track[]>([]);
  const [submitting, setSubmitting] = useState(false);
  const { refresh } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    api.get<Track[]>("/tracks").then(setTracks);
  }, []);

  async function choose(track: Track) {
    setSubmitting(true);
    try {
      await api.post("/onboarding", { ageGroup: CODE_TO_AGE_GROUP[track.code] ?? "ADULTS", trackId: track.id });
      await refresh();
      navigate("/app");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-4 py-10">
      <h1 className="font-display text-3xl mb-2 text-center">¿Cual es tu camino musical?</h1>
      <p className="text-tclas-ink/60 mb-8 text-center max-w-md">Elige el grupo que mejor te representa para adaptar el ritmo, el estilo y las canciones a ti.</p>
      <div className="grid md:grid-cols-3 gap-5 max-w-4xl w-full">
        {tracks.map((t) => (
          <button
            key={t.id}
            disabled={submitting}
            onClick={() => choose(t)}
            className="text-left bg-white/70 border-2 border-tclas-ink/10 hover:border-tclas-gold rounded-2xl p-5 transition-colors disabled:opacity-50"
          >
            <h2 className="font-display text-xl text-tclas-plum mb-1">{t.name}</h2>
            <p className="text-xs text-tclas-ink/50 mb-2">
              {t.minAge}
              {t.maxAge < 99 ? `–${t.maxAge} anos` : "+ anos"}
            </p>
            <p className="text-sm text-tclas-ink/70">{t.description}</p>
          </button>
        ))}
      </div>
    </div>
  );
}
