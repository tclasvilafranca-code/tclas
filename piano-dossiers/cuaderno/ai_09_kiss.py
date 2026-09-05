# -*- coding: utf-8 -*-
"""Kiss the Rain — pieza 9 de Aida. Formato ADULTO exigente.

   Cierra la etapa del acompañamiento y es la primera pieza del cuaderno con
   SEMICORCHEAS impresas. Va aqui y no mas tarde porque las semicorcheas que
   trae son de las faciles: tres seguidas, dentro de un solo tiempo y despues
   de tres compases... no, de tres TIEMPOS de silencio. El resto de la pieza
   respira mucho.

   Lo comprobado sobre el PDF de SU carpeta (Musescore, 2 paginas). Este
   archivo NO lo tiene ningun otro alumno:

     - Detras de la clave no hay nada.
     - 4/4, y no trae numero de metronomo: la casilla se llama "Caracter".
     - Las DOS manos empiezan calladas: la derecha con un silencio de blanca
       con puntillo y la izquierda con un silencio de redonda.
     - Del c. 2 en adelante la izquierda hace corcheas en arpegio.

   LAS ALTURAS del compas 1, medidas a 300 ppp:

       c. 1   silencio de blanca con puntillo   (tres tiempos callada)
              silencio de semicorchea
              Sol4 · Do5 · Re5                  tres semicorcheas

   La suma cierra: 3 + 0,25 + 0,25 + 0,25 + 0,25 = 4. Y la aritmetica es aqui
   la prueba de que son semicorcheas y no corcheas: con corcheas el compas se
   iria a 5,5 tiempos.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, semi, reto, plan, escalera, contar,
                      rodear, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')

# El compas 1 de la DERECHA, medido. Cita literal.
ARRANQUE = [sil('h.'), sil('s')] + semi(['G4', 'C5', 'D5'])

# La izquierda del c. 2 en adelante: arpegio en corcheas. ANDAMIO en Do mayor.
BAJO = corch(['C3', 'G3']) + corch(['C4', 'G3']) + corch(['E3', 'G3']) + corch(['C4', 'G3'])

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=9, nivel='intermedio',
    slug='KissTheRain', formato='adulto',
    titulo_corto='Kiss the Rain', time_sig=(4, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source', 'Kiss the Rain.pdf'),
    yt='https://www.youtube.com/results?search_query=yiruma+kiss+the+rain+piano+easy',

    ficha=dict(
        titulo='Kiss the Rain',
        autor='Yiruma · Lee Ru-ma',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '4/4'),
               ('Carácter', 'Sin marcar'), ('Empieza', 'En el cuarto tiempo'),
               ('Figura', 'Semicorchea')],
        titulo_ritmos='El compás 1, y el arpegio que viene después',
        pie_ritmos='Arriba, el compás 1 de la derecha MEDIDO en tu partitura: tres tiempos callada '
                   'y tres semicorcheas. Abajo, andamio en Do mayor con el arpegio en corcheas que '
                   'la izquierda hace del compás 2 en adelante.',
        armonia=dict(
            titulo='La primera semicorchea del cuaderno',
            tarjetas=[
                ('TRES TIEMPOS', 'Calladas las dos',
                 'La pieza empieza con las dos manos en silencio: tres tiempos enteros. Lo primero '
                 'que se estudia aquí es esperar.'),
                ('LA SEMICORCHEA', 'La mitad de media',
                 'Tres seguidas en el último tiempo. Una semicorchea es la mitad de una corchea: '
                 'cuatro caben en un tiempo, y aquí van tres y un silencio.'),
                ('LA IZQUIERDA', 'Arpegio',
                 'Del compás 2 en adelante, corcheas que dibujan el acorde por dentro. Es la misma '
                 'idea que en Can\'t Help, pero con la mano más abierta.'),
                ('SIN METRÓNOMO', 'Lo eliges tú',
                 'No trae número. Es una pieza lenta y con mucho pedal: la velocidad la marca el '
                 'sitio donde respira, no el reloj.'),
            ],
            pie='Que la primera semicorchea del curso llegue en la pieza 9 y no antes es una '
                'decisión: aquí van tres, en un solo tiempo, y con tres tiempos de silencio delante '
                'para prepararlas. Cuando lleguen las de A comme amour, en la 19, no habrá silencio '
                'ninguno.',
        ),
        ritmos=[
            ('MANO DERECHA', 'el compás 1, MEDIDO · tres semicorcheas al final',
             ARRANQUE, OCRE, 'treble', None),
            ('MANO IZQUIERDA', 'andamio en Do mayor · el arpegio en corcheas',
             BAJO, AZUL, 'bass', None),
        ],
        especial=[
            'Detrás de la clave no hay ni un sostenido ni un bemol.',
            'Las dos manos empiezan calladas: tres tiempos de silencio.',
            'El compás 1 acaba con tres semicorcheas seguidas.',
            'Del compás 2 en adelante la izquierda hace corcheas en arpegio.',
            'No viene ningún número de metrónomo.',
            'Son dos páginas.',
        ],
        reto='Que las tres semicorcheas del final del compás 1 quepan dentro de UN tiempo. La '
             'tentación es darles un tiempo a cada una, y entonces el compás se va a siete.',
        truco='Cuenta el compás entero en semicorcheas para ese último tiempo: "cua-ti-te-ta". Tú '
              'entras en la "ti" y tocas "ti-te-ta". Cuatro sílabas por tiempo es la única manera '
              'de que la mano sepa cuánto dura de verdad una semicorchea.',
        sabias='Yiruma la escribió en 2003 mirando llover por la ventana de un hotel, y la registró '
               'sin pensar que fuera a salir del disco. Es la pieza de piano más buscada en internet '
               'de todo el repertorio contemporáneo.',
        qr=dict(titulo='Escúchala',
                texto='Cuenta tres tiempos desde el silencio del principio. Las tres notas rápidas '
                      'con las que entra la melodía son tus semicorcheas.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Dos cosas nuevas, y las dos se estudian contando: tres tiempos de espera y una '
              'figura que dura un cuarto de tiempo. Ninguna de las dos es de dedos.',
        reglas=['CUENTA EN SEMICORCHEAS: "UN-TI-TE-TA"', 'TRES TIEMPOS CALLADA, Y ENTRAS',
                'LAS TRES RÁPIDAS CABEN EN UN TIEMPO'],
        bloques=[
            dict(num=1, titulo='Cuánto dura una semicorchea',
                 pista='andamio en Do mayor · la misma nota en cuatro figuras, de larga a corta',
                 sistemas=[
                     dict(cap='a) una redonda, dos blancas, cuatro negras · el compás entero cada vez',
                          events=[n('C5', 'w'), n('C5', 'h'), n('C5', 'h'),
                                  n('C5'), n('C5'), n('C5'), n('C5')],
                          matiz='mp',
                          bars=3),
                     dict(cap='b) ocho corcheas, y después dieciséis semicorcheas · el doble de '
                              'notas en el mismo compás',
                          events=corch(['C5', 'D5']) + corch(['E5', 'D5']) + corch(['C5', 'D5']) +
                                 corch(['E5', 'D5']) + semi(['C5', 'D5', 'E5', 'D5']) +
                                 semi(['C5', 'D5', 'E5', 'D5']) + semi(['C5', 'D5', 'E5', 'D5']) +
                                 semi(['C5', 'D5', 'E5', 'D5']),
                          bars=2, show_time=False),
                     dict(cap='c) y ahora tres semicorcheas y un silencio, que es lo que trae tu '
                              'compás 1 · "ti-te-ta" y callar',
                          events=(semi(['G4', 'C5', 'D5']) + [sil('s')] +
                                  semi(['G4', 'C5', 'D5']) + [sil('s')] +
                                  semi(['G4', 'C5', 'D5']) + [sil('s')] +
                                  semi(['G4', 'C5', 'D5']) + [sil('s')]),
                          bars=1, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ LA ARITMÉTICA DECIDE LA FIGURA',
                 texto='En el compás 1 hay tres tiempos de silencio y tres notas rápidas. Si esas '
                       'tres fueran corcheas, el compás sumaría 3 + 1,5 = 4,5 tiempos, y un compás '
                       'de 4/4 no puede sumar cuatro y medio. Con semicorcheas suma 3 + 0,75 más el '
                       'silencio de semicorchea que llevan delante: exactamente 4. Cuando una '
                       'figura no se distinga a la vista, súmala: un compás bien escrito siempre '
                       'cierra, y eso te dice cuál es.'),
            dict(num=2, titulo='El compás 1, tal y como está escrito',
                 pista='c. 1 · MEDIDO en tu partitura, con sus tres tiempos de silencio',
                 sistemas=[
                     dict(cap='a) el compás 1 con el silencio partido en tres negras, para contarlo '
                              '· en tu partitura es UN silencio de blanca con puntillo',
                          events=[sil('q'), sil('q'), sil('q'), sil('s')] +
                                 semi(['G4', 'C5', 'D5']),
                          bars=1),
                     dict(cap='b) y con el compás 2 detrás · la melodía sigue y ya no para',
                          events=list(ARRANQUE) + corch(['E5', 'D5']) + [n('C5', 'h'), n('D5')],
                          bars=2, show_time=False),
                     dict(cap='c) y la entrada tres veces seguidas, para que la mano la encuentre '
                              'sin pensar',
                          events=([sil('h.'), sil('s')] + semi(['G4', 'C5', 'D5']) +
                                  [sil('h.'), sil('s')] + semi(['G4', 'C5', 'E5']) +
                                  [sil('h.'), sil('s')] + semi(['G4', 'D5', 'E5'])),
                          bars=3, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, con el arpegio debajo',
                 pista='andamio en Do mayor · el arpegio es el dibujo que hace tu izquierda',
                 sistemas=[
                     dict(cap='a) el arpegio solo, dos compases · ocho corcheas por compás y sin '
                              'parar entre ellos',
                          events=(corch(['C3', 'G3']) + corch(['E4', 'G3']) +
                                  corch(['C4', 'G3']) + corch(['E3', 'G3']) +
                                  corch(['C3', 'E3']) + corch(['G3', 'C4']) +
                                  corch(['E4', 'C4']) + corch(['G3', 'E3'])),
                          bars=2, clef='bass'),
                     dict(cap='b) y con el acorde cambiando, que es lo que pasa cada compás',
                          events=corch(['C3', 'G3']) + corch(['C4', 'G3']) +
                                 corch(['A2', 'E3']) + corch(['A3', 'E3']),
                          bars=1, clef='bass', show_time=False),
                     dict(cap='c) y las dos manos: la melodía entrando encima del arpegio',
                          events=[ac(('C3', 'G3'), 'e'), ac(('C4',), 'e'), ac(('E3',), 'e'),
                                  ac(('C4',), 'e'), ac(('C3', 'C5'), 'e'), ac(('G3',), 'e'),
                                  ac(('E3', 'D5'), 'e'), ac(('G3',), 'e')],
                          bars=1, manos='dobla', show_time=False),
                     dict(cap='d) y dos compases con el arpegio cambiando de acorde debajo de la '
                              'melodía · es lo que hace tu partitura del compás 2 en adelante',
                          events=[ac(('C3', 'G3'), 'e'), ac(('C4',), 'e'),
                                  ac(('E3', 'E5'), 'e'), ac(('C4',), 'e'),
                                  ac(('C3', 'D5'), 'e'), ac(('G3',), 'e'),
                                  ac(('E3', 'C5'), 'e'), ac(('G3',), 'e'),
                                  ac(('A2', 'E3'), 'e'), ac(('A3',), 'e'),
                                  ac(('E3', 'C5'), 'e'), ac(('A3',), 'e'),
                                  ac(('A2', 'D5'), 'e'), ac(('E3',), 'e'),
                                  ac(('A3', 'C5'), 'e'), ac(('E3',), 'e')],
                          bars=2, manos='dobla', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Cuatro compases, contando en semicorcheas todo el rato. Y una advertencia: '
                       'esta pieza pide pedal, y el pedal tapa los errores de duración. Estudia los '
                       'cuatro compases SIN pedal hasta que las semicorcheas suenen iguales; '
                       'ponerlo antes es taparte los oídos a ti misma.'),
        ] + bloques_extra('Do mayor', 97, 'C5', 'C3',
                          'tres semicorcheas dentro de un solo tiempo, después de tres callados',
                          desde=4, time_sig=(4, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Kiss the Rain · para casa',
            intro='Quince minutos al día, y el metrónomo puesto. La figura nueva de esta semana no '
                  'se aprende de oído: se cuenta.',
            bloques=[
                reto('Que las tres semicorcheas del compás 1 quepan dentro de un solo tiempo.',
                     'Cuenta ese tiempo en cuatro: "cua-ti-te-ta". Entras en la "ti" y tocas tres. '
                     'Si te sale un compás de cinco tiempos, es que les has dado un tiempo a cada '
                     'una.'),
                plan((4, 'Contar en semicorcheas, sin tocar: "un-ti-te-ta dos-ti-te-ta..."'),
                     (4, 'El compás 1: tres tiempos callada y las tres notas rápidas'),
                     (4, 'El arpegio de la izquierda, en corcheas'),
                     (3, 'Los dos primeros compases con las dos manos')),
                escalera((54, 'el compás 1 solo, con las tres semicorcheas iguales'),
                         (66, 'los dos primeros compases con las dos manos'),
                         (78, 'los cuatro primeros, sin parar'),
                         meta='que las tres semicorcheas suenen iguales a la velocidad más alta · '
                              'tu partitura NO trae número de metrónomo, así que estos son de '
                              'trabajo',
                         notas=['Si al subir la última se te queda corta, baja un escalón.']),
                contar(list(ARRANQUE),
                       ['¿Cuántos tiempos dura el silencio del principio?',
                        '¿Cuántas semicorcheas hay?',
                        '¿Cuántas semicorcheas caben en un tiempo?'],
                       titulo='Cuenta sobre tu compás 1',
                       pista='es el compás 1 medido, tal y como está impreso'),
                rodear([[sil('h.'), sil('s')] + semi(['G4', 'C5', 'D5']),
                        [sil('h.'), sil('s')] + semi(['G4', 'C5', 'D5']),
                        [sil('h.'), sil('e')] + semi(['G4', 'C5', 'D5']),
                        [sil('h.'), sil('s')] + semi(['G4', 'C5', 'E5'])],
                       titulo='Rodea los dos compases que son iguales',
                       pista='uno de los dos es tu compás 1 · fíjate en el silencio pequeño'),
                para_clase('Los dos primeros compases con las dos manos y sin pedal. El pedal lo '
                           'ponemos en clase: antes hay que oír si las semicorcheas están donde '
                           'tienen que estar.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
