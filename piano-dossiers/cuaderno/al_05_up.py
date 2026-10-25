# -*- coding: utf-8 -*-
"""Up, tema principal — pieza 5 de Alan. ADULTO exigente, tono de 12 años.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Up - Main theme", Easy
   version, 1 página, imagen a 55 ppp), mirado a 230-260 ppp:

     - FA MAYOR: un bemol detrás de la clave (se ve entero y a tamaño grande).
       3/4. Pone "p" en la primera nota y no trae tempo.
     - c. 1: la izquierda es un silencio de compás entero y la derecha empieza
       con un silencio de negra, un silencio de corchea y tres corcheas.
     - c. 2: una blanca con puntillo en la derecha y un acorde de tres notas
       en la izquierda, y así en casi toda la página.
     - A partir del c. 18 la derecha lleva grupos de corcheas y semicorcheas, y la
       izquierda cambia a clave de sol al final del c. 18.
     - Hay becuadros delante de los acordes de la izquierda.
   Es una imagen de poca resolución: las alturas exactas no se distinguen a
   ojo, y por eso todo el material con notas va como ANDAMIO en Fa mayor.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from al_comun import (n, ac, sil, reto, plan, escalera, inventa, teclado,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')
FA = 'Fa mayor'

CANCION = dict(
    alumno='Alan', carpeta='Alan', num=5, nivel='intermedio', slug='Up',
    formato='adulto',
    titulo_corto='Up · tema principal', time_sig=(3, 4), key_sig=FA,
    partitura=os.path.join(HERE, '..', 'students', 'alan', 'source', 'UP.'),
    yt='https://www.youtube.com/results?search_query=up+married+life+piano+easy',

    ficha=dict(
        titulo='Up · tema principal',
        autor='Easy version · el tema de la película Up',
        datos=[('Tonalidad', 'Fa mayor'), ('Compás', '3/4'),
               ('Carácter', 'p · sin tempo'), ('Armadura', 'Un bemol'),
               ('Páginas', 'Una')],
        titulo_ritmos='Cómo empieza, y la izquierda en acordes',
        pie_ritmos='Andamio en Fa mayor sobre lo que trae tu partitura: la derecha empieza con dos '
                   'silencios y tres corcheas, y la izquierda toca acordes de tres notas en '
                   'blanca con puntillo.',
        armonia=dict(
            titulo='Un vals con silencios, un bemol y un cambio de clave',
            tarjetas=[
                ('EL 3/4', 'Tres golpes, un vals',
                 'Tres negras por compás: se cuenta uno-dos-tres con el primer golpe más fuerte. '
                 'La blanca con puntillo ocupa el compás entero.'),
                ('EL COMIENZO', 'Dos silencios',
                 'La pieza no arranca en el uno: la derecha cuenta un silencio de negra y uno de '
                 'corchea, y entra con tres corcheas. La izquierda ni siquiera toca el primer '
                 'compás.'),
                ('EL BEMOL', 'Todos los Si',
                 'Detrás de la clave hay un bemol: todos los Si suenan a la tecla negra. Es la '
                 'primera cosa que hay que mirar, y la más fácil de olvidar.'),
                ('EL CAMBIO DE CLAVE', 'En el c. 18',
                 'Al final del c. 18 la izquierda pasa a clave de sol: las notas siguen siendo '
                 'las de abajo, pero se leen con otra clave.'),
            ],
            pie='La pieza es una página y es de las más cantables del cuaderno. Lo que cuesta no es '
                'tocarla, es tocarla tranquila y sin prisa.',
        ),
        ritmos=[
            ('MANO DERECHA', 'andamio · dos silencios y tres corcheas',
             [sil('q'), sil('e'), n('F4', 'e'), n('A4', 'e'), n('F4', 'e')], OCRE, 'treble', FA),
            ('MANO IZQUIERDA', 'andamio · un acorde en blanca con puntillo',
             [ac(('F2', 'C3', 'A3'), 'h.'), ac(('F2', 'C3', 'A3'), 'h.')], AZUL, 'bass', FA),
        ],
        especial=[
            'Detrás de la clave hay un bemol: todos los Si suenan a la tecla negra.',
            'El compás es 3/4. Pone p en la primera nota y no trae tempo.',
            'La derecha empieza con un silencio de negra, uno de corchea y tres corcheas.',
            'La izquierda no toca el primer compás: es un silencio de compás entero.',
            'Desde el c. 18 aparecen semicorcheas, y la izquierda cambia a clave de sol.',
            'Hay becuadros delante de algunos acordes de la izquierda.',
        ],
        reto='Entrar bien tras los dos silencios: la melodía no cae en el uno, y las tres corcheas '
             'tienen que salir iguales y tranquilas, no apresuradas.',
        truco='Cuenta "uno-dos-tres" en voz baja y entra en el "y" del segundo tiempo. Si '
              'te precipitas, di el silencio de corchea en voz alta: el "y" es tuyo.',
        sabias='Up es de Pixar, de 2009. La música es de Michael Giacchino, que ganó el Óscar por '
               'ella: el tema principal acompaña la escena muda de la vida del protagonista, sin '
               'una sola palabra.',
        qr=dict(titulo='Escúchala',
                texto='Escucha cómo el vals se repite y cambia de color cada vez. Tu partitura '
                      'hace lo mismo con las notas largas de la izquierda.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Es un vals: tres golpes, uno fuerte y dos suaves. Se estudia contando alto, con la '
              'izquierda de acordes largos y la derecha entrando detrás de los silencios.',
        reglas=['UNO FUERTE, DOS Y TRES SUAVES', 'EL BEMOL EN TODOS LOS SI', 'ENTRAR DESPUÉS DEL SILENCIO'],
        bloques=[
            dict(num=1, titulo='La entrada con dos silencios',
                 pista='c. 1 · el ritmo es el de tu partitura · las notas son andamio en Fa mayor',
                 sistemas=[
                     dict(cap='a) un silencio de negra, uno de corchea y tres corcheas · cuenta '
                              '"uno-dos-y-tres-y" y entra en la "y" del dos',
                          events=[sil('q'), sil('e'), n('F4', 'e'), n('G4', 'e'), n('F4', 'e')],
                          bars=1, key_sig=FA, matiz='p'),
                     dict(cap='b) el mismo ritmo en otras notas · andamio · el Si bemol aparece '
                              'sin signo, porque ya está en la clave',
                          events=[sil('q'), sil('e'), n('A4', 'e'), n('Bb4', 'e'), n('A4', 'e')],
                          bars=1, key_sig=FA, show_time=False),
                 ]),
            dict(num=2, titulo='La blanca con puntillo',
                 pista='c. 2 · el ritmo es el de tu partitura · una blanca con puntillo llena el '
                       'compás de tres golpes',
                 sistemas=[
                     dict(cap='a) una nota de tres golpes · cuenta uno-dos-tres sin soltarla antes '
                              'de tiempo',
                          events=[n('A4', 'h.'), n('G4', 'h.')],
                          bars=2, key_sig=FA),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ UN VALS SE CUENTA EN TRES',
                 texto='En un compás de 3/4 caben tres negras, y el primer golpe pesa más que los '
                       'otros dos. Si lo cuentas en seis, la música se vuelve una marcha lenta; si '
                       'lo cuentas en uno, un balanceo. Cuenta tres y acentúa el primero con la '
                       'cabeza.'),
            dict(num=3, titulo='La izquierda: un acorde por compás',
                 pista='andamio sobre Fa mayor · la izquierda toca el mismo acorde largo mientras la '
                       'derecha canta',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) tres acordes de blanca con puntillo · Fa, Si♭ y Do · el cambio '
                              'de acorde es el único trabajo de la mano',
                          events=[ac(('F2', 'C3', 'A3'), 'h.'), ac(('Bb2', 'D3', 'F3'), 'h.'),
                                  ac(('C3', 'E3', 'G3'), 'h.')],
                          bars=3, clef='bass', key_sig=FA),
                 ]),
            dict(num=4, titulo='Los grupos con semicorcheas del c. 18',
                 pista='andamio · desde el c. 18 la derecha lleva grupos de corcheas y semicorcheas',
                 sistemas=[
                     dict(cap='a) una corchea y dos semicorcheas dentro del mismo golpe · las dos '
                              'cortas caben donde cabría una corchea',
                          events=[sil('q'), n('A4', 'e'), n('G4', 's'), n('A4', 's'),
                                  n('Bb4', 'e'), n('A4', 's'), n('G4', 's')],
                          bars=1, key_sig=FA),
                 ]),
            dict(num=5, titulo='La misma izquierda, en clave de sol',
                 pista='andamio · al final del c. 18 la izquierda se lee con clave de sol: las '
                       'notas se mueven a otro sitio del pentagrama',
                 sistemas=[
                     dict(cap='a) un acorde de Fa en clave de fa, como en casi toda la pieza',
                          events=[ac(('F2', 'C3', 'A3'), 'h.')],
                          bars=1, clef='bass', key_sig=FA),
                     dict(cap='b) el mismo acorde, una octava más arriba, en clave de sol · las '
                              'tres notas siguen siendo Fa, Do y La',
                          events=[ac(('F3', 'C4', 'A4'), 'h.')],
                          bars=1, key_sig=FA, show_time=False),
                 ]),
        ] + bloques_extra(FA, 5, 'F4', 'F2',
                          'el vals se cuenta en tres y el Si es siempre bemol',
                          desde=6, time_sig=(3, 4)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Up · para casa',
            intro='Veinte minutos al día. Es tranquila, así que el reto no es la velocidad: es '
                  'que no se note ninguna.',
            bloques=[
                reto('Tocar los ocho primeros compases con la entrada limpia tras los silencios, tres '
                     'veces seguidas, sin que se apresuren las corcheas.',
                     'Cuenta en voz alta "uno-dos-tres" y apunta cuántas veces seguidas lo '
                     'consigues. Si una vez entras antes de tiempo, vuelves a cero.'),
                plan((4, 'Los acordes de la izquierda, uno por compás'),
                     (6, 'La entrada con dos silencios, diez veces'),
                     (5, 'La derecha sola, cc. 1-8'),
                     (5, 'Las dos manos, cc. 1-8')),
                escalera((50, 'la derecha sola, cc. 1-4'),
                         (60, 'las dos manos, cc. 1-4'),
                         (72, 'los cc. 1-8'),
                         (84, 'la página hasta el c. 17'),
                         meta='Tu partitura no trae número de metrónomo: la meta la eliges tú y la '
                              'apuntas a lápiz.',
                         titulo='La escalera del metrónomo'),
                inventa(['Dos compases en 3/4.',
                         'Que empiecen con un silencio de negra.',
                         'Con una blanca con puntillo en el segundo compás.'],
                        time_sig=(3, 4),
                        titulo='Inventa dos compases como los del principio',
                        pista='con el material de tu partitura de esta semana, pero tuyo'),
                teclado({0: 1, 3: 2, 5: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         'La número 2 es la tónica de la pieza: el Fa.'],
                        titulo='En el teclado',
                        pista='son las notas de un acorde de Fa: las tres teclas se tocan a la vez'),
                para_clase('Los cc. 1-8 con las dos manos tranquilos, y si la entrada tras los '
                           'silencios te sale a la primera. Si te pasa que entras antes, '
                           'tráelo: se arregla contando en voz alta.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
