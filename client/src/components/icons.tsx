// Set de iconos propio, en linea (stroke), coherente con la identidad t-clas:
// mismo grosor de trazo y esquinas redondeadas en todos, para que la barra de
// navegacion, las estadisticas y los estados de las lecciones dejen de
// depender de como cada sistema operativo dibuje sus emoji.
interface IconProps {
  className?: string;
}

const BASE = "stroke-current fill-none";
const STROKE = 1.8;

export function IconHome({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 11.5 12 4l8 7.5" />
      <path d="M6 10v9a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-9" />
      <path d="M10 20v-5h4v5" />
    </svg>
  );
}

// Camino musical: la ruta en zigzag que sigue el alumno, con sus paradas.
export function IconPath({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 20c0-3 4-3 4-6s-3-3-3-6 4-3.5 4-6" />
      <circle cx="5" cy="20" r="1.4" className="fill-current stroke-none" />
      <circle cx="9" cy="8" r="1.4" className="fill-current stroke-none" />
      <circle cx="10" cy="2" r="1.4" className="fill-current stroke-none" />
    </svg>
  );
}

export function IconPiano({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <rect x="3.5" y="5" width="17" height="14" rx="2" />
      <path d="M8 5v8M12 5v8M16 5v8" />
    </svg>
  );
}

export function IconProfile({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="8.5" r="3.5" />
      <path d="M4.5 20c1.2-4 4-6 7.5-6s6.3 2 7.5 6" />
    </svg>
  );
}

export function IconFlame({ className = "w-4 h-4" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`fill-current ${className}`}>
      <path d="M12 2c1 3-2.5 4.2-2.5 7.2 0 1.3 1 2.3 2 2.3.4-1.3-.3-2-.1-3.2 1.3 1 2.6 2.7 2.6 5A4.9 4.9 0 0 1 9.1 18a5.4 5.4 0 0 1-2-4.4C7.1 9 12 8 12 2Z" />
    </svg>
  );
}

export function IconStar({ className = "w-4 h-4" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`fill-current ${className}`}>
      <path d="M12 3.2 14.5 9l6.3.5-4.8 4.2 1.5 6.1L12 16.8 6.5 19.8l1.5-6.1-4.8-4.2L9.5 9Z" />
    </svg>
  );
}

export function IconHeart({ className = "w-4 h-4", filled = true }: IconProps & { filled?: boolean }) {
  if (filled) {
    return (
      <svg viewBox="0 0 24 24" className={`fill-current ${className}`}>
        <path d="M12 20.2S3.5 15 3.5 9.1A4.6 4.6 0 0 1 12 6.5a4.6 4.6 0 0 1 8.5 2.6c0 5.9-8.5 11.1-8.5 11.1Z" />
      </svg>
    );
  }
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 20.2S3.5 15 3.5 9.1A4.6 4.6 0 0 1 12 6.5a4.6 4.6 0 0 1 8.5 2.6c0 5.9-8.5 11.1-8.5 11.1Z" />
    </svg>
  );
}

export function IconClock({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="12" r="8.5" />
      <path d="M12 7.5V12l3.2 2" />
    </svg>
  );
}

export function IconTrophy({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <path d="M7 4h10v4.5A5 5 0 0 1 12 13.5 5 5 0 0 1 7 8.5Z" />
      <path d="M7 5.5H4.8A2.3 2.3 0 0 0 5 10.1M17 5.5h2.2A2.3 2.3 0 0 1 19 10.1" />
      <path d="M12 13.5V17M8.5 20h7M9.5 17h5v3h-5Z" />
    </svg>
  );
}

export function IconLock({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <rect x="5" y="11" width="14" height="9" rx="2" />
      <path d="M8 11V8a4 4 0 0 1 8 0v3" />
    </svg>
  );
}

export function IconCalendarDate({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <rect x="4" y="5.5" width="16" height="14.5" rx="2" />
      <path d="M4 9.5h16M8 3.5v3.5M16 3.5v3.5" />
    </svg>
  );
}

export function IconPlay({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`fill-current ${className}`}>
      <path d="M8 5.5v13l11-6.5Z" />
    </svg>
  );
}

export function IconBell({ className = "w-4 h-4", active = false }: IconProps & { active?: boolean }) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <path d="M6 10a6 6 0 0 1 12 0c0 4.5 1.5 6 1.5 6h-15S6 14.5 6 10Z" />
      <path d="M10 19a2 2 0 0 0 4 0" />
      {!active && <path d="M4 4 20 20" />}
    </svg>
  );
}

export function IconRepeat({ className = "w-4 h-4" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 7h13a3 3 0 0 1 3 3v1" />
      <path d="M20 17H7a3 3 0 0 1-3-3v-1" />
      <path d="M7 4 4 7l3 3M17 20l3-3-3-3" />
    </svg>
  );
}

export function IconCheck({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={2.2} strokeLinecap="round" strokeLinejoin="round">
      <path d="M4.5 12.5 9.5 17.5 19.5 6.5" />
    </svg>
  );
}

export function IconTarget({ className = "w-5 h-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" className={`${BASE} ${className}`} strokeWidth={STROKE} strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="12" r="8.5" />
      <circle cx="12" cy="12" r="4.5" />
      <circle cx="12" cy="12" r="0.6" className="fill-current" />
    </svg>
  );
}
