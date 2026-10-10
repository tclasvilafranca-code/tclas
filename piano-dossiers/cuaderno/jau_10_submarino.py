# -*- coding: utf-8 -*-
"""El submarino amarillo (Lennon y McCartney) — pieza 10 de Jaume. ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Ana Cristina
   Escobés, elcuartodelpiano.com, 1 página, vectorial, 21 compases), mirado a
   110 dpi:

     - **Un sostenido** detrás de la clave (Fa♯): Sol mayor. 4/4, "Allegro" y
       "mf" al empezar. No trae número de metrónomo.
     - **Empieza en anacrusa**: dos corcheas, Si4 y Do5 (MEDIDO con
       `medir_arranque`), antes del primer compás.
     - La derecha va por escalones y **repite mucho la misma nota**: en los
       cc. 11-13 son cuatro corcheas iguales, una negra igual y un silencio,
       primero en La4 y después en Sol4.
     - La izquierda hace un molde que se repite: **la nota grave en el uno,
       el acorde dos veces seguidas en el dos y el tres, y un silencio de
       negra** (Sol · Si-Re · Si-Re en los cc. 1-2; después La, Do, Do; Re y
       el acorde La-Do).
     - Hay ligaduras de unión (la blanca de Re5 del c. 1 va ligada a una
       corchea del mismo Re).
     - En los cc. 10-15 la izquierda cambia a blancas: Sol-Re en el c. 10, Fa♯-Re
       en los cc. 11 y 12, Sol-Re en el 13 y en el 14 y Fa♯-Re en el 15 (leído a
       250 dpi: el Fa♯ de la armadura se toca de verdad en esa mano).

   Mismo archivo que el de Arnau (otro formato): lo literal coincide y lo
   inventado no. Aquí el trabajo va por el **molde de la izquierda** y por las
   **notas repetidas** de la derecha, que son lo que hace que la pieza se toque
   sola a ♩ rápido.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, ordenar, unir, inventa,
                       acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=10, nivel='intermedio', slug='SubmarinoAmarillo',
    formato='adulto',
    titulo_corto='El submarino amarillo', time_sig=(4, 4), key_sig='Sol mayor',
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source',
                           'El submarino amarillo'),
    yt='https://www.youtube.com/results?search_query=yellow+submarine+piano+easy',

    ficha=dict(
        titulo='El submarino amarillo',
        autor='John Lennon y Paul McCartney · arreglo de Ana Cristina Escobés',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'),
               ('Carácter', 'Allegro'), ('Empieza', 'En anacrusa'),
               ('Páginas', 'Una')],
        titulo_ritmos='La anacrusa y el molde de la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: la anacrusa son dos corcheas, Si y Do. Abajo, '
                   'leído: el molde de la izquierda, bajo y dos acordes. Los dedos, en tu partitura.',
        armonia=dict(
            titulo='Un molde, y mucha nota repetida',
            tarjetas=[
                ('EL MOLDE', 'Bajo y dos acordes',
                 'La izquierda hace siempre lo mismo: la nota grave en el uno, el acorde en el dos '
                 'y otra vez el acorde en el tres, con un silencio de negra al final. Cambia de '
                 'notas, no de forma.'),
                ('LA ANACRUSA', 'Dos corcheas',
                 'Entra con Si y Do antes del primer compás. Con "Allegro" y sin número de '
                 'metrónomo, la entrada la marca la profesora: aprende a contarla.'),
                ('NOTAS REPETIDAS', 'La4 y Sol4',
                 'En los cc. 11-13 la derecha toca cuatro corcheas iguales y una negra, dos veces '
                 'en La y una en Sol. Es la parte más fácil de leer y la que más se acelera.'),
                ('LA ARMADURA', 'Sol mayor',
                 'Un sostenido detrás de la clave. La melodía casi no pasa por el Fa, pero la '
                 'izquierda sí: las blancas de los cc. 11, 12 y 15 son Fa♯ y Re.'),
            ],
            pie='Es una pieza para tocar con la izquierda en piloto automático. Con tu base, el '
                'trabajo es dejar de pensar en ella y poner la atención en las notas repetidas '
                'de la derecha, que son las que se aceleran.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la anacrusa · medido',
             [sil('h.'), n('B4', 'e'), n('C5', 'e')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'cc. 1-2 · leído: el bajo y dos acordes',
             [n('G3'), ac(('B3', 'D4')), ac(('B3', 'D4')), sil('q')], AZUL, 'bass', None),
        ],
        especial=[
            'Un sostenido detrás de la clave: es Sol mayor.',
            'Pone "Allegro" y "mf", y no trae ningún número de metrónomo.',
            'Empieza en anacrusa: dos corcheas, Si y Do, antes del primer compás.',
            'La izquierda repite el mismo molde: grave, acorde, acorde y silencio.',
            'En los cc. 11-13 la derecha toca la misma nota cuatro veces seguidas.',
            'La blanca de Re del c. 1 va unida a una corchea del mismo Re.',
        ],
        reto='Que las notas repetidas no se aceleren. Cuando la melodía repite la misma nota cuatro '
             'veces, el oído se aburre y la mano se escapa: la tendencia es acabar el compás '
             'antes de tiempo.',
        truco='Toca los cc. 11-13 con un golpe de metrónomo por corchea y acentúa solo la primera '
              'de cada cuatro. Si las otras tres salen flojas y parejas, el compás ya no se '
              'escapa.',
        sabias='La canción es de 1966, del disco "Revolver", y la cantó Ringo Starr. Se pensó '
               'a propósito para que la pudiera cantar cualquiera, y por eso la melodía es tan '
               'corta de ámbito y tan repetida.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en el acompañamiento: hay un silencio de negra al final de cada '
                      'compás y la canción respira justo ahí. Es el silencio de tu mano '
                      'izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La izquierda es un molde que se aprende una vez; la derecha son notas repetidas que '
              'hay que aprender a no acelerar. Se estudia en ese orden y a un tempo cómodo.',
        reglas=['LA IZQUIERDA, UN MOLDE', 'LAS NOTAS REPETIDAS NO CORREN',
                'LA ANACRUSA SE CUENTA'],
        bloques=[
            dict(num=1, titulo='La izquierda: grave, acorde, acorde, silencio',
                 pista='cc. 1-2 · leído de tu partitura · el mismo molde dos veces seguidas',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) la nota grave en el uno y el acorde dos veces · el silencio de '
                              'negra se cuenta y no se toca · suelta los dedos todos a la vez',
                          events=[n('G3'), ac(('B3', 'D4')), ac(('B3', 'D4')), sil('q'),
                                  n('G3'), ac(('B3', 'D4')), ac(('B3', 'D4')), sil('q')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=2, titulo='La anacrusa y el primer compás de la derecha',
                 pista='anacrusa y c. 1 · leído de tu partitura · dos corcheas y una blanca '
                       'ligada',
                 sistemas=[
                     dict(cap='a) cuenta tres golpes en silencio y entra con las dos corcheas · el '
                              'Re de blanca está unido a la corchea que viene después',
                          events=[sil('h.'), n('B4', 'e'), n('C5', 'e'),
                                  dict(pitch='D5', dur='h', lig=True), n('D5', 'e'),
                                  n('B4', 'e'), n('A4', 'e'), n('B4', 'e')],
                          bars=2, matiz='mf'),
                 ]),
            dict(num=3, titulo='Las notas repetidas de los cc. 11-13',
                 pista='cc. 11-13 · leído de tu partitura · cuatro corcheas iguales y una negra',
                 sistemas=[
                     dict(cap='a) La, La y Sol · acentúa solo la primera de cada cuatro corcheas y '
                              'deja las otras tres parejas',
                          events=[n('A4', 'e'), n('A4', 'e'), n('A4', 'e'), n('A4', 'e'),
                                  n('A4'), sil('q'),
                                  n('A4', 'e'), n('A4', 'e'), n('A4', 'e'), n('A4', 'e'),
                                  n('A4'), sil('q'),
                                  n('G4', 'e'), n('G4', 'e'), n('G4', 'e'), n('G4', 'e'),
                                  n('G4'), sil('q')],
                          bars=3, acento=True),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE ACELERAN LAS NOTAS REPETIDAS',
                 texto='Cuando una nota se repite, el cerebro no tiene nada nuevo que leer y deja de '
                       'contar. La mano sigue por inercia y cada corchea sale un poco antes que la '
                       'anterior. La cura es poner la atención en algo que cambie: el acento del '
                       'primer golpe, el volumen o el silencio de negra del final.'),
            dict(num=4, titulo='El molde con otras notas: La y Do',
                 pista='cc. 3-4 · leído de tu partitura · la forma es la misma, el bajo y el '
                       'acorde cambian',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) La, Do y Do primero, y luego Re con el acorde de La y Do · '
                              'el movimiento de la mano es el mismo que en el c. 1',
                          events=[n('A3'), n('C4'), n('C4'), sil('q'),
                                  n('D3'), ac(('A3', 'C4')), ac(('A3', 'C4')), sil('q')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=5, titulo='Las blancas de la izquierda, cc. 10-13',
                 pista='cc. 10-13 · leído de tu partitura a 250 dpi · el molde se para y aparece '
                       'el Fa♯ de la armadura',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Sol-Re, Fa♯-Re, Fa♯-Re y Sol-Re · el Fa♯ está en la armadura, no '
                              'delante de la nota: no te lo van a recordar',
                          events=[n('G3', 'h'), n('D3', 'h'), n('F3', 'h'), n('D3', 'h'),
                                  n('F3', 'h'), n('D3', 'h'), n('G3', 'h'), n('D3', 'h')],
                          bars=4, clef='bass'),
                 ]),
        ] + bloques_extra('Sol mayor', 10, 'G4', 'G2',
                          'notas repetidas: la atención va al acento y no a la nota',
                          desde=6, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='El submarino amarillo · para casa',
            intro='Veinte minutos al día. La izquierda se aprende una vez; el resto es la derecha.',
            bloques=[
                reto('Tocar los cc. 11-13 sin que las corcheas repetidas se acerquen al compás '
                     'siguiente.',
                     'Un golpe de metrónomo por corchea, acento solo en la primera de cada cuatro. Si '
                     'a mitad de compás empiezas a llegar antes que el metrónomo, el problema es '
                     'que has dejado de contar, no que seas rápido.'),
                plan((4, 'El molde de la izquierda, sin mirar, diez veces'),
                     (5, 'La anacrusa y el primer compás, contando tres antes de entrar'),
                     (6, 'Los cc. 11-13 con metrónomo y acento'),
                     (5, 'Las dos manos, hasta el c. 10')),
                ordenar(['Las dos manos, hasta el c. 10, a tempo cómodo.',
                         'La izquierda sola, el molde con los dos acordes.',
                         'Los cc. 11-13 con metrónomo, acentuando el primer golpe.',
                         'La anacrusa, contando tres golpes en silencio.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='uno de ellos se hace sin piano'),
                unir([('Anacrusa', 'se entra antes del primer compás'),
                      ('Silencio de negra', 'se cuenta y no se toca'),
                      ('Ligadura de unión', 'dos notas iguales que suenan como una'),
                      ('Allegro', 'rápido, sin número de metrónomo')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                inventa(['Dos compases de cuatro golpes.',
                         'Empieza con una anacrusa de dos corcheas.',
                         'Solo Sol, La, Si y Re, que son las notas de la pieza.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases con anacrusa',
                        pista='como los de la pieza, pero tuyos · y tócalo a tempo'),
                acuerdate('La pieza no lleva número de metrónomo, solo "Allegro". Elige un tempo '
                          'que te permita tocarla entera sin acelerar, apúntalo a lápiz y no lo '
                          'cambies en toda la semana.',
                          etiqueta='ELIGE LA VELOCIDAD Y APÚNTALA'),
                para_clase('Los cc. 11-13 con metrónomo, y a qué número te salen sin que las '
                           'corcheas se escapen. Si la anacrusa se te desvía, tráela contada.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
