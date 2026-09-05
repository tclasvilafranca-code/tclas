# -*- coding: utf-8 -*-
"""Counting Stars — pieza 6 de Aida. Formato ADULTO exigente.

   Cierra la segunda etapa. La 4 tenia la izquierda moviendose y la derecha
   quieta, la 5 tenia la derecha callada tres compases, y esta las pone a las
   dos a trabajar a la vez: melodia continua arriba y acordes largos abajo, sin
   que ninguna de las dos descanse.

   Lo comprobado sobre el PDF de SU carpeta (Musescore, "Easy Version, arr.
   Becky Messer", 2 paginas; el mismo archivo, byte a byte, que el de Jose
   Maria, Josep, Nel y Mercè):

     - Do mayor: detras de la clave no hay nada.
     - 4/4, y NO trae numero de metronomo. Por eso la casilla de la ficha se
       llama "Caracter" y no "Tempo".
     - La digitacion viene impresa encima de la melodia (2, 3, 5, 1, 4...).
     - La izquierda hace acordes de dos notas en REDONDA: uno por compas.

   LAS ALTURAS del compas 1, medidas a 300 ppp y comprobadas ampliando con las
   lineas del pentagrama marcadas en rojo:

       c. 1   Re4 · Mi4 · Sol4 · Mi4      cuatro negras

   El compas 2 sigue con cuatro corcheas que bajan (Re4 · Mi4 · Re4 · Do4) y
   una blanca. La blanca es una cabeza hueca y no la lee el detector, asi que
   aqui se cita solo el compas 1, que esta medido entero.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, plan, escalera, inventa, dibujar,
                      nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1 de la DERECHA, medido. Cita literal.
ARRANQUE = [n('D4'), n('E4'), n('G4'), n('E4')]

# La izquierda: un acorde largo por compas. ANDAMIO en Do mayor.
BAJO = [ac(('C3', 'G3'), 'w'), ac(('A2', 'E3'), 'w'), ac(('F2', 'C3'), 'w')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=6, nivel='intermedio',
    slug='CountingStars', formato='adulto',
    titulo_corto='Counting Stars', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Counting Stars.pdf'),
    yt='https://www.youtube.com/results?search_query=counting+stars+onerepublic+piano+easy',

    ficha=dict(
        titulo='Counting Stars',
        autor='OneRepublic · Ryan Tedder · arreglo de Becky Messer',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin marcar'), ('Derecha', 'Sin parar'),
               ('Izquierda', 'Redondas')],
        titulo_ritmos='El compás 1, y lo que hace la izquierda',
        pie_ritmos='Arriba, el compás 1 de la derecha MEDIDO en tu partitura: cuatro negras. Abajo, '
                   'andamio en Do mayor con la figura que usa la izquierda, que es una redonda de '
                   'dos notas por compás.',
        armonia=dict(
            titulo='Las dos manos trabajando, y ninguna descansa',
            tarjetas=[
                ('LA DERECHA', 'No para',
                 'Negras y corcheas de principio a fin. No hay notas largas donde recolocar la '
                 'mano: la digitación impresa está ahí justo por eso.'),
                ('LA IZQUIERDA', 'Una por compás',
                 'Un acorde de dos notas en redonda. Suena poco y es lo que sostiene la canción: '
                 'sin él, la melodía se queda flotando.'),
                ('SIN METRÓNOMO', 'Lo eliges tú',
                 'Tu partitura no trae número. La velocidad la decides en clase, y los números de '
                 'la escalera de esta semana son de trabajo.'),
                ('LA DIGITACIÓN', 'Impresa',
                 'La trae tu edición encima de la melodía. Merece la pena seguirla: está puesta '
                 'para que la mano no tenga que saltar.'),
            ],
            pie='Es la primera pieza del cuaderno en la que las dos manos tienen algo que hacer '
                'todo el rato. Después de la 4 y la 5, donde una de las dos siempre descansaba, '
                'esta es el paso lógico.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el compás 1, MEDIDO · cuatro negras',
             ARRANQUE, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio en Do mayor · una redonda por compás',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'Compás de 4/4, y no viene ningún número de metrónomo.',
            'La digitación está impresa encima de la melodía.',
            'La izquierda hace una redonda de dos notas por compás.',
            'El compás 2 baja en cuatro corcheas y acaba en una blanca.',
            'Son dos páginas.',
        ],
        reto='Que la melodía no se acelere en las corcheas. Cuando la izquierda solo toca una vez '
             'por compás no hay quien sujete el pulso, y las notas cortas se comen el compás.',
        truco='Toca la melodía sola con el metrónomo y cuenta EN VOZ ALTA "un-y-dos-y-tres-y-cua-tro". '
              'Las corcheas caen en las "y". Si te las saltas al contar, también te las saltas al '
              'tocar.',
        sabias='Ryan Tedder ha contado que la escribió en veinte minutos, con la guitarra, y que el '
               'estribillo salió de una frase que llevaba meses apuntada en el móvil. Es la canción '
               'más escuchada de OneRepublic.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que el bajo casi no se mueve: una nota por compás. Toda la energía '
                      'está en la melodía y en la batería, no en la armonía.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí la izquierda se aprende en un día y la derecha necesita la semana entera. '
              'Reparte el tiempo en consecuencia y no al revés.',
        reglas=['LA MELODÍA, CON METRÓNOMO SIEMPRE', 'CUENTA LAS "Y" EN VOZ ALTA',
                'SIGUE LA DIGITACIÓN DE TU PARTITURA'],
        bloques=[
            dict(num=1, titulo='La melodía, empezando por su dibujo',
                 pista='cc. 1–2 · el compás 1 está MEDIDO; el 2 es andamio con la forma que baja',
                 sistemas=[
                     dict(cap='a) el compás 1 con las cuatro negras partidas en corcheas, para '
                              'colocar la mano · en tu partitura son negras',
                          events=corch(['D4', 'D4']) + corch(['E4', 'E4']) +
                                 corch(['G4', 'G4']) + corch(['E4', 'E4']),
                          matiz='mf',
                          bars=1),
                     dict(cap='b) y con el compás 2 detrás · cuatro corcheas que bajan y una blanca',
                          events=list(ARRANQUE) + corch(['D4', 'E4']) + corch(['D4', 'C4']) +
                                 [n('D4', 'h')],
                          bars=2, show_time=False),
                     dict(cap='c) y los dos compases repetidos, sin parar entre ellos',
                          events=list(ARRANQUE) + corch(['D4', 'E4']) + corch(['D4', 'C4']) +
                                 [n('D4', 'h')] + list(ARRANQUE) + corch(['D4', 'E4']) +
                                 corch(['D4', 'C4']) + [n('D4', 'h')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTAN LAS "Y"',
                 texto='Porque una corchea no dura "un poco menos": dura exactamente la mitad. Si '
                       'cuentas solo los números, las corcheas se colocan de oído y el oído siempre '
                       'las acorta. Contando "un-y-dos-y" tienes ocho referencias por compás en vez '
                       'de cuatro, y cada corchea tiene la suya. Cuando la mano ya lo sabe, se deja '
                       'de contar; antes, no.'),
            dict(num=2, titulo='La izquierda, que es media hora de trabajo',
                 pista='andamio en Do mayor · dos notas en redonda, una por compás',
                 sistemas=[
                     dict(cap='a) los dos primeros acordes con la nota de arriba moviéndose · en '
                              'tu partitura las dos notas del acorde no cambian dentro del compás',
                          events=[ac(('C3', 'G3'), 'h'), ac(('C3', 'E3'), 'h'),
                                  ac(('A2', 'E3'), 'h'), ac(('A2', 'C3'), 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) y la vuelta entera con la TERCERA arriba en vez de la quinta · '
                              'es la nota que decide si el acorde suena alegre o triste',
                          events=[ac(('C3', 'E3'), 'w'), ac(('A2', 'C3'), 'w'),
                                  ac(('F2', 'A2'), 'w'), ac(('G2', 'B2'), 'w')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y con esos mismos partidos en dos mitades, para oír las dos '
                              'notas · en tu partitura suenan a la vez',
                          events=[n('C3', 'h'), n('E3', 'h'), n('A2', 'h'), n('C3', 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos',
                 pista='el compás 1 de la derecha está MEDIDO · el acorde de abajo es andamio',
                 sistemas=[
                     dict(cap='a) el compás 2 con su acorde debajo, que no se suelta · cuatro '
                              'corcheas que bajan y una blanca',
                          events=[ac(('A2', 'E3', 'D4'), 'e'), ac(('E4',), 'e'),
                                  ac(('D4',), 'e'), ac(('C4',), 'e'), ac(('D4',), 'h')],
                          bars=1, manos='sostiene'),
                     dict(cap='b) y los dos primeros compases seguidos, con el cambio de acorde',
                          events=[ac(('C3', 'G3', 'D4')), ac(('E4',)), ac(('G4',)), ac(('E4',)),
                                  ac(('A2', 'E3', 'D4'), 'e'), ac(('E4',), 'e'),
                                  ac(('D4',), 'e'), ac(('C4',), 'e'), ac(('D4',), 'h')],
                          bars=2, manos='dobla', show_time=False),
                     dict(cap='c) y la vuelta de cuatro acordes con la melodía encima · es la '
                              'primera línea entera de tu partitura, en versión reducida',
                          events=[ac(('C3', 'G3', 'D4')), ac(('E4',)), ac(('G4',)), ac(('E4',)),
                                  ac(('A2', 'E3', 'G4')), ac(('E4',)), ac(('D4',)), ac(('E4',)),
                                  ac(('F2', 'C3', 'A4')), ac(('G4',)), ac(('E4',)), ac(('G4',)),
                                  ac(('G2', 'D3', 'D4'), 'h'), ac(('C4',), 'h')],
                          bars=4, manos='sostiene', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Cuatro compases con el metrónomo, y la digitación de tu edición puesta. Si '
                       'un dedo te obliga a saltar, no lo cambies a la primera: casi siempre el que '
                       'está mal es el anterior, no el que salta. Mira los dos compases de antes '
                       'antes de tocar nada.'),
        ] + bloques_extra('Do mayor', 91, 'E4', 'C3',
                          'la melodía que no para encima de un bajo que casi no se mueve',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Counting Stars · para casa',
            intro='Quince minutos al día. La izquierda te va a costar un día entero; el resto de la '
                  'semana es para que la melodía no corra.',
            bloques=[
                plan((3, 'Los cuatro acordes de la izquierda, en redondas'),
                     (5, 'La melodía sola, contando "un-y-dos-y" en voz alta'),
                     (4, 'Los cuatro primeros compases con las dos manos'),
                     (3, 'Los mismos cuatro, un escalón más rápido')),
                escalera((66, 'la melodía sola, con las corcheas colocadas'),
                         (84, 'los cuatro primeros compases con las dos manos'),
                         (100, 'la primera línea entera, sin parar'),
                         meta='que las corcheas suenen iguales a la velocidad más alta · tu '
                              'partitura NO trae número de metrónomo, así que estos tres son de '
                              'trabajo y los decidimos en clase',
                         notas=['Si al subir se te juntan las corcheas, baja y quédate ahí.']),
                inventa(['cuatro tiempos en total', 'que lleve dos corcheas por lo menos',
                         'que empiece y acabe en Do'],
                        (4, 4),
                        titulo='Inventa un compás para la melodía',
                        pista='con las notas de tu compás 1: Re, Mi y Sol'),
                dibujar(['Re', 'Mi', 'Sol', 'Do', 'La'],
                        titulo='Dibuja tú estas notas en clave de sol',
                        pista='solo el óvalo · las tres primeras son las de tu compás 1'),
                nombres(['D4', 'E4', 'G4', 'C4', 'A3', 'E4', 'D4'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='están desordenadas · las tres primeras salen en tu compás 1'),
                para_clase('Los cuatro primeros compases con las dos manos y a qué velocidad. Y '
                           'dime si seguiste la digitación impresa o te inventaste otra: las dos '
                           'cosas valen, pero hay que saber cuál estás usando.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
