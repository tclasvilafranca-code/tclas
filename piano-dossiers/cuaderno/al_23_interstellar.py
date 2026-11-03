# -*- coding: utf-8 -*-
"""Interstellar (Hans Zimmer) — pieza 23 de Alan, la última del curso. ADULTO
   exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (Campamento Bye Bye Beethoven,
   6 páginas, VECTORIAL), medido a 300 ppp contra las líneas del pentagrama. La
   sexta página es un sistema vacío con la barra final: para el álbum se genera una
   copia de las cinco primeras (`_cinco_paginas`).

     - Detrás de la clave no hay nada. 3/4. Trae ♩ = 96, "p" al principio, "mp" en el
       c. 5 y "p" otra vez en el c. 12. La digitación va impresa.
     - 100 compases. Arcos de frase sobre casi todo el arpegio. Un 8va hacia el c. 36,
       la derecha pasa a clave de fa en las páginas 4 y 5, y la pieza acaba con un
       calderón sobre un acorde.
     - Ninguna figura más corta que la corchea: corcheas seguidas, negras, blancas y
       blancas con puntillo.
     - MEDIDO, mano derecha:
       cc. 1-5: Mi4 · Do4 · Mi4 · Do4 · Mi4 · Do4 (seis corcheas por compás)
       cc. 6-7: Mi4 · Re4 · Mi4 · Re4 · Mi4 · Re4
       cc. 12-15: La4, La4, Si4, Si4 (negras) cada una con una blanca de Mi5 detrás
     - MEDIDO, mano izquierda: cc. 1-4, silencio de compás entero; c. 5, La2 (blanca
       con puntillo); cc. 6-7, Si2 (blanca con puntillo, ligada al compás siguiente);
       c. 8: La2 · Si2 · Do3; c. 9: Si2 · La2 · Si2 (negras); c. 10, Do3 y c. 11, Si2
       (blancas con puntillo).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, plan, metronomo, nombres, colorear, diferencias,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

ORIGEN = os.path.join(HERE, '..', 'students', 'alan', 'source', 'Interstellar _')
CINCO = os.path.join(HERE, '..', 'students', 'alan', 'source', 'INTERSTELLAR_5p.pdf')


def _cinco_paginas(src, dst):
    """La partitura de Drive trae una sexta página con un sistema vacío: copia sin ella."""
    from pypdf import PdfReader, PdfWriter
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return dst
    r = PdfReader(src)
    w = PdfWriter()
    for p in r.pages[:5]:
        w.add_page(p)
    with open(dst, 'wb') as f:
        w.write(f)
    return dst


if os.path.exists(ORIGEN):
    _cinco_paginas(ORIGEN, CINCO)


def arpegio(a, b, veces=3):
    return [n(a, 'e'), n(b, 'e')] * veces


# MEDIDO: derecha
C1 = arpegio('E4', 'C4')
C6 = arpegio('E4', 'D4')
M12 = [n('A4'), n('E5', 'h')]
M14 = [n('B4'), n('E5', 'h')]
# MEDIDO: izquierda
L5 = [n('A2', 'h.'), dict(n('B2', 'h.'), lig=True), n('B2', 'h.')]
L8 = [n('A2'), n('B2'), n('C3'), n('B2'), n('A2'), n('B2'), n('C3', 'h.'), n('B2', 'h.')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=23, nivel='intermedio', slug='Interstellar',
    formato='adulto',
    titulo_corto='Interstellar', time_sig=(3, 4), key_sig=None,
    partitura=CINCO,
    yt='https://www.youtube.com/results?search_query=interstellar+hans+zimmer+piano+easy',

    ficha=dict(
        titulo='Interstellar',
        autor='Hans Zimmer · versión del Campamento Bye Bye Beethoven',
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '3/4'),
               ('Tempo', '♩ = 96'), ('Dedos', 'Impresos'),
               ('Páginas', 'Cinco')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: seis corcheas por compás que alternan Mi y '
                   'Do. Abajo, medido: la izquierda no toca hasta el c. 5 y entra con una blanca '
                   'con puntillo.',
        armonia=dict(
            titulo='Un arpegio que no se detiene durante cien compases',
            tarjetas=[
                ('EL ARPEGIO', 'Mi, Do, Mi, Do',
                 'La derecha toca seis corcheas por compás, alternando Mi4 y Do4, sin parar. En '
                 'los cc. 6 y 7 el Do sube un tono y pasa a ser Re4: es el único cambio.'),
                ('LA IZQUIERDA', 'Calla y entra',
                 'Los cuatro primeros compases son silencio. En el c. 5 entra la La2 en blanca con '
                 'puntillo, después viene un tramo de negras y, al final, notas largas ligadas.'),
                ('LA MELODÍA', 'Desde el c. 12',
                 'A partir del c. 12 la derecha deja el arpegio y canta: La, Si y una blanca de Mi '
                 'arriba. Es el momento de la pieza donde hay que dejar de correr.'),
                ('LA LONGITUD', 'Cien compases',
                 'Es la pieza más larga del cuaderno. Funciona por repetición: lo que parece mucho '
                 'son cuatro o cinco ideas que vuelven. Hay un 8va hacia el c. 36 y la derecha '
                 'pasa a clave de fa en las dos últimas páginas.'),
            ],
            pie='La digitación va impresa desde el primer compás. Antes de tocar nada, haz el mapa: '
                'marca con lápiz cada vez que vuelve el arpegio, y verás que la pieza es mucho '
                'más corta de lo que parece.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-2 · medido', C1 + C1, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'cc. 1-5 · medido', [sil('h.')] * 4 + [n('A2', 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 3/4 y arriba viene impreso el metrónomo: negra = 96.',
            'Empieza en p, sube a mp en el c. 5 y vuelve a p en el c. 12.',
            'Los cuatro primeros compases la izquierda no toca.',
            'Hacia el c. 36 hay un 8va, y al final un calderón sobre un acorde.',
            'La edición trae digitación impresa.',
        ],
        reto='Mantener seis corcheas iguales durante cuatro compases seguidos, entrando en p y '
             'sin acelerar, y llegar al c. 5 con la izquierda sin que el arpegio se descuadre.',
        truco='Cuenta "uno-y-dos-y-tres-y" con la boca. Si al entrar la izquierda en el c. 5 se te '
              'va el pulso, vuelve atrás y toca el c. 4 con un golpe del pie en cada negra.',
        sabias='Hans Zimmer compuso la música de Interstellar (2014, Christopher Nolan) y la '
               'grabó con un órgano de tubos de una iglesia de Londres. Ese sonido continuo y '
               'creciente es lo que tu arpegio imita en el piano.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el arpegio no se detiene nunca y cómo la música crece por '
                      'acumulación: más notas, más fuerte, más graves. Eso es lo que haces tú.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Son cien compases, pero se estudian por ideas: primero el arpegio, luego la entrada de '
              'la izquierda, y después la melodía. El trabajo de estas semanas es el principio y '
              'el mapa del resto.',
        reglas=['SEIS CORCHEAS IGUALES', 'LA IZQUIERDA ENTRA EN EL C. 5',
                'LA PIEZA ES UN MAPA, NO UNA PARED'],
        bloques=[
            dict(num=1, titulo='El arpegio de los cc. 1-5',
                 pista='cc. 1-5 · medidos sobre tu partitura · seis corcheas por compás: Mi, Do, Mi, '
                       'Do, Mi, Do',
                 sistemas=[
                     dict(cap='a) un compás de seis corcheas, en p · cuenta "uno-y-dos-y-tres-y" y '
                              'que ninguna pese más que otra',
                          events=[dict(C1[0], matiz='p')] + C1[1:], bars=1, time_sig=(3, 4)),
                     dict(cap='b) el mismo dibujo una tercera más arriba · andamio · cambia el '
                              'sitio, no la forma de la mano',
                          events=arpegio('G4', 'E4'), bars=1, time_sig=(3, 4),
                          show_time=False),
                 ]),
            dict(num=2, titulo='Los cc. 6 y 7: el Do sube a Re',
                 pista='cc. 6-7 · medidos sobre tu partitura · el único cambio del arpegio',
                 sistemas=[
                     dict(cap='a) Mi y Re en vez de Mi y Do · la mano se encoge un poco y las '
                              'seis corcheas siguen iguales',
                          events=C6 + C6, bars=2, time_sig=(3, 4)),
                     dict(cap='b) el mismo cambio una tercera más arriba · andamio · la nota de abajo '
                              'sube un tono, la de arriba se queda',
                          events=arpegio('G4', 'F4', 6), bars=2, time_sig=(3, 4),
                          show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE HACE EL MAPA ANTES DE TOCAR',
                 texto='Una pieza de cien compases asusta, pero casi todo se repite. Antes de '
                       'tocar, coge un lápiz y marca cada compás que empieza con el arpegio y '
                       'cada compás que lo cambia. Verás cuatro o cinco ideas, no cien. Estudiarlas '
                       'una a una es la mitad del trabajo.'),
            dict(num=3, titulo='La izquierda entra en el c. 5',
                 pista='cc. 5-7 · medidos sobre tu partitura · una blanca con puntillo, y otra '
                       'ligada al compás siguiente',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) La2 en blanca con puntillo, y Si2 ligada a otra Si2 · la '
                              'ligadura une dos compases: se toca una sola vez',
                          events=L5, bars=3, time_sig=(3, 4), clef='bass'),
                 ]),
            dict(num=4, titulo='Las negras de los cc. 8-11',
                 pista='cc. 8-11 · medidos sobre tu partitura · la izquierda empieza a moverse',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) La, Si, Do; Si, La, Si; y dos blancas con puntillo · el bajo '
                              'sube y baja mientras la derecha no se mueve',
                          events=L8, bars=4, time_sig=(3, 4), clef='bass'),
                 ]),
            dict(num=5, titulo='Las dos manos, cc. 5 y 6',
                 pista='cc. 5-6 · medidos sobre tu partitura · la izquierda sostiene mientras la '
                       'derecha arpegia',
                 sistemas=[
                     dict(cap='a) el La2 del c. 5 y el Si2 del c. 6 con el arpegio de Mi y Do, y '
                              'de Mi y Re · la izquierda cae una vez por compás y se queda',
                          events=[ac(('A2', 'E4'), 'e'), n('C4', 'e'), n('E4', 'e'), n('C4', 'e'),
                                  n('E4', 'e'), n('C4', 'e'),
                                  ac(('B2', 'E4'), 'e'), n('D4', 'e'), n('E4', 'e'), n('D4', 'e'),
                                  n('E4', 'e'), n('D4', 'e')],
                          bars=2, time_sig=(3, 4), manos='sostiene'),
                 ]),
            dict(num=6, titulo='La melodía entra, cc. 12-15',
                 pista='cc. 12-15 · medidos sobre tu partitura · una negra y una blanca de Mi, '
                       'cuatro veces',
                 sistemas=[
                     dict(cap='a) La y Mi, La y Mi, Si y Mi, Si y Mi · de nuevo en p · la '
                              'blanca se escucha hasta el final antes de pasar a la siguiente',
                          events=[dict(M12[0], matiz='p'), M12[1], M12[0], M12[1],
                                  M14[0], M14[1], M14[0], M14[1]],
                          bars=4, time_sig=(3, 4)),
                 ]),
            dict(num=7, titulo='La derecha en clave de fa, páginas 4 y 5',
                 pista='andamio · en las dos últimas páginas la derecha se escribe en clave de fa '
                       'durante varios compases',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) el mismo arpegio de seis corcheas en clave de fa · las notas '
                              'siguen siendo Do, Mi y Sol, pero se leen en otro sitio del pentagrama',
                          events=arpegio('C3', 'G3'), bars=1, time_sig=(3, 4), clef='bass'),
                     dict(cap='b) y con la nota de abajo cambiada, como en los cc. 6 y 7 · andamio '
                              'para fijar el cambio también en clave de fa',
                          events=arpegio('E3', 'D3'), bars=1, time_sig=(3, 4), clef='bass',
                          show_time=False),
                 ]),
            dict(num=8, titulo='El 8va y el calderón del final',
                 pista='andamio · lo que hacen los dos signos de tu partitura: el 8va sube una '
                       'octava y el calderón alarga',
                 sistemas=[
                     dict(cap='a) el arpegio con 8va · suena una octava más alto de lo escrito',
                          events=arpegio('E5', 'C5'), bars=1, time_sig=(3, 4), ottava=True),
                     dict(cap='b) un acorde con calderón · se aguanta más de lo que dura y el '
                              'final lo decides tú',
                          events=[dict(ac(('C4', 'E4', 'G4'), 'h.'), art='calderon')],
                          bars=1, time_sig=(3, 4), show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 23, 'E4', 'A2',
                          'seis corcheas iguales durante muchos compases seguidos',
                          desde=9, time_sig=(3, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Interstellar · para casa',
            intro='Veinte minutos al día. Es la pieza más larga del curso, pero la semana es corta: '
                  'el objetivo son los cc. 1-11 con las dos manos y el mapa de las cinco '
                  'páginas.',
            bloques=[
                plan((5, 'El mapa con lápiz: marca los compases donde cambia el arpegio'),
                     (5, 'El arpegio de los cc. 1-7, con la derecha sola'),
                     (4, 'La izquierda sola, cc. 5-11'),
                     (6, 'Las dos manos, cc. 1-11')),
                metronomo('Empieza a ♩ = 60 con el arpegio solo y sube de cuatro en cuatro hasta '
                          '96, que es el número de tu partitura.',
                          'Si a una velocidad las corcheas se desigualan, no subas: baja cuatro '
                          'y repítelo. El 96 se gana en varios días.',
                          titulo='A qué velocidad te sale'),
                nombres(['E4', 'C4', 'D4', 'A4', 'B4', 'E5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='son las notas de la derecha de los cc. 1-15 de tu partitura'),
                colorear([n('E4', 'e'), n('C4', 'e'), n('E4', 'e'), n('C4', 'e'), n('E4', 'e'),
                          n('C4', 'e'), n('A4'), n('E5', 'h')],
                         ['Las corcheas, de azul.',
                          'La negra, de rojo.',
                          'La blanca, de verde.'],
                         titulo='Colorea según la figura',
                         pista='el arpegio del c. 5 y el principio de la melodía del c. 12'),
                diferencias(list(C1),
                            [n('E4', 'e'), n('C4', 'e'), n('E4', 'e'), n('D4', 'e'), n('E4', 'e'),
                             n('D4', 'e')],
                            cuantas=2,
                            titulo='Busca las diferencias',
                            pista='arriba, el c. 1 de tu partitura · abajo, el mismo compás con '
                                  'dos notas cambiadas'),
                para_clase('Los cc. 1-11 con las dos manos, a la velocidad que te salga sin '
                           'desigualarse, y el mapa de la pieza hecho con lápiz. Es la última '
                           'pieza del curso: dime qué ha sido lo más difícil de todo el año.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
