# -*- coding: utf-8 -*-
"""Demos en WAV de les 3 cançons de Halloween (peques): melodia + acompanyament de la mà esquerra.
   Les notes es llegeixen de les mateixes fitxes (halloween_peques) per no duplicar dades."""
import os
import sys
import wave

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import halloween_peques as hp                                   # noqa: E402
from dibujo_mano import ManoCanvas                              # noqa: E402

SR = 22050
BPM = 92
NOTES = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def midi(p):
    alt = 0
    s = p[0]
    rest = p[1:]
    if rest[0] == '#':
        alt, rest = 1, rest[1:]
    elif rest[0] == 'b':
        alt, rest = -1, rest[1:]
    return 12 * (int(rest) + 1) + NOTES[s] + alt


def to(m, beats, vol=0.5):
    f = 440.0 * 2 ** ((m - 69) / 12.0)
    n = int(SR * beats * 60.0 / BPM)
    t = np.arange(n) / SR
    env = np.exp(-t * 2.2) * (1 - np.exp(-t * 90.0))
    y = sum(a * np.sin(2 * np.pi * f * k * t) for k, a in ((1, 1.0), (2, 0.45), (3, 0.25), (4, 0.12), (5, 0.06)))
    rel = np.minimum(1.0, (n - np.arange(n)) / (SR * 0.06))
    return vol * y * env * rel / 1.9


def clic():
    n = int(SR * 0.06)
    t = np.arange(n) / SR
    return 0.5 * np.sin(2 * np.pi * 1200 * t) * np.exp(-t * 60)


def mix(track, start_beats, y):
    i = int(SR * start_beats * 60.0 / BPM)
    if i + len(y) > len(track):
        track = np.pad(track, (0, i + len(y) - len(track)))
    track[i:i + len(y)] += y
    return track


def captura(fun):
    got = []
    orig = hp.pauta_cancio

    def spy(c, x, ytop, w, compassos, clau='treble', *a, **k):
        got.append((compassos, clau))
        return orig(c, x, ytop, w, compassos, clau, *a, **k)
    hp.pauta_cancio = spy
    c = ManoCanvas('/tmp/_aud.pdf', pagesize=(hp.W, hp.H))
    try:
        fun(c)
    finally:
        hp.pauta_cancio = orig
    return got


def melodia(compassos, vol=0.55):
    tr = np.zeros(1)
    b = 0.0
    for comp in compassos:
        pos = 0.0
        for (p, dur, sil, dit) in comp:
            if p:
                tr = mix(tr, b + pos, to(midi(p), dur * 0.98, vol))
            pos += dur
        b += 4.0
    return tr


def acompanyament(acords, vol=0.28):
    """acords: llista per compàs de (beat_dins_compàs, durada, [notes])."""
    tr = np.zeros(1)
    b = 0.0
    for comp in acords:
        for (pos, dur, notes) in comp:
            for n in notes:
                tr = mix(tr, b + pos, to(midi(n), dur, vol))
        b += 4.0
    return tr


def desa(nom, cap, repetir=2):
    cap = cap / max(1e-6, np.max(np.abs(cap))) * 0.8
    out = (cap * 32767).astype(np.int16)
    with wave.open(nom, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(out.tobytes())


def cançó(nom, compassos, acords, dest):
    mel = melodia(compassos)
    acc = acompanyament(acords)
    n = max(len(mel), len(acc))
    mel = np.pad(mel, (0, n - len(mel)))
    acc = np.pad(acc, (0, n - len(acc)))
    song = mel + acc
    comp_in = np.zeros(1)
    for k in range(4):
        comp_in = mix(comp_in, k, clic())
    pausa = np.zeros(int(SR * 1.2))
    total = np.concatenate([comp_in, song, pausa, song, pausa])
    desa(os.path.join(dest, nom), total)


def main():
    dest = os.path.join(HERE, '..', 'output', 'Halloween_Cancons_demo')
    os.makedirs(dest, exist_ok=True)
    c1, = captura(hp.fitxa_bruixa)
    am = ['A2', 'E3', 'C4']
    ev = ['E2', 'B2', 'G#3']
    cançó('2_La_bruixa_vola.wav', c1[0],
          [[(0, 4, am)], [(0, 4, ev)], [(0, 4, am)], [(0, 2, ev), (2, 2, am)]], dest)
    c2, = captura(hp.fitxa_fantasma)
    cançó('4_El_fantasma_Buuu.wav', c2[0],
          [[(0, 4, ['A2', 'E3'])], [(0, 4, ['A2', 'E3', 'C4'])], [(0, 4, ['A2', 'E3', 'C4'])],
           [(0, 4, ['A2', 'E3'])]], dest)
    cs = captura(hp.fitxa_esquelet)
    (comp_d, _), (comp_e, _) = cs
    acc = []
    for comp in comp_e:
        acc.append([(0, 4, [n[0] for n in comp])])
    cançó('5_Lesquelet_balla.wav', comp_d, acc, dest)
    print(dest, sorted(os.listdir(dest)))


if __name__ == '__main__':
    main()
