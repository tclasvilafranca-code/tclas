# -*- coding: utf-8 -*-
"""Para Elisa (Beethoven) — pieza 23 de Jaume. ADULTO exigente, sin cifrado.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Fur Elise", Beethoven,
   1 página, vectorial, 22 compases), a 250-300 ppp:

     - Detrás de la clave NO hay nada (La menor, con sostenidos y becuadros
       escritos delante de las notas). 3/4. No trae tempo ni indicaciones de intensidad.
     - Es una edición propia, escrita a corcheas: el arranque no va en
       semicorcheas. LA ÚNICA SEMICORCHEA está en el c. 20 (y las que se atan
       a ella en los cc. 21 y 22).
     - La izquierda, cuando entra (c. 3), hace "silencio de negra con puntillo,
       dos corcheas y silencio de corchea", con un arpegio escrito sobre el
       pentagrama de fa.
     - MEDIDO, mano derecha:
       c. 1: silencio de blanca · Mi5 · Re♯5 (corcheas)
       c. 2: Mi5 · Re♯5 · Mi5 · Si4 · Re5 (con becuadro) · Do5 (corcheas)
       c. 20: silencio de negra · La4 (corchea) · Si4 (corchea con puntillo) ·
              Do5 (corchea) · Si4 (semicorchea, ligada al compás siguiente)
       c. 21: Si4 (semicorchea) · La4 (blanca, ligada) · La4 (corchea con puntillo,
              ligada al compás siguiente)
   Es el mismo archivo que el de Isaac y el de Mercè. Aquí lo literal es lo medido
   y el andamio es otro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, plan, metronomo, nombres, colorear, diferencias,
                       para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def lig(p, d='e'):
    return dict(pitch=p, dur=d, lig=True)


# MEDIDO: cc. 1 y 2
C1 = [sil('h'), n('E5', 'e'), n('D#5', 'e')]
C2 = [n('E5', 'e'), n('D#5', 'e'), n('E5', 'e'), n('B4', 'e'), n('Dn5', 'e'), n('C5', 'e')]
# MEDIDO: c. 20 y c. 21
C20 = [sil('q'), n('A4', 'e'), n('B4', 'e.'), n('C5', 'e'), n('B4', 's')]
C21 = [n('B4', 's'), lig('A4', 'h'), n('A4', 'e.')]

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=23, nivel='intermedio', slug='ParaElisa',
    formato='adulto',
    titulo_corto='Para Elisa', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source', 'Para Elisa Beethoven'),
    yt='https://www.youtube.com/results?search_query=fur+elise+beethoven+piano+tutorial',

    ficha=dict(
        titulo='Para Elisa',
        autor='Ludwig van Beethoven · Für Elise',
        datos=[('Tonalidad', 'La menor'), ('Compás', '3/4'),
               ('Carácter', 'Sin tempo'), ('Alteraciones', 'Re♯ y becuadro'),
               ('Páginas', 'Una')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y la izquierda',
        pie_ritmos='Arriba, medido sobre tu partitura: el famoso arranque Mi, Re♯, Mi, Re♯, Mi, Si, '
                   'Re, Do. Abajo, andamio con la misma forma que la izquierda de tu partitura: '
                   'silencio, dos corcheas y silencio.',
        armonia=dict(
            titulo='Corcheas que oscilan, un Re♯ y un becuadro',
            tarjetas=[
                ('EL ARRANQUE', 'Mi y Re♯',
                 'Los dos primeros compases son la oscilación Mi-Re♯ que todo el mundo reconoce, y '
                 'luego Mi, Si, Re y Do. Va a corcheas, tras un silencio de blanca.'),
                ('EL RE♯ Y EL BECUADRO', 'Se anula',
                 'El Re♯ va escrito delante de la nota, no en la armadura. En el c. 2, el Re '
                 'siguiente lleva un becuadro: la tecla vuelve a ser blanca.'),
                ('LOS SILENCIOS', 'La pieza respira',
                 'En los cc. 3 a 5 la derecha toca una nota larga y descansa: el silencio es parte '
                 'de la frase, y se cuenta.'),
                ('LA SEMICORCHEA', 'Solo una, al final',
                 'Hasta el c. 20 todo son negras y corcheas. Ahí aparece una semicorchea, tras una '
                 'corchea con puntillo, y se ata a una nota larga en los compases siguientes.'),
            ],
            pie='Son 22 compases y una página: la pieza entera cabe a un vistazo. La edición no trae '
                'tempo ni indicaciones de intensidad, así que la interpretación es tuya.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1 y 2 · medido', C1 + C2, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio · silencio, dos corcheas y silencio',
             [sil('q.'), n('A2', 'e'), n('E3', 'e'), sil('e')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: La menor, con sostenidos y becuadros escritos delante.',
            'El compás es 3/4. No trae tempo ni indicaciones de intensidad.',
            'El arranque va en corcheas, tras un silencio de blanca: Mi, Re♯, Mi, Re♯, Mi, Si, Re, Do.',
            'En el c. 2 aparece un becuadro delante del Re.',
            'La única semicorchea de la pieza está en el c. 20.',
            'La izquierda no entra hasta el c. 3, y lo hace con silencios y dos corcheas.',
        ],
        reto='Mantener las corcheas del arranque iguales y livianas: Mi y Re♯ van como un balanceo, '
             'sin acentuar el primer Mi. Es la oscilación lo que se oye, no cada nota.',
        truco='Toca el arranque con un solo gesto de muñeca, como si la mano girara sobre las dos '
              'teclas. Si cada nota suena golpeada, baja la velocidad y reduce el peso.',
        sabias='Beethoven la compuso hacia 1810 y no se publicó hasta 1867, cuarenta años después de '
               'su muerte. Nadie sabe con certeza quién era Elisa: la hipótesis más aceptada es '
               'que era Therese Malfatti, aunque nunca se ha confirmado.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el arranque: dos notas que oscilan y después una frase que baja. '
                      'Fíjate en cómo, cada vez que vuelve, la oscilación suena igual de liviana.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Es la pieza más conocida del cuaderno y por eso se estudia con más cuidado: despacio, '
              'con el metrónomo, y con los silencios contados. El arranque se aprende en minutos; '
              'dejarlo bien lleva semanas.',
        reglas=['EL RE♯ Y SU BECUADRO', 'LOS SILENCIOS SE CUENTAN', 'LAS CORCHEAS, LIVIANAS'],
        bloques=[
            dict(num=1, titulo='El c. 2: seis corcheas con un becuadro',
                 pista='c. 2 · medido sobre tu partitura · el Re♯ de la oscilación y el Re natural '
                       'que lo desmiente',
                 sistemas=[
                     dict(cap='a) Mi, Re♯, Mi, Si, Re y Do · el Re del cuarto grupo lleva '
                              'becuadro: ya no es el Re♯ del principio',
                          events=C2, bars=1),
                     dict(cap='b) la oscilación Mi–Re♯ más baja, sin becuadro · andamio para fijar '
                              'el dibujo de la mano',
                          events=[n('B4', 'e'), n('A#4', 'e'), n('B4', 'e'), n('A#4', 'e'),
                                  n('B4', 'e'), n('F#4', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(num=2, titulo='El becuadro, aislado',
                 pista='andamio · lo que dice la regla de la alteración, sin la música alrededor',
                 sistemas=[
                     dict(cap='a) un Re, un Re♯ y un Re con becuadro · el sostenido sube la nota, '
                              'el becuadro la devuelve',
                          events=[n('D5'), n('D#5'), n('Dn5')], bars=1),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL ARRANQUE SE TOCA LIVIANO',
                 texto='Una oscilación entre dos teclas contiguas, repetida, suena a balanceo solo '
                       'si el peso de la mano no cae en cada nota. Es un gesto de muñeca, no de '
                       'dedos: la mano se queda casi quieta y gira. Si cada corchea se golpea, el '
                       'arranque suena a máquina de escribir.'),
            dict(num=3, titulo='La figura larga-corta del c. 20',
                 pista='c. 20 · medido sobre tu partitura · la única semicorchea de la pieza, '
                       'detrás de una corchea con puntillo',
                 sistemas=[
                     dict(cap='a) silencio de negra, La, Si con puntillo, Do y la semicorchea Si · '
                              'la corta cae justo antes de la barra',
                          events=C20, bars=1),
                     dict(cap='b) la misma figura una nota más grave · andamio, para ver que el '
                              'dibujo es el mismo con otras notas',
                          events=[sil('q'), n('G4', 'e'), n('A4', 'e.'), n('B4', 'e'),
                                  n('A4', 's')],
                          bars=1, show_time=False),
                 ]),
            dict(num=4, titulo='La nota larga que se ata, c. 21',
                 pista='c. 21 · medido sobre tu partitura · una blanca ligada a una corchea con '
                       'puntillo',
                 sistemas=[
                     dict(cap='a) la semicorchea, la blanca de La y la corchea con puntillo atada · '
                              'la ligadura suma las dos duraciones: el La se toca una sola vez',
                          events=C21, bars=1),
                 ]),
            dict(num=5, titulo='La izquierda: silencio, dos corcheas y silencio',
                 pista='andamio sobre La menor · la figura es la que lleva tu partitura, con '
                       'notas de apoyo',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) dos compases con la misma forma · el silencio de negra con '
                              'puntillo se cuenta entero antes de las dos corcheas',
                          events=[sil('q.'), n('A2', 'e'), n('E3', 'e'), sil('e'),
                                  sil('q.'), n('E3', 'e'), n('A3', 'e'), sil('e')],
                          bars=2, clef='bass'),
                 ]),
        ] + bloques_extra('La menor', 23, 'A4', 'A2',
                          'la oscilación del principio y la semicorchea del c. 20',
                          desde=6, time_sig=(3, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Para Elisa · para casa',
            intro='Veinte minutos al día. El arranque suena pronto; lo que lleva semanas es que suene '
                  'bien: liviano, igual y sin prisa.',
            bloques=[
                plan((5, 'El arranque con la derecha, solo el c. 2, diez veces'),
                     (5, 'Los silencios de los cc. 3-5, contando en voz alta'),
                     (5, 'La izquierda sola, la figura silencio-dos corcheas-silencio'),
                     (5, 'Las dos manos, cc. 1-8')),
                metronomo('Empieza a ♩ = 56 con el arranque solo y sube de cuatro en cuatro, sin '
                          'dejar de sonar liviano.',
                          'La partitura no trae tempo: la meta la eliges tú y la apuntas a lápiz.',
                          titulo='A qué velocidad te sale'),
                nombres(['E5', 'D#5', 'B4', 'D5', 'C5', 'A4'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='son las notas distintas del arranque de tu partitura · y escribe '
                              'al lado cuál lleva un sostenido'),
                colorear([n('E5', 'e'), n('D#5', 'e'), n('E5', 'e'), n('B4', 'e'),
                          n('Dn5', 'e'), n('C5', 'e'), n('A4', 'q.')],
                         ['Las corcheas, de azul.',
                          'La negra con puntillo, de verde.',
                          'La nota con sostenido o con becuadro, de rojo.'],
                         titulo='Colorea según la figura',
                         pista='la primera parte es el c. 2 de tu partitura'),
                diferencias(C2,
                            [n('E5', 'e'), n('E5', 'e'), n('E5', 'e'), n('A4', 'e'),
                             n('D5', 'e'), n('C5', 'e')],
                            cuantas=3,
                            titulo='Busca las diferencias',
                            pista='arriba, tu compás 2 medido · abajo, un compás parecido con tres '
                                  'cosas cambiadas'),
                para_clase('Los cc. 1-8 a la velocidad que has elegido, y si el arranque te sale '
                           'liviano. Si se te pone duro, tráelo: se arregla con la muñeca y no '
                           'con los dedos.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
