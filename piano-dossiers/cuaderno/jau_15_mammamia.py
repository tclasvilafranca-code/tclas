# -*- coding: utf-8 -*-
"""Mamma Mia (ABBA) — pieza 15 de Jaume. ADULTO exigente, sin cifrado.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Unai Karam,
   3 páginas APAISADAS, 44 compases), a 250-300 ppp, cabeza a cabeza:

     - Detrás de la clave no hay nada: DO MAYOR, con un Sol♯ que se va y vuelve
       en el ostinato de los cuatro primeros compases (y un becuadro).
     - 4/4, y arriba va el metrónomo: **blanca = 68**.
     - No trae cifrado ni letra. La izquierda arranca con corcheas y a partir
       del c. 5 pasa a acordes de tres notas.
     - MEDIDO, c. 1 (las dos manos van juntas, ocho corcheas cada una):
         derecha   Do5 · Sol4 · Do5 · Sol4 · Do5 · Sol4 · Do5 · Sol♯4
         izquierda Do3 · Sol3 · Do3 · Sol3 · Do3 · Sol3 · Do3 · Sol♯3
       c. 2: Do5 · Sol♯4 · Do5 · Sol4 · Do5 · Sol4 · Do5 · Sol♮4 (y lo mismo
       en la izquierda: el Do dos octavas por debajo y el Sol una).
     - c. 5 (derecha): Sol4 · La4 · Do5 · Mi5 (corcheas) y un Mi5 de blanca
       ligado al Mi5 anterior; c. 6: Mi5 de negra (ligada), Mi5 · Re5 · Mi5 ·
       Re5 (corcheas) y Do5 de negra.
     - c. 21 (derecha): Re5 de corchea, Mi5 de negra, Mi5 y Re5 de
       SEMICORCHEA, Do5 de negra y silencio de negra.
     - Lleva semicorcheas (c. 21 y alguno más).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, rodear, unir, colorear, acuerdate,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: ostinato de los cc. 1 y 2
RH_1 = [n('C5', 'e'), n('G4', 'e'), n('C5', 'e'), n('G4', 'e'),
        n('C5', 'e'), n('G4', 'e'), n('C5', 'e'), n('G#4', 'e')]
RH_2 = [n('C5', 'e'), n('G#4', 'e'), n('C5', 'e'), n('G4', 'e'),
        n('C5', 'e'), n('G4', 'e'), n('C5', 'e'), n('Gn4', 'e')]
LH_1 = [n('C3', 'e'), n('G3', 'e'), n('C3', 'e'), n('G3', 'e'),
        n('C3', 'e'), n('G3', 'e'), n('C3', 'e'), n('G#3', 'e')]
LH_2 = [n('C3', 'e'), n('G#3', 'e'), n('C3', 'e'), n('G3', 'e'),
        n('C3', 'e'), n('G3', 'e'), n('C3', 'e'), n('Gn3', 'e')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=15, nivel='intermedio', slug='MammaMia',
    formato='adulto',
    titulo_corto='Mamma Mia', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source', 'Mama Mia'),
    yt='https://www.youtube.com/results?search_query=mamma+mia+abba+piano+tutorial',

    ficha=dict(
        titulo='Mamma Mia',
        autor='ABBA · arreglo de Unai Karam',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', 'Blanca = 68'), ('Páginas', '3, apaisadas'),
               ('Se toca', 'Dos manos')],
        titulo_ritmos='La melodía del c. 5 y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: cuatro corcheas que suben y una blanca ligada. '
                   'Abajo, andamio: dos acordes de tres notas en bloque, como los de la izquierda desde '
                   'el c. 5.',
        armonia=dict(
            titulo='Ocho corcheas que no paran, y un Sol sostenido que se va y vuelve',
            tarjetas=[
                ('EL OSTINATO', 'Ocho corcheas',
                 'En los cuatro primeros compases las dos manos tocan Do y Sol alternados, sin '
                 'respirar. El cuerpo aprende el dibujo, y después hay que dejarlo funcionar solo.'),
                ('EL SOL SOSTENIDO', 'Va, y vuelve',
                 'En el c. 1 el último Sol de la derecha es sostenido. En el c. 2 aparece otro en '
                 'el segundo golpe y el último vuelve a natural, con un becuadro delante.'),
                ('EL METRÓNOMO', 'A la blanca',
                 'El 68 va a la BLANCA, no a la negra: son 136 negras por minuto. Si pones el '
                 'metrónomo a 68 y cuentas negras, vas a la mitad de la velocidad.'),
                ('LAS SEMICORCHEAS', 'Pocas, y en el c. 21',
                 'La pieza es casi toda de corcheas. Las dos semicorcheas del c. 21 son lo único '
                 'rápido, y caen justo después de una nota larga.'),
            ],
            pie='Son tres páginas apaisadas, 44 compases, sin cifrado ni letra: toda la información '
                'está en las notas, y la pieza se estudia por frases.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 5 · medido',
             [n('G4', 'e'), n('A4', 'e'), n('C5', 'e'), dict(pitch='E5', dur='e', lig=True),
              n('E5', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · dos acordes de tres notas',
             [ac(('C3', 'E3', 'G3'), 'h'), ac(('G2', 'B2', 'D3'), 'h')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: Do mayor, con un Sol sostenido escrito delante de la nota.',
            'El compás es 4/4 y el metrónomo va a la blanca: blanca = 68.',
            'En los cc. 1 y 2 las dos manos hacen el mismo dibujo de ocho corcheas.',
            'La izquierda cambia a acordes de tres notas a partir del c. 5.',
            'Lleva semicorcheas (c. 21) y ligaduras de unión.',
            'Las tres páginas son apaisadas: en el álbum van giradas, y se lee con el cuaderno de lado.',
        ],
        reto='Mantener el ostinato dos compases sin que se encoja ni se acelere: ocho corcheas iguales '
             'por compás, con la nota sostenida en su sitio.',
        truco='Toca primero solo la derecha, después solo la izquierda, y la tercera vez juntas pero '
              'a la mitad de velocidad. Si el Sol sostenido se escapa, di en voz alta "sostenido" '
              'justo antes de la última corchea.',
        sabias='Mamma Mia salió en 1975, en el disco que lleva el nombre del grupo, ABBA. El arreglo '
               'de tu partitura la reduce a dos manos y a un dibujo de corcheas que casi no '
               'se detiene.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el principio de la canción: un dibujo de corcheas que se repite sin '
                      'variar. Es lo que tus dos manos hacen en los cc. 1-4.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Es una pieza de mucha repetición y poca variedad, y por eso se estudia contra el '
              'aburrimiento: el ostinato primero, la melodía después, y cada trozo con el '
              'metrónomo.',
        reglas=['EL OSTINATO, PRIMERO', 'EL SOL SOSTENIDO SE ANUNCIA', 'EL 68 VA A LA BLANCA'],
        bloques=[
            dict(num=1, titulo='El ostinato de la derecha, cc. 1 y 2',
                 pista='cc. 1-2 · medido sobre tu partitura · ocho corcheas por compás, cuatro Do y cuatro '
                       'Sol, uno de ellos sostenido, que se mueve de sitio',
                 sistemas=[
                     dict(cap='a) el c. 2 · el Sol sostenido ya no es el último de las ocho: es el segundo, '
                              'y el último vuelve a natural con un becuadro',
                          events=RH_2, bars=1),
                     dict(cap='b) el mismo dibujo en Re y La, sin ninguna alteración · andamio para '
                              'que la mano aprenda el vaivén antes de pelearse con el sostenido',
                          events=[n('D5', 'e'), n('A4', 'e'), n('D5', 'e'), n('A4', 'e'),
                                  n('D5', 'e'), n('A4', 'e'), n('D5', 'e'), n('A4', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='El mismo ostinato, en la izquierda',
                 pista='cc. 1-2 · medido sobre tu partitura · clave de fa, con el Do dos octavas por debajo '
                       'de la derecha',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) el c. 2 con Do3 y Sol3 · la mano no cambia de posición, solo salta '
                              'entre el Do y el Sol, con el sostenido en el segundo golpe',
                          events=LH_2, bars=1, clef='bass'),
                     dict(cap='b) el mismo dibujo en Fa y Do, sin alteraciones · andamio para que el '
                              'salto de quinta se haga sin mirar',
                          events=[n('F2', 'e'), n('C3', 'e'), n('F2', 'e'), n('C3', 'e'),
                                  n('F2', 'e'), n('C3', 'e'), n('F2', 'e'), n('C3', 'e')],
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos juntas',
                 pista='cc. 1-2 · medido sobre tu partitura · las dos manos caen a la vez, '
                       'corchea con corchea',
                 sistemas=[
                     dict(cap='a) el c. 1 y el c. 2 con las dos manos · cada corchea lleva dos '
                              'notas, una por mano',
                          events=[ac(('C3', 'C5'), 'e'), ac(('G3', 'G4'), 'e'),
                                  ac(('C3', 'C5'), 'e'), ac(('G3', 'G4'), 'e'),
                                  ac(('C3', 'C5'), 'e'), ac(('G3', 'G4'), 'e'),
                                  ac(('C3', 'C5'), 'e'), ac(('G#3', 'G#4'), 'e'),
                                  ac(('C3', 'C5'), 'e'), ac(('G#3', 'G#4'), 'e'),
                                  ac(('C3', 'C5'), 'e'), ac(('G3', 'G4'), 'e'),
                                  ac(('C3', 'C5'), 'e'), ac(('G3', 'G4'), 'e'),
                                  ac(('C3', 'C5'), 'e'), ac(('Gn3', 'Gn4'), 'e')],
                          bars=2, manos='dobla'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL 68 VA A LA BLANCA',
                 texto='El número del metrónomo se refiere a la figura dibujada a su lado, y aquí es '
                       'una blanca. Son 68 blancas por minuto, o sea 136 negras. Si no lo lees '
                       'bien y pones el clic a 68 contando negras, tocas a la mitad de lo que '
                       'pide la partitura. Se nota en el ostinato, que parece arrastrarse.'),
            dict(num=4, titulo='La melodía de los cc. 5 y 6',
                 pista='cc. 5-6 · medido sobre tu partitura · una escala corta, una nota larga '
                       'ligada y un balanceo',
                 sistemas=[
                     dict(cap='a) Sol, La, Do y Mi de corcheas, y el Mi que se queda en una blanca '
                              'ligada · el c. 6 retoma esa nota con una negra',
                          events=[n('G4', 'e'), n('A4', 'e'), n('C5', 'e'),
                                  dict(pitch='E5', dur='e', lig=True),
                                  dict(pitch='E5', dur='h', lig=True),
                                  n('E5'), n('E5', 'e'), n('D5', 'e'), n('E5', 'e'), n('D5', 'e'),
                                  n('C5')],
                          bars=2),
                 ]),
            dict(num=5, titulo='Las semicorcheas del c. 21',
                 pista='c. 21 · medido sobre tu partitura · las dos semicorcheas caen después de '
                       'una negra, no de una nota larga',
                 sistemas=[
                     dict(cap='a) el compás entero: corchea, negra, dos semicorcheas, negra y '
                              'silencio de negra',
                          events=[n('D5', 'e'), n('E5'), n('E5', 's'), n('D5', 's'),
                                  n('C5'), sil('q')],
                          bars=1),
                     dict(cap='b) el mismo dibujo una nota más grave · andamio · cuatro '
                              'semicorcheas valen una negra, y aquí solo hay dos',
                          events=[n('B4', 'e'), n('C5'), n('C5', 's'), n('B4', 's'),
                                  n('A4'), sil('q')],
                          bars=1, show_time=False),
                 ]),
            dict(num=6, titulo='El Sol sostenido y su becuadro, aislados',
                 pista='andamio · lo que dice la regla de la alteración, sin la música alrededor',
                 sistemas=[
                     dict(cap='a) un Sol, un Sol sostenido, un Sol con becuadro y otro Sol · el '
                              'becuadro anula el sostenido, y el Sol siguiente sigue sin él',
                          events=[n('G4'), n('G#4'), n('Gn4'), n('G4')], bars=1),
                 ]),
            dict(num=7, titulo='Los acordes de la izquierda, en bloque',
                 pista='andamio en Do mayor · la izquierda pasa a acordes de tres notas desde el '
                       'c. 5; las notas exactas están en tu partitura',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) tres acordes de redonda, para fijar la forma de la mano · los dedos '
                              'cambian de tecla, no de forma',
                          events=[ac(('C3', 'E3', 'G3'), 'w'), ac(('F2', 'A2', 'C3'), 'w'),
                                  ac(('G2', 'B2', 'D3'), 'w')],
                          bars=3, clef='bass'),
                 ]),
        ] + bloques_extra('Do mayor', 15, 'E4', 'C3',
                          'una pieza de ostinatos: lo que se repite se estudia con el metrónomo',
                          desde=8, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Mamma Mia · para casa',
            intro='Veinte minutos al día. El ostinato es lo único difícil, y se aprende con calma: '
                  'dos compases, bien, y después más.',
            bloques=[
                reto('Sostener el ostinato de los cc. 1-2 sin que se acelere: dieciséis corcheas '
                     'iguales, con el Sol sostenido en su sitio.',
                     'Pon el metrónomo a 68, un clic por blanca. Si al terminar el c. 2 vas más '
                     'deprisa que al empezar, baja diez clics y repite.'),
                plan((5, 'La derecha, cc. 1-4, a la mitad de velocidad'),
                     (5, 'La izquierda, cc. 1-4, igual'),
                     (6, 'Las dos manos, cc. 1-4, a 68'),
                     (4, 'La melodía de los cc. 5-6, aparte')),
                dict(rodear([[n('C5', 'e'), n('G4', 'e'), n('C5', 'e'), n('G4', 'e')],
                             [n('C5', 'e'), n('G#4', 'e'), n('C5', 'e'), n('G4', 'e')],
                             [n('C5', 'e'), n('G4', 'e'), n('C5', 'e'), n('G#4', 'e')],
                             [n('C5', 'e'), n('G4', 'e'), n('C5', 'e'), n('G4', 'e')]],
                            titulo='Rodea los dos grupos que son iguales',
                            pista='son medios compases del ostinato de tu partitura · el '
                                  'pentagrama es nuestro, la partitura es la tuya'),
                     clef='treble'),
                unir([('Blanca = 68', 'un clic por blanca, o sea 136 negras por minuto'),
                      ('Sol sostenido delante de la nota', 'vale solo hasta el final del compás'),
                      ('Becuadro', 'anula el sostenido que acaba de sonar'),
                      ('Ostinato', 'un dibujo que se repite sin cambiar')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                colorear([n('G4', 'e'), n('A4', 'e'), n('C5', 'e'), n('E5', 'e'), n('E5', 'h'),
                          n('E5'), n('E5', 'e'), n('D5', 'e'), n('C5')],
                         ['Las corcheas, de azul.',
                          'Las negras, de verde.',
                          'La blanca, de rojo.'],
                         titulo='Colorea según la figura',
                         pista='son las notas de los cc. 5 y 6 de tu partitura'),
                acuerdate('Las tres páginas van apaisadas: gira el cuaderno antes de ponerte a tocar. '
                          'Y el metrónomo va a la blanca, no a la negra.',
                          etiqueta='DOS COSAS QUE SE OLVIDAN'),
                para_clase('Los cc. 1-6 a 68 con las dos manos, y cuál de los dos Sol sostenidos '
                           'del ostinato te cuesta más. Si se te acelera, tráelo: se arregla '
                           'con el metrónomo en la clase.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
