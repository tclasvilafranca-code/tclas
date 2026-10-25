# -*- coding: utf-8 -*-
"""Heart and Soul (Hoagy Carmichael) — pieza 3 de Alan. Formato ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (guestinpiano.fr, "Easy
   Piano Version", 1 página, 24 compases), mirado a 110 dpi:

     - Do mayor sin armadura, 4/4, "♩ = 110" y debajo "Swing".
     - **Tres maneras de acompañar en la misma página**, que es lo que la hace
       útil: cc. 1-8, blancas (Do-La-Fa-Sol); cc. 9-16, **bajo y acorde
       alternando** (la nota grave en el uno, el acorde en el dos); desde el
       c. 17, **bajo y acorde repetido en corcheas**.
     - Barras de repetición al final de los cc. 8 y 16.
     - Desde el c. 17 la derecha sube a **octavas** (dos notas a la vez a
       distancia de octava), y en el c. 22 baja en octavas por grados.
     - El último compás es un acorde de redondas y un Do grave.
     - MEDIDO (300 dpi, ver TRANSCRIPCION_JOSEP_FUENTES): c. 1 Do · Do · Do
       (negra, negra, blanca); c. 2 silencio de corchea y Do · Si · La · Si · Do
       en corcheas y Re de negra.

   Mismo archivo que el de Josep: lo literal coincide, lo inventado no. Aquí el
   material de apoyo va por la **escalera de acompañamientos** (blancas → bajo y
   acorde → corcheas repetidas), que es la lección real de la página.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, plan, metronomo, verdadero_falso, inventa,
                      dibujar, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=3, nivel='intermedio', slug='HeartAndSoul',
    formato='adulto',
    titulo_corto='Heart and Soul', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'Heart-and-soul-'),
    yt='https://www.youtube.com/results?search_query=heart+and+soul+easy+piano+swing',

    ficha=dict(
        titulo='Heart and Soul',
        autor='Hoagy Carmichael · versión fácil',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 110 Swing'), ('Manos', 'Bajo y acorde'),
               ('Páginas', 'Una')],
        titulo_ritmos='Las tres maneras de acompañar',
        pie_ritmos='Leído sobre tu partitura: arriba el c. 1 de la derecha (medido); abajo, el '
                   'acompañamiento del c. 9, que es el que cambia la pieza. Los dedos, en tu '
                   'partitura.',
        armonia=dict(
            titulo='Una página, tres acompañamientos',
            tarjetas=[
                ('LOS CC. 1-8', 'Blancas',
                 'Do, La, Fa y Sol de blanca: la progresión de acordes más usada del pop de los '
                 'años cincuenta, escrita con la figura más tranquila.'),
                ('LOS CC. 9-16', 'Bajo y acorde',
                 'La nota grave en el uno y el acorde en el dos. Es el acompañamiento que se '
                 'queda para toda la vida.'),
                ('DESDE EL C. 17', 'Acorde repetido',
                 'El mismo acorde dos veces seguidas, en corcheas, y la derecha pasa a octavas. '
                 'Parece más difícil y es la misma idea.'),
                ('EL SWING', '♩ = 110',
                 'Las corcheas se escriben iguales y se tocan desiguales: la primera más larga '
                 'que la segunda. La partitura lo avisa con la palabra "Swing".'),
            ],
            pie='Es la pieza que mejor enseña a acompañar del cuaderno: la misma progresión de '
                'acordes con tres texturas distintas. Si aprendes las tres, las has aprendido '
                'para cualquier canción.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido',
             [n('C4'), n('C4'), n('C4', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'c. 9 · leído de tu partitura',
             [n('C3'), ac(('E3', 'G3')), n('A2'), ac(('C3', 'E3'))],
             AZUL, 'bass', None),
        ],
        especial=[
            'Pone "♩ = 110" y debajo "Swing".',
            'La izquierda hace tres cosas distintas: blancas, bajo y acorde, y acorde repetido.',
            'Hay barras de repetición al final del c. 8 y del c. 16.',
            'Desde el c. 17 la derecha toca octavas: dos notas a la vez a distancia de ocho.',
            'La progresión es siempre la misma: Do, La, Fa, Sol.',
            'El último compás es un acorde largo en la derecha y un Do grave en la izquierda.',
        ],
        reto='Que el bajo con acorde de la izquierda ande solo. Si tienes que mirarte la mano para '
             'cambiar de bajo a acorde, la derecha no puede cantar con swing.',
        truco='Toca la izquierda de los cc. 9-16 sin la derecha y con los ojos cerrados hasta que '
              'no falle ni un compás. Después, pon la derecha encima solo cuando la izquierda no '
              'necesite tu atención.',
        sabias='La compuso Hoagy Carmichael en 1938 y es famosa por un detalle: la melodía es tan '
               'repetitiva que se ha convertido en la pieza que "toda la gente sabe tocar" en '
               'dúo, con una persona haciendo el bajo y otra la melodía.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el bajo y el acorde se alternan sin pisarse: en la grabación '
                      'casi se oye el espacio entre los dos. Eso es el swing de la mano izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia de la textura más sencilla a la más compleja, y de la izquierda a la '
              'derecha. Cada una de las tres maneras de acompañar tiene su propio ejercicio.',
        reglas=['LA IZQUIERDA ANDA SOLA', 'DEL BAJO AL ACORDE', 'EL SWING SE ESCUCHA'],
        bloques=[
            dict(num=1, titulo='Los cc. 1-4 de la izquierda: blancas',
                 pista='cc. 1-4 · leído de tu partitura · la progresión Do, La, Fa, Sol',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) cuatro blancas por compás, de dos en dos · dilas con el nombre '
                              'del acorde mientras las tocas: Do, La menor, Fa, Sol',
                          events=[n('C3', 'h'), n('A2', 'h'), n('F2', 'h'), n('G2', 'h')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=2, titulo='El segundo compás de la derecha, con el silencio',
                 pista='c. 2 · MEDIDO · el silencio de corchea del principio es parte de la '
                       'frase',
                 sistemas=[
                     dict(cap='a) di "y-uno, y-dos..." antes de tocar · la derecha entra después '
                              'del primer golpe, no con él',
                          events=[sil('e'), n('C4', 'e'), n('B3', 'e'), n('A3', 'e'),
                                  n('B3', 'e'), n('C4', 'e'), n('D4')],
                          bars=1),
                 ]),
            dict(num=3, titulo='Los cc. 9-10 de la izquierda: bajo y acorde',
                 pista='cc. 9-10 · leído de tu partitura · el bajo en el uno y el acorde en el dos',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) bajo, acorde, bajo, acorde · mantén los dos dedos del acorde '
                              'juntos y suéltalos a la vez',
                          events=[n('C3'), ac(('E3', 'G3')), n('A2'), ac(('C3', 'E3')),
                                  n('F2'), ac(('A2', 'C3')), n('G2'), ac(('B2', 'D3'))],
                          bars=2, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE EMPIEZA POR ABAJO',
                 texto='En esta pieza la derecha es lo menos importante: sin la izquierda no hay '
                       'canción. Si la izquierda no anda sola, la derecha tiene que hacer de '
                       'muleta y no puede balancear. Por eso el orden es siempre izquierda sola, '
                       'derecha sola y solo después las dos.'),
            dict(num=4, titulo='El c. 17: el acorde repetido en corcheas',
                 pista='c. 17 · leído de tu partitura · el mismo acorde dos veces, a corcheas',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) un compás entero · el bajo en el uno y el acorde dos veces '
                              'seguidas, en el dos · el segundo golpe del acorde es más flojo',
                          events=[n('C3'), ac(('E3', 'G3'), 'e'), ac(('E3', 'G3'), 'e'),
                                  n('A2'), ac(('C3', 'E3'), 'e'), ac(('C3', 'E3'), 'e')],
                          bars=1, clef='bass'),
                 ]),
            dict(num=5, titulo='Las octavas de la derecha',
                 pista='c. 17 · leído de tu partitura · desde aquí la derecha toca dos notas '
                       'a la vez',
                 sistemas=[
                     dict(cap='a) los mismos tres golpes del c. 1, pero a la octava · la mano se '
                              'abre del pulgar al meñique y no se cierra entre golpe y golpe',
                          events=[ac(('C4', 'C5')), ac(('C4', 'C5')), ac(('C4', 'C5'), 'h')],
                          bars=1),
                 ]),
            dict(num=6, titulo='Las dos manos juntas, los dos primeros compases',
                 pista='andamio sobre los cc. 1-2 · despacio y con la izquierda de blancas',
                 sistemas=[
                     dict(cap='a) la melodía sobre las blancas del bajo · sin swing todavía: '
                              'primero iguales, después desiguales',
                          events=[ac(('C3', 'E4')), n('E4'), ac(('A2', 'E4'), 'h'),
                                  ac(('F2', 'F4'), 'h'), ac(('G2', 'G4'), 'h')],
                          bars=2, manos='dobla'),
                 ]),
        ] + bloques_extra('Do mayor', 54, 'C4', 'C3',
                          'el swing: escritas iguales, tocadas desiguales',
                          desde=7, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Heart and Soul · para casa',
            intro='Veinte minutos, y la mitad para la mano izquierda sola. Es la pieza donde '
                  'se nota quién practica el bajo.',
            bloques=[
                plan((6, 'Bajo y acorde con los ojos cerrados, cc. 9-16'),
                     (5, 'El acorde repetido en corcheas, cc. 17-18'),
                     (5, 'La derecha sola, con el silencio del c. 2 en su sitio'),
                     (4, 'Las dos juntas, de cuatro en cuatro compases')),
                metronomo('Empieza a ♩ = 70 con corcheas iguales, sin swing, y sube de diez en diez '
                          'hasta 110.',
                          'La meta son 110 con swing, que es lo que pone tu partitura: primero '
                          'limpio y parejo, y después balanceado.',
                          titulo='A qué velocidad te sale'),
                verdadero_falso([
                    'Detrás de la clave hay un bemol.',
                    'La partitura pone "Swing" debajo del metrónomo.',
                    'Desde el c. 17 la derecha toca octavas.',
                    'Los cc. 9-16 de la izquierda son blancas.',
                    'La progresión de acordes es la misma en toda la página.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                inventa(['Dos compases en 4/4.',
                         'Que el bajo y el acorde se alternen.',
                         'Que acabe en el acorde de Do.'],
                        time_sig=(4, 4), clef='bass',
                        titulo='Inventa un acompañamiento de dos compases',
                        pista='con la forma de los cc. 9-16 de tu partitura, pero tuyo'),
                dibujar(['Do', 'La', 'Fa', 'Sol', 'Do'],
                        titulo='Dibuja tú las notas del bajo',
                        pista='son las raíces de los cuatro primeros acordes · solo el óvalo, en clave de fa'),
                para_clase('El bajo con acorde a la velocidad que te salga sin mirar, y los dos '
                           'primeros compases con el silencio en su sitio. El swing lo miramos '
                           'juntos: es más fácil copiarlo que explicarlo.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
