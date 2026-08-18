# -*- coding: utf-8 -*-
"""My Grandfather's Clock — pieza 19 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive (Henry Clay Work, arr.
   Gilbert DeBenedetti, *Level Three*, 2 páginas; el mismo archivo que la
   pieza 9 de José María, byte a byte), leído a 230 dpi:

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
from me_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=19, nivel='intermedio', slug='GrandfathersClock',
    formato='adulto',
    titulo_corto="My Grandfather's Clock", time_sig=(4, 4), key_sig='Sol mayor',
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'Grandfather.pdf'),
    yt='https://www.youtube.com/results?search_query=my+grandfathers+clock+easy+piano',

    ficha=dict(
        titulo="My Grandfather's Clock",
        autor='Henry Clay Work · arr. Gilbert DeBenedetti · Nivel tres',
        datos=[('Tonalidad', 'Sol mayor'), ('Armadura', 'Un sostenido'),
               ('Compás', '4/4'), ('Carácter', 'With precision'),
               ('Trae', 'Dedos, 2 manos')],
        titulo_ritmos='Precisión en las dos manos',
        pie_ritmos='Andamio en Sol mayor. Lo literal es la digitación en las dos manos, pensada '
                   'para que cada dedo caiga siempre en el mismo sitio.',
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
            ('MANO DERECHA', 'negras con el dedo escrito · andamio',
             [n('G4'), n('A4'), n('B4'), n('C5')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'negras con el dedo escrito · andamio',
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
        reto='Que la izquierda siga su digitación tan estrictamente como la derecha. Es fácil '
             'prestar toda la atención a la melodía y dejar que la izquierda improvise sus dedos.',
        truco='Practica la izquierda sola diciendo el número de dedo en voz alta antes de cada '
              'nota, igual que harías con la melodía. Cuando salga sin dudar, añade la derecha.',
        sabias='Henry Clay Work la escribió en 1876 tras oír la historia real de un reloj que se '
               'paró en el momento exacto de la muerte de su dueño, en un hotel de Yorkshire. Se '
               'vendieron más de un millón de copias de la partitura.',
        qr=dict(titulo='Escúchala',
                texto='Escucha alguna versión coral y fíjate en cómo el pulso se mantiene firme de '
                      'principio a fin: eso es "with precision" en la práctica.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana la digitación manda en las dos manos, no solo en la melodía. Se estudia '
              'mano a mano, siguiendo siempre los dedos escritos.',
        reglas=['LOS DEDOS SE SIGUEN EN LAS DOS MANOS', 'EL FA SIEMPRE ES SOSTENIDO',
                'WITH PRECISION: NADA APROXIMADO'],
        bloques=[
            dict(num=1, titulo='La mano en Sol mayor',
                 pista='andamio · el sostenido está en la armadura',
                 sistemas=[
                     dict(cap='a) subiendo por las notas de la tonalidad',
                          events=[n('G4'), n('A4'), n('B4'), n('C5'),
                                  n('D5'), n('C5'), n('B4'), n('A4')],
                          bars=2),
                     dict(cap='b) y la izquierda, con su propia digitación',
                          events=[n('G3'), n('D3'), n('G3'), n('D3'),
                                  n('C3'), n('G3'), n('C3'), n('G3')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='Precisión: negras exactamente iguales',
                 pista='andamio · cada nota, el mismo valor exacto, sin arrastrar',
                 sistemas=[
                     dict(cap='a) cuatro negras seguidas, todas del mismo largo',
                          events=[n('B4'), n('C5'), n('D5'), n('B4')],
                          bars=1),
                     dict(cap='b) y la frase que baja, con la misma exactitud',
                          events=[n('D5'), n('C5'), n('B4'), n('A4')],
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA IZQUIERDA TAMBIÉN LLEVA DEDOS ESCRITOS',
                 texto='Cuando solo la melodía trae digitación, es fácil pensar que la izquierda '
                       'importa menos. Aquí el arreglista decidió marcarla también, y eso es una '
                       'pista: la pieza pide que las dos manos suenen con la misma limpieza, no una '
                       'principal y otra de apoyo. Seguir los dedos en las dos es lo que hace que '
                       '"with precision" se cumpla de verdad.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · las dos manos con la misma exactitud · despacio',
                 sistemas=[
                     dict(cap='a) negras en las dos manos, exactamente a la vez',
                          events=[ac(('G3', 'G4')), ac(('D3', 'A4')), ac(('G3', 'B4')), ac(('D3', 'C5'))],
                          bars=1),
                     dict(cap='b) y la frase que baja, con la misma precisión',
                          events=[ac(('C3', 'D5')), ac(('G3', 'C5')), ac(('C3', 'B4')), ac(('G3', 'A4'))],
                          bars=1, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
