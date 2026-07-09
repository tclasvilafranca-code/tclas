import { useEffect, useRef, useState } from "react";
import type { FormEvent } from "react";
import type { Message } from "../lib/api";
import { IconSend } from "./icons";

interface Props {
  messages: Message[] | null;
  otherName: string;
  onSend: (body: string) => Promise<void>;
}

function formatTime(iso: string): string {
  const d = new Date(iso);
  const today = new Date();
  const sameDay = d.toDateString() === today.toDateString();
  return sameDay
    ? d.toLocaleTimeString("es-ES", { hour: "2-digit", minute: "2-digit" })
    : d.toLocaleDateString("es-ES", { day: "numeric", month: "short" }) + " " + d.toLocaleTimeString("es-ES", { hour: "2-digit", minute: "2-digit" });
}

// Hilo de mensajes reutilizable: lo usan tanto la profesora (dentro de la
// ficha de cada alumno) como el propio alumno (con su profesora), con el
// mismo componente y el mismo aspecto en los dos lados.
export function MessageThread({ messages, otherName, onSend }: Props) {
  const [draft, setDraft] = useState("");
  const [sending, setSending] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ block: "end" });
  }, [messages?.length]);

  async function submit(e: FormEvent) {
    e.preventDefault();
    const body = draft.trim();
    if (!body || sending) return;
    setSending(true);
    try {
      await onSend(body);
      setDraft("");
    } finally {
      setSending(false);
    }
  }

  return (
    <div className="flex flex-col bg-white/70 border border-tclas-ink/10 rounded-xl overflow-hidden">
      <div className="flex-1 overflow-y-auto px-4 py-4 flex flex-col gap-2.5 max-h-96 min-h-[10rem]">
        {messages === null ? (
          <p className="text-sm text-tclas-ink/40 text-center my-auto">Cargando mensajes...</p>
        ) : messages.length === 0 ? (
          <p className="text-sm text-tclas-ink/40 text-center my-auto">Todavía no hay mensajes con {otherName}. ¡Escribe el primero!</p>
        ) : (
          messages.map((m) => (
            <div key={m.id} className={`flex ${m.fromMe ? "justify-end" : "justify-start"}`}>
              <div
                className={`max-w-[80%] rounded-2xl px-3.5 py-2 text-sm leading-snug ${
                  m.fromMe ? "bg-tclas-plum text-tclas-cream rounded-br-sm" : "bg-tclas-ink/5 text-tclas-ink rounded-bl-sm"
                }`}
              >
                <p className="whitespace-pre-wrap break-words">{m.body}</p>
                <p className={`text-2xs mt-1 ${m.fromMe ? "text-tclas-cream/60" : "text-tclas-ink/40"}`}>{formatTime(m.createdAt)}</p>
              </div>
            </div>
          ))
        )}
        <div ref={bottomRef} />
      </div>
      <form onSubmit={submit} className="flex items-end gap-2 border-t border-tclas-ink/10 p-3">
        <textarea
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              submit(e);
            }
          }}
          placeholder={`Escribe a ${otherName}...`}
          rows={1}
          className="flex-1 resize-none border border-tclas-ink/20 rounded-xl px-3 py-2 text-sm max-h-24"
        />
        <button
          type="submit"
          disabled={!draft.trim() || sending}
          className="shrink-0 w-10 h-10 rounded-full bg-tclas-plum text-tclas-cream flex items-center justify-center disabled:opacity-40 hover:bg-tclas-plum-light"
          aria-label="Enviar mensaje"
        >
          <IconSend className="w-4 h-4 ml-0.5" />
        </button>
      </form>
    </div>
  );
}
