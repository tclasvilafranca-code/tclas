# -*- coding: utf-8 -*-
"""Silent Night, de Gruber — pieza 8 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive (2 páginas, con letra en
   dos idiomas), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 3/4, y arriba pone "Gently". No trae número de metrónomo.
     - Encima del primer compás hay una letra de acorde impresa: **C**.
     - La derecha empieza con negra con puntillo · corchea · negra, y el
       compás siguiente es una blanca con puntillo. Ese ritmo es literal.
     - La izquierda hace NEGRA y BLANCA: cambia en el uno y se queda hasta el
       final del compás.
     - La partitura trae DIGITACIÓN IMPRESA (se ven 3, 5, 1, 2) y la letra
       debajo del pentagrama.

   Es la primera pieza de Luisa donde las dos manos llevan ritmos distintos, y
   por eso la hoja de estudio junta las manos con la derecha simplificada a
   negras antes de poner el ritmo de verdad.
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
    alumno='Luisa', carpeta='Luisa', num=8, nivel='iniciación', slug='SilentNight',
    formato='adulto',
    titulo_corto='Silent Night', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source', 'Silent-Night.easy'),
    yt='https://www.youtube.com/results?search_query=silent+night+easy+piano',

    ficha=dict(
        titulo='Silent Night',
        autor='Franz Xaver Gruber · 1818 · con letra y con los dedos escritos',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'Gently · con calma'), ('Izquierda', 'Negra y blanca'),
               ('Trae', 'Dedos escritos')],
        titulo_ritmos='Cada mano hace una cosa distinta',
        pie_ritmos='El ritmo es el de tu partitura, medido. Las notas exactas están allí. Fíjate en '
                   'que la izquierda cambia una sola vez por compás y la derecha, tres.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('DOS RITMOS A LA VEZ', 'Uno en cada mano',
                 'Hasta ahora las dos manos iban juntas o la izquierda esperaba. Aquí cada una '
                 'lleva su propio ritmo, y ese es todo el trabajo de la semana.'),
                ('LARGO, CORTO, MEDIO', 'La derecha',
                 'Negra con puntillo, corchea y negra. Se cuenta "UUUN, y-dos, tres". El corto va '
                 'pegado al que viene después, no al de antes.'),
                ('LOS DEDOS VIENEN PUESTOS', 'Números impresos',
                 'Tu partitura lleva los números de dedo escritos. No son una sugerencia: son la '
                 'manera de que la mano no tenga que saltar.'),
                ('UNA LETRA ENCIMA', 'La C del principio',
                 'Esa C es el nombre del acorde: Do. Te dice qué notas está sonando debajo, aunque '
                 'tú toques solo dos de ellas.'),
            ],
            pie='Compás de tres, como el vals. Se cuenta uno-dos-tres y el uno pesa más que los '
                'otros dos. Si el uno no pesa, la pieza suena plana.',
        ),
        ritmos=[
            ('MANO DERECHA', 'largo · corto · medio · el ritmo es literal',
             [n('G4', 'q.'), n('A4', 'e'), n('G4'), n('E4', 'h.')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'negra y blanca · el ritmo es literal',
             [n('C3'), n('E3', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: no hay teclas negras fijas.',
            'Compás de 3/4: se cuenta uno-dos-tres, y el uno pesa más.',
            'Arriba pone "Gently", que quiere decir con calma. No trae número de velocidad.',
            'La derecha hace negra con puntillo, corchea y negra.',
            'La izquierda hace negra y blanca: una sola vez por compás.',
            'Los números pequeños encima y debajo de las notas son los dedos.',
        ],
        reto='Que la izquierda no se mueva cuando la derecha hace la nota corta. Es la primera vez '
             'que una mano se mueve sola mientras la otra aguanta.',
        truco='Aguanta la blanca de la izquierda y, sin soltarla, di en voz alta "y-dos" mientras la '
              'derecha hace la nota corta. Lo que se te va a olvidar es soltar la izquierda antes de '
              'tiempo, no tocarla.',
        sabias='Se estrenó en Nochebuena de 1818 en un pueblo de Austria y se tocó con guitarra, no '
               'con órgano. Hay quien dice que el órgano se había estropeado. En 2011 la UNESCO la '
               'declaró patrimonio inmaterial.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate solo en la mano izquierda del acompañamiento: cambia una vez por '
                      'compás, y es lo que le da el balanceo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo es que las dos manos ya no hacen lo mismo. Se separan, se aprenden por '
              'dentro y solo al final se juntan.',
        reglas=['LA IZQUIERDA CAMBIA UNA VEZ POR COMPÁS', 'CUENTA "UN, DOS, TRES" EN VOZ ALTA',
                'JUNTARLAS ES EL ÚLTIMO PASO'],
        bloques=[
            dict(num=1, titulo='La izquierda sola: negra y blanca',
                 pista='andamio en Do mayor · el ritmo es el de tu partitura; las notas, allí',
                 sistemas=[
                     dict(cap='a) toca en el uno y aguanta hasta el final del compás · no levantes '
                              'la mano en el dos',
                          events=[n('C3'), n('E3', 'h'), n('C3'), n('E3', 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de sitio · prepara el dedo antes de que le toque, no '
                              'cuando le toca',
                          events=[n('G2'), n('D3', 'h'), n('F2'), n('C3', 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha sola: largo, corto, medio',
                 pista='andamio · cuenta "UUUN, y-dos, tres" en voz alta mientras tocas',
                 sistemas=[
                     dict(cap='a) el ritmo de la pieza · la nota corta va pegada a la siguiente',
                          events=[n('E4', 'q.'), n('F4', 'e'), n('E4'), n('C4', 'h.')],
                          bars=2),
                     dict(cap='b) el mismo ritmo un poco más arriba · si lo cuentas, sale; si lo '
                              'imitas de oído, no',
                          events=[n('A4', 'q.'), n('B4', 'e'), n('A4'), n('F4', 'h.')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ PRIMERO EN NEGRAS',
                 texto='Juntar dos manos con dos ritmos distintos son dos problemas a la vez. En el '
                       'paso 3 la derecha va en negras a propósito: así las dos manos caen juntas y '
                       'solo tienes que pensar en las teclas. Cuando eso salga sin mirar, pon el '
                       'ritmo de verdad del paso 2. Ese orden es el que ahorra la semana.'),
            dict(num=3, titulo='Las dos juntas, con la derecha en negras',
                 pista='andamio · simplificado a propósito · muy despacio',
                 sistemas=[
                     dict(cap='a) las dos caen en el uno; en el dos y el tres la izquierda aguanta '
                              'y solo se mueve la derecha',
                          events=[ac(('C3', 'G4')), ac(('E3', 'A4')), n('G4'),
                                  ac(('C3', 'E4')), ac(('E3', 'F4')), n('E4')],
                          bars=2),
                     dict(cap='b) y bajando · cuando esto salga tres veces seguidas sin parar, '
                              'vuelve al ritmo del paso 2',
                          events=[ac(('G2', 'D4')), ac(('D3', 'C4')), n('B3'),
                                  ac(('C3', 'C4')), ac(('E3', 'E4')), n('C4')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

_S1, _S2, _S3 = sistemas_extra('Do mayor', 'C4', 'C3', time_sig=(3, 4), variante=20,
                          letras=('c', 'd', 'c', 'd', 'c'))
_PASOS = [b for b in CANCION['piano1']['bloques'] if b.get('num')]
_PASOS[0]['sistemas'] = list(_PASOS[0]['sistemas']) + _S1
if len(_PASOS) > 1:
    _PASOS[1]['sistemas'] = list(_PASOS[1]['sistemas']) + _S2
if len(_PASOS) > 2:
    _PASOS[2]['sistemas'] = list(_PASOS[2]['sistemas']) + _S3

if __name__ == '__main__':
    print('generado', construir(CANCION))
