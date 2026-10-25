# -*- coding: utf-8 -*-
"""Greensleeves — pieza 5 de Jaume. Formato ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Greensleeves —
   Traditional English folk song", 2 páginas, 32 compases), mirado a 100 dpi:

     - Detrás de la clave no hay nada: La menor. Los sostenidos van escritos
       delante de la nota.
     - 3/4, "Moderato", "mp" al empezar y **f en los cc. 17 y 25**. No trae
       número de metrónomo. Pone "con pedale" bajo el primer sistema.
     - **Anacrusa**: la derecha entra con un La4 de negra (MEDIDO con
       `medir_arranque`) y la izquierda con un silencio de negra.
     - La izquierda hace **tres negras por compás, subiendo** (un arpegio por
       compás): La-Do-Mi en los cc. 1-2, Sol-Si-Re en los cc. 3-4, Fa-La-Do en
       el 5 y el 6, Mi-Sol♯-Si en el 7. En el c. 8 y en otros finales de frase
       hay un acorde.
     - **Trae CIFRADO impreso**: Am, G, F, E, Am/E, C y G/D.
     - Sostenidos escritos delante de la nota: Sol♯ (cc. 6, 7, 14, 22, 23, 30) y
       Fa♯ (cc. 14, 18, 26 y 30).
     - Dos reguladores: el del c. 23 y el que cruza los cc. 30 y 31.
     - Digitación impresa en unas pocas notas, solo en la derecha.

   Es la pieza 5 del álbum y la primera con **cifrado**: Jaume lee las letras
   de encima y las comprueba con las tres negras de abajo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, escalera, cifrado, colorear,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=5, nivel='intermedio', slug='Greensleeves',
    formato='adulto',
    titulo_corto='Greensleeves', time_sig=(3, 4), key_sig='La menor',
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source', 'Greensleeves.'),
    yt='https://www.youtube.com/results?search_query=greensleeves+easy+piano',

    ficha=dict(
        titulo='Greensleeves',
        autor='Canción popular inglesa',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Carácter', 'Moderato'), ('Empieza', 'En anacrusa'),
               ('Páginas', 'Dos')],
        titulo_ritmos='La entrada y el primer arpegio',
        pie_ritmos='Arriba, medido sobre tu partitura: la anacrusa es un La4 de negra. Abajo, leído: '
                   'las tres negras que suben, La, Do y Mi. Los dedos, en tu partitura.',
        armonia=dict(
            titulo='El cifrado, de verdad',
            tarjetas=[
                ('EL CIFRADO', 'Am, G, F, E…',
                 'Las letras de encima del pentagrama son los acordes: Am, G, F, E, Am/E, C y '
                 'G/D. La m pequeña quiere decir menor; la barra, que el bajo es otra nota.'),
                ('LA IZQUIERDA', 'Un arpegio al compás',
                 'Tres negras que suben: La-Do-Mi con Am, Sol-Si-Re con G, Fa-La-Do con F. Lo que '
                 'toca la izquierda es el acorde que dice la letra, desplegado.'),
                ('LOS SOSTENIDOS', 'Sol♯ y Fa♯',
                 'El Sol♯ del acorde de Mi (cc. 6, 7, 14…) y el Fa♯ de los cc. 14 y 18. Van '
                 'escritos delante de cada nota y valen solo para su compás.'),
                ('LA DINÁMICA', 'mp, f y reguladores',
                 'Empieza en mp, salta a f en el c. 17 y vuelve a f en el 25. Hay un regulador en '
                 'el c. 23 y otro que cruza los cc. 30 y 31.'),
            ],
            pie='Es una pieza en la que se puede empezar a tocar sin leer: el cifrado dice qué '
                'acorde toca cada compás y las tres negras de abajo lo despliegan. Con tu base, '
                'compruébalo: lee solo las letras y toca el arpegio de memoria.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la anacrusa · medido',
             [sil('q'), sil('q'), n('A4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'c. 1 · leído de tu partitura',
             [n('A2'), n('C3'), n('E3')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: es La menor, y los sostenidos van delante de cada nota.',
            'Pone "Moderato" y "mp", y salta a "f" en los cc. 17 y 25.',
            'Empieza en anacrusa: un La4 de negra en la derecha antes del primer compás.',
            'Las letras de encima son el cifrado: Am, G, F, E, Am/E, C y G/D.',
            'La izquierda hace un arpegio de tres negras por compás, subiendo.',
            'Pone "con pedale": la pieza se toca con el pedal puesto.',
        ],
        reto='Que el cifrado y el arpegio se lean a la vez. Si miras las letras, la izquierda se '
             'para; si miras las notas, te pierdes el acorde. Hay que mirar las dos y no mirar ninguna.',
        truco='Toca solo la izquierda leyendo únicamente las letras de encima, sin mirar la clave de '
              'fa. Cuando salga, añade la derecha. Si el arpegio se te acelera, es que estás leyendo '
              'notas en vez de acordes.',
        sabias='Greensleeves se atribuye por tradición a Enrique VIII, pero la melodía es más tardía: '
               'se registra a finales del siglo XVI. Su aire de La menor con un Sol♯ de paso la ha '
               'hecho sonar a antigua desde entonces.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el Sol♯ del acorde de Mi tira del oído hacia el La: ese es el '
                      'sitio donde la pieza deja de ser antigua y empieza a ser tuya.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La pieza son seis acordes y una melodía que los recorre. Se estudia leyendo primero '
              'las letras, después la izquierda que las despliega y al final la melodía encima.',
        reglas=['PRIMERO LAS LETRAS', 'UN ARPEGIO POR COMPÁS', 'LOS SOSTENIDOS, MARCADOS'],
        bloques=[
            dict(num=1, titulo='La anacrusa y los dos primeros compases',
                 pista='anacrusa y cc. 1-2 · leído de tu partitura · el La4 entra antes del compás',
                 sistemas=[
                     dict(cap='a) cuenta dos golpes en silencio y entra en el tercero · el '
                              'compás 1 es la blanca de Do y la negra de Re',
                          events=[sil('q'), sil('q'), n('A4'),
                                  n('C5', 'h'), n('D5'),
                                  n('E5', 'q.'), n('F5', 'e'), n('E5')],
                          bars=3),
                 ]),
            dict(num=2, titulo='Cuatro acordes, cuatro compases',
                 pista='cc. 1, 3, 5 y 7 · leído de tu partitura · cada compás es el acorde que '
                       'dice la letra de encima',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) Am, G, F y E · primero cada arpegio solo, luego los cuatro '
                              'seguidos sin parar · el Sol♯ del último es la tecla negra',
                          events=[n('A2'), n('C3'), n('E3'),
                                  n('G2'), n('B2'), n('D3'),
                                  n('F2'), n('A2'), n('C3'),
                                  n('E2'), n('G#2'), n('B2')],
                          bars=4, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='LEER LETRAS, NO NOTAS',
                 texto='Tapa con un papel la clave de fa y toca los cuatro compases de arriba mirando '
                       'solo las letras. Si sale, ya sabes la mitad de la pieza: el resto son las '
                       'mismas tres negras repetidas y un cambio de acorde cada dos compases.'),
            dict(num=3, titulo='El Sol♯ de paso, en la derecha',
                 pista='cc. 6 y 7 · leído de tu partitura · el Sol♯ aparece dos veces seguidas',
                 sistemas=[
                     dict(cap='a) la tecla negra va en el segundo golpe del c. 6 y en el tercero del '
                              'c. 7 · si se te olvida el sostenido en el segundo, es un clásico',
                          events=[n('A4', 'q.'), n('G#4', 'e'), n('A4'),
                                  n('B4', 'h'), n('G#4')],
                          bars=2),
                 ]),
            dict(num=4, titulo='El salto a f en el c. 17',
                 pista='cc. 17-18 · leído de tu partitura · aquí la pieza cambia de color: del mp '
                       'inicial al f',
                 sistemas=[
                     dict(cap='a) un Sol5 largo y el Fa♯ del compás siguiente · el "f" no es '
                              'más aprisa, es más peso desde el brazo',
                          events=[n('G5', 'h.'), n('G5', 'q.'), n('F#5', 'e'), n('E5')],
                          bars=2, matiz='f'),
                 ]),
            dict(num=5, titulo='Los reguladores de la segunda página',
                 pista='cc. 23 y 30-31 · dos reguladores · andamio de tres compases',
                 sistemas=[
                     dict(cap='a) la curva sube y baja dentro del mismo compás · el regulador es '
                              'una respiración, no un cambio de nivel',
                          events=[n('D5', 'h'), n('B4'), n('E5', 'h.'),
                                  n('C5', 'h'), n('A4')],
                          bars=3, cresc=3, matiz='mp'),
                 ]),
        ] + bloques_extra('La menor', 5, 'A4', 'A2',
                          'tres negras por compás: la izquierda no puede pararse',
                          desde=6, time_sig=(3, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Greensleeves · para casa',
            intro='Veinte minutos al día. Se estudia por acordes: primero las letras, luego las '
                  'notas.',
            bloques=[
                reto('Tocar el arpegio de la izquierda leyendo solo las letras del cifrado, sin '
                     'mirar la clave de fa.',
                     'Tapa la clave de fa con un papel y toca los ocho primeros compases. Si te '
                     'pierdes, para en el acorde y di su nombre en voz alta antes de seguir.'),
                plan((5, 'Las letras, cc. 1-8, diciéndolas en voz alta'),
                     (5, 'La izquierda sola, un arpegio por compás'),
                     (6, 'La melodía sola, con la anacrusa contada'),
                     (4, 'Las dos juntas, de cuatro en cuatro compases')),
                escalera((50, 'la izquierda sola, sin mirar'),
                         (60, 'las dos manos, cuatro compases'),
                         (72, 'los ocho primeros compases'),
                         (84, 'la pieza entera sin parar'),
                         meta='La partitura no trae tempo impreso, solo "Moderato": la meta la '
                              'eliges tú y la apuntas a lápiz.',
                         titulo='La escalera del metrónomo'),
                cifrado(['Am', 'G', 'F', 'E', 'C'],
                        ['Escribe las tres notas de cada uno, de grave a agudo.',
                         'Rodea el que lleva una tecla negra: es el acorde de Mi.'],
                        pista='los cinco primeros que trae impresos tu partitura'),
                colorear([n('A4'), n('C5', 'h'), n('D5'), n('E5', 'q.'), n('F5', 'e'),
                          n('E5'), n('D5', 'h'), n('B4')],
                         ['Las negras con puntillo, de rojo.',
                          'Las blancas, de verde.',
                          'Las corcheas, de azul.'],
                         titulo='Colorea según la figura',
                         pista='son los cc. 1-3 de la derecha de tu partitura'),
                para_clase('Los ocho primeros compases leyendo solo el cifrado, y la velocidad a la '
                           'que te salen. Si el Sol♯ del c. 6 se te escapa, tráelo marcado.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
