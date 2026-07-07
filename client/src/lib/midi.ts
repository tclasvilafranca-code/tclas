import { useEffect, useRef, useState } from "react";
import { midiToNoteName } from "./notes";

export type MidiStatus = "unsupported" | "unavailable" | "connecting" | "connected";

/** Conecta con un piano/teclado MIDI real via Web MIDI API, si el navegador lo soporta y el usuario lo autoriza. */
export function useMidiInput(onNoteOn: (note: string) => void) {
  const [status, setStatus] = useState<MidiStatus>("connecting");
  const [deviceName, setDeviceName] = useState<string | null>(null);
  const callbackRef = useRef(onNoteOn);
  callbackRef.current = onNoteOn;

  useEffect(() => {
    const nav = navigator as Navigator & { requestMIDIAccess?: (opts?: unknown) => Promise<any> };
    if (!nav.requestMIDIAccess) {
      setStatus("unsupported");
      return;
    }
    let access: any;
    nav
      .requestMIDIAccess()
      .then((midiAccess) => {
        access = midiAccess;
        const inputs = Array.from(midiAccess.inputs.values()) as any[];
        if (inputs.length > 0) {
          setDeviceName(inputs[0].name ?? "Teclado MIDI");
          setStatus("connected");
        } else {
          setStatus("unavailable");
        }
        const handleMessage = (event: any) => {
          const [command, note, velocity] = event.data;
          const isNoteOn = command === 144 && velocity > 0;
          if (isNoteOn) callbackRef.current(midiToNoteName(note));
        };
        midiAccess.inputs.forEach((input: any) => (input.onmidimessage = handleMessage));
        midiAccess.onstatechange = () => {
          const currentInputs = Array.from(midiAccess.inputs.values()) as any[];
          currentInputs.forEach((input) => (input.onmidimessage = handleMessage));
          if (currentInputs.length > 0) {
            setDeviceName(currentInputs[0].name ?? "Teclado MIDI");
            setStatus("connected");
          } else {
            setStatus("unavailable");
          }
        };
      })
      .catch(() => setStatus("unavailable"));

    return () => {
      if (access) access.onstatechange = null;
    };
  }, []);

  return { status, deviceName };
}
