export type MascotMood = "cheer" | "celebrate" | "encourage" | "think";

interface Props {
  mood?: MascotMood;
  size?: number;
  className?: string;
}

// Misol, la mascota buho de t-clas. SVG sencillo con un par de variantes de
// expresion segun el momento (animo, celebracion, aliento, pensando).
export function MascotOwl({ mood = "cheer", size = 64, className = "" }: Props) {
  const tilt = mood === "think" ? -8 : 0;
  const wingsUp = mood === "celebrate";
  const wingPat = mood === "encourage";

  return (
    <svg viewBox="0 0 100 100" width={size} height={size} className={className}>
      <g transform={`rotate(${tilt} 50 55)`}>
        {/* orejas */}
        <path d="M28 30 L36 10 L44 28 Z" fill="#4a1942" />
        <path d="M72 30 L64 10 L56 28 Z" fill="#4a1942" />

        {/* ala izquierda */}
        <ellipse
          cx="22"
          cy={wingsUp ? 48 : 66}
          rx="9"
          ry="16"
          fill="#6b2a5e"
          transform={`rotate(${wingsUp ? -35 : wingPat ? -15 : 10} 22 ${wingsUp ? 48 : 66})`}
        />
        {/* ala derecha */}
        <ellipse
          cx="78"
          cy={wingsUp ? 48 : 66}
          rx="9"
          ry="16"
          fill="#6b2a5e"
          transform={`rotate(${wingsUp ? 35 : -10} 78 ${wingsUp ? 48 : 66})`}
        />

        {/* cuerpo */}
        <ellipse cx="50" cy="58" rx="34" ry="38" fill="#4a1942" />
        <ellipse cx="50" cy="64" rx="21" ry="27" fill="#fbf6ee" />

        {/* ojos */}
        <circle cx="37" cy="50" r="14" fill="#fbf6ee" stroke="#4a1942" strokeWidth="2" />
        <circle cx="63" cy="50" r="14" fill="#fbf6ee" stroke="#4a1942" strokeWidth="2" />

        {mood === "encourage" ? (
          <>
            <path d="M31 50 Q37 44 43 50" stroke="#241a2e" strokeWidth="3.5" fill="none" strokeLinecap="round" />
            <path d="M57 50 Q63 44 69 50" stroke="#241a2e" strokeWidth="3.5" fill="none" strokeLinecap="round" />
          </>
        ) : mood === "think" ? (
          <>
            <circle cx="40" cy="52" r="5.5" fill="#241a2e" />
            <circle cx="66" cy="52" r="5.5" fill="#241a2e" />
            <path d="M55 34 Q63 30 70 34" stroke="#241a2e" strokeWidth="2.5" fill="none" strokeLinecap="round" />
          </>
        ) : (
          <>
            <circle cx="37" cy={mood === "celebrate" ? 48 : 50} r={mood === "celebrate" ? 7 : 6} fill="#241a2e" />
            <circle cx="63" cy={mood === "celebrate" ? 48 : 50} r={mood === "celebrate" ? 7 : 6} fill="#241a2e" />
            <circle cx="39.5" cy={mood === "celebrate" ? 45.5 : 47.5} r="2" fill="#fbf6ee" />
            <circle cx="65.5" cy={mood === "celebrate" ? 45.5 : 47.5} r="2" fill="#fbf6ee" />
          </>
        )}

        {/* pico */}
        <path d="M50 60 L44 68 L56 68 Z" fill="#d4a94c" />

        {/* pies */}
        <path d="M40 96 L36 90 M40 96 L44 90" stroke="#d4a94c" strokeWidth="3" strokeLinecap="round" />
        <path d="M60 96 L56 90 M60 96 L64 90" stroke="#d4a94c" strokeWidth="3" strokeLinecap="round" />
      </g>

      {mood === "celebrate" && (
        <g fill="#d4a94c">
          <path d="M12 30 l2 5 5 2 -5 2 -2 5 -2 -5 -5 -2 5 -2 Z" />
          <path d="M88 40 l1.5 4 4 1.5 -4 1.5 -1.5 4 -1.5 -4 -4 -1.5 4 -1.5 Z" />
          <path d="M80 15 l1.2 3.2 3.2 1.2 -3.2 1.2 -1.2 3.2 -1.2 -3.2 -3.2 -1.2 3.2 -1.2 Z" />
        </g>
      )}
    </svg>
  );
}
