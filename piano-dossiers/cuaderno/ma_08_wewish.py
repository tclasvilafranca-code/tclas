# -*- coding: utf-8 -*-
"""We Wish You a Merry Christmas — pieza 8 de Martina (NAVIDAD, una semana). ADULTO
   exigente, tono de niña que empieza de cero.

   Lo comprobado sobre el PDF de su carpeta de Drive (arr. Gilbert DeBenedetti,
   "more words on next page", 2 páginas: la primera es la música y la segunda, la
   letra; imagen a 354 ppp), mirado a 250 ppp compás a compás:

     - UN SOSTENIDO detrás de la clave: Sol mayor. 3/4. No trae tempo.
     - Anacrusa de un solo golpe: la derecha empieza con un Re4 de negra.
     - Trae CIFRADO impreso (G, C, A7, D, B7, Am, D7), la letra debajo de la melodía y
       la digitación impresa. 16 compases con la anacrusa, y la palabra "CHORUS" en el c. 8.
     - Solo negras, blancas y parejas de corcheas.
     - MEDIDO, mano derecha:
       anacrusa: Re4 (negra)
       c. 1: Sol4 (negra) · Sol4 · La4 · Sol4 · Fa♯4 (corcheas)
       c. 2: Mi4 · Mi4 · Mi4 (negras)
       c. 3: La4 (negra) · La4 · Si4 · La4 · Sol4 (corcheas)
       c. 4: Fa♯4 · Re4 · Re4 (negras)
       c. 5: Si4 (negra) · Si4 · Do5 · Si4 · La4 (corcheas)
       c. 6: Sol4 · Mi4 (negras) · Re4 · Re4 (corcheas)
       c. 7: Mi4 · La4 · Fa♯4 (negras)
       c. 8: Sol4 (blanca) · Re4 (negra)
     - La izquierda toca un acorde o una nota por compás, y cambia con las letras.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, reto, plan, escalera, inventa, teclado,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

# MEDIDO: derecha, anacrusa y cc. 1-8
ENTRADA = [sil('h'), n('D4')]
C1 = [n('G4'), n('G4', 'e'), n('A4', 'e'), n('G4', 'e'), n('F#4', 'e')]
C2 = [n('E4'), n('E4'), n('E4')]
C3 = [n('A4'), n('A4', 'e'), n('B4', 'e'), n('A4', 'e'), n('G4', 'e')]
C4 = [n('F#4'), n('D4'), n('D4')]
C5 = [n('B4'), n('B4', 'e'), n('C5', 'e'), n('B4', 'e'), n('A4', 'e')]
C6 = [n('G4'), n('E4'), n('D4', 'e'), n('D4', 'e')]
C7 = [n('E4'), n('A4'), n('F#4')]
C8 = [n('G4', 'h'), n('D4')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=8, nivel='iniciación', slug='WeWish',
    formato='adulto',
    titulo_corto='We Wish You a Merry...', time_sig=(3, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'We Wish You a Merry'),
    yt='https://www.youtube.com/results?search_query=we+wish+you+a+merry+christmas+easy+piano',

    ficha=dict(
        titulo='We Wish You a Merry Christmas',
        autor='Villancico inglés · arr. Gilbert DeBenedetti · NAVIDAD',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '3/4'),
               ('Carácter', 'Sin tempo impreso'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Dos')],
        titulo_ritmos='La entrada y el c. 1, medidos',
        pie_ritmos='Arriba, medido sobre tu partitura: entras con una sola nota, el Re, y el c. 1 es '
                   'una negra y cuatro corcheas. Abajo, andamio: el acorde de G de la izquierda.',
        armonia=dict(
            titulo='Un villancico con un sostenido y un solo golpe de entrada',
            tarjetas=[
                ('EL SOSTENIDO', 'Fa, tecla negra',
                 'Detrás de la clave hay un sostenido, y está en el Fa: todos los Fa de esta pieza '
                 'se tocan con la tecla negra de la derecha del Fa. Es lo único nuevo.'),
                ('LA ENTRADA', 'Un solo golpe',
                 'La canción no empieza en el primer compás: antes hay una sola nota, el Re, que '
                 'cae en el tercer golpe del compás que falta. Entras justo antes del "uno".'),
                ('LAS LETRAS', 'G, C, A7, D…',
                 'Encima de la melodía hay letras: son los acordes. G, C, D, Am… Cada letra manda '
                 'sobre el trozo de música que tiene debajo, hasta la siguiente letra.'),
                ('LAS CORCHEAS', 'Dos en un golpe',
                 'Hay parejas de corcheas, dos notas rápidas que caben en un solo golpe. Se '
                 'cuentan "tres-y" y se tocan sin acelerar.'),
            ],
            pie='La melodía la sabes de oído, así que el trabajo es ponerle nombre: qué nota es '
                'cada una, y dónde está el Fa sostenido.',
        ),
        ritmos=[
            ('MANO DERECHA', 'anacrusa y c. 1 · medido', ENTRADA + C1, OCRE, 'treble', SOL),
            ('MANO IZQUIERDA', 'andamio · acorde de G, una blanca con puntillo',
             [ac(('G2', 'D3', 'B3'), 'h.'), ac(('E3', 'G3', 'C4'), 'h.')], AZUL, 'bass', SOL),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: el Fa. Es Sol mayor.',
            'El compás es 3/4 y no trae número de metrónomo.',
            'Empieza con una sola nota, un Re, antes del primer compás.',
            'Encima de la melodía van las letras de los acordes: G, C, A7, D, B7, Am y D7.',
            'La letra de la canción va impresa debajo de la melodía, y la partitura trae dedos.',
            'La segunda página es solo la letra de las cuatro estrofas.',
        ],
        reto='Entrar a tiempo con una sola nota. Como no hay nada antes, hay que contar el '
             'compás que falta "uno, dos" en silencio y tocar el Re en el tres.',
        truco='Cuenta "uno, dos" y entra en el "tres". Si dudas, canta por dentro la palabra '
              '"We": es justo la primera nota. Cuando la oigas en la cabeza, tócala.',
        sabias='We Wish You a Merry Christmas es un villancico inglés de hace más de 400 años. '
               'Antes se cantaba por las casas, y la tercera estrofa dice "no nos iremos hasta que '
               'nos des algo": era una forma de pedir el aguinaldo.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los golpes de la entrada mientras suena: "uno, dos" y entra la voz en '
                      'el "tres". Es lo que vas a hacer tú con el Re.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La melodía ya la sabes: aquí se aprende a escribirla con notas. Primero la entrada, '
              'después cada frase, y el Fa sostenido se marca con lápiz antes de tocar.',
        reglas=['EL FA, A LA TECLA NEGRA', 'LA ENTRADA SE CUENTA', 'UNA FRASE CADA VEZ'],
        bloques=[
            dict(num=1, titulo='La entrada y los dos primeros compases',
                 pista='anacrusa y cc. 1-2 · medidos sobre tu partitura · entras con el Re y sigue la '
                       'frase',
                 sistemas=[
                     dict(cap='a) cuenta "uno, dos" en silencio y entra con el Re en el tres · '
                              'después, una negra y cuatro corcheas que acaban en Fa sostenido, y '
                              'tres Mi',
                          events=ENTRADA + C1 + C2, bars=3, key_sig=SOL),
                 ]),
            dict(num=2, titulo='Los tres compases siguientes, cc. 2-4',
                 pista='cc. 2-4 · medidos sobre tu partitura · tres Mi iguales, otra frase y el Fa '
                       'sostenido que baja',
                 sistemas=[
                     dict(cap='a) Mi, Mi, Mi; La y cuatro corcheas; y Fa sostenido, Re, Re · la '
                              'segunda frase empieza igual que la primera pero una nota más '
                              'arriba',
                          events=C2 + C3 + C4, bars=3, key_sig=SOL, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL FA ES SIEMPRE NEGRO',
                 texto='El sostenido que está pegado a la clave vale para toda la canción, no solo '
                       'para una nota. Cada vez que aparezca un Fa, aunque sea en otro compás o en '
                       'otra línea, se toca la tecla negra. Por eso se escribe una vez al principio '
                       'y no delante de cada nota.'),
            dict(num=3, titulo='La parte del medio, cc. 5-8',
                 pista='cc. 5-8 · medidos sobre tu partitura · las dos frases que suben y la '
                       'blanca que cierra',
                 sistemas=[
                     dict(cap='a) Si y Do; Sol, Mi, Re, Re; Mi, La, Fa sostenido; y Sol de blanca · '
                              'la blanca dura dos golpes, aguántala entera',
                          events=C5 + C6 + C7 + C8, bars=4, key_sig=SOL),
                 ]),
            dict(num=4, titulo='El acorde de la izquierda',
                 pista='andamio sobre las letras IMPRESAS en tu partitura (G, C, D) · el acorde '
                       'entero, las tres notas a la vez',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) G, C y D, cada uno una blanca con puntillo · las tres notas '
                              'bajan a la vez y se aguantan los tres golpes',
                          events=[ac(('G2', 'B2', 'D3'), 'h.'), ac(('C3', 'E3', 'G3'), 'h.'),
                                  ac(('D3', 'F#3', 'A3'), 'h.')],
                          bars=3, clef='bass', key_sig=SOL),
                 ]),
            dict(num=5, titulo='Las dos manos, el primer compás',
                 pista='el c. 1 de la derecha es MEDIDO · el acorde de la izquierda es andamio',
                 sistemas=[
                     dict(cap='a) el acorde de G suena en el uno y se queda · la melodía hace '
                              'una negra y cuatro corcheas encima',
                          events=[ac(('G2', 'B2', 'D3', 'G4'), 'q'), n('G4', 'e'), n('A4', 'e'),
                                  n('G4', 'e'), n('F#4', 'e')],
                          bars=1, key_sig=SOL, manos='sostiene'),
                 ]),
        ] + bloques_extra(SOL, 8, 'G4', 'G2',
                          'el Fa sostenido y la entrada con un solo golpe',
                          desde=6, time_sig=(3, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='We Wish You a Merry Christmas · para casa',
            intro='Diez o quince minutos al día. Es la semana corta de Navidad, y la melodía ya la '
                  'sabes: lo que se entrena es leerla con notas.',
            bloques=[
                reto('Tocar los cc. 1-8 con el Fa sostenido a la primera, tres veces seguidas, y '
                     'entrando a tiempo con el Re.',
                     'Cuenta "uno, dos" en silencio y entra en el tres. Si una vez tocas el Fa '
                     'blanco, vuelves a cero: tres limpias seguidas, no tres en total.'),
                plan((3, 'Marcar el Fa con un círculo de lápiz en tu partitura'),
                     (4, 'La derecha sola, cc. 1-4, contando la entrada'),
                     (4, 'La derecha sola, cc. 5-8'),
                     (4, 'La izquierda: los acordes G, C y D, uno por compás')),
                escalera((60, 'la derecha sola, cc. 1-4'),
                         (72, 'la derecha sola, cc. 1-8'),
                         (84, 'las dos manos, cc. 1-8'),
                         (96, 'la meta que te pones tú: la partitura no la trae'),
                         meta='Tu partitura no trae número de metrónomo: la meta la pones tú y la '
                              'apuntas a lápiz.',
                         titulo='La escalera del metrónomo'),
                inventa(['Dos compases en 3/4.',
                         'Que empiecen con una negra y cuatro corcheas.',
                         'Que acaben en tres negras iguales.'],
                        time_sig=(3, 4),
                        titulo='Inventa dos compases como los del principio',
                        pista='con las notas Sol, La, Si y Mi de tu partitura, pero tuyos'),
                teclado({4: 1, 5: 2, 2: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         'La número 1 es el Sol, la nota con la que empieza el compás 1.'],
                        titulo='En el teclado',
                        pista='son tres notas de las primeras frases · el Fa sostenido es negra y '
                              'no está marcado'),
                para_clase('Los cc. 1-8 con la derecha, y si el Fa te ha salido siempre a la tecla '
                           'negra. Cántamela primero y luego la tocas: así vemos si la mano sigue '
                           'a la voz.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
