# -*- coding: utf-8 -*-
"""Comprueba que el compas que declara cada pieza es el que trae IMPRESO su
   partitura.

   Sale de encontrar, revisando el album de Arnau a ojo, dos compases mal:
   The Wheels on the Bus decia 3/4 y va en 4/4, y Polly Put the Kettle On
   decia 2/4 y va en 4/4. Dos de once en un solo album es una tasa altisima
   para el dato mas caro de equivocar: un alumno que cuenta de tres una
   cancion de cuatro no puede tocarla bien ni una semana, y encima no sabe
   por que. Asi que se comprobaron LAS 93 partituras distintas del proyecto,
   una por una, recortando del PDF el arranque del primer pentagrama (clave,
   armadura y cifra de compas) y mirandolo a tamano grande. Aparecio una
   tercera: The Mulberry Bush decia 4/4 y va en 6/8.

   Lo de abajo es el resultado de esa lectura, hecha el 21 de agosto de 2026.
   No se deduce del codigo: se leyo en el papel, y por eso vale como testigo.
   Si alguien cambia un `time_sig` sin haber vuelto a mirar la partitura, esto
   falla; y si anade una pieza nueva, esto avisa de que su compas no lo ha
   leido nadie.

   Las piezas van agrupadas por partitura: las que comparten fichero comparten
   lectura porque el PDF es byte a byte el mismo (comprobado por md5), aunque
   cada alumno lo tenga guardado con otro nombre.

   Dos limites que conviene tener presentes:
     - se leyo el PRIMER compas de la PRIMERA pagina de musica; un cambio de
       compas a mitad de pieza no lo ve;
     - la clave es el nombre del modulo y no el del fichero, porque las
       partituras no se versionan (son material del cliente) y el auditor
       tiene que poder correr sin ellas delante.

   Uso:  python3 auditar_compas.py            (todos)
         python3 auditar_compas.py arnau lu   (solo esos prefijos)
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

LEIDO = {
    #  Lucia_.pdf · leido 4/4
    'dilan_05_lucia':          (4, 4),
    #  SOLDADITO DE HIERRO _ Nil Moliner_.pdf · leido 4/4
    'dilan_11_soldadito':      (4, 4),
    'eva_11_soldadito':        (4, 4),
    #  THINKING OUT LOUD _ Ed Sheeran_.pdf · leido 4/4
    'dilan_04_thinking':       (4, 4),
    'eva_05_thinking':         (4, 4),
    #  WHEN I WAS YOUR MAN _ Bruno Mars_.pdf · leido 4/4
    'dilan_09_bruno':          (4, 4),
    'eva_07_bruno':            (4, 4),
    #  YOUR SONG _ Elton John_.pdf · leido 4/4
    'dilan_03_your_song':      (4, 4),
    #  a-sky-full-of-stars-coldplay.pdf · leido 4/4
    'dilan_12_sky':            (4, 4),
    'eva_02_sky':              (4, 4),
    #  arabesque-burgmuller-( 4 manos).pdf · leido 2/4
    'dilan_17_arabesque':      (2, 4),
    'eva_16_arabesque':        (2, 4),
    #  la-promesa-MELENDI.pdf · leido 4/4
    'dilan_08_promesa':        (4, 4),
    'eva_08_promesa':          (4, 4),
    #  poema-de-amor-joan-manuel-serrat_.pdf · leido 4/4
    'dilan_06_poema':          (4, 4),
    'eva_03_poema':            (4, 4),
    # -LOVELY.pdf · leido 4/4
    'jp_12_lovely':            (4, 4),
    'nl_10_lovely':            (4, 4),
    # -PEACHES. · leido 4/4
    'jm_05_peaches':           (4, 4),
    'jp_03_peaches':           (4, 4),
    # A COMME AMOUR _ Richard Clayderman. · leido 4/4
    'jm_17_acomme':            (4, 4),
    'jp_19_acomme':            (4, 4),
    'nl_16_acomme':            (4, 4),
    # ADAGIO. · leido 3/4
    'jm_13_adagio':            (3, 4),
    # Adagio en sol menor. Albinoni.pdf · leido 3/4
    'dilan_16_adagio':         (3, 4),
    # Aloha oe.sib.pdf · leido 2/2
    'arnau_16_aloha':          (2, 2),
    # Amiga mia-alejandro Sanz.pdf · leido 4/4
    'dilan_07_amiga':          (4, 4),
    'eva_09_amiga':            (4, 4),
    # BELLA Y BESTIA .pdf · leido 4/4
    'me_21_beauty':            (4, 4),
    # Baa Baa Black Sheep.pdf · leido 4/4
    'arnau_08_baabaa':         (4, 4),
    # Chopsticks.pdf · leido 3/4
    'arnau_01_chopsticks':     (3, 4),
    # Clementine.pdf · leido 3/4
    'arnau_02_clementine':     (3, 4),
    # Como entrenar a tu dragon. · leido 4/4
    'jm_19_flying':            (4, 4),
    'nl_17_dragon':            (4, 4),
    # Copia de 1-----Greensleeves.pdf · leido 3/4
    'lu_15_greensleeves':      (3, 4),
    'me_16_greensleeves':      (3, 4),
    'is_11_greensleeves':      (3, 4),
    # Counting-stars.pdf · leido 4/4
    'jm_04_counting':          (4, 4),
    'me_17_countingstars':     (4, 4),
    'jp_04_counting':          (4, 4),
    'nl_02_counting':          (4, 4),
    # DIABELLI ( cuatro manos).pdf · leido 2/4
    'is_20_diabelli':          (2, 4),
    # Deck the Halls (with Boughs of Holly) NAVIDAD.pdf · leido 4/4
    'jm_07_deck':              (4, 4),
    'jp_08_deck':              (4, 4),
    'nl_03_deck':              (4, 4),
    # Do Your Ears Hang Low?.pdf · leido 4/4
    'arnau_04_ears':           (4, 4),
    # ElSubmarinoAmarillo-.pdf · leido 4/4
    'arnau_18_submarino':      (4, 4),
    # Eso-que-tu-me-das. Jarabe de Palo.pdf · leido 4/4
    'arnau_11_eso':            (4, 4),
    # Gladyator.pdf · leido 3/4
    'me_22_gladiator':         (3, 4),
    'is_15_gladiator':         (3, 4),
    # Grandfather's Clock.pdf · leido 4/4
    'jm_09_clock':             (4, 4),
    'me_19_grandfather':       (4, 4),
    'is_12_grandfather':       (4, 4),
    # Himno de Estados Unidos.pdf · leido 3/4
    'jm_03_banner':            (3, 4),
    # Interstellar _ .pdf · leido 3/4
    'jm_18_interstellar':      (3, 4),
    # JOLLY OLD SAINT NICHOLAS.pdf · leido 4/4
    'arnau_03_jolly':          (4, 4),
    # LA PRIMAVERA.pdf easy · leido 4/4
    'lu_09_spring':            (4, 4),
    # LAS CUATRO ESTACIONES.pdf · leido 4/4
    'me_15_spring':            (4, 4),
    # La Pantera Rosa.pdf · leido 4/4
    'arnau_13_pantera':        (4, 4),
    'lu_12_panthere':          (4, 4),
    'me_12_panthere':          (4, 4),
    'is_09_panthere':          (4, 4),
    # Largo-Sinfonia 5 Dvorak.pdf · leido 4/4
    'arnau_15_largo':          (4, 4),
    'me_18_largodvorak':       (4, 4),
    # Little Miss Muffet.pdf · leido 6/8
    'arnau_10_muffet':         (6, 8),
    # Mary Popins FACIL.pdf · leido 3/4
    'lu_16_chimchim':          (3, 4),
    # MyBonnie.pdf · leido 3/4
    'arnau_14_bonnie':         (3, 4),
    # Oh when the Saint.pdf · leido 4/4
    'arnau_06_saints':         (4, 4),
    'me_02_saints':            (4, 4),
    'is_02_saints':            (4, 4),
    # Para  Elisa easy.pdf · leido 3/4
    'lu_18_furelise':          (3, 4),
    # Para Elisa.pdf · leido 3/4
    'me_26_furelise':          (3, 4),
    'is_19_furelise':          (3, 4),
    # Polly Put the Kettle On.pdf · leido 4/4
    'arnau_09_polly':          (4, 4),
    # Popeye el marinerito.pdf · leido 3/4
    'arnau_17_popeye':         (3, 4),
    # Romance-Diabelli 4 manos.pdf · leido 2/2
    'jm_01_romance':           (2, 2),
    'jp_01_romance':           (2, 2),
    # SHALLOW. · leido 4/4
    'jm_10_shallow':           (4, 4),
    # SOMEONE YOU LOVED. · leido 4/4
    'jm_06_someone':           (4, 4),
    # SUR LE PONT D'AVIGNON.pdf · leido 4/4
    'me_06_avignon':           (4, 4),
    # Santa-tell-me-ariana-grande NAVIDAD.pdf · leido 4/4
    'dilan_19_santa':          (4, 4),
    'eva_14_santa':            (4, 4),
    # Silent-Night.easy · leido 3/4
    'lu_08_silent':            (3, 4),
    'me_09_silentnight':       (3, 4),
    'is_07_silentnight':       (3, 4),
    # Sonrisas y Lagrimas.pdf · leido 4/4
    'me_07_doremi':            (4, 4),
    'is_13_doremi':            (4, 4),
    # The Beginner Le Debut.pdf · leido 3/4
    'lu_02_beginner':          (3, 4),
    'is_04_beginner':          (3, 4),
    # The Wheels on the Bus.pdf · leido 4/4
    'arnau_05_wheels':         (4, 4),
    # Titanic easy.pdf · leido 2/4
    'lu_10_titanic':           (2, 4),
    # Toreador. Bizet · leido 4/4
    'jm_15_toreador':          (4, 4),
    'me_25_toreador':          (4, 4),
    'is_18_toreador':          (4, 4),
    'nl_09_toreador':          (4, 4),
    # Trouble. · leido 4/4
    'jm_16_trouble':           (4, 4),
    # Un beso-y-una-flor-nino-bravo.pdf · leido 4/4
    'jp_17_unbeso':            (4, 4),
    # WE WISH A MERRY CRISTMAS.pdf · leido 3/4
    'arnau_07_wewish':         (3, 4),
    # WE WISH YOU A MERRY CHRISTMAS.pdf · leido 3/4
    'me_10_wewishyou':         (3, 4),
    'is_05_wewishyou':         (3, 4),
    # WHEN WE WERE YOUNG _ Adele Dm .pdf · leido 4/4
    'eva_10_young':            (4, 4),
    # WRITING_S ON THE WALL _ Sam Smith_.pdf · leido 4/4
    'dilan_14_writings':       (4, 4),
    # _bazzoni-maurizio-sonatina-sol-maggiore (4 manos).pdf · leido 4/4
    'lu_03_sonatina2':         (4, 4),
    'me_05_sonatina2':         (4, 4),
    # al-calor-del-amor-en-un-bar.pdf · leido 4/4
    'dilan_10_calor':          (4, 4),
    # bazzoni-maurizio-sonatina-per-bambini-(4 manos).pdf · leido 4/4
    'lu_01_bambini':           (4, 4),
    'me_01_bambini':           (4, 4),
    # bela-ciao.easy · leido 2/4
    'lu_13_belaciao':          (2, 4),
    'me_14_belaciao':          (2, 4),
    # bella-ciao-piano-(4 MANOS).pdf · leido 4/4
    'jp_10_bellaciao':         (4, 4),
    'nl_07_bellaciao':         (4, 4),
    # bohemian-rhapsody.pdf · leido 4/4
    'eva_17_bohemian':         (4, 4),
    # cant-help-falling-in-love-elvis-presley. · leido 3/4
    'jm_11_canthelp':          (3, 4),
    'jp_11_canthelp':          (3, 4),
    'nl_08_canthelp':          (3, 4),
    'dilan_02_cancion':        (3, 4),
    'eva_01_canthelp':         (3, 4),
    # carol-of-the-bells   NAVIDAD. · leido 3/4
    'jm_12_carol':             (3, 4),
    # christmas-songs-(4 manos).pdf · leido 4/4
    'lu_07_christmas':         (4, 4),
    'me_08_christmas':         (4, 4),
    'is_06_christmas':         (4, 4),
    # have-yourself-a-merry-little-NAVIDAD       ADhristmas_.pdf · leido 4/4
    'dilan_18_merry':          (4, 4),
    'eva_13_merry':            (4, 4),
    # heart-and-soul-hoagy-carmIchael easy.pdf · leido 4/4
    'lu_14_heart':             (4, 4),
    'jp_06_heart':             (4, 4),
    'nl_04_heart':             (4, 4),
    # himno America.pdf · leido 3/4
    'jm_02_america':           (3, 4),
    # hit-the-road-jack-ray-.pdf · leido 4/4
    'jp_07_hittheroad':        (4, 4),
    'nl_05_hittheroad':        (4, 4),
    # i-have-a-dream-abba-children-song.pdf · leido 4/4
    'lu_06_dream':             (4, 4),
    'me_20_dream':             (4, 4),
    'is_14_dream':             (4, 4),
    # its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf · leido 6/8
    'jp_14_beginning':         (6, 8),
    'dilan_20_beginning':      (6, 8),
    'eva_15_beginning':        (6, 8),
    # jailhouse-rock-elvis-presley-.pdf · leido 4/4
    'jm_08_jailhouse':         (4, 4),
    'me_24_jailhouse':         (4, 4),
    'is_17_jailhouse':         (4, 4),
    'jp_09_jailhouse':         (4, 4),
    'nl_06_jailhouse':         (4, 4),
    # merry-go-round-of-life.pdf · leido 3/4
    'jp_18_merry':             (3, 4),
    'nl_15_merry':             (3, 4),
    # my-favourite-things-the-sound-.pdf · leido 3/4
    'jp_15_favourite':         (3, 4),
    'nl_13_favourite':         (3, 4),
    'dilan_15_favourite':      (3, 4),
    'eva_12_favourite':        (3, 4),
    # nocturne-op9-chopin. easy · leido 3/4
    'lu_19_nocturne':          (3, 4),
    'me_27_nocturne':          (3, 4),
    # petite chanson(4 manos).pdf · leido 4/4
    'is_01_petite':            (4, 4),
    'jp_02_petite':            (4, 4),
    'nl_01_petite':            (4, 4),
    # piano-man-easy. · leido 3/4
    'lu_11_pianoman':          (3, 4),
    'me_13_pianoman':          (3, 4),
    'is_10_pianoman':          (3, 4),
    # puff-the-magic-dragon.pdf · leido 4/4
    'arnau_12_puff':           (4, 4),
    'lu_05_puff':              (4, 4),
    'me_04_puff':              (4, 4),
    'is_03_puff':              (4, 4),
    # rain-rain-away-easy-piano-4 manos.pdf · leido 4/4
    'arnau_19_rain':           (4, 4),
    # rasputin easy.pdf · leido 4/4
    'lu_17_rasputin':          (4, 4),
    'jm_14_rasputin':          (4, 4),
    'me_23_rasputin':          (4, 4),
    'is_16_rasputin':          (4, 4),
    'jp_13_rasputin':          (4, 4),
    'nl_11_rasputin':          (4, 4),
    # rihanna-diamond-.pdf · leido 4/4
    'nl_12_diamonds':          (4, 4),
    # silent-night-4-hands. · leido 3/4
    'me_11_silentnight4h':     (3, 4),
    'is_08_silentnight4h':     (3, 4),
    # sweet-child-o-mine-guns-n-roses-easy-piano.pdf · leido 4/4
    'jp_16_sweetchild':        (4, 4),
    'nl_14_sweetchild':        (4, 4),
    # the-mulberry-bush-185807.4 manos.pdf · leido 6/8
    'arnau_20_mulberry':       (6, 8),
    # the-swan.pdf · leido 3/4
    'dilan_01_cancion':        (3, 4),
    'eva_06_cisne':            (3, 4),
    # what-was-i-made-for-billie-eilish.pdf · leido 4/4
    'jp_05_what':              (4, 4),
    'dilan_13_what':           (4, 4),
    'eva_04_what':             (4, 4),
    # youve-got-a-friend-in-me-easy-piano-.pdf · leido 4/4
    'lu_04_friend':            (4, 4),
    'me_03_friend':            (4, 4),
    # ------------------------------------------------------------------
    # EDUARD. Su cuaderno se rehizo entero en agosto de 2026 a partir de SU
    # carpeta de Drive (antes era una copia del de Jose Maria y le quedaba muy
    # por encima del nivel). Las 16 partituras nuevas se leyeron una por una
    # con el recorte ampliado; las cuatro que vienen del dosier antiguo
    # —Romance, America, Star-Spangled y Deck the Halls— conservan la lectura
    # que ya tenian, porque el PDF es el mismo fichero.
    'ed_01_clementine':        (3, 4),
    'ed_02_aristogatos':       (4, 4),
    'ed_03_eso':               (4, 4),
    'ed_04_america':           (3, 4),
    'ed_05_banner':            (3, 4),
    'ed_06_pantera':           (4, 4),
    'ed_07_nocturno':          (3, 4),
    'ed_08_beginner':          (3, 4),
    'ed_09_puff':              (4, 4),
    'ed_10_heart':             (4, 4),
    'ed_11_dream':             (4, 4),
    'ed_12_navidad':           (4, 4),
    'ed_13_greensleeves':      (3, 4),
    'ed_14_honor':             (3, 4),
    'ed_15_rasputin':          (4, 4),
    'ed_16_jinglerock':        (4, 4),
    'ed_17_pianoman':          (3, 4),
    'ed_18_clock':             (4, 4),
    'ed_19_toreador':          (4, 4),

    # --- AIDA -------------------------------------------------------
    # Leidas el 31 de agosto de 2026 sobre los PDF de SU carpeta de
    # Drive, recorte a recorte. Diez de las diecinueve son el mismo
    # fichero que el de otro alumno (md5 comprobado) y por eso repiten
    # exactamente la lectura que ya estaba anotada.
    'ai_01_romance':           (2, 2),
    'ai_02_scherzo':           (3, 4),
    'ai_03_wewishyou':         (3, 4),
    'ai_04_canthelp':          (3, 4),
    'ai_05_what':              (4, 4),
    'ai_06_counting':          (4, 4),
    'ai_07_perfect':           (12, 8),
    'ai_08_boig':              (4, 4),
    'ai_09_kiss':              (4, 4),
    'ai_10_beginning':         (6, 8),
    'ai_11_titanic':           (2, 4),
    'ai_12_hijoluna':          (6, 8),
    'ai_13_carol':             (3, 4),
    'ai_14_silence':           (4, 4),
    'ai_15_gladiator':         (4, 4),
    'ai_16_unbeso':            (4, 4),
    'ai_17_pachelbel':         (4, 4),
    'ai_18_preludio':          (4, 4),
    'ai_19_acomme':            (4, 4),
}


def _cfg(modulo):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        mod = importlib.import_module(modulo)
    return getattr(mod, 'CANCION', None)


def main(prefijos=None):
    prefijos = prefijos or PREFIJOS
    malos, sin_leer = [], []
    n = 0
    for p in prefijos:
        for f in sorted(glob.glob(os.path.join(HERE, p + '_[0-9]*.py'))):
            m = os.path.basename(f)[:-3]
            cfg = _cfg(m)
            if not cfg or not cfg.get('partitura'):
                continue
            n += 1
            ts = tuple(cfg.get('time_sig') or ())
            if m not in LEIDO:
                sin_leer.append((m, os.path.basename(cfg['partitura'])))
            elif ts != LEIDO[m]:
                malos.append((m, ts, LEIDO[m], os.path.basename(cfg['partitura'])))

    print('piezas comprobadas: %d de %d con lectura anotada' % (n, len(LEIDO)))

    print('\nEL DOSIER DICE UN COMPAS Y LA PARTITURA TRAE OTRO: %d' % len(malos))
    for m, ts, leido, base in malos:
        print('   %-22s dice %d/%d · impreso %d/%d · %s'
              % (m, ts[0], ts[1], leido[0], leido[1], base[:38]))

    print('\nPiezas cuyo compas no ha leido nadie en la partitura: %d' % len(sin_leer))
    for m, base in sin_leer:
        print('   %-22s %s' % (m, base[:50]))

    if malos or sin_leer:
        print('\n%d COSAS QUE MIRAR' % (len(malos) + len(sin_leer)))
        return 1
    print('\nCOMPASES OK — lo que declara el dosier es lo que trae la partitura.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or None))
