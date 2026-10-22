# -*- coding: utf-8 -*-
"""The Star-Spangled Banner — pieza 3 de José María. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (arr. Gilbert
   DeBenedetti, "Level 2", 2 páginas):

     - Do mayor: detrás de la clave no hay nada. Compás de 3/4. Pone
       "With pride".
     - EMPIEZA CON SILENCIO: el primer compás lleva un silencio de negra y la
       melodía entra en el segundo golpe. Es la novedad de esta pieza.
     - La digitación viene impresa (3 sobre 1 en el primer acorde, y más
       adelante).
     - Lleva la letra debajo del pentagrama, sílaba a sílaba.
     - La derecha toca en varios sitios DOS NOTAS A LA VEZ.

   Lo que NO se cita nota a nota: la edición mezcla melodía y acordes en el
   mismo pentagrama y la medición de cabezas se ensucia, así que el material
   melódico va rotulado como ANDAMIO en Do mayor y remite a la partitura.
   (Ver TRANSCRIPCION_JM_FUENTES.md.)
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jm_comun import (n, ac, sil, objetivo, plan, rodear, unir, colorear,
                      acuerdate, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='José María', carpeta='JoseMaria', num=3, nivel='iniciación',
    slug='StarSpangledBanner', formato='adulto',
    titulo_corto='The Star-Spangled Banner', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jose_maria', 'source',
                           'Himno de Estados Unidos.pdf'),
    yt='https://www.youtube.com/results?search_query=star+spangled+banner+piano+easy',

    ficha=dict(
        titulo='The Star-Spangled Banner',
        autor='Francis Scott Key y John Stafford Smith · arr. Gilbert DeBenedetti · Level 2',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'With pride'), ('Empieza', 'Con silencio'),
               ('Dedos', 'Escritos')],
        titulo_ritmos='Un compás de cada mano',
        pie_ritmos='Andamio en Do mayor: el dibujo es el de tu partitura y las notas exactas están '
                   'allí. Lo que sí es literal es el silencio del principio.',
        armonia=dict(
            titulo='Lo que cambia respecto a la pieza anterior',
            tarjetas=[
                ('LO NUEVO', 'Entrar tarde',
                 'La melodía no empieza en el primer golpe: hay un silencio delante y se entra en el '
                 'segundo. Contar el hueco es el ejercicio.'),
                ('TAMBIÉN NUEVO', 'Dos a la vez',
                 'En varios sitios la mano derecha toca dos notas al mismo tiempo. Bajan juntas, como '
                 'una sola pieza.'),
                ('IGUAL QUE ANTES', 'Do mayor · 3/4',
                 'Misma tonalidad y mismo compás que America, así que la mano ya sabe dónde está. '
                 'Solo cambia lo que hay que hacer con ella.'),
                ('LA LETRA', 'Va escrita',
                 'Sílaba a sílaba, debajo del pentagrama. Es la forma más fiable de coger el ritmo '
                 'sin contar.'),
            ],
            pie='Es la misma tonalidad y el mismo compás que la pieza 2, y eso es a propósito: cuando '
                'lo nuevo es el ritmo, conviene que las notas sean terreno conocido.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el silencio del principio, y se entra en el dos',
             [sil('q'), n('C4'), n('E4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'una vez por compás, y aguanta · andamio',
             [ac(('C3', 'G3'), 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'El primer compás lleva un silencio de negra: no se toca en el uno.',
            'La digitación viene impresa. En el primer acorde de la derecha pone 3 encima y 1 debajo: '
            'son los dos dedos que bajan a la vez.',
            'La letra va debajo del pentagrama, sílaba a sílaba.',
            'La derecha toca dos notas a la vez en varios compases.',
            'Son dos páginas: la pieza es más larga que las dos anteriores.',
        ],
        reto='Entrar a tiempo después del silencio. Casi todo el mundo entra antes, porque el silencio '
             'se hace largo cuando no suena nada.',
        truco='Cuenta el compás entero en voz alta ANTES de empezar, y entra en el "dos" del segundo '
              'compás de cuenta. O más fácil: di "un" en voz alta y toca en el "dos". Lo importante es '
              'que el uno se oiga, aunque sea con la voz.',
        sabias='La letra la escribió un abogado en 1814 mirando una bandera desde un barco, pero la '
               'música ya existía: era la canción de un club de músicos aficionados de Londres, y era '
               'famosa por lo difícil que resultaba cantarla. Sigue siéndolo.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta con la grabación: fíjate en que la voz entra un golpe después de que '
                      'empiece el acompañamiento.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo único difícil de esta pieza es el principio, y no por las notas: por el hueco que '
              'hay delante. Trabaja primero el hueco solo, sin música, y cuando entres a tiempo diez '
              'veces seguidas, añade la melodía.',
        reglas=['EL SILENCIO SE CUENTA IGUAL QUE UNA NOTA', 'LAS DOS NOTAS BAJAN A LA VEZ',
                'MISMA POSICIÓN QUE LA PIEZA ANTERIOR'],
        bloques=[
            dict(num=1, titulo='El hueco del principio',
                 pista='c. 1 · el silencio de negra es literal, lo demás es andamio',
                 sistemas=[
                     dict(cap='a) silencio y entras · cuenta "UN" en voz alta y toca en el dos',
                          events=[sil('q'), n('C4'), n('E4'),
                                  sil('q'), n('C4'), n('E4')],
                          bars=2),
                     dict(cap='b) y ahora el hueco cambia de sitio · fíjate en que dura lo mismo esté '
                              'donde esté',
                          events=[n('C4'), sil('q'), n('E4'),
                                  n('E4'), n('C4'), sil('q')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL SILENCIO ES LO PRIMERO',
                 texto='Un silencio no es un descanso: es una parte de la música que ocupa su sitio y '
                       'hay que contarla. Si te lo saltas, entras antes de tiempo y a partir de ahí '
                       'toda la pieza va corrida, aunque las notas sean las correctas. Y cuando toques '
                       'con alguien, el que se salta el hueco es el que se pierde.'),
            dict(num=2, titulo='Dos notas a la vez, con la derecha',
                 pista='andamio en Do mayor · en tu partitura llevan la digitación escrita encima y '
                       'debajo',
                 sistemas=[
                     dict(cap='a) las dos bajan juntas, como cuando aplaudes · si oyes dos golpecitos '
                              'seguidos, ve más lento',
                          events=[ac(('C4', 'E4')), ac(('C4', 'E4')), ac(('D4', 'F4')),
                                  ac(('C4', 'E4')), ac(('B3', 'D4')), ac(('C4', 'E4'))],
                          bars=2),
                     dict(cap='b) y mezclando: unas veces una nota y otras dos · es lo que hace la '
                              'pieza de verdad',
                          events=[n('C4'), ac(('C4', 'E4')), n('D4'),
                                  ac(('D4', 'F4')), n('E4'), ac(('C4', 'E4'))],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda, y las dos juntas', clef='bass',
                 pista='andamio · una vez por compás, en el primer golpe',
                 sistemas=[
                     dict(cap='a) la izquierda sola: entra en el uno y aguanta los tres golpes',
                          events=[ac(('C3', 'G3'), 'h.'), ac(('C3', 'F3'), 'h.'),
                                  ac(('B2', 'G3'), 'h.'), ac(('C3', 'G3'), 'h.')],
                          bars=4, clef='bass'),
                     dict(cap='b) y con el silencio del principio delante · la izquierda tampoco '
                              'toca en el uno del primer compás',
                          events=[sil('h.'), ac(('C3', 'G3'), 'h.'),
                                  ac(('B2', 'G3'), 'h.'), ac(('C3', 'G3'), 'h.')],
                          bars=4, clef='bass', show_time=False),
                 ]),
        ] + bloques_extra('Do mayor', 33, 'C5', 'C3',
                          'compás de tres, y la frase empieza antes del primero',
                          desde=4, mas=True, time_sig=(3, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='The Star-Spangled Banner · para casa',
            intro='Veinte minutos al día. Lo que hay que ganar esta semana es entrar a tiempo.',
            bloques=[
                objetivo('Entrar después del silencio a tiempo, diez veces seguidas, sin que nadie '
                         'te cuente. Las notas van después.'),
                plan((5, 'Contar tres golpes en voz alta y entrar en el dos'),
                     (5, 'Los cuatro primeros compases con la derecha sola'),
                     (5, 'Las dos notas a la vez, veinte veces'),
                     (5, 'La izquierda sola: entrar en el uno y aguantar')),
                rodear([[sil('q'), n('C4'), n('E4')], [n('E4'), n('D4'), n('C4')],
                        [sil('q'), n('C4'), n('E4')], [n('C4'), n('E4'), n('G4')]],
                       titulo='Rodea los dos compases iguales',
                       pista='andamio · fíjate también en cuál lleva silencio'),
                unir([('El silencio de negra', 'ir frenando poco a poco'),
                      ('La letra de debajo', 'no se toca, pero se cuenta'),
                      ('Los números de encima', 'te da el ritmo si la dices en voz alta'),
                      ('El "rit." del final', 'qué dedo va en cada nota')],
                     titulo='Une cada cosa de la partitura con lo que es',
                     pista='están desordenadas'),
                colorear([n('C4'), n('E4'), n('C4', 'h'), n('D4'),
                          n('F4'), n('E4', 'h'), n('D4'), n('C4')],
                         ['Un color para las de un golpe y otro para las de dos.'],
                         titulo='Colorea según lo que duran',
                         pista='dos colores'),
                acuerdate('"With pride" no es un adorno del título: es una instrucción. Esta pieza se '
                          'toca con el sonido lleno y sin correr. Si te sale flojita y rápida, está '
                          'mal tocada aunque las notas estén bien.',
                          etiqueta='LO QUE PONE ARRIBA'),
                para_clase('Los cuatro primeros compases con las dos manos, y la duda que te haya '
                           'salido con el silencio del principio.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
