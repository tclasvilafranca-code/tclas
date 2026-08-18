# -*- coding: utf-8 -*-
"""Merry Go Round of Life (Joe Hisaishi) — pieza 15 de Nel.

   Lo comprobado sobre el PDF de su carpeta de Drive ("for Piano Solo",
   Musescore, 2 páginas, 45 compases; el mismo archivo que la pieza 18 de
   Josep, byte a byte):

     - Dos bemoles detrás de la clave: Si bemol mayor / Sol menor.
     - Compás de 3/4.
     - Dos tempos escritos: empieza a "♩ = 120" y en el c. 27 pone
       "♩ = 152".
     - Los cuatro primeros compases la derecha hace terceras en corcheas
       seguidas y la izquierda calla (silencios de compás): introducción.
     - En el c. 5 pone "rit." y en el c. 6 "a tempo".
     - Del c. 27 en adelante la izquierda hace bajo + acorde de vals.
     - Hay barra de repetición al final.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from nl_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SIB = 'Sib mayor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=15, nivel='avanzado', slug='MerryGoRoundOfLife',
    formato='adulto',
    titulo_corto='Merry Go Round of Life', time_sig=(3, 4), key_sig=SIB,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'Merry-go-round-of-life-easy-piano-excerpt.pdf'),
    yt='https://www.youtube.com/results?search_query=merry+go+round+of+life+piano',

    ficha=dict(
        titulo='Merry Go Round of Life',
        autor='Joe Hisaishi · de "El castillo ambulante" · para piano solo',
        datos=[('Tonalidad', 'Si bemol mayor'), ('Compás', '3/4'),
               ('Tempo', '♩ = 120 → 152'), ('Introducción', 'Terceras'),
               ('Páginas', 'Dos · 45 compases')],
        titulo_ritmos='La introducción y el vals',
        pie_ritmos='Andamio en Si bemol mayor. Lo literal es la estructura: terceras en corcheas al '
                   'principio y bajo con acorde de vals a partir del compás 27.',
        armonia=dict(
            titulo='Dos piezas y dos velocidades',
            tarjetas=[
                ('DOS TEMPOS', '120 y 152',
                 'Empieza a ♩ = 120 y en el compás 27 pasa a ♩ = 152: la única pieza de tu álbum '
                 'con dos velocidades escritas.'),
                ('LAS TERCERAS', 'La introducción',
                 'Los cuatro primeros compases son dobles notas en corcheas seguidas, con la '
                 'izquierda callada: lo más difícil de la pieza, en la primera línea.'),
                ('rit. y a tempo', 'Escritos',
                 'En el compás 5 pone "rit." y en el 6 "a tempo": no es libertad del intérprete, '
                 'viene escrito.'),
                ('EL VALS', 'Desde el c. 27',
                 'La izquierda pasa a bajo en el uno y acorde en el dos y el tres: el mismo reparto '
                 'de Heart and Soul, pero en tres y al doble de velocidad.'),
            ],
            pie='Joe Hisaishi lleva componiendo para las películas de Hayao Miyazaki desde 1984. El '
                'vals aparece una y otra vez en la película con orquestaciones distintas.',
        ),
        ritmos=[
            ('MANO DERECHA · INTRO', 'terceras en corcheas · andamio',
             [ac(('D5', 'F5'), 'e'), ac(('Eb5', 'G5'), 'e'), ac(('D5', 'F5'), 'e'),
              ac(('C5', 'Eb5'), 'e'), ac(('D5', 'F5'), 'e'), ac(('Eb5', 'G5'), 'e')],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA · c. 27', 'bajo y acorde de vals · andamio',
             [n('Bb2'), ac(('D3', 'F3')), ac(('D3', 'F3'))], AZUL, 'bass', None),
        ],
        especial=[
            'Dos bemoles detrás de la clave: Si bemol y Mi bemol.',
            'Compás de 3/4.',
            'Empieza a "♩ = 120" y en el compás 27 pone "♩ = 152".',
            'Los cuatro primeros compases son terceras en corcheas, con la izquierda callada.',
            'En el compás 5 pone "rit." y en el 6 "a tempo".',
            'Del compás 27 en adelante la izquierda hace bajo y acorde de vals.',
        ],
        reto='Las terceras de la introducción, seguidas y a ♩ = 120: dos teclas a la vez, ocho veces '
             'por compás, sin que se separe ninguna pareja.',
        truco='Trabaja las terceras de dos en dos: toca la pareja, para, toca la siguiente. Une de '
              'cuatro en cuatro solo cuando las parejas sueltas salgan limpias.',
        sabias='El vals aparece una y otra vez a lo largo de la película con orquestaciones muy '
               'distintas: es el mismo tema, y nunca suena igual dos veces.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en el cambio de velocidad a mitad de pieza: lo vas a oír antes de '
                      'verlo escrito.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza empieza por lo más difícil. Los cuatro primeros compases son todo el '
              'trabajo de la semana, y cuando salgan, el resto de la pieza ya está prácticamente hecho.',
        reglas=['LAS TERCERAS, DE DOS EN DOS', 'DOS VELOCIDADES: 120 Y 152',
                'EL "rit." VIENE ESCRITO'],
        bloques=[
            dict(num=1, titulo='Las terceras, pareja a pareja',
                 pista='andamio en Si bemol mayor · toca la pareja, para, toca la siguiente',
                 sistemas=[
                     dict(cap='a) empezando un peldaño más arriba, con parada larga',
                          events=[ac(('F5', 'A5'), 'q'), ac(('G5', 'Bb5'), 'h'),
                                  ac(('F5', 'A5'), 'q'), ac(('Eb5', 'G5'), 'h')],
                          bars=2, key_sig=SIB, time_sig=(3, 4)),
                     dict(cap='b) y de dos en dos parejas seguidas, con otro dibujo',
                          events=[ac(('F5', 'A5'), 'e'), ac(('G5', 'Bb5'), 'e'), ac(('F5', 'A5'), 'h'),
                                  ac(('Eb5', 'G5'), 'e'), ac(('F5', 'A5'), 'e'),
                                  ac(('G5', 'Bb5'), 'h')],
                          bars=2, key_sig=SIB, time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=2, titulo='El vals del c. 27: bajo y acorde', clef='bass',
                 pista='la FORMA es literal (bajo en el uno, acorde en el dos y el tres)',
                 sistemas=[
                     dict(cap='a) el bajo pesa y los dos acordes no, con otro punto de partida',
                          events=[n('Eb2'), ac(('G2', 'Bb2')), ac(('G2', 'Bb2')),
                                  n('Ab2'), ac(('C3', 'Eb3')), ac(('C3', 'Eb3'))],
                          bars=2, clef='bass', key_sig=SIB, time_sig=(3, 4)),
                     dict(cap='b) cambiando de bajo, con otra pareja de acordes',
                          events=[n('D2'), ac(('F2', 'A2')), ac(('F2', 'A2')),
                                  n('C2'), ac(('Eb2', 'G2')), ac(('Eb2', 'G2'))],
                          bars=2, clef='bass', key_sig=SIB, time_sig=(3, 4), show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LOS DOS TEMPOS, POR SEPARADO',
                 texto='Esta pieza tiene dos velocidades escritas y son dos ejercicios distintos. '
                       'Estudia la primera parte a 120 y la segunda a 152 cada una por su lado: si '
                       'las estudias a la misma velocidad, luego hay que desaprender una de las dos.'),
            dict(num=3, titulo='Las dos manos en el vals',
                 pista='andamio en Si bemol mayor · esta parte a 152, la introducción a 120',
                 sistemas=[
                     dict(cap='a) melodía arriba y vals abajo, con otro punto de partida',
                          events=[ac(('Eb2', 'G5'), 'q'), ac(('G2', 'Bb2')), ac(('G2', 'Bb2')),
                                  ac(('Ab2', 'F5'), 'q'), ac(('C3', 'Eb3')), ac(('C3', 'Eb3'))],
                          bars=2, key_sig=SIB, time_sig=(3, 4)),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
