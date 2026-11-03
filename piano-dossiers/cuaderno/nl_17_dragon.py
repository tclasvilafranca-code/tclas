# -*- coding: utf-8 -*-
"""Flying Theme (Cómo entrenar a tu dragón) — pieza 17 de Nel.
   El último reto del álbum.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Flying Theme, adapted
   from How to Train Your Dragon", arreglo de Perfect Harmony, 3 páginas; el
   mismo archivo que la pieza 19 de José María, byte a byte):

     - Empieza sin armadura (Do mayor) y cambia de tonalidad a mitad de la
       pieza: aparece una armadura de dos sostenidos (Re mayor) hacia el
       c. 31.
     - Compás de 4/4.
     - Las dos manos se mueven a la vez y en corcheas: no hay una mano que
       sostenga mientras la otra corre.
     - Hay acordes de tres notas en la derecha y barras de repetición.
     - Los números de compás vienen impresos (6, 13, 21, 28).

   El dosier acota a la primera página y al trabajo del cambio de armadura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from nl_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
RE = 'Re mayor'

CANCION = dict(
    alumno='Nel', carpeta='Nel', num=17, nivel='avanzado', slug='FlyingTheme',
    formato='adulto',
    titulo_corto='Flying Theme', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'nel', 'source',
                           'Copia de Copia de Como entrenar a tu dragon.'),
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
            titulo='El cierre del álbum, y junta todo lo anterior',
            tarjetas=[
                ('LO NUEVO', 'Cambia de tono',
                 'Empieza sin armadura y hacia el c. 31 aparecen dos sostenidos: la única pieza de tu '
                 'álbum que cambia de tonalidad por el camino.'),
                ('LAS DOS MANOS', 'A la vez',
                 'Corcheas en las dos manos: hasta ahora casi siempre había una que sostenía, aquí no '
                 'hay dónde descansar.'),
                ('LOS ACORDES', 'De tres notas',
                 'La derecha toca acordes además de melodía: la misma mano que lleva la línea.'),
                ('LA TONALIDAD', 'Ya conocida',
                 'Re mayor, los mismos dos sostenidos de Can\'t Help Falling in Love: no es nueva, es '
                 'una que vuelve.'),
            ],
            pie='Esta pieza cierra el álbum porque junta lo de todo el curso: dos manos ocupadas, '
                'corcheas seguidas, acordes y una armadura de dos sostenidos, todo a la vez.',
        ),
        ritmos=[
            ('MANO DERECHA', 'corcheas seguidas · andamio',
             corch(['E4', 'F4']) + corch(['A4', 'F4']) + corch(['E4', 'C4']) +
             corch(['B3', 'E4']), OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'también se mueve, ya no sostiene · andamio',
             [n('C3', 'h'), n('G3', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Empieza sin armadura, en Do mayor.',
            'Hacia el compás 31 aparece una armadura de dos sostenidos: la pieza cambia a Re mayor.',
            'Compás de 4/4.',
            'Las dos manos van en corcheas a la vez: ninguna descansa.',
            'La derecha toca también acordes de tres notas.',
            'Son tres páginas, y los números de compás vienen impresos: 6, 13, 21 y 28.',
        ],
        reto='El cambio de tonalidad: justo cuando llevas media pieza y estás cansado, la mano tiene '
             'que empezar a poner dos teclas negras que llevaba treinta compases sin tocar.',
        truco='Trabaja el cambio como un compás suelto: coge los dos compases de antes y los dos de '
              'después, y toca solo esos cuatro, veinte veces. El momento exacto del cambio se '
              'resuelve aislado en un par de días.',
        sabias='El compositor escribió el tema con la orquesta tocando en directo mientras se '
               'proyectaba la escena del primer vuelo, para que la música respirara con la imagen.',
        qr=dict(titulo='Escúchala',
                texto='Escucha dónde la música cambia de color a mitad: eso es el cambio de armadura '
                      'de tu partitura, y se oye sin saber nada de música.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El cierre del álbum, y no trae nada que no hayas hecho ya por separado. Esta semana: '
              'la primera página, y el momento del cambio de armadura trabajado aparte.',
        reglas=['ESTA SEMANA, LA PRIMERA PÁGINA', 'EL CAMBIO DE TONO, AISLADO',
                'NINGUNA MANO DESCANSA: VE MÁS LENTO'],
        bloques=[
            dict(num=1, titulo='Las dos manos moviéndose a la vez',
                 pista='andamio en Do mayor · aquí no hay mano que sostenga',
                 sistemas=[
                     dict(cap='a) primero en negras, con otro dibujo',
                          events=[n('G4'), n('E4'), n('C4'), n('E4'),
                                  n('A4'), n('F4'), n('D4'), n('F4')],
                          bars=2),
                     dict(cap='b) y ahora en corcheas · si tienes que parar a pensar, baja la '
                              'velocidad a la mitad',
                          events=corch(['G4', 'E4']) + corch(['C4', 'E4']) +
                                 corch(['A4', 'F4']) + corch(['D4', 'F4']),
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='El cambio de armadura, aislado',
                 pista='andamio · dos compases antes y dos después, y nada más',
                 sistemas=[
                     dict(cap='a) antes del cambio: sin sostenidos, otro dibujo de escalones',
                          events=[n('E4'), n('G4'), n('A4'), n('G4'),
                                  n('C4'), n('E4'), n('F4'), n('E4')],
                          bars=2),
                     dict(cap='b) y después del cambio: los mismos escalones, con Fa♯ y Do♯',
                          events=[n('F#4'), n('A4'), n('B4'), n('A4'),
                                  n('D4'), n('F#4'), n('G4'), n('F#4')],
                          bars=2, key_sig=RE, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE TRABAJA UN CAMBIO DE TONALIDAD',
                 texto='Nunca tocando la pieza entera a ver si sale. Se coge el compás del cambio, se '
                       'le ponen dos compases delante y dos detrás, y se tocan solo esos cinco, '
                       'veinte veces seguidas, muy despacio: aislar, repetir, reinsertar.'),
            dict(num=3, titulo='Los acordes de la derecha',
                 pista='andamio · tres notas a la vez, y encima llevando la línea',
                 sistemas=[
                     dict(cap='a) los tres dedos bajan juntos, con otra progresión de acordes',
                          events=[ac(('D4', 'F4', 'A4'), 'h'), ac(('E4', 'G4', 'C5'), 'h'),
                                  ac(('F4', 'A4', 'D5'), 'h'), ac(('D4', 'F4', 'A4'), 'h')],
                          bars=2),
                     dict(cap='b) y con el acorde y la melodía en la misma mano',
                          events=[ac(('D4', 'F4', 'A4'), 'h'), n('A4'), n('F4'),
                                  ac(('E4', 'G4', 'C5'), 'h'), n('C5'), n('G4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
