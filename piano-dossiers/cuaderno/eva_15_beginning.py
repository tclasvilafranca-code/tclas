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
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from dilan_20_beginning import n, ac, corch, DO, FA, SOL, LAm

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
                 'Do · Fa · Do · Fa · Sol · La m. Tú no lo tocas, pero tienes que oírlo.'),
            ],
            pie='La melodía de esta pieza es fácil y se aprende en un rato. Lo que se estudia aquí es '
                'otra cosa: que dos manos toquen exactamente a la vez, y que dos personas empiecen a la '
                'vez. Ninguna de las dos cosas se puede practicar sola.',
        ),
        ritmos=[
            ('MD', 'seis corcheas agrupadas de tres en tres: el pie marca dos',
             corch(['E5', 'F5', 'G5']) + corch(['A5', 'G5', 'F5']), AZUL, 'treble', None),
            ('MI', 'y exactamente lo mismo, una octava más abajo',
             corch(['E4', 'F4', 'G4']) + corch(['A4', 'G4', 'F4']), OCRE, 'treble', None),
        ],
        especial=[
            'No hay armadura: la pieza está en Do mayor.',
            'Compás de 6/8: se cuenta en DOS, no en seis.',
            'Es a cuatro manos: tú tocas el Primo y la profesora el Secondo.',
            'Tus dos manos tocan la misma melodía separadas por una octava.',
            'El Secondo lleva los dos pentagramas en clave de fa.',
            'Los cc. 6–7 repiten la misma nota: ahí se oye cualquier desajuste.',
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
        esquina='Al piano · pasos 1 y 2 de 4',
        intro='Aquí las dos manos tocan lo mismo, separadas por una octava, y por eso se estudian juntas '
              'desde el primer minuto. Por separado las dos van perfectas y no oyes nada; juntas, '
              'cualquier diferencia de milésimas suena a eco. La melodía es lo de menos: lo que se '
              'entrena es que caigan a la vez.',
        reglas=['LAS DOS MANOS, JUNTAS DESDE EL MINUTO UNO', 'UN SONIDO, NO DOS', 'EL PIE MARCA DOS'],
        bloques=[
            dict(num=1, titulo='La melodía, en las dos octavas a la vez',
                 pista='cc. 1–4 medidos · lee arriba con la derecha y abajo con la izquierda, a la vez',
                 sistemas=[
                     dict(cap='a) cc. 1–4 · esto es lo que toca tu derecha · Mi · Fa · Sol · La · Sol · '
                              'Fa · Sol · La · Do · Do · Sol',
                          events=corch(['E5', 'F5', 'G5']) + corch(['A5', 'G5', 'F5']) +
                                 [n('G5', 'h.')] +
                                 corch(['A5', 'C6', 'C6']) + corch(['C6', 'B5', 'A5']) +
                                 [n('G5', 'h.')],
                          bars=4),
                     dict(cap='b) y esto es tu izquierda en los cc. 1–2 · las mismas notas exactamente, '
                              'una octava más abajo: no hay nada nuevo que aprender',
                          events=corch(['E4', 'F4', 'G4']) + corch(['A4', 'G4', 'F4']) +
                                 [n('G4', 'h.')],
                          bars=2, show_time=False),
                     dict(cap='c) y las mismas notas en figuras largas, una por golpe · toca las dos '
                              'manos aquí y escucha si suena UN sonido o dos',
                          events=[n('E4', 'q.'), n('A4', 'q.'), n('G4', 'q.'), n('C5', 'q.'),
                                  n('B4', 'q.'), n('G4', 'q.'), n('A4', 'h.')],
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
                 pista='cc. 6–7 medidos · la misma nota repetida seis veces: no hay dónde esconderse',
                 sistemas=[
                     dict(cap='a) la derecha · el Do repetido, donde la frase se planta',
                          events=corch(['C6', 'C6', 'C6']) + corch(['C6', 'C6', 'C6']) +
                                 corch(['A5', 'B5', 'C6']) + corch(['B5', 'A5', 'G5']) +
                                 [n('C6', 'h.')],
                          bars=3),
                     dict(cap='b) y la izquierda, lo mismo una octava abajo · tócalas juntas y muy '
                              'lento: cada nota repetida es una oportunidad de oír el desajuste',
                          events=corch(['C5', 'C5', 'C5']) + corch(['C5', 'C5', 'C5']) +
                                 corch(['A4', 'B4', 'C5']) + corch(['B4', 'A4', 'G4']) +
                                 [n('C5', 'h.')],
                          bars=3, show_time=False),
                     dict(cap='c) y esos mismos compases en figuras largas, una por golpe · con las dos '
                              'manos: si aquí ya oyes eco, no sigas subiendo el tempo',
                          events=[n('C5', 'q.'), n('C5', 'q.'), n('A4', 'q.'), n('G4', 'q.'),
                                  n('C5', 'h.')],
                          bars=3, show_time=False),
                 ]),
        ],
    ),

    piano2=dict(
        titulo='Cómo se estudia (sigue)',
        esquina='Al piano · pasos 3 y 4',
        intro='Con las dos manos fundidas queda lo que hace que esta pieza sea de dos personas: contar '
              'el 6/8 en dos golpes, que es como lo cuenta quien te acompaña, y saber qué está tocando '
              'la otra parte para poder entrar y salir con ella.',
        reglas=['EL 6/8 SE CUENTA EN DOS', 'ESCUCHA EL SECONDO', 'DESPACIO Y SIN PARAR'],
        bloques=[
            dict(num=3, titulo='El 6/8, en dos golpes',
                 pista='andamio · aprieta un poco la primera de cada tres corcheas y no las demás',
                 sistemas=[
                     dict(cap='a) el pie marca solo dos veces por compás · si marcas seis, ya lo estás '
                              'contando mal',
                          events=corch(['C5', 'D5', 'E5']) + corch(['F5', 'E5', 'D5']) +
                                 corch(['E5', 'F5', 'G5']) + corch(['A5', 'G5', 'F5']) +
                                 corch(['G5', 'F5', 'E5']) + corch(['D5', 'E5', 'D5']) +
                                 [n('C5', 'h.')],
                          bars=4),
                     dict(cap='b) y el c. 12, que cierra la primera parte · tiene que sonar a punto y '
                              'aparte, no a “sigo”',
                          events=corch(['B5', 'C6', 'B5']) + corch(['G5', 'G5', 'G5']) +
                                 [n('A5', 'h.')],
                          bars=3, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='EL 6/8 NO SE CUENTA EN SEIS',
                 texto='Se cuenta en DOS: seis corcheas agrupadas de tres en tres, y el pie marca solo '
                       'la primera de cada grupo. Si cuentas seis, cada corchea pesa lo mismo y la pieza '
                       'suena a marcha en vez de a balanceo. Y si tú cuentas en seis y quien te acompaña '
                       'cuenta en dos, no vais a coincidir aunque las dos toquéis bien las notas.'),
            dict(num=4, titulo='Lo que toca la otra parte', clef='bass',
                 pista='Secondo medido · Do · Fa · Do · Fa · Sol · La m · esto NO lo tocas tú',
                 sistemas=[
                     dict(cap='a) escúchalo y apréndetelo de oído: el cambio de acorde es lo que te '
                              'dice si vais juntas o si una se ha adelantado',
                          events=[ac(DO, 'h.'), ac(FA, 'h.'), ac(DO, 'h.'), ac(FA, 'h.'),
                                  ac(SOL, 'h.'), ac(LAm, 'h.')],
                          bars=6, clef='bass'),
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
                 regla='PASO 4 · SOLO SUBES DE ESCALÓN CUANDO TE SALGA DOS VECES SEGUIDAS SIN PARAR.'),
        ],
    ),
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
