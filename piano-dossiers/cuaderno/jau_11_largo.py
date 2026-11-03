# -*- coding: utf-8 -*-
"""Largo, de la Sinfonía del Nuevo Mundo (Dvořák) — pieza 11 de Jaume. ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Ana Cristina
   Escobés, elcuartodelpiano.com, 1 página, vectorial, 22 compases; el mismo
   archivo que el de Arnau), mirado a 110 dpi y medido cabeza a cabeza con
   `cabezas` a 250 dpi:

     - Detrás de la clave no hay nada: Do mayor. 4/4 y "Largo". No trae número
       de metrónomo.
     - Dinámica por bloques: **p** al empezar y en el c. 13, **mf** en el c. 9,
       **cresc.** desde el c. 17, **f** en el c. 19 y **mp** en el c. 21.
     - Barra de repetición de los cc. 9 a 12.
     - Ligaduras de frase en casi todos los compases.
     - MEDIDO: la derecha de los cc. 1-4 es **Mi4 negra con puntillo · Sol4 corchea
       · Sol4 blanca | Mi4 negra con puntillo · Re4 corchea · Do4 blanca | Re4
       negra con puntillo · Mi4 corchea · Sol4 negra con puntillo · Mi4 corchea |
       Re4 redonda**.
     - MEDIDO en el c. 11: la derecha es La4 · Do5 · Si4 · Sol4 (negras) y la
       izquierda **Fa3 · La3 · Sol3 · Mi3** (negras).
     - Los cc. 9-12 de la derecha: La4 negra con puntillo · Do5 corchea · Do5
       blanca | Si4 · Sol4 negras · La4 blanca | La4 · Do5 · Si4 · Sol4 negras |
       La4 redonda.

   Mismo archivo que el de Arnau (otro formato): lo literal coincide y lo
   inventado no. Aquí el trabajo va por la **dinámica en bloques** y por la
   **línea larga** del c. 9 al c. 12, que es la que lleva la repetición.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, plan, metronomo, nombres, colorear, diferencias,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

D_1_4 = [dict(pitch='E4', dur='q.', lig=2), n('G4', 'e'), n('G4', 'h'),
         n('E4', 'q.'), n('D4', 'e'), n('C4', 'h'),
         n('D4', 'q.'), n('E4', 'e'), n('G4', 'q.'), n('E4', 'e'),
         n('D4', 'w')]
D_9_11 = [n('A4', 'q.'), n('C5', 'e'), n('C5', 'h'),
          n('B4'), n('G4'), n('A4', 'h'),
          n('A4'), n('C5'), n('B4'), n('G4')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=11, nivel='intermedio', slug='LargoDvorak',
    formato='adulto',
    titulo_corto='Largo · Dvořák', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source',
                           'Largo-Sinfonia Dvorak'),
    yt='https://www.youtube.com/results?search_query=dvorak+largo+new+world+piano+easy',

    ficha=dict(
        titulo='Largo · Sinfonía del Nuevo Mundo',
        autor='Antonín Dvořák · arreglo de Ana Cristina Escobés',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Largo'), ('Figura', 'Con puntillo'),
               ('Páginas', 'Una')],
        titulo_ritmos='El c. 1 y el c. 11, mano a mano',
        pie_ritmos='Medido sobre tu partitura. Arriba, el c. 1 de la derecha: Mi con puntillo, Sol y '
                   'Sol de blanca. Abajo, la izquierda del c. 11. Los dedos, en tu partitura.',
        armonia=dict(
            titulo='Una melodía larga y una dinámica por bloques',
            tarjetas=[
                ('LA MELODÍA', 'Negra con puntillo',
                 'El patrón de las frases es una negra con puntillo, una corchea y una blanca: '
                 'largo, corto, largo. Se repite casi igual cuatro veces y por eso hay que '
                 'recordar en qué punto de la línea estás.'),
                ('LA DINÁMICA', 'p, mf, p, cresc., f, mp',
                 'Seis cambios de nivel en veintidós compases. No es un decorado: es la forma '
                 'de la pieza, y la única diferencia entre las cuatro frases iguales.'),
                ('LA REPETICIÓN', 'Cc. 9-12',
                 'Una barra de repetición abre el c. 9 y otra cierra el c. 12. Es la única vez '
                 'que se toca algo dos veces seguidas, y tiene que sonar distinto la segunda.'),
                ('LA IZQUIERDA', 'Lenta, y luego baja',
                 'Acordes de redonda al principio, negras que caminan desde el c. 11 y blancas '
                 'que bajan por grados en los cc. 17 y 18. Si las dos manos se mueven a la vez, '
                 'se pierde la línea larga.'),
            ],
            pie='El tempo es lo de menos: es "Largo", sin número. Lo que cuenta es no cortar la línea '
                'cada vez que cambia el nivel. Con tu base, es el tipo de pieza que se estudia '
                'cantando.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido',
             [n('E4', 'q.'), n('G4', 'e'), n('G4', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'c. 11 · medido',
             [n('F3'), n('A3'), n('G3'), n('E3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada y el compás es 4/4. Pone "Largo": muy lento.',
            'No trae número de metrónomo: el tempo es cosa tuya.',
            'Casi todo el compás de la derecha es una negra con puntillo y una corchea.',
            'Hay una barra de repetición que abarca los cc. 9 a 12.',
            'La dinámica cambia seis veces: p, mf, p, cresc., f y mp.',
            'Casi todo va bajo ligaduras de frase.',
        ],
        reto='Que las cuatro frases iguales no suenen iguales. La melodía repite el mismo dibujo y '
             'lo único que las separa es el nivel: sin dinámica, es una vuelta tras otra.',
        truco='Canta la melodía con el nombre de las notas y exagera el nivel de cada bloque '
              'hasta que te parezca ridículo: p muy flojo, mf claro y f grande. Al piano, '
              'quedará en un punto razonable.',
        sabias='Dvořák la escribió en 1893, durante su estancia en Estados Unidos. En la partitura '
               'pone "Sinfonía nº 5" porque era la numeración de entonces; hoy se llama la '
               'nº 9. Treinta años después, un discípulo le puso letra y la convirtió en el '
               'espiritual "Goin\' Home".',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el corno inglés abre la melodía y fíjate en que no respira al '
                      'acabar cada compás sino donde acaba cada ligadura de tu partitura.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La melodía se aprende en una tarde; lo que lleva semanas es el cambio de nivel '
              'entre bloques. Se estudia como una frase larga con tres puntos donde se respira.',
        reglas=['CANTA ANTES DE TOCAR', 'LA LÍNEA NO SE CORTA', 'CADA BLOQUE, SU NIVEL'],
        bloques=[
            dict(num=1, titulo='Los cuatro primeros compases de la derecha',
                 pista='cc. 1-4 · MEDIDO nota a nota sobre tu partitura · tres figuras: negra '
                       'con puntillo, corchea y blanca',
                 sistemas=[
                     dict(cap='a) la ligadura abarca las tres primeras notas del compás 1 · la '
                              'corchea no es una nota suelta: es el final de la negra con puntillo',
                          events=D_1_4, bars=4, matiz='p'),
                 ]),
            dict(num=2, titulo='La izquierda del c. 11: negras que caminan',
                 pista='cc. 10-11 · MEDIDO en el c. 11 · Fa, La, Sol y Mi, una nota por golpe',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) después de los acordes largos de los primeros compases, la izquierda '
                              'se pone a caminar · el c. 10 es Sol, Mi y Fa de blanca',
                          events=[n('G3'), n('E3'), n('F3', 'h'),
                                  n('F3'), n('A3'), n('G3'), n('E3')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=3, titulo='Los cc. 9-11: la línea que se repite',
                 pista='cc. 9-11 · leído de tu partitura y medido en el c. 11 · la derecha va '
                       'sobre un fondo que se mueve cada medio compás',
                 sistemas=[
                     dict(cap='a) la repetición abarca los cc. 9 a 12 · la primera vez, mf · la '
                              'segunda vez la tienes que hacer distinta',
                          events=D_9_11, bars=3, matiz='mf'),
                 ]),
            dict(tipo='nota',
                 etiqueta='LAS CUATRO FRASES IGUALES',
                 texto='Las frases de los cc. 1-4, 5-8, 13-16 y 17-20 empiezan igual. Lo que cambia '
                       'es el nivel: p, p, p y cresc. Marca a lápiz los cuatro niveles en tu '
                       'partitura y tócalas una detrás de otra, solo con el volumen distinto, antes '
                       'de tocar la pieza entera.'),
            dict(num=4, titulo='Las dos manos de los cc. 9-11',
                 pista='cc. 9-11 · leído · la izquierda sostiene medio compás y cambia, y la '
                       'derecha canta encima',
                 sistemas=[
                     dict(cap='a) en el c. 9 la izquierda cambia a mitad del compás · en el 11 se '
                              'mueve en cada golpe · mismo bloque que el paso 3, con las dos manos',
                          events=[ac(('F3', 'A4'), 'q.'), n('C5', 'e'), ac(('A3', 'C5'), 'h'),
                                  ac(('G3', 'B4')), ac(('E3', 'G4')), ac(('F3', 'A4'), 'h'),
                                  ac(('F3', 'A4')), ac(('A3', 'C5')), ac(('G3', 'B4')),
                                  ac(('E3', 'G4'))],
                          bars=3, manos='sostiene', matiz='mf'),
                 ]),
            dict(num=5, titulo='El crescendo hacia el f',
                 pista='cc. 17-19 · andamio de un crescendo de dos compases hasta un f',
                 sistemas=[
                     dict(cap='a) el crescendo se estudia con el mismo dibujo del c. 1 · sube un '
                              'poco cada nota, no cada compás',
                          events=[n('E4', 'q.'), n('G4', 'e'), n('G4', 'h'),
                                  n('C5', 'q.'), n('D5', 'e'), n('E5', 'h'),
                                  n('D5', 'w')],
                          bars=3, matiz='p', cresc=5),
                 ]),
            dict(num=6, titulo='La izquierda baja en los cc. 17 y 18',
                 pista='cc. 17-18 · leído de tu partitura · cuatro blancas que bajan por grados',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Do, Si, La y Sol de blanca · es la escala bajando por debajo del '
                              'crescendo · la mano baja y el volumen sube',
                          events=[n('C4', 'h'), n('B3', 'h'), n('A3', 'h'), n('G3', 'h')],
                          bars=2, clef='bass'),
                 ]),
        ] + bloques_extra('Do mayor', 11, 'E4', 'C3',
                          'la línea larga: cada ligadura es una sola respiración',
                          desde=7, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Largo · para casa',
            intro='Veinte minutos al día. Se canta primero y se toca después.',
            bloques=[
                plan((4, 'Cantar la melodía entera con los nombres de las notas'),
                     (6, 'La derecha sola, los cuatro primeros compases, con la ligadura'),
                     (5, 'La izquierda sola, las negras de los cc. 10-12'),
                     (5, 'Las dos manos, los cc. 9-12 con la repetición')),
                metronomo('Empieza a ♩ = 40 y no pases de ahí hasta que cada bloque tenga su nivel.',
                          'La partitura no trae número de metrónomo, solo "Largo".',
                          titulo='A qué velocidad te sale'),
                nombres(['E4', 'G4', 'D4', 'C4', 'A4', 'C5', 'B4'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='son notas de los cc. 1-4 y 9-11 de la derecha'),
                colorear([n('E4', 'q.'), n('G4', 'e'), n('G4', 'h'), n('E4', 'q.'),
                          n('D4', 'e'), n('C4', 'h')],
                         ['Las negras con puntillo, de rojo.',
                          'Las blancas, de verde.',
                          'Las corcheas, de azul.'],
                         titulo='Colorea según la figura',
                         pista='son los cc. 1 y 2 de la derecha'),
                diferencias([n('A4', 'q.'), n('C5', 'e'), n('C5', 'h'),
                             n('B4'), n('G4'), n('A4', 'h')],
                            [n('A4', 'q.'), n('C5', 'e'), n('C5', 'h'),
                             n('B4'), n('A4'), n('A4', 'h')],
                            1,
                            titulo='Busca la diferencia en el c. 9 y el c. 10',
                            pista='el de arriba es tu partitura · el de abajo ha cambiado una nota'),
                para_clase('Los cuatro niveles marcados a lápiz y las cuatro frases tocadas una '
                           'detrás de otra con el volumen distinto. Si la repetición de los cc. '
                           '9-12 te suena igual las dos veces, tráela.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
