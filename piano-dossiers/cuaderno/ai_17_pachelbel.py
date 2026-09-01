# -*- coding: utf-8 -*-
"""Canon in D, de Johann Pachelbel — pieza 17 de Aida. Formato ADULTO
   exigente.

   Segunda de la ultima etapa y primera de las tres que van seguidas en mayo y
   junio: Pachelbel, el Preludio de Bach y A comme amour. Las tres trabajan lo
   mismo —la mano abierta en arpegio— y en ese orden cada una prepara la
   siguiente.

   Esta es la unica del cuaderno construida sobre un BAJO OBSTINADO: ocho notas
   en la mano izquierda que se repiten enteras, sin cambiar una sola vez, de
   principio a fin. Aprendidas esas ocho, la izquierda ya no tiene nada mas que
   aprender en toda la pieza.

   Lo comprobado sobre el PDF de SU carpeta (arreglo de Jim Paterson para
   mfiles.co.uk, 2 paginas, vectorial). Es solo suya.

     - Detras de la clave hay **DOS SOSTENIDOS** (Fa y Do): Re mayor.
     - **4/4**.
     - NO trae tempo impreso ni caracter escrito.
     - Lleva semicorcheas, medidas: 82 pares de barras dobles en el PDF. En la
       primera pagina la izquierda pasa de blancas a negras y luego a corcheas:
       el bajo es el mismo y lo que cambia es la velocidad con que se recorre.

   LAS ALTURAS, medidas a 150 ppp sobre las cinco lineas de cada pentagrama:

       IZQUIERDA (el bajo obstinado, cc. 1 a 4, todo blancas)
                 Re3 · La2 · Si2 · Fa#2 · Sol2 · Re2 · Sol2 · La2

       DERECHA   c. 1  Re4+Fa#4 · Do#4+Mi4   (dos notas a la vez, blancas)
                 c. 2  Si3+Re4 · La3+Do#4

   Cada compas cierra en 4: dos blancas.

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
from ai_comun import (n, ac, sil, corch, reto, plan, escalera, contar, rodear,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El BAJO OBSTINADO, medido: ocho notas que se repiten enteras toda la pieza.
# Cita literal (cc. 1 a 4, en blancas).
BAJO = [n('D3', 'h'), n('A2', 'h'), n('B2', 'h'), n('F#2', 'h'),
        n('G2', 'h'), n('D2', 'h'), n('G2', 'h'), n('A2', 'h')]

# Y la derecha de los cc. 1 y 2, medida: dos notas a la vez, blancas.
DER = [ac(('D4', 'F#4'), 'h'), ac(('C#4', 'E4'), 'h'),
       ac(('B3', 'D4'), 'h'), ac(('A3', 'C#4'), 'h')]

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
               ('Se repite', 'Toda la pieza')],
        titulo_ritmos='El bajo que sostiene la pieza',
        pie_ritmos='Arriba, la derecha del c. 1 MEDIDA en tu partitura: dos notas a la vez, '
                   'una blanca cada media parte del compás. Abajo, las ocho notas del bajo, también '
                   'medidas: es el dibujo que se repite entero durante toda la pieza.',
        armonia=dict(
            titulo='Ocho notas y toda una pieza',
            tarjetas=[
                ('EL BAJO OBSTINADO', 'Ocho notas',
                 'Re · La · Si · Fa♯ · Sol · Re · Sol · La. Se repiten enteras, en ese orden, de '
                 'principio a fin. No hay una novena nota que aprender.'),
                ('LO QUE SÍ CAMBIA', 'La velocidad',
                 'Al principio el bajo va en blancas, después en negras y más adelante en corcheas. '
                 'Las notas son las mismas: lo que cambia es cuántas caben en cada compás.'),
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
            ('EL BAJO', 'las ocho notas, medidas · se repiten enteras',
             list(BAJO), AZUL, 'bass', 'Re mayor'),
        ],
        especial=[
            'Detrás de la clave hay dos sostenidos: Fa y Do van en tecla negra.',
            'El compás es 4/4 y los primeros compases son todo blancas.',
            'La partitura no trae ni tempo ni carácter escritos.',
            'La izquierda repite las mismas ocho notas durante toda la pieza.',
            'La cuarta nota del bajo es un Fa sostenido.',
            'Más adelante el bajo pasa a negras y después a corcheas.',
            'La derecha empieza tocando dos notas a la vez.',
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
        intro='Esta semana se empieza y casi se acaba por la izquierda. Ocho notas de memoria y el '
              'resto de la pieza se cae sola encima.',
        reglas=['LAS OCHO NOTAS, DE MEMORIA', 'FA Y DO, SIEMPRE A LA NEGRA',
                'LA DERECHA SE COLOCA Y AGUANTA'],
        bloques=[
            dict(num=1, titulo='Las ocho notas del bajo',
                 pista='cc. 1 a 4 de la mano izquierda · MEDIDO · dos blancas por compás',
                 sistemas=[
                     dict(cap='a) las cuatro primeras (cc. 1 y 2) · dilas en voz alta mientras las '
                              'tocas, y no mires las teclas',
                          events=BAJO[:4], bars=2, clef='bass', key_sig='Re mayor'),
                     dict(cap='b) y las cuatro que cierran la vuelta (cc. 3 y 4) · la sexta baja una '
                              'octava, que es lo que hace que la vuelta suene a que empieza otra vez',
                          events=BAJO[4:], bars=2, clef='bass', show_time=False,
                          key_sig='Re mayor'),
                     dict(cap='c) y con cada nota repetida en corcheas · andamio: así se prepara la '
                              'versión rápida sin cambiar ni una nota',
                          events=corch(['D3', 'D3']) + corch(['A2', 'A2']) +
                                 corch(['B2', 'B2']) + corch(['F#2', 'F#2']),
                          bars=2, clef='bass', show_time=False, key_sig='Re mayor'),
                     dict(cap='d) y la segunda mitad igual, para que la mano no se pare a mitad de '
                              'vuelta · andamio sobre esas mismas cuatro notas',
                          events=corch(['G2', 'G2']) + corch(['D2', 'D2']) +
                                 corch(['G2', 'G2']) + corch(['A2', 'A2']),
                          bars=2, clef='bass', show_time=False, key_sig='Re mayor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES UN BAJO OBSTINADO',
                 texto='Es una línea de bajo que se repite igual una y otra vez mientras por encima '
                       'cambia todo lo demás. "Obstinado" no es una manera de hablar: en italiano '
                       'se llama ostinato y quiere decir justo eso, que se empeña. Lo bueno para '
                       'quien lo toca es que la mano izquierda deja de leer a las dos vueltas y '
                       'pasa a funcionar de memoria; a partir de ahí toda la cabeza queda libre '
                       'para la derecha, que es la que va cambiando.'),
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
                     dict(cap='d) y las dos líneas juntas otra vez, en negras y bajando cuatro '
                              'grados seguidos · andamio: es el camino que hacen las dos a la vez',
                          events=[ac(('D4', 'F#4')), ac(('C#4', 'E4')), ac(('B3', 'D4')),
                                  ac(('A3', 'C#4')), ac(('G3', 'B3')), ac(('F#3', 'A3')),
                                  ac(('G3', 'B3')), ac(('A3', 'C#4'))],
                          bars=2, show_time=False, key_sig='Re mayor'),
                 ]),
            dict(num=3, titulo='Las dos manos, con el bajo debajo',
                 pista='cc. 1-2 con las dos manos · MEDIDO · cada pareja de la derecha cae con una '
                       'nota del bajo',
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
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los cuatro primeros compases con las dos manos, y la izquierda sin mirar el '
                       'papel: para eso se ha aprendido de memoria. Tu edición no dice a qué '
                       'velocidad hay que tocarla, así que empieza despacio y sube solo cuando las '
                       'ocho notas salgan sin pensarlas. Y cuenta cuántas vueltas del bajo hay en '
                       'la primera página: es la mejor manera de ver cómo está hecha la pieza.'),
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
                        '¿Cuántos compases ocupa una vuelta entera en tu partitura?'],
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
