# -*- coding: utf-8 -*-
"""Shallow — pieza 10 de Eduard. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta (Lady Gaga y Bradley Cooper,
   Campamento Musical Bye Bye Beethoven, 3 páginas; el mismo archivo que la
   pieza 10 de José María, byte a byte):

     - SOL MAYOR: un sostenido detrás de la clave, igual que la pieza 9. Todos
       los Fa van a la tecla negra.
     - Compás de 4/4 y ♩ = 96 impreso.
     - EMPIEZA CON SILENCIO DE NEGRA y entra en el segundo golpe, con una
       entrada de dos corcheas.
     - Hay compases enteros de silencio en la derecha, y ligaduras que atan
       una nota con la del compás siguiente.
     - La digitación viene impresa (4 y 3 en los primeros compases).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from ed_comun import (n, ac, sil, corch, plan, metronomo, ordenar, colorear,
                      nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
SOL = 'Sol mayor'

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=10, nivel='iniciación',
    slug='Shallow', formato='adulto',
    titulo_corto='Shallow', time_sig=(4, 4), key_sig=SOL,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source', 'SHALLOW.'),
    yt='https://www.youtube.com/results?search_query=shallow+piano+easy',

    ficha=dict(
        titulo='Shallow',
        autor='Lady Gaga y Bradley Cooper · arreglo del Campamento Bye Bye Beethoven',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 96'), ('Empieza', 'Con silencio'),
               ('Páginas', 'Tres')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Sol mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Los Fa, todos en la tecla negra.',
        armonia=dict(
            titulo='Segunda semana en Sol mayor, y por eso está aquí',
            tarjetas=[
                ('LA ARMADURA', 'La misma',
                 'Un sostenido, igual que la pieza anterior. La mano ya sabe dónde está el Fa: eso ya '
                 'no es trabajo nuevo.'),
                ('LA ENTRADA', 'En el dos',
                 'Silencio de negra y entras con dos corcheas. Como en el himno, pero más rápido.'),
                ('LOS HUECOS', 'Compases enteros',
                 'Hay compases en los que la derecha no toca nada. Se cuentan igual, y son los que le '
                 'dan aire a la canción.'),
                ('LAS LIGADURAS', 'Cruzan la raya',
                 'Algunas notas están atadas a la del compás siguiente: se tocan una vez y suenan a '
                 'caballo entre los dos compases.'),
            ],
            pie='Es la segunda pieza seguida en Sol mayor a propósito: cuando una tonalidad se acaba '
                'de aprender, la mejor forma de fijarla es usarla otra vez enseguida en una pieza que '
                'no traiga nada más nuevo.',
        ),
        ritmos=[
            ('MANO DERECHA', 'entra en el dos, con dos corcheas · andamio',
             [sil('q')] + corch(['E4', 'F#4']) + [n('A4'), n('C5')], OCRE, 'treble', SOL),
            ('MANO IZQUIERDA', 'dos notas largas, y aguantan · andamio',
             [ac(('D3', 'A3'), 'w')], AZUL, 'bass', SOL),
        ],
        especial=[
            'Hay UN sostenido detrás de la clave: todos los Fa van a la tecla negra.',
            'Pone ♩ = 96.',
            'El primer compás lleva un silencio de negra: se entra en el segundo golpe.',
            'Hay compases enteros en los que la derecha no toca nada.',
            'Algunas notas están ligadas a la del compás siguiente.',
            'La digitación viene impresa en los primeros compases.',
        ],
        reto='Los compases de silencio. Cuando la derecha calla un compás entero, es facilísimo entrar '
             'un golpe antes o un golpe después, sobre todo si la izquierda está aguantando y no te da '
             'ninguna pista.',
        truco='Cuenta EN VOZ ALTA los compases en los que no tocas, y cuéntalos más fuerte que los que '
              'sí tocas. Suena raro y funciona: el problema de los silencios largos no es contarlos, '
              'es acordarse de contarlos.',
        sabias='La grabaron en directo en el estudio, los dos a la vez, en vez de por separado como se '
               'hace normalmente. Por eso se oye que se responden: no es un efecto, es que estaban uno '
               'enfrente del otro.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta los compases en los que la voz calla. Son los que te van a costar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La tonalidad ya la sabes de la semana pasada, así que aquí el trabajo es de reloj: '
              'entrar en el dos y contar los compases en los que no tocas. Es un trabajo de voz, no '
              'de dedos.',
        reglas=['SE ENTRA EN EL DOS, NO EN EL UNO', 'LOS COMPASES VACÍOS SE CUENTAN EN VOZ ALTA',
                'LOS FA, EN LA TECLA NEGRA'],
        bloques=[
            dict(num=1, titulo='Entrar en el segundo golpe',
                 pista='c. 1 · el silencio de negra es literal, las notas son andamio',
                 sistemas=[
                     dict(cap='a) silencio, y entras con dos cortas · di "UN" en voz alta y toca en el '
                              'dos',
                          events=[sil('q')] + corch(['A4', 'B4']) + [n('D5'), n('E5')],
                          ligar=True,
                          bars=1, key_sig=SOL),
                     dict(cap='b) y ahora dos veces seguidas, para que el gesto se automatice',
                          events=[sil('q')] + corch(['A4', 'B4']) + [n('D5'), n('E5')] +
                                 [sil('q')] + corch(['A4', 'B4']) + [n('F#5'), n('E5')],
                          bars=2, key_sig=SOL, show_time=False),
                 ]),
            dict(num=2, titulo='El compás en el que no tocas',
                 pista='andamio · cuenta los cuatro golpes en voz alta y más fuerte',
                 sistemas=[
                     dict(cap='a) tocas un compás, callas el siguiente, y vuelves a entrar a tiempo',
                          events=[n('D4'), n('E4'), n('F#4'), n('E4'),
                                  sil('w'),
                                  n('D4'), n('C4'), n('D4'), n('A3')],
                          bars=3, key_sig=SOL),
                     dict(cap='b) y ahora callando dos compases seguidos · aquí es donde se pierde '
                              'todo el mundo, así que cuenta más fuerte',
                          events=[n('F#4'), n('E4'), n('D4'), n('A3'),
                                  sil('w'), sil('w'),
                                  n('D4'), n('E4'), n('F#4'), n('A4')],
                          bars=4, key_sig=SOL, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LAS LIGADURAS QUE CRUZAN LA RAYA',
                 texto='Cuando una raya curva une dos notas iguales a los lados de una barra de compás, '
                       'no son dos notas: es una sola que dura la suma de las dos. Se toca al principio '
                       'y se deja sonar; no se vuelve a apretar. Márcalas a lápiz antes de tocar, '
                       'porque leyendo a velocidad se cuelan casi siempre.'),
            dict(num=3, titulo='La izquierda, y las dos juntas', clef='bass',
                 pista='andamio en Sol mayor · dos notas que duran el compás entero',
                 sistemas=[
                     dict(cap='a) la izquierda sola: entra en el uno y aguanta',
                          events=[ac(('D3', 'A3'), 'w'), ac(('B2', 'F#3'), 'w'),
                                  ac(('G2', 'D3'), 'w'), ac(('A2', 'E3'), 'w')],
                          bars=4, clef='bass', key_sig=SOL),
                     dict(cap='b) y con la derecha encima (andamio) · la derecha entra en el dos y '
                              'la izquierda en el uno: no caen juntas',
                          events=[sil('q')] + corch(['A4', 'B4']) + [n('D5'), n('E5')] +
                                 [n('F#5'), n('E5'), n('D5'), n('A4')],
                          bars=2, key_sig=SOL, show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Shallow · para casa',
            intro='Veinte minutos al día. Esta semana se cuenta en voz alta aunque estés solo en casa.',
            bloques=[
                plan((5, 'Entrar en el dos, diez veces, contando el uno en voz alta'),
                     (5, 'Tocar un compás y callar el siguiente, sin perderse'),
                     (5, 'La melodía despacio, con los Fa en la negra'),
                     (5, 'Las dos manos, cuatro compases con metrónomo')),
                metronomo('La pieza pone ♩ = 96. Empieza a 70 y sube de cinco en cinco.',
                          'Apunta también los días que no toques: el hueco también es información.'),
                ordenar(['Las dos manos, cuatro compases seguidos.',
                         'Marcar a lápiz las ligaduras que cruzan la raya.',
                         'Practicar la entrada en el segundo golpe.',
                         'La melodía sola, comprobando cada Fa.'],
                        titulo='Pon los pasos en el orden bueno',
                        pista='escribe 1, 2, 3 y 4 en las casillas'),
                colorear([n('D4'), n('E4'), n('F#4', 'h'), n('E4'),
                          n('D4'), n('C4', 'h'), n('D4'), n('A3')],
                         ['Un color para las de un golpe y otro para las de dos.'],
                         titulo='Colorea según lo que duran',
                         pista='dos colores'),
                nombres(['D4', 'E4', 'F#4', 'G4', 'A4', 'C4', 'B3', 'D4'],
                        titulo='Los nombres, con la armadura puesta',
                        pista='ojo: en esta pieza el Fa lleva sostenido aunque no esté escrito al lado'),
                para_clase('Los compases en los que no tocas, contados en voz alta, y la entrada '
                           'en el segundo golpe.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
