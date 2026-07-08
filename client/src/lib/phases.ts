import type { ExercisePhase } from "./api";

export const PHASE_LABEL: Record<ExercisePhase, { label: string; className: string }> = {
  VISUAL_AGILITY: { label: "👁️ Agilidad visual", className: "bg-tclas-gold/15 text-tclas-plum" },
  EAR_ACUITY: { label: "👂 Agudeza auditiva", className: "bg-tclas-plum/10 text-tclas-plum" },
  NOTE_RUSH: { label: "⚡ Notas al vuelo", className: "bg-tclas-rose/15 text-tclas-rose" },
  SHEET_PRACTICE: { label: "🎼 Práctica de partitura", className: "bg-tclas-sage/15 text-tclas-sage" },
};

export const PHASE_ORDER: ExercisePhase[] = ["VISUAL_AGILITY", "EAR_ACUITY", "NOTE_RUSH", "SHEET_PRACTICE"];
