import { useEffect, useState } from "react";
import { api } from "../lib/api";
import type { Message } from "../lib/api";
import { MessageThread } from "./MessageThread";

interface Props {
  otherName: string;
  onClose: () => void;
  onRead?: () => void;
}

// Modal de mensajeria del lado del alumno: solo tiene una conversacion (la
// de su profesor/a), asi que no hace falta elegir con quien hablar.
export function MessagesModal({ otherName, onClose, onRead }: Props) {
  const [messages, setMessages] = useState<Message[] | null>(null);

  useEffect(() => {
    api.get<{ messages: Message[] }>("/me/messages").then((r) => {
      setMessages(r.messages);
      onRead?.();
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function send(body: string) {
    const message = await api.post<Message>("/me/messages", { body });
    setMessages((prev) => [...(prev ?? []), message]);
  }

  return (
    <div className="fixed inset-0 bg-tclas-ink/40 backdrop-blur-sm z-50 flex items-center justify-center p-4" onClick={onClose}>
      <div className="bg-tclas-cream rounded-2xl w-full max-w-md shadow-xl border border-tclas-ink/10" onClick={(e) => e.stopPropagation()}>
        <div className="flex items-center justify-between px-5 py-4 border-b border-tclas-ink/10">
          <h2 className="font-display text-xl">{otherName}</h2>
          <button onClick={onClose} className="text-tclas-ink/40 hover:text-tclas-ink text-xl leading-none px-1">
            ✕
          </button>
        </div>
        <div className="p-4">
          <MessageThread messages={messages} otherName={otherName} onSend={send} />
        </div>
      </div>
    </div>
  );
}
