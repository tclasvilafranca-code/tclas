import type { CSSProperties } from "react";

// Bloque base para "esqueletos" de carga: ocupa el hueco exacto que va a
// tener el contenido real, para que la pantalla nunca de un salto al llegar
// los datos y nunca se sienta un prototipo a medio cargar.
export function Skeleton({ className = "", style }: { className?: string; style?: CSSProperties }) {
  return <div style={style} className={`animate-pulse rounded-md bg-tclas-ink/8 ${className}`} />;
}
