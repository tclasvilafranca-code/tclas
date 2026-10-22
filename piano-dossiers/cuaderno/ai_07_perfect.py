# -*- coding: utf-8 -*-
"""Perfect — pieza 7 de Aida. Formato ADULTO exigente.

   Abre la tercera etapa, la del cifrado, y trae ademas el compas mas raro del
   cuaderno: **12/8**. Es la primera pieza de todo el proyecto escrita asi, y
   por ella hubo que enseñarle al motor a dibujar la REDONDA CON PUNTILLO, que
   es la figura que llena un compas de doce corcheas (seis tiempos). Antes el
   motor devolvia una redonda, que son cuatro, y el compas se quedaba a medias.

   Lo comprobado sobre el PDF de SU carpeta (Campamento Bye Bye Beethoven,
   1 pagina). Este archivo NO lo tiene ningun otro alumno:

     - SOL MAYOR: un sostenido detras de la clave.
     - **12/8**, y arriba viene impreso el metronomo: **negra con puntillo =
       94**. Ojo con leerlo: el numero va a la NEGRA CON PUNTILLO, no a la
       negra, asi que son 94 golpes grandes por minuto y cada golpe lleva tres
       corcheas dentro.
     - Encima del pentagrama va el CIFRADO, y la vuelta es G · Em · C · D,
       cuatro letras que se repiten toda la cancion.
     - La digitacion viene impresa.
     - Empieza con una ANACRUSA de tres corcheas, medidas a 300 ppp:
       **Re4 · Mi4 · Sol4**. El compas 1 arranca con un Sol4 en blanca con
       puntillo.

   POR QUE LA FICHA LLEVA ANDAMIO Y NO LA CITA. La anacrusa esta medida, pero
   una fila de la ficha tiene que sumar compases enteros y la anacrusa son tres
   corcheas de un compas de doce. Del compas 1 esta medida la primera figura y
   no las demas, asi que citarlo entero seria escribir lo que no se ha medido.
   Lo medido va en la lista de "lo especial de esta partitura", que es donde no
   hace falta que cuadren los compases.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, plan, escalera, cifrado,
                      verdadero_falso, escribir, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# ANDAMIO en Sol mayor: el dibujo del 12/8, cuatro grupos de tres corcheas.
ARRANQUE = (corch(['G4', 'A4', 'B4'], 3) + corch(['B4', 'A4', 'G4'], 3) +
            corch(['A4', 'B4', 'C5'], 3) + corch(['B4', 'A4', 'G4'], 3))

# ANDAMIO sobre el cifrado IMPRESO: Sol y Mi menor, un acorde por medio compas.
BAJO = [ac(('G2', 'D3', 'B3'), 'h.'), ac(('E2', 'B2', 'G3'), 'h.')]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=7, nivel='intermedio',
    slug='Perfect', formato='adulto',
    titulo_corto='Perfect', time_sig=(12, 8), key_sig='Sol mayor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source', 'Perfect.pdf'),
    yt='https://www.youtube.com/results?search_query=perfect+ed+sheeran+piano+easy',

    ficha=dict(
        titulo='Perfect',
        autor='Ed Sheeran · arreglo del Campamento Bye Bye Beethoven',
        datos=[('Tonalidad', 'Sol mayor'), ('Compás', '12/8'),
               ('Tempo', '♩. = 94'), ('Cifrado', 'G Em C D'),
               ('Empieza', 'Antes del compás')],
        titulo_ritmos='Cómo se reparte un compás de 12/8',
        pie_ritmos='Andamio en Sol mayor. Arriba, los cuatro grupos de tres corcheas en que se '
                   'reparte un compás de 12/8; abajo, andamio sobre las dos primeras letras de '
                   'acorde que trae impresas tu partitura (G y Em).',
        armonia=dict(
            titulo='Doce corcheas que son cuatro golpes',
            tarjetas=[
                ('EL 12/8', 'Cuatro y tres',
                 'Doce corcheas por compás, agrupadas de tres en tres. No se cuenta hasta doce: se '
                 'cuentan CUATRO golpes y cada uno lleva tres corcheas dentro.'),
                ('EL TEMPO', '♩. = 94',
                 'El número va a la negra CON PUNTILLO, o sea al golpe grande. Son 94 golpes por '
                 'minuto, no 94 corcheas: leerlo mal te deja tocando al triple.'),
                ('EL CIFRADO', 'G · Em · C · D',
                 'Cuatro letras que se repiten toda la canción. Con esas cuatro se acompaña la '
                 'pieza entera, y esta semana se aprenden.'),
                ('LA ANACRUSA', 'Tres corcheas',
                 'Re, Mi y Sol antes del primer compás: es un golpe entero de los grandes, y hay '
                 'que contarlo.'),
            ],
            pie='El 12/8 es la manera de escribir un balanceo: cada golpe se parte en tres y por eso '
                'la música suena a vaivén en vez de a marcha. Es el mismo compás de casi todas las '
                'baladas lentas de los años cincuenta, que es exactamente de donde viene esta.',
        ),
        ritmos=[
            ('LA MANO DERECHA', 'andamio · los cuatro grupos de tres',
             ARRANQUE, OCRE, 'treble', None),
            ('LA MANO IZQUIERDA', 'andamio sobre el cifrado impreso (G y Em)',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay un sostenido: todos los Fa a la tecla negra.',
            'El compás es 12/8: doce corcheas agrupadas de tres en tres.',
            'Arriba viene impreso el metrónomo: negra CON PUNTILLO = 94.',
            'Empieza con una anacrusa de tres corcheas: Re, Mi y Sol.',
            'El compás 1 arranca con un Sol en blanca con puntillo.',
            'Encima del pentagrama va el cifrado: G, Em, C y D.',
        ],
        reto='Contar el 12/8 en cuatro y no en doce. Contando doce la música se vuelve un desfile de '
             'corcheas iguales y se pierde el balanceo, que es lo único que tiene esta canción.',
        truco='Cuenta "UN-dos-tres DOS-dos-tres TRES-dos-tres CUA-tro-tres" y marca con el pie solo '
              'las mayúsculas. El pie va a 94: si el pie va más rápido, estás contando corcheas.',
        sabias='Ed Sheeran la escribió para su mujer, Cherry, con la que iba al colegio. La grabó en '
               'un compás de 12/8 a propósito para que sonara a los boleros que bailaban sus padres, '
               'y por eso suena antigua sin serlo.',
        qr=dict(titulo='Escúchala',
                texto='Marca el pie con la canción. Si te salen cuatro pisadas por compás vas bien; '
                      'si te salen doce, estás contando las corcheas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Lo nuevo de esta semana es el compás, y el compás no se estudia con los dedos: se '
              'estudia con el pie y con la voz antes de tocar una sola nota.',
        reglas=['CUATRO GOLPES POR COMPÁS, NO DOCE', 'EL PIE VA A 94, QUE ES LO QUE PONE',
                'TRES CORCHEAS DENTRO DE CADA GOLPE'],
        bloques=[
            dict(num=1, titulo='El vaivén del 12/8',
                 pista='andamio en Sol mayor · lo que se practica aquí es el agrupamiento, no las '
                       'notas',
                 sistemas=[
                     dict(cap='a) un compás entero en una sola nota larga · esto es lo que dura un '
                              'compás de 12/8: seis tiempos',
                          events=[n('G4', 'w.')],
                          matiz='mp',
                          bars=1),
                     dict(cap='b) y el mismo compás partido en cuatro golpes · cada uno vale tres '
                              'corcheas',
                          events=[n('G4', 'q.'), n('B4', 'q.'), n('D5', 'q.'), n('B4', 'q.')],
                          bars=1, show_time=False),
                     dict(cap='c) y ahora los cuatro golpes con sus tres corcheas dentro · di '
                              '"UN-dos-tres" en cada grupo',
                          events=corch(['G4', 'A4', 'B4'], 3) + corch(['D5', 'B4', 'A4'], 3) +
                                 corch(['B4', 'C5', 'D5'], 3) + corch(['C5', 'B4', 'A4'], 3),
                          bars=1, show_time=False),
                     dict(cap='d) y dos compases seguidos, que es donde se ve si el vaivén se '
                              'mantiene · el segundo golpe de cada compás es el que se acorta',
                          events=corch(['G4', 'A4', 'B4'], 3) + corch(['C5', 'B4', 'A4'], 3) +
                                 corch(['B4', 'C5', 'D5'], 3) + corch(['C5', 'B4', 'G4'], 3) +
                                 corch(['A4', 'B4', 'C5'], 3) + corch(['B4', 'A4', 'G4'], 3) +
                                 corch(['G4', 'A4', 'B4'], 3) + corch(['A4', 'G4', 'F#4'], 3),
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL 94 NO ES LO QUE PARECE',
                 texto='El número de metrónomo dice a qué velocidad va la figura que tiene dibujada '
                       'al lado, y aquí la figura es una NEGRA CON PUNTILLO. O sea 94 golpes '
                       'grandes por minuto, con tres corcheas metidas en cada uno: 282 corcheas por '
                       'minuto. Si pones el metrónomo a 94 y le das una corchea por clic, la '
                       'canción te va a durar tres veces más de lo que dura. Es el error clásico '
                       'del compás compuesto y se comete una sola vez.'),
            dict(num=2, titulo='Los cuatro acordes de la letra',
                 pista='andamio sobre el cifrado IMPRESO en tu partitura (G, Em, C, D)',
                 sistemas=[
                     dict(cap='a) los cuatro, uno por compás, en la figura que llena el 12/8',
                          events=[ac(('G2', 'D3', 'B3'), 'w.'), ac(('E2', 'B2', 'G3'), 'w.'),
                                  ac(('C3', 'G3', 'E4'), 'w.'), ac(('D3', 'F#3', 'A3'), 'w.')],
                          bars=4, clef='bass'),
                     dict(cap='b) y con el acorde repetido en cada golpe, para sentir los cuatro',
                          events=[ac(('G2', 'D3', 'B3'), 'q.'), ac(('G2', 'D3', 'B3'), 'q.'),
                                  ac(('G2', 'D3', 'B3'), 'q.'), ac(('G2', 'D3', 'B3'), 'q.'),
                                  ac(('E2', 'B2', 'G3'), 'q.'), ac(('E2', 'B2', 'G3'), 'q.'),
                                  ac(('E2', 'B2', 'G3'), 'q.'), ac(('E2', 'B2', 'G3'), 'q.')],
                          bars=2, clef='bass', show_time=False),
                     dict(cap='c) y desplegado, que es como suena de verdad en una balada',
                          events=corch(['G2', 'D3', 'B3'], 3) + corch(['D3', 'B3', 'D3'], 3) +
                                 corch(['E2', 'B2', 'G3'], 3) + corch(['B2', 'G3', 'B2'], 3),
                          bars=1, clef='bass', show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, con el vaivén puesto',
                 pista='andamio · la melodía encima y el acorde debajo, en 12/8',
                 sistemas=[
                     dict(cap='a) un compás con las dos manos: cuatro golpes arriba y el acorde '
                              'aguantando debajo',
                          events=[ac(('G2', 'D3', 'G4'), 'q.'), ac(('B4',), 'q.'),
                                  ac(('D5',), 'q.'), ac(('B4',), 'q.')],
                          bars=1, manos='sostiene'),
                     dict(cap='b) y dos compases con el cambio de acorde de G a Em, que es el '
                              'primero que trae tu partitura',
                          events=[ac(('G2', 'D3', 'G4'), 'q.'), ac(('B4',), 'q.'),
                                  ac(('D5',), 'q.'), ac(('B4',), 'q.'),
                                  ac(('E2', 'B2', 'G4'), 'q.'), ac(('A4',), 'q.'),
                                  ac(('B4',), 'q.'), ac(('G4',), 'q.')],
                          bars=2, manos='sostiene', show_time=False),
                     dict(cap='c) y la vuelta entera de cuatro acordes, con la melodía moviéndose '
                              'por dentro de cada uno',
                          events=[ac(('G2', 'D3', 'G4'), 'q.'), ac(('B4',), 'q.'),
                                  ac(('D5',), 'q.'), ac(('B4',), 'q.'),
                                  ac(('E2', 'B2', 'G4'), 'q.'), ac(('B4',), 'q.'),
                                  ac(('A4',), 'q.'), ac(('G4',), 'q.'),
                                  ac(('C3', 'G3', 'E4'), 'q.'), ac(('G4',), 'q.'),
                                  ac(('E4',), 'q.'), ac(('G4',), 'q.'),
                                  ac(('D3', 'A3', 'F#4'), 'q.'), ac(('A4',), 'q.'),
                                  ac(('D5',), 'q.'), ac(('A4',), 'q.')],
                          bars=4, manos='sostiene', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Con el metrónomo a 94 y un clic por golpe grande, cuenta la anacrusa (Re, '
                       'Mi, Sol: es un golpe entero) y toca los cuatro primeros compases. Si el '
                       'metrónomo te agobia, bájalo a 70, pero no lo cambies a corcheas: en cuanto '
                       'cuentas doce, el balanceo desaparece y ya no vuelve.'),
        ] + bloques_extra('Sol mayor', 93, 'G4', 'G2',
                          'el 12/8: cuatro golpes con tres corcheas dentro de cada uno',
                          desde=4, time_sig=(12, 8), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Perfect · para casa',
            intro='Veinte minutos al día. Los cinco primeros, sin tocar: contando y marcando con '
                  'el pie. El compás es lo único nuevo y es todo lo que hay que ganar.',
            bloques=[
                plan((5, 'Contar "UN-dos-tres DOS-dos-tres..." con el pie, sin tocar'),
                     (5, 'Los cuatro acordes del cifrado, uno por compás'),
                     (5, 'La anacrusa y el compás 1, con la mano derecha sola'),
                     (5, 'Los dos primeros compases con las dos manos')),
                escalera((70, 'los cuatro acordes, con el pie marcando los cuatro golpes'),
                         (84, 'la anacrusa y los dos primeros compases'),
                         (94, 'los cuatro primeros compases con las dos manos'),
                         meta='94, que es el número IMPRESO en tu partitura · y va a la negra con '
                              'puntillo, o sea un clic por golpe grande',
                         notas=['Un clic por golpe, nunca uno por corchea.']),
                cifrado([('G', 'Sol'), ('Em', 'Mi menor'), ('C', 'Do'), ('D', 'Re')],
                        ['¿Cuál de los cuatro es menor?',
                         '¿Cuál lleva el Fa sostenido de la armadura?'],
                        titulo='Las cuatro letras de acorde de tu partitura',
                        pista='están impresas encima del pentagrama y se repiten toda la canción'),
                verdadero_falso(['Un compás de 12/8 tiene doce corcheas.',
                                 'En 12/8 se cuentan doce golpes por compás.',
                                 'El 94 de tu partitura va a la negra con puntillo.',
                                 'La anacrusa de esta pieza son tres corcheas.',
                                 'Todos los Fa de esta pieza van a la tecla blanca.'],
                                titulo='Verdadero o falso',
                                pista='las cinco frases hablan de TU partitura'),
                escribir(titulo='Copia aquí la anacrusa: Re, Mi y Sol en corcheas',
                         pista='y escribe debajo cuántos tiempos suman las tres juntas'),
                para_clase('La anacrusa y los cuatro primeros compases con el metrónomo a 94. Y '
                           'dime cuántas pisadas te salen por compás: si son cuatro, ya está '
                           'ganado lo difícil de esta pieza.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
