# -*- coding: utf-8 -*-
"""Titanic (My Heart Will Go On) — pieza 11 de Aida. Formato ADULTO exigente.

   Segunda pieza de la cuarta etapa, la de los compases que se cuentan de otra
   manera. Detras del 6/8 del villancico viene el compas mas corto del cuaderno
   —2/4, dos tiempos— y con el, la primera SEMICORCHEA impresa del album.

   Lo comprobado sobre el PDF de SU carpeta (arreglo de Ana Cristina Escobes,
   1 pagina, vectorial; el mismo archivo, byte a byte, que el de Luisa):

     - Detras de la clave no hay nada: Do mayor.
     - **2/4**.
     - Arriba pone **Adagio** y **mp**. NO trae numero de metronomo, asi que la
       casilla de la ficha se llama "Caracter" y no "Tempo".
     - Trae barras de repeticion y casillas de 1a y 2a vez.
     - La derecha abre con **corchea con puntillo + semicorchea**: es el
       largo-corto que le da el balanceo, y esta escrito DENTRO de un solo
       tiempo. La izquierda hace una blanca por compas, que en 2/4 es el
       compas entero.

   LAS ALTURAS de los cuatro primeros compases, medidas a 150 ppp sobre las
   cinco lineas de cada pentagrama:

       DERECHA    c. 1  Do5 (corchea con puntillo) · Do5 (SEMICORCHEA) ·
                        Do5 · Do5 (corcheas)
                  c. 2  Si4 · Do5 (corcheas) · silencio de corchea · Do5 (corchea)
                  c. 3  Si4 · Do5 (corcheas) · silencio de corchea · Re5 (corchea)
                  c. 4  Mi5 · Re5 (negras)

       IZQUIERDA  c. 1  Do3 · c. 2  Sol3 · c. 3  Fa3 · c. 4  Sol3, blancas.

   Cada compas cierra en 2: 0,75 + 0,25 + 0,5 + 0,5 en el primero y 0,5 x 4 en
   los dos siguientes.

   UNA COSA QUE SALIO DE MEDIR: el bajo del c. 3 es un **Fa3**, no un Sol3. Las
   tres blancas de los cc. 2, 3 y 4 se parecen mucho a simple vista, y las dos
   de fuera van en el ESPACIO (Sol3) mientras que la del medio va SOBRE LA
   LINEA (Fa3). Puestas una al lado de la otra a tamano grande no hay duda;
   sueltas, si.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, plan, objetivo, verdadero_falso,
                      inventa, unir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los cuatro primeros compases de la DERECHA, medidos. Cita literal.
D1 = [n('C5', 'e.'), n('C5', 's'), n('C5', 'e'), n('C5', 'e')]
D2 = corch(['B4', 'C5']) + [sil('e'), n('C5', 'e')]
D3 = corch(['B4', 'C5']) + [sil('e'), n('D5', 'e')]
D4 = [n('E5'), n('D5')]

# Y los cuatro de la IZQUIERDA: una blanca por compas, que en 2/4 es el compas
# entero. Tambien medidos.
IZQ = [n('C3', 'h'), n('G3', 'h'), n('F3', 'h'), n('G3', 'h')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=11, nivel='intermedio',
    slug='Titanic', formato='adulto',
    titulo_corto='Titanic', time_sig=(2, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source', 'Titanic.pdf'),
    yt='https://www.youtube.com/results?search_query=my+heart+will+go+on+piano',

    ficha=dict(
        titulo='Titanic',
        autor='James Horner · arr. Ana Cristina Escobés',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '2/4'),
               ('Carácter', 'Adagio · mp'), ('Izquierda', 'Una por compás'),
               ('Trae', '1ª y 2ª vez')],
        titulo_ritmos='Los compases 1 y 2, medidos',
        pie_ritmos='Arriba, los dos primeros compases de la derecha MEDIDOS en tu partitura: el '
                   'largo-corto del c. 1 es corchea con puntillo y semicorchea. Abajo, la '
                   'izquierda de esos mismos compases, una blanca cada uno.',
        armonia=dict(
            titulo='Lo nuevo de esta pieza',
            tarjetas=[
                ('EL 2/4', 'Dos tiempos',
                 'El compás más corto del cuaderno: dos negras y se acabó. Con tan poco sitio, la '
                 'línea divisoria pasa cada dos por tres y hay que saber dónde cae el uno.'),
                ('LA SEMICORCHEA', 'La primera',
                 'Corchea con puntillo y semicorchea: las dos juntas ocupan UN tiempo, no dos. La '
                 'segunda entra muy tarde, casi pegada a la siguiente.'),
                ('LA IZQUIERDA', 'Una y quieta',
                 'Una blanca por compás, que aquí es el compás entero. No tiene ritmo que aprender: '
                 'lo suyo es llegar a tiempo y aguantar hasta el final.'),
                ('1ª Y 2ª VEZ', 'Dos finales',
                 'La pieza se repite y la segunda vez sale por otra puerta. Antes de tocarla, sigue '
                 'con el dedo el camino entero sobre el papel.'),
            ],
            pie='Adagio quiere decir despacio, y aquí conviene de verdad: el largo-corto solo se '
                'oye si hay sitio entre las dos notas. A velocidad rápida las dos se juntan y la '
                'pieza pierde justo lo que la hace reconocible.',
        ),
        ritmos=[
            ('DERECHA', 'los cc. 1 y 2, MEDIDOS · el largo-corto va dentro de un tiempo',
             D1 + D2, OCRE, 'treble', None),
            ('IZQUIERDA', 'los mismos dos compases, medidos · una blanca cada uno',
             IZQ[:2], AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'El compás es 2/4: dos negras por compás.',
            'Arriba pone Adagio y mp, pero no hay número de metrónomo.',
            'El compás 1 lleva corchea con puntillo y semicorchea.',
            'Los compases 2 y 3 llevan un silencio de corchea en medio.',
            'La izquierda hace una blanca por compás, sin excepción.',
            'Hay barras de repetición y casillas de 1ª y 2ª vez.',
        ],
        reto='Que la semicorchea entre tarde de verdad. Casi todo el mundo la toca como si fuera '
             'una corchea normal, y entonces el largo-corto se convierte en dos notas iguales y la '
             'canción deja de reconocerse.',
        truco='Cuenta cada tiempo en cuatro: "UNO-y-dos-y". La nota larga ocupa las tres primeras '
              'partes y la corta entra en la cuarta, justo antes del golpe siguiente.',
        sabias='James Horner escribió el tema antes de que hubiera letra, y durante meses el '
               'director de la película no quiso ni oír hablar de una canción con voz. La grabaron '
               'a escondidas y se la enseñaron ya terminada: es la banda sonora más vendida de la '
               'historia.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate solo en la primera pareja de notas de cada frase: una larga y una '
                      'muy corta pegada al final. Ese desnivel es toda la pieza.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas y ninguna difícil por separado: un compás de dos tiempos y una '
              'figura corta dentro de uno de ellos. Empieza contando, sin tocar.',
        reglas=['DOS TIEMPOS POR COMPÁS', 'LA CORTA ENTRA AL FINAL DEL TIEMPO',
                'LA IZQUIERDA AGUANTA EL COMPÁS ENTERO'],
        bloques=[
            dict(num=1, titulo='El largo-corto del compás 1',
                 pista='c. 1 · MEDIDO en tu partitura · la pareja del principio ocupa UN tiempo',
                 sistemas=[
                     dict(cap='a) el compás 1 tal y como está escrito · corchea con puntillo, '
                              'semicorchea, y dos corcheas iguales detrás',
                          events=list(D1), matiz='mp', bars=1),
                     dict(cap='b) y el mismo compás con las cuatro notas iguales, solo para oír la '
                              'diferencia · esto NO es lo que pone tu partitura',
                          events=corch(['C5', 'C5']) + corch(['C5', 'C5']),
                          bars=1, show_time=False),
                     dict(cap='c) y el largo-corto repetido cuatro veces, cambiando de nota · lo '
                              'que se practica es el desnivel, no las alturas',
                          events=[n('C5', 'e.'), n('C5', 's'), n('D5', 'e.'), n('D5', 's'),
                                  n('E5', 'e.'), n('E5', 's'), n('D5', 'e.'), n('D5', 's')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA CORTA ENTRA TAN TARDE',
                 texto='Un tiempo de negra se parte en dos corcheas, o en cuatro semicorcheas. La '
                       'corchea con puntillo se lleva TRES de esas cuatro partes, y a la '
                       'semicorchea solo le queda la última. Por eso suena pegada a la nota '
                       'siguiente y no a la anterior: no está en medio del tiempo, está al final. '
                       'Si la tocas en medio te sale un par de corcheas normales, que es el error '
                       'clásico y no se oye como error, se oye como otra canción.'),
            dict(num=2, titulo='Los compases 2 y 3, con el silencio en medio',
                 pista='cc. 2-3 · MEDIDO · el silencio de corchea cae en el segundo tiempo',
                 sistemas=[
                     dict(cap='a) el compás 2 · dos corcheas, un silencio de corchea y una corchea',
                          events=list(D2), bars=1),
                     dict(cap='b) y el compás 3, que es igual pero acaba una nota más arriba',
                          events=list(D3), bars=1, show_time=False),
                     dict(cap='c) y los cc. 2, 3 y 4 seguidos · el 4 son ya dos negras, sin prisa',
                          events=D2 + D3 + D4, bars=3, show_time=False),
                 ]),
            dict(num=3, titulo='La izquierda: cuatro blancas y nada más',
                 pista='cc. 1-4 de la mano izquierda · MEDIDO · una blanca por compás',
                 sistemas=[
                     dict(cap='a) las cuatro, tal y como están · en 2/4 una blanca es el compás '
                              'entero, así que no hay dónde equivocarse de tiempo',
                          events=list(IZQ), bars=4, clef='bass'),
                     dict(cap='b) y las mismas partidas en dos negras, solo para contar los dos '
                              'tiempos en voz alta · en tu partitura son blancas',
                          events=[n('C3'), n('C3'), n('G3'), n('G3'),
                                  n('F3'), n('F3'), n('G3'), n('G3')],
                          bars=4, clef='bass', show_time=False),
                     dict(cap='c) y las dos manos en los cc. 3 y 4 · la derecha sube hasta el Mi '
                              'y la izquierda solo cambia de nota al empezar el compás',
                          events=[ac(('F3', 'B4'), 'e'), n('C5', 'e'), sil('e'), n('D5', 'e'),
                                  ac(('G3', 'E5')), n('D5')],
                          bars=2, manos='sostiene', show_time=False),
                 ]),
            dict(num=4, titulo='El largo-corto en otras alturas',
                 pista='andamio en Do mayor · aquí lo que se practica es la figura, no las notas',
                 sistemas=[
                     dict(cap='a) subiendo por los grados de Do mayor, una pareja por tiempo',
                          events=[n('C5', 'e.'), n('D5', 's'), n('E5', 'e.'), n('F5', 's'),
                                  n('G5', 'e.'), n('F5', 's'), n('E5', 'e.'), n('D5', 's')],
                          bars=2),
                     dict(cap='b) y con la corta repitiendo la larga, que es lo que hace tu '
                              'partitura · si las dos suenan iguales, la corta va llegando pronto',
                          events=[n('G4', 'e.'), n('G4', 's'), n('A4', 'e.'), n('A4', 's'),
                                  n('B4', 'e.'), n('B4', 's'), n('C5', 'e.'), n('C5', 's')],
                          bars=2, show_time=False),
                     dict(cap='c) y bajando, que es donde más cuesta: al bajar la mano tiende a '
                              'adelantar la corta',
                          events=[n('C5', 'e.'), n('B4', 's'), n('A4', 'e.'), n('G4', 's'),
                                  n('F4', 'e.'), n('E4', 's'), n('D4', 'e.'), n('C4', 's')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los cuatro primeros compases con las dos manos, despacio, y contando cada '
                       'tiempo en cuatro partes mientras tocas. Cuando salgan, mira el camino de la '
                       'pieza entera antes de seguir: hay barra de repetición y dos finales, y eso '
                       'se decide con el dedo sobre el papel, no tocando.'),
        ] + bloques_extra('Do mayor', 101, 'C5', 'C3',
                          'el 2/4: dos tiempos por compás, con una figura corta dentro de uno',
                          desde=5, time_sig=(2, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Titanic · para casa',
            intro='Quince minutos al día. Lo único nuevo es una figura, así que la mayor parte del '
                  'tiempo es contar en cuatro partes y tocar despacio.',
            bloques=[
                plan((4, 'Contar "UNO-y-dos-y" con el pie, sin tocar'),
                     (4, 'El c. 1 de la derecha, con el largo-corto'),
                     (3, 'La izquierda sola: cuatro blancas, contando los dos tiempos'),
                     (4, 'Los cc. 1 a 4 con las dos manos, muy despacio')),
                objetivo('Que en el compás 1 se oigan una nota larga y una corta, no dos iguales. '
                         'Si al tocarlas seguidas suenan del mismo tamaño, para y cuenta el tiempo '
                         'en cuatro partes antes de volver a intentarlo.'),
                verdadero_falso([
                    'En 2/4 caben dos negras por compás.',
                    'Una blanca ocupa el compás entero en 2/4.',
                    'La semicorchea del compás 1 entra en medio del tiempo.',
                    'Esta partitura trae escrito un número de metrónomo.',
                    'Las casillas de 1ª y 2ª vez dan dos finales distintos.'],
                    titulo='Verdadero o falso',
                    pista='dos son falsas'),
                inventa(['Solo Do, Re, Mi, Fa y Sol.',
                         'Dos compases de dos tiempos.',
                         'Que en cada compás haya una corchea con puntillo y una semicorchea.'],
                        time_sig=(2, 4),
                        titulo='Inventa dos compases con el largo-corto',
                        pista='y tócalos contando cada tiempo en cuatro partes'),
                unir([('2/4', 'dos negras por compás'),
                      ('Blanca', 'ocupa el compás entero en 2/4'),
                      ('Corchea con puntillo', 'se lleva tres cuartas partes del tiempo'),
                      ('Adagio', 'despacio, y aquí está escrito arriba')],
                     titulo='Une cada cosa con lo que significa',
                     pista='las cuatro salen de tu partitura de esta semana'),
                para_clase('Los cuatro primeros compases con las dos manos, a la velocidad que te '
                           'salgan bien. Y trae marcado con lápiz por dónde va la repetición: lo '
                           'miramos juntas antes de tocar la pieza entera.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
