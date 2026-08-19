# -*- coding: utf-8 -*-
"""Flying Theme (Cómo entrenar a tu dragón) — pieza 19 de Eduard.
   Formato ADULTO. EL ÚLTIMO RETO DEL CURSO.

   Lo comprobado sobre el PDF de su carpeta ("Flying Theme, adapted from How
   to Train Your Dragon", arreglo de Perfect Harmony, 3 páginas; el mismo
   archivo que la pieza 19 de José María, byte a byte):

     - Empieza SIN ARMADURA (Do mayor) y CAMBIA DE TONALIDAD a mitad de la
       pieza: aparece una armadura de dos sostenidos (Re mayor) hacia el
       c. 31. Es la única pieza del cuaderno que cambia de tono por el camino.
     - Compás de 4/4.
     - LAS DOS MANOS SE MUEVEN A LA VEZ y en corcheas: no hay una mano que
       sostenga mientras la otra corre.
     - Hay acordes de tres notas en la derecha y barras de repetición.
     - Los números de compás vienen impresos (6, 13, 21, 28).

   El dosier ACOTA a la primera página y al trabajo del cambio de armadura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from ed_comun import (n, ac, sil, corch, objetivo, plan, verdadero_falso,
                      dibujar, contar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
RE = 'Re mayor'

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=19, nivel='iniciación',
    slug='FlyingTheme', formato='adulto',
    titulo_corto='Flying Theme', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source',
                           'Como entrenar a tu dragon.'),
    yt='https://www.youtube.com/results?search_query=flying+theme+how+to+train+your+dragon+piano',

    ficha=dict(
        titulo='Flying Theme',
        autor='de "Cómo entrenar a tu dragón" · arreglo de Perfect Harmony',
        datos=[('Empieza en', 'Do mayor'), ('Y acaba en', 'Re mayor'),
               ('Compás', '4/4'), ('Páginas', 'Tres'),
               ('Esta semana', 'La primera')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio: el dibujo es el de tu partitura y las notas exactas están allí. Lo '
                   'literal es que las dos manos se mueven a la vez.',
        armonia=dict(
            titulo='La última del curso, y junta todo lo anterior',
            tarjetas=[
                ('LO NUEVO', 'Cambia de tono',
                 'Empieza sin armadura y hacia el c. 31 aparecen dos sostenidos. Es la única pieza del '
                 'cuaderno que cambia de tonalidad por el camino.'),
                ('LAS DOS MANOS', 'A la vez',
                 'Corcheas en las dos. Hasta ahora casi siempre había una que sostenía; aquí no hay '
                 'dónde descansar.'),
                ('LOS ACORDES', 'De tres notas',
                 'La derecha toca acordes además de melodía. Ya los has hecho en la izquierda; aquí '
                 'te tocan con la mano que además lleva la línea.'),
                ('LA TONALIDAD', 'Ya conocida',
                 'Re mayor, los mismos dos sostenidos de Can\'t Help Falling in Love. No es una '
                 'tonalidad nueva: es una que vuelve.'),
            ],
            pie='Esta pieza está al final porque junta lo de todo el curso: dos manos ocupadas, '
                'corcheas seguidas, acordes y una armadura de dos sostenidos. Nada de eso es nuevo '
                'por separado. Lo nuevo es tenerlo todo junto.',
        ),
        ritmos=[
            ('MANO DERECHA', 'corcheas seguidas · andamio',
             corch(['B4', 'D5']) + corch(['A4', 'F#4']) + corch(['G4', 'E4']) +
             corch(['F#4', 'A4']), OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'también se mueve, ya no sostiene · andamio',
             [n('G2', 'h'), n('D3', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Empieza sin armadura, en Do mayor.',
            'Hacia el compás 31 aparece una armadura de DOS SOSTENIDOS: la pieza cambia a Re mayor.',
            'Compás de 4/4.',
            'Las dos manos van en corcheas a la vez: ninguna descansa.',
            'La derecha toca también acordes de tres notas.',
            'Son tres páginas, y los números de compás vienen impresos: 6, 13, 21 y 28.',
        ],
        reto='El cambio de tonalidad. Justo cuando llevas media pieza y estás cansado, la mano tiene '
             'que empezar a poner dos teclas negras que llevaba treinta compases sin tocar.',
        truco='Trabaja el cambio como si fuera un compás suelto: coge los dos compases de antes y los '
              'dos de después, y toca solo esos cuatro, veinte veces. Lo difícil de un cambio de '
              'armadura nunca es la armadura nueva: es el momento exacto en que entra. Aislado se '
              'resuelve en dos días.',
        sabias='John Powell escribió el tema con la orquesta tocando en directo mientras se proyectaba '
               'la escena del primer vuelo, para que la música respirara con la imagen y no al revés. '
               'Estuvo nominada al Oscar y perdió contra "Toy Story 3".',
        qr=dict(titulo='Escúchala',
                texto='Escucha dónde la música cambia de color a mitad: eso es el cambio de armadura '
                      'de tu partitura, y se oye sin saber nada de música.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La última del curso, y no trae nada que no hayas hecho ya por separado. Esta semana: la '
              'primera página, y el momento del cambio de armadura trabajado aparte. Lo demás vendrá '
              'después, y vendrá solo.',
        reglas=['ESTA SEMANA, LA PRIMERA PÁGINA', 'EL CAMBIO DE TONO, AISLADO',
                'NINGUNA MANO DESCANSA: VE MÁS LENTO'],
        bloques=[
            dict(num=1, titulo='Las dos manos moviéndose a la vez',
                 pista='andamio en Do mayor · aquí no hay mano que sostenga',
                 sistemas=[
                     dict(cap='a) primero en negras, para ver hacia dónde va cada mano',
                          events=[n('D4'), n('E4'), n('G4'), n('E4'),
                                  n('D4'), n('B3'), n('A3'), n('D4')],
                          bars=2),
                     dict(cap='b) y ahora en corcheas · si tienes que parar a pensar, baja la velocidad '
                              'a la mitad',
                          events=corch(['D4', 'E4']) + corch(['G4', 'E4']) +
                                 corch(['D4', 'B3']) + corch(['A3', 'D4']),
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='El cambio de armadura, aislado',
                 pista='andamio · dos compases antes y dos después, y nada más',
                 sistemas=[
                     dict(cap='a) antes del cambio: sin sostenidos, todo teclas blancas',
                          events=[n('D4'), n('F4'), n('A4'), n('F4'),
                                  n('E4'), n('G4'), n('B4'), n('G4')],
                          bars=2),
                     dict(cap='b) y después del cambio: los mismos escalones, con Fa♯',
                          events=[n('E4'), n('F#4'), n('A4'), n('F#4'),
                                  n('D4'), n('F#4'), n('A4'), n('F#4')],
                          bars=2, key_sig=RE, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE TRABAJA UN CAMBIO DE TONALIDAD',
                 texto='Nunca tocando la pieza entera a ver si sale. Se coge el compás del cambio, se '
                       'le ponen dos compases delante y dos detrás, y se tocan solo esos cinco, veinte '
                       'veces seguidas, muy despacio. La mano aprende el momento exacto y deja de '
                       'dudar. Después se enchufa a la pieza y ya no falla. Es el mismo método para '
                       'cualquier sitio que se atragante: aislar, repetir, reinsertar.'),
            dict(num=3, titulo='Los acordes de la derecha',
                 pista='andamio · tres notas a la vez, y encima llevando la línea',
                 sistemas=[
                     dict(cap='a) los tres dedos bajan juntos, y la mano no se tensa entre acorde y '
                              'acorde',
                          events=[ac(('D4', 'F4', 'A4'), 'h'), ac(('E4', 'G4', 'B4'), 'h'),
                                  ac(('F4', 'A4', 'D5'), 'h'), ac(('D4', 'F4', 'A4'), 'h')],
                          bars=2),
                     dict(cap='b) y con el acorde y la melodía en la misma mano · el acorde no puede '
                              'atropellar a la nota que va suelta',
                          events=[ac(('D4', 'F4', 'A4'), 'h'), n('A4'), n('F4'),
                                  ac(('E4', 'G4', 'B4'), 'h'), n('B4'), n('G4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Flying Theme · para casa',
            intro='La última del curso. Veinte minutos al día, y solo la primera página más el cambio.',
            bloques=[
                objetivo('Los cinco compases del cambio de armadura, seguidos y sin dudar. Y la '
                         'primera página, despacio y sin pararte.'),
                plan((5, 'Las dos manos en negras, primera página'),
                     (5, 'Las mismas en corcheas, a la mitad de velocidad'),
                     (5, 'Los cinco compases del cambio de tono, aislados'),
                     (5, 'Los acordes de tres notas de la derecha')),
                verdadero_falso([
                    'Esta pieza cambia de tonalidad a mitad.',
                    'La armadura nueva son dos sostenidos, los mismos de la pieza 11.',
                    'En esta pieza hay siempre una mano que descansa.',
                    'Un cambio de armadura se trabaja tocando la pieza entera muchas veces.',
                    'La derecha toca también acordes de tres notas.',
                ], titulo='Verdadero o falso', pista='marca la casilla'),
                dibujar(['Re', 'Mi', 'Fa♯', 'Sol', 'La', 'Si', 'Do♯', 'Re'],
                        titulo='Dibuja las notas del tono nuevo',
                        pista='solo el óvalo · el Fa♯ y el Do♯ van en el mismo sitio que el Fa y el Do'),
                contar([n('D4'), n('E4'), n('G4'), n('E4'), n('D4'), n('B3'), n('A3'), n('D4')],
                       ['¿Cuántos Re hay?', '¿Cuántas notas hay en total?',
                        '¿Cuál es la nota más aguda?'],
                       titulo='Mira y cuenta',
                       pista='es el ejercicio 1a de la hoja de al lado'),
                para_clase('Los cinco compases del cambio de tono. Es lo único que me interesa ver de '
                           'esta semana: si eso está, el resto de la pieza es cuestión de tiempo.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
