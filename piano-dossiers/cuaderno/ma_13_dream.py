# -*- coding: utf-8 -*-
"""I Have a Dream (Abba) — pieza 13 de Martina. ADULTO exigente, tono de niña.

   Lo comprobado sobre el PDF de su carpeta de Drive (INeVENT Music Academy, "Ihave-a-dream",
   2 páginas, VECTORIAL, con la letra debajo, 29 compases), medido a 220 ppp y a 600 ppp:

     - Detrás de la clave no hay nada: Do mayor. 4/4. Pone "TEMPO-120", sin el signo de
       negra: la ficha dice ♩ = 120.
     - La derecha **entra tarde**: casi todas las frases empiezan con un silencio de negra.
       Solo hay una figura más corta que la corchea: UNA semicorchea (La4, c. 9).
     - Hay ligaduras de unión: la redonda de Do4 del c. 8 se une a la blanca del c. 9; la
       blanca con puntillo de Re4 del c. 10 a la blanca del c. 11; la de Mi4 del c. 16 a la
       del 17; y las del final (cc. 28-29).
     - MEDIDO, derecha (alturas escritas, sin 8va):
       c. 1 y c. 5:   (silencio de negra) Sol3 · Mi4. · Re4 (corchea)       ["I have a"]
       c. 2 y c. 6:   Fa4 (redonda)
       c. 3 y c. 7:   (silencio de negra) Sol3 · Do4. · Si3 (corchea)
       c. 4:          Do4 (redonda)
       c. 9:   Do4 (blanca, ligada a la redonda del c. 8) · Mi4 · Fa4 (corcheas) ·
               Sol4. (corchea con puntillo) · La4 (semicorchea)
       c. 10:  Sol4 (negra) · Re4 (blanca con puntillo)       c. 11: Re4 (blanca) ·
               Re4 · Mi4 · Fa4 · Sol4 (corcheas)              c. 12: Mi4 (redonda)
     - La Sol3 del principio CUELGA por debajo de DOS líneas adicionales (Do4 y La3), con
       la cabeza debajo de la de La, no encima: mirado a 600 ppp. (La ficha de Eduard la da
       como La3: queda por revisar.)
     - La izquierda: c. 1 Do3 (redonda), c. 2 Sol3 y Do4 juntas (redonda), c. 3 Sol3-Si3 en
       negra y silencios, c. 4 Do3-Fa3, c. 5 Do3-Mi3.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, reto, plan, ordenar, unir, inventa, acuerdate,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: derecha, cc. 1-4
C1 = [sil('q'), n('G3'), n('E4', 'q.'), n('D4', 'e')]
C2 = [n('F4', 'w')]
C3 = [sil('q'), n('G3'), n('C4', 'q.'), n('B3', 'e')]
C4 = [n('C4', 'w')]
# MEDIDO: cc. 8-9 (la ligadura y la semicorchea)
C8 = [dict(n('C4', 'w'), lig=True)]
C9 = [n('C4', 'h'), n('E4', 'e'), n('F4', 'e'), n('G4', 'e.'), n('A4', 's')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=13, nivel='iniciación', slug='IHaveADream',
    formato='adulto',
    titulo_corto='I Have a Dream', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source',
                           'Ihave-a-dream-Abba'),
    yt='https://www.youtube.com/results?search_query=i+have+a+dream+abba+piano+easy',

    ficha=dict(
        titulo='I Have a Dream',
        autor='Abba · edición de INeVENT Music Academy',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 120'), ('Izquierda', 'Redondas'),
               ('Páginas', 'Dos')],
        titulo_ritmos='La melodía entra tarde',
        pie_ritmos='Arriba, medido sobre tu partitura: el silencio, la nota grave, la nota con '
                   'puntillo y la redonda. Abajo, medida también: la primera redonda.',
        armonia=dict(
            titulo='Lo nuevo: no se entra en el uno',
            tarjetas=[
                ('EL SILENCIO', 'Cuenta el uno callada',
                 'La frase empieza con un silencio de negra: el compás arranca y tú todavía no '
                 'tocas. Hay que contar el uno igual, aunque no suene.'),
                ('LA NOTA GRAVE', 'Sol, bajo la clave',
                 'La primera nota cuelga por debajo del pentagrama, de dos líneas cortitas '
                 'que se llaman líneas adicionales. Es el Sol grave: la cabeza va debajo de '
                 'la segunda.'),
                ('LA LIGADURA', 'Dos notas, un sonido',
                 'En el c. 8 hay una redonda de Do unida con una curva a la blanca de Do del '
                 'c. 9. La curva se llama ligadura: se toca una vez y suena seis tiempos.'),
                ('LA SEMICORCHEA', 'La más corta',
                 'En el c. 9 hay una sola semicorchea, la La4. Cuatro como ella caben en un '
                 'golpe: es la nota más rápida de toda la canción.'),
            ],
            pie='Son pocas notas y casi todas por escalones. Lo difícil no son las notas, es el '
                'silencio: entrar justo en el dos y aguantar las largas sin correr.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-4 · medido', C1 + C2 + C3 + C4, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'c. 1 · medido',
             [n('C3', 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 4/4 y arriba pone "TEMPO-120".',
            'Casi todas las frases empiezan con un silencio de negra.',
            'La primera nota cuelga por debajo del pentagrama, con dos líneas adicionales.',
            'Hay una curva, la ligadura, entre las notas de los cc. 8 y 9.',
            'La letra está escrita debajo del pentagrama, sílaba a sílaba.',
        ],
        reto='Entrar justo en el dos, sin adelantarte, las cuatro veces que la frase empieza '
             'con silencio: cc. 1, 3, 5 y 7.',
        truco='Cuenta "un, dos, tres, cuatro" en voz alta con las manos quietas, y entra al '
              'segundo. La voz no miente: si cuentas a gritos, no te adelantas.',
        sabias='Abba grabó esta canción en 1979 con un coro de niños de un colegio de '
               'Estocolmo. Eligieron a niños porque la letra habla de creer en las cosas que '
               'aún no se ven, y les sonaba más sincero.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que la voz entra un poquito después de que empiece el compás. '
                      'Ese huequito es tu silencio de negra.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana lo importante es contar. Las notas ya las sabes leer; lo nuevo es '
              'cuándo entra cada una y cuánto dura el silencio de antes.',
        reglas=['CUENTA EN VOZ ALTA, SIEMPRE', 'EL SILENCIO TAMBIÉN SE CUENTA',
                'CANTA LA LETRA MIENTRAS MIRAS'],
        bloques=[
            dict(num=1, titulo='Entrar después del silencio, cc. 1-2',
                 pista='cc. 1-2 · medidos sobre tu partitura · el silencio del uno es literal',
                 sistemas=[
                     dict(cap='a) cuenta "un" con la mano quieta y entra en el "dos" · el '
                              'Sol está abajo, con dos líneas adicionales',
                          events=C1 + C2, bars=2),
                     dict(cap='b) la misma forma con otras notas · andamio · el silencio '
                              'vuelve a estar en el uno y la redonda cierra',
                          events=[sil('q'), n('A3'), n('F4', 'q.'), n('E4', 'e'),
                                  n('G4', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='UN SILENCIO TAMBIÉN DURA',
                 texto='El silencio de negra dura un golpe entero, igual que la nota que '
                       'ocuparía su sitio. No es "esperar un poquito": es contar uno. Si lo '
                       'cuentas, entras bien siempre; si lo esperas a ojo, cada vez entras '
                       'en un sitio distinto.'),
            dict(num=2, titulo='La nota grave, cc. 3 y 4',
                 pista='cc. 3-4 · medidos sobre tu partitura · el mismo molde que el c. 1',
                 sistemas=[
                     dict(cap='a) Sol grave, Do con puntillo y Si de corchea, y la redonda de '
                              'Do · el Si está justo debajo del Do',
                          events=C3 + C4, bars=2),
                 ]),
            dict(num=3, titulo='La ligadura y la semicorchea, cc. 8-9',
                 pista='cc. 8-9 · medidos sobre tu partitura · la curva une las dos Do',
                 sistemas=[
                     dict(cap='a) la redonda y la blanca de Do unidas · se toca una vez y '
                              'suena seis tiempos · no se vuelve a pulsar',
                          events=C8 + C9, bars=2),
                 ]),
            dict(num=4, titulo='Las dos manos, el principio',
                 pista='cc. 1-2 · la izquierda es una redonda: dura el compás entero',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) la izquierda del c. 1 y del c. 2 · una redonda suelta y '
                              'otra de dos notas, Sol y Do, tocadas juntas',
                          events=[n('C3', 'w'), ac(('G3', 'C4'), 'w')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=5, titulo='Las cuatro corcheas que suben, cc. 10-12',
                 pista='cc. 10-12 · medidos sobre tu partitura · una blanca con puntillo '
                       'ligada, y las corcheas por escalones',
                 sistemas=[
                     dict(cap='a) Sol, la blanca con puntillo de Re ligada a la blanca del '
                              'c. 11, y cuatro corcheas que suben Re, Mi, Fa, Sol · '
                              'cuéntalas "un-y, dos-y"',
                          events=[n('G4'), dict(n('D4', 'h.'), lig=True),
                                  n('D4', 'h'), n('D4', 'e'), n('E4', 'e'), n('F4', 'e'),
                                  n('G4', 'e'), n('E4', 'w')],
                          bars=3),
                 ]),
            dict(num=6, titulo='Subir otra vez, cc. 16-17',
                 pista='cc. 16-17 · la misma idea, más arriba · sube hasta el Do de arriba',
                 sistemas=[
                     dict(cap='a) la redonda de Mi ligada a la blanca, y cuatro corcheas que '
                              'suben Sol, La, Si, Do',
                          events=[dict(n('E4', 'w'), lig=True), n('E4', 'h'), n('G4', 'e'),
                                  n('A4', 'e'), n('B4', 'e'), n('C5', 'e')],
                          bars=2, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 13, 'F4', 'C3',
                          'entrar tarde, contar el silencio y aguantar las largas',
                          desde=7, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='I Have a Dream · para casa',
            intro='Quince minutos al día. Hay pocas notas: lo que se entrena es contar.',
            bloques=[
                reto('Tocar los cc. 1-8 entrando en el dos, tres veces seguidas, sin '
                     'adelantarte ni una.',
                     'Cuenta en voz alta y grábate con el móvil. Cada vez que entras antes de '
                     'tiempo, el contador vuelve a cero.'),
                plan((3, 'La derecha sola, cc. 1-4, contando el silencio'),
                     (3, 'La izquierda sola, las redondas, cc. 1-6'),
                     (4, 'Los cc. 1-8 con las dos manos'),
                     (4, 'Los cc. 9-12: la ligadura y la semicorchea')),
                ordenar(['Contar los cuatro golpes en voz alta con las manos quietas.',
                         'Tocar solo la derecha, cc. 1-4.',
                         'Tocar solo la izquierda: las redondas.',
                         'Tocar las dos manos juntas, cc. 1-8.'],
                        titulo='Pon los cuatro pasos en orden',
                        pista='del más fácil al más completo · uno de ellos no es tocar'),
                unir([('♩ = 120', 'ciento veinte negras por minuto'),
                      ('Silencio de negra', 'un golpe en el que no suena nada'),
                      ('Ligadura', 'dos notas iguales que suenan como una'),
                      ('Semicorchea', 'cuatro caben en un golpe')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro están en tu partitura'),
                inventa(['Dos compases en 4/4.',
                         'Que el primero empiece con un silencio de negra.',
                         'Que el segundo sea una redonda.'],
                        time_sig=(4, 4),
                        titulo='Inventa tu propio "I have a dream"',
                        pista='con el molde del c. 1 y del c. 2 de tu partitura, pero con tus notas'),
                acuerdate('Las notas que duran mucho también hay que contarlas: una redonda son '
                          'cuatro golpes en voz alta, no uno solo.',
                          etiqueta='LAS LARGAS TAMBIÉN SE CUENTAN'),
                para_clase('Los cc. 1-8 con las dos manos y contando el silencio. Dime en cuál '
                           'de las cuatro entradas te adelantas.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
