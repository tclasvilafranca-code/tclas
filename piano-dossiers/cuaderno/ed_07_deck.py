# -*- coding: utf-8 -*-
"""Deck the Halls — pieza 7 de Eduard. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta (mfiles.co.uk, arreglo de Jim
   Paterson, 1 página, 16 compases con repetición; el mismo archivo que la
   pieza 7 de José María, byte a byte):

     - FA MAYOR: un bemol detrás de la clave. Es la PRIMERA pieza del cuaderno
       con armadura, y quiere decir que todos los Si se tocan en la tecla
       negra de al lado.
     - Compás de 4/4. Pone "mp".
     - LAS DOS MANOS tocan acordes de dos notas. No es el reparto de las tres
       piezas anteriores: aquí las dos están ocupadas.
     - Encima vienen los diagramas de guitarra y las letras de los acordes:
       F · C · F · C · F · Dm7 · G · C · B♭.
     - Los números de compás vienen impresos (5, 9, 13).
     - Es MUY repetitiva: los compases 1-4 vuelven casi igual en el 5 y en el
       13. De dieciséis compases, nuevos hay cinco o seis.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from ed_comun import (n, ac, sil, objetivo, plan, diferencias, figuras,
                      acuerdate, cifrado, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=7, nivel='iniciación',
    slug='DeckTheHalls', formato='adulto',
    titulo_corto='Deck the Halls', time_sig=(4, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source',
                           'Deck the Halls (with Boughs of Holly) NAVIDAD.pdf'),
    yt='https://www.youtube.com/results?search_query=deck+the+halls+piano+easy',

    ficha=dict(
        titulo='Deck the Halls',
        autor='Villancico tradicional · arreglo de Jim Paterson · mfiles.co.uk',
        datos=[('Tonalidad', 'Fa mayor'), ('Novedad', 'Un bemol'),
               ('Compás', '4/4'), ('Las dos manos', 'Con acordes'),
               ('Compases', '16')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Fa mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Ojo con los Si: en esta pieza van todos a la tecla negra.',
        armonia=dict(
            titulo='La primera armadura del cuaderno',
            tarjetas=[
                ('EL BEMOL', 'Vale para toda',
                 'Se escribe UNA vez, al principio, y manda en todos los Si de la pieza, estén arriba '
                 'o abajo. No lo repiten en cada nota.'),
                ('LAS DOS MANOS', 'Ocupadas',
                 'Aquí no hay una mano que descanse: las dos tocan acordes de dos notas. Es el cambio '
                 'respecto a las tres piezas anteriores.'),
                ('LAS LETRAS', 'Son acordes',
                 'F, C, Dm7, G, B♭ y los dibujitos de guitarra. No son notas para tocar: son para '
                 'quien te acompañe.'),
                ('LO MEJOR', 'Se repite',
                 'Los compases 1 al 4 vuelven casi igual en el 5 y en el 13. De dieciséis, aprender '
                 'de verdad hay cinco o seis.'),
            ],
            pie='Antes de tocar una nota, coge el lápiz y marca en tu partitura qué compases son '
                'iguales a otros. Vas a descubrir que la pieza es un tercio de lo que parece, y eso '
                'cambia por completo cómo se estudia.',
        ),
        ritmos=[
            ('MANO DERECHA', 'dos notas a la vez, y con puntillo · andamio',
             [ac(('C5', 'A5'), 'q.'), {'pitch': 'Bb4', 'dur': 'e'}, ac(('A4', 'C5')), n('A4')],
             OCRE, 'treble', FA),
            ('MANO IZQUIERDA', 'también dos, y más largas · andamio',
             [ac(('Bb2', 'F3'), 'h'), n('D3'), n('F3')], AZUL, 'bass', FA),
        ],
        especial=[
            'Hay UN bemol detrás de la clave: todos los Si se tocan en la tecla negra.',
            'Las dos manos tocan acordes de dos notas.',
            'Encima del pentagrama vienen las letras de los acordes y los diagramas de guitarra.',
            'Los números de compás están impresos: 5, 9 y 13.',
            'Los compases 1 al 4 vuelven casi iguales en el 5 y en el 13.',
            'Hay barra de repetición al final: la pieza se toca dos veces.',
        ],
        reto='Acordarse del bemol. Los tres primeros días se toca algún Si en blanca sin darse cuenta, '
             'y suena raro sin saber por qué.',
        truco='Antes de tocar, busca en la partitura todos los Si y márcalos a lápiz con un circulito. '
              'Es media hora bien invertida y no vuelves a fallar ninguno. Y en el teclado, deja el '
              'dedo apoyado en esa tecla negra unos segundos antes de empezar: la mano se acuerda por '
              'el tacto mejor que por la vista.',
        sabias='La melodía es galesa y tiene más de quinientos años; la letra en inglés se le puso en '
               '1862. El "fa-la-la-la-la" no es un relleno: en el original era la parte que tocaba el '
               'arpa entre verso y verso, y alguien decidió cantarla.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en el "fa-la-la": es exactamente el mismo trozo repetido cuatro veces.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta pieza trae dos cosas nuevas: la primera armadura y las dos manos con acordes. '
              'Pero también trae un regalo: se repite muchísimo. Empieza por el trabajo de lápiz, que '
              'te va a ahorrar la mitad del tiempo al piano.',
        reglas=['TODOS LOS SI, EN LA TECLA NEGRA', 'MARCA LO QUE SE REPITE ANTES DE TOCAR',
                'LOS DOS DEDOS BAJAN A LA VEZ'],
        bloques=[
            dict(num=1, titulo='El bemol: dónde está la tecla negra',
                 pista='andamio en Fa mayor · todos los Si de esta pieza van ahí',
                 sistemas=[
                     dict(cap='a) la escala de la pieza, bajando · el quinto escalón es el Si bemol',
                          events=[n('C5'), n('Bb4'), n('A4'), n('G4'),
                                  n('F4'), n('G4'), n('A4'), n('Bb4')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y saltando de un Si a otro · para que la mano se aprenda el sitio '
                              'por el tacto',
                          events=[n('Bb4'), n('C5'), n('Bb4'), n('A4'),
                                  n('Bb4'), n('F4'), n('Bb4'), n('G4')],
                          bars=2, key_sig=FA, show_time=False),
                 ]),
            dict(num=2, titulo='Dos notas a la vez, en las dos manos',
                 pista='andamio · las dos bajan juntas, como una sola pieza',
                 sistemas=[
                     dict(cap='a) la derecha: dos notas por golpe',
                          events=[ac(('Bb4', 'D5')), ac(('C5', 'Bb4')), ac(('D5', 'F5')),
                                  ac(('Bb4', 'D5'))],
                          bars=1, key_sig=FA),
                     dict(cap='b) y la izquierda, más largas · toca y deja sonar',
                          events=[ac(('Bb2', 'F3'), 'h'), ac(('F2', 'C3'), 'h'),
                                  ac(('Bb2', 'F3'), 'h'), ac(('D2', 'A2'), 'h')],
                          bars=2, clef='bass', key_sig=FA, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL TRABAJO DE LÁPIZ, ANTES DE TOCAR',
                 texto='Coge la partitura y numera los compases del 1 al 16. Después marca con el mismo '
                       'color los que son iguales entre sí. Vas a ver que el 1 al 4 vuelven en el 5 y '
                       'en el 13 casi sin cambios. Eso quiere decir que lo que hay que aprender de '
                       'verdad son unos cinco compases, y el resto es reconocerlos. Media hora de '
                       'lápiz vale por tres de piano.'),
            dict(num=3, titulo='El compás con puntillo del principio',
                 pista='andamio · es la figura que le da el aire al villancico',
                 sistemas=[
                     dict(cap='a) larga y corta: "LAAA-la" · cuenta "UN dos-y TRES cuatro"',
                          events=[ac(('C5', 'A5'), 'q.'), {'pitch': 'Bb4', 'dur': 'e'},
                                  ac(('A4', 'C5')), n('A4'),
                                  ac(('G4', 'Bb4'), 'q.'), {'pitch': 'A4', 'dur': 'e'},
                                  ac(('G4', 'Bb4')), n('F4')],
                          bars=2, key_sig=FA),
                     dict(cap='b) y sin el puntillo, todo en negras · asi se ve que las notas son las '
                              'mismas y lo unico que cambia es el reparto del tiempo',
                          events=[ac(('C5', 'A5')), n('Bb4'), ac(('A4', 'C5')), n('A4'),
                                  ac(('G4', 'Bb4')), n('A4'), ac(('G4', 'Bb4')), n('F4')],
                          bars=2, key_sig=FA, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Deck the Halls · para casa',
            intro='Veinte minutos al día, y el primer día entero con el lápiz, sin tocar.',
            bloques=[
                objetivo('Marcar en la partitura todos los Si y todos los compases que se repiten, '
                         'y tocar los cuatro primeros compases con las dos manos.'),
                plan((5, 'La escala de Fa, buscando el Si bemol'),
                     (5, 'Los saltos al Si bemol, sin mirar la mano'),
                     (5, 'Los cuatro primeros compases, mano por mano'),
                     (5, 'Los mismos cuatro, con las dos manos')),
                diferencias(
                    [n('C5'), n('Bb4'), n('A4'), n('G4'), n('A4'), n('Bb4')],
                    [n('C5'), n('Bb4'), n('A4'), n('B4'), n('A4'), n('C5')],
                    cuantas=2,
                    titulo='Busca las dos diferencias',
                    pista='una de las dos es justo el fallo que vas a cometer esta semana'),
                figuras([('q.', 'negra con puntillo'), ('e', 'corchea'), ('h', 'blanca'),
                         ('w', 'redonda')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='la negra con puntillo y la corchea van juntas en esta pieza'),
                cifrado(['F', 'C', 'Dm7'],
                        ['Escribe las notas de cada uno, de grave a agudo.',
                         'Ojo: el Dm7 lleva CUATRO notas, no tres. Tienes una casilla de más.'],
                        filas=4, alto_caja=12.0,
                        pista='son los tres que tu partitura lleva impresos encima del pentagrama'),
                para_clase('Los cuatro primeros compases con las dos manos y los Si marcados en la '
                           'partitura. Y trae escritas las notas del Dm7: si te ha salido, ya sabes '
                           'leer cualquier acorde con un 7 detrás.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
