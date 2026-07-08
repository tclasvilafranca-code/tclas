import { useEffect, useRef, useState } from "react";
import type { Exercise } from "../lib/api";
import { StaffView } from "../components/StaffView";

interface Props {
  exercise: Exercise;
  onSubmit: (answer: string) => void;
  feedback: { correct: boolean; explanation: string } | null;
}

type SpeechStatus = "idle" | "listening" | "unsupported" | "done";

export function SpeakAloudExercise({ exercise, onSubmit, feedback }: Props) {
  const [status, setStatus] = useState<SpeechStatus>("idle");
  const [heard, setHeard] = useState("");
  const recognitionRef = useRef<any>(null);

  useEffect(() => {
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setStatus("unsupported");
      return;
    }
    const recognition = new SpeechRecognition();
    recognition.lang = "es-ES";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    recognition.onresult = (event: any) => {
      const transcript = event.results[0][0].transcript;
      setHeard(transcript);
      setStatus("done");
      onSubmit(transcript);
    };
    recognition.onerror = () => setStatus("idle");
    recognitionRef.current = recognition;
    return () => recognition.stop();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function start() {
    if (!recognitionRef.current || feedback) return;
    setStatus("listening");
    recognitionRef.current.start();
  }

  function skip() {
    setStatus("done");
    onSubmit("(omitido)");
  }

  const note = exercise.data.promptNote;

  return (
    <div className="text-center">
      <p className="text-lg font-semibold mb-4">{exercise.prompt}</p>

      {note && (
        <div className="mb-6">
          <StaffView clef="treble" notes={[note]} />
        </div>
      )}

      {status === "unsupported" && (
        <div>
          <p className="text-sm text-tclas-ink/50 mb-3">Tu navegador no soporta reconocimiento de voz.</p>
          {!feedback && (
            <button onClick={skip} className="bg-tclas-ink/10 rounded-full px-5 py-2 font-semibold hover:bg-tclas-ink/20">
              Omitir y continuar
            </button>
          )}
        </div>
      )}

      {status !== "unsupported" && !feedback && (
        <button
          onClick={start}
          className={`rounded-full w-24 h-24 text-3xl font-bold transition-colors ${status === "listening" ? "bg-tclas-rose text-white animate-pulse" : "bg-tclas-gold text-tclas-ink hover:bg-tclas-gold-light"}`}
        >
          🎤
        </button>
      )}
      {status === "listening" && <p className="text-sm text-tclas-ink/50 mt-3">Escuchando... di el nombre en voz alta</p>}
      {heard && <p className="text-sm text-tclas-ink/60 mt-3">Se ha entendido: "{heard}"</p>}

      {feedback && <p className="mt-4 text-sm text-tclas-ink/70 max-w-md mx-auto">{feedback.explanation}</p>}
    </div>
  );
}
