# -*- coding: utf-8 -*-
"""Cruza los sistemas de Eduard: entre sus 20 piezas, y contra José María,
   Josep, Luisa, Mercè, Nel e Isaac.

   Regla del proyecto: las CITAS literales de compases medidos pueden
   coincidir entre alumnos (es la misma partitura), pero el ANDAMIO inventado
   no.

   El motivo del cruce cambió en agosto de 2026, pero el cruce sigue haciendo
   falta. Antes, el álbum de Eduard era una copia del de José María y sus 19
   partituras eran el mismo archivo, byte a byte. Ahora su repertorio sale de
   SU carpeta de Drive y solo **siete** de las veinte comparten fichero con
   otro alumno: el Romance de Diabelli, America, el Star-Spangled Banner,
   Deck the Halls, Rasputin, el Grandfather's Clock y el Toreador. Esas siete
   son justo las que pueden repetir una cita literal —y deben—, y las que hay
   que vigilar para que no repitan andamio.

   Lo que separa a los alumnos automáticamente es la sal de
   `cancion._sal_alumno`, que cambia todas las hojas generadas. Lo que NO
   separa nadie es el material escrito a mano (el andamio de `piano1.bloques`
   y las `ficha.ritmos`), y eso es lo que comprueba este script.
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

EDUARD = ['ed_01_clementine', 'ed_02_aristogatos', 'ed_03_eso', 'ed_04_romance',
          'ed_05_america', 'ed_06_banner', 'ed_07_pantera', 'ed_08_nocturno',
          'ed_09_beginner', 'ed_10_heart', 'ed_11_dream', 'ed_12_deck',
          'ed_13_navidad', 'ed_14_greensleeves', 'ed_15_honor',
          'ed_16_rasputin', 'ed_17_jinglerock', 'ed_18_pianoman',
          'ed_19_clock', 'ed_20_toreador']

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

# Las SIETE partituras que Eduard comparte con otro alumno, byte a byte. Son
# las cuatro que se rescataron de su dosier antiguo (Romance, America,
# Star-Spangled y Deck the Halls) y las tres de su carpeta nueva que resultaron
# ser el mismo fichero que ya tenian otros (Rasputin, Grandfather's Clock y
# Toreador; comprobado por md5). Cada una puede recitar las mismas citas
# literales medidas que su gemela —es la misma musica—, y esas coincidencias SI
# son esperables. Las trece restantes son solo suyas.
COMPARTIDAS = ['Romance · Diabelli (José María 1 · Josep)',
               'America (José María 2)',
               'The Star-Spangled Banner (José María 3)',
               'Deck the Halls (José María 7 · Josep · Nel)',
               'Rasputin (José María 14 · Mercè · Josep · Luisa · Nel · Isaac)',
               "Grandfather's Clock (José María 9 · Mercè · Isaac)",
               'Toreador (José María 15 · Mercè · Nel · Isaac)']

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
for mod in EDUARD + OTROS:
    cfg = __import__(mod).CANCION
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    for nb, fn in cancion._hojas(cfg, qr):
        cur[0] = '%s/%s' % (mod, nb)
        fn(canvas.Canvas(os.devnull, pagesize=(W, H)))
        hojas += 1

print('Las partituras que Eduard comparte con otro alumno, byte a byte:')
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

# Las tres que quedan son CITAS LITERALES intencionadas, no andamio: Eduard y
# José María tienen el mismo archivo de partitura y el pasaje está MEDIDO
# sobre él. Cambiarle las notas a uno de los dos seria escribir mal a
# proposito, porque es la misma música.
#   · America cc. 1-4 (ed_05/jm_02, bloque 1): las alturas MEDIDAS, primero en
#     negras y despues con su ritmo con puntillo. Es la misma partitura y el
#     mismo pasaje: cambiarle las notas a uno de los dos seria escribir mal a
#     proposito. Los dos archivos la tienen marcada "Cita literal".
CITAS_LITERALES_OK = {
    frozenset(['ed_05_america/piano 1', 'jm_02_america/piano 1']),
}

inesperados = [(n, clef, refs) for n, clef, refs in entre_alumnos
               if frozenset(refs) not in CITAS_LITERALES_OK]
esperados = [(n, clef, refs) for n, clef, refs in entre_alumnos
             if frozenset(refs) in CITAS_LITERALES_OK]

print('\nEDUARD contra José María, Josep, Luisa, Mercè, Nel e Isaac · sistemas compartidos: %d'
      % len(entre_alumnos))
print('   de los cuales, citas literales esperadas (mismo pasaje medido): %d' % len(esperados))
for n, clef, refs in sorted(esperados, reverse=True):
    print('   [cita literal, OK] %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))
print('   y andamio inventado que coincide sin motivo (esto SÍ es un fallo): %d' % len(inesperados))
for n, clef, refs in sorted(inesperados, reverse=True):
    print('   [FALLO] %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

print('\nDentro de Eduard · sistemas repetidos entre piezas: %d' % len(dentro))
for n, clef, refs in sorted(dentro, reverse=True):
    print('   %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

sys.exit(1 if inesperados or dentro else 0)
