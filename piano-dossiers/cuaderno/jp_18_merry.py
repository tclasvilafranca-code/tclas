# -*- coding: utf-8 -*-
"""Merry Go Round of Life (Joe Hisaishi) — pieza 18 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive ("for Piano Solo",
   Musescore, 2 páginas, 45 compases):

     - DOS BEMOLES detrás de la clave: Si bemol mayor / Sol menor.
     - Compás de 3/4.
     - DOS TEMPOS ESCRITOS: empieza a "♩ = 120" y en el c. 27 pone "♩ = 152".
       Es la única pieza del cuaderno con dos velocidades marcadas.
     - Los cuatro primeros compases la derecha hace TERCERAS EN CORCHEAS
       seguidas y la izquierda calla (silencios de compás): es la introducción.
     - En el c. 5 pone "rit." y en el c. 6 "a tempo".
     - Del c. 27 en adelante la izquierda hace bajo + acorde de vals.
     - Hay barra de repetición al final.

   Todo el material inventado va como ANDAMIO en Si bemol mayor.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, sil, reto, plan, escalera, inventa, teclado, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=18, nivel='intermedio', slug='MerryGoRoundOfLife',
    formato='adulto',
    titulo_corto='Merry Go Round of Life', time_sig=(3, 4), key_sig='Sib mayor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source', 'merry-go-round-of-life.pdf'),
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
                 'Empieza a ♩ = 120 y en el compás 27 pasa a ♩ = 152. Es la única pieza del '
                 'cuaderno con dos velocidades escritas, y el cambio está marcado.'),
                ('LAS TERCERAS', 'La introducción',
                 'Los cuatro primeros compases son dobles notas en corcheas seguidas, con la '
                 'izquierda callada. Es lo más difícil de la pieza y está en la primera línea.'),
                ('rit. y a tempo', 'Escritos',
                 'En el compás 5 pone "rit." (frenar) y en el 6 "a tempo" (volver). No es libertad '
                 'de intérprete: viene escrito y hay que hacerlo.'),
                ('EL VALS', 'Desde el c. 27',
                 'La izquierda pasa a bajo en el uno y acorde en el dos y el tres. Es el mismo '
                 'reparto de Heart and Soul, pero en tres y al doble de velocidad.'),
            ],
            pie='La pieza empieza por lo más difícil, que es una crueldad de la edición y una suerte '
                'para estudiarla: si trabajas los cuatro primeros compases hasta el final del mes, '
                'el resto de la pieza ya lo sabes tocar.',
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
        reto='Las terceras de la introducción, seguidas y a ♩ = 120. Dos teclas a la vez, ocho veces '
             'por compás, con la mano abierta y sin que se separe ninguna pareja.',
        truco='Trabaja las terceras de DOS EN DOS: toca la pareja, para, toca la siguiente, para. '
              'Cuando las ocho parejas del compás salgan sueltas, únelas de cuatro en cuatro, y solo '
              'al final el compás entero. Nunca empieces por el compás entero: solo aprendes a '
              'tropezar más rápido.',
        sabias='Joe Hisaishi lleva componiendo para las películas de Hayao Miyazaki desde 1984, y '
               'esta es de "El castillo ambulante". El vals aparece una y otra vez a lo largo de la '
               'película con orquestaciones distintas: es el mismo tema y no suena igual dos veces.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en el cambio de velocidad a mitad de pieza. Lo vas a oír antes de '
                      'verlo escrito, y en tu partitura está marcado con un número.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza empieza por lo más difícil. Aprovéchalo: los cuatro primeros compases son '
              'todo el trabajo del mes, y cuando salgan, el resto de la pieza ya está.',
        reglas=['LAS TERCERAS, DE DOS EN DOS', 'DOS VELOCIDADES: 120 Y 152',
                'EL "rit." VIENE ESCRITO'],
        bloques=[
            dict(num=1, titulo='Las terceras, pareja a pareja',
                 pista='andamio en Si bemol mayor · toca la pareja, para, toca la siguiente',
                 sistemas=[
                     dict(cap='a) las dos notas juntas y una parada larga · si oyes dos golpes en '
                              'vez de uno, ahí está el trabajo',
                          events=[ac(('D5', 'F5'), 'q'), ac(('Eb5', 'G5'), 'h'),
                                  ac(('D5', 'F5'), 'q'), ac(('C5', 'Eb5'), 'h')],
                          bars=2, key_sig='Sib mayor', time_sig=(3, 4)),
                     dict(cap='b) y ahora de dos en dos parejas seguidas · la mano se abre una vez y '
                              'ya no se cierra entre pareja y pareja',
                          events=[ac(('D5', 'F5'), 'e'), ac(('Eb5', 'G5'), 'e'), ac(('D5', 'F5'), 'h'),
                                  ac(('C5', 'Eb5'), 'e'), ac(('D5', 'F5'), 'e'),
                                  ac(('Eb5', 'G5'), 'h')],
                          bars=2, key_sig='Sib mayor', time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=2, titulo='El vals del c. 27: bajo y acorde', clef='bass',
                 pista='la FORMA es literal (bajo en el uno, acorde en el dos y el tres)',
                 sistemas=[
                     dict(cap='a) el bajo pesa y los dos acordes no · a 152 los acordes tienen que '
                              'ser casi un roce',
                          events=[n('Bb2'), ac(('D3', 'F3')), ac(('D3', 'F3')),
                                  n('F2'), ac(('C3', 'F3')), ac(('C3', 'F3'))],
                          bars=2, clef='bass', key_sig='Sib mayor', time_sig=(3, 4)),
                     dict(cap='b) cambiando de bajo, que es donde se rompe · el brazo va al bajo '
                              'nuevo mientras suena el último acorde del compás anterior',
                          events=[n('Eb2'), ac(('G2', 'Bb2')), ac(('G2', 'Bb2')),
                                  n('G2'), ac(('Bb2', 'D3')), ac(('Bb2', 'D3'))],
                          bars=2, clef='bass', key_sig='Sib mayor', time_sig=(3, 4), show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LOS DOS TEMPOS, POR SEPARADO',
                 texto='Esta pieza tiene dos velocidades escritas y son dos ejercicios distintos. '
                       'Estudia la primera parte a 120 y la segunda a 152 desde el principio, cada '
                       'una por su lado: si las estudias las dos a la misma velocidad, luego hay '
                       'que desaprender una de las dos, y desaprender cuesta más que aprender.'),
            dict(num=3, titulo='Las dos manos en el vals',
                 pista='andamio en Si bemol mayor · esta parte a 152, la introducción a 120',
                 sistemas=[
                     dict(cap='a) melodía arriba y vals abajo · la melodía va en notas largas, así '
                              'que a 152 lo que corre es la izquierda',
                          events=[ac(('Bb2', 'F5'), 'q'), ac(('D3', 'F3')), ac(('D3', 'F3')),
                                  ac(('F2', 'Eb5'), 'q'), ac(('C3', 'F3')), ac(('C3', 'F3'))],
                          bars=2, key_sig='Sib mayor', time_sig=(3, 4)),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Merry Go Round of Life · para casa',
            intro='Veinte minutos, y quince de ellos en los cuatro primeros compases.',
            bloques=[
                reto('Los cuatro compases de la introducción, seguidos, a ♩ = 120.',
                     'Pareja a pareja con parada, después de dos en dos, después de cuatro en '
                     'cuatro, y solo el último día el compás entero. Si empiezas por el compás '
                     'entero, lo único que aprendes es a tropezar más rápido.'),
                plan((8, 'Las terceras de la introducción, pareja a pareja'),
                     (4, 'El vals del c. 27, izquierda sola, a 152'),
                     (4, 'La melodía de la segunda parte, sola'),
                     (4, 'Las dos manos de la segunda parte, muy lento')),
                escalera((60, 'las parejas de terceras, con parada'),
                         (90, 'de cuatro en cuatro parejas'),
                         (120, 'la introducción entera: su primer tempo'),
                         meta='♩ = 120 para la introducción y ♩ = 152 para el c. 27 en adelante, '
                              'que es lo que pone tu partitura',
                         notas=['Las dos partes se suben por separado: son dos escaleras, no una.']),
                inventa(['Solo terceras: dos teclas a la vez, saltando una en medio.',
                         'Dos compases de tres golpes.',
                         'Con Si bemol y Mi bemol donde toque.'],
                        time_sig=(3, 4),
                        titulo='Inventa dos compases de terceras',
                        pista='y tócalos pareja a pareja, como el ejercicio 1'),
                teclado({6: 1, 2: 2, 4: 3},
                        ['Escribe el nombre de las tres teclas blancas marcadas.',
                         'Y pinta las dos negras de tu armadura: Si bemol y Mi bemol.'],
                        titulo='En el teclado',
                        pista='la número 1 es el Si'),
                para_clase('Los cuatro compases de la introducción a la velocidad que hayas '
                           'alcanzado, aunque sea a 70. Y dime si alguna pareja de terceras se te '
                           'separa siempre: casi seguro es una en la que la mano tiene que abrirse '
                           'más de lo que puede sin girar la muñeca.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
