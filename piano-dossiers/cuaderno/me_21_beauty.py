# -*- coding: utf-8 -*-
"""Beauty and the Beast — pieza 21 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Beauty and Beast",
   arr. Naf, 1 página), leído a 230 dpi:

     - Detrás de la clave hay UN BEMOL: Fa mayor.
     - 4/4, y pone "♩ = 80".
     - Arriba dice "Right hand must play on a superior octave": la derecha
       suena una octava más aguda de lo escrito.
     - La derecha calla dos tiempos y sigue con un grupo de cuatro corcheas.
     - La izquierda toca ACORDES de tres notas en cada negra, todo el compás.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac, sil, corch

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=21, nivel='intermedio', slug='BeautyAndTheBeast',
    formato='adulto',
    titulo_corto='Beauty and the Beast', time_sig=(4, 4), key_sig='Fa mayor',
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source', 'BELLA Y BESTIA .pdf'),
    yt='https://www.youtube.com/results?search_query=beauty+and+the+beast+piano+easy',

    ficha=dict(
        titulo='Beauty and the Beast',
        autor='Alan Menken · arr. Naf',
        datos=[('Tonalidad', 'Fa mayor'), ('Armadura', 'Un bemol'),
               ('Compás', '4/4'), ('Tempo', '♩ = 80'),
               ('Izquierda', 'Acordes de tres')],
        titulo_ritmos='Acordes de tres notas, una vez por tiempo',
        pie_ritmos='Andamio en Fa mayor. Lo literal es el reparto: la izquierda toca un acorde de '
                   'tres notas en cada negra, y la derecha entra tras dos tiempos callados.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('UN BEMOL', 'Fa mayor',
                 'Todos los Si de la pieza son bemoles, en las dos manos. Es tu primera pieza con '
                 'bemol en vez de sostenido.'),
                ('ACORDES DE TRES', 'En cada negra',
                 'La izquierda ya no toca dos notas como en piezas anteriores: aquí son tres, y se '
                 'repiten en cada tiempo del compás.'),
                ('UNA OCTAVA MÁS ARRIBA', 'Que lo escrito',
                 'La partitura avisa: la derecha suena una octava más aguda de lo que está escrito '
                 'en el papel.'),
                ('DOS TIEMPOS CALLADOS', 'Y luego corcheas',
                 'La derecha espera medio compás y entra con un grupo de cuatro corcheas seguidas.'),
            ],
            pie='Es el tema principal de la película de animación de 1991, y aquí en un arreglo que '
                'trabaja los acordes de tres notas en la mano izquierda.',
        ),
        ritmos=[
            ('MANO DERECHA', 'silencio y cuatro corcheas · literal',
             [sil('h')] + corch(['F4', 'G4', 'A4', 'G4']), OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'acorde de tres notas en cada negra · literal',
             [ac(('F2', 'A2', 'C3')), ac(('F2', 'A2', 'C3')),
              ac(('F2', 'A2', 'C3')), ac(('F2', 'A2', 'C3'))], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un bemol: todos los Si son teclas negras.',
            'La tonalidad es Fa mayor.',
            'Compás de 4/4, con "♩ = 80" escrito arriba.',
            'La derecha suena una octava más aguda de lo escrito en el papel.',
            'La derecha calla dos tiempos y entra con cuatro corcheas seguidas.',
            'La izquierda toca un acorde de tres notas en cada negra.',
        ],
        reto='Que las tres notas del acorde de la izquierda suenen siempre juntas y limpias, '
             'repetidas en cada tiempo sin que ningún dedo se retrase.',
        truco='Toca solo el acorde de la izquierda, negra a negra, escuchando después de cada golpe '
              'si las tres notas han sonado como una sola. Cuando eso salga limpio cuatro veces '
              'seguidas, añade la derecha.',
        sabias='Alan Menken ganó el Óscar a la mejor canción original con este tema en 1992, el '
               'mismo año en que la película se convirtió en la primera de animación nominada a '
               'mejor película.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el acompañamiento de la izquierda: son acordes completos repetidos, '
                      'no una melodía. Fíjate en que suenan como un solo bloque, no como notas sueltas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El acorde de tres notas es lo nuevo. Se estudia solo, luego la entrada de la '
              'derecha, y al final las dos juntas.',
        reglas=['LAS TRES NOTAS DEL ACORDE, JUNTAS', 'DOS TIEMPOS CALLADOS Y ENTRAS',
                '♩ = 80: NI RÁPIDO NI ARRASTRADO'],
        bloques=[
            dict(num=1, titulo='La izquierda: el acorde repetido',
                 pista='andamio en Fa mayor · las tres notas bajan con el brazo, no con los dedos',
                 sistemas=[
                     dict(cap='a) el mismo acorde, cuatro veces por compás',
                          events=[ac(('F2', 'A2', 'C3')), ac(('F2', 'A2', 'C3')),
                                  ac(('F2', 'A2', 'C3')), ac(('F2', 'A2', 'C3')),
                                  ac(('Bb2', 'D3', 'F3')), ac(('Bb2', 'D3', 'F3')),
                                  ac(('Bb2', 'D3', 'F3')), ac(('Bb2', 'D3', 'F3'))],
                          bars=2, clef='bass'),
                     dict(cap='b) cambiando de acorde cada compás',
                          events=[ac(('C3', 'E3', 'G3')), ac(('C3', 'E3', 'G3')),
                                  ac(('C3', 'E3', 'G3')), ac(('C3', 'E3', 'G3')),
                                  ac(('F2', 'A2', 'C3')), ac(('F2', 'A2', 'C3')),
                                  ac(('F2', 'A2', 'C3')), ac(('F2', 'A2', 'C3'))],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(num=2, titulo='La derecha: entrar tras el silencio',
                 pista='andamio · dos tiempos callados y un grupo de cuatro corcheas',
                 sistemas=[
                     dict(cap='a) silencio y corcheas, dos veces',
                          events=[sil('h')] + corch(['F4', 'G4', 'A4', 'G4'])
                                 + [sil('h')] + corch(['A4', 'Bb4', 'C5', 'Bb4']),
                          bars=2),
                     dict(cap='b) el mismo dibujo, una tercera más abajo',
                          events=[sil('h')] + corch(['D4', 'E4', 'F4', 'E4'])
                                 + [sil('h')] + corch(['F4', 'G4', 'A4', 'G4']),
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL ACORDE SE TOCA CON EL BRAZO',
                 texto='Tres notas a la vez no se controlan bien moviendo cada dedo por separado: '
                       'el gesto que funciona es soltar el peso del brazo entero sobre las tres '
                       'teclas de golpe, con los dedos ya colocados encima. Practicarlo así, en vez '
                       'de "apretar" con la mano, es lo que evita que una de las tres notas suene '
                       'más floja que las otras.'),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · el acorde marca el pulso bajo el silencio de la derecha · despacio',
                 sistemas=[
                     dict(cap='a) el acorde sigue sonando mientras la derecha calla, y luego entra',
                          events=[ac(('F2', 'A2', 'C3')), ac(('F2', 'A2', 'C3')),
                                  ac(('F2', 'A2', 'C3')), ac(('F2', 'A2', 'C3'))]
                                 + [ac(('F2', 'A2', 'F4')), ac(('F2', 'A2', 'G4')),
                                    ac(('F2', 'A2', 'A4')), ac(('F2', 'A2', 'G4'))],
                          bars=2),
                     dict(cap='b) y con el acorde que cambia',
                          events=[ac(('Bb2', 'D3', 'F3')), ac(('Bb2', 'D3', 'F3')),
                                  ac(('Bb2', 'D3', 'F3')), ac(('Bb2', 'D3', 'F3'))]
                                 + [ac(('Bb2', 'D3', 'A4')), ac(('Bb2', 'D3', 'Bb4')),
                                    ac(('Bb2', 'D3', 'C5')), ac(('Bb2', 'D3', 'Bb4'))],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
