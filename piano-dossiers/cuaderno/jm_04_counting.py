# -*- coding: utf-8 -*-
"""Counting Stars — pieza 4 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (OneRepublic, arr. Becky
   Messer, "Easy Version", descarga de Musescore, 2 páginas):

     - Do mayor: detrás de la clave no hay nada. Compás de 4/4.
     - LA IZQUIERDA TOCA REDONDAS: dos notas a la vez que duran el compás
       entero, una por compás, y en varios sitios ligadas al compás siguiente.
       Es lo que hace que esta pieza sea asequible.
     - La derecha lleva corcheas y algún silencio de corchea, y la digitación
       viene impresa: 2 · 3 · 5 · 2 · 1 · 3 · 2 · 4 · 5 · 1 en los primeros
       compases, y 1 · 5 debajo de la izquierda.
     - Los números de compás vienen impresos (6, 10, 14, 18, 22) y hay barras
       de repetición y una casilla de primera vez.

   Lo que NO se cita nota a nota: la melodía va en corcheas muy juntas y la
   medición de cabezas no sale limpia, así que el material melódico va como
   ANDAMIO en Do mayor y remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jm_comun import (n, ac, sil, corch, plan, metronomo, verdadero_falso,
                      inventa, dibujar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=4, nivel='iniciación',
    slug='CountingStars', formato='adulto',
    titulo_corto='Counting Stars', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'Counting-stars.pdf'),
    yt='https://www.youtube.com/results?search_query=counting+stars+piano+easy',

    ficha=dict(
        titulo='Counting Stars',
        autor='OneRepublic · arreglo de Becky Messer · "Easy Version"',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Mano izq.', 'Redondas'), ('Mano dcha.', 'La melodía'),
               ('Dedos', 'Escritos')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Do mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Lo literal es lo que hace cada mano.',
        armonia=dict(
            titulo='El reparto de trabajo entre las dos manos',
            tarjetas=[
                ('LA IZQUIERDA', 'Una vez por compás',
                 'Dos notas a la vez que duran los cuatro golpes. Se toca en el uno y no se vuelve a '
                 'tocar hasta el compás siguiente.'),
                ('LA DERECHA', 'Corcheas',
                 'Notas cortas, de dos en dos. Es donde está toda la canción y todo el trabajo de '
                 'esta pieza.'),
                ('LOS HUECOS', 'Silencios de corchea',
                 'Medios golpes en los que no se toca. Son los que le dan el aire de la canción, así '
                 'que no se acortan.'),
                ('LAS REPETICIONES', 'Con casilla',
                 'La pieza tiene barras de repetición y una casilla de primera vez. Mira el camino '
                 'antes de tocar, con el lápiz.'),
            ],
            pie='Esta es la primera pieza del cuaderno con el reparto clásico: una mano sostiene y la '
                'otra canta. A partir de aquí casi todas van así, y por eso conviene aprender bien el '
                'gesto de dejar la izquierda quieta.',
        ),
        ritmos=[
            ('MANO DERECHA', 'notas cortas de dos en dos · andamio',
             corch(['C5', 'B4']) + corch(['A4', 'G4']) +
             corch(['A4', 'B4']) + corch(['C5', 'G4']), OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos notas que duran el compás entero · andamio',
             [ac(('F2', 'C3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'La izquierda toca redondas: dos notas a la vez que duran los cuatro golpes.',
            'En varios sitios la redonda está ligada a la del compás siguiente: se toca una vez y '
            'suena ocho golpes.',
            'La derecha va en corcheas, con silencios de corchea en medio.',
            'La digitación viene impresa en las dos manos.',
            'Los números de compás están impresos, y hay repeticiones con casilla de primera vez.',
        ],
        reto='Dejar la izquierda quieta. Cuando la derecha se pone a hacer notas cortas, la izquierda '
             'quiere moverse con ella y suelta la redonda antes de tiempo.',
        truco='Toca la redonda de la izquierda y, sin soltarla, cuenta los cuatro golpes en voz alta '
              'mientras haces la derecha. Si la izquierda se levanta, has perdido. Hazlo con un compás '
              'solo hasta que la mano se quede dormida ahí.',
        sabias='"Easy Version" no quiere decir versión mala: quiere decir que alguien ha decidido qué '
               'se puede quitar sin que la canción deje de ser ella. Aquí lo que se ha quitado es el '
               'movimiento de la izquierda, y la canción sigue reconociéndose entera.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en el bajo de la grabación: cambia una vez por compás, exactamente como '
                      'tu mano izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí las dos manos hacen por primera vez cosas muy distintas: una se queda quieta y la '
              'otra corre. Eso no se aprende tocando las dos: se aprende enseñándole a la izquierda a '
              'no moverse mientras la derecha se mueve.',
        reglas=['LA IZQUIERDA NO SE LEVANTA', 'LAS CORCHEAS, DE DOS EN DOS',
                'LOS HUECOS SE CUENTAN'],
        bloques=[
            dict(num=1, titulo='La izquierda, sola y quieta', clef='bass',
                 pista='andamio en Do mayor · en tu partitura lleva 1 y 5 escritos debajo',
                 sistemas=[
                     dict(cap='a) una vez por compás, y aguantar los cuatro golpes contando en voz '
                              'alta',
                          events=[ac(('C3', 'G3'), 'w'), ac(('A2', 'E3'), 'w'),
                                  ac(('F2', 'C3'), 'w'), ac(('G2', 'D3'), 'w')],
                          ligar=True,
                          bars=4, clef='bass'),
                 ]),
            dict(num=2, titulo='La derecha: notas cortas de dos en dos',
                 pista='andamio · el dibujo de corcheas es el de tu partitura',
                 sistemas=[
                     dict(cap='a) primero en negras, para ver por dónde va la mano',
                          events=[n('E4'), n('F4'), n('G4'), n('A4'),
                                  n('G4'), n('F4'), n('E4'), n('D4')],
                          bars=2),
                     dict(cap='b) y ahora en corcheas, que es como está escrito · de dos en dos, sin '
                              'acelerar',
                          events=corch(['E4', 'F4']) + corch(['G4', 'A4']) +
                                 corch(['G4', 'F4']) + corch(['E4', 'D4']),
                          bars=1, show_time=False),
                     dict(cap='c) y empezando con un hueco de medio golpe · el hueco dura, no se '
                              'salta',
                          events=[{'rest': True, 'dur': 'e'}] + corch(['E4']) +
                                 corch(['F4', 'G4']) + corch(['A4', 'G4']) +
                                 corch(['F4', 'E4']),
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL TRUCO DE LA MANO QUIETA',
                 texto='Pon la izquierda en su sitio, tócala una vez y déjala apoyada con su peso: no '
                       'apretando, apoyada. Ahora haz la derecha. La izquierda tiene que seguir ahí '
                       'cuando acabes el compás. Si se ha levantado, no es un problema de la '
                       'izquierda: es que estás poniendo demasiada atención en la derecha. Ve más '
                       'lento.'),
            dict(num=3, titulo='Y las dos juntas, un compás',
                 pista='muy despacio · un solo compás hasta que salga cinco veces seguidas',
                 sistemas=[
                     dict(cap='a) esto es lo que hace la derecha mientras la izquierda aguanta',
                          events=corch(['E4', 'F4']) + corch(['G4', 'A4']) +
                                 [n('G4'), n('E4')],
                          bars=1),
                     dict(cap='b) y esto la izquierda a la vez (andamio) · una sola vez, en el uno',
                          events=[ac(('C3', 'G3'), 'w')],
                          bars=1, clef='bass', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Counting Stars · para casa',
            intro='Veinte minutos al día. Esta semana la izquierda importa más que la derecha.',
            bloques=[
                plan((5, 'La izquierda sola: tocar y aguantar cuatro golpes'),
                     (5, 'La derecha en negras, los cuatro primeros compases'),
                     (5, 'La derecha en corcheas, de dos en dos'),
                     (5, 'Un compás con las dos manos, cinco veces seguidas')),
                metronomo('Empieza donde te salga el compás entero sin pararte.',
                          'Sube de cuatro en cuatro, y solo si ha salido limpio tres veces.'),
                verdadero_falso([
                    'La mano izquierda toca una vez por compás.',
                    'Una redonda dura cuatro golpes.',
                    'Los silencios de corchea se pueden acortar si tienes prisa.',
                    'La digitación viene escrita en las dos manos.',
                    'Esta pieza tiene repeticiones y una casilla de primera vez.',
                ], titulo='Verdadero o falso', pista='de tu partitura · marca la casilla'),
                inventa(['Solo Do, Re, Mi, Fa y Sol.',
                         'Dos compases de cuatro golpes.',
                         'La mano izquierda, una redonda en cada compás.'],
                        time_sig=(4, 4),
                        titulo='Escribe dos compases con este reparto',
                        pista='una mano quieta y la otra en movimiento'),
                dibujar(['Do', 'Mi', 'Sol', 'Fa', 'Re', 'La', 'Si', 'Do'],
                        titulo='Dibuja tú las notas',
                        pista='solo el óvalo · debajo pone cuál va en cada sitio'),
                para_clase('Los ocho primeros compases con las dos manos y a qué número de metrónomo te han salido. Si la digitación impresa te falla siempre en el mismo sitio, tráelo marcado.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
