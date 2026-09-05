# -*- coding: utf-8 -*-
"""Sonatina per bambini, de Bazzoni — pieza 1 de Luisa.

   Luisa es la abuela de Arnau: empezó hace poco y le gusta el piano. El
   encargo del cliente: poquito pero bien, que se entienda todo, sencillo.
   Formato de adulto, nivel de iniciación.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore, 2 páginas,
   "Sonatina per bambini - in la minore - A minor", M. Bazzoni):

     - Detrás de la clave NO HAY NADA. La pieza es de La menor y el Sol
       sostenido aparece escrito delante de la nota, en la parte del profesor.
     - 4/4.
     - Es a cuatro manos. La parte del alumno se llama "Bambini / Children 1" y
       lleva LOS DOS PENTAGRAMAS EN CLAVE DE SOL, con un 8va encima: las dos
       manos tocan LO MISMO, a distancia de octava.
     - En la parte del alumno solo hay NEGRAS, y una blanca al final de cada
       frase de cuatro compases.

   Es la pieza más fácil de toda la carpeta y por eso abre el cuaderno. Todo el
   material generado va como ANDAMIO en La menor y remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import sistemas_extra
from lu_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=1, nivel='iniciación', slug='SonatinaBambini',
    formato='adulto',
    titulo_corto='Sonatina per bambini', time_sig=(4, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           'bazzoni-maurizio-sonatina-per-bambini-(4 manos).pdf'),
    yt='https://www.youtube.com/results?search_query=bazzoni+sonatina+per+bambini+4+mani',

    ficha=dict(
        titulo='Sonatina per bambini',
        autor='Maurizio Bazzoni · a cuatro manos · tu parte es la de arriba',
        datos=[('Tonalidad', 'La menor'), ('Compás', '4/4'),
               ('Figuras', 'Negras'), ('Manos', 'Las dos igual'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Las dos manos hacen lo mismo',
        pie_ritmos='Andamio en La menor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Lo importante es que arriba y abajo es lo mismo, una más grave.',
        armonia=dict(
            titulo='Por qué esta es la primera',
            tarjetas=[
                ('LAS DOS IGUAL', 'Al unísono',
                 'Las dos manos tocan la misma melodía. Aprendes una cosa y ya sabes las dos.'),
                ('SOLO NEGRAS', 'Una por golpe',
                 'En tu parte no hay más figura que la negra, y una blanca al acabar cada frase. '
                 'Nada de contar medios tiempos.'),
                ('LAS DOS EN SOL', 'La misma clave',
                 'Tus dos pentagramas llevan clave de sol. La mano izquierda lee igual que la '
                 'derecha, no en la otra clave.'),
                ('NO ESTÁS SOLA', 'A cuatro manos',
                 'La otra parte la toca la profesora. Tú llevas la melodía y ella pone todo lo '
                 'demás debajo.'),
            ],
            pie='Es la pieza más fácil de tu carpeta, y no es un ejercicio: es música de verdad. '
                'Está escrita justo para esto, para que suene bien desde el primer día.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras, una por golpe · andamio',
             [n('A4'), n('C5'), n('B4'), n('D5')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'lo mismo, más grave · andamio',
             [n('A3'), n('C4'), n('B3'), n('D4')], AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: no hay teclas negras fijas.',
            'Tus dos pentagramas van en clave de sol, los dos.',
            'Las dos manos tocan lo mismo, una más grave que la otra.',
            'En tu parte solo hay negras, y una blanca al final de cada frase.',
            'Encima de tu pentagrama hay un 8va: suena más agudo de lo que está escrito.',
            'La otra parte, la de abajo, la toca la profesora.',
        ],
        reto='Que las dos manos bajen a la vez. Como tocan lo mismo, si una llega un poquito antes '
             'se oyen dos golpes en vez de uno, y se nota mucho.',
        truco='Toca primero solo la mano derecha, hasta que salga sin pensar. Después pon la '
              'izquierda encima de sus teclas SIN tocar, y vuelve a tocar la derecha. Y solo '
              'entonces bájalas juntas.',
        sabias='Bazzoni escribió estas sonatinas para que un alumno pueda tocar con su profesor '
               'desde el primer día. La parte fácil no suena a ejercicio porque no lo es: es una '
               'de las dos mitades de una pieza entera.',
        qr=dict(titulo='Escúchala',
                texto='Escucha las dos partes juntas. La tuya es la sencilla, y aun así es la que '
                      'lleva la melodía.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Tres pasos, y en este orden. El segundo parece tonto y es el que hace que el tercero '
              'salga.',
        reglas=['UNA MANO PRIMERO', 'LAS DOS A LA VEZ, NO UNA DETRÁS DE OTRA',
                'DESPACIO, QUE NO HAY PRISA'],
        bloques=[
            dict(num=1, titulo='La mano derecha sola',
                 pista='andamio en La menor · las notas exactas están en tu partitura',
                 sistemas=[
                     dict(cap='a) negras, una por golpe · cuenta "un, dos, tres, cuatro" en voz alta',
                          events=[n('A4'), n('B4'), n('C5'), n('B4'),
                                  n('A4'), n('B4'), n('C5'), n('A4')],
                          bars=2),
                     dict(cap='b) y con la blanca del final, que dura dos golpes · aguántala entera',
                          events=[n('C5'), n('B4'), n('A4'), n('B4'), n('C5', 'h'), n('A4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ UNA MANO PRIMERO',
                 texto='Casi todo lo que sale mal al empezar sale mal por hacer dos cosas a la vez. '
                       'Con una mano sola solo hay que pensar en las notas; con las dos, además hay '
                       'que juntarlas. Son dos trabajos, y se hacen de uno en uno.'),
            dict(num=2, titulo='La mano izquierda sola, que hace lo mismo', clef='bass',
                 pista='andamio · el mismo dibujo, ahora en clave de fa: es la mano que lo toca',
                 sistemas=[
                     dict(cap='a) las mismas notas, más abajo · ya en clave de fa',
                          events=[n('A3'), n('B3'), n('C4'), n('B3'),
                                  n('A3'), n('B3'), n('C4'), n('A3')],
                          bars=2, clef='bass'),
                     dict(cap='b) el mismo dibujo bajando · el meñique es el que menos fuerza tiene, '
                              'y aquí es el que empieza',
                          events=[n('C4'), n('B3'), n('A3'), n('G3'),
                                  n('A3'), n('B3'), n('C4', 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Y ahora las dos juntas',
                 pista='andamio · muy despacio · si oyes dos golpecitos, ve más lento',
                 sistemas=[
                     dict(cap='a) las dos manos, a la vez · un solo sonido, no dos',
                          events=[ac(('A3', 'A4')), ac(('B3', 'B4')), ac(('C4', 'C5')),
                                  ac(('B3', 'B4')), ac(('A3', 'A4'), 'h'), ac(('C4', 'C5'), 'h')],
                          bars=2),
                     dict(cap='b) y con el dibujo bajando, que también sale en la pieza',
                          events=[ac(('C4', 'C5')), ac(('B3', 'B4')), ac(('A3', 'A4')),
                                  ac(('G3', 'G4')), ac(('A3', 'A4'), 'h'), ac(('A3', 'A4'), 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('La menor', 'A3', 'A2', time_sig=(4, 4), variante=0,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
