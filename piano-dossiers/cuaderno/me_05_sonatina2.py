# -*- coding: utf-8 -*-
"""Sonatina nº 2, de Bazzoni — pieza 5 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Sonatina n. 2 -
   pianoforte a 4 mani", in sol maggiore - in G Major, 2 páginas; el mismo
   archivo que la pieza 3 de Luisa, byte a byte), leído a 230 dpi:

     - Detrás de la clave hay UN SOSTENIDO: Sol mayor.
     - 4/4.
     - Es a cuatro manos, con los dos pentagramas del alumno en clave de sol,
       y las dos manos tocando lo mismo, a distancia de octava.
     - Solo negras, con alguna blanca al cierre de frase.

   Es la primera pieza del álbum con armadura de verdad, y con las manos al
   unísono no cuesta nada aprenderla: aparece un sostenido y ya está.
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
    alumno='Mercè', carpeta='Merce', num=5, nivel='intermedio', slug='SonatinaSolMayor',
    formato='adulto',
    titulo_corto='Sonatina nº 2', time_sig=(4, 4), key_sig='Sol mayor',
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source',
                           'bazzoni-maurizio-sonatia-sol-maggiore-174724.'),
    yt='https://www.youtube.com/results?search_query=bazzoni+sonatina+sol+maggiore+4+mani',

    ficha=dict(
        titulo='Sonatina nº 2',
        autor='Maurizio Bazzoni · a cuatro manos · tu parte es Pianoforte 1',
        datos=[('Tonalidad', 'Sol mayor'), ('Armadura', 'Un sostenido'),
               ('Compás', '4/4'), ('Manos', 'Al unísono'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='La primera armadura de verdad',
        pie_ritmos='Andamio en Sol mayor. Las dos manos tocan la misma melodía, a distancia de '
                   'octava, y el sostenido de la armadura vale para las dos.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('UN SOSTENIDO FIJO', 'Al lado de la clave',
                 'Todos los Fa de la pieza son sostenidos, en las dos manos, sin que haga falta '
                 'escribirlo cada vez.'),
                ('SIGUE AL UNÍSONO', 'Igual en las dos',
                 'Como en la pieza anterior, aprender una mano es aprender la otra: tocan lo mismo, '
                 'una octava más grave.'),
                ('SOLO NEGRAS', 'Con alguna blanca',
                 'El ritmo sigue siendo sencillo; lo nuevo de esta semana es solo la armadura.'),
                ('A CUATRO MANOS', 'Con la profesora',
                 'La parte de acompañamiento la toca ella; tú llevas la melodía entera con el '
                 'sostenido ya puesto.'),
            ],
            pie='Es la segunda sonatina de la colección, pensada para el mismo tipo de dueto que la '
                'primera, pero ya con un color armónico distinto.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras, con el Fa sostenido · andamio',
             [n('G4'), n('A4'), n('B4'), n('C5')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'lo mismo, una octava abajo · andamio',
             [n('G3'), n('A3'), n('B3'), n('C4')], AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa son teclas negras.',
            'La tonalidad es Sol mayor.',
            'Compás de 4/4.',
            'Las dos manos tocan la misma melodía, a distancia de octava.',
            'Solo hay negras, con alguna blanca al final de frase.',
            'La otra parte, la de abajo del todo, la toca la profesora.',
        ],
        reto='Acordarse del Fa sostenido sin tener que pensarlo cada vez que aparece. Al ser la '
             'primera armadura de tu cuaderno, la mano todavía no lo tiene automatizado.',
        truco='Antes de tocar la pieza entera, toca solo la escala de Sol mayor de arriba abajo '
              'tres veces, fijándote en que el Fa siempre sale negro. Después la partitura no te '
              'sorprende en ningún sitio.',
        sabias='Poner un solo sostenido en la armadura, en vez de escribirlo nota a nota, es una '
               'convención que se estandarizó en el siglo XVIII: antes cada compositor lo hacía a su '
               'manera, y la lectura era mucho más lenta.',
        qr=dict(titulo='Escúchala',
                texto='Escucha las dos partes juntas y fíjate en el color distinto que tiene '
                      'respecto a la primera sonatina: es el mismo tipo de pieza, pero en otro tono.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El único cambio real respecto a la pieza anterior es la armadura. El orden de '
              'estudio es el mismo: una mano, luego la otra, y solo entonces las dos.',
        reglas=['EL FA SIEMPRE ES SOSTENIDO', 'UNA MANO PRIMERO', 'LAS DOS A LA VEZ AL FINAL'],
        bloques=[
            dict(num=1, titulo='La mano derecha sola, en Sol mayor',
                 pista='andamio · el Fa sostenido está en la armadura, no hay que escribirlo',
                 sistemas=[
                     dict(cap='a) subiendo por las notas de la tonalidad',
                          events=[n('G4'), n('A4'), n('B4'), n('C5'),
                                  n('D5'), n('C5'), n('B4', 'h')],
                          bars=2),
                     dict(cap='b) y la frase que baja, pasando por el Fa sostenido',
                          events=[n('D5'), n('C5'), n('B4'), n('A4'),
                                  n('G4'), n('F#4'), n('G4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La mano izquierda sola, que hace lo mismo',
                 pista='andamio · el mismo dibujo, una octava más abajo',
                 sistemas=[
                     dict(cap='a) las mismas notas, más graves',
                          events=[n('G3'), n('A3'), n('B3'), n('C4'),
                                  n('D4'), n('C4'), n('B3', 'h')],
                          bars=2),
                     dict(cap='b) y bajando igual, con el Fa sostenido',
                          events=[n('D4'), n('C4'), n('B3'), n('A3'),
                                  n('G3'), n('F#3'), n('G3', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ NO HACE FALTA ESCRIBIR EL SOSTENIDO CADA VEZ',
                 texto='La armadura es un acuerdo: en cuanto se ve un sostenido junto a la clave, '
                       'vale para toda la pieza y para las dos manos, sin excepción. Es distinto de '
                       'un sostenido escrito delante de una nota suelta, que solo dura ese compás. '
                       'Con una sola armadura de un sostenido, memorizarla es cuestión de minutos: '
                       'solo hay una tecla que recordar.'),
            dict(num=3, titulo='Y ahora las dos juntas',
                 pista='andamio · a la vez, con la misma precisión de la pieza anterior',
                 sistemas=[
                     dict(cap='a) las dos manos, exactamente igual, a la vez',
                          events=[ac(('G3', 'G4')), ac(('A3', 'A4')), ac(('B3', 'B4')), ac(('C4', 'C5')),
                                  ac(('D4', 'D5')), ac(('C4', 'C5')), ac(('B3', 'B4'), 'h')],
                          bars=2),
                     dict(cap='b) y con el Fa sostenido, que también sale en la pieza',
                          events=[ac(('D4', 'D5')), ac(('C4', 'C5')), ac(('B3', 'B4')), ac(('A3', 'A4')),
                                  ac(('G3', 'G4')), ac(('F#3', 'F#4')), ac(('G3', 'G4'), 'h')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Sol mayor', 7, 'G3', 'G2',
                          'el Fa sostenido vale para toda la pieza, no solo al principio',
                          desde=4, time_sig=(4, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
