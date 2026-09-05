# -*- coding: utf-8 -*-
"""Spring, de Vivaldi (edición con acordes) — pieza 15 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("'Spring' from the Four
   Seasons", Antonio Vivaldi, 1 página), leído a 230 dpi. Es una edición
   DISTINTA a la de Luisa: aquí la derecha toca INTERVALOS DOBLES repetidos,
   no una melodía de una sola voz.

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4, y pone "Allegro" y "f".
     - La derecha repite un intervalo de dos notas en negras (con dedos 1 y 3
       alternando) y cierra la frase con una nota larga y dos corcheas.
     - La izquierda hace dos blancas por compás.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from me_comun import n, ac, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=15, nivel='intermedio', slug='Spring',
    formato='adulto',
    titulo_corto='Spring · La primavera', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'LAS CUATRO ESTACIONES.pdf'),
    yt='https://www.youtube.com/results?search_query=vivaldi+spring+piano+intermediate',

    ficha=dict(
        titulo='Spring · La primavera',
        autor='Antonio Vivaldi · de Las cuatro estaciones',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Allegro'), ('Derecha', 'Intervalos dobles'),
               ('Izquierda', 'Dos blancas')],
        titulo_ritmos='Un intervalo que se repite, con dos dedos',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la derecha repite un intervalo '
                   'de dos notas en negras y la izquierda hace dos blancas por compás.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('DOS NOTAS A LA VEZ', 'Repetidas',
                 'La derecha no toca una melodía de una sola voz: repite un intervalo de dos notas, '
                 'como un tremolo lento, con los dedos 1 y 3.'),
                ('DOS DEDOS FIJOS', 'La mano no viaja',
                 'Mientras se repite el intervalo, la mano no se mueve de sitio: solo bajan y suben '
                 'los mismos dos dedos.'),
                ('LA FRASE SE CIERRA', 'Larga y dos cortas',
                 'Cada grupo de intervalos repetidos acaba con un gesto distinto: una nota que dura '
                 'y dos corcheas que resuelven.'),
                ('ALLEGRO Y f', 'Vivo y con fuerza',
                 'A diferencia de otras piezas tranquilas de tu cuaderno, esta pide energía desde '
                 'la primera nota.'),
            ],
            pie='Es una edición distinta a la que suele verse de esta pieza: en vez de la melodía '
                'sola, trabaja el intervalo repetido, una textura muy propia del violín original.',
        ),
        ritmos=[
            ('MANO DERECHA', 'intervalo repetido y cierre de frase · andamio',
             [ac(('C4', 'E4')), ac(('C4', 'E4')), ac(('C4', 'E4')), ac(('C4', 'E4'))],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos blancas por compás · andamio',
             [n('C3', 'h'), n('G3', 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, con "Allegro" y "f" escritos arriba.',
            'La derecha repite un intervalo de dos notas en negras.',
            'La frase se cierra con una nota larga y dos corcheas.',
            'La izquierda hace dos blancas por compás.',
            'El carácter pide energía: se toca vivo y con fuerza, no despacio.',
        ],
        reto='Que las dos notas del intervalo suenen siempre exactamente a la vez, repetidas cuatro '
             'veces seguidas sin que ninguna se adelante ni se atrase.',
        truco='Toca el intervalo cuatro veces seguidas muy despacio, escuchando después de cada '
              'golpe si ha sonado limpio o doble. Sube la velocidad solo cuando las cuatro repeticiones '
              'salgan igual de limpias.',
        sabias='Vivaldi publicó Las cuatro estaciones en 1725 junto con un poema para cada una, '
               'probablemente escrito por él mismo. La primavera arranca describiendo el canto de '
               'los pájaros que regresan.',
        qr=dict(titulo='Escúchala',
                texto='Escucha la versión de orquesta y busca el intervalo repetido en los '
                      'violines: ese temblor rápido es lo que tu mano derecha imita en negras.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo es repetir un intervalo con los mismos dos dedos, sin que la mano se mueva '
              'de sitio. Se aprende sola antes de juntarla con la izquierda.',
        reglas=['LOS DOS DEDOS NO CAMBIAN DE SITIO', 'LAS DOS NOTAS, SIEMPRE JUNTAS',
                'ALLEGRO: VIVO, NO ATROPELLADO'],
        bloques=[
            dict(num=1, titulo='La derecha: el intervalo repetido',
                 pista='andamio en Do mayor · la mano no cambia de postura',
                 sistemas=[
                     dict(cap='a) cuatro repeticiones y el cierre con nota larga y dos corcheas',
                          events=[ac(('C4', 'E4')), ac(('C4', 'E4')), ac(('C4', 'E4')), ac(('C4', 'E4')),
                                  ac(('D4', 'F4'), 'h.')] + corch(['E4', 'D4']),
                          bars=2),
                     dict(cap='b) el mismo dibujo con otro intervalo',
                          events=[ac(('E4', 'G4')), ac(('E4', 'G4')), ac(('E4', 'G4')), ac(('E4', 'G4')),
                                  ac(('F4', 'A4'), 'h.')] + corch(['G4', 'F4']),
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La izquierda: dos blancas por compás',
                 pista='andamio · una nota, la otra, y vuelta a empezar',
                 sistemas=[
                     dict(cap='a) el pulso de fondo, sin melodía',
                          events=[n('C3', 'h'), n('G2', 'h'), n('F2', 'h'), n('C3', 'h')],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de acorde cada compás',
                          events=[n('G2', 'h'), n('D3', 'h'), n('C3', 'h'), n('G2', 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL INTERVALO SE ESTUDIA SOLO Y DESPACIO',
                 texto='Un intervalo repetido suena limpio o suena doble, y a velocidad normal el '
                       'oído no siempre distingue cuál de las dos cosas está pasando. Tocarlo muy '
                       'despacio, escuchando cada repetición por separado, es la única manera de '
                       'saber con certeza si los dos dedos bajan juntos. Cuando eso esté seguro, la '
                       'velocidad se puede subir sin miedo.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · la izquierda no cambia mientras se repite el intervalo · despacio',
                 sistemas=[
                     dict(cap='a) el intervalo repetido encima de las dos blancas',
                          events=[ac(('C3', 'C4', 'E4')), ac(('C4', 'E4')), ac(('C4', 'E4')),
                                  ac(('G2', 'C4', 'E4')),
                                  ac(('F2', 'D4', 'F4'), 'h.')] + corch(['E4', 'D4']),
                          bars=2),
                     dict(cap='b) y con el cierre de frase',
                          events=[ac(('C3', 'E4', 'G4')), ac(('E4', 'G4')), ac(('E4', 'G4')),
                                  ac(('G2', 'E4', 'G4')),
                                  ac(('C3', 'F4', 'A4'), 'h.')] + corch(['G4', 'F4']),
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 62, 'C4', 'C3',
                          'se entra en el cuarto tiempo, ni antes ni después',
                          desde=4, time_sig=(4, 4)),
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
