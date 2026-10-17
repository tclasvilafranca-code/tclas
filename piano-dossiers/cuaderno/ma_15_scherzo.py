# -*- coding: utf-8 -*-
"""Scherzo, de Diabelli (op. 149 nº 6) — pieza 15 de Martina (dueto). ADULTO exigente,
   tono de niña.

   Lo comprobado sobre el PDF de su carpeta de Drive ("Scherzo · 28 Melodic Studies
   op. 149, no. 6", 2 páginas, vectorial, 206 ppp), medido con las líneas del
   pentagrama a 300 ppp y mirado a 200 ppp:

     - Do mayor en el Scherzo: detrás de la clave no hay nada. 3/4. Pone
       "Allegro" y no trae número de metrónomo. 48 compases en dos páginas.
     - A cuatro manos. El PRIMO (arriba) lleva sus dos pentagramas en clave de sol y
       el de arriba lleva un 8va encima. El SECONDO (abajo) lleva clave de sol y de fa.
     - Intensidad escrita: p al principio, f en el c. 9, p en el c. 17 y reguladores
       (abre en el c. 2, cierra en los cc. 3 y 4).
     - Staccato impreso sobre casi todas las negras; acento encima de la blanca de los
       cc. 11 y 12; una pareja de notas pequeñas de adorno antes del Fa del c. 14.
     - Barras de repetición al final de los cc. 8, 16, 24 y 32. "Fine" en el c. 32.
     - A partir del c. 33 viene el TRIO, con TRES BEMOLES detrás de la clave, y la partitura
       acaba con "Scherzo D.C. al Fine": se vuelve al principio y se toca hasta el Fine.
     - MEDIDO, Primo (alturas tal como están escritas, con el 8va encima):
       c. 1: Mi5 · Fa5 (corcheas) · Sol5 · Sol5 (negras, staccato)
       c. 2: Sol5 · Sol5 · Sol5 (negras, staccato)
       c. 3: Sol5 (blanca) · Mi5 (negra)
       c. 4: Mi5 (blanca) · Do5 (negra)
       c. 5: Re5 · Mi5 (corcheas) · Fa5 · Fa5 (negras)
       c. 6: Fa5 · Mi5 · Re5 (negras)
       c. 7: Do5 · Re5 (corcheas) · Mi5 · Mi5 (negras)
       c. 8: Mi5 (blanca) · Do5 (negra)
       c. 13: Re5 · Mi5 (corcheas) · Re5 · Re5 (negras)
       c. 14: dos notas de adorno (Re y Mi) y Fa5 · Mi5 · Re5 (negras)
     - El Secondo, en cada compás del Scherzo: silencio de negra y dos acordes de
       negra, con una nota grave en el primer golpe.
   Mismo archivo que el de Aída y el de Alan: lo literal coincide y el andamio va por otros caminos.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from reportlab.lib.colors import HexColor
from cancion import construir
from relleno import bloques_extra
from ma_comun import (n, ac, sil, plan, escalera, a_cuatro_manos, diferencias, nombres,
                      para_clase)

HERE = os.path.dirname(__file__)
AZUL = HexColor('#3E6E8F')
OCRE = HexColor('#8C6A3F')


def st(ev):
    """La misma nota con el punto de staccato que trae la partitura."""
    d = dict(ev)
    d['art'] = 'staccato'
    return d


def ace(ev):
    """La misma nota con el acento que trae la partitura."""
    d = dict(ev)
    d['art'] = 'acento'
    return d


# MEDIDO: Primo, cc. 1-8 (alturas escritas, con el 8va encima)
C1 = [n('E5', 'e'), n('F5', 'e'), st(n('G5')), st(n('G5'))]
C2 = [st(n('G5')), st(n('G5')), st(n('G5'))]
C3 = [n('G5', 'h'), n('E5')]
C4 = [n('E5', 'h'), n('C5')]
C5 = [n('D5', 'e'), n('E5', 'e'), st(n('F5')), st(n('F5'))]
C6 = [st(n('F5')), st(n('E5')), st(n('D5'))]
C7 = [n('C5', 'e'), n('D5', 'e'), st(n('E5')), st(n('E5'))]
C8 = [n('E5', 'h'), n('C5')]
# MEDIDO: cc. 11-12 (acento sobre la blanca) y cc. 13-14 (dos notas de adorno)
C11 = [ace(n('G5', 'h')), st(n('F5'))]
C12 = [ace(n('F5', 'h')), st(n('E5'))]
C13 = [n('D5', 'e'), n('E5', 'e'), st(n('D5')), st(n('D5'))]
C14 = [dict(n('F5'), gracia=['D5', 'E5']), st(n('E5')), st(n('D5'))]

CANCION = dict(
    alumno='Martina', carpeta='Martina', num=15, nivel='intermedio',
    slug='Scherzo', formato='adulto',
    titulo_corto='Scherzo · Diabelli', time_sig=(3, 4), key_sig=None,
    partitura=os.path.join(HERE, '..', 'students', 'martina', 'source', 'Sherzo 4 manos'),
    yt='https://www.youtube.com/results?search_query=diabelli+op+149+no+6+scherzo+piano+4+hands',

    ficha=dict(
        titulo='Scherzo',
        autor='Anton Diabelli · op. 149 nº 6 · a cuatro manos · tu parte es el Primo',
        datos=[('Tonalidad', 'Do mayor'), ('Compás', '3/4'),
               ('Carácter', 'Allegro'), ('Ataque', 'Staccato'),
               ('Se toca', 'Entre dos')],
        titulo_ritmos='Los cc. 1 y 2, medidos, y el Secondo',
        pie_ritmos='Arriba, medido sobre tu partitura (escrito, con el 8va encima): dos corcheas '
                   'y dos negras sueltas, y tres negras iguales. Abajo, andamio: lo que hace el '
                   'Secondo.',
        armonia=dict(
            titulo='Un scherzo con staccato, contrastes y un Trio con tres bemoles',
            tarjetas=[
                ('EL STACCATO', 'Corto y suelto',
                 'Casi todas las negras llevan un punto: se tocan cortas. El staccato no es '
                 'tocar más fuerte ni más deprisa, es soltar la tecla antes.'),
                ('LOS CONTRASTES', 'p y f',
                 'Empieza en p, en el c. 9 salta a f y en el c. 17 vuelve a p. Los reguladores '
                 'abren y cierran dentro de las frases: la música respira.'),
                ('EL TRIO', 'Tres bemoles',
                 'En el c. 33 la partitura cambia: aparecen tres bemoles detrás de la clave y '
                 'todos los Si, Mi y La suenan a la tecla negra. Dura 16 compases.'),
                ('EL FINAL', 'D.C. al Fine',
                 'Al acabar el Trio pone "Scherzo D.C. al Fine": se vuelve al principio y se toca '
                 'hasta el compás donde pone "Fine". Es la parte difícil de leer sin perderse.'),
            ],
            pie='Un scherzo es literalmente una broma, pero esta es larga: 48 compases con dos '
                'partes y una vuelta. Lo que se aprende aquí es a leer la estructura, no solo '
                'las notas.',
        ),
        ritmos=[
            ('MANO DERECHA', 'cc. 1-2 · medido', C1 + C2, OCRE, 'treble', None),
            ('SECONDO', 'andamio · silencio y dos acordes',
             [sil('q'), ac(('E4', 'G4', 'C5')), ac(('E4', 'G4', 'C5'))], AZUL, 'treble', None),
        ],
        especial=[
            'En el Scherzo no hay ni un sostenido ni un bemol: todo teclas blancas.',
            'Arriba pone "Allegro", pero no viene ningún número de metrónomo.',
            'Casi todas las negras llevan un punto de staccato encima.',
            'Empieza en p, salta a f en el c. 9 y vuelve a p en el c. 17.',
            'En el c. 33 empieza el Trio, con tres bemoles detrás de la clave.',
            'Al final pone "D.C. al Fine": se vuelve al principio hasta el Fine.',
        ],
        reto='Que el staccato siga corto cuando sube la velocidad, y que el salto de p a f en el '
             'c. 9 se oiga sin que se acelere ni una negra.',
        truco='Toca la nota y cuenta en voz alta hasta dos con la tecla ya levantada. Para el f, '
              'no pegues más: pesa más con el brazo, deja los dedos igual.',
        sabias='Los "28 estudios melódicos" de Diabelli están escritos a cuatro manos a propósito: '
               'el alumno toca una posición fija y el profesor pone debajo la armonía que la '
               'convierte en música. Anton Diabelli es el mismo de las Variaciones que Beethoven '
               'escribió sobre un vals suyo.',
        qr=dict(titulo='Escúchala',
                texto='Fíjate en lo cortas que suenan las negras y en cómo cambia el color al '
                      'llegar al Trio. Con tres bemoles, el mismo piano suena distinto.'),
    ),

    calentamiento=dict(),
    agudeza=dict(),

    piano1=dict(
        titulo='Cómo se estudia',
        esquina='Al piano · el orden de estudio',
        intro='Se estudia el Scherzo antes del Trio, y el Trio antes de la vuelta. El staccato se '
              'prepara despacio, soltando la tecla; la velocidad llega al final.',
        reglas=['EL STACCATO SE HACE SOLTANDO', 'DEL p AL f SIN CORRER',
                'EL TRIO TIENE TRES BEMOLES'],
        bloques=[
            dict(num=1, titulo='Los dos primeros compases, con su p',
                 pista='cc. 1-2 · medidos sobre tu partitura · tal como está escrito, con el 8va '
                       'encima',
                 sistemas=[
                     dict(cap='a) el c. 1: dos corcheas ligadas y dos negras sueltas · empieza en p',
                          events=[dict(C1[0], matiz='p')] + C1[1:],
                          bars=1, time_sig=(3, 4), ottava=True),
                     dict(cap='b) el c. 2: tres negras sueltas, iguales · ninguna más larga que '
                              'las otras',
                          events=C2, bars=1, time_sig=(3, 4), ottava=True, show_time=False),
                     dict(cap='c) el mismo gesto sobre otras notas · andamio · para comprobar que '
                              'sabes soltar sin mirar las notas',
                          events=[n('G4', 'e'), n('A4', 'e'), st(n('B4')), st(n('B4')),
                                  st(n('B4')), st(n('B4')), st(n('B4'))],
                          bars=2, time_sig=(3, 4), show_time=False),
                 ]),
            dict(num=2, titulo='Los reguladores, cc. 3-4',
                 pista='cc. 3-4 · medidos sobre tu partitura · una blanca y una negra, dos veces, '
                       'con el sonido cerrando',
                 sistemas=[
                     dict(cap='a) Sol blanca y Mi negra, Mi blanca y Do negra · el regulador '
                              'cierra: cada nota un poco más suave que la anterior',
                          events=[dict(C3[0], dim=3), C3[1], C4[0], C4[1]],
                          bars=2, time_sig=(3, 4), ottava=True),
                 ]),
            dict(tipo='nota',
                 etiqueta='POR QUÉ EL STACCATO SE ESTUDIA DESPACIO',
                 texto='A velocidad lenta el silencio que queda detrás de cada nota se oye y se '
                       'puede medir. A velocidad de concierto ya no da tiempo a corregirlo. El '
                       'orden es: corto primero, rápido después, nunca al revés.'),
            dict(num=3, titulo='Cuatro compases de melodía, cc. 5-8',
                 pista='cc. 5-8 · medidos sobre tu partitura · bajan por escalones y cierran en '
                       'el Do',
                 sistemas=[
                     dict(cap='a) Re y Mi en corcheas, Fa, Fa; Fa, Mi, Re; Do y Re en corcheas, '
                              'Mi, Mi; y la blanca con la negra de cierre',
                          events=C5 + C6 + C7 + C8, bars=4, time_sig=(3, 4), ottava=True),
                 ]),
            dict(num=4, titulo='El acento de los cc. 11 y 12',
                 pista='cc. 11-12 · medidos sobre tu partitura · el acento va sobre la blanca, el '
                       'staccato sobre la negra siguiente',
                 sistemas=[
                     dict(cap='a) la blanca con acento y la negra suelta · el acento es un ataque '
                              'más marcado, no más largo',
                          events=C11 + C12, bars=2, time_sig=(3, 4), ottava=True),
                 ]),
            dict(num=5, titulo='Las dos notas pequeñas del c. 14',
                 pista='cc. 13-14 · medidos sobre tu partitura · las dos notas pequeñas no cuentan en '
                       'el compás: se tocan justo antes del Fa',
                 sistemas=[
                     dict(cap='a) dos notas de adorno que suben, Re y Mi, antes del Fa · se tocan '
                              'rápidas y ligeras, y la negra del Fa cae en el golpe',
                          events=C13 + C14, bars=2, time_sig=(3, 4), ottava=True),
                 ]),
            dict(num=6, titulo='El Trio, con tres bemoles',
                 pista='andamio en Mi bemol mayor · lo que cambia con la armadura nueva: Si, Mi y La '
                       'bemol, siempre',
                 sistemas=[
                     dict(cap='a) tres negras en el nuevo tono · el Mi y el Si ya van a la tecla '
                              'negra sin que el pentagrama lo repita',
                          events=[n('Bb4'), n('Ab4'), n('G4'), n('Eb4', 'h.')],
                          bars=2, time_sig=(3, 4), key_sig='Mib mayor'),
                     dict(cap='b) y una nota más arriba · andamio · el Si♭ y el La♭ no se '
                              'escriben delante de la nota: vienen en la armadura',
                          events=[n('Eb4'), n('G4'), n('Bb4'), n('G4', 'h.')],
                          bars=2, time_sig=(3, 4), key_sig='Mib mayor', show_time=False),
                 ]),
            dict(num=7, titulo='La vuelta: Scherzo D.C. al Fine',
                 pista='andamio · el camino que recorre la partitura entera, de arriba abajo',
                 sistemas=[
                     dict(cap='a) tres compases, con barra de repetición · se toca, se repite, y '
                              'después se vuelve al principio',
                          events=[n('E4'), n('F4'), n('G4'), n('G4', 'h.'), sil('q'), n('E4', 'h')],
                          bars=3, time_sig=(3, 4), repetir='cierra'),
                 ]),
        ] + bloques_extra('Do mayor', 15, 'C5', 'C3',
                          'el staccato corto y el salto de p a f',
                          desde=8, time_sig=(3, 4), mas=True) + [
            dict(num=10, titulo='Las dos manos del Primo, a la octava',
                 pista='andamio · en tu partitura las dos manos del Primo tocan lo mismo; aquí, '
                       'con las dos a la vez en un sistema de piano',
                 sistemas=[
                     dict(cap='a) dos corcheas y dos negras sueltas con las dos manos · si una '
                              'suelta antes que la otra, se oye enseguida',
                          events=[ac(('A3', 'A4'), 'e'), ac(('B3', 'B4'), 'e'),
                                  st(ac(('C4', 'C5'))), st(ac(('C4', 'C5')))],
                          bars=1, time_sig=(3, 4), manos='dobla'),
                 ]),
        ],
    ),

    trabajo=[
        dict(
            titulo='El trabajo de esta semana',
            esquina='Scherzo · para casa',
            intro='Quince minutos al día. Es una pieza larga, pero el Scherzo es el mismo cuatro '
                  'veces: se trabaja por trozos, no de golpe.',
            bloques=[
                plan((5, 'Los cc. 1-4 con la derecha, primero ligados y después con staccato'),
                     (5, 'Los cc. 5-8, solos y despacio'),
                     (5, 'El Secondo: el silencio y los dos acordes, contados en voz alta'),
                     (5, 'Los cc. 1-8 con el compañero, sin correr')),
                a_cuatro_manos('El Secondo toca en el segundo y el tercer golpe, así que si tú '
                               'alargas las negras, os pisáis. Acordad quién da la entrada, a qué '
                               'velocidad y quién marca el p y el f del c. 9.'),
                escalera((60, 'los cc. 1-4, con staccato'),
                         (72, 'los cc. 1-8, solos'),
                         (84, 'los cc. 1-8 con el compañero'),
                         (96, 'el Scherzo entero, hasta el c. 32'),
                         meta='La partitura pone "Allegro" pero no trae número: la meta la eliges '
                              'tú y la apuntas a lápiz.',
                         titulo='La escalera del metrónomo'),
                diferencias(C1 + C2,
                            [n('E5', 'e'), n('F5', 'e'), st(n('G5')), st(n('G5')),
                             st(n('G5')), st(n('F5')), st(n('G5'))],
                            cuantas=1,
                            titulo='Busca la diferencia en la melodía',
                            pista='el de arriba son tus cc. 1 y 2 · el de abajo ha cambiado una nota'),
                nombres(['G5', 'E5', 'F5', 'D5', 'C5'],
                        titulo='¿Cómo se llama cada nota?',
                        pista='son las notas de los cc. 1-8 tal como están escritas, con el 8va '
                              'encima'),
                para_clase('Los cc. 1-8 con el staccato corto, y cuántas veces seguidas te ha '
                           'salido. Y una pregunta para hacer entre los dos: ¿en qué compás '
                           'empieza el Trio y qué cambia al llegar ahí?'),
            ],
        ),
    ],
)

if __name__ == '__main__':
    print('generado', construir(CANCION))
