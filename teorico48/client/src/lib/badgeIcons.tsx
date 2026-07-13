import type { ReactNode } from "react";
import { BookOpen, CheckCircle, Diamond, Flame, Medal, Star, Target } from "../components/Icons";

const ICONS: Record<string, ReactNode> = {
  "primer-test": <Target className="h-4 w-4" />,
  "primer-aprobado": <CheckCircle className="h-4 w-4" />,
  "racha-3": <Flame className="h-4 w-4" />,
  "racha-7": <Flame className="h-4 w-4" />,
  "xp-100": <Star className="h-4 w-4" filled={false} />,
  "xp-500": <Star className="h-4 w-4" />,
  "xp-1000": <Diamond className="h-4 w-4" />,
  perfecto: <Medal className="h-4 w-4" />,
  "diez-tests": <BookOpen className="h-4 w-4" />,
};

export function badgeIcon(id: string): ReactNode {
  return ICONS[id] ?? <Star className="h-4 w-4" filled={false} />;
}
