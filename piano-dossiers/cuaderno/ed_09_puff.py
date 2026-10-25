# -*- coding: utf-8 -*-
"""Puff, el dragón mágico — pieza 9 de Eduard. Formato ADULTO.

   La partitura la subió el cliente a la carpeta de Eduard el 30 de agosto de
   2026, cuando el resto del álbum ya estaba montado. En Drive se llama "Copia
   de Puff era un Drac Magic.pdf"; dentro pone *Puff the Magic Dragon*, de
   Eric Moore.

   Medido sobre ESE PDF (vectorial, una pagina, dos pentagramas por sistema):

     - 4/4 y detras de la clave no hay nada.
     - No trae numero de metronomo impreso, asi que la casilla de la ficha se
       llama "Caracter" y no "Tempo".
     - La DERECHA, medida a 300 ppp:

         c. 1   Do5 · Do5 · Do5 · Do5
                negra con puntillo, corchea, negra y negra
         c. 2   La4 · Fa4                  dos blancas
         c. 3   La4 · Do5 · Do5            blanca y dos negras

     - La IZQUIERDA lleva UNA REDONDA DE DOS NOTAS por compas, y nada mas:

         c. 1   Do3 y Mi3
         c. 2   Mi3 y Sol3
         c. 3   Fa3 y La3

   POR QUE SE MIRO AMPLIADA. En el pentagrama de fa, dos redondas a distancia
   de tercera pegadas una encima de otra dibujan **un ocho**, y el lector de
   alturas le encuentra cuatro bordes en vez de dos centros: en el c. 3 devolvia
   La3, Sol3, Fa3 y Mi3, que son los bordes de arriba y de abajo de los dos
   agujeros. Ampliado a ocho aumentos, con las lineas del pentagrama marcadas,
   se ve sin ninguna duda. Es el mismo susto que dio el *Grandfather's Clock*,
   donde el "8" del bajo parecia una cifra de compas de 6/8.

   POR QUE VA AQUI. Es el paso natural despues de *The Beginner*: alli las dos
   manos hacen lo mismo, y aqui cada una hace lo suyo pero la izquierda no
   podria ser mas facil —se colocan dos dedos, se aprieta una vez y se aguanta
   el compas entero—. Ademas trae la negra con puntillo, que es justo lo que
   *I Have a Dream* va a pedir dos piezas despues dentro de una frase.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ed_comun import (n, ac, plan, escalera, diferencias, teclado, escribir,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1 de la DERECHA, medido. Cita literal.
ARRANQUE = [n('C5', 'q.'), n('C5', 'e'), n('C5'), n('C5')]

# Los compases 1 y 2 de la IZQUIERDA, medidos: dos notas y a aguantar.
BAJO = [ac(('C3', 'E3'), 'w'), ac(('E3', 'G3'), 'w')]

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=9, nivel='iniciación',
    slug='PuffDragon', formato='adulto',
    titulo_corto='Puff, el dragón mágico', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source_new',
                           'Puff the Magic Dragon.pdf'),
    yt='https://www.youtube.com/results?search_query=puff+the+magic+dragon+piano+easy',

    ficha=dict(
        titulo='Puff, el dragón mágico',
        autor='Peter Yarrow y Leonard Lipton · arreglo de Eric Moore',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Manos', 'Las dos, distintas'), ('Carácter', 'Tranquilo'),
               ('Izquierda', 'Acordes largos')],
        titulo_ritmos='Así empieza',
        pie_ritmos='Medido en tu partitura. Arriba, el compás 1 de la derecha. Abajo, la izquierda '
                   'de los compases 1 y 2: dos notas a la vez, y duran el compás entero.',
        armonia=dict(
            titulo='La izquierda más fácil de todo el cuaderno',
            tarjetas=[
                ('UN ACORDE, UN COMPÁS', 'Y no se suelta',
                 'La izquierda toca dos teclas a la vez y las aguanta los cuatro tiempos. En toda '
                 'la primera línea solo cambia de sitio tres veces.'),
                ('DOS NOTAS JUNTAS', 'Do y Mi',
                 'Son dos teclas seguidas saltándose una: una tercera. Se cogen con el cinco y el '
                 'tres y la mano no se abre más.'),
                ('LA MISMA TECLA', 'Cuatro veces',
                 'El compás 1 de la derecha es cuatro veces el mismo Do. Lo único que cambia es '
                 'cuánto dura cada una.'),
                ('EL PUNTILLO', 'Una y media',
                 'La primera nota lleva puntillo: dura un tiempo y medio, y la corchea que va '
                 'detrás ocupa el medio que sobra.'),
            ],
            pie='Fíjate en el reparto: la izquierda no tiene ritmo ninguno y la derecha lo tiene '
                'todo. Es la manera más cómoda que hay de empezar a tocar dos cosas distintas a la '
                'vez, porque una de las dos no te pide nada.',
        ),
        ritmos=[
            ('LA DERECHA', 'el compás 1, medido · cuatro veces la misma tecla',
             ARRANQUE, OCRE, 'treble', None),
            ('LA IZQUIERDA', 'cc. 1 y 2, medidos · una redonda por compás',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Compás de 4/4, y no hay ni un sostenido ni un bemol.',
            'La izquierda toca dos notas a la vez, y duran el compás entero.',
            'El compás 1 de la derecha es cuatro veces el mismo Do.',
            'La primera nota lleva puntillo: dura un tiempo y medio.',
            'En el compás 2 la derecha hace dos blancas.',
            'Tu partitura no trae número de metrónomo.',
        ],
        reto='Que la izquierda no se levante. Cuando la derecha se pone a hacer ritmo, la mano que '
             'aguanta tiende a soltar la tecla sin darse cuenta, y el acorde deja de sonar.',
        truco='Toca el acorde de la izquierda y, sin soltarlo, cuenta los cuatro tiempos en voz '
              'alta mirándote la mano. Si al llegar al cuatro los dos dedos siguen abajo, ya está. '
              'Después haz lo mismo añadiendo la derecha.',
        sabias='La letra la escribió un estudiante de diecinueve años en 1959, a partir de un poema '
               'que había dejado escrito en la máquina de un amigo. Ese amigo era Peter Yarrow, que '
               'la convirtió en canción y lo buscó años después para pagarle su parte.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el acompañamiento: son acordes largos que casi no se mueven. Eso es '
                      'exactamente lo que va a hacer tu mano izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda de esta pieza se aprende en cinco minutos y no vuelve a dar guerra. '
              'Todo el trabajo está arriba, en el puntillo del primer compás.',
        reglas=['EL ACORDE NO SE SUELTA', 'CUATRO TIEMPOS POR ACORDE',
                'EL PUNTILLO DURA UNA Y MEDIA'],
        bloques=[
            dict(num=1, titulo='La izquierda: dos teclas y aguantar', clef='bass',
                 pista='cc. 1–3 · medidos en tu partitura · un acorde por compás',
                 sistemas=[
                     dict(cap='a) los tres acordes de la primera línea y la vuelta al primero · '
                              'los tres primeros están medidos, el cuarto cierra la ronda',
                          events=[ac(('C3', 'E3'), 'w'), ac(('E3', 'G3'), 'w'),
                                  ac(('F3', 'A3'), 'w'), ac(('C3', 'E3'), 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y volviendo al primero · el salto entre ellos es de una tecla',
                          events=[ac(('F3', 'A3'), 'w'), ac(('E3', 'G3'), 'w'),
                                  ac(('C3', 'E3'), 'w')],
                          bars=3, clef='bass', show_time=False),
                     dict(cap='c) y ahora contando los cuatro tiempos sin soltar · dos por acorde',
                          events=[ac(('C3', 'E3'), 'h'), ac(('C3', 'E3'), 'h'),
                                  ac(('E3', 'G3'), 'h'), ac(('E3', 'G3'), 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ CUESTA AGUANTAR UN ACORDE',
                 texto='Porque la mano que no hace nada se olvida de que está haciendo algo. En '
                       'cuanto la derecha pide atención, los dedos de la izquierda se relajan y la '
                       'tecla sube sin ruido: el acorde deja de sonar y nadie se entera hasta que '
                       'escucha la grabación. El truco es sencillo: mientras cuentas, siente el peso '
                       'del brazo en las dos teclas. Un acorde sostenido no se aprieta, se apoya.'),
            dict(num=2, titulo='La negra con puntillo del compás 1',
                 pista='c. 1 · medido en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) primero las cuatro notas en negras, para tener los golpes',
                          events=[n('C5'), n('C5'), n('C5'), n('C5')],
                          bars=1),
                     dict(cap='b) y con el puntillo, que es como está escrito · cuenta las mitades',
                          events=[n('C5', 'q.'), n('C5', 'e'), n('C5'), n('C5'),
                                  n('C5', 'q.'), n('C5', 'e'), n('C5'), n('C5')],
                          bars=2, show_time=False),
                     dict(cap='c) y con el compás 2 detrás, que son dos blancas y descansa',
                          events=[n('C5', 'q.'), n('C5', 'e'), n('C5'), n('C5'),
                                  n('A4', 'h'), n('F4', 'h')],
                          bars=2, show_time=False),
                     dict(cap='d) el compás 3, dos veces · empieza largo y acaba en dos negras',
                          events=[n('A4', 'h'), n('C5'), n('C5'),
                                  n('A4', 'h'), n('C5'), n('C5')],
                          bars=2, show_time=False),
                     dict(cap='e) y los compases 2 y 3 seguidos, que es donde la derecha respira',
                          events=[n('A4', 'h'), n('F4', 'h'),
                                  n('A4', 'h'), n('C5'), n('C5')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, los tres primeros compases',
                 pista='cc. 1–3 · medidos · arriba el ritmo, abajo el acorde quieto',
                 sistemas=[
                     dict(cap='a) los compases 1 y 2 · abajo el acorde va partido en mitades para '
                              'colocar la mano; en tu partitura es una redonda',
                          events=[ac(('C3', 'E3', 'C5'), 'q.'), ac(('C5',), 'e'),
                                  ac(('C3', 'E3', 'C5')), ac(('C5',)),
                                  ac(('E3', 'G3', 'A4'), 'h'), ac(('E3', 'G3', 'F4'), 'h')],
                          bars=2, manos='sostiene'),
                     dict(cap='b) y los compases 2 y 3, donde la derecha se para y el acorde cambia',
                          events=[ac(('E3', 'G3', 'A4'), 'h'), ac(('F4',), 'h'),
                                  ac(('F3', 'A3', 'A4'), 'h'), ac(('C5',)), ac(('C5',))],
                          bars=2, manos='sostiene', show_time=False),
                     dict(cap='c) y los tres seguidos, que es la primera línea entera de tu partitura',
                          events=[ac(('C3', 'E3', 'C5'), 'q.'), ac(('C5',), 'e'),
                                  ac(('C5',)), ac(('C5',)),
                                  ac(('E3', 'G3', 'A4'), 'h'), ac(('F4',), 'h'),
                                  ac(('F3', 'A3', 'A4'), 'h'), ac(('C5',)), ac(('C5',))],
                          bars=3, manos='sostiene', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Puff · para casa',
            intro='Quince minutos al día. La izquierda la tienes el primer día: dedica el resto de '
                  'la semana a que el puntillo del compás 1 suene siempre igual.',
            bloques=[
                plan((3, 'Los tres acordes de la izquierda, aguantando cuatro tiempos'),
                     (4, 'El compás 1 de la derecha, contando las mitades'),
                     (4, 'Los compases 2 y 3, que son notas largas'),
                     (4, 'Los tres primeros compases con las dos manos')),
                escalera((60, 'la derecha sola, el compás 1 con su puntillo'),
                         (76, 'los tres primeros compases con las dos manos'),
                         (92, 'la primera línea entera, sin parar'),
                         meta='la primera línea con las dos manos · tu partitura no trae número de '
                              'metrónomo, así que estos son de trabajo',
                         notas=['Apunta cada día hasta qué escalón has llegado.']),
                diferencias([n('C5', 'q.'), n('C5', 'e'), n('C5'), n('C5')],
                            [n('C5', 'q.'), n('C5', 'e'), n('C5'), n('A4')],
                            cuantas=1,
                            titulo='Busca la diferencia',
                            pista='arriba, tu compás 1 medido · abajo, con un cambio'),
                teclado([('Do', 'la de abajo del primer acorde'),
                         ('Mi', 'la de arriba del primer acorde')],
                        ['¿Cuántas teclas hay entre las dos, contando las negras?',
                         '¿Con qué dos dedos las coges?'],
                        titulo='Marca en el teclado el acorde de la izquierda',
                        pista='es una tercera: se salta una tecla blanca por en medio'),
                escribir(titulo='Copia aquí el compás 1, con su puntillo',
                         pista='y luego tócalo cinco veces contando "un-y-dos-y-tres-y-cua-tro"'),
                para_clase('Los tres primeros compases con las dos manos. Y dime si al final del '
                           'compás la izquierda sigue sonando: eso es lo que vamos a mirar.'),
            ],
        ),
    ],
)

CANCION['piano1']['bloques'] = list(CANCION['piano1']['bloques']) + bloques_extra(
    'Do mayor', 72, 'C5', 'C3',
    'la izquierda quieta mientras la derecha lleva el ritmo',
    desde=4, time_sig=(4, 4), mas=True)

if __name__ == '__main__':
    print('generado', construir(CANCION))
