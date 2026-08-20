# -*- coding: utf-8 -*-
"""Sonatina per bambini, de Bazzoni — pieza 1 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive (Musescore, 2 páginas,
   "Sonatina per bambini - in la minore - A minor", M. Bazzoni; el mismo
   archivo que la pieza 1 de Luisa, byte a byte):

     - Detrás de la clave NO HAY NADA. La pieza es de La menor y el Sol
       sostenido aparece escrito delante de la nota, en la parte del profesor.
     - 4/4.
     - Es a cuatro manos. La parte del alumno se llama "Bambini / Children 1"
       y lleva los dos pentagramas en clave de sol, con un 8va encima: las dos
       manos tocan lo mismo, a distancia de octava.
     - En la parte del alumno solo hay negras, y una blanca al final de cada
       frase de cuatro compases.

   Abre el álbum porque es la más fácil de toda la carpeta. Todo el material
   generado va como ANDAMIO en La menor y remite a la partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from me_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=1, nivel='intermedio', slug='SonatinaBambini',
    formato='adulto',
    titulo_corto='Sonatina per bambini', time_sig=(4, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source',
                           'Maurizio Bazzoni sonatina para 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=bazzoni+sonatina+per+bambini+4+mani',

    ficha=dict(
        titulo='Sonatina per bambini',
        autor='Maurizio Bazzoni · a cuatro manos · tu parte es la de arriba',
        datos=[('Tonalidad', 'La menor'), ('Compás', '4/4'),
               ('Figuras', 'Negras'), ('Manos', 'Las dos igual'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Las dos manos, la misma melodía',
        pie_ritmos='Andamio en La menor: la forma es la de tu partitura y las notas exactas están '
                   'allí. Arriba y abajo suena lo mismo, una octava más grave.',
        armonia=dict(
            titulo='Por qué esta abre el cuaderno',
            tarjetas=[
                ('AL UNÍSONO', 'Igual en las dos',
                 'Tocan la misma melodía a la vez, una octava de distancia. Lo que aprende una mano '
                 'ya lo sabe la otra.'),
                ('SOLO NEGRAS', 'Y una blanca al final',
                 'Cada frase de cuatro compases dura lo mismo y acaba en una nota larga. Contar aquí '
                 'es sencillo.'),
                ('DOS CLAVES DE SOL', 'Ninguna clave de fa',
                 'Tus dos pentagramas van en clave de sol; la izquierda lee igual que la derecha, '
                 'solo que más abajo.'),
                ('A CUATRO MANOS', 'Con la profesora',
                 'La otra parte la toca ella. Tú llevas la melodía entera y ella pone la armonía '
                 'debajo.'),
            ],
            pie='No es un ejercicio de método: es música real escrita para que un alumno toque con '
                'su profesor desde la primera semana.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras, una por golpe · andamio',
             [n('E4'), n('D4'), n('C4'), n('D4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'lo mismo, una octava abajo · andamio',
             [n('E3'), n('D3'), n('C3'), n('D3')], AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: la armadura es la de La menor sin alteraciones fijas.',
            'Tus dos pentagramas van en clave de sol, los dos.',
            'Las dos manos tocan la misma melodía, a distancia de octava.',
            'Solo hay negras, y una blanca al final de cada frase de cuatro compases.',
            'Encima de tu pentagrama hay un 8va: suena una octava más aguda de lo escrito.',
            'La otra parte, la de abajo del todo, la toca la profesora.',
        ],
        reto='Que las dos manos bajen exactamente a la vez. Como tocan lo mismo, un desajuste de una '
             'fracción de segundo se oye como dos golpes en vez de uno.',
        truco='Aprende primero la mano derecha sola, hasta que la toques sin mirar las teclas. '
              'Coloca entonces la izquierda encima de sus notas sin pulsarlas, y solo entonces baja '
              'las dos juntas.',
        sabias='Bazzoni escribió esta colección de sonatinas para que un alumno pudiera tocar con su '
               'profesor desde la primera clase. Por eso la parte fácil no suena a ejercicio: es la '
               'mitad de una pieza entera, no un boceto.',
        qr=dict(titulo='Escúchala',
                texto='Escucha las dos partes juntas y fíjate en que la tuya, aunque es la más '
                      'sencilla, es la que lleva la melodía.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Tres pasos, en este orden. El segundo parece de más y es el que hace que el tercero '
              'salga bien a la primera.',
        reglas=['UNA MANO PRIMERO', 'LAS DOS A LA VEZ, NO UNA DETRÁS DE OTRA',
                'SIN PRISA: NO HAY NINGUNA'],
        bloques=[
            dict(num=1, titulo='La mano derecha sola',
                 pista='andamio en La menor · las notas exactas están en tu partitura',
                 sistemas=[
                     dict(cap='a) negras, y la frase se cierra con una blanca',
                          events=[n('E4'), n('D4'), n('C4'), n('D4'),
                                  n('E4'), n('F4'), n('E4', 'h')],
                          bars=2),
                     dict(cap='b) la frase que sigue, con el mismo dibujo bajando',
                          events=[n('F4'), n('E4'), n('D4'), n('E4'),
                                  n('D4'), n('C4'), n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La mano izquierda sola, que hace lo mismo',
                 pista='andamio · el mismo dibujo, una octava más abajo',
                 sistemas=[
                     dict(cap='a) las mismas notas, más graves, y también en clave de sol',
                          events=[n('E3'), n('D3'), n('C3'), n('D3'),
                                  n('E3'), n('F3'), n('E3', 'h')],
                          bars=2),
                     dict(cap='b) bajando igual que antes',
                          events=[n('F3'), n('E3'), n('D3'), n('E3'),
                                  n('D3'), n('C3'), n('D3', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Y ahora las dos juntas',
                 pista='andamio · a la vez, con la misma precisión que un solo instrumento',
                 sistemas=[
                     dict(cap='a) las dos manos, exactamente igual, a la vez',
                          events=[ac(('E3', 'E4')), ac(('D3', 'D4')), ac(('C3', 'C4')),
                                  ac(('D3', 'D4')), ac(('E3', 'E4')), ac(('F3', 'F4')),
                                  ac(('E3', 'E4'), 'h')],
                          bars=2),
                     dict(cap='b) y con el dibujo bajando, que también sale en la pieza',
                          events=[ac(('F3', 'F4')), ac(('E3', 'E4')), ac(('D3', 'D4')),
                                  ac(('E3', 'E4')), ac(('D3', 'D4')), ac(('C3', 'C4')),
                                  ac(('D3', 'D4'), 'h')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('La menor', 7, 'A3', 'A2',
                          'las dos manos van a la vez: un dedo lento se oye el doble',
                          desde=4, time_sig=(4, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
