# -*- coding: utf-8 -*-
"""Jailhouse Rock — pieza 7 de Jaume. Formato ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (Elvis Presley, arreglo de
   Sadie King, Musescore, 1 página, 20 compases), mirado a 100 y a 300 dpi:

     - Detrás de la clave no hay nada, pero la pieza no es Do mayor limpio: lleva
       **Mi♭**, Fa♯ y Si♭ escritos delante de las notas. Es blues.
     - 4/4, "♩ = 150" y "Swing", "mf" al empezar y "f" en el c. 12, con un
       regulador en el c. 11.
     - **EMPIEZA CON SILENCIO**: el c. 1 de la derecha es un silencio de blanca,
       un silencio de corchea y un **Mi♭4 de negra con puntillo** (MEDIDO a 300
       dpi: la cabeza va en la primera línea y lleva el bemol delante). Después
       viene una barra de repetición.
     - El c. 2 es un Mi4 de redonda (con el becuadro implícito: ya no es Mi♭) y
       el c. 3 un Mi4 de blanca, silencio de corchea y otro Mi♭4 de negra con
       puntillo.
     - La izquierda empieza con dos notas a la vez (dobles notas, con Fa♯) y a
       partir del c. 12 hace **cuatro negras que suben con la digitación 5 · 3 ·
       2 · 1 impresa debajo**: Fa · La · Do · Re (medido por Josep sobre el
       mismo archivo y comprobado aquí a 100 dpi).
     - Hay un tremolo sobre un Si♭ de redonda hacia el final y la palabra
       **"ritardando"** sobre el c. 19.

   Es el mismo archivo que el de Josep y José María; lo literal coincide y lo
   inventado no. Aquí el trabajo va por la **entrada con silencios**, el Mi♭
   frente al Mi natural y los cuatro compases de la izquierda que suben.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, escalera, inventa, teclado,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=7, nivel='intermedio', slug='JailhouseRock',
    formato='adulto',
    titulo_corto='Jailhouse Rock', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source',
                           'Jailhouse Elvis Presley'),
    yt='https://www.youtube.com/results?search_query=jailhouse+rock+piano+easy',

    ficha=dict(
        titulo='Jailhouse Rock',
        autor='Elvis Presley · arreglo de Sadie King',
        datos=[('Tonalidad', 'Do · con blues'), ('Compás', '4/4'),
               ('Tempo', '♩ = 150 Swing'), ('Empieza', 'Con silencios'),
               ('Páginas', 'Una')],
        titulo_ritmos='La entrada y la izquierda que sube',
        pie_ritmos='Arriba, medido sobre tu partitura: silencio de blanca, silencio de corchea y '
                   'Mi bemol. Abajo, medido: Fa, La, Do y Re del c. 12. Los dedos, en tu partitura.',
        armonia=dict(
            titulo='La pieza rápida, y con un Mi bemol',
            tarjetas=[
                ('♩ = 150', 'Con swing',
                 'Es el tempo más alto del cuaderno hasta ahora. Las corcheas se escriben iguales '
                 'y se tocan desiguales; a esta velocidad, con las dos manos, no se puede '
                 'pensar cada una.'),
                ('LA ENTRADA', 'Silencio primero',
                 'El c. 1 de la derecha es un silencio de blanca, otro de corchea y solo entonces '
                 'un Mi♭ largo. La pieza no arranca en el uno: arranca en el tres y medio.'),
                ('EL MI BEMOL', 'Y el Mi natural',
                 'La nota de blues. El c. 1 trae un Mi♭ y el c. 2 un Mi natural: los separan una '
                 'tecla negra y una barra de repetición, y el oído tiene que notarlo.'),
                ('EL C. 12', 'La izquierda sube',
                 'Cuatro negras que suben, con la digitación 5 · 3 · 2 · 1 impresa debajo: Fa, La, '
                 'Do y Re. Es la única digitación escrita de la página.'),
            ],
            pie='Hay dos formas de equivocarse con esta pieza: tocarla rápida antes de tocarla '
                'limpia, y olvidar que acaba frenando. El "ritardando" del final no es un adorno: '
                'es parte de la pieza, y si la haces rápida de punta a punta, la has tocado mal.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido',
             [sil('h'), sil('e'), n('Eb4', 'q.')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'c. 12 · medido: los cuatro dedos que suben',
             [n('F3'), n('A3'), n('C4'), n('D4')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, pero hay Mi bemol, Fa sostenido y Si bemol escritos delante.',
            'Pone "♩ = 150 Swing": rápido y balanceado, y el primer compás es "mf".',
            'La pieza empieza con tres silencios seguidos y entra con un Mi♭ de negra con puntillo.',
            'En el c. 12 la izquierda sube con los dedos 5 · 3 · 2 · 1 impresos debajo.',
            'Al final hay un Si♭ de redonda con tremolo y la palabra "ritardando".',
            'La izquierda empieza con dobles notas, dos a la vez.',
        ],
        reto='Contar el compás de entrada a ♩ = 150. El silencio de blanca más el de corchea dura '
             'dos segundos y cuarto: hay que contarlo, no sentirlo, y entrar en el tiempo justo.',
        truco='Pon el metrónomo a ♩ = 60 y cuenta el c. 1 en voz alta, "uno, dos, tres, y", y '
              'entra con el Mi♭ en el cuatro. Cuando entres limpio cinco veces seguidas, sube cinco. '
              'A 150 la entrada ya la sabes de memoria.',
        sabias='Elvis la grabó en 1957 para la película del mismo nombre. La secuencia de baile de '
               'la cárcel fue coreografiada por él mismo, y es una de las escenas de baile más '
               'recordadas del cine de los cincuenta.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en la entrada: la voz espera medio compás y la guitarra no entra '
                      'hasta el cuatro. Es el mismo silencio que tu mano derecha tiene que '
                      'contar antes del Mi bemol.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia por tres lados que no tienen que ver con la velocidad: la entrada con '
              'silencios, el Mi♭ frente al Mi natural y la izquierda que sube. La velocidad se '
              'sube por escalones, y la última.',
        reglas=['LA ENTRADA SE CUENTA', 'MI♭ Y MI, DOS TECLAS', 'LA VELOCIDAD, LA ÚLTIMA'],
        bloques=[
            dict(num=1, titulo='La entrada: tres silencios y un Mi bemol',
                 pista='c. 1 · MEDIDO sobre tu partitura · silencio de blanca, silencio de corchea '
                       'y Mi♭ con puntillo',
                 sistemas=[
                     dict(cap='a) el c. 1 literal, dos veces · cuenta "uno, dos, tres, y" y entra en el cuatro',
                          events=[sil('h'), sil('e'), n('Eb4', 'q.'),
                                  sil('h'), sil('e'), n('Eb4', 'q.')],
                          bars=2, matiz='mf'),
                 ]),
            dict(num=2, titulo='El Mi bemol y el Mi natural, uno detrás de otro',
                 pista='cc. 1-3 · leído de tu partitura · con la barra de repetición entre el c. 1 '
                       'y el c. 2',
                 sistemas=[
                     dict(cap='a) la entrada, la redonda de Mi natural y la entrada otra vez · '
                              'fíjate en que el Mi del medio no lleva bemol',
                          events=[sil('h'), sil('e'), n('Eb4', 'q.'),
                                  n('E4', 'w'),
                                  n('E4', 'h'), sil('e'), n('Eb4', 'q.')],
                          bars=3, repetir='abre'),
                 ]),
            dict(num=3, titulo='La izquierda del c. 12: Fa, La, Do, Re',
                 pista='c. 12 · MEDIDO · digitación 5 · 3 · 2 · 1 impresa debajo en tu partitura',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) el c. 12 literal y luego bajando por las mismas notas (andamio) · escribe tú los '
                              'dedos encima y compruébalos · el 5 es el meñique',
                          events=[n('F3'), n('A3'), n('C4'), n('D4'),
                                  n('D4'), n('C4'), n('A3'), n('F3')],
                          bars=2, clef='bass', matiz='f'),
                     dict(cap='b) la misma forma desde el Do, para que el dedo aprenda la distancia '
                              'y no la nota · andamio',
                          events=[n('C3'), n('E3'), n('G3'), n('A3'),
                                  n('G3'), n('B3'), n('D4'), n('E4')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTA LA ENTRADA CON LA BOCA',
                 texto='A ♩ = 150 un compás dura menos de dos segundos y medio. Con las manos '
                       'quietas y sin sonido, el cerebro deja de contar a mitad del silencio. '
                       'Decirlo en voz alta lo obliga a seguir. En clase, la profesora te va a '
                       'quitar el metrónomo sonoro y te dejará solo con la boca.'),
            dict(num=4, titulo='El regulador del c. 11, y el f del c. 12',
                 pista='cc. 11-12 · andamio de un compás de crescendo y uno de f',
                 sistemas=[
                     dict(cap='a) la curva empieza en el c. 11 y llega al f en el c. 12 · el '
                              'crescendo no es más rápido, es más peso',
                          events=[n('G4'), n('G4'), n('Bb4'), n('G4'),
                                  n('C5', 'w')],
                          bars=2, matiz='mf', cresc=4),
                 ]),
            dict(num=5, titulo='Las dos manos del c. 12',
                 pista='c. 12 · la derecha tiene una redonda de Do y la izquierda sube',
                 sistemas=[
                     dict(cap='a) la derecha sostiene el Do mientras la izquierda sube, y ninguna '
                              'de las dos corre · si se te adelanta la izquierda, cuenta en voz alta',
                          events=[ac(('F3', 'C5')), n('A3'), n('C4'), n('D4')],
                          bars=1, manos='sostiene'),
                 ]),
        ] + bloques_extra('Do mayor', 7, 'C5', 'C3',
                          'el blues: la nota de paso no es un error, es el estilo',
                          desde=6, time_sig=(4, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Jailhouse Rock · para casa',
            intro='Veinte minutos al día, y ni uno a 150. Esta semana se sube por escalones.',
            bloques=[
                reto('Llegar a ♩ = 150 sin haber ensuciado nada por el camino.',
                     'Tres veces limpias y subes cinco. Un fallo y bajas cinco. Apunta cada día el '
                     'número en que te has quedado: la semana que viene se empieza ahí.'),
                plan((4, 'Contar el compás de entrada y entrar, diez veces'),
                     (5, 'El Mi bemol y el Mi natural, uno detrás de otro, sin mirar'),
                     (6, 'La melodía por escalones de metrónomo'),
                     (5, 'La izquierda del c. 12 con los dedos 5 3 2 1')),
                escalera((60, 'la entrada y el primer compás'),
                         (90, 'los cuatro primeros compases'),
                         (120, 'la pieza sin el final'),
                         (150, 'la pieza entera, con el ritardando'),
                         meta='♩ = 150, que es lo que pone tu partitura.',
                         titulo='La escalera del metrónomo'),
                inventa(['Dos compases de cuatro golpes.',
                         'Empieza con un silencio de blanca y un silencio de corchea.',
                         'Que el primer sonido sea un Mi bemol de negra con puntillo.'],
                        time_sig=(4, 4),
                        titulo='Inventa dos compases con la misma entrada',
                        pista='como el c. 1, pero los dos compases son tuyos'),
                teclado({2: 1, 3: 2},
                        ['Escribe el nombre de la tecla 1: es el Mi natural del c. 2.',
                         'El Mi bemol del c. 1 es la tecla negra justo a su izquierda: '
                         'dibújala y escribe entre qué dos teclas blancas está.'],
                        titulo='En el teclado',
                        pista='las dos teclas salen de los cc. 1 y 2 de tu partitura'),
                para_clase('El número de metrónomo al que te has quedado, y la entrada. Si la '
                           'izquierda del c. 12 te descoloca, tráela: se arregla mirando los dedos '
                           'impresos una vez.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
