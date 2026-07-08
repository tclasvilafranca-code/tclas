import { describe, it, expect } from "vitest";
import { gradeExercise, sanitizeExerciseData, starsForScore } from "./gamification";

describe("gradeExercise", () => {
  it("NOTE_NAME acepta la respuesta correcta sin importar mayusculas", () => {
    const data = { correctAnswer: "Do" };
    expect(gradeExercise("NOTE_NAME", data, "do")).toBe(true);
    expect(gradeExercise("NOTE_NAME", data, "Re")).toBe(false);
  });

  it("KEYBOARD_PLAY exige la secuencia exacta de notas, en orden", () => {
    const data = { notes: ["C4", "D4", "E4"] };
    expect(gradeExercise("KEYBOARD_PLAY", data, ["C4", "D4", "E4"])).toBe(true);
    expect(gradeExercise("KEYBOARD_PLAY", data, ["c4", "d4", "e4"])).toBe(true);
    expect(gradeExercise("KEYBOARD_PLAY", data, ["D4", "C4", "E4"])).toBe(false);
    expect(gradeExercise("KEYBOARD_PLAY", data, ["C4", "D4"])).toBe(false);
  });

  it("RHYTHM_TAP tiene tolerancia generosa (no exige precision de metronomo)", () => {
    const data = { pattern: [1, 1, 2] };
    expect(gradeExercise("RHYTHM_TAP", data, [1.2, 0.85, 2.3])).toBe(true);
    expect(gradeExercise("RHYTHM_TAP", data, [1, 1, 1])).toBe(false);
    expect(gradeExercise("RHYTHM_TAP", data, [1, 1])).toBe(false);
  });

  it("HOLD_NOTE acepta manterner al menos el 60% de la duracion exigida", () => {
    const data = { note: "C4", beats: 2, bpm: 60 }; // 2 beats a 60bpm = 2000ms exigidos
    expect(gradeExercise("HOLD_NOTE", data, { note: "C4", heldMs: 1250 })).toBe(true); // 62.5%
    expect(gradeExercise("HOLD_NOTE", data, { note: "C4", heldMs: 1000 })).toBe(false); // 50%
    expect(gradeExercise("HOLD_NOTE", data, { note: "D4", heldMs: 2000 })).toBe(false);
  });

  it("WRITE_ANSWER normaliza acentos, mayusculas y espacios", () => {
    const data = { correctAnswer: "Fa Sostenido", acceptableAnswers: ["Fa#"] };
    expect(gradeExercise("WRITE_ANSWER", data, "  fa sostenido ")).toBe(true);
    expect(gradeExercise("WRITE_ANSWER", data, "FA#")).toBe(true);
    expect(gradeExercise("WRITE_ANSWER", data, "sol")).toBe(false);
  });

  it("SEGMENT_PRACTICE aplana los tramos antes de comparar", () => {
    const data = { segments: [["C4", "D4"], ["E4"]] };
    expect(gradeExercise("SEGMENT_PRACTICE", data, ["C4", "D4", "E4"])).toBe(true);
    expect(gradeExercise("SEGMENT_PRACTICE", data, ["C4", "E4", "D4"])).toBe(false);
  });

  it("un tipo desconocido nunca da por buena la respuesta", () => {
    expect(gradeExercise("NOPE" as any, {}, "cualquier cosa")).toBe(false);
  });
});

describe("sanitizeExerciseData", () => {
  it("quita la respuesta correcta antes de mandarla al cliente", () => {
    const data = { correctAnswer: "Do", options: ["Do", "Re", "Mi"] };
    const clean = sanitizeExerciseData("NOTE_NAME", data);
    expect(clean.correctAnswer).toBeUndefined();
  });

  it("baraja las opciones de multiple-choice para evitar memorizar la posicion", () => {
    const options = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"];
    const data = { correctAnswer: "Do", options };
    const orders = new Set<string>();
    for (let i = 0; i < 30; i++) {
      const clean = sanitizeExerciseData("THEORY_MCQ", { ...data, options: [...options] });
      expect([...clean.options].sort()).toEqual([...options].sort()); // mismo contenido, sin mutar el original
      orders.add(clean.options.join(","));
    }
    expect(orders.size).toBeGreaterThan(1); // el orden realmente varia entre llamadas
  });

  it("MATCHING nunca manda los pares ya emparejados", () => {
    const data = { pairs: [{ left: "STAFF:C4", right: "Do" }, { left: "STAFF:D4", right: "Re" }] };
    const clean = sanitizeExerciseData("MATCHING", data);
    expect(clean.pairs).toBeUndefined();
    expect(clean.leftItems).toEqual(["STAFF:C4", "STAFF:D4"]);
    expect(clean.rightItems.sort()).toEqual(["Do", "Re"]);
  });

  it("DRAG_STAFF quita la nota objetivo", () => {
    const clean = sanitizeExerciseData("DRAG_STAFF", { targetNote: "C4", clef: "treble" });
    expect(clean.targetNote).toBeUndefined();
  });
});

describe("starsForScore", () => {
  it("mapea el porcentaje de acierto a 0-3 estrellas", () => {
    expect(starsForScore(1)).toBe(3);
    expect(starsForScore(0.85)).toBe(2);
    expect(starsForScore(0.5)).toBe(1);
    expect(starsForScore(0.1)).toBe(0);
  });
});
