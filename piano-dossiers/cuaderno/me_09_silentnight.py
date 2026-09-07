# -*- coding: utf-8 -*-
"""Silent Night, de Gruber — pieza 9 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive (2 páginas, con letra en
   dos idiomas; el mismo archivo que la pieza 8 de Luisa, byte a byte), leído
   a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 3/4, y arriba pone "Gently". Encima del primer compás hay una letra de
       acorde impresa: C.
     - La derecha empieza con negra con puntillo, corchea y negra; el compás
       siguiente es una blanca con puntillo.
     - La izquierda hace negra y blanca: cambia en el uno y se queda hasta el
       final del compás.
     - Trae digitación impresa y la letra debajo del pentagrama.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from me_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=9, nivel='intermedio', slug='SilentNight',
    formato='adulto',
    titulo_corto='Silent Night', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'SILENT NINGT.easy'),
    yt='https://www.youtube.com/results?search_query=silent+night+easy+piano',

    ficha=dict(
        titulo='Silent Night',
        autor='Franz Xaver Gruber · 1818 · con letra y con los dedos escritos',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'Gently'), ('Izquierda', 'Negra y blanca'),
               ('Trae', 'Letra de acorde')],
        titulo_ritmos='Cada mano con su propio ritmo',
        pie_ritmos='El ritmo es el de tu partitura, medido. La izquierda cambia una sola vez por '
                   'compás y la derecha, con el dibujo largo-corto-medio.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('DOS RITMOS DISTINTOS', 'Uno en cada mano',
                 'La derecha lleva negra con puntillo, corchea y negra; la izquierda, negra y '
                 'blanca. No coinciden en todos los tiempos, y ese es el trabajo de la semana.'),
                ('LARGO, CORTO, MEDIO', 'En la melodía',
                 'Se cuenta "UUUN, y-dos, tres". El corto va pegado a la nota siguiente, no a la de '
                 'antes.'),
                ('UNA LETRA DE ACORDE', 'La C del principio',
                 'Te dice qué notas suenan debajo, aunque tú toques solo dos de ellas con la mano '
                 'izquierda.'),
                ('COMPÁS DE TRES', 'Como un vals',
                 'Se cuenta uno-dos-tres, y el uno pesa más que los otros dos tiempos.'),
            ],
            pie='Se estrenó en Nochebuena de 1818 en un pueblo de Austria, y desde entonces es una '
                'de las canciones navideñas más traducidas del mundo.',
        ),
        ritmos=[
            # Medido nota a nota sobre el PDF a 300 ppp (21 ago 2026). Decia
            # Mi-Fa-Mi y Do-Sol: la melodia esta una TERCERA mas arriba (Sol-La-Sol,
            # que es el 5-6-5 de siempre de este villancico) y la segunda nota de
            # la izquierda es un Mi, no un Sol. El ritmo si estaba bien.
            ('MANO DERECHA', 'largo, corto, medio · literal',
             [n('G4', 'q.'), n('A4', 'e'), n('G4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'negra y blanca · literal',
             [n('C3'), n('E3', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 3/4, con "Gently" escrito arriba.',
            'Encima del primer compás hay una letra de acorde: C.',
            'La derecha hace negra con puntillo, corchea y negra.',
            'La izquierda hace negra y blanca: una sola vez por compás.',
            'Trae dedos escritos y la letra de la canción debajo del pentagrama.',
        ],
        reto='Que la izquierda no se mueva mientras la derecha hace la nota corta. Cada mano tiene '
             'su propio ritmo, y hay que sostener uno mientras se mueve el otro.',
        truco='Aguanta la blanca de la izquierda y, sin soltarla, cuenta en voz alta "y-dos" '
              'mientras la derecha hace su nota corta. Lo que suele fallar es soltar la izquierda '
              'antes de tiempo, no tocar mal la derecha.',
        sabias='Se tocó por primera vez con guitarra, no con órgano: hay quien dice que el órgano de '
               'la iglesia se había estropeado esa Nochebuena. En 2011 la UNESCO la declaró '
               'patrimonio cultural inmaterial.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate solo en la mano izquierda del acompañamiento: cambia una vez por '
                      'compás, y ese balanceo lento es lo que le da su carácter.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Las dos manos ya no hacen lo mismo: cada una tiene su propio dibujo. Se separan, se '
              'aprenden por dentro y solo al final se juntan.',
        reglas=['LA IZQUIERDA CAMBIA UNA VEZ POR COMPÁS', 'CUENTA "UN, DOS, TRES" EN VOZ ALTA',
                'JUNTARLAS ES EL ÚLTIMO PASO'],
        bloques=[
            dict(num=1, titulo='La izquierda sola: negra y blanca',
                 pista='andamio en Do mayor · el ritmo es el de tu partitura',
                 sistemas=[
                     dict(cap='a) toca en el uno y aguanta hasta el final del compás',
                          events=[n('C3'), n('E3', 'h'), n('F2'), n('A2', 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de sitio, con el dedo preparado antes de tiempo',
                          events=[n('G2'), n('B2', 'h'), n('C3'), n('E3', 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha sola: largo, corto, medio',
                 pista='andamio · cuenta "UUUN, y-dos, tres" en voz alta mientras tocas',
                 sistemas=[
                     dict(cap='a) el ritmo de la pieza, con la nota corta pegada a la siguiente',
                          events=[n('D4', 'q.'), n('E4', 'e'), n('D4'), n('B3', 'h.')],
                          bars=2),
                     dict(cap='b) el mismo ritmo un poco más arriba',
                          events=[n('G4', 'q.'), n('A4', 'e'), n('G4'), n('E4', 'h.')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ PRIMERO SE ESTUDIAN SEPARADAS',
                 texto='Cuando cada mano tiene un ritmo distinto, tocar de golpe las dos junta dos '
                       'dificultades a la vez: acertar las notas y coordinar dos pulsos que no '
                       'coinciden en todos los tiempos. Aprender cada mano hasta que suene segura '
                       'por su cuenta es lo que hace que el paso 3 no se convierta en adivinar.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · muy despacio, dejando sonar la blanca de la izquierda entera',
                 sistemas=[
                     dict(cap='a) la izquierda aguanta mientras la derecha hace su ritmo',
                          events=[ac(('C3', 'E4'), 'q.'), n('F4', 'e'), n('E4'),
                                  ac(('F2', 'C4'), 'h.')],
                          bars=2),
                     dict(cap='b) y con la frase que sigue',
                          events=[ac(('G2', 'G4'), 'q.'), n('A4', 'e'), n('G4'),
                                  ac(('C3', 'E4'), 'h.')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 42, 'C4', 'C3',
                          'compás de tres: el peso va al primero y los otros dos acompañan',
                          desde=4, time_sig=(3, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
