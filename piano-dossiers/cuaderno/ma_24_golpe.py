# -*- coding: utf-8 -*-
"""The Entertainer (Scott Joplin), «El golpe» — pieza 24 de Martina, la última del curso. ADULTO exigente,
   tono de niña.

   Lo comprobado sobre el PDF de su carpeta de Drive (arreglo de Gilbert
   DeBenedetti, edición Gradimi "Level Three", 2 páginas, imagen a 72 ppp), a
   150-250 ppp:

     - Detrás de la clave no hay nada: DO MAYOR, con alteraciones escritas
       (un La♭ en el c. 6, un Re♯ en el c. 8 y más adelante).
     - Compás de **2/2** (el signo de la ¢, "alla breve"). Arriba pone
       **Not fast** y la dinámica **p**; NO trae número de metrónomo.
     - Los dos primeros compases llevan un **8va** (se tocan una octava más
       alta de lo escrito).
     - Lleva digitación impresa, staccato, un acento, un calderón y
       matices p y f. La izquierda, en los primeros compases, no toca.
     - NO LLEVA CORCHEAS: solo negras, blancas y redondas.
     - MEDIDO, mano derecha:
       cc. 1-2 (con 8va): Re5 · Mi5 · Do5 · La4 (la última ligada) |
                          La4 · Si4 · Sol4 (staccato) · silencio de negra
       cc. 5-6: Re4 · Mi4 · Do4 · La3 (ligada) | La3 · Si3 · La3 · La♭3
       c. 7: Sol3 (staccato) y silencio de negra y de blanca
     - La numeración de este módulo es la que se obtiene contando los compases.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, plan, escalera, rodear, escribir, verdadero_falso,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def lig(p, d='q'):
    return dict(pitch=p, dur=d, lig=True)


# MEDIDO: cc. 1-2 (con 8va)
C12 = [n('D5'), n('E5'), n('C5'), lig('A4'),
       n('A4'), n('B4'), dict(pitch='G4', dur='q', art='staccato'), sil('q')]
# MEDIDO: cc. 5-6 (sin 8va)
C56 = [n('D4'), n('E4'), n('C4'), lig('A3'),
       n('A3'), n('B3'), n('A3'), n('Ab3')]
C6 = [n('A3'), n('B3'), n('A3'), n('Ab3')]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=24, nivel='intermedio', slug='ElGolpe',
    formato='adulto',
    titulo_corto='The Entertainer', time_sig=(2, 2), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'El Golpe'),
    yt='https://www.youtube.com/results?search_query=the+entertainer+scott+joplin+piano+tutorial',

    ficha=dict(
        titulo='The Entertainer',
        autor='Scott Joplin · arreglo de Gilbert DeBenedetti (Gradimi, Level Three)',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '2/2'),
               ('Carácter', 'Not fast · p'), ('Alteraciones', 'La♭ y Re♯'),
               ('Empieza', 'Con 8va')],
        titulo_ritmos='El c. 6, medido, y el bajo de la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: el c. 6 de la derecha, con el La♭. Abajo, '
                   'andamio: el dibujo de la izquierda (nota grave, silencio, acorde, silencio).',
        armonia=dict(
            titulo='El rag más famoso, escrito a dos por compás y sin corcheas',
            tarjetas=[
                ('EL 2/2', 'Dos golpes',
                 'El signo ¢ es el 2/2: cada compás tiene cuatro negras, pero se cuentan en dos '
                 'golpes largos. Es lo que da a la pieza su aire de marcha.'),
                ('EL 8VA', 'Una octava más alta',
                 'Los dos primeros compases llevan un 8va: se tocan una octava por encima de lo '
                 'escrito. Es la primera cosa que el ojo no debe dejar pasar.'),
                ('LAS ALTERACIONES', 'La♭ y Re♯',
                 'La armadura está vacía, pero el c. 6 trae un La♭ y el c. 8 un Re♯: dos teclas '
                 'negras escritas delante de la nota, que valen solo hasta el final del compás.'),
                ('LA DIGITACIÓN', 'Va escrita',
                 'La edición imprime los dedos de las dos manos. El motivo del principio se '
                 'toca con 4-3-1 y se repite igual, así que la mano se lo aprende.'),
            ],
            pie='La pieza no lleva ni una corchea: todo es negra, blanca y redonda. La dificultad '
                'está en el estilo (el bajo que salta y el staccato), no en el ritmo.',
        ),
        ritmos=[
            ('MANO DERECHA', 'c. 6 · medido', C6, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · nota grave y acorde',
             [n('F2'), sil('q'), ac(('A2', 'C3')), sil('q')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: Do mayor, con alteraciones escritas.',
            'El compás es 2/2 (el signo ¢): cuatro negras por compás, contadas en dos.',
            'Arriba pone Not fast y p, pero no trae número de metrónomo.',
            'Los cc. 1 y 2 llevan un 8va: se tocan una octava más alta de lo escrito.',
            'La edición imprime la digitación, el staccato, un acento y un calderón.',
            'No lleva ni una corchea: solo negras, blancas y redondas.',
        ],
        reto='Tocar el motivo de los cc. 5-6 sin mirar las manos: Re, Mi, Do y La con la última '
             'ligada, y después La, Si, La y La♭ sin que el bemol se escape.',
        truco='Aprende el motivo con la digitación impresa y no la cambies. Si el La♭ se te '
              'escapa, di su nombre en voz alta justo antes de tocarlo: el oído necesita saber '
              'que viene un bemol.',
        sabias='The Entertainer es un rag que Scott Joplin publicó en 1902. Se hizo famosa de '
               'nuevo en 1973, cuando sonó en la película El golpe (The Sting), de ahí que en tu '
               'carpeta aparezca como El golpe.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo la izquierda salta: una nota grave y un acorde, una y otra '
                      'vez. Esa alternancia es la que hace "caminar" la pieza.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La pieza se estudia por frases: primero el motivo del principio, que vuelve varias '
              'veces, y después el bajo. El 8va y el staccato son las dos cosas que se pasan por '
              'alto.',
        reglas=['EL 8VA SE TOCA UNA OCTAVA ARRIBA', 'EL BEMOL VALE HASTA LA BARRA',
                'EL STACCATO ACORTA, NO ACELERA'],
        bloques=[
            dict(num=1, titulo='Los dos primeros compases, con el 8va',
                 pista='cc. 1-2 · medido sobre tu partitura · el 8va quiere decir que suena una '
                       'octava más alta que lo escrito',
                 sistemas=[
                     dict(cap='a) Re, Mi, Do y La ligada, y después La, Si, Sol con staccato y un '
                              'silencio · la nota ligada se aguanta hasta el segundo compás',
                          events=C12, bars=2, ottava=True, matiz='p'),
                 ]),
            dict(num=2, titulo='La misma frase, sin 8va, en los cc. 5 y 6',
                 pista='cc. 5-6 · medido sobre tu partitura · empieza igual que el c. 1 pero la '
                       'segunda mitad es otra',
                 sistemas=[
                     dict(cap='a) Re, Mi, Do y La ligada · el c. 6 sigue con La, Si, La y un '
                              'La♭ · aquí no hay 8va: suena donde está escrito',
                          events=C56, bars=2),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL BEMOL VALE HASTA LA BARRA',
                 texto='El La♭ del c. 6 está escrito delante de la nota, no en la armadura, y vale '
                       'solo para su compás. Cuando empieza el compás siguiente, la tecla vuelve '
                       'a ser blanca. Si el compás de después trae un La, es un La natural, y no '
                       'hace falta que lo diga nadie.'),
            dict(num=3, titulo='El bemol, aislado',
                 pista='andamio · lo que dice la regla de la alteración, sin la música alrededor',
                 sistemas=[
                     dict(cap='a) Mi, Mi♭ dos veces y Fa · el bemol vale hasta la barra · el compás '
                              'siguiente, cuatro Mi naturales',
                          events=[n('E4'), n('Eb4'), n('Eb4'), n('F4'),
                                  n('E4'), n('E4'), n('E4'), n('E4')],
                          bars=2),
                 ]),
            dict(num=4, titulo='El bajo: nota grave, silencio, acorde, silencio',
                 pista='andamio · el dibujo de la izquierda de los cc. 9 y siguientes, sobre Sol y '
                       'Do',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) el dibujo sobre Sol · una nota grave en el primer golpe y un '
                              'acorde en el tercero, con los silencios entre ellos',
                          events=[n('G2'), sil('q'), ac(('B2', 'D3')), sil('q'),
                                  n('G2'), sil('q'), ac(('C3', 'E3')), sil('q')],
                          bars=2, clef='bass'),
                     dict(cap='b) el mismo dibujo con un acorde entero en cada golpe fuerte · '
                              'andamio, para ver el salto sin los silencios',
                          events=[n('G2'), ac(('B2', 'D3')), n('G2'), ac(('B2', 'D3'))],
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(num=5, titulo='Piano, fuerte y calderón',
                 pista='andamio · los matices y el calderón que trae tu partitura (p al principio, '
                       'f en el c. 8)',
                 sistemas=[
                     dict(cap='a) un motivo en piano · los matices no cambian las notas, cambian '
                              'cuánto pesa el dedo',
                          events=[n('G4'), n('D5', 'h'), n('G4')], bars=1, matiz='p'),
                     dict(cap='b) el mismo motivo en forte, con un acento en la primera nota y '
                              'un calderón al final',
                          events=[n('G4'), n('D5', 'h'), n('G4')], bars=1, matiz='f',
                          acento=True, calderon=True, show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 24, 'E4', 'C3',
                          'el motivo del principio y el bajo que salta',
                          desde=6, time_sig=(2, 2)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='The Entertainer · para casa',
            intro='Quince minutos al día. El motivo es corto y sale pronto; lo que lleva trabajo es '
                  'el bajo y el staccato.',
            bloques=[
                plan((5, 'El motivo de los cc. 1-2, con el 8va, una octava arriba'),
                     (5, 'El mismo motivo en los cc. 5-6, sin 8va'),
                     (5, 'El bajo de nota grave y acorde, con la izquierda sola'),
                     (5, 'Las dos manos, solo los ocho primeros compases')),
                escalera((50, 'el motivo con la derecha, sin el bajo'),
                         (60, 'el bajo solo, sin mirar'),
                         (72, 'las dos manos, ocho compases'),
                         (84, 'la pieza hasta el calderón'),
                         meta='La partitura no trae número, solo "Not fast": la meta la eliges tú '
                              'y la apuntas a lápiz.',
                         titulo='La escalera del metrónomo'),
                rodear([[n('A3'), n('B3'), n('A3'), n('Ab3')],
                        [n('A3'), n('B3'), n('A3'), n('A3')],
                        [n('A3'), n('B3'), n('A3'), n('Ab3')],
                        [n('B3'), n('A3'), n('B3'), n('Ab3')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='el primero es el c. 6 de tu partitura · los demás llevan una nota '
                             'cambiada: ojo con el bemol'),
                escribir(titulo='Copia el c. 6 de la derecha',
                         pista='cuatro negras: La, Si, La y La bemol · y escribe debajo cómo se '
                               'llama cada una',
                         lineas=1),
                verdadero_falso([
                    'Detrás de la clave no hay nada.',
                    'El compás es 2/2, el de la ¢.',
                    'Arriba viene un número de metrónomo.',
                    'Los dos primeros compases llevan un 8va.',
                    'La pieza lleva corcheas en toda la primera línea.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas · y las dos hablan de TU partitura'),
                para_clase('Los cc. 1-8 con las dos manos y la velocidad que has elegido. Y dime si '
                           'el staccato te sale corto o solo rápido: no es lo mismo.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
