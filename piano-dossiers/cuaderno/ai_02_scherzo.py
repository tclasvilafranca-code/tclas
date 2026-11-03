# -*- coding: utf-8 -*-
"""Scherzo, de Diabelli — pieza 2 de Aida. Formato ADULTO exigente.

   La pareja del Romance, y por eso va detras: es la MISMA posicion de mano y
   la misma manera de tocar a cuatro manos, pero a "Allegro" y con staccato.
   Primero se monta la posicion (pieza 1) y despues se le pide velocidad
   (pieza 2). Ese es todo el argumento del principio del album.

   Lo comprobado sobre el PDF de SU carpeta ("Scherzo · 28 Melodic Studies
   op. 149, no. 6", parte del Primo, 2 paginas). Este archivo NO lo tiene
   ningun otro alumno:

     - Do mayor: detras de la clave no hay nada.
     - 3/4, y arriba pone "Allegro". No trae numero de metronomo.
     - Los dos pentagramas del Primo van en clave de sol y traen lo mismo; el
       de arriba lleva 8va. Debajo pone "p" y hay reguladores.
     - STACCATO impreso encima de casi todas las negras: es lo que separa esta
       pieza del Romance, que iba "sempre legato".

   LAS ALTURAS, medidas a 300 ppp sobre el pentagrama de arriba del Primo
   (apertura morfologica; los puntos de staccato no sobreviven a la apertura,
   asi que no se cuelan como cabezas):

       c. 1   Mi5 · Fa5 (dos corcheas ligadas por su barra) · Sol5 · Sol5
       c. 2   Sol5 · Sol5 · Sol5      tres negras

   Las dos sumas cierran en tres tiempos: 0,5 + 0,5 + 1 + 1 y 1 + 1 + 1.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ai_comun import (n, ac, sil, corch, plan, a_cuatro_manos, escalera,
                      contar, teclado, para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def _st(ev):
    """La misma nota, con el punto de staccato que trae la partitura."""
    d = dict(ev)
    d['art'] = 'staccato'
    return d


# El compas 1 del Primo, medido. Cita literal, con su staccato impreso.
ARRANQUE = corch(['E5', 'F5']) + [_st(n('G5')), _st(n('G5'))]

# El compas 2, medido: tres negras iguales, las tres con staccato.
SEGUNDO = [_st(n('G5')), _st(n('G5')), _st(n('G5'))]

CANCION = dict(
    alumno='Aída', carpeta='Aida', num=2, nivel='intermedio',
    slug='ScherzoDiabelli', formato='adulto',
    titulo_corto='Scherzo · Diabelli', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'aida', 'source',
                           'Scherzo Diabelli 4 manos.pdf'),
    yt='https://www.youtube.com/results?search_query=diabelli+op+149+no+6+scherzo+piano+4+hands',

    ficha=dict(
        titulo='Scherzo',
        autor='Anton Diabelli · 28 Estudios melódicos, op. 149 nº 6 · parte del Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'Allegro'), ('Ataque', 'Staccato'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Los dos primeros compases, medidos',
        pie_ritmos='Medido en tu partitura, a 300 puntos por pulgada. Los puntos encima de las '
                   'notas son los que trae tu edición: staccato, o sea corto y suelto.',
        armonia=dict(
            titulo='La misma mano que el Romance, y todo lo contrario',
            tarjetas=[
                ('LA MISMA POSICIÓN', 'Cinco dedos',
                 'Sigues sin mover la mano de sitio. Lo único que ha cambiado desde la pieza 1 es '
                 'lo que se le pide a los dedos.'),
                ('STACCATO', 'Corto y suelto',
                 'El punto encima de la nota dice que se levanta enseguida. No es tocar más fuerte '
                 'ni más rápido: es soltar antes.'),
                ('ALLEGRO', 'Sin número',
                 'Tu partitura pone "Allegro" y no da metrónomo, así que la velocidad la decides '
                 'tú. Los números de la escalera de esta semana son de trabajo, no de la edición.'),
                ('DOS CORCHEAS', 'Y a correr',
                 'El compás 1 arranca con dos corcheas unidas por su barra y sigue con dos negras. '
                 'Esas dos corcheas son la firma de la pieza: vuelven una y otra vez.'),
            ],
            pie='Un "scherzo" es literalmente una broma. Diabelli lo escribió dentro de una '
                'colección de estudios, así que es a la vez ejercicio y música: exactamente lo que '
                'hace falta en la segunda semana de un curso.',
        ),
        ritmos=[
            ('COMPÁS 1', 'medido · dos corcheas y dos negras sueltas',
             ARRANQUE, OCRE, 'treble', None),
            ('COMPÁS 2', 'medido · tres negras iguales, las tres en staccato',
             SEGUNDO, AZUL, 'treble', None),
        ],
        especial=[
            'No hay ni un sostenido ni un bemol: todo teclas blancas.',
            'Arriba pone "Allegro", pero no viene ningún número de metrónomo.',
            'Casi todas las negras llevan un punto encima: staccato.',
            'Los dos pentagramas del Primo llevan clave de sol y traen lo mismo.',
            'Encima del pentagrama de arriba hay un 8va.',
            'Debajo del pentagrama hay reguladores: el sonido crece y baja.',
        ],
        reto='Que el staccato no se convierta en un golpe. Cuando se sube la velocidad, el dedo '
             'tiende a atacar más fuerte en vez de soltar antes, y la pieza se vuelve dura.',
        truco='Toca la nota y cuenta en voz alta hasta dos con la tecla ya levantada. Si tienes que '
              'esperar, es que la has soltado a tiempo. El staccato lo hace el silencio de después, '
              'no el golpe de antes.',
        sabias='Los "28 estudios melódicos" de Diabelli están escritos a cuatro manos a propósito: '
               'el alumno toca una posición fija y el profesor pone debajo la armonía que la '
               'convierte en música. Es la misma idea que usan hoy los métodos modernos.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en lo cortas que suenan las negras. Ese aire de broma es el staccato, '
                      'no la velocidad.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='La posición ya la montaste la semana pasada. Esta semana se trabaja el ataque: '
              'cómo se suelta la tecla, que es lo que hace que un Allegro suene ligero y no duro.',
        reglas=['LA MANO SIGUE SIN MOVERSE', 'EL STACCATO SE HACE SOLTANDO, NO PEGANDO',
                'PRIMERO CORTO, DESPUÉS RÁPIDO'],
        bloques=[
            dict(num=1, titulo='Soltar la tecla, sin prisa',
                 pista='andamio en Do mayor · a media velocidad, para que dé tiempo a sentir el '
                       'momento en que el dedo se va',
                 sistemas=[
                     dict(cap='a) las cinco teclas de la posición, todas sueltas · levanta el dedo '
                              'nada más sonar la nota',
                          events=[_st(n('C4')), _st(n('D4')), _st(n('E4')),
                                  _st(n('F4')), _st(n('G4')), _st(n('F4'))],
                          matiz='p',
                          bars=2),
                     dict(cap='b) y ahora alternando: una suelta y una ligada · la diferencia '
                              'tiene que oírse sin mirar el papel',
                          events=[_st(n('G4')), n('F4'), _st(n('E4')),
                                  n('D4'), _st(n('C4')), n('D4')],
                          bars=2, show_time=False),
                     dict(cap='c) y en corcheas, que es como entra la célula de la pieza · las '
                              'dos primeras van ligadas y las dos negras de detrás, sueltas',
                          events=[n('C4', 'e'), n('D4', 'e'), _st(n('E4')), _st(n('E4')),
                                  n('D4', 'e'), n('E4', 'e'), _st(n('F4')), _st(n('F4'))],
                          bars=2, show_time=False),
                     dict(cap='d) y lo mismo con la izquierda sola, en su clave · esta mano se '
                              'queda dura antes que la otra',
                          events=[n('C3', 'e'), n('D3', 'e'), _st(n('E3')), _st(n('E3')),
                                  n('D3', 'e'), n('E3', 'e'), _st(n('F3')), _st(n('F3'))],
                          bars=2, clef='bass', show_time=False),
                     dict(cap='e) y subiendo la posición con el sonido creciendo · así se lee el '
                              'regulador que tu edición trae debajo del pentagrama',
                          events=[dict(n('C4'), cresc=5), n('D4'), n('E4'),
                                  n('F4'), n('G4'), n('C5')],
                          bars=2, show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='QUÉ ES DE VERDAD UN STACCATO',
                 texto='No es tocar fuerte ni tocar deprisa: es acortar la nota. La tecla suena lo '
                       'mismo y se levanta antes, así que lo que cambia es el SILENCIO que queda '
                       'detrás. Por eso el staccato se estudia despacio: a velocidad lenta el '
                       'silencio se oye y se puede medir; a velocidad de concierto ya no da tiempo '
                       'a corregirlo, solo a repetir lo que salga.'),
            dict(num=2, titulo='Los dos primeros compases, como están escritos',
                 pista='cc. 1–2 · MEDIDOS en tu partitura, con su staccato',
                 sistemas=[
                     dict(cap='a) el compás 1 con las cuatro notas en negras, para colocar las '
                              'alturas · en tu partitura las dos primeras son corcheas',
                          events=[n('E5'), n('F5'), _st(n('G5')), _st(n('G5')),
                                  n('E5'), n('F5')],
                          bars=2),
                     dict(cap='b) y ahora con su figura de verdad, los dos compases seguidos',
                          events=list(ARRANQUE) + list(SEGUNDO),
                          bars=2, show_time=False),
                     dict(cap='c) y el mismo par de compases repetido, que es como se estudia una '
                              'célula: dos veces seguidas y sin parar entre medias',
                          events=list(ARRANQUE) + list(SEGUNDO) + list(ARRANQUE) + list(SEGUNDO),
                          bars=4, show_time=False),
                 ]),
            dict(num=3, titulo='Las dos manos, a la octava',
                 pista='andamio · las dos hacen lo mismo, igual que en el Romance',
                 sistemas=[
                     dict(cap='a) la célula de dos corcheas con las dos manos · si una suelta '
                              'antes que la otra, se oye enseguida',
                          events=[ac(('C3', 'C4'), 'e'), ac(('D3', 'D4'), 'e'),
                                  _st(ac(('E3', 'E4'))), _st(ac(('E3', 'E4'))),
                                  ac(('D3', 'D4'), 'e'), ac(('E3', 'E4'), 'e'),
                                  _st(ac(('F3', 'F4'))), _st(ac(('F3', 'F4')))],
                          bars=2, manos='dobla'),
                     dict(cap='b) y con las tres negras sueltas detrás, que es el compás 2',
                          events=[_st(ac(('E3', 'E4'))), _st(ac(('E3', 'E4'))),
                                  _st(ac(('E3', 'E4'))),
                                  _st(ac(('C3', 'C4'))), _st(ac(('C3', 'C4'))),
                                  _st(ac(('C3', 'C4')))],
                          bars=2, manos='dobla', show_time=False),
                     dict(cap='c) y la vuelta entera: célula, tres negras y a empezar · cuatro '
                              'compases seguidos, que es la unidad con la que se estudia',
                          events=[ac(('C3', 'C4'), 'e'), ac(('D3', 'D4'), 'e'),
                                  _st(ac(('E3', 'E4'))), _st(ac(('E3', 'E4'))),
                                  _st(ac(('D3', 'D4'))), _st(ac(('D3', 'D4'))),
                                  _st(ac(('D3', 'D4'))),
                                  ac(('E3', 'E4'), 'e'), ac(('F3', 'F4'), 'e'),
                                  _st(ac(('G3', 'G4'))), _st(ac(('G3', 'G4'))),
                                  _st(ac(('C3', 'C4'), 'h.'))],
                          bars=4, manos='dobla', show_time=False),
                 ]),
            dict(tipo='nota',
                 etiqueta='Y AHORA A LA PARTITURA',
                 texto='Coge la primera línea entera y tócala tres veces: la primera muy despacio y '
                       'toda ligada, la segunda igual de despacio pero con el staccato puesto, y la '
                       'tercera un escalón más rápida. Si en la tercera el staccato se pierde, no '
                       'subas: el orden es corto primero y rápido después, nunca al revés.'),
        ] + bloques_extra('Do mayor', 82, 'C5', 'C3',
                          'el staccato: la nota se acorta soltando, no pegando',
                          desde=4, time_sig=(3, 4), mas=True),
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Scherzo · para casa',
            intro='Veinte minutos al día. La posición ya la tienes: esta semana se gana o se pierde '
                  'en cómo sueltas la tecla.',
            bloques=[
                plan((5, 'Las cinco teclas sueltas, muy despacio'),
                     (5, 'Los compases 1 y 2, con su staccato'),
                     (5, 'La primera línea, primero ligada y después suelta'),
                     (5, 'Las dos manos a la octava, con la célula de corcheas')),
                a_cuatro_manos('El Secondo lleva acordes en el "y" de cada tiempo, así que si tú '
                               'alargas las negras, choca. Acordad en clase quién marca el pulso: '
                               'en esta pieza es más fácil que lo lleve la parte de abajo.'),
                escalera((60, 'los compases 1 y 2 con el staccato bien corto'),
                         (76, 'la primera línea entera, sin parar'),
                         (92, 'la primera línea con las dos manos'),
                         meta='que a la velocidad más alta el staccato siga sonando corto · tu '
                              'partitura pone "Allegro" pero NO trae número de metrónomo, así que '
                              'estos tres números son de trabajo',
                         notas=['Si al subir un escalón las notas se alargan, baja y quédate ahí.']),
                contar(list(ARRANQUE) + list(SEGUNDO),
                       ['¿Cuántas notas llevan punto de staccato?',
                        '¿Cuántas corcheas hay?',
                        '¿Cuántas veces se repite el Sol?'],
                       titulo='Cuenta sobre tus dos primeros compases',
                       pista='son los cc. 1 y 2 medidos, tal y como están impresos'),
                teclado({4: 1, 5: 2, 6: 3},
                        ['Escribe el nombre de las tres teclas marcadas.',
                         '¿Cuál de las tres se repite más veces en tus dos primeros compases?'],
                        titulo='En el teclado',
                        pista='son las tres notas de tus dos primeros compases'),
                para_clase('La primera línea a la velocidad más alta que te salga con el staccato '
                           'todavía corto. Dime también cuál es esa velocidad: la vamos a usar para '
                           'decidir la de las dos partes juntas.'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
