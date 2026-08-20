# -*- coding: utf-8 -*-
"""Puff the Magic Dragon — pieza 3 de Isaac.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Puff the Magic
   Dragon", arr. Eric Moore, 1 página; el mismo archivo que la pieza 4 de
   Mercè y la 5 de Luisa, byte a byte):

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4.
     - La izquierda hace una redonda de DOS notas a la vez por compás.
     - La derecha lleva la melodía en negras y blancas.
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

CANCION = dict(
    alumno='Isaac', carpeta='Isaac', num=3, nivel='intermedio', slug='PuffTheMagicDragon',
    formato='adulto',
    titulo_corto='Puff the Magic Dragon', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'isaac', 'source', 'Puff era un Drac Magic.pdf'),
    yt='https://www.youtube.com/results?search_query=puff+the+magic+dragon+easy+piano',

    ficha=dict(
        titulo='Puff the Magic Dragon',
        autor='Peter Yarrow y Leonard Lipton · arr. Eric Moore',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Izquierda', 'Redonda doble'), ('Derecha', 'Negras y blancas'),
               ('Carácter', 'Suave')],
        titulo_ritmos='Dos notas a la vez, una vez por compás',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la izquierda toca dos notas '
                   'juntas y las sostiene, y la derecha lleva la melodía.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('DOS NOTAS A LA VEZ', 'En la izquierda',
                 'Bajan dos dedos juntos, y los dos tienen que sonar exactamente al mismo tiempo.'),
                ('SIGUE SOSTENIENDO', 'El compás entero',
                 'Aunque ahora sean dos notas, se tocan una vez y se dejan sonar hasta el compás '
                 'siguiente.'),
                ('MELODÍA SUAVE', 'Sin saltos grandes',
                 'La derecha se mueve por notas vecinas casi siempre. Es una canción de cuna, no '
                 'una marcha.'),
                ('POCOS ACORDES', 'Se repiten',
                 'La izquierda usa dos o tres combinaciones de notas en toda la pieza.'),
            ],
            pie='Es una canción sobre crecer y dejar atrás la infancia. Se toca despacio y sin '
                'prisa, como quien recuerda algo con cariño: nada en la partitura pide velocidad, '
                'y forzarla rompe justo lo que hace especial a esta pieza.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras y blancas · andamio',
             [n('C4'), n('D4'), n('E4'), n('F4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos notas juntas, un compás · literal',
             [ac(('C3', 'E3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4.',
            'La izquierda toca dos notas a la vez, una sola vez por compás.',
            'La derecha lleva la melodía en negras y blancas.',
            'Las dos notas de la izquierda se sostienen el compás entero.',
            'La izquierda usa solo dos o tres combinaciones de notas en toda la pieza.',
        ],
        reto='Que las dos notas de la izquierda caigan exactamente juntas. Si un dedo llega antes '
             'que el otro se oye un pequeño golpe doble.',
        truco='Toca solo la izquierda y baja las dos notas con el brazo entero, no con los dedos por '
              'separado. Repítelo despacio varias veces mirando que los dos dedos toquen la tecla '
              'exactamente en el mismo instante.',
        sabias='La canción se basa en un poema de Leonard Lipton de 1959, y aunque durante años '
               'circuló el rumor de que hablaba de drogas, sus autores siempre explicaron que trata '
               'de la pérdida de la infancia.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo la base de piano nunca se adelanta a la voz.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo es que la mano izquierda ya no toca una nota sola, sino dos juntas. El resto '
              'sigue el mismo orden de siempre.',
        reglas=['LAS DOS NOTAS CAEN A LA VEZ', 'SE SOSTIENEN EL COMPÁS ENTERO',
                'SUAVE: SIN ACENTOS FUERTES'],
        bloques=[
            dict(num=1, titulo='La izquierda: dos notas juntas',
                 pista='andamio en Do mayor · otra pareja de acordes',
                 sistemas=[
                     dict(cap='a) dos notas por compás, sostenidas enteras',
                          events=[ac(('D3', 'F3'), 'w'), ac(('G2', 'B2'), 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de combinación, sin soltar antes de tiempo',
                          events=[ac(('A2', 'C3'), 'w'), ac(('D3', 'F3'), 'w')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: la melodía suave',
                 pista='andamio · notas vecinas, sin saltos',
                 sistemas=[
                     dict(cap='a) empezando más arriba y bajando',
                          events=[n('G4'), n('F4'), n('E4'), n('D4'), n('C4', 'h'), n('D4', 'h')],
                          bars=2),
                     dict(cap='b) y la frase que sigue, subiendo otra vez',
                          events=[n('E4'), n('F4'), n('G4'), n('A4'), n('G4', 'h'), n('F4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE TOCAN LAS DOS NOTAS COMO UNA SOLA',
                 texto='Un acorde de dos notas suena como una unidad, no como dos golpes separados. '
                       'Si al escuchar la izquierda de esta pieza notas cualquier desajuste, sigue '
                       'practicándola sola hasta que suene limpia como un solo sonido.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · muy despacio, dejando sonar la izquierda entera',
                 sistemas=[
                     dict(cap='a) la izquierda entra en el uno y la derecha se mueve encima',
                          events=[ac(('D3', 'F3', 'D4')), n('E4'), n('F4'), n('G4'),
                                  ac(('G2', 'B2', 'F4'), 'h'), n('E4', 'h')],
                          bars=2),
                     dict(cap='b) y con la frase que baja',
                          events=[ac(('A2', 'C3', 'A4')), n('G4'), n('F4'), n('E4'),
                                  ac(('D3', 'F3', 'D4'), 'h'), n('E4', 'h')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 24, 'C5', 'C3',
                          'las dos notas de la izquierda entran como un solo golpe',
                          desde=4, time_sig=(4, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
