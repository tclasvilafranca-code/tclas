# -*- coding: utf-8 -*-
"""It's Beginning to Look a Lot Like Christmas (dúo) — pieza 12 de Jaume. ADULTO exigente.

   Lo comprobado sobre el PDF de su carpeta de Drive (Piano Duet, arreglo de
   Rachel Chytelman, Musescore, 2 páginas, 33 compases), mirado a 110 dpi:

     - Detrás de la clave no hay nada: Do mayor, con sostenidos escritos delante
       de algunas notas (el primero, un Fa♯ en el c. 2).
     - **6/8**. No trae número de metrónomo.
     - Es a cuatro manos: el PIANO 1 lleva dos pentagramas en clave de sol, y los
       dos escriben la MISMA melodía a distancia de octava; el PIANO 2 lleva dos
       claves de fa (y una de sol en un compás de la segunda página).
     - MEDIDO (`medir_arranque`, pentagrama de arriba): el c. 1 es un silencio
       de negra con puntillo, **Mi5** de negra y **Fa5** de corchea.
     - El c. 2 de la melodía (pentagrama de abajo, una octava más grave):
       Sol · La · Sol (corcheas) · Fa♯ (negra) · Sol (corchea). Los cc. 3 y 4 son
       negras con puntillo: La · Do | Mi · Sol.
     - **El Piano 2 va con un silencio de negra con puntillo y un acorde de
       negra con puntillo** en cada compás (marca el segundo pulso, no el
       primero) y un bajo en blanca con puntillo debajo.
     - El c. 5 es un compás entero de silencio en el Piano 1.
     - Del c. 13 en adelante vuelve el dibujo del principio y acaba con un
       acorde largo y mantenido en el Piano 2.

   Mismo archivo que el de Josep, Aída, Dilan y Eva: lo literal coincide y lo
   inventado no. Aquí el trabajo va por **contar en dos** y por el **silencio
   que abre el compás** (la melodía no entra en el uno, y el otro piano
   tampoco).
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from jau_comun import (n, ac, sil, reto, plan, a_cuatro_manos, contar, unir,
                       verdadero_falso, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Jaume', carpeta='Jaume', num=12, nivel='intermedio', slug='ItsBeginningToLook',
    formato='adulto',
    titulo_corto="It's Beginning to Look a Lot Like Christmas", time_sig=(6, 8), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'jaume', 'source',
                           'Its-beginning-to-look-a-lot-li ke (4 manos NAVIDAD)'),
    yt='https://www.youtube.com/results?search_query=its+beginning+to+look+a+lot+like+christmas+piano+duet',

    ficha=dict(
        titulo="It's Beginning to Look a Lot Like Christmas",
        autor='Meredith Willson · dúo de piano · arreglo de Rachel Chytelman',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '6/8'),
               ('Carácter', 'Sin tempo impreso'), ('Alteración', 'Fa sostenido'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='La entrada, y el acorde del segundo pulso',
        pie_ritmos='Arriba, medido sobre tu partitura: silencio de negra con puntillo, Mi y Fa. '
                   'Abajo, andamio: el Piano 2 marca el segundo pulso con un acorde de negra con '
                   'puntillo.',
        armonia=dict(
            titulo='El 6/8 se cuenta en dos, y el otro piano se retrasa',
            tarjetas=[
                ('EL 6/8', 'Dos pulsos de tres',
                 'Seis corcheas por compás, agrupadas de tres en tres. Se cuenta uno-dos, no '
                 'uno-dos-tres-cuatro-cinco-seis: si cuentas seis, cada nota parece una pregunta.'),
                ('LA ENTRADA', 'Silencio y anacrusa',
                 'El c. 1 empieza con un silencio de negra con puntillo y entra con Mi y Fa en el '
                 'segundo pulso. La melodía no arranca en el uno, y el otro piano tampoco.'),
                ('EL PIANO 2', 'Acorde en el dos',
                 'En cada compás hace un silencio de negra con puntillo y, justo después, un acorde '
                 'de negra con puntillo. Marca el segundo pulso, no el primero: es un contratiempo.'),
                ('EL FA SOSTENIDO', 'Escrito delante',
                 'Ya aparece en el c. 2, y no está en la armadura: va delante de cada nota, y '
                 'vale solo hasta el final del compás.'),
            ],
            pie='Es un dúo, y la pieza se lee abierta en dos páginas: la 1 y la 2 de la partitura '
                'quedan enfrentadas en el álbum, para no tener que pasar hoja a mitad del dúo.',
        ),
        ritmos=[
            ('PIANO 1', 'c. 1 · medido',
             [sil('q.'), n('E5'), n('F5', 'e')], OCRE, 'treble', None),
            ('PIANO 2', 'un acorde en el segundo pulso · andamio',
             [sil('q.'), ac(('E3', 'G3', 'C4'), 'q.')], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay nada, pero aparecen sostenidos escritos delante de algunas notas.',
            'El compás es 6/8: seis corcheas por compás, contadas de tres en tres.',
            'El Piano 1 escribe la misma melodía en dos pentagramas, una octava aparte.',
            'El Piano 2 hace un silencio de negra con puntillo y un acorde de negra con puntillo en cada compás.',
            'El c. 5 es un compás entero de silencio en el Piano 1.',
            'Son dos páginas y 33 compases: se leen abiertas, con el otro piano al lado.',
        ],
        reto='Entrar en el segundo pulso sin que te lo marque nadie. El Piano 2 tampoco toca en el uno, '
             'así que el primer golpe del compás no suena en ningún piano: hay que contarlo sin '
             'oírlo.',
        truco='Cuenta "uno-dos" en voz alta, con el uno en la mano izquierda sobre la mesa y el '
              'dos con un golpe de la derecha. Cuando los dos pianos coincidan sin mirarse, la '
              'entrada sale sola.',
        sabias='La canción es de Meredith Willson, de 1951, y es casi el primer villancico que se '
               'escribió para sonar a anuncio de los grandes almacenes: habla de los '
               'escaparates, los guantes y las ramas de abeto, más que del Nacimiento.',
        qr=dict(titulo='Escúchala',
                texto='Escucha el acompañamiento: no marca el uno, marca el dos. Esa es la '
                      'sensación de balanceo que tu mano izquierda tiene que fabricar.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia primero la parte de cada piano por separado, y los dos pianos juntos solo '
              'cuando cada uno puede contar sin el otro. La clave de todo es contar en dos.',
        reglas=['CONTAR EN DOS', 'EL SILENCIO ABRE EL COMPÁS', 'LOS DOS PIANOS, DESPUÉS'],
        bloques=[
            dict(num=1, titulo='La melodía de los cuatro primeros compases',
                 pista='cc. 1-4 · leído del pentagrama de abajo del Piano 1 · una octava más '
                       'grave que el de arriba',
                 sistemas=[
                     dict(cap='a) la entrada con silencio, las corcheas con el Fa♯, y las dos negras '
                              'con puntillo del final · dos pulsos por compás en todo el trozo',
                          events=[sil('q.'), n('E4'), n('F4', 'e'),
                                  n('G4', 'e'), n('A4', 'e'), n('G4', 'e'), n('F#4'), n('G4', 'e'),
                                  n('A4', 'q.'), n('C5', 'q.'),
                                  n('E5', 'q.'), n('G4', 'q.')],
                          bars=4),
                 ]),
            dict(num=2, titulo='Seis corcheas en dos pulsos',
                 pista='c. 2 · leído de tu partitura · las cinco notas y la negra que se tocan '
                       'dentro del mismo compás',
                 sistemas=[
                     dict(cap='a) las tres primeras corcheas son un pulso y las dos siguientes el '
                              'segundo · el Fa♯ es la negra del segundo pulso',
                          events=[n('G4', 'e'), n('A4', 'e'), n('G4', 'e'), n('F#4'), n('G4', 'e')],
                          bars=1),
                     dict(cap='b) el mismo compás contando solo dos · di "uno" en la primera y '
                              '"dos" en la cuarta, y no digas nada en las demás · andamio',
                          events=[n('C5', 'e'), n('D5', 'e'), n('C5', 'e'), n('B4'), n('C5', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ SE CUENTA EN DOS',
                 texto='Seis corcheas se pueden contar de muchas maneras, y casi todas son malas: '
                       'contando seis, la pieza se arrastra; contando tres veces dos, parece un '
                       'vals. Contando dos golpes largos, uno-dos, el compás se balancea solo. Es '
                       'lo que hace la partitura al escribir negras con puntillo en los cc. 3 y 4.'),
            dict(num=3, titulo='Los cc. 3 y 4: negras con puntillo',
                 pista='cc. 3-4 · leído de tu partitura · cuatro negras con puntillo, una por golpe',
                 sistemas=[
                     dict(cap='a) La, Do, Mi y Sol, una por golpe · son los dos compases que mejor '
                              'enseñan el 6/8: cada nota es un pulso y la corchea ni aparece',
                          events=[n('A4', 'q.'), n('C5', 'q.'), n('E5', 'q.'), n('G4', 'q.')],
                          bars=2),
                 ]),
            dict(num=4, titulo='El Piano 2: el silencio y el acorde',
                 pista='andamio · el acorde del segundo pulso con el bajo en blanca con puntillo '
                       'debajo',
                 clef='bass',
                 sistemas=[
                     dict(cap='a) el silencio de negra con puntillo cuenta como un pulso entero · '
                              'si el acorde cae antes, estás contando como una pieza en 3/4',
                          events=[sil('q.'), ac(('E3', 'G3', 'C4'), 'q.'),
                                  sil('q.'), ac(('F3', 'A3', 'C4'), 'q.')],
                          bars=2, clef='bass'),
                 ]),
            dict(num=5, titulo='Un compás entero de silencio',
                 pista='c. 5 · el Piano 1 no toca · andamio con los silencios alrededor',
                 sistemas=[
                     dict(cap='a) el compás de silencio se cuenta, no se espera · dos pulsos '
                              'enteros antes de volver a entrar',
                          events=[n('A4', 'q.'), n('C5', 'q.'),
                                  sil('q.'), sil('q.'),
                                  sil('q.'), n('E4'), n('F4', 'e')],
                          bars=3),
                 ]),
            dict(num=6, titulo='El Fa♯ del c. 2, con y sin él',
                 pista='c. 2 · leído de tu partitura · el sostenido va escrito delante y se cancela '
                       'solo en la barra',
                 sistemas=[
                     dict(cap='a) el compás con el Sol tres veces y el Fa♯ en medio '
                              '· después de la barra, el Fa vuelve a ser natural',
                          events=[n('G4', 'e'), n('A4', 'e'), n('G4', 'e'), n('F#4'), n('G4', 'e'),
                                  n('A4', 'q.'), n('F4', 'q.')],
                          bars=2),
                 ]),
        ] + bloques_extra('Do mayor', 12, 'E4', 'C3',
                          'el 6/8 se cuenta en dos: la corchea es el pulso del compás',
                          desde=6, time_sig=(6, 8)),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="It's Beginning to Look… · para casa",
            intro='Veinte minutos, y la mitad con metrónomo para contar en dos.',
            bloques=[
                reto('Entrar en el segundo pulso, sin que ningún piano marque el primero.',
                     'Cuenta "uno-dos" en voz alta, golpeando el uno en la mesa. Si al entrar el '
                     'otro piano te adelanta, es que has contado tres en lugar de dos.'),
                plan((4, 'El c. 1 con el silencio, contando en dos, diez veces'),
                     (6, 'La melodía de los cc. 1-4, sola'),
                     (5, 'El silencio y el acorde del Piano 2, sin tu parte'),
                     (5, 'Los dos pianos juntos, solo el principio')),
                a_cuatro_manos('Acordad antes de tocar quién cuenta el compás de entrada, a qué '
                               'velocidad vais y quién espera en el c. 5, el compás de silencio. '
                               'Se decide en voz alta y se apunta a lápiz en el margen.'),
                contar([n('A4', 'q.'), n('C5', 'q.'), n('E5', 'q.'), n('G4', 'q.')],
                       ['¿Cuántas negras con puntillo hay?', '¿Cuántos pulsos hay en total?',
                        '¿Cuántos compases son?'],
                       titulo='Cuenta sobre los cc. 3 y 4',
                       pista='son dos compases de dos pulsos cada uno, de tu partitura'),
                unir([('6/8', 'seis corcheas contadas de dos en dos pulsos'),
                      ('Negra con puntillo', 'dura un pulso entero del compás'),
                      ('Silencio de negra con puntillo', 'se cuenta, no se toca'),
                      ('Sostenido delante de la nota', 'vale solo hasta el final del compás')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                verdadero_falso([
                    'El 6/8 se cuenta en seis golpes iguales.',
                    'En el c. 5 el Piano 1 no toca.',
                    'El Piano 2 marca el primer pulso de cada compás.',
                    'El Fa sostenido va escrito delante de la nota y no en la armadura.',
                    'La partitura trae un número de metrónomo.'],
                    titulo='Verdadero o falso',
                    pista='tres son falsas'),
                para_clase('Los cc. 1-5 con el otro piano, y quién cuenta la entrada. Si el '
                           'silencio del c. 5 se te acorta, tráelo: se arregla contando en voz '
                           'alta.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
