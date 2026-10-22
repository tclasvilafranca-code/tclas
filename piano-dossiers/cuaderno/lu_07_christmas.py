# -*- coding: utf-8 -*-
"""Christmas Songs for Four Little Hands — pieza 7 de Luisa. Formato adulto.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Christmas Songs for Four
   Little Hands — Jingle Bells + We Wish You A Merry Christmas", Mindy Liang,
   marcado "Beginner Version", 2 páginas):

     - Detrás de la clave no hay nada: Do mayor.
     - 4/4, y pone "♩ = 100".
     - Es a cuatro manos. El Piano 1 lleva LOS DOS PENTAGRAMAS EN CLAVE DE SOL:
       la melodía arriba, en negras y blancas, y la izquierda en BLANCAS.
     - Son dos villancicos seguidos en la misma pieza.
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
    alumno='Luisa', carpeta='Luisa', num=7, nivel='iniciación', slug='ChristmasSongs',
    formato='adulto',
    titulo_corto='Christmas Songs · a cuatro manos', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'luisa', 'source',
                           'christmas-songs-(4 manos).pdf'),
    yt='https://www.youtube.com/results?search_query=jingle+bells+piano+duet+beginner',

    ficha=dict(
        titulo='Christmas Songs',
        autor='Jingle Bells + We Wish You a Merry Christmas · arr. Mindy Liang · a cuatro manos',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 100'), ('Izquierda', 'Blancas'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Melodía arriba, blancas abajo',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: la melodía en negras y blancas '
                   'arriba, y la izquierda en blancas, dos por compás.',
        armonia=dict(
            titulo='Dos villancicos en una pieza',
            tarjetas=[
                ('LA IZQUIERDA SE MUEVE', 'Blancas',
                 'Hasta ahora hacía una redonda y esperaba. Ahora hace DOS notas por compás, una '
                 'en el uno y otra en el tres. Es el primer paso hacia acompañar de verdad.'),
                ('DOS CANCIONES', 'Seguidas',
                 'Primero Jingle Bells y después We Wish You a Merry Christmas. Son dos piezas '
                 'cortas pegadas, y se estudian por separado.'),
                ('LAS DOS EN SOL', 'La misma clave',
                 'Tu parte lleva los dos pentagramas en clave de sol, como las tres primeras del '
                 'cuaderno.'),
                ('♩ = 100', 'Con número',
                 'Tiene velocidad escrita, así que se puede comprobar con el metrónomo si vas o no '
                 'vas.'),
            ],
            pie='Es de Navidad, así que se trabaja en diciembre. Y es a cuatro manos: se toca con '
                'la profesora, o con Arnau, que es de la familia y también toca.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, negras y blancas · andamio',
             [n('E5'), n('E5'), n('E5', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos blancas por compás · literal',
             [n('C4', 'h'), n('G4', 'h')], AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4 y "♩ = 100" escrito arriba.',
            'Tus dos pentagramas van en clave de sol.',
            'La izquierda hace dos blancas por compás: una en el uno y otra en el tres.',
            'La pieza son dos villancicos seguidos: Jingle Bells y We Wish You a Merry Christmas.',
            'La otra parte la toca la profesora.',
        ],
        reto='Que la izquierda cambie de nota en el tercer golpe sin frenar la derecha. Es la '
             'primera vez que las dos manos se mueven en momentos distintos.',
        truco='Toca solo la izquierda contando "UN, dos, TRES, cuatro" en voz alta, marcando el uno '
              'y el tres. Hazlo hasta que puedas hablar de otra cosa mientras tocas. Entonces pon '
              'la derecha encima.',
        sabias='Jingle Bells no era un villancico: se escribió en 1857 para el día de Acción de '
               'Gracias y habla de carreras de trineos, no de Navidad. Se coló en la Navidad sola, '
               'por costumbre.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuántas veces se repite la melodía. Cuando lo veas, la pieza se te '
                      'hace la mitad de larga.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo está abajo: la izquierda deja de esperar y cambia de nota a mitad de '
              'compás. Ese es todo el trabajo.',
        reglas=['LA IZQUIERDA CAMBIA EN EL TRES', 'CUENTA "UN, DOS, TRES, CUATRO"',
                'LOS DOS VILLANCICOS, POR SEPARADO'],
        bloques=[
            dict(num=1, titulo='La izquierda: dos blancas por compás',
                 pista='andamio en Do mayor · la forma es la de tu partitura, y va en clave de sol',
                 sistemas=[
                     dict(cap='a) una en el uno y otra en el tres · cuenta en voz alta y cambia '
                              'justo en el tres',
                          events=[n('C4', 'h'), n('G4', 'h'), n('C4', 'h'), n('G4', 'h')],
                          bars=2),
                     dict(cap='b) cambiando de acorde · el dedo nuevo se prepara antes de que le '
                              'toque',
                          events=[n('F4', 'h'), n('C4', 'h'), n('G4', 'h'), n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La melodía de Jingle Bells',
                 pista='andamio en Do mayor · negras y blancas, nada más',
                 sistemas=[
                     dict(cap='a) tres notas iguales y una larga · así empiezan las dos frases',
                          events=[n('E5'), n('E5'), n('E5', 'h'), n('E5'), n('E5'), n('E5', 'h')],
                          bars=2),
                     dict(cap='b) y la frase que sube y baja · la última se aguanta entera',
                          events=[n('E5'), n('G5'), n('C5'), n('D5'), n('E5', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LOS DOS VILLANCICOS POR SEPARADO',
                 texto='Son dos canciones distintas escritas una detrás de otra. Si las estudias '
                       'seguidas, la segunda siempre sale peor que la primera, porque le dedicas la '
                       'mitad de tiempo. Trabaja una esta semana y la otra la siguiente, y luego '
                       'júntalas.'),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='andamio · muy despacio, y contando en voz alta',
                 sistemas=[
                     dict(cap='a) arriba la melodía y abajo las dos blancas · la izquierda no se '
                              'para cuando la derecha se mueve',
                          events=[ac(('C4', 'E5')), n('E5'), ac(('G4', 'E5'), 'h'),
                                  ac(('C4', 'E5')), n('E5'), ac(('G4', 'E5'), 'h')],
                          bars=2),
                     dict(cap='b) y con el segundo villancico, que empieza más abajo · la izquierda '
                              'hace exactamente lo mismo',
                          events=[ac(('C4', 'C5')), n('C5'), ac(('G4', 'D5'), 'h'),
                                  ac(('F4', 'C5')), n('B4'), ac(('C5', 'A4'), 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
