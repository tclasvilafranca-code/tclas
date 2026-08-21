# -*- coding: utf-8 -*-
"""Comprueba que la ARMADURA que implica la tonalidad declarada es la que trae
   impresa la partitura detras de la clave.

   Tercer dato caro, despues del compas y de la figura. Los tres se equivocan
   igual de facil y por el mismo motivo: son lo primero que se ve, parecen
   obvios y por eso nadie vuelve a mirarlos. Se comprobaron LAS 93 partituras
   distintas el 21 de agosto de 2026, recortando del PDF el arranque del primer
   pentagrama y contando los sostenidos o bemoles pegados a la clave. Salieron
   las 93 bien: la tonalidad era el unico de los tres datos que estaba
   completamente sano, y saberlo tambien vale.

   LO QUE SE COMPRUEBA ES LA ARMADURA, NO EL NOMBRE DE LA TONALIDAD. Un
   sostenido puede llamarse Sol mayor o Mi menor y las dos cosas son ciertas:
   son la misma armadura y la eleccion depende de donde descanse la musica.
   `My Favourite Things` es el caso: empieza en Mi menor y acaba en Sol mayor,
   y por eso Josep y Nel la llaman Mi menor mientras Dilan y Eva la llaman Sol
   mayor. Las dos hojas dicen lo mismo con distinto titular, y ninguna miente.
   Lo que si seria un fallo —y esto lo caza— es que una pieza en Fa mayor
   pasara a declararse en Sol mayor: eso cambia las teclas negras.

   Limites, los mismos que el auditor de compas: se leyo la PRIMERA pagina de
   musica (un cambio de armadura a mitad de pieza no lo ve, y hay al menos uno,
   el de `al calor del amor en un bar`, que su hoja explica aparte), y la clave
   es el nombre del modulo porque las partituras no se versionan.

   Uso:  python3 auditar_tonalidad.py            (todos)
         python3 auditar_tonalidad.py arnau lu   (solo esos prefijos)
"""
import contextlib
import glob
import importlib
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'engine'))

PREFIJOS = ['arnau', 'lu', 'jm', 'ed', 'me', 'is', 'jp', 'nl', 'dilan', 'eva']

# Cuantas alteraciones lleva cada tonalidad que el proyecto usa. Si alguien
# escribe una tonalidad que no esta aqui, el auditor lo dice en vez de callarse:
# no vale dar por buena una tonalidad cuya armadura nadie ha pensado.
ARMADURA = {
    None: '0',
    'La menor': '0',
    'Sol mayor': '1 SOST',
    'Mi menor': '1 SOST',
    'Re mayor': '2 SOST',
    'Si menor': '2 SOST',
    'La mayor': '3 SOST',
    'Fa mayor': '1 BEM',
    'Re menor': '1 BEM',
    'Sib mayor': '2 BEM',
    'Sol menor': '2 BEM',
    'Mib mayor': '3 BEM',
}

# Lo LEIDO en el papel, pieza a pieza. El comentario de la derecha es lo que
# declaraba el dosier el dia de la lectura.
LEIDO = {
    #  Lucia_.pdf                                          0
    'dilan_05_lucia':          '0',        # dice nada
    #  SOLDADITO DE HIERRO _ Nil Moliner_.pdf              0
    'dilan_11_soldadito':      '0',        # dice nada
    'eva_11_soldadito':        '0',        # dice nada
    #  THINKING OUT LOUD _ Ed Sheeran_.pdf                 2 SOST
    'dilan_04_thinking':       '2 SOST',   # dice Re mayor
    'eva_05_thinking':         '2 SOST',   # dice Re mayor
    #  WHEN I WAS YOUR MAN _ Bruno Mars_.pdf               0
    'dilan_09_bruno':          '0',        # dice nada
    'eva_07_bruno':            '0',        # dice nada
    #  YOUR SONG _ Elton John_.pdf                         3 BEM
    'dilan_03_your_song':      '3 BEM',    # dice Mib mayor
    #  a-sky-full-of-stars-coldplay.pdf                    1 BEM
    'dilan_12_sky':            '1 BEM',    # dice Fa mayor
    'eva_02_sky':              '1 BEM',    # dice Fa mayor
    #  arabesque-burgmuller-( 4 manos).pdf                 0
    'dilan_17_arabesque':      '0',        # dice nada
    'eva_16_arabesque':        '0',        # dice nada
    #  la-promesa-MELENDI.pdf                              1 SOST
    'dilan_08_promesa':        '1 SOST',   # dice Sol mayor
    'eva_08_promesa':          '1 SOST',   # dice Sol mayor
    #  poema-de-amor-joan-manuel-serrat_.pdf               2 BEM
    'dilan_06_poema':          '2 BEM',    # dice Sol menor
    'eva_03_poema':            '2 BEM',    # dice Sol menor
    # -LOVELY.pdf                                          1 SOST
    'jp_12_lovely':            '1 SOST',   # dice Mi menor
    'nl_10_lovely':            '1 SOST',   # dice Mi menor
    # -PEACHES.                                            0
    'jm_05_peaches':           '0',        # dice nada
    'ed_05_peaches':           '0',        # dice nada
    'jp_03_peaches':           '0',        # dice nada
    # A COMME AMOUR _ Richard Clayderman.                  1 SOST
    'jm_17_acomme':            '1 SOST',   # dice Mi menor
    'ed_17_acomme':            '1 SOST',   # dice Mi menor
    'jp_19_acomme':            '1 SOST',   # dice Mi menor
    'nl_16_acomme':            '1 SOST',   # dice Mi menor
    # ADAGIO.                                              0
    'jm_13_adagio':            '0',        # dice nada
    'ed_13_adagio':            '0',        # dice nada
    # Adagio en sol menor. Albinoni.pdf                    2 BEM
    'dilan_16_adagio':         '2 BEM',    # dice Sol menor
    # Aloha oe.sib.pdf                                     0
    'arnau_16_aloha':          '0',        # dice nada
    # Amiga mia-alejandro Sanz.pdf                         2 SOST
    'dilan_07_amiga':          '2 SOST',   # dice Re mayor
    'eva_09_amiga':            '2 SOST',   # dice Re mayor
    # BELLA Y BESTIA .pdf                                  1 BEM
    'me_21_beauty':            '1 BEM',    # dice Fa mayor
    # Baa Baa Black Sheep.pdf                              0
    'arnau_08_baabaa':         '0',        # dice nada
    # Chopsticks.pdf                                       0
    'arnau_01_chopsticks':     '0',        # dice nada
    # Clementine.pdf                                       0
    'arnau_02_clementine':     '0',        # dice nada
    # Como entrenar a tu dragon.                           0
    'jm_19_flying':            '0',        # dice nada
    'ed_19_flying':            '0',        # dice nada
    'nl_17_dragon':            '0',        # dice nada
    # Copia de 1-----Greensleeves.pdf                      0
    'lu_15_greensleeves':      '0',        # dice La menor
    'me_16_greensleeves':      '0',        # dice La menor
    'is_11_greensleeves':      '0',        # dice La menor
    # Counting-stars.pdf                                   0
    'jm_04_counting':          '0',        # dice nada
    'ed_04_counting':          '0',        # dice nada
    'me_17_countingstars':     '0',        # dice nada
    'jp_04_counting':          '0',        # dice nada
    'nl_02_counting':          '0',        # dice nada
    # DIABELLI ( cuatro manos).pdf                         0
    'is_20_diabelli':          '0',        # dice nada
    # Deck the Halls (with Boughs of Holly) NAVIDAD.pdf    1 BEM
    'jm_07_deck':              '1 BEM',    # dice Fa mayor
    'ed_07_deck':              '1 BEM',    # dice Fa mayor
    'jp_08_deck':              '1 BEM',    # dice Fa mayor
    'nl_03_deck':              '1 BEM',    # dice Fa mayor
    # Do Your Ears Hang Low?.pdf                           0
    'arnau_04_ears':           '0',        # dice nada
    # ElSubmarinoAmarillo-.pdf                             1 SOST
    'arnau_18_submarino':      '1 SOST',   # dice Sol mayor
    # Eso-que-tu-me-das. Jarabe de Palo.pdf                0
    'arnau_11_eso':            '0',        # dice nada
    # Gladyator.pdf                                        3 SOST
    'me_22_gladiator':         '3 SOST',   # dice La mayor
    'is_15_gladiator':         '3 SOST',   # dice La mayor
    # Grandfather's Clock.pdf                              1 SOST
    'jm_09_clock':             '1 SOST',   # dice Sol mayor
    'ed_09_clock':             '1 SOST',   # dice Sol mayor
    'me_19_grandfather':       '1 SOST',   # dice Sol mayor
    'is_12_grandfather':       '1 SOST',   # dice Sol mayor
    # Himno de Estados Unidos.pdf                          0
    'jm_03_banner':            '0',        # dice nada
    'ed_03_banner':            '0',        # dice nada
    # Interstellar _ .pdf                                  0
    'jm_18_interstellar':      '0',        # dice nada
    'ed_18_interstellar':      '0',        # dice nada
    # JOLLY OLD SAINT NICHOLAS.pdf                         0
    'arnau_03_jolly':          '0',        # dice nada
    # LA PRIMAVERA.pdf easy                                0
    'lu_09_spring':            '0',        # dice nada
    # LAS CUATRO ESTACIONES.pdf                            0
    'me_15_spring':            '0',        # dice nada
    # La Pantera Rosa.pdf                                  0
    'arnau_13_pantera':        '0',        # dice nada
    'lu_12_panthere':          '0',        # dice nada
    'me_12_panthere':          '0',        # dice nada
    'is_09_panthere':          '0',        # dice nada
    # Largo-Sinfonia 5 Dvorak.pdf                          0
    'arnau_15_largo':          '0',        # dice nada
    'me_18_largodvorak':       '0',        # dice nada
    # Little Miss Muffet.pdf                               1 BEM
    'arnau_10_muffet':         '1 BEM',    # dice Fa mayor
    # Mary Popins FACIL.pdf                                0
    'lu_16_chimchim':          '0',        # dice La menor
    # MyBonnie.pdf                                         0
    'arnau_14_bonnie':         '0',        # dice nada
    # Oh when the Saint.pdf                                0
    'arnau_06_saints':         '0',        # dice nada
    'me_02_saints':            '0',        # dice nada
    'is_02_saints':            '0',        # dice nada
    # Para  Elisa easy.pdf                                 0
    'lu_18_furelise':          '0',        # dice La menor
    # Para Elisa.pdf                                       0
    'me_26_furelise':          '0',        # dice La menor
    'is_19_furelise':          '0',        # dice La menor
    # Polly Put the Kettle On.pdf                          1 BEM
    'arnau_09_polly':          '1 BEM',    # dice Fa mayor
    # Popeye el marinerito.pdf                             1 SOST
    'arnau_17_popeye':         '1 SOST',   # dice Sol mayor
    # Romance-Diabelli 4 manos.pdf                         0
    'jm_01_romance':           '0',        # dice nada
    'ed_01_romance':           '0',        # dice nada
    'jp_01_romance':           '0',        # dice nada
    # SHALLOW.                                             1 SOST
    'jm_10_shallow':           '1 SOST',   # dice Sol mayor
    'ed_10_shallow':           '1 SOST',   # dice Sol mayor
    # SOMEONE YOU LOVED.                                   0
    'jm_06_someone':           '0',        # dice nada
    'ed_06_someone':           '0',        # dice nada
    # SUR LE PONT D'AVIGNON.pdf                            0
    'me_06_avignon':           '0',        # dice nada
    # Santa-tell-me-ariana-grande NAVIDAD.pdf              1 SOST
    'dilan_19_santa':          '1 SOST',   # dice Sol mayor
    'eva_14_santa':            '1 SOST',   # dice Sol mayor
    # Silent-Night.easy                                    0
    'lu_08_silent':            '0',        # dice nada
    'me_09_silentnight':       '0',        # dice nada
    'is_07_silentnight':       '0',        # dice nada
    # Sonrisas y Lagrimas.pdf                              0
    'me_07_doremi':            '0',        # dice nada
    'is_13_doremi':            '0',        # dice nada
    # The Beginner Le Debut.pdf                            0
    'lu_02_beginner':          '0',        # dice nada
    'is_04_beginner':          '0',        # dice nada
    # The Wheels on the Bus.pdf                            1 BEM
    'arnau_05_wheels':         '1 BEM',    # dice Fa mayor
    # Titanic easy.pdf                                     0
    'lu_10_titanic':           '0',        # dice nada
    # Toreador. Bizet                                      1 BEM
    'jm_15_toreador':          '1 BEM',    # dice Fa mayor
    'ed_15_toreador':          '1 BEM',    # dice Fa mayor
    'me_25_toreador':          '1 BEM',    # dice Fa mayor
    'is_18_toreador':          '1 BEM',    # dice Fa mayor
    'nl_09_toreador':          '1 BEM',    # dice Fa mayor
    # Trouble.                                             1 SOST
    'jm_16_trouble':           '1 SOST',   # dice Sol mayor
    'ed_16_trouble':           '1 SOST',   # dice Sol mayor
    # Un beso-y-una-flor-nino-bravo.pdf                    1 BEM
    'jp_17_unbeso':            '1 BEM',    # dice Fa mayor
    # WE WISH A MERRY CRISTMAS.pdf                         0
    'arnau_07_wewish':         '0',        # dice nada
    # WE WISH YOU A MERRY CHRISTMAS.pdf                    1 SOST
    'me_10_wewishyou':         '1 SOST',   # dice Sol mayor
    'is_05_wewishyou':         '1 SOST',   # dice Sol mayor
    # WHEN WE WERE YOUNG _ Adele Dm .pdf                   1 BEM
    'eva_10_young':            '1 BEM',    # dice Re menor
    # WRITING_S ON THE WALL _ Sam Smith_.pdf               1 BEM
    'dilan_14_writings':       '1 BEM',    # dice Re menor
    # _bazzoni-maurizio-sonatina-sol-maggiore (4 manos).pdf 1 SOST
    'lu_03_sonatina2':         '1 SOST',   # dice Sol mayor
    'me_05_sonatina2':         '1 SOST',   # dice Sol mayor
    # al-calor-del-amor-en-un-bar.pdf                      1 SOST
    'dilan_10_calor':          '1 SOST',   # dice Mi menor
    # bazzoni-maurizio-sonatina-per-bambini-(4 manos).pdf  0
    'lu_01_bambini':           '0',        # dice La menor
    'me_01_bambini':           '0',        # dice La menor
    # bela-ciao.easy                                       1 SOST
    'lu_13_belaciao':          '1 SOST',   # dice Mi menor
    'me_14_belaciao':          '1 SOST',   # dice Mi menor
    # bella-ciao-piano-(4 MANOS).pdf                       2 BEM
    'jp_10_bellaciao':         '2 BEM',    # dice Sol menor
    'nl_07_bellaciao':         '2 BEM',    # dice Sol menor
    # bohemian-rhapsody.pdf                                2 BEM
    'eva_17_bohemian':         '2 BEM',    # dice Sib mayor
    # cant-help-falling-in-love-elvis-presley.             2 SOST
    'jm_11_canthelp':          '2 SOST',   # dice Re mayor
    'ed_11_canthelp':          '2 SOST',   # dice Re mayor
    'jp_11_canthelp':          '2 SOST',   # dice Re mayor
    'nl_08_canthelp':          '2 SOST',   # dice Re mayor
    'dilan_02_cancion':        '2 SOST',   # dice Re mayor
    'eva_01_canthelp':         '2 SOST',   # dice Re mayor
    # carol-of-the-bells   NAVIDAD.                        2 BEM
    'jm_12_carol':             '2 BEM',    # dice Sol menor
    'ed_12_carol':             '2 BEM',    # dice Sol menor
    # christmas-songs-(4 manos).pdf                        0
    'lu_07_christmas':         '0',        # dice nada
    'me_08_christmas':         '0',        # dice nada
    'is_06_christmas':         '0',        # dice nada
    # have-yourself-a-merry-little-NAVIDAD       ADhristmas_.pdf 0
    'dilan_18_merry':          '0',        # dice nada
    'eva_13_merry':            '0',        # dice nada
    # heart-and-soul-hoagy-carmIchael easy.pdf             0
    'lu_14_heart':             '0',        # dice nada
    'jp_06_heart':             '0',        # dice nada
    'nl_04_heart':             '0',        # dice nada
    # himno America.pdf                                    0
    'jm_02_america':           '0',        # dice nada
    'ed_02_america':           '0',        # dice nada
    # hit-the-road-jack-ray-.pdf                           1 BEM
    'jp_07_hittheroad':        '1 BEM',    # dice Fa mayor
    'nl_05_hittheroad':        '1 BEM',    # dice Fa mayor
    # i-have-a-dream-abba-children-song.pdf                0
    'lu_06_dream':             '0',        # dice nada
    'me_20_dream':             '0',        # dice nada
    'is_14_dream':             '0',        # dice nada
    # its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf 0
    'jp_14_beginning':         '0',        # dice nada
    'dilan_20_beginning':      '0',        # dice nada
    'eva_15_beginning':        '0',        # dice nada
    # jailhouse-rock-elvis-presley-.pdf                    0
    'jm_08_jailhouse':         '0',        # dice nada
    'ed_08_jailhouse':         '0',        # dice nada
    'me_24_jailhouse':         '0',        # dice nada
    'is_17_jailhouse':         '0',        # dice nada
    'jp_09_jailhouse':         '0',        # dice nada
    'nl_06_jailhouse':         '0',        # dice nada
    # merry-go-round-of-life.pdf                           2 BEM
    'jp_18_merry':             '2 BEM',    # dice Sib mayor
    'nl_15_merry':             '2 BEM',    # dice Sib mayor
    # my-favourite-things-the-sound-.pdf                   1 SOST
    'jp_15_favourite':         '1 SOST',   # dice Mi menor
    'nl_13_favourite':         '1 SOST',   # dice Mi menor
    'dilan_15_favourite':      '1 SOST',   # dice Sol mayor
    'eva_12_favourite':        '1 SOST',   # dice Sol mayor
    # nocturne-op9-chopin. easy                            0
    'lu_19_nocturne':          '0',        # dice nada
    'me_27_nocturne':          '0',        # dice nada
    # petite chanson(4 manos).pdf                          0
    'is_01_petite':            '0',        # dice nada
    'jp_02_petite':            '0',        # dice nada
    'nl_01_petite':            '0',        # dice nada
    # piano-man-easy.                                      0
    'lu_11_pianoman':          '0',        # dice nada
    'me_13_pianoman':          '0',        # dice nada
    'is_10_pianoman':          '0',        # dice nada
    # puff-the-magic-dragon.pdf                            0
    'arnau_12_puff':           '0',        # dice nada
    'lu_05_puff':              '0',        # dice nada
    'me_04_puff':              '0',        # dice nada
    'is_03_puff':              '0',        # dice nada
    # rain-rain-away-easy-piano-4 manos.pdf                0
    'arnau_19_rain':           '0',        # dice nada
    # rasputin easy.pdf                                    2 SOST
    'lu_17_rasputin':          '2 SOST',   # dice Si menor
    'jm_14_rasputin':          '2 SOST',   # dice Si menor
    'ed_14_rasputin':          '2 SOST',   # dice Si menor
    'me_23_rasputin':          '2 SOST',   # dice Si menor
    'is_16_rasputin':          '2 SOST',   # dice Si menor
    'jp_13_rasputin':          '2 SOST',   # dice Si menor
    'nl_11_rasputin':          '2 SOST',   # dice Si menor
    # rihanna-diamond-.pdf                                 2 SOST
    'nl_12_diamonds':          '2 SOST',   # dice Re mayor
    # silent-night-4-hands.                                0
    'me_11_silentnight4h':     '0',        # dice nada
    'is_08_silentnight4h':     '0',        # dice nada
    # sweet-child-o-mine-guns-n-roses-easy-piano.pdf       2 BEM
    'jp_16_sweetchild':        '2 BEM',    # dice Sib mayor
    'nl_14_sweetchild':        '2 BEM',    # dice Sib mayor
    # the-mulberry-bush-185807.4 manos.pdf                 0
    'arnau_20_mulberry':       '0',        # dice nada
    # the-swan.pdf                                         1 SOST
    'dilan_01_cancion':        '1 SOST',   # dice Sol mayor
    'eva_06_cisne':            '1 SOST',   # dice Sol mayor
    # what-was-i-made-for-billie-eilish.pdf                0
    'jp_05_what':              '0',        # dice nada
    'dilan_13_what':           '0',        # dice nada
    'eva_04_what':             '0',        # dice nada
    # youve-got-a-friend-in-me-easy-piano-.pdf             0
    'lu_04_friend':            '0',        # dice nada
    'me_03_friend':            '0',        # dice nada
}


def _cfg(modulo):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        mod = importlib.import_module(modulo)
    return getattr(mod, 'CANCION', None)


def main(prefijos=None):
    prefijos = prefijos or PREFIJOS
    malos, sin_leer, sin_tabla = [], [], []
    n = 0
    for p in prefijos:
        for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py'))):
            m = os.path.basename(f)[:-3]
            cfg = _cfg(m)
            if not cfg or not cfg.get('partitura'):
                continue
            n += 1
            ks = cfg.get('key_sig')
            if ks not in ARMADURA:
                sin_tabla.append((m, ks))
                continue
            if m not in LEIDO:
                sin_leer.append((m, os.path.basename(cfg['partitura'])))
            elif ARMADURA[ks] != LEIDO[m]:
                malos.append((m, ks, ARMADURA[ks], LEIDO[m]))

    print('piezas comprobadas: %d de %d con lectura anotada' % (n, len(LEIDO)))

    print('\nLA ARMADURA DECLARADA NO ES LA IMPRESA: %d' % len(malos))
    for m, ks, dice, leido in malos:
        print('   %-22s dice %-11s (%s) · impreso %s' % (m, ks or 'nada', dice, leido))

    print('\nTonalidades cuya armadura no esta en la tabla: %d' % len(sin_tabla))
    for m, ks in sin_tabla:
        print('   %-22s %r' % (m, ks))

    print('\nPiezas cuya armadura no ha leido nadie: %d' % len(sin_leer))
    for m, base in sin_leer:
        print('   %-22s %s' % (m, base[:50]))

    fallos = len(malos) + len(sin_tabla) + len(sin_leer)
    if fallos:
        print('\n%d COSAS QUE MIRAR' % fallos)
        return 1
    print('\nARMADURAS OK — lo que declara el dosier es lo que trae la partitura.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
