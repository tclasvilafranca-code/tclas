# -*- coding: utf-8 -*-
"""Boig per tu — pieza 8 de Aida. Formato ADULTO exigente.

   Segunda de la etapa del acompañamiento. Lo nuevo aqui es la ENTRADA A
   CONTRATIEMPO: el compas 1 empieza con un silencio de negra con puntillo y la
   melodia entra en la segunda mitad del segundo tiempo. Es el mismo problema
   que la anacrusa de la pieza 3, un escalon mas arriba: alli se entraba antes
   del compas y aqui se entra DENTRO, en un sitio que no coincide con ningun
   golpe del metronomo.

   Lo comprobado sobre el PDF de SU carpeta (1 pagina, escaneada). Este archivo
   NO lo tiene ningun otro alumno:

     - Detras de la clave no hay nada. La pieza se mueve en La menor / Do mayor.
     - 4/4, y no trae numero de metronomo: la casilla de la ficha se llama
       "Caracter".
     - La izquierda hace un acorde de dos notas en REDONDA por compas.

   UNA PARTITURA QUE NO SE PUEDE MEDIR. El PDF lleva dentro una imagen de 86
   ppi y a esa resolucion las dos barras de una semicorchea no existen, asi que
   `medir_figuras` dice NO MEDIBLE en vez de inventarse un numero. Se miro a
   tamano grande, sistema a sistema: corcheas sueltas y de dos en dos, negras
   con puntillo, blancas y acordes largos abajo. **Ni una barra doble.** Queda
   anotado en `auditar_figuras.MIRADAS`.

   LAS ALTURAS del compas 1, medidas a 300 ppp sobre el escaneo (que a esa
   resolucion si da para las cabezas, aunque no para las barras):

       c. 1   silencio de negra con puntillo
              Sol4 · Si4 (corcheas) · Do5 (negra) · Re5 (corchea)

   La suma cierra: 1,5 + 0,5 + 0,5 + 1 + 0,5 = 4.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, plan, metronomo, diferencias,
                      rodear, dibujar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1 de la DERECHA, medido. Cita literal.
ARRANQUE = [sil('q.')] + corch(['G4', 'B4']) + [n('C5'), n('D5', 'e')]

# La izquierda: un acorde de dos notas en redonda por compas. ANDAMIO.
BAJO = [ac(('A2', 'E3'), 'w'), ac(('F2', 'C3'), 'w')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=8, nivel='intermedio',
    slug='BoigPerTu', formato='adulto',
    titulo_corto='Boig per tu', time_sig=(4, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source', 'Boig per tu.pdf'),
    yt='https://www.youtube.com/results?search_query=boig+per+tu+sau+piano',

    ficha=dict(
        titulo='Boig per tu',
        autor='Sau · Carles Sabater i Pep Sala',
        datos=[('Tonalidad', 'La menor'), ('Compás', '4/4'),
               ('Carácter', 'Sin marcar'), ('Empieza', 'A contratiempo'),
               ('Izquierda', 'Redondas')],
        titulo_ritmos='El compás 1, y lo que hace la izquierda',
        pie_ritmos='Arriba, el compás 1 de la derecha MEDIDO en tu partitura, con su silencio de '
                   'entrada. Abajo, andamio en La menor con la figura de la izquierda, que es una '
                   'redonda de dos notas por compás.',
        armonia=dict(
            titulo='Entrar donde no hay golpe',
            tarjetas=[
                ('EL SILENCIO', 'Negra con puntillo',
                 'Tiempo y medio callada. La melodía entra en la segunda mitad del segundo tiempo, '
                 'que es justo donde el metrónomo no suena.'),
                ('LA IZQUIERDA', 'Una redonda',
                 'Dos notas que duran el compás entero. Es el suelo: mientras esté ahí, la entrada '
                 'a contratiempo tiene con qué medirse.'),
                ('SIN ARMADURA', 'La menor',
                 'Detrás de la clave no hay nada, pero la pieza no suena a Do mayor: descansa en '
                 'La, que es su relativo menor.'),
                ('SIN METRÓNOMO', 'Lo eliges tú',
                 'Tu partitura no trae número. Es una balada: lenta, y con sitio para respirar '
                 'entre frase y frase.'),
            ],
            pie='La grabó Sau en 1990 y sigue siendo la canción en catalán más versionada que hay. '
                'La letra la escribió Pep Sala en una noche, y Carles Sabater la cantó por primera '
                'vez sin habérsela aprendido: leyéndola del papel.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el compás 1, MEDIDO · entra a tiempo y medio',
             ARRANQUE, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio en La menor · una redonda por compás',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás 1 empieza con un silencio de negra con puntillo.',
            'La melodía entra en la segunda mitad del segundo tiempo.',
            'La izquierda hace una redonda de dos notas por compás.',
            'No viene ningún número de metrónomo.',
            'Es un escaneo: la partitura está fotografiada, no impresa desde un programa.',
        ],
        reto='Entrar a tiempo y medio. El metrónomo suena en el "uno" y en el "dos", y tú entras '
             'entre el "dos" y el "tres": justo donde no hay clic.',
        truco='Cuenta "un-y-dos-Y" y entra en esa última "y", que es la que va en mayúscula. Contar '
              'solo los números no sirve aquí: la nota de entrada no cae en ningún número.',
        sabias='Es de las pocas canciones en catalán que se cantan enteras en toda España sin que '
               'casi nadie sepa lo que dice la letra. Sau la tocó en directo por última vez en 1999, '
               'cuatro meses antes de que muriera Sabater.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta "un-y-dos-y" desde el primer acorde. La voz entra justo en la última '
                      '"y", y ese retraso es toda la gracia de la frase.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La entrada de esta pieza no se aprende tocando: se aprende contando. Los primeros '
              'cinco minutos de cada día van sin piano.',
        reglas=['CUENTA "UN-Y-DOS-Y" SIEMPRE', 'LA ENTRADA CAE EN LA SEGUNDA "Y"',
                'LA IZQUIERDA NO SE SUELTA'],
        bloques=[
            dict(num=1, titulo='El sitio donde entra la melodía',
                 pista='andamio en La menor · lo que se practica es el hueco, no las notas',
                 sistemas=[
                     dict(cap='a) primero el compás entero en negras, para tener los cuatro golpes',
                          events=[n('A4'), n('B4'), n('C5'), n('B4')],
                          matiz='mp',
                          bars=1),
                     dict(cap='b) y ahora quitando la primera negra y media · ese hueco es tu '
                              'silencio de entrada',
                          events=[sil('q.'), n('A4', 'e'), n('B4'), n('C5')],
                          bars=1, show_time=False),
                     dict(cap='c) y el mismo hueco dos veces seguidas · entrar siempre en el mismo '
                              'sitio es lo que hay que automatizar',
                          events=[sil('q.'), n('A4', 'e'), n('B4'), n('C5'),
                                  sil('q.'), n('C5', 'e'), n('B4'), n('A4')],
                          bars=2, show_time=False),
                     dict(cap='d) y con la izquierda sola marcando el "uno" de cada compás · el '
                              'acorde suena y tú entras después',
                          events=[n('A2'), n('E3'), n('A3'), n('E3'),
                                  n('F2'), n('C3'), n('F3'), n('C3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ ESTA ENTRADA ES DISTINTA DE UNA ANACRUSA',
                 texto='En una anacrusa entras ANTES del compás, y el sitio se encuentra contando '
                       'hacia atrás desde el "uno". Aquí entras DENTRO del compás, en la mitad de '
                       'un tiempo, y no hay ningún golpe con el que coincidir: el metrónomo suena '
                       'en el "dos" y tú entras después. Por eso hay que contar las mitades en voz '
                       'alta hasta que la mano se acostumbre; con los números solos no se llega.'),
            dict(num=2, titulo='El compás 1, tal y como está escrito',
                 pista='c. 1 · MEDIDO en tu partitura, nota a nota',
                 sistemas=[
                     dict(cap='a) el compás 1 con el silencio partido en negra y corchea, para '
                              'contarlo · en tu partitura es UN silencio de negra con puntillo',
                          events=[sil('q'), sil('e')] + corch(['G4', 'B4']) +
                                 [n('C5'), n('D5', 'e')],
                          bars=1),
                     dict(cap='b) y repetido, sin parar entre los dos · el silencio también se cuenta',
                          events=list(ARRANQUE) + list(ARRANQUE),
                          bars=2, show_time=False),
                     dict(cap='c) y sin el silencio, con las notas pegadas al principio · así se ve '
                              'lo que cambia el hueco',
                          events=corch(['G4', 'B4']) + [n('C5'), n('D5', 'e'), sil('q.')],
                          bars=1, show_time=False),
                     dict(cap='d) y dos compases con la misma entrada y distinta nota de llegada · '
                              'el hueco no se mueve nunca de sitio',
                          events=([sil('q.')] + corch(['G4', 'B4']) + [n('C5'), n('D5', 'e')] +
                                  [sil('q.')] + corch(['G4', 'B4']) + [n('E5'), n('D5', 'e')]),
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, con el suelo debajo',
                 pista='el compás 1 de la derecha está MEDIDO · el acorde de abajo es andamio',
                 sistemas=[
                     dict(cap='a) el acorde suena en el "uno" y la melodía entra después',
                          events=[ac(('A2', 'E3'), 'q.'), ac(('G4',), 'e'), ac(('B4',), 'e'),
                                  ac(('C5',)), ac(('D5',), 'e')],
                          bars=1, manos='sostiene'),
                     dict(cap='b) y dos compases seguidos, con el acorde cambiando por debajo',
                          events=[ac(('A2', 'E3'), 'q.'), ac(('G4',), 'e'), ac(('B4',), 'e'),
                                  ac(('C5',)), ac(('D5',), 'e'),
                                  ac(('F2', 'C3'), 'q.'), ac(('C5',), 'e'), ac(('B4',), 'e'),
                                  ac(('A4',)), ac(('G4',), 'e')],
                          bars=2, manos='sostiene', show_time=False),
                     dict(cap='c) y cuatro compases, que es la frase entera · la izquierda marca '
                              'los cuatro "unos" y tú entras cuatro veces en el mismo sitio',
                          events=[ac(('A2', 'E3'), 'q.'), ac(('G4',), 'e'), ac(('B4',), 'e'),
                                  ac(('C5',)), ac(('D5',), 'e'),
                                  ac(('F2', 'C3'), 'q.'), ac(('C5',), 'e'), ac(('B4',), 'e'),
                                  ac(('A4',)), ac(('G4',), 'e'),
                                  ac(('C3', 'G3'), 'q.'), ac(('E4',), 'e'), ac(('G4',), 'e'),
                                  ac(('A4',)), ac(('B4',), 'e'),
                                  ac(('G2', 'D3'), 'q.'), ac(('D5',), 'e'), ac(('B4',), 'e'),
                                  ac(('G4',), 'q.')],
                          bars=4, manos='sostiene', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Cuatro compases con el metrónomo. Si la entrada te sale tarde, no es que '
                       'vayas lenta: es que estás esperando a oír el clic para tocar, y el clic no '
                       'está donde tú entras. Cuenta las mitades en voz alta y entra con la voz, no '
                       'con el oído.'),
        ] + bloques_extra('La menor', 95, 'A4', 'A2',
                          'entrar a tiempo y medio, donde el metrónomo no suena',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Boig per tu · para casa',
            intro='Quince minutos al día, y los cinco primeros contando sin tocar. Es la manera más '
                  'rápida de ganar esta pieza.',
            bloques=[
                plan((5, 'Contar "un-y-dos-y" y dar una palmada en la segunda "y"'),
                     (4, 'El compás 1 de la derecha, con su silencio'),
                     (3, 'Los acordes de la izquierda, en redondas'),
                     (3, 'Los dos primeros compases con las dos manos')),
                metronomo('Empieza a ♩ = 60 con la derecha sola: a esa velocidad da tiempo a oír el '
                          'hueco entero antes de entrar.',
                          'Tu partitura no trae número de metrónomo, así que estos son de trabajo. '
                          'Sube a 76 solo cuando la entrada salga tres veces seguidas.'),
                diferencias(list(ARRANQUE),
                            [sil('q')] + corch(['G4', 'B4']) + [n('C5'), n('D5')],
                            cuantas=2,
                            titulo='Busca las diferencias',
                            pista='arriba, tu compás 1 medido · abajo, con el silencio y una figura '
                                  'cambiados'),
                rodear([[sil('q.')] + corch(['G4', 'B4']) + [n('C5'), n('D5', 'e')],
                        [sil('q.')] + corch(['G4', 'B4']) + [n('C5'), n('D5', 'e')],
                        [sil('q')] + corch(['G4', 'B4']) + [n('C5'), n('D5'), sil('e')],
                        [sil('q.')] + corch(['G4', 'A4']) + [n('C5'), n('D5', 'e')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='uno de los dos es el compás 1 de tu partitura'),
                dibujar(['La', 'Do', 'Mi', 'Sol', 'Si'],
                        titulo='Dibuja estas notas en clave de sol',
                        pista='las tres primeras son el acorde de La menor, que es donde descansa '
                              'la canción'),
                para_clase('Los dos primeros compases con las dos manos, y la entrada contada en '
                           'voz alta. Si la entrada te sale bien sin contar, dímelo: entonces la '
                           'semana que viene subimos la velocidad en vez de repetirla.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
