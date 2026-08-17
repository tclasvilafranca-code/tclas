# -*- coding: utf-8 -*-
"""It's Beginning to Look a Lot Like Christmas (a cuatro manos) — pieza 14 de
   Josep. Formato ADULTO.

   Lo comprobado sobre el PDF de su carpeta de Drive (Piano Duet, arreglo de
   Rachel Chytelman, Musescore, 2 páginas, 33 compases):

     - Detrás de la clave no hay nada. Aparecen Fa sostenidos escritos delante
       de las notas, uno a uno.
     - COMPÁS DE 6/8. Es el único 6/8 de todo el cuaderno.
     - Es a cuatro manos. El Piano 1 lleva LOS DOS PENTAGRAMAS EN CLAVE DE SOL;
       el Piano 2 lleva dos claves de fa (y una de sol suelta en un compás).
     - Empieza con silencio de negra con puntillo y anacrusa.
     - El Piano 2 hace acordes con puntillo marcando los dos pulsos del compás.

   El 6/8 es la razón por la que esta pieza está aquí y no antes: es lo único
   del cuaderno que no se cuenta ni en dos ni en cuatro.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from jp_comun import (n, ac, sil, plan, a_cuatro_manos, escalera, diferencias,
                      nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Josep', carpeta='Josep', num=14, nivel='intermedio', slug='BeginningChristmas',
    formato='adulto',
    titulo_corto="It's Beginning to Look a Lot Like Christmas", time_sig=(6, 8), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'josep', 'source',
                           'its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD).pdf'),
    yt='https://www.youtube.com/results?search_query=its+beginning+to+look+a+lot+like+christmas+piano+duet',

    ficha=dict(
        titulo="It's Beginning to Look a Lot Like Christmas",
        autor='Meredith Willson · dúo de piano · arreglo de Rachel Chytelman',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '6/8'),
               ('Carácter', 'Sin tempo impreso'), ('Alteración', 'Fa sostenido'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Seis corcheas que se cuentan en dos',
        pie_ritmos='Andamio en Do mayor. Lo literal es el compás: 6/8, seis corcheas por compás '
                   'agrupadas de tres en tres, y dos pulsos por compás, no seis.',
        armonia=dict(
            titulo='El único 6/8 del cuaderno',
            tarjetas=[
                ('SEIS OCHOS', 'Se cuenta en dos',
                 'Seis corcheas por compás, pero agrupadas de tres en tres: el compás tiene DOS '
                 'pulsos, no seis. Si cuentas seis, la canción se arrastra.'),
                ('DE TRES EN TRES', 'Las barras lo dicen',
                 'Las corcheas van unidas de tres en tres, y esa agrupación es la que te dice dónde '
                 'está cada pulso. Míralas antes de leer las notas.'),
                ('EN CLAVE DE SOL', 'Las dos manos',
                 'Tu parte lleva los dos pentagramas en clave de sol, como la Petite Chanson. El '
                 'Piano 2 lleva las dos en clave de fa.'),
                ('LA ANACRUSA', 'Se entra antes',
                 'La pieza empieza con un silencio de negra con puntillo, o sea medio compás, y '
                 'después entras.'),
            ],
            pie='Un 6/8 no es un 3/4 con más notas: son dos pulsos largos, cada uno partido en '
                'tres. Es la diferencia entre "UN-dos-tres, DOS-dos-tres" y "UN, DOS, TRES", y una '
                'vez que el cuerpo lo pilla ya no se pierde.',
        ),
        ritmos=[
            ('MANO DERECHA', 'seis corcheas agrupadas de tres en tres · andamio',
             [n('C5', 'e'), n('D5', 'e'), n('E5', 'e'), n('F5', 'e'), n('E5', 'e'), n('D5', 'e')],
             OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'dos pulsos por compás, con puntillo · andamio',
             [n('C4', 'q.'), n('G4', 'q.')], AZUL, 'treble', None),
        ],
        especial=[
            'Compás de 6/8: el único del cuaderno.',
            'Seis corcheas por compás, agrupadas de tres en tres.',
            'Dos pulsos por compás, no seis.',
            'Detrás de la clave no hay nada, pero hay Fa sostenidos escritos delante de las notas.',
            'Los dos pentagramas del Piano 1 van en clave de sol.',
            'Empieza con silencio de negra con puntillo y anacrusa.',
        ],
        reto='Contar en dos y no en seis. Con seis corcheas delante, la cabeza quiere contarlas '
             'todas, y entonces la pieza deja de balancearse y se convierte en una lista de notas.',
        truco='Anda por la habitación mientras cuentas: un paso por cada grupo de tres, dos pasos '
              'por compás. El 6/8 es un compás de caminar, y el cuerpo lo entiende antes que la '
              'cabeza. Cuando puedas andar y contar a la vez, siéntate y toca.',
        sabias='La canción es de 1951 y la escribió Meredith Willson, el mismo de "The Music Man". '
               'La grabó Bing Crosby ese mismo año y desde entonces no ha dejado de sonar: es de '
               'las pocas canciones navideñas modernas que no habla de Papá Noel ni de la nieve, '
               'sino de los escaparates de las tiendas.',
        qr=dict(titulo='Escúchala',
                texto='Marca el pulso con el pie mientras la escuchas. Verás que el pie va a la '
                      'mitad de velocidad de lo que suena: eso son los dos pulsos del 6/8.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Todo lo de esta semana es el compás. Las notas son fáciles y el 6/8 no, así que '
              'primero se aprende a contar en dos y después se toca.',
        reglas=['DOS PULSOS POR COMPÁS, NO SEIS', 'LAS CORCHEAS VAN DE TRES EN TRES',
                'LAS DOS MANOS LEEN EN CLAVE DE SOL'],
        bloques=[
            dict(num=1, titulo='Contar en dos: los grupos de tres',
                 pista='andamio en Do mayor · di "UN-dos-tres, DOS-dos-tres" en voz alta',
                 sistemas=[
                     dict(cap='a) seis corcheas, y el acento cae solo en la primera de cada grupo · '
                              'las otras cinco no pesan',
                          events=[n('C5', 'e'), n('D5', 'e'), n('E5', 'e'),
                                  n('F5', 'e'), n('E5', 'e'), n('D5', 'e'),
                                  n('C5', 'e'), n('D5', 'e'), n('E5', 'e'),
                                  n('G5', 'e'), n('F5', 'e'), n('E5', 'e')],
                          bars=2, time_sig=(6, 8)),
                     dict(cap='b) y ahora con una nota larga por pulso · las dos figuras valen lo '
                              'mismo: tres corcheas o una negra con puntillo',
                          events=[n('C5', 'q.'), n('E5', 'q.'),
                                  n('G5', 'q.'), n('E5', 'q.')],
                          bars=2, time_sig=(6, 8), show_time=False),
                 ]),
            dict(num=2, titulo='La entrada: medio compás de silencio',
                 pista='c. 1 · el silencio de negra con puntillo es literal',
                 sistemas=[
                     dict(cap='a) espera un pulso entero y entra en el segundo · cuenta "UN-dos-tres" '
                              'sin tocar y entra en el "DOS"',
                          events=[sil('q.'), n('C5', 'e'), n('D5', 'e'), n('E5', 'e'),
                                  n('F5', 'q.'), n('E5', 'e'), n('D5', 'e'), n('C5', 'e')],
                          bars=2, time_sig=(6, 8)),
                     dict(cap='b) y entrando a falta de una sola corchea, que es la otra manera de '
                              'empezar una frase en 6/8 · esa corchea empuja hacia el pulso',
                          events=[sil('q.'), sil('q'), n('G4', 'e'),
                                  n('C5', 'q.'), n('E5', 'e'), n('D5', 'e'), n('C5', 'e')],
                          bars=2, time_sig=(6, 8), show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ NO SE CUENTA HASTA SEIS',
                 texto='En 6/8 el pulso es la negra con puntillo, no la corchea. Contar seis por '
                       'compás es como leer una palabra letra a letra: sale, pero no suena a nada. '
                       'Cuenta dos y deja que las tres corcheas de cada pulso caigan dentro solas, '
                       'igual que al andar no cuentas los músculos de la pierna.'),
            dict(num=3, titulo='Las dos manos, las dos en clave de sol',
                 pista='andamio · tu izquierda marca los dos pulsos y la derecha rellena',
                 sistemas=[
                     dict(cap='a) la izquierda con las notas largas y la derecha con las corcheas · '
                              'si la izquierda empieza a moverse con la derecha, para',
                          events=[ac(('C4', 'C5'), 'e'), n('D5', 'e'), n('E5', 'e'),
                                  ac(('G4', 'F5'), 'e'), n('E5', 'e'), n('D5', 'e'),
                                  ac(('C4', 'C5'), 'q.'), ac(('G4', 'E5'), 'q.')],
                          bars=2, time_sig=(6, 8)),
                     dict(cap='b) y con el Fa sostenido, que aparece escrito delante de la nota · '
                              'no está en la armadura, así que hay que verlo cada vez',
                          events=[ac(('D4', 'D5'), 'e'), n('E5', 'e'), n('F#5', 'e'),
                                  ac(('G4', 'G5'), 'q.'),
                                  ac(('C4', 'E5'), 'e'), n('D5', 'e'), n('C5', 'e'),
                                  ac(('G4', 'C5'), 'q.')],
                          bars=2, time_sig=(6, 8), show_time=False),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="It's Beginning to Look a Lot Like Christmas · para casa",
            intro='Veinte minutos, y los cinco primeros andando por la habitación.',
            bloques=[
                plan((5, 'Andar contando "UN-dos-tres, DOS-dos-tres"'),
                     (5, 'La derecha sola, con el acento solo en la primera de cada grupo'),
                     (5, 'La izquierda sola, marcando los dos pulsos'),
                     (5, 'Las dos juntas, muy lento')),
                a_cuatro_manos('El Piano 2 marca los dos pulsos del compás con acordes. Antes de '
                               'empezar, contad medio compás en voz alta los dos juntos: en 6/8, '
                               'si cada uno entiende el pulso a su manera, no hay quien lo junte.'),
                escalera((50, 'contar en dos, sin tocar'),
                         (60, 'la derecha sola, en grupos de tres'),
                         (72, 'las dos manos, la primera página'),
                         meta='la velocidad a la que puedas contar en dos sin pensarlo — esta '
                              'partitura no trae tempo impreso',
                         notas=['Si al subir empiezas a contar en seis, baja un escalón.']),
                diferencias([n('C5', 'e'), n('D5', 'e'), n('E5', 'e'),
                             n('F5', 'e'), n('E5', 'e'), n('D5', 'e')],
                            [n('C5', 'e'), n('D5', 'e'), n('E5', 'e'),
                             n('F5', 'e'), n('E5', 'e'), n('C5', 'e')],
                            1,
                            titulo='Busca la diferencia',
                            pista='son dos compases de 6/8 casi iguales · solo cambia una nota'),
                nombres(['C5', 'E5', 'G5', 'F#5', 'D5', 'F5', 'C5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='ojo con la cuarta: lleva sostenido escrito delante'),
                para_clase('La derecha sola contando en dos, y a qué escalón has llegado. Si al '
                           'juntar las manos se te va el compás siempre en el mismo sitio, tráelo '
                           'marcado: casi seguro es donde cambia la agrupación de las corcheas.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
