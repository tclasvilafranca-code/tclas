# -*- coding: utf-8 -*-
"""Christmas Songs for Four Little Hands — pieza 8 de Mercè.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Christmas Songs for
   Four Little Hands — Jingle Bells + We Wish You A Merry Christmas", Mindy
   Liang, *Beginner Version*, 2 páginas; el mismo archivo que la pieza 7 de
   Luisa, byte a byte), leído a 230 dpi:

     - Detrás de la clave NO HAY NADA: Do mayor.
     - 4/4, y pone "♩ = 100".
     - Es a cuatro manos, con los dos pentagramas del Piano 1 en clave de
       sol: la melodía arriba en negras y blancas, y la izquierda en
       BLANCAS, dos por compás.
     - Son dos villancicos seguidos en la misma pieza.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from me_comun import n, ac

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Mercè', carpeta='Merce', num=8, nivel='intermedio', slug='ChristmasSongs',
    formato='adulto',
    titulo_corto='Christmas Songs · a cuatro manos', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'merce', 'source',
                           'christmas-songs-for-four-little- 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=jingle+bells+piano+duet+beginner',

    ficha=dict(
        titulo='Christmas Songs',
        autor='Jingle Bells + We Wish You a Merry Christmas · arr. Mindy Liang · a cuatro manos',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Tempo', '♩ = 100'), ('Izquierda', 'Dos blancas'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Dos blancas por compás, bajo la melodía',
        pie_ritmos='Andamio en Do mayor. Lo literal es el reparto: melodía en negras y blancas '
                   'arriba, y la izquierda en dos blancas por compás.',
        armonia=dict(
            titulo='Lo que trae esta pieza',
            tarjetas=[
                ('DOS BLANCAS POR COMPÁS', 'Uno y tres',
                 'La izquierda cambia de nota a mitad de compás, no solo al principio. Es un paso '
                 'más de independencia que las piezas con redonda.'),
                ('DOS VILLANCICOS', 'En la misma pieza',
                 'Primero Jingle Bells y después We Wish You a Merry Christmas, pegados sin pausa. '
                 'Conviene estudiarlos por separado.'),
                ('LAS DOS EN CLAVE DE SOL', 'Sin clave de fa',
                 'Tu parte entera va en clave de sol, arriba y abajo; la izquierda lee igual que la '
                 'derecha, solo más grave.'),
                ('♩ = 100', 'Con número',
                 'Tiene tempo escrito, así que se puede comprobar con el metrónomo si el pulso se '
                 'mantiene igual en las dos canciones.'),
            ],
            pie='Es a cuatro manos: se toca con la profesora, o con quien más practique piano en '
                'casa. La parte de abajo completa la armonía que aquí no se ve.',
        ),
        ritmos=[
            ('MANO DERECHA', 'negras y blancas, la melodía · andamio',
             [n('E4'), n('E4'), n('E4', 'h')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos blancas por compás · literal',
             [n('D4', 'h'), n('A3', 'h')], AZUL, 'treble', None),
        ],
        especial=[
            'Detrás de la clave no hay nada.',
            'Compás de 4/4, con "♩ = 100" escrito arriba.',
            'Tus dos pentagramas van en clave de sol.',
            'La izquierda hace dos blancas por compás: una en el uno y otra en el tres.',
            'La pieza son dos villancicos seguidos, y conviene estudiarlos por separado.',
            'La otra parte, la de abajo, la toca la profesora o quien toque contigo.',
        ],
        reto='Que la izquierda cambie de nota en el tercer tiempo sin que la derecha se frene. Las '
             'dos manos se mueven en momentos distintos, y eso pide más atención que moverse juntas.',
        truco='Toca solo la izquierda contando "UN, dos, TRES, cuatro" en voz alta, marcando fuerte '
              'el uno y el tres, hasta que el cambio de nota salga sin pensarlo. Solo entonces añade '
              'la melodía.',
        sabias='Jingle Bells no se escribió para Navidad: se compuso en 1857 para una función de '
               'Acción de Gracias y habla de carreras de trineos por la nieve, no de Papá Noel.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuántas veces se repite la melodía de cada villancico. Cuando lo veas, '
                      'la pieza se hace la mitad de larga de memorizar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo es que la izquierda cambia de nota a mitad de compás. Se estudia sola, '
              'luego la melodía, y las dos canciones siempre por separado.',
        reglas=['LA IZQUIERDA CAMBIA EN EL TRES', 'CUENTA "UN, DOS, TRES, CUATRO"',
                'LOS DOS VILLANCICOS, CADA UNO POR SU LADO'],
        bloques=[
            dict(num=1, titulo='La izquierda: dos blancas por compás',
                 pista='andamio en Do mayor · la forma es la de tu partitura',
                 sistemas=[
                     dict(cap='a) una en el uno y otra en el tres, sin pararse a pensarlo',
                          events=[n('C4', 'h'), n('G3', 'h'), n('F3', 'h'), n('C4', 'h')],
                          bars=2),
                     dict(cap='b) cambiando de acorde, con el dedo ya preparado antes de tiempo',
                          events=[n('D4', 'h'), n('A3', 'h'), n('G3', 'h'), n('D4', 'h')],
                          bars=2, show_time=False),
                 ]),
            dict(num=2, titulo='La melodía de Jingle Bells',
                 pista='andamio en Do mayor · negras y blancas, nada más',
                 sistemas=[
                     dict(cap='a) tres notas iguales y una larga: así empiezan las dos frases',
                          events=[n('G4'), n('G4'), n('G4', 'h'), n('A4'), n('A4'), n('A4', 'h')],
                          bars=2),
                     dict(cap='b) y la frase que sube y baja, con la última aguantada entera',
                          events=[n('G4'), n('C5'), n('D5'), n('E5'), n('F5', 'w')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LOS DOS VILLANCICOS POR SEPARADO',
                 texto='Son dos canciones distintas escritas una detrás de otra sin pausa. Si se '
                       'estudian seguidas de principio a fin, la segunda siempre sale peor que la '
                       'primera porque recibe menos tiempo de trabajo. Aprende una entera antes de '
                       'tocar la otra, y solo júntalas cuando las dos salgan bien por separado.'),
            dict(num=3, titulo='Las dos manos, dos compases',
                 pista='andamio · muy despacio, contando en voz alta',
                 sistemas=[
                     dict(cap='a) arriba la melodía y abajo las dos blancas: la izquierda no se '
                              'para cuando la derecha se mueve',
                          events=[ac(('C4', 'G4')), n('G4'), ac(('G3', 'G4'), 'h'),
                                  ac(('F3', 'A4')), n('A4'), ac(('C4', 'A4'), 'h')],
                          bars=2),
                     dict(cap='b) y con el segundo villancico, que empieza más abajo',
                          events=[ac(('D4', 'D5')), n('C5'), ac(('A3', 'B4'), 'h'),
                                  ac(('G3', 'C5')), n('B4'), ac(('D4', 'A4'), 'h')],
                          bars=2, show_time=False),
                 ]),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
