# -*- coding: utf-8 -*-
"""What Was I Made For? — pieza 5 de Aida. Formato ADULTO exigente.

   Es la pieza del cuaderno que empieza CALLANDO, y por eso esta aqui: la
   anterior enseño a repartir el trabajo entre las dos manos, y esta enseña que
   una de las dos puede no hacer nada durante tres compases enteros sin que eso
   sea un error de imprenta.

   Lo comprobado sobre el PDF de SU carpeta (Musescore, easy piano, 2 paginas;
   el mismo archivo, byte a byte, que el de Josep, Dilan y Eva):

     - Do mayor: detras de la clave no hay nada.
     - 4/4, y arriba viene impreso el metronomo: **negra = 78**. Por eso la
       casilla de la ficha se llama "Tempo" y no "Caracter".
     - Encima del pentagrama van las LETRAS DE ACORDE, y la primera vuelta es
       C · Em · F · C · Em · F · C.
     - Debajo va la letra ("I used to float...").

   LO MEDIDO, y es lo que decide la hoja entera: el pentagrama de ARRIBA trae
   TRES SILENCIOS DE REDONDA seguidos, uno por compas. La mano derecha no toca
   hasta el compas 4, y ahi entra despues de un silencio de blanca. Mientras
   tanto la izquierda hace acordes largos: blancas en los compases 1 y 3, y una
   redonda en el 2 y en el 4.

   Los tres silencios se leyeron con el detector de cabezas y con la vista: el
   silencio de redonda es un rectangulo macizo que la apertura morfologica deja
   pasar como si fuera una nota, asi que el lector automatico devolvia tres
   cabezas a la misma altura. Son los silencios, no notas — el mismo susto que
   ya dio el *Piano Man* de Eduard.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, reto, plan, metronomo, unir,
                      colorear, acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los compases 1, 2 y 3 de la DERECHA, medidos: no toca. Cita literal.
ARRANQUE = [sil('w'), sil('w'), sil('w')]

# La izquierda de esos tres compases, sobre el cifrado IMPRESO (C, Em, F).
BAJO = [ac(('C3', 'G3'), 'h'), ac(('E3', 'B3'), 'h'),
        ac(('F3', 'C4'), 'w'),
        ac(('C3', 'G3'), 'h'), ac(('E3', 'B3'), 'h')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=5, nivel='intermedio',
    slug='WhatWasIMadeFor', formato='adulto',
    titulo_corto='What Was I Made For?', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'What Was I Made For.pdf'),
    yt='https://www.youtube.com/results?search_query=what+was+i+made+for+billie+eilish+piano+easy',

    ficha=dict(
        titulo='What Was I Made For?',
        autor='Billie Eilish y Finneas O\'Connell · easy piano',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 78'), ('Derecha', 'Calla 3 compases'),
               ('Trae', 'Cifrado y letra')],
        titulo_ritmos='Así empieza: la derecha no toca',
        pie_ritmos='MEDIDO en tu partitura. Arriba, los compases 1, 2 y 3 de la derecha: tres '
                   'silencios de redonda, uno por compás. Abajo, andamio sobre las letras de '
                   'acorde IMPRESAS (C, Em, F), que es lo que sostiene esos tres compases.',
        armonia=dict(
            titulo='Empezar callando también es tocar',
            tarjetas=[
                ('TRES COMPASES', 'Sin tocar',
                 'La derecha entra en el compás 4. Los tres primeros son silencio de redonda: no es '
                 'una errata, es la introducción.'),
                ('EL TEMPO', '♩ = 78',
                 'Viene impreso en tu partitura, así que no hay que decidirlo. Es lento: algo más '
                 'de un golpe por segundo.'),
                ('EL CIFRADO', 'C · Em · F',
                 'Tres letras que se repiten toda la canción. Con esas tres se acompaña la pieza '
                 'entera aunque no leas ni una nota.'),
                ('LA IZQUIERDA', 'Acordes largos',
                 'Blancas y redondas. No hay ritmo que resolver: hay que colocar la mano y dejarla '
                 'sonar hasta que toque cambiar.'),
            ],
            pie='Contar tres compases de silencio con el metrónomo puesto parece lo más fácil del '
                'cuaderno y es de lo que más falla. Un compás vacío no se siente: hay que contarlo, '
                'y contarlo es una habilidad que se entrena.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1–3, MEDIDOS · tres silencios de redonda',
             ARRANQUE, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio sobre el cifrado impreso',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'Arriba viene impreso el metrónomo: negra = 78.',
            'La mano derecha no toca hasta el compás 4.',
            'Los tres primeros compases de arriba son silencios de redonda.',
            'Encima del pentagrama van las letras de acorde: C, Em y F.',
            'Debajo del pentagrama va la letra de la canción.',
        ],
        reto='Contar tres compases enteros de silencio y entrar exactamente en el compás 4. Sin '
             'metrónomo es casi imposible: el silencio no tiene con qué medirse.',
        truco='Cuenta los tres compases EN VOZ ALTA y con el número de compás delante: "UNO dos '
              'tres cuatro, DOS dos tres cuatro, TRES dos tres cuatro". Decir el número de compás '
              'en vez de contar hasta doce es lo que evita perderse.',
        sabias='La escribió para la película de Barbie en 2023 y ganó el Óscar a la mejor canción. '
               'Billie Eilish ha contado que la letra salió en un día en el que no le salía nada, y '
               'que la canción va precisamente de eso.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los compases desde el primer sonido del piano. La voz no entra hasta '
                      'el cuarto, y ese hueco es exactamente lo que tienes que aprender a medir.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo de esta semana no se toca: se cuenta. Tres compases de silencio con el '
              'metrónomo a 78, y entrar en el cuarto sin dudar.',
        reglas=['CUENTA EL NÚMERO DE COMPÁS, NO HASTA DOCE', 'METRÓNOMO A 78, QUE LO PONE TU PAPEL',
                'LA IZQUIERDA COLOCA Y DEJA'],
        bloques=[
            dict(num=1, titulo='Los tres acordes, y nada más',
                 pista='andamio sobre el cifrado IMPRESO en tu partitura (C, Em, F)',
                 sistemas=[
                     dict(cap='a) los tres acordes en redondas, uno por compás · colocar la mano y '
                              'dejarla',
                          events=[ac(('C3', 'E3', 'G3'), 'w'), ac(('E3', 'G3', 'B3'), 'w'),
                                  ac(('F3', 'A3', 'C4'), 'w')],
                          matiz='mp',
                          bars=3, clef='bass'),
                     dict(cap='b) y la vuelta entera, que es la que se repite toda la canción',
                          events=[ac(('C3', 'E3', 'G3'), 'w'), ac(('E3', 'G3', 'B3'), 'w'),
                                  ac(('F3', 'A3', 'C4'), 'w'), ac(('C3', 'E3', 'G3'), 'w')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y con la nota de arriba moviéndose sola · es lo que hace que tres '
                              'acordes no suenen a ejercicio',
                          events=[ac(('C3', 'E3', 'G3'), 'h'), ac(('C3', 'E3', 'A3'), 'h'),
                                  ac(('E3', 'G3', 'B3'), 'h'), ac(('E3', 'G3', 'A3'), 'h')],
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE CUENTA UN COMPÁS VACÍO',
                 texto='Diciendo el número del compás en el primer tiempo y el resto normal: "UNO '
                       'dos tres cuatro, DOS dos tres cuatro, TRES dos tres cuatro". Contar hasta '
                       'doce seguido no sirve, porque a la mitad ya no sabes por dónde vas. Y '
                       'contar en la cabeza tampoco: en voz alta, aunque estés sola, hasta que la '
                       'entrada salga tres veces seguidas.'),
            dict(num=2, titulo='Los tres compases callados, y la entrada',
                 pista='cc. 1–4 · MEDIDOS en tu partitura · lo que hace la derecha es esperar',
                 sistemas=[
                     dict(cap='a) los tres compases de silencio y la entrada del cuarto · los '
                              'silencios están MEDIDOS y las alturas de la melodía son andamio',
                          events=[sil('w'), sil('w'), sil('w'),
                                  sil('h'), n('C5', 'e'), n('C5', 'e'), n('E5')],
                          bars=4),
                     dict(cap='b) y ahora solo el compás 4, para no gastar tres compases cada vez '
                              'que quieras repetir la entrada',
                          events=[sil('h'), n('C5', 'e'), n('C5', 'e'), n('E5'),
                                  sil('h'), n('C5', 'e'), n('C5', 'e'), n('D5')],
                          bars=2, show_time=False),
                     dict(cap='c) y con la melodía subiendo, que es lo que hace la frase entera · '
                              'la entrada siempre en el mismo sitio',
                          events=[sil('h'), n('C5', 'e'), n('D5', 'e'), n('E5'),
                                  sil('h'), n('E5', 'e'), n('F5', 'e'), n('G5')],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, con la izquierda sonando desde el uno',
                 pista='andamio sobre el cifrado impreso · la izquierda empieza y la derecha espera',
                 sistemas=[
                     dict(cap='a) los compases 1 y 2: abajo el acorde, arriba nada',
                          events=[ac(('C3', 'E3', 'G3'), 'w'), ac(('E3', 'G3', 'B3'), 'w')],
                          bars=2, clef='bass'),
                     dict(cap='b) y el compás 4, ya con las dos manos · la izquierda no cambia '
                              'porque entre la derecha',
                          events=[ac(('F3', 'A3', 'C4'), 'h'), ac(('C5',), 'e'), ac(('C5',), 'e'),
                                  ac(('E5',)),
                                  ac(('C3', 'E3', 'G3'), 'h'), ac(('C5',), 'e'), ac(('C5',), 'e'),
                                  ac(('D5',))],
                          bars=2, manos='sostiene', show_time=False),
                     dict(cap='c) y los cuatro compases enteros: la izquierda desde el uno y la '
                              'derecha entrando en el cuatro',
                          events=[ac(('C3', 'E3', 'G3'), 'w'), ac(('E3', 'G3', 'B3'), 'w'),
                                  ac(('F3', 'A3', 'C4'), 'w'),
                                  ac(('C3', 'E3', 'G3'), 'h'), ac(('C5',), 'e'), ac(('C5',), 'e'),
                                  ac(('E5',))],
                          bars=4, manos='sostiene', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Pon el metrónomo a 78 y toca los cuatro primeros compases enteros: la '
                       'izquierda desde el uno, la derecha entrando en el cuatro. Cuando salga tres '
                       'veces seguidas, y solo entonces, sigue leyendo. Si la entrada te falla, no '
                       'es que tengas que estudiar más notas: es que tienes que contar en voz alta.'),
        ] + bloques_extra('Do mayor', 89, 'C5', 'C3',
                          'contar tres compases de silencio y entrar en el cuarto',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='What Was I Made For · para casa',
            intro='Quince minutos al día, y el metrónomo puesto desde el primero. Esta semana la '
                  'dificultad no está en los dedos.',
            bloques=[
                reto('Entrar en el compás 4 después de tres compases de silencio, con el metrónomo '
                     'a 78 y sin dudar.',
                     'Cuenta en voz alta diciendo el número de compás: "UNO dos tres cuatro, DOS '
                     'dos tres cuatro, TRES dos tres cuatro". Tres veces seguidas bien y ya está.'),
                plan((4, 'Los tres acordes de la izquierda, colocando y dejando sonar'),
                     (4, 'Contar los tres compases de silencio en voz alta, sin tocar'),
                     (4, 'La entrada del compás 4, sola'),
                     (3, 'Los cuatro compases enteros, con las dos manos')),
                metronomo('A 78 desde el primer día: es el número que trae impreso tu partitura, '
                          'así que no hay nada que decidir.',
                          'Si la entrada se te va, no bajes la velocidad: cuenta más alto. El '
                          'problema no es el tempo, es la referencia.'),
                unir([('C', 'Do · Mi · Sol'), ('Em', 'Mi · Sol · Si'),
                      ('F', 'Fa · La · Do'), ('4/4', 'cuatro tiempos por compás')],
                     titulo='Une cada letra con lo que significa',
                     pista='las tres primeras están impresas encima de tu pentagrama'),
                colorear(list(BAJO),
                         [('blancas', 'los acordes que duran dos tiempos'),
                          ('redondas', 'los que duran el compás entero')],
                         titulo='Colorea por figuras los acordes de la izquierda',
                         pista='un color para las blancas y otro para las redondas'),
                acuerdate('Un silencio no es un hueco: es una figura, con su duración exacta, y se '
                          'cuenta igual que una nota. El silencio de redonda que ves colgando de '
                          'la cuarta línea vale un compás entero de 4/4, ni más ni menos.',
                          etiqueta='EL SILENCIO SE CUENTA'),
                para_clase('Los cuatro primeros compases con el metrónomo a 78. Y dime si contaste '
                           'en voz alta o por dentro: si fue por dentro y salió, perfecto; si falló, '
                           'ya sabemos qué probar.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
