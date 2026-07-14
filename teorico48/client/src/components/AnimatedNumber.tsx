import { useEffect, useRef, useState } from "react";

/** Anima un número contando desde 0 (o el valor anterior) hasta el valor final. */
export function AnimatedNumber({ value, duration = 700, className }: { value: number; duration?: number; className?: string }) {
  const [display, setDisplay] = useState(value);
  const prevValue = useRef(value);
  const frameRef = useRef<number | null>(null);

  useEffect(() => {
    const from = prevValue.current;
    const to = value;
    if (from === to) return;
    const start = performance.now();

    function tick(now: number) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setDisplay(Math.round(from + (to - from) * eased));
      if (progress < 1) {
        frameRef.current = requestAnimationFrame(tick);
      } else {
        prevValue.current = to;
      }
    }
    frameRef.current = requestAnimationFrame(tick);
    return () => {
      if (frameRef.current) cancelAnimationFrame(frameRef.current);
    };
  }, [value, duration]);

  return <span className={className}>{display}</span>;
}
