# -*- coding: utf-8 -*-
"""Cruza los sistemas de Luisa: entre sus 19 piezas, y contra José María y Josep.

   Regla del proyecto: las CITAS literales de compases medidos pueden coincidir
   entre alumnos (es la misma partitura), pero el ANDAMIO inventado no.

   Aquí hace falta porque **dos de las diecinueve partituras de Luisa son el
   mismo archivo que las de otro alumno**, byte a byte:

     - *Heart and Soul* — la pieza 6 de Josep;
     - *Rasputin* — la 14 de José María y la 13 de Josep.

   Lo que separa a los alumnos automáticamente es la sal de
   `cancion._sal_alumno`, que cambia todas las hojas generadas. Lo que no
   separa nadie es el material escrito a mano, y eso es lo que mira este
   script.

   Nota sobre el listón: Luisa es de iniciación y su andamio usa muchas negras
   y muchas notas de la escala de la tonalidad. Coincidir con otro alumno es
   más fácil aquí que en ningún otro cuaderno, así que el umbral se queda en
   ocho eventos, igual que en los demás, y no se sube para que salga limpio.
"""
import os
import sys
import tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))
import notation as nt
import segno
import cancion
from reportlab.pdfgen import canvas
from portada import W, H
import hoja_piano, ficha_info, hoja_calentamiento, hoja_lectura, hoja_relax
import hoja_taller, hoja_deberes

LUISA = ['lu_01_bambini', 'lu_02_beginner', 'lu_03_sonatina2', 'lu_04_friend',
         'lu_05_puff', 'lu_06_dream', 'lu_07_christmas', 'lu_08_silent',
         'lu_09_spring', 'lu_10_titanic', 'lu_11_pianoman', 'lu_12_panthere',
         'lu_13_belaciao', 'lu_14_heart', 'lu_15_greensleeves', 'lu_16_chimchim',
         'lu_17_rasputin', 'lu_18_furelise', 'lu_19_nocturne']

OTROS = ['jm_01_romance', 'jm_02_america', 'jm_03_banner', 'jm_04_counting',
         'jm_05_peaches', 'jm_06_someone', 'jm_07_deck', 'jm_08_jailhouse',
         'jm_09_clock', 'jm_10_shallow', 'jm_11_canthelp', 'jm_12_carol',
         'jm_13_adagio', 'jm_14_rasputin', 'jm_15_toreador', 'jm_16_trouble',
         'jm_17_acomme', 'jm_18_interstellar', 'jm_19_flying',
         'jp_01_romance', 'jp_02_petite', 'jp_03_peaches', 'jp_04_counting',
         'jp_05_what', 'jp_06_heart', 'jp_07_hittheroad', 'jp_08_deck',
         'jp_09_jailhouse', 'jp_10_bellaciao', 'jp_11_canthelp', 'jp_12_lovely',
         'jp_13_rasputin', 'jp_14_beginning', 'jp_15_favourite',
         'jp_16_sweetchild', 'jp_17_unbeso', 'jp_18_merry', 'jp_19_acomme']

# Las dos partituras que Luisa comparte con otro alumno, comprobadas con md5sum.
COMPARTIDAS = ['Heart and Soul (Josep 6)', 'Rasputin (José María 14 · Josep 13)']

MIN_EVENTOS = 8

orig = nt.draw_system
qr = os.path.join(tempfile.mkdtemp(), 'qr.png')
seqs, cur = {}, ['?']


def patched(c, x, top, w, gap, events, clef='treble', time_sig=(4, 4), show_clef=True,
            show_time=True, key_sig=None, spacing='linear', **extra):
    # `**extra` recoge lo que el motor fue ganando despues (repetir, casilla,
    # ottava...): sin eso, cada marca nueva rompia todos los cruces a la vez.
    # No anotar las pasadas de MEDICION de `hoja_piano` (la hoja se pagina y se
    # justifica dibujando antes sobre un lienzo que se tira): contarlas duplica
    # cada sistema y encima con la etiqueta de la hoja anterior.
    import hoja_piano
    # La tecnica comun (escalas, arpegios y cadencias de la tonalidad, que salen
    # de `relleno`) puede coincidir entre alumnos sin que eso sea un fallo: es
    # el mismo caso que una cita literal del mismo compas. Lo que se persigue
    # aqui es el andamio INVENTADO repetido sin motivo.
    if events and all(e.get('tecnica') for e in events):
        return orig(c, x, top, w, gap, events, clef=clef, time_sig=time_sig,
                    show_clef=show_clef, show_time=show_time, key_sig=key_sig,
                    spacing=spacing, **extra)
    if hoja_piano.MIDIENDO[0]:
        return orig(c, x, top, w, gap, events, clef=clef, time_sig=time_sig,
                    show_clef=show_clef, show_time=show_time, key_sig=key_sig,
                    spacing=spacing, **extra)
    k = tuple((e.get('pitch') or tuple(e.get('pitches', [])) or 'R', e['dur']) for e in events)
    if len(k) >= MIN_EVENTOS:
        seqs.setdefault((clef, k), set()).add(cur[0])
    return orig(c, x, top, w, gap, events, clef=clef, time_sig=time_sig,
                show_clef=show_clef, show_time=show_time, key_sig=key_sig,
                spacing=spacing, **extra)


nt.draw_system = patched
for m in (hoja_piano, ficha_info, hoja_calentamiento, hoja_lectura, hoja_relax,
          hoja_taller, hoja_deberes):
    if hasattr(m, 'draw_system'):
        m.draw_system = patched

hojas = 0
for mod in LUISA + OTROS:
    cfg = __import__(mod).CANCION
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    for nb, fn in cancion._hojas(cfg, qr):
        cur[0] = '%s/%s' % (mod, nb)
        fn(canvas.Canvas(os.devnull, pagesize=(W, H)))
        hojas += 1

print('Las partituras que Luisa comparte con otro alumno, byte a byte:')
for t in COMPARTIDAS:
    print('   · %s' % t)
print('\nhojas escaneadas: %d · sistemas distintos de >=%d eventos: %d'
      % (hojas, MIN_EVENTOS, len(seqs)))


def alumno(ref):
    return ref.split('_')[0]


def pieza_de(ref):
    return ref.split('/')[0]


entre_alumnos, dentro = [], []
for (clef, k), refs in seqs.items():
    piezas = {pieza_de(r) for r in refs}
    if len(piezas) < 2:
        continue
    alumnos = {alumno(p) for p in piezas}
    if 'lu' not in alumnos:
        continue
    if len(alumnos) > 1:
        entre_alumnos.append((len(k), clef, sorted(refs)))
    else:
        dentro.append((len(k), clef, sorted(refs)))

print('\nLUISA contra José María y Josep · sistemas compartidos: %d' % len(entre_alumnos))
for n, clef, refs in sorted(entre_alumnos, reverse=True):
    print('   %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

print('\nDentro de Luisa · sistemas repetidos entre piezas: %d' % len(dentro))
for n, clef, refs in sorted(dentro, reverse=True):
    print('   %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

sys.exit(1 if entre_alumnos or dentro else 0)
