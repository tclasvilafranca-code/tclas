interface IconProps {
  className?: string;
}

const base = {
  viewBox: "0 0 24 24",
  fill: "none",
  stroke: "currentColor",
  strokeWidth: 1.75,
  strokeLinecap: "round" as const,
  strokeLinejoin: "round" as const,
  "aria-hidden": "true" as const,
  focusable: "false" as const,
};

export function Flame({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M12 21.5c-4.1 0-7.3-2.8-7.3-6.8 0-3.8 2.6-6.7 3.9-10.2.5 2 1.8 3.6 3.1 3.6.9 0 1.6-.7 1.6-1.6 0-.5-.1-.9-.3-1.3 3 1.7 6.3 5.3 6.3 9.5 0 4-3.2 6.8-7.3 6.8Z" />
      <path d="M12 21.5c-1.9 0-3.4-1.3-3.4-3.2 0-1.9 1.4-3 2-4.6.3 1 .9 1.8 1.7 1.8.5 0 .9-.4.9-.9 0 1.9 2.2 2.9 2.2 4.9 0 1.9-1.5 3-3.4 3Z" />
    </svg>
  );
}

export function Star({ className = "h-5 w-5", filled = true }: IconProps & { filled?: boolean }) {
  return (
    <svg
      viewBox="0 0 24 24"
      fill={filled ? "currentColor" : "none"}
      stroke="currentColor"
      strokeWidth={1.5}
      strokeLinejoin="round"
      className={className}
      aria-hidden="true"
      focusable="false"
    >
      <path d="M12 3.2l2.7 5.6 6.1.7-4.5 4.3 1.2 6-5.5-3-5.5 3 1.2-6-4.5-4.3 6.1-.7L12 3.2Z" />
    </svg>
  );
}

export function CheckCircle({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="12" cy="12" r="8.5" />
      <path d="M8.3 12.3l2.4 2.4 5-5.4" />
    </svg>
  );
}

export function Target({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="12" cy="12" r="8" />
      <circle cx="12" cy="12" r="4.3" />
      <circle cx="12" cy="12" r="0.8" fill="currentColor" stroke="none" />
    </svg>
  );
}

export function Repeat({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M4.5 12a7.5 7.5 0 0 1 12.6-5.5M19.5 12a7.5 7.5 0 0 1-12.6 5.5" />
      <path d="M16.3 3.8v3.2h-3.2M7.7 20.2V17h3.2" />
    </svg>
  );
}

export function Medal({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="12" cy="14.5" r="5.2" />
      <path d="M9.3 9.8 7.2 3.3h3l1.8 4.7 1.8-4.7h3l-2.1 6.5" />
    </svg>
  );
}

export function Diamond({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M4.5 9 9 3.5h6L19.5 9 12 20.5 4.5 9Z" />
      <path d="M4.5 9h15M9 3.5 7.2 9l4.8 11.5M15 3.5 16.8 9l-4.8 11.5" />
    </svg>
  );
}

export function Clock({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="12" cy="12" r="8.5" />
      <path d="M12 7.5V12l3 2" />
    </svg>
  );
}

export function BookOpen({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M12 6.2c-1.6-1.4-3.7-2-6.2-2v12.6c2.5 0 4.6.6 6.2 2 1.6-1.4 3.7-2 6.2-2V4.2c-2.5 0-4.6.6-6.2 2Z" />
      <path d="M12 6.2v12.6" />
    </svg>
  );
}

export function Bolt({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" className={className} aria-hidden="true" focusable="false">
      <path d="M13.2 2 5 13.6h5.4l-1 8.4L18.6 10h-5.4l1-8Z" />
    </svg>
  );
}

export function Lock({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <rect x="5" y="10.5" width="14" height="9.5" rx="2" />
      <path d="M8 10.5V7.5a4 4 0 0 1 8 0v3" />
    </svg>
  );
}

export function XCircle({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="12" cy="12" r="8.5" />
      <path d="M9.3 9.3l5.4 5.4M14.7 9.3l-5.4 5.4" />
    </svg>
  );
}

export function Sign({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M12 3.5 21 19H3L12 3.5Z" />
      <path d="M12 10v4" />
      <circle cx="12" cy="16.5" r="0.6" fill="currentColor" stroke="none" />
    </svg>
  );
}

export function Overtake({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M4 8h11M15 8l-3-3M15 8l-3 3" />
      <path d="M20 16H9M9 16l3-3M9 16l3 3" />
    </svg>
  );
}

export function Parking({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <rect x="4" y="3.5" width="16" height="17" rx="2.5" />
      <path d="M9.5 16V8h3a2.6 2.6 0 0 1 0 5.2h-3" />
    </svg>
  );
}

export function Lightbulb({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M9 18h6M9.7 21h4.6" />
      <path d="M12 3a6 6 0 0 0-3.5 10.9c.6.4 1 1.1 1 1.9v.7h5v-.7c0-.8.4-1.5 1-1.9A6 6 0 0 0 12 3Z" />
    </svg>
  );
}

export function Drop({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M12 3.5c3 3.6 5.5 7 5.5 9.9a5.5 5.5 0 1 1-11 0c0-2.9 2.5-6.3 5.5-9.9Z" />
    </svg>
  );
}

export function Wrench({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M14.5 6.5a4 4 0 0 1-5 3.9L4.5 15.4a1.8 1.8 0 0 0 2.5 2.5l5-5a4 4 0 0 1 4-5.1l-2.6 2.6-2-2 2.6-2.6c.3-.1.6-.2 1-.3Z" />
    </svg>
  );
}

export function Radar({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="12" cy="12" r="1.1" fill="currentColor" stroke="none" />
      <path d="M12 12 17 8" />
      <path d="M8.5 8.5a5 5 0 0 1 7 0M6 6a8.5 8.5 0 0 1 12 0" />
    </svg>
  );
}

export function Child({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="12" cy="6" r="2.3" />
      <path d="M7 20v-4.5A3.5 3.5 0 0 1 10.5 12h3A3.5 3.5 0 0 1 17 15.5V20" />
    </svg>
  );
}

export function Users({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="9" cy="8" r="2.6" />
      <path d="M4 19v-1.5A3.5 3.5 0 0 1 7.5 14h3a3.5 3.5 0 0 1 3.5 3.5V19" />
      <path d="M15.2 6.3a2.6 2.6 0 0 1 0 5M17.8 14a3.4 3.4 0 0 1 2.2 3.2V19" />
    </svg>
  );
}

export function Leaf({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M5 19c0-7.5 5-13 14-13 0 9-5.5 14-14 13Z" />
      <path d="M5 19c3-3 6-6 9.5-10" />
    </svg>
  );
}

export function Road({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M9 3 5 21M15 3l4 18" />
      <path d="M12 3v3M12 10.5v3M12 18v3" />
    </svg>
  );
}

export function Scooter({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="6" cy="19" r="2" />
      <circle cx="18" cy="19" r="2" />
      <path d="M6 19h6.5L16 8.5h3M9 8.5h5.5" />
      <path d="M9 3.5h2.2" />
    </svg>
  );
}

export function ShieldCheck({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M12 3.3 19 6v5.5c0 4.5-3 7.6-7 9.2-4-1.6-7-4.7-7-9.2V6l7-2.7Z" />
      <path d="M9 12l2.1 2.1L15.5 10" />
    </svg>
  );
}

export function BarChart({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M4 20V10M12 20V4M20 20v-7" />
      <path d="M2.5 20h19" />
    </svg>
  );
}

export function Share({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <circle cx="18" cy="5.5" r="2.5" />
      <circle cx="6" cy="12" r="2.5" />
      <circle cx="18" cy="18.5" r="2.5" />
      <path d="M8.2 10.7 15.8 6.8M8.2 13.3l7.6 3.9" />
    </svg>
  );
}

export function Download({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <path d="M12 3v12" />
      <path d="M7 10.5 12 15.5 17 10.5" />
      <path d="M4.5 18.5h15" />
    </svg>
  );
}

export function Calendar({ className = "h-5 w-5" }: IconProps) {
  return (
    <svg {...base} className={className}>
      <rect x="3.5" y="5" width="17" height="15" rx="2.5" />
      <path d="M3.5 9.5h17" />
      <path d="M8 3v3.5M16 3v3.5" />
      <path d="M8 13.2h1.2M12 13.2h1.2M16 13.2h1.2M8 16.6h1.2M12 16.6h1.2" />
    </svg>
  );
}
