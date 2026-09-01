# -*- coding: utf-8 -*-
"""Carol of the Bells — pieza 13 de Aida. Formato ADULTO exigente.

   Abre la quinta etapa, la del modo menor. Y lo hace con la pieza que menos
   material tiene de todo el cuaderno: **cuatro notas**, repetidas compas tras
   compas sin cambiar una sola vez. Lo dificil no es aprenderselas, es no
   acelerar ni aflojar mientras se repiten.

   Lo comprobado sobre el PDF de SU carpeta (arreglo de Jim Paterson para
   mfiles.co.uk, 1 pagina, vectorial; el mismo archivo que el de Jose Maria):

     - Detras de la clave hay **DOS BEMOLES** (Si y Mi): Sol menor.
     - **3/4**.
     - **NO trae nada escrito arriba**: ni tempo, ni caracter, ni una sola
       indicacion de fuerza. Todo
       lo que se diga de la velocidad en estas hojas sale de la clase, no de la
       edicion, y asi esta dicho en la propia hoja.
     - La cabecera pone "Keyboard: Piano/Organ or tuned percussion".
     - Trae barras de repeticion: la de abrir esta al principio del c. 5.

   LAS ALTURAS, medidas a 150 ppp sobre las cinco lineas de cada pentagrama:

       DERECHA    cc. 1 a 7 (y siguen): SIEMPRE el mismo compas
                  Si bemol4 (negra) · La4 · Si bemol4 (corcheas) · Sol4 (negra)

       IZQUIERDA  cc. 1 a 4  compas entero de silencio
                  c. 5  Sol4 · c. 6  Fa4 · c. 7  Mi bemol4
                  todas blancas con puntillo, o sea el compas entero.

   El compas cierra en 3: 1 + 0,5 + 0,5 + 1.

   UNA COSA QUE HAY QUE MIRAR DOS VECES: la izquierda de los cc. 5 a 7 esta
   escrita en clave de FA pero suena por encima del Do central, colgando de
   dos y tres lineas adicionales POR ARRIBA. No es una errata de la edicion ni
   nuestra: es que en esta pieza las dos manos van muy juntas. Se cita tal
   cual, con su clave, porque pasarla a clave de sol escondería de quien es la
   nota — el mismo motivo por el que el cruce de manos de *My Bonnie* tiene su
   excepcion en `auditar_registro`.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, plan, escalera, inventa, dibujar,
                      nombres, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas de la DERECHA, medido. Es el mismo desde el c. 1 hasta bien entrada
# la pieza: cita literal.
CELULA = [n('Bb4')] + corch(['A4', 'Bb4']) + [n('G4')]

# Y la IZQUIERDA de los cc. 5, 6 y 7: una blanca con puntillo por compas.
BAJO = [n('G4', 'h.'), n('F4', 'h.'), n('Eb4', 'h.')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=13, nivel='intermedio',
    slug='CarolOfTheBells', formato='adulto',
    titulo_corto='Carol of the Bells', time_sig=(3, 4), key_sig='Sol menor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Carol of the Bells.pdf'),
    yt='https://www.youtube.com/results?search_query=carol+of+the+bells+piano',

    ficha=dict(
        titulo='Carol of the Bells',
        autor='Mykola Leontovych · arr. Jim Paterson',
        datos=[('Tonalidad', 'Sol menor'), ('Compás', '3/4'),
               ('Armadura', 'Dos bemoles'), ('Motivo', 'Cuatro notas'),
               ('Trae', 'Repetición')],
        titulo_ritmos='El compás que se repite',
        pie_ritmos='Arriba, el compás 1 de la derecha MEDIDO en tu partitura, y es el mismo compás '
                   'siete veces seguidas. Abajo, la izquierda de los cc. 5 y 6, medida: una blanca '
                   'con puntillo en cada uno.',
        armonia=dict(
            titulo='Cuatro notas y tres bajos',
            tarjetas=[
                ('LA CÉLULA', 'Si♭ La Si♭ Sol',
                 'Cuatro notas que caben en una mano quieta y no cambian nunca. Aprendidas una vez, '
                 'la derecha ya no tiene nada más que aprender en toda esta parte.'),
                ('DOS BEMOLES', 'Si y Mi',
                 'La armadura de Sol menor. El Si de la célula va SIEMPRE en la tecla negra, y el '
                 'Mi de la izquierda del c. 7 también.'),
                ('EL BAJO QUE BAJA', 'Sol · Fa · Mi♭',
                 'La izquierda entra en el c. 5 y hace tres notas largas que bajan de grado en '
                 'grado. Eso es todo lo que cambia mientras la derecha repite.'),
                ('LA CLAVE DE FA', 'Y muy arriba',
                 'Esas tres notas van escritas en clave de fa pero suenan por encima del Do '
                 'central, con dos y tres líneas adicionales. Las manos quedan muy juntas.'),
            ],
            pie='Es la pieza con menos notas del cuaderno y una de las que más cuesta: cuando algo '
                'se repite doce veces, el error no es tocarlo mal, es empezar a acelerar sin darte '
                'cuenta. Por eso esta semana el metrónomo no es un adorno.',
        ),
        ritmos=[
            ('DERECHA', 'el c. 1, MEDIDO · y los seis siguientes son iguales',
             CELULA, OCRE, 'treble', 'Sol menor'),
            ('IZQUIERDA', 'los cc. 5 y 6, medidos · una por compás',
             BAJO[:2], AZUL, 'bass', 'Sol menor'),
        ],
        especial=[
            'Detrás de la clave hay dos bemoles: Si y Mi van en tecla negra.',
            'El compás es 3/4: tres negras por compás.',
            'La partitura no trae ni tempo ni carácter escritos.',
            'El compás de la derecha es siempre el mismo: Si♭ · La · Si♭ · Sol.',
            'La izquierda calla los cuatro primeros compases.',
            'En el compás 5 hay una barra de repetición.',
            'La izquierda de los cc. 5 a 7 va con líneas adicionales por arriba.',
        ],
        reto='Repetir el mismo compás siete veces sin acelerar. No hay ninguna nota difícil: la '
             'dificultad es que el oído se acostumbra y la mano empieza a correr sin avisar.',
        truco='Con el metrónomo puesto, cuenta en voz alta "UN dos tres" y fíjate solo en el clic '
              'del uno. Si el clic empieza a llegar tarde, eres tú quien va rápido.',
        sabias='La escribió Leontovych en 1914 sobre una canción de año nuevo ucraniana que habla '
               'de una golondrina, no de campanas: la letra inglesa de las campanas se le puso '
               'veinte años después, en Estados Unidos. La melodía original tiene esas mismas '
               'cuatro notas repetidas de principio a fin.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta cuántas veces seguidas se repite el mismo compás antes de que cambie '
                      'algo. Y fíjate en que lo que cambia nunca es la melodía: es lo de debajo.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Cuatro notas y ya está. Todo el trabajo de esta semana es que esas cuatro notas '
              'suenen exactamente igual la primera vez y la duodécima.',
        reglas=['SI Y MI, EN TECLA NEGRA', 'TRES TIEMPOS POR COMPÁS',
                'EL MISMO COMPÁS, SIEMPRE IGUAL'],
        bloques=[
            dict(num=1, titulo='La célula de cuatro notas',
                 pista='c. 1 · MEDIDO en tu partitura · y los seis compases siguientes son iguales',
                 sistemas=[
                     dict(cap='a) los cuatro primeros compases, que son el mismo compás cuatro '
                              'veces · lo que se mira es si el cuarto suena igual que el primero',
                          events=CELULA * 4, bars=4, key_sig='Sol menor'),
                     dict(cap='b) y con las dos corcheas del medio contadas en negras, para '
                              'colocarlas · en tu partitura son dos corcheas',
                          events=[n('Bb4'), n('A4'), n('Bb4'), n('G4'), n('Bb4'), n('G4')],
                          bars=2, show_time=False, key_sig='Sol menor'),
                 ]),
            dict(num=2, titulo='La misma figura, empezando en otra nota',
                 pista='andamio en Sol menor · lo que se practica es el dibujo de la célula, no '
                       'las alturas',
                 sistemas=[
                     dict(cap='a) empezando un grado más arriba · Do, Si bemol, Do, La',
                          events=([n('C5')] + corch(['Bb4', 'C5']) + [n('A4')]) * 2,
                          bars=2, key_sig='Sol menor'),
                     dict(cap='b) y otro más · Re, Do, Re, Si bemol',
                          events=([n('D5')] + corch(['C5', 'D5']) + [n('Bb4')]) * 2,
                          bars=2, show_time=False, key_sig='Sol menor'),
                     dict(cap='c) y bajando desde el Sol, que es donde acaba la célula de verdad',
                          events=([n('G4')] + corch(['F4', 'G4']) + [n('Eb4')]) * 2,
                          bars=2, show_time=False, key_sig='Sol menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ REPETIR CANSA MÁS QUE CAMBIAR',
                 texto='Cuando una frase cambia, el oído está pendiente y la mano va detrás de él. '
                       'Cuando se repite, el oído se despista a los tres o cuatro compases y la '
                       'mano se queda sola: es entonces cuando empieza a acelerar, y como acelera '
                       'poco a poco, no se nota desde dentro. Se nota desde fuera, o con un '
                       'metrónomo. En esta pieza el metrónomo no es para ir más rápido: es para '
                       'saber si vas donde crees que vas.'),
            dict(num=3, titulo='La izquierda: tres notas largas que bajan',
                 pista='cc. 5, 6 y 7 de la mano izquierda · MEDIDO · una blanca con puntillo por '
                       'compás',
                 sistemas=[
                     dict(cap='a) las tres, tal y como están · en clave de fa y con líneas '
                              'adicionales por arriba: es tu mano izquierda, aunque suene alto',
                          events=list(BAJO), bars=3, clef='bass', key_sig='Sol menor'),
                     dict(cap='b) y las mismas tres partidas en negras, para contar los tres tiempos '
                              'en voz alta · en tu partitura son blancas con puntillo',
                          events=[n('G4'), n('G4'), n('G4'), n('F4'), n('F4'), n('F4'),
                                  n('Eb4'), n('Eb4'), n('Eb4')],
                          bars=3, clef='bass', show_time=False, key_sig='Sol menor'),
                     dict(cap='c) y con el compás callado de delante · en tu partitura la izquierda '
                              'no toca hasta el c. 5, y ese silencio hay que contarlo',
                          events=[sil('h.')] + list(BAJO),
                          bars=4, clef='bass', show_time=False, key_sig='Sol menor'),
                 ]),
            dict(num=4, titulo='Las dos manos, que van muy juntas',
                 pista='cc. 5 y 6 con las dos manos · MEDIDO · la izquierda entra y ya no se mueve '
                       'hasta el compás siguiente',
                 sistemas=[
                     dict(cap='a) los cc. 5 y 6 · entre un compás y el otro solo cambia la nota '
                              'de abajo',
                          events=[ac(('G4', 'Bb4'))] + corch(['A4', 'Bb4']) + [n('G4')] +
                                 [ac(('F4', 'Bb4'))] + corch(['A4', 'Bb4']) + [n('G4')],
                          bars=2, manos='sostiene', key_sig='Sol menor'),
                     dict(cap='b) y el c. 7, donde la nota de abajo llega al Mi bemol y cierra la '
                              'bajada',
                          events=[ac(('Eb4', 'Bb4'))] + corch(['A4', 'Bb4']) + [n('G4')],
                          bars=1, manos='sostiene', show_time=False, key_sig='Sol menor'),
                     dict(cap='c) y los tres seguidos, que es la bajada entera · la derecha no se '
                              'entera de nada y ese es justo el trabajo',
                          events=[ac(('G4', 'Bb4'))] + corch(['A4', 'Bb4']) + [n('G4')] +
                                 [ac(('F4', 'Bb4'))] + corch(['A4', 'Bb4']) + [n('G4')] +
                                 [ac(('Eb4', 'Bb4'))] + corch(['A4', 'Bb4']) + [n('G4')],
                          bars=3, manos='sostiene', show_time=False, key_sig='Sol menor'),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Los siete primeros compases con las dos manos y con el metrónomo puesto de '
                       'principio a fin. Y una advertencia sobre el camino: en el compás 5 empieza '
                       'una repetición, así que antes de tocar sigue con el dedo por dónde va la '
                       'pieza. Tu edición no dice a qué velocidad hay que tocarla, así que la '
                       'decidimos nosotras y la anotas tú a lápiz.'),
        ] + bloques_extra('Sol menor', 105, 'G4', 'G2',
                          'la célula de cuatro notas que se repite sin cambiar',
                          desde=5, time_sig=(3, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Carol of the Bells · para casa',
            intro='Quince minutos al día y el metrónomo puesto siempre. Con tan pocas notas, lo que '
                  'se trabaja esta semana es la regularidad.',
            bloques=[
                plan((3, 'La célula sola, muy despacio, mirando los dos bemoles'),
                     (5, 'Cuatro compases seguidos con el metrónomo, sin acelerar'),
                     (3, 'La izquierda sola: Sol, Fa, Mi bemol, contando tres'),
                     (4, 'Los cc. 5 a 7 con las dos manos')),
                escalera((60, 'la célula sola, cuatro veces seguidas e iguales'),
                         (72, 'los cc. 1 a 4 sin mirarte las manos'),
                         (84, 'los cc. 1 a 7 con la izquierda dentro'),
                         (96, 'y ahí paramos esta semana'),
                         meta='Tu partitura NO trae número de metrónomo, así que estos cuatro son '
                              'de trabajo, no de la edición: los ponemos nosotras y se pueden '
                              'cambiar en clase.'),
                inventa(['Solo Sol, La, Si bemol y Do.',
                         'Dos compases de tres tiempos.',
                         'Que los dos compases sean exactamente iguales.'],
                        time_sig=(3, 4),
                        titulo='Inventa una célula que se repita',
                        pista='y tócala ocho veces seguidas con el metrónomo, a ver si aguanta'),
                dibujar(['Sol', 'Si bemol', 'La', 'Mi bemol', 'Fa', 'Re', 'Sol'],
                        titulo='Dibuja tú las notas',
                        pista='en clave de sol, y acuérdate de que dos de ellas llevan bemol'),
                nombres(['Bb4', 'A4', 'G4', 'F4', 'Eb4', 'D4', 'Bb4'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='las cuatro primeras salen de tu célula · ojo con las dos que van en '
                              'tecla negra por la armadura'),
                para_clase('Los cuatro primeros compases con el metrónomo y a la velocidad más alta '
                           'que te salgan iguales. Y dime si te has despistado en alguna repetición: '
                           'eso es lo que vamos a mirar.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
