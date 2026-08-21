# -*- coding: utf-8 -*-
"""Comprueba que el TEMPO que la ficha presenta como dato de la pieza es el que
   trae impreso la partitura.

   Cuarto dato que el dosier afirma sobre el papel, despues del compas, la
   armadura y la figura mas corta. Es el menos grave de los cuatro —un
   metronomo mal puesto es una molestia, no un aprendizaje torcido— pero se
   equivoca igual de facil, y ademas manda sobre la ESCALERA de velocidad: si
   la meta dice 124 y la partitura pone 96, el alumno se pasa el curso
   persiguiendo un numero que no existe.

   COMO SE COMPRUEBA. La mayoria de estas partituras son PDF con texto de
   verdad, asi que el numero se saca con `pdftotext` y se cruza solo: no hace
   falta tabla ni acordarse de nada. Las que son un escaneo no dan texto, y
   esas van en `MIRADAS`, con lo que se leyo al ampliarlas.

   Las 69 piezas que citan un tempo se comprobaron el 21 de agosto de 2026 y
   coincidian TODAS. Tambien se miraron las nueve que dicen lo contrario —"tu
   partitura no trae numero de metronomo"— y ninguna lo trae.

   Uso:  python3 auditar_tempo.py            (todos)
         python3 auditar_tempo.py arnau lu   (solo esos prefijos)
"""
import contextlib
import glob
import importlib
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'dilan', 'eva']

NUM = re.compile(r'(\d{2,3})')
# El signo de negra es un glifo de fuente musical y casi nunca se extrae; el
# "= 96" que va detras, si.
IMPRESO = re.compile(r'[=＝]\s*(\d{2,3})')

# Partituras que no dan texto (son un escaneo) y el tempo que se LEYO en ellas
# al ampliarlas. Igual que `auditar_figuras.MIRADAS`: mirarlas y no anotar el
# resultado seria mirarlas para nada.
MIRADAS = {
    'i-have-a-dream-abba-children-song.pdf': [120],   # pone "TEMPO-120", sin el signo
    'i-have-a-dream-abba-.pdf': [120],
    'ADAGIO.': [60],                                # "Adagio ♩ = 60"
    'Rasputin.pdf': [124],
    'christmas-songs-for-four-little- 4 manos.pdf': [100],
    'christmas-songs-( 4 manos).pdf': [100],
    'Piano Men.pdf': [178],
    'BELLA Y BESTIA .pdf': [80],
    'Jailhouse Elvis Presley.pdf': [150],           # "♩ = 150  Swing"
    'Petite chanson.(4 MANOS)': [80],               # "♩ = 80 andante"
    'petite chanson.(4 manos)': [80],
    'heart-and-soul-.pdf': [110],                   # "♩ = 110 Swing"
    '-LOVELY.pdf': [115],
    'LOVELY.': [115],
    'Merry-go-round-of-life-easy-piano-.pdf': [120, 152],
    'Copia de Copia de  A COMME AMOUR _ Richard Clayderman.': [69],
    'THINKING OUT LOUD _ Ed Sheeran .pdf': [145],
}


def _cfg(modulo):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        mod = importlib.import_module(modulo)
    return getattr(mod, 'CANCION', None)


def impresos(ruta):
    """Los numeros de metronomo que trae escritos la partitura, o None si no se
       puede saber (un escaneo sin texto)."""
    base = os.path.basename(ruta)
    if base in MIRADAS:
        return MIRADAS[base]
    if not os.path.exists(ruta):
        return None
    try:
        texto = subprocess.run(['pdftotext', '-q', ruta, '-'],
                               capture_output=True, text=True, timeout=40).stdout
    except Exception:                                            # noqa: BLE001
        return None
    if not texto.strip():
        return None
    return sorted(set(int(x) for x in IMPRESO.findall(texto)))


def main(prefijos=None):
    prefijos = prefijos or PREFIJOS
    malos, sin_saber = [], []
    n = 0
    cache = {}
    for p in prefijos:
        for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py'))):
            m = os.path.basename(f)[:-3]
            cfg = _cfg(m)
            if not cfg:
                continue
            datos = dict((k, v) for k, v in (cfg.get('ficha') or {}).get('datos', []) or [])
            t = datos.get('Tempo')
            if not t:
                continue
            dice = [int(x) for x in NUM.findall(t)]
            if not dice:
                continue          # "Lento", "Allegretto": palabra, no numero
            n += 1
            ruta = cfg.get('partitura') or ''
            if ruta not in cache:
                cache[ruta] = impresos(ruta)
            trae = cache[ruta]
            if trae is None:
                sin_saber.append((m, t, os.path.basename(ruta)))
            elif not set(dice) & set(trae):
                malos.append((m, t, trae, os.path.basename(ruta)))

    print('piezas que citan un tempo con número: %d' % n)

    print('\nLA FICHA DICE UN TEMPO Y LA PARTITURA TRAE OTRO: %d' % len(malos))
    for m, t, trae, base in malos:
        print('   %-22s ficha %-18r partitura %s · %s' % (m, t, trae, base[:30]))

    print('\nPartituras cuyo tempo no se puede sacar ni está en MIRADAS: %d' % len(sin_saber))
    for m, t, base in sin_saber:
        print('   %-22s %-18r %s' % (m, t, base[:40]))

    if malos or sin_saber:
        print('\n%d COSAS QUE MIRAR' % (len(malos) + len(sin_saber)))
        return 1
    print('\nTEMPOS OK — el número que cita la ficha es el que trae impreso el papel.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
