# -*- coding: utf-8 -*-
"""Sonatina per bambini, de Bazzoni — pieza 1 de Martina (dueto). ADULTO exigente,
   tono de niña que empieza de cero.

   Lo comprobado sobre el PDF de su carpeta de Drive (M. Bazzoni, "Sonatina per
   bambini - Sonatina for children", In la minore, 2 páginas, VECTORIAL), medido a
   300 ppp contra las líneas del pentagrama:

     - Detrás de la clave no hay nada: La menor. 4/4. No trae tempo. "f" en la parte
       del alumno y "p" en la del maestro. 16 compases.
     - A cuatro manos. La parte del alumno ("Bambini / Children 1") lleva sus dos
       pentagramas en clave de sol y escriben LO MISMO; el de arriba lleva un 8va
       encima en las dos páginas. El maestro, dos pentagramas en clave de fa.
     - Barra de repetición al final del c. 8 (se vuelve al c. 1) y al final del c. 16
       (se vuelve al c. 9).
     - Negras, blancas y, en los cc. 9, 10, 13, 14 y 15, parejas de corcheas.
     - MEDIDO, parte del alumno (alturas tal como están escritas, con el 8va):
       c. 1: La4 · Do5 · La4 · Do5        c. 2: Si4 · Re5 · Si4 · Re5
       c. 3: Do5 · Mi5 · Do5 · La4        c. 4: Si4 · Mi5 (negras) · Mi5 (blanca)
       c. 8: Si4 · Mi5 (negras) · La4 (blanca)
       c. 9: Si4 (negra) · Si4 · Do5 (corcheas) · Re5 (blanca)
       c. 10: Do5 (negra) · Do5 · Re5 (corcheas) · Mi5 (blanca)
       c. 11: Si4 · Mi5 · Si4 · Re5    c. 12: Do5 · Si4 · Do5 · La4 (negras)
       c. 15: Si4 · Mi5 (negras) · Mi5 · Re5 · Do5 · Si4 (corcheas)
       c. 16: La4 · Do5 (negras) · La4 (blanca)
     - El maestro: silencio de negra y acorde de negra, dos veces por compás, en los
       cc. 1-8; después, acordes de negra sobre un bajo que repite la misma nota.
   OJO: la pieza 1 de Luisa y la de Mercè dicen que solo hay negras y blancas;
   en los cc. 9, 10, 13, 14 y 15 hay corcheas.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, reto, plan, a_cuatro_manos, ordenar, nombres,
                      figuras, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: parte del alumno, cc. 1-4 y 8-16 (alturas escritas, con el 8va encima)
C1 = [n('A4'), n('C5'), n('A4'), n('C5')]
C2 = [n('B4'), n('D5'), n('B4'), n('D5')]
C3 = [n('C5'), n('E5'), n('C5'), n('A4')]
C4 = [n('B4'), n('E5'), n('E5', 'h')]
C8 = [n('B4'), n('E5'), n('A4', 'h')]
C9 = [n('B4'), n('B4', 'e'), n('C5', 'e'), n('D5', 'h')]
C10 = [n('C5'), n('C5', 'e'), n('D5', 'e'), n('E5', 'h')]
C11 = [n('B4'), n('E5'), n('B4'), n('D5')]
C12 = [n('C5'), n('B4'), n('C5'), n('A4')]
C15 = [n('B4'), n('E5'), n('E5', 'e'), n('D5', 'e'), n('C5', 'e'), n('B4', 'e')]
C16 = [n('A4'), n('C5'), n('A4', 'h')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=1, nivel='iniciación', slug='SonatinaBambini',
    formato='adulto',
    titulo_corto='Sonatina per bambini', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'sonatina-per-bambini'),
    yt='https://www.youtube.com/results?search_query=bazzoni+sonatina+per+bambini+4+mani',

    ficha=dict(
        titulo='Sonatina per bambini',
        autor='Maurizio Bazzoni · a cuatro manos · tu parte es la de arriba',
        datos=[('Tonalidad', 'La menor'), ('Compás', '4/4'),
               ('Carácter', 'f · sin tempo'), ('Manos', 'Las dos igual'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='El c. 1, y lo que hace el maestro',
        pie_ritmos='Arriba, medido sobre tu partitura: el c. 1 son cuatro negras, La, Do, La, Do. '
                   'Abajo, andamio: el maestro toca un silencio y un acorde, dos veces por compás.',
        armonia=dict(
            titulo='La primera: cinco notas, dos manos y alguien tocando contigo',
            tarjetas=[
                ('EL PENTAGRAMA', 'Cinco rayas',
                 'La música se escribe sobre cinco líneas. Cada nota ocupa una línea o un espacio, y '
                 'según dónde esté, se llama La, Si, Do, Re o Mi.'),
                ('LAS DOS IGUAL', 'Una más grave',
                 'Tus dos pentagramas dicen lo mismo: lo que toca una mano lo toca la otra. Solo '
                 'que la izquierda suena más grave que la derecha.'),
                ('EL 4/4', 'Cuatro golpes',
                 'En cada compás caben cuatro golpes, como cuatro pasos. La negra dura un golpe, la '
                 'blanca dura dos, y el 4/4 es el número de golpes que se cuenta.'),
                ('LA REPETICIÓN', 'Dos barras',
                 'Los dos puntos de la barra gruesa dicen "vuelve". Al final del c. 8 se vuelve al '
                 'principio, y al final del c. 16, al c. 9.'),
            ],
            pie='Es la pieza más fácil de tu carpeta, y no es un ejercicio: es música de verdad, '
                'escrita para tocar con alguien desde el primer día.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido · con el 8va encima', C1, OCRE, 'treble', None),
            ('EL MAESTRO', 'andamio · silencio y acorde, dos veces',
             [sil('q'), ac(('A3', 'C4', 'E4')), sil('q'), ac(('A3', 'C4', 'E4'))], AZUL, 'treble',
             None),
        ],
        especial=[
            'Detrás de la clave no hay nada: no hay teclas negras que recordar.',
            'Tus dos pentagramas van en clave de sol, los dos, y dicen lo mismo.',
            'Encima del pentagrama de arriba hay un 8va: suena más agudo de lo que está escrito.',
            'Hay negras, blancas y, en el centro de la pieza, parejas de corcheas.',
            'Hay dos barras de repetición: una en el c. 8 y otra en el c. 16.',
            'La parte del maestro la toca otra persona; empieza en p y tú en f.',
        ],
        reto='Que las dos manos bajen a la vez. Como tocan lo mismo, si una llega un poquito antes, '
             'se oyen dos golpes en vez de uno, y se nota enseguida.',
        truco='Toca primero solo la mano derecha, hasta que salga sin pensar. Después pon la '
              'izquierda sobre sus teclas SIN tocar, y vuelve a tocar la derecha. Solo entonces '
              'bájalas juntas.',
        sabias='Bazzoni escribió estas sonatinas para que un alumno pueda tocar con su profesor '
               'desde el primer día. La parte fácil no suena a ejercicio porque no lo es: es una de '
               'las dos mitades de una pieza entera.',
        qr=dict(titulo='Escúchala',
                texto='Escucha las dos partes juntas. La tuya es la sencilla, y aun así es la que '
                      'lleva la melodía.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Tres pasos, y en este orden: una mano, la otra, y las dos juntas. El segundo parece '
              'tonto y es el que hace que el tercero salga.',
        reglas=['UNA MANO PRIMERO', 'LAS DOS A LA VEZ, NO UNA DETRÁS DE OTRA',
                'DESPACIO, QUE NO HAY PRISA'],
        bloques=[
            dict(num=1, titulo='Las cinco notas de tu partitura',
                 pista='andamio en La menor · son las cinco notas que aparecen en tu partitura: La, '
                       'Si, Do, Re y Mi',
                 sistemas=[
                     dict(cap='a) La, Si, Do, Re, y la subida hasta Mi · cada una dura un golpe; '
                              'di su nombre en voz alta al tocarla',
                          events=[n('A4'), n('B4'), n('C5'), n('D5'),
                                  n('E5'), n('D5'), n('C5'), n('B4')],
                          bars=2),
                     dict(cap='b) y bajando, con una blanca para respirar · la blanca dura dos golpes',
                          events=[n('E5'), n('D5'), n('C5'), n('B4'), n('A4', 'h'), n('A4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='Los cuatro primeros compases, tal como están',
                 pista='cc. 1-4 · medidos sobre tu partitura · con el 8va encima',
                 sistemas=[
                     dict(cap='a) La-Do-La-Do, Si-Re-Si-Re, Do-Mi-Do-La y Si-Mi con una blanca · '
                              'son cuatro compases iguales de largos',
                          events=C1 + C2 + C3 + C4, bars=4, ottava=True, matiz='f'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ UNA MANO PRIMERO',
                 texto='Casi todo lo que sale mal al empezar sale mal por hacer dos cosas a la vez. '
                       'Con una mano sola solo hay que pensar en las notas; con las dos, además hay '
                       'que juntarlas. Son dos trabajos, y se hacen de uno en uno.'),
            dict(num=3, titulo='Las blancas del final de cada frase, cc. 8 y 16',
                 pista='cc. 8 y 16 · medidos sobre tu partitura · la blanca dura dos golpes',
                 sistemas=[
                     dict(cap='a) dos negras y una blanca · aguanta la blanca entera: cuenta "tres, '
                              'cuatro" con la tecla bajada',
                          events=C8 + C16, bars=2, ottava=True),
                 ]),
            dict(num=4, titulo='Las corcheas del centro, cc. 9 y 10',
                 pista='cc. 9-10 · medidos sobre tu partitura · dos corcheas caben en un solo golpe',
                 sistemas=[
                     dict(cap='a) una negra, dos corcheas y una blanca, dos veces · las dos '
                              'corcheas se tocan juntas, rápidas, dentro del mismo golpe',
                          events=C9 + C10, bars=2, ottava=True),
                 ]),
            dict(num=5, titulo='La carrera del c. 15',
                 pista='c. 15 · medido sobre tu partitura · cuatro corcheas seguidas bajando',
                 sistemas=[
                     dict(cap='a) dos negras y cuatro corcheas bajando: Mi, Re, Do, Si · cuenta '
                              '"tres-y, cuatro-y" en las corcheas',
                          events=C15, bars=1, ottava=True),
                 ]),
            dict(num=6, titulo='Y ahora las dos manos juntas',
                 pista='andamio · muy despacio · si oyes dos golpecitos, ve más lento',
                 sistemas=[
                     dict(cap='a) las dos manos, a la vez · la derecha tres notas más arriba que la '
                              'izquierda · un solo sonido, no dos',
                          events=[ac(('A3', 'A4')), ac(('B3', 'B4')), ac(('C4', 'C5')),
                                  ac(('B3', 'B4')), ac(('A3', 'A4'), 'h'), ac(('A3', 'A4'), 'h')],
                          bars=2, manos='dobla'),
                 ]),
        ] + bloques_extra('La menor', 1, 'A4', 'A2',
                          'las dos manos juntas, sin que una llegue antes que la otra',
                          desde=7, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Sonatina per bambini · para casa',
            intro='Quince minutos al día. Hoy lo importante es que las dos manos suenen como una '
                  'sola, y eso se consigue despacio.',
            bloques=[
                reto('Tocar los cc. 1-8 con las dos manos exactamente a la vez, tres veces seguidas, '
                     'sin parar.',
                     'Cuenta "un, dos, tres, cuatro" en voz alta y apunta cuántas veces seguidas te '
                     'sale. Si una vez una mano llega antes, vuelves a cero.'),
                plan((4, 'La mano derecha sola, cc. 1-8, diciendo las notas en voz alta'),
                     (4, 'La mano izquierda sola, la misma música'),
                     (4, 'Las dos juntas, un compás cada vez, muy despacio'),
                     (3, 'Con tu profesora: tú la melodía y ella los acordes')),
                a_cuatro_manos('Antes de tocar, acordad tres cosas: quién cuenta "un, dos, tres, '
                               'cuatro" para empezar, a qué velocidad vais y quién avisa si hay que '
                               'repetir. Se decide en voz alta antes de tocar, no a mitad.'),
                ordenar(['Tocar los cc. 1-8 con las dos manos juntas.',
                         'Tocar los cc. 1-8 solo con la mano derecha.',
                         'Decir en voz alta los nombres de las notas del c. 1.',
                         'Tocar los cc. 1-8 solo con la mano izquierda.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='del más fácil al más completo · uno de ellos va antes de tocar nada'),
                nombres(['A4', 'B4', 'C5', 'D5', 'E5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='son las cinco notas de tu partitura · escribe su nombre debajo'),
                figuras([('q', 'negra'), ('h', 'blanca'), ('e', 'corchea'), ('w', 'redonda')],
                        titulo='¿Cuántos golpes dura cada figura?',
                        pista='escribe el número en la caja · en 4/4 un compás son cuatro golpes'),
                para_clase('Los cc. 1-8 con las dos manos, y cuántas veces seguidas te han salido '
                           'a la vez. Si alguna vez una mano llega antes, dime cuál: es la que '
                           'vamos a entrenar.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
