import { useEffect, useState } from "react";
import { AnimatedNumber } from "./AnimatedNumber";

export function ScoreRing({ percent, passed, size = 168 }: { percent: number; passed: boolean; size?: number }) {
  const [animatedPercent, setAnimatedPercent] = useState(0);
  const stroke = 12;
  const radius = (size - stroke) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (animatedPercent / 100) * circumference;

  useEffect(() => {
    const id = requestAnimationFrame(() => setAnimatedPercent(percent));
    return () => cancelAnimationFrame(id);
  }, [percent]);

  const color = passed ? "var(--color-t48-green-dark)" : "var(--color-t48-red)";

  return (
    <div className="relative inline-flex items-center justify-center" style={{ width: size, height: size }}>
      <svg width={size} height={size} className="-rotate-90">
        <circle cx={size / 2} cy={size / 2} r={radius} stroke="#f1f5f9" strokeWidth={stroke} fill="none" />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke={color}
          strokeWidth={stroke}
          fill="none"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          style={{ transition: "stroke-dashoffset 0.9s cubic-bezier(0.16, 1, 0.3, 1)" }}
        />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center">
        <span className="text-4xl font-extrabold tabular-nums text-t48-ink">
          <AnimatedNumber value={percent} duration={900} />%
        </span>
      </div>
    </div>
  );
}
