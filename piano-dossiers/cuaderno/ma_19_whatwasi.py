# -*- coding: utf-8 -*-
"""What Was I Made For? (Billie Eilish) — pieza 19 de Martina. ADULTO exigente, con cifrado, tono de niña.

   Lo comprobado sobre el PDF de su carpeta de Drive (versión de Musescore, 2
   páginas, 50 compases, vectorial), a 250 ppp, cabeza a cabeza:

     - Detrás de la clave no hay nada: DO MAYOR. 4/4, y arriba va el metrónomo
       **negra = 78**.
     - Va a dos manos, a dos pentagramas, con la LETRA debajo de la melodía y el
       CIFRADO encima: C · Em · F · Am · Dm · G.
     - Los cc. 1 a 3 son tres compases enteros de silencio en la derecha, con
       solo los acordes de la izquierda (C y Em, F, C y Em).
     - MEDIDO, mano derecha:
       c. 4: silencio de blanca, Si4 y Do5 (corcheas), Do5 (semicorchea,
             ligada al Do5 anterior), Mi4 (semicorchea), Sol4 (corchea, ligada
             a la negra del compás siguiente).
       c. 5: Sol4 (negra), silencio de negra y Si4 · Do5 · Mi4 · Sol4 (corcheas).
     - LLEVA SEMICORCHEAS (c. 4 y varios más) y ligaduras de unión.
     - Trae signos de repetición, con una casilla 1 y una casilla 2.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, reto, plan, cifrado, verdadero_falso, figuras,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# MEDIDO: cc. 4 y 5, mano derecha
C4 = [sil('h'), n('B4', 'e'), dict(pitch='C5', dur='e', lig=True), n('C5', 's'),
      n('E4', 's'), dict(pitch='G4', dur='e', lig=True)]
C5 = [n('G4'), sil('q'), n('B4', 'e'), n('C5', 'e'), n('E4', 'e'), n('G4', 'e')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=19, nivel='intermedio', slug='WhatWasIMadeFor',
    formato='adulto',
    titulo_corto='What Was I Made For?', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source',
                           'What-was-i-made-for-billie-eilish'),
    yt='https://www.youtube.com/results?search_query=what+was+i+made+for+billie+eilish+piano+tutorial',

    ficha=dict(
        titulo='What Was I Made For?',
        autor='Billie Eilish · versión para piano de Musescore',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 78'), ('Cifrado', 'C Em F Am Dm G'),
               ('Estructura', 'Con repeticiones')],
        titulo_ritmos='La entrada del c. 4, medida',
        pie_ritmos='Arriba, medido sobre tu partitura: el c. 4 entero. Abajo, andamio: '
                   'los tres acordes con que arranca la izquierda (C, Em y F), solo con bajo y quinta.',
        armonia=dict(
            titulo='Tres compases de silencio y una melodía que se mueve poco',
            tarjetas=[
                ('LA ENTRADA', 'Cuatro compases',
                 'La derecha no toca en los cc. 1 a 3: solo suena la izquierda con C, Em y F. '
                 'Entra en el c. 4, con una blanca de silencio y un Si, así que hay que contar los '
                 'tres compases vacíos.'),
                ('EL CIFRADO', 'Seis letras',
                 'Seis letras en toda la pieza. Casi todo se mueve entre C, Em y F; Am, Dm y G '
                 'salen poco, y casi siempre al final de una frase.'),
                ('EL RITMO', 'Con ligaduras',
                 'En el c. 4 hay una corchea ligada a una semicorchea, y una semicorchea más. '
                 'Rápidas, pero dentro de un pulso lento: la dificultad está en la ligadura, no en '
                 'la velocidad.'),
                ('LAS REPETICIONES', 'Casilla 1 y casilla 2',
                 'La partitura trae signos de repetición y dos finales, marcados 1 y 2. Antes de '
                 'tocar, localiza dónde vuelve cada signo.'),
            ],
            pie='Son dos páginas, 50 compases y la letra impresa debajo: el texto de la canción ayuda '
                'a ver dónde respira cada frase.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 4 · medido', C4, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · C, Em y F, bajo y quinta',
             [ac(('C3', 'G3'), 'w'), ac(('E3', 'B3'), 'h'),
              ac(('F3', 'C4'), 'h')],
             AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: Do mayor, sin una sola alteración en la armadura.',
            'El compás es 4/4 y arriba viene impreso el metrónomo: negra = 78.',
            'Los cc. 1 a 3 son tres compases de silencio en la derecha, con solo la izquierda.',
            'Encima del pentagrama va el cifrado: C, Em, F, Am, Dm y G.',
            'Lleva semicorcheas y ligaduras de unión (c. 4 y varios más).',
            'Trae signos de repetición, con una casilla 1 y una casilla 2.',
        ],
        reto='Entrar en el c. 4 después de tres compases de silencio. Sin nadie que te dé la nota, el '
             'Si de la entrada es el único que se oye solo, y hay que acertarlo a la primera.',
        truco='Cuenta los tres compases en voz alta, uno-dos-tres-cuatro cada vez, y canta mentalmente '
              'el Si antes de tocarlo. Si dudas del Si, recuerda que es la línea central del '
              'pentagrama de sol.',
        sabias='Billie Eilish y su hermano Finneas la escribieron para la película Barbie, de 2023. '
               'Ganó el Óscar a la mejor canción original en 2024.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo entra la melodía: casi hablada, y sin prisa. Esa calma es lo '
                      'que tiene que oírse en tus semicorcheas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La pieza tiene poco que tocar y mucho que oír: se estudia sin prisa, y la derecha no '
              'empieza hasta el c. 4. Lo difícil no es la velocidad, es esperar bien.',
        reglas=['TRES COMPASES DE ESPERA', 'LA LIGADURA, ANTES QUE LA SEMICORCHEA',
                'LOS ACORDES POR LETRAS'],
        bloques=[
            dict(num=1, titulo='Los tres compases de espera, y la entrada',
                 pista='cc. 1-4 · medido sobre tu partitura · la derecha calla tres compases',
                 sistemas=[
                     dict(cap='a) tres compases de silencio de redonda y el c. 4, con la blanca de '
                              'silencio que precede al Si · la entrada es lo único que se oye solo',
                          events=[sil('w'), sil('w'), sil('w')] + C4, bars=4),
                 ]),
            dict(num=2, titulo='La figura del c. 4, aislada',
                 pista='c. 4 · la corchea ligada a la semicorchea, y la semicorchea que le sigue',
                 sistemas=[
                     dict(cap='a) la figura sin el silencio · el Do5 de la corchea no se vuelve a '
                              'tocar: la ligadura lo alarga hasta la semicorchea',
                          events=[n('B4', 'e'), dict(pitch='C5', dur='e', lig=True),
                                  n('C5', 's'), n('E4', 's'), dict(pitch='G4', dur='e', lig=True),
                                  n('G4', 'h')],
                          bars=1),
                     dict(cap='b) el mismo dibujo una nota más grave, para que la mano lo aprenda sin '
                              'depender de las notas · andamio',
                          events=[n('F4', 'e'), dict(pitch='G4', dur='e', lig=True),
                                  n('G4', 's'), n('B3', 's'), dict(pitch='D4', dur='e', lig=True),
                                  n('D4', 'h')],
                          bars=1, show_time=False),
                 ]),
            dict(num=3, titulo='Los cc. 4 y 5 con la izquierda sosteniendo',
                 pista='melodía MEDIDA sobre tu partitura · los acordes de la izquierda son andamio '
                       'sobre el cifrado impreso (F, C y Em)',
                 sistemas=[
                     dict(cap='a) la izquierda aguanta el acorde de F en el c. 4, y cambia a C y a '
                              'Em en el c. 5 · no se mueve hasta el cambio de letra',
                          events=[ac(('F2', 'C3'), 'h'),
                                  ac(('B4',), 'e'), ac(('C5',), 'e'),
                                  ac(('C5',), 's'), ac(('E4',), 's'), ac(('G4',), 'e'),
                                  ac(('C2', 'E2', 'G2', 'G4'), 'q'), sil('q'),
                                  ac(('E2', 'G2', 'B2', 'B4'), 'e'), ac(('C5',), 'e'),
                                  ac(('E4',), 'e'), ac(('G4',), 'e')],
                          bars=2, manos='sostiene'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA SEMICORCHEA NO SE CORRE',
                 texto='Con la negra a 78 el pulso es tranquilo, y una semicorchea dura la cuarta '
                       'parte de ese pulso: a esa velocidad no se toca deprisa, se toca justo. Lo '
                       'que hace que suene mal es acortarla, no alargarla. Si dudas, di "ta-ta-ta-ta" '
                       'cuatro veces por pulso con el metrónomo, y solo después pon las notas.'),
            dict(num=4, titulo='Los acordes que salen menos: Am, Dm y G',
                 pista='andamio sobre el cifrado IMPRESO en tu partitura · aparecen al final de las '
                       'frases',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) uno por compás, en bloque · Am y Dm comparten el La, y G cierra '
                              'con el Si, que es el que más tira hacia el Do',
                          events=[ac(('A2', 'E3', 'A3'), 'w'), ac(('D2', 'A2', 'D3'), 'w'),
                                  ac(('G2', 'D3', 'G3'), 'w')],
                          bars=3, clef='bass'),
                 ]),
            dict(num=5, titulo='Las repeticiones y las dos casillas',
                 pista='andamio · el signo se lee igual en cualquier pieza · en tu partitura '
                       'localiza dónde está cada uno',
                 sistemas=[
                     dict(cap='a) la primera vez se toca el compás de la casilla 1, y al llegar a '
                              'la barra de repetición se vuelve atrás',
                          events=[n('E4', 'h'), n('G4', 'h'), n('A4', 'h'), n('G4', 'h')],
                          bars=2, repetir='cierra', casilla='1'),
                     dict(cap='b) la segunda vez se salta la casilla 1 y se toca la 2 · es el final '
                              'de verdad',
                          events=[n('A4', 'h'), n('D4', 'h'), n('C4', 'w')],
                          bars=2, casilla='2', show_time=False),
                 ]),
            dict(num=6, titulo='Las semicorcheas, contadas de cuatro en cuatro',
                 pista='andamio · cuatro semicorcheas ocupan un golpe de negra: aquí, sobre una '
                       'sola nota',
                 sistemas=[
                     dict(cap='a) cuatro semicorcheas por golpe, y una blanca para respirar · di '
                              '"ta-ta-ta-ta" mientras las tocas',
                          events=[n('A4', 's'), n('A4', 's'), n('A4', 's'), n('A4', 's'),
                                  n('B4', 's'), n('B4', 's'), n('B4', 's'), n('B4', 's'),
                                  n('C5', 'h')],
                          bars=1),
                 ]),
            dict(num=7, titulo='Las tres posiciones del acorde de F',
                 pista='andamio sobre la letra F IMPRESA en tu partitura · mismas notas, distinto '
                       'orden',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) en posición fundamental, en primera inversión y en segunda · el '
                              'acorde es el mismo y solo cambia cuál va abajo',
                          events=[ac(('F2', 'A2', 'C3'), 'w'), ac(('A2', 'C3', 'F3'), 'w'),
                                  ac(('C3', 'F3', 'A3'), 'w')],
                          bars=3, clef='bass'),
                 ]),
            dict(num=8, titulo='Los acordes que salen menos, con bajo y octava',
                 pista='andamio sobre las letras Am, Dm y G IMPRESAS · lo mínimo para sostenerlos '
                       'cuando la melodía va por encima',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) el bajo y su octava de cada uno, en blanca y en redonda · suena igual '
                              'de hondo con dos notas que con tres',
                          events=[ac(('A2', 'A3'), 'h'), ac(('D3', 'D4'), 'h'),
                                  ac(('G2', 'G3'), 'w')],
                          bars=2, clef='bass'),
                 ]),
        ] + bloques_extra('Do mayor', 19, 'E4', 'C3',
                          'el pulso es tranquilo: la dificultad está en la ligadura',
                          desde=9, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='What Was I Made For? · para casa',
            intro='Quince minutos al día. La pieza es lenta: el trabajo es de control, no de '
                  'velocidad.',
            bloques=[
                reto('Entrar en el c. 4 sin contar con la partitura: tres compases de silencio y el '
                     'Si a la primera.',
                     'Pon el metrónomo a 78, cuenta los tres compases en voz alta y toca el Si sin '
                     'mirar el teclado. Repite hasta acertar cinco seguidas.'),
                plan((5, 'La izquierda sola, solo los acordes C, Em y F'),
                     (5, 'La figura del c. 4, con la ligadura, diez veces'),
                     (5, 'La derecha de los cc. 4 y 5, sin la izquierda'),
                     (5, 'Los cc. 1-5 con las dos manos')),
                cifrado(['C', 'Em', 'F', 'Am', 'Dm', 'G'],
                        ['Escribe las tres notas de cada uno, de grave a agudo.',
                         'Marca con una cruz los que comparten dos notas con el de al lado.',
                         'Rodea el acorde que lleva una tecla negra, si lo hay.'],
                        titulo='Las seis letras de tu partitura',
                        pista='están impresas encima del pentagrama; C, Em y F son las del principio'),
                verdadero_falso([
                    'Detrás de la clave no hay nada.',
                    'La partitura trae ♩ = 78.',
                    'La derecha toca desde el c. 1.',
                    'En el c. 4 hay semicorcheas.',
                    'La partitura no trae signos de repetición.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                figuras([('s', 'semicorchea'), ('e', 'corchea'), ('q', 'negra'),
                         ('h', 'blanca')],
                        titulo='¿Cuántos golpes dura cada figura del c. 4?',
                        pista='escribe el número en la caja · la semicorchea es la que lleva dos barras'),
                para_clase('Los cc. 1-8 a 78, y cómo te sale la entrada del c. 4. Si el Si te falla, '
                           'tráelo: se arregla con la mano izquierda por delante.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
