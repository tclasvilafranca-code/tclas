# -*- coding: utf-8 -*-
"""Un Beso y una Flor (Nino Bravo) — pieza 17 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musicaymaestro.com,
   2 páginas, 35 compases):

     - UN BEMOL detrás de la clave: Fa mayor.
     - Compás partido / C, y pone "Allegro".
     - CIFRADO IMPRESO encima del pentagrama: F · Dm · B♭ · Am · A · C · F/A.
       Siete acordes, y uno de ellos con la nota del bajo indicada (F/A).
     - La derecha lleva SEMICORCHEAS desde el primer compás.
     - La izquierda empieza con blancas ligadas y luego salta: bajos sueltos,
       lejos unos de otros.
     - En los cc. 33-35 hay TRESILLOS marcados con el número 3.
     - Hay barra de repetición y casillas de primera y segunda vez.

   Todo el material inventado va como ANDAMIO en Fa mayor. Las semicorcheas no
   se escriben en las hojas generadas (el motor no las tiene): se trabajan como
   grupos de cuatro por golpe y se explican en prosa.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, semi, plan, escalera, cifrado, unir, nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=17, nivel='intermedio', slug='UnBesoYUnaFlor',
    formato='adulto',
    titulo_corto='Un Beso y una Flor', time_sig=(4, 4), key_sig='Fa mayor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'Un beso-y-una-flor-nino-bravo.pdf'),
    yt='https://www.youtube.com/results?search_query=un+beso+y+una+flor+piano',

    ficha=dict(
        titulo='Un Beso y una Flor',
        autor='Nino Bravo · edición de Musicaymaestro.com',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', 'C (4/4)'),
               ('Carácter', 'Allegro'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Dos')],
        titulo_ritmos='Cuatro notas por golpe',
        pie_ritmos='Andamio en Fa mayor, escrito en corcheas para que se lea. En tu partitura son '
                   'SEMICORCHEAS: cuatro por golpe en vez de dos.',
        armonia=dict(
            titulo='La primera pieza en semicorcheas',
            tarjetas=[
                ('CUATRO POR GOLPE', 'Semicorcheas',
                 'Donde hasta ahora ponías dos notas por golpe, aquí van cuatro. No son más '
                 'difíciles de leer: son más difíciles de mantener iguales.'),
                ('SIETE ACORDES', 'Y uno con bajo',
                 'F, Dm, B♭, Am, A, C y F/A. Esa barra del F/A quiere decir: acorde de Fa, pero con '
                 'La en el bajo. Es la primera vez que lo ves escrito.'),
                ('LOS SALTOS', 'La izquierda',
                 'Los bajos están lejos unos de otros y hay que ir a buscarlos. Con la derecha en '
                 'semicorcheas, la izquierda no puede mirarse.'),
                ('LOS TRESILLOS', 'Al final',
                 'En los tres últimos compases hay grupos de tres marcados con un 3: tres notas en '
                 'el tiempo de dos. Es el frenazo escrito de la canción.'),
            ],
            pie='Es la pieza más rápida de leer del cuaderno junto con A comme amour, y las dos '
                'están al final por lo mismo: cuatro notas por golpe solo se sostienen cuando la '
                'mano ya está suelta, y eso son meses, no días.',
        ),
        ritmos=[
            ('MANO DERECHA', 'en tu partitura son cuatro por golpe · andamio',
             [n('F4', 'e'), n('G4', 'e'), n('A4', 'e'), n('Bb4', 'e'),
              n('A4', 'e'), n('G4', 'e'), n('F4', 'e'), n('E4', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'blancas ligadas, y luego saltos · andamio',
             [n('F2', 'h'), n('C3', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Un bemol detrás de la clave: Fa mayor.',
            'Pone "Allegro": rápido, y sin número de metrónomo.',
            'El cifrado viene impreso: F, Dm, B♭, Am, A, C y F/A.',
            'F/A quiere decir acorde de Fa con La en el bajo.',
            'La derecha lleva semicorcheas desde el primer compás.',
            'En los tres últimos compases hay tresillos marcados con un 3.',
        ],
        reto='Que las cuatro notas de cada golpe suenen iguales. Con semicorcheas, la primera de '
             'cada grupo sale sola y las otras tres se atropellan: se oye un "ta-carara" en vez de '
             'cuatro notas.',
        truco='Toca los grupos de cuatro PARANDO en cada primera nota: cuatro rápidas, parada larga, '
              'cuatro rápidas, parada larga. Las paradas le dan tiempo a la mano a recolocarse, y '
              'lo que aprende es el grupo entero, no la primera nota más tres tropiezos.',
        sabias='Nino Bravo la grabó en 1972, poco antes de morir en un accidente con veintiocho '
               'años. La canción llevaba meses sin publicarse porque el sello no la veía como '
               'single: acabó siendo la más conocida de toda su discografía.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el final, donde la música frena. Ahí están los tresillos escritos: '
                      'no es que el pianista vaya más lento, es que están escritos así.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí hay dos cosas nuevas y las dos son de mano: cuatro notas por golpe arriba y '
              'saltos a ciegas abajo. Se trabajan por separado y con paradas, nunca seguido.',
        reglas=['GRUPOS DE CUATRO, CON PARADAS', 'LA IZQUIERDA SALTA SIN MIRARSE',
                'UN BEMOL: TODOS LOS SI'],
        bloques=[
            dict(num=1, titulo='Los grupos de cuatro, con parada',
                 pista='andamio en Fa mayor escrito en corcheas · en tu partitura van al doble de '
                       'notas por golpe',
                 sistemas=[
                     dict(cap='a) cuatro notas rápidas y una parada larga · la parada es parte del '
                              'ejercicio, no un descanso',
                          events=[n('F4', 'e'), n('G4', 'e'), n('A4', 'e'), n('Bb4', 'e'),
                                  n('C5', 'h'),
                                  n('C5', 'e'), n('Bb4', 'e'), n('A4', 'e'), n('G4', 'e'),
                                  n('F4', 'h')],
                          bars=2, key_sig='Fa mayor'),
                     dict(cap='b) y AHORA con su figura de verdad, la semicorchea · el mismo dibujo el doble de rápido, tal y como está impreso en tu partitura',
                          events=semi(['F4', 'G4', 'A4', 'Bb4']) + semi(['C5', 'C5', 'Bb4', 'A4']) + [n('F4'), n('G4')],
                          bars=1, show_time=False, key_sig='Fa mayor'),
                 ]),
            dict(num=2, titulo='Los saltos de la izquierda, a ciegas', clef='bass',
                 pista='andamio en Fa mayor · el brazo aprende la distancia, no la tecla',
                 sistemas=[
                     dict(cap='a) de un bajo al siguiente, sin mirar · llega antes de tiempo y '
                              'espera encima de la tecla',
                          events=[n('F2', 'h'), n('C3', 'h'), n('Bb2', 'h'), n('F2', 'h')],
                          bars=2, clef='bass', key_sig='Fa mayor'),
                     dict(cap='b) con los saltos grandes de verdad · prepáralo durante la nota '
                              'anterior, no en el momento',
                          events=[n('F2', 'h'), n('A3', 'h'), n('D2', 'h'), n('C3', 'h')],
                          bars=2, clef='bass', key_sig='Fa mayor', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UN TRESILLO, Y QUÉ ES F/A',
                 texto='Un tresillo son tres notas donde caben dos, y por eso la música se aprieta; '
                       'en tus tres últimos compases van marcados con un 3. Y F/A es el acorde de '
                       'Fa de siempre con el La abajo: cambia el bajo, no el acorde.'),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='andamio en Fa mayor · a un tercio de la velocidad final',
                 sistemas=[
                     dict(cap='a) grupos arriba y bajo largo abajo · el bajo cae en el uno y ya no '
                              'se mueve hasta el tres',
                          events=[ac(('F2', 'F4'), 'e'), n('G4', 'e'), n('A4', 'e'), n('Bb4', 'e'),
                                  ac(('C3', 'C5'), 'e'), n('Bb4', 'e'), n('A4', 'e'), n('G4', 'e')],
                          bars=2, key_sig='Fa mayor'),
                     dict(cap='b) y con el salto de la izquierda metido dentro · el bajo se va '
                              'lejos justo cuando la derecha va más rápido',
                          events=[ac(('Bb2', 'D5'), 'e'), n('C5', 'e'), n('Bb4', 'e'), n('A4', 'e'),
                                  ac(('A3', 'F4'), 'e'), n('G4', 'e'), n('A4', 'e'), n('F4', 'e')],
                          bars=2, key_sig='Fa mayor', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Un Beso y una Flor · para casa',
            intro='Veinte minutos, todo con paradas. Esta semana no se toca nada seguido.',
            bloques=[
                plan((6, 'Grupos de cuatro con parada larga entre grupo y grupo'),
                     (5, 'Los saltos de la izquierda, sin mirarse la mano'),
                     (5, 'La derecha sola, de dos en dos compases'),
                     (4, 'Las dos juntas, a un tercio de velocidad')),
                escalera((50, 'grupos de cuatro con parada'),
                         (65, 'dos grupos seguidos, sin parar entre ellos'),
                         (80, 'un compás entero, las dos manos'),
                         meta='la velocidad a la que las cuatro notas suenen iguales — tu partitura '
                              'pone "Allegro" pero no trae número',
                         notas=['Si la primera nota de cada grupo empieza a sonar más fuerte que '
                                'las otras tres, baja un escalón.']),
                cifrado(['F', 'Dm', 'B♭', 'Am', 'C'],
                        ['Escribe las tres notas de cada uno, de grave a agudo.',
                         'Y aparte: ¿qué nota va abajo del todo en el F/A?'],
                        pista='son cinco de los siete que trae impresos tu partitura'),
                unir([('F/A', 'acorde de Fa con La en el bajo'),
                      ('Tresillo', 'tres notas donde caben dos'),
                      ('Semicorchea', 'la mitad de una corchea: cuatro por golpe'),
                      ('Allegro', 'rápido, pero sin número de metrónomo')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                nombres(['F4', 'A4', 'Bb4', 'D5', 'C5', 'G4', 'F4'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='estamos en Fa mayor: ojo con la tercera'),
                para_clase('Los grupos de cuatro con parada y a qué escalón has llegado. Los '
                           'tresillos del final ni los mires todavía: los contamos juntos, que '
                           'explicados por escrito no se entienden.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
