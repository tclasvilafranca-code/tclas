# -*- coding: utf-8 -*-
"""My Grandfather's Clock — pieza 12 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive (Henry Clay Work, arr.
   Gilbert DeBenedetti, *Level Three*, 2 páginas; el mismo archivo que la
   pieza 19 de Mercè y la 9 de José María, byte a byte):

     - Detrás de la clave hay UN SOSTENIDO: Sol mayor.
     - El compás se escribe con una C (4/4), y pone "With precision".
     - Lleva letra debajo del pentagrama, sílaba a sílaba, y digitación
       impresa en las dos manos.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from is_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=12, nivel='intermedio', slug='GrandfathersClock',
    formato='adulto',
    titulo_corto="My Grandfather's Clock", time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', 'Grandfather.pdf'),
    yt='https://www.youtube.com/results?search_query=my+grandfathers+clock+easy+piano',

    ficha=dict(
        titulo="My Grandfather's Clock",
        autor='Henry Clay Work · arr. Gilbert DeBenedetti · Nivel tres',
        datos=[('Tonalidad', 'Sol mayor'), ('Armadura', 'Un sostenido'),
               ('Compás', '4/4'), ('Carácter', 'With precision'),
               ('Trae', 'Dedos, 2 manos')],
        titulo_ritmos='Precisión en las dos manos',
        pie_ritmos='Andamio en Sol mayor. Lo literal es que las dos manos van por negras sueltas. '
                   'Los números de dedo están en tu partitura, no aquí: cópialos encima de estas '
                   'notas, que es justo lo que hay que mirar esta semana.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('WITH PRECISION', 'Con precisión',
                 'No es una indicación de velocidad, es de actitud: cada nota tiene que caer '
                 'exactamente donde toca, ni un pelo antes ni después.'),
                ('DEDOS EN LAS DOS MANOS', 'Sin saltos',
                 'A diferencia de otras piezas, aquí la digitación viene marcada también en la '
                 'izquierda, no solo en la melodía.'),
                ('NIVEL TRES', 'Del propio arreglista',
                 'El arreglista la marca un escalón por encima de piezas parecidas de tu cuaderno: '
                 'es un paso real hacia adelante.'),
                ('UN SOSTENIDO', 'Todos los Fa',
                 'Está en la armadura, así que vale para toda la pieza y las dos manos sin '
                 'excepción.'),
            ],
            pie='Habla de un reloj que se paró para siempre el mismo día que murió su dueño, y se '
                'hizo tan popular en el siglo XIX que dio nombre a un tipo de reloj de pie.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras sueltas, una por golpe · andamio',
             [n('G4'), n('A4'), n('B4'), n('C5')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'negras sueltas, una por golpe · andamio',
             [n('G3'), n('D3'), n('G3'), n('D3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa son teclas negras.',
            'El compás se escribe con una C, que equivale a 4/4.',
            'Arriba pone "With precision".',
            'Trae la letra de la canción, sílaba a sílaba, debajo del pentagrama.',
            'Trae dedos escritos en las dos manos, no solo en la melodía.',
            'El propio arreglista la marca como un nivel por encima de piezas parecidas.',
        ],
        reto='Que la izquierda siga su digitación tan estrictamente como la derecha.',
        truco='Practica la izquierda sola diciendo el número de dedo en voz alta antes de cada '
              'nota, igual que harías con la melodía.',
        sabias='Henry Clay Work la escribió en 1876 tras oír la historia real de un reloj que se '
               'paró en el momento exacto de la muerte de su dueño.',
        qr=dict(titulo='Escúchala',
                texto='Escucha alguna versión coral y fíjate en cómo el pulso se mantiene firme.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana la digitación manda en las dos manos, no solo en la melodía. Los '
              'números están en tu partitura, no en estas hojas: cópialos aquí encima y '
              'después síguelos siempre.',
        reglas=['LOS DEDOS SE SIGUEN EN LAS DOS MANOS', 'EL FA SIEMPRE ES SOSTENIDO',
                'WITH PRECISION: NADA APROXIMADO'],
        bloques=[
            dict(num=1, titulo='La mano en Sol mayor',
                 pista='andamio · el sostenido está en la armadura',
                 sistemas=[
                     dict(cap='a) bajando por las notas de la tonalidad',
                          events=[n('D5'), n('C5'), n('B4'), n('A4'),
                                  n('G4'), n('A4'), n('B4'), n('C5')],
                          bars=2),
                     dict(cap='b) y la izquierda, con otra combinación',
                          events=[n('D3'), n('G3'), n('D3'), n('G3'),
                                  n('B2'), n('D3'), n('B2'), n('D3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='Precisión: negras exactamente iguales',
                 pista='andamio · cada nota, el mismo valor exacto, sin arrastrar',
                 sistemas=[
                     dict(cap='a) cuatro negras seguidas, subiendo esta vez',
                          events=[n('D5'), n('C5'), n('B4'), n('D5')],
                          bars=1),
                     dict(cap='b) y la frase que baja, con la misma exactitud',
                          events=[n('D5'), n('C5'), n('B4'), n('G4')],
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA IZQUIERDA TAMBIÉN LLEVA DEDOS ESCRITOS',
                 texto='Cuando solo la melodía trae digitación, es fácil pensar que la izquierda '
                       'importa menos. Aquí el arreglista decidió marcarla también, y eso es una '
                       'pista: la pieza pide que las dos manos suenen con la misma limpieza.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · las dos manos con la misma exactitud · despacio',
                 sistemas=[
                     dict(cap='a) negras en las dos manos, con otra combinación',
                          events=[ac(('D3', 'D5')), ac(('G3', 'C5')), ac(('D3', 'B4')), ac(('G3', 'D5'))],
                          bars=1),
                     dict(cap='b) y la frase que baja, con la misma precisión',
                          events=[ac(('B2', 'B4')), ac(('D3', 'C5')), ac(('B2', 'D5')), ac(('D3', 'B4'))],
                          bars=1, show_time=False),
                 ]),
        ] + bloques_extra('Sol mayor', 19, 'G4', 'G2',
                          '"with precision": cada nota exactamente donde toca',
                          desde=4, time_sig=(4, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
