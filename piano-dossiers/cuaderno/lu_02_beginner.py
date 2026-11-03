# -*- coding: utf-8 -*-
"""The Beginner, de Gurlitt — pieza 2 de Luisa. Formato adulto, iniciación.

   Lo comprobado sobre el PDF de su carpeta de Drive ("The Beginner, Le Début,
   Der Anfänger — 22 Melodic Studies, Piano 4-Hands, op. 211, no. 3",
   Cornelius Gurlitt, 1 página):

     - Detrás de la clave no hay nada: Do mayor.
     - 3/4, y pone "Allegretto".
     - Es a cuatro manos. El Primo lleva LOS DOS PENTAGRAMAS EN CLAVE DE SOL,
       con 8va encima, y las dos manos tocan lo mismo a distancia de octava.
     - Solo negras, blancas y blancas con puntillo. Hay ligaduras de frase.
     - Trae reguladores escritos (crescendo y diminuendo) desde el compás 1.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from lu_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Luisa', carpeta='Luisa', num=2, nivel='iniciación', slug='TheBeginner',
    formato='adulto',
    titulo_corto='The Beginner · Gurlitt', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           'The Beginner Le Debut.pdf'),
    yt='https://www.youtube.com/results?search_query=gurlitt+op+211+the+beginner+piano+4+hands',

    ficha=dict(
        titulo='The Beginner',
        autor='Cornelius Gurlitt · op. 211 nº 3 · a cuatro manos · tu parte es la de arriba',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'Allegretto'), ('Manos', 'Las dos igual'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Tres golpes por compás',
        pie_ritmos='Andamio en Do mayor. Lo importante es lo mismo que en la pieza 1: arriba y '
                   'abajo es el mismo dibujo, una octava más grave.',
        armonia=dict(
            titulo='Lo nuevo respecto a la primera',
            tarjetas=[
                ('TRES, NO CUATRO', 'Compás de 3/4',
                 'Ahora se cuenta "un, dos, tres". El primer golpe pesa un poco más que los otros '
                 'dos: eso es lo único que hay que hacer para que suene a vals.'),
                ('LAS DOS IGUAL', 'Otra vez',
                 'Igual que en la Sonatina: las dos manos tocan lo mismo. Ya sabes hacerlo.'),
                ('LAS RAYAS', 'Fuerte y flojo',
                 'Encima del pentagrama hay unas rayas que se abren y se cierran. Cuando se abren, '
                 'un poco más fuerte; cuando se cierran, un poco más flojo.'),
                ('LAS LIGADURAS', 'Sin cortar',
                 'La rayita curva que une varias notas quiere decir que van seguidas, sin levantar '
                 'la mano entre una y otra.'),
            ],
            pie='La pieza se llama "El principiante" y está escrita para eso mismo. Gurlitt hizo '
                'veintidós, y esta es la tercera: son de las pocas piezas para empezar que suenan '
                'bien de verdad.',
        ),
        ritmos=[
            ('MANO DERECHA', 'tres negras por compás · andamio',
             [n('E5'), n('E5'), n('E5')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'lo mismo, más grave · andamio',
             [n('E4'), n('E4'), n('E4')], AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada: todo son teclas blancas.',
            'Compás de 3/4: tres golpes en cada compás.',
            'Pone "Allegretto": alegre, pero sin correr.',
            'Tus dos pentagramas van en clave de sol, y las dos manos tocan lo mismo.',
            'Encima hay un 8va: suena una octava más alto de lo escrito.',
            'Hay reguladores escritos desde el primer compás: un poco más fuerte, un poco más flojo.',
        ],
        reto='Contar tres y no cuatro. Venimos de una pieza de cuatro golpes, y la mano sola se va '
             'al cuatro sin que te des cuenta.',
        truco='Cuenta "UN, dos, tres" en voz alta antes de tocar una sola nota, y sigue contando '
              'mientras tocas. En voz alta de verdad, no por dentro: contar por dentro es justo lo '
              'que deja de hacerse cuando la música se complica.',
        sabias='Gurlitt fue profesor de piano en Hamburgo y escribió cientos de piezas cortas para '
               'sus alumnos. Casi nadie recuerda su nombre y casi todo el que aprende piano ha '
               'tocado algo suyo.',
        qr=dict(titulo='Escúchala',
                texto='Mientras la escuchas, lleva el pulso con el pie. Verás que va de tres en '
                      'tres, y no de cuatro en cuatro.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo mismo que la semana pasada, pero contando tres. Empieza contando sin tocar.',
        reglas=['CUENTA "UN, DOS, TRES" EN VOZ ALTA', 'EL PRIMERO PESA, LOS OTROS DOS NO',
                'UNA MANO Y DESPUÉS LAS DOS'],
        bloques=[
            dict(num=1, titulo='Tres golpes por compás, mano derecha',
                 pista='andamio en Do mayor · cuenta en voz alta desde antes de empezar',
                 sistemas=[
                     dict(cap='a) tres negras iguales · el primero pesa un poco más, nada más',
                          events=[n('E5'), n('E5'), n('E5'), n('G5'), n('F5'), n('E5')],
                          ligar=True,
                          cresc=4,
                          bars=2, time_sig=(3, 4)),
                     dict(cap='b) y con la blanca con puntillo, que llena el compás entero · aguanta '
                              'los tres golpes',
                          events=[n('D5'), n('E5'), n('F5'), n('E5', 'h.')],
                          bars=2, time_sig=(3, 4), show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LA BLANCA CON PUNTILLO',
                 texto='Una blanca vale dos golpes. El puntito de al lado le añade la mitad, así que '
                       'vale tres: justo un compás entero de esta pieza. Cuando la veas, cuenta "un, '
                       'dos, tres" con la tecla bajada y no la sueltes hasta el tres.'),
            dict(num=2, titulo='La izquierda, que hace lo mismo',
                 pista='andamio · el mismo dibujo, una octava más abajo',
                 sistemas=[
                     dict(cap='a) las mismas notas, más graves · también en clave de sol',
                          events=[n('E4'), n('E4'), n('E4'), n('G4'), n('F4'), n('E4')],
                          bars=2, time_sig=(3, 4)),
                     dict(cap='b) y bajando hasta la nota de casa · la última se aguanta entera',
                          events=[n('G4'), n('F4'), n('E4'), n('D4'), n('C4', 'h')],
                          bars=2, time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=3, titulo='Las dos juntas',
                 pista='andamio · despacio, y contando en voz alta',
                 sistemas=[
                     dict(cap='a) un solo sonido, no dos · si oyes dos golpecitos, ve más lento',
                          events=[ac(('E4', 'E5')), ac(('E4', 'E5')), ac(('E4', 'E5')),
                                  ac(('G4', 'G5')), ac(('F4', 'F5')), ac(('E4', 'E5'))],
                          bars=2, time_sig=(3, 4)),
                     dict(cap='b) y acabando en una nota larga, que es como cierra cada frase',
                          events=[ac(('D4', 'D5')), ac(('E4', 'E5')), ac(('F4', 'F5')),
                                  ac(('E4', 'E5'), 'h.')],
                          bars=2, time_sig=(3, 4), show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
