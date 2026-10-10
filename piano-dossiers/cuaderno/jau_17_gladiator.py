# -*- coding: utf-8 -*-
"""Gladiator (Hans Zimmer) — pieza 17 de Jaume. ADULTO exigente, sin cifrado.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de A. C. Escobés,
   edición de El Cuarto del Piano, 1 página, 27 compases), a 100-300 ppp:

     - UN SOSTENIDO detrás de la clave: la pieza va en Mi menor. 4/4.
     - Arriba pone **Allegro** y **ff**. No trae número de metrónomo.
     - NUMERACIÓN IMPRESA: la anacrusa NO cuenta. Los cuatro primeros compases
       son c. 1 a c. 4, y el segundo sistema se rotula "5" y arranca con una
       redonda con calderón y una barra de repetición.
     - Empieza con una anacrusa de un tiempo: silencio de corchea con puntillo y
       una semicorchea (Mi4). Lleva doble puntillo, semicorchea, tresillos y
       calderón. Los dos pentagramas hacen lo mismo, una octava aparte.
     - MEDIDO (a 300 ppp), mano derecha:
       c. 1: Si4 (negra con DOBLE puntillo), Mi4 (semicorchea), Si4 (negra con
             DOBLE puntillo), Sol4 (semicorchea)
       c. 2: Si4 (blanca con puntillo) y un tresillo de corcheas Si4 · Sol4 · Do5
       c. 3: igual que el c. 1
       c. 4: Si4 (blanca con puntillo) y un tresillo Si4 · La♯4 · Re5
       c. 5: Si4 (redonda con calderón)
       mano izquierda: lo mismo una octava más grave.

   Es el mismo archivo que el de Aída, Isaac, Mercè y Eduard. La numeración que
   usa este módulo es la IMPRESA en la partitura (la anacrusa no cuenta).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, corch, plan, metronomo, ordenar, contar,
                       teclado, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def tres(pitches, gid):
    """Un tresillo de corcheas: tres notas en el hueco de dos."""
    return [dict(pitch=p, dur='e', tresillo=gid, beam=gid) for p in pitches]


ENTRADA = [sil('h.'), sil('e.'), n('E4', 's')]                      # anacrusa
C1 = [n('B4', 'q..'), n('E4', 's'), n('B4', 'q..'), n('G4', 's')]    # cc. 1 y 3
C2 = [n('B4', 'h.')] + tres(['B4', 'G4', 'C5'], 171)                 # c. 2
C4 = [n('B4', 'h.')] + tres(['B4', 'A#4', 'D5'], 172)                # c. 4
C1_I = [n('B3', 'q..'), n('E3', 's'), n('B3', 'q..'), n('G3', 's')]
C2_I = [n('B3', 'h.')] + tres(['B3', 'G3', 'C4'], 173)

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=17, nivel='intermedio', slug='Gladiator',
    formato='adulto',
    titulo_corto='Gladiator', time_sig=(4, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source', 'Gladiator II Hans Zinmer'),
    yt='https://www.youtube.com/results?search_query=gladiator+hans+zimmer+piano+tutorial',

    ficha=dict(
        titulo='Gladiator',
        autor='Hans Zimmer · arreglo de A. C. Escobés',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '4/4'),
               ('Carácter', 'Allegro · ff'), ('Armadura', 'Un sostenido'),
               ('Empieza', 'Con anacrusa')],
        titulo_ritmos='Los cc. 1 y 2, medidos',
        pie_ritmos='Medido sobre tu partitura: arriba la derecha y abajo la izquierda, una octava '
                   'más grave, que hace exactamente lo mismo. La anacrusa va antes del c. 1 y no '
                   'se dibuja aquí.',
        armonia=dict(
            titulo='Doble puntillo, tresillo y calderón: tres maneras de escribir el tiempo',
            tarjetas=[
                ('EL DOBLE PUNTILLO', 'Vale 1 ¾',
                 'Una negra con dos puntillos dura 1,75 tiempos: el primero suma la mitad y el '
                 'segundo, la mitad del primero. La semicorchea que le sigue cae casi encima del '
                 'tiempo siguiente.'),
                ('EL TRESILLO', 'Tres donde caben dos',
                 'Las tres corcheas de los cc. 2 y 4 llevan un 3 encima: se tocan en el hueco de '
                 'dos, o sea en un solo tiempo.'),
                ('EL CALDERÓN', 'Se alarga',
                 'En el c. 5 hay una redonda con calderón y, justo detrás, una barra de '
                 'repetición. El calderón dice que la nota se alarga; cuánto, lo decides tú.'),
                ('LAS DOS MANOS', 'Lo mismo, a la octava',
                 'Los dos pentagramas llevan la misma línea, separada una octava. Hay una sola '
                 'melodía que aprender, y cualquier desajuste se oye como un eco.'),
            ],
            pie='La numeración de los compases de tu partitura no cuenta la anacrusa: el primer '
                'compás completo es el 1, y el segundo sistema arranca en el 5.',
        ),
        ritmos=[
            ('DERECHA', 'cc. 1 y 2 · medido', C1 + C2, OCRE, 'treble', 'Mi menor'),
            ('IZQUIERDA', 'cc. 1 y 2 · medido, una octava por debajo', C1_I + C2_I, AZUL,
             'bass', 'Mi menor'),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa suenan a la tecla negra.',
            'Arriba pone Allegro y ff, pero no trae número de metrónomo.',
            'Empieza con una anacrusa de un tiempo; la numeración no la cuenta.',
            'Hay negras con DOS puntillos, que valen 1 tiempo y tres cuartos.',
            'Hay tresillos de corcheas, marcados con un 3, y una redonda con calderón en el c. 5.',
            'Los dos pentagramas llevan la misma música, separada una octava.',
        ],
        reto='Colocar la semicorchea del doble puntillo donde va: casi encima del tiempo siguiente. '
             'Con un puntillo ya cuesta; con dos, la larga se lleva casi todo y la corta queda '
             'pegada a la que viene.',
        truco='Parte cada tiempo en cuatro y cuenta "1-2-3-4": la larga ocupa hasta el 3 del '
              'segundo tiempo, y la corta cae en el 4. Si la corta te sale antes, estás tocando '
              'un solo puntillo.',
        sabias='La música de la película Gladiator (2000) es de Hans Zimmer y de Lisa Gerrard, y '
               'ganó el Globo de Oro a la mejor banda sonora. Las dos manos a la octava del '
               'arreglo imitan la fuerza de la orquesta entera.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en el principio: una nota corta de entrada y después el balanceo '
                      'largo-corto. Ese desnivel tan marcado es el doble puntillo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Hay tres cosas nuevas y ninguna es una nota difícil: son tres maneras de escribir el '
              'tiempo. Se cuenta antes de tocar, y se cuenta en voz alta.',
        reglas=['TODOS LOS FA, EN TECLA NEGRA', 'LA LARGA VALE 1 Y ¾', 'LAS DOS MANOS, A LA OCTAVA'],
        bloques=[
            dict(num=1, titulo='La anacrusa y el c. 1',
                 pista='anacrusa y c. 1 · MEDIDO sobre tu partitura · en la edición el primer '
                       'compás solo trae el último tiempo',
                 sistemas=[
                     dict(cap='a) la anacrusa con tres tiempos de silencio delante para poder '
                              'contarla, y el c. 1 detrás · el ff es de la primera nota',
                          events=ENTRADA + C1, bars=2, matiz='ff'),
                     dict(cap='b) el c. 1 con las largas de UN solo puntillo · NO es lo que pone '
                              'tu partitura: sirve para oír la diferencia entre uno y dos',
                          events=[n('B4', 'q.'), n('E4', 'e'), n('B4', 'q.'), n('G4', 'e')],
                          bars=1, show_time=False),
                     dict(cap='c) las cuatro notas del c. 1, todas de negra · andamio: sin el ritmo, '
                              'se ve el trabajo que hace el doble puntillo',
                          events=[n('B4'), n('E4'), n('B4'), n('G4')],
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE CUENTA UN DOBLE PUNTILLO',
                 texto='Un puntillo suma la mitad de la figura y el segundo suma la mitad del '
                       'primero: negra = 1, con un puntillo 1,5, con dos 1,75. Para la nota '
                       'corta queda un cuarto de tiempo, o sea una semicorchea. Si la corta te '
                       'sale antes de tiempo, estás tocando un puntillo solo: es medio tiempo de '
                       'diferencia, y se oye.'),
            dict(num=2, titulo='Los tresillos de los cc. 2 y 4',
                 pista='cc. 2 y 4 · MEDIDO sobre tu partitura · una blanca con puntillo y tres '
                       'corcheas en el hueco de dos',
                 sistemas=[
                     dict(cap='a) el c. 2 · tres tiempos de nota larga y el tresillo en el '
                              'cuarto, con el 3 encima del grupo',
                          events=C2, bars=1),
                     dict(cap='b) el c. 4 · la misma forma con otras dos notas dentro del tresillo '
                              '· ojo al La sostenido, escrito delante de la nota',
                          events=C4, bars=1, show_time=False),
                     dict(cap='c) el c. 4 con dos corcheas en vez de tres · NO es lo que pone tu '
                              'partitura: sirve para oír cuánto aprieta el tresillo',
                          events=[n('B4', 'h.')] + corch(['B4', 'D5']),
                          bars=1, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda hace lo mismo, una octava abajo',
                 pista='cc. 1 y 2 de la mano izquierda · MEDIDO sobre tu partitura · nota por nota, '
                       'lo mismo que la derecha',
                 sistemas=[
                     dict(cap='a) el c. 1 de la izquierda · con el primer sistema de la hoja a la '
                              'vista, son las mismas notas una octava más abajo',
                          events=C1_I, bars=1, clef='bass', key_sig='Mi menor'),
                     dict(cap='b) y el c. 1 con las dos manos a la vez · cada pareja de notas es '
                              'una octava justa: si suena a otra cosa, una de las dos se ha ido',
                          events=[ac(('B3', 'B4'), 'q..'), ac(('E3', 'E4'), 's'),
                                  ac(('B3', 'B4'), 'q..'), ac(('G3', 'G4'), 's')],
                          bars=1, show_time=False, manos='dobla'),
                 ]),
            dict(num=4, titulo='El c. 5: la redonda con calderón y la barra de repetición',
                 pista='c. 5 · MEDIDO sobre tu partitura · detrás de la redonda hay una barra de '
                       'repetición que abre',
                 sistemas=[
                     dict(cap='a) el calderón dice que la nota dura más de lo que vale, y cuánto '
                              'lo decides tú · se queda hasta que el oído lo pide',
                          events=[dict(pitch='B4', dur='w', art='calderon')],
                          bars=1),
                     dict(cap='b) la barra de repetición que abre · andamio: lo que viene después '
                              'se repite al llegar a la barra que cierra',
                          events=[n('B3'), n('E4'), n('G4'), n('E4'),
                                  n('F#4'), n('B3'), n('D4'), n('F#4')],
                          bars=2, show_time=False, repetir='abre'),
                     dict(cap='c) el calderón sobre la tónica, después de una bajada de cuatro notas '
                              '· andamio · la última nota se queda mientras el oído lo pide',
                          events=[n('G4'), n('F#4'), n('E4'), n('D4'),
                                  dict(pitch='E4', dur='w', art='calderon')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Mi menor', 17, 'E4', 'E2',
                          'el doble puntillo: la larga se lleva 1 tiempo y ¾, y la corta el resto',
                          desde=5, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Gladiator · para casa',
            intro='Quince minutos al día, y los cinco primeros sin piano: contando cada tiempo en '
                  'cuatro partes con el pie. Esta pieza es de contar.',
            bloques=[
                plan((5, 'Contar "1-2-3-4" por tiempo y decir dónde cae la nota corta'),
                     (4, 'La anacrusa y el c. 1, con la derecha sola'),
                     (3, 'El tresillo del c. 2, contando "tres en el hueco de dos"'),
                     (3, 'Las dos manos, de la anacrusa al c. 5')),
                metronomo('Empieza a ♩ = 60 con la derecha sola: a esa velocidad da tiempo a partir '
                          'el tiempo en cuatro y colocar la semicorchea donde va.',
                          'Tu partitura pone Allegro pero no trae número, así que el 60 es de '
                          'trabajo. Sube de seis en seis cuando el doble puntillo salga tres veces '
                          'seguidas sin adelantarse.'),
                ordenar(['Tocar los cc. 1-5 con las dos manos, contando en voz alta.',
                         'Contar el c. 1 sin tocar, partiendo cada tiempo en cuatro.',
                         'Tocar el c. 1 con la derecha sola.',
                         'Tocar los cc. 1 y 2 con la derecha, con el metrónomo a 60.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='del más fácil al más completo · uno de ellos va antes de tocar nada'),
                contar([n('B4', 'q..'), n('E4', 's'), n('B4', 'q..'), n('G4', 's'),
                        n('B4', 'h.'), n('B4', 'e'), n('G4', 'e'), n('C5', 'e')],
                       ['¿Cuántas notas llevan doble puntillo?',
                        '¿Cuántas semicorcheas hay?',
                        '¿Cuántas corcheas forman el tresillo?'],
                       titulo='Cuenta sobre los cc. 1 y 2',
                       pista='son los dos primeros compases de tu partitura'),
                teclado({2: 1, 4: 2, 6: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         'La número 3 es la nota larga de los cc. 1 y 2: el Si.'],
                        titulo='En el teclado',
                        pista='la 1 y la 2 son las dos notas cortas del c. 1; la 3 es la larga'),
                para_clase('La anacrusa y los cc. 1 a 5 con las dos manos, a la velocidad que te '
                           'salga el doble puntillo sin adelantar la corta. Y tráeme apuntado ese '
                           'número: el Allegro lo ponemos a partir de ahí, no al revés.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
