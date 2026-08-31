# -*- coding: utf-8 -*-
"""Can't Help Falling in Love — pieza 4 de Aida. Formato ADULTO exigente.

   Abre la segunda etapa, la de "cada mano con su papel", y lo hace con el
   reparto mas claro que existe: arriba UNA nota por compas, abajo corcheas sin
   parar. Es la pieza en la que se ve, sin explicar nada, que las dos manos no
   tienen por que hacer lo mismo.

   Lo comprobado sobre el PDF de SU carpeta (Musescore, "Piano ~ Chords ~
   Lyrics", 2 paginas; el mismo archivo, byte a byte, que el de Jose Maria,
   Josep, Nel, Dilan y Eva):

     - RE MAYOR: dos sostenidos detras de la clave (Fa# y Do#).
     - 3/4. Es un vals, y de los lentos.
     - Encima del pentagrama van las letras de acorde, y debajo DOS estrofas de
       letra ("Wise men say" y "Shall I stay").
     - La mano derecha lleva una BLANCA CON PUNTILLO por compas: una nota que
       dura el compas entero. La izquierda va en corcheas continuas.

   LAS ALTURAS de la derecha, medidas a 300 ppp con las lineas del pentagrama
   marcadas en rojo:

       c. 1   Re4     blanca con puntillo     "Wise"
       c. 2   La4     blanca con puntillo     "men"

   El c. 1 se leyo dos veces porque la primera daba una nota mas grave de lo que
   parecia a simple vista: la cabeza cuelga medio espacio por debajo de la linea
   del Mi4, o sea Re4. Con la armadura de dos sostenidos ese Re NO se altera.

   El archivo lo comparten cinco alumnos mas, asi que la CITA coincide y debe
   coincidir; el andamio de aqui va por el ARPEGIO de Re, que es lo que hace la
   izquierda, y no por la melodia.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, reto, plan, objetivo, teclado,
                      ordenar, figuras, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# Los compases 1 y 2 de la DERECHA, medidos. Cita literal.
ARRANQUE = [n('D4', 'h.'), n('A4', 'h.')]

# La izquierda: el arpegio de Re, que es el dibujo que hace. ANDAMIO.
BAJO = corch(['D3', 'A3']) + corch(['D4', 'A3']) + corch(['F#3', 'A3'])

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=4, nivel='intermedio',
    slug='CantHelpFallingInLove', formato='adulto',
    titulo_corto="Can't Help Falling in Love", time_sig=(3, 4), key_sig='Re mayor',
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           "Can't Help Falling in Love.pdf"),
    yt='https://www.youtube.com/results?search_query=cant+help+falling+in+love+piano+easy',

    ficha=dict(
        titulo="Can't Help Falling in Love",
        autor='Elvis Presley · Weiss, Peretti y Creatore · arreglo con cifrado y letra',
        datos=[('Tonalidad', 'Re mayor'), ('Armadura', 'Dos sostenidos'),
               ('Compás', '3/4'), ('Derecha', 'Notas largas'),
               ('Izquierda', 'Corcheas')],
        titulo_ritmos='El reparto entre las dos manos',
        pie_ritmos='Arriba, los compases 1 y 2 de la derecha MEDIDOS en tu partitura. Abajo, '
                   'andamio en Re mayor: el arpegio que la izquierda hace en corcheas, con las '
                   'notas exactas en tu papel.',
        armonia=dict(
            titulo='Una mano quieta y la otra sin parar',
            tarjetas=[
                ('LA DERECHA', 'Una por compás',
                 'Blanca con puntillo: tres tiempos, una sola nota. Toda la melodía del principio '
                 'va así, y por eso lo difícil no es tocarla sino no adelantarse.'),
                ('LA IZQUIERDA', 'Corcheas',
                 'Seis por compás, sin parar, dibujando el acorde por dentro. Es el motor: si se '
                 'para, la pieza se cae aunque la melodía siga.'),
                ('DOS SOSTENIDOS', 'Fa# y Do#',
                 'Están en la armadura, así que valen para toda la pieza y para las dos manos.'),
                ('UN VALS LENTO', 'Tres tiempos',
                 'Se cuenta de tres, con el peso en el "un". Elvis lo grabó en 1961 y la melodía '
                 'es de una canción francesa del siglo XVIII.'),
            ],
            pie='Es la primera pieza del cuaderno donde las dos manos hacen cosas de verdad '
                'distintas. Y está aquí y no más tarde porque el reparto es el más fácil que hay: '
                'la que se mueve no tiene que pensar y la que piensa no se mueve.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1 y 2, MEDIDOS · una nota por compás',
             ARRANQUE, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio en Re mayor · el arpegio, en corcheas',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave hay dos sostenidos: Fa y Do van a la tecla negra.',
            'Compás de 3/4: es un vals, y de los lentos.',
            'La derecha hace una blanca con puntillo por compás: tres tiempos, una nota.',
            'La izquierda hace seis corcheas por compás, sin parar.',
            'Encima del pentagrama van las letras de acorde.',
            'Debajo hay dos estrofas de letra: "Wise men say" y "Shall I stay".',
        ],
        reto='Que la izquierda no acelere. Cuando la derecha aguanta una nota larga, la mano que se '
             'mueve se queda sin referencia y tiende a comerse el compás.',
        truco='Estudia la izquierda sola con el metrónomo a la NEGRA, no a la corchea. Con seis '
              'corcheas por compás y tres golpes, cada golpe cae en una corchea de cada dos: si te '
              'sales, se oye inmediatamente.',
        sabias='La melodía no es de los años sesenta: es "Plaisir d\'amour", que escribió '
               'Jean-Paul-Égide Martini en 1784. Elvis la grabó casi doscientos años después y '
               'desde entonces casi nadie recuerda de dónde venía.',
        qr=dict(titulo='Escúchala',
                texto='Escucha solo la mano izquierda: son corcheas iguales de principio a fin. Esa '
                      'regularidad es lo que sostiene la canción entera.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Aquí el orden no es opinable: primero la izquierda sola hasta que vaya sin pensar, y '
              'solo después la melodía encima. Al revés no se sostiene.',
        reglas=['LA IZQUIERDA, PRIMERO Y SOLA', 'EL METRÓNOMO A LA NEGRA, NO A LA CORCHEA',
                'LA DERECHA AGUANTA LOS TRES TIEMPOS'],
        bloques=[
            dict(num=1, titulo='El arpegio de la izquierda',
                 pista='andamio en Re mayor · es el dibujo que hace tu partitura, con las notas del '
                       'acorde de Re',
                 sistemas=[
                     dict(cap='a) el acorde de Re desplegado, subiendo y bajando · en corcheas',
                          events=corch(['D3', 'F#3']) + corch(['A3', 'D4']) + corch(['A3', 'F#3']),
                          matiz='mp',
                          bars=1, clef='bass'),
                     dict(cap='b) y dos compases seguidos, sin parar entre ellos · el hueco entre '
                              'compás y compás es donde todo el mundo respira, y aquí no se puede',
                          events=corch(['D3', 'F#3']) + corch(['A3', 'D4']) +
                                 corch(['A3', 'F#3']) + corch(['D3', 'F#3']) +
                                 corch(['A3', 'D4']) + corch(['A3', 'F#3']),
                          bars=2, clef='bass', show_time=False),
                     dict(cap='c) y cambiando de acorde, que es lo que pasa de verdad · de Re a Sol',
                          events=corch(['D3', 'F#3']) + corch(['A3', 'F#3']) +
                                 corch(['A3', 'D4']) + corch(['G2', 'B2']) +
                                 corch(['D3', 'G3']) + corch(['D3', 'B2']),
                          bars=2, clef='bass', show_time=False),
                     dict(cap='d) y con la mano abierta hasta la octava, que es donde llega tu '
                              'partitura en la segunda línea',
                          events=corch(['D3', 'A3']) + corch(['D4', 'A3']) +
                                 corch(['F#3', 'D3']) + corch(['A2', 'D3']) +
                                 corch(['F#3', 'D3']) + corch(['A2', 'D3']),
                          bars=2, clef='bass', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL METRÓNOMO VA A LA NEGRA',
                 texto='Si lo pones a la corchea tienes un golpe por nota y no te puedes salir: el '
                       'aparato toca por ti. Puesto a la negra hay tres golpes y seis notas, así '
                       'que cada golpe cae en una corchea de cada dos y las otras tres las tienes '
                       'que colocar tú. Ahí es donde se ve si la mano va regular o solo lo parece.'),
            dict(num=2, titulo='La melodía, que no hace casi nada',
                 pista='cc. 1–2 · MEDIDOS en tu partitura, una nota por compás',
                 sistemas=[
                     dict(cap='a) los cuatro primeros compases, con la nota larga de cada uno · '
                              'los dos primeros están MEDIDOS y los otros dos son andamio',
                          events=[n('D4', 'h.'), n('A4', 'h.'), n('B4', 'h.'), n('A4', 'h.')],
                          bars=4),
                     dict(cap='b) y contando los tres tiempos en voz alta, con la nota partida · en '
                              'tu partitura es UNA blanca con puntillo, no tres negras',
                          events=[n('D4'), n('D4'), n('D4'), n('A4'), n('A4'), n('A4')],
                          bars=2, show_time=False),
                     dict(cap='c) y la frase un poco más larga, con la nota de cada compás cambiando',
                          events=[n('D4', 'h.'), n('A4', 'h.'), n('A4', 'h.'), n('F#4', 'h.')],
                          bars=4, show_time=False),
                     dict(cap='d) y ahora las mismas alturas repartidas en tres negras cada una · '
                              'es solo para contar: en tu partitura son notas de tres tiempos',
                          events=[n('D4'), n('D4'), n('D4'), n('A4'), n('A4'), n('A4'),
                                  n('B4'), n('B4'), n('B4'), n('A4'), n('A4'), n('A4')],
                          bars=4, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, por fin',
                 pista='andamio · la derecha del compás 1 MEDIDA, con el arpegio debajo',
                 sistemas=[
                     dict(cap='a) el compás 1: la nota larga arriba y las seis corcheas debajo',
                          events=[ac(('D3', 'D4'), 'e'), ac(('F#3',), 'e'), ac(('A3',), 'e'),
                                  ac(('D4',), 'e'), ac(('A3',), 'e'), ac(('F#3',), 'e')],
                          bars=1, manos='dobla'),
                     dict(cap='b) y los compases 1 y 2 seguidos, que ya son media frase',
                          events=[ac(('D3', 'D4'), 'e'), ac(('F#3',), 'e'), ac(('A3',), 'e'),
                                  ac(('D4',), 'e'), ac(('A3',), 'e'), ac(('F#3',), 'e'),
                                  ac(('D3', 'A4'), 'e'), ac(('F#3',), 'e'), ac(('A3',), 'e'),
                                  ac(('D4',), 'e'), ac(('A3',), 'e'), ac(('F#3',), 'e')],
                          bars=2, manos='dobla', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Cuatro compases, no más. Izquierda sola con metrónomo, derecha sola '
                       'contando los tres tiempos, y las dos juntas muy despacio. Cuando los cuatro '
                       'salgan tres veces seguidas sin parar, coge los cuatro siguientes. La pieza '
                       'entera se monta así, de cuatro en cuatro, y no de arriba abajo.'),
        ] + bloques_extra('Re mayor', 87, 'D4', 'D3',
                          'la izquierda en corcheas sin parar mientras la derecha aguanta',
                          desde=4, time_sig=(3, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina="Can't Help · para casa",
            intro='Veinte minutos al día, y los diez primeros para la izquierda sola. Es lo que más '
                  'rinde de todo el cuaderno y lo que más cuesta hacer.',
            bloques=[
                reto('Que la izquierda mantenga las seis corcheas iguales durante cuatro compases '
                     'seguidos, con la derecha encima.',
                     'Metrónomo a la NEGRA (tres golpes por compás), y la izquierda sola hasta que '
                     'te aburra. Solo entonces añades la melodía.'),
                plan((10, 'La izquierda sola, con metrónomo a la negra'),
                     (3, 'La derecha sola, contando los tres tiempos en voz alta'),
                     (4, 'Los cuatro primeros compases con las dos manos'),
                     (3, 'Los mismos cuatro, un escalón más rápido')),
                objetivo('Que en los cuatro primeros compases la izquierda no cambie de velocidad '
                         'cuando entra la derecha. Es lo único que se mira esta semana.'),
                teclado({2: 1, 6: 2, 9: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         '¿Cuál de las tres NO está en el acorde de Re mayor?'],
                        titulo='En el teclado',
                        pista='ojo con la armadura: en esta pieza el Fa y el Do van a la negra'),
                ordenar(['Las dos manos juntas, muy despacio.',
                         'La izquierda sola, con metrónomo a la negra.',
                         'Las dos manos, un escalón más rápido.',
                         'La derecha sola, contando los tres tiempos.'],
                        titulo='El orden de los cuatro pasos',
                        pista='numéralos del 1 al 4 · aquí el orden no es opinable'),
                figuras([('h.', 'blanca con puntillo'), ('e', 'corchea'), ('q', 'negra'),
                         ('h', 'blanca')],
                        titulo='¿Cuántos tiempos vale cada una?',
                        pista='y di cuál de las cuatro llena ella sola un compás de 3/4'),
                para_clase('Los cuatro primeros compases con las dos manos y a qué velocidad de '
                           'metrónomo te salen sin que la izquierda se acelere. Ese número es el '
                           'que vamos a mover en clase.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
