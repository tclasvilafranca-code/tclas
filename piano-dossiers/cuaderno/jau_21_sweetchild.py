# -*- coding: utf-8 -*-
"""Sweet Child O' Mine (Guns N' Roses) — pieza 21 de Jaume. ADULTO exigente, sin cifrado.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Sadie King,
   Musescore, 1 página, vectorial, 33 compases), a 250-300 ppp:

     - DOS BEMOLES detrás de la clave: Si♭ y Mi♭ (Si♭ mayor). 4/4. No trae
       tempo. Pone "mf" al empezar y "p (repeat mf)" más adelante.
     - Lleva el PEDAL MARCADO bajo el pentagrama de la izquierda, con corchetes
       compás a compás, barras de repetición (la primera se abre tras el c. 8)
       y dos casillas (1 y 2) al final.
     - La izquierda empieza en redondas; después pasa a acordes y a un dibujo de
       corcheas con silencios.
     - MEDIDO, mano derecha, c. 1 (y se repite igual en los cc. 2-8):
       silencio de corchea · Si♭4 · Fa4 · Mi♭4 · Mi♭5 · Si♭4 · Re5 · Si♭4,
       todo corcheas (el riff).
     - A partir del c. 9 la derecha deja el riff y pasa a una melodía de negras,
       corcheas y blancas con puntillo ligadas (NO sigue en corcheas seguidas).

   Es el mismo arreglo que el de Josep y el de Nel. Aquí lo literal es el c. 1;
   la izquierda va como andamio porque las redondas no se han medido una a una.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, plan, escalera, rodear, escribir, verdadero_falso,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
BB = 'Sib mayor'

# MEDIDO: el riff del c. 1
RIFF = [sil('e'), n('Bb4', 'e'), n('F4', 'e'), n('Eb4', 'e'),
        n('Eb5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('Bb4', 'e')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=21, nivel='intermedio', slug='SweetChild',
    formato='adulto',
    titulo_corto="Sweet Child O' Mine", time_sig=(4, 4), key_sig=BB,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source',
                           "Sweet child o mine G'n Roses"),
    yt='https://www.youtube.com/results?search_query=sweet+child+o+mine+piano+easy',

    ficha=dict(
        titulo="Sweet Child O' Mine",
        autor="Guns N' Roses · arreglo de Sadie King",
        datos=[('Tonalidad', 'Si bemol mayor'), ('Compás', '4/4'),
               ('Carácter', 'mf · sin tempo'), ('Pedal', 'Marcado'),
               ('Páginas', 'Una')],
        titulo_ritmos='El riff del c. 1 y la redonda',
        pie_ritmos='Arriba, medido sobre tu partitura: un silencio de corchea y siete corcheas. '
                   'Abajo, andamio: una redonda aguantada, como la que hay debajo del riff.',
        armonia=dict(
            titulo='El riff que no cambia y el pedal que sí',
            tarjetas=[
                ('EL RIFF', 'Un solo gesto',
                 'En los cc. 1 a 8 la derecha repite el mismo compás: silencio de corchea y siete '
                 'corcheas. La mano casi no se mueve, y por eso hay que oír cómo suena cada vez.'),
                ('EL PEDAL', 'Viene marcado',
                 'Debajo del pentagrama de la izquierda hay corchetes que dicen cuándo se pisa y '
                 'cuándo se suelta, compás a compás. Se cambia justo después del acorde.'),
                ('DOS BEMOLES', 'Si♭ y Mi♭',
                 'La armadura trae dos bemoles: todos los Si y todos los Mi suenan a la tecla '
                 'negra, salvo que un becuadro diga otra cosa.'),
                ('LA ESTRUCTURA', 'Casillas',
                 'A partir del c. 9 hay barras de repetición y, al final, dos casillas. La derecha '
                 'deja el riff y pasa a una melodía de negras, corcheas y blancas ligadas.'),
            ],
            pie='La pieza tiene 33 compases y una sola página. El riff es lo que más se reconoce y lo '
                'que menos cuesta; lo que de verdad se estudia es el pedal.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 1 · medido', RIFF, OCRE, 'treble', BB),
            ('MANO IZQUIERDA', 'andamio · una redonda aguantada con el pedal',
             [ac(('Bb2', 'F3'), 'w')], AZUL, 'bass', BB),
        ],
        especial=[
            'Dos bemoles detrás de la clave: Si♭ y Mi♭.',
            'El compás es 4/4. No trae número de metrónomo.',
            'Pone mf al empezar y p más adelante.',
            'El pedal viene marcado debajo del pentagrama de la izquierda.',
            'Los cc. 1 a 8 repiten el riff en corcheas; a partir del c. 9 es una melodía.',
            'Hay barras de repetición, y dos casillas al final.',
        ],
        reto='Cambiar el pedal justo después del acorde de la izquierda y no con la derecha: si el '
             'pedal cambia con las corcheas, el riff se vuelve un charco.',
        truco='Toca solo la izquierda con el pedal, mirando los corchetes de tu partitura. El pie '
              'sube y baja justo después del acorde, nunca a la vez. Cuando salga solo, pon el '
              'riff encima.',
        sabias="Sweet Child O' Mine salió en 1987, en el disco Appetite for Destruction, y fue el "
               "único número uno de Guns N' Roses en Estados Unidos.",
        qr=dict(titulo='Escúchala',
                texto='Fíjate en que el riff no cambia casi nunca. Lo que cambia debajo es la '
                      'armonía, y es lo que hace que suene distinto cada ocho compases.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='El riff se aprende en diez minutos y el pedal no: primero el pie, después las manos. '
              'La pieza se estudia con el pedal desde el primer día, no al final.',
        reglas=['EL PEDAL CAMBIA DESPUÉS DEL ACORDE', 'EL RIFF, CON LA MANO QUIETA',
                'DOS BEMOLES: SI Y MI'],
        bloques=[
            dict(num=1, titulo='El riff del c. 1, en dos mitades',
                 pista='c. 1 · medido sobre tu partitura · siete corcheas detrás de un silencio',
                 sistemas=[
                     dict(cap='a) la primera mitad: Si♭, Fa y Mi♭ · son tres corcheas que bajan, '
                              'detrás del silencio de corchea',
                          events=[sil('e'), n('Bb4', 'e'), n('F4', 'e'), n('Eb4', 'e'), sil('h')],
                          bars=1, key_sig=BB, matiz='mf'),
                     dict(cap='b) la segunda mitad: Mi♭ agudo, Si♭, Re y Si♭ · el salto del Mi♭ '
                              'grave al agudo es de una octava justa',
                          events=[sil('h'), n('Eb5', 'e'), n('Bb4', 'e'), n('D5', 'e'),
                                  n('Bb4', 'e')],
                          bars=1, show_time=False, key_sig=BB),
                 ]),
            dict(num=2, titulo='La izquierda: una redonda y el pedal',
                 pista='andamio sobre Si♭ mayor · en tu partitura los corchetes del pedal van '
                       'compás a compás, uno por cada redonda',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) dos redondas con el pedal escrito debajo · el pie sube y baja '
                              'JUSTO DESPUÉS del acorde',
                          events=[ac(('Bb2', 'F3'), 'w'), ac(('Eb2', 'Bb2'), 'w')],
                          bars=2, clef='bass', key_sig=BB, pedal=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL PEDAL VA DESPUÉS',
                 texto='El pedal levanta los apagadores y deja sonar todo lo que se toque. Si lo '
                       'cambias a la vez que el acorde, las notas del acorde anterior se quedan '
                       'vivas y se mezclan con las nuevas: el riff se convierte en niebla. Por '
                       'eso en tu partitura el corchete se cierra y se abre justo detrás del '
                       'golpe de la izquierda: primero suena el acorde, después se cambia el '
                       'pie.'),
            dict(num=3, titulo='Las dos manos: el riff sobre la redonda',
                 pista='la derecha es el c. 1, MEDIDA sobre tu partitura · la izquierda es andamio '
                       'sobre Si♭',
                 sistemas=[
                     dict(cap='a) el riff con la izquierda sosteniendo · la mano de abajo toca una '
                              'vez y aguanta todo el compás',
                          events=[ac(('Bb2', 'F3'), 'e'), ac(('Bb4',), 'e'), ac(('F4',), 'e'),
                                  ac(('Eb4',), 'e'), ac(('Eb5',), 'e'), ac(('Bb4',), 'e'),
                                  ac(('D5',), 'e'), ac(('Bb4',), 'e')],
                          bars=1, key_sig=BB, manos='sostiene'),
                 ]),
            dict(num=4, titulo='Los matices: mf al empezar, p después',
                 pista='tu partitura pone mf en el c. 1 y p (repeat mf) más adelante · aquí, '
                       'andamio sobre el mismo material',
                 sistemas=[
                     dict(cap='a) una frase en mezzoforte · el sonido es firme, sin golpear',
                          events=[n('D5'), n('F5'), n('Eb5'), n('D5')], bars=1, key_sig=BB,
                          matiz='mf'),
                     dict(cap='b) la misma frase en piano · se toca con menos peso, no más despacio',
                          events=[n('D5'), n('F5'), n('Eb5'), n('D5')], bars=1, key_sig=BB,
                          matiz='p', show_time=False),
                 ]),
            dict(num=5, titulo='La barra de repetición y las casillas',
                 pista='andamio · el signo se lee igual en cualquier pieza · en tu partitura '
                       'localiza dónde está cada uno',
                 sistemas=[
                     dict(cap='a) la barra de repetición que cierra: se vuelve atrás, y la primera '
                              'vez se toca la casilla 1',
                          events=[n('F5', 'h'), n('D5', 'h'), n('Bb4', 'w')],
                          bars=2, repetir='cierra', casilla='1', key_sig=BB),
                     dict(cap='b) la casilla 2: la segunda vez se salta la 1 y se toca este '
                              'compás, que es el final',
                          events=[n('Bb4', 'w')], bars=1, casilla='2', show_time=False,
                          key_sig=BB),
                 ]),
            dict(num=6, titulo='La izquierda con acordes de tres notas',
                 pista='andamio sobre Si♭ mayor · a partir de la mitad de la pieza la izquierda pasa '
                       'a acordes; las notas exactas están en tu partitura',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) tres acordes de redonda, con la mano abierta · la mano no cambia '
                              'de forma, solo de tecla',
                          events=[ac(('Bb2', 'F3', 'Bb3'), 'w'), ac(('Eb2', 'Bb2', 'Eb3'), 'w'),
                                  ac(('F2', 'C3', 'F3'), 'w')],
                          bars=3, clef='bass', key_sig=BB, pedal=3),
                     dict(cap='b) los mismos acordes de blanca, dos por compás · el pedal cambia '
                              'con cada acorde',
                          events=[ac(('Bb2', 'F3', 'Bb3'), 'h'), ac(('Eb2', 'Bb2', 'Eb3'), 'h'),
                                  ac(('F2', 'C3', 'F3'), 'h'), ac(('Bb2', 'F3', 'Bb3'), 'h')],
                          bars=2, clef='bass', key_sig=BB, show_time=False, pedal=3),
                 ]),
            dict(num=7, titulo='La melodía: blanca con puntillo ligada',
                 pista='andamio sobre Si♭ mayor · desde el c. 9 la derecha abandona el riff y '
                       'canta; las notas exactas están en tu partitura',
                 sistemas=[
                     dict(cap='a) corcheas que se ligan a una nota larga · la ligadura une las dos '
                              'duraciones y se toca una sola vez',
                          events=[n('F4', 'e'), n('F4', 'e'), n('F4', 'e'), dict(pitch='D5', dur='e', lig=True),
                                  n('D5', 'h.'), sil('h.')],
                          bars=2, key_sig=BB),
                 ]),
        ] + bloques_extra(BB, 21, 'D5', 'Bb2',
                          'el pedal después del acorde y el riff con la mano quieta',
                          desde=8, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="Sweet Child O' Mine · para casa",
            intro='Veinte minutos al día. El riff se aprende pronto; lo que lleva trabajo es el '
                  'pedal y que el riff no se acelere.',
            bloques=[
                plan((5, 'Solo la izquierda con el pedal, mirando los corchetes de tu partitura'),
                     (5, 'El riff del c. 1 con la derecha, sin pedal'),
                     (6, 'Riff y pedal juntos, cc. 1-4'),
                     (4, 'Los cc. 1-8 de una vez, sin parar')),
                escalera((60, 'el riff con la derecha, sin pedal'),
                         (72, 'riff y pedal, cuatro compases'),
                         (84, 'los cc. 1-8'),
                         (96, 'la pieza hasta la primera barra de repetición'),
                         meta='Tu partitura no trae número de metrónomo: la meta la eliges tú y la '
                              'apuntas a lápiz.',
                         titulo='La escalera del metrónomo'),
                dict(rodear([[sil('e'), n('Bb4', 'e'), n('F4', 'e'), n('Eb4', 'e'),
                              n('Eb5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('Bb4', 'e')],
                             [sil('e'), n('Bb4', 'e'), n('F4', 'e'), n('Eb4', 'e'),
                              n('Eb5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('F5', 'e')],
                             [sil('e'), n('Bb4', 'e'), n('F4', 'e'), n('Eb4', 'e'),
                              n('Eb5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('Bb4', 'e')],
                             [sil('e'), n('Bb4', 'e'), n('F4', 'e'), n('D4', 'e'),
                              n('Eb5', 'e'), n('Bb4', 'e'), n('D5', 'e'), n('Bb4', 'e')]],
                            titulo='Rodea los dos compases que son iguales',
                            pista='dos son el c. 1 de tu partitura · los otros llevan una nota '
                                  'cambiada · el pentagrama es nuestro, la partitura es la tuya'),
                     clef='treble'),
                escribir(titulo='Copia aquí el c. 1 de la derecha de tu partitura',
                         pista='un silencio de corchea y siete corcheas · y escribe debajo el '
                               'nombre de cada nota'),
                verdadero_falso([
                    'La armadura trae dos bemoles.',
                    'El pedal está marcado debajo del pentagrama de la izquierda.',
                    'La partitura trae un número de metrónomo.',
                    'La derecha empieza con un silencio de corchea.',
                    'En el c. 1 la izquierda toca corcheas.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                para_clase('Los cc. 1-8 con riff y pedal, y dime si el pedal te arrastra el riff o '
                           'si se limpia bien. Si se te empasta, tráelo: se arregla con el pie, no '
                           'con las manos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
