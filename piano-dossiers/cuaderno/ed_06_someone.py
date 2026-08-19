# -*- coding: utf-8 -*-
"""Someone You Loved — pieza 6 de Eduard. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta (Lewis Capaldi, Campamento
   Musical Bye Bye Beethoven, 3 páginas; el mismo archivo que la pieza 6 de
   José María, byte a byte):

     - Do mayor: detrás de la clave no hay nada. Compás de 4/4.
     - LA IZQUIERDA TOCA REDONDAS: una o dos notas a la vez que duran el
       compás entero. En los cuatro primeros compases es una sola nota; del
       c. 5 en adelante son dos.
     - LA DERECHA VA EN CORCHEAS SEGUIDAS, casi sin parar, y con ligaduras
       que atan una nota con la siguiente.
     - Hay barra de repetición en el c. 5, y los números de compás vienen
       impresos (5, 9, 13).
     - Del c. 13 en adelante la izquierda deja las redondas y empieza a
       moverse.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from ed_comun import (n, ac, sil, corch, plan, metronomo, nombres, colorear,
                      escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=6, nivel='iniciación',
    slug='SomeoneYouLoved', formato='adulto',
    titulo_corto='Someone You Loved', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source',
                           'SOMEONE YOU LOVED.'),
    yt='https://www.youtube.com/results?search_query=someone+you+loved+piano+easy',

    ficha=dict(
        titulo='Someone You Loved',
        autor='Lewis Capaldi · arreglo del Campamento Musical Bye Bye Beethoven',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Mano izq.', 'Redondas'), ('Mano dcha.', 'Corcheas seguidas'),
               ('Páginas', 'Tres')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Do mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Lo literal es lo que hace cada mano.',
        armonia=dict(
            titulo='Es la misma receta de las dos anteriores, con más notas',
            tarjetas=[
                ('LA IZQUIERDA', 'Sigue quieta',
                 'Redondas: una vez por compás. En los cuatro primeros es una sola nota; después son '
                 'dos a la vez.'),
                ('LA DERECHA', 'Sin parar',
                 'Corcheas casi todo el rato. Es lo nuevo: hasta ahora había huecos donde respirar y '
                 'aquí casi no los hay.'),
                ('LAS LIGADURAS', 'Sin cortar',
                 'Las rayitas que unen dos notas quieren decir que no se levanta el dedo entre una y '
                 'otra. Es lo que hace que suene a canción y no a ejercicio.'),
                ('DEL C. 13', 'Ya se mueve',
                 'Ahí deja las redondas y empieza a andar. Es la segunda mitad, y llega cuando la '
                 'primera esté.'),
            ],
            pie='Tres piezas seguidas con el mismo reparto no es repetirse: es lo que hace que el '
                'gesto se automatice. Cuando la izquierda se quede quieta sola, sin pensarlo, esta '
                'parte del cuaderno habrá cumplido.',
        ),
        ritmos=[
            ('MANO DERECHA', 'corcheas seguidas, sin huecos · andamio',
             corch(['E5', 'D5']) + corch(['C5', 'B4']) + corch(['A4', 'B4']) +
             corch(['C5', 'D5']), OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una nota que dura el compás entero · andamio',
             [n('A2', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'La izquierda toca redondas: en los cuatro primeros compases, una sola nota.',
            'A partir del compás 5 la izquierda toca dos notas a la vez, también redondas.',
            'La derecha va en corcheas casi sin parar, con ligaduras que atan unas notas con otras.',
            'Hay barra de repetición en el compás 5.',
            'Del compás 13 en adelante la izquierda deja de estar quieta.',
        ],
        reto='Aguantar las corcheas sin acelerar. Cuando no hay huecos donde respirar, la mano tiende '
             'a ir cada vez más rápido sin darse cuenta.',
        truco='Toca con el metrónomo puesto MUY lento, de forma que cada golpe caiga en la primera de '
              'cada pareja de corcheas. Si el clic se te adelanta, estás acelerando. Es el único '
              'ejercicio que sirve para esto: contar en voz alta no basta cuando las notas van tan '
              'seguidas.',
        sabias='Capaldi la escribió en veinte minutos y estuvo siete semanas en el número uno en el '
               'Reino Unido. La parte que todo el mundo reconoce no es la melodía: es el bajo, esas '
               'cuatro notas largas que aquí toca tu mano izquierda.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo el bajo, el sonido más grave. Cambia una vez por compás: es tu '
                      'mano izquierda entera.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Ya sabes el reparto, así que esta semana el trabajo es de resistencia: mantener las '
              'corcheas iguales del principio al final del compás. Empieza por cuatro compases y no '
              'sigas hasta que esos cuatro salgan sin acelerar.',
        reglas=['LAS CORCHEAS, TODAS IGUALES', 'LA IZQUIERDA NO SE LEVANTA',
                'CON METRÓNOMO DESDE EL PRIMER DÍA'],
        bloques=[
            dict(num=1, titulo='Las corcheas, sin acelerar',
                 pista='andamio en Do mayor · el dibujo es el de tu partitura',
                 sistemas=[
                     dict(cap='a) primero en negras: la mitad de velocidad y las mismas notas',
                          events=[n('B4'), n('C5'), n('D5'), n('E5'),
                                  n('D5'), n('C5'), n('B4'), n('A4')],
                          bars=2),
                     dict(cap='b) y ahora en corcheas · que la última suene igual de tranquila que la '
                              'primera',
                          events=corch(['B4', 'C5']) + corch(['D5', 'E5']) +
                                 corch(['D5', 'C5']) + corch(['B4', 'A4']),
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ AQUÍ HACE FALTA EL METRÓNOMO',
                 texto='Contar en voz alta funciona cuando hay notas largas: te da tiempo a decir el '
                       'número. Con corcheas seguidas no llegas, y sin darte cuenta empiezas a contar '
                       'al ritmo al que vas tocando en vez de al revés. El metrónomo no se cansa y no '
                       'te sigue. Ponlo lento y déjalo mandar.'),
            dict(num=2, titulo='La izquierda: redondas, y luego dos a la vez', clef='bass',
                 pista='andamio · en los cuatro primeros compases es UNA nota',
                 sistemas=[
                     dict(cap='a) una sola nota por compás, los cuatro primeros',
                          events=[n('B2', 'w'), n('G2', 'w'), n('D3', 'w'), n('A2', 'w')],
                          bars=4, clef='bass'),
                     dict(cap='b) y del c. 5 en adelante, dos a la vez · bajan juntas',
                          events=[ac(('B2', 'F3'), 'w'), ac(('G2', 'D3'), 'w'),
                                  ac(('D3', 'A3'), 'w'), ac(('A2', 'E3'), 'w')],
                          bars=4, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, un compás',
                 pista='muy despacio y con metrónomo · un solo compás hasta que salga cinco veces',
                 sistemas=[
                     dict(cap='a) la derecha, con la izquierda aguantando debajo',
                          events=corch(['B4', 'C5']) + corch(['D5', 'E5']) +
                                 [n('D5'), n('B4')],
                          bars=1),
                     dict(cap='b) y la izquierda a la vez (andamio) · una redonda y nada más',
                          events=[n('B2', 'w')],
                          bars=1, clef='bass', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Someone You Loved · para casa',
            intro='Veinte minutos al día, y el metrónomo puesto desde el primer día.',
            bloques=[
                plan((5, 'Las corcheas en negras, a la mitad de velocidad'),
                     (5, 'Las mismas en corcheas, con metrónomo lento'),
                     (5, 'La izquierda sola: redondas, y luego dos a la vez'),
                     (5, 'Un compás con las dos manos, cinco veces')),
                metronomo('Empieza donde el compás entero salga sin acelerar.',
                          'Apunta el número aunque el día te haya salido mal: eso también es dato.'),
                nombres(['B4', 'C5', 'D5', 'E5', 'C5', 'A4', 'G4', 'B4'],
                        titulo='Los nombres, sin mirar la partitura',
                        pista='son las notas de la zona por la que se mueve la melodía'),
                colorear([n('B4'), n('C5'), n('D5', 'h'), n('E5'),
                          n('D5'), n('C5', 'h'), n('B4'), n('A4')],
                         ['Un color para las de un golpe y otro para las de dos.'],
                         titulo='Colorea según lo que duran',
                         pista='dos colores'),
                escribir(titulo='Copia aquí el compás que peor te salga',
                         pista='con sus ligaduras · cópialo y luego tócalo cinco veces'),
                para_clase('Cuatro compases seguidos con metrónomo, y el número al que te han '
                           'salido sin acelerar.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
