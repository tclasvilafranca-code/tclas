# -*- coding: utf-8 -*-
"""Cruza los sistemas de Eduard: entre sus 19 piezas, y contra José María,
   Josep, Luisa, Mercè, Nel e Isaac.

   Regla del proyecto: las CITAS literales de compases medidos pueden
   coincidir entre alumnos (es la misma partitura), pero el ANDAMIO inventado
   no.

   Aquí hace falta más que en casi ningún otro álbum: **las 19 partituras de
   Eduard son el mismo archivo que las de José María, byte a byte** — se
   pidió expresamente "el mismo repertorio" y las fuentes se copiaron
   directamente de `students/jose_maria/source/` (ver
   TRANSCRIPCION_EDUARD_FUENTES.md). Lo que separa a los alumnos
   automáticamente es la sal de `cancion._sal_alumno`, que cambia todas las
   hojas generadas. Lo que NO separa nadie es el material escrito a mano
   (el andamio de `piano1.bloques` y las `ficha.ritmos`), y eso es lo que
   comprueba este script: que, salvo las citas literales ya conocidas y
   documentadas, el andamio de Eduard usa pitches propios.
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

EDUARD = ['ed_01_romance', 'ed_02_america', 'ed_03_banner', 'ed_04_counting',
          'ed_05_peaches', 'ed_06_someone', 'ed_07_deck', 'ed_08_jailhouse',
          'ed_09_clock', 'ed_10_shallow', 'ed_11_canthelp', 'ed_12_carol',
          'ed_13_adagio', 'ed_14_rasputin', 'ed_15_toreador', 'ed_16_trouble',
          'ed_17_acomme', 'ed_18_interstellar', 'ed_19_flying']

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
         'me_25_toreador', 'me_26_furelise', 'me_27_nocturne',
         'nl_01_petite', 'nl_02_counting', 'nl_03_deck', 'nl_04_heart',
         'nl_05_hittheroad', 'nl_06_jailhouse', 'nl_07_bellaciao', 'nl_08_canthelp',
         'nl_09_toreador', 'nl_10_lovely', 'nl_11_rasputin', 'nl_12_diamonds',
         'nl_13_favourite', 'nl_14_sweetchild', 'nl_15_merry', 'nl_16_acomme',
         'nl_17_dragon',
         'is_01_petite', 'is_02_saints', 'is_03_puff', 'is_04_beginner',
         'is_05_wewishyou', 'is_06_christmas', 'is_07_silentnight', 'is_08_silentnight4h',
         'is_09_panthere', 'is_10_pianoman', 'is_11_greensleeves', 'is_12_grandfather',
         'is_13_doremi', 'is_14_dream', 'is_15_gladiator', 'is_16_rasputin',
         'is_17_jailhouse', 'is_18_toreador', 'is_19_furelise', 'is_20_diabelli']

# Las 19 partituras que Eduard comparte con José María, byte a byte (repertorio
# idéntico, pedido así por el cliente). Cada una recita, además, las mismas
# citas literales medidas que su gemela jm_XX (silencios de entrada, la FRASE
# de America, el compás 12 de Jailhouse Rock...): esas coincidencias SÍ son
# esperables y no son un fallo. El resto de alumnos solo comparte partitura
# con José María pieza a pieza (ver TRANSCRIPCION_*_FUENTES.md de cada uno).
COMPARTIDAS = ['Romance · Diabelli (José María 1)', 'America (José María 2)',
               'The Star-Spangled Banner (José María 3)', 'Counting Stars (José María 4)',
               'Peaches (José María 5)', 'Someone You Loved (José María 6)',
               'Deck the Halls (José María 7)', 'Jailhouse Rock (José María 8 · Mercè · Josep · Nel)',
               "Grandfather's Clock (José María 9 · Mercè · Isaac)", 'Shallow (José María 10)',
               "Can't Help Falling in Love (José María 11 · Josep · Nel)",
               'Carol of the Bells (José María 12)', 'Adagio · Albinoni (José María 13)',
               'Rasputin (José María 14 · Mercè · Josep · Luisa · Nel · Isaac)',
               'Toreador (José María 15 · Mercè · Nel · Isaac)', 'Trouble (José María 16)',
               'A comme amour (José María 17 · Josep · Nel)', 'Interstellar (José María 18)',
               'Flying Theme (José María 19)']

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
for mod in EDUARD + OTROS:
    cfg = __import__(mod).CANCION
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    for nb, fn in cancion._hojas(cfg, qr):
        cur[0] = '%s/%s' % (mod, nb)
        fn(canvas.Canvas(os.devnull, pagesize=(W, H)))
        hojas += 1

print('Las 19 partituras que Eduard comparte con José María, byte a byte:')
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
    if 'ed' not in alumnos:
        continue
    if len(alumnos) > 1:
        entre_alumnos.append((len(k), clef, sorted(refs)))
    else:
        dentro.append((len(k), clef, sorted(refs)))

print('\nEDUARD contra José María, Josep, Luisa, Mercè, Nel e Isaac · sistemas compartidos: %d'
      % len(entre_alumnos))
for n, clef, refs in sorted(entre_alumnos, reverse=True):
    print('   %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

print('\nDentro de Eduard · sistemas repetidos entre piezas: %d' % len(dentro))
for n, clef, refs in sorted(dentro, reverse=True):
    print('   %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

sys.exit(1 if entre_alumnos or dentro else 0)
