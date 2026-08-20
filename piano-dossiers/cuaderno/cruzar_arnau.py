# -*- coding: utf-8 -*-
"""Cruza los sistemas de Arnau: entre sus 20 canciones, y contra Dilan y Eva.

   Regla del proyecto: las CITAS literales de compases medidos pueden coincidir
   entre alumnos (es la misma partitura), pero el ANDAMIO inventado no. Arnau no
   comparte ninguna pieza con Dilan ni con Eva, asi que cualquier coincidencia
   de >=8 eventos seria casual y hay que mirarla.
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

ARNAU = ['arnau_01_chopsticks', 'arnau_02_clementine', 'arnau_03_jolly',
         'arnau_04_ears', 'arnau_05_wheels', 'arnau_06_saints',
         'arnau_07_wewish', 'arnau_08_baabaa', 'arnau_09_polly',
         'arnau_10_muffet', 'arnau_11_eso', 'arnau_12_puff',
         'arnau_13_pantera', 'arnau_14_bonnie', 'arnau_15_largo',
         'arnau_16_aloha', 'arnau_17_popeye', 'arnau_18_submarino',
         'arnau_19_rain', 'arnau_20_mulberry']
OTROS = ['dilan_01_cancion', 'dilan_02_cancion', 'dilan_03_your_song',
         'dilan_04_thinking', 'dilan_05_lucia', 'dilan_06_poema',
         'dilan_07_amiga', 'dilan_08_promesa', 'dilan_09_bruno',
         'dilan_10_calor', 'dilan_11_soldadito', 'dilan_12_sky',
         'dilan_13_what', 'dilan_14_writings', 'dilan_15_favourite',
         'dilan_16_adagio', 'dilan_17_arabesque', 'dilan_18_merry',
         'dilan_19_santa', 'dilan_20_beginning',
         'eva_01_canthelp', 'eva_02_sky', 'eva_03_poema', 'eva_04_what',
         'eva_05_thinking', 'eva_06_cisne', 'eva_07_bruno', 'eva_08_promesa',
         'eva_09_amiga', 'eva_10_young', 'eva_11_soldadito',
         'eva_12_favourite', 'eva_13_merry', 'eva_14_santa',
         'eva_15_beginning', 'eva_16_arabesque', 'eva_17_bohemian']

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
for mod in ARNAU + OTROS:
    cfg = __import__(mod).CANCION
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    for nb, fn in cancion._hojas(cfg, qr):
        cur[0] = '%s/%s' % (mod, nb)
        fn(canvas.Canvas(os.devnull, pagesize=(W, H)))
        hojas += 1

print('hojas escaneadas: %d · sistemas distintos de >=%d eventos: %d'
      % (hojas, MIN_EVENTOS, len(seqs)))


def alumno(ref):
    return ref.split('_')[0]


def cancion_de(ref):
    return ref.split('/')[0]


choques_alumno, choques_arnau = [], []
for (clef, k), refs in seqs.items():
    piezas = {cancion_de(r) for r in refs}
    if len(piezas) < 2:
        continue
    alumnos = {alumno(p) for p in piezas}
    tiene_arnau = 'arnau' in alumnos
    if len(alumnos) > 1 and tiene_arnau:
        choques_alumno.append((len(k), clef, sorted(refs)))
    elif tiene_arnau:
        choques_arnau.append((len(k), clef, sorted(refs)))

print('\nARNAU contra Dilan/Eva · sistemas compartidos: %d' % len(choques_alumno))
for n, clef, refs in sorted(choques_alumno, reverse=True):
    print('   %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

print('\nDentro de Arnau · sistemas repetidos entre canciones: %d' % len(choques_arnau))
for n, clef, refs in sorted(choques_arnau, reverse=True):
    print('   %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))
