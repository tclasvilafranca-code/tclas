# -*- coding: utf-8 -*-
"""La primavera (Vivaldi, de Las cuatro estaciones) — pieza 22 de Jaume. ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (edición de 8notes.com,
   1 página, imagen a 88 ppp), mirado a 110 y 220 ppp:

     - Detrás de la clave NO hay nada: DO MAYOR. 4/4. Arriba pone "Allegro" y "f";
       no trae metrónomo. Trae digitación impresa, ligaduras largas de frase y
       matices (f, p, un regulador que abre y f al final).
     - Empieza con una ANACRUSA: Do4 de negra en la derecha y un silencio de
       negra en la izquierda.
     - MEDIDO, mano derecha (a 220 ppp):
       anacrusa: Do4 (negra)
       c. 1: intervalo Do4+Mi4 (negra) ×3 · Re4 (corchea) · Do4 (corchea)
       c. 2: intervalo Mi4+Sol4 (blanca con puntillo) · Sol4 (corchea) · Fa4 (corchea)
       cc. 3-4: repiten los cc. 1-2.
       La primera ligadura de frase sale de la anacrusa y acaba en el intervalo
       del c. 2.
     - MEDIDO, mano izquierda, c. 1: Do3 (blanca) · Do3 (blanca).
   Es el mismo arreglo que el de Mercè (su "Spring"); la de Luisa es otra edición.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, ordenar, unir, inventa, acuerdate,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def dy(a, b, d='q'):
    return ac((a, b), d)


# MEDIDO: anacrusa, c. 1 y c. 2 (derecha)
ANA = [sil('h.'), n('C4')]
C1 = [dy('C4', 'E4'), dy('C4', 'E4'), dy('C4', 'E4'), n('D4', 'e'), n('C4', 'e')]
C2 = [dy('E4', 'G4', 'h.'), n('G4', 'e'), n('F4', 'e')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=22, nivel='intermedio', slug='Primavera',
    formato='adulto',
    titulo_corto='La primavera · Vivaldi', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source', 'La Primavera. Vivaldi'),
    yt='https://www.youtube.com/results?search_query=vivaldi+spring+piano+easy',

    ficha=dict(
        titulo='La primavera',
        autor="Antonio Vivaldi · de Las cuatro estaciones · edición de 8notes.com",
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Allegro · f'), ('Derecha', 'Intervalos dobles'),
               ('Empieza', 'Con anacrusa')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: tres intervalos de negra y dos corcheas, y '
                   'un intervalo de blanca con puntillo. Abajo, la izquierda de los cc. 1 y 2: dos '
                   'blancas por compás sobre Do.',
        armonia=dict(
            titulo='Una frase que se repite, con dos notas a la vez',
            tarjetas=[
                ('LA ANACRUSA', 'Una negra',
                 'La pieza empieza antes del primer compás, con un Do de negra en la derecha y un '
                 'silencio de negra en la izquierda. El c. 1 cae justo después del tiempo de '
                 'espera.'),
                ('LOS INTERVALOS', 'Dos notas a la vez',
                 'La derecha no toca una sola voz: repite un intervalo de dos notas en negras y '
                 'cierra con otro, más largo, de blanca con puntillo. La mano casi no se mueve.'),
                ('LA FRASE', 'Dos veces',
                 'Los cc. 3 y 4 repiten los cc. 1 y 2 tal cual. Es una pieza hecha de bloques que '
                 'vuelven: se estudia el bloque, no el compás.'),
                ('LAS LIGADURAS', 'Largas, de frase',
                 'Las curvas largas de la partitura abarcan una frase entera, no dos notas. '
                 'Dicen "esto va de un tirón", y se tocan en un solo gesto.'),
            ],
            pie='La pieza cabe en una página. Lo que importa de verdad es el equilibrio entre las '
                'dos manos: la izquierda aguanta dos blancas y la derecha dibuja la frase.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1 y 2 · medido', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'cc. 1 y 2 · medido',
             [n('C3', 'h')] * 4, AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: Do mayor.',
            'El compás es 4/4. Arriba pone Allegro y f, pero no trae número de metrónomo.',
            'Empieza con una anacrusa de una negra, con un silencio en la izquierda.',
            'La derecha repite intervalos de dos notas; la izquierda toca dos blancas por compás.',
            'Los cc. 3 y 4 repiten los cc. 1 y 2.',
            'Lleva ligaduras largas de frase, matices (f y p) y la digitación impresa.',
        ],
        reto='Mantener la mano de la derecha quieta mientras repite el intervalo, y que la corchea '
             'final de cada compás no se adelante. Si la mano viaja, el sonido se ensucia.',
        truco='Toca el intervalo sin moverlo del teclado y deja que solo bajen los dedos, con la '
              'digitación impresa. Cuenta uno-dos-tres-y-cuatro-y: las corcheas van en los "y".',
        sabias='Las cuatro estaciones son cuatro conciertos para violín que Vivaldi publicó en 1725. '
               'Cada uno lleva un soneto que describe la estación, y los pájaros de la primavera '
               'se oyen en los trinos del violín.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo la primera frase vuelve igual la segunda vez: es lo que hace '
                      'tu partitura en los cc. 3 y 4, que repiten los cc. 1 y 2.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La pieza se estudia en bloques de cuatro compases: la primera frase, bien, vale para la '
              'segunda. Y se estudia con la mano quieta, sin que el intervalo viaje.',
        reglas=['EL INTERVALO NO VIAJA', 'LA ANACRUSA SE CUENTA', 'LA LIGADURA LARGA, DE UN GESTO'],
        bloques=[
            dict(num=1, titulo='La anacrusa y el c. 1',
                 pista='anacrusa y c. 1 · medido sobre tu partitura · una negra de espera, tres '
                       'intervalos de negra y dos corcheas',
                 sistemas=[
                     dict(cap='a) la anacrusa con tres tiempos de silencio delante para poder '
                              'contarla, y el c. 1 detrás',
                          events=ANA + C1, bars=2, matiz='f'),
                 ]),
            dict(num=2, titulo='El c. 2 y la primera ligadura de frase',
                 pista='c. 2 · medido sobre tu partitura · la curva larga arranca en la anacrusa y '
                       'acaba en el intervalo de blanca con puntillo',
                 sistemas=[
                     dict(cap='a) la anacrusa, el c. 1 y el intervalo del c. 2, con la ligadura que '
                              'los une · se toca de un tirón, sin respirar entre los compases',
                          events=[sil('h.'), dict(pitch='C4', dur='q', lig=6)] + C1 +
                                 [dy('E4', 'G4', 'h.')] + [sil('q')],
                          bars=3),
                 ]),
            dict(tipo='nota',
                 etiqueta='UNA LIGADURA LARGA NO ES UNA LIGADURA DE UNIÓN',
                 texto='La ligadura que une dos notas iguales suma sus duraciones y se toca una sola '
                       'vez. La curva larga de tu partitura abarca varias notas distintas y dice '
                       'otra cosa: que la frase va unida, sin cortes. Se toca cada nota, pero el '
                       'dedo no se levanta de golpe entre una y otra.'),
            dict(num=3, titulo='La izquierda: dos blancas sobre Do',
                 pista='c. 1 · medido sobre tu partitura · la izquierda es lo más sencillo de la '
                       'pieza, y también lo más fácil de descuidar',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) cuatro compases de dos blancas sobre el mismo Do, que es lo que '
                              'hace la izquierda de los cc. 1-4 · se aguantan los dos tiempos enteros',
                          events=[n('C3', 'h')] * 8, bars=4, clef='bass'),
                 ]),
            dict(num=4, titulo='Las dos manos, el c. 1',
                 pista='c. 1 · medido sobre tu partitura · la izquierda cae en el primer y en el '
                       'tercer tiempo',
                 sistemas=[
                     dict(cap='a) la izquierda cae con el primer intervalo y con el tercero, y '
                              'aguanta cada una dos tiempos',
                          events=[ac(('C3', 'C4', 'E4'), 'q'), dy('C4', 'E4'),
                                  ac(('C3', 'C4', 'E4'), 'q'), n('D4', 'e'), n('C4', 'e')],
                          bars=1, manos='sostiene'),
                 ]),
            dict(num=5, titulo='Piano y forte, y un regulador',
                 pista='andamio sobre Do mayor · tu partitura pone f al principio, p y f '
                       'después, y un regulador que abre antes del final',
                 sistemas=[
                     dict(cap='a) un intervalo repetido en forte · el sonido es firme, sin golpear',
                          events=[dy('C4', 'E4'), dy('C4', 'E4'), dy('C4', 'E4'), dy('D4', 'F4')],
                          bars=1, matiz='f'),
                     dict(cap='b) el mismo en piano, con un regulador que abre · se toca con menos '
                              'peso al principio y crece sin cambiar la velocidad',
                          events=[dy('C4', 'E4'), dy('C4', 'E4'), dy('C4', 'E4'), dy('D4', 'F4')],
                          bars=1, matiz='p', cresc=3, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 22, 'E4', 'C3',
                          'el intervalo repetido con la mano quieta y la frase que vuelve',
                          desde=6, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='La primavera · para casa',
            intro='Veinte minutos al día. Se estudia por frases de cuatro compases, y la segunda vez '
                  'es más fácil que la primera.',
            bloques=[
                reto('Tocar los cuatro primeros compases de un tirón, con la mano quieta y las '
                     'corcheas del final sin adelantarse.',
                     'Cuenta uno-dos-tres-y-cuatro-y en voz alta. Si la mano se mueve de sitio, '
                     'vuelve a empezar y pega el codo al cuerpo.'),
                plan((5, 'La izquierda sola: dos blancas por compás, sin cortar la segunda'),
                     (6, 'La derecha sola, cc. 1-4, con la digitación impresa'),
                     (5, 'Las dos manos, cc. 1-4, despacio y con la curva larga'),
                     (4, 'Los cc. 1-8 de una vez, con el f y el p')),
                ordenar(['Tocar los cc. 1-4 con las dos manos.',
                         'Contar la anacrusa y el c. 1 sin tocar.',
                         'Tocar la derecha sola, cc. 1-4.',
                         'Tocar la izquierda sola, cc. 1-4.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='del más fácil al más completo · uno va antes de tocar nada'),
                unir([('Anacrusa', 'una negra de espera antes del primer compás'),
                      ('Intervalo', 'dos notas que suenan a la vez'),
                      ('Ligadura larga', 'la frase va de un tirón'),
                      ('f', 'fuerte, sin golpear')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                inventa(['Dos compases en 4/4.',
                         'Con un intervalo de dos notas repetido tres veces.',
                         'Que acabe en una blanca con puntillo.',
                         'Con una anacrusa de una negra.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases como los de la pieza',
                        pista='con el material de tu partitura de esta semana, pero tuyo'),
                acuerdate('La ligadura larga no es una ligadura de unión: no suma duraciones. Dice que '
                          'la frase va de un tirón, y cada nota se toca.',
                          etiqueta='DOS LIGADURAS DISTINTAS'),
                para_clase('Los cc. 1-8 con las dos manos, y si la mano se te mueve al repetir el '
                           'intervalo. Si las corcheas se adelantan, tráelas: se arreglan contando '
                           'en voz alta.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
