# -*- coding: utf-8 -*-
"""My Favourite Things (The Sound of Music) — pieza 15 de Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Rodgers y Hammerstein,
   arreglo de Kaitlin, Musescore, 1 página, 55 compases):

     - UN SOSTENIDO detrás de la clave, y la música empieza y descansa en Mi:
       Mi menor, con el estribillo pasando a Sol mayor.
     - 3/4, y pone "♩ = 160". Es el tempo más alto del cuaderno.
     - CIFRADO IMPRESO encima del pentagrama: Em · C · Am · D · G · B.
     - La izquierda hace acordes con puntillo, uno por compás, y luego pasa a
       tres golpes por compás.
     - Hay barras de repetición, casilla de primera y segunda vez, calderón y
       acentos escritos (>) en la última parte.
     - 55 compases en una sola página: es la pieza más apretada de leer.

   Todo el material inventado va como ANDAMIO en Mi menor y remite a la
   partitura.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, reto, plan, escalera, cifrado, colorear, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=15, nivel='intermedio', slug='MyFavouriteThings',
    formato='adulto',
    titulo_corto='My Favourite Things', time_sig=(3, 4), key_sig='Mi menor',
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'my-favourite-things-the-sound-.pdf'),
    yt='https://www.youtube.com/results?search_query=my+favourite+things+piano+easy',

    ficha=dict(
        titulo='My Favourite Things',
        autor='Richard Rodgers y Oscar Hammerstein II · arreglo de Kaitlin',
        datos=[('Tonalidad', 'Mi menor'), ('Compás', '3/4'),
               ('Tempo', '♩ = 160'), ('Cifrado', 'Impreso'),
               ('Páginas', 'Una · 55 compases')],
        titulo_ritmos='Un vals rápido',
        pie_ritmos='Andamio en Mi menor. Lo literal es el reparto: melodía en negras arriba y un '
                   'acorde por compás abajo, en compás de tres y a ♩ = 160.',
        armonia=dict(
            titulo='Rápida, larga y apretada',
            tarjetas=[
                ('♩ = 160', 'El más alto',
                 'Es el tempo más rápido de todo tu cuaderno. En 3/4 eso son casi 55 compases por '
                 'minuto: la pieza entera dura poco más de un minuto.'),
                ('CINCO Y UNO', 'El cifrado',
                 'Em, C, Am, D, G y B impresos encima del pentagrama. El B es mayor en medio de una '
                 'pieza menor: es el que empuja de vuelta al Mi.'),
                ('55 COMPASES', 'En una página',
                 'La partitura más apretada del cuaderno. No es más difícil de tocar; es más '
                 'difícil de LEER, y eso se arregla con lápiz, no con dedos.'),
                ('LOS ACENTOS', 'Escritos',
                 'En la última parte hay acentos (>) sobre algunas notas, y un calderón. Están '
                 'escritos: no son adorno ni opción.'),
            ],
            pie='A 160 no hay tiempo de leer nota a nota: hay que leer por grupos. Por eso esta pieza '
                'viene después del cifrado de Rasputin y de Can\'t Help Falling: si reconoces el '
                'acorde de un vistazo, ya no lees seis notas, lees una palabra.',
        ),
        ritmos=[
            ('MANO DERECHA', 'la melodía, en negras · andamio',
             [n('E4'), n('G4'), n('G4')], OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'un acorde por compás · andamio',
             [ac(('E2', 'B2', 'E3'), 'h.')], AZUL, 'bass', None),
        ],
        especial=[
            'Un sostenido detrás de la clave: Fa sostenido.',
            'La pieza empieza y descansa en Mi: es Mi menor.',
            'Compás de 3/4 y "♩ = 160": el tempo más alto del cuaderno.',
            'El cifrado viene impreso: Em, C, Am, D, G y B.',
            'Hay repeticiones, casillas de primera y segunda vez y un calderón.',
            'En la última parte hay acentos (>) escritos sobre algunas notas.',
        ],
        reto='Leer 55 compases a ♩ = 160 sin perderte de renglón. La dificultad de esta pieza no '
             'está en las manos: está en el ojo, que a esa velocidad no tiene tiempo de volver a '
             'buscar dónde iba.',
        truco='Marca a lápiz en tu partitura dónde empieza cada frase de cuatro compases, con una '
              'rayita vertical. Son marcas de tráfico: cuando el ojo se pierda, no vuelve al '
              'principio, vuelve a la rayita más cercana. Es lo que hace cualquier profesional con '
              'una partitura apretada.',
        sabias='La canción es de 1959 y en la película se canta durante una tormenta. Diez años '
               'después John Coltrane la convirtió en un estándar de jazz de catorce minutos, y '
               'para mucha gente esa es la versión de verdad.',
        qr=dict(titulo='Escúchala',
                texto='Escucha primero la versión de la película y luego la de Coltrane. La misma '
                      'melodía, y no la reconocerías si no te lo dijeran.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo primero de esta semana no es tocar: es coger el lápiz y marcar las frases. A 160 '
              'la pieza se estudia leyendo por grupos, no nota a nota.',
        reglas=['MARCAR LAS FRASES A LÁPIZ', 'LEER POR ACORDES, NO POR NOTAS',
                'EL PRIMER GOLPE PESA, LOS OTROS DOS NO'],
        bloques=[
            dict(num=1, titulo='Los seis acordes del cifrado, de un vistazo', clef='bass',
                 pista='son los que trae impresos tu partitura · el objetivo es reconocerlos sin leer',
                 sistemas=[
                     dict(cap='a) Em, C y Am · los tres primeros, y los tres comparten notas: mira '
                              'cuáles antes de tocarlos',
                          events=[ac(('E2', 'B2', 'E3'), 'h.'), ac(('C2', 'G2', 'C3'), 'h.'),
                                  ac(('A2', 'E3', 'A3'), 'h.')],
                          acento=True,
                          bars=3, clef='bass', key_sig='Mi menor', time_sig=(3, 4)),
                     dict(cap='b) D, G y B · el B es mayor en medio de una pieza menor, y por eso '
                              'suena a que algo va a pasar',
                          events=[ac(('D2', 'A2', 'D3'), 'h.'), ac(('G2', 'D3', 'G3'), 'h.'),
                                  ac(('B2', 'D#3', 'F#3'), 'h.')],
                          calderon=True,
                          bars=3, clef='bass', key_sig='Mi menor', time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=2, titulo='El vals: el primero pesa y los otros dos no',
                 pista='andamio en Mi menor · a 160 el compás dura poco más de un segundo',
                 sistemas=[
                     dict(cap='a) tres negras por compás, y solo la primera con peso · si pesan las '
                              'tres, esto deja de ser un vals',
                          events=[n('E4'), n('G4'), n('G4'),
                                  n('A4'), n('B4'), n('B4'),
                                  n('E5'), n('D5'), n('B4'),
                                  n('G4', 'h.')],
                          bars=4, key_sig='Mi menor', time_sig=(3, 4)),
                     dict(cap='b) y con la frase bajando, que es como se cierra cada cuatro '
                              'compases · la última nota se aguanta el compás entero',
                          events=[n('B4'), n('A4'), n('G4'),
                                  n('F#4'), n('G4'), n('A4'),
                                  n('E4', 'h.')],
                          bars=3, key_sig='Mi menor', time_sig=(3, 4), show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='LAS RAYITAS DE LÁPIZ',
                 texto='Marca con una rayita el principio de cada frase de cuatro compases. Cuando '
                       'el ojo se pierda —y a 160 se va a perder— vuelves a la rayita más cercana '
                       'y no al principio de la línea.'),
            dict(num=3, titulo='Las dos manos, cuatro compases',
                 pista='andamio en Mi menor · empieza a 90, no a 160',
                 sistemas=[
                     dict(cap='a) el acorde en el uno y la melodía por encima · el acorde no se '
                              'repite en el dos ni en el tres',
                          events=[ac(('E2', 'E4')), n('G4'), n('G4'),
                                  ac(('C2', 'A4')), n('B4'), n('B4')],
                          bars=2, key_sig='Mi menor', time_sig=(3, 4)),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='My Favourite Things · para casa',
            intro='Veinte minutos, y el primer día empieza con lápiz y no con piano.',
            bloques=[
                reto('Tocar los 55 compases de un tirón sin perder el sitio en la página.',
                     'Marca a lápiz una rayita vertical al principio de cada frase de cuatro '
                     'compases. Cuando te pierdas, vuelves a la rayita más cercana en vez de al '
                     'principio: así no paras nunca del todo.'),
                plan((4, 'Los seis acordes del cifrado, reconociéndolos de un vistazo'),
                     (6, 'La melodía sola, por frases de cuatro compases'),
                     (5, 'La izquierda sola, un acorde por compás'),
                     (5, 'Las dos juntas, subiendo por escalones')),
                escalera((90, 'las dos manos, frase a frase'),
                         (115, 'cuatro frases seguidas'),
                         (140, 'la página entera, sin parar'),
                         (160, 'su velocidad'),
                         meta='♩ = 160, que es lo que pone tu partitura',
                         notas=['A 160 no da tiempo a leer nota a nota: si te pierdes, es que aún '
                                'no lees por acordes. Baja un escalón.']),
                cifrado(['Em', 'C', 'Am', 'D', 'G', 'B'],
                        ['Escribe las tres notas de cada uno, de grave a agudo.',
                         'Y rodea el único que es mayor teniendo una nota alterada: es el que '
                         'empuja de vuelta al principio.'],
                        pista='son los seis que trae impresos tu partitura'),
                colorear([n('E4'), n('G4'), n('B4', 'h.'), n('A4'),
                          n('F#4'), n('E4', 'h.'), n('D5'), n('B4')],
                         ['Las notas que caen en el primer golpe del compás, de rojo.',
                          'Las blancas con puntillo, de verde.',
                          'Y rodea el Fa sostenido de la armadura.'],
                         titulo='Colorea el vals',
                         pista='las rojas son las únicas que pesan'),
                para_clase('La página entera al escalón que hayas alcanzado, y con las rayitas de '
                           'lápiz puestas. Si hay una frase en la que siempre te pierdes, tráela '
                           'marcada con otro color.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
