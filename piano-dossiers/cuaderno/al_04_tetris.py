# -*- coding: utf-8 -*-
"""Tetris (Korobeiniki) — pieza 4 de Alan. ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Tetris Theme
   (Korobeniki)", 3 páginas, imagen a 52 ppp con el pentagrama muy claro), mirado
   a 200-250 ppp:

     - Detrás de la clave no hay nada. 4/4. No trae tempo ni indicaciones de intensidad.
     - La izquierda toca CORCHEAS sin parar: una nota grave y su octava
       alternando, ocho por compás.
     - MEDIDO, mano derecha:
       c. 1: Mi5 (negra) · Si4 · Do5 (corcheas) · Re5 (negra) · Do5 · Si4 (corcheas)
       c. 2: La4 (negra) · La4 · Do5 (corcheas) · Mi5 (negra) · Re5 · Do5 (corcheas)
       c. 3: Si4 (negra con puntillo) · Do5 (corchea) · Re5 (negra) · Mi5 (negra)
       c. 4: Do5 · La4 · La4 (negras) y silencio de negra
     - No lleva semicorcheas: negras, corcheas, negras con puntillo, blancas y
       redondas.
   La izquierda se da como andamio: la imagen es de poca resolución y no se
   distingue a ojo qué octava toca cada nota.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, plan, metronomo, ordenar, contar, teclado,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: cc. 1-4 (derecha)
C1 = [n('E5'), n('B4', 'e'), n('C5', 'e'), n('D5'), n('C5', 'e'), n('B4', 'e')]
C2 = [n('A4'), n('A4', 'e'), n('C5', 'e'), n('E5'), n('D5', 'e'), n('C5', 'e')]
C3 = [n('B4', 'q.'), n('C5', 'e'), n('D5'), n('E5')]
C4 = [n('C5'), n('A4'), n('A4'), sil('q')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=4, nivel='intermedio', slug='Tetris',
    formato='adulto',
    titulo_corto='Tetris · Korobeiniki', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'TETRIX.'),
    yt='https://www.youtube.com/results?search_query=tetris+theme+piano+tutorial',

    ficha=dict(
        titulo='Tetris',
        autor='Korobeiniki · canción popular rusa · tema de Tetris',
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Izquierda', 'Corcheas'),
               ('Páginas', 'Tres')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: la melodía que todo el mundo reconoce. Abajo, '
                   'andamio: la izquierda toca corcheas sin parar, una nota grave y su octava.',
        armonia=dict(
            titulo='Una melodía que sube y baja, y una izquierda que no para',
            tarjetas=[
                ('LA MELODÍA', 'Mi, Si, Do, Re',
                 'Los cuatro primeros compases son la melodía del juego: Mi, Si, Do, Re, Do, Si, '
                 'La… Salta de una nota larga a dos cortas y vuelve, como una pieza que cae.'),
                ('LA IZQUIERDA', 'Ocho corcheas',
                 'La mano de abajo no descansa: una nota grave y su octava, una y otra vez. Es '
                 'mucho más difícil mantenerla pareja que tocar la melodía.'),
                ('LOS RITMOS', 'Largo-corto',
                 'Hay negras, parejas de corcheas y, en el c. 3, una negra con puntillo seguida de '
                 'una corchea: el gesto de "largo-corto".'),
                ('SIN ARMADURA', 'Pero con alteraciones',
                 'Detrás de la clave no hay nada, y más adelante aparece algún sostenido escrito '
                 'delante de la nota. Mira dónde antes de tocar.'),
            ],
            pie='La pieza son tres páginas de la misma idea contada con variaciones. Si la primera '
                'página sale redonda, el resto es repetirla con otras notas.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1 y 2 · medido', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · una nota y su octava, en corcheas',
             [n('E2', 'e'), n('E3', 'e'), n('E2', 'e'), n('E3', 'e'),
              n('E2', 'e'), n('E3', 'e'), n('E2', 'e'), n('E3', 'e')],
             AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, y no trae número de metrónomo.',
            'El compás es 4/4.',
            'La izquierda toca corcheas sin parar, ocho por compás.',
            'La derecha mezcla negras, corcheas y una negra con puntillo.',
            'No lleva semicorcheas.',
            'Son tres páginas de la misma melodía con variaciones.',
        ],
        reto='Mantener la izquierda pareja mientras la derecha cambia de ritmo. Si la izquierda se '
             'acelera cuando la derecha tiene corcheas, el juego se pierde.',
        truco='Toca la izquierda sola hasta que puedas hablar mientras tocas. Cuando puedas '
              'contar cosas sin equivocarte, ponle la derecha encima.',
        sabias='La melodía se llama Korobeiniki y es una canción popular rusa que cuenta la historia '
               'de un vendedor ambulante. El juego Tetris, creado por Alexey Pajitnov en 1984, '
               'la hizo famosa en todo el mundo cuando salió para la Game Boy.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo la melodía baja y sube con calma mientras el fondo corre. '
                      'Eso es lo que hay que conseguir: arriba tranquilo, abajo sin parar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia la izquierda sola hasta que sea automática, y después se le pone la '
              'derecha. La melodía son cuatro compases que se repiten: aprendida la primera '
              'vez, ya la sabes toda.',
        reglas=['LA IZQUIERDA, PRIMERO', 'CUATRO COMPASES QUE SE REPITEN', 'EL LARGO-CORTO DEL C. 3'],
        bloques=[
            dict(num=1, titulo='La célula del c. 1',
                 pista='c. 1 · medido sobre tu partitura · una negra, dos corcheas, una negra y '
                       'otras dos corcheas',
                 sistemas=[
                     dict(cap='a) el compás de la melodía: Mi, Si, Do, Re, Do, Si · cuenta '
                              '1-2-y-3-4-y-... y marca cada golpe con el pie',
                          events=C1, bars=1),
                     dict(cap='b) el mismo ritmo sobre una sola nota · andamio, para aprender el '
                              'ritmo sin pensar en las notas',
                          events=[n('G4'), n('G4', 'e'), n('G4', 'e'), n('G4'), n('G4', 'e'),
                                  n('G4', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='El c. 3 y el c. 4: el largo-corto y el silencio',
                 pista='cc. 3-4 · medidos sobre tu partitura · una negra con puntillo, una corchea '
                       'y un compás que acaba en silencio',
                 sistemas=[
                     dict(cap='a) la negra con puntillo dura una negra y media, y la corchea que '
                              'viene después completa el tiempo · el silencio del c. 4 se cuenta',
                          events=C3 + C4, bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA IZQUIERDA VA PRIMERO',
                 texto='Ocho corcheas seguidas por compás son un esfuerzo de resistencia, no de '
                       'lectura. Si empiezas por la derecha, la izquierda se te acelera en cuanto '
                       'la derecha se complica. Al revés, la derecha se acopla a la izquierda: la '
                       'izquierda manda y la derecha canta por encima.'),
            dict(num=3, titulo='La izquierda: una nota y su octava',
                 pista='andamio sobre el estilo de tu partitura · la mano no se cierra entre '
                       'una nota y otra',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) un compás de octavas alternando · el dedo 5 baja y el 1 sube, '
                              'sin mover la mano de sitio',
                          events=[n('A2', 'e'), n('A3', 'e')] * 4,
                          bars=1, clef='bass'),
                     dict(cap='b) el mismo compás en la nota siguiente · andamio · el cambio de '
                              'nota no cambia la forma de la mano',
                          events=[n('G#2', 'e'), n('G#3', 'e')] * 4,
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(num=4, titulo='Las corcheas, de dos en dos',
                 pista='andamio sobre el c. 2 · el ritmo de dos corcheas dentro de un tiempo',
                 sistemas=[
                     dict(cap='a) dos corcheas valen una negra · se tocan en el mismo tiempo, no '
                              'una detrás de otra',
                          events=[n('C5'), n('D5', 'e'), n('E5', 'e'), n('D5'),
                                  n('C5', 'e'), n('B4', 'e')],
                          bars=1),
                 ]),
        ] + bloques_extra('Do mayor', 4, 'E4', 'C3',
                          'la izquierda sin parar mientras la derecha cambia de ritmo',
                          desde=5, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Tetris · para casa',
            intro='Veinte minutos al día. La melodía es lo fácil: lo difícil es que la izquierda no '
                  'se desmande.',
            bloques=[
                plan((6, 'La izquierda sola, las octavas en corcheas, sin mirar'),
                     (4, 'La melodía sola, cc. 1-4'),
                     (5, 'Las dos manos, un compás cada vez'),
                     (5, 'Los cc. 1-8 seguidos con el metrónomo')),
                metronomo('Empieza a ♩ = 60 con la izquierda sola y sube de cuatro en cuatro hasta '
                          'que la melodía te salga sin pensar.',
                          'Tu partitura no trae tempo: la meta la eliges tú y la apuntas a lápiz.',
                          titulo='A qué velocidad te sale'),
                ordenar(['Tocar los cc. 1-4 con las dos manos.',
                         'Tocar la izquierda sola, solo el c. 1.',
                         'Tocar la derecha sola, cc. 1-4.',
                         'Tocar la izquierda sola, cc. 1-4.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='del más fácil al más completo · uno va antes de tocar nada'),
                contar([n('B4', 'q.'), n('C5', 'e'), n('D5'), n('E5'),
                        n('C5'), n('A4'), n('A4'), sil('q')],
                       ['¿Cuántas negras hay?', '¿Cuántas corcheas hay?',
                        '¿Cuántos silencios hay?'],
                       titulo='Cuenta sobre los cc. 3 y 4',
                       pista='son dos compases de la derecha de tu partitura'),
                teclado({9: 1, 6: 2, 7: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         'La número 1 es el Mi, la nota con la que empieza el tema.'],
                        titulo='En el teclado',
                        pista='son las tres primeras notas distintas de la melodía'),
                para_clase('Los cc. 1-4 con las dos manos sin parar, y si la izquierda se te acelera '
                           'cuando entra la derecha. Si te pasa, tráelo: se arregla con el '
                           'metrónomo.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
