# -*- coding: utf-8 -*-
"""Sonatina nº 2, de Bazzoni (en Sol mayor) — pieza 11 de Martina (dueto). ADULTO
   exigente, tono de niña.

   Lo comprobado sobre el PDF de su carpeta de Drive ("SONATINA N. 2 - pianoforte a 4
   mani, in sol maggiore - in G Major", M. Bazzoni, 2 páginas, VECTORIAL), mirado a
   300 ppp y a 130 ppp compás a compás:

     - UN SOSTENIDO detrás de la clave (Fa♯): Sol mayor. 4/4. No trae tempo. "f" en la
       parte del alumno (cc. 1 y 17) y "p" en la del maestro. 24 compases.
     - A cuatro manos. El Pianoforte 1 (el alumno) lleva sus dos pentagramas en clave de
       sol, que escriben LO MISMO; el de arriba lleva un 8va encima. El Pianoforte 2, el
       maestro, dos pentagramas en clave de fa.
     - Barras de repetición: al final del c. 8 (se vuelve al c. 1), de |: a :| en los
       cc. 9-16 y de |: a :| en los cc. 17-24.
     - Solo negras y blancas.
     - MEDIDO, parte del alumno (alturas escritas, con el 8va encima):
       c. 1: Sol4 · Re4 · Sol4 · Re4 (negras)     c. 2: Mi4 · La4 · Mi4 · La4
       c. 3: como el c. 1                         c. 4: Fa♯4 · Mi4 (negras) · Re4 (blanca)
       c. 8: Mi4 · Fa♯4 (negras) · Sol4 (blanca)
       c. 9: La4 · Fa♯4 · La4 · Fa♯4             c. 10: Sol4 · Mi4 · Sol4 · Mi4
       c. 11: Fa♯4 · Re4 · Fa♯4 · Re4            c. 12: Mi4 · La4 (negras) · La4 (blanca)
       c. 16: Mi4 · La4 (negras) · Re4 (blanca)
     - El maestro: silencio de negra y acorde de negra, dos veces por compás, y un bajo en
       negras que repite la misma nota.
   Es el mismo archivo que el de Luisa y el de Mercè.
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
SOL = 'Sol mayor'

# MEDIDO: parte del alumno (alturas escritas, con el 8va encima)
C1 = [n('G4'), n('D4'), n('G4'), n('D4')]
C2 = [n('E4'), n('A4'), n('E4'), n('A4')]
C4 = [n('F#4'), n('E4'), n('D4', 'h')]
C8 = [n('E4'), n('F#4'), n('G4', 'h')]
C9 = [n('A4'), n('F#4'), n('A4'), n('F#4')]
C10 = [n('G4'), n('E4'), n('G4'), n('E4')]
C11 = [n('F#4'), n('D4'), n('F#4'), n('D4')]
C12 = [n('E4'), n('A4'), n('A4', 'h')]
C16 = [n('E4'), n('A4'), n('D4', 'h')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=11, nivel='iniciación', slug='SonatinaSolMaggiore',
    formato='adulto',
    titulo_corto='Sonatina nº 2 · Bazzoni', time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'Sonatina-sol-maggiore'),
    yt='https://www.youtube.com/results?search_query=bazzoni+sonatina+sol+maggiore+4+mani',

    ficha=dict(
        titulo='Sonatina nº 2',
        autor='Maurizio Bazzoni · en Sol mayor · a cuatro manos · tu parte es la de arriba',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'),
               ('Carácter', 'f · sin tempo'), ('Manos', 'Las dos igual'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='El c. 1, y lo que hace el maestro',
        pie_ritmos='Arriba, medido sobre tu partitura (con el 8va encima): cuatro negras, Sol, Re, Sol '
                   'y Re. Abajo, andamio: el maestro toca un silencio y un acorde, dos veces.',
        armonia=dict(
            titulo='Como la primera sonatina, pero con un sostenido',
            tarjetas=[
                ('EL SOSTENIDO', 'Fa, tecla negra',
                 'Detrás de la clave hay un sostenido en el Fa: todos los Fa se tocan con la tecla '
                 'negra. Es la gran novedad respecto a la sonatina de La menor.'),
                ('LAS DOS IGUAL', 'Una más grave',
                 'Como antes, tus dos pentagramas dicen lo mismo y la izquierda suena una octava '
                 'más grave. La mano derecha lleva el 8va encima.'),
                ('TRES PARTES', 'Con repeticiones',
                 'Son 24 compases en tres partes de ocho. Cada una acaba en una barra de '
                 'repetición: se toca dos veces. La pieza dura mucho menos de lo que parece.'),
                ('SOLO NEGRAS Y BLANCAS', 'Sin prisa',
                 'No hay corcheas: en tu parte solo hay negras y blancas. El trabajo no es el '
                 'ritmo, es acordarse del Fa sostenido y tocar juntos.'),
            ],
            pie='Es la segunda sonatina de Bazzoni de tu carpeta. Si la primera ya te sale, esta es '
                'la misma idea con una nota nueva: la tecla negra del Fa.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido · con el 8va encima', C1, OCRE, 'treble', SOL),
            ('EL MAESTRO', 'andamio · silencio y acorde, dos veces',
             [sil('q'), ac(('D4', 'G4', 'B4')), sil('q'), ac(('D4', 'G4', 'B4'))], AZUL, 'treble',
             SOL),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: el Fa. Es Sol mayor.',
            'Tus dos pentagramas van en clave de sol, los dos, y dicen lo mismo.',
            'Encima del pentagrama de arriba hay un 8va: suena más agudo de lo que está escrito.',
            'Solo hay negras y blancas, y tres barras de repetición.',
            'Empiezas en f y el maestro en p.',
            'Son 24 compases en tres partes de ocho.',
        ],
        reto='Tocar las dos manos juntas SIN equivocarte con el Fa: el sostenido está en la clave y no '
             'delante de la nota, así que es fácil que se escape. Tres veces seguidas, sin fallar.',
        truco='Antes de empezar, rodea con un lápiz todos los Fa de tu partitura. Tu mano tiene que '
              'saber de antemano dónde está cada tecla negra.',
        sabias='Esta sonatina forma pareja con la de La menor: las dos son del mismo autor y las '
               'dos se tocan con un profesor. Aquí tú cambias de tonalidad sin cambiar de mano.',
        qr=dict(titulo='Escúchala',
                texto='Escucha las dos partes juntas y fíjate en que la parte del maestro marca los '
                      'golpes dos y cuatro. Son los golpes donde no tienes que tocar fuerte.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia igual que la primera sonatina: una mano, la otra y las dos juntas. Lo '
              'nuevo es marcar los Fa antes de tocar.',
        reglas=['EL FA, A LA TECLA NEGRA', 'LAS DOS A LA VEZ, NO UNA DETRÁS DE OTRA',
                'DESPACIO, QUE NO HAY PRISA'],
        bloques=[
            dict(num=1, titulo='El Fa sostenido, aislado',
                 pista='andamio en Sol mayor · una escala corta con el Fa en su sitio',
                 sistemas=[
                     dict(cap='a) bajando desde Re: Re, Do, Si, La, Sol, Fa sostenido, Mi y Re · el Fa es la '
                              'tecla negra, a la derecha del Fa blanco; di su nombre al tocarla',
                          events=[n('D5'), n('C5'), n('B4'), n('A4'),
                                  n('G4'), n('F#4'), n('E4'), n('D4')],
                          bars=2, key_sig=SOL),
                 ]),
            dict(num=2, titulo='Los cuatro primeros compases, tal como están',
                 pista='cc. 1-4 · medidos sobre tu partitura · con el 8va encima',
                 sistemas=[
                     dict(cap='a) Sol-Re-Sol-Re, Mi-La-Mi-La, Sol-Re-Sol-Re y Fa sostenido, Mi, y '
                              'Re de blanca · el único Fa de los cuatro es el del c. 4',
                          events=C1 + C2 + C1 + C4, bars=4, key_sig=SOL, ottava=True, matiz='f'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE MARCAN LOS FA ANTES DE TOCAR',
                 texto='El sostenido de la clave vale para toda la pieza, pero es fácil olvidarlo '
                       'porque no vuelve a aparecer delante de cada Fa. Si rodeas los Fa con '
                       'lápiz, tu ojo los ve antes de que llegue la mano.'),
            dict(num=3, titulo='Las dos blancas de cierre, cc. 8 y 12',
                 pista='cc. 8 y 12 · medidos sobre tu partitura · la blanca dura dos golpes',
                 sistemas=[
                     dict(cap='a) Mi, Fa sostenido y Sol de blanca · y Mi, La y La de blanca · '
                              'aguanta la blanca entera: cuenta "tres, cuatro"',
                          events=C8 + C12, bars=2, key_sig=SOL, ottava=True),
                 ]),
            dict(num=4, titulo='La parte del centro: tres compases que bajan, cc. 9-11',
                 pista='cc. 9-11 · medidos sobre tu partitura · el dibujo repetido sobre notas '
                       'cada vez más graves',
                 sistemas=[
                     dict(cap='a) La-Fa♯-La-Fa♯, Sol-Mi-Sol-Mi y Fa♯-Re-Fa♯-Re · el mismo dibujo '
                              'bajando un escalón cada compás',
                          events=C9 + C10 + C11, bars=3, key_sig=SOL, ottava=True),
                 ]),
            dict(num=5, titulo='Y ahora las dos manos juntas',
                 pista='andamio · muy despacio · si oyes dos golpecitos, ve más lento',
                 sistemas=[
                     dict(cap='a) las dos manos, a la vez · la derecha una octava más arriba que la '
                              'izquierda · un solo sonido, no dos',
                          events=[ac(('G3', 'G4')), ac(('D3', 'D4')), ac(('G3', 'G4')),
                                  ac(('D3', 'D4')), ac(('G3', 'B3'), 'h'), ac(('G3', 'G4'), 'h')],
                          bars=2, key_sig=SOL, manos='dobla'),
                 ]),
        ] + bloques_extra(SOL, 11, 'G4', 'G2',
                          'las dos manos juntas y el Fa sostenido sin olvidarlo',
                          desde=6, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Sonatina nº 2 · para casa',
            intro='Quince minutos al día. Esta semana lo importante es que no se te escape ningún '
                  'Fa, y que las dos manos suenen como una.',
            bloques=[
                reto('Tocar los cc. 1-8 con las dos manos a la vez y sin ningún Fa blanco, tres '
                     'veces seguidas.',
                     'Rodea los Fa con lápiz y toca despacio. Si una vez tocas un Fa blanco, '
                     'vuelves a cero: tres limpias seguidas, no tres en total.'),
                plan((3, 'Marcar todos los Fa de la partitura con un círculo de lápiz'),
                     (4, 'La mano derecha sola, cc. 1-8, diciendo las notas en voz alta'),
                     (4, 'La mano izquierda sola, la misma música'),
                     (4, 'Las dos juntas, un compás cada vez, y después con el maestro')),
                a_cuatro_manos('Acordad quién cuenta "un, dos, tres, cuatro" para empezar, a qué '
                               'velocidad vais y cuántas veces repetís cada parte. Hay tres '
                               'barras de repetición: decidid antes de tocar si las hacéis.'),
                ordenar(['Tocar los cc. 1-8 con las dos manos juntas.',
                         'Rodear con lápiz todos los Fa de la partitura.',
                         'Tocar los cc. 1-8 solo con la mano derecha.',
                         'Tocar los cc. 1-8 solo con la mano izquierda.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='del más fácil al más completo · uno de ellos va antes de tocar nada'),
                nombres(['G4', 'D4', 'E4', 'A4', 'F#4'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='son las cinco notas de los primeros compases · la última es el Fa '
                              'sostenido'),
                figuras([('q', 'negra'), ('h', 'blanca'), ('w', 'redonda'), ('e', 'corchea')],
                        titulo='¿Cuántos golpes dura cada figura?',
                        pista='escribe el número en la caja · en 4/4 un compás son cuatro golpes'),
                para_clase('Los cc. 1-8 con las dos manos, y dónde se te escapa el Fa. Si hay un '
                           'sitio donde siempre falla, dime cuál y empezamos por ahí.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
