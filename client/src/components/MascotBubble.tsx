import type { MascotMood } from "./MascotOwl";
import { MascotOwl } from "./MascotOwl";

interface Props {
  message: string;
  mood?: MascotMood;
  size?: number;
  className?: string;
  align?: "left" | "center";
}

// Misol hablando: buho + bocadillo de texto. Se usa por toda la app para dar
// animos, celebrar aciertos y presentar cada pieza.
export function MascotBubble({ message, mood = "cheer", size = 56, className = "", align = "left" }: Props) {
  return (
    <div className={`flex items-start gap-2.5 min-w-0 ${align === "center" ? "justify-center" : ""} ${className}`}>
      <MascotOwl mood={mood} size={size} className="shrink-0" />
      <div className="relative bg-white/90 border border-tclas-ink/10 rounded-2xl rounded-tl-sm px-3.5 py-2 shadow-sm max-w-xs min-w-0">
        <p className="text-xs font-semibold text-tclas-plum/70 mb-0.5">Misol</p>
        <p className="text-sm text-tclas-ink leading-snug">{message}</p>
      </div>
    </div>
  );
}
