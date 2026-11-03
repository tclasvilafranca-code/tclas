# -*- coding: utf-8 -*-
"""The Star-Spangled Banner — pieza 5 de Eduard. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta (arr. Gilbert DeBenedetti,
   "Level 2", 2 páginas; el mismo archivo que la pieza 3 de José María,
   byte a byte):

     - Do mayor: detrás de la clave no hay nada. Compás de 3/4. Pone
       "With pride".
     - EMPIEZA CON SILENCIO: el primer compás lleva un silencio de negra y la
       melodía entra en el segundo golpe.
     - La digitación viene impresa.
     - Lleva la letra debajo del pentagrama, sílaba a sílaba.
     - La derecha toca en varios sitios DOS NOTAS A LA VEZ.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from ed_comun import n, ac, sil, objetivo, plan, rodear, unir, colorear, acuerdate, para_clase

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eduard', carpeta='Eduard', num=5, nivel='iniciación',
    slug='StarSpangledBanner', formato='adulto',
    titulo_corto='The Star-Spangled Banner', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eduard', 'source',
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
                 'La melodía no empieza en el primer golpe: hay un silencio delante y se entra en '
                 'el segundo. Contar el hueco es el ejercicio.'),
                ('TAMBIÉN NUEVO', 'Dos a la vez',
                 'En varios sitios la mano derecha toca dos notas al mismo tiempo. Bajan juntas, '
                 'como una sola pieza.'),
                ('IGUAL QUE ANTES', 'Do mayor · 3/4',
                 'Misma tonalidad y mismo compás que America, así que la mano ya sabe dónde está. '
                 'Solo cambia lo que hay que hacer con ella.'),
                ('LA LETRA', 'Va escrita',
                 'Sílaba a sílaba, debajo del pentagrama. Es la forma más fiable de coger el ritmo '
                 'sin contar.'),
            ],
            pie='Es la misma tonalidad y el mismo compás que la pieza 2, y eso es a propósito: '
                'cuando lo nuevo es el ritmo, conviene que las notas sean terreno conocido.',
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
            'La digitación viene impresa.',
            'La letra va debajo del pentagrama, sílaba a sílaba.',
            'La derecha toca dos notas a la vez en varios compases.',
            'Son dos páginas: la pieza es más larga que las dos anteriores.',
        ],
        reto='Entrar a tiempo después del silencio. Casi todo el mundo entra antes, porque el '
             'silencio se hace largo cuando no suena nada.',
        truco='Cuenta el compás entero en voz alta ANTES de empezar, y entra en el "dos" del '
              'segundo compás de cuenta.',
        sabias='La letra la escribió un abogado en 1814 mirando una bandera desde un barco, pero la '
               'música ya existía: era la canción de un club de músicos aficionados de Londres.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta con la grabación: fíjate en que la voz entra un golpe después.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo único difícil de esta pieza es el principio, y no por las notas: por el hueco que '
              'hay delante. Trabaja primero el hueco solo, sin música.',
        reglas=['EL SILENCIO SE CUENTA IGUAL QUE UNA NOTA', 'LAS DOS NOTAS BAJAN A LA VEZ',
                'MISMA POSICIÓN QUE LA PIEZA ANTERIOR'],
        bloques=[
            dict(num=1, titulo='El hueco del principio',
                 pista='c. 1 · el silencio de negra es literal, lo demás es andamio',
                 sistemas=[
                     dict(cap='a) silencio y entras, con otro dibujo',
                          events=[sil('q'), n('D4'), n('F4'),
                                  sil('q'), n('D4'), n('F4')],
                          bars=2),
                     dict(cap='b) y ahora el hueco cambia de sitio',
                          events=[n('D4'), sil('q'), n('F4'),
                                  n('F4'), n('D4'), sil('q')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL SILENCIO ES LO PRIMERO',
                 texto='Un silencio no es un descanso: es una parte de la música que ocupa su sitio '
                       'y hay que contarla. Si te lo saltas, entras antes de tiempo y a partir de '
                       'ahí toda la pieza va corrida, aunque las notas sean las correctas.'),
            dict(num=2, titulo='Dos notas a la vez, con la derecha',
                 pista='andamio en Do mayor · en tu partitura llevan la digitación escrita',
                 sistemas=[
                     dict(cap='a) las dos bajan juntas, con otro par de notas',
                          events=[ac(('D4', 'F4')), ac(('D4', 'F4')), ac(('E4', 'G4')),
                                  ac(('D4', 'F4')), ac(('C4', 'E4')), ac(('D4', 'F4'))],
                          bars=2),
                     dict(cap='b) y mezclando: unas veces una nota y otras dos',
                          events=[n('D4'), ac(('D4', 'F4')), n('E4'),
                                  ac(('E4', 'G4')), n('F4'), ac(('D4', 'F4'))],
                          bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda, y las dos juntas', clef='bass',
                 pista='andamio · una vez por compás, en el primer golpe',
                 sistemas=[
                     dict(cap='a) la izquierda sola: entra en el uno y aguanta',
                          events=[ac(('D3', 'A3'), 'h.'), ac(('D3', 'G3'), 'h.'),
                                  ac(('C3', 'A3'), 'h.'), ac(('D3', 'A3'), 'h.')],
                          bars=4, clef='bass'),
                     dict(cap='b) y con el silencio del principio delante',
                          events=[sil('h.'), ac(('D3', 'A3'), 'h.'),
                                  ac(('C3', 'A3'), 'h.'), ac(('D3', 'A3'), 'h.')],
                          bars=4, clef='bass', show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='The Star-Spangled Banner · para casa',
            intro='Veinte minutos al día. Lo que hay que ganar esta semana es entrar a tiempo.',
            bloques=[
                objetivo('Entrar después del silencio a tiempo, diez veces seguidas, sin que nadie '
                         'te cuente.'),
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
                acuerdate('"With pride" no es un adorno del título: es una instrucción. Esta pieza '
                          'se toca con el sonido lleno y sin correr.',
                          etiqueta='LO QUE PONE ARRIBA'),
                para_clase('Los cuatro primeros compases con las dos manos, y la duda que te haya '
                           'salido con el silencio del principio.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
