# -*- coding: utf-8 -*-
"""It's Beginning to Look a Lot Like Christmas (canción 15 de Eva, avanzado).
   A CUATRO MANOS. Misma edición que la de Dilan (sha256 idéntico); el
   material medido se importa de `dilan_20_beginning`. Ver TRANSCRIPCION_D18_20.md.

   Camino distinto al de Dilan:

     - A Dilan se le da primero la melodía en la octava de la derecha, después
       la de la izquierda, y al final se juntan.
     - A Eva se le juntan DESDE EL PRIMER MINUTO. En esta pieza el Primo toca
       la misma melodía con las dos manos a distancia de octava, y ahí la
       dificultad no es aprenderse la melodía —es una sola línea— sino que las
       dos manos caigan exactamente a la vez. Una octava doblada no perdona:
       si una mano llega dos milésimas antes, no suena a error, suena a ECO. Y
       un eco no se oye estudiando cada mano por separado, porque por separado
       las dos van perfectas.

   Do mayor, 6/8. El Primo es la parte del alumno; el Secondo lo toca la
   profesora.

   MEDIDO DE NUEVO EL 1 DE SEPTIEMBRE DE 2026 junto con el de Dilan, y las
   citas hubo que rehacerlas: lo que este dosier llamaba "cc. 1-4 medidos" y
   "cc. 6-7 medidos" no era lo impreso. La transcripcion completa del Piano 1,
   compas a compas, esta en la cabecera de `dilan_20_beginning.py`, que es de
   donde se importa el material.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_20_beginning import (n, ac, sil, corch, C1, C2, C34, C67, C910,
                                B1, B2, B67, BAJO_SECONDO)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

CANCION = dict(
    alumno='Eva', num=15, nivel='avanzado', slug='BeginningChristmas',
    titulo_corto="It's Beginning to Look a Lot Like Christmas",
    time_sig=(6, 8), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'eva', 'source', 'EVA',
                           'its-beginning-to-look-a-lot-like (4 manos).pdf'),
    yt='https://www.youtube.com/results?search_query=its+beginning+to+look+a+lot+like+christmas',

    ficha=dict(
        titulo="It's Beginning to Look a Lot Like Christmas",
        autor='Meredith Willson (1951) · arr. Rachel Chytelman · a cuatro manos',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '6/8'), ('Formato', 'Cuatro manos'),
               ('Tu parte', 'Primo'), ('Las dos manos', 'A la octava')],
        armonia=dict(
            titulo='Una sola línea, tocada con dos manos',
            tarjetas=[
                ('TU PARTE', 'Primo',
                 'La de arriba. Las dos manos tocan la MISMA melodía, separadas por una octava.'),
                ('EL PROBLEMA', 'El eco',
                 'Si una mano llega un pelo antes que la otra, no suena a fallo: suena a eco.'),
                ('EL 6/8', 'Dos golpes, no seis',
                 'Seis corcheas por compás agrupadas de tres en tres. El pie marca dos veces.'),
                ('EL SECONDO', 'Lo toca la profe',
                 'Su nota grave, medida en los cc. 2 a 7: Do · Fa · Do · Do · Do · Sol. Tú no lo '
                 'tocas, pero tienes que oírlo.'),
            ],
            pie='La melodía de esta pieza es fácil y se aprende en un rato. Lo que se estudia aquí es '
                'otra cosa: que dos manos toquen exactamente a la vez, y que dos personas empiecen a la '
                'vez. Ninguna de las dos cosas se puede practicar sola.',
        ),
        ritmos=[
            ('MD', 'el c. 1 MEDIDO · entras a la mitad, después del silencio',
             list(C1), AZUL, 'treble', None),
            ('MI', 'y exactamente lo mismo, una octava más abajo',
             list(B1), OCRE, 'treble', None),
        ],
        especial=[
            'No hay armadura: la pieza está en Do mayor.',
            'Compás de 6/8: se cuenta en DOS, no en seis.',
            'Es a cuatro manos: tú tocas el Primo y la profesora el Secondo.',
            'Tus dos manos tocan la misma melodía separadas por una octava.',
            'El Secondo lleva los dos pentagramas en clave de fa.',
            'Tu entrada llega después de un silencio de negra con puntillo.',
            'Los cc. 6 y 7 llevan notas largas ATADAS: ahí se oye cualquier desajuste.',
        ],
        reto='Que las dos manos caigan exactamente a la vez. Doblar una melodía a la octava es lo más '
             'fácil de leer y lo más difícil de que suene limpio: cualquier diferencia de milésimas se '
             'convierte en un eco que se oye desde la última fila.',
        truco='No estudies cada mano por separado, porque por separado las dos van perfectas y no vas a '
              'oír nada. Estúdialas juntas desde el primer minuto y muy lento, escuchando si suena UN '
              'sonido o dos. Y busca los cc. 6–7, donde la misma nota se repite: ahí el eco no se puede '
              'esconder.',
        sabias='Meredith Willson, que la escribió en 1951, es el mismo que hizo el musical “The Music '
               'Man”. La compuso antes de que existiera la costumbre de sacar villancicos nuevos cada '
               'año: entonces era raro que una canción de Navidad fuera de estreno.',
        qr=dict(titulo='Escucha la original',
                texto='Marca solo dos golpes por compás con el pie mientras la escuchas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · pasos 1 a 3 de 6',
        intro='Aquí las dos manos tocan lo mismo, separadas por una octava, y por eso se estudian juntas '
              'desde el primer minuto. Por separado las dos van perfectas y no oyes nada; juntas, '
              'cualquier diferencia de milésimas suena a eco. La melodía es lo de menos: lo que se '
              'entrena es que caigan a la vez.',
        reglas=['LAS DOS MANOS, JUNTAS DESDE EL MINUTO UNO', 'UN SONIDO, NO DOS', 'EL PIE MARCA DOS'],
        bloques=[
            dict(num=1, titulo='La melodía, en las dos octavas a la vez',
                 pista='cc. 1–4 MEDIDOS · lee arriba con la derecha y abajo con la izquierda, a la vez',
                 sistemas=[
                     dict(cap='a) cc. 1–4 · esto es lo que toca tu derecha · entras después del '
                              'silencio, y el cuarto sonido es un FA SOSTENIDO',
                          events=C1 + C2 + C34, bars=4),
                     dict(cap='b) y esto es tu izquierda en los cc. 1–2 · las mismas notas exactamente, '
                              'una octava más abajo: no hay nada nuevo que aprender',
                          events=B1 + B2, bars=2, show_time=False),
                     dict(cap='c) y la primera nota de cada compás DOBLADA a la octava, larga · '
                              'andamio: es la prueba del eco, y aquí no hay dónde esconderlo',
                          events=[ac(('E4', 'E5'), 'h.'), ac(('G4', 'G5'), 'h.'),
                                  ac(('A4', 'A5'), 'h.'), ac(('E5', 'E6'), 'h.')],
                          bars=4, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ AQUÍ NO SE ESTUDIA CADA MANO POR SU LADO',
                 texto='Porque el problema de esta pieza no está dentro de ninguna de las dos manos: '
                       'está ENTRE las dos. Por separado te va a salir perfecto a la primera, y eso no '
                       'demuestra nada. La prueba de verdad es tocarlas juntas muy lento y preguntarte '
                       'si oyes un sonido grueso o dos sonidos seguidos. Si oyes dos, no toques más '
                       'rápido: baja el tempo hasta que se fundan, y sube desde ahí.'),
            dict(num=2, titulo='Los cc. 6–7, donde el eco se delata',
                 pista='cc. 6–7 MEDIDOS · notas largas atadas y la misma nota tres veces: no hay '
                       'dónde esconderse',
                 sistemas=[
                     dict(cap='a) la derecha · el c. 6 es el mismo Mi tres veces, y las dos primeras '
                              'van ATADAS: suenan como una sola nota larga',
                          events=list(C67), bars=2),
                     dict(cap='b) y la izquierda, lo mismo una octava abajo · tócalas juntas y muy '
                              'lento: la nota larga es donde el desajuste se oye entero',
                          events=list(B67), bars=2, show_time=False),
                     dict(cap='c) y los cc. 9–10 de la derecha, MEDIDOS · la misma entrada un grado '
                              'más arriba, y otra tecla negra al final',
                          events=list(C910), bars=2, show_time=False),
                 ]),
            dict(num=3, titulo='El final de la primera página',
                 pista='cc. 8, 11, 13 y 14 MEDIDOS · dos notas largas, y la subida que cierra',
                 sistemas=[
                     dict(cap='a) los cc. 8 y 11 · dos compases enteros con UNA sola nota cada uno · '
                              'con las dos manos a la octava, es donde el eco dura más rato',
                          events=[n('A5', 'h.'), n('B5', 'h.')], bars=2),
                     dict(cap='b) y los cc. 13 y 14 · la blanca, el silencio, el LA SOSTENIDO, y la '
                              'subida Si-Do-Re-Mi que cierra la página',
                          events=[n('A5', 'h'), sil('e'), n('A#5', 'e'),
                                  n('B5'), n('C6', 'e'), n('D6'), n('E6', 'e')],
                          bars=2, show_time=False),
                     dict(cap='c) y esa misma subida doblada a la octava, larga · andamio: la última '
                              'prueba del eco antes de tocarla a tempo',
                          events=[ac(('B4', 'B5'), 'q.'), ac(('C5', 'C6'), 'q.'),
                                  ac(('D5', 'D6'), 'q.'), ac(('E5', 'E6'), 'q.')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LAS NOTAS LARGAS SON LAS MÁS DIFÍCILES AQUÍ',
                 texto='Parece al revés, pero es así: en las corcheas el desajuste dura un instante y '
                       'se disimula, y en una nota que dura el compás entero se queda sonando. Los '
                       'cc. 8 y 11 son cada uno una sola nota, y los cc. 6 y 7 llevan notas atadas: '
                       'esos cuatro compases son el examen de esta pieza. Si ahí suena UN sonido y no '
                       'dos, el resto ya está.'),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 4 a 6',
        intro='Con las dos manos fundidas queda lo que hace que esta pieza sea de dos personas: contar '
              'el 6/8 en dos golpes, que es como lo cuenta quien te acompaña, y saber qué está tocando '
              'la otra parte para poder entrar y salir con ella.',
        reglas=['EL 6/8 SE CUENTA EN DOS', 'ESCUCHA EL SECONDO', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=4, titulo='El 6/8, en dos golpes',
                 pista='la primera línea es andamio y el c. 12 va MEDIDO · aprieta un poco la '
                       'primera de cada tres corcheas y no las demás',
                 sistemas=[
                     dict(cap='a) el pie marca solo dos veces por compás · si marcas seis, ya lo estás '
                              'contando mal',
                          events=corch(['C5', 'D5', 'E5']) + corch(['F5', 'E5', 'D5']) +
                                 corch(['E5', 'F5', 'G5']) + corch(['A5', 'G5', 'F5']) +
                                 corch(['G5', 'F5', 'E5']) + corch(['D5', 'E5', 'D5']) +
                                 [n('C5', 'h.')],
                          bars=4),
                     dict(cap='b) y el c. 12, MEDIDO · acaba en SOL SOSTENIDO, que es la nota que '
                              'empuja hacia el La del compás siguiente',
                          events=corch(['B5', 'C6', 'B5']) + [n('G5'), n('G#5', 'e')],
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL 6/8 NO SE CUENTA EN SEIS',
                 texto='Se cuenta en DOS: seis corcheas agrupadas de tres en tres, y el pie marca solo '
                       'la primera de cada grupo. Si cuentas seis, cada corchea pesa lo mismo y la pieza '
                       'suena a marcha en vez de a balanceo. Y si tú cuentas en seis y quien te acompaña '
                       'cuenta en dos, no vais a coincidir aunque las dos toquéis bien las notas.'),
            dict(num=5, titulo='Lo que toca la otra parte', clef='bass',
                 pista='Secondo MEDIDO · cc. 2–7 · esto NO lo tocas tú, pero es lo que oyes debajo',
                 sistemas=[
                     dict(cap='a) su nota grave, cc. 2–7 · una por compás y sostenida entera: Do · Fa '
                              '· Do · Do · Do · Sol. El cambio de nota te dice si vais juntas',
                          events=list(BAJO_SECONDO), bars=6, clef='bass'),
                 ]),
            dict(tipo='nota',
                 etiqueta='CÓMO SE ENSAYA UNA PIEZA A DÚO',
                 texto='Tres reglas y ninguna es de dedos. Primera: la entrada se cuenta en voz alta, un '
                       'compás entero antes, y la cuenta la misma persona siempre. Segunda: si una de '
                       'las dos se pierde, NO se para — se sigue tocando y se vuelve a entrar en el '
                       'compás siguiente, porque en un dúo parar es peor que fallar. Y tercera: se '
                       'ensaya mirando de vez en cuando a la otra, no a las manos propias. Eso hay que '
                       'practicarlo, no sale solo.'),
            dict(tipo='nota',
                 etiqueta='LA OCTAVA ES UN INSTRUMENTO, NO DOS',
                 texto='Cuando dos manos tocan la misma nota a distancia de octava y caen exactamente a '
                       'la vez, el oído no oye dos notas: oye una sola, más gorda y más brillante. Ese '
                       'es el efecto que busca el arreglo, y es la razón de que el Primo esté escrito '
                       'así. Cuando lo consigas lo vas a notar de golpe, porque el sonido cambia de '
                       'color. Hasta que no pase eso, la pieza no está.'),
            dict(tipo='escalera', valores=[50, 58, 66, 74, 82, 90],
                 regla='PASO 6 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
