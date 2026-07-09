import { describe, it, expect } from "vitest";
import { notesEqual, noteToMidi } from "./notes";

describe("notesEqual", () => {
  it("considera iguales dos notas enarmonicas (mismo tono, distinta escritura)", () => {
    expect(notesEqual("Bb4", "A#4")).toBe(true);
    expect(notesEqual("C#5", "Db5")).toBe(true);
    expect(notesEqual("F3", "F3")).toBe(true);
  });

  it("distingue notas realmente distintas", () => {
    expect(notesEqual("Bb4", "B4")).toBe(false);
    expect(notesEqual("C4", "C5")).toBe(false);
  });

  it("noteToMidi da el mismo valor para enarmonicos", () => {
    expect(noteToMidi("Bb4")).toBe(noteToMidi("A#4"));
  });
});
