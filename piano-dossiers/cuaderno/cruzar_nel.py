# -*- coding: utf-8 -*-
"""Cruza los sistemas de Nel: entre sus 17 piezas, y contra José María,
   Josep, Luisa y Mercè.

   Regla del proyecto: las CITAS literales de compases medidos pueden
   coincidir entre alumnos (es la misma partitura), pero el ANDAMIO inventado
   no.

   Aquí hace falta más que en casi ningún otro álbum: **16 de las 17
   partituras de Nel son el mismo archivo que las de otro alumno**, byte a
   byte — comprobado con `md5sum` sobre `students/*/source/` (ver
   TRANSCRIPCION_NEL_FUENTES.md para la tabla completa). El repertorio de Nel
   es, pieza a pieza, casi el mismo que el de Josep (14 de 17), con tres
   añadidas de José María. Lo que separa a los alumnos automáticamente es la
   sal de `cancion._sal_alumno`, que cambia todas las hojas generadas. Lo que
   NO separa nadie es el material escrito a mano, y eso es lo que comprueba
   este script.
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

NEL = ['nl_01_petite', 'nl_02_counting', 'nl_03_deck', 'nl_04_heart',
       'nl_05_hittheroad', 'nl_06_jailhouse', 'nl_07_bellaciao', 'nl_08_canthelp',
       'nl_09_toreador', 'nl_10_lovely', 'nl_11_rasputin', 'nl_12_diamonds',
       'nl_13_favourite', 'nl_14_sweetchild', 'nl_15_merry', 'nl_16_acomme',
       'nl_17_dragon']

OTROS = ['jm_01_romance', 'jm_02_america', 'jm_03_banner', 'jm_04_counting',
         'jm_05_peaches', 'jm_06_someone', 'jm_07_deck', 'jm_08_jailhouse',
         'jm_09_clock', 'jm_10_shallow', 'jm_11_canthelp', 'jm_12_carol',
         'jm_13_adagio', 'jm_14_rasputin', 'jm_15_toreador', 'jm_16_trouble',
         'jm_17_acomme', 'jm_18_interstellar', 'jm_19_flying',
         'jp_01_romance', 'jp_02_petite', 'jp_03_peaches', 'jp_04_counting',
         'jp_05_what', 'jp_06_heart', 'jp_07_hittheroad', 'jp_08_deck',
         'jp_09_jailhouse', 'jp_10_bellaciao', 'jp_11_canthelp', 'jp_12_lovely',
         'jp_13_rasputin', 'jp_14_beginning', 'jp_15_favourite',
         'jp_16_sweetchild', 'jp_17_unbeso', 'jp_18_merry', 'jp_19_acomme',
         'lu_01_bambini', 'lu_02_beginner', 'lu_03_sonatina2', 'lu_04_friend',
         'lu_05_puff', 'lu_06_dream', 'lu_07_christmas', 'lu_08_silent',
         'lu_09_spring', 'lu_10_titanic', 'lu_11_pianoman', 'lu_12_panthere',
         'lu_13_belaciao', 'lu_14_heart', 'lu_15_greensleeves', 'lu_16_chimchim',
         'lu_17_rasputin', 'lu_18_furelise', 'lu_19_nocturne',
         'me_01_bambini', 'me_02_saints', 'me_03_friend', 'me_04_puff',
         'me_05_sonatina2', 'me_06_avignon', 'me_07_doremi', 'me_08_christmas',
         'me_09_silentnight', 'me_10_wewishyou', 'me_11_silentnight4h', 'me_12_panthere',
         'me_13_pianoman', 'me_14_belaciao', 'me_15_spring', 'me_16_greensleeves',
         'me_17_countingstars', 'me_18_largodvorak', 'me_19_grandfather', 'me_20_dream',
         'me_21_beauty', 'me_22_gladiator', 'me_23_rasputin', 'me_24_jailhouse',
         'me_25_toreador', 'me_26_furelise', 'me_27_nocturne']

# Las 16 partituras que Nel comparte con otro alumno, comprobadas con md5sum.
COMPARTIDAS = ["Can't Help Falling in Love (José María 11 · Josep 11)",
               'A comme amour (José María 17 · Josep 19)',
               'Flying Theme (José María 19)',
               'Toreador (José María 15 · Mercè 25)',
               'Counting Stars (José María 4 · Josep 4 · Mercè 17)',
               'Deck the Halls (José María 7 · Josep 8)',
               'Lovely (Josep 12)', 'Merry Go Round of Life (Josep 18)',
               'Rasputin (José María 14 · Josep 13 · Luisa 17 · Mercè 23)',
               'Bella Ciao (Josep 10)', 'Heart and Soul (Luisa 14 · Josep 6)',
               'Hit the Road Jack (Josep 7)',
               'Jailhouse Rock (José María 8 · Josep 9 · Mercè 24)',
               'My Favourite Things (Josep 15)', 'Petite Chanson (Josep 2)',
               "Sweet Child O' Mine (Josep 16)"]

MIN_EVENTOS = 8

orig = nt.draw_system
qr = os.path.join(tempfile.mkdtemp(), 'qr.png')
seqs, cur = {}, ['?']


def patched(c, x, top, w, gap, events, clef='treble', time_sig=(4, 4), show_clef=True,
            show_time=True, key_sig=None, spacing='linear'):
    k = tuple((e.get('pitch') or tuple(e.get('pitches', [])) or 'R', e['dur']) for e in events)
    if len(k) >= MIN_EVENTOS:
        seqs.setdefault((clef, k), set()).add(cur[0])
    return orig(c, x, top, w, gap, events, clef=clef, time_sig=time_sig,
                show_clef=show_clef, show_time=show_time, key_sig=key_sig, spacing=spacing)


nt.draw_system = patched
for m in (hoja_piano, ficha_info, hoja_calentamiento, hoja_lectura, hoja_relax,
          hoja_taller, hoja_deberes):
    if hasattr(m, 'draw_system'):
        m.draw_system = patched

hojas = 0
for mod in NEL + OTROS:
    cfg = __import__(mod).CANCION
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    for nb, fn in cancion._hojas(cfg, qr):
        cur[0] = '%s/%s' % (mod, nb)
        fn(canvas.Canvas(os.devnull, pagesize=(W, H)))
        hojas += 1

print('Las 16 partituras que Nel comparte con otro alumno, byte a byte:')
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
    if 'nl' not in alumnos:
        continue
    if len(alumnos) > 1:
        entre_alumnos.append((len(k), clef, sorted(refs)))
    else:
        dentro.append((len(k), clef, sorted(refs)))

# Estas dos coincidencias son CITAS LITERALES intencionadas, no andamio: la
# regla del proyecto las permite porque los dos alumnos tienen el mismo
# archivo de partitura y el pasaje citado está MEDIDO sobre él (no inventado).
#   · Heart and Soul cc. 1-2 (jp_06_heart/nl_04_heart, "piano 1" bloque 1a):
#     el compás 1 medido nota a nota, marcado "MEDIDO... no es andamio".
#   · Jailhouse Rock c. 12 (jm_08_jailhouse/nl_06_jailhouse, "piano 1" bloque 3a):
#     la subida de la izquierda con digitación 5-3-2-1 impresa, medida sobre
#     la partitura real.
CITAS_LITERALES_OK = {
    frozenset(['jp_06_heart/piano 1', 'nl_04_heart/piano 1']),
    frozenset(['jm_08_jailhouse/piano 1', 'nl_06_jailhouse/piano 1']),
}

inesperados = [(n, clef, refs) for n, clef, refs in entre_alumnos
               if frozenset(refs) not in CITAS_LITERALES_OK]
esperados = [(n, clef, refs) for n, clef, refs in entre_alumnos
             if frozenset(refs) in CITAS_LITERALES_OK]

print('\nNEL contra José María, Josep, Luisa y Mercè · sistemas compartidos: %d' % len(entre_alumnos))
print('   de los cuales, citas literales esperadas (mismo pasaje medido): %d' % len(esperados))
for n, clef, refs in sorted(esperados, reverse=True):
    print('   [cita literal, OK] %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))
print('   y andamio inventado que coincide sin motivo (esto SÍ es un fallo): %d' % len(inesperados))
for n, clef, refs in sorted(inesperados, reverse=True):
    print('   [FALLO] %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

print('\nDentro de Nel · sistemas repetidos entre piezas: %d' % len(dentro))
for n, clef, refs in sorted(dentro, reverse=True):
    print('   %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

sys.exit(1 if inesperados or dentro else 0)
