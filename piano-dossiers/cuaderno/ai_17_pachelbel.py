# -*- coding: utf-8 -*-
"""Canon in D, de Johann Pachelbel — pieza 17 de Aida. Formato ADULTO
   exigente.

   Segunda de la ultima etapa y primera de las tres que van seguidas en mayo y
   junio: Pachelbel, el Preludio de Bach y A comme amour. Las tres trabajan lo
   mismo —la mano abierta en arpegio— y en ese orden cada una prepara la
   siguiente.

   Esta es la unica del cuaderno construida sobre un BAJO OBSTINADO: las ocho
   notas de los cuatro primeros compases, que son el suelo famoso de la pieza.

   Lo comprobado sobre el PDF de SU carpeta (arreglo de Jim Paterson para
   mfiles.co.uk, 2 paginas, vectorial). Es solo suya.

     - Detras de la clave hay **DOS SOSTENIDOS** (Fa y Do): Re mayor.
     - **4/4**.
     - NO trae tempo impreso ni caracter escrito.
     - Lleva SEMICORCHEAS, medidas: 82 pares de barras dobles en el PDF.

   LAS ALTURAS, medidas a 300 ppp sobre las cinco lineas de cada pentagrama
   (las divisorias se localizaron por columnas de tinta que cruzan el sistema
   entero, y cada cabeza se leyo por su centro contra las lineas):

       IZQUIERDA (el bajo obstinado, cc. 1 a 4, todo blancas)
                 Re3 · La2 · Si2 · Fa#2 · Sol2 · Re2 · Sol2 · La2

       DERECHA   c. 1  Re4+Fa#4 · Do#4+Mi4   (dos notas a la vez, blancas)
                 c. 2  Si3+Re4 · La3+Do#4

   Cada uno de esos compases cierra en 4: dos blancas.

   LO QUE PASA DESPUES, tambien medido, porque la primera version de esta hoja
   afirmaba que las ocho notas "se repiten enteras, sin cambiar una sola vez,
   de principio a fin" y eso NO es lo que hay en el papel:

       c.  5  IZQUIERDA en NEGRAS   Re3 · Fa#3 · La3 · Sol3
       c.  6  IZQUIERDA en NEGRAS   Fa#3 · Re3 · Fa#3 · Mi3

   Es decir: a partir del c. 5 la izquierda deja las blancas, va en negras y
   rellena por el medio; mas adelante llega a corcheas. El suelo de la pieza
   sigue siendo el mismo, pero **no vuelve a estar escrito igual**, y decirle a
   la alumna que no hay nada mas que aprender seria mentirle.

   Y LA SEMICORCHEA, que es lo que este dosier no dibujaba: entra en el
   **c. 21** —el ultimo de la primera pagina— y a partir de ahi llena la
   segunda entera. El c. 21, medido nota a nota:

       DERECHA    t.1  La5 (corchea) · Fa#5 · Sol5      (dos semicorcheas)
                  t.2  La5 (corchea) · Fa#5 · Sol5      (dos semicorcheas)
                  t.3  La5 · La4 · Si4 · Do#5           (cuatro semicorcheas)
                  t.4  Re5 · Mi5 · Fa#5 · Sol5          (cuatro semicorcheas)
       IZQUIERDA  Fa#3 (negra) · Re3 (negra) · La2 (blanca)

   Los dos primeros tiempos llevan una sola barra larga y un TROCITO de segunda
   barra sobre las dos ultimas notas: es el reparto corchea + dos semicorcheas,
   y el motor lo dibuja asi solo (`notation.draw_system` pone la segunda barra
   entera si todo el grupo son semicorcheas y un muñon si no lo son todas).
   Suma 4 tiempos: 1 + 1 + 1 + 1.

   EL FA Y EL DO VAN SIEMPRE A LA NEGRA. Con dos sostenidos en la armadura no
   hay ni un Fa ni un Do natural en toda la pagina, y el bajo obstinado lleva
   uno de cada: el Fa#2 de la cuarta nota y el Do#4 que la derecha toca encima.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, reto, plan, escalera, contar, rodear,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El BAJO OBSTINADO, medido: las ocho notas sobre las que esta hecha la pieza.
# Cita literal (cc. 1 a 4, en blancas).
BAJO = [n('D3', 'h'), n('A2', 'h'), n('B2', 'h'), n('F#2', 'h'),
        n('G2', 'h'), n('D2', 'h'), n('G2', 'h'), n('A2', 'h')]

# Y la derecha de los cc. 1 y 2, medida: dos notas a la vez, blancas.
DER = [ac(('D4', 'F#4'), 'h'), ac(('C#4', 'E4'), 'h'),
       ac(('B3', 'D4'), 'h'), ac(('A3', 'C#4'), 'h')]

# Los cc. 5 y 6 de la izquierda, medidos: cuatro negras por compas. Es la
# prueba de que el bajo NO se repite escrito igual.
BAJO_NEGRAS = [n('D3'), n('F#3'), n('A3'), n('G3'),
               n('F#3'), n('D3'), n('F#3'), n('E3')]

# EL COMPAS 21 de la derecha, medido nota a nota. Es donde entra la
# semicorchea: el ultimo compas de la primera pagina, y a partir de ahi ya no
# para. Suma 4 tiempos, un golpe cada grupo.
#
# Las barras las pone solo `hoja_piano._autobeam`, que agrupa POR GOLPE: los
# dos primeros llevan corchea + dos semicorcheas, y `notation.draw_system`
# dibuja ahi una barra larga sobre las tres notas y un trocito de segunda sobre
# las dos cortas, que es como esta grabado en su edicion.
C21 = [n('A5', 'e'), n('F#5', 's'), n('G5', 's'),
       n('A5', 'e'), n('F#5', 's'), n('G5', 's'),
       n('A5', 's'), n('A4', 's'), n('B4', 's'), n('C#5', 's'),
       n('D5', 's'), n('E5', 's'), n('F#5', 's'), n('G5', 's')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=17, nivel='intermedio',
    slug='CanonPachelbel', formato='adulto',
    titulo_corto='Canon de Pachelbel', time_sig=(4, 4), key_sig='Re mayor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Canon de Pachelbel.pdf'),
    yt='https://www.youtube.com/results?search_query=pachelbel+canon+in+d+piano',

    ficha=dict(
        titulo='Canon de Pachelbel',
        autor='Johann Pachelbel · Canon in D · arr. Jim Paterson',
        datos=[('Tonalidad', 'Re mayor'), ('Compás', '4/4'),
               ('Armadura', 'Dos sostenidos'), ('El bajo', 'Ocho notas'),
               ('Semicorcheas', 'Desde el c. 21')],
        titulo_ritmos='El bajo que sostiene la pieza',
        pie_ritmos='Arriba, la derecha del c. 1 MEDIDA en tu partitura: dos notas a la vez, '
                   'una blanca cada media parte del compás. Abajo, las ocho notas del bajo de los '
                   'cc. 1 a 4, también medidas: son el suelo sobre el que está hecha la pieza.',
        armonia=dict(
            titulo='Ocho notas y toda una pieza',
            tarjetas=[
                ('EL BAJO OBSTINADO', 'Ocho notas',
                 'Re · La · Si · Fa♯ · Sol · Re · Sol · La, en blancas, en los cuatro primeros '
                 'compases. Ese es el suelo de la pieza y lo que hay que saber de memoria.'),
                ('LO QUE SÍ CAMBIA', 'A partir del c. 5',
                 'Medido: en el c. 5 la izquierda ya no va en blancas sino en negras (Re · Fa♯ · '
                 'La · Sol) y rellena por el medio; más adelante llega a corcheas. Mismo suelo, '
                 'escrito cada vez con más notas.'),
                ('DOS SOSTENIDOS', 'Fa y Do',
                 'Re mayor. No hay ni un Fa ni un Do natural en toda la página: la cuarta nota del '
                 'bajo es un Fa♯ y la derecha toca un Do♯ encima.'),
                ('LA DERECHA', 'Dos a la vez',
                 'Empieza con dos notas simultáneas por golpe, en blancas. Es la manera más suave '
                 'de abrir la mano: se coloca una vez y se aguanta.'),
            ],
            pie='Este bajo lleva trescientos años usándose: es la misma vuelta de acordes que hay '
                'debajo de decenas de canciones modernas. Cuando lo tengas en los dedos, te vas a '
                'encontrar tocándolo sin querer debajo de otras cosas.',
        ),
        ritmos=[
            ('DERECHA', 'el c. 1, MEDIDO · dos notas a la vez',
             DER[:2], OCRE, 'treble', 'Re mayor'),
            ('EL BAJO', 'las ocho notas de los cc. 1 a 4, medidas',
             list(BAJO), AZUL, 'bass', 'Re mayor'),
        ],
        especial=[
            'Detrás de la clave hay dos sostenidos: Fa y Do van en tecla negra.',
            'El compás es 4/4 y los primeros compases son todo blancas.',
            'La partitura no trae ni tempo ni carácter escritos.',
            'Las ocho notas del bajo están en los cuatro primeros compases.',
            'La cuarta nota del bajo es un Fa sostenido.',
            'En el compás 5 el bajo deja las blancas y pasa a negras.',
            'La derecha empieza tocando dos notas a la vez.',
            'La derecha entra en semicorcheas en el compás 21.',
        ],
        reto='Aprenderse las ocho notas del bajo DE MEMORIA, en orden, antes de tocar la pieza. '
             'Suena a poco y es todo: mientras la izquierda tenga que leer, la derecha no puede '
             'ocuparse de nada más.',
        truco='Dilas en voz alta cuatro veces seguidas sin mirar el papel: "Re, La, Si, Fa '
              'sostenido, Sol, Re, Sol, La". Cuando salgan de carrerilla, tócalas; hasta entonces, '
              'no.',
        sabias='Pachelbel escribió el canon hacia 1690 y estuvo doscientos años olvidado. Lo '
               'recuperó una grabación de 1968 y desde entonces no ha parado: es la misma vuelta '
               'de acordes de docenas de canciones pop, y hay quien la reconoce sin haber oído '
               'nunca el original.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo la mano izquierda y cuenta cuántas veces da la vuelta entera '
                      'antes de que la grabación termine. Son más de las que parecen.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Esta semana se empieza por la izquierda. Ocho notas de memoria, y con ese suelo '
              'puesto la derecha se lee mucho mejor.',
        reglas=['LAS OCHO NOTAS, DE MEMORIA', 'FA Y DO, SIEMPRE A LA NEGRA',
                'LA DERECHA SE COLOCA Y AGUANTA'],
        bloques=[
            dict(num=1, titulo='Las ocho notas del bajo',
                 pista='cc. 1 a 6 de la mano izquierda · MEDIDO · dos blancas por compás hasta el '
                       'c. 4, y negras a partir del 5',
                 sistemas=[
                     dict(cap='a) las cuatro primeras (cc. 1 y 2) · dilas en voz alta mientras las '
                              'tocas, y no mires las teclas',
                          events=BAJO[:4], bars=2, clef='bass', key_sig='Re mayor'),
                     dict(cap='b) y las cuatro que cierran la vuelta (cc. 3 y 4) · la sexta baja una '
                              'octava, que es lo que hace que la vuelta suene a que empieza otra vez',
                          events=BAJO[4:], bars=2, clef='bass', show_time=False,
                          key_sig='Re mayor'),
                     dict(cap='c) y así sigue: los cc. 5 y 6, MEDIDOS · el bajo deja las blancas, '
                              'pasa a negras y rellena por el medio',
                          events=list(BAJO_NEGRAS),
                          bars=2, clef='bass', show_time=False, key_sig='Re mayor'),
                     dict(cap='d) y los cc. 7 y 8, MEDIDOS · el final de esa vuelta, también en '
                              'negras: Re-Si-Re-La y Sol-Si-Do♯-La',
                          events=[n('D3'), n('B2'), n('D3'), n('A2'),
                                  n('G2'), n('B2'), n('C#3'), n('A2')],
                          bars=2, clef='bass', show_time=False, key_sig='Re mayor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UN BAJO OBSTINADO',
                 texto='Es una línea de bajo que vuelve una y otra vez, siempre por el mismo sitio, '
                       'mientras por encima cambia todo lo demás. "Obstinado" no es una manera de '
                       'hablar: en italiano se llama ostinato y quiere decir justo eso, que se '
                       'empeña. Ojo a una cosa que se ve en los ejercicios c) y d): en tu edición '
                       'el bajo no está copiado igual cada vez. Vuelve por el mismo camino, pero '
                       'escrito con más notas y más cortas. Por eso lo que hay que aprenderse de '
                       'memoria son las OCHO, el esqueleto: lo demás es relleno entre ellas, y '
                       'cuando sabes por dónde va se lee solo.'),
            dict(num=2, titulo='La derecha, dos notas a la vez',
                 pista='cc. 1-2 de la derecha · MEDIDO · una pareja de notas por cada media parte '
                       'del compás',
                 sistemas=[
                     dict(cap='a) los dos primeros compases con cada pareja partida en dos negras, '
                              'para colocar la mano · en tu partitura son blancas',
                          events=[ac(('D4', 'F#4')), ac(('D4', 'F#4')),
                                  ac(('C#4', 'E4')), ac(('C#4', 'E4')),
                                  ac(('B3', 'D4')), ac(('B3', 'D4')),
                                  ac(('A3', 'C#4')), ac(('A3', 'C#4'))],
                          bars=2, key_sig='Re mayor'),
                     dict(cap='b) y solo la nota de arriba de cada pareja, para oír por dónde va la '
                              'melodía · en tu partitura son dos notas a la vez',
                          events=[n('F#4', 'h'), n('E4', 'h'), n('D4', 'h'), n('C#4', 'h')],
                          bars=2, show_time=False, key_sig='Re mayor'),
                     dict(cap='c) y solo la de abajo, que baja igual pero un poco más lenta de oído',
                          events=[n('D4', 'h'), n('C#4', 'h'), n('B3', 'h'), n('A3', 'h')],
                          bars=2, show_time=False, key_sig='Re mayor'),
                     dict(cap='d) y a dónde va todo esto: el c. 21 de la derecha, MEDIDO · aquí '
                              'entra la semicorchea y ya no se va',
                          events=C21, bars=1, show_time=False, key_sig='Re mayor'),
                 ]),
            dict(num=3, titulo='Las dos manos, con el bajo debajo',
                 pista='cc. 1-2 y c. 21 con las dos manos · MEDIDO · cada pareja de la derecha cae '
                       'con una nota del bajo',
                 sistemas=[
                     dict(cap='a) los cc. 1 y 2 · el bajo entra a la vez que la derecha, y las dos '
                              'manos cambian juntas a mitad de compás',
                          events=[ac(('D3', 'D4', 'F#4'), 'h'), ac(('A2', 'C#4', 'E4'), 'h'),
                                  ac(('B2', 'B3', 'D4'), 'h'), ac(('F#2', 'A3', 'C#4'), 'h')],
                          bars=2, manos='dobla', key_sig='Re mayor'),
                     dict(cap='b) y los cc. 3 y 4, que cierran la vuelta del bajo · andamio sobre '
                              'esas cuatro notas del bajo, con la derecha bajando',
                          events=[ac(('G2', 'B3', 'D4'), 'h'), ac(('D2', 'A3', 'D4'), 'h'),
                                  ac(('G2', 'B3', 'D4'), 'h'), ac(('A2', 'A3', 'C#4'), 'h')],
                          bars=2, manos='dobla', show_time=False, key_sig='Re mayor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y LA SEGUNDA PÁGINA, PARA QUE NO TE PILLE',
                 texto='Míralo ahora, aunque no lo toques todavía: en el compás 21, el último de la '
                       'primera página, la derecha se pone en semicorcheas y ya no para hasta el '
                       'final. Son cuatro notas por cada golpe en vez de una, y la izquierda '
                       'debajo sigue haciendo lo de siempre. No es una pieza distinta ni hay nada '
                       'nuevo que aprenderse: es el mismo camino de acordes recorrido al doble de '
                       'velocidad. Por eso esta semana solo se pide la primera vuelta del bajo: '
                       'cuando llegues ahí, lo único que va a hacer falta es que la izquierda no '
                       'tenga que pensar.'),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los cuatro primeros compases con las dos manos, y la izquierda sin mirar el '
                       'papel: para eso se ha aprendido de memoria. Tu edición no dice a qué '
                       'velocidad hay que tocarla, así que empieza despacio y sube solo cuando las '
                       'ocho notas salgan sin pensarlas. Y mira el compás 5: ahí la izquierda deja '
                       'las blancas. Esta semana llegamos hasta ahí y ni un compás más.'),
        ] + bloques_extra('Re mayor', 113, 'D4', 'D2',
                          'el bajo obstinado: ocho notas que vuelven a empezar sin parar',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Canon de Pachelbel · para casa',
            intro='Quince minutos al día, y los ocho primeros con la izquierda sola. Esta semana la '
                  'memoria vale más que los dedos.',
            bloques=[
                reto('Las ocho notas del bajo, de memoria y sin mirar las teclas.',
                     'Dilas en voz alta cuatro veces seguidas sin el papel delante. Cuando salgan '
                     'de carrerilla, tócalas con los ojos en la partitura de la derecha: ahí sabrás '
                     'que están.'),
                plan((5, 'Las ocho notas del bajo, diciéndolas en voz alta'),
                     (4, 'El bajo en blancas y después en negras'),
                     (3, 'La derecha sola: las cuatro parejas de los cc. 1 y 2'),
                     (3, 'Los cc. 1 a 4 con las dos manos')),
                escalera((54, 'el bajo solo, las ocho notas seguidas y sin fallo'),
                         (66, 'los cc. 1 a 4 con las dos manos'),
                         (76, 'dos vueltas enteras del bajo sin parar'),
                         (88, 'y ahí paramos esta semana'),
                         meta='Tu partitura NO trae número de metrónomo, así que estos cuatro son '
                              'de trabajo, no de la edición: los ponemos nosotras y se pueden '
                              'cambiar en clase.'),
                contar([n('D3'), n('A2'), n('B2'), n('F#2'),
                        n('G2'), n('D2'), n('G2'), n('A2')],
                       ['¿Cuántas notas distintas hay? (ojo: dos se repiten)',
                        '¿Cuántas de las ocho van en tecla negra?',
                        '¿En qué compás deja el bajo de ir en blancas?'],
                       titulo='Cuenta sobre el bajo obstinado',
                       pista='son las ocho notas medidas de tu partitura, aquí en negras para que '
                             'quepan en una línea · en el papel van en blancas'),
                rodear([[n('D3', 'h'), n('A2', 'h')],
                        [n('D3', 'h'), n('A2', 'h')],
                        [n('D3', 'h'), n('B2', 'h')],
                        [n('D2', 'h'), n('A2', 'h')]],
                       titulo='Rodea los dos compases que son iguales',
                       pista='uno de los dos es el compás 1 de tu partitura · fíjate en la octava '
                             'de la primera nota'),
                para_clase('Las ocho notas del bajo de memoria, y los cuatro primeros compases con '
                           'las dos manos. Dime también a qué velocidad te salen: la del resto de '
                           'la pieza la decidimos a partir de ahí.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
