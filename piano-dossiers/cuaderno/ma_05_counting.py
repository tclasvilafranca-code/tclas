# -*- coding: utf-8 -*-
"""Counting Stars (OneRepublic) — pieza 5 de Martina. ADULTO exigente,
   tono de niña que empieza de cero.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Becky Messer,
   "Easy Version", Musescore, 2 páginas, vectorial), a 220-250 ppp:

     - DO MAYOR: detrás de la clave no hay nada. 4/4. No trae tempo.
     - La DIGITACIÓN va impresa encima de las notas. En el álbum no se imprime
       ningún número de dedo: los escribe Alan.
     - La izquierda toca intervalos de dos notas en redonda, uno por compás.
     - Trae barras de repetición y una casilla "1.".
     - MEDIDO, mano derecha:
       c. 1: Re4 · Mi4 · Sol4 · Mi4 (negras)
       c. 2: Re4 · Mi4 · Re4 · Do4 (corcheas) y Mi4 (blanca)
       c. 3: silencio de corchea y Re4 · Re4 · Mi4 · Fa4 · Mi4 · Re4 · Do4 (corcheas)
   Es el mismo archivo que el de José María y Josep. Aquí lo literal es lo medido y
   el andamio es otro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, plan, metronomo, verdadero_falso, inventa, dibujar,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: cc. 1-3 (derecha)
C1 = [n('D4'), n('E4'), n('G4'), n('E4')]
C2 = [n('D4', 'e'), n('E4', 'e'), n('D4', 'e'), n('C4', 'e'), n('E4', 'h')]
C3 = [sil('e'), n('D4', 'e'), n('D4', 'e'), n('E4', 'e'), n('F4', 'e'), n('E4', 'e'),
      n('D4', 'e'), n('C4', 'e')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=5, nivel='iniciación', slug='CountingStars',
    formato='adulto',
    titulo_corto='Counting Stars', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'Counting-stars'),
    yt='https://www.youtube.com/results?search_query=counting+stars+piano+easy+version',

    ficha=dict(
        titulo='Counting Stars',
        autor='OneRepublic · arreglo de Becky Messer · Easy Version',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin tempo impreso'), ('Digitación', 'Impresa'),
               ('Páginas', 'Dos')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: cuatro negras y después cuatro corcheas con una '
                   'blanca. Abajo, andamio: la izquierda toca dos notas a la vez en redonda.',
        armonia=dict(
            titulo='Tres compases, tres ritmos distintos',
            tarjetas=[
                ('LAS NEGRAS', 'Para empezar',
                 'El c. 1 son cuatro negras: Re, Mi, Sol, Mi. Es el arranque tranquilo; la '
                 'melodía todavía no corre.'),
                ('LAS CORCHEAS', 'Después aceleran',
                 'En el c. 2 aparecen cuatro corcheas seguidas, y en el c. 3 siete. Mismas notas '
                 'cercanas, pero más rápidas: la mano no puede ir saltando.'),
                ('LOS DEDOS', 'Vienen escritos',
                 'Tu partitura trae los números de dedo encima de las notas. No son una '
                 'sugerencia: si los cambias, la frase siguiente no te cabe en la mano.'),
                ('LAS REPETICIONES', 'Y una casilla 1',
                 'Hay barras de repetición y una casilla "1.". La pieza parece más larga de lo que '
                 'es: muchos compases vuelven.'),
            ],
            pie='La izquierda lo único que hace es aguantar dos notas por compás. Todo el trabajo está '
                'en la derecha, y por eso se estudia con la mano quieta y los dedos que vienen escritos.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1 y 2 · medido', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · dos notas a la vez',
             [ac(('C3', 'G3'), 'w'), ac(('A2', 'E3'), 'w')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: Do mayor.',
            'El compás es 4/4. No trae número de metrónomo.',
            'Los números de dedo vienen impresos encima de las notas.',
            'La izquierda toca dos notas a la vez en redonda, una vez por compás.',
            'Hay barras de repetición y una casilla "1.".',
            'Pasa de negras a corcheas en los tres primeros compases.',
        ],
        reto='Tocar los tres primeros compases sin pararte cuando las negras se convierten en '
             'corcheas: no frenes ni aceleres, solo cambia de ritmo.',
        truco='Cuenta "1-2-3-4" con el pie y di "y" entre cada golpe cuando lleguen las '
              'corcheas: "1-y-2-y-3-y-4-y". Las corcheas caen en las "y".',
        sabias='Counting Stars es de OneRepublic y salió en 2013. El arreglo "easy" que tienes '
               'la deja en lo esencial: la melodía en la derecha y un acorde largo debajo.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en cómo la voz empieza despacio y luego va metiendo más sílabas por '
                      'segundo: es exactamente lo que ves en las notas, de negras a corcheas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La pieza se estudia en trozos de tres compases: primero los dedos, después el ritmo '
              'y por último las dos manos. Si falla un dedo, vuelve al principio del trozo.',
        reglas=['LOS DEDOS QUE VIENEN ESCRITOS', 'DE NEGRAS A CORCHEAS', 'LA MANO QUIETA'],
        bloques=[
            dict(num=1, titulo='El c. 3: siete corcheas seguidas',
                 pista='c. 3 · medido sobre tu partitura · un silencio de corchea y siete corcheas '
                       'que suben y bajan',
                 sistemas=[
                     dict(cap='a) el compás tal y como está · el silencio de corchea cuenta: no te lo '
                              'te saltes',
                          events=C3, bars=1),
                     dict(cap='b) la misma forma una nota más arriba · andamio · si te sale a la '
                              'primera, ya tienes el dibujo en la mano',
                          events=[sil('e'), n('G4', 'e'), n('G4', 'e'), n('A4', 'e'), n('B4', 'e'),
                                  n('A4', 'e'), n('G4', 'e'), n('F4', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='De negras a corcheas: el c. 2 contra el c. 1',
                 pista='cc. 1 y 2 · medidos sobre tu partitura · las mismas notas, el doble de '
                       'deprisa',
                 sistemas=[
                     dict(cap='a) negras en el c. 1, corcheas en el c. 2 · en el segundo caben el '
                              'doble de notas en el mismo tiempo',
                          events=[n('E4'), n('G4'), n('E4'), n('D4'),
                                  n('E4', 'e'), n('G4', 'e'), n('E4', 'e'), n('D4', 'e'),
                                  n('E4', 'e'), n('G4', 'e'), n('E4', 'e'), n('D4', 'e')],
                          bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA IZQUIERDA SE ESTUDIA SOLA',
                 texto='La izquierda toca una sola vez por compás, y precisamente por eso es fácil '
                       'equivocarse: tiene tanto tiempo libre que te pones a mirarla. El truco es '
                       'tocar el acorde, soltar y mirar la derecha. Si la izquierda se te escapa, '
                       'tócala sola tres veces antes de juntarla.'),
            dict(num=3, titulo='La izquierda: dos notas a la vez',
                 pista='andamio sobre Do mayor · el intervalo no se mueve dentro del compás, solo '
                       'cambia de nota entre compases',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) tres redondas de dos notas · la mano cambia de forma entre uno y '
                              'otro, pero dentro del compás está quieta',
                          events=[ac(('F2', 'C3'), 'w'), ac(('G2', 'D3'), 'w'),
                                  ac(('C3', 'E3'), 'w')],
                          bars=3, clef='bass'),
                 ]),
            dict(num=4, titulo='Las dos manos: el c. 1',
                 pista='c. 1 · la derecha medida sobre tu partitura · la izquierda es andamio',
                 sistemas=[
                     dict(cap='a) la izquierda toca una vez y aguanta todo el compás · la derecha '
                              'hace las cuatro negras encima',
                          events=[ac(('C2', 'G2', 'D4'), 'q'), ac(('E4',), 'q'), ac(('G4',), 'q'),
                                  ac(('E4',), 'q')],
                          bars=1, manos='sostiene'),
                 ]),
            dict(num=5, titulo='La barra de repetición y la casilla 1',
                 pista='andamio · el signo se lee igual en cualquier pieza · en tu partitura '
                       'localiza dónde está cada uno',
                 sistemas=[
                     dict(cap='a) casilla 1: la primera vez se toca este compás y al llegar a la '
                              'barra de repetición se vuelve atrás',
                          events=[n('E4'), n('D4'), n('C4'), n('D4')],
                          bars=1, repetir='cierra', casilla='1'),
                 ]),
        ] + bloques_extra('Do mayor', 5, 'E4', 'C3',
                          'de negras a corcheas sin frenar y sin acelerar',
                          desde=6, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Counting Stars · para casa',
            intro='Quince minutos al día. Ya sabes leer las cinco notas de tu mano: lo que se entrena '
                  'ahora es no frenar cuando llegan las corcheas.',
            bloques=[
                plan((4, 'La derecha sola, cc. 1-4, con los dedos escritos'),
                     (4, 'Las siete corcheas del c. 3, diez veces'),
                     (4, 'La izquierda sola, solo los acordes largos'),
                     (5, 'Las dos manos, cc. 1-4, sin pararte')),
                metronomo('Empieza a ♩ = 60 con la derecha sola y sube de cuatro en cuatro hasta que '
                          'las corcheas te salgan sin pensar.',
                          'Tu partitura no trae número de metrónomo: la meta la eliges tú y la '
                          'apuntas a lápiz.',
                          titulo='A qué velocidad te sale'),
                verdadero_falso([
                    'Detrás de la clave no hay nada.',
                    'El c. 1 son cuatro negras.',
                    'La izquierda toca corcheas en todos los compases.',
                    'El c. 3 empieza con un silencio de corchea.',
                    'La partitura trae el número de metrónomo.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                inventa(['Dos compases en 4/4.',
                         'Que el primero lleve cuatro negras.',
                         'Que el segundo lleve corcheas y acabe en una blanca.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases como los del principio',
                        pista='con las notas Re, Mi, Sol y Do de tu partitura, pero tuyos'),
                dibujar(['Re', 'Mi', 'Sol', 'Do', 'Fa'],
                        titulo='Dibuja tú las notas',
                        pista='son notas de tu partitura · solo el óvalo, en clave de sol'),
                para_clase('Los cc. 1-4 con las dos manos, y a qué número de metrónomo llegas sin '
                           'que las corcheas se aprieten. Si te pasa que frenas en las corcheas, '
                           'tráelo: se arregla con el pie.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
