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
