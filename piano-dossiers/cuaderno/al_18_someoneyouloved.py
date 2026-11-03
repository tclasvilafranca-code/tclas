# -*- coding: utf-8 -*-
"""Someone You Loved (Lewis Capaldi) — pieza 18 de Alan. ADULTO exigente,
   tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (Campamento Musical Bye Bye
   Beethoven, 3 páginas, VECTORIAL), medido a 300 ppp contra las líneas del
   pentagrama:

     - Detrás de la clave no hay nada. 4/4. No trae tempo ni intensidad.
     - 58 compases en tres páginas. Barra de repetición desde el c. 5 hasta el c. 28,
       con casilla de primera vez (c. 28) y de segunda (c. 29). Un 8va sobre las dos
       manos hacia los cc. 37-45. Termina con un calderón sobre un acorde. Muchas
       notas unidas por una curva entre compases.
     - Ninguna figura más corta que la corchea: corcheas seguidas, negras,
       blancas, negras con puntillo y redondas.
     - MEDIDO, mano derecha (ocho corcheas por compás, alternando dos notas):
       c. 1: Mi5 · Sol4 · Mi5 · Sol4 · Mi5 · Sol4 · Mi5 · Sol4
       c. 2: Si4 · Re4 · Si4 · Re4 · Si4 · Re4 · Si4 · Re4
       c. 3: Do5 · Mi4 · Do5 · Mi4 · Do5 · Mi4 · Do5 · Mi4
       c. 4: La4 · Do4 · La4 · Do4 · La4 · Do4 · Sol4 · Do4
     - MEDIDO, mano izquierda: una redonda por compás, Do4 · Sol3 · La3 · Fa3.
   Del c. 5 en adelante la izquierda toca dos notas (negra y blanca, o las dos en
   redonda) y la derecha pasa a una melodía con notas unidas por una curva: va como ANDAMIO.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, plan, escalera, rodear, escribir, verdadero_falso,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def par(a, b, veces=4):
    return [n(a, 'e'), n(b, 'e')] * veces


# MEDIDO: cc. 1-4 (derecha)
C1 = par('E5', 'G4')
C2 = par('B4', 'D4')
C3 = par('C5', 'E4')
C4 = par('A4', 'C4', 3) + [n('G4', 'e'), n('C4', 'e')]
# MEDIDO: cc. 1-4 (izquierda)
LH = [n('C4', 'w'), n('G3', 'w'), n('A3', 'w'), n('F3', 'w')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=18, nivel='intermedio', slug='SomeoneYouLoved',
    formato='adulto',
    titulo_corto='Someone You Loved', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'SOMEONE YOU LOVED.'),
    yt='https://www.youtube.com/results?search_query=someone+you+loved+piano+easy',

    ficha=dict(
        titulo='Someone You Loved',
        autor='Lewis Capaldi · versión de Bye Bye Beethoven',
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Repetición', 'cc. 5-28'),
               ('Páginas', 'Tres')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: ocho corcheas por compás que alternan una '
                   'nota aguda y otra grave. Abajo, medido: una redonda por compás.',
        armonia=dict(
            titulo='Un arpegio que no para, y cuatro acordes que se repiten',
            tarjetas=[
                ('EL ARPEGIO', 'Aguda y grave',
                 'Cada compás de la derecha son ocho corcheas que alternan una nota aguda y una '
                 'grave: Mi5 con Sol4, Si4 con Re4, Do5 con Mi4… La mano salta, no se estira.'),
                ('LA IZQUIERDA', 'Una redonda',
                 'En los cuatro primeros compases la izquierda toca una sola nota por compás: Do4, '
                 'Sol3, La3 y Fa3. Aguanta cuatro golpes y no se mueve.'),
                ('LA REPETICIÓN', 'Casillas 1 y 2',
                 'Desde el c. 5 hasta el c. 28 hay barra de repetición, con una casilla de primera '
                 'vez y otra de segunda. Aprende dónde se salta antes de tocar.'),
                ('EL 8VA', 'Las dos manos',
                 'Hacia el c. 37 aparece un 8va sobre las dos manos: todo suena una octava más '
                 'alto de lo escrito durante unos nueve compases. Al final, un calderón.'),
            ],
            pie='58 compases, tres páginas y una estructura que se repite: cuatro acordes dando '
                'vueltas. Si los cuatro primeros compases salen limpios, la pieza entera se '
                'sostiene sola.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-2 · medido', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'cc. 1-2 · medido', [n('C4', 'w'), n('G3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 4/4 y no trae número de metrónomo.',
            'La derecha de los cc. 1-4 son ocho corcheas por compás.',
            'La izquierda de los cc. 1-4 son redondas: Do4, Sol3, La3 y Fa3.',
            'Hay barra de repetición con casilla de primera y de segunda vez.',
            'Hacia el c. 37 aparece un 8va sobre las dos manos, y al final un calderón.',
        ],
        reto='Tocar los cuatro primeros compases con las ocho corcheas iguales y la izquierda '
             'sin moverse: arriba salta, abajo se queda.',
        truco='Toca primero solo las notas graves de la derecha, y después solo las agudas. Cuando '
              'cada una suene sola y pareja, júntalas.',
        sabias='Lewis Capaldi la compuso tras la muerte de su abuela, y salió en 2018. Fue número '
               'uno en el Reino Unido y en muchos países más, y lleva más de dos mil millones de '
               'reproducciones.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el piano del principio y cuenta los cuatro acordes que se repiten. '
                      'Si los reconoces de oído, ya sabes cuándo cambia la izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El arpegio se estudia en dos manos pequeñas: primero las graves, luego las agudas y '
              'solo después las ocho juntas. La izquierda, al final.',
        reglas=['LAS GRAVES Y LAS AGUDAS, POR SEPARADO', 'LA IZQUIERDA NO SE MUEVE',
                'LA REPETICIÓN TIENE DOS CASILLAS'],
        bloques=[
            dict(num=1, titulo='Los compases 3 y 4, nota a nota',
                 pista='cc. 3-4 · medidos sobre tu partitura · Do5-Mi4 y La4-Do4, con una sola '
                       'nota que cambia',
                 sistemas=[
                     dict(cap='a) Do5 y Mi4, cuatro veces · una nota aguda y una grave, sin '
                              'acentuar ninguna',
                          events=C3, bars=1),
                     dict(cap='b) La4 y Do4 tres veces, y la última pareja baja de La a Sol',
                          events=C4, bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='Las notas de arriba, separadas',
                 pista='cc. 1-4 · sacadas de tu partitura · solo la nota aguda de cada pareja',
                 sistemas=[
                     dict(cap='a) Mi5, Si4, Do5 y La4 · la melodía escondida dentro del arpegio',
                          events=[n('E5', 'h'), n('B4', 'h'), n('C5', 'h'), n('A4', 'h')],
                          bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE ESTUDIAN LAS NOTAS GRAVES Y LAS AGUDAS POR SEPARADO',
                 texto='En el arpegio hay dos voces escondidas: la aguda, que dibuja la melodía, y '
                       'la grave, que va por debajo. Si las tocas por separado, oyes cada una y '
                       'corriges la que cojea. Después se juntan y la mano salta de una a otra '
                       'sin que se note.'),
            dict(num=3, titulo='La izquierda, una redonda por compás',
                 pista='cc. 1-4 · medidos sobre tu partitura · Do4, Sol3, La3 y Fa3',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) cuatro redondas, una por compás · el Do4 queda por encima del '
                              'pentagrama, en una línea adicional',
                          events=LH, bars=4, clef='bass'),
                 ]),
            dict(num=4, titulo='Las dos manos, cc. 1-2',
                 pista='cc. 1-2 · la derecha es MEDIDA · la izquierda también, en una redonda',
                 sistemas=[
                     dict(cap='a) las ocho corcheas de arriba con la redonda de abajo · la '
                              'redonda suena una vez y se queda',
                          events=[ac(('C4', 'E5'), 'e'), n('G4', 'e'), n('E5', 'e'), n('G4', 'e'),
                                  n('E5', 'e'), n('G4', 'e'), n('E5', 'e'), n('G4', 'e')],
                          bars=1, manos='sostiene'),
                 ]),
            dict(num=5, titulo='La repetición con dos casillas',
                 pista='andamio · la forma de los cc. 5-29 de tu partitura: primera casilla y '
                       'segunda casilla',
                 sistemas=[
                     dict(cap='a) la primera vez acaba así y se vuelve atrás · el compás de la '
                              'casilla 2 no se toca',
                          events=[n('E4'), n('G4'), n('A4'), n('G4'), n('E4', 'h'), n('D4', 'h')],
                          bars=2, repetir='cierra', casilla='1'),
                     dict(cap='b) la segunda vez se salta el compás de arriba y se toca este',
                          events=[n('E4', 'h'), n('C4', 'h')],
                          bars=1, show_time=False, casilla='2'),
                 ]),
            dict(num=6, titulo='El 8va y el calderón del final',
                 pista='andamio · lo que hacen los dos signos de tu partitura: el 8va sube una '
                       'octava y el calderón alarga',
                 sistemas=[
                     dict(cap='a) las mismas notas con 8va · suenan una octava más alto de lo '
                              'escrito durante todo el tramo',
                          events=[n('C5', 'e'), n('E5', 'e'), n('C5', 'e'), n('E5', 'e'),
                                  n('D5', 'h')],
                          bars=1, ottava=True),
                     dict(cap='b) un acorde con calderón · se aguanta más de lo que dura, y el '
                              'final lo decides tú',
                          events=[dict(ac(('C4', 'E4', 'G4'), 'w'), art='calderon')],
                          bars=1, show_time=False),
                 ]),
            dict(num=7, titulo='La melodía de después, con una nota atada',
                 pista='andamio · desde el c. 5 la derecha canta y algunas notas se unen con una '
                       'curva al compás siguiente',
                 sistemas=[
                     dict(cap='a) la ligadura une dos corcheas iguales: se toca una vez y suena '
                              'las dos · no se vuelve a pulsar',
                          events=[n('G4', 'e'), n('A4', 'e'), n('G4', 'e'), n('E4', 'e'),
                                  n('G4', 'e'), n('A4', 'e'), n('G4', 'e'),
                                  dict(n('E4', 'e'), lig=True),
                                  n('E4', 'e'), n('D4', 'e'), n('D4', 'h'), sil('q')],
                          bars=2),
                 ]),
            dict(num=8, titulo='La izquierda con dos notas a la vez',
                 pista='andamio · desde el c. 5 la izquierda toca dos notas en redonda',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) cuatro dobles en redonda · las dos notas bajan a la vez, '
                              'nunca una detrás de otra',
                          events=[ac(('C3', 'G3'), 'w'), ac(('G2', 'D3'), 'w'),
                                  ac(('A2', 'E3'), 'w'), ac(('F2', 'C3'), 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) los mismos dobles con negra y blanca · la negra marca el golpe y '
                              'la blanca se queda',
                          events=[n('C3'), n('G3'), ac(('C3', 'G3'), 'h'),
                                  n('G2'), n('D3'), ac(('G2', 'D3'), 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 18, 'E4', 'C3',
                          'el arpegio parejo mientras la izquierda aguanta',
                          desde=9, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Someone You Loved · para casa',
            intro='Veinte minutos al día. Lo importante es que el arpegio salga igual al principio y '
                  'al final, y eso solo se consigue por pasos.',
            bloques=[
                plan((5, 'Las notas graves de la derecha solas, cc. 1-4'),
                     (5, 'Las notas agudas solas, cc. 1-4'),
                     (4, 'La izquierda: Do4, Sol3, La3 y Fa3, sin mirar'),
                     (6, 'Las dos manos, cc. 1-4, con metrónomo')),
                escalera((50, 'la derecha sola, cc. 1-4'),
                         (60, 'las dos manos, cc. 1-4'),
                         (72, 'los cc. 1-8 seguidos'),
                         (84, 'la meta que te pones tú: la partitura no la trae'),
                         meta='Tu partitura no trae número de metrónomo: la meta la pones tú y la '
                              'apuntas a lápiz.',
                         titulo='La escalera del metrónomo'),
                rodear([list(par('E5', 'G4', 2)),
                        list(par('B4', 'D4', 2)),
                        list(par('C5', 'E4', 2)),
                        list(par('E5', 'G4', 2))],
                       titulo='Rodea los dos medios compases que son iguales',
                       pista='son medios compases de los cc. 1, 2 y 3 de tu partitura'),
                escribir(titulo='Copia el c. 4 de la derecha',
                         pista='ocho corcheas · y escribe debajo cuál es la única pareja que '
                               'cambia respecto a las otras'),
                verdadero_falso([
                    'Detrás de la clave no hay nada.',
                    'La izquierda de los cc. 1-4 toca redondas.',
                    'La partitura tiene 40 compases.',
                    'Hacia el c. 37 hay un 8va sobre las dos manos.',
                    'La derecha de los cc. 1-4 toca negras.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                para_clase('Los cc. 1-4 con las dos manos y a qué número de metrónomo llegas sin '
                           'que las corcheas se desigualen. Traed también la pregunta del '
                           'compás en que se salta la repetición.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
