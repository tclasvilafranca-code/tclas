# -*- coding: utf-8 -*-
"""Cruza los sistemas de Aida: entre sus 19 piezas, y contra los otros diez
   alumnos del proyecto.

   Regla del proyecto: las CITAS literales de compases medidos pueden coincidir
   entre alumnos (es la misma partitura), pero el ANDAMIO inventado no.

   Aida es la alumna que MAS partituras comparte de todo el cuaderno: diez de
   sus diecinueve son el mismo archivo, byte a byte, que las de otro alumno
   (comprobado por md5). Eso hace que este cruce no sea opcional. Lo que separa
   a los alumnos automaticamente es la sal de `cancion._sal_alumno`, que cambia
   todas las hojas generadas; lo que NO separa nadie es el material escrito a
   mano (el andamio de `piano1.bloques` y las `ficha.ritmos`), y eso es lo que
   comprueba este script.
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

AIDA = ['ai_01_romance', 'ai_02_scherzo', 'ai_03_wewishyou', 'ai_04_canthelp',
        'ai_05_what', 'ai_06_counting', 'ai_07_perfect', 'ai_08_boig',
        'ai_09_kiss', 'ai_10_beginning', 'ai_11_titanic', 'ai_12_hijoluna',
        'ai_13_carol', 'ai_14_silence', 'ai_15_gladiator', 'ai_16_unbeso',
        'ai_17_pachelbel', 'ai_18_preludio', 'ai_19_acomme']

OTROS = ['arnau_01_chopsticks', 'arnau_02_clementine', 'arnau_03_jolly',
         'arnau_04_ears', 'arnau_05_wheels', 'arnau_06_saints', 'arnau_07_wewish',
         'arnau_08_baabaa', 'arnau_09_polly', 'arnau_10_muffet', 'arnau_11_eso',
         'arnau_12_puff', 'arnau_13_pantera', 'arnau_14_bonnie', 'arnau_15_largo',
         'arnau_16_aloha', 'arnau_17_popeye', 'arnau_18_submarino',
         'arnau_19_rain', 'arnau_20_mulberry', 'dilan_01_cancion', 'dilan_01_data',
         'dilan_02_cancion', 'dilan_02_data', 'dilan_03_your_song',
         'dilan_04_thinking', 'dilan_05_lucia', 'dilan_06_poema', 'dilan_07_amiga',
         'dilan_08_promesa', 'dilan_09_bruno', 'dilan_10_calor',
         'dilan_11_soldadito', 'dilan_12_sky', 'dilan_13_what',
         'dilan_14_writings', 'dilan_15_favourite', 'dilan_16_adagio',
         'dilan_17_arabesque', 'dilan_18_merry', 'dilan_19_santa',
         'dilan_20_beginning', 'ed_01_clementine', 'ed_02_aristogatos',
         'ed_03_eso', 'ed_04_america', 'ed_05_banner', 'ed_06_pantera',
         'ed_07_nocturno', 'ed_08_beginner', 'ed_09_puff', 'ed_10_heart',
         'ed_11_dream', 'ed_12_navidad', 'ed_13_greensleeves', 'ed_14_honor',
         'ed_15_rasputin', 'ed_16_jinglerock', 'ed_17_pianoman', 'ed_18_clock',
         'ed_19_toreador', 'eva_01_canthelp', 'eva_02_sky', 'eva_03_poema',
         'eva_04_what', 'eva_05_thinking', 'eva_06_cisne', 'eva_07_bruno',
         'eva_08_promesa', 'eva_09_amiga', 'eva_10_young', 'eva_11_soldadito',
         'eva_12_favourite', 'eva_13_merry', 'eva_14_santa', 'eva_15_beginning',
         'eva_16_arabesque', 'eva_17_bohemian', 'is_01_petite', 'is_02_saints',
         'is_03_puff', 'is_04_beginner', 'is_05_wewishyou', 'is_06_christmas',
         'is_07_silentnight', 'is_08_silentnight4h', 'is_09_panthere',
         'is_10_pianoman', 'is_11_greensleeves', 'is_12_grandfather',
         'is_13_doremi', 'is_14_dream', 'is_15_gladiator', 'is_16_rasputin',
         'is_17_jailhouse', 'is_18_toreador', 'is_19_furelise', 'is_20_diabelli',
         'jm_01_romance', 'jm_02_america', 'jm_03_banner', 'jm_04_counting',
         'jm_05_peaches', 'jm_06_someone', 'jm_07_deck', 'jm_08_jailhouse',
         'jm_09_clock', 'jm_10_shallow', 'jm_11_canthelp', 'jm_12_carol',
         'jm_13_adagio', 'jm_14_rasputin', 'jm_15_toreador', 'jm_16_trouble',
         'jm_17_acomme', 'jm_18_interstellar', 'jm_19_flying', 'jp_01_romance',
         'jp_02_petite', 'jp_03_peaches', 'jp_04_counting', 'jp_05_what',
         'jp_06_heart', 'jp_07_hittheroad', 'jp_08_deck', 'jp_09_jailhouse',
         'jp_10_bellaciao', 'jp_11_canthelp', 'jp_12_lovely', 'jp_13_rasputin',
         'jp_14_beginning', 'jp_15_favourite', 'jp_16_sweetchild', 'jp_17_unbeso',
         'jp_18_merry', 'jp_19_acomme', 'lu_01_bambini', 'lu_02_beginner',
         'lu_03_sonatina2', 'lu_04_friend', 'lu_05_puff', 'lu_06_dream',
         'lu_07_christmas', 'lu_08_silent', 'lu_09_spring', 'lu_10_titanic',
         'lu_11_pianoman', 'lu_12_panthere', 'lu_13_belaciao', 'lu_14_heart',
         'lu_15_greensleeves', 'lu_16_chimchim', 'lu_17_rasputin',
         'lu_18_furelise', 'lu_19_nocturne', 'me_01_bambini', 'me_02_saints',
         'me_03_friend', 'me_04_puff', 'me_05_sonatina2', 'me_06_avignon',
         'me_07_doremi', 'me_08_christmas', 'me_09_silentnight', 'me_10_wewishyou',
         'me_11_silentnight4h', 'me_12_panthere', 'me_13_pianoman',
         'me_14_belaciao', 'me_15_spring', 'me_16_greensleeves',
         'me_17_countingstars', 'me_18_largodvorak', 'me_19_grandfather',
         'me_20_dream', 'me_21_beauty', 'me_22_gladiator', 'me_23_rasputin',
         'me_24_jailhouse', 'me_25_toreador', 'me_26_furelise', 'me_27_nocturne',
         'nl_01_petite', 'nl_02_counting', 'nl_03_deck', 'nl_04_heart',
         'nl_05_hittheroad', 'nl_06_jailhouse', 'nl_07_bellaciao',
         'nl_08_canthelp', 'nl_09_toreador', 'nl_10_lovely', 'nl_11_rasputin',
         'nl_12_diamonds', 'nl_13_favourite', 'nl_14_sweetchild', 'nl_15_merry',
         'nl_16_acomme', 'nl_17_dragon']

# Las DIEZ partituras que Aida comparte con otro alumno, byte a byte. Cada una
# puede recitar las mismas citas literales medidas que su gemela --es la misma
# musica--, y esas coincidencias SI son esperables. Las nueve restantes son
# solo suyas: el Scherzo de Diabelli, Perfect, Boig per tu, Kiss the Rain,
# Hijo de la luna, The Sound of Silence, el Gladiator de Escobes, el Canon de
# Pachelbel y el Preludio n. 1 de Bach.
COMPARTIDAS = ['Romance . Diabelli (José María 1 · Josep 1)',
               'We Wish You a Merry Christmas (Mercè 10 · Isaac 5)',
               "Can't Help Falling in Love (José María 11 · Josep 11 · Nel 8 · "
               'Dilan 1 · Eva 1)',
               'What Was I Made For (Josep 5 · Dilan 13 · Eva 4)',
               'Counting Stars (José María 4 · Josep 4 · Nel 2 · Mercè 17)',
               "It's Beginning to Look a Lot Like Christmas (Josep 14 · "
               'Dilan 20 · Eva 15)',
               'Titanic (Luisa 10)',
               'Carol of the Bells (José María 12)',
               'Un beso y una flor (Josep 17)',
               'A comme amour (José María 17 · Josep 19 · Nel 16)']

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
for mod in AIDA + OTROS:
    cfg = __import__(mod).CANCION
    segno.make(cfg['yt'], error='m').save(qr, scale=10, border=2, dark='#1A2332', light='#F3F1EA')
    for nb, fn in cancion._hojas(cfg, qr):
        cur[0] = '%s/%s' % (mod, nb)
        fn(canvas.Canvas(os.devnull, pagesize=(W, H)))
        hojas += 1

print('Las partituras que Aída comparte con otro alumno, byte a byte:')
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
    fila = (len(k), clef, sorted(refs))
    if 'ai' in alumnos and len(alumnos) > 1:
        entre_alumnos.append(fila)
    elif alumnos == {'ai'}:
        dentro.append(fila)

# Las citas literales intencionadas: mismo archivo de partitura y mismo pasaje
# MEDIDO sobre el. Cambiarle las notas a uno de los dos seria escribir mal a
# proposito, porque es la misma musica. Se anotan aqui una a una segun
# aparecen, con el bloque y el motivo.
CITAS_LITERALES_OK = set()

inesperados = [(n, clef, refs) for n, clef, refs in entre_alumnos
               if frozenset(refs) not in CITAS_LITERALES_OK]
esperados = [(n, clef, refs) for n, clef, refs in entre_alumnos
             if frozenset(refs) in CITAS_LITERALES_OK]

print('\nAÍDA contra los otros diez alumnos · sistemas compartidos: %d'
      % len(entre_alumnos))
print('   de los cuales, citas literales esperadas (mismo pasaje medido): %d' % len(esperados))
for n, clef, refs in sorted(esperados, reverse=True):
    print('   [cita literal, OK] %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))
print('   y andamio inventado que coincide sin motivo (esto SÍ es un fallo): %d' % len(inesperados))
for n, clef, refs in sorted(inesperados, reverse=True):
    print('   [FALLO] %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

print('\nDentro de Aída · sistemas repetidos entre piezas: %d' % len(dentro))
for n, clef, refs in sorted(dentro, reverse=True):
    print('   [FALLO] %2d eventos · %-7s · %s' % (n, clef, ' + '.join(refs)))

sys.exit(1 if (inesperados or dentro) else 0)
