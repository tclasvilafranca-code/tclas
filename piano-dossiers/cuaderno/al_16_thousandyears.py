# -*- coding: utf-8 -*-
"""A Thousand Years (Christina Perri) — pieza 16 de Alan. ADULTO exigente,
   tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Piano Seeds
   STUDIO, 2 páginas, imagen a 55 ppp), mirado a 200 ppp:

     - Detrás de la clave no hay nada. 6/8. No trae tempo ni intensidad.
     - 33 compases: 17 en la primera página y 16 en la segunda. La letra va impresa
       y la partitura trae los números de dedo.
     - Solo negras con puntillo, negras, corcheas (de tres en tres) y blancas con
       puntillo, más alguna nota ligada. Ninguna figura más corta que la corchea.
     - MEDIDO, mano derecha, a 200 ppp contra las líneas del pentagrama:
       cc. 1 y 3: dos intervalos de Sol4 y Mi5 en negra con puntillo
       cc. 2 y 4: Sol4 y Mi5, y después Sol4 y Re5 (negras con puntillo)
       c. 9: Do5 · Do5 (negras con puntillo)
       c. 10: Do5 (negra con puntillo) · Mi5 · Re5 · Do5 (corcheas)
     - La izquierda, cc. 1-4: una blanca con puntillo ligada a una negra con puntillo,
       y después otra negra con puntillo. Desde el c. 9, acordes en negra con puntillo.
     - Desde el c. 21 la melodía sube y se queda arriba durante cuatro compases.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, reto, plan, escalera, inventa, teclado,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
T = (6, 8)

# MEDIDO: cc. 1-2 y cc. 9-10 (derecha)
D1 = ac(('G4', 'E5'), 'q.')
D2 = ac(('G4', 'D5'), 'q.')
C1 = [D1, D1]
C2 = [D1, D2]
C9 = [n('C5', 'q.'), n('C5', 'q.')]
C10 = [n('C5', 'q.'), n('E5', 'e'), n('D5', 'e'), n('C5', 'e')]

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=16, nivel='intermedio', slug='AThousandYears',
    formato='adulto',
    titulo_corto='A Thousand Years', time_sig=T, key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'A THOUSAND YEARS.'),
    yt='https://www.youtube.com/results?search_query=a+thousand+years+christina+perri+piano+easy',

    ficha=dict(
        titulo='A Thousand Years',
        autor='David Hodges y Christina Perri · arreglo de Piano Seeds STUDIO',
        datos=[('Tonalidad', 'Sin armadura'), ('Compás', '6/8'),
               ('Carácter', 'Sin tempo impreso'), ('Letra', 'Impresa'),
               ('Páginas', 'Dos')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: dos notas a la vez, en negra con puntillo, '
                   'cuatro veces. Abajo, andamio: la blanca con puntillo ligada de la izquierda.',
        armonia=dict(
            titulo='Un 6/8 que se cuenta en dos, con las notas largas ligadas',
            tarjetas=[
                ('EL 6/8', 'Dos golpes largos',
                 'Seis corcheas por compás, agrupadas de tres en tres: se cuenta "uno-dos", no '
                 '"uno-dos-tres-cuatro-cinco-seis". La negra con puntillo es el golpe.'),
                ('EL COMIENZO', 'Dos notas a la vez',
                 'Los cuatro primeros compases son pares de notas en negra con puntillo: Sol4 con '
                 'Mi5, y en el c. 2 y el c. 4 el segundo par cambia a Sol4 con Re5.'),
                ('LA IZQUIERDA', 'Larga y ligada',
                 'Una blanca con puntillo ligada a una negra con puntillo, y después otra negra '
                 'con puntillo. A partir del c. 9 la mano pasa a acordes de tres notas.'),
                ('LA MELODÍA', 'Con letra',
                 'En el c. 9 empiezan las notas de la melodía con letra impresa: Do5 en negras con '
                 'puntillo y, al final del c. 10, tres corcheas que bajan: Mi, Re y Do.'),
            ],
            pie='33 compases, dos páginas, ni un sostenido ni un bemol. Lo difícil es respirar en '
                'dos golpes largos sin que se note el seis por dentro.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-2 · medido', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · una blanca con puntillo ligada',
             [dict(n('C3', 'h.'), lig=True), n('C3', 'q.'), n('B2', 'q.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 6/8 y no trae número de metrónomo.',
            'La derecha empieza con pares de notas en negra con puntillo.',
            'La izquierda lleva una blanca con puntillo ligada a una negra con puntillo.',
            'La letra va impresa debajo de la melodía.',
            'En los cc. 22-24 la melodía se sale del pentagrama por arriba.',
        ],
        reto='Contar en dos, no en seis. Una negra con puntillo dura tres corcheas: si cuentas '
             'seis, la música se parte en trozos y pierdes el aire de la canción.',
        truco='Di "UN-dos" con el cuerpo, balanceándote con cada golpe, y toca encima. Si el '
              'balanceo se entrecorta, es que has contado alguna corchea por separado.',
        sabias='A Thousand Years es de Christina Perri y David Hodges, de 2011, para la película '
               'Crepúsculo: Amanecer, primera parte. Se ha oído en miles de bodas y es de las '
               'canciones de piano que más se piden.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el piano del principio: tres notas por golpe, siempre dos golpes '
                      'por compás. Cuando lo notes, ya sabes contar el 6/8.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia contando en dos desde el primer día. Las notas son sencillas: lo que '
              'cuesta es que el 6/8 suene a dos golpes y no a seis.',
        reglas=['CUENTA EN DOS, NO EN SEIS', 'LA LIGADURA NO SE VUELVE A TOCAR',
                'LAS TRES CORCHEAS, IGUALES'],
        bloques=[
            dict(num=1, titulo='Las dos notas a la vez, cc. 1 y 2',
                 pista='cc. 1-2 · medidos sobre tu partitura · pares de notas en negra con puntillo',
                 sistemas=[
                     dict(cap='a) Sol4 y Mi5 a la vez, dos veces · cada par dura tres corcheas y '
                              'se cuenta "UN-dos"',
                          events=C1, bars=1, time_sig=T),
                     dict(cap='b) y el segundo par, que baja del Mi al Re · el Sol de abajo se '
                              'queda igual',
                          events=[D1, D2], bars=1, time_sig=T, show_time=False),
                 ]),
            dict(num=2, titulo='La melodía con letra, cc. 9-10',
                 pista='cc. 9-10 · medidos sobre tu partitura · Do5 en negras con puntillo y tres '
                       'corcheas que bajan',
                 sistemas=[
                     dict(cap='a) dos Do en negras con puntillo y, en el c. 10, Do, Mi, Re y Do · las '
                              'tres corcheas se tocan iguales, sin apoyar ninguna',
                          events=C9 + C10, bars=2, time_sig=T),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTA EN DOS',
                 texto='El 6/8 son seis corcheas, pero se sienten como dos golpes de tres cada uno: '
                       'un balanceo largo, un "UN-dos, UN-dos". Si cuentas las seis, cada corchea '
                       'pesa lo mismo y la música suena a marcha. Cuenta dos, siente las tres '
                       'corcheas dentro de cada golpe, y la pieza respira sola.'),
            dict(num=3, titulo='La izquierda, con la nota larga ligada',
                 pista='cc. 1-2 · el ritmo es el de tu partitura · las notas son andamio',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) una blanca con puntillo ligada a una negra con puntillo, y otra '
                              'negra con puntillo · la ligadura une las dos notas: no se pulsa '
                              'otra vez',
                          events=[dict(n('F2', 'h.'), lig=True), n('F2', 'q.'), n('E2', 'q.')],
                          bars=2, time_sig=T, clef='bass'),
                 ]),
            dict(num=4, titulo='Las dos manos, el comienzo del c. 9',
                 pista='cc. 9-10 · la derecha es MEDIDA · el acorde de la izquierda es andamio',
                 sistemas=[
                     dict(cap='a) los dos Do de la derecha con el acorde largo de la izquierda · el '
                              'acorde entra una sola vez y se queda sonando',
                          events=[ac(('C3', 'E3', 'G3', 'C5'), 'q.'), n('C5', 'q.')],
                          bars=1, time_sig=T, manos='sostiene'),
                 ]),
        ] + bloques_extra('Do mayor', 16, 'E4', 'C3',
                          'contar en dos y las tres corcheas que bajan',
                          desde=5, time_sig=T, mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='A Thousand Years · para casa',
            intro='Veinte minutos al día. Primero se aprende a contar en dos, y solo después se '
                  'toca.',
            bloques=[
                reto('Tocar los cc. 1-4 contando en dos, tres veces seguidas, sin que se te '
                     'cuelen seis golpes por compás.',
                     'Pon el metrónomo a 40 (un clic por cada negra con puntillo) y cuenta '
                     '"UN-dos" en voz alta. Apunta cuántas veces seguidas lo consigues: tres '
                     'limpias, no tres en total.'),
                plan((5, 'Contar en dos y dar una palmada en cada golpe, sin tocar'),
                     (5, 'La derecha sola, cc. 1-4 y 9-12'),
                     (4, 'La izquierda sola, la blanca con puntillo ligada'),
                     (6, 'Las dos manos, cc. 1-4, con el metrónomo')),
                escalera((36, 'la derecha sola, cc. 1-4'),
                         (44, 'las dos manos, cc. 1-4'),
                         (52, 'los cc. 1-12 seguidos'),
                         (60, 'la meta que te pones tú: la partitura no la trae'),
                         meta='Tu partitura no trae número de metrónomo: la meta la pones tú y la '
                              'apuntas a lápiz. Los números cuentan negras con puntillo, o sea dos '
                              'clics por compás.',
                         titulo='La escalera del metrónomo'),
                inventa(['Dos compases en 6/8.',
                         'Con una negra con puntillo en cada golpe.',
                         'Que acaben en tres corcheas que bajan.'],
                        time_sig=(6, 8),
                        titulo='Inventa dos compases como los del c. 10',
                        pista='con el ritmo de los cc. 9-10 de tu partitura, pero tuyo'),
                teclado({4: 1, 9: 2, 8: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         'La número 1 es el Sol, la nota que suena abajo en los cc. 1 y 2.'],
                        titulo='En el teclado',
                        pista='son las notas de los pares de los cc. 1 y 2 · las dos de arriba '
                              'cambian de un par a otro'),
                para_clase('Los cc. 1-4 con las dos manos, contando en dos, y la velocidad que '
                           'has elegido como meta. Dime cuál ha sido: si es muy alta, la bajamos '
                           'juntos, que la meta no es correr.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
